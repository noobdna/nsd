⸻

NSD – Detection Logic & Rule Engine

Overview

This document describes the detection logic and rule engine used in the NSD (Network Suspicious Detection) system.

The detection engine analyzes incoming device data, GPS data, user activity, and system events to identify suspicious behavior and generate alerts.

The system is rule-based in the initial phase and may later incorporate machine learning–based anomaly detection.

⸻

Detection Objectives

The detection engine aims to:
	•	Detect suspicious movement patterns
	•	Detect abnormal device behavior
	•	Detect unusual activity times
	•	Detect geofence violations
	•	Detect device tampering or signal loss
	•	Assign risk scores to events
	•	Generate alerts for operators
	•	Support investigation and case management

⸻

Input Data for Detection

The detection engine uses the following data:

Device Data
	•	Device ID
	•	Device type
	•	Device owner
	•	Device status
	•	Battery level
	•	Signal strength
	•	Last communication time

GPS / Location Data
	•	Latitude
	•	Longitude
	•	Speed
	•	Direction
	•	Timestamp
	•	Geofence area

Event Data
	•	Login attempts
	•	Access logs
	•	Device movement events
	•	System events
	•	Sensor triggers

Historical Data
	•	Past movement patterns
	•	Normal activity hours
	•	Previous alerts
	•	Device usage history

⸻

Detection Rule Engine

The NSD detection engine uses rule-based logic.

Each rule generates a risk score.
Multiple rules can be combined to increase the total risk level.

⸻

Detection Rules

Rule 1 – Geofence Breach

If a device enters or exits a restricted area unexpectedly, generate a suspicious event.

Example:
	•	Device leaves allowed area
	•	Device enters restricted zone
	•	Device crosses boundary multiple times

Risk Score: Medium

⸻

Rule 2 – Unusual Time Activity

If activity occurs during unusual hours, increase risk score.

Example:
	•	Device movement at midnight
	•	Login attempts at unusual hours
	•	Activity outside normal working hours

Risk Score: Low to Medium

⸻

Rule 3 – Repeated Abnormal Movement

If repeated short-interval movements occur in unusual patterns, flag as suspicious.

Example:
	•	Device appears in multiple distant locations quickly
	•	Repeated back-and-forth movement
	•	Impossible travel speed

Risk Score: Medium

⸻

Rule 4 – Device Tampering / Signal Loss

If a device suddenly stops sending data or shows inconsistent telemetry.

Example:
	•	GPS signal lost suddenly
	•	Device offline unexpectedly
	•	Battery removed
	•	Signal strength drops abruptly

Risk Score: Medium to High

⸻

Rule 5 – Multiple Failed Login Attempts

If repeated login failures occur within a short period.

Example:
	•	5 failed logins within 10 minutes
	•	Login attempts from multiple locations
	•	Login attempts from unknown device

Risk Score: Medium

⸻

Rule 6 – Risk Combination Logic

Multiple low-risk events combined may become high risk.

Example Combination:
	•	Night activity + Geofence breach
	•	Signal loss + Movement anomaly
	•	Failed logins + New device login

Combined Risk: High

⸻

Risk Scoring Model

Risk Level	Score Range	Description
Low	0 – 30	Minor anomaly
Medium	31 – 70	Suspicious activity
High	71 – 100	Highly suspicious
Critical	100+	Immediate alert

Example Risk Score Calculation

Event	Score
Night activity	+10
Geofence breach	+30
Signal loss	+25
Repeated movement	+20
Failed logins	+15

Total Risk Score = Sum of all triggered rules

⸻

Detection Flow

Detection engine workflow:
	1.	Receive device/event data
	2.	Validate data
	3.	Check geofence rules
	4.	Check time-based rules
	5.	Check movement patterns
	6.	Check device status
	7.	Check login/activity anomalies
	8.	Calculate risk score
	9.	Determine risk level
	10.	Generate alert if threshold exceeded
	11.	Store event and risk score in database

⸻

Alert Trigger Threshold

Risk Score	Action
0 – 30	Store event only
31 – 70	Create alert
71 – 100	High priority alert
100+	Critical alert + notification


⸻

Future Enhancements

Future detection improvements may include:
	•	Machine learning anomaly detection
	•	Behavioral pattern learning
	•	Device fingerprinting
	•	Network traffic anomaly detection
	•	Face recognition / camera integration
	•	Predictive risk scoring
	•	Automated response (device lock / account disable)
	•	Integration with SIEM systems
	•	Integration with Cloudflare / AWS logs
	•	AI-based suspicious pattern analysis

⸻

Summary

The NSD detection engine:
	•	Uses rule-based detection logic
	•	Calculates risk scores from multiple events
	•	Combines multiple low-risk signals into high-risk alerts
	•	Generates alerts and investigation cases
	•	Stores all detection data for analysis
	•	Can later evolve into AI/ML detection system

⸻
