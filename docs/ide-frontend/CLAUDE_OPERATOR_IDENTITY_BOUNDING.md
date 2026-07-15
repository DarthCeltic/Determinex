# Operator Identity Bounding

> Locked under `locks/sentinel/CLAUDE_OPERATOR_IDENTITY_BOUNDING_LOCK_001.json`.

Reduces residual risk from **CLAUDE-AUTH-014**:
`operator_identity` on `RealHumanApprovalAdmissionRecord` is a free
string.

## BoundedOperatorIdentity

| Field | Constraint |
|---|---|
| `operator_id` | non-empty, no NUL, ≤128 chars |
| `display_name` | no NUL, ≤256 chars |
| `signing_key_ref` | sha256(secret-file path), 64 hex |
| `timestamp` | non-empty |
| `workspace_identity_hash` | sha256(workspace path), 64 hex |
| `approval_payload_hash` | sha256(canonical approval payload), 64 hex |

## The bound check

`scripts/ide/operator_identity_bounding.check(admission, bound)` returns
`OPERATOR_IDENTITY_BOUNDING_PASSED` iff:

1. `admission.is_accepted` and not `is_fixture`
2. `admission.signature_kind == "real_local_hmac"`
3. `bound.is_well_formed`
4. `bound.operator_id == admission.operator_identity`
5. `bound.workspace_identity_hash == sha256(admission.workspace_identity)`
6. `bound.approval_payload_hash == recomputed canonical payload hash`

## Refusal codes

| Decision | Cause |
|---|---|
| `OPERATOR_IDENTITY_BLOCKED_FREE_STRING_ONLY` | bound is `None` |
| `OPERATOR_IDENTITY_BLOCKED_MISSING_SIGNING_REF` | empty `signing_key_ref`, or admission signature_kind != real_local_hmac |
| `OPERATOR_IDENTITY_BLOCKED_PAYLOAD_MISMATCH` | operator_id / payload_hash mismatch |
| `OPERATOR_IDENTITY_BLOCKED_WORKSPACE_MISMATCH` | workspace_identity_hash mismatch |
| `OPERATOR_IDENTITY_BLOCKED_MALFORMED_IDENTITY` | bad shape (NUL, oversize, non-hex) |
| `OPERATOR_IDENTITY_BLOCKED_STALE` | reserved for the staleness rung |

## Does NOT authorize source mutation

A `PASSED` decision attests only that a named operator is coupled
to a specific admission packet. The apply gate still owns the
source-mutation decision.

## What this does NOT yet do

- No asymmetric crypto. `signing_key_ref` is sha256 of the secret
  *path*, not a public key. An ed25519 + registry upgrade path is
  reserved for a future lock.
- Not yet wired as a hard precondition into the apply gate. It is
  a validator a downstream rung may require.
