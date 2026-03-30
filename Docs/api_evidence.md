⸻

NSD – Evidence API

Overview

The Evidence API manages investigation evidence within the NSD (Network Suspicious Detection) system.

Evidence is attached to investigation cases and may include logs, images, documents, videos, network captures, GPS data, and other digital artifacts used during investigations.

The Evidence API supports:
	•	evidence upload
	•	evidence listing
	•	evidence details retrieval
	•	linking evidence to cases
	•	linking evidence to alerts
	•	evidence tagging
	•	evidence integrity verification
	•	evidence download
	•	evidence deletion (restricted)
	•	audit trail tracking

Evidence is critical for investigations and must be stored securely with integrity verification and full audit logging.

⸻

Evidence Object

Evidence Structure

{
  "evidence_id": "EVD-20260330-0001",
  "case_id": "CASE-20260330-0001",
  "alert_id": "ALT-20260330-0001",
  "file_name": "failed_login_logs.txt",
  "file_type": "text/plain",
  "file_size": 204800,
  "file_hash": "a3f5b6c7d8e9f1234567890abcdef1234567890",
  "storage_path": "/evidence/2026/03/30/failed_login_logs.txt",
  "uploaded_by": "USR-002",
  "uploaded_at": "2026-03-30T10:30:00Z",
  "description": "Failed login logs collected from server",
  "tags": ["login", "security", "server"],
  "integrity_status": "verified",
  "retention_policy": "case_closed_plus_5_years",
  "status": "active"
}


⸻

Evidence Fields

Field	Description
evidence_id	Unique evidence ID
case_id	Related case
alert_id	Related alert
file_name	Original file name
file_type	MIME type
file_size	File size in bytes
file_hash	SHA256 hash for integrity
storage_path	Storage location
uploaded_by	User who uploaded
uploaded_at	Upload timestamp
description	Evidence description
tags	Evidence tags
integrity_status	verified / corrupted
retention_policy	Evidence retention rule
status	active / archived / deleted


⸻

API Endpoints

Upload Evidence

POST /api/v1/evidence

Uploads new evidence file and metadata.

Request:

{
  "case_id": "CASE-20260330-0001",
  "alert_id": "ALT-20260330-0001",
  "file_name": "failed_login_logs.txt",
  "description": "Failed login logs",
  "tags": ["login", "security"]
}

Response:

{
  "evidence_id": "EVD-20260330-0001",
  "status": "uploaded"
}


⸻

List Evidence

GET /api/v1/evidence

Query Parameters:

Parameter	Description
case_id	Filter by case
alert_id	Filter by alert
tag	Filter by tag
status	active / archived
uploaded_by	Filter by user

Example:

GET /api/v1/evidence?case_id=CASE-20260330-0001


⸻

Get Evidence Details

GET /api/v1/evidence/{evidence_id}

Returns detailed evidence information.

⸻

Download Evidence

GET /api/v1/evidence/{evidence_id}/download

Downloads the evidence file.

Access should be logged for audit purposes.

⸻

Verify Evidence Integrity

POST /api/v1/evidence/{evidence_id}/verify

Verifies file hash to ensure evidence integrity.

Response:

{
  "evidence_id": "EVD-20260330-0001",
  "integrity_status": "verified"
}


⸻

Update Evidence Metadata

PUT /api/v1/evidence/{evidence_id}

Update description, tags, retention policy.

⸻

Archive Evidence

POST /api/v1/evidence/{evidence_id}/archive

Archives evidence when case is closed.

⸻

Delete Evidence (Restricted)

DELETE /api/v1/evidence/{evidence_id}

Deletion should require admin approval and audit logging.

⸻

Evidence Integrity Policy

To maintain forensic integrity:
	•	All files must have SHA256 hash
	•	Hash must be calculated at upload
	•	Integrity must be verified periodically
	•	Evidence files should be immutable
	•	Access must be logged
	•	Deletion must be restricted
	•	Retention policy must be enforced
	•	Chain of custody must be recorded

⸻

Evidence Audit Log Example

{
  "audit_id": "AUD-00921",
  "action": "download_evidence",
  "evidence_id": "EVD-20260330-0001",
  "user_id": "USR-004",
  "timestamp": "2026-03-30T11:20:00Z",
  "ip_address": "203.0.113.55"
}


⸻

Evidence Storage Architecture (Recommended)

Evidence files should be stored in secure object storage:

Examples:
	•	AWS S3
	•	Cloudflare R2
	•	Azure Blob Storage
	•	Google Cloud Storage

Metadata should be stored in the NSD database, not inside file storage.

⸻

Evidence Lifecycle

Evidence lifecycle:

Upload → Verify → Store → Link to Case → Use in Investigation
→ Archive → Retain → Delete (after retention period)


⸻
