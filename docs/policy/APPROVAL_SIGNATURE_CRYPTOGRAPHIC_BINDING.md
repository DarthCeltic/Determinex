# Approval Signature Cryptographic Binding

> Locked under `locks/sentinel/APPROVAL_SIGNATURE_CRYPTOGRAPHIC_BINDING_LOCK_001.json`.

Remediates **CLAUDE-AUTH-008**: previously the strict admission gate
verified only `_is_hex64(signature)` — any 64-char hex string passed.

The fix introduces `scripts/ide/local_signing.py`:

- Canonical payload: `v1`-tagged LF-separated key/value lines binding
  `trace_id`, `canonical_patch_body_hash`, `diff_hash`,
  `verifier_status`, `rollback_snapshot_ref`,
  `sha256(workspace_identity)`, `operator_identity`, `stale_after`
- Per-host secret stored at `~/.determinex/local_signing_secret`
  (32 random bytes, `0600` on POSIX, generated on first call)
- `sign(payload)` returns hex HMAC-SHA256
- `verify(payload, signature)` uses constant-time comparison

The admission gate (`real_human_approval_admission.admit`) now:

- Requires `signature_kind == "real_local_hmac"` — the legacy
  `real_local_signed` is rejected as `BLOCKED_FIXTURE`
- Builds the canonical payload from the same inputs the operator's
  signing flow used and HMAC-verifies the submitted signature

Tampering with any field (operator identity, diff hash, body hash,
verifier status, stale_after, etc.) invalidates the signature. The
workspace identity never appears in the payload verbatim — it is
hashed first.

Future upgrade path: ed25519 asymmetric signatures with a per-host
public-key registry. Pinned for a later lock.
