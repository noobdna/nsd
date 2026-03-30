⸻

NSD – Data Architecture

Overview

This document describes the data architecture for the NSD (Network Suspicious Detection) system.

The NSD data architecture is designed to support:
	•	Large-scale event ingestion
	•	Suspicious behavior detection
	•	Alert and case management
	•	Investigation workflows
	•	Evidence storage
	•	Audit logging
	•	Reporting and analytics
	•	Long-term evidence retention
	•	Multi-tenant environments (future)

The architecture separates operational data, analytical data, logs, and evidence storage to ensure scalability, security, and auditability.

⸻

Data Architecture Goals

1. Scalability

The system must handle:
	•	High-volume event ingestion
	•	Logs from network devices
	•	IoT telemetry
	•	Access logs
	•	GPS/location data
	•	User activity logs
	•	Detection results

2. Auditability

All actions must be traceable:
	•	User actions
	•	Alert changes
	•	Case updates
	•	Evidence uploads
	•	Rule changes
	•	Admin operations

3. Evidence Preservation

Evidence must be:
	•	Immutable
	•	Timestamped
	•	Traceable
	•	Securely stored
	•	Retained for long periods

4. Separation of Data Types

Different data types must be stored separately:
	•	Operational relational data
	•	Event / telemetry data
	•	Logs / audit logs
	•	Evidence files
	•	Analytics / reporting data

⸻

High Level Data Architecture

Devices / Logs / Sensors / GPS
            ↓
      Data Ingestion API
            ↓
        Event Store
            ↓
     Detection Engine
            ↓
     Alerts / Risk Scores
            ↓
     Case Management
            ↓
       Evidence Storage
            ↓
       Reporting / Analytics


⸻

Data Storage Layers

1. Operational Database (Relational DB)

Stores structured operational data.

Main Entities
	•	Users
	•	Organizations
	•	Devices
	•	Locations
	•	Events (metadata)
	•	Alerts
	•	Cases
	•	Risk Scores
	•	Rules
	•	Assignments
	•	Comments
	•	Reports
	•	Audit Logs (metadata)

Example Database
	•	PostgreSQL
	•	MySQL
	•	Aurora
	•	Cloud SQL

This database supports:
	•	Dashboard
	•	API
	•	Case management
	•	Alert management
	•	Device management
	•	User management

⸻

2. Event Store (High Volume Data)

Stores large volumes of events and telemetry.

Event Types
	•	Login attempts
	•	Access logs
	•	Network traffic metadata
	•	GPS location events
	•	Device status
	•	Sensor events
	•	Authentication logs
	•	API access logs
	•	Behavior events

Example Technologies
	•	Elasticsearch / OpenSearch
	•	BigQuery
	•	ClickHouse
	•	TimescaleDB
	•	Kafka + Data Lake
	•	AWS Timestream
	•	Azure Data Explorer

This store is optimized for:
	•	Time-series queries
	•	Detection processing
	•	Behavior analysis
	•	Pattern detection
	•	Risk scoring
	•	Timeline reconstruction

⸻

3. Audit Log Store

Stores system and user activity logs.

Audit Log Examples
	•	User login
	•	Password change
	•	Alert status change
	•	Case status change
	•	Evidence upload
	•	Rule modification
	•	Admin actions
	•	API access
	•	Permission changes

Audit logs must be:
	•	Immutable
	•	Append-only
	•	Timestamped
	•	Traceable to user
	•	Stored long-term

Storage Options
	•	Append-only database
	•	Log storage
	•	Object storage
	•	SIEM integration

⸻

4. Evidence Storage

Stores investigation evidence files.

Evidence Types
	•	Log files
	•	Images
	•	Camera snapshots
	•	Video files
	•	Network captures (pcap)
	•	Documents
	•	Screenshots
	•	Exported reports
	•	Forensic files

Storage Requirements
	•	Immutable storage
	•	Versioning
	•	Hash verification
	•	Access logging
	•	Encryption
	•	Long-term retention

Storage Options
	•	Object storage (S3 / GCS / Azure Blob)
	•	On-prem object storage
	•	WORM storage
	•	Evidence vault

⸻

5. Analytics / Reporting Data Warehouse

Used for:
	•	Statistics
	•	Risk trends
	•	Incident trends
	•	Device risk ranking
	•	User behavior analysis
	•	Monthly reports
	•	SLA metrics
	•	Detection performance
	•	Investigation metrics

Example Technologies
	•	BigQuery
	•	Snowflake
	•	Redshift
	•	ClickHouse
	•	Data Lake

⸻

Data Flow Architecture

Data Flow Steps

Step 1 – Data Ingestion

Data sources:
	•	IoT devices
	•	GPS trackers
	•	Cameras
	•	Network logs
	•	Access logs
	•	Cloud logs
	•	API logs
	•	Authentication systems

Data is sent to:

Ingestion API → Event Store

Step 2 – Detection Processing

Detection engine reads events from Event Store and generates:
	•	Risk scores
	•	Alerts
	•	Behavior anomalies
	•	Suspicious patterns

Event Store → Detection Engine → Alerts / Risk Scores

Step 3 – Alert Handling

Alerts are stored in operational DB and shown in dashboard.

Operators can:
	•	Review alerts
	•	Assign alerts
	•	Escalate to cases
	•	Add comments
	•	Link evidence

Step 4 – Case Investigation

Cases store:
	•	Linked alerts
	•	Evidence
	•	Notes
	•	Timeline
	•	Assignments
	•	Status changes
	•	Final report

Step 5 – Reporting / Analytics

Operational DB + Event Store data is aggregated into analytics warehouse.

Used for:
	•	Reports
	•	Statistics
	•	Risk trends
	•	Investigation metrics

⸻

Data Retention Strategy

Data Type	Retention
Events	90–365 days
Alerts	3–5 years
Cases	5–10 years
Audit Logs	5–10 years
Evidence Files	5–10+ years
Reports	5 years
Risk Scores	1–3 years
Device Logs	1 year
Access Logs	1 year

Retention depends on:
	•	Legal requirements
	•	Investigation needs
	•	Storage cost
	•	Organization policy

⸻

Data Security

Data Security Requirements

Encryption
	•	Data at rest encryption
	•	Data in transit encryption (TLS)
	•	Evidence encryption
	•	Backup encryption

Access Control
	•	RBAC (Role-Based Access Control)
	•	Organization isolation
	•	Evidence access restrictions
	•	Admin access control

Logging

All access must be logged:
	•	Evidence access
	•	Case access
	•	Admin actions
	•	Rule changes
	•	Data exports

⸻

Data Architecture Summary

Data Storage Components

Component	Purpose
Operational DB	Alerts, cases, users, devices
Event Store	Telemetry and events
Audit Log Store	System and user logs
Evidence Storage	Investigation evidence
Data Warehouse	Reporting and analytics
Backup Storage	Disaster recovery


⸻

Final Architecture Concept

                +-------------------+
                | Devices / Logs    |
                +-------------------+
                           |
                           v
                +-------------------+
                | Data Ingestion API|
                +-------------------+
                           |
                           v
                +-------------------+
                | Event Store       |
                +-------------------+
                           |
                           v
                +-------------------+
                | Detection Engine  |
                +-------------------+
                           |
                           v
        +-----------------------------------+
        | Operational Database              |
        | Alerts / Cases / Users / Devices  |
        +-----------------------------------+
                           |
            +--------------+--------------+
            |                             |
            v                             v
+-----------------------+      +----------------------+
| Evidence Storage      |      | Audit Log Store      |
+-----------------------+      +----------------------+
            |
            v
+-----------------------+
| Reporting / Analytics |
+-----------------------+


⸻
