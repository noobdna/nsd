⸻

NSD – Deployment Architecture

Overview

This document describes the deployment architecture for the NSD (Network Suspicious Detection) system.

The deployment architecture defines how system components are deployed across cloud infrastructure, edge services, backend services, databases, and client applications.

The system is designed to be:
	•	cloud-native
	•	scalable
	•	secure
	•	observable
	•	resilient
	•	multi-tenant ready
	•	edge-integrated
	•	automation friendly

NSD can be deployed in small environments (single organization) and scaled to multi-organization or city-scale monitoring systems.

⸻

Deployment Architecture Overview

High Level Deployment

Devices / Sensors / Logs / Cameras
                ↓
          Edge / Ingestion Layer
                ↓
            API Layer
                ↓
       Detection / Processing Layer
                ↓
        Alert / Case Management
                ↓
             Database Layer
                ↓
        Dashboard / Admin UI
                ↓
           Operators / Analysts


⸻

Deployment Layers

1. Edge / Ingestion Layer

This layer receives data from devices, sensors, logs, and external systems.

Components
	•	API Gateway
	•	Ingestion API
	•	Authentication
	•	Rate limiting
	•	Logging
	•	Edge security filtering

Possible Deployment Platforms
	•	Cloudflare
	•	AWS API Gateway
	•	NGINX
	•	FastAPI Gateway
	•	Load Balancer

Responsibilities
	•	Receive events
	•	Validate API keys / tokens
	•	Normalize event data
	•	Forward events to backend
	•	Apply rate limits
	•	Log ingestion activity
	•	Block malicious traffic

⸻

2. API Layer

This layer provides all system APIs.

API Services
	•	Authentication API
	•	Users API
	•	Devices API
	•	Events API
	•	Risk Scoring API
	•	Alerts API
	•	Cases API
	•	Evidence API
	•	Reports API
	•	Admin API

Deployment Options
	•	Containerized services
	•	Kubernetes
	•	Docker Compose
	•	Serverless Functions
	•	VM-based deployment

Recommended Stack
	•	FastAPI / Node.js
	•	Docker
	•	Kubernetes (future scale)
	•	REST API
	•	JWT Authentication
	•	API Gateway

⸻

3. Detection / Processing Layer

This is the core intelligence of NSD.

Components
	•	Detection Engine
	•	Risk Scoring Engine
	•	Rule Engine
	•	Behavior Analysis
	•	Alert Generator
	•	Correlation Engine
	•	Scheduler / Batch Jobs

Processing Types

Processing	Description
Real-time processing	Immediate detection from events
Stream processing	Continuous event streams
Batch processing	Risk recalculation
Correlation	Multi-event pattern detection
ML detection (future)	Anomaly detection

Deployment Options
	•	Python services
	•	Worker containers
	•	Message queue workers
	•	Stream processing engines

⸻

4. Database Layer

This layer stores all system data.

Databases

Database	Purpose
PostgreSQL	Main relational data
Object Storage	Evidence files
Elasticsearch / OpenSearch	Logs & search
Redis	Cache / queues
Data Warehouse (future)	Analytics

Stored Data
	•	Users
	•	Organizations
	•	Devices
	•	Events
	•	Alerts
	•	Cases
	•	Evidence
	•	Risk scores
	•	Rules
	•	Audit logs
	•	Reports

⸻

Example Deployment Architecture (Cloud)

Cloud Deployment Example

                Internet
                    │
             Cloudflare / WAF
                    │
              API Gateway
                    │
        ┌─────────────────────┐
        │      API Servers     │
        └─────────────────────┘
                    │
        ┌─────────────────────┐
        │ Detection Workers    │
        └─────────────────────┘
                    │
        ┌─────────────────────┐
        │      Database        │
        └─────────────────────┘
                    │
        ┌─────────────────────┐
        │ Object Storage       │
        └─────────────────────┘
                    │
              Dashboard UI


⸻

Container Deployment Example

Docker Deployment

Services:
	•	api-service
	•	detection-engine
	•	worker
	•	postgres
	•	redis
	•	object-storage
	•	dashboard
	•	nginx / gateway

Example Docker Services

Service	Description
api	Backend API
worker	Detection engine
scheduler	Risk recalculation
postgres	Database
redis	Cache / queue
minio	Object storage
frontend	Dashboard
nginx	Reverse proxy


⸻

Kubernetes Deployment (Future Scale)

Kubernetes Components

Component	Purpose
API Pods	Backend APIs
Worker Pods	Detection engine
Scheduler Pods	Batch jobs
PostgreSQL	Database
Redis	Cache
Object Storage	Evidence
Ingress Controller	API entry
Monitoring	Metrics
Logging	Log aggregation


⸻

Monitoring & Observability

Monitoring Tools
	•	Prometheus
	•	Grafana
	•	OpenTelemetry
	•	ELK / OpenSearch
	•	Cloud Logging
	•	Alerting system

Metrics to Monitor

Metric	Description
Event ingestion rate	Events per second
Alert generation rate	Alerts per hour
Detection latency	Detection delay
API response time	API performance
DB query time	Database performance
Queue length	Worker backlog
Error rate	System health


⸻

Security Deployment Considerations

Security Controls
	•	API authentication
	•	MFA for admins
	•	TLS everywhere
	•	Network segmentation
	•	Private subnets
	•	Secrets management
	•	Audit logging
	•	WAF
	•	Rate limiting
	•	Backup encryption
	•	Evidence access control
	•	Zero Trust access

⸻

Backup & Disaster Recovery

Backup Strategy

Data	Backup
Database	Daily snapshot
Evidence	Object storage replication
Logs	Archive storage
Config	Git repository
Rules	Database backup

Recovery Strategy
	•	Database restore
	•	Object storage restore
	•	Re-deploy containers
	•	Rebuild from Infrastructure as Code
	•	Restore configuration
	•	Resume ingestion

⸻

Deployment Environments

Environment	Purpose
Local	Development
Dev	Integration testing
Staging	Pre-production
Production	Live system
DR	Disaster recovery


⸻

Future Deployment Expansion

Future architecture may include:
	•	Multi-region deployment
	•	Edge detection nodes
	•	AI anomaly detection cluster
	•	City-wide sensor networks
	•	Federation between organizations
	•	Government / enterprise deployment
	•	Mobile monitoring platform
	•	Real-time streaming analytics
	•	Data lake / analytics platform

⸻

Summary

Deployment Architecture Summary

NSD deployment architecture consists of:
	1.	Edge / Ingestion Layer
	2.	API Layer
	3.	Detection / Processing Layer
	4.	Database Layer
	5.	Dashboard / UI Layer
	6.	Monitoring & Logging
	7.	Security Controls
	8.	Backup & Disaster Recovery
	9.	Multi-Environment Deployment

The architecture is designed to support both MVP deployment and large-scale production deployment without major redesign.

⸻
