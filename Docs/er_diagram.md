⸻

NSD – ER Diagram

Overview

This document describes the Entity Relationship (ER) structure for the NSD (Network Suspicious Detection) database.

The NSD data model is designed around the investigation flow:

Organization → Users → Devices → Events → Alerts → Cases → Evidence → Reports

The system must support audit logs, risk scoring, rule engines, and multi-tenant environments.

⸻

Core Entities

Main entities in the NSD system:

Entity	Description
Organization	Tenant / company / group
User	System users / operators
Device	IoT, camera, GPS, network device
Location	Physical or logical location
Event	Raw logs / telemetry / activity
Risk Score	Risk evaluation result
Alert	Suspicious activity alert
Case	Investigation case
Evidence	Files / logs / images
Report	Investigation report
Rule	Detection rules
Audit Log	System activity logs


⸻

Main Relationships

High-Level Relationships

Organization
    ├── Users
    ├── Devices
    ├── Locations
    └── Cases

Users
    ├── Alerts (assigned_to)
    ├── Cases (assigned_to)
    └── Audit Logs

Devices
    ├── Events
    ├── Alerts
    └── Risk Scores

Events
    ├── Risk Scores
    └── Alerts

Alerts
    └── Cases

Cases
    ├── Evidence
    └── Reports


⸻

ER Diagram (Text Version)

[Organization]
      |
      | 1
      |
      | N
   [User]
      |
      | N
      |
   [AuditLog]

[Organization] 1 ─── N [Device] 1 ─── N [Event] 1 ─── 1 [RiskScore]
                                         |
                                         N
                                         |
                                      [Alert] N ─── 1 [Case]
                                                        |
                                                        N
                                                        |
                                                   [Evidence]
                                                        |
                                                        N
                                                        |
                                                     [Report]

[Location] 1 ─── N [Device]
[Location] 1 ─── N [Event]


⸻

Relationship Details

Organization Relationships

Parent	Child
Organization	Users
Organization	Devices
Organization	Locations
Organization	Cases


⸻

Device Relationships

Parent	Child
Device	Events
Device	Risk Scores
Device	Alerts


⸻

Event Flow Relationships

This is the most important chain in NSD:

Device → Event → Risk Score → Alert → Case → Evidence → Report

This represents the full investigation lifecycle.

⸻

Investigation Flow ER Chain

Step	Entity	Description
1	Device	Source of activity
2	Event	Raw activity / logs
3	Risk Score	Risk evaluation
4	Alert	Suspicious detection
5	Case	Investigation
6	Evidence	Collected evidence
7	Report	Final report


⸻

Simplified ER Flow Diagram

Device
   ↓
Event
   ↓
Risk Score
   ↓
Alert
   ↓
Case
   ↓
Evidence
   ↓
Report

This pipeline is the core data model of NSD.

⸻

Multi-Tenant Structure

NSD is designed to support multi-tenant environments.

Organization
   ├── Users
   ├── Devices
   ├── Locations
   ├── Alerts
   ├── Cases
   └── Reports

All major entities should include:

organization_id
created_at
updated_at
created_by


⸻

Key Design Principles

The ER model is designed based on the following principles:
	1.	Clear investigation workflow
	2.	Event-driven architecture
	3.	Multi-tenant ready
	4.	Auditability and traceability
	5.	Evidence preservation
	6.	Scalable event storage
	7.	Separation of raw data and investigation data
	8.	Risk-based detection model
	9.	Support for automation and rule engines
	10.	Future AI / behavior analysis support

⸻

Summary

The NSD ER model is centered around the investigation pipeline:

Organization
   ↓
Users / Devices / Locations
   ↓
Events
   ↓
Risk Scores
   ↓
Alerts
   ↓
Cases
   ↓
Evidence
   ↓
Reports
   ↓
Audit Logs

This structure allows NSD to function as:
	•	Security monitoring system
	•	Incident response platform
	•	Investigation management system
	•	Evidence management system
	•	Suspicious behavior detection platform

⸻

