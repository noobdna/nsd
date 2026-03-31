⸻

NSD – Admin API

Overview

The Admin API manages system-level configuration, rules, risk scoring parameters, integrations, and administrative operations for the NSD (Network Suspicious Detection) platform.

This API is restricted to administrative users and system operators.

The Admin API is responsible for:
	•	system configuration
	•	detection rules management
	•	risk scoring configuration
	•	organization management
	•	location management
	•	system logs
	•	audit logs
	•	integrations
	•	API key management
	•	system health monitoring

This API requires admin-level authentication and all actions must be logged in the audit trail.

⸻

Admin API Categories

1. System Configuration

2. Detection Rules

3. Risk Score Settings

4. Organization Management

5. Location Management

6. Integration Management

7. API Key Management

8. System Logs

9. Audit Logs

10. System Health

⸻

1. System Configuration

Get System Settings

GET

/api/admin/system/settings

Response

{
  "system_name": "NSD Platform",
  "environment": "production",
  "alert_email_enabled": true,
  "max_risk_score": 100,
  "auto_case_creation": true,
  "data_retention_days": 365
}


⸻

Update System Settings

PUT

/api/admin/system/settings

Request

{
  "alert_email_enabled": true,
  "auto_case_creation": false,
  "data_retention_days": 180
}


⸻

2. Detection Rules Management

Detection rules define suspicious behavior patterns.

Get Rules

GET

/api/admin/rules


⸻

Create Rule

POST

/api/admin/rules

Request

{
  "rule_name": "Multiple Failed Login",
  "description": "More than 5 failed logins in 10 minutes",
  "event_type": "login_failed",
  "threshold": 5,
  "time_window_minutes": 10,
  "risk_score": 30,
  "severity": "medium",
  "enabled": true
}


⸻

Update Rule

PUT

/api/admin/rules/{rule_id}


⸻

Delete Rule

DELETE

/api/admin/rules/{rule_id}


⸻

3. Risk Score Settings

Get Risk Score Settings

GET

/api/admin/risk-settings

Response

{
  "login_failed_weight": 5,
  "night_access_weight": 10,
  "new_device_weight": 15,
  "location_change_weight": 20,
  "max_score": 100
}


⸻

Update Risk Score Settings

PUT

/api/admin/risk-settings


⸻

4. Organization Management

Get Organizations

GET

/api/admin/organizations


⸻

Create Organization

POST

/api/admin/organizations

Request

{
  "organization_name": "ABC Security",
  "contact_email": "admin@abc.com",
  "status": "active"
}


⸻

5. Location Management

Get Locations

GET

/api/admin/locations


⸻

Create Location

POST

/api/admin/locations

Request

{
  "location_name": "Main Office",
  "address": "Tokyo, Japan",
  "organization_id": "ORG-001"
}


⸻

6. Integration Management

External system integrations such as:
	•	Email servers
	•	SMS gateways
	•	Cloud logging
	•	SIEM
	•	External APIs

Get Integrations

GET

/api/admin/integrations


⸻

Add Integration

POST

/api/admin/integrations

Request

{
  "integration_name": "Email Notification",
  "type": "email",
  "endpoint": "smtp.example.com",
  "status": "active"
}


⸻

7. API Key Management

Create API Key

POST

/api/admin/api-keys

Request

{
  "key_name": "IoT Devices",
  "permissions": ["event:write"]
}

Response

{
  "api_key": "NSD-API-XXXX-XXXX",
  "created_at": "2026-03-30T12:00:00Z"
}


⸻

8. System Logs

Get System Logs

GET

/api/admin/system-logs

Query Parameters:

?level=error
?start_date=
?end_date=


⸻

9. Audit Logs

Audit logs track all administrative and user actions.

Get Audit Logs

GET

/api/admin/audit-logs

Response

{
  "audit_logs": [
    {
      "log_id": "AUD-001",
      "user_id": "USR-001",
      "action": "rule_created",
      "resource_type": "rule",
      "resource_id": "RULE-001",
      "timestamp": "2026-03-30T12:00:00Z"
    }
  ]
}


⸻

10. System Health

Get System Health Status

GET

/api/admin/system-health

Response

{
  "status": "healthy",
  "database": "ok",
  "event_ingestion": "ok",
  "alert_system": "ok",
  "api": "ok",
  "timestamp": "2026-03-30T12:00:00Z"
}


⸻

Admin API Summary

Main Admin Endpoints

Category	Endpoint
System Settings	/api/admin/system/settings
Rules	/api/admin/rules
Risk Settings	/api/admin/risk-settings
Organizations	/api/admin/organizations
Locations	/api/admin/locations
Integrations	/api/admin/integrations
API Keys	/api/admin/api-keys
System Logs	/api/admin/system-logs
Audit Logs	/api/admin/audit-logs
System Health	/api/admin/system-health


⸻

NSD API Structure (Complete)

これでAPIモジュール全部揃った。

NSD API Modules
	1.	Authentication API
	2.	Users API
	3.	Devices API
	4.	Events API
	5.	Risk Score API
	6.	Alerts API
	7.	Case API
	8.	Evidence API
	9.	Reports API
	10.	Admin API

⸻
