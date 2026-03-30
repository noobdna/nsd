⸻

NSD – Data Flow Architecture

Overview

This document describes how data flows through the NSD (Network Suspicious Detection) system from data sources to storage, detection, alerts, and dashboards.

The system is designed to ingest large volumes of telemetry and activity data, analyze suspicious behavior, generate alerts, and support investigation workflows.

⸻

High Level Data Flow

Devices / Logs / Sensors / Cloud Logs
                ↓
          Data Ingestion API
                ↓
          Message Queue
                ↓
          Processing Workers
                ↓
         Detection Engine
                ↓
        Risk Scoring Engine
                ↓
           Alert System
                ↓
            Database
                ↓
         Backend API
                ↓
      Frontend Dashboard


⸻

Data Flow Stages

1. Data Sources

Data originates from multiple sources:

Device Data
	•	IoT devices
	•	GPS trackers
	•	Cameras
	•	Sensors
	•	Mobile devices

Network & System Logs
	•	Firewall logs
	•	Router logs
	•	VPN logs
	•	Authentication logs
	•	Server logs
	•	Cloud logs
	•	Access logs

User Activity
	•	Logins
	•	Password resets
	•	Device changes
	•	Location changes
	•	Admin actions
	•	Configuration changes

Each event must include:

event_id
timestamp
source_type
device_id
user_id
location
ip_address
event_type
event_data


⸻

2. Data Ingestion Layer

Data Ingestion API

The ingestion layer receives events via:
	•	REST API
	•	Webhooks
	•	Log forwarders
	•	Streaming agents
	•	Cloud log integrations
	•	IoT gateways

Responsibilities
	•	Authentication
	•	Rate limiting
	•	Schema validation
	•	Timestamp normalization
	•	Data enrichment
	•	Queue publishing
	•	Raw event logging

Output

Validated events are pushed to the message queue.

⸻

3. Message Queue / Streaming Layer

The queue decouples ingestion from processing.

Purpose
	•	Handle burst traffic
	•	Prevent ingestion overload
	•	Enable asynchronous processing
	•	Support scaling workers
	•	Provide event replay capability

Example Technologies
	•	Kafka
	•	RabbitMQ
	•	AWS SQS
	•	Google Pub/Sub
	•	Redis Streams

⸻

4. Processing Workers

Workers consume events from the queue and process them.

Processing Tasks
	•	Event normalization
	•	GeoIP lookup
	•	Device lookup
	•	User lookup
	•	Organization lookup
	•	Event enrichment
	•	Event classification
	•	Event storage
	•	Detection engine forwarding

Workers produce:
	•	normalized events
	•	enriched events
	•	detection inputs

⸻

5. Detection Engine

The detection engine analyzes behavior patterns and identifies suspicious activity.

Detection Examples
	•	Multiple failed logins
	•	Impossible travel
	•	Login at unusual time
	•	Multiple password resets
	•	Device change
	•	Access from new country
	•	High activity rate
	•	Privilege escalation
	•	Suspicious network scanning
	•	Data download anomalies

The detection engine outputs:

detection_id
event_id
rule_id
risk_score
severity
detection_time


⸻

6. Risk Scoring Engine

Risk scoring aggregates multiple events and detections.

Risk Score Sources
	•	Login failures
	•	Location changes
	•	Device changes
	•	Suspicious access times
	•	Admin actions
	•	Detection engine results
	•	Historical behavior
	•	User risk history
	•	Device risk history
	•	Organization risk level

Output

entity_type (user/device/location/org)
entity_id
risk_score
risk_level
updated_at

Risk scores are stored and used for alerting and dashboards.

⸻

7. Alert System

Alerts are generated when:
	•	Risk score exceeds threshold
	•	Critical detection rule triggered
	•	Multiple detections in short time
	•	Manual alert created
	•	Incident escalation

Alert Flow

Detection → Risk Score → Alert Rule → Alert Created
                                 ↓
                        Notification System

Notifications
	•	Email
	•	SMS
	•	Push notification
	•	Slack / Teams
	•	Web dashboard alert
	•	Incident management system

⸻

8. Database Storage

Data stored includes:

Data Type	Description
Events	Raw and processed events
Detections	Detection engine results
Alerts	Generated alerts
Cases	Investigation cases
Evidence	Files and logs
Users	System users
Devices	Registered devices
Locations	Location data
Risk Scores	Risk scoring
Rules	Detection rules
Audit Logs	System activity logs
Reports	Generated reports


⸻

9. Backend API

The backend API provides access to system data.

Backend API Functions
	•	Event search
	•	Alert management
	•	Case management
	•	Evidence upload
	•	Risk score lookup
	•	Device management
	•	User management
	•	Report generation
	•	Dashboard statistics
	•	Rule management
	•	Audit log access

⸻

10. Frontend Dashboard

The dashboard visualizes system data.

Dashboard Features
	•	Alert list
	•	Alert timeline
	•	Risk score overview
	•	Event search
	•	Map view
	•	Device status
	•	User activity
	•	Case management
	•	Investigation timeline
	•	Reports
	•	System health
	•	Metrics

⸻

Data Flow Summary

Full Data Flow

1. Devices / Logs generate events
2. Events sent to Ingestion API
3. Events pushed to Message Queue
4. Workers process events
5. Events analyzed by Detection Engine
6. Risk Score calculated
7. Alerts generated
8. Data stored in Database
9. Backend API provides access
10. Dashboard displays data
11. Notifications sent to users


⸻

Real-Time vs Batch Processing

Real-Time Flow

Used for:
	•	login monitoring
	•	intrusion detection
	•	device alerts
	•	suspicious behavior alerts

Flow:

Event → Queue → Worker → Detection → Risk → Alert → Notification

Batch Flow

Used for:
	•	daily risk recalculation
	•	reports
	•	analytics
	•	anomaly detection
	•	trend analysis

Flow:

Events → Data Warehouse → Analytics Engine → Reports


⸻

Data Flow Design Goals

System Goals
	1.	Scalable ingestion
	2.	Real-time detection
	3.	Reliable alerting
	4.	Full audit trail
	5.	Evidence retention
	6.	Investigation support
	7.	Multi-tenant support
	8.	High availability
	9.	Data integrity
	10.	Security and privacy
	11.	Analytics support
	12.	Future AI detection integration

⸻

Future Extensions

Planned Enhancements
	•	Machine learning anomaly detection
	•	Behavior profiling
	•	Graph analysis of relationships
	•	Device fingerprinting
	•	UEBA (User and Entity Behavior Analytics)
	•	Automated response actions
	•	Account lock automation
	•	Network isolation automation
	•	SOAR integration
	•	Threat intelligence integration
	•	External API integrations

⸻
