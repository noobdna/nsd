⸻

NSD – System Data Flow

Overview

This document describes the data flow of the NSD (Network / Neighborhood Suspicious Detection) system.

The NSD system collects data from devices, logs, and external systems, processes the data through detection logic, generates alerts, supports investigation workflows, and stores all data for auditing and reporting.

The data flow is designed to be scalable, auditable, and near real-time.

⸻

High Level Data Flow

Devices / Logs / Sensors / External Systems
                    ↓
              Ingestion API
                    ↓
                Event Queue
                    ↓
             Detection Engine
                    ↓
               Risk Scoring
                    ↓
                 Alert Engine
                    ↓
                 Case System
                    ↓
               Evidence Storage
                    ↓
                  Database
                    ↓
              Dashboard / Reports
                    ↓
             Notification System

This represents the main data lifecycle in the NSD system.

⸻

Data Flow Stages

1. Data Sources

The system receives data from multiple sources:

Examples:
	•	IoT devices
	•	GPS trackers
	•	Cameras
	•	Network logs
	•	Access logs
	•	Authentication logs
	•	Cloud logs
	•	Mobile applications
	•	External APIs
	•	Manual reports

Typical Data Fields:
	•	device_id
	•	timestamp
	•	location
	•	event_type
	•	status
	•	user_id
	•	ip_address
	•	message
	•	metadata

These sources generate raw events.

⸻

2. Ingestion API

All incoming data is sent to the Ingestion API.

Responsibilities:
	•	authenticate device / system
	•	validate data format
	•	normalize event schema
	•	attach organization / device metadata
	•	write event to event queue
	•	log ingestion activity
	•	prevent malformed data
	•	rate limiting

The ingestion layer protects the backend systems from direct exposure.

⸻

3. Event Queue

After ingestion, events are written to a queue system.

Purpose:
	•	absorb traffic spikes
	•	enable asynchronous processing
	•	prevent detection engine overload
	•	allow scaling detection workers
	•	enable event replay if needed

Possible technologies:
	•	Kafka
	•	RabbitMQ
	•	AWS SQS
	•	Redis Streams

⸻

4. Detection Engine

The Detection Engine processes incoming events and analyzes suspicious behavior.

Detection methods may include:
	•	rule-based detection
	•	anomaly detection
	•	behavior pattern detection
	•	threshold detection
	•	time-based detection
	•	location-based detection
	•	frequency analysis
	•	correlation between events
	•	device risk scoring
	•	user risk scoring

The detection engine produces:
	•	risk scores
	•	suspicious flags
	•	detection logs

⸻

5. Risk Scoring

Each event, device, or user can receive a risk score.

Risk score factors:
	•	number of failed logins
	•	unusual access time
	•	abnormal location
	•	abnormal activity frequency
	•	device reputation
	•	IP reputation
	•	past incidents
	•	rule triggers

Risk scores are used to determine whether an alert should be generated.

⸻

6. Alert Engine

When risk score or rules exceed thresholds, the system generates alerts.

Alerts include:
	•	alert_id
	•	related_event_id
	•	device_id
	•	user_id
	•	severity
	•	priority
	•	status
	•	description
	•	created_at

Alerts may:
	•	trigger notifications
	•	be assigned to operators
	•	be escalated into cases

⸻

7. Case Management

Alerts can be escalated into investigation cases.

Case system manages:
	•	investigation status
	•	assignments
	•	evidence
	•	notes
	•	timeline
	•	related alerts
	•	related events
	•	incident reports
	•	closure results

This represents the investigation workflow.

⸻

8. Evidence Storage

Evidence may include:
	•	logs
	•	images
	•	video clips
	•	documents
	•	exported reports
	•	forensic data
	•	screenshots
	•	device data snapshots

Evidence must be:
	•	immutable
	•	timestamped
	•	auditable
	•	securely stored

Possible storage:
	•	Object storage (S3)
	•	Secure file storage
	•	Encrypted storage

⸻

9. Database Storage

The database stores structured system data:

Main Entities:
	•	organizations
	•	users
	•	devices
	•	locations
	•	events
	•	risk_scores
	•	alerts
	•	cases
	•	evidence
	•	reports
	•	rules
	•	audit_logs

The database supports:
	•	operations
	•	investigation
	•	reporting
	•	analytics
	•	auditing

⸻

10. Dashboard / Reporting

Operators interact with the system through dashboards.

Dashboard features:
	•	alerts view
	•	case management
	•	device monitoring
	•	map view
	•	timeline view
	•	risk score monitoring
	•	event search
	•	report generation
	•	statistics and analytics

⸻

11. Notification System

The system sends notifications when important events occur.

Notification channels:
	•	Email
	•	SMS
	•	Push notifications
	•	Slack / Teams
	•	Webhooks
	•	Dashboard alerts

Triggers:
	•	high severity alert
	•	case assigned
	•	case updated
	•	system warning
	•	device offline
	•	suspicious activity detected

⸻

End-to-End Data Flow Summary

Complete flow:

Device / Log / Sensor
        ↓
Ingestion API
        ↓
Event Queue
        ↓
Detection Engine
        ↓
Risk Scoring
        ↓
Alert Engine
        ↓
Case Management
        ↓
Evidence Storage
        ↓
Database
        ↓
Dashboard / Reports
        ↓
Notifications

This represents the full lifecycle of data inside the NSD system.

⸻

Key Design Principles

The NSD data flow is designed with the following principles:
	•	Event-driven architecture
	•	Asynchronous processing
	•	Scalable ingestion
	•	Auditability and traceability
	•	Evidence preservation
	•	Investigation workflow support
	•	Multi-tenant readiness
	•	Security-first design
	•	Cloud-native compatibility
	•	Real-time alert capability

⸻

