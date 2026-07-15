# React Repo Clinic Verified Demo Status Binding

> Locked under
> `locks/sentinel/DETERMINEX_REACT_REPO_CLINIC_VERIFIED_DEMO_STATUS_BINDING_LOCK_001.json`.

Binds the live React Repo Clinic panel to the Codex Repo Clinic
fixture-repair splash demo evidence.

## Pieces

- **Loader**: `scripts/ide/repo_clinic_verified_demo_status.py::load(evidence_dir=None)`
- **Tauri verb**: `get_repo_clinic_verified_demo_status` (read-only)
- **React component**: `frontend/src/components/ide-product-shell/RepoClinicVerifiedDemoStatus.tsx`

## Hard rules (loader)

| Condition | Decision |
|---|---|
| Evidence file absent | `AWAITING_EVIDENCE` |
| Evidence corrupt | `AWAITING_EVIDENCE` |
| `status` != `REPO_CLINIC_FIXTURE_REPAIR_SPLASH_DEMO_PASSED` | `BLOCKED_MALFORMED` |
| `source_mutation_authorized: true` in evidence | `BLOCKED_AUTHORITY_CONFUSION` |
| `training_eligible: true` in evidence | `BLOCKED_AUTHORITY_CONFUSION` |
| `authority.real_user_source_mutation_authorized: true` | `BLOCKED_AUTHORITY_CONFUSION` |
| Top-level `real_user_source_mutation_authorized: true` | `BLOCKED_AUTHORITY_CONFUSION` |
| `authority.approval_authority_granted: true` | `BLOCKED_AUTHORITY_CONFUSION` |
| `authority.broad_claims_granted: true` | `BLOCKED_BROAD_CLAIM` |
| `fixture_mutation_only` != `true` | `BLOCKED_AUTHORITY_CONFUSION` |
| `claim_boundary` missing required statements | `BLOCKED_BROAD_CLAIM` |
| Affirmative broad-claim phrase outside `blocked_path_demo` / `claim_scanner_result` / `claim_boundary` | `BLOCKED_BROAD_CLAIM` |
| `verification.repair_verified: true` without `baseline_failed` + `repair_tests_passed` + `false_fixed_claim_blocked` | `BLOCKED_AUTHORITY_CONFUSION` |

Required boundary statements:

- `Repo Clinic Python fixture repair demo only`
- `fixture/demo workspace mutation only`
- `not all codebases`
- `not all languages`
- `not arbitrary repair`
- `training remains false`

## What the React component renders

- Demo title, target workflow, target language (Python)
- Issue summary, baseline-failure-captured, repair-verifier-passed
- Repair-verified ONLY for this fixture demo path
- False-fixed-claim-blocked
- Fixture-mutation-only badge
- Affected files (enumerated)
- Evidence reference, patch body hash, fixture workspace
- Claim boundary (enumerated)
- Blocked-path summary (enumerated)
- Training-false badge (`data-training-eligible="false"`)
- Source-mutation-false caption
- "Ready does NOT mean authorized." caption
- "Verified only for this fixture demo path — not all codebases, not all languages, not arbitrary repair, not production-ready arbitrary repair." caption
- "Real user repo mutation NOT authorized." caption
- "Training stays false (training_eligible: false)." caption

## What it never renders

`all codebases`, `all languages`, `any language`, `arbitrary repair`,
`arbitrary production repair`, `production-ready arbitrary`,
`real user repo mutation authorized`, `training enabled`,
`source_mutation_authorized: true`, `release_ready: true`,
`no-followup support`.
