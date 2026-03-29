⸻

backend/docs/iot_gps_integration.md

# NSD – IoT & GPS Integration

## Overview
This document describes how IoT devices, GPS trackers, cameras,
and sensors integrate with the NSD (Network Suspicious Detection) system.

The integration layer is responsible for receiving device data,
normalizing the data format, and sending it to the Detection Engine.

---

## Supported Devices

NSD can integrate with the following device types:

- GPS trackers
- Mobile devices
- IoT sensors
- Security cameras
- Vehicle trackers
- Wearable devices
- Environmental sensors
- Access control devices

Each device must be registered before sending data.

---

## Device Registration

Before a device can send data, it must be registered in the system.

Device registration includes:

- device_id
- device_type
- owner_user_id
- device_name
- firmware_version
- status
- registered_at

Example API:

POST /api/v1/devices/register

---

## Data Transmission Methods

Devices can send data using:

1. HTTPS REST API
2. MQTT
3. WebSocket
4. Batch upload
5. Edge gateway relay

Recommended method:
HTTPS REST API or MQTT.

---

## GPS Data Format

Example GPS data payload:

```json
{
  "device_id": "GPS-0001",
  "timestamp": "2026-03-29T12:00:00Z",
  "location": {
    "lat": 35.681236,
    "lng": 139.767125
  },
  "speed": 12.5,
  "direction": 180,
  "battery": 78,
  "status": "moving"
}


⸻

Event Data Format

Devices may also send event-based data.

Example event payload:

{
  "device_id": "CAM-0021",
  "timestamp": "2026-03-29T12:01:10Z",
  "event_type": "motion_detected",
  "location": {
    "lat": 35.681236,
    "lng": 139.767125
  },
  "metadata": {
    "confidence": 0.87,
    "image_url": "https://example.com/event/123.jpg"
  }
}


⸻

Data Flow

Device → API Gateway → Data Ingestion Service → Database → Detection Engine → Alert System → Dashboard

Flow steps:
	1.	Device sends data
	2.	API validates device
	3.	Data stored in database
	4.	Detection engine analyzes data
	5.	Risk score calculated
	6.	Alert generated if needed
	7.	Dashboard updated

⸻

Security Requirements

All device communication must follow security rules:
	•	HTTPS only
	•	API Key or Token authentication
	•	Device ID validation
	•	Rate limiting
	•	Data encryption
	•	Tamper detection
	•	Device certificate (optional)
	•	Audit logging

⸻

Edge Gateway (Optional)

In large deployments, devices may send data to an edge gateway first.

Flow:

Devices → Edge Gateway → Cloud API → NSD System

Edge gateway responsibilities:
	•	Data aggregation
	•	Temporary storage
	•	Offline buffering
	•	Data filtering
	•	Secure relay
	•	Local detection (optional)

⸻

Offline Handling

If a device loses connectivity:
	•	Store data locally
	•	Retry upload
	•	Send batch data when online
	•	Mark delayed data
	•	Raise device offline alert

⸻

Future Enhancements

Possible future features:
	•	Real-time video streaming
	•	AI object detection integration
	•	Vehicle tracking analytics
	•	Crowd movement detection
	•	Drone integration
	•	Satellite communication devices
	•	Emergency alert triggers

⸻

Summary

The IoT & GPS integration layer connects physical devices
to the NSD platform and provides location, event, and telemetry data
for suspicious behavior detection and alert generation.

---
