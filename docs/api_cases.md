# NSD – Case API

## Overview

The Case API manages investigation cases created from alerts.

When suspicious activity is confirmed or requires deeper investigation, alerts can be escalated into cases. Cases are used to track investigations, evidence, notes, status changes, assignments, and final outcomes.

The Case API supports:

- case creation
- case listing
- case details retrieval
- case status updates
- case assignment
- linking alerts to cases
- adding evidence
- adding investigation notes
- case closure
- audit trail tracking

---

## Case Object

### Case Structure

```json
{
  "case_id": "CASE-20260330-0001",
  "title": "Suspicious Night Access Investigation",
  "description": "Repeated night access and failed logins detected",
  "status": "open",
  "priority": "high",
  "severity": "medium",
  "created_at": "2026-03-30T10:00:00Z",
  "updated_at": "2026-03-30T10:20:00Z",
  "assigned_to": "USR-002",
  "created_by": "system",
  "organization_id": "ORG-001",
  "related_alerts": [
    "ALT-20260330-0001",
    "ALT-20260330-0002"
  ]
}

Field Notes

Field	Type	Description
case_id	string	Unique case identifier
title	string	Short case title
description	string	Investigation summary
status	string	Current case status
priority	string	Operational urgency
severity	string	Business or security impact
created_at	datetime	Case creation timestamp
updated_at	datetime	Last update timestamp
assigned_to	string	Assigned investigator user ID
created_by	string	User or system that created the case
organization_id	string	Related organization ID
related_alerts	array[string]	Alerts linked to the case


⸻

Case Status

Case Status Values

Status	Description
open	Case created but not yet investigated
investigating	Investigation is in progress
waiting	Waiting for additional information or dependency
resolved	Investigation completed and issue resolved
closed	Case formally closed
escalated	Escalated to higher authority or another team


⸻

Case Priority

Priority Values

Priority	Description
low	Minor issue
medium	Needs investigation
high	Serious issue
critical	Immediate response required


⸻

API Endpoints

1. Create Case

POST /api/cases

Request

{
  "title": "Suspicious Login Attempts",
  "description": "Multiple failed login attempts and unusual login time",
  "priority": "high",
  "severity": "medium",
  "assigned_to": "USR-002",
  "related_alerts": [
    "ALT-20260330-0001"
  ]
}

Response

{
  "case_id": "CASE-20260330-0001",
  "status": "open",
  "created_at": "2026-03-30T10:00:00Z"
}

Notes
	•	A case may be created manually or from an alert escalation workflow.
	•	All linked alerts should belong to the same organization.
	•	Case creation should be recorded in the audit trail.

⸻

2. List Cases

GET /api/cases

Query Parameters

Parameter	Description
status	Filter by case status
priority	Filter by priority
assigned_to	Filter by assigned investigator
organization_id	Filter by organization
date_from	Start date
date_to	End date

Example

GET /api/cases?status=open&priority=high

Example Response

{
  "items": [
    {
      "case_id": "CASE-20260330-0001",
      "title": "Suspicious Login Attempts",
      "status": "open",
      "priority": "high",
      "severity": "medium",
      "assigned_to": "USR-002",
      "created_at": "2026-03-30T10:00:00Z"
    },
    {
      "case_id": "CASE-20260330-0002",
      "title": "Unusual Device Activity",
      "status": "open",
      "priority": "high",
      "severity": "high",
      "assigned_to": "USR-005",
      "created_at": "2026-03-30T11:20:00Z"
    }
  ],
  "total": 2
}


⸻

3. Get Case Details

GET /api/cases/{case_id}

Response

{
  "case_id": "CASE-20260330-0001",
  "title": "Suspicious Login Attempts",
  "description": "Multiple failed login attempts",
  "status": "investigating",
  "priority": "high",
  "severity": "medium",
  "assigned_to": "USR-002",
  "related_alerts": [
    "ALT-20260330-0001"
  ],
  "evidence_count": 3,
  "notes_count": 5,
  "created_at": "2026-03-30T10:00:00Z",
  "updated_at": "2026-03-30T10:45:00Z"
}

Notes
	•	This endpoint returns summary-level case details.
	•	Full evidence and note contents should be retrieved via the Evidence API and Notes API, if separated.

⸻

4. Update Case Status

PATCH /api/cases/{case_id}/status

Request

{
  "status": "investigating"
}

Response

{
  "case_id": "CASE-20260330-0001",
  "status": "investigating",
  "updated_at": "2026-03-30T10:30:00Z"
}

Notes
	•	Status transitions should be validated by business rules.
	•	All status changes should be captured in the audit trail.

⸻

5. Assign Case

PATCH /api/cases/{case_id}/assign

Request

{
  "assigned_to": "USR-005"
}

Response

{
  "case_id": "CASE-20260330-0001",
  "assigned_to": "USR-005",
  "updated_at": "2026-03-30T10:32:00Z"
}

Notes
	•	Only valid investigator accounts should be assignable.
	•	Assignment changes should be recorded in the audit log.

⸻

6. Link Alert to Case

POST /api/cases/{case_id}/alerts

Request

{
  "alert_id": "ALT-20260330-0003"
}

Response

{
  "case_id": "CASE-20260330-0001",
  "alert_id": "ALT-20260330-0003",
  "linked": true
}

Notes
	•	The API should reject duplicate alert links.
	•	Only alerts from the same organization should be linkable.
	•	Linking activity should be recorded in the audit trail.

⸻

7. Close Case

POST /api/cases/{case_id}/close

Request

{
  "resolution": "Unauthorized access attempt confirmed. Password reset and account locked.",
  "closed_by": "USR-001"
}

Response

{
  "case_id": "CASE-20260330-0001",
  "status": "closed",
  "closed_at": "2026-03-30T12:00:00Z",
  "closed_by": "USR-001"
}

Notes
	•	A closed case should normally include a resolution summary.
	•	Reopening policy should be defined separately if supported.
	•	Closure events must be recorded in the audit trail.

⸻

Case Investigation Flow

Investigation Workflow

Alert Generated
      ↓
Alert Reviewed
      ↓
Escalate to Case
      ↓
Case Created
      ↓
Assign Investigator
      ↓
Collect Evidence
      ↓
Investigation Notes
      ↓
Resolution
      ↓
Case Closed


⸻

Related APIs

API	Purpose
Alerts API	Alert management
Evidence API	Evidence storage
Report API	Incident reporting
Audit API	Audit log tracking
Users API	Investigator management


⸻

Summary

The Case API is responsible for managing investigations and incident tracking.

Main Responsibilities
	•	manage investigation cases
	•	link alerts to cases
	•	track investigation progress
	•	store evidence and notes
	•	manage case status and assignment
	•	maintain audit trail
	•	support incident reporting

The Case API represents the investigation workflow layer of the NSD system.

