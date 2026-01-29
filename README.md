# 🔐 Password Cracking Dashboard
## Educational Cybersecurity Simulation Platform

### Project Overview

The **Password Cracking Dashboard** is a faculty-ready educational platform that demonstrates the complete lifecycle of password-based attacks, defenses, and security analytics in a controlled, ethical environment.

**All attacks are simulated for cybersecurity awareness and learning — no real credentials or systems are involved.**

---

## 📋 Table of Contents

1. [Quick Start](#quick-start)
2. [System Architecture](#system-architecture)
3. [Features](#features)
4. [Project Structure](#project-structure)
5. [Attack Simulations](#attack-simulations)
6. [Defense Mechanisms](#defense-mechanisms)
7. [Dashboard & Analytics](#dashboard--analytics)
8. [Educational Outcomes](#educational-outcomes)
9. [Safety & Ethics](#safety--ethics)

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. **Navigate to project directory:**
```bash
cd "d:\cyber attacks"
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the application:**
```bash
python app.py
```

4. **Open in browser:**
```
http://127.0.0.1:5000
```

### Demo Credentials
- **Username:** `demo`
- **Password:** `DemoPassword123!`

---

## 🏗️ System Architecture

### Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| Backend | Flask (Python) | Application logic, routing, API endpoints |
| Database | SQLite | User accounts, logs, attack records |
| Frontend | HTML/CSS/JavaScript | User interface, real-time updates |
| Visualization | Chart.js | Dashboard charts and analytics |

### System Flow

```
┌─────────────────────┐
│  User / Attacker    │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│  Login / Phishing   │
│     Page            │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│  Attack Simulation  │
│     Engine          │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│  Detection & Defense│
│     Layer           │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│  Logging System     │
│  (SQLite)           │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│  Security Dashboard │
│  (Charts & Metrics) │
└─────────────────────┘
```

---

## ✨ Features

### 1. **Secure Login System**
- Secure password hashing (Werkzeug)
- Real-time password strength meter
- Estimated crack time calculation
- Login attempt logging

### 2. **Attack Simulations**
- **Brute-Force Attack:** Try passwords from wordlist systematically
- **Dictionary Attack:** Use common password lists
- **Phishing Attack:** Capture credentials via fake login page
- **Credential Stuffing:** Try same password across multiple accounts

### 3. **Defense Mechanisms**
- **Rate Limiting:** Limit login attempts per timeframe
- **Account Lockout:** Lock account after N failed attempts
- **MFA Simulation:** Multi-factor authentication toggle
- **Defense Toggle Control:** Enable/disable defenses to see impact

### 4. **Real-Time Dashboard**
- Attack distribution charts
- Success rate visualization
- Defense effectiveness metrics
- Live attempt counter

### 5. **Forensics & Incident Analysis**
- Complete audit logs with timestamps
- Attack timeline visualization
- Defense trigger analysis
- Incident recommendations

---

## 📁 Project Structure

```
d:\cyber attacks\
├── app.py                  # Main Flask application
├── database.py             # SQLite database setup & functions
├── password_strength.py    # Password strength calculator
├── attack_engine.py        # Attack simulation logic
├── requirements.txt        # Python dependencies
├── security_system.db      # SQLite database (created on first run)
│
├── templates/              # HTML templates
│   ├── base.html          # Base template with navbar/footer
│   ├── index.html         # Home page
│   ├── login.html         # Secure login page
│   ├── phishing.html      # Phishing demo page
│   ├── dashboard.html     # Security dashboard
│   └── forensics.html     # Forensics view
│
└── static/                # Static assets
    ├── style.css          # Stylesheet
    └── main.js            # JavaScript utilities
```

---

## 🎯 Attack Simulations

### 1. Brute-Force Attack
**What it does:**
- Attempts common passwords against the demo account
- Shows password cracking progression
- Blocked by rate limiting if defense is enabled

**Real-World Context:**
- Attackers use GPU/cloud computing for speed
- Weak passwords fall in minutes/hours
- Defense: Strong passwords + rate limiting

**API Endpoint:**
```
POST /api/attack/brute-force
Body: { "target": "demo" }
```

### 2. Dictionary Attack
**What it does:**
- Uses predefined wordlist of common passwords
- More efficient than brute force
- Blocked immediately if rate limiting enabled

**Real-World Context:**
- Common passwords account for ~30% of breaches
- Often sourced from previous breaches
- Defense: Prevent common passwords

**API Endpoint:**
```
POST /api/attack/dictionary
Body: { "target": "demo" }
```

### 3. Phishing Attack
**What it does:**
- Fake login page captures credentials
- User is redirected after capture
- Credentials logged as "phishing" attack

**Real-World Context:**
- #1 vector for credential theft
- Bypasses technical security
- Defense: User awareness + email filtering

**Demo Page:** `/phishing-demo`

### 4. Credential Stuffing
**What it does:**
- Try captured password across multiple accounts
- Simulates account enumeration
- Blocked by rate limiting

**Real-World Context:**
- Uses credentials from past breaches
- Automated, high-volume attacks
- Defense: Monitor for patterns

**API Endpoint:**
```
POST /api/attack/dictionary
Body: { "target": "demo" }
```

---

## 🛡️ Defense Mechanisms

### Rate Limiting
**Implementation:**
- Maximum 5 login attempts allowed
- Resets after successful login or lockout
- Prevents brute-force attacks

**Toggle:** Via dashboard control panel

**Real-World Use:**
- Enterprise systems typically: 3-5 attempts → lockout
- Delays between attempts (exponential backoff)

### Account Lockout
**Implementation:**
- Account locks after failed attempts
- Temporary lockout (simulated)
- Prevents rapid-fire attacks

**Toggle:** Via dashboard control panel

**Real-World Use:**
- 30 min - 24 hour lockout periods
- Admin unlock / self-service unlock

### MFA (Multi-Factor Authentication)
**Implementation:**
- Toggle to simulate MFA requirement
- Additional verification step
- Blocks phishing effectiveness

**Toggle:** Via dashboard control panel

**Real-World Use:**
- 2FA/TOTP/SMS/Hardware keys
- ~99% effective against phishing

### Password Requirements
**Implemented:**
- Minimum 8 characters
- Complexity scoring (upper, lower, numbers, symbols)
- Common password blocking
- Crack time estimation

**Real-World Use:**
- NIST recommends: 8+ chars, no composition rules
- Focus on length over complexity

---

## 📊 Dashboard & Analytics

### Real-Time Metrics

**Displayed on Dashboard:**
- Total login attempts
- Successful logins
- Failed attempts
- Success rate percentage

### Charts & Visualization

1. **Attack Distribution** (Doughnut Chart)
   - Shows breakdown of attack types
   - Visual comparison of threat vectors

2. **Login Success Rate** (Pie Chart)
   - Successful vs. failed attempts
   - Defense effectiveness indicator

3. **Attack Timeline** (Line Chart)
   - Attacks over time
   - Trend analysis

4. **Defense Triggers** (Bar Chart)
   - How often each defense activated
   - Defense effectiveness

### Forensics View

**Complete Audit Trail:**
- Timestamp of each event
- Username targeted
- Password attempted
- Result (success/failure)
- Attack classification
- Defense response

**Timeline Visualization:**
- Color-coded by attack type
- Attack chain analysis
- Pattern identification

**Recommendations:**
- Password policy suggestions
- Defense implementation advice
- User training recommendations
- Monitoring strategy

---

## 🎓 Educational Outcomes

### Students Learn:

#### 1. **Authentication Security** 🔐
- How passwords are hashed and stored
- Why weak passwords fail
- Salt and hashing importance
- Attack surface analysis

#### 2. **Attack Methodology** 🎯
- How attackers enumerate targets
- Password attack vectors
- Social engineering techniques
- Attack cost-benefit analysis

#### 3. **Defense Strategy** 🛡️
- Layered security (defense in depth)
- Detection vs. prevention
- Cost of security controls
- Risk vs. usability tradeoffs

#### 4. **Security Analytics** 📊
- Log analysis and interpretation
- Incident pattern recognition
- Threat assessment
- Metrics-driven decision making

---

## Routes & Endpoints

### Frontend Routes

| Route | Purpose |
|-------|---------|
| `/` | Home page |
| `/login` | Login form |
| `/logout` | Logout |
| `/dashboard` | Main security dashboard |
| `/forensics` | Forensics & incident analysis |
| `/phishing-demo` | Phishing demonstration |

### API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/password-strength` | POST | Check password strength |
| `/api/attack/brute-force` | POST | Simulate brute-force |
| `/api/attack/dictionary` | POST | Simulate dictionary attack |
| `/api/attack/phishing` | POST | Simulate phishing |
| `/api/defense/toggle` | POST | Toggle defense |
| `/api/stats` | GET | Get dashboard stats |

---

## 🔒 Safety & Ethics

### What This Project IS:
✅ **Fully local** - No internet connectivity required
✅ **Non-destructive** - No files or systems modified
✅ **Simulated** - No real password cracking occurs
✅ **Educational** - Designed for learning
✅ **Transparent** - Clear disclaimers throughout
✅ **Safe** - No external system access

### What This Project IS NOT:
❌ Real hacking tool
❌ Illegal password cracking
❌ External system attacks
❌ Real credential theft
❌ Production security system
❌ Real user data exposure

### Ethical Usage
- Use only for educational purposes
- In classroom or controlled lab environment
- With proper institutional approval
- Clear disclaimers to all users
- No unauthorized access attempts
- No real system targeting

### Legal Compliance
- Complies with CFAA (Computer Fraud and Abuse Act)
- Authorized use only
- Educational fair use
- No unauthorized access
- Local, isolated environment

---

## 📚 Faculty Implementation

### In the Classroom

1. **Lecture Setup (30 min)**
   - Explain attack vectors
   - Discuss real-world breaches
   - Review password statistics

2. **Live Demo (20 min)**
   - Run brute-force attack
   - Show defense blocking
   - Review logs and analytics

3. **Student Lab (60 min)**
   - Students toggle defenses
   - Run attack simulations
   - Analyze results
   - Write incident report

### Lab Exercises

**Exercise 1: Password Strength**
- Create weak vs. strong passwords
- Observe crack time differences
- Understand character sets

**Exercise 2: Attack Simulation**
- Run each attack type
- Observe attack progression
- Compare against defenses

**Exercise 3: Defense Evaluation**
- Toggle each defense mechanism
- Measure effectiveness
- Recommend optimal settings

**Exercise 4: Forensics Analysis**
- Analyze attack logs
- Identify attack patterns
- Write security recommendations

---

## 🔧 Customization

### Adding New Passwords to Wordlist

Edit `attack_engine.py`:
```python
self.wordlist = [
    'password', '123456', '12345678', 'qwerty', 'abc123', 'monkey',
    'DemoPassword123!', 'letmein', 'trustno1', 'dragon', 'password123',
    # Add more passwords here
]
```

### Adding New Users

Edit `database.py` after `init_db()`:
```python
c.execute('''INSERT INTO users (username, email, password_hash)
             VALUES (?, ?, ?)''',
         ('newuser', 'user@example.com', generate_password_hash('password')))
```

### Adjusting Defense Parameters

Edit `attack_engine.py`:
```python
self.max_attempts = 5  # Change attempt limit
```

---

## 🐛 Troubleshooting

### Database Errors
- **Problem:** "database.db is locked"
- **Solution:** Restart Flask app or delete `security_system.db` to reset

### Port Already in Use
- **Problem:** "Address already in use on 127.0.0.1:5000"
- **Solution:** Change port in `app.py`: `app.run(port=5001)`

### Charts Not Displaying
- **Problem:** Charts appear empty
- **Solution:** Ensure Chart.js CDN loads - check browser console

### Login Not Working
- **Problem:** Demo credentials don't work
- **Solution:** Check database exists - may need to delete `security_system.db` and restart

---

## 📞 Support & Questions

### Recommended Reading
- OWASP Password Security Guidelines
- NIST Digital Identity Guidelines
- "Cracking Codes with Python" - Al Sweigart
- Real-world breach case studies

### Further Learning
- OWASP Top 10
- Cybersecurity certifications (Security+, OSCP)
- Penetration testing courses
- Bug bounty platforms (HackTheBox)

---

## 📄 License & Disclaimer

**Educational Use Only**

This project is provided for educational and authorized testing purposes only. Users are responsible for ensuring they comply with all applicable laws and regulations, including:

- Computer Fraud and Abuse Act (CFAA)
- Local cybersecurity laws
- Institutional policies
- Ethical guidelines

**The creators are not responsible for misuse or unauthorized access attempts.**

---

## 🎯 One-Line Summary

> *"A controlled, ethical cybersecurity simulation demonstrating how password attacks occur, how defenses stop them, and how security teams analyze incidents — with real-time dashboards and forensics analysis."*

---

**Created:** January 2026  
**Purpose:** Faculty-ready cybersecurity education  
**Status:** Production-ready for classroom use  
**Disclaimer:** All attacks simulated | No real credentials | Educational use only

🔐 **Secure Learning Starts Here** 🔐
"# cyber-attacks" 
