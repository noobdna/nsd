⸻

NSD – Database Design

Overview

This document describes the database design for NSD (Network Suspicious Detection).

The NSD database is designed to support:
	•	large-scale event ingestion
	•	suspicious activity detection
	•	alert generation and management
	•	investigation workflows
	•	auditability and evidence retention
	•	future multi-tenant expansion

The system stores users, organizations, devices, events, alerts, cases, locations, risk scores, rules, audit logs, evidence files, and incident reports.

The design aims to balance:
	•	operational simplicity
	•	scalability
	•	relational consistency
	•	analytics readiness
	•	security and traceability

This schema is designed to support both a lean MVP and a future production-grade detection platform without major structural redesign.

⸻

Design Goals

1. Scalable Event Storage

NSD may ingest large numbers of telemetry and activity events from:
	•	devices
	•	network logs
	•	sensors
	•	cameras
	•	mobile clients
	•	authentication systems
	•	cloud services
	•	access control systems

The database must support high write throughput and efficient time-based queries.

⸻

2. Clear Investigation Flow

The investigation pipeline should be represented clearly in the data model:

Device / Source → Event → Risk Score → Alert → Case → Incident Report

This pipeline is the core workflow of the NSD system.

⸻

3. Multi-Source Data Support

The schema should support multiple event sources such as:
	•	GPS trackers
	•	cameras
	•	sensors
	•	mobile devices
	•	access logs
	•	network logs
	•	authentication logs
	•	firewall logs
	•	cloud logs
	•	admin activity logs

Because event structures differ by source, the system uses a hybrid relational + JSONB model.

⸻

4. Security and Auditability

The system must:
	•	preserve original event data
	•	maintain audit logs
	•	record user actions
	•	store evidence files
	•	allow incident report generation
	•	support legal or compliance review

⸻

5. Future Expansion

The schema is designed to support future features:
	•	multi-organization deployment
	•	rule engine and detection tuning
	•	ML-based anomaly scoring
	•	notification delivery tracking
	•	evidence file management
	•	incident reporting
	•	workflow management
	•	external integrations
	•	geospatial search with PostGIS

⸻

Database Architecture

Recommended Data Stores

The NSD platform uses multiple storage layers depending on workload type.

⸻

1. PostgreSQL (Primary Database)

Used for structured relational data:
	•	organizations
	•	users
	•	devices
	•	locations
	•	events metadata
	•	risk scores
	•	alerts
	•	cases
	•	alert rules
	•	audit logs
	•	notification history
	•	evidence file references
	•	incident reports

Why PostgreSQL
	•	ACID compliance
	•	strong relational modeling
	•	JSONB support
	•	indexing and partitioning
	•	mature ecosystem
	•	PostGIS support for geospatial features
	•	good analytics capability

⸻

2. Redis

Used for fast temporary and real-time data:
	•	session cache
	•	temporary counters
	•	risk scoring cache
	•	rate limiting
	•	alert suppression windows
	•	geofence temporary state
	•	online device status
	•	sliding window event counters

Redis should not be used as primary storage.

⸻

3. Object Storage

Used for large files and raw data:
	•	raw logs
	•	camera images
	•	device snapshots
	•	attachments
	•	packet capture files
	•	exported evidence
	•	archived data backups
	•	report attachments

Examples:
	•	Amazon S3
	•	Google Cloud Storage
	•	Azure Blob Storage
	•	MinIO
	•	S3-compatible storage

The database stores only file references, not file contents.

⸻

Logical Data Flow

The logical system flow:
	1.	Devices and systems send events
	2.	Events are stored in the Events table
	3.	Detection engine evaluates events
	4.	Risk scores are calculated and stored
	5.	Alerts are generated for suspicious behavior
	6.	Operators investigate alerts as cases
	7.	Evidence files are uploaded and linked to cases
	8.	Audit logs record all actions
	9.	Final findings are stored as incident reports

⸻

Core Entity Relationship Overview

High-level relationship summary:
	•	One Organization → Many Users
	•	One Organization → Many Devices
	•	One Organization → Many Locations
	•	One Device → Many Events
	•	One Event → Many Risk Score Records
	•	One Event → Zero or Many Alerts
	•	One Alert → Zero or One Case (MVP)
	•	One Case → One Incident Report
	•	One Case → Many Evidence Files
	•	One Alert → Many Notifications
	•	One User → Many Audit Logs
	•	One Device → Many Device Groups

Core pipeline:

Organizations
    ├── Users
    ├── Devices → Events → Risk Scores → Alerts → Cases → Incident Reports
    ├── Locations
    ├── Alert Rules
    └── Audit Logs


⸻

Main Tables

1. Organizations

Stores tenant or customer-level ownership of resources.

Column	Type	Description
organization_id	UUID	Primary key
name	VARCHAR(255)	Organization name
organization_type	VARCHAR(100)	company / school / municipal / private / other
status	VARCHAR(50)	active / inactive
created_at	TIMESTAMP	Creation time
updated_at	TIMESTAMP	Last update time


⸻

2. Users

Stores system users such as operators, administrators, analysts, and viewers.

Column	Type	Description
user_id	UUID	Primary key
organization_id	UUID	Owning organization
name	VARCHAR(255)	User name
email	VARCHAR(255)	Email
role	VARCHAR(50)	admin / operator / analyst / viewer
status	VARCHAR(50)	active / disabled
password_hash	VARCHAR(255)	Password hash
last_login_at	TIMESTAMP	Last login
created_at	TIMESTAMP	Creation
updated_at	TIMESTAMP	Update


⸻

3. Devices

Stores registered devices and monitored sources.

Column	Type
device_id	UUID
organization_id	UUID
owner_user_id	UUID
device_name	VARCHAR
device_type	VARCHAR
serial_number	VARCHAR
status	VARCHAR
registered_at	TIMESTAMP
last_seen_at	TIMESTAMP
metadata	JSONB
created_at	TIMESTAMP
updated_at	TIMESTAMP


⸻

4. Device Groups

Logical grouping of devices.

Column	Type
group_id	UUID
organization_id	UUID
name	VARCHAR
description	TEXT
created_at	TIMESTAMP


⸻

5. Device Group Members

Column	Type
group_id	UUID
device_id	UUID
added_at	TIMESTAMP

Composite primary key: (group_id, device_id)

⸻

6. Locations

Stores monitored locations and geofence definitions.

Column	Type
location_id	UUID
organization_id	UUID
name	VARCHAR
location_type	VARCHAR
latitude	DECIMAL
longitude	DECIMAL
geo_fence_radius	INT
metadata	JSONB
created_at	TIMESTAMP
updated_at	TIMESTAMP

Future: PostGIS polygon support.

⸻

7. Events (Central Table)

Stores incoming telemetry, activity records, and system events.

Column	Type
event_id	UUID
organization_id	UUID
device_id	UUID
user_id	UUID
event_type	VARCHAR
event_source	VARCHAR
event_timestamp	TIMESTAMP
received_at	TIMESTAMP
location_lat	DECIMAL
location_lng	DECIMAL
ip_address	VARCHAR
severity_hint	VARCHAR
ingestion_source	VARCHAR
correlation_id	UUID
session_id	VARCHAR
raw_data	JSONB
normalized_data	JSONB
ingestion_id	UUID
created_at	TIMESTAMP

This table will be very large and must be partitioned.

⸻

8. Risk Scores

Stores scoring history for events evaluated by the detection engine.

Column	Type
score_id	UUID
event_id	UUID
score	INT
score_level	VARCHAR
scoring_model	VARCHAR
reason	TEXT
factors	JSONB
calculated_at	TIMESTAMP


⸻

9. Alert Rules

Detection rules used by the detection engine.

Column	Type
rule_id	UUID
organization_id	UUID
name	VARCHAR
rule_type	VARCHAR
description	TEXT
threshold_value	VARCHAR
severity_default	VARCHAR
enabled	BOOLEAN
rule_config	JSONB
created_at	TIMESTAMP
updated_at	TIMESTAMP


⸻

10. Alerts

Column	Type
alert_id	UUID
organization_id	UUID
event_id	UUID
rule_id	UUID
risk_score	INT
alert_level	VARCHAR
title	VARCHAR
description	TEXT
status	VARCHAR
first_seen_at	TIMESTAMP
last_seen_at	TIMESTAMP
created_at	TIMESTAMP
updated_at	TIMESTAMP

Future versions may allow one alert to be linked to multiple events via an alert_events table.

⸻

11. Cases

Column	Type
case_id	UUID
organization_id	UUID
alert_id	UUID
assigned_to	UUID
priority	VARCHAR
status	VARCHAR
summary	VARCHAR
notes	TEXT
resolution	TEXT
opened_at	TIMESTAMP
resolved_at	TIMESTAMP
created_at	TIMESTAMP
updated_at	TIMESTAMP


⸻

12. Notification History

Column	Type
notification_id	UUID
alert_id	UUID
case_id	UUID
channel	VARCHAR
recipient	VARCHAR
delivery_status	VARCHAR
payload	JSONB
sent_at	TIMESTAMP
created_at	TIMESTAMP


⸻

13. Audit Logs

Append-only security and activity logs.

Column	Type
log_id	UUID
organization_id	UUID
user_id	UUID
action	VARCHAR
target_type	VARCHAR
target_id	UUID
details	TEXT
metadata	JSONB
ip_address	VARCHAR
created_at	TIMESTAMP


⸻

14. Evidence Files

Column	Type
evidence_id	UUID
organization_id	UUID
case_id	UUID
alert_id	UUID
file_name	VARCHAR
object_path	VARCHAR
content_type	VARCHAR
file_size	BIGINT
uploaded_by	UUID
created_at	TIMESTAMP


⸻

15. Incident Reports

Column	Type
report_id	UUID
organization_id	UUID
case_id	UUID
title	VARCHAR
summary	TEXT
report_body	TEXT
report_status	VARCHAR
created_by	UUID
created_at	TIMESTAMP
updated_at	TIMESTAMP


⸻

Index Strategy

Indexes are critical because event and audit tables can become very large.

Important Indexes

Events
	•	events(device_id)
	•	events(organization_id)
	•	events(event_timestamp)
	•	events(device_id, event_timestamp)
	•	events(event_type)
	•	events(event_source)
	•	events(ip_address)
	•	events(organization_id, event_timestamp)

Alerts
	•	alerts(status)
	•	alerts(alert_level)
	•	alerts(created_at)
	•	alerts(event_id)

Cases
	•	cases(assigned_to)
	•	cases(status)
	•	cases(priority)

Audit Logs
	•	audit_logs(user_id)
	•	audit_logs(action)
	•	audit_logs(created_at)

⸻

Partitioning Strategy

The Events table must be partitioned.

Recommended Partition Method

Range partitioning by event_timestamp.

Example monthly partitions:

events_2026_01
events_2026_02
events_2026_03

Additional partition candidates:
	•	audit_logs
	•	risk_scores
	•	notification_history

⸻

Data Retention Policy

Data	Recommended Retention
Events	1–3 years
Alerts	5 years
Cases	5–10 years
Audit Logs	5 years
Risk Scores	1–3 years
Notification History	1–3 years
Evidence Files	Case dependent
Raw Logs	Long-term archive

Old event data should be archived to cold storage.

⸻

Security Considerations

Access Control

Use role-based access control:
	•	administrators
	•	operators
	•	analysts
	•	viewers

Sensitive Data

Sensitive data may include:
	•	location data
	•	identity information
	•	IP addresses
	•	evidence files
	•	investigation records

Protect using:
	•	encryption at rest
	•	TLS in transit
	•	least privilege database access
	•	field-level masking if needed

Auditability

All administrative and investigative actions should be logged.

Data Integrity

Alerts, cases, audit logs, and evidence references should be protected from unauthorized modification.

Backup and Recovery

Use scheduled PostgreSQL backups and object storage lifecycle management.

⸻

Recommended First Release Scope (MVP)

Required for MVP
	•	organizations
	•	users
	•	devices
	•	events
	•	alerts
	•	cases
	•	audit_logs

Recommended but Optional
	•	locations
	•	risk_scores
	•	alert_rules
	•	notification_history
	•	evidence_files
	•	incident_reports

This allows fast development while preserving future scalability.

⸻

ER Model Summary

The core relational flow of the NSD database is centered around the event investigation pipeline:

Organizations → Users → Devices → Events → Risk Scores → Alerts → Cases → Incident Reports

Relationship overview:
	•	organizations → users
	•	organizations → devices
	•	organizations → locations
	•	devices → events
	•	events → risk_scores
	•	events → alerts
	•	alerts → cases
	•	cases → evidence_files
	•	cases → incident_reports
	•	users → audit_logs
	•	alerts → notification_history

Future extension may include:
	•	alert_events (many events per alert)
	•	case_comments
	•	workflow_states
	•	watchlists
	•	model_registry

⸻

Event Data Modeling Strategy

Because NSD handles many different event types from multiple sources, the event table uses a hybrid schema approach.

Structured Columns

Common searchable fields are stored as structured columns:
	•	event_id
	•	device_id
	•	user_id
	•	event_type
	•	event_timestamp
	•	location
	•	ip_address
	•	severity_hint

Flexible JSONB Fields

Source-specific or variable data is stored in JSONB:
	•	raw_data
	•	normalized_data
	•	vendor-specific fields
	•	enriched data
	•	detection metadata

Benefits
	•	supports many event sources
	•	allows schema evolution without frequent migrations
	•	preserves original evidence
	•	supports structured querying
	•	supports analytics and ML pipelines

⸻

Constraints and Foreign Keys

To maintain data integrity, the following foreign key relationships are recommended:

Foreign Key Relationships:

- users.organization_id → organizations.organization_id
- devices.organization_id → organizations.organization_id
- devices.owner_user_id → users.user_id
- device_groups.organization_id → organizations.organization_id
- device_group_members.group_id → device_groups.group_id
- device_group_members.device_id → devices.device_id
- locations.organization_id → organizations.organization_id
- events.organization_id → organizations.organization_id
- events.device_id → devices.device_id
- events.user_id → users.user_id
- risk_scores.event_id → events.event_id
- alerts.organization_id → organizations.organization_id
- alerts.event_id → events.event_id
- alerts.rule_id → alert_rules.rule_id
- cases.organization_id → organizations.organization_id
- cases.alert_id → alerts.alert_id
- cases.assigned_to → users.user_id
- audit_logs.organization_id → organizations.organization_id
- audit_logs.user_id → users.user_id
- evidence_files.case_id → cases.case_id
- evidence_files.alert_id → alerts.alert_id
- incident_reports.case_id → cases.case_id

Recommended Constraints:

- UUID primary keys for all major tables
- NOT NULL for required foreign keys
- Append-only behavior for audit_logs
- Soft delete recommended for users, devices, alerts, and cases
- Unique constraint on users.email per organization
- Composite primary key for device_group_members
- Index foreign keys for performance


These constraints help maintain referential integrity and ensure reliable investigation data.

⸻

Conclusion

The NSD database design is centered around a scalable investigation pipeline:

Organizations → Users / Devices / Locations → Events → Risk Scores → Alerts → Cases → Incident Reports

This design supports:
	•	suspicious behavior detection
	•	device monitoring
	•	alert management
	•	operator investigations
	•	evidence preservation
	•	audit logging
	•	incident reporting
	•	future multi-tenant deployment
	•	analytics and machine learning integration

The schema is intentionally structured to remain simple enough for an MVP, while still supporting future growth into a production-grade suspicious detection platform.

⸻
