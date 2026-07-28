# Real Approval Apply + Post-Apply Verifier Trace

> Locked under `locks/sentinel/REAL_APPROVAL_APPLY_POST_VERIFY_TRACE_LOCK_001.json`.

`scripts/repair/real_approval_apply_post_verify_trace.py` is the
end-to-end orchestrator for the first real Determinex repair flow:

1. Rollback snapshot is taken
2. Source is mutated (via the locked apply-after-approval gate)
3. The real build-adapter verifier runs against the mutated source
   through `intake.hardened_runner.run`
4. On verifier failure, the rollback snapshot is executed

Refusal codes:

- `REAL_APPROVAL_REQUIRED` — no approval supplied
- `BLOCKED_NO_TEMP_VERIFY` — upstream temp verify missing/failed
- `BLOCKED_NO_VERIFIER` — verifier selection missing/blocked
- `BLOCKED_NO_APPROVAL` — approval is not ACCEPTED or is fixture
- `BLOCKED_MISMATCH` — trace/diff/verifier-status binding mismatch
  or snapshot/apply blocked downstream

Pass paths:

- `REAL_APPROVAL_APPLY_POST_VERIFY_PASSED` — applied, verifier passed
- `REAL_APPROVAL_APPLY_POST_VERIFY_FAILED_ROLLBACK_REQUIRED` —
  applied, verifier failed, rollback executed

`training_eligible=False` on every record; promotion is gated by a
separate (future) global training guard.
