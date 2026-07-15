# React Learning Studio Verified Demo Status Binding

> Locked under
> `locks/sentinel/DETERMINEX_REACT_LEARNING_STUDIO_VERIFIED_DEMO_STATUS_BINDING_LOCK_001.json`.

Binds the live React Learning Studio panel to the Codex Learning
Studio teaching splash demo evidence. Teaching outputs are
**non-authorizing by construction** — even at PASSED, no field
implies source mutation, approval, training, or release.

## Pieces

- **Loader**: `scripts/ide/learning_studio_verified_demo_status.py::load(evidence_dir=None)`
- **Tauri verb**: `get_learning_studio_verified_demo_status` (read-only)
- **React component**: `frontend/src/components/ide-product-shell/LearningStudioVerifiedDemoStatus.tsx`

## Hard rules (loader)

| Condition | Decision |
|---|---|
| Evidence file absent | `AWAITING_EVIDENCE` |
| Evidence corrupt | `AWAITING_EVIDENCE` |
| `status` != `LEARNING_STUDIO_TEACHING_SPLASH_DEMO_PASSED` | `BLOCKED_MALFORMED` |
| `source_mutation_authorized` true (top-level or `authority.*`) | `BLOCKED_AUTHORITY_CONFUSION` |
| `training_eligible` / `training_rows_written` true (top-level or `authority.*`) | `BLOCKED_AUTHORITY_CONFUSION` |
| `approval_authority_granted` true (top-level or `authority.*`) | `BLOCKED_AUTHORITY_CONFUSION` |
| `release_ready` true (top-level or `authority.*`) | `BLOCKED_AUTHORITY_CONFUSION` |
| `authority.real_user_source_mutation_authorized` true | `BLOCKED_AUTHORITY_CONFUSION` |
| `non_authorizing_teaching_only` != true | `BLOCKED_AUTHORITY_CONFUSION` |
| `broad_claims_granted` true (top-level or `authority.*`) | `BLOCKED_BROAD_CLAIM` |
| `verification.learning_success_label.success_label_allowed` true | `BLOCKED_BROAD_CLAIM` |
| Any of `beginner_explanation_written` / `pro_explanation_written` / `failure_explanation_written` / `safe_next_steps_written` / `what_this_does_not_prove_written` / `verifier_grounding_present` != true | `BLOCKED_MALFORMED` |
| `claim_boundary` missing required statements | `BLOCKED_BROAD_CLAIM` |
| Affirmative broad-claim phrase outside `verification.*` / `claim_boundary` / `blocked_path_demo` / `evidence.claim_scanner_result` / `explanations` / `source_evidence_summary` | `BLOCKED_BROAD_CLAIM` |

Required boundary statements:

- `Learning Studio explanation only`
- `non-authorizing teaching only`
- `no source mutation authorized`
- `not all projects`
- `not all languages`
- `not all users`
- `training remains false`
- `release readiness remains false`

## What the React component renders

- Status / decision, target surface ("Learning Studio"), target workflow ("non-authorizing verifier-grounded teaching and explanation"), teaching subject
- Written-flag rows: beginner explanation, professional explanation, failure explanation (verifier-grounded), safe next steps, what-this-does-not-prove
- Verifier grounding present (`data-verifier-grounding={true|false}`)
- Non-authorizing teaching only badge (`data-non-authorizing={true|false}`)
- Authority-bag captions, all false:
  - `source_mutation_authorized: false (remains false)`
  - `approval_authority_granted: false (remains false)`
  - Training badge (`data-training-eligible="false"`, `training_eligible: false`, `training_rows_written: false`)
  - `release_ready: false (remains false)` (`data-release-ready="false"`)
  - `broad_claims_granted: false (remains false)`
- Evidence reference, final teaching report path, evidence manifest path
- Source verified evidence consumed (Repo Clinic + Maintenance Bay PASSED evidence paths, enumerated)
- Explanation text snippets (beginner, professional, what_failed, why_fix_or_update_worked, safe_next_steps, what_this_does_not_prove)
- Claim boundary section (enumerated)
- Blocked path summary section (enumerated refusals: apply_patch_attempt, authorize_source_mutation, false_fixed_claim_without_verifier, false_maintained_claim_without_verifier, false_updated_claim_without_verifier, ready_or_understood_converted_to_authorized, release_readiness_grant, training_eligibility_grant, all_languages_all_projects_all_users_claim)
- Required captions:
  - "Ready does NOT mean authorized."
  - "Learning can explain; it cannot mutate code."
  - "Verified only for this Learning Studio teaching splash path."
  - "Source mutation remains false."
  - "Approval authority remains false."
  - "Training stays false."
  - "Release readiness remains false."
  - "No all-projects, all-languages, all-users, arbitrary-teaching, production-ready, or autonomous-repair claim is granted."
  - "Teaching explanations are grounded in existing verifier evidence, not new authorization."

## What it never renders

`all projects supported`, `any language supported`, `all codebases supported`,
`all users supported`, `production-ready in any repo`,
`training enabled by default`, `release ready: true`,
`real user repo mutation authorized`, `arbitrary production repair`,
`arbitrary teaching`, `autonomous repair`, `no follow-up required`,
`deploy now`, `source_mutation_authorized: true`,
`training_eligible: true`, `approval_authority_granted: true`.

## Upstream source evidence

This binding reads the Codex Learning Studio splash bundle, which
itself summarizes two upstream verifier-backed splash demos:

- `assurance/evidence/repo_clinic_fixture_repair_splash_demo/run_*.REPO_CLINIC_FIXTURE_REPAIR_SPLASH_DEMO_PASSED.json`
- `assurance/evidence/maintenance_bay_dry_run_update_splash_demo/run_*.MAINTENANCE_BAY_DRY_RUN_UPDATE_SPLASH_DEMO_PASSED.json`

Teaching is allowed to explain those records; it is not allowed to
broaden them.
