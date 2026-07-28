# Determinex React Universal 100 Top-Level Blocker Inventory Binding

Lock: `DETERMINEX_REACT_UNIVERSAL_100_TOP_LEVEL_BLOCKER_INVENTORY_BINDING_LOCK_001`

Loader decision: `REACT_UNIVERSAL_100_TOP_LEVEL_BLOCKER_INVENTORY_BINDING_PASSED`

## Summary

Read-only React binding of Codex Universal 100 top-level blocker inventory. 10 blockers classified by 5 categories. local_resolvability_counts: requires_authority_gate=1, requires_network_provider_gate=1, requires_new_harness=3, resolvable_now=3, resolvable_with_operator_install=2.

## Claim boundary

- Read-only React binding to Codex top-level blocker inventory evidence.
- 10 blockers classified across categories: AUTHORITY_MISSING=1, LOCAL_DEPENDENCY_MISSING=2, NETWORK_REQUIRED_BUT_NOT_ALLOWED=1, TOOLCHAIN_MISSING_OR_UNVERIFIED=3, VERIFIER_MISSING=3.
- Inventory classifies blockers and safe next rungs only.
- Inventory does NOT promote support or grant capability.
- Forbidden shortcuts remain forbidden.
- Operator-action and provider-gate blockers remain operator-gated.
- Local resolvability does NOT mean automatic closure.
- No source mutation, training, release, approval, proof-execution, or broad-claims authority granted.

## Captions

- This panel displays evidence; it does not grant authority.
- Inventory classifies blockers and safe next rungs only.
- Inventory does not promote support or grant capability.
- Forbidden shortcuts remain forbidden.
- Operator-action and provider-gate blockers remain operator-gated.
- Local resolvability does not mean automatic closure.
- Universal 100 means routing/accounting, not universal execution.

## Hard rules enforced

- status mismatch -> BLOCKED_MALFORMED
- authority flag true -> BLOCKED_AUTHORITY_CONFUSION
- broad_claims_granted true -> BLOCKED_BROAD_CLAIM
- blockers list absent / empty when blocker_count > 0 -> BLOCKED_MALFORMED
- blocker missing blocker_id / category / family / sector_id / local_resolvability / safe_next_rung / forbidden_shortcut -> BLOCKED_MALFORMED
- category_counts / local_resolvability_counts absent -> BLOCKED_MALFORMED
- forbidden broad-claim phrase outside refusal context -> BLOCKED_BROAD_CLAIM
- evidence absent/corrupt -> AWAITING_EVIDENCE
