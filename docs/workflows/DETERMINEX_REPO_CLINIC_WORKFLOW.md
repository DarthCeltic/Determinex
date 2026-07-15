# Repo Clinic Workflow

> Locked under `locks/sentinel/DETERMINEX_REPO_CLINIC_WORKFLOW_LOCK_001.json`.

Existing-codebase workflow for diagnosis, repair, refactor, and
update. Preserves every authority gate from the prior campaigns.

## 17 flow steps

`open_existing_repo`, `workspace_toolchain_scan`,
`language_build_detection`, `health_report`,
`issue_failure_intake`, `verifier_discovery`, `diagnosis`,
`patch_refactor_update_proposal`, `quarantine`, `temp_apply`,
`verifier_run`, `approval_request`,
`source_mutation_after_approval_only`, `post_apply_verifier`,
`rollback_if_failed`, `evidence`, `training_remains_blocked`.

## 13 UI states

`REPO_OPENED`, `REPO_ANALYZED`, `TOOLCHAIN_MISSING`,
`VERIFIER_MISSING`, `ISSUE_DIAGNOSED_UNVERIFIED`,
`PATCH_PROPOSED_QUARANTINED`, `TEMP_VERIFIER_PASSED`,
`APPROVAL_REQUIRED`, `SOURCE_MUTATION_AUTHORIZED`,
`SOURCE_MUTATION_APPLIED`, `POST_APPLY_VERIFIER_PASSED`,
`REPAIR_VERIFIED`, `REPAIR_FAILED_HONESTLY`.

## Hard rules

| Rule | Refusal |
|---|---|
| Verifier missing while mutation attempted or 'fixed' shown | `BLOCKED_VERIFIER_MISSING` |
| Diagnosis treated as source authorization | `BLOCKED_SOURCE_MUTATION_CONFUSION` |
| Local-model admission treated as source authorization | `BLOCKED_SOURCE_MUTATION_CONFUSION` |
| `source_mutation_authorized_by_gate` without temp_verify + approval | `BLOCKED_SOURCE_MUTATION_CONFUSION` |
| 'Fixed' label without post-apply verifier pass | `BLOCKED_FALSE_FIXED_LABEL` |

`source_mutation_authorized` and `training_eligible` stay False
on the record.
