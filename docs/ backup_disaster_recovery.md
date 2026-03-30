⸻

NSD – Backup & Disaster Recovery

Overview

This document describes the backup and disaster recovery (DR) strategy for the NSD (Network Suspicious Detection) system.

The goal of backup and disaster recovery is to ensure that the system can recover from failures such as hardware issues, software bugs, data corruption, cyber attacks, or cloud outages while minimizing data loss and downtime.

The backup and DR strategy covers:
	•	Database backups
	•	Evidence file backups
	•	Configuration backups
	•	Log backups
	•	Infrastructure recovery
	•	Disaster recovery procedures
	•	Recovery objectives

⸻

Backup Strategy

Data Types to Back Up

The NSD system stores several types of data that must be backed up.

Critical Data

Must be backed up frequently and stored securely.
	•	Users
	•	Organizations
	•	Devices
	•	Events
	•	Alerts
	•	Cases
	•	Evidence metadata
	•	Risk scores
	•	Rules
	•	Audit logs
	•	Reports

File Data

Stored separately from the main database.
	•	Evidence files
	•	Images
	•	Videos
	•	Log archives
	•	Report exports

Configuration Data

System configuration must also be backed up.
	•	Application configuration
	•	Environment variables
	•	API keys
	•	Certificates
	•	Infrastructure configuration
	•	Deployment scripts
	•	Detection rules
	•	Notification rules

⸻

Backup Types

1. Full Backup

A full backup contains the entire database and file storage.

Frequency:
	•	Daily full backup

Used for:
	•	Disaster recovery
	•	Full system restore
	•	Long-term archival

⸻

2. Incremental Backup

Incremental backups store only changes since the last backup.

Frequency:
	•	Every hour or every few hours

Used for:
	•	Minimizing data loss
	•	Faster backups
	•	Reduced storage usage

⸻

3. Snapshot Backup

Infrastructure snapshots capture the state of servers or databases at a specific time.

Examples:
	•	Database snapshots
	•	VM snapshots
	•	Storage snapshots

Frequency:
	•	Every 6–12 hours

⸻

Backup Storage Strategy

Backups must be stored in multiple locations.

Storage Locations
	1.	Primary Backup Storage
	•	Same cloud provider
	•	Fast restore
	2.	Secondary Backup Storage
	•	Different region
	•	Protect against regional failure
	3.	Offline / Cold Storage
	•	Long-term retention
	•	Ransomware protection
	•	Archive storage

⸻

Backup Retention Policy

Example retention policy:

Backup Type	Retention
Hourly	48 hours
Daily	30 days
Weekly	3 months
Monthly	1 year
Yearly	5 years

Retention should follow legal and audit requirements.

⸻

Recovery Objectives

RTO – Recovery Time Objective

RTO is the maximum acceptable downtime.

Example:
	•	Critical system: 1–4 hours
	•	Non-critical system: 24 hours

RPO – Recovery Point Objective

RPO is the maximum acceptable data loss window.

Example:
	•	Critical data: 1 hour
	•	Standard data: 6 hours
	•	Logs: 24 hours

⸻

Disaster Scenarios

The system should be able to recover from the following scenarios:
	•	Database failure
	•	Server failure
	•	Storage failure
	•	Cloud region outage
	•	Accidental data deletion
	•	Data corruption
	•	Ransomware attack
	•	Security breach
	•	Network outage
	•	Power outage
	•	Application deployment failure

⸻

Disaster Recovery Strategy

Recovery Environments

Two environments should exist:
	1.	Primary Environment
	2.	Disaster Recovery Environment

The DR environment may be:
	•	Warm standby
	•	Cold standby
	•	Hot standby

Cold Standby

Infrastructure created only during disaster.
Lowest cost, slow recovery.

Warm Standby

Infrastructure exists but scaled down.
Medium cost, medium recovery time.

Hot Standby

Fully running duplicate system.
Highest cost, fastest recovery.

⸻

Recovery Procedure (Example)

Database Recovery
	1.	Stop application
	2.	Restore database from latest backup
	3.	Apply incremental backups
	4.	Verify database integrity
	5.	Restart application
	6.	Monitor system

File Storage Recovery
	1.	Restore file storage from backup
	2.	Verify file integrity
	3.	Re-link files with database records

Full System Recovery
	1.	Provision infrastructure
	2.	Deploy application
	3.	Restore database
	4.	Restore file storage
	5.	Restore configuration
	6.	Update DNS / load balancer
	7.	Start services
	8.	Run health checks
	9.	Resume operations

⸻

Backup Security

Backups must be protected because they contain sensitive data.

Security measures:
	•	Encrypt backups
	•	Use separate backup accounts
	•	Restrict backup access
	•	Enable audit logging
	•	Use immutable backups (WORM)
	•	Protect against ransomware
	•	Rotate encryption keys
	•	Test backup restoration regularly

⸻

Backup Monitoring

Backup jobs must be monitored.

Monitoring should include:
	•	Backup success / failure alerts
	•	Backup duration monitoring
	•	Backup size anomalies
	•	Restore test results
	•	Storage capacity monitoring

Alerts should be generated if:
	•	Backup fails
	•	Backup not run
	•	Backup size abnormal
	•	Restore test fails

⸻

Backup Testing

Backups are useless if they cannot be restored.

Regular restore tests should be performed.

Testing schedule example:

Test Type	Frequency
File restore test	Monthly
Database restore test	Monthly
Full system restore	Quarterly
Disaster recovery drill	Yearly


⸻

Summary

The NSD backup and disaster recovery strategy ensures that:
	•	All critical data is backed up regularly
	•	Backups are stored in multiple locations
	•	Data can be restored within defined RTO
	•	Data loss is limited by RPO
	•	The system can recover from major disasters
	•	Backup data is encrypted and protected
	•	Backup restoration is tested regularly

A reliable backup and disaster recovery plan is essential for system reliability, security, and operational continuity.

⸻
