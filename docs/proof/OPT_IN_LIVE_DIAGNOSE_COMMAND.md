# Opt-In Live Diagnose Command

> Locked under `locks/sentinel/OPT_IN_LIVE_DIAGNOSE_COMMAND_LOCK_001.json`.

Opt-in CLI/API entry that runs diagnose-only against an admitted
local model config. Requires explicit `opt_in=True`. Response captured
as advisory; verifier remains source of truth. No patch, no source
mutation, no corpus row.
