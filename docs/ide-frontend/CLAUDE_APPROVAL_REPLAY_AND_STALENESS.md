# Approval Replay & Staleness

> Locked under
> `locks/sentinel/CLAUDE_APPROVAL_REPLAY_AND_STALENESS_LOCK_001.json`.

Remediates **CLAUDE-AUTH-016** (no replay-protection) and
**CLAUDE-AUTH-013** (no freshness window).

## ApprovalPacket fields

| Field | Purpose |
|---|---|
| `approval_id` | Monotonic nonce; consumed on first use |
| `timestamp_epoch_s` | Issuance time (epoch seconds) |
| `trace_id` | Audit trace |
| `workspace_identity_hash` | sha256 of workspace path |
| `canonical_patch_body_hash` | sha256 over sorted patch rows |
| `verifier_ref` | Identifier of the temp-verifier run |
| `rollback_snapshot_ref` | Identifier of the rollback snapshot |

## Verifier refusal codes

| Decision | Cause |
|---|---|
| `APPROVAL_REPLAY_BLOCKED_REUSED_NONCE` | `approval_id` already in ledger |
| `APPROVAL_REPLAY_BLOCKED_STALE_APPROVAL` | `age > max_age_seconds` (default 24h) |
| `APPROVAL_REPLAY_BLOCKED_WORKSPACE_MISMATCH` | packet bound to a different workspace |
| `APPROVAL_REPLAY_BLOCKED_PATCH_BODY_MISMATCH` | packet bound to a different patch body |
| `APPROVAL_REPLAY_BLOCKED_VERIFIER_REF_MISMATCH` | packet bound to a different verifier |
| `APPROVAL_REPLAY_BLOCKED_SNAPSHOT_REF_MISMATCH` | packet bound to a different snapshot |
| `APPROVAL_REPLAY_BLOCKED_MALFORMED_PACKET` | missing / NUL / negative ts / wrong shape |

## Replay attack scenario (test)

A previously valid `("captured", body=B, ws=W)` packet:

- Replayed in the same workspace later → `REUSED_NONCE`
- Replayed in a different workspace → `REUSED_NONCE` (nonce check runs first)
- Replayed with a different patch body → `REUSED_NONCE`

The nonce ledger short-circuits before bind checks, so the
attacker can't piece together a new mismatch surface.

## Pluggable ledger

`NonceLedger` is a protocol — `__contains__`/`add`. Default is
`InMemoryNonceLedger`. A persistent ledger (sqlite, file-backed)
can be wired in without touching the verifier.
