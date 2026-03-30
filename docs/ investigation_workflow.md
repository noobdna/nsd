⸻

NSD – Investigation Workflow

Overview

This document describes the investigation workflow in the NSD (Network Suspicious Detection) system.

The investigation workflow defines how suspicious events are detected, reviewed, escalated, investigated, and resolved. The workflow ensures that all alerts and cases are handled consistently, auditable, and traceable.

The investigation process follows this general flow:

Event → Risk Score → Alert → Case → Investigation → Report → Closure

This workflow allows operators and investigators to manage suspicious activities systematically.

⸻

Investigation Workflow Stages

1. Event Detection

Events are generated from multiple sources:
	•	IoT devices
	•	GPS trackers
	•	cameras
	•	network logs
	•	authentication logs
	•	access control systems
	•	cloud logs
	•	user activity logs
	•	sensors

Each event includes:
	•	timestamp
	•	device
	•	user (optional)
	•	location
	•	event type
	•	event data
	•	severity indicator (optional)

These events are stored in the events table.

⸻

2. Risk Scoring

After an event is ingested, the Detection Engine evaluates the event and assigns a risk score.

Risk score is calculated based on:
	•	repeated failed logins
	•	unusual access time
	•	unusual location
	•	abnormal activity frequency
	•	device risk history
	•	user risk history
	•	rule matches
	•	anomaly detection
	•	blacklist / watchlist matches

Risk score range example:

Risk Score	Meaning
0–20	Normal
21–40	Low Risk
41–60	Medium Risk
61–80	High Risk
81–100	Critical

If the risk score exceeds a threshold, an alert is generated.

⸻

3. Alert Generation

An alert is created when:
	•	risk score exceeds threshold
	•	detection rule is triggered
	•	anomaly detection is triggered
	•	blacklist match occurs
	•	geofence violation occurs
	•	impossible travel detected
	•	device tampering detected
	•	sensor abnormal behavior detected

Alert includes:
	•	alert_id
	•	timestamp
	•	severity
	•	priority
	•	risk_score
	•	related event
	•	device
	•	user
	•	location
	•	description
	•	status
	•	assigned_to

Alert status flow:

open → in_review → escalated → closed → false_positive

⸻

4. Alert Review (Operator Stage)

An operator reviews alerts from the dashboard.

Operator actions:
	•	view alert details
	•	view related events
	•	view device history
	•	view user history
	•	add comments
	•	change priority
	•	assign alert
	•	mark false positive
	•	escalate to case

Decision options:

Decision	Action
False Positive	Close alert
Monitor	Keep alert open
Investigate	Escalate to case
Immediate Action	Escalate high priority case


⸻

5. Case Creation

If deeper investigation is required, an alert is escalated to a case.

Case includes:
	•	case_id
	•	title
	•	description
	•	severity
	•	priority
	•	status
	•	assigned investigator
	•	related alerts
	•	related devices
	•	related users
	•	related locations
	•	evidence
	•	investigation notes
	•	timeline
	•	actions taken
	•	final report

Case status flow:

open → investigating → pending → resolved → closed

⸻

6. Investigation Phase

During investigation, investigators perform:
	•	log analysis
	•	device activity review
	•	user activity review
	•	location tracking
	•	timeline reconstruction
	•	evidence collection
	•	interview notes (if physical security)
	•	incident classification
	•	root cause analysis
	•	impact analysis
	•	mitigation actions

Evidence examples:
	•	logs
	•	images
	•	videos
	•	GPS tracks
	•	network captures
	•	configuration snapshots
	•	audit logs
	•	screenshots
	•	documents

All investigation actions should be logged in audit_logs.

⸻

7. Incident Report

After investigation is completed, an incident report is generated.

Report includes:
	•	incident summary
	•	timeline
	•	affected systems
	•	affected users
	•	root cause
	•	attacker behavior (if applicable)
	•	impact assessment
	•	actions taken
	•	recommendations
	•	prevention measures
	•	lessons learned

Reports are stored in the reports table.

⸻

8. Case Closure

Case can be closed when:
	•	investigation completed
	•	report generated
	•	mitigation completed
	•	evidence stored
	•	approvals completed

Closure types:

Closure Type	Description
confirmed incident	confirmed malicious activity
policy violation	internal violation
user error	human mistake
system error	system malfunction
false positive	not suspicious
unresolved	insufficient evidence


⸻

Workflow Summary Diagram

Investigation workflow summary:

Event
  ↓
Risk Scoring
  ↓
Alert
  ↓
Alert Review
  ↓
Escalate?
  ├─ No → Close Alert
  └─ Yes
        ↓
       Case
        ↓
   Investigation
        ↓
   Incident Report
        ↓
     Closure


⸻

Roles in Investigation Workflow

Role	Responsibilities
Operator	Monitor alerts
Analyst	Investigate alerts
Investigator	Handle cases
Admin	Manage rules and system
Auditor	Review logs and reports
Manager	Approve closures


⸻

Key Principles

The investigation workflow is designed with the following principles:
	•	Traceability
	•	Auditability
	•	Evidence preservation
	•	Role-based access control
	•	Standardized workflow
	•	Incident documentation
	•	Chain of custody
	•	Reproducibility
	•	Security and privacy compliance
	•	Scalability for large environments

⸻

Investigation Workflow Data Flow

Workflow data relationships:

Device → Event → Risk Score → Alert → Case → Evidence → Report
                      ↓
                   Audit Log

This structure ensures all suspicious activity can be traced from the original event to the final investigation report.

⸻

Conclusion

The NSD investigation workflow provides a structured process for handling suspicious activity from detection to investigation and closure.

The workflow ensures that:
	•	alerts are properly reviewed
	•	serious incidents are investigated
	•	evidence is preserved
	•	actions are documented
	•	reports are generated
	•	incidents are traceable
	•	the system remains auditable

This workflow forms the operational backbone of the NSD platform.

⸻
