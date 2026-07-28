# Determinex React Universal 100 Support Depth Ledger Binding

Lock: `DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_DEPTH_LEDGER_BINDING_LOCK_001`

Loader decision: `REACT_UNIVERSAL_100_SUPPORT_DEPTH_LEDGER_BINDING_PASSED`

## Summary

Read-only React binding of Codex Universal 100 support-depth ledger (59 known cells; 34 fixture-local smoke; 7 test; 3 repair; 1 maintain; 1 teach; 0 user-ready; 0 release-supported).

## Claim boundary

- Read-only React binding to Codex support-depth ledger evidence.
- Support-depth ledger is accounting, not promotion.
- "Accounted for" does not mean "supported."
- "Smoke-supported" does not mean "production-ready."
- "Fixture-local" does not mean "real user repo authorized."
- "User-ready" remains false unless Codex evidence explicitly proves it.
- "Release-supported" remains false unless packaging/fresh-install/release gates explicitly prove it.
- "Missing rung named" is progress, not support.
- No source mutation, training, release, approval, proof-execution, or broad-claims granted.

## Captions

- This panel displays evidence; it does not grant authority.
- Support-depth ledger is accounting, not promotion.
- "Accounted for" does not mean "supported."
- "Smoke-supported" does not mean "production-ready."
- "Fixture-local" does not mean "real user repo authorized."
- "User-ready" remains false unless Codex evidence explicitly proves it.
- "Release-supported" remains false unless packaging/fresh-install/release gates explicitly prove it.
- "Missing rung named" is progress, not support.
- Universal 100 means universal intake/routing, not magic execution.
- Blocked cells are visible by exact missing rung.

## Hard rules enforced

- status mismatch -> BLOCKED_MALFORMED
- authority flag true -> BLOCKED_AUTHORITY_CONFUSION
- broad_claims_granted true -> BLOCKED_BROAD_CLAIM
- summary.total_known_cells missing -> BLOCKED_MALFORMED
- summary.support_depth_counts missing or empty -> BLOCKED_MALFORMED
- support_depth_counts.release_supported > 0 without release-proof source path -> BLOCKED_RELEASE_OVERCLAIM
- support_depth_counts.user_ready_with_caveats > 0 without user-ready-proof source path -> BLOCKED_USER_READY_OVERCLAIM
- forbidden broad-claim phrase as current claim -> BLOCKED_BROAD_CLAIM
- evidence absent/corrupt -> AWAITING_EVIDENCE
