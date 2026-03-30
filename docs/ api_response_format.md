⸻

api_response_format.md

NSD API Response Format Standard

This document defines the standard response format for all NSD backend APIs.
All APIs must return responses in a consistent JSON structure.

⸻

1. Basic Response Structure

All API responses must follow this structure:

{
  "status": "success | error",
  "code": 200,
  "message": "Human readable message",
  "data": {},
  "timestamp": "2026-03-30T12:00:00Z",
  "request_id": "uuid"
}


⸻

2. Response Fields

Field	Type	Description
status	string	success or error
code	integer	HTTP status code
message	string	Description message
data	object	Response data payload
timestamp	string	ISO8601 timestamp
request_id	string	Unique request ID


⸻

3. Success Response Example

{
  "status": "success",
  "code": 200,
  "message": "User retrieved successfully",
  "data": {
    "user_id": "u_001",
    "name": "Taro",
    "email": "taro@example.com"
  },
  "timestamp": "2026-03-30T12:00:00Z",
  "request_id": "550e8400-e29b-41d4-a716-446655440000"
}


⸻

4. Error Response Example

{
  "status": "error",
  "code": 404,
  "message": "User not found",
  "data": null,
  "timestamp": "2026-03-30T12:00:00Z",
  "request_id": "550e8400-e29b-41d4-a716-446655440000"
}


⸻

5. Validation Error Response

{
  "status": "error",
  "code": 400,
  "message": "Validation error",
  "errors": [
    {
      "field": "email",
      "message": "Invalid email format"
    }
  ],
  "timestamp": "2026-03-30T12:00:00Z",
  "request_id": "550e8400-e29b-41d4-a716-446655440000"
}


⸻

6. Pagination Response Format

{
  "status": "success",
  "code": 200,
  "message": "Events list",
  "data": {
    "items": [],
    "pagination": {
      "page": 1,
      "per_page": 20,
      "total": 150,
      "total_pages": 8
    }
  },
  "timestamp": "2026-03-30T12:00:00Z",
  "request_id": "550e8400-e29b-41d4-a716-446655440000"
}


⸻

7. HTTP Status Code Usage

Code	Meaning
200	Success
201	Created
400	Bad request
401	Unauthorized
403	Forbidden
404	Not found
409	Conflict
422	Validation error
500	Internal server error


⸻

8. Request ID

Every API request must generate a unique request ID for tracing and logging.

Example:

X-Request-ID: 550e8400-e29b-41d4-a716-446655440000

Used for:
	•	Log tracing
	•	Incident investigation
	•	Debugging
	•	Audit logging

⸻

9. Design Principles

NSD API response design principles:
	1.	Always return JSON
	2.	Always include status field
	3.	Always include request_id
	4.	Errors must be structured
	5.	Pagination must be standardized
	6.	Messages must be human readable
	7.	Data must be inside “data” object

⸻

10. Standard Success Template

{
  "status": "success",
  "code": 200,
  "message": "",
  "data": {},
  "timestamp": "",
  "request_id": ""
}


⸻

11. Standard Error Template

{
  "status": "error",
  "code": 400,
  "message": "",
  "errors": [],
  "timestamp": "",
  "request_id": ""
}


⸻

