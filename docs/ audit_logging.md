⸻

NSD – Audit Logging

Overview

The Audit Logging system records all important actions and system events in the NSD (Network Suspicious Detection) platform.

Audit logs are critical for:
	•	security monitoring
	•	investigation and forensics
	•	compliance and accountability
	•	incident reconstruction
	•	user activity tracking
	•	system change tracking
	•	evidence preservation
	•	legal and regulatory requirements

The audit logging system must be tamper-resistant, searchable, and long-term retainable.

⸻

Goals of Audit Logging

The audit logging system is designed to ensure:
	1.	All critical actions are recorded
	2.	Logs cannot be silently modified or deleted
	3.	Investigators can reconstruct timelines
	4.	User actions are traceable
	5.	System changes are traceable
	6.	Evidence handling is traceable
	7.	Alerts and cases lifecycle are traceable
	8.	API access is traceable
	9.	Multi-tenant environments remain auditable
	10.	Logs can be exported for legal evidence

⸻

What Should Be Logged

Authentication Events
	•	login success
	•	login failure
	•	logout
	•	password change
	•	MFA enabled / disabled
	•	token issued
	•	token revoked
	•	API key created
	•	API key revoked

User Management
	•	user created
	•	user updated
	•	user deleted
	•	role changed
	•	permissions changed
	•	organization membership changed

Device Management
	•	device registered
	•	device updated
	•	device deactivated
	•	device ownership changed
	•	device location changed
	•	device risk score updated

Event & Detection
	•	event received
	•	detection rule triggered
	•	risk score calculated
	•	alert generated
	•	alert updated
	•	alert escalated to case

Case Management
	•	case created
	•	case assigned
	•	case status changed
	•	evidence added
	•	evidence downloaded
	•	investigation note added
	•	case closed

Evidence Handling
	•	file uploaded
	•	file accessed
	•	file downloaded
	•	file deleted
	•	hash verified
	•	evidence linked to case

System Administration
	•	rule created
	•	rule updated
	•	rule deleted
	•	system settings changed
	•	integrations configured
	•	notification settings changed

API Access
	•	API request
	•	API error
	•	permission denied
	•	rate limit triggered

⸻

Audit Log Structure

Audit Log Object

{
  "audit_id": "AUD-20260330-0001",
  "timestamp": "2026-03-30T12:10:33Z",
  "actor_type": "user",
  "actor_id": "USR-001",
  "actor_ip": "203.0.113.25",
  "action": "alert_escalated",
  "resource_type": "alert",
  "resource_id": "ALT-20260330-0001",
  "organization_id": "ORG-001",
  "details": {
    "case_id": "CASE-20260330-0003",
    "previous_status": "open",
    "new_status": "escalated"
  },
  "result": "success"
}


⸻

Audit Log Fields

Field	Description
audit_id	Unique audit log ID
timestamp	Event timestamp
actor_type	user / system / device / api
actor_id	ID of the actor
actor_ip	Source IP address
action	Action performed
resource_type	Type of resource
resource_id	Resource ID
organization_id	Organization
details	Additional metadata
result	success / failure
reason	Failure reason (optional)


⸻

Example Audit Actions

Action	Description
user_login	User logged in
login_failed	Login failed
device_registered	Device added
event_ingested	Event received
alert_created	Alert generated
alert_updated	Alert modified
alert_escalated	Alert escalated to case
case_created	Case created
evidence_uploaded	Evidence uploaded
evidence_downloaded	Evidence downloaded
rule_updated	Detection rule updated
settings_changed	System settings changed
api_key_created	API key created
permission_denied	Unauthorized action


⸻

Storage Strategy

Audit logs should be stored separately from operational data.

Recommended storage:
	•	Primary Database (recent logs)
	•	Log Storage (S3 / Object Storage)
	•	Immutable Storage / WORM storage
	•	SIEM / Log Analytics system
	•	Cold Archive storage for long-term retention

Log Retention Policy

Log Type	Retention
Authentication logs	1–3 years
Audit logs	3–7 years
Evidence logs	7+ years
System logs	1 year
API logs	1 year

Retention policies depend on legal and organizational requirements.

⸻

Tamper Resistance

Audit logs must be protected from modification.

Recommended methods:
	•	Append-only logging
	•	Write-once storage
	•	Hash chain logging
	•	Digital signatures
	•	Log replication
	•	Off-site backup
	•	Separate audit database
	•	Access control (read-only for most users)

Hash Chain Example

Each audit log stores a hash of the previous log:

hash_n = SHA256(log_n + hash_(n-1))

This makes log tampering detectable.

⸻

Audit Log Access Control

Role	Access
Admin	Full access
Investigator	Read logs
Auditor	Read logs
Operator	Limited logs
User	Own activity only
System	Write only

Only specific roles should be able to export logs.

⸻

Audit Log Query Examples

Find user activity

GET /audit?actor_id=USR-001

Find changes to a device

GET /audit?resource_type=device&resource_id=DEV-001

Find failed logins

GET /audit?action=login_failed

Find evidence access

GET /audit?action=evidence_downloaded


⸻

Audit Logging Flow

System Action Flow:

User / System Action
        ↓
   API / Service
        ↓
  Audit Logger
        ↓
 Audit Log Database
        ↓
 Log Storage / Archive
        ↓
 Investigation / Compliance / Reports


⸻

Summary

The NSD audit logging system ensures that:
	•	all actions are traceable
	•	investigations can reconstruct events
	•	evidence handling is auditable
	•	system changes are recorded
	•	logs are tamper-resistant
	•	logs can be used for legal evidence
	•	compliance requirements can be met
	•	multi-tenant environments remain auditable

The audit logging system is a core security and investigation component of the NSD platform.

⸻
