# System Architecture

## Overview
NSD (Network / Neighborhood Suspicious Detection System) is a behavior-based suspicious detection platform.

The system collects logs, events, and device data,
analyzes behavior patterns,
calculates risk scores,
and generates alerts and incident records.

---

## System Components

### Detection Engine
Analyzes logs and events to detect suspicious behavior.

### Backend API
Handles system logic, authentication, data processing, and API endpoints.

### Database
Stores users, devices, logs, alerts, cases, and evidence.

### Alert System
Sends notifications when suspicious activity is detected.

### Frontend Dashboard
Provides monitoring dashboards and incident management interface.

### IoT / GPS Devices
Collects location and sensor data.

### Security System
Handles authentication, authorization, encryption, and audit logs.

### Deployment Infrastructure
Cloud / On-premise deployment environment.

---

## High Level Flow

1. Logs / Events / Device Data collected
2. Detection Engine analyzes behavior
3. Risk Score calculated
4. Alert generated
5. Incident Case created
6. Stored in Database
7. Dashboard displays alerts and cases
