# NSD – Database Design

## Overview

This document describes the database design for **NSD (Network Suspicious Detection)**.

The NSD database is designed to support:

- large-scale event ingestion
- suspicious activity detection
- alert generation and management
- investigation workflows
- auditability and evidence retention
- future multi-tenant expansion

The system stores users, organizations, devices, events, alerts, cases, locations, risk scores, rules, and audit logs.

The design aims to balance:

- operational simplicity
- scalability
- relational consistency
- analytics readiness
- security and traceability

---

## Design Goals

The database design is based on the following goals:

### 1. Scalable Event Storage
NSD may ingest large numbers of telemetry and activity events from devices, network logs, sensors, cameras, mobile clients, and cloud systems.

### 2. Clear Investigation Flow
The investigation pipeline should be represented clearly in the data model:

**Device / Source → Event → Risk Score → Alert → Case**

### 3. Multi-Source Data Support
The schema should support multiple event sources such as:

- GPS trackers
- cameras
- sensors
- mobile devices
- access logs
- network logs
- authentication logs
- cloud logs

### 4. Security and Auditability
The system should preserve evidence, maintain audit logs, and support review of user actions and system decisions.

### 5. Future Expansion
The schema should be extensible for:

- multi-organization support
- alert rule management
- notification history
- ML-based scoring
- evidence file management
- incident reporting

---

## Database Architecture

### Recommended Data Stores

The NSD platform uses multiple storage layers depending on workload type.

#### 1. PostgreSQL
Primary relational database for structured data.

Used for:

- users
- organizations
- devices
- events metadata
- alerts
- cases
- rules
- audit logs
- risk score history

Why PostgreSQL:

- strong ACID guarantees
- excellent relational modeling
- JSONB support for flexible event fields
- indexing and partitioning support
- mature ecosystem

#### 2. Redis
Used for fast temporary data and real-time scoring support.

Used for:

- session cache
- temporary counters
- risk scoring cache
- rate limiting
- hot alert suppression windows
- short-lived geofence state

#### 3. Object Storage
Used for large or semi-structured files.

Used for:

- raw logs
- camera images
- device snapshots
- attachments
- exported evidence
- archived data backups

Examples:

- Amazon S3
- Google Cloud Storage
- Azure Blob Storage
- S3-compatible object storage

---

## Logical Data Flow

The logical data flow is:

1. Devices and systems send events
2. Events are stored in the Events table
3. Detection engine evaluates event patterns
4. Risk scores are calculated and stored
5. Alerts are generated for suspicious events
6. Operators investigate alerts as cases
7. Audit logs record user and system actions
8. Evidence files and reports are retained for later review

---

## Core Entity Relationship Overview

High-level relationship summary:

- One Organization → Many Users
- One Organization → Many Devices
- One User → Many Devices
- One Device → Many Events
- One Event → Many Risk Score Records
- One Event → Zero or Many Alerts
- One Alert → Zero or One Case
- One User → Many Assigned Cases
- One User → Many Audit Logs
- One Organization → Many Locations
- Alert Rules are used by the Detection Engine
- Evidence Files may belong to Cases or Alerts

---

## Main Tables

## 1. Organizations

Stores tenant or customer-level ownership of resources.

This enables future multi-tenant deployment for:

- companies
- schools
- municipalities
- neighborhood watch groups
- private security operators

| Column | Type | Description |
|---|---|---|
| organization_id | UUID | Primary key |
| name | VARCHAR(255) | Organization name |
| organization_type | VARCHAR(100) | company / school / municipal / private / other |
| status | VARCHAR(50) | active / inactive |
| created_at | TIMESTAMP | Creation time |
| updated_at | TIMESTAMP | Last update time |

### Notes
- Recommended to use this table from the beginning.
- Even if the first version is single-organization, this avoids future migration pain.

---

## 2. Users

Stores system users such as operators, administrators, analysts, and viewers.

| Column | Type | Description |
|---|---|---|
| user_id | UUID | Primary key |
| organization_id | UUID | Owning organization |
| name | VARCHAR(255) | User name |
| email | VARCHAR(255) | Email address |
| role | VARCHAR(50) | admin / operator / analyst / viewer |
| status | VARCHAR(50) | active / disabled |
| password_hash | VARCHAR(255) | Password hash if local auth is used |
| last_login_at | TIMESTAMP | Last login time |
| created_at | TIMESTAMP | Creation time |
| updated_at | TIMESTAMP | Last update time |

### Notes
- External identity providers can also be used later.
- Store least privilege roles.
- Avoid storing plaintext passwords under any condition.

---

## 3. Devices

Stores registered devices and monitored sources.

Examples:

- GPS tracker
- security camera
- door sensor
- mobile app client
- router log source
- server agent
- network appliance

| Column | Type | Description |
|---|---|---|
| device_id | UUID | Primary key |
| organization_id | UUID | Owning organization |
| owner_user_id | UUID | Device owner or manager |
| device_name | VARCHAR(255) | Human-readable device name |
| device_type | VARCHAR(100) | gps / camera / sensor / mobile / network / cloud |
| serial_number | VARCHAR(255) | Device serial if available |
| status | VARCHAR(50) | active / inactive / maintenance / retired |
| registered_at | TIMESTAMP | Registration time |
| last_seen_at | TIMESTAMP | Last event received time |
| metadata | JSONB | Flexible device data |
| created_at | TIMESTAMP | Creation time |
| updated_at | TIMESTAMP | Last update time |

### Notes
- `metadata` can hold firmware version, vendor, model, tags, capabilities.
- Device status can be updated automatically from heartbeat logic.

---

## 4. Device Groups

Stores logical groups of devices.

Examples:

- School Cameras
- Delivery Trackers
- Office Entry Sensors
- Neighborhood North Zone
- Retail Branch A

| Column | Type | Description |
|---|---|---|
| group_id | UUID | Primary key |
| organization_id | UUID | Owning organization |
| name | VARCHAR(255) | Group name |
| description | TEXT | Optional description |
| created_at | TIMESTAMP | Creation time |

---

## 5. Device Group Members

Maps devices to groups.

| Column | Type | Description |
|---|---|---|
| group_id | UUID | Related group |
| device_id | UUID | Related device |
| added_at | TIMESTAMP | Membership creation time |

### Notes
- Composite primary key: `(group_id, device_id)`

---

## 6. Locations

Stores monitored locations and geofence definitions.

Used for:

- permitted zones
- restricted zones
- watch areas
- school boundaries
- office premises
- neighborhood sectors

| Column | Type | Description |
|---|---|---|
| location_id | UUID | Primary key |
| organization_id | UUID | Owning organization |
| name | VARCHAR(255) | Location name |
| location_type | VARCHAR(100) | site / geofence / restricted / safe_zone |
| latitude | DECIMAL(10, 7) | Latitude |
| longitude | DECIMAL(10, 7) | Longitude |
| geo_fence_radius | INT | Radius in meters |
| metadata | JSONB | Optional location details |
| created_at | TIMESTAMP | Creation time |
| updated_at | TIMESTAMP | Last update time |

### Notes
- Future versions may support polygon geofences instead of radius only.
- Spatial extensions can be added later with PostGIS.

---

## 7. Events

Stores incoming telemetry, activity records, and system events.

This is the **central table** of the NSD system.

Examples:

- GPS movement
- login success
- login failure
- access attempt
- camera motion
- tamper event
- device offline
- firewall denial
- password reset
- unusual access time
- policy violation
- cloud admin action

| Column | Type | Description |
|---|---|---|
| event_id | UUID | Primary key |
| organization_id | UUID | Owning organization |
| device_id | UUID | Related device |
| user_id | UUID | Related user if known |
| event_type | VARCHAR(100) | movement / login / access / tamper / offline / reset / policy_violation |
| event_source | VARCHAR(100) | gps / camera / sensor / app / network / cloud / auth |
| event_timestamp | TIMESTAMP | Original event time |
| received_at | TIMESTAMP | Time ingested by system |
| location_lat | DECIMAL(10, 7) | Latitude if available |
| location_lng | DECIMAL(10, 7) | Longitude if available |
| ip_address | VARCHAR(64) | Source IP if available |
| severity_hint | VARCHAR(50) | low / medium / high / critical |
| raw_data | JSONB | Raw original event data |
| normalized_data | JSONB | Normalized parsed event fields |
| ingestion_id | UUID | Batch or pipeline identifier |
| created_at | TIMESTAMP | Row creation time |

### Notes
- `raw_data` preserves original information for traceability.
- `normalized_data` supports cross-source analytics.
- This table will become very large and must be optimized carefully.

---

## 8. Risk Scores

Stores scoring history for events evaluated by the detection engine.

This keeps scoring explainable and auditable.

| Column | Type | Description |
|---|---|---|
| score_id | UUID | Primary key |
| event_id | UUID | Related event |
| score | INT | Risk score value |
| score_level | VARCHAR(50) | low / medium / high / critical |
| scoring_model | VARCHAR(100) | rule_based / anomaly_model / heuristic_v1 |
| reason | TEXT | Explanation of score |
| factors | JSONB | Scoring factor breakdown |
| calculated_at | TIMESTAMP | Calculation time |

### Notes
- An event may have multiple scores over time if models are re-run.
- This is useful for tuning detection logic later.

---

## 9. Alerts

Stores alerts generated by the detection engine.

An alert may be created for:

- a single suspicious event
- multiple related events
- threshold violations
- anomaly detections
- geofence breaches
- repeated failures over time

| Column | Type | Description |
|---|---|---|
| alert_id | UUID | Primary key |
| organization_id | UUID | Owning organization |
| event_id | UUID | Related primary event |
| rule_id | UUID | Matched rule if applicable |
| risk_score | INT | Final alert score |
| alert_level | VARCHAR(50) | low / medium / high / critical |
| title | VARCHAR(255) | Alert title |
| description | TEXT | Alert description |
| status | VARCHAR(50) | open / acknowledged / investigating / closed / suppressed |
| first_seen_at | TIMESTAMP | First relevant event time |
| last_seen_at | TIMESTAMP | Most recent relevant event time |
| created_at | TIMESTAMP | Alert creation time |
| updated_at | TIMESTAMP | Last update time |

### Notes
- A future correlation table can connect one alert to multiple events.
- Suppression state is useful to reduce alert floods.

---

## 10. Cases

Stores investigation cases created from alerts.

Operators use cases to track investigation progress.

| Column | Type | Description |
|---|---|---|
| case_id | UUID | Primary key |
| organization_id | UUID | Owning organization |
| alert_id | UUID | Related alert |
| assigned_to | UUID | Assigned operator |
| priority | VARCHAR(50) | low / medium / high / urgent |
| status | VARCHAR(50) | open / investigating / resolved / closed |
| summary | VARCHAR(255) | Short case summary |
| notes | TEXT | Investigation notes |
| resolution | TEXT | Resolution details |
| opened_at | TIMESTAMP | Case open time |
| resolved_at | TIMESTAMP | Case resolved time |
| created_at | TIMESTAMP | Creation time |
| updated_at | TIMESTAMP | Last update time |

### Notes
- One alert may produce one case in the basic model.
- Future versions may support many-to-many alert-case linkage.

---

## 11. Alert Rules

Stores detection rules that drive alert generation.

Examples:

- repeated login failures
- unusual access hours
- geofence exit
- multiple password resets
- device offline for too long
- impossible travel
- repeated tamper signals

| Column | Type | Description |
|---|---|---|
| rule_id | UUID | Primary key |
| organization_id | UUID | Owning organization |
| name | VARCHAR(255) | Rule name |
| rule_type | VARCHAR(100) | threshold / sequence / anomaly / geofence |
| description | TEXT | Rule description |
| threshold_value | VARCHAR(100) | Threshold setting if applicable |
| severity_default | VARCHAR(50) | low / medium / high / critical |
| enabled | BOOLEAN | Rule enabled status |
| rule_config | JSONB | Structured rule definition |
| created_at | TIMESTAMP | Creation time |
| updated_at | TIMESTAMP | Last update time |

### Notes
- `rule_config` can store flexible parameters for future engines.
- This avoids hardcoding every rule in source code only.

---

## 12. Notification History

Stores delivery history for alerts and cases.

Examples:

- email
- SMS
- push notification
- webhook
- dashboard notification

| Column | Type | Description |
|---|---|---|
| notification_id | UUID | Primary key |
| alert_id | UUID | Related alert |
| case_id | UUID | Related case if applicable |
| channel | VARCHAR(50) | email / sms / push / webhook |
| recipient | VARCHAR(255) | Recipient target |
| delivery_status | VARCHAR(50) | pending / sent / failed |
| payload | JSONB | Delivered payload |
| sent_at | TIMESTAMP | Delivery time |
| created_at | TIMESTAMP | Creation time |

---

## 13. Audit Logs

Stores user and system activity logs for accountability.

Examples:

- user login
- role change
- alert close
- case assignment
- rule update
- device registration
- export action
- evidence download

| Column | Type | Description |
|---|---|---|
| log_id | UUID | Primary key |
| organization_id | UUID | Owning organization |
| user_id | UUID | Actor user if available |
| action | VARCHAR(100) | Action performed |
| target_type | VARCHAR(100) | alert / case / device / user / rule / report |
| target_id | UUID | Related target object |
| details | TEXT | Human-readable details |
| metadata | JSONB | Structured metadata |
| ip_address | VARCHAR(64) | Actor IP if available |
| created_at | TIMESTAMP | Action time |

### Notes
- This table is important for security, compliance, and investigations.
- Prefer append-only behavior.

---

## 14. Evidence Files

Stores references to evidence objects stored in object storage.

Examples:

- screenshots
- camera images
- exported logs
- packet capture files
- PDFs
- investigation attachments

| Column | Type | Description |
|---|---|---|
| evidence_id | UUID | Primary key |
| organization_id | UUID | Owning organization |
| case_id | UUID | Related case |
| alert_id | UUID | Related alert |
| file_name | VARCHAR(255) | Original file name |
| object_path | VARCHAR(500) | Object storage path |
| content_type | VARCHAR(100) | MIME type |
| file_size | BIGINT | File size in bytes |
| uploaded_by | UUID | Uploader user |
| created_at | TIMESTAMP | Upload time |

---

## 15. Incident Reports

Stores final structured incident reports.

Used for:

- internal reporting
- police / legal documentation
- customer reporting
- executive summary
- compliance evidence

| Column | Type | Description |
|---|---|---|
| report_id | UUID | Primary key |
| organization_id | UUID | Owning organization |
| case_id | UUID | Related case |
| title | VARCHAR(255) | Report title |
| summary | TEXT | Executive summary |
| report_body | TEXT | Detailed report |
| report_status | VARCHAR(50) | draft / finalized / archived |
| created_by | UUID | Author |
| created_at | TIMESTAMP | Creation time |
| updated_at | TIMESTAMP | Last update time |

---

## Relationship Details

### Organizations
- One organization has many users
- One organization has many devices
- One organization has many locations
- One organization has many alerts and cases

### Users
- One user may own many devices
- One user may be assigned many cases
- One user may generate many audit log entries

### Devices
- One device produces many events
- One device may belong to many groups

### Events
- One event may have multiple risk score records
- One event may trigger zero or many alerts

### Alerts
- One alert may produce zero or one case in the basic model
- One alert may generate multiple notifications

### Cases
- One case may contain multiple evidence files
- One case may have one incident report

---

## Suggested Foreign Keys

Recommended foreign key relationships:

- `users.organization_id` → `organizations.organization_id`
- `devices.organization_id` → `organizations.organization_id`
- `devices.owner_user_id` → `users.user_id`
- `device_groups.organization_id` → `organizations.organization_id`
- `device_group_members.group_id` → `device_groups.group_id`
- `device_group_members.device_id` → `devices.device_id`
- `locations.organization_id` → `organizations.organization_id`
- `events.organization_id` → `organizations.organization_id`
- `events.device_id` → `devices.device_id`
- `events.user_id` → `users.user_id`
- `risk_scores.event_id` → `events.event_id`
- `alerts.organization_id` → `organizations.organization_id`
- `alerts.event_id` → `events.event_id`
- `alerts.rule_id` → `alert_rules.rule_id`
- `cases.organization_id` → `organizations.organization_id`
- `cases.alert_id` → `alerts.alert_id`
- `cases.assigned_to` → `users.user_id`
- `alert_rules.organization_id` → `organizations.organization_id`
- `audit_logs.organization_id` → `organizations.organization_id`
- `audit_logs.user_id` → `users.user_id`
- `evidence_files.case_id` → `cases.case_id`
- `evidence_files.alert_id` → `alerts.alert_id`
- `incident_reports.case_id` → `cases.case_id`

---

## Event Data Modeling Strategy

Because NSD handles many event types, event data should follow a hybrid model.

### Structured Columns
Store common fields as normal columns:

- event_id
- device_id
- user_id
- event_type
- event_timestamp
- location
- ip_address

### Flexible JSONB Fields
Store source-specific or changing fields in JSONB:

- raw payloads
- vendor-specific fields
- variable attributes
- enriched data

### Benefits
- supports many device types
- supports evolving schemas
- preserves original evidence
- enables structured querying where needed

---

## Index Strategy

Indexes are critical because event and audit tables can become very large.

### Recommended Indexes

#### Organizations
- `organizations(name)`

#### Users
- `users(organization_id)`
- `users(email)`
- `users(role)`

#### Devices
- `devices(organization_id)`
- `devices(owner_user_id)`
- `devices(device_type)`
- `devices(status)`

#### Device Groups
- `device_groups(organization_id)`

#### Locations
- `locations(organization_id)`
- `locations(latitude, longitude)`

#### Events
- `events(device_id)`
- `events(organization_id)`
- `events(event_timestamp)`
- `events(device_id, event_timestamp)`
- `events(event_type)`
- `events(event_source)`
- `events(ip_address)`
- `events(organization_id, event_timestamp)`

#### Risk Scores
- `risk_scores(event_id)`
- `risk_scores(score_level)`
- `risk_scores(calculated_at)`

#### Alerts
- `alerts(organization_id)`
- `alerts(status)`
- `alerts(alert_level)`
- `alerts(risk_score)`
- `alerts(created_at)`
- `alerts(event_id)`

#### Cases
- `cases(alert_id)`
- `cases(assigned_to)`
- `cases(status)`
- `cases(priority)`
- `cases(created_at)`

#### Audit Logs
- `audit_logs(user_id)`
- `audit_logs(action)`
- `audit_logs(target_type)`
- `audit_logs(created_at)`

#### Evidence Files
- `evidence_files(case_id)`
- `evidence_files(alert_id)`

---

## Partitioning Strategy

The **Events** table is expected to be the largest table in the system.

To maintain performance, PostgreSQL partitioning is strongly recommended.

### Recommended Partition Method
**Range partitioning by event_timestamp**

Example monthly partitions:

- `events_2026_01`
- `events_2026_02`
- `events_2026_03`

### Benefits
- faster time-range queries
- easier archival
- lower index overhead per partition
- easier maintenance and retention management

### Additional Candidates for Partitioning
If volume grows significantly, also consider partitioning:

- audit_logs
- risk_scores
- notification_history

---

## Data Retention Policy

Recommended retention policy depends on operational, legal, and compliance needs.

| Data | Recommended Retention |
|---|---|
| Events | 1–3 years |
| Alerts | 5 years |
| Cases | 5–10 years |
| Audit Logs | 5 years |
| Risk Scores | 1–3 years |
| Notification History | 1–3 years |
| Evidence Files | Based on case policy |
| Raw Logs in Object Storage | Long-term archive |

### Notes
- Old event data can be archived to cold storage.
- Retention may differ by organization or regulation.
- Evidence linked to legal cases may need longer preservation.

---

## Security Considerations

### 1. Access Control
Use role-based access control for:

- administrators
- operators
- analysts
- viewers

### 2. Sensitive Data Protection
Potentially sensitive data includes:

- location data
- access history
- identity information
- IP addresses
- evidence files

Protect using:

- encryption at rest
- TLS in transit
- least privilege database access
- field-level masking where needed

### 3. Auditability
Administrative and investigative actions should always be logged.

### 4. Data Integrity
Important records such as alerts, cases, audit logs, and evidence references should be protected from unauthorized modification.

### 5. Backup and Recovery
Use scheduled backups for PostgreSQL and object storage lifecycle controls for evidence.

---

## Performance Considerations

### Write Performance
NSD may ingest events continuously, so ingestion paths should be optimized.

Recommendations:

- batch inserts where possible
- avoid excessive synchronous enrichment during ingestion
- use async pipelines for heavy analysis

### Read Performance
Common queries will include:

- recent events for a device
- alerts by status
- cases assigned to operator
- suspicious events in a time range
- geofence violations
- user activity history

### Reporting
For dashboards and analytics, consider:

- materialized views
- rollup tables
- separate analytics store in later versions

---

## Future Extensions

Possible future tables and features:

### 1. Correlated Alert Events
Maps one alert to multiple related events.

### 2. ML Model Registry
Stores model versions and metadata for anomaly scoring.

### 3. Rule Execution History
Stores when rules ran and what they matched.

### 4. Operator Comments
Allows threaded discussion inside cases.

### 5. Watchlists
Stores monitored users, devices, IPs, or locations.

### 6. External Integrations
Stores webhook endpoints and integration settings.

### 7. Workflow State Tables
Supports approval flows and escalation routing.

### 8. Spatial Extension
Use PostGIS for advanced geospatial search and polygon geofences.

---

## Example Investigation Flow

A typical investigation workflow may look like this:

1. A device sends an event
2. The event is stored in `events`
3. Detection logic calculates a risk score
4. The score is stored in `risk_scores`
5. An alert is generated in `alerts`
6. An operator opens a case in `cases`
7. Evidence is uploaded to object storage and referenced in `evidence_files`
8. All user actions are stored in `audit_logs`
9. Final findings are stored in `incident_reports`

---

## Example Core Schema Summary

A simplified high-level database structure:

- organizations
- users
- devices
- device_groups
- device_group_members
- locations
- events
- risk_scores
- alert_rules
- alerts
- cases
- notification_history
- audit_logs
- evidence_files
- incident_reports

---

## Recommended First Release Scope

For MVP or pilot testing, the following tables are enough:

- organizations
- users
- devices
- locations
- events
- risk_scores
- alerts
- cases
- audit_logs

### Optional in MVP
- alert_rules
- notification_history
- evidence_files

This allows fast development while preserving the future roadmap.

---

## Conclusion

The NSD database design is centered around a scalable investigation pipeline:

**Organizations → Users / Devices / Locations → Events → Risk Scores → Alerts → Cases**

This design supports:

- suspicious behavior detection
- device monitoring
- alert management
- operator investigations
- evidence preservation
- future product expansion

The schema is intentionally structured to remain simple enough for an MVP, while still supporting future growth into a production-grade suspicious detection platform.

---
