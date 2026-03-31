⸻

incident_response_runbook.md

Incident Response Runbook

1. Overview

This runbook describes the procedures for responding to security incidents detected by the NSD (Network Suspicious Detection) system.

The objectives are to:
	•	detect incidents quickly
	•	contain threats
	•	investigate and collect evidence
	•	recover systems safely
	•	document and learn from incidents

This runbook should be used by operators, security engineers, and administrators.

⸻

2. Incident Severity Levels

Severity	Description	Example
Critical	Active attack or data breach	Account takeover, malware spread
High	Confirmed suspicious activity	Multiple failed logins, abnormal access
Medium	Suspicious behavior	Unusual login time/location
Low	Minor anomaly	Single failed login
Info	Informational event	Normal system event


⸻

3. Incident Response Phases

Phase 1 – Detection

Incident is detected by:
	•	NSD detection engine
	•	Monitoring alerts
	•	User report
	•	Log analysis
	•	External notification

Actions
	1.	Alert generated
	2.	Alert assigned to operator
	3.	Initial review
	4.	Determine severity level
	5.	Create incident case

⸻

Phase 2 – Initial Triage

Checklist
	•	Who triggered the alert?
	•	What device/system?
	•	When did it happen?
	•	Where did access come from?
	•	How many events?
	•	Is it ongoing?
	•	Similar past alerts?

Initial Triage Actions
	•	Review logs
	•	Check user activity
	•	Check device status
	•	Check IP reputation
	•	Check recent changes
	•	Determine if false positive

Triage Result
	•	False Positive → Close alert
	•	Suspicious → Investigate
	•	Confirmed Incident → Escalate

⸻

Phase 3 – Containment

Goal: Stop the incident from spreading.

Containment Actions
	•	Disable user account
	•	Isolate device
	•	Block IP address
	•	Revoke API keys
	•	Reset passwords
	•	Stop suspicious processes
	•	Disable network access
	•	Block firewall rules
	•	Disable VPN session
	•	Suspend device credentials

Containment must be logged and auditable.

⸻

Phase 4 – Investigation

Investigation Steps
	1.	Collect logs
	2.	Collect evidence files
	3.	Identify timeline
	4.	Identify affected systems
	5.	Identify attacker entry point
	6.	Determine scope
	7.	Determine impact
	8.	Check data exfiltration
	9.	Check persistence mechanisms
	10.	Document findings

Evidence Examples
	•	Access logs
	•	Network logs
	•	Authentication logs
	•	System logs
	•	Screenshots
	•	Files
	•	Packet capture
	•	Database logs
	•	Cloud logs

All evidence must be stored securely and hashed.

⸻

Phase 5 – Eradication

Remove the root cause.

Examples
	•	Remove malware
	•	Patch vulnerability
	•	Rotate credentials
	•	Remove unauthorized accounts
	•	Reinstall compromised systems
	•	Update firewall rules
	•	Update security policies

⸻

Phase 6 – Recovery

Restore systems safely.

Recovery Steps
	1.	Restore systems from backup
	2.	Re-enable accounts
	3.	Monitor systems closely
	4.	Verify system integrity
	5.	Verify logs are working
	6.	Verify alerts are working
	7.	Return system to production

Recovery must be gradual and monitored.

⸻

Phase 7 – Post-Incident Review

After incident is resolved:

Post-Incident Actions
	•	Write incident report
	•	Timeline reconstruction
	•	Root cause analysis
	•	Detection improvement
	•	Rule tuning
	•	Security improvements
	•	Documentation update
	•	Training update
	•	Lessons learned meeting

⸻

4. Incident Response Flow

Alert Detected
      ↓
Initial Triage
      ↓
Is False Positive?
      ↓
  Yes → Close Alert
  No
      ↓
Containment
      ↓
Investigation
      ↓
Eradication
      ↓
Recovery
      ↓
Post-Incident Review
      ↓
Close Incident


⸻

5. Roles and Responsibilities

Role	Responsibility
Operator	Alert monitoring, triage
Security Analyst	Investigation
Incident Commander	Decision making
System Admin	System containment and recovery
Network Admin	Network containment
Forensics	Evidence collection
Management	Communication
Legal	Legal response
PR	External communication


⸻

6. Evidence Handling Rules

Evidence must:
	•	Not be modified
	•	Be hashed (SHA256)
	•	Be timestamped
	•	Be stored securely
	•	Have access logs
	•	Maintain chain of custody

Evidence Storage Examples:
	•	Secure storage server
	•	Object storage
	•	Evidence vault
	•	Encrypted storage

⸻

7. Communication Plan

Severity	Notify
Critical	Security Lead, Management, Legal
High	Security Team
Medium	Operator
Low	Logged only

Communication Channels:
	•	Email
	•	Slack / Teams
	•	Incident Dashboard
	•	Phone (Critical only)

⸻

8. Incident Checklist

Quick Response Checklist
	•	Confirm alert
	•	Determine severity
	•	Create incident case
	•	Assign owner
	•	Containment started
	•	Evidence collected
	•	Investigation started
	•	Root cause identified
	•	Systems recovered
	•	Report written
	•	Incident closed

⸻

9. Incident Timeline Template

Time	Event
10:01	Alert triggered
10:05	Triage started
10:12	Incident confirmed
10:20	Account disabled
11:30	Investigation started
14:00	Root cause found
Next day	Recovery completed


⸻

10. Summary

The incident response process consists of:
	1.	Detection
	2.	Triage
	3.	Containment
	4.	Investigation
	5.	Eradication
	6.	Recovery
	7.	Post-Incident Review

A well-defined runbook ensures:
	•	faster response
	•	consistent handling
	•	proper evidence collection
	•	reduced damage
	•	continuous security improvement

⸻
