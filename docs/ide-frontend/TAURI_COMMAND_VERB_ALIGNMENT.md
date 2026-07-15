# Tauri Command Verb Alignment

> Locked under `locks/sentinel/TAURI_COMMAND_VERB_ALIGNMENT_LOCK_001.json`.

Remediates **CLAUDE-AUTH-006**: previously the Tauri command
`source_apply_dry_run` aliased to the backend command
`get_repair_state`, which returned a repair-state record. The verb
implied an apply attempt; the behavior was a state read.

The fix:

- `scripts/ide/backend_command_surface.py` adds a dedicated
  `source_apply_dry_run` inner command and `_source_apply_dry_run`
  handler that returns a payload with:
  - `mode: "dry_run_only"`
  - `source_apply_attempted: False`
  - `source_mutation: "BLOCKED_PENDING_REAL_HUMAN_APPROVAL"`
  - `training_eligible: False`
- `scripts/ide/_tauri_driver.py` is updated so `source_apply_dry_run`
  routes to the new inner command (not `get_repair_state`).
- Status code remains `TAURI_COMMAND_SOURCE_MUTATION_BLOCKED`.

No real source apply is attempted. The verb now matches the behavior.
