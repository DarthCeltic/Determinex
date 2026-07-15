# Frontend Command Invoke Client

> Locked under `locks/sentinel/FRONTEND_COMMAND_INVOKE_CLIENT_LOCK_001.json`.

Typed wrapper at `frontend/src/lib/ide-invoke-client.ts` layered on the
already-locked `ide-repair-api.ts`. Provides discriminated-union request
shapes per command, a pluggable `IdeInvokeTransport` (real Tauri or mock
for tests), Tauri-unavailable surfaced as a typed status, and unknown
commands rejected with a safe response. Errors are visible via the
standard `IdeRepairResponse.notes` channel — panels never throw.
