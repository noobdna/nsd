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

Example:
- Activity between 00:00 and 05:00
- Activity outside expected schedule
- Repeated late-night movement

### Rule 3: Repeated Abnormal Movement
If short-interval repeated movement is detected in unusual patterns,
flag as suspicious.

Example indicators:
- Frequent back-and-forth movement
- Repeated appearance near the same monitored area
- Sudden route deviation

### Rule 4: Device Tampering / Signal Loss
If the device suddenly stops sending data or shows inconsistent telemetry,
raise alert.

Example indicators:
- Signal loss without recovery
- GPS jump / impossible location change
- Device battery removal or forced shutdown

### Rule 5: Risk Combination Logic
Multiple low-level suspicious signals can be combined
to generate a higher severity alert.

Example:
- Night activity + geofence breach = High risk
- Tampering + signal loss = Critical risk candidate

## Risk Scoring Model
Each event is evaluated using weighted risk factors.

### Risk Factors
- Location risk
- Time risk
- Movement pattern risk
- Device integrity risk
- Historical behavior risk

### Risk Levels
- Low: minor anomaly
- Medium: suspicious pattern
- High: likely threat
- Critical: urgent response required

## Rule Engine Design
The rule engine processes events in the following order:
1. Event ingestion
2. Rule evaluation
3. Risk score calculation
4. Alert generation
5. Case creation trigger

## Output
The detection engine can produce:
- Suspicious event records
- Risk scores
- Alerts
- Escalation recommendations
- Case creation triggers

## Future Enhancements
- Machine learning anomaly detection
- Pattern learning by region
- Personalized behavior baseline
- False positive reduction
