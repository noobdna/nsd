⸻

NSD – Operations Runbook

Overview

This document describes operational procedures for the NSD (Network Suspicious Detection) system.

The operations runbook provides guidance for:
	•	system monitoring
	•	alert handling
	•	incident response
	•	investigation workflow
	•	system maintenance
	•	backup and recovery
	•	security operations
	•	operational escalation procedures

This runbook is intended for system operators, security analysts, and administrators.

⸻

1. System Overview for Operators

NSD Operational Flow

Devices / Logs / Sensors
        ↓
   Event Ingestion API
        ↓
   Detection Engine
        ↓
   Alert System
        ↓
   Case Management
        ↓
   Evidence / Reports
        ↓
   Dashboard / Operators

Operators mainly interact with:
	•	Dashboard
	•	Alerts
	•	Cases
	•	Evidence
	•	Reports
	•	System Health
	•	Audit Logs

⸻

2. Daily Operations Checklist

Operators should perform the following checks daily.

Daily Checklist

Task	Description
Check system health	API, Detection Engine, DB
Review new alerts	Open alerts
Review high severity alerts	Immediate attention
Check ingestion status	Event ingestion volume
Review failed jobs	Detection / notification failures
Review audit logs	Unauthorized actions
Check storage usage	Evidence storage
Verify backups	Backup success
Review system errors	Logs and errors
Review active investigations	Open cases


⸻

3. System Health Monitoring

Components to Monitor

Component	What to Check
API	Response time / errors
Detection Engine	Processing delay
Database	CPU / disk / connections
Storage	Evidence storage capacity
Notification System	Email / SMS / Push
Dashboard	Availability
Ingestion Pipeline	Event delay
Backup System	Backup success
Audit Logging	Log ingestion

Health Status Levels

Status	Meaning
Healthy	System operating normally
Warning	Degraded performance
Critical	Service disruption
Down	Service unavailable


⸻

4. Alert Handling Procedure

Alert Handling Workflow

New Alert
   ↓
Review Alert Details
   ↓
Validate Alert (True / False Positive)
   ↓
Assign Severity & Priority
   ↓
Take Action
   ↓
Close Alert or Escalate to Case

Alert Response Guidelines

Severity	Action
Critical	Immediate investigation
High	Investigate within SLA
Medium	Review and monitor
Low	Log and monitor

Example Alert Types
	•	Multiple failed login attempts
	•	Access at unusual hours
	•	Device offline unexpectedly
	•	New device registered
	•	Location anomaly
	•	Suspicious network activity
	•	Repeated password reset
	•	Unauthorized admin action
	•	Data download spike
	•	Evidence deletion attempt

⸻

5. Case / Investigation Workflow

Case Lifecycle

Alert Escalated
      ↓
Case Created
      ↓
Assign Investigator
      ↓
Collect Evidence
      ↓
Analyze Activity
      ↓
Add Investigation Notes
      ↓
Determine Outcome
      ↓
Close Case
      ↓
Generate Report

Investigation Checklist
	•	Review related alerts
	•	Review device history
	•	Review user activity
	•	Check location data
	•	Check login history
	•	Check network logs
	•	Collect screenshots/logs/files
	•	Add investigation notes
	•	Determine incident type
	•	Document timeline
	•	Generate incident report

⸻

6. Incident Response Procedure

Incident Severity Levels

Severity	Description
SEV-1	Major security incident
SEV-2	Confirmed suspicious activity
SEV-3	Potential suspicious behavior
SEV-4	Minor issue
SEV-5	Informational

Incident Response Flow

Incident Detected
       ↓
Confirm Incident
       ↓
Containment
       ↓
Investigation
       ↓
Eradication
       ↓
Recovery
       ↓
Post Incident Review
       ↓
Incident Report

Containment Actions
	•	Disable user account
	•	Disable device
	•	Block IP address
	•	Revoke API keys
	•	Reset passwords
	•	Isolate network device
	•	Lock case evidence
	•	Enable increased logging

⸻

7. Backup and Recovery

Backup Policy

Data	Backup Frequency
Database	Daily
Evidence Files	Daily
Reports	Daily
Audit Logs	Daily
Configurations	Weekly
Rules	Weekly

Recovery Procedure

Database Recovery
	1.	Stop API
	2.	Restore database from backup
	3.	Verify data integrity
	4.	Restart services
	5.	Verify system functionality

Evidence Storage Recovery
	1.	Restore storage
	2.	Verify file integrity
	3.	Rebuild metadata index
	4.	Verify evidence links

⸻

8. Maintenance Procedures

Regular Maintenance

Task	Frequency
Security updates	Monthly
OS updates	Monthly
Database optimization	Monthly
Storage cleanup	Monthly
Log rotation	Weekly
Backup test	Monthly
Rule review	Monthly
Risk scoring tuning	Quarterly
Access review	Quarterly
Audit review	Quarterly


⸻

9. Security Operations

Security Monitoring

Operators should monitor:
	•	Unauthorized login attempts
	•	Privilege escalation
	•	Admin actions
	•	Evidence deletion
	•	Audit log tampering
	•	API abuse
	•	Unusual data exports
	•	System configuration changes
	•	Disabled logging
	•	New admin accounts

⸻

10. Escalation Procedures

Escalation Levels

Level	Escalate To
Level 1	System Operator
Level 2	Security Analyst
Level 3	Security Manager
Level 4	System Administrator
Level 5	Executive / Organization

Escalation Triggers
	•	Data breach suspected
	•	Evidence tampering
	•	System compromise
	•	Admin account compromise
	•	Database access breach
	•	Evidence deletion
	•	Logging disabled
	•	Multiple critical alerts
	•	Detection engine failure
	•	Backup failure
	•	Storage full
	•	API outage

⸻

11. Operational Metrics

Metrics to Track

Metric	Description
Alerts per day	Alert volume
Cases per week	Investigation workload
False positive rate	Detection accuracy
Mean time to detect	MTTD
Mean time to respond	MTTR
Mean time to close case	Investigation time
System uptime	Availability
Event ingestion rate	System load
Storage usage	Evidence growth
Notification delivery rate	Alert delivery success


⸻

12. Runbook Summary

Operator Responsibilities

Operators are responsible for:
	•	monitoring system health
	•	reviewing alerts
	•	managing cases
	•	collecting evidence
	•	responding to incidents
	•	maintaining system availability
	•	ensuring backups
	•	reviewing audit logs
	•	escalating incidents
	•	documenting investigations

The NSD system must remain auditable, reliable, and secure at all times.

⸻
