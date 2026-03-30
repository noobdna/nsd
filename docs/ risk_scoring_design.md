⸻

NSD – Risk Scoring Design

Overview

The Risk Scoring System evaluates events, behaviors, and anomalies detected in the NSD system and assigns a numerical risk score.
This score is used to determine alert levels, trigger notifications, and prioritize investigations.

The goal of the risk scoring system is to:
	•	Quantify suspicious behavior
	•	Reduce false positives
	•	Prioritize incidents
	•	Automate alert severity
	•	Support investigation workflow

⸻

Risk Scoring Architecture

Logs / Events / Behavior Data
            ↓
      Feature Extraction
            ↓
      Risk Calculation Engine
            ↓
        Risk Score
            ↓
   Alert / Case / Dashboard


⸻

Risk Score Components

Risk score is calculated from multiple factors.

Main Risk Factors

Factor	Description
Login Failures	Repeated login failures
Access Time	Unusual access time
Geo Location	Unusual location
Access Frequency	Too many operations
Device Change	New device login
Privilege Usage	Admin privilege usage
Network Behavior	Suspicious network activity
Error Behavior	Repeated user errors
Data Access	Large data access
Policy Violation	Security policy violation


⸻

Risk Score Formula

Basic scoring model:

Risk Score = 
    LoginFailureScore +
    TimeAnomalyScore +
    GeoScore +
    FrequencyScore +
    DeviceScore +
    PrivilegeScore +
    NetworkScore +
    ErrorScore +
    DataAccessScore +
    PolicyScore

Example weighted model:

Risk Score =
    (LoginFailures × 5) +
    (UnusualTime × 10) +
    (NewLocation × 15) +
    (HighFrequency × 8) +
    (NewDevice × 10) +
    (AdminAction × 12) +
    (NetworkAnomaly × 15) +
    (UserErrors × 4) +
    (LargeDataAccess × 10) +
    (PolicyViolation × 20)


⸻

Risk Score Levels

Score	Level	Description
0–19	Low	Normal behavior
20–39	Medium	Suspicious
40–59	High	Likely suspicious
60–79	Critical	Highly suspicious
80+	Severe	Immediate response


⸻

Alert Mapping

Risk Level	Alert
Low	No alert
Medium	Log only
High	Alert
Critical	Alert + Notification
Severe	Incident + Immediate Notification


⸻

Risk Score Example

Example Scenario

User behavior:
	•	5 login failures
	•	Access at unusual time
	•	New device
	•	Admin action

Calculation:

LoginFailures = 5 × 5 = 25
UnusualTime = 10
NewDevice = 10
AdminAction = 12

Total Risk Score = 57

Result:

Risk Level = HIGH
Action = Alert


⸻

Time-Based Risk Adjustment

Risk should increase when events occur in a short period.

Example:

If events within 10 minutes:
    Score × 1.5

If events within 1 hour:
    Score × 1.2

Decay model:

RiskScore = RiskScore × e^(-time / decay_factor)

This prevents old events from keeping risk high forever.

⸻

Entity Risk Scoring

Risk scores are tracked per entity.

Entities

Entity	Description
User	User account
Device	Device ID
IP Address	Source IP
Location	Geo
Session	Login session

Each entity has its own risk score history.

⸻

Risk Score Storage

Risk score table example:

entity_id	entity_type	risk_score	last_updated
user_001	user	45	timestamp
ip_10.0.0.5	ip	60	timestamp


⸻

Risk Scoring Flow

Event Received
      ↓
Feature Extraction
      ↓
Score Calculation
      ↓
Time Adjustment
      ↓
Entity Score Update
      ↓
Risk Level Determination
      ↓
Alert Decision


⸻

Future Improvements

Future enhancements may include:
	•	Machine learning scoring
	•	Behavior baseline per user
	•	Peer group analysis
	•	Risk trend analysis
	•	Automatic account lock
	•	Automatic device isolation
	•	UEBA (User Behavior Analytics)
	•	Graph-based risk propagation
	•	AI anomaly detection

⸻

Summary

The Risk Scoring System is the core intelligence of NSD.

It:
	•	Converts behavior into numerical risk
	•	Determines alert severity
	•	Prioritizes investigations
	•	Tracks risky entities
	•	Enables automated response

Without risk scoring, detection systems generate too many alerts.
Risk scoring makes the system intelligent and actionable.

⸻
