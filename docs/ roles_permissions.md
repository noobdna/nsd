⸻

NSD – Roles & Permissions

Overview

This document defines the role-based access control (RBAC) model for the NSD (Network Suspicious Detection) system.

The purpose of the roles and permissions system is to:
	•	control access to system resources
	•	protect sensitive investigation data
	•	separate operational responsibilities
	•	support multi-organization environments
	•	ensure auditability and accountability
	•	enable future enterprise deployment

The system uses Role-Based Access Control (RBAC) with optional fine-grained permissions.

⸻

Access Control Model

NSD uses the following access control hierarchy:

User
  ↓
Role
  ↓
Permissions
  ↓
Resources (API / Data / Actions)

Access decisions are based on:
	•	user role
	•	organization membership
	•	resource ownership
	•	permission rules
	•	system policies

⸻

Default Roles

The NSD system defines several default roles.

1. Super Admin

Full system access across all organizations.

Permissions include:
	•	manage organizations
	•	manage users
	•	manage roles
	•	manage system rules
	•	view all alerts and cases
	•	access audit logs
	•	system configuration
	•	database exports
	•	evidence access
	•	delete data
	•	manage API keys
	•	manage integrations

This role should be restricted to very few users.

⸻

2. Organization Admin

Administrator for a specific organization.

Permissions include:
	•	manage organization users
	•	assign roles
	•	register devices
	•	view all organization alerts
	•	manage cases
	•	upload and access evidence
	•	generate reports
	•	configure organization rules
	•	manage locations
	•	view audit logs (organization scope)

Cannot access other organizations.

⸻

3. Security Analyst

Primary investigation and monitoring role.

Permissions include:
	•	view events
	•	view alerts
	•	update alert status
	•	assign alerts
	•	escalate alerts to cases
	•	create and update cases
	•	add investigation notes
	•	upload evidence
	•	view evidence
	•	generate reports
	•	risk score review
	•	dashboard access

Cannot manage users or system settings.

⸻

4. Operator / Monitoring Operator

Operational monitoring role.

Permissions include:
	•	dashboard access
	•	view alerts
	•	acknowledge alerts
	•	assign alerts
	•	basic event search
	•	device status monitoring
	•	alert comments

Cannot create cases or access evidence deletion.

⸻

5. Investigator

Investigation-focused role with evidence handling.

Permissions include:
	•	view alerts
	•	create cases
	•	manage cases
	•	upload evidence
	•	view evidence
	•	add notes
	•	generate reports
	•	link alerts to cases
	•	timeline analysis

⸻

6. Viewer / Auditor

Read-only role.

Permissions include:
	•	view dashboard
	•	view alerts
	•	view cases
	•	view reports
	•	view audit logs
	•	export reports

Cannot modify anything.

⸻

Permission Categories

Permissions are grouped by system modules.

User Management
	•	user.create
	•	user.read
	•	user.update
	•	user.delete
	•	user.assign_role

Organization Management
	•	org.create
	•	org.read
	•	org.update
	•	org.delete

Device Management
	•	device.create
	•	device.read
	•	device.update
	•	device.delete
	•	device.assign_location
	•	device.assign_owner

Events
	•	event.read
	•	event.search
	•	event.export

Risk Scoring
	•	risk.read
	•	risk.rules.manage

Alerts
	•	alert.create
	•	alert.read
	•	alert.update
	•	alert.assign
	•	alert.acknowledge
	•	alert.escalate
	•	alert.close

Cases
	•	case.create
	•	case.read
	•	case.update
	•	case.assign
	•	case.close

Evidence
	•	evidence.upload
	•	evidence.read
	•	evidence.delete

Reports
	•	report.generate
	•	report.read
	•	report.export

Audit Logs
	•	audit.read
	•	audit.export

System Administration
	•	system.settings
	•	system.rules
	•	system.integrations
	•	system.api_keys

⸻

Role Permission Matrix

Permission	Super Admin	Org Admin	Analyst	Operator	Investigator	Viewer
Manage Users	✔	✔				
Manage Roles	✔	✔				
Register Devices	✔	✔	✔			
View Events	✔	✔	✔	✔	✔	✔
Manage Alerts	✔	✔	✔	✔	✔	
Escalate Alerts	✔	✔	✔		✔	
Manage Cases	✔	✔	✔		✔	
Upload Evidence	✔	✔	✔		✔	
Delete Evidence	✔	✔				
Generate Reports	✔	✔	✔		✔	✔
View Audit Logs	✔	✔				✔
System Settings	✔					


⸻

Multi-Organization Access Rules

The system must enforce organization boundaries.

Rules:
	•	Users belong to one or more organizations
	•	Users can only access:
	•	devices
	•	events
	•	alerts
	•	cases
	•	evidence
	•	reports
within their organization
	•	Super Admin can access all organizations
	•	Evidence access must be logged
	•	Case access must be logged
	•	Report exports must be logged

⸻

Permission Enforcement Points

Permissions must be enforced at multiple layers:

1. API Layer

Every API endpoint must check:
	•	authentication
	•	role
	•	permission
	•	organization scope

2. Database Layer

Row-level access control may be used for:
	•	events
	•	alerts
	•	cases
	•	evidence
	•	audit logs

3. Frontend Dashboard

UI should hide:
	•	unauthorized buttons
	•	unauthorized data
	•	admin features
	•	evidence deletion
	•	system settings

⸻

Audit Requirements

All permission-related actions must be logged:
	•	login
	•	logout
	•	role change
	•	permission change
	•	evidence access
	•	evidence deletion
	•	case closure
	•	report export
	•	API key creation
	•	system rule changes

Audit Log Example:

timestamp
user_id
organization_id
action
resource_type
resource_id
old_value
new_value
ip_address
user_agent


⸻

Future Extensions

Future access control improvements may include:
	•	Attribute-Based Access Control (ABAC)
	•	time-based permissions
	•	location-based access restrictions
	•	device trust level
	•	case-level access control
	•	evidence classification levels
	•	legal hold permissions
	•	external auditor temporary access
	•	API token scoped permissions

⸻

Summary

The NSD roles and permissions model:
	•	uses RBAC
	•	supports multi-organization environments
	•	protects investigation data and evidence
	•	separates monitoring and investigation roles
	•	enforces least privilege principle
	•	logs all sensitive actions
	•	is designed for future enterprise expansion

⸻
