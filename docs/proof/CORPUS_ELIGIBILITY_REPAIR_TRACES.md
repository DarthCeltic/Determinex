# Corpus Eligibility — Repair Traces

> Locked under `locks/sentinel/CORPUS_ELIGIBILITY_REPAIR_TRACE_GUARD_LOCK_001.json`.
> Evidence: `assurance/evidence/corpus_eligibility_repair_trace_guard/run_20260527.json`.

The eligibility guard is the apparatus's *training data* boundary. It
makes the difference between **evidence** and **training data**
explicit, and pins it in a closed set of blocked reasons.

## Evidence vs training data

| Artifact            | Lives in                  | Purpose                                       |
|---------------------|---------------------------|-----------------------------------------------|
| `VerifiedRepairTrace` | `assurance/evidence/`     | Signed, indexed; auditable replay             |
| Training corpus row | `corpus/` (gated)         | Input to model fine-tuning                    |

Every trace this apparatus produces is valid *evidence*. None of them
are valid *training data* at this rung.

## Blocked reasons (closed set)

| Reason                            | When it fires                                            |
|-----------------------------------|----------------------------------------------------------|
| `BLOCKED_MOCKED_MODEL_OUTPUT`     | Trace routed through `MockModelClient` (always today)    |
| `BLOCKED_TEMP_WORKSPACE_ONLY`     | Patch only ever applied to `SafePatchWorkspace` temp    |
| `BLOCKED_NO_LIVE_MODEL_CALL`      | No live model was invoked (always today)                 |
| `BLOCKED_POLICY`                  | Default policy refuses corpus admission                  |
| `BLOCKED_SOURCE_NOT_APPROVED`     | No accepted `ApprovalGateDecision` supplied              |
| `BLOCKED_HUMAN_APPROVAL_REQUIRED` | Approval is `None` or `REQUIRED`                         |
| `BLOCKED_VERIFIER_FAILED`         | `safe_patch_result.verifier_status == PATCH_VERIFIER_FAILED` |
| `BLOCKED_UNSUPPORTED_REPO`        | `trace.final_status == TRACE_BLOCKED_UNSUPPORTED_REPO`   |

## Why the guard always blocks

At this rung, every trace fails at least four checks (mocked / temp /
no-live / policy). Even a FIXTURE-accepted approval clears only one
reason (`SOURCE_NOT_APPROVED`); the rest still apply.

A future rung can flip individual policy flags. Even with every flag
flipped, the decision is `CORPUS_ELIGIBILITY_EVIDENCE_ONLY` — never
`ELIGIBLE`. Eligibility requires a *positive* admission step, not just
the absence of blockers.

## What this lock does *not* do

* No corpus row write. The guard is a decision; the existing
  `CORPUS_WRITE_GUARD_LOCK_001` enforces the actual file-system
  refusal.
* No flipping of `training_eligible` to True under any policy. The
  scalar is locked False at this rung.
* No live-model integration.

## Reproducing the evidence

```
.\.venv\Scripts\python.exe -m pytest tests/corpus/test_corpus_eligibility_repair_trace_guard_lock.py -q --tb=short
```
