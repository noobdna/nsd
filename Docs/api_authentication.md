NSD – API Authentication & Authorization

Architecture Specification

⸻

1. Overview

This document defines the authentication and authorization architecture for the NSD (Network Suspicious Detection) API.

The API security model must ensure:
	•	Only authorized users and systems can access the API
	•	All requests are authenticated
	•	All actions are authorized
	•	All operations are auditable
	•	Sensitive operations require stronger permissions
	•	The system can support multi-tenant environments
	•	The system can scale to enterprise environments

The authentication platform must support the following clients:
	•	Web dashboard users
	•	Mobile applications
	•	IoT devices
	•	Backend services
	•	External integrations
	•	Admin users
	•	Automated systems

⸻

2. Authentication Methods

Different client types use different authentication mechanisms.

Client Type	Authentication Method
Web Dashboard	JWT Token
Mobile App	JWT Token
IoT Devices	API Key
Backend Services	Service Token
External Integrations	API Key / OAuth
Admin	JWT + MFA
Internal Services	mTLS / Service Token


⸻

3. User Authentication Flow (Login)

Login Flow
	1.	User sends login request
	2.	API validates credentials
	3.	Authentication service generates JWT access token
	4.	Refresh token is generated
	5.	Tokens returned to client
	6.	Client includes token in Authorization header
	7.	API validates token on every request

⸻

Login Endpoint

POST /api/v1/auth/login

Request

{
  "email": "user@example.com",
  "password": "password"
}

Response

{
  "access_token": "jwt_token",
  "refresh_token": "refresh_token",
  "expires_in": 3600
}


⸻

4. JWT Token Structure

JWT tokens contain identity and authorization data.

Example JWT Payload

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

JWT Security Requirements

JWT tokens must:
	•	Be signed using a secure secret or private key
	•	Be short-lived
	•	Be transmitted only over HTTPS
	•	Contain organization context (multi-tenant support)
	•	Be refreshable via refresh tokens

⸻

5. Refresh Token Flow

Refresh tokens allow clients to obtain new access tokens without re-authentication.

Refresh Endpoint

POST /api/v1/auth/refresh

Request

{
  "refresh_token": "token"
}

Response

{
  "access_token": "new_jwt_token",
  "expires_in": 3600
}

Refresh Token Security Rules

Refresh tokens must:
	•	Be stored securely
	•	Be revocable
	•	Be long-lived but rotated
	•	Be stored hashed in the database
	•	Be invalidated after rotation

⸻

6. API Key Authentication (Devices & Integrations)

Used for:
	•	IoT devices
	•	External integrations
	•	Automated systems

Header Examples

Authorization: ApiKey NSD_xxxxxxxxxxxxx

or

X-API-Key: NSD_xxxxxxxxxxxxx

API Key Security Rules
	•	Unique per device or integration
	•	Stored hashed in database
	•	Can be revoked
	•	Must have permission scope
	•	Must have expiration date
	•	Must be logged for audit
	•	Should support rotation

⸻

7. Service-to-Service Authentication

Internal services must not use user JWT tokens.

Instead use:
	•	Service Tokens
	•	Mutual TLS (mTLS)
	•	Internal network restrictions
	•	Signed internal requests

Example

Authorization: Bearer service_token

Service Token Rules
	•	Stored in secret manager
	•	Rotated regularly
	•	Limited permissions
	•	Bound to service identity

⸻

8. Authorization Model (RBAC)

NSD uses Role-Based Access Control (RBAC).

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

9. Authentication Middleware Flow

Every API request must pass through authentication middleware.

Request Flow
	1.	Check Authorization header
	2.	Validate JWT / API Key / Service Token
	3.	Identify user, device, or service
	4.	Load permissions
	5.	Authorize request
	6.	Log audit entry
	7.	Process request

⸻

10. Security Best Practices

The authentication system must enforce the following security controls:
	•	All API traffic must use HTTPS
	•	Tokens must be short-lived
	•	Refresh tokens must be revocable
	•	API keys must be hashed
	•	MFA required for admin users
	•	Log all authentication attempts
	•	Rate limit login attempts
	•	Detect brute force attacks
	•	Detect token abuse
	•	Rotate secrets regularly
	•	Use a secret manager
	•	Support IP allow lists for admin APIs

⸻

11. Token Lifecycle Management

Token Type	Lifetime
Access Token	15–60 minutes
Refresh Token	7–30 days
Service Token	Rotate every 90 days
API Key	90–180 days expiration

Short-lived access tokens reduce risk if compromised.

⸻

12. Token Revocation

The system must support token revocation for:
	•	User logout
	•	Password change
	•	Account disabled
	•	Security incident
	•	API key compromised
	•	Device removed
	•	Organization access revoked

Revocation Methods
	•	Token blacklist
	•	Token version field
	•	Revocation table
	•	Short token lifetime
	•	Refresh token rotation

⸻

13. Multi-Tenant Authorization

NSD supports multi-tenant architecture.

Each authenticated request must include:
	•	user_id
	•	organization_id
	•	role
	•	permissions

Authorization rules must verify:

User.organization_id == Resource.organization_id

This prevents cross-organization data access.

⸻

14. Authentication Audit Logging

All authentication and authorization events must be logged.

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

Audit logs are required for:
	•	Security investigations
	•	Incident response
	•	Compliance
	•	Suspicious behavior detection (NSD integration)

⸻

15. Recommended Production Authentication Architecture

Component	Example Technology
API Gateway	Cloudflare / AWS API Gateway
Authentication Service	Auth Service
Token	JWT
MFA	TOTP / Email / Push
Secret Storage	AWS Secrets Manager
Audit Logs	Database / Log System
Rate Limiting	API Gateway
WAF	Cloudflare
mTLS	Internal Services
IAM	Role Management


⸻

16. Full Authentication System Flow

Full System Flow

Client
   ↓
API Gateway
   ↓
Auth Middleware
   ↓
Authorization (RBAC / Tenant Check)
   ↓
API Service
   ↓
Database

          ↓
      Audit Log
          ↓
      NSD Engine

The NSD engine monitors:
	•	Login failures
	•	Unusual login locations
	•	API key abuse
	•	Token abuse
	•	Permission abuse
	•	Brute force attempts
	•	Suspicious access patterns

Authentication system and NSD detection engine are tightly integrated.

⸻

17. Architecture Summary

NSD Authentication Architecture Summary

The NSD authentication architecture is based on:
	•	JWT for user authentication
	•	Refresh tokens for session renewal
	•	API Keys for devices and integrations
	•	Service tokens / mTLS for internal services
	•	RBAC for authorization
	•	Multi-tenant isolation
	•	Token lifecycle management
	•	Token revocation
	•	Full audit logging
	•	MFA for admin accounts
	•	Secret rotation
	•	API Gateway security controls

This authentication model supports:
	•	MVP deployment
	•	Cloud deployment
	•	Enterprise environments
	•	Multi-tenant SaaS architecture
	•	Zero Trust internal service communication

⸻
