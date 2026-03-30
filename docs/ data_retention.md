⸻

NSD – Data Retention Policy

Overview

This document defines the data retention policy for the NSD (Network Suspicious Detection) system.

The system collects and stores various types of data including events, alerts, cases, audit logs, and evidence files.
To ensure privacy, legal compliance, storage efficiency, and system performance, data must be retained only for appropriate periods and archived or deleted when no longer needed.

The retention policy ensures:
	•	evidence preservation
	•	investigation traceability
	•	auditability
	•	legal compliance
	•	storage cost control
	•	system performance
	•	privacy protection

⸻

Data Classification

NSD stores multiple categories of data. Each category has different retention requirements.

Data Categories

Data Type	Description
Events	Raw telemetry, logs, device activity
Alerts	Suspicious activity alerts
Cases	Investigation cases
Evidence	Files, logs, screenshots, exported data
Audit Logs	User actions and system actions
Risk Scores	Risk scoring history
Reports	Investigation and incident reports
User Data	Users, roles, organizations
Device Data	Device metadata and status
System Logs	Application/system logs
Backups	Database backups


⸻

Retention Period Policy

Default Retention Periods

Data Type	Retention Period
Events	90 days
Alerts	1 year
Cases	3 years
Evidence	3–5 years
Audit Logs	2 years
Risk Score History	1 year
Reports	3 years
System Logs	90 days
Backups	30–90 days
User / Organization Data	Until account deletion
Device Metadata	Until device deletion


⸻

Retention Strategy

Event Data

Event data can grow very large, so retention should be shorter.

Lifecycle:
	1.	Store raw events in hot storage
	2.	After 30 days → move to warm storage
	3.	After 90 days → archive or delete
	4.	Keep aggregated statistics longer

Event lifecycle example:

Hot Storage (0–30 days)
Warm Storage (30–90 days)
Archive / Delete (>90 days)


⸻

Alerts and Cases

Alerts and cases are part of investigations and should be retained longer.

Policy:
	•	Alerts retained for at least 1 year
	•	Cases retained for at least 3 years
	•	Closed cases may be archived
	•	High severity cases may be retained longer

⸻

Evidence Data

Evidence may be required for:
	•	internal investigations
	•	legal cases
	•	incident reports
	•	law enforcement requests

Evidence retention:
	•	minimum 3 years
	•	recommended 5 years
	•	must not be modified
	•	must be access logged
	•	must support export

Evidence storage should be:
	•	encrypted
	•	access controlled
	•	immutable (WORM storage recommended)

⸻

Audit Logs

Audit logs record:
	•	login
	•	logout
	•	alert updates
	•	case updates
	•	evidence uploads
	•	admin actions
	•	rule changes
	•	permission changes
	•	system configuration changes

Audit logs must:
	•	be immutable
	•	be tamper-evident
	•	be retained at least 2 years
	•	be exportable

⸻

Data Lifecycle Management

Data Lifecycle Flow

Data Created
    ↓
Active Storage
    ↓
Archive Storage
    ↓
Retention Expired
    ↓
Deletion / Anonymization


⸻

Data Deletion Policy

When retention period expires:

Possible actions:
	•	permanent deletion
	•	anonymization
	•	aggregation only
	•	archive to cold storage
	•	legal hold extension

Deletion must:
	•	be logged
	•	be auditable
	•	be irreversible
	•	follow retention policy rules
	•	respect legal hold

⸻

Legal Hold

If an investigation or legal request is active:

Data must:
	•	not be deleted
	•	not be modified
	•	be preserved
	•	be exportable
	•	be access logged

Legal hold applies to:
	•	events
	•	alerts
	•	cases
	•	evidence
	•	audit logs
	•	reports

Legal hold overrides retention policy.

⸻

Storage Tier Strategy

Storage Tier	Purpose
Hot Storage	Active investigations
Warm Storage	Recent historical data
Cold Storage	Archived investigations
Immutable Storage	Evidence and audit logs
Backup Storage	Disaster recovery


⸻

Security Requirements for Stored Data

Stored data must be:
	•	encrypted at rest
	•	encrypted in transit
	•	access controlled
	•	audit logged
	•	backed up
	•	protected against deletion
	•	protected against tampering
	•	exportable for investigations

Recommended:
	•	Object storage with versioning
	•	Immutable storage for evidence
	•	Separate audit log storage
	•	Separate backup account
	•	Encryption key management

⸻

Summary

Retention Summary Table

Data	Retention
Events	90 days
Alerts	1 year
Cases	3 years
Evidence	3–5 years
Audit Logs	2 years
Reports	3 years
System Logs	90 days
Backups	30–90 days


⸻

Final Notes

The NSD data retention policy is designed to balance:
	•	security
	•	investigation capability
	•	legal compliance
	•	privacy protection
	•	storage cost
	•	system performance
	•	long-term auditability

Proper data retention and lifecycle management are critical for any security monitoring and investigation platform.

⸻
