
# NSD – System Architecture

## Overview
NSD (Network Suspicious Detection) is a distributed detection platform designed to identify suspicious behavior, stalking risks, and anomaly activities using network, cloud, mobile, and IoT technologies.

## Architecture Components

### 1. IoT / Devices
- GPS devices
- Mobile phones
- Network sensors
- Cameras
- BLE trackers

### 2. Cloud Platform
- API Server
- Detection Engine
- Database
- Alert System
- Dashboard Backend

### 3. Detection Engine
- Behavior anomaly detection
- Geo-fencing alerts
- Repeated access detection
- Time-pattern analysis
- Risk scoring

### 4. Dashboard / Operator UI
- Incident view
- Map view
- Alert management
- Device management
- Case management

### 5. Notification System
- Mobile push
- SMS
- Email
- Police / Organization alert interface

## High Level Architecture Flow

Devices → API → Detection Engine → Database → Alert → Dashboard / Notification

---

## System Flow

IoT / GPS Devices
        ↓
API Gateway / Data Ingestion
        ↓
Message Queue / Stream Processing
        ↓
Detection Engine
        ↓
Database
        ↓
Alert System
        ↓
Notification Service
        ↓
Dashboard / Operator / Guardian / Police

---

## Data Flow Description

1. Devices send location, sensor, and event data to backend API.
2. Data is stored in database and forwarded to detection engine.
3. Detection engine evaluates behavior using rules and risk scoring.
4. If risk threshold is exceeded, alert is generated.
5. Notification service sends alerts to users or authorities.
6. Dashboard displays events, alerts, and device status.

---

## Technology Stack (Example)

| Layer | Technology |
|------|------------|
| Frontend | React / Vue |
| Backend API | Node.js / Python |
| Database | PostgreSQL |
| Realtime | WebSocket / MQTT |
| Queue | Kafka / RabbitMQ |
| Cloud | AWS / GCP / Azure |
| Monitoring | Prometheus / Grafana |
| Logging | ELK Stack |
| Authentication | OAuth / Zero Trust |


