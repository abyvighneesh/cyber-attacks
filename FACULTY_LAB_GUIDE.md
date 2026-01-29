# 🔐 Password Cracking Dashboard - Faculty Lab Guide

## Complete Lesson Plan & Lab Exercises

---

## PART 1: LECTURE (45 minutes)

### Introduction (10 min)

**Opening Statement:**
> "Passwords are the weakest link in cybersecurity. We're going to explore why, how attackers target them, how defenses protect systems, and what modern security teams see when attacks happen."

**Key Points to Cover:**
- Passwords are still the #1 authentication method
- 81% of breaches involve weak/stolen passwords (Verizon DBIR)
- Users reuse passwords across sites
- Phishing bypasses technical security (human element)
- Layered defenses reduce breach probability

### The Attack Lifecycle (15 min)

**Explain This Flow:**

```
RECONNAISSANCE
    ↓ (Attacker gathers info)
TARGETING
    ↓ (Selects password attack method)
ATTACK EXECUTION
    ↓ (Brute force / Phishing / Dictionary)
DEFENSE DETECTION
    ↓ (System detects and responds)
LOGGING & ANALYSIS
    ↓ (Security team investigates)
INCIDENT RESPONSE
    ↓ (Mitigation and lessons learned)
```

**Attack Vectors to Discuss:**

1. **Brute Force**
   - Random password attempts
   - Speed: Modern GPU = 1B guesses/sec
   - Weakness: Gets caught quickly
   - Example: 8-char password = 62^8 = 218 trillion possibilities

2. **Dictionary Attack**
   - Uses wordlists from past breaches
   - Speed: Thousands to millions of guesses/sec
   - Weakness: Only works on weak passwords
   - Example: 90% of passwords in top 1000 common passwords

3. **Phishing**
   - Fake login page captures credentials
   - Speed: Immediate if user falls for it
   - Weakness: Bypasses technical defenses
   - Reality: 3.4B phishing emails sent daily (Microsoft)

4. **Credential Stuffing**
   - Compromised email:password pairs
   - Targets password reuse
   - Speed: Millions of attempts
   - Reality: People reuse passwords across 4+ sites avg.

### Defense Mechanisms (15 min)

**Layered Defense Approach:**

```
┌─────────────────────────────────────┐
│ 1. POLICY LAYER                      │
│    • Strong password requirements     │
│    • Regular expiration               │
│    • No common passwords              │
└─────────────────────────────────────┘
         ↓
┌─────────────────────────────────────┐
│ 2. TECHNICAL LAYER                   │
│    • Password hashing (bcrypt)        │
│    • Salting (random per password)    │
│    • Rate limiting (5 attempts)       │
│    • Account lockout (30 min)         │
└─────────────────────────────────────┘
         ↓
┌─────────────────────────────────────┐
│ 3. AUTHENTICATION LAYER              │
│    • MFA / 2FA (SMS, TOTP, Key)       │
│    • Passwordless (biometric, keys)   │
│    • Context-aware (location, device) │
└─────────────────────────────────────┘
         ↓
┌─────────────────────────────────────┐
│ 4. DETECTION LAYER                   │
│    • Log all attempts                 │
│    • Alert on anomalies               │
│    • Analyze patterns                 │
│    • Forensic investigation           │
└─────────────────────────────────────┘
```

**Defense Statistics:**
- MFA blocks 99% of phishing
- Rate limiting reduces success by 90%
- Strong passwords + MFA = nearly impenetrable

### Real-World Examples (5 min)

**Show These Breaches:**
1. **LinkedIn (2012)** - 6.5M passwords stolen, weak hashing
2. **Yahoo (2014)** - 3B accounts affected, phishing used
3. **Twitch (2021)** - 4.7M accounts, cookie theft
4. **Okta (2023)** - Supply chain attack, credential theft

**Key Takeaway:** "These all could have been prevented or detected with the defenses we're demonstrating today."

---

## PART 2: LIVE DEMONSTRATION (30 minutes)

### Setup & Access (5 min)

**Show Students:**
```bash
cd d:\cyber attacks
python app.py
# Application running at http://127.0.0.1:5000
```

**Browser Open to:** `http://127.0.0.1:5000`

**Walkthrough Pages:**
- Home page overview
- Explain the flow diagram
- Show featured content

### Demo 1: Login & Password Strength (8 min)

**Step 1: Visit Login Page**
- Navigate to `/login`
- Show the login form
- Highlight: "Real-time password strength meter"

**Step 2: Test Weak Passwords**
- Type: `123456`
- Show: Red bar, "WEAK", "< 1 second crack time"
- Explain: This password fails instantly
- Type: `password123`
- Show: Yellow bar, "MEDIUM", "45 minutes"
- Explain: Common passwords are known

**Step 3: Test Strong Password**
- Type: `DemoPassword123!`
- Show: Green bar, "STRONG", "847 years"
- Explain: Complexity, length, character variety

**Key Teaching Point:**
> "This is what users should do before hitting submit. Real systems should enforce this."

### Demo 2: Login with Demo Account (5 min)

**Login Successfully:**
- Username: `demo`
- Password: `DemoPassword123!`
- Show: Dashboard appears
- Explain: "This is what security teams monitor"

### Demo 3: View the Dashboard (7 min)

**Show Dashboard Elements:**

1. **Defense Controls**
   - Show Rate Limiting toggle: **ON**
   - Show MFA toggle: **ON**
   - Explain: "We can toggle defenses to see impact"

2. **Statistics Cards**
   - Total Attempts: (shows 0 initially)
   - Successful Logins: 1
   - Failed Attempts: 0
   - Success Rate: 100%

3. **Charts**
   - Attack Distribution: Empty (no attacks yet)
   - Success Rate: 100% green
   - Timeline: Not enough data
   - Defense Triggers: None yet

**Key Teaching Point:**
> "This is a SOC (Security Operations Center) dashboard. In real organizations, this runs 24/7."

### Demo 4: Run Brute-Force Attack (5 min)

**Scroll to Attack Simulations**

**Click: "Start Brute Force Attack"**
- Show progress: "⏳ Running brute-force attack..."
- Results appear:
  ```
  Attempts: 5
  Successful: ✗ NO
  Blocked: ✓ YES
  Defense: 🛡️ Enabled
  ```

**Explain What Happened:**
- Attack tried 5 passwords from wordlist
- Attack was blocked by rate limiting
- Defense worked!

**Toggle Defense OFF and Run Again:**
- Click "Rate Limiting" toggle: **OFF**
- Run brute-force attack
- Results:
  ```
  Attempts: 11 (more attempts)
  Successful: ✓ YES! (password found)
  Password: DemoPassword123!
  Defense: ⚠️ Disabled
  ```

**Key Teaching Point:**
> "See the difference? Rate limiting reduced the attack surface from 1000s of attempts to just 5. Without defense, the demo password was cracked."

### Demo 5: Review Logs (5 min)

**Scroll Down to "Recent Login Attempts"**
- Show table with all attempts
- Columns: Timestamp, Username, Password, Result, Attack Type, Defense
- Successful attempts are green
- Failed attempts are red
- Show "RATE_LIMIT_BLOCK" defense triggered

**Key Teaching Point:**
> "Every single attempt is logged. Security teams use this to investigate incidents and improve defenses."

---

## PART 3: STUDENT LAB (60-90 minutes)

### Lab Exercise 1: Password Strength Analysis (15 min)

**Objective:** Understand password strength factors

**Instructions:**
1. Go to `/login` page
2. Test 10 different passwords:
   - `a` (too short)
   - `aaaaaaaa` (no complexity)
   - `12345678` (no letters)
   - `password123` (common)
   - `MyP@ss1` (decent)
   - `MyPassword123!` (good)
   - `MyPassword123!abc` (very good)
   - `XyZ9$kL&qMnP2*vW` (excellent)
   - `Tr0pic@lBre3ze!Sun` (excellent)
   - `AEIOUaeiou12345` (weak despite length)

**Analysis Questions:**
1. What password scored highest?
2. Why did common passwords score lower despite length?
3. If each special character adds 4 bits of entropy, calculate total for your strongest password
4. How do crack times change with each additional character?

**Expected Outcome:**
Students understand that:
- Length matters most
- Complexity adds security
- Common passwords are detected
- Math behind crack time estimation

**Rubric (30 points):**
- Tested 10+ passwords: 10 pts
- Identified 3+ factors affecting strength: 10 pts
- Explained findings clearly: 10 pts

---

### Lab Exercise 2: Attack Simulation & Defense (25 min)

**Objective:** Observe how attacks fail with proper defenses

**Part A: Defense ENABLED (10 min)**

**Instructions:**
1. Verify Rate Limiting is **ON**
2. Verify MFA is **ON**
3. Verify Account Lockout is **ON**
4. Run Brute-Force Attack
5. Record results:
   - Attempts before blocked: _____
   - Attack successful?: _____
   - Defense triggered?: _____

6. Run Dictionary Attack
7. Record results

**Part B: Defense DISABLED (10 min)**

**Instructions:**
1. Toggle Rate Limiting **OFF**
2. Toggle MFA **OFF**
3. Toggle Account Lockout **OFF**
4. Run Brute-Force Attack
5. Record results
6. Run Dictionary Attack
7. Record results

**Comparison Analysis:**
1. How many more attempts were needed without defenses?
2. Did any attacks succeed with defenses disabled?
3. Which defense was most effective?
4. What's the cost of perfect defense (difficulty, user experience)?

**Expected Outcome:**
Students see:
- Rate limiting reduces attack surface 50-90%
- Defenses don't stop all attacks
- Layered defense is better than single control

**Rubric (35 points):**
- Ran all attacks with/without defenses: 10 pts
- Recorded all data accurately: 10 pts
- Provided thoughtful analysis: 10 pts
- Identified tradeoffs: 5 pts

---

### Lab Exercise 3: Phishing Analysis (20 min)

**Objective:** Understand why phishing is effective

**Instructions:**
1. Navigate to `/phishing-demo`
2. Read the educational sidebar
3. Enter fake credentials:
   - Email: yourname@evil.com
   - Username: john.doe
   - Password: SuperSecret123!
4. Click "Sign In"
5. Note: You're redirected to real login
6. Go to `/forensics`
7. Look for your phishing entry in audit log
8. Find it in "Incident Timeline"

**Analysis Questions:**
1. How easy would it be to fool a real user?
2. What visual indicators could have warned you?
3. If MFA was enabled, would phishing still work?
4. What training would help users?

**Report (write 1 paragraph):**
"Why was this phishing page effective? What defenses would have prevented credential capture?"

**Expected Outcome:**
Students understand:
- Phishing bypasses technical security
- User awareness is critical
- MFA provides additional protection
- Logging is essential for forensics

**Rubric (20 points):**
- Successfully captured credentials: 5 pts
- Located entry in forensics: 5 pts
- Thoughtful analysis: 10 pts

---

### Lab Exercise 4: Forensics & Incident Response (20 min)

**Objective:** Analyze security incidents like professionals

**Instructions:**
1. Navigate to `/forensics`
2. Review the Incident Timeline
3. Click each event to see details
4. Review the Audit Log table
5. Analyze Attack Pattern Analysis section
6. Read the Incident Recommendations

**Analysis Questions:**
1. How many attacks occurred today?
2. Which attack type was most common?
3. How many phishing credentials were captured?
4. Which defense was triggered most often?
5. Did any defenses fail?

**Written Report (1-2 pages):**
**Title:** "Incident Analysis Report"

**Include:**
- Summary of incidents
- Timeline of events
- Attack pattern analysis
- Defense effectiveness assessment
- Recommendations for improvement

**Expected Outcome:**
Students think like SOC analysts:
- Pattern recognition
- Risk assessment
- Data-driven decisions
- Incident response planning

**Rubric (30 points):**
- Accurate event analysis: 10 pts
- Pattern identification: 10 pts
- Clear recommendations: 10 pts

---

## PART 4: DISCUSSION & CLOSURE (15 minutes)

### Group Discussion (10 min)

**Ask Students:**

1. **Which defense was most effective?**
   - Expected: MFA (99% against phishing)
   - But also: Rate limiting + lockout combination

2. **How would you improve this system?**
   - Possible answers: Better hashing, passwordless auth, device recognition, behavioral biometrics

3. **What's the real-world impact of this?**
   - Connect to LinkedIn breach, Yahoo breach, etc.
   - Show statistics

4. **How does this apply to YOUR passwords?**
   - Make personal connection
   - Encourage strong passwords + MFA

### Key Takeaways (5 min)

**Summarize for Students:**

✅ **Passwords will always exist** - Even with biometrics, passwords remain common

✅ **Weak passwords fail immediately** - Even basic defenses stop most attacks

✅ **Multiple layers matter** - Password + MFA + rate limiting is strong

✅ **Phishing bypasses technology** - Human awareness is critical

✅ **Logging is essential** - You can only protect what you measure

✅ **This is real work** - Security professionals do this daily

✅ **You can make a difference** - Use strong passwords, enable MFA

### Closing Challenge

**For Next Class:**
- "Enable MFA on your personal accounts this week"
- "Create a strong passphrase (15+ characters)"
- "See if you can crack the harder demo password we'll set up"

---

## ASSESSMENT RUBRIC

### Lab Report (100 points total)

| Component | Points | Criteria |
|-----------|--------|----------|
| Exercise 1: Password Strength | 30 | Thorough testing, clear analysis, understanding demonstrated |
| Exercise 2: Attack Simulation | 35 | Accurate data collection, insightful comparison, thoughtful tradeoff analysis |
| Exercise 3: Phishing Analysis | 20 | Successfully identified vulnerabilities, understood defenses |
| Exercise 4: Forensics Report | 15 | Professional analysis, clear recommendations, evidence-based conclusions |

### Grading Scale
- **90-100:** Excellent - Deep understanding, clear thinking
- **80-89:** Good - Solid understanding, minor gaps
- **70-79:** Satisfactory - Basic understanding, some confusion
- **60-69:** Needs Improvement - Significant gaps
- **<60:** Incomplete - Requires revision

---

## DIFFERENTIATION

### For Advanced Students
- Modify the wordlist to include longer passwords
- Add new users with different password strengths
- Analyze the Python code
- Calculate entropy mathematically
- Research real-world attack statistics

### For Struggling Students
- Provide guided questions for each exercise
- Start with just defense toggle observation
- Focus on narrative rather than numbers
- Pair with peer mentor
- Record video walkthrough

### For Mixed Levels
- Group students with different abilities
- Assign roles: Attacker, Defender, Analyst
- Have groups compare findings
- Peer teaching opportunities

---

## TIMING FLEXIBILITY

| Format | Timing |
|--------|--------|
| **Quick Demo** | 15 min (show attacks + dashboard) |
| **Class Period** | 45 min (lecture + quick demos) |
| **2-Hour Lab** | 90 min (full exercises + reports) |
| **Full Day** | 4 hours (with advanced exercises) |
| **Multiple Classes** | Spread over 2-3 weeks with homework |

---

## COMMON STUDENT QUESTIONS

**Q: "Can you actually use this to crack real passwords?"**
A: "No, this is simulated. Real systems have additional protections and limits. This teaches principles safely."

**Q: "Why use passwords at all if they're weak?"**
A: "Good question! We're moving toward passwordless, but passwords persist due to cost and compatibility."

**Q: "How do hackers get such big wordlists?"**
A: "Previous breaches, public dumps, dictionary databases. That's why I shouldn't reuse passwords!"

**Q: "Can MFA be bypassed?"**
A: "In theory yes (SIM swap, intercept). But it stops 99% of automated attacks. Layering matters."

**Q: "What about biometric authentication?"**
A: "Great follow-up! We should use biometrics + password + MFA for strongest security."

---

## EXTENSIONS & HOMEWORK

### For Computer Science Track
- Analyze the source code (Python, Flask, SQL)
- Modify the attack engine
- Implement new defenses
- Calculate entropy mathematically
- Research cryptographic hashing

### For Security/Networking Track
- Research real-world breach case studies
- Design a complete security policy
- Create incident response procedures
- Build a pen-testing methodology
- Propose passwordless architecture

### For General Education
- Write policy recommendations
- Create user training materials
- Design security awareness campaign
- Analyze security team job roles
- Propose defenses for specific scenarios

---

## FACULTY TIPS

✅ **Do:**
- Emphasize this is simulated and ethical
- Connect to real breaches and statistics
- Let students explore freely
- Encourage questions and discussion
- Use actual breach case studies
- Show real SOC dashboards (screenshots)

❌ **Don't:**
- Use this on non-consenting systems
- Claim it teaches "real hacking"
- Rush through demonstrations
- Skip the ethical discussion
- Use real usernames/passwords
- Present as network security

---

## RESOURCES FOR STUDENTS

### Reading
- "Cracking Codes with Python" by Al Sweigart
- OWASP Top 10 Web Security Risks
- NIST Digital Identity Guidelines
- Real breach case studies (links provided)

### Videos
- Cybersecurity documentaries
- TED talks on authentication
- Real-world SOC walkthroughs
- Penetration testing demonstrations

### Practice
- HackTheBox (CTF challenges)
- TryHackMe (beginner labs)
- PicoCTF (CTF competitions)
- OverTheWire (wargames)

---

## FACULTY ASSESSMENT

### Outcomes Achieved:

**Students will be able to:**
- ✅ Explain password attack vectors
- ✅ Evaluate defense effectiveness
- ✅ Analyze security incidents
- ✅ Recommend security policies
- ✅ Apply principles to personal security

**Students will understand:**
- ✅ Why passwords are weak and strong
- ✅ How attackers target systems
- ✅ Why layered defense matters
- ✅ How security teams work
- ✅ Real-world breach prevention

---

## FINAL CHECKLIST

Before teaching:
- [ ] Tested application on Windows/Mac/Linux
- [ ] Verified all features work
- [ ] Read through documentation
- [ ] Tried all demo scenarios
- [ ] Created backup of database
- [ ] Printed lab exercises
- [ ] Set up projection/screen
- [ ] Tested internet connectivity (if needed)
- [ ] Informed students of ethical use
- [ ] Prepared real-world examples

---

**This lab is ready to go! Your students will learn real cybersecurity principles in a safe, engaging, ethical way.**

🔐 **Good luck with your classes!** 🔐

---

*Lab Guide Created: January 27, 2026*  
*Version: 1.0 - Production Ready*  
*Estimated Teaching Time: 90 minutes*  
*Student Assessment: Complete rubric included*
