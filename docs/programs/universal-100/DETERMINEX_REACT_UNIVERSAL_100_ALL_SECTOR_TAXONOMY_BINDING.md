# Determinex React Universal 100 All-Sector Taxonomy Binding

Lock: `DETERMINEX_REACT_UNIVERSAL_100_ALL_SECTOR_TAXONOMY_BINDING_LOCK_001`

Loader decision: `REACT_UNIVERSAL_100_ALL_SECTOR_TAXONOMY_BINDING_PASSED`

## Summary

Read-only React binding of Codex Universal 100 all-sector taxonomy (40 sectors; 40 top-level families; 40 routing templates; 40 missing-rung templates). Routing only — every sector defaults to NOT_CLAIMED / classified.

## Claim boundary

- Read-only React binding to Codex all-sector taxonomy evidence.
- Taxonomy is routing structure, not support proof.
- Every sector defaults to NOT_CLAIMED / classified; membership does not promote capability.
- Missing-rung templates document the path required to grow support; they are not a support claim.
- No source mutation, training, release, approval, proof-execution, or broad-claims granted.

## Captions

- This panel displays evidence; it does not grant authority.
- Taxonomy is routing structure, not support proof.
- "Taxonomy family present" does not mean capability exists.
- Default claim state remains NOT_CLAIMED; default support state remains classified.
- No source mutation without authority.
- Universal 100 means universal intake/routing, not magic execution.
- Blocked cells are visible by exact missing rung.

## Hard rules enforced

- status mismatch -> BLOCKED_MALFORMED
- authority flag true -> BLOCKED_AUTHORITY_CONFUSION
- broad_claims_granted true -> BLOCKED_BROAD_CLAIM
- sectors missing or empty -> BLOCKED_MALFORMED
- sector_count != len(sectors) -> BLOCKED_MALFORMED
- sector default_support_state above scaffold_only -> BLOCKED_TAXONOMY_OVERCLAIM
- sector default_claim_state in {IMPLEMENTED, IMPLEMENTED_WITH_CAVEATS, PARTIAL} -> BLOCKED_TAXONOMY_OVERCLAIM
- forbidden broad-claim phrase as current claim outside refusal context -> BLOCKED_BROAD_CLAIM
- evidence absent/corrupt -> AWAITING_EVIDENCE

## Deferred bindings

- `DETERMINEX_REACT_UNIVERSAL_100_CONVEYOR_BACKLOG_AND_DEPTH_QUEUE_BINDING_LOCK_001` — Codex source lock DETERMINEX_UNIVERSAL_100_CONVEYOR_BACKLOG_AND_DEPTH_QUEUE_LOCK_001 not present in locks/sentinel/. Awaiting Codex commit of the backlog + depth-promotion-candidate queue evidence.
