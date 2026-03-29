# NSD – Detection Logic & Rule Engine

## Overview
This document describes how NSD detects suspicious activity
based on incoming device, GPS, behavioral, and event data.

## Detection Objectives
- Identify suspicious movement patterns
- Detect abnormal device behavior
- Flag geofence violations
- Score risk levels for alerts
- Support operator review and escalation

## Input Data
- GPS location data
- Device status events
- User/device association
- Historical movement patterns
- Time-based activity logs

## Detection Rules

### Rule 1: Geofence Breach
If a device enters or exits a restricted area unexpectedly,
create a suspicious event.

### Rule 2: Unusual Time Activity
If movement or activity occurs during unusual hours,
increase risk score.

### Rule 3: Repeated Abnormal Movement
If short-interval repeated movement is detected in unusual patterns,
flag as suspicious.

### Rule 4: Device Tampering / Signal Loss
If the device suddenly stops sending data or shows inconsistent telemetry,
raise alert.

### Rule 5: Risk Combination Logic
Multiple low-level suspicious signals can be combined
to generate a higher severity alert.

## Risk Scoring Model
- Low: minor anomaly
- Medium: suspicious pattern
- High: likely threat
- Critical: urgent response required

## Rule Engine Design
- Event ingestion
- Rule evaluation
- Risk score calculation
- Alert generation
- Case creation trigger

## Future Enhancements
- Machine learning anomaly detection
- Pattern learning by region
- Personalized behavior baseline
- False positive reduction
