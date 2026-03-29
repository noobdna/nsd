# NSD – Backend API Design

## Overview
This document describes the backend API design for NSD (Network Suspicious Detection).

The backend API is responsible for receiving device data, managing alerts and cases,
handling users and authentication, and providing data to the frontend dashboard.

---

## Main Responsibilities

The Backend API handles:

- Device registration
- Data ingestion from IoT / GPS / cameras / sensors
- Event storage and retrieval
- Risk scoring requests
- Alert generation and management
- Case management
- User and role management
- Dashboard data delivery
- Audit logging

---

## API Style

Recommended API style:

- REST API for standard business operations
- JSON request / response format
- HTTPS only
- Token-based authentication
- Role-based access control (RBAC)

Optional future extension:

- WebSocket for real-time alerts
- GraphQL for flexible dashboard queries

---

## Main API Modules

### 1. Authentication API
Handles login, token validation, and user session management.

Example endpoints:

- `POST /api/v1/auth/login`
- `POST /api/v1/auth/logout`
- `GET /api/v1/auth/me`

Main functions:

- User authentication
- Access token issuance
- Session validation
- Role verification

---

### 2. User Management API
Handles operator and admin user data.

Example endpoints:

- `GET /api/v1/users`
- `GET /api/v1/users/{user_id}`
- `POST /api/v1/users`
- `PUT /api/v1/users/{user_id}`
- `DELETE /api/v1/users/{user_id}`

Main functions:

- Create users
- Update user profiles
- Assign roles
- Enable / disable accounts

---

### 3. Device Management API
Handles registration and status management of GPS devices, cameras, and sensors.

Example endpoints:

- `GET /api/v1/devices`
- `GET /api/v1/devices/{device_id}`
- `POST /api/v1/devices`
- `PUT /api/v1/devices/{device_id}`
- `DELETE /api/v1/devices/{device_id}`

Main functions:

- Register new devices
- Update device metadata
- Check device status
- Associate devices with users or locations

---

### 4. Event Ingestion API
Receives raw event data from devices and external systems.

Example endpoints:

- `POST /api/v1/events`
- `GET /api/v1/events`
- `GET /api/v1/events/{event_id}`

Main functions:

- Receive event payloads
- Validate event schema
- Store raw event data
- Forward data to detection engine

Example event fields:

- device_id
- timestamp
- latitude
- longitude
- event_type
- raw_data

---

### 5. Detection / Risk API
Handles suspicious activity analysis and scoring results.

Example endpoints:

- `POST /api/v1/detection/evaluate`
- `GET /api/v1/risk-scores`
- `GET /api/v1/risk-scores/{score_id}`

Main functions:

- Trigger rule evaluation
- Calculate risk score
- Store evaluation result
- Return risk reasons

---

### 6. Alert Management API
Handles creation and lifecycle management of alerts.

Example endpoints:

- `GET /api/v1/alerts`
- `GET /api/v1/alerts/{alert_id}`
- `POST /api/v1/alerts`
- `PUT /api/v1/alerts/{alert_id}`
- `POST /api/v1/alerts/{alert_id}/acknowledge`
- `POST /api/v1/alerts/{alert_id}/close`

Main functions:

- Create alerts from detection results
- Update alert status
- Assign alert priority
- Support acknowledgement and escalation

Typical alert statuses:

- open
- acknowledged
- investigating
- closed

---

### 7. Case Management API
Handles investigation workflow after an alert is raised.

Example endpoints:

- `GET /api/v1/cases`
- `GET /api/v1/cases/{case_id}`
- `POST /api/v1/cases`
- `PUT /api/v1/cases/{case_id}`
- `POST /api/v1/cases/{case_id}/assign`
- `POST /api/v1/cases/{case_id}/close`

Main functions:

- Create investigation case
- Assign operator
- Add notes
- Update case status
- Close case

Typical case statuses:

- new
- assigned
- in_progress
- resolved
- closed

---

### 8. Location / Geofence API
Handles managed areas and geofence definitions.

Example endpoints:

- `GET /api/v1/locations`
- `GET /api/v1/locations/{location_id}`
- `POST /api/v1/locations`
- `PUT /api/v1/locations/{location_id}`
- `DELETE /api/v1/locations/{location_id}`

Main functions:

- Register monitored areas
- Define geofence radius
- Update area metadata
- Support map display

---

### 9. Dashboard API
Provides aggregated data for the frontend dashboard.

Example endpoints:

- `GET /api/v1/dashboard/summary`
- `GET /api/v1/dashboard/alerts`
- `GET /api/v1/dashboard/map`
- `GET /api/v1/dashboard/stats`

Main functions:

- Alert count summary
- Live event feed
- Map markers
- Risk trends
- Device activity overview

---

### 10. Audit Log API
Handles security and operational logs for traceability.

Example endpoints:

- `GET /api/v1/audit-logs`
- `GET /api/v1/audit-logs/{log_id}`

Main functions:

- Track user actions
- Record admin changes
- Record alert handling history
- Support investigation and compliance

---

## Example Request Flow

### Device Event Flow

1. Device sends event data to Event Ingestion API
2. Backend validates and stores the event
3. Detection engine evaluates suspicious behavior
4. Risk score is generated
5. Alert is created if threshold is exceeded
6. Dashboard displays the alert
7. Operator opens a case and starts investigation

---

## Example JSON Payload

### Event Ingestion Request

```json
{
  "device_id": "dev-1001",
  "timestamp": "2026-03-29T10:15:00Z",
  "latitude": 35.6812,
  "longitude": 139.7671,
  "event_type": "movement_detected",
  "raw_data": {
    "speed": 12.4,
    "direction": "north"
  }
}

Alert Response Example

{
  "alert_id": "alert-5001",
  "event_id": "event-9001",
  "risk_score": 87,
  "alert_level": "high",
  "status": "open",
  "created_at": "2026-03-29T10:15:05Z"
}


⸻

Security Requirements

The Backend API should include:
	•	HTTPS encryption
	•	JWT or equivalent token authentication
	•	Role-based access control
	•	Input validation
	•	Rate limiting
	•	API logging
	•	Audit trail recording
	•	Protection against replay / spoofed device requests

Recommended additional controls:
	•	API Gateway
	•	WAF
	•	Device authentication key
	•	IP allowlist for trusted device networks
	•	Signed requests for IoT devices

⸻

Error Handling

All APIs should return standard HTTP status codes.

Examples:
	•	200 OK – successful read/update
	•	201 Created – resource created
	•	400 Bad Request – invalid input
	•	401 Unauthorized – authentication required
	•	403 Forbidden – permission denied
	•	404 Not Found – resource not found
	•	409 Conflict – duplicate or conflicting state
	•	500 Internal Server Error – unexpected server failure

Example error response:

{
  "error": "invalid_request",
  "message": "device_id is required"
}


⸻

Non-Functional Requirements

The Backend API should support:
	•	Scalability for many devices and events
	•	Low-latency alert generation
	•	High availability
	•	Secure logging
	•	Observability and monitoring
	•	Maintainability and version control

⸻

Suggested Technology Options

Possible backend technology stack:
	•	Python (FastAPI / Django)
	•	Node.js (NestJS / Express)
	•	Java (Spring Boot)

Supporting components:
	•	PostgreSQL
	•	Redis
	•	Message Queue
	•	Object Storage
	•	Monitoring / Logging platform

⸻

Future Enhancements

Possible future improvements:
	•	Real-time streaming API
	•	Multi-tenant organization support
	•	External law enforcement / partner integration
	•	AI-assisted anomaly detection API
	•	Mobile app API support
	•	Bulk import / export API
	•	Webhook notification API

⸻

Summary

The Backend API is the core operational interface of NSD.

It connects devices, detection logic, alerts, cases, dashboard views,
and security controls into one manageable platform.
A well-designed backend API makes the whole system scalable, secure,
and ready for real-world operation.
## API Versioning

All APIs should be versioned to allow backward compatibility.

Example:
- /api/v1/users
- /api/v1/devices
- /api/v2/...

Versioning strategy:
- Major version in URL
- Backward compatible changes do not change version
- Breaking changes require new version
## Authentication Flow

Typical authentication flow:

1. User logs in with email/password
2. Backend validates credentials
3. Backend issues JWT access token
4. Client includes token in Authorization header
5. Backend validates token for each request

Header example:

Authorization: Bearer <access_token>
