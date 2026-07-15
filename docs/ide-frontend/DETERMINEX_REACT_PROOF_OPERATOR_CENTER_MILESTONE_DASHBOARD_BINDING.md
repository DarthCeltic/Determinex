# React Proof / Operator Center Milestone Dashboard Binding

> Locked under
> `locks/sentinel/DETERMINEX_REACT_PROOF_OPERATOR_CENTER_MILESTONE_DASHBOARD_BINDING_LOCK_001.json`.

Binds the live React Proof / Operator Center panel to the Codex
Proof / Operator Center milestone dashboard evidence. The dashboard
**DISPLAYS** authority; it does **NOT GRANT** authority. Visibility
is not authorization.

## Pieces

- **Loader**: `scripts/ide/proof_operator_center_milestone_dashboard_status.py::load(evidence_dir=None)`
- **Tauri verb**: `get_proof_operator_center_milestone_dashboard_status` (read-only)
- **React component**: `frontend/src/components/ide-product-shell/ProofOperatorCenterMilestoneDashboard.tsx`

## Hard rules (loader)

| Condition | Decision |
|---|---|
| Evidence file absent | `AWAITING_EVIDENCE` |
| Evidence corrupt | `AWAITING_EVIDENCE` |
| `status` != `PROOF_OPERATOR_CENTER_MILESTONE_DASHBOARD_PASSED` | `BLOCKED_MALFORMED` |
| Any of `source_mutation_authorized` / `training_eligible` / `training_rows_written` / `approval_authority_granted` / `release_ready` / `proof_execution_authority_granted` / `release_deploy_workflow_created` / `artifact_import_authorized` / `benchmark_execution_authorized` / `programbench_execution_authorized` True (top-level or under `authority_status`) | `BLOCKED_AUTHORITY_CONFUSION` |
| `broad_claims_granted` True (top-level or under `authority_status`) | `BLOCKED_BROAD_CLAIM` |
| `release_gate_status.release_ready` True | `BLOCKED_AUTHORITY_CONFUSION` |
| `release_gate_status.columbia_house_tracker` not in `{pending, pending_not_built}` | `BLOCKED_BROAD_CLAIM` |
| `scale_to_100_status.normalized_as_current_ct_lock` True | `BLOCKED_BROAD_CLAIM` |
| `surface_statuses` missing any of Idea Lab / Repo Clinic / Maintenance Bay / Learning Studio / Proof / Operator Center | `BLOCKED_MALFORMED` |
| Proof / Operator Center pre-declares `react_bound: True` inside dashboard evidence | `BLOCKED_MALFORMED` |
| `evidence_health.count_drift_status` != `EVIDENCE_COUNT_DRIFT_GUARD_PASSED` | `BLOCKED_MALFORMED` |
| `evidence_health.append_only_ledger_chain_valid` != True | `BLOCKED_MALFORMED` |
| `evidence_health.evidence_index_valid` != True | `BLOCKED_MALFORMED` |
| `claim_boundary` missing required statements | `BLOCKED_BROAD_CLAIM` |
| Affirmative broad-claim phrase outside `blocked_path_demo` / `claim_boundary` / `claim_boundary_status` / `surface_statuses` / `source_evidence_paths` / `source_audit_paths` | `BLOCKED_BROAD_CLAIM` |

Required boundary statements:

- `Proof / Operator Center milestone dashboard only`
- `evidence dashboard is read-only`
- `not release ready`
- `source mutation remains false`
- `approval authority remains false`
- `proof execution authority remains false`
- `training remains false`
- `not all apps`
- `not all languages`
- `not all platforms`
- `Scale-to-100 remains roadmap draft, not current C&T lock`
- `Columbia House Tracker remains pending`

## What the React component renders

**Five rooms**

A row per surface (Idea Lab, Repo Clinic, Maintenance Bay, Learning
Studio, Proof / Operator Center) with verified / react_bound flags,
binding status token, and per-surface claim.

**Authority status (all false)**

- `source_mutation_authorized: false (remains false)`
- `approval_authority_granted: false (remains false)`
- `proof_execution_authority_granted: false (remains false)`
- Training badge: `training_eligible: false (remains false); training_rows_written: 0 / false`
- `release_ready: false (remains false)` (`data-release-ready="false"`)
- `broad_claims_granted: false (remains false)`

**Release gate status**

- Cathedral Index: `pending`
- Columbia House Tracker: `pending_not_built` (not built)
- Public claims ledger: `pending`
- Release repo scrub: `pending`
- Fresh install / demo workflow: `pending`
- Windows-first support matrix: `pending`

**Scale-to-100 (roadmap / audit input only — NOT current C&T lock)**

- Claim truth status
- Normalized as current C&T lock: `false (remains false — roadmap draft only)`
- Windows-first matrix lock, corpus / training reconciliation lock,
  platform / language / app-class expansion queue, legacy / enterprise,
  audit doc path

**Evidence health**

- Evidence index count (310) / declared / valid
- Append-only ledger status / chain valid / entry count
- Count drift guard status / expected / actual
- JSON parse status
- Evidence ref, dashboard report path, machine-readable dashboard path

**Lists**

- Claim boundary (enumerated)
- Forbidden claims (enumerated, refused by dashboard)
- Blocked path summary (10 scenarios)
- Roadmap items (enumerated, NOT validated — audit input only)

**Next rung**

`current_next_rung` (evidence-governed) + note that after this
binding, Codex reconciliation runs if drift appears; then Cathedral
Index / Scale-to-100 normalization / Columbia House ordering must
be governed by evidence, not hype.

**Required captions (verbatim in footer)**

- "Ready does NOT mean authorized."
- "Verified rooms do NOT mean universal support."
- "Proof Center displays authority; it does not grant authority."
- "Release ready remains false."
- "Training remains false."
- "Source mutation remains false."
- "Scale-to-100 is roadmap/audit input, not current C&T lock."
- "Columbia House is pending, not built."
- "Full Cathedral roadmap is not validated by this binding."

## What it never renders

`all apps supported`, `any language supported`, `all platforms
supported`, `all codebases supported`, `production-ready arbitrary`,
`arbitrary app generation`, `fully autonomous maintenance`,
`release_ready: true`, `training_eligible: true`,
`approval_authority_granted: true`,
`proof_execution_authority_granted: true`,
`broad_claims_granted: true`, `Columbia House Tracker built`,
`Columbia House Tracker verified`, `Scale-to-100 lock active`,
`Scale-to-100 is the current C&T lock`,
`Full Cathedral roadmap validated`,
`verified room means universal support`.

## Upstream source evidence

The Codex Proof / Operator Center milestone dashboard bundle summarizes
the four already-bound room demos plus dashboard evidence health
fields:

- `assurance/evidence/idea_lab_python_cli_verified_splash_demo/run_*.IDEA_LAB_PYTHON_CLI_VERIFIED_SPLASH_DEMO_PASSED.json`
- `assurance/evidence/determinex_react_idea_lab_verified_demo_status_binding/run_*.json`
- `assurance/evidence/repo_clinic_fixture_repair_splash_demo/run_*.REPO_CLINIC_FIXTURE_REPAIR_SPLASH_DEMO_PASSED.json`
- `assurance/evidence/determinex_react_repo_clinic_verified_demo_status_binding/run_*.json`
- `assurance/evidence/maintenance_bay_dry_run_update_splash_demo/run_*.MAINTENANCE_BAY_DRY_RUN_UPDATE_SPLASH_DEMO_PASSED.json`
- `assurance/evidence/determinex_react_maintenance_bay_verified_demo_status_binding/run_*.json`
- `assurance/evidence/learning_studio_teaching_splash_demo/run_*.LEARNING_STUDIO_TEACHING_SPLASH_DEMO_PASSED.json`
- `assurance/evidence/determinex_react_learning_studio_verified_demo_status_binding/run_*.json`
- `assurance/evidence/append_only_evidence_ledger/run_*.APPEND_ONLY_EVIDENCE_LEDGER_VALIDATED.json`
- `assurance/evidence/evidence_count_drift_guard/run_*.EVIDENCE_COUNT_DRIFT_GUARD_PASSED.json`

This binding does not widen them; it shows them, refuses tampering,
and forbids visibility from converting into authority.
