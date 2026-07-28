# Arbitrary Repo Readiness Matrix

> Locked under `locks/sentinel/ARBITRARY_REPO_READINESS_MATRIX_LOCK_001.json`.
> Evidence: `assurance/evidence/arbitrary_repo_readiness_matrix/run_20260527.json`.

A machine-readable matrix that says, for each `(language, build_system,
test_framework)` row, exactly how ready the apparatus is to repair an
arbitrary repo of that shape.

## Rows

| Language    | Build system | Test framework | Adapter | Verifier | Mocked trace | Safe patch | IDE state | Corpus guard |
|-------------|--------------|----------------|---------|----------|--------------|------------|-----------|--------------|
| Python      | `pip`        | `pytest`       | ✓       | ✓        | ✓            | ✓          | ✓         | ✓            |
| Rust        | `cargo`      | `cargo test`   | ✓       | ✓        | ✓            | ✓          | ✓         | ✓            |
| Go          | `go`         | `go test`      | ✓       | ✓        | ✓            | ✓          | ✓         | ✓            |
| TypeScript  | `npm`        | `jest`         | ✓       | ✓        | ✓            | ✓          | ✓         | ✓            |
| TypeScript  | `npm`        | `vitest`       | ✓       | ✓        | ✓            | ✓          | ✓         | ✓            |
| Java        | `maven`      | `junit`        | ✓       | ✓        | ✓            | ✓          | ✓         | ✓            |
| Java        | `gradle`     | `junit`        | ✓       | ✓        | ✓            | ✓          | ✓         | ✓            |
| Unknown     | `unknown`    | —              | ✗       | ✗        | ✗            | ✗          | ✓         | ✓            |

## Ready levels (closed set)

| Level                                  | Meaning                                                  |
|----------------------------------------|----------------------------------------------------------|
| `READY_MOCKED_TRACE`                   | Full mocked end-to-end trace works for this row's shape  |
| `READY_TEMP_PATCH_ONLY`                | Verifier-backed, no live model admission                 |
| `READY_REQUIRES_LIVE_MODEL_ADMISSION`  | Foundation landed, awaiting live model admission         |
| `READY_REQUIRES_VERIFIER`              | Adapter exists but verifier coverage is missing/partial  |
| `BLOCKED_UNSUPPORTED`                  | No adapter; cannot proceed                               |

`live_model_admitted` is **False** on every row at this rung — no row
falsely claims live admission. A future LIVE rung produces a
regenerated matrix with selected rows flipped.

## What this lock does *not* do

* No execution. No subprocess. No network.
* No false ready claim. Unsupported rows are explicitly
  `BLOCKED_UNSUPPORTED`.
* No row admits a live model.

## Reproducing the evidence

```
.\.venv\Scripts\python.exe -m pytest tests/intake/test_arbitrary_repo_readiness_matrix_lock.py -q --tb=short
```
