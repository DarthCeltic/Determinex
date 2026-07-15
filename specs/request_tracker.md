# Request Tracker CLI

## Overview
A command-line tool written in Python that tracks requests, shows which ones are 
pending, and lets the user approve or reject them. Requests persist between runs 
via a JSON file.

## Commands

### `reqtrack add <title> [--description <text>]`
Add a new request. Assigns a unique integer ID and sets status to "pending".

### `reqtrack list [--status pending|approved|rejected|all]`
Display requests in a formatted table. Default: show all. Columns: ID, Status, Title, Created.
Pending requests are highlighted (ANSI yellow). Approved = green. Rejected = red.

### `reqtrack approve <id>`
Set a request's status to "approved". Print confirmation.

### `reqtrack reject <id> [--reason <text>]`
Set a request's status to "rejected". Optionally store a rejection reason.

### `reqtrack show <id>`
Show full details of a single request: ID, title, description, status, reason, timestamps.

### `reqtrack clear --status rejected`
Remove all requests matching a given status. Requires confirmation prompt.

## Data Model
Stored in `~/.reqtrack/requests.json` as a JSON array:
```json
[
  {
    "id": 1,
    "title": "Add dark mode",
    "description": "Support system dark mode preference",
    "status": "pending",
    "reason": null,
    "created_at": "2026-04-24T18:00:00",
    "updated_at": "2026-04-24T18:00:00"
  }
]
```

## Implementation
- Single file: `reqtrack.py`
- Entry point: `if __name__ == "__main__"` using `argparse` with subparsers
- No third-party dependencies (stdlib only: argparse, json, pathlib, datetime, sys, os)
- Storage: `~/.reqtrack/requests.json`, created on first run
- IDs are auto-incrementing integers starting at 1
- All timestamps in ISO 8601 format
- Exit code 0 on success, 1 on error (unknown ID, etc.)

## Python Typing Rules (mypy strict)
- Fields that can be absent must be typed `Optional[str] = None`, never `str = None`
- Use `from typing import Optional` at the top of the file
- Dict values that may be null must be typed `dict[str, Optional[str]]`, not `dict[str, str]`
- Never assign `None` to a variable typed as `str` — use `""` as the empty default for required string fields
- **Do NOT use dataclasses.** Request objects are plain Python `dict` values stored in a `list[dict]`

## Error Handling
- Unknown ID: print "Error: request #N not found" to stderr, exit 1
- Empty list: print "No requests found." with a hint to use `reqtrack add`
- Corrupt JSON: print warning, offer to reset the store
