⸻

NSD – Devices API

Overview

The Devices API manages devices that send data to the NSD (Network Suspicious Detection) system.

Devices represent any source that can generate events, logs, telemetry, or activity data used for risk analysis and investigations.

Devices may include:
	•	IoT devices
	•	GPS trackers
	•	Cameras
	•	Mobile devices
	•	Network sensors
	•	Access control devices
	•	Servers
	•	Routers
	•	Cloud systems

The Devices API is responsible for the full lifecycle and management of devices in the NSD platform.

The API supports:
	•	device registration
	•	device listing and filtering
	•	device details retrieval
	•	device updates
	•	device status updates
	•	device ownership assignment
	•	device location assignment
	•	device activity tracking
	•	device risk score tracking
	•	device deactivation (soft delete)
	•	audit trail tracking

⸻

Device Object

Device Structure

{
  "device_id": "DEV-001",
  "device_name": "Front Gate Camera",
  "device_type": "camera",
  "status": "active",
  "risk_score": 12,
  "organization_id": "ORG-001",
  "location_id": "LOC-001",
  "owner_user_id": "USR-002",
  "ip_address": "192.168.1.10",
  "mac_address": "AA:BB:CC:DD:EE:FF",
  "last_seen_at": "2026-03-30T09:10:00Z",
  "created_at": "2026-03-01T10:00:00Z",
  "updated_at": "2026-03-30T09:10:00Z",
  "metadata": {
    "vendor": "Ubiquiti",
    "model": "UVC-G4",
    "firmware": "1.2.3"
  }
}


⸻

Device Status Values

Status	Description
active	Device is active and sending data
inactive	Device registered but not active
offline	Device not seen for a period
suspended	Device blocked due to risk
compromised	Device suspected compromised
decommissioned	Device retired / removed from service


⸻

Device Risk Score

Each device may have a risk score calculated based on:
	•	failed logins
	•	unusual activity time
	•	abnormal traffic
	•	location anomalies
	•	repeated errors
	•	suspicious behavior patterns
	•	linked alerts
	•	linked cases

Risk Score Levels

Score	Risk Level
0–20	Low
21–50	Medium
51–80	High
81–100	Critical


⸻

API Endpoints

Endpoint Summary

Method	Endpoint	Description
POST	/api/devices	Register device
GET	/api/devices	List devices
GET	/api/devices/{device_id}	Device details
PUT	/api/devices/{device_id}	Update device
PATCH	/api/devices/{device_id}/status	Update status
PATCH	/api/devices/{device_id}/risk	Update risk score
DELETE	/api/devices/{device_id}	Decommission device


⸻

Register Device

POST /api/devices

Register a new device.

Request

{
  "device_name": "Warehouse Door Sensor",
  "device_type": "sensor",
  "organization_id": "ORG-001",
  "location_id": "LOC-002",
  "owner_user_id": "USR-005",
  "ip_address": "10.0.0.25",
  "mac_address": "11:22:33:44:55:66",
  "metadata": {
    "vendor": "Bosch",
    "model": "DoorSensor X"
  }
}

Response

{
  "device_id": "DEV-009",
  "status": "active",
  "created_at": "2026-03-30T11:00:00Z"
}


⸻

List Devices

GET /api/devices

Query Parameters

Parameter	Description
status	Filter by device status
device_type	Filter by type
organization_id	Filter by organization
location_id	Filter by location
risk_min	Minimum risk score
risk_max	Maximum risk score
last_seen_from	Last seen start time
last_seen_to	Last seen end time

Example

GET /api/devices?status=active&device_type=camera


⸻

Get Device Details

GET /api/devices/{device_id}

Response

{
  "device_id": "DEV-001",
  "device_name": "Front Gate Camera",
  "device_type": "camera",
  "status": "active",
  "risk_score": 18,
  "location_id": "LOC-001",
  "last_seen_at": "2026-03-30T09:10:00Z"
}


⸻

Update Device

PUT /api/devices/{device_id}

Update device information.

{
  "device_name": "Front Gate Camera V2",
  "location_id": "LOC-003"
}


⸻

Update Device Status

PATCH /api/devices/{device_id}/status

{
  "status": "suspended",
  "reason": "Suspicious traffic detected"
}


⸻

Update Device Risk Score

PATCH /api/devices/{device_id}/risk

{
  "risk_score": 72,
  "reason": "Multiple failed logins detected"
}


⸻

Deactivate Device

DELETE /api/devices/{device_id}

Soft delete only:

status = decommissioned


⸻

Device Activity Tracking

The system should track the following activity metrics:
	•	last_seen_at
	•	total_events
	•	total_alerts
	•	total_cases
	•	last_alert_at
	•	last_risk_update_at

This information is useful for investigations, monitoring, and device behavior analysis.

⸻

Relationships

Devices are linked to multiple entities in the NSD system.

Entity	Relationship
Organization	Device belongs to organization
Location	Device installed at location
User	Device owner
Events	Device generates events
Alerts	Device can trigger alerts
Cases	Device can be investigated
Risk Scores	Device risk tracking
Audit Logs	Device changes logged


⸻

Device Lifecycle

Devices follow a lifecycle from registration to decommission.

Typical Lifecycle
	1.	Device registered
	2.	Device becomes active
	3.	Device sends events
	4.	Risk score changes
	5.	Alerts may be generated
	6.	Device linked to cases
	7.	Device suspended or compromised
	8.	Device decommissioned

Lifecycle Flow

registered → active → monitored → risk_detected → suspended/compromised → decommissioned


⸻

Security Considerations

The Devices API must enforce security controls:
	•	Only authorized users can register devices
	•	Device updates must be logged in audit logs
	•	Device status changes must be auditable
	•	Suspended or compromised devices may be automatically blocked
	•	API access requires authentication (JWT / API Key)
	•	Sensitive fields (IP, MAC) should be access controlled
	•	Device deletion must be logical (soft delete)

⸻

Audit Log Events

The following actions must generate audit log entries:

Action	Description
device_created	Device registered
device_updated	Device information updated
device_status_changed	Device status changed
device_risk_updated	Risk score updated
device_deactivated	Device decommissioned
device_owner_changed	Owner reassigned
device_location_changed	Location changed


⸻

Final Architecture Position

In the NSD system architecture, the device is the origin of most security events.

NSD Core Investigation Flow

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
Investigation
  ↓
Report

This flow represents the core investigation pipeline of the NSD platform.

⸻
