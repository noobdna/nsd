# NSD – System Architecture

## 1. Overview

NSD (Network / Neighborhood Suspicious Detection) is a monitoring and detection platform designed to collect telemetry, logs, and device data, analyze suspicious behavior, and support alerting and investigation workflows.

The system is intended for use in environments such as:

- network monitoring
- facility monitoring
- neighborhood safety support
- device activity tracking
- suspicious behavior detection across physical and digital domains

NSD is designed to support both an MVP implementation and a future production-grade platform.

The architecture emphasizes:

- clear separation of responsibilities
- scalable event ingestion
- flexible detection processing
- operational visibility
- secure administration
- auditable investigation workflows

---

## 2. Architecture Goals

The system architecture is designed around the following goals.

### 2.1 Scalable Data Ingestion

NSD must be able to receive large numbers of events from multiple sources, including devices, logs, sensors, and external systems.

### 2.2 Modular Detection Flow

The detection pipeline should be logically separated so that ingestion, storage, analysis, alerting, and investigation can evolve independently.

### 2.3 Real-Time and Asynchronous Processing

Some operations may happen immediately, while others should be processed asynchronously through workers or queues.

### 2.4 Strong Security and Access Control

The platform must support secure access for operators, administrators, services, and devices.

### 2.5 Auditability and Evidence Retention

Security-relevant actions must be logged, traceable, and suitable for later review or investigation.

### 2.6 Cloud-Native Expansion

The architecture should remain simple for initial deployment while supporting future scaling in cloud environments.

---

## 3. High-Level Logical Architecture

At a high level, NSD follows this flow:

```text
Devices / Logs / External Sources
              ↓
        Ingestion Layer
              ↓
      Raw Event Storage
              ↓
       Detection Pipeline
              ↓
     Risk Scoring / Rules
              ↓
        Alert Generation
              ↓
    Notification / Dashboard
              ↓
   Case Management / Investigation

This architecture separates event intake, analysis, response, and investigation into distinct stages.

⸻

4. Core System Components

4.1 Data Sources

NSD can receive input from a variety of physical and digital sources.

Examples include:
	•	IoT devices
	•	GPS trackers
	•	cameras
	•	mobile devices
	•	routers
	•	servers
	•	access control systems
	•	authentication systems
	•	network logs
	•	cloud service logs
	•	external integrations

Typical incoming data may include:
	•	timestamps
	•	device identifiers
	•	user identifiers
	•	event types
	•	location data
	•	status changes
	•	login activity
	•	network activity
	•	uploaded files or evidence metadata

⸻

4.2 Ingestion Layer

The ingestion layer is responsible for receiving data from devices and external systems.

Its responsibilities include:
	•	receiving telemetry and log data
	•	validating request format and required fields
	•	authenticating devices or source systems
	•	applying rate limiting and request controls
	•	normalizing incoming event payloads
	•	storing raw events
	•	forwarding accepted events into the detection pipeline

Possible interface types include:
	•	REST API over HTTPS
	•	webhook endpoints
	•	MQTT for IoT scenarios
	•	batch upload endpoints
	•	internal service ingestion endpoints

The ingestion layer should be separated from operator-facing business APIs so that data collection and administrative functions can scale independently.

⸻

4.3 Raw Event Storage

Before advanced analysis is performed, incoming events should be preserved in raw or normalized form.

This layer exists to support:
	•	forensic traceability
	•	reprocessing
	•	replay of historical events
	•	debugging of detection logic
	•	evidence retention

Stored raw data may include:
	•	original request payloads
	•	normalized event records
	•	ingestion timestamps
	•	source identifiers
	•	validation results
	•	correlation IDs

⸻

4.4 Detection Pipeline

The detection pipeline is the analytical core of NSD.

It processes accepted events and determines whether they represent suspicious or risky behavior.

The detection layer may include:
	•	rule-based detection
	•	threshold-based evaluation
	•	pattern matching
	•	event correlation
	•	temporal behavior analysis
	•	geofence analysis
	•	anomaly indicators
	•	risk score calculation

Detection examples include:
	•	geofence violations
	•	unusual night-time activity
	•	repeated movement patterns
	•	impossible travel patterns
	•	unusual login times
	•	repeated failed logins
	•	excessive password reset attempts
	•	device tampering
	•	unusual network access behavior
	•	repeated abnormal operations

The detection pipeline may run in two modes:
	•	synchronous checks for simple validations
	•	asynchronous worker-based processing for deeper analysis

For production systems, asynchronous processing is preferred for scalability and resilience.

⸻

4.5 Risk Scoring

Risk scoring translates raw suspicious indicators into a measurable severity model.

Risk scoring may consider:
	•	event type
	•	source trust level
	•	repetition frequency
	•	historical behavior
	•	geolocation anomalies
	•	device reputation
	•	user behavior context
	•	rule weight

Outputs may include:
	•	numeric risk score
	•	severity level
	•	matched rules
	•	confidence indicators
	•	escalation recommendation

Risk scoring helps prioritize alerts and reduce operator overload.

⸻

4.6 Alert Management

When suspicious behavior exceeds defined thresholds or rule conditions, NSD generates alerts.

The alert subsystem is responsible for:
	•	creating alerts
	•	assigning severity and priority
	•	deduplicating repeated alert conditions
	•	correlating related events
	•	tracking alert lifecycle
	•	triggering notifications
	•	supporting escalation to investigation cases

Example alert levels:
	•	Low
	•	Medium
	•	High
	•	Critical

Alert status examples:
	•	open
	•	acknowledged
	•	investigating
	•	resolved
	•	false_positive
	•	escalated

⸻

4.7 Notification Service

The notification service delivers alerts to operators or external systems.

Supported channels may include:
	•	email
	•	SMS
	•	push notification
	•	dashboard notification
	•	webhook delivery
	•	third-party messaging integrations

Its responsibilities include:
	•	routing notifications by severity
	•	applying escalation rules
	•	retrying failed deliveries
	•	recording delivery status
	•	supporting multiple notification targets

This layer should be logically separated from alert generation so that new delivery channels can be added without changing core detection logic.

⸻

4.8 Backend API

The backend API provides operator-facing and administrative business functions.

Its responsibilities include:
	•	user management
	•	organization management
	•	device management
	•	alert management
	•	case management
	•	evidence management
	•	dashboard data APIs
	•	report APIs
	•	authentication and authorization
	•	audit log access
	•	system configuration management

This API is distinct from the ingestion interface.

Typical backend consumers include:
	•	frontend dashboard
	•	admin tools
	•	mobile operator apps
	•	internal services
	•	authorized external integrations

⸻

4.9 Case Management and Investigation

When an alert requires further review, it can be escalated into a case.

The case management layer supports:
	•	case creation from alerts
	•	assignment to investigators
	•	status tracking
	•	linked evidence
	•	notes and comments
	•	investigation timeline
	•	outcome recording
	•	incident report generation

This layer provides the operational bridge between detection and formal investigation.

⸻

4.10 Evidence and File Storage

NSD may need to store files associated with alerts and investigations.

Examples include:
	•	screenshots
	•	exported logs
	•	images
	•	attachments
	•	incident reports
	•	supporting documents

This storage must support:
	•	secure upload
	•	metadata tracking
	•	retention control
	•	access control
	•	traceability
	•	later retrieval for reporting or legal review

⸻

4.11 Database Layer

The database layer stores structured operational data.

Main data domains include:
	•	users
	•	organizations
	•	devices
	•	locations
	•	raw events
	•	normalized events
	•	risk scores
	•	alerts
	•	cases
	•	evidence metadata
	•	audit logs
	•	system settings
	•	rule definitions

A relational database such as PostgreSQL is a strong fit for the transactional core of NSD.

Additional storage systems may be added for specialized workloads such as high-volume event analytics or caching.

⸻

4.12 Cache and Short-Lived State

A cache layer may be used to improve performance and support short-lived system state.

Typical uses include:
	•	session caching
	•	rate-limit tracking
	•	alert deduplication windows
	•	temporary correlation state
	•	worker coordination
	•	frequently requested dashboard data

Redis is a typical choice for this layer.

⸻

4.13 Frontend Dashboard

The frontend dashboard is used by operators and administrators to monitor activity and manage investigations.

Typical functions include:
	•	map view of device locations
	•	live alert list
	•	alert detail views
	•	case management
	•	device inventory and status
	•	user and role management
	•	reports and analytics
	•	system health visibility
	•	audit log review

Typical frontend technologies may include:
	•	React
	•	Vue
	•	TypeScript
	•	Mapbox
	•	Google Maps

⸻

4.14 Monitoring and Observability

Operational visibility is essential for production use.

The monitoring layer should provide visibility into:
	•	API health
	•	ingestion rate
	•	queue depth
	•	worker failures
	•	detection latency
	•	notification failures
	•	database health
	•	storage usage
	•	authentication anomalies
	•	infrastructure errors

Common tooling may include:
	•	Prometheus
	•	Grafana
	•	CloudWatch
	•	structured logs
	•	audit log pipelines
	•	alerting on operational failures

⸻

5. End-to-End Data Flow

A typical NSD data flow is as follows:
	1.	A device, application, or external system sends an event.
	2.	The ingestion layer authenticates and validates the request.
	3.	The raw event is stored for traceability.
	4.	The event is normalized and forwarded into the detection pipeline.
	5.	Detection logic evaluates the event.
	6.	A risk score is calculated.
	7.	If the score or rule result exceeds thresholds, an alert is created.
	8.	The alert is stored in the database.
	9.	The notification service sends alert notifications.
	10.	The frontend dashboard displays the new alert.
	11.	An operator reviews the alert.
	12.	If needed, the alert is escalated into a case.
	13.	Evidence, notes, and investigation updates are attached to the case.
	14.	Final outcomes are stored for reporting and audit purposes.

⸻

6. Logical Deployment Architecture

Before cloud-specific implementation details, the system can be represented logically as follows:

Internet / Devices / External Systems
                 ↓
          Ingestion Endpoints
                 ↓
        API / Application Layer
                 ↓
        Queue / Worker Processing
                 ↓
      Detection / Alert Processing
                 ↓
   Relational Database / Object Storage
                 ↓
        Dashboard / Notifications
                 ↓
      Monitoring / Audit / Reporting

This model shows the main execution flow without binding the architecture to a specific cloud vendor.

⸻

7. Production Architecture (Cloudflare + AWS)

NSD production deployment is designed around Cloudflare for edge protection and secure access, and AWS for application hosting, storage, and service orchestration.

7.1 Role of Cloudflare

Cloudflare is used for:
	•	DNS
	•	WAF protection
	•	DDoS mitigation
	•	secure edge access
	•	Zero Trust access control
	•	protected administrative entry points
	•	optional tunnel-based private service exposure

7.2 Role of AWS

AWS is used for:
	•	application hosting
	•	backend service execution
	•	detection workers
	•	relational database hosting
	•	object storage
	•	cache and short-lived state
	•	notification integration
	•	infrastructure monitoring

⸻

8. Production Architecture Diagram

flowchart TB
    User[Users / Admin Operators]
    Device[IoT Devices / GPS / Sensors / External Sources]

    subgraph CF[Cloudflare]
        DNS[DNS]
        WAF[WAF / DDoS Protection]
        CDN[CDN / Edge]
        ACCESS[Zero Trust Access]
        TUNNEL[Cloudflare Tunnel]
    end

    subgraph AWS[AWS Cloud]
        ALB[Application Load Balancer]
        ING[Ingestion API]
        API[Backend API]
        QUEUE[Queue / Event Buffer]
        DET[Detection Workers]
        NOTIFY[Notification Service]
        DB[(RDS PostgreSQL)]
        REDIS[(Redis)]
        S3[(S3 Object Storage)]
        MAIL[SES / SNS]
        MON[Monitoring / Logs]
    end

    User --> DNS --> WAF --> CDN --> ALB
    ALB --> API

    User --> ACCESS --> TUNNEL --> API

    Device --> ING
    ING --> DB
    ING --> QUEUE
    QUEUE --> DET
    DET --> DB
    DET --> NOTIFY
    NOTIFY --> MAIL

    API --> DB
    API --> REDIS
    API --> S3
    API --> MON
    ING --> MON
    DET --> MON


⸻

9. Production Flow Explanation

In the production model:
	•	operators access the dashboard and backend services through Cloudflare-protected entry points
	•	administrative access can be additionally protected using Cloudflare Zero Trust and Tunnel
	•	devices and external systems submit events through the ingestion API
	•	accepted events are stored and forwarded into queue-based processing
	•	detection workers evaluate events asynchronously
	•	alerts and risk results are written to the database
	•	notification services distribute alerts through configured channels
	•	evidence files and investigation artifacts are stored in object storage
	•	monitoring systems track service health, failures, and operational metrics

This design separates public ingestion, internal business logic, and administrative access paths.

⸻

10. Security Considerations

The system architecture should support the following security controls:
	•	TLS for all external communications
	•	strong authentication for users and services
	•	API key or stronger authentication for devices
	•	role-based access control
	•	audit logging for security-sensitive actions
	•	least-privilege access between services
	•	database access restriction
	•	secure storage of secrets and credentials
	•	encryption at rest for stored data
	•	protected evidence access
	•	administrative access hardening through Zero Trust controls

⸻

11. Scalability Considerations

NSD should be able to scale in the following areas:
	•	ingestion throughput
	•	worker-based detection processing
	•	notification delivery
	•	dashboard read traffic
	•	evidence storage volume
	•	alert and case history retention

Scalability can be improved by:
	•	separating ingestion API from backend API
	•	introducing queue-based asynchronous processing
	•	scaling stateless services horizontally
	•	caching frequent dashboard queries
	•	offloading large files to object storage
	•	isolating transactional and analytical workloads over time

⸻

12. Future Architecture Extensions

Future versions of NSD may add:
	•	multi-tenant isolation
	•	advanced analytics pipelines
	•	machine learning assisted detection
	•	streaming event platforms
	•	SIEM / SOAR integration
	•	mobile operator applications
	•	third-party webhook ecosystem
	•	real-time map intelligence
	•	automated containment actions
	•	policy-based response workflows

The current architecture is intentionally structured so these can be added without major redesign.

⸻

13. Summary

NSD is structured as a modular monitoring and suspicious detection platform composed of:
	•	data sources
	•	ingestion interfaces
	•	raw event storage
	•	detection and risk scoring
	•	alert and notification services
	•	backend business APIs
	•	case and evidence management
	•	dashboard interfaces
	•	monitoring and audit systems

Its architecture supports a practical MVP while remaining ready for a more resilient production deployment using Cloudflare and AWS.
