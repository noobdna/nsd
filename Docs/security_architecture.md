⸻

NSD – Security Architecture

Overview

This document describes the security architecture of the NSD (Network Suspicious Detection) system.

The NSD system handles sensitive data such as:
	•	device telemetry
	•	network logs
	•	location data
	•	user activity
	•	investigation data
	•	evidence files
	•	incident reports

Therefore, security is a core component of the system architecture, not an add-on feature.

The security model is based on:
	•	Zero Trust Architecture
	•	Least Privilege Access
	•	Strong Authentication
	•	End-to-End Encryption
	•	Full Audit Logging
	•	Evidence Integrity Protection

⸻

Security Principles

1. Zero Trust Architecture

NSD follows a Zero Trust model.

Principles:
	•	Never trust internal network
	•	Always verify identity
	•	Always verify device
	•	Always log access
	•	Limit access by role and organization
	•	Assume breach and design for containment

All services must require authentication and authorization.

⸻

2. Least Privilege Access

Users and systems only receive the minimum permissions required.

Examples:
	•	Viewer → read only
	•	Investigator → alerts, cases, evidence
	•	Admin → system configuration
	•	Device → event upload only
	•	API service → specific scoped access

Role-Based Access Control (RBAC) is enforced across the system.

⸻

3. Defense in Depth

Security is implemented in multiple layers:

Layer	Security Control
Network	Firewall, private network
Edge	WAF, Access control
Application	Authentication, RBAC
API	Token validation, rate limit
Database	Encryption, access control
Storage	Evidence encryption
Logging	Audit logs
Monitoring	Intrusion detection
Backup	Encrypted backups


⸻

Authentication Architecture

Authentication Methods

Different clients use different authentication methods.

Client	Authentication
Web Dashboard	JWT
Mobile App	JWT
IoT Devices	API Key
Backend Services	Service Token
External Integration	API Key / OAuth
Admin	JWT + MFA
Internal Services	mTLS


⸻

Authentication Flow (User)
	1.	User logs in
	2.	API validates credentials
	3.	System generates JWT token
	4.	Token includes:
	•	user_id
	•	role
	•	organization_id
	•	permissions
	•	expiration
	5.	Client sends JWT in Authorization header
	6.	API validates token for every request

⸻

Authorization Model (RBAC)

Roles

Role	Permissions
Viewer	Read dashboards, alerts
Operator	Manage alerts
Investigator	Manage cases & evidence
Admin	System configuration
Super Admin	Multi-tenant administration
Device	Upload events only
Service	Internal system communication

Access control is enforced at:
	•	API layer
	•	Backend services
	•	Database queries
	•	Storage access

⸻

Encryption Architecture

Encryption in Transit

All communications must use TLS.

Examples:
	•	HTTPS
	•	Secure WebSocket
	•	TLS device communication
	•	VPN / Private network
	•	mTLS between services

Encryption at Rest

Sensitive data must be encrypted:
	•	Database encryption
	•	Disk encryption
	•	Evidence file storage encryption
	•	Backup encryption
	•	Key management system (KMS)

Sensitive fields:
	•	passwords (hashed)
	•	API keys
	•	tokens
	•	location history
	•	evidence files
	•	incident reports
	•	personal data

⸻

Audit Logging & Traceability

All critical actions must be logged.

Audit Log Events

Examples:
	•	login
	•	logout
	•	failed login
	•	permission change
	•	role change
	•	device registration
	•	device deactivation
	•	alert creation
	•	case creation
	•	evidence upload
	•	evidence download
	•	report generation
	•	system configuration change
	•	API key creation
	•	API key revocation

Audit log fields:
	•	timestamp
	•	user_id
	•	organization_id
	•	action
	•	resource_type
	•	resource_id
	•	IP address
	•	user agent
	•	result (success / failure)

Audit logs must be:
	•	immutable
	•	tamper-evident
	•	retained long term

⸻

Evidence Integrity Protection

Evidence files must be protected against tampering.

Evidence Security Measures
	•	Hash file on upload (SHA-256)
	•	Store hash in database
	•	Verify hash on download
	•	Timestamp evidence
	•	Record uploader
	•	Record chain of custody
	•	Immutable storage (WORM / object lock)
	•	Version history
	•	Access logging

This ensures forensic integrity.

⸻

Network Security Architecture

Network Segmentation

System components should be separated:

Network	Components
Public	API Gateway
Application	Backend services
Processing	Detection engine
Database	Database servers
Storage	Evidence storage
Management	Admin tools
Logging	Log storage
Monitoring	Monitoring system

Only necessary ports are opened between networks.

⸻

Security Monitoring

The system itself must be monitored.

Monitoring Targets
	•	login failures
	•	unusual access times
	•	abnormal API usage
	•	large data exports
	•	repeated evidence downloads
	•	permission changes
	•	admin activity
	•	device anomalies
	•	system errors
	•	intrusion attempts

Alerts should be generated for suspicious behavior.

⸻

Backup & Disaster Recovery Security

Backups must be:
	•	encrypted
	•	access controlled
	•	immutable
	•	regularly tested
	•	stored in separate environment

Backup data includes:
	•	database
	•	evidence storage
	•	audit logs
	•	configuration
	•	rules
	•	reports

⸻

Security Incident Response

When a security incident occurs:
	1.	Detect incident
	2.	Generate alert
	3.	Open investigation case
	4.	Preserve logs and evidence
	5.	Restrict affected accounts/devices
	6.	Investigate timeline
	7.	Generate incident report
	8.	Apply remediation
	9.	Review security controls
	10.	Update detection rules

⸻

Summary

The NSD security architecture is built on:
	•	Zero Trust Architecture
	•	Least Privilege Access
	•	RBAC Authorization
	•	Strong Authentication (JWT, API Keys, mTLS)
	•	Encryption in Transit and at Rest
	•	Full Audit Logging
	•	Evidence Integrity Protection
	•	Network Segmentation
	•	Continuous Monitoring
	•	Secure Backup & Disaster Recovery
	•	Incident Response Procedures

Security is integrated into every layer of the NSD architecture.

⸻
