⸻

infrastructure_network_design.md

Infrastructure & Network Design

Overview

This document describes the infrastructure and network design for the NSD (Network Suspicious Detection) system.

The system is designed to be:
	•	secure
	•	scalable
	•	observable
	•	fault tolerant
	•	cloud and edge compatible
	•	suitable for security monitoring workloads

The infrastructure supports:
	•	data ingestion
	•	detection processing
	•	alerting
	•	investigation workflows
	•	dashboard access
	•	evidence storage
	•	audit logging

⸻

1. High Level Infrastructure Architecture

System Zones

The infrastructure is divided into multiple security zones.

                Internet
                    |
            Cloudflare / WAF / CDN
                    |
                API Gateway
                    |
        -------------------------
        |                       |
   Application Network     Admin Network
        |                       |
   Backend Services        Admin Tools
        |
   Processing / Detection
        |
   Database Network
        |
   Storage / Evidence / Logs


⸻

2. Network Segmentation

Network Segments

1. Edge Network

Handles external traffic.

Components:
	•	CDN
	•	WAF
	•	DDoS protection
	•	Reverse proxy
	•	TLS termination

Purpose:
	•	protect origin infrastructure
	•	filter malicious traffic
	•	provide secure entry point

⸻

2. Application Network

Handles application services.

Components:
	•	Backend API
	•	Detection Engine
	•	Alert Service
	•	Notification Service
	•	Report Service
	•	Case Management Service

Rules:
	•	Only API Gateway can access backend services
	•	No direct internet access
	•	Internal service-to-service communication only

⸻

3. Database Network

Handles databases and storage systems.

Components:
	•	PostgreSQL / MySQL
	•	Event Storage DB
	•	Alert DB
	•	Audit Log DB
	•	Evidence Metadata DB
	•	Object Storage

Rules:
	•	Only backend services can access databases
	•	No public access
	•	Strict firewall rules
	•	Encrypted connections only

⸻

4. Admin Network

Used for administrative access.

Components:
	•	Bastion Host
	•	Admin Dashboard
	•	Monitoring tools
	•	Log analysis tools
	•	Incident response tools

Access:
	•	VPN / Zero Trust only
	•	MFA required
	•	All actions logged

⸻

3. Network Traffic Flow

Data Flow – Event Ingestion

Device / Sensor / Log Source
        |
        v
    Internet
        |
    Cloudflare / WAF
        |
    API Gateway
        |
    Ingestion Service
        |
    Event Queue / Stream
        |
    Detection Engine
        |
    Alert Service
        |
    Database


⸻

Dashboard Access Flow

User Browser
     |
     v
Cloudflare Access / Zero Trust
     |
Frontend Dashboard
     |
Backend API
     |
Database


⸻

Investigation Flow

Analyst
   |
Admin Network (VPN / Zero Trust)
   |
Backend API
   |
Database / Evidence Storage
   |
Case Management


⸻

4. Security Controls

Network Security Controls

Firewall Rules
	•	Deny all by default
	•	Allow only required ports
	•	Segment networks
	•	Restrict DB access
	•	Restrict admin access

Encryption
	•	TLS for all external traffic
	•	TLS for internal service communication
	•	Database encryption
	•	Storage encryption

Access Control
	•	Zero Trust access
	•	MFA for admin users
	•	Service-to-service authentication
	•	API authentication
	•	Role-based access control

Logging

All network actions must be logged:
	•	login attempts
	•	admin access
	•	API access
	•	configuration changes
	•	firewall changes
	•	database access

⸻

5. Recommended Network Architecture (Cloud Example)

Example Cloud Layout

VPC
 |
 |-- Public Subnet
 |      |-- Load Balancer
 |
 |-- Private Subnet (App)
 |      |-- Backend API
 |      |-- Detection Engine
 |      |-- Alert Service
 |
 |-- Private Subnet (DB)
 |      |-- PostgreSQL
 |      |-- Storage
 |
 |-- Admin Subnet
        |-- Bastion
        |-- Monitoring


⸻

6. Zero Trust Network Concept

The system should follow Zero Trust principles.

Principles:
	•	Never trust network location
	•	Always authenticate users
	•	Always authenticate services
	•	Least privilege access
	•	Full audit logging
	•	Device verification
	•	Short-lived credentials
	•	Network segmentation
	•	Continuous monitoring

⸻

7. Availability Design

High Availability

To ensure system availability:
	•	Load balancer
	•	Multiple application servers
	•	Database replication
	•	Multi-AZ deployment
	•	Backup system
	•	Disaster recovery region
	•	Health checks
	•	Auto scaling

⸻

8. Monitoring Network Infrastructure

Infrastructure monitoring should include:

Metrics
	•	CPU
	•	Memory
	•	Network traffic
	•	Disk usage
	•	DB connections
	•	API latency
	•	Queue size
	•	Error rate

Logs
	•	Access logs
	•	Firewall logs
	•	API logs
	•	Audit logs
	•	System logs
	•	Security logs

Alerts
	•	High CPU
	•	DB down
	•	API errors
	•	Suspicious traffic
	•	Unauthorized access
	•	Failed logins
	•	Network anomalies

⸻

9. Infrastructure Design Goals Summary

Design Principles

The infrastructure must be:
	•	Secure by default
	•	Network segmented
	•	Fully logged
	•	Highly available
	•	Scalable
	•	Observable
	•	Incident ready
	•	Forensics ready
	•	Zero Trust based
	•	Cloud / Edge compatible

⸻

Summary

This infrastructure and network design supports the NSD system by providing:
	•	secure network segmentation
	•	protected internet exposure
	•	scalable backend infrastructure
	•	secure database network
	•	admin access via Zero Trust
	•	full logging and monitoring
	•	incident response readiness
	•	high availability and disaster recovery

This design forms the foundation for a production-grade security monitoring and detection platform.

⸻
