import re

COMMON_PASSWORDS = {
    'password', '123456', '12345678', 'qwerty', 'abc123', 'monkey', '1234567', 
    'letmein', 'trustno1', 'dragon', 'baseball', 'iloveyou', 'sunshine', 'princess',
    'admin', 'welcome', 'login', 'passw0rd', 'pass', 'test', 'guest'
}

def calculate_strength(password):
    """
    Calculate password strength and return score (0-100) and level
    """
    score = 0
    
    # Length scoring
    if len(password) >= 8:
        score += 20
    elif len(password) >= 6:
        score += 10
    
    if len(password) >= 12:
        score += 15
    
    # Complexity scoring
    if re.search(r'[a-z]', password):
        score += 10
    if re.search(r'[A-Z]', password):
        score += 15
    if re.search(r'[0-9]', password):
        score += 15
    if re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'"<>,.?/\\|]', password):
        score += 20
    
    # Penalize common patterns
    if password.lower() in COMMON_PASSWORDS:
        score = max(0, score - 40)
    
    # Check for sequential characters
    if has_sequential_chars(password):
        score = max(0, score - 10)
    
    score = min(100, score)
    
    # Determine strength level
    if score >= 70:
        strength = 'Strong'
        color = '#28a745'
    elif score >= 50:
        strength = 'Medium'
        color = '#ffc107'
    else:
        strength = 'Weak'
        color = '#dc3545'
    
    # Estimate crack time
    crack_time = estimate_crack_time(password, score)
    
    return {
        'score': score,
        'strength': strength,
        'color': color,
        'crack_time': crack_time,
        'feedback': get_feedback(password, score)
    }

def has_sequential_chars(password):
    """Check for sequential characters like 'abc' or '123'"""
    for i in range(len(password) - 2):
        if ord(password[i+1]) - ord(password[i]) == 1 and \
           ord(password[i+2]) - ord(password[i+1]) == 1:
            return True
    return False

def estimate_crack_time(password, score):
    """Estimate time to crack based on password strength"""
    password_space = 26  # lowercase
    if re.search(r'[A-Z]', password):
        password_space += 26
    if re.search(r'[0-9]', password):
        password_space += 10
    if re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'"<>,.?/\\|]', password):
        password_space += 32
    
    total_combinations = password_space ** len(password)
    guesses_per_second = 1_000_000_000  # 1B guesses/sec (modern GPU)
    seconds_needed = total_combinations / (2 * guesses_per_second)
    
    if seconds_needed < 1:
        return "< 1 second"
    elif seconds_needed < 60:
        return f"{int(seconds_needed)} seconds"
    elif seconds_needed < 3600:
        return f"{int(seconds_needed / 60)} minutes"
    elif seconds_needed < 86400:
        return f"{int(seconds_needed / 3600)} hours"
    elif seconds_needed < 2592000:
        return f"{int(seconds_needed / 86400)} days"
    elif seconds_needed < 31536000:
        return f"{int(seconds_needed / 2592000)} months"
    else:
        return f"{int(seconds_needed / 31536000)} years"

def get_feedback(password, score):
    """Provide improvement feedback"""
    feedback = []
    
    if len(password) < 8:
        feedback.append("Use at least 8 characters")
    if len(password) < 12:
        feedback.append("12+ characters is ideal")
    
    if not re.search(r'[A-Z]', password):
        feedback.append("Add uppercase letters")
    if not re.search(r'[0-9]', password):
        feedback.append("Add numbers")
    if not re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'"<>,.?/\\|]', password):
        feedback.append("Add special characters")
    
    if password.lower() in COMMON_PASSWORDS:
        feedback.append("This password is too common")
    
    return feedback if feedback else ["Strong password!"]
