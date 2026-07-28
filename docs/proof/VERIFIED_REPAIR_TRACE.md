# Verified Repair Trace

> Locked under `locks/sentinel/VERIFIED_REPAIR_TRACE_LOCK_001.json`.
> Evidence: `assurance/evidence/verified_repair_trace/run_20260527.json`.

The verified repair trace is the apparatus proof — the moment the four
foundation rungs compose into a single, signed, end-to-end record.

```
intake
  → adapter detection             (BuildAdapterRegistry — read-only)
  → verifier baseline             (stub or injected callable)
  → route decisions               (ModelRouter, per task class, LIVE mode)
  → mocked patch plan             (MockModelClient — canned responses)
  → temp patch application        (SafePatchWorkspace — temp-only)
  → verifier result               (injected callable on temp workspace)
  → source-preservation check     (sha256 tree before == after)
  → VerifiedRepairTrace assembly  (signed dataclass + JSON)
```

## Trace identity

* `trace_id` — sha256 over `(workspace, salt, canned_kind)`. Reproducible
  from inputs alone; tests pin it.
* `trace_fingerprint` — sha256 over canonical JSON of the trace.
  Captures the full output. Stable across repeated `to_json()` calls of
  the same trace; will vary across runs only via fields that legitimately
  differ (e.g. temp_workspace path).

## Final statuses

| Status                            | Meaning                                                           |
|-----------------------------------|-------------------------------------------------------------------|
| `VERIFIED_REPAIR_TRACE_WRITTEN`   | Generic terminal (rare; usually a more specific status fires)     |
| `TRACE_VERIFIER_PASSED_TEMP_ONLY` | Patch applied to temp + verifier passed                           |
| `TRACE_VERIFIER_FAILED`           | Patch applied to temp + verifier rejected; safe-patch rolled back |
| `TRACE_PATCH_FAILED`              | Safe-patch rejected the patch (path escape / symlink / binary)    |
| `TRACE_BLOCKED_NO_VERIFIER`       | Verifier callable was None and patch applied                      |
| `TRACE_BLOCKED_NO_ROUTE`          | Router blocked BUILD_DIAGNOSIS or PATCH_GENERATION                |
| `TRACE_BLOCKED_UNSUPPORTED_REPO`  | UnknownAdapter selected; no mock invocation, no patch              |

`TRACE_SOURCE_UNCHANGED_CONFIRMED` and `TRAINING_ELIGIBLE_FALSE` always
appear in `statuses_seen` on every supported path.

## Source-preservation

The runner asserts `original_unchanged` through the safe-patch layer.
Across all five fixtures (`python_broken`, `rust_broken`, `go_broken`,
`ts_broken`, `unsupported_repo`), the workspace sha256 tree before
`runner.run()` equals the sha256 tree after.

## Corpus and training eligibility

Every `VerifiedRepairTrace` carries:

* `corpus_eligibility = "BLOCKED_BY_DEFAULT"` — set on construction, not
  flippable by the runner.
* `training_eligible = False` — set on construction, never flipped.

Corpus admission for repair traces lives behind
`CORPUS_ELIGIBILITY_REPAIR_TRACE_GUARD_LOCK_001`. The trace is the
*evidence*; whether it becomes a *training row* is a separate gate.

## What this lock does *not* do

* No real toolchain invocation in tests. Tests use `stub_verifier_pass`
  and `stub_verifier_fail`. Real BuildAdapter-backed verifiers are
  opt-in via the `verifier` argument.
* No human-approval gate yet — that's the next rung
  (`HUMAN_APPROVAL_SOURCE_MUTATION_GATE_LOCK_001`). The trace
  *prepares* the packet a future gate would consume.
* No corpus row write.

## Reproducing the evidence

```
.\.venv\Scripts\python.exe -m pytest tests/repair/test_verified_repair_trace_lock.py -q --tb=short
```
