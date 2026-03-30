⸻

NSD – Users API

Overview

The Users API manages user accounts, roles, permissions, and organization membership in the NSD (Network Suspicious Detection) system.

Users can log in to the dashboard, manage devices, review alerts, investigate cases, and administer the system depending on their role and permissions.

The Users API supports:
	•	user creation
	•	user listing
	•	user details retrieval
	•	user updates
	•	role assignment
	•	organization assignment
	•	user activation / deactivation
	•	password reset
	•	audit trail tracking

⸻

User Object

User Structure

{
  "user_id": "USR-001",
  "username": "mark",
  "email": "mark@example.com",
  "full_name": "Mark Imagawa",
  "role": "admin",
  "status": "active",
  "organization_id": "ORG-001",
  "created_at": "2026-03-30T10:00:00Z",
  "updated_at": "2026-03-30T10:10:00Z",
  "last_login": "2026-03-30T09:00:00Z"
}


⸻

User Roles

The system supports role-based access control (RBAC).

Roles

Role	Description
admin	Full system access
operator	Manage alerts and cases
analyst	Investigation and analysis
viewer	Read-only access
device_manager	Manage devices only
auditor	Audit logs and reports


⸻

Users API Endpoints

1. Create User

POST
/api/v1/users

Creates a new user.

Request

{
  "username": "john",
  "email": "john@example.com",
  "full_name": "John Smith",
  "role": "operator",
  "organization_id": "ORG-001"
}

Response

{
  "user_id": "USR-010",
  "message": "User created"
}


⸻

2. List Users

GET
/api/v1/users

Returns a list of users.

Response

{
  "users": [
    {
      "user_id": "USR-001",
      "username": "mark",
      "role": "admin",
      "status": "active"
    }
  ]
}


⸻

3. Get User Details

GET
/api/v1/users/{user_id}

Returns detailed user information.

⸻

4. Update User

PUT
/api/v1/users/{user_id}

Updates user information.

Request

{
  "full_name": "John A. Smith",
  "role": "analyst"
}


⸻

5. Deactivate User

POST
/api/v1/users/{user_id}/deactivate

Disables a user account.

⸻

6. Activate User

POST
/api/v1/users/{user_id}/activate

Re-enables a user account.

⸻

7. Reset Password

POST
/api/v1/users/{user_id}/reset-password

Triggers password reset.

⸻

Permissions Model

The system uses Role-Based Access Control (RBAC).

Example Permission Matrix

Action	Admin	Operator	Analyst	Viewer
View Devices	✓	✓	✓	✓
Register Device	✓	✓	✗	✗
View Alerts	✓	✓	✓	✓
Manage Alerts	✓	✓	✗	✗
Manage Cases	✓	✓	✓	✗
Manage Users	✓	✗	✗	✗
View Reports	✓	✓	✓	✓
System Settings	✓	✗	✗	✗


⸻

Audit Logging

All user-related actions must be logged.

Logged Actions
	•	user login
	•	user logout
	•	user creation
	•	role changes
	•	password reset
	•	account activation/deactivation
	•	permission changes

Example Audit Log:

{
  "audit_id": "AUD-1001",
  "user_id": "USR-001",
  "action": "create_user",
  "target_user_id": "USR-010",
  "timestamp": "2026-03-30T10:05:00Z",
  "ip_address": "203.0.113.10"
}


⸻

Summary

The Users API is responsible for identity and access management in the NSD system.

It provides:
	•	user account management
	•	role and permission control
	•	organization membership
	•	authentication integration
	•	audit tracking

The Users API is tightly integrated with:
	•	Authentication API
	•	Devices API
	•	Alerts API
	•	Case API
	•	Audit Log System

⸻
