⸻

NSD – Risk Scoring Engine

Overview

The Risk Scoring Engine is responsible for evaluating events, behaviors, and entities (devices, users, locations) and assigning a numerical risk score that represents the level of suspicious activity.

Risk scores are used to:
	•	trigger alerts
	•	prioritize investigations
	•	identify high-risk devices or users
	•	detect abnormal behavior patterns
	•	support automated responses
	•	generate reports and analytics

The risk scoring system is a core component of the NSD (Network Suspicious Detection) platform.

⸻

Risk Scoring Targets

Risk scores can be calculated for multiple entities:

Entity	Description
Event	Individual event risk
Device	Device behavior risk
User	User behavior risk
Location	Location-based risk
Session	Login or activity session risk
Organization	Aggregate risk level


⸻

Risk Score Range

Risk scores range from:

0 – 100

Score	Risk Level
0–19	Very Low
20–39	Low
40–59	Medium
60–79	High
80–100	Critical


⸻

Risk Factors

Risk scores are calculated based on multiple factors.

Example Risk Factors

Factor	Description
Failed login attempts	Repeated authentication failures
Login time anomaly	Login at unusual hours
Location anomaly	Access from unusual location
Device anomaly	Unknown or new device
Activity frequency	Too many operations in short time
Privilege usage	Admin or sensitive operations
Rule match	Detection rule triggered
Blacklist match	IP / device / user flagged
Behavior deviation	Behavior outside normal pattern
Multiple alerts	Repeated alerts for same entity


⸻

Example Risk Weight Table

Event Type	Risk Points
Failed login	+5
Multiple failed logins	+15
Login from new location	+20
Login at unusual time	+10
Admin action	+15
Data export	+25
Access restricted area	+30
Device offline abnormal	+10
Detection rule match	+20
Blacklist match	+40


⸻

Risk Score Calculation Example

Example scenario:
	•	10 failed logins → +15
	•	Login from new location → +20
	•	Login at unusual time → +10

Total Risk Score = 45 → Medium Risk

Another example:
	•	Detection rule triggered → +20
	•	Blacklist IP → +40
	•	Data export → +25

Total Risk Score = 85 → Critical Risk → Alert Generated


⸻

Risk Score Aggregation

Risk scores can be aggregated over time.

Device Risk Score

Device Risk = Sum of recent event risk scores
              + behavior anomaly score
              + alert history score

User Risk Score

User Risk = Failed logins
            + unusual login times
            + privilege usage
            + alerts
            + case history

Location Risk Score

Location Risk = number of alerts
                + suspicious events
                + device risk average


⸻

Time Decay (Risk Score Reduction)

Risk should decrease over time if no suspicious activity occurs.

Example decay model:

Time Without Events	Risk Reduction
1 hour	−5
6 hours	−10
24 hours	−20
7 days	reset to baseline

This prevents permanent high risk after old events.

⸻

Risk Score → Alert Threshold

Risk Score	Action
0–39	No alert
40–59	Low alert
60–79	High alert
80+	Critical alert
90+	Auto case creation
95+	Auto response / lock


⸻

Example Risk Scoring Flow

Event occurs
     ↓
Risk Engine evaluates event
     ↓
Assign event risk score
     ↓
Update device risk score
     ↓
Update user risk score
     ↓
Check thresholds
     ↓
Generate alert if needed
     ↓
Escalate to case if high risk


⸻

Risk Score Database Tables

risk_scores Table

Field	Description
risk_id	Risk record ID
entity_type	device / user / location / event
entity_id	ID of entity
risk_score	Current risk score
risk_level	low / medium / high / critical
calculated_at	Calculation time
calculation_reason	Why risk changed


⸻

risk_score_history Table

Field	Description
history_id	History ID
entity_type	device / user / location
entity_id	Entity ID
old_score	Previous score
new_score	New score
reason	Reason for change
event_id	Related event
created_at	Timestamp


⸻

Risk Engine Pseudocode

function calculateRisk(event):
    score = 0

    if event.type == "failed_login":
        score += 5

    if event.failed_login_count > 5:
        score += 10

    if event.new_location:
        score += 20

    if event.unusual_time:
        score += 10

    if event.rule_match:
        score += 20

    if event.blacklist_match:
        score += 40

    return score


⸻

Future Enhancements

Future versions of the risk engine may include:
	•	Machine learning anomaly detection
	•	Behavior baseline modeling
	•	User behavior profiling
	•	Device fingerprinting
	•	Geo velocity detection
	•	Risk prediction
	•	Automated response actions
	•	Cross-organization threat intelligence
	•	Risk graph analysis
	•	Relationship-based risk scoring

⸻

Summary

The Risk Scoring Engine:
	•	converts events into risk scores
	•	tracks device/user/location risk levels
	•	triggers alerts and cases
	•	prioritizes investigations
	•	supports automation
	•	enables analytics and reporting

The risk engine is the decision core of the NSD platform.

⸻
