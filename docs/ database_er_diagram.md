# NSD – Database ER Diagram

## Overview

This document describes the relationships between database entities in the NSD (Network Suspicious Detection) system.

The database is designed to track devices, events, alerts, investigations, users, and audit logs.

---

## Main Entities

The main database entities are:

- Organizations
- Users
- Devices
- Locations
- Events
- Risk Scores
- Alerts
- Cases
- Evidence
- Reports
- Rules
- Audit Logs

---

## Entity Relationships

### Organization Relationships

Organization
 ├── Users
 ├── Devices
 └── Locations

Each organization can have multiple users, devices, and locations.

---

### Device and Event Flow

Device → Events → Risk Score → Alert → Case → Evidence → Report

This represents the investigation and detection pipeline.

1. Devices generate events
2. Events are analyzed and assigned risk scores
3. High risk scores generate alerts
4. Alerts can be escalated into cases
5. Cases can contain evidence
6. Reports are generated from cases

---

### User Relationships

Users can be assigned to:

- Alerts
- Cases
- Organizations
- Devices (ownership)
- Locations

Users perform actions that are recorded in audit logs.

---

### Audit Logging

All important actions are recorded in Audit Logs:

- Login / Logout
- Device registration
- Alert updates
- Case updates
- Evidence uploads
- System configuration changes

AuditLog can reference:

- User
- Device
- Alert
- Case
- Organization

---

## Simplified ER Structure
