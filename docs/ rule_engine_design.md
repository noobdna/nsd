NSD – Rule Engine Design

⸻

Overview

The Rule Engine is responsible for evaluating incoming events and determining whether they match suspicious behavior patterns.
It is a core component of the Detection Engine and transforms raw events into risk signals, alerts, and cases.

The Rule Engine must support:
	•	Real-time rule evaluation
	•	Behavioral detection
	•	Threshold-based alerts
	•	Rule versioning
	•	Rule testing / simulation
	•	Multi-tenant rule isolation
	•	Auditability

⸻

Rule Engine Architecture

Event Stream
     ↓
Event Normalizer
     ↓
Rule Engine
     ↓
Risk Scoring Engine
     ↓
Alert Engine
     ↓
Case Management

The Rule Engine evaluates normalized events and produces rule matches and risk signals.

⸻

Rule Types

The system supports multiple rule types.

1. Threshold Rules

Triggered when a value exceeds a defined threshold.

Examples:
	•	Login failures > 5 within 10 minutes
	•	Password reset attempts > 3 per hour
	•	Access attempts from > 3 countries in 24h
	•	File downloads > 100 in 1 hour

⸻

2. Frequency Rules

Triggered when an action happens too frequently.

Examples:
	•	Same user login attempts every few seconds
	•	Door access repeated many times
	•	Same API called repeatedly
	•	Same GPS location ping spam

⸻

3. Sequence Rules

Triggered when a suspicious sequence of events occurs.

Examples:
	•	Login success → Password change → Data export
	•	Login failure → Login success from different country
	•	Account created → Privilege escalation → API key creation
	•	Device offline → Device online → Configuration change

⸻

4. Behavior Rules

Triggered when behavior deviates from normal patterns.

Examples:
	•	Login time outside normal hours
	•	Access from unusual location
	•	Abnormal data transfer volume
	•	Unusual device usage pattern

⸻

5. Correlation Rules

Triggered when multiple related events occur across systems.

Examples:
	•	VPN login + Office login from different country
	•	Network scan + Failed login attempts
	•	Malware alert + Privilege escalation
	•	Camera motion + Door access at night

⸻

Rule Definition Structure

Rules are defined in a structured format such as JSON or YAML.

Example rule:

{
  "rule_id": "RULE_LOGIN_FAILURE_BURST",
  "name": "Multiple Login Failures",
  "description": "Detect multiple login failures in short period",
  "event_type": "login_failure",
  "threshold": 5,
  "time_window": "10m",
  "severity": "medium",
  "risk_score": 30,
  "enabled": true
}


⸻

Rule Evaluation Flow
	1.	Event received
	2.	Event normalized
	3.	Relevant rules loaded
	4.	Rule conditions evaluated
	5.	If rule matched:
	•	Rule match recorded
	•	Risk score generated
	•	Alert generated (if threshold reached)
	6.	Send to Case Management

⸻

Rule Matching Logic

Each rule consists of conditions.

Example condition logic:

IF
    event.type == "login_failure"
AND
    count(user.login_failure, 10 minutes) > 5
THEN
    trigger alert

More complex example:

IF
    login_success
AND
    previous_event == login_failure
AND
    country_changed == true
THEN
    high risk alert


⸻

Rule Engine Components

Rule Loader
	•	Loads rules from database
	•	Supports rule versioning
	•	Caches active rules
	•	Supports hot reload

Rule Evaluator
	•	Evaluates event against rules
	•	Supports threshold, sequence, behavior, correlation rules

State Store

Stores temporary state for rule evaluation:
	•	Counters
	•	Sliding windows
	•	Event sequences
	•	Behavior baselines

Can use:
	•	Redis
	•	In-memory store
	•	Stream processor state store

Rule Match Recorder

Records rule matches:
	•	rule_id
	•	event_id
	•	timestamp
	•	risk_score
	•	matched_conditions

⸻

Rule Versioning

Rules must be version controlled.

Example:

rule_id	version	enabled	created_at
LOGIN_FAIL	v1	false	2025
LOGIN_FAIL	v2	true	2026

This allows:
	•	Rule rollback
	•	Rule testing
	•	Historical audit
	•	Rule tuning

⸻

Rule Severity Levels

Severity	Description
Low	Suspicious but minor
Medium	Suspicious activity
High	Likely malicious
Critical	Confirmed attack

Severity affects:
	•	Risk score
	•	Alert priority
	•	Notification method
	•	Auto-response actions

⸻

Rule Engine Data Flow Example

Example scenario:

User login failure x5
        ↓
Threshold rule matched
        ↓
Risk score +30
        ↓
Another rule matched (login from new country)
        ↓
Risk score +40
        ↓
Total risk score = 70
        ↓
Alert generated
        ↓
Case created


⸻

Performance Considerations

The Rule Engine must handle high event throughput.

Design considerations:
	•	Rule caching
	•	Event partitioning by user/device
	•	Sliding window counters
	•	Stream processing (Kafka / Kinesis)
	•	Redis for counters
	•	Horizontal scaling
	•	Async processing
	•	Batch rule evaluation for analytics
	•	Real-time evaluation for alerts

⸻

Future Enhancements
	•	Machine learning anomaly detection
	•	Adaptive thresholds
	•	User behavior profiling
	•	Rule simulation mode
	•	Rule testing environment
	•	Visual rule editor
	•	Auto rule generation
	•	Threat intelligence integration
	•	MITRE ATT&CK mapping
	•	Automated response actions

⸻

Summary

The Rule Engine is the brain of the detection system.

It:
	•	Evaluates events
	•	Applies detection rules
	•	Generates risk scores
	•	Triggers alerts
	•	Feeds case management
	•	Enables behavioral detection
	•	Supports real-time security monitoring

