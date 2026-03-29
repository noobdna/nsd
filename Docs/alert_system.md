⸻

NSD – Alert & Notification System

Overview

This document describes the alert and notification system used in NSD (Network Suspicious Detection).

The alert system is responsible for notifying operators when suspicious activity is detected and ensuring that alerts are tracked, escalated, and resolved properly.

The system must support real-time alerts, alert management, escalation workflows, and audit logging.

⸻

Alert Flow Overview

Detection to alert flow:

Device / GPS / Event Data
        ↓
Detection Engine
        ↓
Risk Scoring
        ↓
Alert Generation
        ↓
Notification Service
        ↓
Operator Dashboard / Email / Push
        ↓
Case Management / Investigation


⸻

Alert Types

NSD supports multiple alert categories.

1. Geofence Alert

Triggered when a device enters or exits a restricted or monitored area.

Examples:
	•	Device enters restricted area
	•	Device leaves safe zone
	•	Device remains in restricted area too long

⸻

2. Behavior Alert

Triggered when unusual behavior patterns are detected.

Examples:
	•	Activity during unusual hours
	•	Repeated abnormal movement
	•	Suspicious repeated actions
	•	Abnormal device usage pattern

⸻

3. Device Alert

Triggered when device status indicates possible tampering or malfunction.

Examples:
	•	Device offline unexpectedly
	•	Battery removed
	•	Signal lost
	•	Device reset detected

⸻

4. Risk Score Alert

Triggered when combined risk score exceeds a threshold.

Examples:
	•	Multiple minor anomalies combined
	•	Repeated suspicious events
	•	Pattern-based risk escalation

⸻

Alert Severity Levels

Each alert has a severity level.

Level	Name	Description
1	Low	Minor anomaly
2	Medium	Suspicious behavior
3	High	Highly suspicious
4	Critical	Immediate action required

Severity is calculated using:
	•	Risk score
	•	Alert type
	•	Event frequency
	•	Time of occurrence
	•	Device history

⸻

Alert Data Model

Alert information stored in database:

Field	Description
alert_id	Alert unique ID
device_id	Device ID
alert_type	Type of alert
severity	Alert severity
risk_score	Calculated risk score
location	GPS location
timestamp	Alert time
status	Open / Investigating / Closed
assigned_to	Operator
description	Alert details
created_at	Creation time
updated_at	Last update


⸻

Alert Status Lifecycle

Alert status transitions:

Open → Investigating → Resolved → Closed

Status definitions:

Status	Description
Open	New alert created
Investigating	Operator reviewing
Resolved	Issue resolved
Closed	Case completed


⸻

Notification Methods

The system should support multiple notification channels.

Notification Channels
	•	Dashboard alert
	•	Email notification
	•	SMS (optional)
	•	Mobile push notification
	•	Slack / Teams (optional)
	•	Webhook (for external systems)

⸻

Escalation Rules

If alerts are not handled within a certain time, escalation occurs.

Example escalation policy:

Severity	Escalation Time
Low	No escalation
Medium	1 hour
High	15 minutes
Critical	Immediate

Escalation actions:
	•	Notify supervisor
	•	Send additional notifications
	•	Create incident case automatically

⸻

Alert Dashboard Features

The frontend dashboard should allow operators to:
	•	View alert list
	•	Filter alerts by severity
	•	Filter by device / location
	•	View alert details
	•	Assign alert to operator
	•	Change alert status
	•	Create investigation case
	•	View alert history
	•	View alert map
	•	Export alert report

⸻

Alert Logging & Audit Trail

All alert-related actions must be logged.

Audit log should record:
	•	Alert created
	•	Alert updated
	•	Status change
	•	Assignment change
	•	Escalation triggered
	•	Notification sent
	•	Alert closed

Audit fields:
	•	log_id
	•	alert_id
	•	action
	•	user_id
	•	timestamp
	•	notes

⸻

Future Enhancements

Planned improvements:
	•	AI-based alert prioritization
	•	Alert correlation (multiple alerts grouped)
	•	False positive detection
	•	Automatic device lock / disable
	•	Predictive alerting
	•	Risk trend analysis
	•	Heatmap visualization
	•	Incident timeline view

⸻

Summary

The NSD Alert System is responsible for:
	•	Generating alerts from detection engine
	•	Assigning severity and risk score
	•	Notifying operators
	•	Managing alert lifecycle
	•	Supporting escalation workflow
	•	Logging all actions for audit
	•	Integrating with dashboard and case management

This system is critical for real-time monitoring and incident response operations.

⸻
