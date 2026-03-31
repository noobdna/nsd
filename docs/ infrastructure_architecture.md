⸻

NSD – Infrastructure Architecture

Overview

This document describes the infrastructure architecture for the NSD (Network / Neighborhood Suspicious Detection) system.

The infrastructure is designed to be:
	•	scalable
	•	secure
	•	cloud-native
	•	event-driven
	•	resilient
	•	auditable
	•	deployable in small or large environments

The system can run on cloud infrastructure, hybrid environments, or on-premise deployments depending on the use case.

⸻

Infrastructure Architecture Goals

Design Goals

The infrastructure architecture is designed with the following goals:
	1.	High availability
	2.	Secure by default
	3.	Scalable event ingestion
	4.	Real-time detection processing
	5.	Reliable alert delivery
	6.	Evidence and audit log retention
	7.	Easy deployment and operations
	8.	Multi-tenant ready
	9.	API-first architecture
	10.	Zero-trust friendly network design

⸻

High Level Infrastructure Architecture

Infrastructure Overview

Devices / Sensors / Logs / Cameras / GPS
                ↓
        Edge / Gateway / API
                ↓
          Load Balancer
                ↓
        Backend Services
                ↓
   Detection Engine / Workers
                ↓
             Database
                ↓
        Alert / Notification
                ↓
        Dashboard / Frontend
                ↓
        Operators / Investigators


⸻

Infrastructure Components

1. Edge Layer

The edge layer receives incoming data from devices and external systems.

Responsibilities
	•	Device API endpoints
	•	Event ingestion API
	•	Authentication
	•	Rate limiting
	•	WAF protection
	•	TLS termination
	•	API routing
	•	Logging
	•	Geo/IP filtering
	•	DDoS protection

Example Technologies
	•	Cloudflare
	•	AWS CloudFront
	•	API Gateway
	•	Nginx
	•	Envoy
	•	HAProxy

⸻

2. Load Balancer Layer

The load balancer distributes traffic across backend services.

Responsibilities
	•	Traffic distribution
	•	Health checks
	•	Failover
	•	SSL termination (optional)
	•	Internal routing
	•	Service discovery integration

Example
	•	AWS ALB / NLB
	•	GCP Load Balancer
	•	Nginx
	•	HAProxy
	•	Kubernetes Ingress

⸻

3. Backend Services Layer

Backend services handle core system functionality.

Services
	•	User Service
	•	Device Service
	•	Event Service
	•	Alert Service
	•	Case Management Service
	•	Evidence Service
	•	Reporting Service
	•	Admin Service
	•	Notification Service
	•	Audit Log Service
	•	Risk Scoring Service
	•	Rule Engine Service

These services may run as:
	•	microservices
	•	modular monolith
	•	containers
	•	serverless functions

⸻

4. Detection Engine

The detection engine analyzes incoming events and detects suspicious behavior.

Responsibilities
	•	Rule-based detection
	•	Behavior analysis
	•	Risk scoring
	•	Pattern detection
	•	Threshold detection
	•	Time-based anomaly detection
	•	Alert generation
	•	Event correlation
	•	Device/user risk calculation

The detection engine may run as:
	•	Worker processes
	•	Stream processing system
	•	Queue consumers
	•	Scheduled jobs
	•	ML/AI analysis engine

⸻

5. Database Layer

The database stores all system data.

Stored Data
	•	Users
	•	Organizations
	•	Devices
	•	Locations
	•	Events
	•	Alerts
	•	Cases
	•	Evidence
	•	Reports
	•	Rules
	•	Risk scores
	•	Audit logs
	•	Notification logs
	•	System configuration

Possible Databases

Data Type	Database
Relational data	PostgreSQL
Large event data	TimescaleDB / BigQuery
Logs	Elasticsearch / OpenSearch
Cache	Redis
Files	Object Storage (S3)


⸻

Infrastructure Data Flow

Event Flow

Device → API → Event Service → Event DB
                           ↓
                     Detection Engine
                           ↓
                        Alerts
                           ↓
                    Notification Service
                           ↓
                   Email / SMS / Push


⸻

Investigation Flow

Alert → Case → Evidence → Report


⸻

Deployment Architecture Options

Option 1 – Single Server Deployment (Small Deployment)

Nginx
Backend API
Detection Engine
PostgreSQL
Redis
File Storage

Used for:
	•	small organizations
	•	pilot deployments
	•	lab environments
	•	development environments

⸻

Option 2 – Cloud Deployment (Recommended)

Cloudflare / CDN
Load Balancer
Backend Containers
Worker / Detection Engine
Managed Database
Object Storage
Notification Service
Monitoring


⸻

Option 3 – Kubernetes Deployment

Ingress
API Pods
Worker Pods
Detection Engine Pods
DB
Redis
Object Storage
Monitoring Stack

Used for:
	•	large scale
	•	multi-tenant environments
	•	enterprise deployment
	•	high availability environments

⸻

Network Architecture

Network Zones

Zone	Description
Edge	Public API
Application	Backend services
Processing	Detection engine
Data	Databases
Storage	Evidence storage
Admin	Admin access
Monitoring	Logging / metrics

Network Security Principles
	•	Zero trust access
	•	Private subnets for databases
	•	No direct DB access from internet
	•	Admin access via VPN / Zero Trust
	•	Service-to-service authentication
	•	Network segmentation
	•	Audit logging of all access

⸻

Security Infrastructure

Security Controls

Area	Control
Network	Firewall / Security Groups
Edge	WAF / Rate Limit
Identity	IAM / RBAC
Data	Encryption at rest
Transport	TLS
Secrets	Secret Manager
Access	Zero Trust
Audit	Audit Logging
Backup	Automated backups
Monitoring	SIEM / Metrics


⸻

Monitoring & Observability

Monitoring Components
	•	System metrics
	•	API metrics
	•	Event ingestion rate
	•	Detection engine performance
	•	Alert volume
	•	Database performance
	•	Queue size
	•	Errors
	•	Security events
	•	Login failures
	•	Admin activity
	•	Infrastructure health

Tools
	•	Prometheus
	•	Grafana
	•	ELK / OpenSearch
	•	CloudWatch
	•	Datadog
	•	Loki
	•	Jaeger / tracing

⸻

Backup & Disaster Recovery

Backup Strategy

Data	Backup
Database	Daily backup
Evidence files	Replicated storage
Logs	Archive storage
Config	Version control
Secrets	Secret manager backup

Disaster Recovery Goals

Metric	Target
RPO	< 15 minutes
RTO	< 2 hours


⸻

Infrastructure Summary

Infrastructure Layers Summary

Layer	Components
Edge	CDN / WAF / API Gateway
Load Balancer	Traffic routing
Application	Backend services
Processing	Detection engine
Data	Databases
Storage	Evidence storage
Notification	Email / SMS / Push
Monitoring	Logs / Metrics
Security	IAM / Audit / Encryption


⸻

Final Architecture Summary

Full Infrastructure Flow

Devices / Logs / Sensors
        ↓
      Edge
        ↓
   Load Balancer
        ↓
 Backend Services
        ↓
 Detection Engine
        ↓
     Database
        ↓
 Alerts / Cases
        ↓
 Notification
        ↓
 Dashboard
        ↓
 Operators


⸻

End of Document

⸻
