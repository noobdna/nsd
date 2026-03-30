⸻

NSD – Notification Rules

Overview

This document defines the notification rules for the NSD (Network Suspicious Detection) system.

The notification system is responsible for informing users, administrators, and security operators when important events occur, such as alerts, case updates, system issues, or suspicious activities.

Notification rules ensure that the right people receive the right information at the right time without causing notification overload.

⸻

Notification Event Types

The NSD system generates notifications for various event types.

1. Alert Notifications

Triggered when a new alert is created.

Examples:
	•	Multiple failed logins
	•	Unusual login time
	•	Device offline
	•	Suspicious location access
	•	Risk score exceeded threshold
	•	Detection rule triggered

2. Alert Status Changes

Triggered when alert status changes.

Examples:
	•	Alert assigned
	•	Alert acknowledged
	•	Alert escalated to case
	•	Alert resolved
	•	Alert closed

3. Case Notifications

Triggered when investigation cases change.

Examples:
	•	Case created
	•	Case assigned
	•	Evidence added
	•	Case status changed
	•	Case closed
	•	Investigation report generated

4. System Notifications

Triggered by system events.

Examples:
	•	Detection engine stopped
	•	Notification service failure
	•	Database connection issue
	•	Storage limit reached
	•	API errors
	•	Device ingestion stopped

5. Security Notifications

Triggered by security-related events.

Examples:
	•	Multiple admin login failures
	•	Suspicious API usage
	•	Permission changes
	•	User role changes
	•	Unauthorized access attempt
	•	Audit log tampering detected

⸻

Notification Severity Levels

Notifications have severity levels that determine priority and delivery method.

Severity	Description	Example
Critical	Immediate action required	Admin account compromise
High	Serious suspicious activity	Multiple login failures
Medium	Suspicious but not urgent	Unusual login time
Low	Informational	Device status change
Info	System information	Report generated


⸻

Notification Channels

Notifications can be delivered through multiple channels.

Channel	Use Case
Email	Alerts, case updates, reports
SMS	Critical alerts
Push Notification	Mobile alerts
Dashboard	All notifications
Webhook	External integrations
Slack / Teams	Team notifications
PagerDuty	Critical incidents
API	External systems


⸻

Notification Routing Rules

Notifications are routed based on event type, severity, and organization settings.

Example Routing Rules

Event	Severity	Notify
Critical security alert	Critical	Admin + Security Team + SMS
High risk alert	High	Security Team
Medium alert	Medium	Assigned operator
Low alert	Low	Dashboard only
Case assigned	Info	Assigned user
Case closed	Info	Case creator
System error	High	System admin
Device offline	Medium	Device owner


⸻

Notification Rule Logic

Notification rule logic determines when notifications are sent.

Example Logic
	1.	Alert created
	2.	Calculate severity
	3.	Determine organization notification policy
	4.	Determine recipients
	5.	Determine notification channels
	6.	Send notification
	7.	Log notification in audit log

Flow:

Event Occurs
     ↓
Notification Rule Engine
     ↓
Determine Severity
     ↓
Determine Recipients
     ↓
Determine Channels
     ↓
Send Notification
     ↓
Log Notification


⸻

Notification Rule Configuration

Notification rules are configurable per organization.

Configurable Settings

Organizations can configure:
	•	Alert severity thresholds
	•	Notification channels per severity
	•	Quiet hours / Do Not Disturb
	•	Escalation timeouts
	•	Re-notification intervals
	•	Notification recipients
	•	Webhook URLs
	•	Integration settings (Slack, PagerDuty, etc.)
	•	Notification language
	•	Digest notifications (daily / weekly)

⸻

Escalation Rules

If alerts are not acknowledged within a defined time, escalation rules apply.

Example Escalation Policy

Severity	Escalate After
Critical	5 minutes
High	15 minutes
Medium	1 hour
Low	No escalation

Escalation actions:
	•	Notify supervisor
	•	Notify admin
	•	Send SMS
	•	Create case automatically
	•	Increase alert severity

⸻

Notification Deduplication

To avoid notification spam, the system supports deduplication.

Deduplication Examples
	•	Same alert repeated within 5 minutes → single notification
	•	Device offline alerts grouped
	•	Multiple failed logins grouped
	•	Daily summary instead of multiple low alerts

Deduplication keys may include:
	•	device_id
	•	user_id
	•	alert_type
	•	location_id
	•	time window

⸻

Notification Audit Log

All notifications must be logged for auditing.

Notification Log Fields

Field	Description
notification_id	Notification ID
event_type	Alert / Case / System
related_id	alert_id / case_id
severity	Severity
recipient	User or group
channel	Email / SMS / Push
status	Sent / Failed
sent_at	Timestamp
retry_count	Retry attempts


⸻

Summary

The NSD notification rules system ensures that:
	•	Important events trigger notifications
	•	Notifications are routed correctly
	•	Severity determines delivery method
	•	Escalations happen automatically
	•	Duplicate notifications are minimized
	•	All notifications are auditable
	•	Organizations can customize notification behavior

The notification rules engine is a core operational component of the NSD platform and supports alert response, investigation workflows, and system reliability.

⸻
