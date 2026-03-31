⸻

NSD – Case Management

Overview

The Case Management system is used to manage investigations related to suspicious events and alerts detected by the NSD (Network Suspicious Detection) platform.

When suspicious activity is detected and an alert is generated, operators may escalate the alert into an investigation case. The case management system allows investigators to track incidents, collect evidence, document findings, and manage the investigation lifecycle.

The case management system is a core component of NSD and provides auditability, traceability, and structured incident handling workflows.

⸻

Investigation Flow

The investigation workflow in NSD follows this general flow:

Device / User / Network
        ↓
       Event
        ↓
    Risk Score
        ↓
       Alert
        ↓
       Case
        ↓
   Investigation
        ↓
     Evidence
        ↓
      Report
        ↓
      Closed

This flow represents how suspicious activity progresses from detection to investigation and final resolution.

⸻

Case Lifecycle

A case moves through several lifecycle stages.

Case Status

Typical case statuses include:

Status	Description
open	Case created and under investigation
investigating	Investigation in progress
waiting_evidence	Waiting for additional evidence
escalated	Escalated to higher authority
resolved	Investigation completed
closed	Case officially closed
false_positive	Alert determined to be false positive


⸻

Case Priority

Cases can be assigned a priority level:

Priority	Description
low	Minor issue
medium	Requires investigation
high	Serious suspicious activity
critical	Immediate action required


⸻

Case Severity

Severity represents the impact level of the incident.

Severity	Description
low	Minimal impact
medium	Moderate impact
high	High impact
critical	Severe impact / security breach


⸻

Case Object Structure

Case Data Model

Example case object:

{
  "case_id": "CASE-20260330-0001",
  "title": "Repeated Night Access Attempts",
  "description": "Multiple failed logins detected during night hours",
  "status": "open",
  "priority": "high",
  "severity": "medium",
  "created_at": "2026-03-30T10:00:00Z",
  "updated_at": "2026-03-30T10:30:00Z",
  "assigned_to": "USR-002",
  "created_by": "system",
  "organization_id": "ORG-001"
}


⸻

Case Relationships

A case can be related to multiple entities in the system.

Case Relationships

Entity	Relationship
Alerts	A case may be created from one or more alerts
Events	Cases may reference related events
Devices	Devices involved in the incident
Users	Users involved in the incident
Evidence	Files, logs, images, recordings
Reports	Investigation reports
Audit Logs	Case activity history


⸻

Case Management Operations

The Case Management system supports the following operations:

Operation	Description
Create Case	Create a new investigation case
View Cases	List cases
Case Details	View case details
Update Case	Update case information
Assign Case	Assign investigator
Change Status	Update case status
Add Evidence	Attach evidence files
Add Notes	Add investigation notes
Link Alerts	Link alerts to case
Generate Report	Generate investigation report
Close Case	Close case
Audit Log	Track all changes


⸻

Case Notes

Investigators can add notes to document findings and investigation progress.

Example note structure:

{
  "note_id": "NOTE-001",
  "case_id": "CASE-20260330-0001",
  "author": "USR-002",
  "note": "Checked access logs and found repeated login attempts from unknown IP.",
  "created_at": "2026-03-30T11:00:00Z"
}


⸻

Evidence Management

Evidence may include:
	•	Log files
	•	Network captures
	•	Images
	•	Camera recordings
	•	GPS records
	•	System audit logs
	•	Email records
	•	Screenshots
	•	Configuration files
	•	Reports

Each evidence item should be linked to a case and stored securely.

⸻

Audit Trail

All case-related actions must be logged.

Audit log should record:

Field	Description
audit_id	Audit log ID
case_id	Related case
action	Action performed
user	User who performed action
timestamp	Time of action
old_value	Previous value
new_value	Updated value

This ensures full traceability for investigations.

⸻

Case Management Goals

The Case Management system is designed to:
	•	Provide structured investigation workflow
	•	Maintain evidence integrity
	•	Ensure auditability
	•	Support collaboration between investigators
	•	Track incident lifecycle
	•	Generate investigation reports
	•	Support legal / compliance requirements
	•	Maintain historical incident records
	•	Support multi-organization environments
	•	Enable incident analytics and reporting

⸻

Summary

The Case Management system is the investigation core of the NSD platform.

It connects alerts, events, evidence, investigators, and reports into a structured investigation workflow and ensures that suspicious incidents can be investigated, documented, and resolved in a controlled and auditable manner.

The case system transforms detection into actionable investigation and incident management.

⸻
