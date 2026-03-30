
⸻

NSD – Logging Architecture

Overview

The Logging Architecture defines how logs are generated, collected, transported, stored, and analyzed across the NSD (Network / Neighborhood Suspicious Detection) system.

Logging is critical for:
	•	Security monitoring
	•	Incident investigation
	•	Forensics and evidence
	•	System debugging
	•	Audit compliance
	•	Detection engine input
	•	Operational monitoring
	•	Performance analysis

The logging system must be centralized, tamper-resistant, searchable, and long-retained.

⸻

Logging Goals

1. Security Visibility

Capture all security-relevant activities:
	•	Logins
	•	Access attempts
	•	Device activity
	•	API calls
	•	Configuration changes
	•	Alerts
	•	Investigations
	•	Evidence uploads
	•	Admin actions

2. Incident Investigation & Forensics

Logs must allow reconstruction of:
	•	Who did what
	•	When it happened
	•	From where
	•	On which device
	•	What data changed
	•	What alerts were triggered

3. Tamper Resistance

Logs should:
	•	Not be editable
	•	Not be deletable by normal admins
	•	Be stored in append-only storage
	•	Be backed up and archived

4. Centralized Logging

All components send logs to a central logging system.

Sources include:
	•	IoT devices
	•	Cameras
	•	GPS trackers
	•	Backend API
	•	Detection engine
	•	Database
	•	Frontend
	•	Authentication system
	•	Network devices
	•	Cloud services
	•	OS logs
	•	Containers
	•	Reverse proxy / gateway
	•	WAF / CDN logs

⸻

High Level Logging Flow

Devices / Apps / Network / Cloud / Backend
                ↓
            Log Agents
                ↓
          Log Ingestion
                ↓
           Log Pipeline
                ↓
        Log Storage (Hot)
                ↓
      Log Archive (Cold)
                ↓
       Search / Analytics / Detection
                ↓
            Dashboard
                ↓
         Alerts / Reports


⸻

Log Sources

Device Logs
	•	IoT sensor logs
	•	Camera events
	•	GPS location updates
	•	Device status / heartbeat
	•	Firmware updates
	•	Device errors

Application Logs
	•	Backend API logs
	•	Frontend errors
	•	Authentication logs
	•	Authorization logs
	•	Alert generation logs
	•	Case management logs
	•	Evidence upload logs

Security Logs
	•	Login success / failure
	•	Password reset
	•	MFA events
	•	Suspicious behavior detection
	•	Account lockouts
	•	Role/permission changes
	•	Admin actions
	•	Audit logs
	•	Access logs

Network Logs
	•	Firewall logs
	•	Router logs
	•	VPN logs
	•	DNS logs
	•	Proxy logs
	•	NetFlow / traffic logs
	•	IDS/IPS logs
	•	Cloudflare logs
	•	WAF logs
	•	Load balancer logs

Infrastructure Logs
	•	Server system logs
	•	Container logs
	•	Kubernetes logs
	•	Database logs
	•	Backup logs
	•	Scheduler logs
	•	Deployment logs
	•	Monitoring alerts

⸻

Log Types

Log Type	Description
Access Log	User or device access
Audit Log	Administrative actions
Security Log	Security events
Application Log	Backend / frontend events
System Log	OS / infrastructure
Network Log	Firewall / router / VPN
Detection Log	Detection engine results
Alert Log	Alert generation
Investigation Log	Case / investigation activity
Evidence Log	Evidence uploads
Error Log	Errors and exceptions
Performance Log	Performance metrics


⸻

Log Pipeline Architecture

Log Source
   ↓
Log Agent / Collector
   ↓
Log Ingestion API
   ↓
Message Queue (Kafka / PubSub)
   ↓
Log Processor / Enricher
   ↓
Log Storage
   ├─ Hot Storage (Search)
   ├─ Warm Storage
   └─ Cold Archive

Log Agent

Examples:
	•	Fluent Bit
	•	Fluentd
	•	Filebeat
	•	Vector
	•	Cloud logging agent

Responsibilities:
	•	Collect logs
	•	Add metadata
	•	Buffer logs
	•	Send logs securely
	•	Retry on failure

⸻

Log Storage Tiers

Hot Storage

Used for:
	•	Recent logs
	•	Search
	•	Detection engine
	•	Dashboards
	•	Incident response

Examples:
	•	Elasticsearch / OpenSearch
	•	ClickHouse
	•	Loki
	•	BigQuery
	•	PostgreSQL (small scale)

Retention:
	•	7–30 days

Warm Storage

Used for:
	•	Older logs
	•	Investigation
	•	Reporting

Retention:
	•	3–12 months

Cold Storage / Archive

Used for:
	•	Long-term retention
	•	Legal evidence
	•	Compliance
	•	Forensics

Examples:
	•	Object storage
	•	S3 / GCS / Azure Blob
	•	Glacier / Archive storage

Retention:
	•	1–7 years (depending on policy)

⸻

Log Schema (Standard Log Format)

All logs should follow a common structure.

Example JSON log:

{
  "timestamp": "2026-03-30T10:15:22Z",
  "log_type": "security",
  "event_type": "login_failed",
  "user_id": "user_123",
  "device_id": "device_456",
  "ip_address": "203.0.113.10",
  "location": "Tokyo",
  "severity": "medium",
  "action": "login",
  "status": "failed",
  "message": "Invalid password",
  "service": "auth-service",
  "trace_id": "abc123",
  "metadata": {
    "user_agent": "iOS",
    "attempt_count": 3
  }
}


⸻

Log Severity Levels

Level	Description
DEBUG	Detailed debugging
INFO	Normal operation
NOTICE	Important event
WARNING	Suspicious / unusual
ERROR	Error occurred
CRITICAL	Serious failure
ALERT	Immediate action required
EMERGENCY	System unusable


⸻

Security Requirements for Logging

Log Integrity
	•	Append-only logs
	•	Hash chain logs
	•	Signed logs
	•	Immutable storage
	•	Write-once storage
	•	Separate logging account/project

Access Control
	•	Logs are read-only for most users
	•	Only logging service can write logs
	•	Security team can view logs
	•	Audit access to logs

Log Encryption
	•	Encryption in transit (TLS)
	•	Encryption at rest
	•	Key management system (KMS)

⸻

Logging and Detection Integration

Logs are the primary input for the detection engine.

Logs → Detection Engine → Risk Score → Alert → Case → Investigation

Detection examples:
	•	Multiple login failures
	•	Access from unusual location
	•	Access at unusual time
	•	Device behavior anomaly
	•	Network anomaly
	•	Admin privilege change
	•	Evidence deletion attempt
	•	Log tampering attempt

⸻

Logging Architecture Diagram (Conceptual)

Devices / Apps / Network / Cloud
                ↓
           Log Collectors
                ↓
           Log Ingestion
                ↓
           Message Queue
                ↓
        Log Processing / Enrichment
                ↓
   ┌───────────────┬───────────────┬───────────────┐
   │   Hot Logs    │   Warm Logs   │   Cold Logs   │
   │ (Search)      │ (History)     │ (Archive)     │
   └───────────────┴───────────────┴───────────────┘
                ↓
      Detection / Analytics / Dashboard
                ↓
            Alerts / Reports


⸻

Summary

The NSD logging architecture provides:
	•	Centralized logging across all systems
	•	Security and audit logging
	•	Tamper-resistant storage
	•	Multi-tier log retention
	•	Search and analytics
	•	Detection engine input
	•	Incident investigation support
	•	Long-term evidence retention

Logging is one of the most critical components of the NSD system because:
No logs = No detection, No investigation, No evidence.

⸻
