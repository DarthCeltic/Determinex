# Post-Apply Verifier — No Default Pass

> Locked under `locks/sentinel/POST_APPLY_VERIFIER_NO_DEFAULT_PASS_LOCK_001.json`.

Remediates **CLAUDE-AUTH-003**: previously `verifier=None` would
silently default to `stub_verifier_pass`, producing
`POST_APPLY_VERIFIER_PASSED` for free.

The fix changes `scripts/repair/post_apply_verifier.run`:

- `verifier=None` →
  `POST_APPLY_VERIFIER_BLOCKED_MISSING_VERIFIER` with
  `POST_APPLY_VERIFIER_EXPLICIT_REQUIRED` in `statuses_seen`.
- Stub callables (`stub_verifier_pass`, `stub_verifier_fail`) without
  `fixture_mode=True` →
  `POST_APPLY_VERIFIER_BLOCKED_FIXTURE_VERIFIER_IN_LIVE_PATH`.
- Stubs are still usable when the caller explicitly passes
  `fixture_mode=True` (so existing fixture-only tests still work).
- A real (non-stub) verifier callable runs normally.

The rung-8 orchestrator
(`real_approval_apply_post_verify_trace`) builds a real
hardened-runner-backed callable that is not a stub, so production
flow is unaffected.
