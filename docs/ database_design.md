⸻

NSD – Database Design (Restructured Version)

1. Overview

This document defines the database design for NSD (Network Suspicious Detection).

The NSD database is designed to support:
	•	large-scale event ingestion
	•	suspicious activity detection
	•	alert generation and management
	•	investigation workflows
	•	auditability and evidence retention
	•	incident reporting
	•	future multi-tenant expansion

The system stores organizations, users, devices, locations, events, risk scores, alert rules, alerts, cases, evidence files, audit logs, notification history, and incident reports.

The design aims to balance:
	•	operational simplicity
	•	scalability
	•	relational consistency
	•	analytics readiness
	•	security and traceability

This schema is intended to support both an MVP implementation and a future production-grade detection platform without major structural redesign.

⸻

2. Design Goals

2.1 Scalable Event Storage

NSD may ingest large volumes of telemetry and activity events from:
	•	devices
	•	network logs
	•	sensors
	•	cameras
	•	mobile clients
	•	authentication systems
	•	cloud services
	•	access control systems

The database must support high write throughput, efficient time-based queries, and long-term archival.

2.2 Clear Investigation Flow

The core NSD workflow should be represented clearly in the data model:

Device / Source → Event → Risk Score → Alert → Case → Incident Report

This investigation pipeline is the center of the platform design.

2.3 Multi-Source Data Support

NSD must support heterogeneous event sources such as:
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

Because source data structures vary significantly, the schema uses a hybrid relational + JSONB model.

2.4 Security and Auditability

The database must support:
	•	preservation of original event data
	•	tracking of user and system actions
	•	append-only audit logging
	•	evidence file linkage
	•	incident report generation
	•	compliance and legal review support

2.5 Future Expansion

The schema is designed to support future capabilities such as:
	•	multi-organization deployment
	•	rule engine enhancements
	•	ML-based anomaly scoring
	•	notification delivery tracking
	•	advanced evidence management
	•	workflow orchestration
	•	external integrations
	•	geospatial search with PostGIS

⸻

3. Database Architecture

NSD uses multiple storage layers based on workload type.

3.1 PostgreSQL (Primary Database)

PostgreSQL is the primary system of record for structured and relational data, including:
	•	organizations
	•	users
	•	devices
	•	locations
	•	event metadata
	•	risk scores
	•	alert rules
	•	alerts
	•	cases
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
	•	PostGIS support
	•	strong analytics compatibility

3.2 Redis

Redis is used for real-time and temporary operational data, such as:
	•	session cache
	•	temporary counters
	•	risk score cache
	•	rate limiting
	•	alert suppression windows
	•	geofence temporary state
	•	online device status
	•	sliding window event counters

Redis is not a primary storage system.

3.3 Object Storage

Object storage is used for large files and raw artifacts, including:
	•	raw logs
	•	camera images
	•	device snapshots
	•	attachments
	•	packet capture files
	•	exported evidence
	•	archived backups
	•	report attachments

Examples:
	•	Amazon S3
	•	Google Cloud Storage
	•	Azure Blob Storage
	•	MinIO
	•	S3-compatible storage

The database stores only references and metadata, not file contents.

⸻

4. Logical Data Flow

The logical processing flow in NSD is:
	1.	Devices and systems send events.
	2.	Events are stored in the events table.
	3.	The detection engine evaluates incoming events.
	4.	Risk scores are calculated and stored.
	5.	Alerts are generated for suspicious behavior.
	6.	Operators review alerts and escalate them into cases.
	7.	Evidence files are uploaded and linked to cases or alerts.
	8.	Audit logs record all important actions.
	9.	Final findings are stored as incident reports.

⸻

5. Core Entity Relationship Overview

5.1 High-Level Relationship Summary
	•	One organization has many users
	•	One organization has many devices
	•	One organization has many locations
	•	One device has many events
	•	One event has many risk score records
	•	One event may generate zero or many alerts
	•	One alert may create zero or one case in the MVP
	•	One case may have one incident report
	•	One case may have many evidence files
	•	One alert may trigger many notifications
	•	One user may generate many audit logs
	•	One device may belong to many device groups

5.2 Core Pipeline

Organizations
    ├── Users
    ├── Devices → Events → Risk Scores → Alerts → Cases → Incident Reports
    ├── Locations
    ├── Alert Rules
    └── Audit Logs


⸻

6. Multi-Tenant Strategy

NSD is designed to be multi-tenant ready.

6.1 Tenant Boundary

organization_id is the primary tenant boundary for major business tables.

6.2 Tenant-Aware Tables

The following tables should include organization_id:
	•	users
	•	devices
	•	device_groups
	•	locations
	•	events
	•	alert_rules
	•	alerts
	•	cases
	•	audit_logs
	•	evidence_files
	•	incident_reports

6.3 Design Principles
	•	all application queries should filter by organization_id
	•	indexes should include organization_id where appropriate
	•	cross-organization access should not be allowed by default
	•	future row-level security may be added if needed
	•	future database-per-tenant deployment should remain possible

⸻

7. Main Tables

7.1 Organizations

Stores tenant or customer ownership.

Column	Type	Description
organization_id	UUID	Primary key
name	VARCHAR(255)	Organization name
organization_type	VARCHAR(100)	company / school / municipal / private / other
status	VARCHAR(50)	active / inactive
created_at	TIMESTAMP	Creation time
updated_at	TIMESTAMP	Last update time

7.2 Users

Stores platform users such as administrators, operators, analysts, and viewers.

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

7.3 Devices

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

7.4 Device Groups

Logical grouping of devices.

Column	Type
group_id	UUID
organization_id	UUID
name	VARCHAR
description	TEXT
created_at	TIMESTAMP

7.5 Device Group Members

Column	Type
group_id	UUID
device_id	UUID
added_at	TIMESTAMP

Composite primary key: (group_id, device_id)

7.6 Locations

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

Future extension: PostGIS polygon support.

7.7 Events

The central event ingestion table.

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

This table will grow very large and should be partitioned.

7.8 Risk Scores

Stores scoring history for evaluated events.

Column	Type
score_id	UUID
event_id	UUID
score	INT
score_level	VARCHAR
scoring_model	VARCHAR
reason	TEXT
factors	JSONB
calculated_at	TIMESTAMP

7.9 Alert Rules

Stores detection rules used by the detection engine.

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

7.10 Alerts

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

Future versions may support many-to-many mapping through an alert_events table.

7.11 Cases

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

7.12 Notification History

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

7.13 Audit Logs

Append-only security and activity records.

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

7.14 Evidence Files

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

7.15 Incident Reports

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

8. Event Data Modeling Strategy

NSD handles many event types from many source systems.
For that reason, the events table uses a hybrid modeling strategy.

8.1 Structured Columns

Common searchable fields are stored in relational columns:
	•	event_id
	•	organization_id
	•	device_id
	•	user_id
	•	event_type
	•	event_source
	•	event_timestamp
	•	location
	•	ip_address
	•	severity_hint

8.2 Flexible JSONB Fields

Source-specific and variable data is stored in JSONB:
	•	raw_data
	•	normalized_data
	•	vendor-specific fields
	•	enriched data
	•	detection metadata

8.3 Benefits
	•	supports many event sources
	•	preserves original evidence
	•	avoids frequent schema migrations
	•	supports structured filtering
	•	supports analytics and ML enrichment

⸻

9. Constraints and Foreign Keys

To preserve referential integrity, the following relationships are recommended.

9.1 Foreign Key Relationships
	•	users.organization_id → organizations.organization_id
	•	devices.organization_id → organizations.organization_id
	•	devices.owner_user_id → users.user_id
	•	device_groups.organization_id → organizations.organization_id
	•	device_group_members.group_id → device_groups.group_id
	•	device_group_members.device_id → devices.device_id
	•	locations.organization_id → organizations.organization_id
	•	events.organization_id → organizations.organization_id
	•	events.device_id → devices.device_id
	•	events.user_id → users.user_id
	•	risk_scores.event_id → events.event_id
	•	alerts.organization_id → organizations.organization_id
	•	alerts.event_id → events.event_id
	•	alerts.rule_id → alert_rules.rule_id
	•	cases.organization_id → organizations.organization_id
	•	cases.alert_id → alerts.alert_id
	•	cases.assigned_to → users.user_id
	•	audit_logs.organization_id → organizations.organization_id
	•	audit_logs.user_id → users.user_id
	•	evidence_files.case_id → cases.case_id
	•	evidence_files.alert_id → alerts.alert_id
	•	incident_reports.case_id → cases.case_id

9.2 Recommended Constraints
	•	UUID primary keys for all major tables
	•	NOT NULL on required foreign keys
	•	append-only behavior for audit_logs
	•	unique constraint on users.email per organization
	•	composite primary key on device_group_members
	•	foreign key columns indexed for performance

⸻

10. Index Strategy

Indexes are critical because event and audit data can become very large.

10.1 Important Indexes for Events
	•	events(device_id)
	•	events(organization_id)
	•	events(event_timestamp)
	•	events(device_id, event_timestamp)
	•	events(event_type)
	•	events(event_source)
	•	events(ip_address)
	•	events(organization_id, event_timestamp)

10.2 Important Indexes for Alerts
	•	alerts(status)
	•	alerts(alert_level)
	•	alerts(created_at)
	•	alerts(event_id)

10.3 Important Indexes for Cases
	•	cases(assigned_to)
	•	cases(status)
	•	cases(priority)

10.4 Important Indexes for Audit Logs
	•	audit_logs(user_id)
	•	audit_logs(action)
	•	audit_logs(created_at)

⸻

11. Partitioning Strategy

The events table should be partitioned from the beginning or introduced very early.

11.1 Recommended Method

Use range partitioning by event_timestamp.

11.2 Example Monthly Partitions
	•	events_2026_01
	•	events_2026_02
	•	events_2026_03

11.3 Additional Future Candidates

These tables may also require partitioning depending on scale:
	•	audit_logs
	•	risk_scores
	•	notification_history

11.4 Operational Note

Retention, archival, and pruning become much easier when time-based partitions are used.

⸻

12. Data Lifecycle and Retention

12.1 Retention Policy

Data	Recommended Retention
Events	1–3 years
Alerts	5 years
Cases	5–10 years
Audit Logs	5 years
Risk Scores	1–3 years
Notification History	1–3 years
Evidence Files	Case dependent
Raw Logs	Long-term archive

12.2 Lifecycle Stages

Hot Data
Recent operational data stored in PostgreSQL partitions and used for active detection and investigation.

Warm Data
Older but still queryable data retained in PostgreSQL or an analytics warehouse.

Cold Data
Archived data moved to object storage or other long-term storage systems.

Evidence Files
Stored in object storage with lifecycle policies and integrity preservation.

⸻

13. Security Considerations

13.1 Access Control

Use role-based access control:
	•	administrators
	•	operators
	•	analysts
	•	viewers

13.2 Sensitive Data

Sensitive data may include:
	•	location data
	•	user identity information
	•	IP addresses
	•	evidence files
	•	investigation records

Recommended protections:
	•	encryption at rest
	•	TLS in transit
	•	least-privilege database access
	•	masking or redaction where needed
	•	controlled access to evidence artifacts

13.3 Auditability

Administrative and investigative actions should be logged consistently.

13.4 Data Integrity

Alerts, cases, audit logs, and evidence references should be protected from unauthorized modification.

13.5 Backup and Recovery

Use scheduled PostgreSQL backups, tested restore procedures, and object storage lifecycle controls.

⸻

14. Soft Delete Strategy

Soft delete is recommended for operational tables where historical traceability matters.

14.1 Candidate Tables
	•	users
	•	devices
	•	alerts
	•	cases

14.2 Recommended Columns
	•	deleted_at TIMESTAMP
	•	deleted_by UUID

Soft delete helps preserve operational history while preventing accidental data loss.

⸻

15. Naming Convention

To keep the schema consistent, use the following conventions.

15.1 Primary Keys

Use:
	•	organization_id
	•	user_id
	•	device_id
	•	event_id

15.2 Foreign Keys

Use the referenced entity name plus _id.

Examples:
	•	organization_id
	•	device_id
	•	alert_id
	•	case_id

15.3 Timestamps

Standard timestamp fields:
	•	created_at
	•	updated_at
	•	deleted_at
	•	opened_at
	•	resolved_at

15.4 Status and Boolean Fields

Use descriptive names such as:
	•	status
	•	enabled
	•	is_active
	•	delivery_status

⸻

16. ID Strategy

All major primary keys should use UUID.

Reasons
	•	suitable for distributed systems
	•	avoids sequential ID exposure
	•	supports multi-region or offline generation
	•	simplifies future data migration and merges

ULID may also be considered in future if sortable identifiers are needed.

⸻

17. Recommended First Release Scope (MVP)

17.1 Required for MVP
	•	organizations
	•	users
	•	devices
	•	events
	•	alerts
	•	cases
	•	audit_logs

17.2 Recommended but Optional for Early Phase
	•	locations
	•	risk_scores
	•	alert_rules
	•	notification_history
	•	evidence_files
	•	incident_reports

This scope allows rapid implementation while preserving future scalability.

⸻

18. ER Model Summary

The core relational flow of the NSD database is:

Organizations → Users / Devices / Locations → Events → Risk Scores → Alerts → Cases → Incident Reports

Relationship Overview
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

Future Extensions

Possible future tables include:
	•	alert_events
	•	case_comments
	•	workflow_states
	•	watchlists
	•	model_registry

⸻

19. Conclusion

The NSD database design is centered around a scalable investigation pipeline:

Organizations → Users / Devices / Locations → Events → Risk Scores → Alerts → Cases → Incident Reports

This design supports:
	•	suspicious behavior detection
	•	device and source monitoring
	•	alert management
	•	operator investigations
	•	evidence preservation
	•	audit logging
	•	incident reporting
	•	multi-tenant expansion
	•	analytics and machine learning integration

The schema is intentionally designed to remain simple enough for an MVP while still supporting future expansion into a production-grade suspicious detection platform.

⸻
