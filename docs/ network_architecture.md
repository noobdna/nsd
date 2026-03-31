⸻

NSD – Network Architecture

Overview

This document describes the network architecture of the NSD (Network Suspicious Detection) system.

NSD collects data from devices, network systems, IoT sensors, cameras, and cloud services, sends the data securely to backend services, processes suspicious behavior detection, and delivers alerts and dashboards to operators.

The network architecture is designed with the following goals:
	•	Secure data ingestion
	•	Zero-Trust network access
	•	Scalable cloud processing
	•	Isolated internal services
	•	Secure remote operations
	•	Reliable alert delivery
	•	Audit and forensic logging
	•	Multi-region ready design

⸻

High Level Network Architecture

Devices / Sensors / Cameras / Network Logs
                ↓
        Edge / Gateway Layer
                ↓
         Secure Tunnel / VPN
                ↓
           Cloud Edge / WAF
                ↓
           Ingestion API
                ↓
          Internal Services
                ↓
           Databases / Storage
                ↓
         Dashboard / Admin


⸻

Network Zones

The NSD network is divided into multiple security zones.

1. Device Network Zone

This zone contains devices that generate data.

Examples:
	•	IoT sensors
	•	GPS trackers
	•	Cameras
	•	Mobile devices
	•	Routers
	•	Servers
	•	Access control systems
	•	Network monitoring systems

Characteristics:
	•	Untrusted or semi-trusted devices
	•	Outbound communication only
	•	No inbound access allowed
	•	Devices send data to ingestion endpoints

Security controls:
	•	Device authentication (API key / certificate)
	•	TLS encryption
	•	Device ID verification
	•	Rate limiting
	•	Firmware integrity checks

⸻

2. Edge / Gateway Zone

This layer aggregates device traffic before sending to the cloud.

Components:
	•	Edge gateway servers
	•	Local collectors
	•	Log forwarders
	•	MQTT brokers
	•	Syslog collectors
	•	Video stream gateways
	•	Network sensors

Responsibilities:
	•	Buffer data
	•	Normalize data
	•	Compress logs
	•	Encrypt traffic
	•	Forward to ingestion API
	•	Local temporary storage
	•	Offline operation capability

This layer prevents devices from directly connecting to core backend services.

⸻

3. Cloud Edge / Security Layer

This layer protects the system from the internet.

Components:
	•	CDN / Edge network
	•	WAF
	•	DDoS protection
	•	API Gateway
	•	Rate limiting
	•	Bot protection
	•	Zero Trust Access
	•	Identity-aware proxy

Responsibilities:
	•	TLS termination
	•	Traffic filtering
	•	Authentication
	•	Access control
	•	Logging
	•	API protection
	•	Admin dashboard protection

⸻

4. Application Network (Private Network)

This is the internal backend network.

Components:
	•	Ingestion API
	•	Detection Engine
	•	Alert Service
	•	Case Management Service
	•	Reporting Service
	•	Admin API
	•	Worker / Queue processors
	•	Internal APIs

Characteristics:
	•	Private network only
	•	No direct internet access
	•	Access only via API Gateway / Zero Trust
	•	Service-to-service authentication
	•	Internal logging
	•	Audit logging

⸻

5. Data Network (Database Layer)

This layer stores all persistent data.

Components:
	•	Event database
	•	Alert database
	•	Case database
	•	User database
	•	Device database
	•	Audit log storage
	•	Evidence storage
	•	Object storage
	•	Backup storage
	•	Archive storage

Security:
	•	Private subnet only
	•	No public IP
	•	Encryption at rest
	•	Backup encryption
	•	Access logging
	•	Database activity monitoring

⸻

6. Admin / Operator Access Network

This network is used by administrators and investigators.

Access methods:
	•	Zero Trust access portal
	•	MFA authentication
	•	Identity provider login
	•	Bastion host
	•	Secure VPN
	•	Device posture check

Accessible systems:
	•	Dashboard
	•	Admin API
	•	Investigation tools
	•	Evidence viewer
	•	Reporting tools
	•	Logs
	•	Monitoring systems

⸻

Network Traffic Flow

Device Data Flow

Device
  ↓
Edge Gateway / Collector
  ↓
Secure Tunnel / TLS
  ↓
Cloud Edge / WAF
  ↓
Ingestion API
  ↓
Queue / Stream
  ↓
Detection Engine
  ↓
Database
  ↓
Alert System


⸻

Admin Access Flow

Admin User
  ↓
Zero Trust Access
  ↓
Identity Provider + MFA
  ↓
Access Proxy
  ↓
Dashboard / Admin API
  ↓
Internal Services


⸻

Alert Notification Flow

Detection Engine
  ↓
Alert Service
  ↓
Notification Service
  ↓
Email / SMS / Push / Slack


⸻

Network Security Principles

The NSD network follows several security principles.

Zero Trust Network
	•	No network is trusted by default
	•	All access must be authenticated
	•	All traffic must be encrypted
	•	Least privilege access
	•	Continuous monitoring

Network Segmentation
	•	Device network
	•	Edge network
	•	Application network
	•	Data network
	•	Admin network
	•	Monitoring network

Segmentation reduces blast radius and lateral movement risk.

Encryption

Encryption is required for:
	•	Device → Gateway
	•	Gateway → Cloud
	•	API communication
	•	Service-to-service communication
	•	Database storage
	•	Backup storage
	•	Evidence files
	•	Admin access

⸻

Example Network Topology

                Internet
                    |
             Cloud Edge / WAF
                    |
               API Gateway
                    |
          ---------------------
          |                   |
     Ingestion API       Admin Access
          |                   |
     Detection Engine      Dashboard
          |
        Queue
          |
        Database
          |
      Object Storage


⸻

Monitoring Network

The network must also include monitoring and logging.

Monitoring includes:
	•	Network traffic logs
	•	API access logs
	•	Authentication logs
	•	Device activity logs
	•	System logs
	•	Database logs
	•	Audit logs
	•	Security alerts
	•	Intrusion detection alerts

Monitoring systems:
	•	Metrics system
	•	Log aggregation
	•	SIEM
	•	Alert monitoring
	•	Uptime monitoring
	•	Network monitoring

⸻

Future Network Expansion

The architecture should support future expansion:
	•	Multi-region deployment
	•	Edge processing
	•	On-premise gateway deployment
	•	Partner network integration
	•	Law enforcement integration
	•	Smart city integration
	•	Retail / banking integration
	•	School / campus integration
	•	Factory / industrial IoT integration

⸻

Summary

The NSD network architecture is built with:
	•	Zero Trust networking
	•	Network segmentation
	•	Secure data ingestion
	•	Private backend network
	•	Secure admin access
	•	Encrypted communication
	•	Monitoring and audit logging
	•	Scalable cloud architecture

This network architecture supports a secure, scalable, and forensic-ready suspicious detection platform.

⸻
