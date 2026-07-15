# Maintenance Bay Workflow

> Locked under `locks/sentinel/DETERMINEX_MAINTENANCE_BAY_WORKFLOW_LOCK_001.json`.

Maintenance and updates for real projects with compatibility
verifier gates.

## 8 maintenance types

`dependency_update`, `security_fix`, `docs_update`,
`test_hardening`, `refactor`, `migration`,
`formatting_lint_cleanup`, `performance_cleanup`.

## 8 UI states

`MAINTENANCE_REQUESTED`, `MAINTENANCE_PLAN_WRITTEN`,
`UPDATE_PROPOSED_QUARANTINED`, `COMPATIBILITY_VERIFIER_REQUIRED`,
`UPDATE_VERIFIED`, `UPDATE_BLOCKED_UNVERIFIED`,
`UPDATE_APPLIED_AFTER_APPROVAL`, `UPDATE_FAILED_HONESTLY`.

## Hard rules

| Rule | Refusal |
|---|---|
| Unknown maintenance type | `BLOCKED_AUTHORITY_CONFUSION` |
| Dependency/security w/o `risk_visible` | `BLOCKED_AUTHORITY_CONFUSION` |
| Dependency/security w/o advisory caveat | `BLOCKED_AUTHORITY_CONFUSION` |
| Applied label w/o compatibility verifier | `BLOCKED_MISSING_COMPATIBILITY_VERIFIER` |
| "Updated" label w/o post-apply verifier pass | `BLOCKED_FALSE_UPDATED_LABEL` |
| Applied label w/o approval present | `BLOCKED_AUTHORITY_CONFUSION` |
| Applied label w/o compatibility verifier pass | `BLOCKED_AUTHORITY_CONFUSION` |

`source_mutation_authorized` and `training_eligible` stay False.
