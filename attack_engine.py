import time
from werkzeug.security import check_password_hash
from database import get_db, log_login_attempt, log_attack

class AttackSimulation:
    """Simulate various password attacks"""
    
    def __init__(self, defense_enabled=True):
        self.defense_enabled = defense_enabled
        self.max_attempts = 5 if defense_enabled else 100
        self.attempt_count = 0
        self.success_count = 0
        self.blocked_count = 0
        self.wordlist = [
            'password', '123456', '12345678', 'qwerty', 'abc123', 'monkey',
            'DemoPassword123!', 'letmein', 'trustno1', 'dragon', 'password123'
        ]
    
    def brute_force_attack(self, username, target_password=None):
        """
        Simulate brute-force attack on a demo account
        """
        results = {
            'total_attempts': 0,
            'successful': False,
            'password_found': None,
            'blocked': False,
            'attempts_before_block': 0
        }
        
        conn = get_db()
        c = conn.cursor()
        
        # Get the user from database
        c.execute('SELECT password_hash FROM users WHERE username = ?', (username,))
        user = c.fetchone()
        conn.close()
        
        if not user:
            return results
        
        password_hash = user['password_hash']
        
        # Simulate attack
        for attempt_num, password in enumerate(self.wordlist, 1):
            results['total_attempts'] = attempt_num
            self.attempt_count += 1
            
            # Simulate defense: rate limiting
            if self.defense_enabled and self.attempt_count > self.max_attempts:
                results['blocked'] = True
                results['attempts_before_block'] = self.max_attempts
                self.blocked_count += 1
                log_login_attempt(
                    username, password, False, 
                    attack_type='brute_force',
                    defense_triggered='RATE_LIMIT_BLOCK'
                )
                break
            
            # Check password
            if check_password_hash(password_hash, password):
                results['successful'] = True
                results['password_found'] = password
                self.success_count += 1
                log_login_attempt(
                    username, password, True,
                    attack_type='brute_force',
                    defense_triggered=None
                )
                break
            else:
                log_login_attempt(
                    username, password, False,
                    attack_type='brute_force',
                    defense_triggered=None
                )
            
            # Simulate delay between attempts
            time.sleep(0.2)
        
        # Log attack statistics
        log_attack(
            'Brute Force',
            username,
            self.attempt_count,
            self.success_count,
            self.blocked_count,
            self.defense_enabled
        )
        
        return results
    
    def phishing_attack(self, username, email, password):
        """
        Simulate phishing attack - capture credentials
        """
        from database import log_phishing
        
        results = {
            'credentials_captured': True,
            'username': username,
            'email': email,
            'password': password
        }
        
        # Log the phishing capture
        log_phishing(username, email, password)
        
        # Log as phishing attack
        log_login_attempt(
            username, password, False,
            attack_type='phishing',
            defense_triggered='MFA_BYPASS' if self.defense_enabled else None
        )
        
        log_attack(
            'Phishing',
            username,
            1,
            1,
            0 if not self.defense_enabled else 1,
            self.defense_enabled
        )
        
        return results
    
    def dictionary_attack(self, username, common_passwords_only=True):
        """
        Simplified dictionary attack simulation
        """
        results = {
            'attempted': len(self.wordlist),
            'successful': False,
            'defense_blocked': False
        }
        
        if self.defense_enabled:
            results['defense_blocked'] = True
            self.blocked_count += 1
        
        log_attack(
            'Dictionary Attack',
            username,
            len(self.wordlist),
            1 if results['successful'] else 0,
            self.blocked_count,
            self.defense_enabled
        )
        
        return results
    
    def credential_stuffing(self, username_list, password_to_try):
        """
        Simulate credential stuffing (trying same password across multiple accounts)
        """
        results = {
            'attempted_count': len(username_list),
            'successful_count': 0,
            'blocked': self.defense_enabled
        }
        
        if self.defense_enabled:
            results['blocked'] = True
            self.blocked_count += len(username_list)
        
        log_attack(
            'Credential Stuffing',
            'multiple',
            len(username_list),
            results['successful_count'],
            self.blocked_count if self.defense_enabled else 0,
            self.defense_enabled
        )
        
        return results
    
    def reset_counters(self):
        """Reset attack counters"""
        self.attempt_count = 0
        self.success_count = 0
        self.blocked_count = 0
