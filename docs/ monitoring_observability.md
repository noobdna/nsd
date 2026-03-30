⸻

NSD – Monitoring & Observability

Overview

This document describes the monitoring and observability architecture for the NSD (Network Suspicious Detection) system.

Monitoring and observability ensure that the system is:
	•	operational
	•	reliable
	•	secure
	•	auditable
	•	performant
	•	traceable during incidents

The observability platform collects metrics, logs, and traces from all system components and provides dashboards, alerts, and incident visibility.

⸻

Observability Goals

The NSD observability system is designed to:
	1.	Monitor system health
	2.	Monitor infrastructure and services
	3.	Monitor security events and anomalies
	4.	Detect failures and performance degradation
	5.	Provide audit visibility
	6.	Support incident investigation
	7.	Support capacity planning
	8.	Ensure SLA / uptime visibility
	9.	Provide operational dashboards
	10.	Enable automated alerting

⸻

Observability Pillars

NSD observability is built on three pillars:

1. Metrics

Numeric measurements over time.

Examples:
	•	CPU usage
	•	Memory usage
	•	Disk usage
	•	API latency
	•	API request rate
	•	Error rate
	•	Event ingestion rate
	•	Detection processing time
	•	Alert generation rate
	•	Database query latency
	•	Queue length
	•	Active users
	•	Active devices
	•	Risk score calculation time

2. Logs

Detailed event records.

Examples:
	•	API access logs
	•	Authentication logs
	•	Device activity logs
	•	Detection engine logs
	•	Alert lifecycle logs
	•	Case management logs
	•	Audit logs
	•	Security logs
	•	Database logs
	•	System logs
	•	Worker / background job logs

3. Traces

Request flow tracking across services.

Used to track:
	•	API request flow
	•	Detection pipeline flow
	•	Alert generation flow
	•	Evidence upload flow
	•	Report generation flow

Tracing helps identify:
	•	slow services
	•	bottlenecks
	•	failures
	•	service dependencies

⸻

Monitoring Scope

Infrastructure Monitoring

Monitors infrastructure health.

Includes:
	•	Servers
	•	Containers
	•	Databases
	•	Storage
	•	Network
	•	Load balancers
	•	Message queues
	•	IoT gateways
	•	Cameras / devices
	•	Cloud services

Metrics:
	•	CPU
	•	Memory
	•	Disk
	•	Network traffic
	•	Disk I/O
	•	Container health
	•	Node availability
	•	Database connections
	•	Replication status
	•	Storage usage

⸻

Application Monitoring

Monitors application behavior.

Includes:
	•	API servers
	•	Detection engine
	•	Alert system
	•	Case management system
	•	Report generator
	•	Notification system
	•	Dashboard frontend
	•	Background workers

Metrics:
	•	API latency
	•	Error rate
	•	Request rate
	•	Queue processing time
	•	Job failures
	•	Alert processing time
	•	Detection processing time
	•	Login success/failure rate
	•	Evidence upload time
	•	Report generation time

⸻

Security Monitoring

Monitors security events.

Includes:
	•	Login failures
	•	Suspicious activity
	•	Access policy violations
	•	Privilege changes
	•	Admin actions
	•	Data access
	•	File downloads
	•	Evidence access
	•	API abuse
	•	Brute force attempts
	•	Device anomalies
	•	Network anomalies

Security monitoring integrates with:
	•	NSD detection engine
	•	Alert system
	•	SIEM
	•	Audit logging system

⸻

Logging Architecture

Log Sources

Log sources include:
	•	API servers
	•	Detection engine
	•	Databases
	•	Devices
	•	Cameras
	•	IoT sensors
	•	Authentication services
	•	Cloud services
	•	Network devices
	•	Load balancers
	•	Operating systems
	•	Containers
	•	Background jobs

Log Pipeline

Typical log pipeline:

Applications / Devices / Servers
            ↓
        Log Collector
            ↓
        Log Pipeline
            ↓
        Log Storage
            ↓
        Search / Analytics
            ↓
        Dashboards / Alerts

Log collectors may include:
	•	Fluentd
	•	Logstash
	•	Vector
	•	Cloud logging agents

Log storage may include:
	•	Elasticsearch / OpenSearch
	•	Cloud logging services
	•	Data warehouse
	•	Object storage (long-term archive)

⸻

Metrics Architecture

Metrics pipeline:

Services / Infrastructure
            ↓
        Metrics Agent
            ↓
        Metrics Collector
            ↓
        Time Series Database
            ↓
        Dashboards
            ↓
        Alerts

Metrics tools may include:
	•	Prometheus
	•	Cloud Monitoring
	•	Datadog
	•	Grafana
	•	CloudWatch
	•	Azure Monitor
	•	Stackdriver

⸻

Distributed Tracing Architecture

Tracing pipeline:

Client Request
      ↓
   API Gateway
      ↓
   Backend API
      ↓
   Detection Engine
      ↓
   Database
      ↓
   Alert System
      ↓
   Notification Service

Tracing tools:
	•	OpenTelemetry
	•	Jaeger
	•	Zipkin
	•	Datadog APM
	•	New Relic

Tracing enables end-to-end visibility of system requests.

⸻

Alerting Strategy

Monitoring alerts are triggered when thresholds or anomalies are detected.

Infrastructure Alerts
	•	High CPU usage
	•	High memory usage
	•	Disk full
	•	Node down
	•	Database down
	•	Replication failure
	•	Network failure

Application Alerts
	•	High API error rate
	•	High latency
	•	Queue backlog
	•	Detection engine failure
	•	Alert system failure
	•	Notification failure
	•	Evidence upload failure

Security Alerts
	•	Multiple login failures
	•	Privilege escalation
	•	Suspicious device behavior
	•	Data exfiltration
	•	Unauthorized access
	•	API abuse
	•	Brute force attempts
	•	Anomalous activity detection

Alerts may be sent via:
	•	Email
	•	SMS
	•	Slack / Teams
	•	Push notifications
	•	PagerDuty
	•	Incident management system

⸻

Dashboards

Dashboards provide real-time system visibility.

Operations Dashboard

Shows:
	•	system health
	•	infrastructure metrics
	•	service status
	•	queue status
	•	ingestion rate
	•	alert rate
	•	active incidents

Security Dashboard

Shows:
	•	suspicious activity
	•	login failures
	•	anomalies
	•	alerts by severity
	•	high risk users
	•	high risk devices
	•	geographic anomalies

Business / Usage Dashboard

Shows:
	•	number of users
	•	number of devices
	•	events per day
	•	alerts per day
	•	cases per day
	•	investigation time
	•	system usage
	•	organization activity

⸻

Incident Monitoring & Response

Monitoring integrates with incident response workflows.

When incidents occur:
	1.	Alert triggered
	2.	Incident created
	3.	Operators notified
	4.	Logs and metrics reviewed
	5.	Investigation started
	6.	Evidence collected
	7.	Incident resolved
	8.	Post-incident review
	9.	Metrics and alerts adjusted

Monitoring data is critical for incident investigation and forensic analysis.

⸻

Retention Strategy

Monitoring data retention policy:

Data Type	Retention
Metrics	90 days
Logs	180 days
Security Logs	1–3 years
Audit Logs	3–7 years
Traces	30 days
Alerts	Permanent
Incidents	Permanent
Reports	Permanent

Long-term logs may be archived to cold storage.

⸻

High Level Observability Architecture

Devices / APIs / Services / Infrastructure
                ↓
         Metrics / Logs / Traces
                ↓
          Observability Platform
                ↓
     Dashboards / Alerts / Reports
                ↓
      Incident Response / Operations

Observability is a core part of the NSD platform and supports operations, security monitoring, investigations, and system reliability.

⸻

Summary

The NSD monitoring and observability system provides:
	•	Infrastructure monitoring
	•	Application monitoring
	•	Security monitoring
	•	Logging platform
	•	Metrics platform
	•	Distributed tracing
	•	Alerting system
	•	Dashboards
	•	Incident monitoring
	•	Forensic visibility
	•	Capacity planning
	•	SLA monitoring
	•	Auditability and traceability

Observability ensures the NSD system remains reliable, secure, and operational at scale.

⸻
