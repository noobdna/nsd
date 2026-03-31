
# NSD – System Overview

## Purpose
NSD is a distributed suspicious detection platform that collects signals from devices, networks, and sensors, analyzes behavior patterns, calculates risk scores, and generates alerts for operators or users.

The goal is to detect meaningful suspicious patterns early and support timely human decision-making.

## System Layers

### 1. Device Layer
This layer includes devices that generate data.

- GPS devices
- Mobile phones
- BLE trackers
- Cameras
- Network sensors
- IoT devices
- Access control systems

### 2. Ingestion Layer
This layer receives data from devices.

- API Gateway
- Device authentication
- Data ingestion service
- Event queue / streaming
- Secure communication (TLS)

### 3. Processing Layer
This layer analyzes data and detects suspicious behavior.

- Detection engine
- Risk scoring engine
- Rule engine
- Geo-fencing analysis
- Time pattern analysis
- Behavior pattern analysis
- Correlation engine

### 4. Data Layer
This layer stores system data.

- Raw event database
- Device database
- User database
- Alert history
- Case management data
- Audit logs

### 5. Application Layer
This layer is used by operators or users.

- Dashboard
- Incident management
- Device management
- Alert management
- Reporting
- Administration

### 6. Notification Layer
This layer sends alerts.

- Mobile push
- SMS
- Email
- External system interface
- Police / Security organization interface

## High Level Data Flow

Devices → API → Event Queue → Detection Engine → Database → Alert → Dashboard / Notification
