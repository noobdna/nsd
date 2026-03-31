⸻

NSD – Reporting & Reports Documentation

Overview

The Reporting system in NSD (Network Suspicious Detection) is responsible for generating investigation reports, incident summaries, operational statistics, and audit documentation.

Reports are used for:
	•	security incident documentation
	•	investigation summaries
	•	management reporting
	•	compliance and audit records
	•	operational metrics
	•	risk analysis summaries
	•	law enforcement / legal evidence documentation
	•	internal security reviews

The reporting system converts alerts, cases, evidence, audit logs, and risk data into structured reports.

⸻

Types of Reports

1. Incident Report

Used when a security incident or suspicious activity investigation is completed.

Includes:
	•	incident summary
	•	timeline
	•	affected devices/users
	•	alerts involved
	•	investigation notes
	•	evidence references
	•	actions taken
	•	final assessment
	•	recommendations

Typical use cases:
	•	unauthorized access
	•	suspicious login behavior
	•	device compromise
	•	insider threat investigation
	•	physical intrusion detection
	•	network anomaly investigation

⸻

2. Investigation Report

Generated during or after an investigation case.

Includes:
	•	case details
	•	investigators
	•	related alerts
	•	evidence collected
	•	activity timeline
	•	notes
	•	status history
	•	risk evaluation

⸻

3. Alert Summary Report

Summarizes alerts over a time period.

Examples:
	•	alerts per day
	•	alerts by severity
	•	alerts by location
	•	alerts by device
	•	alerts by user
	•	false positive rate
	•	escalated alerts

⸻

4. Risk Report

Summarizes risk scores and trends.

Includes:
	•	high risk devices
	•	high risk users
	•	risk score trends
	•	repeated suspicious behavior
	•	risk hotspots by location
	•	risk trend over time

⸻

5. Audit Report

Used for compliance and internal review.

Includes:
	•	user activity logs
	•	admin actions
	•	permission changes
	•	login history
	•	data access history
	•	system configuration changes
	•	case access logs
	•	evidence access logs

⸻

6. Operational Report

Used by system operators and administrators.

Includes:
	•	system uptime
	•	ingestion volume
	•	alerts generated
	•	cases opened
	•	cases closed
	•	average investigation time
	•	SLA compliance
	•	notification statistics

⸻

Report Data Sources

Reports are generated from multiple NSD components.

Data Sources
	•	Events
	•	Alerts
	•	Cases
	•	Evidence
	•	Audit Logs
	•	Risk Scores
	•	Devices
	•	Users
	•	Locations
	•	Notifications
	•	System Logs

Reports aggregate and summarize data across the system.

⸻

Report Generation Flow

Reporting Flow

Database / Logs / Evidence
            ↓
     Reporting Engine
            ↓
     Report Generator
            ↓
   PDF / JSON / CSV / Dashboard
            ↓
      Export / Email / Archive


⸻

Report Formats

Reports can be exported in multiple formats.

Supported Formats

PDF

Used for:
	•	incident reports
	•	investigation reports
	•	audit reports
	•	legal documentation

JSON

Used for:
	•	API integrations
	•	automation
	•	data exchange

CSV

Used for:
	•	statistics
	•	data analysis
	•	spreadsheets

Dashboard View

Used for:
	•	operational monitoring
	•	risk overview
	•	alert statistics

⸻

Report Object Structure

Report Object

{
  "report_id": "RPT-20260330-0001",
  "report_type": "incident",
  "title": "Unauthorized Access Investigation Report",
  "description": "Investigation of repeated failed logins and night access",
  "generated_at": "2026-03-30T12:00:00Z",
  "generated_by": "USR-001",
  "case_id": "CASE-20260330-0003",
  "time_range_start": "2026-03-25T00:00:00Z",
  "time_range_end": "2026-03-30T00:00:00Z",
  "format": "pdf",
  "status": "generated",
  "file_path": "/reports/2026/03/report_0001.pdf",
  "organization_id": "ORG-001"
}


⸻

Incident Report Structure

Typical Incident Report sections:

Incident Report Layout

1. Incident Summary
2. Incident Information
3. Timeline of Events
4. Alerts Involved
5. Devices / Users Involved
6. Investigation Actions
7. Evidence Collected
8. Risk Assessment
9. Root Cause Analysis
10. Actions Taken
11. Recommendations
12. Conclusion
13. Appendix (Logs / Evidence References)

This structure is important for audit and legal documentation.

⸻

Reporting Engine Responsibilities

The Reporting Engine should:
	•	collect data from multiple tables
	•	build timelines from events and alerts
	•	calculate statistics
	•	include evidence references
	•	include audit logs
	•	generate structured documents
	•	store generated reports
	•	allow exporting
	•	allow scheduled reports
	•	allow automated incident reports

⸻

Scheduled Reports

The system may generate reports automatically.

Examples

Daily Reports:
	•	alerts summary
	•	risk summary
	•	system activity

Weekly Reports:
	•	investigation summary
	•	incident summary
	•	operational metrics

Monthly Reports:
	•	risk trends
	•	audit report
	•	system usage
	•	security summary

⸻

Report Access Control

Reports may contain sensitive information.

Access should be restricted based on roles.

Example Permissions

Role	Permissions
Viewer	View reports
Analyst	Generate reports
Investigator	Generate incident reports
Admin	All reports
Auditor	Audit reports
Organization Admin	Org reports only


⸻

Report Retention Policy

Reports must be retained for evidence and compliance.

Example Retention

Report Type	Retention
Incident Reports	5–10 years
Investigation Reports	5 years
Audit Reports	7 years
Operational Reports	1–2 years
Alert Reports	1 year

Retention policies may depend on legal requirements.

⸻

Reporting System Summary

Reporting System Responsibilities

The NSD Reporting system provides:
	•	Incident reports
	•	Investigation reports
	•	Alert summaries
	•	Risk reports
	•	Audit reports
	•	Operational reports
	•	Scheduled reports
	•	Exportable reports
	•	Evidence documentation reports
	•	Compliance documentation
	•	Management reports

⸻

NSD System – Big Picture (Important)

At this point, NSD documentation structure is roughly:

Docs/
 ├── system_architecture.md
 ├── system_data_flow.md
 ├── er_diagram.md
 ├── database_design.md
 ├── detection_logic.md
 ├── alert_system.md
 ├── api_index.md
 ├── api_authentication.md
 ├── api_users.md
 ├── api_devices.md
 ├── api_events.md
 ├── api_alerts.md
 ├── api_cases.md
 ├── api_evidence.md
 ├── api_reports.md
 ├── api_admin.md
 ├── dashboard.md
 ├── investigation_workflow.md
 ├── risk_scoring.md
 ├── notification_system.md
 ├── audit_logging.md
 ├── data_retention.md
 ├── deployment_architecture.md
 ├── operations_runbook.md
 └── reporting.md   ← 今ここ


⸻
