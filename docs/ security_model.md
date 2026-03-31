⸻

NSD – Security Model

Overview

This document describes the security model for the NSD (Network Suspicious Detection) system.

The NSD platform processes sensitive operational data including:
	•	device activity
	•	location data
	•	user accounts
	•	alerts
	•	investigation cases
	•	evidence files
	•	audit logs
	•	incident reports

Because the system handles security-related data and potential evidence, the platform must be designed with strong security controls, auditability, and data integrity protections.

The security model is based on the following principles:
	•	Zero Trust
	•	Least Privilege
	•	Defense in Depth
	•	Full Auditability
	•	Evidence Integrity
	•	Secure by Default
	•	Multi-tenant Isolation
	•	Compliance Ready Design

⸻

Security Principles

1. Zero Trust Architecture

NSD follows a Zero Trust model:
	•	No implicit trust between services
	•	Every API request must be authenticated
	•	Every action must be authorized
	•	Internal services must authenticate as well
	•	Device ingestion endpoints must use API keys or certificates
	•	Admin operations require MFA
	•	Service-to-service communication should use mTLS or service tokens

Rule:

Trust nothing, verify everything.

⸻

2. Least Privilege

Users and systems should only have the minimum permissions required.

Examples:

Role	Permissions
Viewer	View alerts and dashboards
Analyst	Review alerts, create cases
Investigator	Manage cases, evidence
Admin	Manage users, rules, system
System	Event ingestion, risk scoring
Auditor	Read-only access to audit logs

No role should have unnecessary write or admin privileges.

⸻

3. Defense in Depth

Security should be implemented in multiple layers:

Layer	Security Controls
Network	Firewall, Zero Trust Access
API	Authentication, Authorization
Application	RBAC, Validation
Database	Encryption, Access Control
Storage	Evidence integrity, Hashing
Logging	Audit logs
Monitoring	Alerting, anomaly detection
Infrastructure	IAM, Security groups
Backup	Encrypted backups
CI/CD	Signed deployments

If one layer fails, other layers still protect the system.

⸻

Authentication Model

Authentication Methods

Client Type	Authentication Method
Web Dashboard	JWT
Mobile App	JWT
IoT Devices	API Key
Backend Services	Service Token
External Integrations	API Key / OAuth
Admin	JWT + MFA
Internal Services	mTLS / Service Token


⸻

Authorization Model (RBAC)

NSD uses Role-Based Access Control (RBAC).

Roles

Role	Description
Viewer	Read-only access
Analyst	Alert review
Investigator	Case & evidence management
Admin	System management
Auditor	Audit logs access
System	Automated services

Permission Categories

Resource	Actions
Devices	read, write
Events	read
Alerts	read, update
Cases	read, write
Evidence	upload, read
Reports	read, generate
Users	manage
Rules	manage
Audit Logs	read
System Settings	manage


⸻

Data Protection

Encryption

Data	Encryption
API traffic	HTTPS / TLS
Database	Encryption at rest
Evidence files	Encrypted storage
Backups	Encrypted
Logs	Encrypted storage
Secrets	Secret manager

Sensitive Data

Sensitive data includes:
	•	passwords (hashed)
	•	API keys
	•	service tokens
	•	location history
	•	investigation evidence
	•	incident reports
	•	personal information

Passwords must be stored using:
	•	bcrypt
	•	argon2

Never store plaintext passwords.

⸻

Audit Logging

All important actions must be logged.

Audit Log Events

Event	Logged
Login	Yes
Failed login	Yes
User creation	Yes
Permission changes	Yes
Alert status change	Yes
Case creation	Yes
Evidence upload	Yes
Evidence download	Yes
Rule change	Yes
Device registration	Yes
Admin actions	Yes
System configuration	Yes

Audit logs must be:
	•	immutable
	•	timestamped
	•	user linked
	•	stored securely
	•	retained long-term

⸻

Evidence Integrity

Evidence files must be protected against tampering.

Evidence Protection

For each evidence file:
	•	Generate SHA-256 hash
	•	Store hash in database
	•	Store file in secure storage
	•	Log upload/download access
	•	Evidence should be immutable
	•	Versioning should be enabled

Evidence chain of custody should be trackable.

⸻

Multi-Tenant Security

Future NSD versions may support multiple organizations.

Isolation must be enforced by:
	•	organization_id on all records
	•	tenant-aware queries
	•	tenant-aware RBAC
	•	tenant-aware API authorization
	•	separate storage buckets (optional)
	•	separate encryption keys (optional)

No tenant should be able to access another tenant’s data.

⸻

Infrastructure Security

Infrastructure Controls

Area	Security
Cloud	IAM roles
Network	Private subnets
Access	Zero Trust
Secrets	Secret Manager
Containers	Image scanning
CI/CD	Signed builds
Monitoring	Security alerts
Backup	Automated encrypted backups


⸻

Security Monitoring

NSD should monitor:
	•	failed logins
	•	unusual API usage
	•	abnormal event ingestion
	•	alert spikes
	•	privilege escalation
	•	large evidence downloads
	•	suspicious admin actions
	•	API key misuse
	•	service token misuse

Security events should generate alerts.

⸻

Security Checklist

Application Security
	•	Authentication required
	•	Authorization checks
	•	Input validation
	•	Rate limiting
	•	Audit logs
	•	Secure file uploads
	•	Error handling without data leakage

Infrastructure Security
	•	TLS everywhere
	•	IAM roles
	•	Private networks
	•	Encrypted storage
	•	Backup
	•	Monitoring
	•	Logging
	•	Patch management

Operations Security
	•	MFA for admins
	•	Key rotation
	•	Backup testing
	•	Incident response plan
	•	Access review
	•	Log review

⸻

Summary

The NSD security model is built on:
	•	Zero Trust
	•	RBAC
	•	Encryption
	•	Audit logging
	•	Evidence integrity
	•	Multi-tenant isolation
	•	Defense in Depth
	•	Secure infrastructure
	•	Monitoring and alerting

The system must be designed so that:
	•	all actions are traceable
	•	all access is controlled
	•	evidence is protected
	•	data is encrypted
	•	tenants are isolated
	•	administrators are accountable
	•	incidents can be investigated
	•	the system is secure by default

⸻
