NSD – Events API

File: Docs/api_events.md

Overview

The Events API manages incoming events sent from devices, sensors, logs, applications, and external systems into the NSD (Network Suspicious Detection) platform.

Events represent raw activity data such as:
	•	login attempts
	•	GPS location updates
	•	camera detections
	•	network traffic logs
	•	access control logs
	•	system logs
	•	user activity
	•	IoT sensor readings

The Events API is the main ingestion point of the NSD system.
Events are later processed by the Detection Engine to calculate risk scores and generate alerts.

⸻

Event Flow in NSD

Device / System → Event API → Event Storage → Detection Engine → Risk Score → Alert → Case

⸻

Event Object

Event Structure

{
  "event_id": "EVT-20260330-0001",
  "timestamp": "2026-03-30T09:10:22Z",
  "event_type": "login_failed",
  "device_id": "DEV-001",
  "user_id": "USR-009",
  "organization_id": "ORG-001",
  "location_id": "LOC-001",
  "severity": "low",
  "source_ip": "192.168.10.45",
  "destination_ip": "192.168.10.10",
  "description": "Failed login attempt",
  "metadata": {
    "username": "admin",
    "attempt_count": 1,
    "protocol": "ssh"
  },
  "created_at": "2026-03-30T09:10:22Z"
}


⸻

Event Fields Description

Field	Description
event_id	Unique event ID
timestamp	Time when the event occurred
event_type	Type of event
device_id	Device that generated the event
user_id	Related user (optional)
organization_id	Organization
location_id	Physical or logical location
severity	low / medium / high
source_ip	Source IP address
destination_ip	Destination IP
description	Event description
metadata	Additional event-specific data
created_at	Event record creation time


⸻

Event Types Examples

Common event types supported by NSD:

Event Type	Description
login_success	Successful login
login_failed	Failed login
password_reset	Password reset
gps_update	GPS location update
motion_detected	Camera motion detection
door_open	Door access opened
door_denied	Access denied
network_connection	Network connection detected
system_error	System error
device_offline	Device offline
device_online	Device online
file_access	File accessed
config_change	Configuration change
api_access	API access
suspicious_behavior	Suspicious activity detected


⸻

API Endpoints

Create Event

POST /api/events

Creates a new event.

Request:

{
  "event_type": "login_failed",
  "device_id": "DEV-001",
  "user_id": "USR-009",
  "severity": "low",
  "source_ip": "192.168.10.45",
  "description": "Failed login attempt",
  "metadata": {
    "username": "admin"
  }
}

Response:

{
  "event_id": "EVT-20260330-0001",
  "status": "created"
}


⸻

List Events

GET /api/events

Query parameters:
	•	device_id
	•	user_id
	•	event_type
	•	severity
	•	start_time
	•	end_time
	•	organization_id
	•	location_id
	•	page
	•	limit

Example:

GET /api/events?device_id=DEV-001&event_type=login_failed


⸻

Event Details

GET /api/events/{event_id}

Returns full event details.

⸻

Update Event Severity

PATCH /api/events/{event_id}/severity

{
  "severity": "high"
}


⸻

Delete Event (Optional / Admin Only)

DELETE /api/events/{event_id}

Note: In many security systems, events are not deleted but archived.

⸻

Event Metadata Design

The metadata field allows flexible event-specific data.

Examples:

Login Event:

{
  "username": "admin",
  "protocol": "ssh",
  "port": 22
}

GPS Event:

{
  "latitude": 35.6895,
  "longitude": 139.6917,
  "speed": 40
}

Camera Event:

{
  "camera_id": "CAM-01",
  "image_url": "https://storage/events/img123.jpg"
}


⸻

Event Severity Levels

Severity	Meaning
low	Normal activity
medium	Suspicious activity
high	High risk activity
critical	Immediate action required


⸻

Event Retention Policy (Example)

Event Type	Retention
Normal events	90 days
Security events	1 year
Critical events	3 years
Investigation-related	Permanent


⸻

Audit Trail

All event changes must be logged.

Audit log example:

{
  "audit_id": "AUD-001",
  "entity": "event",
  "entity_id": "EVT-20260330-0001",
  "action": "update_severity",
  "old_value": "low",
  "new_value": "high",
  "changed_by": "USR-001",
  "timestamp": "2026-03-30T09:20:00Z"
}


⸻

Summary

The Events API is the ingestion backbone of the NSD system.

Responsibilities:
	•	receive events from devices and systems
	•	store events
	•	provide event search and retrieval
	•	support detection engine processing
	•	maintain audit trail
	•	support long-term investigation data

⸻

