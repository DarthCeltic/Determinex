# Real Build-Adapter Temp Verify Trace

> Locked under `locks/sentinel/REAL_BUILD_ADAPTER_TEMP_VERIFY_TRACE_LOCK_001.json`.

`scripts/repair/real_build_adapter_temp_verify_trace.py` composes
the locked `SafePatchWorkspace` + `REAL_TEMP_PATCH_VERIFY_LOCK_001`
modules with a real verifier callable that invokes the
build-adapter command (e.g. `pytest -q`, `cargo test`, `go test`)
through `intake.hardened_runner.run`.

The plan is applied to a temp workspace; the verifier runs there;
the original workspace is **never** touched. Pre/post sha256 of the
original tree is recorded as a defense-in-depth invariant.

Decisions:

| Decision | Meaning |
|---|---|
| `PASSED_APPROVAL_REQUIRED` | verifier exit 0 on temp; human approval needed |
| `FAILED` | verifier non-zero / timed out / blocked |
| `BLOCKED_NOT_QUARANTINED` | upstream plan missing or not quarantined |
| `BLOCKED_NO_VERIFIER` | verifier selection missing or blocked |
| `BLOCKED_HARDENED_RUNNER` | hardened runner import failed |
| `BLOCKED_APPLY_REJECTED` | safe-patch apply blocked |

`source_mutation_authorized=False`, `training_eligible=False`,
`SOURCE_UNCHANGED` always in `statuses_seen`.
