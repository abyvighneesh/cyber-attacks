import sqlite3
import os
from datetime import datetime
from werkzeug.security import generate_password_hash

DB_PATH = 'security_system.db'

def init_db():
    """Initialize database with schema"""
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    # Users table
    c.execute('''CREATE TABLE users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  username TEXT UNIQUE NOT NULL,
                  email TEXT UNIQUE NOT NULL,
                  password_hash TEXT NOT NULL,
                  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    
    # Login attempts table (for logging)
    c.execute('''CREATE TABLE login_attempts
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  username TEXT NOT NULL,
                  password_entered TEXT NOT NULL,
                  success BOOLEAN NOT NULL,
                  attack_type TEXT,
                  ip_address TEXT DEFAULT '127.0.0.1',
                  defense_triggered TEXT,
                  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    
    # Attack logs table
    c.execute('''CREATE TABLE attack_logs
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  attack_type TEXT NOT NULL,
                  target_username TEXT,
                  attack_count INTEGER,
                  success_count INTEGER,
                  blocked_count INTEGER,
                  defense_enabled BOOLEAN,
                  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    
    # Phishing captures table
    c.execute('''CREATE TABLE phishing_captures
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  username TEXT,
                  email TEXT,
                  password_captured TEXT,
                  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    
    # Insert demo user
    demo_password = generate_password_hash('DemoPassword123!')
    c.execute('''INSERT INTO users (username, email, password_hash)
                 VALUES (?, ?, ?)''',
             ('demo', 'demo@example.com', demo_password))
    
    conn.commit()
    conn.close()

def get_db():
    """Get database connection"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def log_login_attempt(username, password, success, attack_type=None, defense_triggered=None):
    """Log a login attempt"""
    conn = get_db()
    c = conn.cursor()
    c.execute('''INSERT INTO login_attempts 
                 (username, password_entered, success, attack_type, defense_triggered)
                 VALUES (?, ?, ?, ?, ?)''',
             (username, password, success, attack_type, defense_triggered))
    conn.commit()
    conn.close()

def log_attack(attack_type, target_username, attack_count, success_count, blocked_count, defense_enabled):
    """Log attack statistics"""
    conn = get_db()
    c = conn.cursor()
    c.execute('''INSERT INTO attack_logs 
                 (attack_type, target_username, attack_count, success_count, blocked_count, defense_enabled)
                 VALUES (?, ?, ?, ?, ?, ?)''',
             (attack_type, target_username, attack_count, success_count, blocked_count, defense_enabled))
    conn.commit()
    conn.close()

def log_phishing(username, email, password):
    """Log phishing capture"""
    conn = get_db()
    c = conn.cursor()
    c.execute('''INSERT INTO phishing_captures (username, email, password)
                 VALUES (?, ?, ?)''', (username, email, password))
    conn.commit()
    conn.close()

def get_login_logs(limit=100):
    """Retrieve login attempt logs"""
    conn = get_db()
    c = conn.cursor()
    c.execute('''SELECT * FROM login_attempts ORDER BY timestamp DESC LIMIT ?''', (limit,))
    logs = c.fetchall()
    conn.close()
    return logs

def get_attack_stats():
    """Get attack statistics for dashboard"""
    conn = get_db()
    c = conn.cursor()
    
    # Attacks by type
    c.execute('''SELECT attack_type, COUNT(*) as count FROM attack_logs GROUP BY attack_type''')
    attack_types = c.fetchall()
    
    # Success rate
    c.execute('''SELECT success, COUNT(*) as count FROM login_attempts GROUP BY success''')
    success_data = c.fetchall()
    
    # Phishing captures
    c.execute('''SELECT COUNT(*) as count FROM phishing_captures''')
    phishing_count = c.fetchone()['count']
    
    conn.close()
    
    return {
        'attack_types': dict(attack_types) if attack_types else {},
        'success_data': dict(success_data) if success_data else {},
        'phishing_count': phishing_count
    }
