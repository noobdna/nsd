⸻

NSD – Detection Logic

Docs/detection_logic.md

Overview

This document describes the detection logic used in the NSD (Network Suspicious Detection) system.

The Detection Engine analyzes incoming events from devices, network logs, sensors, authentication systems, and user activity logs to identify suspicious behavior patterns and generate risk scores, alerts, and investigation cases.

The detection system is designed to be:
	•	behavior-based
	•	rule-based
	•	score-based
	•	explainable
	•	auditable
	•	extensible
	•	near real-time capable
	•	suitable for security, safety, and anomaly detection

The system does not rely only on signatures, but focuses on behavior patterns and anomalies.

⸻

Detection Flow

Detection Pipeline

The detection process follows this pipeline:

Event → Normalization → Rule Evaluation → Risk Scoring → Alert → Case

Step-by-step Flow
	1.	Event is received from Event API
	2.	Event is normalized into a standard format
	3.	Detection rules are evaluated
	4.	Risk score is calculated
	5.	If threshold exceeded → Alert created
	6.	If severe → Case created
	7.	All steps logged for audit

⸻

Event Normalization

Different event sources produce different formats.
The system converts all incoming data into a unified event structure.

Normalized Event Structure

Example:

{
  "event_id": "EVT-20260330-0001",
  "timestamp": "2026-03-30T12:00:00Z",
  "event_type": "login_failed",
  "source_type": "authentication",
  "device_id": "DEV-001",
  "user_id": "USR-002",
  "ip_address": "203.0.113.5",
  "location_id": "LOC-001",
  "severity": "low",
  "raw_data": {}
}

Normalization ensures that the Detection Engine can process events consistently regardless of source.

⸻

Detection Categories

The NSD Detection Engine focuses on behavior-based suspicious activity rather than malware signatures.

Major Detection Categories

1. Authentication Anomalies

Examples:
	•	repeated failed logins
	•	login from unusual location
	•	login at unusual time
	•	impossible travel (Tokyo → New York in 1 hour)
	•	multiple accounts from same IP
	•	password reset abuse
	•	login after account disable
	•	login from TOR / VPN / suspicious ASN

⸻

2. Device Behavior Anomalies

Examples:
	•	device suddenly changes location
	•	device goes offline frequently
	•	device sends abnormal number of events
	•	device firmware changes unexpectedly
	•	device communicates with unknown servers
	•	device IP address changes repeatedly

⸻

3. Network Behavior Anomalies

Examples:
	•	port scanning
	•	repeated connection attempts
	•	unusual traffic volume
	•	access to restricted endpoints
	•	repeated API failures
	•	unusual protocol usage
	•	abnormal DNS queries

⸻

4. Physical / GPS / Movement Anomalies

Examples:
	•	movement outside allowed area
	•	movement during restricted time
	•	device stopped unexpectedly
	•	device moving too fast
	•	device location spoofing suspicion

⸻

5. User Behavior Anomalies

Examples:
	•	unusual working hours
	•	excessive downloads
	•	unusual number of operations
	•	repeated mistakes / failed operations
	•	accessing many devices in short time
	•	privilege escalation attempts

⸻

Rule-Based Detection

The system supports rule-based detection logic.

Rule Example

Example rule:

IF failed_login_count > 5 within 10 minutes
THEN risk_score += 30

Another example:

IF login_location not in allowed_locations
THEN risk_score += 40

Rules are stored in the rules table in the database and can be updated without redeploying the system.

⸻

Risk Scoring Model

Each event contributes to a risk score.

Example Risk Score Weights

Event Type	Score
Failed login	+5
Multiple failed logins	+20
Login from new country	+40
Device offline unexpectedly	+10
Port scanning detected	+50
Access denied repeatedly	+15
Privilege escalation	+60

Risk Score Thresholds

Risk Score	Action
0 – 19	Log only
20 – 39	Low risk
40 – 59	Medium risk → Alert
60 – 79	High risk → Alert
80+	Critical → Alert + Case

Risk scores can be calculated for:
	•	event
	•	device
	•	user
	•	IP address
	•	organization
	•	location

⸻

Alert Generation Logic

An alert is generated when:

risk_score >= alert_threshold

Example:

IF risk_score >= 50
→ create alert

Alert includes:
	•	related events
	•	device
	•	user
	•	IP
	•	risk score
	•	severity
	•	rule triggered

⸻

Case Creation Logic

A case is created when:
	•	risk score is very high
	•	multiple alerts related
	•	manual escalation
	•	security incident confirmed
	•	investigation required

Example:

IF risk_score >= 80
→ create case automatically

Or:

IF 3 alerts within 1 hour for same device
→ create case


⸻

Detection Engine Architecture

Detection Engine Components

The Detection Engine consists of:
	1.	Event Normalizer
	2.	Rule Engine
	3.	Risk Scoring Engine
	4.	Alert Engine
	5.	Case Engine
	6.	Audit Logger

Logical Flow

Event API
   ↓
Event Normalizer
   ↓
Rule Engine
   ↓
Risk Scoring Engine
   ↓
Alert Engine
   ↓
Case Engine
   ↓
Database


⸻

Future Detection Enhancements

The detection engine may be extended with:
	•	machine learning anomaly detection
	•	behavior baseline modeling
	•	peer group analysis
	•	time-series anomaly detection
	•	graph-based relationship detection
	•	insider threat detection
	•	fraud detection patterns
	•	automated response (account lock, device isolation)
	•	integration with SIEM / SOAR
	•	threat intelligence feeds
	•	reputation scoring (IP / ASN / domain)

⸻

Summary

The NSD Detection Engine is based on:
	•	Event normalization
	•	Rule-based detection
	•	Risk scoring
	•	Alert generation
	•	Case creation
	•	Behavior analysis
	•	Audit logging

The detection pipeline is:

Device / Logs / Sensors
        ↓
      Event
        ↓
   Detection Engine
        ↓
    Risk Score
        ↓
      Alert
        ↓
       Case
        ↓
   Investigation

This detection logic forms the core intelligence layer of the NSD system.

⸻
