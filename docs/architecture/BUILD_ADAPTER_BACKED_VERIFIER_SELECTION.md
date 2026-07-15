# Build-Adapter-Backed Verifier Selection

> Locked under `locks/sentinel/BUILD_ADAPTER_BACKED_VERIFIER_SELECTION_LOCK_001.json`.

`scripts/repair/build_adapter_backed_verifier_selection.py` picks a
real verifier command for a workspace using the locked
`BuildAdapterRegistry`. The chosen `test_framework_id`
(e.g. `pytest`, `cargo test`, `go test`) is `shlex.split` into a
deterministic argv. The argv is recorded but NEVER executed by
this lock — the downstream rung calls `intake.hardened_runner.run`
to actually invoke it.

Decisions:

- `SELECTED` — adapter matched, command derived
- `BLOCKED_UNSUPPORTED_REPO` — only `UnknownAdapter` matched
- `BLOCKED_NO_TEST_COMMAND` — adapter has no `test_framework_id`
- `BLOCKED_HARDENED_RUNNER` — `intake.hardened_runner` unavailable
- `BLOCKED_WORKSPACE_MISSING` — workspace path does not exist

`verifier_command_executed=False`, `source_mutation_authorized=False`,
`training_eligible=False` on every record.
