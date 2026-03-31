⸻

NSD – Reports API

Overview

The Reports API generates investigation reports, incident summaries, statistics, and analytics for the NSD (Network Suspicious Detection) system.

Reports are used for:
	•	incident investigation summaries
	•	security reports
	•	operational statistics
	•	audit reports
	•	management reports
	•	compliance documentation
	•	evidence summaries
	•	device risk reports
	•	user activity reports
	•	alert trend analysis

The Reports API supports both on-demand report generation and scheduled reports.

⸻

Report Types

The system supports multiple report types.

Report Type	Description
incident_report	Investigation / incident report
alert_summary	Alert statistics
device_risk_report	Device risk overview
user_activity_report	User activity summary
audit_report	Audit trail report
evidence_report	Evidence summary
security_report	Security overview
system_report	System statistics
compliance_report	Compliance / policy report


⸻

Report Object

Report Structure

{
  "report_id": "REP-20260330-0001",
  "report_type": "incident_report",
  "title": "Night Access Incident Report",
  "description": "Investigation report for suspicious night access",
  "status": "completed",
  "created_at": "2026-03-30T10:00:00Z",
  "generated_at": "2026-03-30T10:05:00Z",
  "created_by": "USR-001",
  "organization_id": "ORG-001",
  "case_id": "CASE-20260330-0001",
  "file_url": "https://storage/reports/REP-20260330-0001.pdf",
  "format": "pdf"
}


⸻

Report Status

Status	Description
pending	Report requested
generating	Report is being generated
completed	Report ready
failed	Report generation failed
archived	Report archived


⸻

Reports API Endpoints

1. Generate Report

Generate a new report.

Endpoint

POST /api/reports

Request Body

{
  "report_type": "incident_report",
  "title": "Night Access Incident Report",
  "description": "Investigation summary",
  "case_id": "CASE-20260330-0001",
  "format": "pdf"
}

Response

{
  "report_id": "REP-20260330-0001",
  "status": "generating",
  "message": "Report generation started"
}


⸻

2. List Reports

Get a list of reports.

Endpoint

GET /api/reports

Query Parameters

Parameter	Description
report_type	Filter by type
status	Filter by status
case_id	Filter by case
created_by	Filter by creator
organization_id	Filter by organization
date_from	Start date
date_to	End date
page	Pagination
limit	Pagination


⸻

3. Get Report Details

Endpoint

GET /api/reports/{report_id}

Response

{
  "report_id": "REP-20260330-0001",
  "report_type": "incident_report",
  "title": "Night Access Incident Report",
  "description": "Investigation summary",
  "status": "completed",
  "created_at": "2026-03-30T10:00:00Z",
  "generated_at": "2026-03-30T10:05:00Z",
  "created_by": "USR-001",
  "case_id": "CASE-20260330-0001",
  "file_url": "https://storage/reports/REP-20260330-0001.pdf",
  "format": "pdf"
}


⸻

4. Download Report

Endpoint

GET /api/reports/{report_id}/download

Returns the generated report file (PDF / CSV / JSON).

⸻

5. Delete Report

Endpoint

DELETE /api/reports/{report_id}

Used for cleanup or retention policy management.

⸻

6. Schedule Report

Schedule recurring reports.

Endpoint

POST /api/reports/schedule

Request Body

{
  "report_type": "alert_summary",
  "schedule": "daily",
  "format": "pdf",
  "organization_id": "ORG-001"
}

Schedule Options

Schedule	Description
hourly	Every hour
daily	Daily
weekly	Weekly
monthly	Monthly


⸻

Report Generation Flow

Incident Report Flow

Case → Evidence → Alerts → Events → Report Generator → PDF Report

Alert Summary Flow

Alerts → Aggregation → Statistics → Report → Dashboard / PDF

Device Risk Report Flow

Devices → Risk Scores → Risk Trends → Report


⸻

Report Formats

Format	Usage
pdf	Investigation / official report
csv	Data export
json	API / integration
html	Dashboard preview


⸻

Example Incident Report Contents

An incident report may include:
	•	Case information
	•	Timeline
	•	Devices involved
	•	Users involved
	•	Alerts triggered
	•	Evidence files
	•	Investigation notes
	•	Risk analysis
	•	Final conclusion
	•	Recommended actions
	•	Audit trail
	•	Attachments

⸻

Permissions

Role	Permissions
admin	full access
analyst	generate / view reports
investigator	incident reports
auditor	audit reports
viewer	view reports only


⸻

Summary

The Reports API is responsible for:
	•	generating incident reports
	•	generating statistics and summaries
	•	exporting data
	•	supporting audits and compliance
	•	supporting management reporting
	•	scheduling periodic reports
	•	storing report files
	•	linking reports to cases and organizations

⸻

これで NSD API モジュールはほぼ揃った：
	1.	Authentication API
	2.	Users API
	3.	Devices API
	4.	Events API
	5.	Risk API
	6.	Alerts API
	7.	Case API
	8.	Evidence API
	9.	Reports API
	10.	Admin API
  
