Docs/api_endpoint_standards.md

# NSD – API Endpoint Standards

## Overview

This document defines the endpoint naming conventions, URL structure, HTTP methods, request/response formats, and general standards used across all NSD APIs.

The goal is to keep the API:
- consistent
- predictable
- RESTful
- easy to maintain
- easy to integrate
- scalable for future expansion

All APIs in the NSD system must follow these standards.

---

## Base URL Structure

All endpoints follow this base structure:

/api/v1/{resource}

Examples:

/api/v1/devices
/api/v1/events
/api/v1/alerts
/api/v1/cases
/api/v1/users
/api/v1/reports

Versioning is included in the URL to allow future API changes without breaking existing clients.

---

## Resource Naming Rules

### Use plural nouns for resources

Correct:

/devices
/events
/alerts
/cases
/users

Incorrect:

/device
/getDevices
/deviceList

### Use lowercase and hyphens if needed

/risk-scores
/audit-logs
/system-settings

---

## Standard Endpoint Patterns

Each resource should follow standard REST patterns.

### List Resources

GET /api/v1/devices
GET /api/v1/events
GET /api/v1/alerts

### Get Resource by ID

GET /api/v1/devices/{device_id}
GET /api/v1/alerts/{alert_id}
GET /api/v1/cases/{case_id}

### Create Resource

POST /api/v1/devices
POST /api/v1/alerts
POST /api/v1/cases

### Update Resource

PUT /api/v1/devices/{device_id}
PATCH /api/v1/alerts/{alert_id}

### Delete / Deactivate Resource

DELETE /api/v1/devices/{device_id}

Note:
Some resources may use "deactivate" instead of delete for audit reasons.

---

## Nested Resource Endpoints

When resources are related, nested endpoints may be used.

Examples:

GET /api/v1/devices/{device_id}/events
GET /api/v1/alerts/{alert_id}/comments
GET /api/v1/cases/{case_id}/evidence
GET /api/v1/cases/{case_id}/notes

This represents relationships between objects.

---

## Common Special Endpoints

Some endpoints represent actions rather than resources.

Examples:

POST /api/v1/alerts/{alert_id}/assign
POST /api/v1/alerts/{alert_id}/escalate
POST /api/v1/cases/{case_id}/close
POST /api/v1/devices/{device_id}/status

Use verbs only for actions that cannot be represented as simple resource updates.

---

## HTTP Methods Standards

Method | Usage
------ | -----
GET | Retrieve data
POST | Create new resource
PUT | Full update
PATCH | Partial update
DELETE | Delete resource
OPTIONS | API capability check

---

## Request Format

All requests must use JSON.

Example:

POST /api/v1/devices
Content-Type: application/json

Request Body Example:

```json
{
  "device_name": "Front Gate Camera",
  "device_type": "camera",
  "location_id": "LOC-001"
}


⸻

Response Format

All responses should follow a standard structure.

Success Response

{
  "status": "success",
  "data": {},
  "message": ""
}

Error Response

{
  "status": "error",
  "error_code": "DEVICE_NOT_FOUND",
  "message": "Device not found"
}


⸻

HTTP Status Codes

Code	Meaning
200	OK
201	Created
204	No Content
400	Bad Request
401	Unauthorized
403	Forbidden
404	Not Found
409	Conflict
500	Internal Server Error


⸻

Pagination

List endpoints should support pagination.

Example:

GET /api/v1/events?page=1&limit=50

Response:

{
  "status": "success",
  "data": [],
  "pagination": {
    "page": 1,
    "limit": 50,
    "total": 1200
  }
}


⸻

Filtering and Search

Endpoints should support filtering via query parameters.

Examples:

GET /api/v1/events?device_id=DEV-001
GET /api/v1/alerts?severity=high
GET /api/v1/devices?status=active
GET /api/v1/events?start_time=2026-03-01&end_time=2026-03-02


⸻

Sorting

Sorting should be supported using:

GET /api/v1/events?sort=timestamp
GET /api/v1/events?sort=-timestamp

	•	sort=timestamp → ascending
	•	sort=-timestamp → descending

⸻

API Design Principles Summary

All NSD APIs should follow these principles:
	1.	Use RESTful design
	2.	Use plural resource names
	3.	Use consistent URL structure
	4.	Use proper HTTP methods
	5.	Always return JSON
	6.	Use standard response format
	7.	Support pagination
	8.	Support filtering and sorting
	9.	Keep endpoints predictable
	10.	Maintain auditability and security

⸻

Example Full Endpoint Set (Device API Example)

GET    /api/v1/devices
GET    /api/v1/devices/{device_id}
POST   /api/v1/devices
PUT    /api/v1/devices/{device_id}
PATCH  /api/v1/devices/{device_id}
DELETE /api/v1/devices/{device_id}

GET    /api/v1/devices/{device_id}/events
GET    /api/v1/devices/{device_id}/alerts
POST   /api/v1/devices/{device_id}/status


⸻

Conclusion

The API endpoint standards ensure that all NSD APIs are consistent, maintainable, scalable, and easy to use for developers, integrations, and future system expansion.

All future APIs must follow this document.

