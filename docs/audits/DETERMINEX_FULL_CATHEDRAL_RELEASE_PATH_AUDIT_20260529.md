# Determinex Full Cathedral Release Path Audit - 2026-05-29

Status: `FULL_CATHEDRAL_RELEASE_PATH_AUDIT_WRITTEN`

Audit target: proposed `DETERMINEX_FULL_CATHEDRAL_RELEASE_PATH_LOCK_001`

Current HEAD audited: `d06fab296` (`DETERMINEX_REACT_MAINTENANCE_BAY_VERIFIED_DEMO_STATUS_BINDING_LOCK_001`)

Board refresh after Codex Learning Studio run: `DETERMINEX_LEARNING_STUDIO_TEACHING_SPLASH_DEMO_LOCK_001` is included in this evidence update and awaits React binding.

Purpose: give collaborators a current, evidence-grounded view of where the proposed Full Cathedral Release Path fits relative to the locks already completed.

## Executive Verdict

The proposed cathedral document is directionally aligned as the release narrative and roadmap, but it is not current enough to accept as a validated lock.

It should be treated as:

`ROADMAP_DRAFT_REQUIRES_NORMALIZATION_BEFORE_LOCK`

The main correction is sequencing. The draft still says Repo Clinic is the next room and Maintenance Bay is planned. In the current repo state, Repo Clinic and Maintenance Bay splash demos have already passed and are bound into the live React shell. The Learning Studio teaching splash is now the active Codex-room result and still needs a React binding lock before it is considered live-shell accepted.

The correct next rung from current evidence is:

`DETERMINEX_REACT_LEARNING_STUDIO_VERIFIED_DEMO_STATUS_BINDING_LOCK_001`

## Evidence Consulted

Committed locks and evidence:

- `locks/sentinel/DETERMINEX_IDEA_LAB_PYTHON_CLI_VERIFIED_SPLASH_DEMO_LOCK_001.json`
- `locks/sentinel/DETERMINEX_REACT_IDEA_LAB_VERIFIED_DEMO_STATUS_BINDING_LOCK_001.json`
- `locks/sentinel/DETERMINEX_REPO_CLINIC_FIXTURE_REPAIR_SPLASH_DEMO_LOCK_001.json`
- `locks/sentinel/DETERMINEX_REACT_REPO_CLINIC_VERIFIED_DEMO_STATUS_BINDING_LOCK_001.json`
- `locks/sentinel/DETERMINEX_MAINTENANCE_BAY_DRY_RUN_UPDATE_SPLASH_DEMO_LOCK_001.json`
- `locks/sentinel/DETERMINEX_REACT_MAINTENANCE_BAY_VERIFIED_DEMO_STATUS_BINDING_LOCK_001.json`
- `locks/sentinel/DETERMINEX_LEARNING_STUDIO_TEACHING_SPLASH_DEMO_LOCK_001.json`
- `locks/sentinel/DETERMINEX_LIVE_REACT_UNIFIED_PRODUCT_SHELL_FINAL_STATE_LOCK_001.json`
- `locks/sentinel/DETERMINEX_LIVE_REACT_PRODUCT_SHELL_DEMO_READINESS_FINAL_STATE_LOCK_001.json`
- `assurance/evidence/idea_lab_python_cli_verified_splash_demo/run_20260529.IDEA_LAB_PYTHON_CLI_VERIFIED_SPLASH_DEMO_PASSED.json`
- `assurance/evidence/repo_clinic_fixture_repair_splash_demo/run_20260529.REPO_CLINIC_FIXTURE_REPAIR_SPLASH_DEMO_PASSED.json`
- `assurance/evidence/maintenance_bay_dry_run_update_splash_demo/run_20260529.MAINTENANCE_BAY_DRY_RUN_UPDATE_SPLASH_DEMO_PASSED.json`
- `assurance/evidence/learning_studio_teaching_splash_demo/run_20260529.LEARNING_STUDIO_TEACHING_SPLASH_DEMO_PASSED.json`
- `assurance/evidence/evidence_index.json`
- `assurance/evidence/append_only_evidence_ledger/run_20260528.APPEND_ONLY_EVIDENCE_LEDGER_VALIDATED.json`
- `assurance/evidence/evidence_count_drift_guard/run_20260528.EVIDENCE_COUNT_DRIFT_GUARD_PASSED.json`

Maintenance Bay binding is now committed proof at `d06fab296`.

## Current Product State

| Surface | Current evidence state | Live shell binding state | Release meaning |
|---|---|---|---|
| Idea Lab | `IDEA_LAB_PYTHON_CLI_VERIFIED_SPLASH_DEMO_PASSED` | Bound by `DETERMINEX_REACT_IDEA_LAB_VERIFIED_DEMO_STATUS_BINDING_LOCK_001` | First narrow verified room is open. |
| Repo Clinic | `REPO_CLINIC_FIXTURE_REPAIR_SPLASH_DEMO_PASSED` | Bound by `DETERMINEX_REACT_REPO_CLINIC_VERIFIED_DEMO_STATUS_BINDING_LOCK_001` | Second narrow verified room is open. |
| Maintenance Bay | `MAINTENANCE_BAY_DRY_RUN_UPDATE_SPLASH_DEMO_PASSED` | Bound by `DETERMINEX_REACT_MAINTENANCE_BAY_VERIFIED_DEMO_STATUS_BINDING_LOCK_001` | Third narrow verified room is open. |
| Learning Studio | `LEARNING_STUDIO_TEACHING_SPLASH_DEMO_PASSED` | Binding lock missing | Demo proof exists, but the live shell has not yet accepted the verified status. |
| Proof / Operator Center | View-model and panel locks exist | Milestone dashboard lock not found | Control-room foundation exists; release dashboard still pending. |

## Current Evidence Health

Evidence state from current committed records:

| Check | Current result |
|---|---|
| Evidence index entry count | `307` before Learning Studio evidence refresh |
| Append-only ledger chain | `chain_valid: true` |
| Count drift guard | `EVIDENCE_COUNT_DRIFT_GUARD_PASSED` |
| Count drift expected | `307` before Learning Studio evidence refresh |
| Count drift actual | `307` before Learning Studio evidence refresh |
| Training eligibility | `false` on the splash evidence checked |
| Real user source mutation | `false` on Repo Clinic and Maintenance Bay evidence |
| Broad claims | blocked by the splash evidence checked |

Workspace caveat:

The workspace is not clean. There are unrelated ProgramBench/operator/audit edits and untracked audit inbox files. This audit did not revert or stage those files.

## Where The Proposed Cathedral Text Is Correct

The following parts align with the existing product doctrine and current proof model:

- Five surfaces are the correct release-facing product skin: Idea Lab, Repo Clinic, Maintenance Bay, Learning Studio, Proof / Operator Center.
- The release should remain evidence-scoped.
- `source_mutation_authorized: false`, `training_eligible: false`, `approval_authority_granted: false`, `broad_claims_granted: false`, and `release_ready: false` are still the correct global authority posture.
- Columbia House Tracker is a strong north-star demo concept because it is local, funny, low-stakes, explainable, and naturally exercises all five surfaces.
- The release gates are directionally right: all five surfaces need verified/bound demos before public release claims widen.
- The "nothing is called working without proof" doctrine matches the active no-success-without-verifier policy.

## Where The Proposed Cathedral Text Is Stale

These entries should be updated before the lock is accepted:

| Draft statement | Current correction |
|---|---|
| Repo Clinic status: `DEMO_READY_TO_RUN` | Repo Clinic fixture repair demo has passed and is bound into the live shell. |
| Maintenance Bay status: `PLANNED` | Maintenance Bay dry-run update splash demo has passed and is bound into the live shell. |
| Learning Studio status: `PLANNED` | Learning Studio teaching splash demo has passed locally and needs React binding. |
| Workflow row: broken repo demo locked until Repo Clinic demo | Repo Clinic demo is no longer locked; it passed. |
| Workflow row: maintenance demo locked until Maintenance demo | Maintenance demo evidence and binding now exist. |
| Next recommended rung: `DETERMINEX_REPO_CLINIC_FIXTURE_REPAIR_SPLASH_DEMO_LOCK_001` | This is stale. Correct next rung is `DETERMINEX_REACT_LEARNING_STUDIO_VERIFIED_DEMO_STATUS_BINDING_LOCK_001`. |
| Phase 1 Step 1: Repo Clinic demo still pending | Complete. |
| Phase 1 Step 2: Maintenance Bay demo still pending | Complete and bound. |
| Phase 1 Step 3: Learning Studio demo still pending | Codex demo complete; React binding pending. |

## Where The Proposed Cathedral Text Overclaims Or Needs Caveats

These phrases are useful as internal vision, but unsafe as public product claims until the claim ledger classifies them and evidence supports them:

| Phrase or claim | Audit classification | Required correction |
|---|---|---|
| "hardware-agnostic software factory" | `SAFE_WITH_CAVEATS` at best | Use "local-first with documented hardware and toolchain caveats." |
| "gives any individual the same software agency previously only available to well-funded engineering teams" | `ROADMAP_OR_MARKETING_WITH_CAVEATS` | Keep as mission language, not verified capability. |
| "If a domain has a deterministic verifier, Determinex can learn to generate correct outputs" | `ROADMAP_THEOREM_NOT_CURRENT_PRODUCT_CLAIM` | Say this is the architecture thesis; each domain still needs a verifier, support matrix, evidence, and gate. |
| "There is no ceiling" | `NOT_A_VERIFIABLE_CLAIM` | Keep only as internal rally language or label as vision. |
| "Columbia House demo is verified smoke-tested" | `FORBIDDEN_UNTIL_STEP_5_RUNS` | The demo is not built yet. |
| Community/club tracker: `YES - Columbia House demo` | `ROADMAP` | Mark pending until Columbia House lock passes. |
| IOU/debt/ledger tracker: `YES - Columbia House demo` | `ROADMAP` | Mark pending until Columbia House lock passes. |
| "Free for local operation" | `SAFE_WITH_CAVEATS` only | Must disclose hardware, model storage, toolchains, dependency install, hosting, domains, app store, payment, and cloud API costs. |
| "Runs on consumer hardware" | `SAFE_WITH_CAVEATS` | Needs minimum hardware and slow CPU-only caveat. |
| "all programming languages" | `ROADMAP`, not implemented | Must stay locked behind matrix proof. |
| "production-ready enterprise deployment" | `FORBIDDEN` | Do not include as current capability. |

## Corrected Phase 1 Sequence

The release path should be normalized to this current sequence:

1. `DETERMINEX_IDEA_LAB_PYTHON_CLI_VERIFIED_SPLASH_DEMO_LOCK_001`
   - Status: complete.
   - React binding: complete.

2. `DETERMINEX_REPO_CLINIC_FIXTURE_REPAIR_SPLASH_DEMO_LOCK_001`
   - Status: complete.
   - React binding: complete.

3. `DETERMINEX_MAINTENANCE_BAY_DRY_RUN_UPDATE_SPLASH_DEMO_LOCK_001`
   - Status: complete.
   - React binding: complete.

4. `DETERMINEX_REACT_MAINTENANCE_BAY_VERIFIED_DEMO_STATUS_BINDING_LOCK_001`
   - Status: complete.
   - Purpose: bind Maintenance Bay verified dry-run evidence into the live React shell.

5. `DETERMINEX_LEARNING_STUDIO_TEACHING_SPLASH_DEMO_LOCK_001`
   - Status: complete locally.
   - Purpose: use failure/repair material as a non-authorizing teaching demo.

6. `DETERMINEX_REACT_LEARNING_STUDIO_VERIFIED_DEMO_STATUS_BINDING_LOCK_001`
   - Status: current next rung.
   - Purpose: bind Learning Studio verified teaching evidence into the live React shell.

7. `DETERMINEX_PROOF_OPERATOR_CENTER_DASHBOARD_LOCK_001`
   - Status: pending.
   - Purpose: show verified, failed, blocked, claim-safe, and authority status in the control room.

8. `DETERMINEX_COLUMBIA_HOUSE_TRACKER_NORTH_STAR_DEMO_LOCK_001`
   - Status: pending.
   - Purpose: canonical public-facing north-star demo.
   - Claim boundary: proves the scoped workflow, not universal app support.

9. `DETERMINEX_CATHEDRAL_INDEX_FOUNDATION_LOCK_001`
   - Status: pending.
   - Purpose: machine-readable cathedral matrices and public claim ledger.

## Columbia House Tracker Readiness

The Columbia House Tracker concept is suitable, but it is not ready to be described as verified.

Recommended preconditions before building it:

- Maintenance Bay evidence is bound into React.
- Learning Studio teaching demo is bound into React.
- Proof / Operator Center dashboard exists and can show evidence boundaries.
- Cathedral claim ledger has a row for the Columbia House demo.
- Public copy says "verified for this local demo path only."
- Any real historical facts used in app content are source-attributed and frozen into fixture data.

Recommended demo structure:

- Idea Lab: generate local app spec from the group story.
- Repo Clinic: repair a broken obligation calculation in a fixture version.
- Maintenance Bay: dry-run update to timeline/report fields.
- Learning Studio: explain the obligation/debt calculation in beginner and pro versions.
- Proof / Operator Center: show test, smoke, claim boundary, blocked broad claims, and release status.

## Release Gate Audit

| Gate | Current state |
|---|---|
| Repo Clinic fixture repair demo | Complete and bound. |
| Maintenance Bay dry-run/update demo | Complete and bound. |
| Learning Studio teaching/non-authorizing demo | Complete locally; React binding pending. |
| Proof / Operator Center milestone dashboard | Pending. |
| Cathedral Index machine-readable matrices | Pending. |
| Public claim ledger | Pending. |
| Public release repo scrub | Pending. |
| Fresh clone install/demo workflow | Pending. |
| Cost/setup disclosure active | Existing policy active; public release integration still pending. |
| No-success-without-verifier policy | Existing policy active. |
| Broad claims blocked | Active in current splash evidence; public claim ledger still pending. |
| Training remains false | Active. |
| Release ready false | Active. |
| Columbia House Tracker verified | Pending. |

## Collaborator Handoff

For Claude/frontend collaborator:

Current next task:

`DETERMINEX_REACT_LEARNING_STUDIO_VERIFIED_DEMO_STATUS_BINDING_LOCK_001`

Read-only evidence to bind:

`assurance/evidence/learning_studio_teaching_splash_demo/run_20260529.LEARNING_STUDIO_TEACHING_SPLASH_DEMO_PASSED.json`

Required binding behavior:

- Show Learning Studio demo status as non-authorizing verifier-grounded teaching evidence.
- Do not say Learning Studio fixed, updated, maintained, applied, or authorized anything.
- Do not say arbitrary teaching works for all users, all projects, or all languages.
- Keep `source_mutation_authorized: false`.
- Keep `training_eligible: false`.
- Keep `approval_authority_granted: false`.
- Keep `release_ready: false`.
- Show blocked paths for patch application, source mutation authorization, false fixed/updated/maintained claims, all-projects/all-languages/all-users claim, release readiness, training eligibility, and ready/understood converted into authorized.

Do not count any Learning Studio React binding work as complete until it is tested, locked, and committed by the collaborator.

## Recommended Rewrite Status For The Proposed Lock

The proposed `DETERMINEX_FULL_CATHEDRAL_RELEASE_PATH_LOCK_001` should not be marked `FULL_CATHEDRAL_RELEASE_ROADMAP_VALIDATED` yet.

Recommended status:

`FULL_CATHEDRAL_RELEASE_ROADMAP_WRITTEN_REQUIRES_EVIDENCE_NORMALIZATION`

Validation blockers:

- Surface table is stale.
- Workflow table is stale.
- App-class table marks Columbia House-derived app classes as verified before the Columbia House demo exists.
- Several public claims need claim-ledger classification before publication.
- Cathedral Index machine-readable records do not exist yet.
- Public claim scanner for every public sentence has not been run against this cathedral text.
- Learning Studio React binding lock is missing.
- Proof dashboard, Columbia House, release scrub, install/demo, and public claim ledger remain pending.

## What This Audit Did Not Do

- Did not edit Claude frontend implementation.
- Did not create the cathedral lock.
- Did not build the Columbia House Tracker.
- Did not run Docker.
- Did not run ProgramBench.
- Did not import artifacts.
- Did not mutate a real user source repo.
- Did not approve operator packets.
- Did not call network models.
- Did not write training rows.
- Did not create a release or deploy workflow.
- Did not grant broad all-app, all-language, all-codebase, or production-ready claims.

## Final Recommendation

Use the cathedral text as the north-star narrative, but route it through evidence normalization before making it a lock.

Next recommended rung:

`DETERMINEX_REACT_LEARNING_STUDIO_VERIFIED_DEMO_STATUS_BINDING_LOCK_001`
