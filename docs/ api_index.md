NSD – API Index

Overview

This document provides an index of all APIs available in the NSD (Network Suspicious Detection) system.

The NSD API layer serves as the central interface between devices, detection engines, backend services, investigation tools, dashboards, and administrative systems.

The APIs are organized into functional modules that support:
	•	authentication and access control
	•	user and organization management
	•	device and location management
	•	event ingestion and processing
	•	risk scoring and detection
	•	alert and incident management
	•	investigation workflows
	•	evidence management
	•	reporting and analytics
	•	system administration
	•	auditing and security tracking

The API architecture is designed to be:
	•	RESTful
	•	secure
	•	auditable
	•	scalable
	•	automation-friendly
	•	multi-tenant ready
	•	cloud-native compatible

⸻

API Modules

The NSD system consists of the following API modules.

1. Authentication API

Handles authentication and session management.

Main functions:
	•	login
	•	logout
	•	token refresh
	•	MFA verification
	•	session validation
	•	service authentication
	•	API key validation

Used by:
	•	Web dashboard
	•	Mobile apps
	•	Admin users
	•	Backend services
	•	IoT devices (API key)

⸻

2. User Management API

Handles user accounts, roles, permissions, and organization membership.

Main functions:
	•	create user
	•	update user
	•	deactivate user
	•	assign roles
	•	manage permissions
	•	assign organization
	•	password reset
	•	user activity tracking

⸻

3. Organization API

Handles organizations, tenants, and multi-organization environments.

Main functions:
	•	create organization
	•	update organization
	•	organization settings
	•	organization membership
	•	organization roles
	•	tenant isolation settings

⸻

4. Device API

Handles device registration, device status, ownership, and device metadata.

Devices may include:
	•	IoT sensors
	•	cameras
	•	GPS trackers
	•	mobile devices
	•	servers
	•	routers
	•	network sensors
	•	access control devices
	•	cloud systems

Main functions:
	•	register device
	•	update device
	•	device status update
	•	assign owner
	•	assign location
	•	device activity tracking
	•	device risk score retrieval
	•	deactivate device

⸻

5. Location API

Handles locations such as buildings, rooms, areas, GPS zones, and network segments.

Main functions:
	•	create location
	•	update location
	•	assign devices to location
	•	location hierarchy
	•	geofence management
	•	location risk level
	•	location activity summary

⸻

6. Event API

Handles event ingestion from devices, logs, sensors, and external systems.

Events may include:
	•	login attempts
	•	access logs
	•	GPS updates
	•	device status changes
	•	network logs
	•	sensor alerts
	•	system events
	•	cloud logs

Main functions:
	•	ingest event
	•	list events
	•	event details
	•	event filtering
	•	event search
	•	event timeline
	•	event tagging

⸻

7. Risk Scoring API

Calculates and retrieves risk scores for devices, users, locations, and events.

Risk scores are calculated by the detection engine based on behavior patterns and suspicious activity.

Main functions:
	•	calculate risk score
	•	get device risk score
	•	get user risk score
	•	get location risk score
	•	get event risk score
	•	risk history
	•	risk factors
	•	risk trend analysis

⸻

8. Alert API

Handles alerts generated from suspicious activity or high risk scores.

Main functions:
	•	create alert
	•	list alerts
	•	alert details
	•	update alert status
	•	assign alert
	•	add comments
	•	escalate alert to case
	•	alert SLA tracking
	•	alert deduplication
	•	alert timeline
	•	alert audit trail

⸻

9. Case API

Handles investigation cases created from alerts.

Cases are used for investigation management, evidence tracking, notes, and incident resolution.

Main functions:
	•	create case
	•	list cases
	•	case details
	•	update case status
	•	assign case
	•	link alerts to case
	•	add evidence
	•	add investigation notes
	•	case timeline
	•	close case
	•	case audit trail

⸻

10. Evidence API

Handles investigation evidence such as logs, files, images, and documents.

Main functions:
	•	upload evidence
	•	download evidence
	•	evidence metadata
	•	evidence tagging
	•	evidence chain of custody
	•	evidence access control
	•	evidence audit trail

⸻

11. Report API

Generates investigation reports, incident summaries, statistics, and analytics reports.

Main functions:
	•	generate incident report
	•	generate investigation report
	•	generate risk report
	•	generate activity report
	•	export reports (PDF / CSV / JSON)
	•	scheduled reports
	•	report templates

⸻

12. Admin API

Handles system administration, configuration, and rule management.

Main functions:
	•	system settings
	•	detection rules management
	•	risk scoring rules
	•	alert rules
	•	notification settings
	•	integration settings
	•	API key management
	•	system status
	•	system maintenance mode

⸻

13. Audit Log API

Tracks all system actions and changes for auditing and security monitoring.

Audit logs include:
	•	user actions
	•	login history
	•	configuration changes
	•	device changes
	•	alert updates
	•	case updates
	•	evidence access
	•	admin actions
	•	API access logs

Main functions:
	•	list audit logs
	•	audit log details
	•	audit search
	•	export audit logs
	•	compliance reports

⸻

API Module Summary Table

API Module	Purpose
Authentication API	Authentication and session management
User Management API	User accounts and permissions
Organization API	Organizations and multi-tenant management
Device API	Device registration and management
Location API	Location and geofence management
Event API	Event ingestion and event management
Risk Scoring API	Risk calculation and scoring
Alert API	Alert management
Case API	Investigation case management
Evidence API	Evidence storage and tracking
Report API	Reports and analytics
Admin API	System configuration and rules
Audit Log API	Audit and security tracking


⸻

API Structure Example

All NSD APIs follow a consistent RESTful structure.

Example Endpoint Structure

/api/v1/auth/login
/api/v1/users
/api/v1/devices
/api/v1/devices/{device_id}
/api/v1/events
/api/v1/alerts
/api/v1/cases
/api/v1/evidence
/api/v1/reports
/api/v1/admin/settings
/api/v1/audit-logs

Example Request

POST /api/v1/devices
Authorization: Bearer <token>
Content-Type: application/json

Example Response

{
  "status": "success",
  "data": {
    "device_id": "DEV-001",
    "device_name": "Front Gate Camera",
    "status": "active"
  }
}


⸻

Summary

The NSD API architecture is modular and designed around the investigation workflow:

Device / User / Location → Event → Risk Score → Alert → Case → Evidence → Report → Audit

This structure allows the system to scale from a small deployment to a large multi-organization security and monitoring platform.

⸻
