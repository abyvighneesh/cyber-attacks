from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
import json
from datetime import datetime, timedelta

from database import init_db, get_db, log_login_attempt, get_login_logs, get_attack_stats
from password_strength import calculate_strength
from attack_engine import AttackSimulation

app = Flask(__name__)
app.secret_key = 'demo-secret-key-cybersecurity-2026'

# Global state for defense toggle
DEFENSE_STATE = {
    'mfa_enabled': True,
    'rate_limiting_enabled': True,
    'account_lockout_enabled': True
}

# Initialize database on first run
try:
    init_db()
except:
    pass

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if not username or not password:
            return render_template('login.html', error='Username and password required')
        
        conn = get_db()
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = c.fetchone()
        conn.close()
        
        if user and check_password_hash(user['password_hash'], password):
            session['user_id'] = user['id']
            session['username'] = user['username']
            log_login_attempt(username, password, True, attack_type='legitimate')
            return redirect(url_for('dashboard'))
        else:
            log_login_attempt(username, password, False, attack_type='failed_login')
            return render_template('login.html', error='Invalid credentials')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    """Logout"""
    session.clear()
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    """Security dashboard"""
    if 'username' not in session:
        return redirect(url_for('login'))
    
    logs = get_login_logs(50)
    stats = get_attack_stats()
    
    return render_template('dashboard.html', 
                          logs=logs, 
                          stats=stats,
                          defense_state=DEFENSE_STATE)

@app.route('/api/password-strength', methods=['POST'])
def password_strength_api():
    """Check password strength"""
    try:
        data = request.get_json()
        if not data or 'password' not in data:
            return jsonify({'error': 'Missing password field'}), 400
        
        password = data.get('password', '')
        strength = calculate_strength(password)
        return jsonify(strength)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/attack/brute-force', methods=['POST'])
def attack_brute_force():
    """Simulate brute-force attack"""
    data = request.get_json()
    target_username = data.get('target', 'demo')
    
    defense_enabled = DEFENSE_STATE['rate_limiting_enabled']
    attack = AttackSimulation(defense_enabled=defense_enabled)
    results = attack.brute_force_attack(target_username)
    
    return jsonify({
        'success': results.get('successful', False),
        'attempts': results.get('total_attempts', 0),
        'blocked': results.get('blocked', False),
        'password_found': results.get('password_found'),
        'defense_enabled': defense_enabled
    })

@app.route('/api/attack/phishing', methods=['POST'])
def attack_phishing():
    """Simulate phishing attack"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid JSON'}), 400
        
        username = data.get('username', '')
        email = data.get('email', '')
        password = data.get('password', '')
        
        attack = AttackSimulation()
        results = attack.phishing_attack(username, email, password)
        
        return jsonify({
            'credentials_captured': True,
            'message': 'Credentials logged for analysis'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/attack/dictionary', methods=['POST'])
def attack_dictionary():
    """Simulate dictionary attack"""
    try:
        data = request.get_json()
        if not data or 'target' not in data:
            return jsonify({'error': 'Missing target field'}), 400
        
        target_username = data.get('target', 'demo')
        defense_enabled = DEFENSE_STATE['rate_limiting_enabled']
        attack = AttackSimulation(defense_enabled=defense_enabled)
        results = attack.dictionary_attack(target_username)
        
        return jsonify({
            'attempted': results['attempted'],
            'blocked': results['defense_blocked'],
            'defense_enabled': defense_enabled
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/defense/toggle', methods=['POST'])
def toggle_defense():
    """Toggle defense mechanisms"""
    try:
        data = request.get_json()
        if not data or 'type' not in data or 'enabled' not in data:
            return jsonify({'error': 'Missing type or enabled field'}), 400
        
        defense_type = data.get('type')
        enabled = data.get('enabled')
        
        if defense_type == 'mfa':
            DEFENSE_STATE['mfa_enabled'] = enabled
        elif defense_type == 'rate_limiting':
            DEFENSE_STATE['rate_limiting_enabled'] = enabled
        elif defense_type == 'account_lockout':
            DEFENSE_STATE['account_lockout_enabled'] = enabled
        else:
            return jsonify({'error': f'Unknown defense type: {defense_type}'}), 400
        
        return jsonify({'status': 'success', 'defense_state': DEFENSE_STATE})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get current security statistics"""
    try:
        stats = get_attack_stats()
        logs = get_login_logs(100)
        
        # Calculate metrics
        total_attempts = len(logs)
        successful = sum(1 for log in logs if log['success'])
        failed = total_attempts - successful
        
        # Attack distribution
        attack_types = {}
        for log in logs:
            attack_type = log['attack_type'] or 'unknown'
            attack_types[attack_type] = attack_types.get(attack_type, 0) + 1
        
        # Defense triggers
        defense_triggers = {}
        for log in logs:
            if log['defense_triggered']:
                defense_triggers[log['defense_triggered']] = defense_triggers.get(log['defense_triggered'], 0) + 1
        
        return jsonify({
            'total_attempts': total_attempts,
            'successful_logins': successful,
            'failed_attempts': failed,
            'success_rate': f"{(successful/total_attempts*100):.1f}%" if total_attempts > 0 else "0%",
            'attack_types': attack_types,
            'defense_triggers': defense_triggers,
            'phishing_captures': stats.get('phishing_count', 0)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/phishing-demo')
def phishing_demo():
    """Phishing page (looks like login but captures creds)"""
    return render_template('phishing.html')

@app.route('/api/phishing-submit', methods=['POST'])
def phishing_submit():
    """Handle phishing form submission"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid JSON'}), 400
        
        attack = AttackSimulation()
        attack.phishing_attack(
            data.get('username', ''),
            data.get('email', ''),
            data.get('password', '')
        )
        
        # Redirect to real login after capture
        return jsonify({'redirectTo': url_for('login')})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/forensics')
def forensics():
    """Forensics view for security team"""
    logs = get_login_logs(500)
    stats = get_attack_stats()
    
    return render_template('forensics.html', logs=logs, stats=stats)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
