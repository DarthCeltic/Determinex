# DETERMINEX 100% Completion Release/Public Launch Prep Wave 001 - Dirty State Triage

**Marker:** `DIRTY_STATE_TRIAGE`
**Author:** Codex executor
**Timestamp UTC:** `2026-06-02T21:58:01Z`
**Branch:** `clean-main`
**Observed HEAD:** `5b0014cd8`
**Observed origin/clean-main:** `ddfcac285`

## Verdict

The dirty state is intentional Lane A/C recovery work, not an accidental verifier weakening.

The 39 tracked modifications reconcile already-committed current release registry truth (`13` exact release-supported cells, `0` release-supported families) with historical proof/status records that were produced when the current canonical count was `10`.

This triage does not claim release readiness, beta readiness, public distribution readiness, family support, clean-host proof, signed/trusted distribution, Proof Center installed-app smoke, or full `tests/status` completion.

## Dirty Set Classification

- `assurance/evidence/release_cell_mutation_proof_center_full_status_distribution_preflight_wave_001/release_cell_registry_mutation_signoff_20260602.json`
- `assurance/evidence/release_cell_mutation_proof_center_full_status_distribution_preflight_wave_001/wave_state_summary_20260602.json`

These two JSON files are timestamp-only regenerations. The readiness headline and blockers remain unchanged:

- `RELEASE_SUPPORTED_CELLS_ADVANCED_PUBLIC_DISTRIBUTION_BLOCKERS_REMAIN`
- internal release-candidate ready remains `false`
- public release-ready remains `false`
- Proof Center installed-app result remains `BLOCKED_EXACT`
- public distribution remains `NO_GO_PUBLIC_DISTRIBUTION`
- release-supported cells remain `10 -> 13`
- release-supported families remain `0 -> 0`

The remaining modified files fall into three proof/test buckets:

1. Historical Claude-common review payload finalizers now accept historical release-cell counts bounded by the current registry count (`release_supported_cells <= CANONICAL_CELLS`) while keeping families exact (`release_supported_families == CANONICAL_FAMILIES`).
2. Historical Wave 018/019 assertion helpers preserve exact historical record pins (`record["release_supported_cells"] == 10`) and add exact current registry pins (`canonical_release_cell_count() == 13`).
3. Current release-wave logic keeps current registry truth exact by validating against `canonical_release_cell_count()` and by deriving install-packaging cell counts from the registry mix.

## Current vs Historical Boundary

Current authority is still the registry:

- `scripts/proof/release_cell_registry.py`
- `canonical_release_cell_count() == 13`
- `canonical_release_supported_families() == 0`

Historical proof payloads that record `10` cells are not rewritten to pretend they were generated after the 13-cell promotion. They are tolerated only as bounded non-source historical evidence. The tests and assertion helpers keep a separate exact pin for those records:

- historical record count: `10`
- current canonical count: `13`
- families: strict `0`

This closes the undercount concern for the migrated Wave 018/019 helpers: the bounded comparison is paired with explicit historical `10` and explicit current `13` assertions. Current registry/conveyor tests still reject drift and family inference.

## Guardrails Checked Before Test Execution

- No `tests/status/conftest.py` modification is present in the dirty set.
- No package manifest, lockfile, training corpus, model artifact, or release distribution artifact is modified in this dirty set.
- No source mutation authority, training eligibility, public upload, release readiness, beta readiness, universal support, broad family support, signing/trust, clean-host install proof, or Proof Center installed-app proof is granted by this triage.

## Verification Plan

Codex will run the focused proof/status tests that touch the dirty files, then the standard evidence/guard validators:

- focused dirty-slice status tests
- `scripts/status/anti_god_script_rule_check.py --check`
- `scripts/evidence_index.py --check`
- `scripts/determinex_cli.py evidence validate`
- release registry direct validation

Full `tests/status` completion remains outside this triage unless it is explicitly run and completed; this marker does not claim it.

## Verification Results

Passed.

- Focused dirty-slice status tests:
  - Command: `.\\.venv\\Scripts\\python.exe -m pytest tests/status/test_installer_install_launch_uninstall_release_signoff_wave_001.py tests/status/test_overnight_7_hour_autonomous_sprint.py tests/status/test_wave_016_canonical_promotion_and_hard_floor.py tests/status/test_wave_018_canonical_backfill_and_first_family.py tests/status/test_wave_019_execution_floor_and_family_expansion.py tests/status/test_wave_020c_contract_execution.py tests/status/test_wave_021_program_authority.py tests/status/test_release_cell_mutation_proof_center_full_status_distribution_preflight_wave_001.py -q --tb=short`
  - Result: `97 passed in 10.80s`
- Anti-god guard:
  - Command: `.\\.venv\\Scripts\\python.exe scripts/status/anti_god_script_rule_check.py --check`
  - Result: `ANTI_GOD_SCRIPT_RULE_CHECK_PASSED`
- Evidence index:
  - Command: `.\\.venv\\Scripts\\python.exe scripts/evidence_index.py --check`
  - Result: `validation_errors: []`
- Determinex evidence validation:
  - Command: `.\\.venv\\Scripts\\python.exe scripts/determinex_cli.py evidence validate`
  - Result: `Evidence index: 1882 entries; All referenced files present`
- Release registry direct validation:
  - Command: `.\\.venv\\Scripts\\python.exe -c "from scripts.proof.release_cell_registry import canonical_release_cell_count, canonical_release_supported_families, validate_canonical_registry; result=validate_canonical_registry(); print({'cells': canonical_release_cell_count(), 'families': canonical_release_supported_families(), 'passed': result['passed'], 'errors': result['errors']})"`
  - Result: `{'cells': 13, 'families': 0, 'passed': True, 'errors': []}`
- Stale release-supported invariant regression sweep:
  - Command: `.\\.venv\\Scripts\\python.exe -m pytest tests/status -q --tb=short -k "release_supported_invariant_bound_to_registry"`
  - Result: `76 passed, 11335 deselected in 10.26s`
- Append-only evidence ledger:
  - Command: `.\\.venv\\Scripts\\python.exe scripts/proof/append_only_evidence_ledger.py --json --no-write`
  - Result: `chain_valid: true`
- Evidence count drift guard:
  - Command: `.\\.venv\\Scripts\\python.exe scripts/proof/evidence_count_drift_guard.py --json --no-write`
  - Result: `EVIDENCE_COUNT_DRIFT_GUARD_PASSED`, `validation_errors: []`, `actual_evidence_count: 1882`, `expected_evidence_count: 1882`
- Day-one public claim scanner:
  - Command: `.\\.venv\\Scripts\\python.exe scripts/claim_scanner/day_one_public_claim_scanner.py --print`
  - Result: `DAY_ONE_PUBLIC_CLAIM_SCANNER_PASSED`, `current_repo_violation_count: 0`

## Signoff Lock Status

The release registry mutation signoff lock is present and tracked:

- `locks/sentinel/DETERMINEX_RELEASE_REGISTRY_MUTATION_SIGNOFF_LOCK_001.json`

It was not modified by this triage. The active dirty evidence JSON changes remain timestamp-only regenerations.

## Explicit Non-Claims

Full `tests/status` was not run to completion in this triage. The previous full-status runtime blocker remains a runtime/completion issue, not a claimed pass.

This triage does not grant:

- release readiness
- beta readiness
- public distribution readiness
- family support
- clean-host proof
- signing/trust proof
- Proof Center installed-app smoke
- training eligibility
- source mutation authority
