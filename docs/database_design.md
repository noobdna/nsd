# NSD – Database Design

## Overview
This document defines the database structure for NSD (Network Suspicious Detection).
The database stores users, devices, suspicious events, alerts, investigation cases,
locations, risk scores, and audit logs.

---

## Main Entities

### 1. Users
Stores operator and admin account information.

**Fields**
- user_id
- name
- email
- role
- organization
- created_at
- updated_at

---

### 2. Devices
Stores registered IoT devices, GPS trackers, cameras, or mobile endpoints.

**Fields**
- device_id
- device_type
- device_name
- owner_user_id
- status
- registered_at
- updated_at

**Relations**
- Many devices can belong to one user

---

### 3. Events
Stores raw suspicious activity data collected from devices or external systems.

**Fields**
- event_id
- device_id
- timestamp
- location_lat
- location_lng
- event_type
- raw_data
- created_at

**Relations**
- Many events belong to one device

---

### 4. Alerts
Stores alerts generated from suspicious events.

**Fields**
- alert_id
- event_id
- risk_score
- alert_level
- status
- created_at
- updated_at

**Relations**
- One alert is linked to one event

---

### 5. Cases
Stores investigation or response cases created from alerts.

**Fields**
- case_id
- alert_id
- assigned_to
- status
- notes
- created_at
- updated_at

**Relations**
- One case is linked to one alert
- One user can manage many cases

---

### 6. Locations
Stores predefined monitored locations and geofence settings.

**Fields**
- location_id
- name
- latitude
- longitude
- geo_fence_radius
- created_at
- updated_at

---

### 7. Risk Scores
Stores calculated risk evaluation results for events.

**Fields**
- score_id
- event_id
- score
- reason
- calculated_at

**Relations**
- One risk score is linked to one event

---

### 8. Audit Logs
Stores important user and system actions for security and traceability.

**Fields**
- log_id
- user_id
- action
- details
- timestamp

**Relations**
- Many audit logs can belong to one user

---

## Entity Relationships

- One user can own multiple devices
- One device can generate multiple events
- One event can generate one alert
- One alert can create one case
- One event can have one risk score
- One user can be assigned multiple cases
- One user can generate multiple audit logs

---

## Suggested Database Type

NSD can use a relational database such as:
- PostgreSQL
- MySQL

For location search and geospatial analysis, PostgreSQL with PostGIS is recommended.

---

## Future Extensions

Possible future tables:
- organizations
- notification_history
- media_files
- incident_reports
- watchlists
- access_policies

---

## Notes

The database should support:
- secure data storage
- auditability
- case tracking
- geolocation queries
- future AI/risk analysis expansion
