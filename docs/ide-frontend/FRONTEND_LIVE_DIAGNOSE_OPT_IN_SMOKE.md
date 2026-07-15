# Frontend Live Diagnose Opt-In Smoke

> Locked under `locks/sentinel/FRONTEND_LIVE_DIAGNOSE_OPT_IN_SMOKE_LOCK_001.json`.

Drives the visible diagnose flow through the production
`_tauri_driver._dispatch` in-process and asserts the gate ladder
fires correctly:

1. Dry-run path always succeeds.
2. Live path is blocked without `opt_in=True`.
3. Live path is blocked when no provider is configured even with
   `opt_in=True` (`TAURI_COMMAND_BLOCKED_NO_MODEL`).
4. Output is advisory only; the smoke never asks for a patch.

No subprocess. No socket. No source mutation. No training row.
