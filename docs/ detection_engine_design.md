
⸻

NSD – Detection Engine Design

detection_engine_design.md

Overview

The Detection Engine is the core component of NSD (Network / Neighborhood Suspicious Detection).
It analyzes incoming events, evaluates risk scores, detects suspicious behavior patterns, and generates alerts.

The engine is designed to detect anomalies and suspicious activities from multiple data sources such as:
	•	Network logs
	•	Authentication logs
	•	IoT devices
	•	GPS trackers
	•	Cameras
	•	Access control systems
	•	Application logs
	•	Cloud logs

The Detection Engine operates in near real-time and supports rule-based detection, behavior analysis, and risk scoring.

⸻

Detection Engine Architecture

High Level Flow

Event Ingestion
      ↓
Event Normalization
      ↓
Rule Engine
      ↓
Behavior Analysis
      ↓
Risk Scoring
      ↓
Alert Decision
      ↓
Alert / Case Creation
      ↓
Database / Notification


⸻

Detection Engine Components

1. Event Normalization

Different sources produce different event formats.
The normalization layer converts all events into a unified structure.

Normalized Event Example

{
  event_id
  timestamp
  source_type
  device_id
  user_id
  location
  ip_address
  event_type
  action
  status
  metadata
}

Source Examples

Source	Example Events
Network Logs	login attempt, port scan
GPS	location update
Camera	motion detected
IoT Sensor	door open
Access Control	badge entry
Cloud Logs	API access
Application Logs	password reset

Normalization ensures the detection engine can process all events uniformly.

⸻

Rule Engine

The Rule Engine detects suspicious events based on predefined rules.

Rule Examples

Rule	Description
Multiple login failures	Possible brute force
Login from new country	Suspicious login
Access at unusual time	Behavior anomaly
Too many password resets	Account takeover
Device offline suddenly	Device tampering
GPS impossible travel	Location anomaly
Multiple door open events	Physical intrusion
Port scanning detected	Network recon
Access to sensitive data	Data exfil risk

Rules can be stored in a database and updated dynamically.

⸻

Behavior Analysis Engine

Rule-based detection alone is not enough.
Behavior analysis detects anomalies based on historical patterns.

Behavior Analysis Examples

Behavior	Detection
Login time	unusual time
Access frequency	spike
Movement speed	impossible travel
Device usage	abnormal pattern
Network traffic	abnormal volume
Command usage	suspicious commands
User activity	deviation from baseline

Behavior analysis requires historical data and baseline profiles.

⸻

Risk Scoring Engine

Each event and behavior contributes to a risk score.

Risk Score Formula Example

Risk Score =
    Rule Score
  + Behavior Score
  + Location Score
  + Device Score
  + User Score
  + Time Score

Example Score Table

Event	Score
Login failure	+5
Multiple login failures	+20
New device	+15
New country	+25
Impossible travel	+40
Night activity	+10
Port scanning	+30
Sensitive data access	+35

Risk Levels

Score	Level
0–19	Low
20–39	Medium
40–59	High
60+	Critical


⸻

Alert Decision Engine

The Alert Decision Engine determines whether to generate an alert.

Alert Logic Example

IF risk_score >= 40 → Create Alert
IF risk_score >= 60 → Critical Alert
IF impossible_travel → Alert immediately
IF port_scan_detected → Alert immediately
IF device_tampering → Alert immediately

Alerts may also trigger automatic actions:
	•	Lock account
	•	Disable device
	•	Block IP
	•	Send notification
	•	Create investigation case
	•	Start incident workflow

⸻

Detection Types

Supported Detection Categories

Category	Examples
Authentication	login failures, brute force
Network	port scan, unusual traffic
Location	impossible travel
Device	device tampering
Behavior	unusual usage
Physical	door access
Cloud	API misuse
Data	data exfiltration
System	privilege escalation


⸻

Real-Time vs Batch Detection

Real-Time Detection

Used for immediate threats.

Examples:
	•	Brute force attack
	•	Impossible travel
	•	Port scanning
	•	Unauthorized access
	•	Device tampering

Batch Detection

Used for pattern detection.

Examples:
	•	Weekly behavior anomaly
	•	Data access trends
	•	Risk score trends
	•	Repeated suspicious activity
	•	Long-term anomaly detection

⸻

Detection Engine Data Flow

Data Ingestion API
        ↓
Event Queue (Kafka / Queue)
        ↓
Detection Engine
    ├ Rule Engine
    ├ Behavior Engine
    ├ Risk Scoring
    └ Alert Decision
        ↓
Alerts Table
Cases Table
Events Table
Risk Scores Table
        ↓
Notification System
Dashboard
Investigation System


⸻

Detection Engine Database Tables

Main tables used by the detection engine:

Table	Purpose
events	All incoming events
rules	Detection rules
alerts	Generated alerts
cases	Investigation cases
risk_scores	Risk scoring history
user_profiles	Behavior baseline
device_profiles	Device baseline
locations	Known locations
audit_logs	Engine actions


⸻

Future Enhancements

The Detection Engine may later include:
	•	Machine learning anomaly detection
	•	User behavior analytics (UBA)
	•	Entity behavior analytics (UEBA)
	•	Graph analysis
	•	Attack chain detection
	•	Automated incident response
	•	Threat intelligence integration
	•	Geo risk scoring
	•	Device trust scoring
	•	AI detection assistant

⸻

Summary

The Detection Engine is the brain of NSD.

It performs:
	1.	Event normalization
	2.	Rule-based detection
	3.	Behavior analysis
	4.	Risk scoring
	5.	Alert decision
	6.	Alert / Case creation
	7.	Notification
	8.	Logging and audit

The engine supports both real-time detection and long-term behavior analysis, enabling NSD to detect suspicious activity across networks, devices, users, locations, and physical environments.

⸻
