NSD – API Authentication & Authorization

Overview

This document describes authentication and authorization mechanisms for the NSD (Network Suspicious Detection) API.

The API must ensure that:
	•	only authorized users and systems can access the API
	•	all requests are authenticated
	•	all actions are auditable
	•	sensitive operations require stronger permissions
	•	the system supports multi-tenant environments in the future

The authentication system is designed to support:
	•	Web dashboard users
	•	Mobile applications
	•	IoT devices
	•	Backend services
	•	External integrations
	•	Admin users
	•	Automated systems

⸻

Authentication Methods

The NSD API supports multiple authentication methods depending on the client type.

Client Type	Authentication Method
Web Dashboard	JWT Token
Mobile App	JWT Token
IoT Devices	API Key
Backend Services	Service Token
External Integrations	API Key / OAuth
Admin	JWT + MFA
Internal Services	mTLS / Service Token


⸻

Authentication Flow – User Login

Login Flow
	1.	User sends login request
	2.	API validates credentials
	3.	API generates JWT token
	4.	Token returned to client
	5.	Client sends token in Authorization header
	6.	API validates token for each request

Login Endpoint

POST /api/v1/auth/login

Request:

{
  "email": "user@example.com",
  "password": "password"
}

Response:

{
  "access_token": "jwt_token",
  "refresh_token": "refresh_token",
  "expires_in": 3600
}


⸻

JWT Token Structure

JWT tokens contain user and permission information.

Example payload:

{
  "user_id": "uuid",
  "organization_id": "uuid",
  "role": "admin",
  "permissions": [
    "read_events",
    "read_alerts",
    "manage_cases"
  ],
  "exp": 1710000000,
  "iat": 1709990000
}

JWT tokens should be:
	•	signed with a secure secret or private key
	•	short-lived (e.g., 1 hour)
	•	refreshed using refresh tokens
	•	transmitted only over HTTPS

⸻

Refresh Token Flow

Refresh tokens allow users to obtain a new access token without logging in again.

Refresh Endpoint

POST /api/v1/auth/refresh

Request:

{
  "refresh_token": "token"
}

Response:

{
  "access_token": "new_jwt_token",
  "expires_in": 3600
}

Refresh tokens should be:
	•	stored securely
	•	revocable
	•	long-lived but rotated
	•	stored hashed in database

⸻

API Key Authentication (Devices & Integrations)

IoT devices and external integrations may use API keys.

Header Example

Authorization: ApiKey NSD_xxxxxxxxxxxxx

or

X-API-Key: NSD_xxxxxxxxxxxxx

API Key Rules
	•	Keys must be unique per device
	•	Keys must be stored hashed in database
	•	Keys can be revoked
	•	Keys should have permissions
	•	Keys should have expiration dates
	•	Keys should be logged for audit

⸻

Service-to-Service Authentication

Internal services should not use user tokens.

Instead use:
	•	Service Tokens
	•	Mutual TLS (mTLS)
	•	Internal network restrictions
	•	Signed requests

Example:

Authorization: Bearer service_token

Service tokens should:
	•	be stored in secret manager
	•	rotate regularly
	•	have limited permissions

⸻

Authorization (RBAC)

NSD uses Role-Based Access Control.

Roles

Role	Permissions
Viewer	Read-only
Analyst	Events, Alerts, Cases
Investigator	Evidence, Reports
Admin	System Management
Super Admin	Organization Management

Permission Examples

Permission	Description
read_events	View events
read_alerts	View alerts
manage_cases	Create/update cases
upload_evidence	Upload evidence
manage_users	Manage users
system_admin	System settings


⸻

Middleware Authentication Flow

For every API request:
	1.	Check Authorization header
	2.	Validate JWT / API Key / Service Token
	3.	Identify user or device
	4.	Load permissions
	5.	Authorize request
	6.	Log audit entry
	7.	Process request

⸻

Security Best Practices

The API authentication system must follow these rules:
	•	All API traffic must use HTTPS
	•	Tokens must be short-lived
	•	Refresh tokens must be revocable
	•	API keys must be hashed
	•	Support MFA for admin users
	•	Log all authentication attempts
	•	Rate limit login attempts
	•	Detect brute force attacks
	•	Detect token abuse
	•	Rotate secrets regularly
	•	Use a secret manager
	•	Support IP allow lists for admin APIs

⸻

Example Authentication Headers

JWT

Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

API Key

X-API-Key: NSD_123456789

Service Token

Authorization: Bearer service_token_xxxxxx


⸻

Summary

The NSD authentication architecture is based on:
	•	JWT for users
	•	Refresh tokens for session renewal
	•	API Keys for devices and integrations
	•	Service tokens / mTLS for internal services
	•	RBAC for authorization
	•	Full audit logging
	•	Secret rotation
	•	MFA for admin accounts

This authentication model supports MVP deployment and can scale to enterprise multi-tenant environments.

⸻

Token Lifecycle Management

Access Token Lifetime

Access tokens should be short-lived to reduce risk if compromised.

Recommended:
	•	Access Token: 15–60 minutes
	•	Refresh Token: 7–30 days
	•	Service Token: 90 days rotation
	•	API Key: 90–180 days expiration

⸻

Token Revocation

The system must support token revocation in the following cases:
	•	User logout
	•	Password change
	•	Account disabled
	•	Security incident
	•	API key compromised
	•	Device removed
	•	Organization access revoked

Revocation can be implemented using:
	•	Token blacklist
	•	Token version field
	•	Revocation table
	•	Short token lifetime
	•	Refresh token rotation

⸻

Multi-Tenant Authorization

NSD supports multi-tenant environments where multiple organizations use the same platform.

Every authenticated request must include:
	•	user_id
	•	organization_id
	•	role
	•	permissions

Authorization must verify:
	•	User belongs to organization
	•	Resource belongs to organization
	•	User has permission for action

Example rule:

User.organization_id == Resource.organization_id

This prevents cross-organization data access.

⸻

Authentication Audit Logging

All authentication events must be logged.

Logged Events

Event	Description
login_success	Successful login
login_failed	Failed login
token_refresh	Token refreshed
logout	User logout
api_key_used	API key authentication
service_token_used	Service authentication
permission_denied	Authorization failure
mfa_required	MFA triggered
mfa_success	MFA success
account_locked	Too many failures

Example Audit Log

{
  "event_type": "login_success",
  "user_id": "uuid",
  "ip_address": "1.2.3.4",
  "user_agent": "Mozilla/5.0",
  "timestamp": "2026-01-01T12:00:00Z"
}

Audit logs are critical for:
	•	security investigations
	•	incident response
	•	compliance
	•	suspicious behavior detection (NSD integration)

⸻

Recommended Authentication Architecture

Production Authentication Stack Example

Component	Technology Example
API Gateway	Cloudflare / AWS API Gateway
Authentication	Auth Service
Token	JWT
MFA	TOTP / Email / Push
Secret Storage	AWS Secrets Manager
Audit Logs	Database / Log System
Rate Limit	API Gateway
WAF	Cloudflare
mTLS	Internal Services
IAM	Role Management


⸻

Final Authentication Flow (Full System)

Client → API Gateway → Auth Middleware → Authorization → API Service → Database
                         ↓
                    Audit Log
                         ↓
                     NSD Engine

NSD can monitor:
	•	login failures
	•	unusual login locations
	•	API key abuse
	•	token abuse
	•	permission abuse
	•	brute force attempts
	•	suspicious access patterns

Authentication system and NSD detection system are tightly connected.

⸻

