# React Maintenance Bay Verified Demo Status Binding

> Locked under
> `locks/sentinel/DETERMINEX_REACT_MAINTENANCE_BAY_VERIFIED_DEMO_STATUS_BINDING_LOCK_001.json`.

Binds the live React Maintenance Bay panel to the Codex Maintenance
Bay dry-run/update splash demo evidence.

## Pieces

- **Loader**: `scripts/ide/maintenance_bay_verified_demo_status.py::load(evidence_dir=None)`
- **Tauri verb**: `get_maintenance_bay_verified_demo_status` (read-only)
- **React component**: `frontend/src/components/ide-product-shell/MaintenanceBayVerifiedDemoStatus.tsx`

## Hard rules (loader)

| Condition | Decision |
|---|---|
| Evidence file absent | `AWAITING_EVIDENCE` |
| Evidence corrupt | `AWAITING_EVIDENCE` |
| `status` != `MAINTENANCE_BAY_DRY_RUN_UPDATE_SPLASH_DEMO_PASSED` | `BLOCKED_MALFORMED` |
| `source_mutation_authorized` / `training_eligible` / `training_rows_written` true | `BLOCKED_AUTHORITY_CONFUSION` |
| `authority.real_user_source_mutation_authorized` true | `BLOCKED_AUTHORITY_CONFUSION` |
| `authority.approval_authority_granted` true | `BLOCKED_AUTHORITY_CONFUSION` |
| Top-level `real_user_source_mutation_authorized` true | `BLOCKED_AUTHORITY_CONFUSION` |
| `authority.broad_claims_granted` true | `BLOCKED_BROAD_CLAIM` |
| `fixture_mutation_only` != true | `BLOCKED_AUTHORITY_CONFUSION` |
| `compatibility_verified` != true | `BLOCKED_AUTHORITY_CONFUSION` (updated/maintained invariant) |
| `post_change_tests_passed` != true | `BLOCKED_AUTHORITY_CONFUSION` |
| `claim_boundary` missing required statements | `BLOCKED_BROAD_CLAIM` |
| Affirmative broad-claim phrase outside `blocked_path_demo` / `claim_scanner_result` / `claim_boundary` | `BLOCKED_BROAD_CLAIM` |

Required boundary statements:

- `Maintenance Bay Python fixture dry-run demo only`
- `fixture compatibility workspace mutation only`
- `not all projects`
- `not all languages`
- `not arbitrary maintenance`
- `not production-ready maintenance`
- `training remains false`

## What the React component renders

- Status / decision, target surface ("Maintenance Bay"), target workflow, target language
- Fixture workspace, maintenance issue summary, change type (`dry-run test configuration and documentation maintenance`)
- Baseline verifier command + baseline-failed-before-maintenance flag
- Compatibility verifier command + `compatibility_verified` flag
- `post_change_tests_passed` flag
- Fixture-mutation-only badge
- `real_user_source_mutation_authorized: false (remains false)` caption
- `approval_authority_granted: false (remains false)` caption
- Training badge (`data-training-eligible="false"`, `training_eligible: false`, `training_rows_written: false`)
- Affected files, evidence ref, change body hash
- Fixture / compatibility / source-repo workspaces
- `UPDATE_VERIFIED` badge gated on `passed && compatibility_verified && post_change_tests_passed`; otherwise reads `UPDATED_LABEL_DISABLED_NO_VERIFIER_EVIDENCE`
- Blocked-claims summary section listing 6 refusals (false_updated, false_maintained, unsafe_real_repo_mutation, all-projects/all-languages, training-without-positive-gate, release/deploy-readiness)
- Claim boundary section (enumerated)
- Blocked-path summary section (enumerated)
- Required captions:
  - "Ready does NOT mean authorized."
  - "Verified only for this Maintenance Bay fixture dry-run/update path."
  - "Real user repo mutation NOT authorized."
  - "Training stays false."
  - "No all-projects, all-languages, arbitrary-maintenance, production-ready maintenance, or release/deploy claim is granted."

## What it never renders

`all projects supported`, `any language supported`, `all codebases supported`,
`production-ready in any repo`, `training enabled by default`,
`release ready: true`, `real user repo mutation authorized`,
`arbitrary production repair`, `no follow-up required`, `deploy now`.
