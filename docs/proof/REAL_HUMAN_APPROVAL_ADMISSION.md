# Real Human Approval Admission

> Locked under `locks/sentinel/REAL_HUMAN_APPROVAL_ADMISSION_LOCK_001.json`.

`scripts/ide/real_human_approval_admission.py` is a strict admission
gate that distinguishes a REAL operator approval from the fixture
path used by tests/UI previews.

Required for `REAL_HUMAN_APPROVAL_ACCEPTED`:

- temp verify record `REAL_TEMP_PATCH_VERIFIER_PASSED`
- observed `verifier_status == PATCH_VERIFIER_PASSED_TEMP_ONLY`
- observed diff hash == packet diff hash
- `expected_stale_after` parseable and in the future
- `submitted_action == "approve"`
- `submitted_operator_identity` non-empty
- `submitted_signature_kind == "real_local_signed"`
- `submitted_signature` is a 64-char hex digest

Block codes: `BLOCKED_STALE`, `BLOCKED_DIFF_MISMATCH`,
`BLOCKED_VERIFIER_NOT_PASSED`, `BLOCKED_FIXTURE`,
`BLOCKED_OPERATOR_EMPTY`, `BLOCKED_SIGNATURE_INVALID`. Other
decisions: `REJECTED` (explicit reject) and `REQUIRED` (no action
submitted yet).

Accepting an approval still leaves
`source_mutation_authorized=False`. The rollback-snapshot and
source-apply rungs are the only places that flip that.
