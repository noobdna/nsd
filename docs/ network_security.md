⸻

NSD – Network Security Architecture

network_security.md

Overview

This document describes the network security architecture of the NSD (Network Suspicious Detection) system.

The goal of network security in NSD is to ensure:
	•	secure data ingestion
	•	secure communication between services
	•	protection of APIs and backend systems
	•	secure device connectivity
	•	network isolation
	•	monitoring and intrusion detection
	•	auditability and traceability

The system is designed with Zero Trust and Defense-in-Depth principles.

⸻

Security Design Principles

1. Zero Trust Network Model

NSD follows Zero Trust principles:
	•	Never trust internal network automatically
	•	Always verify identity
	•	Always authorize access
	•	Encrypt all communications
	•	Log all access
	•	Monitor all traffic

Zero Trust Rules

Rule	Description
Authenticate	All users and devices must authenticate
Authorize	Access controlled by roles and policies
Encrypt	All traffic via TLS
Log	All network activity logged
Monitor	Suspicious behavior detected
Isolate	Services separated by network zones


⸻

Network Zones

The NSD network is divided into multiple security zones.

Network Zones Overview

Zone	Purpose
Internet	External devices and users
Edge Zone	Load balancer / WAF / API Gateway
Application Zone	Backend services
Detection Zone	Detection engine
Data Zone	Databases and storage
Admin Zone	Admin tools
Monitoring Zone	Logging and monitoring


⸻

Network Architecture Flow

Internet
   ↓
WAF / Load Balancer
   ↓
API Gateway
   ↓
Backend Services
   ↓
Detection Engine
   ↓
Database / Storage
   ↓
Monitoring / Logging


⸻

Firewall Rules

Default Firewall Policy
	•	Deny all inbound traffic
	•	Allow only required ports
	•	Restrict outbound traffic
	•	Log all denied traffic

Example Firewall Rules

Source	Destination	Port	Purpose
Internet	WAF	443	HTTPS
WAF	API Gateway	443	API traffic
API	Backend	443	Service communication
Backend	Database	5432	PostgreSQL
Backend	Object Storage	443	Evidence storage
Admin	Admin Server	22	SSH
Monitoring	All services	Various	Metrics


⸻

Secure Communication

TLS Encryption

All communications must use TLS:

Communication	Encryption
Device → API	HTTPS
API → Backend	HTTPS / mTLS
Backend → DB	TLS
Backend → Storage	HTTPS
Admin → Servers	SSH
Logs → Monitoring	TLS


⸻

mTLS (Mutual TLS)

mTLS is used for internal service communication.

Used for:
	•	API → Backend
	•	Backend → Detection Engine
	•	Detection Engine → Database
	•	Internal microservices

Benefits:
	•	Service identity verification
	•	Prevents unauthorized services
	•	Protects internal traffic

⸻

API Security

API Protection Layers

Layer	Protection
WAF	Blocks attacks
Rate Limit	Prevents abuse
Authentication	JWT / API Key
Authorization	RBAC
Logging	Audit logs
Monitoring	Suspicious behavior detection


⸻

Device Network Security

Devices connecting to NSD must follow security rules.

Device Security Requirements
	•	Unique device ID
	•	API Key authentication
	•	TLS communication
	•	IP logging
	•	Device certificate (optional)
	•	Firmware integrity check
	•	Rate limit per device
	•	Device behavior monitoring

⸻

Network Monitoring

NSD monitors network activity for suspicious behavior.

Monitored Events

Event	Description
Failed login attempts	Brute force detection
Unusual IP access	Geo anomaly
High request rate	DoS detection
Suspicious device behavior	Compromised device
Admin login outside hours	Insider risk
Large data transfer	Data exfiltration
Unauthorized API access	Intrusion attempt


⸻

Intrusion Detection Strategy

NSD detection engine analyzes:
	•	Login failures
	•	IP reputation
	•	Access time anomalies
	•	Device behavior anomalies
	•	Data transfer anomalies
	•	API abuse patterns
	•	Network scanning behavior
	•	Privilege escalation attempts

This integrates with:
	•	Risk scoring system
	•	Alert system
	•	Case management
	•	Investigation workflow

⸻

Logging and Audit Network Security

All network actions must be logged.

Logged Network Events
	•	API requests
	•	Login attempts
	•	Admin actions
	•	Device connections
	•	Firewall blocks
	•	WAF blocks
	•	Configuration changes
	•	Database access
	•	Evidence downloads
	•	Alert acknowledgements

Logs must be:
	•	Immutable
	•	Timestamped
	•	Signed (optional)
	•	Stored securely
	•	Retained per policy

⸻

Network Security Checklist

Security Checklist

Item	Status
TLS everywhere	Required
WAF enabled	Required
API authentication	Required
RBAC authorization	Required
Firewall rules configured	Required
Network segmentation	Required
Intrusion detection	Required
Audit logging	Required
Log retention policy	Required
Backup network isolation	Recommended
Admin network isolation	Recommended
mTLS internal services	Recommended
Bastion host for SSH	Recommended


⸻

Summary

The NSD network security architecture is based on:
	•	Zero Trust Architecture
	•	Network Segmentation
	•	TLS Encryption Everywhere
	•	WAF + API Gateway Protection
	•	RBAC Access Control
	•	Intrusion Detection
	•	Full Audit Logging
	•	Defense in Depth Strategy

The network is designed to ensure that even if one layer is compromised, the entire system is not compromised.

⸻

Next Related Documents

After network_security.md, the next recommended documents are:
	1.	infrastructure_architecture.md
	2.	security_architecture.md
	3.	deployment_architecture.md
	4.	monitoring_observability.md
	5.	backup_disaster_recovery.md

⸻
