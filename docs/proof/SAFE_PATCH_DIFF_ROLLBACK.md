# Safe Patch Workspace

> Locked under `locks/sentinel/SAFE_PATCH_DIFF_ROLLBACK_LOCK_001.json`.
> Evidence: `assurance/evidence/safe_patch_diff_rollback/run_20260527.json`.

`SafePatchWorkspace` is the bounded surface that lets a candidate patch
be applied to a repo **without ever touching the original**. It stages a
copy under a caller-supplied `temp_root`, validates each `FilePatch`,
applies the changes to the temp copy, computes a unified diff, and runs
an injected verifier callable.

## Hard invariants

1. The original repo is treated as immutable. The applier hashes the
   tree before and after every call; any divergence flips the status to
   `SOURCE_MUTATION_BLOCKED`.
2. All writes go to `<temp_root>/safe_patch_<workspace_id>/`. A baseline
   snapshot at `<temp_root>/safe_patch_<workspace_id>__BASELINE_/` is
   used to compute the diff.
3. `rollback()` deletes both the temp and the baseline. It is
   idempotent.

## Patch validation

Each `FilePatch(path, new_content)` is checked in order. The first
rejection short-circuits with the appropriate status:

| Status                              | When                                                  |
|-------------------------------------|-------------------------------------------------------|
| `PATCH_BLOCKED_PATH_ESCAPE`         | `..`, absolute, drive-anchored, or empty path         |
| `PATCH_BLOCKED_SYMLINK_ESCAPE`      | target is a symlink, or resolves outside temp         |
| `PATCH_BLOCKED_BINARY_CONTENT`      | content contains a NUL byte                           |
| `PATCH_REJECTED`                    | per-file size > 2 MB or total > 16 MB                 |
| `PATCH_APPLIED_TO_TEMP_WORKSPACE`   | all validations passed; write complete                |

## Verifier callable

```python
def my_verifier(temp_workspace: Path) -> VerifierResult:
    ...
    return VerifierResult(passed=True, output="cargo check: 0 errors")
```

The verifier is the only place where toolchain invocation might happen.
This rung ships only stub verifiers (`stub_verifier_pass`,
`stub_verifier_fail`). The real BuildAdapter-backed verifier composes
on top in `VERIFIED_REPAIR_TRACE_LOCK_001`.

## Rollback semantics

* `rollback_on_failure=True` (default) — deletes the temp tree on
  verifier failure and sets status `PATCH_ROLLED_BACK`.
* `rollback_on_failure=False` — temp tree persists for debugging; the
  status stays `PATCH_APPLIED_TO_TEMP_WORKSPACE` with
  `verifier_status=PATCH_VERIFIER_FAILED`.

In both cases the original repo is unchanged.

## What this lock does *not* do

* No real toolchain invocation. The verifier is a callable.
* No source mutation, ever. The original repo is read once for staging
  and never written.
* No corpus row, no training eligibility.
* No hunk-level diff application. Patches are file-replacement only.

## Reproducing the evidence

```
.\.venv\Scripts\python.exe -m pytest tests/repair/test_safe_patch_diff_rollback_lock.py -q --tb=short
```
