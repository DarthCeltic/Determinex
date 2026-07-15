# Human Approval Source-Mutation Gate

> Locked under `locks/sentinel/HUMAN_APPROVAL_SOURCE_MUTATION_GATE_LOCK_001.json`.
> Evidence: `assurance/evidence/human_approval_source_mutation_gate/run_20260527.json`.

The approval gate is the only place the apparatus says "yes, this
verified temp patch may be applied to the original repo." Source
mutation is **blocked by default**. The gate itself performs no write
— it returns an `ApprovalGateDecision` that an IDE/CLI consumer would
honor under its own audited write path.

## Approval packet

```python
@dataclass(frozen=True)
class ApprovalPacket:
    trace_id: str
    workspace_identity: str
    diff_sha256: str
    verifier_status: str
    timestamp_utc: str
    operator: str
    approval_token: str
    fixture: bool = True
```

Every field must match the corresponding field in the
`VerifiedRepairTrace` being approved. Any mismatch yields a specific
blocked status.

## Decision matrix

| Failure                                  | Decision                                          |
|------------------------------------------|---------------------------------------------------|
| Empty `operator`                         | `SOURCE_MUTATION_BLOCKED_OPERATOR_EMPTY`          |
| Empty `approval_token`                   | `SOURCE_MUTATION_BLOCKED_MISSING_APPROVAL`        |
| `trace_id` mismatch                      | `SOURCE_MUTATION_BLOCKED_TRACE_ID_MISMATCH`       |
| `workspace_identity` mismatch            | `SOURCE_MUTATION_BLOCKED_REPO_MISMATCH`           |
| `diff_sha256` mismatch (or empty)        | `SOURCE_MUTATION_BLOCKED_DIFF_MISMATCH`           |
| Trace verifier_status not PASSED_TEMP    | `SOURCE_MUTATION_BLOCKED_VERIFIER_NOT_PASSED`     |
| Trace final_status not PASSED_TEMP       | `SOURCE_MUTATION_BLOCKED_STALE_TRACE`             |
| All checks pass                          | `SOURCE_MUTATION_APPROVAL_ACCEPTED_FIXTURE`       |

`HumanApprovalGate.required(trace)` emits a
`SOURCE_MUTATION_APPROVAL_REQUIRED` decision suitable for an IDE to
render the approval surface.

## FIXTURE suffix

The accepted token is `SOURCE_MUTATION_APPROVAL_ACCEPTED_FIXTURE` on
purpose. This rung does not admit live operator approvals — it pins the
decision logic. A future rung adding the live path (with timestamp
expiry, single-use nonce, signed token) introduces a distinct
`SOURCE_MUTATION_APPROVAL_ACCEPTED_LIVE` token without breaking the
closed set.

## What this lock does *not* do

* No actual original-repo write. The IDE/CLI consumer of an
  `ACCEPTED_FIXTURE` decision is responsible for the write under its
  own audited path.
* No replay protection (timestamp staleness, nonce, expiry). Live
  semantics are deferred.
* No file I/O. The gate is a pure decision function.

## Reproducing the evidence

```
.\.venv\Scripts\python.exe -m pytest tests/repair/test_human_approval_source_mutation_gate_lock.py -q --tb=short
```
