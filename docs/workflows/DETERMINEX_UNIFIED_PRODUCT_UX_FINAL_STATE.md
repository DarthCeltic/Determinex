# Determinex Unified Product UX — Final State

> Locked under `locks/sentinel/DETERMINEX_UNIFIED_PRODUCT_UX_FINAL_STATE_LOCK_001.json`.

Finale of `DETERMINEX_UNIFIED_PRODUCT_UX_SHELL_SERIES`.

`scripts/repair/unified_product_ux_final_state.evaluate(repo_root)`
reads the eight prior rungs' lock manifests on disk and produces
the campaign's terminal state record.

## Eight UX-shell dimensions

| Dimension | Lock |
|---|---|
| Navigation model | `DETERMINEX_UNIFIED_PRODUCT_NAVIGATION_MODEL_LOCK_001` |
| Idea Lab workflow | `DETERMINEX_IDEA_LAB_WORKFLOW_LOCK_001` |
| Repo Clinic workflow | `DETERMINEX_REPO_CLINIC_WORKFLOW_LOCK_001` |
| Maintenance Bay workflow | `DETERMINEX_MAINTENANCE_BAY_WORKFLOW_LOCK_001` |
| Learning Studio workflow | `DETERMINEX_LEARNING_STUDIO_WORKFLOW_LOCK_001` |
| Proof / Operator Center view-model | `DETERMINEX_PROOF_OPERATOR_CENTER_VIEWMODEL_LOCK_001` |
| User levels & teaching windows | `DETERMINEX_UNIFIED_USER_LEVELS_AND_TEACHING_WINDOWS_LOCK_001` |
| Splash demo spec | `DETERMINEX_UNIFIED_PRODUCT_SPLASH_DEMO_SPEC_LOCK_001` |

## Aggregate invariants

- `source_mutation_authorized: false`
- `training_eligible: false`
- `release_ready: false` (public-release scrub/install/demo workflow is a future rung)
- `demo_ready_as_spec: true`
- `unified_ux_shell_ready_as_model: true`
- `real_react_mount_pending: true`
- `unsupported_claims_blocked: true` — no `all_apps_claim`, `all_languages_claim`, `all_codebases_claim`, `no_followup_claim`, `production_ready_arbitrary_apps_claim`, or `training_enabled_in_demo` key is set True anywhere

## Next recommended rung

`live_react_mount_for_unified_product_shell`.
