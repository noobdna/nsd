⸻

NSD – Alert System Design

Overview

This document describes the alert and notification system for NSD (Network Suspicious Detection).

The alert system is responsible for:
	•	detecting suspicious activity
	•	generating alerts
	•	notifying operators
	•	managing alert lifecycle
	•	supporting escalation to investigation cases
	•	maintaining audit trails

The alert system acts as the bridge between Detection Engine and Investigation / Response workflows.

⸻

Alert Flow

High-Level Flow

Event → Detection Engine → Risk Scoring → Alert → Notification → Case (optional)

Detailed flow:

Device / Log / Sensor
        ↓
      Event
        ↓
 Detection Engine
        ↓
 Risk Score Calculation
        ↓
 Alert Generated
        ↓
 Notification Sent
        ↓
 Operator Review
        ↓
 Escalate to Case (if needed)


⸻

Alert Severity Levels

Alerts should be categorized by severity.

Severity Levels

Level	Name	Description
1	Info	Informational event
2	Low	Minor suspicious behavior
3	Medium	Suspicious activity
4	High	High-risk activity
5	Critical	Immediate action required

Example

Event	Severity
Single failed login	Low
Multiple failed logins	Medium
Login from unusual country	High
Brute force attack	Critical
Data exfiltration	Critical


⸻

Alert Types

The system should support multiple alert categories.

Alert Categories
	•	authentication_alert
	•	network_alert
	•	device_alert
	•	behavior_alert
	•	location_alert
	•	anomaly_alert
	•	system_alert
	•	security_alert
	•	policy_alert
	•	investigation_alert

Example Alert Types

Alert Type	Description
multiple_failed_logins	Multiple login failures
unusual_login_time	Login at unusual hours
unusual_location	Login from unusual location
device_offline	Device stopped sending data
device_tampering	Device tampering suspected
abnormal_network_traffic	Unusual network traffic
gps_boundary_violation	GPS left allowed area
excessive_operations	Too many operations
privilege_escalation	Permission escalation
data_access_spike	Sudden large data access


⸻

Alert Object Structure

Alert JSON Example

{
  "alert_id": "ALT-20260330-0001",
  "title": "Multiple Failed Login Attempts",
  "description": "5 failed login attempts detected within 10 minutes",
  "severity": "medium",
  "status": "open",
  "alert_type": "authentication_alert",
  "source_type": "user_account",
  "source_id": "USR-001",
  "device_id": "DEV-002",
  "location_id": "LOC-003",
  "risk_score": 72,
  "event_count": 5,
  "first_event_time": "2026-03-30T10:00:00Z",
  "last_event_time": "2026-03-30T10:08:00Z",
  "created_at": "2026-03-30T10:09:00Z",
  "assigned_to": null,
  "case_id": null,
  "organization_id": "ORG-001"
}


⸻

Alert Status Lifecycle

Alerts should have a lifecycle.

Alert Status

Status	Description
open	Newly created alert
acknowledged	Operator acknowledged
investigating	Under investigation
escalated	Escalated to case
resolved	Issue resolved
closed	Closed
false_positive	False alert

Lifecycle Flow

open → acknowledged → investigating → resolved → closed
                        ↓
                     escalated → case


⸻

Notification System

Alerts should trigger notifications depending on severity.

Notification Methods
	•	Email
	•	SMS
	•	Push notification
	•	Slack / Teams
	•	Dashboard alert
	•	Webhook
	•	API callback
	•	SIEM integration

Notification Rules Example

Severity	Notification
Info	Dashboard only
Low	Dashboard
Medium	Email
High	Email + Push
Critical	Email + SMS + Push


⸻

Alert Escalation Rules

Alerts may automatically escalate.

Example Escalation Rules

Condition	Action
Critical alert	Create case automatically
Same alert repeated 5 times	Escalate
Alert not acknowledged for 30 min	Escalate
Multiple alerts from same device	Escalate
Risk score > 85	Escalate


⸻

Alert Correlation

The system should correlate alerts.

Correlation Examples

Situation	Correlated Alert
Failed login + unusual location	Account takeover
Device offline + GPS movement	Device theft
Multiple network alerts	Intrusion
Privilege escalation + data access spike	Insider threat

Alert correlation improves detection accuracy and reduces false positives.

⸻

Alert Dashboard Information

Dashboard should display:
	•	Open alerts
	•	Alerts by severity
	•	Alerts by location
	•	Alerts by device
	•	Alerts timeline
	•	Alerts heatmap
	•	Alert trends
	•	Top risky devices
	•	Top risky users
	•	Escalated cases
	•	Response time metrics

⸻

Metrics for Alert System

Important metrics:

Metric	Description
alerts_per_day	Number of alerts per day
critical_alerts	Critical alerts count
mean_time_to_acknowledge	Time to acknowledge
mean_time_to_resolve	Time to resolve
escalation_rate	Alerts escalated to cases
false_positive_rate	False alert rate
alerts_by_type	Alerts per category
alerts_by_device	Alerts per device

These metrics help evaluate detection performance.

⸻

Summary

The Alert System is responsible for:
	•	generating alerts from detection engine
	•	categorizing alerts
	•	managing alert lifecycle
	•	notifying operators
	•	escalating to investigation cases
	•	correlating alerts
	•	providing dashboard visibility
	•	tracking response metrics

The alert system is a core component of NSD and connects Detection Engine, Case Management, Notification System, and Dashboard.

⸻
