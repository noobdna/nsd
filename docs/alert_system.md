⸻

NSD – Alert & Notification System

Overview

The Alert & Notification System is responsible for notifying operators when suspicious activity or risk events are detected by the Detection Engine.

The system converts detection results into alerts, manages alert levels, sends notifications, and supports escalation and case creation.

⸻

Alert Flow
	1.	Event is received from device
	2.	Detection Engine analyzes event
	3.	Risk score is calculated
	4.	Alert is generated
	5.	Notification is sent
	6.	Alert may become a Case
	7.	Operator reviews and resolves

Flow:

Event → Detection → Risk Score → Alert → Notification → Case → Resolution

⸻

Alert Levels

The system uses multiple alert levels based on risk score.

Level	Name	Description
1	Info	Minor event, no action needed
2	Low	Slightly suspicious
3	Medium	Suspicious activity
4	High	Dangerous behavior
5	Critical	Immediate response required

Example:
	•	Night movement → Low
	•	Repeated geofence breach → Medium
	•	Device tampering → High
	•	Confirmed intrusion → Critical

⸻

Alert Data Structure

Each alert should contain the following information:
	•	alert_id
	•	event_id
	•	device_id
	•	risk_score
	•	alert_level
	•	alert_type
	•	location
	•	timestamp
	•	status
	•	assigned_to
	•	description
	•	created_at
	•	updated_at

⸻

Alert Status

Status	Description
Open	New alert
Acknowledged	Operator has seen it
Investigating	Under investigation
Escalated	Sent to higher authority
Closed	Resolved


⸻

Notification Methods

The system can send alerts through multiple channels:
	•	Dashboard alerts
	•	Email notifications
	•	Push notifications
	•	SMS (optional)
	•	Webhook (external systems)
	•	Mobile app notifications (future)

⸻

Escalation Rules

If alerts are not handled within a certain time, they should be escalated.

Example escalation policy:

Alert Level	Escalation Time
Low	No escalation
Medium	30 minutes
High	10 minutes
Critical	Immediate

Escalation actions:
	•	Notify supervisor
	•	Send additional alerts
	•	Create incident case
	•	Notify authorities (future integration)

⸻

Alert → Case Conversion

When an alert is serious, it should be converted into a Case.

Case includes:
	•	Multiple alerts
	•	Investigation notes
	•	Assigned operator
	•	Evidence / logs
	•	Final resolution

This allows proper incident management.

⸻

Future Extensions

Possible future improvements:
	•	AI-based alert prioritization
	•	Alert correlation (multiple alerts → one incident)
	•	Predictive alerts
	•	Automatic camera activation
	•	Automatic recording
	•	Integration with police / security companies
	•	Mobile operator app
	•	Real-time map alerts

⸻

Summary

The Alert System is responsible for:
	•	Generating alerts from detection results
	•	Managing alert levels
	•	Sending notifications
	•	Escalating critical alerts
	•	Converting alerts into cases
	•	Supporting incident management

This system is a core component of NSD.

⸻

