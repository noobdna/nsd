⸻

NSD – Backend Architecture

Overview

This document describes the backend architecture of the NSD (Network Suspicious Detection) system.

The backend is responsible for:
	•	data ingestion
	•	detection processing
	•	alert generation
	•	investigation and case management
	•	user and device management
	•	evidence storage
	•	reporting
	•	audit logging
	•	API services for frontend and external integrations

The backend is designed to be scalable, secure, auditable, and resilient.

⸻

Backend Architecture – High Level

Devices / Logs / Sensors / External Systems
                ↓
          Ingestion API
                ↓
        Event Processing Queue
                ↓
         Detection Engine
                ↓
        Alert Engine
                ↓
         Backend API
                ↓
 Database / Storage / Evidence
                ↓
        Frontend Dashboard


⸻

Backend Components

1. API Gateway

The API Gateway is the entry point for all backend requests.

Responsibilities:
	•	authentication
	•	authorization
	•	rate limiting
	•	request validation
	•	routing
	•	logging
	•	API key management
	•	JWT validation
	•	tenant isolation (future)

Possible technologies:
	•	Cloudflare
	•	NGINX
	•	AWS API Gateway
	•	Kong
	•	Envoy

Endpoints handled:
	•	Device API
	•	Events API
	•	Alerts API
	•	Cases API
	•	Evidence API
	•	Reports API
	•	Admin API
	•	Users API

⸻

2. Ingestion Service

The ingestion service receives events from devices, logs, and external systems.

Examples of ingested data:
	•	device telemetry
	•	GPS data
	•	network logs
	•	authentication logs
	•	camera events
	•	sensor events
	•	access logs
	•	cloud logs
	•	firewall logs
	•	DNS logs
	•	VPN logs

Responsibilities:
	•	receive events
	•	validate schema
	•	normalize data
	•	add metadata
	•	timestamp normalization
	•	device lookup
	•	organization lookup
	•	risk pre-tagging
	•	push to event queue

This service must support high throughput ingestion.

⸻

3. Event Queue / Stream

The event queue decouples ingestion from detection processing.

Reasons:
	•	handle spikes
	•	prevent data loss
	•	enable asynchronous processing
	•	allow multiple consumers
	•	improve scalability

Possible technologies:
	•	Kafka
	•	RabbitMQ
	•	AWS SQS
	•	Redis Streams
	•	Google Pub/Sub

Events stored in queue:
	•	device events
	•	login events
	•	network events
	•	access events
	•	location updates
	•	system events
	•	audit events

⸻

4. Detection Engine

The detection engine analyzes events and determines suspicious behavior.

Detection types:
	•	repeated login failures
	•	unusual access time
	•	impossible travel
	•	abnormal activity frequency
	•	device anomaly
	•	network anomaly
	•	rule-based detection
	•	behavior-based detection
	•	risk score calculation

Detection methods:
	•	rule engine
	•	threshold detection
	•	pattern detection
	•	statistical anomaly detection
	•	behavior baseline comparison
	•	risk scoring model

Outputs:
	•	risk score
	•	detection result
	•	alert trigger
	•	event tagging
	•	case suggestion

⸻

5. Alert Engine

The alert engine generates and manages alerts.

Responsibilities:
	•	alert creation
	•	alert severity calculation
	•	alert deduplication
	•	alert correlation
	•	alert escalation
	•	notification triggering
	•	alert lifecycle management
	•	alert status tracking
	•	link alerts to cases

Alert severity examples:
	•	Low
	•	Medium
	•	High
	•	Critical

Notifications:
	•	Email
	•	SMS
	•	Push notification
	•	Dashboard notification
	•	Webhook
	•	Slack / Teams
	•	PagerDuty

⸻

6. Backend API Service

The Backend API provides services to the frontend dashboard and external systems.

Main APIs:
	•	Users API
	•	Organizations API
	•	Devices API
	•	Events API
	•	Alerts API
	•	Cases API
	•	Evidence API
	•	Reports API
	•	Risk Scores API
	•	Rules API
	•	Audit Logs API
	•	Notification API
	•	Admin API

Responsibilities:
	•	business logic
	•	database operations
	•	permissions
	•	filtering
	•	search
	•	pagination
	•	audit logging
	•	reporting queries
	•	export
	•	case workflow management

⸻

7. Database Layer

The backend uses multiple storage systems.

Relational Database

Stores structured data:
	•	users
	•	organizations
	•	devices
	•	alerts
	•	cases
	•	rules
	•	reports
	•	audit logs
	•	permissions
	•	configurations

Examples:
	•	PostgreSQL
	•	MySQL
	•	Aurora

Event Storage

Stores large volumes of events:
	•	event logs
	•	telemetry
	•	network logs
	•	authentication logs
	•	activity logs

Examples:
	•	Elasticsearch
	•	OpenSearch
	•	ClickHouse
	•	BigQuery
	•	Snowflake

Object Storage

Stores files and evidence:
	•	images
	•	videos
	•	documents
	•	log archives
	•	exported reports
	•	evidence files

Examples:
	•	S3
	•	Cloudflare R2
	•	GCS
	•	Azure Blob

⸻

8. Evidence Service

The evidence service manages evidence files and forensic data.

Responsibilities:
	•	file upload
	•	secure storage
	•	hash calculation
	•	chain of custody
	•	metadata storage
	•	access control
	•	download logging
	•	evidence linking to cases
	•	retention policy enforcement

Evidence types:
	•	screenshots
	•	camera images
	•	videos
	•	log files
	•	PCAP
	•	documents
	•	reports
	•	forensic images

⸻

9. Notification Service

Responsible for sending notifications.

Channels:
	•	email
	•	SMS
	•	push
	•	webhook
	•	Slack
	•	Teams
	•	PagerDuty

Responsibilities:
	•	template management
	•	retry logic
	•	rate limiting
	•	escalation policy
	•	delivery tracking
	•	notification logs

⸻

10. Audit Logging Service

All important actions must be logged.

Audit logs include:
	•	login
	•	logout
	•	password change
	•	device registration
	•	alert updates
	•	case updates
	•	evidence upload
	•	evidence download
	•	admin actions
	•	permission changes
	•	rule changes
	•	system configuration changes

Audit logs must be:
	•	immutable
	•	timestamped
	•	user linked
	•	IP logged
	•	tamper resistant

⸻

Backend Data Flow

Device / Logs
      ↓
Ingestion API
      ↓
Normalization
      ↓
Event Queue
      ↓
Detection Engine
      ↓
Risk Score
      ↓
Alert Engine
      ↓
Database
      ↓
Backend API
      ↓
Frontend Dashboard


⸻

Scalability Strategy

To scale the backend:
	•	stateless API servers
	•	horizontal scaling
	•	queue-based processing
	•	event partitioning
	•	database read replicas
	•	object storage for files
	•	caching layer (Redis)
	•	async processing
	•	microservices (future)
	•	multi-tenant architecture
	•	regional deployment

⸻

Security Considerations

Backend security requirements:
	•	JWT authentication
	•	MFA for admins
	•	RBAC
	•	API rate limiting
	•	IP allow list (admin)
	•	encryption at rest
	•	encryption in transit
	•	audit logging
	•	evidence integrity hashing
	•	secure secrets management
	•	key rotation
	•	zero trust network access
	•	service-to-service authentication
	•	tenant isolation
	•	backup and disaster recovery

⸻

Suggested Backend Technology Stack (Example)

Example stack:
	•	API Gateway: Cloudflare / Kong
	•	Backend API: Python (FastAPI) / Node.js
	•	Detection Engine: Python
	•	Queue: Kafka / SQS
	•	Database: PostgreSQL
	•	Event Store: OpenSearch / ClickHouse
	•	Object Storage: S3 / Cloudflare R2
	•	Cache: Redis
	•	Auth: JWT / OAuth / MFA
	•	Notifications: Email / Webhook
	•	Deployment: Docker / Kubernetes
	•	Monitoring: Prometheus / Grafana
	•	Logging: OpenSearch
	•	CI/CD: GitHub Actions
	•	IaC: Terraform

⸻

Summary

The NSD backend architecture consists of:
	1.	API Gateway
	2.	Ingestion Service
	3.	Event Queue
	4.	Detection Engine
	5.	Alert Engine
	6.	Backend API
	7.	Database Layer
	8.	Evidence Service
	9.	Notification Service
	10.	Audit Logging Service

This architecture supports:
	•	large-scale event ingestion
	•	suspicious behavior detection
	•	alert management
	•	investigation workflows
	•	evidence management
	•	reporting and analytics
	•	auditability
	•	security and compliance
	•	future multi-tenant expansion
	•	cloud or hybrid deployment

⸻

