# Apply Gate Fixture Refusal

> Locked under `locks/sentinel/APPLY_GATE_FIXTURE_REFUSAL_LOCK_001.json`.

Remediates **CLAUDE-AUTH-002**: previously `is_fixture` /
`signature_kind` checks lived only at the strict admission
constructor and the rung-8 orchestrator. A direct caller of
`source_mutation_apply_after_approval` with a fixture-`ACCEPTED`
record would write source.

The fix adds two new fail-closed checks at the apply boundary:

- `SOURCE_MUTATION_BLOCKED_FIXTURE_APPROVAL` — `approval.is_fixture` is `True`
- `SOURCE_MUTATION_BLOCKED_INVALID_SIGNATURE_KIND` — `signature_kind`
  is not in `{"real_local_signed", "real_local_hmac"}`

The `real_local_hmac` value is reserved for rung 7's cryptographic
binding upgrade. Existing production tests using `real_local_signed`
continue to pass.

Regression coverage:
- `test_claude_auth_002_fixture_approval_blocked`
- `test_claude_auth_002_invalid_signature_kind_blocked`
