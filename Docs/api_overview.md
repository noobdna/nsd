＃NSD – API Overview

1. Overview

This document describes the API architecture, endpoint structure, and design principles for the NSD (Network Suspicious Detection) system.

The NSD API acts as the central communication layer connecting devices, backend services, the detection engine, alert workflows, investigation tools, dashboards, and external systems.

The API is designed to be:
	•	RESTful
	•	secure
	•	auditable
	•	scalable
	•	automation friendly
	•	integration friendly
	•	cloud-native compatible
	•	multi-tenant ready

The API layer supports both MVP deployment and future production-scale expansion.

⸻

2. API Role in the System

The NSD API sits between ingestion sources, processing services, storage systems, and operational interfaces.

High-Level Flow

Devices / Logs / Sensors
            ↓
         Event API
            ↓
      Detection Engine
            ↓
          Alert API
            ↓
           Case API
            ↓
        Evidence API
            ↓
         Report API
            ↓
   Dashboard / Admin / External Systems

The API layer functions as the backbone of the NSD platform.

⸻

3. Base URL

Example base URL:

https://api.nsd.example.com/v1/

Versioning is included in the URL path to support backward compatibility and future evolution.

⸻

4. Core API Domains

The NSD API is divided into the following functional domains:

Category	Description
Auth API	Authentication and session management
Device API	Device registration and lifecycle management
Event API	Event ingestion, storage access, and queries
Detection API	Detection execution, rules, and risk scoring
Alert API	Alert generation and workflow management
Case API	Investigation and case management
Evidence API	Evidence upload, storage, and retrieval
Location API	Geospatial and location-related operations
User API	User and organization management
Admin API	Administrative and system operations
Audit API	Audit history and access logging
Report API	Reports, analytics, and statistics
Integration API	External system integration


⸻

5. Authentication and Authorization

Most NSD API endpoints require authentication.

Supported Authentication Methods
	•	API Key
	•	OAuth2
	•	JWT Access Token
	•	Service Token for devices
	•	Admin Session Token

Example Header

Authorization: Bearer <access_token>

Authentication Rules
	•	All API requests must use HTTPS
	•	Access tokens must expire and support refresh
	•	Admin endpoints require elevated privileges
	•	Device tokens are restricted to device-scoped operations
	•	All authentication events must be logged in audit logs

Recommended Standard Headers

Authorization: Bearer <token>
X-API-Key: <api_key>
X-Request-ID: <request_id>
X-Organization-ID: <organization_id>
Content-Type: application/json


⸻

6. Standard Request and Response Format

To ensure consistency across services, NSD APIs should follow a common response pattern.

Success Response Example

{
  "success": true,
  "data": {},
  "message": "",
  "request_id": "abc-123",
  "timestamp": "2026-03-30T12:00:00Z"
}

Error Response Example

{
  "success": false,
  "error": "not_found",
  "message": "Device not found",
  "status": 404,
  "request_id": "abc-123",
  "timestamp": "2026-03-30T12:00:00Z"
}

Error Response Principles
	•	Errors must be machine-readable
	•	Messages should be human-readable
	•	Every response should include a request identifier for traceability
	•	Sensitive internal details must not be exposed

⸻

7. Role and Permission Model

NSD should enforce role-based access control (RBAC).

Example Roles

Role	Description
admin	Full system administration
organization_admin	Organization-level administration
security_analyst	Investigate alerts, cases, and evidence
operator	Monitor alerts and operational events
viewer	Read-only access
device	Device-scoped API access only

Authorization rules should ensure tenant isolation, least privilege, and auditability.

⸻

8. Auth API

The Auth API manages login, token refresh, logout, and current session information.

Endpoints

| Method | Endpoint | Description |
|—|—|
| POST | /auth/login | Authenticate user |
| POST | /auth/refresh | Refresh access token |
| POST | /auth/logout | Logout session |
| GET | /auth/me | Get current user information |

Login Example

Request

{
  "email": "user@example.com",
  "password": "password"
}

Response

{
  "access_token": "...",
  "refresh_token": "...",
  "expires_in": 3600
}


⸻

9. Device API

The Device API manages device registration, configuration, retrieval, and lifecycle operations.

Endpoints

| Method | Endpoint | Description |
|—|—|
| POST | /devices | Register new device |
| GET | /devices | List devices |
| GET | /devices/{device_id} | Get device information |
| PUT | /devices/{device_id} | Update device |
| DELETE | /devices/{device_id} | Deactivate device |
| GET | /devices/{device_id}/events | Get device events |

⸻

10. Event API

The Event API is responsible for ingesting telemetry and retrieving stored events.

Supported Event Types
	•	login
	•	gps
	•	network
	•	camera
	•	sensor
	•	access_log
	•	system_event
	•	firewall_log
	•	cloud_log
	•	authentication_event
	•	anomaly_event

Endpoints

| Method | Endpoint | Description |
|—|—|
| POST | /events | Ingest event |
| GET | /events | Query events |
| GET | /events/{event_id} | Get event details |

Common Filters
	•	device_id
	•	user_id
	•	event_type
	•	time_range
	•	location
	•	risk_score
	•	status
	•	organization_id

Event Ingestion Example

{
  "device_id": "dev-001",
  "event_type": "login",
  "timestamp": "2026-03-30T10:00:00Z",
  "location": {
    "lat": 35.6895,
    "lon": 139.6917
  },
  "data": {
    "username": "john",
    "result": "failed",
    "ip": "1.2.3.4"
  }
}


⸻

11. Detection API

The Detection API manages detection execution, rule management, and risk evaluation.

Endpoints

| Method | Endpoint | Description |
|—|—|
| POST | /detection/run | Run detection engine manually |
| GET | /detection/rules | List detection rules |
| POST | /detection/rules | Create detection rule |
| PUT | /detection/rules/{rule_id} | Update detection rule |
| DELETE | /detection/rules/{rule_id} | Delete detection rule |
| GET | /detection/risk-score/{event_id} | Get event risk score |

This API supports both automated detection workflows and analyst-driven rule operations.

⸻

12. Alert API

The Alert API manages suspicious findings produced by the detection engine.

Endpoints

| Method | Endpoint | Description |
|—|—|
| GET | /alerts | List alerts |
| POST | /alerts | Create alert |
| GET | /alerts/{alert_id} | Get alert details |
| PUT | /alerts/{alert_id} | Update alert status |
| POST | /alerts/{alert_id}/assign | Assign alert |

Alert Statuses
	•	open
	•	investigating
	•	resolved
	•	false_positive
	•	escalated

⸻

13. Case API

The Case API supports investigation workflows and case lifecycle management.

Endpoints

| Method | Endpoint | Description |
|—|—|
| GET | /cases | List cases |
| POST | /cases | Create case |
| GET | /cases/{case_id} | Get case details |
| PUT | /cases/{case_id} | Update case |
| POST | /cases/{case_id}/assign | Assign investigator |
| GET | /cases/{case_id}/alerts | List alerts in case |
| GET | /cases/{case_id}/evidence | List evidence in case |

Cases may aggregate alerts, evidence, notes, assignments, and workflow state.

⸻

14. Evidence API

The Evidence API manages evidence upload, storage access, and retrieval.

Endpoints

| Method | Endpoint | Description |
|—|—|
| POST | /evidence/upload | Upload evidence |
| GET | /evidence/{evidence_id} | Download evidence |
| GET | /evidence/case/{case_id} | List case evidence |

Evidence Types
	•	logs
	•	images
	•	videos
	•	documents
	•	pcap files
	•	forensic data
	•	exported reports

Evidence access should always be logged for chain-of-custody and forensic traceability.

⸻

15. Location API

The Location API supports geospatial registration and queries.

Endpoints

| Method | Endpoint | Description |
|—|—|
| GET | /locations | Get locations |
| POST | /locations | Register location |
| GET | /locations/nearby | Search nearby locations |
| GET | /locations/device/{device_id} | Get device location history |

This API is intended for GPS, device movement analysis, and map-based visualization.

⸻

16. User and Organization API

The User API manages users and organizational entities.

Endpoints

| Method | Endpoint | Description |
|—|—|
| GET | /users | List users |
| POST | /users | Create user |
| PUT | /users/{user_id} | Update user |
| DELETE | /users/{user_id} | Deactivate user |
| GET | /organizations | List organizations |

This domain should support future multi-tenant administration and scoped access control.

⸻

17. Admin API

The Admin API provides operational and maintenance capabilities.

Endpoints

| Method | Endpoint | Description |
|—|—|
| GET | /admin/system | Get system status |
| POST | /admin/reindex | Reindex search |
| POST | /admin/backup | Run backup |
| GET | /admin/metrics | Get system metrics |
| GET | /admin/health | Health check |

Admin operations must be restricted, logged, and protected with elevated privileges.

⸻

18. Audit API

The Audit API provides access to historical operational records.

Endpoint

| Method | Endpoint | Description |
|—|—|
| GET | /audit/logs | Get audit logs |

Audit Log Coverage
	•	login history
	•	API usage
	•	alert changes
	•	case updates
	•	evidence access
	•	admin operations
	•	detection rule changes
	•	system configuration changes
	•	user management actions

Audit integrity is critical for investigations, compliance, and incident reconstruction.

⸻

19. Report API

The Report API provides analytics and operational reporting.

Endpoints

Endpoint	Description
/reports/incidents	Incident reports
/reports/statistics	System statistics
/reports/risk-trends	Risk trend reports
/reports/device-activity	Device activity reports
/reports/user-activity	User activity reports

These reports support dashboards, exports, and strategic analysis.

⸻

20. Integration API

The Integration API supports external system connectivity.

Typical Integration Targets
	•	SIEM
	•	cloud logs
	•	firewall systems
	•	IAM systems
	•	monitoring tools
	•	external alert systems

Endpoints

Method	Endpoint
POST	/integration/events
POST	/integration/alerts

This layer enables NSD to act as part of a broader security ecosystem.

⸻

21. API Versioning

Versioning should be explicit and path-based.

Examples

https://api.nsd.example.com/v1/
https://api.nsd.example.com/v2/

Versioning Rules
	•	Minor non-breaking changes do not require a new version
	•	Breaking changes require a new API version
	•	Deprecated versions may be retired over time

⸻

22. Rate Limiting

Rate limiting protects the system against abuse and overload.

Example Limits
	•	Device API: 60 requests per minute
	•	Event ingestion API: 1000 requests per minute
	•	Admin API: 30 requests per minute
	•	Authentication API: 10 requests per minute

Exceeded Limit Response

HTTP 429 Too Many Requests

Per-tenant, per-device, and per-IP controls may be added in later versions.

⸻

23. Pagination

List endpoints should support pagination.

Examples

GET /events?page=1&limit=50
GET /alerts?page=2&limit=25
GET /devices?page=1&limit=100

Response Example

{
  "page": 1,
  "limit": 50,
  "total": 1250,
  "data": []
}

Cursor-based pagination may be considered for high-volume event streams.

⸻

24. Common Error Model

NSD APIs should use standard HTTP status codes and a consistent error schema.

Error Example

{
  "error": "invalid_request",
  "message": "Device ID not found",
  "status": 404
}

Common Status Codes

Code	Meaning
200	OK
201	Created
400	Bad Request
401	Unauthorized
403	Forbidden
404	Not Found
429	Too Many Requests
500	Internal Server Error


⸻

25. Security Considerations

API security is a core design principle of NSD.

Security Controls
	•	HTTPS only
	•	token-based authentication
	•	role-based access control
	•	audit logging
	•	rate limiting
	•	input validation
	•	file upload scanning
	•	evidence access logging
	•	admin action logging
	•	multi-tenant data isolation
	•	encryption for sensitive data
	•	API access logging
	•	suspicious API usage detection

Security design must support both operational safety and forensic traceability.

⸻

26. Real-Time and Future API Extensions

NSD may expand beyond standard REST endpoints.

Planned Future Extensions
	•	AI Detection API
	•	Threat Intelligence API
	•	Incident Response Automation API
	•	Mobile Push Notification API
	•	Real-time WebSocket API
	•	Map Visualization API
	•	Multi-tenant Admin API
	•	Risk Analytics API
	•	Behavior Analysis API

Example Real-Time Endpoints

wss://api.nsd.example.com/v1/stream/alerts
wss://api.nsd.example.com/v1/stream/events
wss://api.nsd.example.com/v1/stream/system

These capabilities will improve operational responsiveness and dashboard interactivity.

⸻

27. API Structure Summary

The logical API structure is as follows:

/auth
/devices
/events
/detection
/alerts
/cases
/evidence
/locations
/users
/organizations
/admin
/audit
/reports
/integration
/stream

This structure is designed to support modular implementation and future service separation.

⸻

28. Summary

The NSD API layer connects all major system components, including:
	•	devices
	•	logs and sensors
	•	detection engine
	•	alerts
	•	investigation workflows
	•	evidence management
	•	reporting and analytics
	•	administration
	•	external integrations

The API layer serves as the central communication backbone of the NSD system and is designed to support both early-stage MVP development and future large-scale production deployment.

⸻
