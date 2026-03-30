⸻

NSD – Detection Pipeline Architecture

Overview

The Detection Pipeline is the core processing flow of NSD (Network / Neighborhood Suspicious Detection).
It is responsible for ingesting events, normalizing data, detecting suspicious behavior, calculating risk scores, and generating alerts.

The pipeline is designed to be scalable, modular, and near real-time, allowing the system to process data from networks, devices, logs, and sensors.

⸻

Detection Pipeline Flow

High Level Flow

Data Sources
    ↓
Ingestion Layer
    ↓
Normalization Layer
    ↓
Enrichment Layer
    ↓
Detection Engine
    ↓
Risk Scoring Engine
    ↓
Alert Engine
    ↓
Case Management / Storage

This pipeline ensures that raw data is transformed into actionable security alerts.

⸻

1. Data Sources

The system can ingest data from multiple sources:

Examples
	•	Network logs
	•	Firewall logs
	•	Cloud logs
	•	Authentication logs
	•	IoT sensors
	•	GPS trackers
	•	Cameras
	•	Access control systems
	•	Application logs
	•	API logs
	•	User activity logs

Example Events
	•	Login success / failure
	•	Device movement
	•	Door access
	•	Network connection
	•	File access
	•	Configuration change
	•	Admin operation
	•	Password reset
	•	Suspicious network traffic

⸻

2. Ingestion Layer

The Ingestion Layer collects data from external systems.

Methods
	•	REST API
	•	Log forwarder
	•	Syslog
	•	MQTT (IoT)
	•	Webhooks
	•	Batch upload
	•	Streaming (Kafka / Kinesis)

Responsibilities
	•	Accept incoming data
	•	Validate schema
	•	Add timestamp
	•	Add source identifier
	•	Push events into message queue

Output

Events are sent to a message queue for processing.

Data Source → Ingestion API → Message Queue


⸻

3. Normalization Layer

Different systems produce logs in different formats.
The normalization layer converts all events into a common schema.

Example Normalized Event

{
  event_id
  timestamp
  event_type
  user_id
  device_id
  location
  source_ip
  action
  status
  raw_log_reference
}

Responsibilities
	•	Parse logs
	•	Convert formats
	•	Standardize fields
	•	Validate required fields
	•	Remove malformed events

This step is critical for scalable detection logic.

⸻

4. Enrichment Layer

The enrichment layer adds additional context to events.

Enrichment Examples
	•	GeoIP lookup
	•	Device owner
	•	Organization info
	•	Known bad IP list
	•	User risk profile
	•	Time-of-day classification
	•	Location risk score
	•	Historical behavior baseline

Example

Before enrichment:

source_ip: 185.xxx.xxx.xxx

After enrichment:

source_ip: 185.xxx.xxx.xxx
country: RU
ip_risk_score: 80
known_malicious: true

This improves detection accuracy.

⸻

5. Detection Engine

The Detection Engine analyzes events and identifies suspicious behavior.

Detection methods may include:

Rule-Based Detection
	•	Multiple login failures
	•	Access outside business hours
	•	Impossible travel
	•	Repeated password resets
	•	Excessive API calls
	•	Admin privilege changes
	•	Access to sensitive files
	•	Device offline → sudden login
	•	Repeated human errors
	•	Unusual operation frequency

Behavior-Based Detection
	•	Deviation from normal login time
	•	Deviation from normal location
	•	Abnormal activity volume
	•	New device usage
	•	Unusual network destination
	•	Movement pattern anomaly
	•	Access pattern anomaly

The Detection Engine produces detections, not alerts yet.

⸻

6. Risk Scoring Engine

Each detection contributes to a risk score.

Example Risk Scoring

Event	Score
Login failure	+5
Login from new country	+40
Admin privilege change	+50
Access at midnight	+10
Known malicious IP	+70

Example Calculation

Total Risk Score = Sum of detection scores

Risk Levels

Score	Risk Level
0–20	Low
21–50	Medium
51–80	High
81+	Critical

Risk scoring allows prioritization of alerts.

⸻

7. Alert Engine

Alerts are generated when risk score or detection rules exceed thresholds.

Alert Types
	•	Security alert
	•	Suspicious behavior alert
	•	Device alert
	•	Network alert
	•	Location alert
	•	System alert
	•	Policy violation alert

Alert Channels
	•	Email
	•	SMS
	•	Push notification
	•	Dashboard alert
	•	Webhook
	•	Slack / Teams
	•	Incident management system

⸻

8. Case Management / Storage

When alerts are generated, the system can create investigation cases.

Stored Data
	•	Events
	•	Detections
	•	Risk scores
	•	Alerts
	•	Cases
	•	Evidence files
	•	Audit logs

This enables incident investigation and forensic analysis.

⸻

Detection Pipeline Architecture Diagram

                +------------------+
                |   Data Sources   |
                +------------------+
                          |
                          v
                +------------------+
                |  Ingestion Layer |
                +------------------+
                          |
                          v
                +------------------+
                | Normalization    |
                +------------------+
                          |
                          v
                +------------------+
                | Enrichment       |
                +------------------+
                          |
                          v
                +------------------+
                | Detection Engine |
                +------------------+
                          |
                          v
                +------------------+
                | Risk Scoring     |
                +------------------+
                          |
                          v
                +------------------+
                | Alert Engine     |
                +------------------+
                          |
                          v
                +------------------+
                | Case Management  |
                +------------------+


⸻

Pipeline Design Goals

1. Scalability

The system must handle large volumes of events.

2. Near Real-Time Detection

Alerts should be generated quickly.

3. Modular Architecture

Each component should be independent.

4. Auditability

All events and alerts must be traceable.

5. Extensibility

New detection rules and data sources should be easy to add.

6. Reliability

Events must not be lost.

⸻

Future Enhancements
	•	Machine learning anomaly detection
	•	User behavior modeling
	•	Device behavior modeling
	•	Graph-based relationship detection
	•	Automatic account isolation
	•	Automatic device quarantine
	•	Automated incident response
	•	Threat intelligence integration
	•	Predictive risk scoring

⸻

Summary

The Detection Pipeline is the core of the NSD system.

Ingest → Normalize → Enrich → Detect → Score → Alert → Investigate

This pipeline transforms raw logs and sensor data into actionable security intelligence.

⸻
