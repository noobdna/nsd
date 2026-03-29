# NSD – Data Model

## Overview
This document describes the database structure for NSD (Network Suspicious Detection).

## Main Entities

### Users
- user_id
- name
- email
- role
- organization
- created_at

### Devices
- device_id
- device_type
- owner_user_id
- status
- registered_at

### Events
- event_id
- device_id
- timestamp
- location_lat
- location_lng
- event_type
- raw_data

### Alerts
- alert_id
- event_id
- risk_score
- alert_level
- created_at
- status

### Cases
- case_id
- alert_id
- assigned_to
- status
- notes
- created_at

### Locations
- location_id
- name
- latitude
- longitude
- geo_fence_radius

### Risk Scores
- score_id
- event_id
- score
- reason
- calculated_at

### Audit Logs
- log_id
- user_id
- action
- timestamp
- details
