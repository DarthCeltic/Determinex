# Determinex Evidence Index

> Machine-generated from `locks/sentinel/` and `locks/drain/` manifests.
> Regenerate with: `python scripts/evidence_index.py --md docs/EVIDENCE_INDEX.md`

**1889 entries** | Schema: `determinex-evidence-index-v1`

## Sentinel Locks

| Lock | Tests | Full Suite | Commit | Reproduction |
|------|------:|----------:|--------|-------------|
| [ACTION_GOVERNOR_LOCK_001](../locks/sentinel/ACTION_GOVERNOR_LOCK_001.json) | 28 | 862 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/agents/test_action_safety_g…` |
| [AIDER_POLYGLOT_TRACE_HARNESS_LOCK_001](../locks/sentinel/AIDER_POLYGLOT_TRACE_HARNESS_LOCK_001.json) | 8 | 772 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/test_aider_polyglot_trace_h…` |
| [APPLY_GATE_FIXTURE_REFUSAL_LOCK_001](../locks/sentinel/APPLY_GATE_FIXTURE_REFUSAL_LOCK_001.json) | 18 | 18 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_source_mutation…` |
| [APPROVAL_SIGNATURE_CRYPTOGRAPHIC_BINDING_LOCK_001](../locks/sentinel/APPROVAL_SIGNATURE_CRYPTOGRAPHIC_BINDING_LOCK_001.json) | 11 | 11 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_local_signing_lock…` |
| [ARBITRARY_REPO_READINESS_MATRIX_LOCK_001](../locks/sentinel/ARBITRARY_REPO_READINESS_MATRIX_LOCK_001.json) | 13 | 13 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/intake/test_arbitrary_repo_…` |
| [ARCH_GAUNTLET_CI_LOCK_001](../locks/sentinel/ARCH_GAUNTLET_CI_LOCK_001.json) | 35 | 35 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/dev/test_arch_gauntlet_ci_l…` |
| [BENCH_TO_CORPUS_ELIGIBILITY_LOCK_001](../locks/sentinel/BENCH_TO_CORPUS_ELIGIBILITY_LOCK_001.json) | 10 | 750 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/test_bench_to_corpus…` |
| [BROWSER_AGENT_LOCK_001](../locks/sentinel/BROWSER_AGENT_LOCK_001.json) | 18 | 704 | `0a3d1150e9` | `.\.venv\Scripts\python.exe -m pytest tests/locks/test_browser_agent_lo…` |
| [BUILD_ADAPTER_BACKED_VERIFIER_SELECTION_LOCK_001](../locks/sentinel/BUILD_ADAPTER_BACKED_VERIFIER_SELECTION_LOCK_001.json) | 12 | 12 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_build_adapter_b…` |
| [BUILD_ADAPTER_REGISTRY_LOCK_001](../locks/sentinel/BUILD_ADAPTER_REGISTRY_LOCK_001.json) | 36 | 36 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/intake/test_build_adapter_r…` |
| [CANONICAL_LOCAL_MODEL_ID_SELECTION_LOCK_001](../locks/sentinel/CANONICAL_LOCAL_MODEL_ID_SELECTION_LOCK_001.json) | 16 | 16 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/models/test_canonical_local…` |
| [DETERMINEX_40_FAMILY_EVIDENCE_FOOTHOLD_EXPANSION_LOCK_001](../locks/sentinel/DETERMINEX_40_FAMILY_EVIDENCE_FOOTHOLD_EXPANSION_LOCK_001.json) | 13 | 13 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_forty_family_ev…` |
| [DETERMINEX_44_FAMILY_EXACT_CELL_EXPANSION_PRESSURE_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_44_FAMILY_EXACT_CELL_EXPANSION_PRESSURE_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_forty_four_fami…` |
| [DETERMINEX_ACRTDSK_CLAUDE_APPEND_ONLY_COUNT_DRIFT_ANTI_GOD_REVIEW_001](../locks/sentinel/DETERMINEX_ACRTDSK_CLAUDE_APPEND_ONLY_COUNT_DRIFT_ANTI_GOD_REVIEW_001.json) | 1 | 1 | `2d5325decd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_acrtdsk_claude_…` |
| [DETERMINEX_ACRTDSK_CLAUDE_BROADER_REPO_SBOM_PACKET_READY_REVIEW_001](../locks/sentinel/DETERMINEX_ACRTDSK_CLAUDE_BROADER_REPO_SBOM_PACKET_READY_REVIEW_001.json) | 1 | 1 | `2d5325decd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_acrtdsk_claude_…` |
| [DETERMINEX_ACRTDSK_CLAUDE_CLAIM_SCANNER_DAY1_OVERCLAIM_REVIEW_001](../locks/sentinel/DETERMINEX_ACRTDSK_CLAUDE_CLAIM_SCANNER_DAY1_OVERCLAIM_REVIEW_001.json) | 1 | 1 | `2d5325decd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_acrtdsk_claude_…` |
| [DETERMINEX_ACRTDSK_CLAUDE_CLEAN_RUNNER_BLOCKER_HONESTLY_SHARPENED_REVIEW_001](../locks/sentinel/DETERMINEX_ACRTDSK_CLAUDE_CLEAN_RUNNER_BLOCKER_HONESTLY_SHARPENED_REVIEW_001.json) | 1 | 1 | `2d5325decd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_acrtdsk_claude_…` |
| [DETERMINEX_ACRTDSK_CLAUDE_CLEAN_RUNNER_EXECUTION_REVIEW_001](../locks/sentinel/DETERMINEX_ACRTDSK_CLAUDE_CLEAN_RUNNER_EXECUTION_REVIEW_001.json) | 1 | 1 | `2d5325decd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_acrtdsk_claude_…` |
| [DETERMINEX_ACRTDSK_CLAUDE_CLEAN_RUNNER_ONE_TIME_SPEND_REVIEW_001](../locks/sentinel/DETERMINEX_ACRTDSK_CLAUDE_CLEAN_RUNNER_ONE_TIME_SPEND_REVIEW_001.json) | 1 | 1 | `2d5325decd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_acrtdsk_claude_…` |
| [DETERMINEX_ACRTDSK_CLAUDE_CLEAN_RUNNER_PACKET_VALIDATION_REVIEW_001](../locks/sentinel/DETERMINEX_ACRTDSK_CLAUDE_CLEAN_RUNNER_PACKET_VALIDATION_REVIEW_001.json) | 1 | 1 | `2d5325decd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_acrtdsk_claude_…` |
| [DETERMINEX_ACRTDSK_CLAUDE_CLEAN_RUNNER_QUEUE_ADMISSION_REVIEW_001](../locks/sentinel/DETERMINEX_ACRTDSK_CLAUDE_CLEAN_RUNNER_QUEUE_ADMISSION_REVIEW_001.json) | 1 | 1 | `2d5325decd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_acrtdsk_claude_…` |
| [DETERMINEX_ACRTDSK_CLAUDE_CLEAN_RUNNER_TRANSCRIPTS_REVIEW_001](../locks/sentinel/DETERMINEX_ACRTDSK_CLAUDE_CLEAN_RUNNER_TRANSCRIPTS_REVIEW_001.json) | 1 | 1 | `2d5325decd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_acrtdsk_claude_…` |
| [DETERMINEX_ACRTDSK_CLAUDE_C_STORAGE_INVENTORY_REVIEW_001](../locks/sentinel/DETERMINEX_ACRTDSK_CLAUDE_C_STORAGE_INVENTORY_REVIEW_001.json) | 1 | 1 | `2d5325decd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_acrtdsk_claude_…` |
| [DETERMINEX_ACRTDSK_CLAUDE_EVIDENCE_INDEX_CLEAN_REVIEW_001](../locks/sentinel/DETERMINEX_ACRTDSK_CLAUDE_EVIDENCE_INDEX_CLEAN_REVIEW_001.json) | 1 | 1 | `2d5325decd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_acrtdsk_claude_…` |
| [DETERMINEX_ACRTDSK_CLAUDE_FAMILY_CONVEYOR_BROWSER_TAURI_REVIEW_001](../locks/sentinel/DETERMINEX_ACRTDSK_CLAUDE_FAMILY_CONVEYOR_BROWSER_TAURI_REVIEW_001.json) | 1 | 1 | `2d5325decd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_acrtdsk_claude_…` |
| [DETERMINEX_ACRTDSK_CLAUDE_FAMILY_CONVEYOR_HIGH_RISK_REVIEW_001](../locks/sentinel/DETERMINEX_ACRTDSK_CLAUDE_FAMILY_CONVEYOR_HIGH_RISK_REVIEW_001.json) | 1 | 1 | `2d5325decd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_acrtdsk_claude_…` |
| [DETERMINEX_ACRTDSK_CLAUDE_FAMILY_CONVEYOR_PHP_RUBY_REVIEW_001](../locks/sentinel/DETERMINEX_ACRTDSK_CLAUDE_FAMILY_CONVEYOR_PHP_RUBY_REVIEW_001.json) | 1 | 1 | `2d5325decd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_acrtdsk_claude_…` |
| [DETERMINEX_ACRTDSK_CLAUDE_FORBIDDEN_ACTIONS_DIRTY_STATE_REVIEW_001](../locks/sentinel/DETERMINEX_ACRTDSK_CLAUDE_FORBIDDEN_ACTIONS_DIRTY_STATE_REVIEW_001.json) | 1 | 1 | `2d5325decd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_acrtdsk_claude_…` |
| [DETERMINEX_ACRTDSK_CLAUDE_FULL_STATUS_SEGMENTATION_REVIEW_001](../locks/sentinel/DETERMINEX_ACRTDSK_CLAUDE_FULL_STATUS_SEGMENTATION_REVIEW_001.json) | 1 | 1 | `2d5325decd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_acrtdsk_claude_…` |
| [DETERMINEX_ACRTDSK_CLAUDE_GUI_BUILD_INSTALLER_BETA_NOT_EXECUTED_REVIEW_001](../locks/sentinel/DETERMINEX_ACRTDSK_CLAUDE_GUI_BUILD_INSTALLER_BETA_NOT_EXECUTED_REVIEW_001.json) | 1 | 1 | `2d5325decd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_acrtdsk_claude_…` |
| [DETERMINEX_ACRTDSK_CLAUDE_KNOWN_WORLD_CAPABILITY_REGISTRY_REVIEW_001](../locks/sentinel/DETERMINEX_ACRTDSK_CLAUDE_KNOWN_WORLD_CAPABILITY_REGISTRY_REVIEW_001.json) | 1 | 1 | `2d5325decd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_acrtdsk_claude_…` |
| [DETERMINEX_ACRTDSK_CLAUDE_KNOWN_WORLD_DETECTOR_GAP_QUEUE_REVIEW_001](../locks/sentinel/DETERMINEX_ACRTDSK_CLAUDE_KNOWN_WORLD_DETECTOR_GAP_QUEUE_REVIEW_001.json) | 1 | 1 | `2d5325decd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_acrtdsk_claude_…` |
| [DETERMINEX_ACRTDSK_CLAUDE_NO_C_PATH_MOVED_NO_DELETION_REVIEW_001](../locks/sentinel/DETERMINEX_ACRTDSK_CLAUDE_NO_C_PATH_MOVED_NO_DELETION_REVIEW_001.json) | 1 | 1 | `2d5325decd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_acrtdsk_claude_…` |
| [DETERMINEX_ACRTDSK_CLAUDE_NO_FAKE_CLEAN_RUNNER_PROOF_REVIEW_001](../locks/sentinel/DETERMINEX_ACRTDSK_CLAUDE_NO_FAKE_CLEAN_RUNNER_PROOF_REVIEW_001.json) | 1 | 1 | `2d5325decd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_acrtdsk_claude_…` |
| [DETERMINEX_ACRTDSK_CLAUDE_NO_FAMILY_PROMOTION_NO_OVERCLAIM_REVIEW_001](../locks/sentinel/DETERMINEX_ACRTDSK_CLAUDE_NO_FAMILY_PROMOTION_NO_OVERCLAIM_REVIEW_001.json) | 1 | 1 | `2d5325decd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_acrtdsk_claude_…` |
| [DETERMINEX_ACRTDSK_CLAUDE_NO_RELEASE_READY_NO_BETA_CLAIM_REVIEW_001](../locks/sentinel/DETERMINEX_ACRTDSK_CLAUDE_NO_RELEASE_READY_NO_BETA_CLAIM_REVIEW_001.json) | 1 | 1 | `2d5325decd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_acrtdsk_claude_…` |
| [DETERMINEX_ACRTDSK_CLAUDE_NO_SILENT_HASH_MISMATCH_ACCEPTANCE_REVIEW_001](../locks/sentinel/DETERMINEX_ACRTDSK_CLAUDE_NO_SILENT_HASH_MISMATCH_ACCEPTANCE_REVIEW_001.json) | 1 | 1 | `2d5325decd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_acrtdsk_claude_…` |
| [DETERMINEX_ACRTDSK_CLAUDE_NO_TEST_VERIFIER_LOCKFILE_MUTATION_REVIEW_001](../locks/sentinel/DETERMINEX_ACRTDSK_CLAUDE_NO_TEST_VERIFIER_LOCKFILE_MUTATION_REVIEW_001.json) | 1 | 1 | `2d5325decd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_acrtdsk_claude_…` |
| [DETERMINEX_ACRTDSK_CLAUDE_QUEUE_SPEND_CONSERVATION_REVIEW_001](../locks/sentinel/DETERMINEX_ACRTDSK_CLAUDE_QUEUE_SPEND_CONSERVATION_REVIEW_001.json) | 1 | 1 | `2d5325decd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_acrtdsk_claude_…` |
| [DETERMINEX_ACRTDSK_CLAUDE_RELEASE_CAMPAIGN_STAGING_REVIEW_001](../locks/sentinel/DETERMINEX_ACRTDSK_CLAUDE_RELEASE_CAMPAIGN_STAGING_REVIEW_001.json) | 1 | 1 | `2d5325decd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_acrtdsk_claude_…` |
| [DETERMINEX_ACRTDSK_CLAUDE_RELEASE_CELLS_CANONICAL_REVIEW_001](../locks/sentinel/DETERMINEX_ACRTDSK_CLAUDE_RELEASE_CELLS_CANONICAL_REVIEW_001.json) | 1 | 1 | `2d5325decd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_acrtdsk_claude_…` |
| [DETERMINEX_ACRTDSK_CLAUDE_RELEASE_FAMILIES_CANONICAL_REVIEW_001](../locks/sentinel/DETERMINEX_ACRTDSK_CLAUDE_RELEASE_FAMILIES_CANONICAL_REVIEW_001.json) | 1 | 1 | `2d5325decd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_acrtdsk_claude_…` |
| [DETERMINEX_ACRTDSK_CLAUDE_REMAINING_NLV_FAMILIES_REVIEW_001](../locks/sentinel/DETERMINEX_ACRTDSK_CLAUDE_REMAINING_NLV_FAMILIES_REVIEW_001.json) | 1 | 1 | `2d5325decd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_acrtdsk_claude_…` |
| [DETERMINEX_ACRTDSK_CLAUDE_RUNNER_CONTEXT_MATERIALLY_DISTINCT_REVIEW_001](../locks/sentinel/DETERMINEX_ACRTDSK_CLAUDE_RUNNER_CONTEXT_MATERIALLY_DISTINCT_REVIEW_001.json) | 1 | 1 | `2d5325decd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_acrtdsk_claude_…` |
| [DETERMINEX_ACRTDSK_CLAUDE_SAFE_RELOCATION_PLAN_REVIEW_001](../locks/sentinel/DETERMINEX_ACRTDSK_CLAUDE_SAFE_RELOCATION_PLAN_REVIEW_001.json) | 1 | 1 | `2d5325decd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_acrtdsk_claude_…` |
| [DETERMINEX_ACRTDSK_CLAUDE_SBOM_BYTE_EXACT_GITATTRIBUTES_REVIEW_001](../locks/sentinel/DETERMINEX_ACRTDSK_CLAUDE_SBOM_BYTE_EXACT_GITATTRIBUTES_REVIEW_001.json) | 1 | 1 | `2d5325decd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_acrtdsk_claude_…` |
| [DETERMINEX_ACRTDSK_CLAUDE_SBOM_MAIN_WORKTREE_HASH_STABLE_REVIEW_001](../locks/sentinel/DETERMINEX_ACRTDSK_CLAUDE_SBOM_MAIN_WORKTREE_HASH_STABLE_REVIEW_001.json) | 1 | 1 | `2d5325decd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_acrtdsk_claude_…` |
| [DETERMINEX_ACRTDSK_CLAUDE_SCORE_MOVEMENT_ZERO_EVIDENCE_BOUND_REVIEW_001](../locks/sentinel/DETERMINEX_ACRTDSK_CLAUDE_SCORE_MOVEMENT_ZERO_EVIDENCE_BOUND_REVIEW_001.json) | 1 | 1 | `2d5325decd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_acrtdsk_claude_…` |
| [DETERMINEX_ACRTDSK_CLAUDE_SYNTHESIS_REVIEW_001](../locks/sentinel/DETERMINEX_ACRTDSK_CLAUDE_SYNTHESIS_REVIEW_001.json) | 1 | 1 | `2d5325decd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_acrtdsk_claude_…` |
| [DETERMINEX_ACRTDSK_CLAUDE_T_DRIVE_DETECTION_WRITABILITY_REVIEW_001](../locks/sentinel/DETERMINEX_ACRTDSK_CLAUDE_T_DRIVE_DETECTION_WRITABILITY_REVIEW_001.json) | 1 | 1 | `2d5325decd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_acrtdsk_claude_…` |
| [DETERMINEX_ACTIVE_UNIVERSAL_FAMILY_BOUNDED_EXECUTION_LOCK_001](../locks/sentinel/DETERMINEX_ACTIVE_UNIVERSAL_FAMILY_BOUNDED_EXECUTION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_ACTIVE_UNIVERSAL_FAMILY_CAPABILITY_PROMOTION_RULE_LOCK_001](../locks/sentinel/DETERMINEX_ACTIVE_UNIVERSAL_FAMILY_CAPABILITY_PROMOTION_RULE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_ACTIVE_UNIVERSAL_FAMILY_CONVEYOR_SCHEMA_LOCK_001](../locks/sentinel/DETERMINEX_ACTIVE_UNIVERSAL_FAMILY_CONVEYOR_SCHEMA_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_ACTIVE_UNIVERSAL_FAMILY_MARCH_PLAN_DASHBOARD_LOCK_001](../locks/sentinel/DETERMINEX_ACTIVE_UNIVERSAL_FAMILY_MARCH_PLAN_DASHBOARD_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_ACTIVE_UNIVERSAL_FAMILY_PRIORITIZATION_LOCK_001](../locks/sentinel/DETERMINEX_ACTIVE_UNIVERSAL_FAMILY_PRIORITIZATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_ACTIVE_UNIVERSAL_FAMILY_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_ACTIVE_UNIVERSAL_FAMILY_RECONCILIATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_ACTIVE_UNIVERSAL_FAMILY_REPAIR_DISCIPLINE_GUARD_LOCK_001](../locks/sentinel/DETERMINEX_ACTIVE_UNIVERSAL_FAMILY_REPAIR_DISCIPLINE_GUARD_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_ACTIVE_UNIVERSAL_FAMILY_SBOM_NEXT_ACTION_PREP_LOCK_001](../locks/sentinel/DETERMINEX_ACTIVE_UNIVERSAL_FAMILY_SBOM_NEXT_ACTION_PREP_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_ACTIVE_UNIVERSAL_FAMILY_SCORE_CANONICALIZATION_DECISION_LOCK_001](../locks/sentinel/DETERMINEX_ACTIVE_UNIVERSAL_FAMILY_SCORE_CANONICALIZATION_DECISION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_ACTIVE_UNIVERSAL_FAMILY_STATUS_UPDATE_LOCK_001](../locks/sentinel/DETERMINEX_ACTIVE_UNIVERSAL_FAMILY_STATUS_UPDATE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_ADMITTED_CLEAN_RUNNER_EXECUTION_LOCK_001](../locks/sentinel/DETERMINEX_ADMITTED_CLEAN_RUNNER_EXECUTION_LOCK_001.json) | 18 | 1 | `e4ff17592c` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_admitted_clean_…` |
| [DETERMINEX_ADMITTED_CLEAN_RUNNER_PACKET_LOCK_001](../locks/sentinel/DETERMINEX_ADMITTED_CLEAN_RUNNER_PACKET_LOCK_001.json) | 18 | 1 | `e4ff17592c` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_admitted_clean_…` |
| [DETERMINEX_ADMITTED_CLEAN_RUNNER_QUEUE_SPEND_LOCK_001](../locks/sentinel/DETERMINEX_ADMITTED_CLEAN_RUNNER_QUEUE_SPEND_LOCK_001.json) | 18 | 1 | `e4ff17592c` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_admitted_clean_…` |
| [DETERMINEX_ADMITTED_CLEAN_RUNNER_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_ADMITTED_CLEAN_RUNNER_RECONCILIATION_LOCK_001.json) | 18 | 1 | `e4ff17592c` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_admitted_clean_…` |
| [DETERMINEX_ADMITTED_CLEAN_RUNNER_SAFE_CLONE_RETRY_LOCK_001](../locks/sentinel/DETERMINEX_ADMITTED_CLEAN_RUNNER_SAFE_CLONE_RETRY_LOCK_001.json) | 21 | 21 | `pending-fi` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_runner_sa…` |
| [DETERMINEX_AFR_CLAUDE_ACTIVE_CONVEYOR_SCHEMA_REVIEW_001](../locks/sentinel/DETERMINEX_AFR_CLAUDE_ACTIVE_CONVEYOR_SCHEMA_REVIEW_001.json) | 1 | 1 | `cb243c5c2a` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_afr_claude_acti…` |
| [DETERMINEX_AFR_CLAUDE_BLOCKED_IS_ACCOUNTING_REVIEW_001](../locks/sentinel/DETERMINEX_AFR_CLAUDE_BLOCKED_IS_ACCOUNTING_REVIEW_001.json) | 1 | 1 | `cb243c5c2a` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_afr_claude_bloc…` |
| [DETERMINEX_AFR_CLAUDE_CAPABILITY_WITH_VERIFICATION_REVIEW_001](../locks/sentinel/DETERMINEX_AFR_CLAUDE_CAPABILITY_WITH_VERIFICATION_REVIEW_001.json) | 1 | 1 | `cb243c5c2a` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_afr_claude_capa…` |
| [DETERMINEX_AFR_CLAUDE_EVERY_NONVERIFIED_NEXT_ACTION_REVIEW_001](../locks/sentinel/DETERMINEX_AFR_CLAUDE_EVERY_NONVERIFIED_NEXT_ACTION_REVIEW_001.json) | 1 | 1 | `cb243c5c2a` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_afr_claude_ever…` |
| [DETERMINEX_AFR_CLAUDE_EVIDENCE_INDEX_GUARDS_REVIEW_001](../locks/sentinel/DETERMINEX_AFR_CLAUDE_EVIDENCE_INDEX_GUARDS_REVIEW_001.json) | 1 | 1 | `cb243c5c2a` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_afr_claude_evid…` |
| [DETERMINEX_AFR_CLAUDE_FAMILIES_SELECTED_REVIEW_001](../locks/sentinel/DETERMINEX_AFR_CLAUDE_FAMILIES_SELECTED_REVIEW_001.json) | 1 | 1 | `cb243c5c2a` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_afr_claude_fami…` |
| [DETERMINEX_AFR_CLAUDE_FAMILY_COUNT_MAPPED_REVIEW_001](../locks/sentinel/DETERMINEX_AFR_CLAUDE_FAMILY_COUNT_MAPPED_REVIEW_001.json) | 1 | 1 | `cb243c5c2a` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_afr_claude_fami…` |
| [DETERMINEX_AFR_CLAUDE_FAMILY_EXECUTION_VERDICTS_REVIEW_001](../locks/sentinel/DETERMINEX_AFR_CLAUDE_FAMILY_EXECUTION_VERDICTS_REVIEW_001.json) | 1 | 1 | `cb243c5c2a` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_afr_claude_fami…` |
| [DETERMINEX_AFR_CLAUDE_FAMILY_PRIORITIZATION_REVIEW_001](../locks/sentinel/DETERMINEX_AFR_CLAUDE_FAMILY_PRIORITIZATION_REVIEW_001.json) | 1 | 1 | `cb243c5c2a` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_afr_claude_fami…` |
| [DETERMINEX_AFR_CLAUDE_FAMILY_PROMOTIONS_REVIEW_001](../locks/sentinel/DETERMINEX_AFR_CLAUDE_FAMILY_PROMOTIONS_REVIEW_001.json) | 1 | 1 | `cb243c5c2a` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_afr_claude_fami…` |
| [DETERMINEX_AFR_CLAUDE_FAMILY_REPAIR_VERDICTS_REVIEW_001](../locks/sentinel/DETERMINEX_AFR_CLAUDE_FAMILY_REPAIR_VERDICTS_REVIEW_001.json) | 1 | 1 | `cb243c5c2a` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_afr_claude_fami…` |
| [DETERMINEX_AFR_CLAUDE_FAMILY_STATUS_SUMMARY_REVIEW_001](../locks/sentinel/DETERMINEX_AFR_CLAUDE_FAMILY_STATUS_SUMMARY_REVIEW_001.json) | 1 | 1 | `cb243c5c2a` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_afr_claude_fami…` |
| [DETERMINEX_AFR_CLAUDE_FAMILY_VERIFICATION_VERDICTS_REVIEW_001](../locks/sentinel/DETERMINEX_AFR_CLAUDE_FAMILY_VERIFICATION_VERDICTS_REVIEW_001.json) | 1 | 1 | `cb243c5c2a` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_afr_claude_fami…` |
| [DETERMINEX_AFR_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001](../locks/sentinel/DETERMINEX_AFR_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001.json) | 1 | 1 | `cb243c5c2a` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_afr_claude_forb…` |
| [DETERMINEX_AFR_CLAUDE_MARCH_PLAN_DASHBOARD_REVIEW_001](../locks/sentinel/DETERMINEX_AFR_CLAUDE_MARCH_PLAN_DASHBOARD_REVIEW_001.json) | 1 | 1 | `cb243c5c2a` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_afr_claude_marc…` |
| [DETERMINEX_AFR_CLAUDE_NO_BINARY_MUTATION_REVIEW_001](../locks/sentinel/DETERMINEX_AFR_CLAUDE_NO_BINARY_MUTATION_REVIEW_001.json) | 1 | 1 | `cb243c5c2a` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_afr_claude_no_b…` |
| [DETERMINEX_AFR_CLAUDE_NO_FAMILY_SUPPORT_REVIEW_001](../locks/sentinel/DETERMINEX_AFR_CLAUDE_NO_FAMILY_SUPPORT_REVIEW_001.json) | 1 | 1 | `cb243c5c2a` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_afr_claude_no_f…` |
| [DETERMINEX_AFR_CLAUDE_NO_LADDER_INVERSION_REVIEW_001](../locks/sentinel/DETERMINEX_AFR_CLAUDE_NO_LADDER_INVERSION_REVIEW_001.json) | 1 | 1 | `cb243c5c2a` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_afr_claude_no_l…` |
| [DETERMINEX_AFR_CLAUDE_NO_LOCKFILE_MUTATION_REVIEW_001](../locks/sentinel/DETERMINEX_AFR_CLAUDE_NO_LOCKFILE_MUTATION_REVIEW_001.json) | 1 | 1 | `cb243c5c2a` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_afr_claude_no_l…` |
| [DETERMINEX_AFR_CLAUDE_NO_TEST_MUTATION_REVIEW_001](../locks/sentinel/DETERMINEX_AFR_CLAUDE_NO_TEST_MUTATION_REVIEW_001.json) | 1 | 1 | `cb243c5c2a` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_afr_claude_no_t…` |
| [DETERMINEX_AFR_CLAUDE_NO_UNIVERSAL_SUPPORT_REVIEW_001](../locks/sentinel/DETERMINEX_AFR_CLAUDE_NO_UNIVERSAL_SUPPORT_REVIEW_001.json) | 1 | 1 | `cb243c5c2a` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_afr_claude_no_u…` |
| [DETERMINEX_AFR_CLAUDE_NO_VERIFIER_MUTATION_REVIEW_001](../locks/sentinel/DETERMINEX_AFR_CLAUDE_NO_VERIFIER_MUTATION_REVIEW_001.json) | 1 | 1 | `cb243c5c2a` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_afr_claude_no_v…` |
| [DETERMINEX_AFR_CLAUDE_OTHER_PACKETS_NOT_EXECUTED_REVIEW_001](../locks/sentinel/DETERMINEX_AFR_CLAUDE_OTHER_PACKETS_NOT_EXECUTED_REVIEW_001.json) | 1 | 1 | `cb243c5c2a` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_afr_claude_othe…` |
| [DETERMINEX_AFR_CLAUDE_REACT_VITE_EVIDENCE_NOT_OVERSTATED_REVIEW_001](../locks/sentinel/DETERMINEX_AFR_CLAUDE_REACT_VITE_EVIDENCE_NOT_OVERSTATED_REVIEW_001.json) | 1 | 1 | `cb243c5c2a` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_afr_claude_reac…` |
| [DETERMINEX_AFR_CLAUDE_RELEASE_INVARIANTS_REVIEW_001](../locks/sentinel/DETERMINEX_AFR_CLAUDE_RELEASE_INVARIANTS_REVIEW_001.json) | 1 | 1 | `cb243c5c2a` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_afr_claude_rele…` |
| [DETERMINEX_AFR_CLAUDE_REMEDIATION_QUEUE_COUNT_REVIEW_001](../locks/sentinel/DETERMINEX_AFR_CLAUDE_REMEDIATION_QUEUE_COUNT_REVIEW_001.json) | 1 | 1 | `cb243c5c2a` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_afr_claude_reme…` |
| [DETERMINEX_AFR_CLAUDE_REPAIR_DISCIPLINE_REVIEW_001](../locks/sentinel/DETERMINEX_AFR_CLAUDE_REPAIR_DISCIPLINE_REVIEW_001.json) | 1 | 1 | `cb243c5c2a` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_afr_claude_repa…` |
| [DETERMINEX_AFR_CLAUDE_SBOM_NOT_EXECUTED_REVIEW_001](../locks/sentinel/DETERMINEX_AFR_CLAUDE_SBOM_NOT_EXECUTED_REVIEW_001.json) | 1 | 1 | `cb243c5c2a` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_afr_claude_sbom…` |
| [DETERMINEX_AFR_CLAUDE_SCORE_BEFORE_AFTER_REVIEW_001](../locks/sentinel/DETERMINEX_AFR_CLAUDE_SCORE_BEFORE_AFTER_REVIEW_001.json) | 1 | 1 | `cb243c5c2a` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_afr_claude_scor…` |
| [DETERMINEX_AFR_CLAUDE_SCORE_CANONICALIZATION_REVIEW_001](../locks/sentinel/DETERMINEX_AFR_CLAUDE_SCORE_CANONICALIZATION_REVIEW_001.json) | 1 | 1 | `cb243c5c2a` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_afr_claude_scor…` |
| [DETERMINEX_AFR_CLAUDE_SYNTHESIS_REVIEW_001](../locks/sentinel/DETERMINEX_AFR_CLAUDE_SYNTHESIS_REVIEW_001.json) | 1 | 1 | `cb243c5c2a` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_afr_claude_synt…` |
| [DETERMINEX_AFR_CLAUDE_TIER1_STATUS_REVIEW_001](../locks/sentinel/DETERMINEX_AFR_CLAUDE_TIER1_STATUS_REVIEW_001.json) | 1 | 1 | `cb243c5c2a` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_afr_claude_tier…` |
| [DETERMINEX_ALL_CURRENT_RELEASE_CELL_READERS_BIND_TO_REGISTRY_LOCK_001](../locks/sentinel/DETERMINEX_ALL_CURRENT_RELEASE_CELL_READERS_BIND_TO_REGISTRY_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_018_canoni…` |
| [DETERMINEX_ALL_FAMILY_ADAPTER_STUB_COMPLETION_LOCK_001](../locks/sentinel/DETERMINEX_ALL_FAMILY_ADAPTER_STUB_COMPLETION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_under…` |
| [DETERMINEX_ALL_GAP_CLOSURE_BATCH_002_LOCK](../locks/sentinel/DETERMINEX_ALL_GAP_CLOSURE_BATCH_002_LOCK.json) | 6 | 6 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_all_gap_closure…` |
| [DETERMINEX_ALL_GAP_CLOSURE_BATCH_003_LOCK](../locks/sentinel/DETERMINEX_ALL_GAP_CLOSURE_BATCH_003_LOCK.json) | 6 | 6 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_all_gap_closure…` |
| [DETERMINEX_APPEND_ONLY_EVIDENCE_LEDGER_LOCK_001](../locks/sentinel/DETERMINEX_APPEND_ONLY_EVIDENCE_LEDGER_LOCK_001.json) | 5 | 5 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/proof/test_determinex_append_o…` |
| [DETERMINEX_APPROVAL_AUDIT_LOG_APPEND_ONLY_WRITER_LOCK_001](../locks/sentinel/DETERMINEX_APPROVAL_AUDIT_LOG_APPEND_ONLY_WRITER_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_APPROVAL_PACKET_SIGNING_SIMULATION_DRY_RUN_LOCK_001](../locks/sentinel/DETERMINEX_APPROVAL_PACKET_SIGNING_SIMULATION_DRY_RUN_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_APPROVAL_RESOLUTION_MATRIX_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_APPROVAL_RESOLUTION_MATRIX_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_007_approv…` |
| [DETERMINEX_APPROVAL_VALIDATOR_AT_EXECUTION_SITE_WIRING_LOCK_001](../locks/sentinel/DETERMINEX_APPROVAL_VALIDATOR_AT_EXECUTION_SITE_WIRING_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_APP_CLASS_LANGUAGE_AND_WORKFLOW_SUPPORT_MATRIX_LOCK_001](../locks/sentinel/DETERMINEX_APP_CLASS_LANGUAGE_AND_WORKFLOW_SUPPORT_MATRIX_LOCK_001.json) | 17 | 17 | `cd3a6d5322` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_determinex_unified…` |
| [DETERMINEX_APP_CREATION_BENCH_SEED_LOCK_001](../locks/sentinel/DETERMINEX_APP_CREATION_BENCH_SEED_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_determinex_univers…` |
| [DETERMINEX_ARCHITECTURE_REGRESSION_GAUNTLET_LOCK_001](../locks/sentinel/DETERMINEX_ARCHITECTURE_REGRESSION_GAUNTLET_LOCK_001.json) | 16 | 16 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/dev/test_architecture_regre…` |
| [DETERMINEX_ATASFC_CLAUDE_APPEND_ONLY_COUNT_DRIFT_GUARDS_REVIEW_001](../locks/sentinel/DETERMINEX_ATASFC_CLAUDE_APPEND_ONLY_COUNT_DRIFT_GUARDS_REVIEW_001.json) | 1 | 1 | `057dabd514` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_atasfc_claude_a…` |
| [DETERMINEX_ATASFC_CLAUDE_AUTHORITY_REQUIRED_EXECUTION_SCOPED_REVIEW_001](../locks/sentinel/DETERMINEX_ATASFC_CLAUDE_AUTHORITY_REQUIRED_EXECUTION_SCOPED_REVIEW_001.json) | 1 | 1 | `057dabd514` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_atasfc_claude_a…` |
| [DETERMINEX_ATASFC_CLAUDE_BETA_DASHBOARD_NOT_PUBLISHED_REVIEW_001](../locks/sentinel/DETERMINEX_ATASFC_CLAUDE_BETA_DASHBOARD_NOT_PUBLISHED_REVIEW_001.json) | 1 | 1 | `057dabd514` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_atasfc_claude_b…` |
| [DETERMINEX_ATASFC_CLAUDE_CAPABILITY_PROMOTION_EVIDENCE_BOUND_REVIEW_001](../locks/sentinel/DETERMINEX_ATASFC_CLAUDE_CAPABILITY_PROMOTION_EVIDENCE_BOUND_REVIEW_001.json) | 1 | 1 | `057dabd514` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_atasfc_claude_c…` |
| [DETERMINEX_ATASFC_CLAUDE_CLAIM_SCANNER_DAY1_OVERCLAIM_REVIEW_001](../locks/sentinel/DETERMINEX_ATASFC_CLAUDE_CLAIM_SCANNER_DAY1_OVERCLAIM_REVIEW_001.json) | 1 | 1 | `057dabd514` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_atasfc_claude_c…` |
| [DETERMINEX_ATASFC_CLAUDE_CLEAN_HOST_NOT_EXECUTED_REVIEW_001](../locks/sentinel/DETERMINEX_ATASFC_CLAUDE_CLEAN_HOST_NOT_EXECUTED_REVIEW_001.json) | 1 | 1 | `057dabd514` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_atasfc_claude_c…` |
| [DETERMINEX_ATASFC_CLAUDE_DIRTY_UNTRACKED_STATE_REVIEW_001](../locks/sentinel/DETERMINEX_ATASFC_CLAUDE_DIRTY_UNTRACKED_STATE_REVIEW_001.json) | 1 | 1 | `057dabd514` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_atasfc_claude_d…` |
| [DETERMINEX_ATASFC_CLAUDE_EVERY_REMAINING_FAMILY_ADVANCED_OR_SHARPENED_REVIEW_001](../locks/sentinel/DETERMINEX_ATASFC_CLAUDE_EVERY_REMAINING_FAMILY_ADVANCED_OR_SHARPENED_REVIEW_001.json) | 1 | 1 | `057dabd514` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_atasfc_claude_e…` |
| [DETERMINEX_ATASFC_CLAUDE_EVIDENCE_INDEX_CLEAN_REVIEW_001](../locks/sentinel/DETERMINEX_ATASFC_CLAUDE_EVIDENCE_INDEX_CLEAN_REVIEW_001.json) | 1 | 1 | `057dabd514` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_atasfc_claude_e…` |
| [DETERMINEX_ATASFC_CLAUDE_EXACT_LOCAL_NOT_FAMILY_SUPPORT_REVIEW_001](../locks/sentinel/DETERMINEX_ATASFC_CLAUDE_EXACT_LOCAL_NOT_FAMILY_SUPPORT_REVIEW_001.json) | 1 | 1 | `057dabd514` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_atasfc_claude_e…` |
| [DETERMINEX_ATASFC_CLAUDE_FAMILY_REPAIR_SCOPE_REVIEW_001](../locks/sentinel/DETERMINEX_ATASFC_CLAUDE_FAMILY_REPAIR_SCOPE_REVIEW_001.json) | 1 | 1 | `057dabd514` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_atasfc_claude_f…` |
| [DETERMINEX_ATASFC_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001](../locks/sentinel/DETERMINEX_ATASFC_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001.json) | 1 | 1 | `057dabd514` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_atasfc_claude_f…` |
| [DETERMINEX_ATASFC_CLAUDE_FULL_STATUS_TIMEOUT_REVIEW_001](../locks/sentinel/DETERMINEX_ATASFC_CLAUDE_FULL_STATUS_TIMEOUT_REVIEW_001.json) | 1 | 1 | `057dabd514` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_atasfc_claude_f…` |
| [DETERMINEX_ATASFC_CLAUDE_GUI_BUILD_NOT_EXECUTED_REVIEW_001](../locks/sentinel/DETERMINEX_ATASFC_CLAUDE_GUI_BUILD_NOT_EXECUTED_REVIEW_001.json) | 1 | 1 | `057dabd514` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_atasfc_claude_g…` |
| [DETERMINEX_ATASFC_CLAUDE_INSTALLER_RELEASE_NOT_EXECUTED_REVIEW_001](../locks/sentinel/DETERMINEX_ATASFC_CLAUDE_INSTALLER_RELEASE_NOT_EXECUTED_REVIEW_001.json) | 1 | 1 | `057dabd514` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_atasfc_claude_i…` |
| [DETERMINEX_ATASFC_CLAUDE_MARCH_PLAN_DASHBOARD_REVIEW_001](../locks/sentinel/DETERMINEX_ATASFC_CLAUDE_MARCH_PLAN_DASHBOARD_REVIEW_001.json) | 1 | 1 | `057dabd514` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_atasfc_claude_m…` |
| [DETERMINEX_ATASFC_CLAUDE_MISSING_TOOLS_CONVERTED_TO_PACKETS_REVIEW_001](../locks/sentinel/DETERMINEX_ATASFC_CLAUDE_MISSING_TOOLS_CONVERTED_TO_PACKETS_REVIEW_001.json) | 1 | 1 | `057dabd514` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_atasfc_claude_m…` |
| [DETERMINEX_ATASFC_CLAUDE_NO_FAKE_SBOM_REVIEW_001](../locks/sentinel/DETERMINEX_ATASFC_CLAUDE_NO_FAKE_SBOM_REVIEW_001.json) | 1 | 1 | `057dabd514` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_atasfc_claude_n…` |
| [DETERMINEX_ATASFC_CLAUDE_NO_TEST_MUTATION_REVIEW_001](../locks/sentinel/DETERMINEX_ATASFC_CLAUDE_NO_TEST_MUTATION_REVIEW_001.json) | 1 | 1 | `057dabd514` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_atasfc_claude_n…` |
| [DETERMINEX_ATASFC_CLAUDE_NO_UNCONTROLLED_INSTALL_REVIEW_001](../locks/sentinel/DETERMINEX_ATASFC_CLAUDE_NO_UNCONTROLLED_INSTALL_REVIEW_001.json) | 1 | 1 | `057dabd514` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_atasfc_claude_n…` |
| [DETERMINEX_ATASFC_CLAUDE_NO_UNIVERSAL_SUPPORT_CLAIM_REVIEW_001](../locks/sentinel/DETERMINEX_ATASFC_CLAUDE_NO_UNIVERSAL_SUPPORT_CLAIM_REVIEW_001.json) | 1 | 1 | `057dabd514` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_atasfc_claude_n…` |
| [DETERMINEX_ATASFC_CLAUDE_NO_VERIFIER_ORACLE_MUTATION_REVIEW_001](../locks/sentinel/DETERMINEX_ATASFC_CLAUDE_NO_VERIFIER_ORACLE_MUTATION_REVIEW_001.json) | 1 | 1 | `057dabd514` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_atasfc_claude_n…` |
| [DETERMINEX_ATASFC_CLAUDE_NPM_DEPENDENCY_REPAIR_REVIEW_001](../locks/sentinel/DETERMINEX_ATASFC_CLAUDE_NPM_DEPENDENCY_REPAIR_REVIEW_001.json) | 1 | 1 | `057dabd514` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_atasfc_claude_n…` |
| [DETERMINEX_ATASFC_CLAUDE_OPERATOR_TOOL_ACQUISITION_AUTHORIZATION_SCOPED_REVIEW_001](../locks/sentinel/DETERMINEX_ATASFC_CLAUDE_OPERATOR_TOOL_ACQUISITION_AUTHORIZATION_SCOPED_REVIEW_001.json) | 1 | 1 | `057dabd514` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_atasfc_claude_o…` |
| [DETERMINEX_ATASFC_CLAUDE_PACKAGE_LOCKFILE_AUTHORITY_REVIEW_001](../locks/sentinel/DETERMINEX_ATASFC_CLAUDE_PACKAGE_LOCKFILE_AUTHORITY_REVIEW_001.json) | 1 | 1 | `057dabd514` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_atasfc_claude_p…` |
| [DETERMINEX_ATASFC_CLAUDE_RELEASE_CELLS_CANONICAL_REVIEW_001](../locks/sentinel/DETERMINEX_ATASFC_CLAUDE_RELEASE_CELLS_CANONICAL_REVIEW_001.json) | 1 | 1 | `057dabd514` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_atasfc_claude_r…` |
| [DETERMINEX_ATASFC_CLAUDE_RELEASE_FAMILIES_CANONICAL_REVIEW_001](../locks/sentinel/DETERMINEX_ATASFC_CLAUDE_RELEASE_FAMILIES_CANONICAL_REVIEW_001.json) | 1 | 1 | `057dabd514` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_atasfc_claude_r…` |
| [DETERMINEX_ATASFC_CLAUDE_REPO_LOCAL_PATH_PREFERRED_REVIEW_001](../locks/sentinel/DETERMINEX_ATASFC_CLAUDE_REPO_LOCAL_PATH_PREFERRED_REVIEW_001.json) | 1 | 1 | `057dabd514` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_atasfc_claude_r…` |
| [DETERMINEX_ATASFC_CLAUDE_RUNTIME_QUEUE_SPEND_ACCURATE_REVIEW_001](../locks/sentinel/DETERMINEX_ATASFC_CLAUDE_RUNTIME_QUEUE_SPEND_ACCURATE_REVIEW_001.json) | 1 | 1 | `057dabd514` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_atasfc_claude_r…` |
| [DETERMINEX_ATASFC_CLAUDE_SBOM_BLOCKER_NARROWER_REVIEW_001](../locks/sentinel/DETERMINEX_ATASFC_CLAUDE_SBOM_BLOCKER_NARROWER_REVIEW_001.json) | 1 | 1 | `057dabd514` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_atasfc_claude_s…` |
| [DETERMINEX_ATASFC_CLAUDE_SBOM_OUTPUT_EXISTS_HASHED_REVIEW_001](../locks/sentinel/DETERMINEX_ATASFC_CLAUDE_SBOM_OUTPUT_EXISTS_HASHED_REVIEW_001.json) | 1 | 1 | `057dabd514` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_atasfc_claude_s…` |
| [DETERMINEX_ATASFC_CLAUDE_SCORE_MOVEMENT_EVIDENCE_BOUND_REVIEW_001](../locks/sentinel/DETERMINEX_ATASFC_CLAUDE_SCORE_MOVEMENT_EVIDENCE_BOUND_REVIEW_001.json) | 1 | 1 | `057dabd514` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_atasfc_claude_s…` |
| [DETERMINEX_ATASFC_CLAUDE_SYFT_ADMISSION_LEGITIMATE_REVIEW_001](../locks/sentinel/DETERMINEX_ATASFC_CLAUDE_SYFT_ADMISSION_LEGITIMATE_REVIEW_001.json) | 1 | 1 | `057dabd514` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_atasfc_claude_s…` |
| [DETERMINEX_ATASFC_CLAUDE_SYNTHESIS_REVIEW_001](../locks/sentinel/DETERMINEX_ATASFC_CLAUDE_SYNTHESIS_REVIEW_001.json) | 1 | 1 | `057dabd514` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_atasfc_claude_s…` |
| [DETERMINEX_ATASFC_CLAUDE_TOOLCHAIN_ACQUISITION_SCOPED_AUTHORIZED_REVIEW_001](../locks/sentinel/DETERMINEX_ATASFC_CLAUDE_TOOLCHAIN_ACQUISITION_SCOPED_AUTHORIZED_REVIEW_001.json) | 1 | 1 | `057dabd514` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_atasfc_claude_t…` |
| [DETERMINEX_ATASFC_CLAUDE_TOOL_ACQUISITION_QUEUE_SPEND_BEFORE_EXEC_REVIEW_001](../locks/sentinel/DETERMINEX_ATASFC_CLAUDE_TOOL_ACQUISITION_QUEUE_SPEND_BEFORE_EXEC_REVIEW_001.json) | 1 | 1 | `057dabd514` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_atasfc_claude_t…` |
| [DETERMINEX_ATASFC_CLAUDE_UNKNOWN_NOVEL_NO_BROAD_CLAIM_REVIEW_001](../locks/sentinel/DETERMINEX_ATASFC_CLAUDE_UNKNOWN_NOVEL_NO_BROAD_CLAIM_REVIEW_001.json) | 1 | 1 | `057dabd514` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_atasfc_claude_u…` |
| [DETERMINEX_AUTHORITY_BATCH_EXECUTION_LOCK_001](../locks/sentinel/DETERMINEX_AUTHORITY_BATCH_EXECUTION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_AUTHORIZED_TOOL_ACQUISITION_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_AUTHORIZED_TOOL_ACQUISITION_RECONCILIATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_AUTHORIZED_TOOL_DASHBOARD_MARCH_PLAN_LOCK_001](../locks/sentinel/DETERMINEX_AUTHORIZED_TOOL_DASHBOARD_MARCH_PLAN_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_BRIDGE_CLAUDE_APPEND_ONLY_COUNT_DRIFT_REVIEW_001](../locks/sentinel/DETERMINEX_BRIDGE_CLAUDE_APPEND_ONLY_COUNT_DRIFT_REVIEW_001.json) | 1 | 1 | `973e14baf4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_bridge_claude_a…` |
| [DETERMINEX_BRIDGE_CLAUDE_BETA_DASHBOARD_NO_PUBLISH_REVIEW_001](../locks/sentinel/DETERMINEX_BRIDGE_CLAUDE_BETA_DASHBOARD_NO_PUBLISH_REVIEW_001.json) | 1 | 1 | `973e14baf4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_bridge_claude_b…` |
| [DETERMINEX_BRIDGE_CLAUDE_BRIDGE_REJECTION_CORPUS_REVIEW_001](../locks/sentinel/DETERMINEX_BRIDGE_CLAUDE_BRIDGE_REJECTION_CORPUS_REVIEW_001.json) | 1 | 1 | `973e14baf4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_bridge_claude_b…` |
| [DETERMINEX_BRIDGE_CLAUDE_CLAIM_SCANNER_OVERCLAIM_REVIEW_001](../locks/sentinel/DETERMINEX_BRIDGE_CLAUDE_CLAIM_SCANNER_OVERCLAIM_REVIEW_001.json) | 1 | 1 | `973e14baf4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_bridge_claude_c…` |
| [DETERMINEX_BRIDGE_CLAUDE_CLEAN_HOST_NO_SEPARATE_SPEND_REVIEW_001](../locks/sentinel/DETERMINEX_BRIDGE_CLAUDE_CLEAN_HOST_NO_SEPARATE_SPEND_REVIEW_001.json) | 1 | 1 | `973e14baf4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_bridge_claude_c…` |
| [DETERMINEX_BRIDGE_CLAUDE_COMMAND_MATCHES_APPROVED_REVIEW_001](../locks/sentinel/DETERMINEX_BRIDGE_CLAUDE_COMMAND_MATCHES_APPROVED_REVIEW_001.json) | 1 | 1 | `973e14baf4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_bridge_claude_c…` |
| [DETERMINEX_BRIDGE_CLAUDE_DIRTY_STATE_REPORTED_REVIEW_001](../locks/sentinel/DETERMINEX_BRIDGE_CLAUDE_DIRTY_STATE_REPORTED_REVIEW_001.json) | 1 | 1 | `973e14baf4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_bridge_claude_d…` |
| [DETERMINEX_BRIDGE_CLAUDE_EVIDENCE_INDEX_CLEAN_REVIEW_001](../locks/sentinel/DETERMINEX_BRIDGE_CLAUDE_EVIDENCE_INDEX_CLEAN_REVIEW_001.json) | 1 | 1 | `973e14baf4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_bridge_claude_e…` |
| [DETERMINEX_BRIDGE_CLAUDE_EXACTLY_ONE_ADMITTED_FIRST_REVIEW_001](../locks/sentinel/DETERMINEX_BRIDGE_CLAUDE_EXACTLY_ONE_ADMITTED_FIRST_REVIEW_001.json) | 1 | 1 | `973e14baf4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_bridge_claude_e…` |
| [DETERMINEX_BRIDGE_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001](../locks/sentinel/DETERMINEX_BRIDGE_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001.json) | 1 | 1 | `973e14baf4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_bridge_claude_f…` |
| [DETERMINEX_BRIDGE_CLAUDE_GUI_BUILD_NO_SEPARATE_SPEND_REVIEW_001](../locks/sentinel/DETERMINEX_BRIDGE_CLAUDE_GUI_BUILD_NO_SEPARATE_SPEND_REVIEW_001.json) | 1 | 1 | `973e14baf4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_bridge_claude_g…` |
| [DETERMINEX_BRIDGE_CLAUDE_INSTALLER_RELEASE_NO_SEPARATE_SPEND_REVIEW_001](../locks/sentinel/DETERMINEX_BRIDGE_CLAUDE_INSTALLER_RELEASE_NO_SEPARATE_SPEND_REVIEW_001.json) | 1 | 1 | `973e14baf4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_bridge_claude_i…` |
| [DETERMINEX_BRIDGE_CLAUDE_NO_FORBIDDEN_PROTECTED_ACTION_REVIEW_001](../locks/sentinel/DETERMINEX_BRIDGE_CLAUDE_NO_FORBIDDEN_PROTECTED_ACTION_REVIEW_001.json) | 1 | 1 | `973e14baf4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_bridge_claude_n…` |
| [DETERMINEX_BRIDGE_CLAUDE_OARG_PACKET_DISCOVERY_REVIEW_001](../locks/sentinel/DETERMINEX_BRIDGE_CLAUDE_OARG_PACKET_DISCOVERY_REVIEW_001.json) | 1 | 1 | `973e14baf4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_bridge_claude_o…` |
| [DETERMINEX_BRIDGE_CLAUDE_OTHER_PACKETS_NOT_EXECUTED_REVIEW_001](../locks/sentinel/DETERMINEX_BRIDGE_CLAUDE_OTHER_PACKETS_NOT_EXECUTED_REVIEW_001.json) | 1 | 1 | `973e14baf4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_bridge_claude_o…` |
| [DETERMINEX_BRIDGE_CLAUDE_PACKET_HASH_VERIFICATION_REVIEW_001](../locks/sentinel/DETERMINEX_BRIDGE_CLAUDE_PACKET_HASH_VERIFICATION_REVIEW_001.json) | 1 | 1 | `973e14baf4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_bridge_claude_p…` |
| [DETERMINEX_BRIDGE_CLAUDE_QUEUE_BEFORE_AFTER_REVIEW_001](../locks/sentinel/DETERMINEX_BRIDGE_CLAUDE_QUEUE_BEFORE_AFTER_REVIEW_001.json) | 1 | 1 | `973e14baf4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_bridge_claude_q…` |
| [DETERMINEX_BRIDGE_CLAUDE_REACT_VITE_FIRST_TARGETED_REVIEW_001](../locks/sentinel/DETERMINEX_BRIDGE_CLAUDE_REACT_VITE_FIRST_TARGETED_REVIEW_001.json) | 1 | 1 | `973e14baf4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_bridge_claude_r…` |
| [DETERMINEX_BRIDGE_CLAUDE_REACT_VITE_IN_SCOPE_REVIEW_001](../locks/sentinel/DETERMINEX_BRIDGE_CLAUDE_REACT_VITE_IN_SCOPE_REVIEW_001.json) | 1 | 1 | `973e14baf4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_bridge_claude_r…` |
| [DETERMINEX_BRIDGE_CLAUDE_RELEASE_CELLS_CANONICAL_REVIEW_001](../locks/sentinel/DETERMINEX_BRIDGE_CLAUDE_RELEASE_CELLS_CANONICAL_REVIEW_001.json) | 1 | 1 | `973e14baf4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_bridge_claude_r…` |
| [DETERMINEX_BRIDGE_CLAUDE_RELEASE_FAMILIES_CANONICAL_REVIEW_001](../locks/sentinel/DETERMINEX_BRIDGE_CLAUDE_RELEASE_FAMILIES_CANONICAL_REVIEW_001.json) | 1 | 1 | `973e14baf4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_bridge_claude_r…` |
| [DETERMINEX_BRIDGE_CLAUDE_RUNTIME_QUEUE_BRIDGE_REVIEW_001](../locks/sentinel/DETERMINEX_BRIDGE_CLAUDE_RUNTIME_QUEUE_BRIDGE_REVIEW_001.json) | 1 | 1 | `973e14baf4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_bridge_claude_r…` |
| [DETERMINEX_BRIDGE_CLAUDE_SBOM_NO_SEPARATE_SPEND_REVIEW_001](../locks/sentinel/DETERMINEX_BRIDGE_CLAUDE_SBOM_NO_SEPARATE_SPEND_REVIEW_001.json) | 1 | 1 | `973e14baf4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_bridge_claude_s…` |
| [DETERMINEX_BRIDGE_CLAUDE_SCORES_EVIDENCE_BOUND_REVIEW_001](../locks/sentinel/DETERMINEX_BRIDGE_CLAUDE_SCORES_EVIDENCE_BOUND_REVIEW_001.json) | 1 | 1 | `973e14baf4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_bridge_claude_s…` |
| [DETERMINEX_BRIDGE_CLAUDE_SPEND_BEFORE_AFTER_REVIEW_001](../locks/sentinel/DETERMINEX_BRIDGE_CLAUDE_SPEND_BEFORE_AFTER_REVIEW_001.json) | 1 | 1 | `973e14baf4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_bridge_claude_s…` |
| [DETERMINEX_BRIDGE_CLAUDE_SPEND_ONE_ENTRY_CONSUMED_REVIEW_001](../locks/sentinel/DETERMINEX_BRIDGE_CLAUDE_SPEND_ONE_ENTRY_CONSUMED_REVIEW_001.json) | 1 | 1 | `973e14baf4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_bridge_claude_s…` |
| [DETERMINEX_BRIDGE_CLAUDE_SPEND_REUSE_REJECTED_REVIEW_001](../locks/sentinel/DETERMINEX_BRIDGE_CLAUDE_SPEND_REUSE_REJECTED_REVIEW_001.json) | 1 | 1 | `973e14baf4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_bridge_claude_s…` |
| [DETERMINEX_BRIDGE_CLAUDE_SYNTHESIS_REVIEW_001](../locks/sentinel/DETERMINEX_BRIDGE_CLAUDE_SYNTHESIS_REVIEW_001.json) | 1 | 1 | `973e14baf4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_bridge_claude_s…` |
| [DETERMINEX_BRIDGE_CLAUDE_TIMEOUT_NOT_HIDDEN_REVIEW_001](../locks/sentinel/DETERMINEX_BRIDGE_CLAUDE_TIMEOUT_NOT_HIDDEN_REVIEW_001.json) | 1 | 1 | `973e14baf4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_bridge_claude_t…` |
| [DETERMINEX_BROADER_REPO_SBOM_AUTHORITY_GUARD_LOCK_001](../locks/sentinel/DETERMINEX_BROADER_REPO_SBOM_AUTHORITY_GUARD_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_BROADER_REPO_SBOM_EXECUTION_LOCK_001](../locks/sentinel/DETERMINEX_BROADER_REPO_SBOM_EXECUTION_LOCK_001.json) | 21 | 21 | `pending-fi` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_runner_sa…` |
| [DETERMINEX_BROADER_REPO_SBOM_PACKET_LOCK_001](../locks/sentinel/DETERMINEX_BROADER_REPO_SBOM_PACKET_LOCK_001.json) | 18 | 1 | `e4ff17592c` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_admitted_clean_…` |
| [DETERMINEX_BROWSER_EXTENSION_AUTHORITY_GATE_LOCK_001](../locks/sentinel/DETERMINEX_BROWSER_EXTENSION_AUTHORITY_GATE_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_BROWSER_TAURI_HARNESS_PACKET_STAGING_LOCK_001](../locks/sentinel/DETERMINEX_BROWSER_TAURI_HARNESS_PACKET_STAGING_LOCK_001.json) | 21 | 21 | `pending-fi` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_runner_sa…` |
| [DETERMINEX_BUILD_TEST_SMOKE_LADDER_EXPANSION_LOCK_001](../locks/sentinel/DETERMINEX_BUILD_TEST_SMOKE_LADDER_EXPANSION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_CANONICAL_CELLS_FAKE_TRANSCRIPT_REJECTION_COVERAGE_LOCK_001](../locks/sentinel/DETERMINEX_CANONICAL_CELLS_FAKE_TRANSCRIPT_REJECTION_COVERAGE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_018_canoni…` |
| [DETERMINEX_CANONICAL_CELL_PROOF_REPORT_ANCHOR_BACKFILL_LOCK_001](../locks/sentinel/DETERMINEX_CANONICAL_CELL_PROOF_REPORT_ANCHOR_BACKFILL_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_017_canoni…` |
| [DETERMINEX_CANONICAL_FAMILY_REGISTRY_ALIAS_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_CANONICAL_FAMILY_REGISTRY_ALIAS_RECONCILIATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_CANONICAL_RELEASE_SUPPORTED_CELLS_SINGLE_SOURCE_LOCK_001](../locks/sentinel/DETERMINEX_CANONICAL_RELEASE_SUPPORTED_CELLS_SINGLE_SOURCE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_016_canoni…` |
| [DETERMINEX_CANONICAL_TAXONOMY_EXPANSION_40_TO_44_LOCK_001](../locks/sentinel/DETERMINEX_CANONICAL_TAXONOMY_EXPANSION_40_TO_44_LOCK_001.json) | 25 | 25 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_canonical_taxon…` |
| [DETERMINEX_CANONICAL_TAXONOMY_EXPANSION_AND_MISSING_LANES_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_CANONICAL_TAXONOMY_EXPANSION_AND_MISSING_LANES_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_canonical_taxon…` |
| [DETERMINEX_CAPABILITY_SCORE_DELTA_GUARD_LOCK_001](../locks/sentinel/DETERMINEX_CAPABILITY_SCORE_DELTA_GUARD_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_019_execut…` |
| [DETERMINEX_CAPABILITY_SUPPORT_MATRIX_EXPANSION_SPRINT_LOCK_001](../locks/sentinel/DETERMINEX_CAPABILITY_SUPPORT_MATRIX_EXPANSION_SPRINT_LOCK_001.json) | 23 | 23 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_capability_supp…` |
| [DETERMINEX_CAPABILITY_UNIVERSE_EXHAUSTIVE_MATRIX_LOCK_001](../locks/sentinel/DETERMINEX_CAPABILITY_UNIVERSE_EXHAUSTIVE_MATRIX_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_CATHEDRAL_INDEX_FOUNDATION_LOCK_001](../locks/sentinel/DETERMINEX_CATHEDRAL_INDEX_FOUNDATION_LOCK_001.json) | 15 | 15 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_determinex_cathedr…` |
| [DETERMINEX_CHRFSF_CLAUDE_APPEND_ONLY_COUNT_DRIFT_ANTI_GOD_REVIEW_001](../locks/sentinel/DETERMINEX_CHRFSF_CLAUDE_APPEND_ONLY_COUNT_DRIFT_ANTI_GOD_REVIEW_001.json) | 1 | 1 | `f6a8393352` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_chrfsf_claude_a…` |
| [DETERMINEX_CHRFSF_CLAUDE_AUTHORITY_BATCH_GATE_REVIEW_001](../locks/sentinel/DETERMINEX_CHRFSF_CLAUDE_AUTHORITY_BATCH_GATE_REVIEW_001.json) | 1 | 1 | `f6a8393352` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_chrfsf_claude_a…` |
| [DETERMINEX_CHRFSF_CLAUDE_CLAIM_SCANNER_DAY1_OVERCLAIM_REVIEW_001](../locks/sentinel/DETERMINEX_CHRFSF_CLAUDE_CLAIM_SCANNER_DAY1_OVERCLAIM_REVIEW_001.json) | 1 | 1 | `f6a8393352` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_chrfsf_claude_c…` |
| [DETERMINEX_CHRFSF_CLAUDE_CLEAN_HOST_BLOCKER_SHARPENED_HONEST_REVIEW_001](../locks/sentinel/DETERMINEX_CHRFSF_CLAUDE_CLEAN_HOST_BLOCKER_SHARPENED_HONEST_REVIEW_001.json) | 1 | 1 | `f6a8393352` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_chrfsf_claude_c…` |
| [DETERMINEX_CHRFSF_CLAUDE_CLEAN_HOST_DEPENDENCY_CHECKS_REVIEW_001](../locks/sentinel/DETERMINEX_CHRFSF_CLAUDE_CLEAN_HOST_DEPENDENCY_CHECKS_REVIEW_001.json) | 1 | 1 | `f6a8393352` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_chrfsf_claude_c…` |
| [DETERMINEX_CHRFSF_CLAUDE_CLEAN_HOST_ENVIRONMENT_FINGERPRINT_REVIEW_001](../locks/sentinel/DETERMINEX_CHRFSF_CLAUDE_CLEAN_HOST_ENVIRONMENT_FINGERPRINT_REVIEW_001.json) | 1 | 1 | `f6a8393352` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_chrfsf_claude_c…` |
| [DETERMINEX_CHRFSF_CLAUDE_CLEAN_HOST_EXECUTION_TRANSCRIPT_REVIEW_001](../locks/sentinel/DETERMINEX_CHRFSF_CLAUDE_CLEAN_HOST_EXECUTION_TRANSCRIPT_REVIEW_001.json) | 1 | 1 | `f6a8393352` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_chrfsf_claude_c…` |
| [DETERMINEX_CHRFSF_CLAUDE_CLEAN_HOST_ONE_TIME_SPEND_REVIEW_001](../locks/sentinel/DETERMINEX_CHRFSF_CLAUDE_CLEAN_HOST_ONE_TIME_SPEND_REVIEW_001.json) | 1 | 1 | `f6a8393352` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_chrfsf_claude_c…` |
| [DETERMINEX_CHRFSF_CLAUDE_CLEAN_HOST_PACKET_REPAIR_REVIEW_001](../locks/sentinel/DETERMINEX_CHRFSF_CLAUDE_CLEAN_HOST_PACKET_REPAIR_REVIEW_001.json) | 1 | 1 | `f6a8393352` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_chrfsf_claude_c…` |
| [DETERMINEX_CHRFSF_CLAUDE_CLEAN_HOST_QUEUE_ADMISSION_REVIEW_001](../locks/sentinel/DETERMINEX_CHRFSF_CLAUDE_CLEAN_HOST_QUEUE_ADMISSION_REVIEW_001.json) | 1 | 1 | `f6a8393352` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_chrfsf_claude_c…` |
| [DETERMINEX_CHRFSF_CLAUDE_CLEAN_HOST_RELEASE_PROOF_NOT_CLAIMED_REVIEW_001](../locks/sentinel/DETERMINEX_CHRFSF_CLAUDE_CLEAN_HOST_RELEASE_PROOF_NOT_CLAIMED_REVIEW_001.json) | 1 | 1 | `f6a8393352` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_chrfsf_claude_c…` |
| [DETERMINEX_CHRFSF_CLAUDE_EVERY_NONLV_ADVANCED_OR_SHARPENED_REVIEW_001](../locks/sentinel/DETERMINEX_CHRFSF_CLAUDE_EVERY_NONLV_ADVANCED_OR_SHARPENED_REVIEW_001.json) | 1 | 1 | `f6a8393352` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_chrfsf_claude_e…` |
| [DETERMINEX_CHRFSF_CLAUDE_EVIDENCE_INDEX_CLEAN_REVIEW_001](../locks/sentinel/DETERMINEX_CHRFSF_CLAUDE_EVIDENCE_INDEX_CLEAN_REVIEW_001.json) | 1 | 1 | `f6a8393352` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_chrfsf_claude_e…` |
| [DETERMINEX_CHRFSF_CLAUDE_FAMILY_MAP_COVERAGE_REVIEW_001](../locks/sentinel/DETERMINEX_CHRFSF_CLAUDE_FAMILY_MAP_COVERAGE_REVIEW_001.json) | 1 | 1 | `f6a8393352` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_chrfsf_claude_f…` |
| [DETERMINEX_CHRFSF_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001](../locks/sentinel/DETERMINEX_CHRFSF_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001.json) | 1 | 1 | `f6a8393352` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_chrfsf_claude_f…` |
| [DETERMINEX_CHRFSF_CLAUDE_FULL_STATUS_SEGMENTED_REVIEW_001](../locks/sentinel/DETERMINEX_CHRFSF_CLAUDE_FULL_STATUS_SEGMENTED_REVIEW_001.json) | 1 | 1 | `f6a8393352` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_chrfsf_claude_f…` |
| [DETERMINEX_CHRFSF_CLAUDE_GUI_BUILD_INSTALLER_BETA_NOT_EXECUTED_REVIEW_001](../locks/sentinel/DETERMINEX_CHRFSF_CLAUDE_GUI_BUILD_INSTALLER_BETA_NOT_EXECUTED_REVIEW_001.json) | 1 | 1 | `f6a8393352` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_chrfsf_claude_g…` |
| [DETERMINEX_CHRFSF_CLAUDE_KOTLIN_SWIFT_GATE_REVIEW_001](../locks/sentinel/DETERMINEX_CHRFSF_CLAUDE_KOTLIN_SWIFT_GATE_REVIEW_001.json) | 1 | 1 | `f6a8393352` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_chrfsf_claude_k…` |
| [DETERMINEX_CHRFSF_CLAUDE_NO_FAMILY_PROMOTION_NO_SUPPORT_OVERCLAIM_REVIEW_001](../locks/sentinel/DETERMINEX_CHRFSF_CLAUDE_NO_FAMILY_PROMOTION_NO_SUPPORT_OVERCLAIM_REVIEW_001.json) | 1 | 1 | `f6a8393352` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_chrfsf_claude_n…` |
| [DETERMINEX_CHRFSF_CLAUDE_NO_PACKAGE_LOCKFILE_MUTATION_REVIEW_001](../locks/sentinel/DETERMINEX_CHRFSF_CLAUDE_NO_PACKAGE_LOCKFILE_MUTATION_REVIEW_001.json) | 1 | 1 | `f6a8393352` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_chrfsf_claude_n…` |
| [DETERMINEX_CHRFSF_CLAUDE_NO_RELEASE_READY_CLAIM_REVIEW_001](../locks/sentinel/DETERMINEX_CHRFSF_CLAUDE_NO_RELEASE_READY_CLAIM_REVIEW_001.json) | 1 | 1 | `f6a8393352` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_chrfsf_claude_n…` |
| [DETERMINEX_CHRFSF_CLAUDE_NO_TEST_OR_VERIFIER_MUTATION_REVIEW_001](../locks/sentinel/DETERMINEX_CHRFSF_CLAUDE_NO_TEST_OR_VERIFIER_MUTATION_REVIEW_001.json) | 1 | 1 | `f6a8393352` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_chrfsf_claude_n…` |
| [DETERMINEX_CHRFSF_CLAUDE_NO_UNCONTROLLED_INSTALL_REVIEW_001](../locks/sentinel/DETERMINEX_CHRFSF_CLAUDE_NO_UNCONTROLLED_INSTALL_REVIEW_001.json) | 1 | 1 | `f6a8393352` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_chrfsf_claude_n…` |
| [DETERMINEX_CHRFSF_CLAUDE_NO_UNIVERSAL_SUPPORT_CLAIM_REVIEW_001](../locks/sentinel/DETERMINEX_CHRFSF_CLAUDE_NO_UNIVERSAL_SUPPORT_CLAIM_REVIEW_001.json) | 1 | 1 | `f6a8393352` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_chrfsf_claude_n…` |
| [DETERMINEX_CHRFSF_CLAUDE_PHP_RUBY_GATE_REVIEW_001](../locks/sentinel/DETERMINEX_CHRFSF_CLAUDE_PHP_RUBY_GATE_REVIEW_001.json) | 1 | 1 | `f6a8393352` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_chrfsf_claude_p…` |
| [DETERMINEX_CHRFSF_CLAUDE_POST_EXECUTION_VERIFICATION_REVIEW_001](../locks/sentinel/DETERMINEX_CHRFSF_CLAUDE_POST_EXECUTION_VERIFICATION_REVIEW_001.json) | 1 | 1 | `f6a8393352` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_chrfsf_claude_p…` |
| [DETERMINEX_CHRFSF_CLAUDE_QUEUE_SPEND_CONSERVATION_REVIEW_001](../locks/sentinel/DETERMINEX_CHRFSF_CLAUDE_QUEUE_SPEND_CONSERVATION_REVIEW_001.json) | 1 | 1 | `f6a8393352` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_chrfsf_claude_q…` |
| [DETERMINEX_CHRFSF_CLAUDE_RELEASE_CELLS_CANONICAL_REVIEW_001](../locks/sentinel/DETERMINEX_CHRFSF_CLAUDE_RELEASE_CELLS_CANONICAL_REVIEW_001.json) | 1 | 1 | `f6a8393352` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_chrfsf_claude_r…` |
| [DETERMINEX_CHRFSF_CLAUDE_RELEASE_FAMILIES_CANONICAL_REVIEW_001](../locks/sentinel/DETERMINEX_CHRFSF_CLAUDE_RELEASE_FAMILIES_CANONICAL_REVIEW_001.json) | 1 | 1 | `f6a8393352` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_chrfsf_claude_r…` |
| [DETERMINEX_CHRFSF_CLAUDE_RUNTIME_QUEUE_SPEND_ACCURATE_REVIEW_001](../locks/sentinel/DETERMINEX_CHRFSF_CLAUDE_RUNTIME_QUEUE_SPEND_ACCURATE_REVIEW_001.json) | 1 | 1 | `f6a8393352` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_chrfsf_claude_r…` |
| [DETERMINEX_CHRFSF_CLAUDE_SBOM_BROADER_REPO_NEXT_GATE_REVIEW_001](../locks/sentinel/DETERMINEX_CHRFSF_CLAUDE_SBOM_BROADER_REPO_NEXT_GATE_REVIEW_001.json) | 1 | 1 | `f6a8393352` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_chrfsf_claude_s…` |
| [DETERMINEX_CHRFSF_CLAUDE_SBOM_CONTINUITY_INNER_WORKTREE_CRLF_REVIEW_001](../locks/sentinel/DETERMINEX_CHRFSF_CLAUDE_SBOM_CONTINUITY_INNER_WORKTREE_CRLF_REVIEW_001.json) | 1 | 1 | `f6a8393352` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_chrfsf_claude_s…` |
| [DETERMINEX_CHRFSF_CLAUDE_SBOM_CONTINUITY_MAIN_WORKTREE_REVIEW_001](../locks/sentinel/DETERMINEX_CHRFSF_CLAUDE_SBOM_CONTINUITY_MAIN_WORKTREE_REVIEW_001.json) | 1 | 1 | `f6a8393352` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_chrfsf_claude_s…` |
| [DETERMINEX_CHRFSF_CLAUDE_SCORE_MOVEMENT_ZERO_EVIDENCE_BOUND_REVIEW_001](../locks/sentinel/DETERMINEX_CHRFSF_CLAUDE_SCORE_MOVEMENT_ZERO_EVIDENCE_BOUND_REVIEW_001.json) | 1 | 1 | `f6a8393352` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_chrfsf_claude_s…` |
| [DETERMINEX_CHRFSF_CLAUDE_STRUCTURAL_FAMILY_GATE_REVIEW_001](../locks/sentinel/DETERMINEX_CHRFSF_CLAUDE_STRUCTURAL_FAMILY_GATE_REVIEW_001.json) | 1 | 1 | `f6a8393352` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_chrfsf_claude_s…` |
| [DETERMINEX_CHRFSF_CLAUDE_SYNTHESIS_REVIEW_001](../locks/sentinel/DETERMINEX_CHRFSF_CLAUDE_SYNTHESIS_REVIEW_001.json) | 1 | 1 | `f6a8393352` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_chrfsf_claude_s…` |
| [DETERMINEX_DETERMINEX_CLI_FIRST_LOCAL_INSTALL_AND_COMMAND_LOCK_001](../locks/sentinel/DETERMINEX_DETERMINEX_CLI_FIRST_LOCAL_INSTALL_AND_COMMAND_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_DETERMINEX_CLI_LOCAL_INSTALL_MOMENT_LOCK_001](../locks/sentinel/DETERMINEX_DETERMINEX_CLI_LOCAL_INSTALL_MOMENT_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_DETERMINEX_CLI_PYPI_FEASIBILITY_AND_PACKAGE_SCAFFOLD_LOCK_001](../locks/sentinel/DETERMINEX_DETERMINEX_CLI_PYPI_FEASIBILITY_AND_PACKAGE_SCAFFOLD_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_DETERMINEX_CLI_SUBPACKAGE_FEASIBILITY_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_DETERMINEX_CLI_SUBPACKAGE_FEASIBILITY_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_determinex_cli_sub…` |
| [DETERMINEX_DETERMINEX_CLOAK_FIRST_LOCAL_INSTALL_AND_FIXTURE_LOCK_001](../locks/sentinel/DETERMINEX_DETERMINEX_CLOAK_FIRST_LOCAL_INSTALL_AND_FIXTURE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_DETERMINEX_CLOAK_LOCAL_INSTALL_AND_FIXTURE_LOCK_001](../locks/sentinel/DETERMINEX_DETERMINEX_CLOAK_LOCAL_INSTALL_AND_FIXTURE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_DETERMINEX_CLOAK_SUBPACKAGE_FEASIBILITY_AND_SCAFFOLD_LOCK_001](../locks/sentinel/DETERMINEX_DETERMINEX_CLOAK_SUBPACKAGE_FEASIBILITY_AND_SCAFFOLD_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_DETERMINEX_CLOAK_SUBPACKAGE_FEASIBILITY_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_DETERMINEX_CLOAK_SUBPACKAGE_FEASIBILITY_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_determinex_cloak_s…` |
| [DETERMINEX_DETERMINEX_PROOF_REPORT_SUBPACKAGE_FEASIBILITY_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_DETERMINEX_PROOF_REPORT_SUBPACKAGE_FEASIBILITY_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_determinex_proof_r…` |
| [DETERMINEX_CLAIM_SCANNER_CI_EXPANSION_LOCK_001](../locks/sentinel/DETERMINEX_CLAIM_SCANNER_CI_EXPANSION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_019_execut…` |
| [DETERMINEX_CLASSIFIER_STATE_SAFETY_AND_PROBE_TRANSCRIPTS_LOCK_001](../locks/sentinel/DETERMINEX_CLASSIFIER_STATE_SAFETY_AND_PROBE_TRANSCRIPTS_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_015_canoni…` |
| [DETERMINEX_CLEAN_HOST_ANTI_GOD_GUARD_EXPECTED_PASS_LOCK_001](../locks/sentinel/DETERMINEX_CLEAN_HOST_ANTI_GOD_GUARD_EXPECTED_PASS_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_CLEAN_HOST_APPEND_ONLY_LEDGER_EXPECTED_PASS_GUARD_LOCK_001](../locks/sentinel/DETERMINEX_CLEAN_HOST_APPEND_ONLY_LEDGER_EXPECTED_PASS_GUARD_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_CLEAN_HOST_AUDIT_LOG_ENTRY_GUARD_LOCK_001](../locks/sentinel/DETERMINEX_CLEAN_HOST_AUDIT_LOG_ENTRY_GUARD_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_CLEAN_HOST_BETA_READINESS_BOUNDARY_GUARD_LOCK_001](../locks/sentinel/DETERMINEX_CLEAN_HOST_BETA_READINESS_BOUNDARY_GUARD_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_CLEAN_HOST_CLAIM_SCANNER_EXPECTED_PASS_GUARD_LOCK_001](../locks/sentinel/DETERMINEX_CLEAN_HOST_CLAIM_SCANNER_EXPECTED_PASS_GUARD_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_CLEAN_HOST_COUNT_DRIFT_EXPECTED_PASS_GUARD_LOCK_001](../locks/sentinel/DETERMINEX_CLEAN_HOST_COUNT_DRIFT_EXPECTED_PASS_GUARD_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_CLEAN_HOST_DAY1_OVERCLAIM_EXPECTED_PASS_GUARD_LOCK_001](../locks/sentinel/DETERMINEX_CLEAN_HOST_DAY1_OVERCLAIM_EXPECTED_PASS_GUARD_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_CLEAN_HOST_DEPENDENCY_CHECKS_GUARD_LOCK_001](../locks/sentinel/DETERMINEX_CLEAN_HOST_DEPENDENCY_CHECKS_GUARD_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_CLEAN_HOST_FAMILY_SUPPORT_BOUNDARY_GUARD_LOCK_001](../locks/sentinel/DETERMINEX_CLEAN_HOST_FAMILY_SUPPORT_BOUNDARY_GUARD_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_CLEAN_HOST_FRESH_INSTALL_RUNNER_EXECUTION_LOCK_001](../locks/sentinel/DETERMINEX_CLEAN_HOST_FRESH_INSTALL_RUNNER_EXECUTION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_CLEAN_HOST_MUTATION_BOUNDARY_GUARD_LOCK_001](../locks/sentinel/DETERMINEX_CLEAN_HOST_MUTATION_BOUNDARY_GUARD_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_CLEAN_HOST_NEXT_GATE_ESCALATION_LOCK_001](../locks/sentinel/DETERMINEX_CLEAN_HOST_NEXT_GATE_ESCALATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_CLEAN_HOST_PACKET_FIELDS_GUARD_LOCK_001](../locks/sentinel/DETERMINEX_CLEAN_HOST_PACKET_FIELDS_GUARD_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_CLEAN_HOST_PACKET_HARDENING_LOCK_001](../locks/sentinel/DETERMINEX_CLEAN_HOST_PACKET_HARDENING_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_CLEAN_HOST_PACKET_TARGET_COMMIT_GUARD_LOCK_001](../locks/sentinel/DETERMINEX_CLEAN_HOST_PACKET_TARGET_COMMIT_GUARD_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_CLEAN_HOST_QUEUE_CONSERVATION_GUARD_LOCK_001](../locks/sentinel/DETERMINEX_CLEAN_HOST_QUEUE_CONSERVATION_GUARD_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_CLEAN_HOST_RELEASE_READINESS_BOUNDARY_GUARD_LOCK_001](../locks/sentinel/DETERMINEX_CLEAN_HOST_RELEASE_READINESS_BOUNDARY_GUARD_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_CLEAN_HOST_RELEASE_REGISTRY_INVARIANT_GUARD_LOCK_001](../locks/sentinel/DETERMINEX_CLEAN_HOST_RELEASE_REGISTRY_INVARIANT_GUARD_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_CLEAN_HOST_REPO_STATUS_GUARD_LOCK_001](../locks/sentinel/DETERMINEX_CLEAN_HOST_REPO_STATUS_GUARD_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_CLEAN_HOST_ROUTE_SELECTION_AND_FIRST_EXECUTION_LOCK_001](../locks/sentinel/DETERMINEX_CLEAN_HOST_ROUTE_SELECTION_AND_FIRST_EXECUTION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_CLEAN_HOST_RUNNER_ADMISSION_AND_EXECUTION_LOCK_003](../locks/sentinel/DETERMINEX_CLEAN_HOST_RUNNER_ADMISSION_AND_EXECUTION_LOCK_003.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_014_signed…` |
| [DETERMINEX_CLEAN_HOST_RUNNER_ADMISSION_AND_FIRST_TRANSCRIPT_LOCK_004](../locks/sentinel/DETERMINEX_CLEAN_HOST_RUNNER_ADMISSION_AND_FIRST_TRANSCRIPT_LOCK_004.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_015_canoni…` |
| [DETERMINEX_CLEAN_HOST_RUNNER_DECISION_AND_FIRST_TRANSCRIPT_LOCK_001](../locks/sentinel/DETERMINEX_CLEAN_HOST_RUNNER_DECISION_AND_FIRST_TRANSCRIPT_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_CLEAN_HOST_RUNNER_IF_ADMITTED_LOCK_005](../locks/sentinel/DETERMINEX_CLEAN_HOST_RUNNER_IF_ADMITTED_LOCK_005.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_016_canoni…` |
| [DETERMINEX_CLEAN_HOST_RUNTIME_EXECUTION_LOCK_001](../locks/sentinel/DETERMINEX_CLEAN_HOST_RUNTIME_EXECUTION_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_CLEAN_HOST_RUNTIME_PACKET_FINALIZATION_LOCK_001](../locks/sentinel/DETERMINEX_CLEAN_HOST_RUNTIME_PACKET_FINALIZATION_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_CLEAN_HOST_RUNTIME_QUEUE_ADMISSION_LOCK_001](../locks/sentinel/DETERMINEX_CLEAN_HOST_RUNTIME_QUEUE_ADMISSION_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_CLEAN_HOST_RUNTIME_SCORE_RELEASE_DISCIPLINE_LOCK_001](../locks/sentinel/DETERMINEX_CLEAN_HOST_RUNTIME_SCORE_RELEASE_DISCIPLINE_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_CLEAN_HOST_RUNTIME_SIGNED_SPEND_LOCK_001](../locks/sentinel/DETERMINEX_CLEAN_HOST_RUNTIME_SIGNED_SPEND_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_CLEAN_HOST_RUNTIME_SURGE_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_CLEAN_HOST_RUNTIME_SURGE_RECONCILIATION_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_CLEAN_HOST_RUNTIME_VERIFICATION_LOCK_001](../locks/sentinel/DETERMINEX_CLEAN_HOST_RUNTIME_VERIFICATION_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_CLEAN_HOST_SBOM_CONTINUITY_GUARD_LOCK_001](../locks/sentinel/DETERMINEX_CLEAN_HOST_SBOM_CONTINUITY_GUARD_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_CLEAN_HOST_SPEND_CONSERVATION_GUARD_LOCK_001](../locks/sentinel/DETERMINEX_CLEAN_HOST_SPEND_CONSERVATION_GUARD_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_CLEAN_HOST_SPEND_REUSE_REJECTION_GUARD_LOCK_001](../locks/sentinel/DETERMINEX_CLEAN_HOST_SPEND_REUSE_REJECTION_GUARD_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_CLEAN_HOST_TRANSCRIPT_ENVIRONMENT_GUARD_LOCK_001](../locks/sentinel/DETERMINEX_CLEAN_HOST_TRANSCRIPT_ENVIRONMENT_GUARD_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_CLEAN_HOST_UNIVERSAL_SUPPORT_BOUNDARY_GUARD_LOCK_001](../locks/sentinel/DETERMINEX_CLEAN_HOST_UNIVERSAL_SUPPORT_BOUNDARY_GUARD_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_CLEAN_RUNNER_ADMISSION_AND_FIRST_TRANSCRIPT_LOCK_001](../locks/sentinel/DETERMINEX_CLEAN_RUNNER_ADMISSION_AND_FIRST_TRANSCRIPT_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_CLEAN_RUNNER_SAFE_CLONE_GIT_DIAGNOSIS_LOCK_001](../locks/sentinel/DETERMINEX_CLEAN_RUNNER_SAFE_CLONE_GIT_DIAGNOSIS_LOCK_001.json) | 21 | 21 | `pending-fi` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_runner_sa…` |
| [DETERMINEX_CLEAN_RUNNER_SAFE_CLONE_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_CLEAN_RUNNER_SAFE_CLONE_RECONCILIATION_LOCK_001.json) | 21 | 21 | `pending-fi` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_runner_sa…` |
| [DETERMINEX_CLI_LOCK_001](../locks/sentinel/DETERMINEX_CLI_LOCK_001.json) | 13 | 13 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/test_determinex_cli.py -q --tb…` |
| [DETERMINEX_CLOAK_CRYPTO_PROOF_AND_LEAK_REVIEW_LOCK_001](../locks/sentinel/DETERMINEX_CLOAK_CRYPTO_PROOF_AND_LEAK_REVIEW_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_CLOAK_DEMO_PANEL_AND_THREE_FIXTURES_LOCK_001](../locks/sentinel/DETERMINEX_CLOAK_DEMO_PANEL_AND_THREE_FIXTURES_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_CLOAK_DEMO_PANEL_PRIVACY_PROOF_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_CLOAK_DEMO_PANEL_PRIVACY_PROOF_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_cloak_demo_pane…` |
| [DETERMINEX_CLOAK_DEMO_PANEL_VISUAL_COMPONENT_PROOF_LOCK_001](../locks/sentinel/DETERMINEX_CLOAK_DEMO_PANEL_VISUAL_COMPONENT_PROOF_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_CLOAK_HASH_CHAIN_AND_LEAK_AUDIT_LOCK_001](../locks/sentinel/DETERMINEX_CLOAK_HASH_CHAIN_AND_LEAK_AUDIT_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_CLOAK_PANEL_PRIVACY_BOUNDARY_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_CLOAK_PANEL_PRIVACY_BOUNDARY_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_007_cloak_…` |
| [DETERMINEX_CLOAK_PRIVACY_DEMO_POST_CERTIFICATION_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_CLOAK_PRIVACY_DEMO_POST_CERTIFICATION_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_cloak_privacy_d…` |
| [DETERMINEX_CLOAK_PRODUCTIZATION_AND_PRIVACY_CLAIM_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_CLOAK_PRODUCTIZATION_AND_PRIVACY_CLAIM_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_cloak_productiz…` |
| [DETERMINEX_CLOAK_USER_FACING_PROOF_PATH_AND_DEMO_CELL_LOCK_001](../locks/sentinel/DETERMINEX_CLOAK_USER_FACING_PROOF_PATH_AND_DEMO_CELL_LOCK_001.json) | 16 | 16 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_cloak_user_faci…` |
| [DETERMINEX_CODEX_COMMITS_BEFORE_CLAUDE_REVIEW_PROTOCOL_LOCK_001](../locks/sentinel/DETERMINEX_CODEX_COMMITS_BEFORE_CLAUDE_REVIEW_PROTOCOL_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_CODEX_STATUS_SUBPROCESS_CLASSIFICATION_REPAIR_PLAN_LOCK_001](../locks/sentinel/DETERMINEX_CODEX_STATUS_SUBPROCESS_CLASSIFICATION_REPAIR_PLAN_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/dev/test_script_helper_exec…` |
| [DETERMINEX_CODE_SIGNING_ROUTE_AND_INSTALLER_WORDING_LINTER_LOCK_001](../locks/sentinel/DETERMINEX_CODE_SIGNING_ROUTE_AND_INSTALLER_WORDING_LINTER_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_CODE_SIGNING_SMARTSCREEN_PUBLIC_INSTALLER_TRUST_BOARD_LOCK_001](../locks/sentinel/DETERMINEX_CODE_SIGNING_SMARTSCREEN_PUBLIC_INSTALLER_TRUST_BOARD_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_COMMERCIAL_LICENSE_TRIGGER_LOCK_001](../locks/sentinel/DETERMINEX_COMMERCIAL_LICENSE_TRIGGER_LOCK_001.json) | 10 | 10 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_commercial_lice…` |
| [DETERMINEX_COMPANION_RAG_ANSWER_BOUNDARY_AND_OBSERVABILITY_LOCK_001](../locks/sentinel/DETERMINEX_COMPANION_RAG_ANSWER_BOUNDARY_AND_OBSERVABILITY_LOCK_001.json) | 34 | 34 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_companion_rag_a…` |
| [DETERMINEX_COMPANION_RAG_DESKTOP_E2E_BLOCKER_AND_OPERATOR_ROUTE_LOCK_001](../locks/sentinel/DETERMINEX_COMPANION_RAG_DESKTOP_E2E_BLOCKER_AND_OPERATOR_ROUTE_LOCK_001.json) | 30 | 1094 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_companion_rag_d…` |
| [DETERMINEX_COMPANION_RAG_DESKTOP_E2E_SMOKE_LOCK_001](../locks/sentinel/DETERMINEX_COMPANION_RAG_DESKTOP_E2E_SMOKE_LOCK_001.json) | 30 | 1064 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_companion_rag_d…` |
| [DETERMINEX_COMPANION_RAG_FIXTURE_EXPANSION_AND_PRODUCT_GATE_LOCK_001](../locks/sentinel/DETERMINEX_COMPANION_RAG_FIXTURE_EXPANSION_AND_PRODUCT_GATE_LOCK_001.json) | 13 | 13 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_companion_rag_f…` |
| [DETERMINEX_COMPANION_RAG_NON_GUI_REPORT_CELL_APPROVAL_AND_CERTIFICATION_LOCK_001](../locks/sentinel/DETERMINEX_COMPANION_RAG_NON_GUI_REPORT_CELL_APPROVAL_AND_CERTIFICATION_LOCK_001.json) | 30 | 30 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_companion_rag_n…` |
| [DETERMINEX_COMPANION_RAG_PRODUCTIZATION_AND_ANSWER_CORRECTNESS_BOUNDARY_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_COMPANION_RAG_PRODUCTIZATION_AND_ANSWER_CORRECTNESS_BOUNDARY_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_companion_rag_p…` |
| [DETERMINEX_COMPANION_RAG_PRODUCT_CELL_PREREQUISITE_GATE_LOCK_001](../locks/sentinel/DETERMINEX_COMPANION_RAG_PRODUCT_CELL_PREREQUISITE_GATE_LOCK_001.json) | 29 | 29 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_companion_rag_p…` |
| [DETERMINEX_COMPANION_RAG_PRODUCT_SMOKE_LOCK_001](../locks/sentinel/DETERMINEX_COMPANION_RAG_PRODUCT_SMOKE_LOCK_001.json) | 18 | 18 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_companion_rag_p…` |
| [DETERMINEX_COMPANION_RAG_REPORT_EXPORT_WITH_CITATIONS_LOCK_001](../locks/sentinel/DETERMINEX_COMPANION_RAG_REPORT_EXPORT_WITH_CITATIONS_LOCK_001.json) | 32 | 32 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_companion_rag_r…` |
| [DETERMINEX_COMPANION_RAG_REPORT_PANEL_VISUAL_COMPONENT_PROOF_LOCK_001](../locks/sentinel/DETERMINEX_COMPANION_RAG_REPORT_PANEL_VISUAL_COMPONENT_PROOF_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_COMPANION_RAG_SIGNED_USER_FACING_EXPORT_PROOF_LOCK_001](../locks/sentinel/DETERMINEX_COMPANION_RAG_SIGNED_USER_FACING_EXPORT_PROOF_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_COMPANION_RAG_UI_ANSWER_OBSERVABILITY_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_COMPANION_RAG_UI_ANSWER_OBSERVABILITY_BINDING_LOCK_001.json) | 33 | 33 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_companion_rag_u…` |
| [DETERMINEX_COMPANION_RAG_UI_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_COMPANION_RAG_UI_BINDING_LOCK_001.json) | 15 | 981 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_companion_rag_u…` |
| [DETERMINEX_COMPANION_SEEDER_RESOURCE_PATH_ALIGNMENT_LOCK_001](../locks/sentinel/DETERMINEX_COMPANION_SEEDER_RESOURCE_PATH_ALIGNMENT_LOCK_001.json) | 15 | 932 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_companion_seede…` |
| [DETERMINEX_COMPILER_LOOP_WAL_ATTEMPT_TRACE_RENDER_LOCK_001](../locks/sentinel/DETERMINEX_COMPILER_LOOP_WAL_ATTEMPT_TRACE_RENDER_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_COMPILER_LOOP_WAL_TRACE_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_COMPILER_LOOP_WAL_TRACE_BINDING_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_CONDITIONAL_REACT_VITE_LOCAL_VERIFICATION_LOCK_001](../locks/sentinel/DETERMINEX_CONDITIONAL_REACT_VITE_LOCAL_VERIFICATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_CONDITIONAL_REACT_VITE_SIGNATURE_IMPORT_LOCK_001](../locks/sentinel/DETERMINEX_CONDITIONAL_REACT_VITE_SIGNATURE_IMPORT_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_CONDITIONAL_REACT_VITE_SIGNED_SPEND_LOCK_001](../locks/sentinel/DETERMINEX_CONDITIONAL_REACT_VITE_SIGNED_SPEND_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_CONDITIONAL_SIGNATURE_CURRENT_STATE_RECHECK_LOCK_001](../locks/sentinel/DETERMINEX_CONDITIONAL_SIGNATURE_CURRENT_STATE_RECHECK_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_CONDITIONAL_SIGNATURE_OR_RELEASE_SUBSTRATE_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_CONDITIONAL_SIGNATURE_OR_RELEASE_SUBSTRATE_RECONCILIATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_CONDITIONAL_SIGNATURE_OR_RELEASE_SUBSTRATE_REVIEW_READY_LOCK_001](../locks/sentinel/DETERMINEX_CONDITIONAL_SIGNATURE_OR_RELEASE_SUBSTRATE_REVIEW_READY_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_CONDITIONAL_SIGNATURE_RELEASE_SUBSTRATE_SCORE_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_CONDITIONAL_SIGNATURE_RELEASE_SUBSTRATE_SCORE_RECONCILIATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_AUTHORITY_BOUNDARY_REVIEW_001](../locks/sentinel/DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_AUTHORITY_BOUNDARY_REVIEW_001.json) | 1 | 1 | `8bfbbbb108` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_conditional_sig…` |
| [DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_BETA_DASHBOARD_REVIEW_001](../locks/sentinel/DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_BETA_DASHBOARD_REVIEW_001.json) | 1 | 1 | `8bfbbbb108` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_conditional_sig…` |
| [DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_CLEAN_HOST_PACKET_HARDENING_REVIEW_001](../locks/sentinel/DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_CLEAN_HOST_PACKET_HARDENING_REVIEW_001.json) | 1 | 1 | `8bfbbbb108` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_conditional_sig…` |
| [DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_CURRENT_SOURCE_TRUTH_REVIEW_001](../locks/sentinel/DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_CURRENT_SOURCE_TRUTH_REVIEW_001.json) | 1 | 1 | `8bfbbbb108` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_conditional_sig…` |
| [DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001](../locks/sentinel/DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001.json) | 1 | 1 | `8bfbbbb108` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_conditional_sig…` |
| [DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_GUI_BUILD_PACKET_HARDENING_REVIEW_001](../locks/sentinel/DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_GUI_BUILD_PACKET_HARDENING_REVIEW_001.json) | 1 | 1 | `8bfbbbb108` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_conditional_sig…` |
| [DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_INSTALLER_RELEASE_PACKET_HARDENING_REVIEW_001](../locks/sentinel/DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_INSTALLER_RELEASE_PACKET_HARDENING_REVIEW_001.json) | 1 | 1 | `8bfbbbb108` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_conditional_sig…` |
| [DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_MARKER_HASH_STABILITY_REVIEW_001](../locks/sentinel/DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_MARKER_HASH_STABILITY_REVIEW_001.json) | 1 | 1 | `8bfbbbb108` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_conditional_sig…` |
| [DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_OPERATOR_ACTION_PACKET_REVIEW_001](../locks/sentinel/DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_OPERATOR_ACTION_PACKET_REVIEW_001.json) | 1 | 1 | `8bfbbbb108` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_conditional_sig…` |
| [DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_QUEUE_COUNT_REVIEW_001](../locks/sentinel/DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_QUEUE_COUNT_REVIEW_001.json) | 1 | 1 | `8bfbbbb108` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_conditional_sig…` |
| [DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_REACT_VITE_SPEND_VERIFY_REVIEW_001](../locks/sentinel/DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_REACT_VITE_SPEND_VERIFY_REVIEW_001.json) | 1 | 1 | `8bfbbbb108` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_conditional_sig…` |
| [DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_SBOM_PACKET_HARDENING_REVIEW_001](../locks/sentinel/DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_SBOM_PACKET_HARDENING_REVIEW_001.json) | 1 | 1 | `8bfbbbb108` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_conditional_sig…` |
| [DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_SCORE_MOVEMENT_REVIEW_001](../locks/sentinel/DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_SCORE_MOVEMENT_REVIEW_001.json) | 1 | 1 | `8bfbbbb108` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_conditional_sig…` |
| [DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_SIGNATURE_SCAN_IMPORT_REVIEW_001](../locks/sentinel/DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_SIGNATURE_SCAN_IMPORT_REVIEW_001.json) | 1 | 1 | `8bfbbbb108` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_conditional_sig…` |
| [DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_SPEND_COUNT_REVIEW_001](../locks/sentinel/DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_SPEND_COUNT_REVIEW_001.json) | 1 | 1 | `8bfbbbb108` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_conditional_sig…` |
| [DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_SYNTHESIS_REVIEW_001](../locks/sentinel/DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_SYNTHESIS_REVIEW_001.json) | 1 | 1 | `8bfbbbb108` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_conditional_sig…` |
| [DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_TIMER_REVIEW_001](../locks/sentinel/DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_TIMER_REVIEW_001.json) | 1 | 1 | `8bfbbbb108` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_conditional_sig…` |
| [DETERMINEX_CONTRACT_CONSUMPTION_RECEIPT_PER_WAVE_LOCK_001](../locks/sentinel/DETERMINEX_CONTRACT_CONSUMPTION_RECEIPT_PER_WAVE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_contract_consum…` |
| [DETERMINEX_COST_LOCAL_COMPUTE_AND_SETUP_DISCLOSURE_POLICY_LOCK_001](../locks/sentinel/DETERMINEX_COST_LOCAL_COMPUTE_AND_SETUP_DISCLOSURE_POLICY_LOCK_001.json) | 17 | 17 | `cd3a6d5322` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_determinex_unified…` |
| [DETERMINEX_CROSS_LANE_AUTHORITY_BOUNDARY_LOCK_001](../locks/sentinel/DETERMINEX_CROSS_LANE_AUTHORITY_BOUNDARY_LOCK_001.json) | 5 | 5 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_determinex_cross_l…` |
| [DETERMINEX_CRSBST_CLAUDE_APPEND_ONLY_COUNT_DRIFT_ANTI_GOD_REVIEW_001](../locks/sentinel/DETERMINEX_CRSBST_CLAUDE_APPEND_ONLY_COUNT_DRIFT_ANTI_GOD_REVIEW_001.json) | 1 | 1 | `e9cbd8b5ad` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_crsbst_claude_a…` |
| [DETERMINEX_CRSBST_CLAUDE_BROADER_REPO_SBOM_BLOCKER_SHARPENED_REVIEW_001](../locks/sentinel/DETERMINEX_CRSBST_CLAUDE_BROADER_REPO_SBOM_BLOCKER_SHARPENED_REVIEW_001.json) | 1 | 1 | `e9cbd8b5ad` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_crsbst_claude_b…` |
| [DETERMINEX_CRSBST_CLAUDE_BROADER_REPO_SBOM_PACKET_ADMISSION_REVIEW_001](../locks/sentinel/DETERMINEX_CRSBST_CLAUDE_BROADER_REPO_SBOM_PACKET_ADMISSION_REVIEW_001.json) | 1 | 1 | `e9cbd8b5ad` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_crsbst_claude_b…` |
| [DETERMINEX_CRSBST_CLAUDE_BROWSER_TAURI_HARNESS_PACKETS_REVIEW_001](../locks/sentinel/DETERMINEX_CRSBST_CLAUDE_BROWSER_TAURI_HARNESS_PACKETS_REVIEW_001.json) | 1 | 1 | `e9cbd8b5ad` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_crsbst_claude_b…` |
| [DETERMINEX_CRSBST_CLAUDE_CLAIM_SCANNER_DAY1_OVERCLAIM_REVIEW_001](../locks/sentinel/DETERMINEX_CRSBST_CLAUDE_CLAIM_SCANNER_DAY1_OVERCLAIM_REVIEW_001.json) | 1 | 1 | `e9cbd8b5ad` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_crsbst_claude_c…` |
| [DETERMINEX_CRSBST_CLAUDE_CLEAN_RUNNER_BLOCKER_REDUCED_HONEST_REVIEW_001](../locks/sentinel/DETERMINEX_CRSBST_CLAUDE_CLEAN_RUNNER_BLOCKER_REDUCED_HONEST_REVIEW_001.json) | 1 | 1 | `e9cbd8b5ad` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_crsbst_claude_c…` |
| [DETERMINEX_CRSBST_CLAUDE_CLEAN_RUNNER_GIT_BLOCKER_DIAGNOSIS_REVIEW_001](../locks/sentinel/DETERMINEX_CRSBST_CLAUDE_CLEAN_RUNNER_GIT_BLOCKER_DIAGNOSIS_REVIEW_001.json) | 1 | 1 | `e9cbd8b5ad` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_crsbst_claude_c…` |
| [DETERMINEX_CRSBST_CLAUDE_CLEAN_RUNNER_RETRY_EXECUTION_REVIEW_001](../locks/sentinel/DETERMINEX_CRSBST_CLAUDE_CLEAN_RUNNER_RETRY_EXECUTION_REVIEW_001.json) | 1 | 1 | `e9cbd8b5ad` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_crsbst_claude_c…` |
| [DETERMINEX_CRSBST_CLAUDE_CLEAN_RUNNER_RETRY_ONE_TIME_SPEND_REVIEW_001](../locks/sentinel/DETERMINEX_CRSBST_CLAUDE_CLEAN_RUNNER_RETRY_ONE_TIME_SPEND_REVIEW_001.json) | 1 | 1 | `e9cbd8b5ad` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_crsbst_claude_c…` |
| [DETERMINEX_CRSBST_CLAUDE_CLEAN_RUNNER_RETRY_PACKET_VALIDATION_REVIEW_001](../locks/sentinel/DETERMINEX_CRSBST_CLAUDE_CLEAN_RUNNER_RETRY_PACKET_VALIDATION_REVIEW_001.json) | 1 | 1 | `e9cbd8b5ad` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_crsbst_claude_c…` |
| [DETERMINEX_CRSBST_CLAUDE_EVIDENCE_PATH_INTEGRITY_REVIEW_001](../locks/sentinel/DETERMINEX_CRSBST_CLAUDE_EVIDENCE_PATH_INTEGRITY_REVIEW_001.json) | 1 | 1 | `e9cbd8b5ad` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_crsbst_claude_e…` |
| [DETERMINEX_CRSBST_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001](../locks/sentinel/DETERMINEX_CRSBST_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001.json) | 1 | 1 | `e9cbd8b5ad` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_crsbst_claude_f…` |
| [DETERMINEX_CRSBST_CLAUDE_FULL_STATUS_NOT_RUN_HONEST_REVIEW_001](../locks/sentinel/DETERMINEX_CRSBST_CLAUDE_FULL_STATUS_NOT_RUN_HONEST_REVIEW_001.json) | 1 | 1 | `e9cbd8b5ad` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_crsbst_claude_f…` |
| [DETERMINEX_CRSBST_CLAUDE_GUI_BUILD_INSTALLER_BETA_NOT_EXECUTED_REVIEW_001](../locks/sentinel/DETERMINEX_CRSBST_CLAUDE_GUI_BUILD_INSTALLER_BETA_NOT_EXECUTED_REVIEW_001.json) | 1 | 1 | `e9cbd8b5ad` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_crsbst_claude_g…` |
| [DETERMINEX_CRSBST_CLAUDE_HIGH_RISK_GATES_UNCHANGED_REVIEW_001](../locks/sentinel/DETERMINEX_CRSBST_CLAUDE_HIGH_RISK_GATES_UNCHANGED_REVIEW_001.json) | 1 | 1 | `e9cbd8b5ad` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_crsbst_claude_h…` |
| [DETERMINEX_CRSBST_CLAUDE_KNOWN_WORLD_DETECTOR_SEGMENT_1_REVIEW_001](../locks/sentinel/DETERMINEX_CRSBST_CLAUDE_KNOWN_WORLD_DETECTOR_SEGMENT_1_REVIEW_001.json) | 1 | 1 | `e9cbd8b5ad` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_crsbst_claude_k…` |
| [DETERMINEX_CRSBST_CLAUDE_KNOWN_WORLD_REGISTRY_STILL_ACCOUNTING_REVIEW_001](../locks/sentinel/DETERMINEX_CRSBST_CLAUDE_KNOWN_WORLD_REGISTRY_STILL_ACCOUNTING_REVIEW_001.json) | 1 | 1 | `e9cbd8b5ad` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_crsbst_claude_k…` |
| [DETERMINEX_CRSBST_CLAUDE_NO_C_PATH_MOVED_NO_DELETION_REVIEW_001](../locks/sentinel/DETERMINEX_CRSBST_CLAUDE_NO_C_PATH_MOVED_NO_DELETION_REVIEW_001.json) | 1 | 1 | `e9cbd8b5ad` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_crsbst_claude_n…` |
| [DETERMINEX_CRSBST_CLAUDE_NO_FAMILY_PROMOTION_NO_OVERCLAIM_REVIEW_001](../locks/sentinel/DETERMINEX_CRSBST_CLAUDE_NO_FAMILY_PROMOTION_NO_OVERCLAIM_REVIEW_001.json) | 1 | 1 | `e9cbd8b5ad` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_crsbst_claude_n…` |
| [DETERMINEX_CRSBST_CLAUDE_NO_RELEASE_READY_NO_BETA_NO_INSTALLER_CLAIM_REVIEW_001](../locks/sentinel/DETERMINEX_CRSBST_CLAUDE_NO_RELEASE_READY_NO_BETA_NO_INSTALLER_CLAIM_REVIEW_001.json) | 1 | 1 | `e9cbd8b5ad` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_crsbst_claude_n…` |
| [DETERMINEX_CRSBST_CLAUDE_NO_SILENT_HASH_MISMATCH_REVIEW_001](../locks/sentinel/DETERMINEX_CRSBST_CLAUDE_NO_SILENT_HASH_MISMATCH_REVIEW_001.json) | 1 | 1 | `e9cbd8b5ad` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_crsbst_claude_n…` |
| [DETERMINEX_CRSBST_CLAUDE_NO_TEST_VERIFIER_LOCKFILE_MUTATION_REVIEW_001](../locks/sentinel/DETERMINEX_CRSBST_CLAUDE_NO_TEST_VERIFIER_LOCKFILE_MUTATION_REVIEW_001.json) | 1 | 1 | `e9cbd8b5ad` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_crsbst_claude_n…` |
| [DETERMINEX_CRSBST_CLAUDE_PHP_RUBY_GATES_UNCHANGED_REVIEW_001](../locks/sentinel/DETERMINEX_CRSBST_CLAUDE_PHP_RUBY_GATES_UNCHANGED_REVIEW_001.json) | 1 | 1 | `e9cbd8b5ad` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_crsbst_claude_p…` |
| [DETERMINEX_CRSBST_CLAUDE_QUEUE_SPEND_CONSERVATION_REVIEW_001](../locks/sentinel/DETERMINEX_CRSBST_CLAUDE_QUEUE_SPEND_CONSERVATION_REVIEW_001.json) | 1 | 1 | `e9cbd8b5ad` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_crsbst_claude_q…` |
| [DETERMINEX_CRSBST_CLAUDE_RELEASE_CELLS_CANONICAL_REVIEW_001](../locks/sentinel/DETERMINEX_CRSBST_CLAUDE_RELEASE_CELLS_CANONICAL_REVIEW_001.json) | 1 | 1 | `e9cbd8b5ad` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_crsbst_claude_r…` |
| [DETERMINEX_CRSBST_CLAUDE_RELEASE_FAMILIES_CANONICAL_REVIEW_001](../locks/sentinel/DETERMINEX_CRSBST_CLAUDE_RELEASE_FAMILIES_CANONICAL_REVIEW_001.json) | 1 | 1 | `e9cbd8b5ad` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_crsbst_claude_r…` |
| [DETERMINEX_CRSBST_CLAUDE_REMAINING_NLV_FAMILIES_REVIEW_001](../locks/sentinel/DETERMINEX_CRSBST_CLAUDE_REMAINING_NLV_FAMILIES_REVIEW_001.json) | 1 | 1 | `e9cbd8b5ad` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_crsbst_claude_r…` |
| [DETERMINEX_CRSBST_CLAUDE_RUNNER_CONTEXT_DISTINCT_REVIEW_001](../locks/sentinel/DETERMINEX_CRSBST_CLAUDE_RUNNER_CONTEXT_DISTINCT_REVIEW_001.json) | 1 | 1 | `e9cbd8b5ad` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_crsbst_claude_r…` |
| [DETERMINEX_CRSBST_CLAUDE_RUNNER_SAFE_CLONE_POLICY_REVIEW_001](../locks/sentinel/DETERMINEX_CRSBST_CLAUDE_RUNNER_SAFE_CLONE_POLICY_REVIEW_001.json) | 1 | 1 | `e9cbd8b5ad` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_crsbst_claude_r…` |
| [DETERMINEX_CRSBST_CLAUDE_SAFE_DIRECTORY_SCOPED_NOT_GLOBAL_REVIEW_001](../locks/sentinel/DETERMINEX_CRSBST_CLAUDE_SAFE_DIRECTORY_SCOPED_NOT_GLOBAL_REVIEW_001.json) | 1 | 1 | `e9cbd8b5ad` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_crsbst_claude_s…` |
| [DETERMINEX_CRSBST_CLAUDE_SBOM_BYTE_EXACT_MISMATCH_DIAGNOSIS_REVIEW_001](../locks/sentinel/DETERMINEX_CRSBST_CLAUDE_SBOM_BYTE_EXACT_MISMATCH_DIAGNOSIS_REVIEW_001.json) | 1 | 1 | `e9cbd8b5ad` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_crsbst_claude_s…` |
| [DETERMINEX_CRSBST_CLAUDE_SBOM_FRONTEND_CONTINUITY_REVIEW_001](../locks/sentinel/DETERMINEX_CRSBST_CLAUDE_SBOM_FRONTEND_CONTINUITY_REVIEW_001.json) | 1 | 1 | `e9cbd8b5ad` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_crsbst_claude_s…` |
| [DETERMINEX_CRSBST_CLAUDE_SCORE_OPEN_AVAILABILITY_MOVED_EVIDENCE_BOUND_REVIEW_001](../locks/sentinel/DETERMINEX_CRSBST_CLAUDE_SCORE_OPEN_AVAILABILITY_MOVED_EVIDENCE_BOUND_REVIEW_001.json) | 1 | 1 | `e9cbd8b5ad` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_crsbst_claude_s…` |
| [DETERMINEX_CRSBST_CLAUDE_SYNTHESIS_REVIEW_001](../locks/sentinel/DETERMINEX_CRSBST_CLAUDE_SYNTHESIS_REVIEW_001.json) | 1 | 1 | `e9cbd8b5ad` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_crsbst_claude_s…` |
| [DETERMINEX_CRSBST_CLAUDE_T_DRIVE_RELOCATION_PACKETS_PREPARED_REVIEW_001](../locks/sentinel/DETERMINEX_CRSBST_CLAUDE_T_DRIVE_RELOCATION_PACKETS_PREPARED_REVIEW_001.json) | 1 | 1 | `e9cbd8b5ad` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_crsbst_claude_t…` |
| [DETERMINEX_CURRENT_STATE_SOURCE_TRUTH_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_CURRENT_STATE_SOURCE_TRUTH_RECONCILIATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_under…` |
| [DETERMINEX_DAY1_IDE_DASHBOARD_COMPLETION_LOCK_001](../locks/sentinel/DETERMINEX_DAY1_IDE_DASHBOARD_COMPLETION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_under…` |
| [DETERMINEX_DAY1_OVERCLAIM_SCANNER_HARDENING_LOCK_001](../locks/sentinel/DETERMINEX_DAY1_OVERCLAIM_SCANNER_HARDENING_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_under…` |
| [DETERMINEX_DAY1_STRUCTURAL_COVERAGE_DASHBOARD_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_DAY1_STRUCTURAL_COVERAGE_DASHBOARD_BINDING_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_DAY1_STRUCTURAL_DASHBOARD_RENDERED_LOCK_001](../locks/sentinel/DETERMINEX_DAY1_STRUCTURAL_DASHBOARD_RENDERED_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_DAY_ONE_CLAIM_SCANNER_AND_SAFE_SHOCK_TEMPLATE_LOCK_001](../locks/sentinel/DETERMINEX_DAY_ONE_CLAIM_SCANNER_AND_SAFE_SHOCK_TEMPLATE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_DAY_ONE_CLAIM_SCANNER_CI_ENFORCEMENT_LOCK_001](../locks/sentinel/DETERMINEX_DAY_ONE_CLAIM_SCANNER_CI_ENFORCEMENT_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_DAY_ONE_PUBLIC_CLAIM_REMEDIATION_APPLY_LOCK_001](../locks/sentinel/DETERMINEX_DAY_ONE_PUBLIC_CLAIM_REMEDIATION_APPLY_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_day_one_public_…` |
| [DETERMINEX_DAY_ONE_PUBLIC_CLAIM_SCANNER_LOCK_001](../locks/sentinel/DETERMINEX_DAY_ONE_PUBLIC_CLAIM_SCANNER_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_day_one_public_…` |
| [DETERMINEX_DEPENDENCY_BLOCKER_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_DEPENDENCY_BLOCKER_RECONCILIATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_dependency_bloc…` |
| [DETERMINEX_DESKTOP_COCKPIT_GUI_E2E_REALITY_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_DESKTOP_COCKPIT_GUI_E2E_REALITY_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_desktop_cockpit…` |
| [DETERMINEX_DESKTOP_FIRST_PAINT_AFTER_DRIVER_ADMISSION_LOCK_001](../locks/sentinel/DETERMINEX_DESKTOP_FIRST_PAINT_AFTER_DRIVER_ADMISSION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_DESKTOP_GUI_E2E_AND_COCKPIT_REALITY_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_DESKTOP_GUI_E2E_AND_COCKPIT_REALITY_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_desktop_gui_e2e…` |
| [DETERMINEX_DESKTOP_GUI_E2E_DRIVER_ADMISSION_AND_BOUNDED_PROOF_LOCK_001](../locks/sentinel/DETERMINEX_DESKTOP_GUI_E2E_DRIVER_ADMISSION_AND_BOUNDED_PROOF_LOCK_001.json) | 28 | 28 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_desktop_gui_e2e…` |
| [DETERMINEX_DETECTOR_CLASSIFIER_FIXTURE_CI_BACKFILL_LOCK_001](../locks/sentinel/DETERMINEX_DETECTOR_CLASSIFIER_FIXTURE_CI_BACKFILL_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_016_canoni…` |
| [DETERMINEX_DETECTOR_FIXTURE_CORPUS_AND_CI_ASSERTION_LOCK_001](../locks/sentinel/DETERMINEX_DETECTOR_FIXTURE_CORPUS_AND_CI_ASSERTION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_014_signed…` |
| [DETERMINEX_DETECTOR_FIXTURE_CORPUS_CI_HARDENING_LOCK_002](../locks/sentinel/DETERMINEX_DETECTOR_FIXTURE_CORPUS_CI_HARDENING_LOCK_002.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_015_canoni…` |
| [DETERMINEX_DETECTOR_FOUR_STATE_TOOLCHAIN_CLASSIFIER_LOCK_001](../locks/sentinel/DETERMINEX_DETECTOR_FOUR_STATE_TOOLCHAIN_CLASSIFIER_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_DETECTOR_RUNTIME_PROBE_IMPLEMENTATION_LOCK_001](../locks/sentinel/DETERMINEX_DETECTOR_RUNTIME_PROBE_IMPLEMENTATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_DOCS_STATIC_CELL_SMOKE_PROOF_LOCK_001](../locks/sentinel/DETERMINEX_DOCS_STATIC_CELL_SMOKE_PROOF_LOCK_001.json) | 34 | 34 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_docs_static_cel…` |
| [DETERMINEX_DOCS_STATIC_FIRST_RELEASE_SUPPORTED_CELL_CERTIFICATION_LOCK_001](../locks/sentinel/DETERMINEX_DOCS_STATIC_FIRST_RELEASE_SUPPORTED_CELL_CERTIFICATION_LOCK_001.json) | 38 | 38 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_docs_static_fir…` |
| [DETERMINEX_DOCS_STATIC_FIRST_RELEASE_SUPPORTED_CELL_CERTIFICATION_RETRY_LOCK_001](../locks/sentinel/DETERMINEX_DOCS_STATIC_FIRST_RELEASE_SUPPORTED_CELL_CERTIFICATION_RETRY_LOCK_001.json) | 34 | 34 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_docs_static_fir…` |
| [DETERMINEX_DOCS_STATIC_LINK_CHECK_AND_VERIFIER_LOCK_001](../locks/sentinel/DETERMINEX_DOCS_STATIC_LINK_CHECK_AND_VERIFIER_LOCK_001.json) | 40 | 40 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_docs_static_lin…` |
| [DETERMINEX_DOCS_STATIC_OPERATOR_APPROVAL_RECORD_LOCK_001](../locks/sentinel/DETERMINEX_DOCS_STATIC_OPERATOR_APPROVAL_RECORD_LOCK_001.json) | 30 | 30 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_docs_static_ope…` |
| [DETERMINEX_DOCS_STATIC_RELEASE_SUPPORTED_CELL_PREREQUISITE_LOCK_001](../locks/sentinel/DETERMINEX_DOCS_STATIC_RELEASE_SUPPORTED_CELL_PREREQUISITE_LOCK_001.json) | 34 | 34 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_docs_static_rel…` |
| [DETERMINEX_DRY_RUN_INSTALL_MISLABEL_KILL_SWITCH_LOCK_001](../locks/sentinel/DETERMINEX_DRY_RUN_INSTALL_MISLABEL_KILL_SWITCH_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_DRY_RUN_SIGNATURE_IMPORT_LOCK_001](../locks/sentinel/DETERMINEX_DRY_RUN_SIGNATURE_IMPORT_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_signature_deliv…` |
| [DETERMINEX_EMBEDDED_HARDWARE_AUTHORITY_GATE_LOCK_001](../locks/sentinel/DETERMINEX_EMBEDDED_HARDWARE_AUTHORITY_GATE_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_ENVISIONED_IDE_CAPABILITY_COMPLETION_MAP_LOCK_001](../locks/sentinel/DETERMINEX_ENVISIONED_IDE_CAPABILITY_COMPLETION_MAP_LOCK_001.json) | 42 | 42 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_envisioned_ide_…` |
| [DETERMINEX_ENVISIONED_IDE_COMPLETION_CLAUDE_CRITIQUE_AND_QUEUE_001](../locks/sentinel/DETERMINEX_ENVISIONED_IDE_COMPLETION_CLAUDE_CRITIQUE_AND_QUEUE_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_envisioned_ide_…` |
| [DETERMINEX_EVIDENCE_COUNT_DRIFT_GUARD_LOCK_001](../locks/sentinel/DETERMINEX_EVIDENCE_COUNT_DRIFT_GUARD_LOCK_001.json) | 5 | 5 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/proof/test_determinex_evidence…` |
| [DETERMINEX_EXACT_CELL_PROMOTION_GATE_EXPANSION_LOCK_001](../locks/sentinel/DETERMINEX_EXACT_CELL_PROMOTION_GATE_EXPANSION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_EXACT_CELL_PROMOTION_REQUIRES_LADDER_AND_VERIFIER_SIGNOFF_LOCK_001](../locks/sentinel/DETERMINEX_EXACT_CELL_PROMOTION_REQUIRES_LADDER_AND_VERIFIER_SIGNOFF_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_EXISTING_CAPABILITY_HARVEST_LOCK_001](../locks/sentinel/DETERMINEX_EXISTING_CAPABILITY_HARVEST_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_determinex_univers…` |
| [DETERMINEX_EXTERNAL_AUTHORITY_HARD_FLOOR_UNLOCK_PACKET_LOCK_001](../locks/sentinel/DETERMINEX_EXTERNAL_AUTHORITY_HARD_FLOOR_UNLOCK_PACKET_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_under…` |
| [DETERMINEX_EXTERNAL_AUTHORITY_TRACK_CARRY_LOCK_001](../locks/sentinel/DETERMINEX_EXTERNAL_AUTHORITY_TRACK_CARRY_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_EXTERNAL_AUTHORITY_UNLOCK_PLAN_LOCK_001](../locks/sentinel/DETERMINEX_EXTERNAL_AUTHORITY_UNLOCK_PLAN_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_FAMILY_READINESS_MATRIX_AND_GATE_DEFINITION_LOCK_001](../locks/sentinel/DETERMINEX_FAMILY_READINESS_MATRIX_AND_GATE_DEFINITION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_018_canoni…` |
| [DETERMINEX_FAMILY_SUPPORT_GATE_DEFINITION_AND_CI_INVARIANT_LOCK_001](../locks/sentinel/DETERMINEX_FAMILY_SUPPORT_GATE_DEFINITION_AND_CI_INVARIANT_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_019_execut…` |
| [DETERMINEX_FAMILY_SUPPORT_READINESS_MATRIX_LOCK_001](../locks/sentinel/DETERMINEX_FAMILY_SUPPORT_READINESS_MATRIX_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_017_canoni…` |
| [DETERMINEX_FASTEMBED_MODEL_ASSET_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_FASTEMBED_MODEL_ASSET_BINDING_LOCK_001.json) | 12 | 880 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_fastembed_model…` |
| [DETERMINEX_FINAL_OMG_DEMO_PROOF_EXPORT_ATTEMPT_LOCK_001](../locks/sentinel/DETERMINEX_FINAL_OMG_DEMO_PROOF_EXPORT_ATTEMPT_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_final_omg_demo_…` |
| [DETERMINEX_FIRST_AUTHORITY_SPEND_AND_BASELINE_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_FIRST_AUTHORITY_SPEND_AND_BASELINE_RECONCILIATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_first_authority…` |
| [DETERMINEX_FIRST_CLEAN_HOST_TRANSCRIPT_IF_RUNNER_ADMITTED_LOCK_001](../locks/sentinel/DETERMINEX_FIRST_CLEAN_HOST_TRANSCRIPT_IF_RUNNER_ADMITTED_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_019_execut…` |
| [DETERMINEX_FIRST_EXACT_SUPPORT_DEPTH_PROMOTION_ATTEMPT_LOCK_001](../locks/sentinel/DETERMINEX_FIRST_EXACT_SUPPORT_DEPTH_PROMOTION_ATTEMPT_LOCK_001.json) | 30 | 30 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_first_exact_sup…` |
| [DETERMINEX_FIRST_FAMILY_SUPPORT_PROMOTION_ELIGIBILITY_REVIEW_LOCK_001](../locks/sentinel/DETERMINEX_FIRST_FAMILY_SUPPORT_PROMOTION_ELIGIBILITY_REVIEW_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_first_authority…` |
| [DETERMINEX_FIRST_GUI_VISUAL_PROOF_IF_APPROVED_LOCK_001](../locks/sentinel/DETERMINEX_FIRST_GUI_VISUAL_PROOF_IF_APPROVED_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_019_execut…` |
| [DETERMINEX_FIRST_REACT_VITE_SIGNED_SPEND_LOCK_001](../locks/sentinel/DETERMINEX_FIRST_REACT_VITE_SIGNED_SPEND_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_real_signature_…` |
| [DETERMINEX_FIRST_REAL_SIGNATURE_BOUNDED_GUI_LAUNCH_LOCK_001](../locks/sentinel/DETERMINEX_FIRST_REAL_SIGNATURE_BOUNDED_GUI_LAUNCH_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_FIRST_REAL_SIGNATURE_IMPORT_AND_SPEND_IF_PRESENT_LOCK_001](../locks/sentinel/DETERMINEX_FIRST_REAL_SIGNATURE_IMPORT_AND_SPEND_IF_PRESENT_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_019_execut…` |
| [DETERMINEX_FIRST_REAL_SIGNATURE_MSEDGEDRIVER_DOWNLOAD_ADMISSION_LOCK_001](../locks/sentinel/DETERMINEX_FIRST_REAL_SIGNATURE_MSEDGEDRIVER_DOWNLOAD_ADMISSION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_FIRST_REAL_SIGNATURE_NSIS_INSTALL_LAUNCH_UNINSTALL_LOCK_001](../locks/sentinel/DETERMINEX_FIRST_REAL_SIGNATURE_NSIS_INSTALL_LAUNCH_UNINSTALL_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_FIRST_REAL_SIGNATURE_SPEND_IF_PRESENT_LOCK_001](../locks/sentinel/DETERMINEX_FIRST_REAL_SIGNATURE_SPEND_IF_PRESENT_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_016_canoni…` |
| [DETERMINEX_FIRST_REAL_SIGNATURE_SYFT_SBOM_TOOL_ADMISSION_LOCK_001](../locks/sentinel/DETERMINEX_FIRST_REAL_SIGNATURE_SYFT_SBOM_TOOL_ADMISSION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_FIRST_RUN_INSTALL_AND_DEMO_BUNDLE_PROOF_LOCK_001](../locks/sentinel/DETERMINEX_FIRST_RUN_INSTALL_AND_DEMO_BUNDLE_PROOF_LOCK_001.json) | 12 | 12 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_first_run_insta…` |
| [DETERMINEX_FIRST_SBOM_ARTIFACT_IF_SYFT_ADMITTED_LOCK_001](../locks/sentinel/DETERMINEX_FIRST_SBOM_ARTIFACT_IF_SYFT_ADMITTED_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_019_execut…` |
| [DETERMINEX_FIRST_SBOM_ARTIFACT_IF_TOOL_ADMITTED_LOCK_006](../locks/sentinel/DETERMINEX_FIRST_SBOM_ARTIFACT_IF_TOOL_ADMITTED_LOCK_006.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_016_canoni…` |
| [DETERMINEX_FIRST_SBOM_OR_EXACT_TOOL_ADMISSION_PACKET_LOCK_001](../locks/sentinel/DETERMINEX_FIRST_SBOM_OR_EXACT_TOOL_ADMISSION_PACKET_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_FIRST_SBOM_TOOL_ADMISSION_AND_ARTIFACT_LOCK_005](../locks/sentinel/DETERMINEX_FIRST_SBOM_TOOL_ADMISSION_AND_ARTIFACT_LOCK_005.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_015_canoni…` |
| [DETERMINEX_FIRST_SBOM_TOOL_ADMISSION_AND_EMISSION_LOCK_004](../locks/sentinel/DETERMINEX_FIRST_SBOM_TOOL_ADMISSION_AND_EMISSION_LOCK_004.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_014_signed…` |
| [DETERMINEX_FIRST_SIGNATURE_SPEND_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_FIRST_SIGNATURE_SPEND_RECONCILIATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_signature_spend…` |
| [DETERMINEX_FIRST_SIGNED_AUTHORITY_SPEND_REACT_VITE_DEPENDENCY_ADMISSION_LOCK_001](../locks/sentinel/DETERMINEX_FIRST_SIGNED_AUTHORITY_SPEND_REACT_VITE_DEPENDENCY_ADMISSION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_first_authority…` |
| [DETERMINEX_FIRST_SIGNED_AUTHORITY_SPEND_REACT_VITE_LOCK_001](../locks/sentinel/DETERMINEX_FIRST_SIGNED_AUTHORITY_SPEND_REACT_VITE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_signature_spend…` |
| [DETERMINEX_FIRST_USER_VISIBLE_IDE_WORKFLOW_PROOF_CANDIDATE_LOCK_001](../locks/sentinel/DETERMINEX_FIRST_USER_VISIBLE_IDE_WORKFLOW_PROOF_CANDIDATE_LOCK_001.json) | 38 | 38 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_first_user_visi…` |
| [DETERMINEX_FIXTURE_ADMISSION_PIPELINE_LOCK_001](../locks/sentinel/DETERMINEX_FIXTURE_ADMISSION_PIPELINE_LOCK_001.json) | 18 | 18 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_fixture_admissi…` |
| [DETERMINEX_FIXTURE_FACTORY_SEED_LOCK_001](../locks/sentinel/DETERMINEX_FIXTURE_FACTORY_SEED_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_determinex_univers…` |
| [DETERMINEX_FIX_BROKEN_CANONICAL_CELL_PROOF_ANCHOR_LOCK_001](../locks/sentinel/DETERMINEX_FIX_BROKEN_CANONICAL_CELL_PROOF_ANCHOR_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_018_canoni…` |
| [DETERMINEX_FRESH_CLONE_BOOTSTRAP_PROOF_LOCK_001](../locks/sentinel/DETERMINEX_FRESH_CLONE_BOOTSTRAP_PROOF_LOCK_001.json) | 24 | 24 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_fresh_clone_boo…` |
| [DETERMINEX_FRESH_CLONE_BOOTSTRAP_PROOF_RETRY_LOCK_001](../locks/sentinel/DETERMINEX_FRESH_CLONE_BOOTSTRAP_PROOF_RETRY_LOCK_001.json) | 36 | 36 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_fresh_clone_boo…` |
| [DETERMINEX_FRESH_INSTALL_PROOF_PATH_SPLIT_LOCK_001](../locks/sentinel/DETERMINEX_FRESH_INSTALL_PROOF_PATH_SPLIT_LOCK_001.json) | 21 | 21 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_fresh_install_p…` |
| [DETERMINEX_FULL_STATUS_SEGMENTATION_REPAIR_LOCK_001](../locks/sentinel/DETERMINEX_FULL_STATUS_SEGMENTATION_REPAIR_LOCK_001.json) | 18 | 1 | `e4ff17592c` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_admitted_clean_…` |
| [DETERMINEX_FULL_STATUS_SEGMENTED_TIMING_REPAIR_LOCK_001](../locks/sentinel/DETERMINEX_FULL_STATUS_SEGMENTED_TIMING_REPAIR_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_FULL_STATUS_TIMEOUT_DIAGNOSTIC_LOCK_001](../locks/sentinel/DETERMINEX_FULL_STATUS_TIMEOUT_DIAGNOSTIC_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_FULL_SYSTEM_OMG_DEMO_GAP_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_FULL_SYSTEM_OMG_DEMO_GAP_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_full_system_omg…` |
| [DETERMINEX_GLOBAL_OPERATOR_ACTION_QUEUE_DEDUP_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_GLOBAL_OPERATOR_ACTION_QUEUE_DEDUP_RECONCILIATION_LOCK_001.json) | 5 | 5 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_determinex_global_…` |
| [DETERMINEX_GLOBAL_OPERATOR_ACTION_QUEUE_LOCK_001](../locks/sentinel/DETERMINEX_GLOBAL_OPERATOR_ACTION_QUEUE_LOCK_001.json) | 6 | 6 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_determinex_global_…` |
| [DETERMINEX_GLOBAL_TRAINING_ELIGIBILITY_GUARD_LOCK_001](../locks/sentinel/DETERMINEX_GLOBAL_TRAINING_ELIGIBILITY_GUARD_LOCK_001.json) | 5 | 5 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_determinex_global_…` |
| [DETERMINEX_GLOBAL_TRAINING_POSITIVE_GATE_DESIGN_LOCK_001](../locks/sentinel/DETERMINEX_GLOBAL_TRAINING_POSITIVE_GATE_DESIGN_LOCK_001.json) | 5 | 5 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_determinex_global_…` |
| [DETERMINEX_GO_TOOLCHAIN_REPAIR_AND_VITE_STATIC_SMOKE_LOCK_001](../locks/sentinel/DETERMINEX_GO_TOOLCHAIN_REPAIR_AND_VITE_STATIC_SMOKE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_GUI_AUTOMATION_AND_FIRST_PAINT_CAPABILITY_ROUTE_LOCK_001](../locks/sentinel/DETERMINEX_GUI_AUTOMATION_AND_FIRST_PAINT_CAPABILITY_ROUTE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_GUI_BUILD_PACKET_HARDENING_LOCK_001](../locks/sentinel/DETERMINEX_GUI_BUILD_PACKET_HARDENING_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_GUI_BUILD_SMOKE_INSTALLER_AND_RELEASE_CELL_CERTIFICATION_WAVE_001](../locks/sentinel/DETERMINEX_GUI_BUILD_SMOKE_INSTALLER_AND_RELEASE_CELL_CERTIFICATION_WAVE_001.json) | 9 | 69 | `9555e7ab2b` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_gui_build_smoke…` |
| [DETERMINEX_GUI_E2E_DRIVER_AUTHORIZATION_REFRESH_LOCK_001](../locks/sentinel/DETERMINEX_GUI_E2E_DRIVER_AUTHORIZATION_REFRESH_LOCK_001.json) | 20 | 20 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_gui_e2e_driver_…` |
| [DETERMINEX_GUI_E2E_HARNESS_REQUIREMENTS_LOCK_001](../locks/sentinel/DETERMINEX_GUI_E2E_HARNESS_REQUIREMENTS_LOCK_001.json) | 34 | 1128 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_gui_e2e_harness…` |
| [DETERMINEX_GUI_E2E_ROUTE_HARDENING_OR_FALLBACK_LOCK_001](../locks/sentinel/DETERMINEX_GUI_E2E_ROUTE_HARDENING_OR_FALLBACK_LOCK_001.json) | 26 | 26 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_gui_e2e_route_h…` |
| [DETERMINEX_GUI_FIRST_PAINT_AFTER_RUNTIME_APPROVAL_LOCK_001](../locks/sentinel/DETERMINEX_GUI_FIRST_PAINT_AFTER_RUNTIME_APPROVAL_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_GUI_FIRST_PAINT_EXECUTION_IF_AUTHORIZED_LOCK_001](../locks/sentinel/DETERMINEX_GUI_FIRST_PAINT_EXECUTION_IF_AUTHORIZED_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_GUI_FIRST_PAINT_EXECUTION_WITH_ADMITTED_DRIVER_LOCK_001](../locks/sentinel/DETERMINEX_GUI_FIRST_PAINT_EXECUTION_WITH_ADMITTED_DRIVER_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_GUI_FIRST_PAINT_VISUAL_PROOF_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_GUI_FIRST_PAINT_VISUAL_PROOF_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_007_gui_fi…` |
| [DETERMINEX_GUI_FIRST_VISUAL_PROOF_BATCH_OR_APPROVAL_PACKET_LOCK_001](../locks/sentinel/DETERMINEX_GUI_FIRST_VISUAL_PROOF_BATCH_OR_APPROVAL_PACKET_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_GUI_FIRST_VISUAL_PROOF_IF_APPROVED_LOCK_003](../locks/sentinel/DETERMINEX_GUI_FIRST_VISUAL_PROOF_IF_APPROVED_LOCK_003.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_016_canoni…` |
| [DETERMINEX_GUI_HARNESS_DEPENDENCY_AUTHORIZATION_LOCK_001](../locks/sentinel/DETERMINEX_GUI_HARNESS_DEPENDENCY_AUTHORIZATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_gui_harness_dep…` |
| [DETERMINEX_GUI_IDEA_LAB_PROMPT_TO_PLAN_FLOW_EXECUTION_LOCK_001](../locks/sentinel/DETERMINEX_GUI_IDEA_LAB_PROMPT_TO_PLAN_FLOW_EXECUTION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_GUI_MOAT_VISUAL_FLOW_BATCH_LOCK_001](../locks/sentinel/DETERMINEX_GUI_MOAT_VISUAL_FLOW_BATCH_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_GUI_NOT_EXECUTED_BOUNDARY_GUARD_LOCK_001](../locks/sentinel/DETERMINEX_GUI_NOT_EXECUTED_BOUNDARY_GUARD_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_GUI_PANEL_VISUAL_PROOF_BATCH_LOCK_001](../locks/sentinel/DETERMINEX_GUI_PANEL_VISUAL_PROOF_BATCH_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_GUI_PROGRAMBENCH_COCKPIT_FLOW_EXECUTION_LOCK_001](../locks/sentinel/DETERMINEX_GUI_PROGRAMBENCH_COCKPIT_FLOW_EXECUTION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_GUI_PROOF_LADDER_FIRST_PAINT_MEANINGFUL_FLOW_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_GUI_PROOF_LADDER_FIRST_PAINT_MEANINGFUL_FLOW_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_gui_proof_ladde…` |
| [DETERMINEX_GULP_WAVE_001_RECONCILIATION_AND_NEXT_WAVE_LOCK_001](../locks/sentinel/DETERMINEX_GULP_WAVE_001_RECONCILIATION_AND_NEXT_WAVE_LOCK_001.json) | 25 | 25 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_gulp_wave_001_r…` |
| [DETERMINEX_GULP_WAVE_002_RECONCILIATION_AND_NEXT_WAVE_LOCK_001](../locks/sentinel/DETERMINEX_GULP_WAVE_002_RECONCILIATION_AND_NEXT_WAVE_LOCK_001.json) | 30 | 30 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_gulp_wave_002_r…` |
| [DETERMINEX_GULP_WAVE_003_RECONCILIATION_AND_NEXT_WAVE_LOCK_001](../locks/sentinel/DETERMINEX_GULP_WAVE_003_RECONCILIATION_AND_NEXT_WAVE_LOCK_001.json) | 34 | 2704 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_gulp_wave_003_r…` |
| [DETERMINEX_GULP_WAVE_004_CLAUDE_SYNTHESIS_AND_CODEX_DELTA_QUEUE_001](../locks/sentinel/DETERMINEX_GULP_WAVE_004_CLAUDE_SYNTHESIS_AND_CODEX_DELTA_QUEUE_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_gulp_wave_004_c…` |
| [DETERMINEX_GULP_WAVE_004_RECONCILIATION_AND_WAVE_005_GENERATOR_LOCK_001](../locks/sentinel/DETERMINEX_GULP_WAVE_004_RECONCILIATION_AND_WAVE_005_GENERATOR_LOCK_001.json) | 35 | 35 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_gulp_wave_004_r…` |
| [DETERMINEX_GULP_WAVE_005_CLAUDE_SYNTHESIS_AND_CODEX_PRESSURE_QUEUE_001](../locks/sentinel/DETERMINEX_GULP_WAVE_005_CLAUDE_SYNTHESIS_AND_CODEX_PRESSURE_QUEUE_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_gulp_wave_005_c…` |
| [DETERMINEX_GULP_WAVE_005_RECONCILIATION_AND_WAVE_006_GENERATOR_LOCK_001](../locks/sentinel/DETERMINEX_GULP_WAVE_005_RECONCILIATION_AND_WAVE_006_GENERATOR_LOCK_001.json) | 18 | 18 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_gulp_wave_005_r…` |
| [DETERMINEX_GULP_WAVE_006_RECONCILIATION_AND_WAVE_007_GENERATOR_LOCK_001](../locks/sentinel/DETERMINEX_GULP_WAVE_006_RECONCILIATION_AND_WAVE_007_GENERATOR_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_gulp_wave_006_r…` |
| [DETERMINEX_GULP_WAVE_007_RECONCILIATION_AND_WAVE_008_GENERATOR_LOCK_001](../locks/sentinel/DETERMINEX_GULP_WAVE_007_RECONCILIATION_AND_WAVE_008_GENERATOR_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_GULP_WAVE_008_RECONCILIATION_AND_WAVE_009_QUEUE_LOCK_001](../locks/sentinel/DETERMINEX_GULP_WAVE_008_RECONCILIATION_AND_WAVE_009_QUEUE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_GULP_WAVE_009_RECONCILIATION_AND_WAVE_010_QUEUE_LOCK_001](../locks/sentinel/DETERMINEX_GULP_WAVE_009_RECONCILIATION_AND_WAVE_010_QUEUE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_GULP_WAVE_010_RECONCILIATION_AND_WAVE_011_QUEUE_LOCK_001](../locks/sentinel/DETERMINEX_GULP_WAVE_010_RECONCILIATION_AND_WAVE_011_QUEUE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_GULP_WAVE_011_RECONCILIATION_AND_WAVE_012_QUEUE_LOCK_001](../locks/sentinel/DETERMINEX_GULP_WAVE_011_RECONCILIATION_AND_WAVE_012_QUEUE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_HIVE_BUILD_LOOP_WAL_PANEL_WIRE_LOCK_001](../locks/sentinel/DETERMINEX_HIVE_BUILD_LOOP_WAL_PANEL_WIRE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_HIVE_BUILD_LOOP_WAL_RENDER_CONTRACT_LOCK_001](../locks/sentinel/DETERMINEX_HIVE_BUILD_LOOP_WAL_RENDER_CONTRACT_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_HIVE_BUILD_LOOP_WAL_VISIBILITY_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_HIVE_BUILD_LOOP_WAL_VISIBILITY_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_hive_build_loop…` |
| [DETERMINEX_HTML_PROOF_REPORT_ATTACK_REVIEW_CLAUDE_001](../locks/sentinel/DETERMINEX_HTML_PROOF_REPORT_ATTACK_REVIEW_CLAUDE_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_007_html_p…` |
| [DETERMINEX_HTML_PROOF_REPORT_INVESTOR_SHAREABILITY_FINALIZATION_LOCK_001](../locks/sentinel/DETERMINEX_HTML_PROOF_REPORT_INVESTOR_SHAREABILITY_FINALIZATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_HTML_PROOF_REPORT_SHAREABILITY_HARDENING_LOCK_001](../locks/sentinel/DETERMINEX_HTML_PROOF_REPORT_SHAREABILITY_HARDENING_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_IDEA_LAB_ACCEPTANCE_TEST_EXECUTION_PIPELINE_LOCK_001](../locks/sentinel/DETERMINEX_IDEA_LAB_ACCEPTANCE_TEST_EXECUTION_PIPELINE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_IDEA_LAB_CERTIFICATION_AND_PRODUCT_SURFACE_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_IDEA_LAB_CERTIFICATION_AND_PRODUCT_SURFACE_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_idea_lab_certif…` |
| [DETERMINEX_IDEA_LAB_DETERMINISTIC_ARTIFACT_RELEASE_SUPPORTED_CELL_CERTIFICATION_LOCK_001](../locks/sentinel/DETERMINEX_IDEA_LAB_DETERMINISTIC_ARTIFACT_RELEASE_SUPPORTED_CELL_CERTIFICATION_LOCK_001.json) | 36 | 36 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_idea_lab_determ…` |
| [DETERMINEX_IDEA_LAB_END_TO_END_ARTIFACT_PROOF_LOCK_001](../locks/sentinel/DETERMINEX_IDEA_LAB_END_TO_END_ARTIFACT_PROOF_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_idea_lab_end_to…` |
| [DETERMINEX_IDEA_LAB_EXACT_CELL_CERTIFICATION_RETRY_LOCK_001](../locks/sentinel/DETERMINEX_IDEA_LAB_EXACT_CELL_CERTIFICATION_RETRY_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_idea_lab_exact_…` |
| [DETERMINEX_IDEA_LAB_FREEFORM_ACCEPTANCE_TEST_GENERATOR_LOCK_001](../locks/sentinel/DETERMINEX_IDEA_LAB_FREEFORM_ACCEPTANCE_TEST_GENERATOR_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_IDEA_LAB_PROMPT_TO_PLAN_DETERMINISM_LOCK_001](../locks/sentinel/DETERMINEX_IDEA_LAB_PROMPT_TO_PLAN_DETERMINISM_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_idea_lab_prompt…` |
| [DETERMINEX_IDEA_LAB_PYTHON_CLI_VERIFIED_SPLASH_DEMO_LOCK_001](../locks/sentinel/DETERMINEX_IDEA_LAB_PYTHON_CLI_VERIFIED_SPLASH_DEMO_LOCK_001.json) | 13 | 13 | `1fd1c90f7` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_determinex_idea_la…` |
| [DETERMINEX_IDEA_LAB_PYTHON_CLI_VERIFIED_SPLASH_DEMO_READINESS_LOCK_001](../locks/sentinel/DETERMINEX_IDEA_LAB_PYTHON_CLI_VERIFIED_SPLASH_DEMO_READINESS_LOCK_001.json) | 15 | 15 | `e113efbd6e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_determinex_splash_…` |
| [DETERMINEX_IDEA_LAB_UNDER_THE_HOOD_E2E_PIPELINE_LOCK_001](../locks/sentinel/DETERMINEX_IDEA_LAB_UNDER_THE_HOOD_E2E_PIPELINE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_under…` |
| [DETERMINEX_IDEA_LAB_WORKFLOW_LOCK_001](../locks/sentinel/DETERMINEX_IDEA_LAB_WORKFLOW_LOCK_001.json) | 16 | 16 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_idea_lab_workflow_…` |
| [DETERMINEX_IDE_BACKEND_FINAL_STATE_LOCK_001](../locks/sentinel/DETERMINEX_IDE_BACKEND_FINAL_STATE_LOCK_001.json) | 31 | 31 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/dev/test_determinex_ide_backen…` |
| [DETERMINEX_IDE_CONSUMER_READY_FINAL_STATE_LOCK_001](../locks/sentinel/DETERMINEX_IDE_CONSUMER_READY_FINAL_STATE_LOCK_001.json) | 19 | 19 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/dev/test_determinex_ide_consum…` |
| [DETERMINEX_IDE_FRONTEND_READY_FINAL_STATE_LOCK_001](../locks/sentinel/DETERMINEX_IDE_FRONTEND_READY_FINAL_STATE_LOCK_001.json) | 20 | 20 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/dev/test_determinex_ide_fronte…` |
| [DETERMINEX_IDE_RELEASE_ASCENT_RECONCILIATION_AND_NEXT_PROOF_LOCK_001](../locks/sentinel/DETERMINEX_IDE_RELEASE_ASCENT_RECONCILIATION_AND_NEXT_PROOF_LOCK_001.json) | 35 | 999 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_ide_release_asc…` |
| [DETERMINEX_IDE_TAURI_INTEGRATED_FINAL_STATE_LOCK_001](../locks/sentinel/DETERMINEX_IDE_TAURI_INTEGRATED_FINAL_STATE_LOCK_001.json) | 17 | 17 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/dev/test_determinex_ide_tauri_…` |
| [DETERMINEX_IDE_UI_READY_FINAL_STATE_LOCK_001](../locks/sentinel/DETERMINEX_IDE_UI_READY_FINAL_STATE_LOCK_001.json) | 20 | 20 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/dev/test_determinex_ide_ui_rea…` |
| [DETERMINEX_IMPORT_REAL_SIGNED_APPROVALS_AND_SPEND_QUEUE_LOCK_001](../locks/sentinel/DETERMINEX_IMPORT_REAL_SIGNED_APPROVALS_AND_SPEND_QUEUE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_INSTALLER_DISTRIBUTION_TRUST_CHAIN_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_INSTALLER_DISTRIBUTION_TRUST_CHAIN_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_installer_distr…` |
| [DETERMINEX_INSTALLER_INSTALL_LAUNCH_UNINSTALL_RELEASE_SIGNOFF_WAVE_001](../locks/sentinel/DETERMINEX_INSTALLER_INSTALL_LAUNCH_UNINSTALL_RELEASE_SIGNOFF_WAVE_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_installer_insta…` |
| [DETERMINEX_INSTALLER_NOT_EXECUTED_BOUNDARY_GUARD_LOCK_001](../locks/sentinel/DETERMINEX_INSTALLER_NOT_EXECUTED_BOUNDARY_GUARD_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_INSTALLER_REALITY_SBOM_SIGNING_PUBLIC_DISTRIBUTION_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_INSTALLER_REALITY_SBOM_SIGNING_PUBLIC_DISTRIBUTION_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_installer_reali…` |
| [DETERMINEX_INSTALLER_RELEASE_PACKET_HARDENING_LOCK_001](../locks/sentinel/DETERMINEX_INSTALLER_RELEASE_PACKET_HARDENING_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_INTERNAL_PREVIEW_AND_SUBPACKAGE_DISTRIBUTION_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_INTERNAL_PREVIEW_AND_SUBPACKAGE_DISTRIBUTION_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_internal_previe…` |
| [DETERMINEX_INTERNAL_PREVIEW_DISTRIBUTION_PACKET_LOCK_001](../locks/sentinel/DETERMINEX_INTERNAL_PREVIEW_DISTRIBUTION_PACKET_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_internal_previe…` |
| [DETERMINEX_INVALID_SIGNATURE_REJECTION_CORPUS_LOCK_001](../locks/sentinel/DETERMINEX_INVALID_SIGNATURE_REJECTION_CORPUS_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_signature_deliv…` |
| [DETERMINEX_KNOWN_WORLD_CAPABILITY_UNIVERSE_REGISTRY_LOCK_001](../locks/sentinel/DETERMINEX_KNOWN_WORLD_CAPABILITY_UNIVERSE_REGISTRY_LOCK_001.json) | 18 | 1 | `e4ff17592c` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_admitted_clean_…` |
| [DETERMINEX_KNOWN_WORLD_DETECTOR_GAP_QUEUE_LOCK_001](../locks/sentinel/DETERMINEX_KNOWN_WORLD_DETECTOR_GAP_QUEUE_LOCK_001.json) | 18 | 1 | `e4ff17592c` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_admitted_clean_…` |
| [DETERMINEX_KNOWN_WORLD_DETECTOR_SEGMENT_1_LOCK_001](../locks/sentinel/DETERMINEX_KNOWN_WORLD_DETECTOR_SEGMENT_1_LOCK_001.json) | 21 | 21 | `pending-fi` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_runner_sa…` |
| [DETERMINEX_KOTLIN_TOOLCHAIN_GLOBAL_GATE_LOCK_001](../locks/sentinel/DETERMINEX_KOTLIN_TOOLCHAIN_GLOBAL_GATE_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_LADDER_INVERSION_CI_BLOCKING_LOCK_002](../locks/sentinel/DETERMINEX_LADDER_INVERSION_CI_BLOCKING_LOCK_002.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_015_canoni…` |
| [DETERMINEX_LADDER_RUNG_INVERSION_CI_LOCK_001](../locks/sentinel/DETERMINEX_LADDER_RUNG_INVERSION_CI_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_014_signed…` |
| [DETERMINEX_LANGUAGE_FRAMEWORK_ADAPTER_REGISTRY_LOCK_001](../locks/sentinel/DETERMINEX_LANGUAGE_FRAMEWORK_ADAPTER_REGISTRY_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_determinex_univers…` |
| [DETERMINEX_LANGUAGE_TOOLCHAIN_DETECTOR_MATRIX_LOCK_001](../locks/sentinel/DETERMINEX_LANGUAGE_TOOLCHAIN_DETECTOR_MATRIX_LOCK_001.json) | 15 | 15 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_language_toolch…` |
| [DETERMINEX_LANGUAGE_TOOLCHAIN_DETECTOR_MATRIX_RECONCILIATION_LOCK_002](../locks/sentinel/DETERMINEX_LANGUAGE_TOOLCHAIN_DETECTOR_MATRIX_RECONCILIATION_LOCK_002.json) | 17 | 17 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_language_toolch…` |
| [DETERMINEX_LEARNING_STUDIO_TEACHING_SPLASH_DEMO_LOCK_001](../locks/sentinel/DETERMINEX_LEARNING_STUDIO_TEACHING_SPLASH_DEMO_LOCK_001.json) | 13 | 13 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_determinex_learnin…` |
| [DETERMINEX_LEARNING_STUDIO_WORKFLOW_LOCK_001](../locks/sentinel/DETERMINEX_LEARNING_STUDIO_WORKFLOW_LOCK_001.json) | 21 | 21 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_learning_studio_wo…` |
| [DETERMINEX_LEGACY_FULL_VERIFIER_SIGNOFF_COMPLETION_LOCK_001](../locks/sentinel/DETERMINEX_LEGACY_FULL_VERIFIER_SIGNOFF_COMPLETION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_019_execut…` |
| [DETERMINEX_LEGACY_RELEASE_CELL_SIGNOFF_BACKFILL_LOCK_001](../locks/sentinel/DETERMINEX_LEGACY_RELEASE_CELL_SIGNOFF_BACKFILL_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_017_canoni…` |
| [DETERMINEX_LEGACY_TEN_RELEASE_CELLS_SIGNOFF_BACKFILL_LOCK_002](../locks/sentinel/DETERMINEX_LEGACY_TEN_RELEASE_CELLS_SIGNOFF_BACKFILL_LOCK_002.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_018_canoni…` |
| [DETERMINEX_LICENSE_SECURITY_SIGNING_POSTURE_DECISION_LOCK_001](../locks/sentinel/DETERMINEX_LICENSE_SECURITY_SIGNING_POSTURE_DECISION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_license_securit…` |
| [DETERMINEX_LICENSE_SECURITY_SIGNING_ROUTE_EXECUTION_BOARD_LOCK_001](../locks/sentinel/DETERMINEX_LICENSE_SECURITY_SIGNING_ROUTE_EXECUTION_BOARD_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_LINUX_CI_FRESH_INSTALL_CANDIDATE_PROOF_LOCK_001](../locks/sentinel/DETERMINEX_LINUX_CI_FRESH_INSTALL_CANDIDATE_PROOF_LOCK_001.json) | 22 | 22 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_linux_ci_fresh_…` |
| [DETERMINEX_LINUX_CI_FRESH_INSTALL_EXECUTION_LOCK_001](../locks/sentinel/DETERMINEX_LINUX_CI_FRESH_INSTALL_EXECUTION_LOCK_001.json) | 24 | 24 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_linux_ci_fresh_…` |
| [DETERMINEX_LINUX_CLEAN_RUNNER_EXECUTION_LOCK_001](../locks/sentinel/DETERMINEX_LINUX_CLEAN_RUNNER_EXECUTION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_LINUX_CLEAN_RUNNER_TOOLING_UNBLOCK_LOCK_001](../locks/sentinel/DETERMINEX_LINUX_CLEAN_RUNNER_TOOLING_UNBLOCK_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_linux_clean_run…` |
| [DETERMINEX_LIVE_REACT_PRODUCT_SHELL_DEMO_READINESS_FINAL_STATE_LOCK_001](../locks/sentinel/DETERMINEX_LIVE_REACT_PRODUCT_SHELL_DEMO_READINESS_FINAL_STATE_LOCK_001.json) | 13 | 13 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_live_react_prod…` |
| [DETERMINEX_LIVE_REACT_UNIFIED_PRODUCT_SHELL_FINAL_STATE_LOCK_001](../locks/sentinel/DETERMINEX_LIVE_REACT_UNIFIED_PRODUCT_SHELL_FINAL_STATE_LOCK_001.json) | 13 | 13 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_live_react_unif…` |
| [DETERMINEX_LOCAL_PACKAGE_DRY_RUN_BATCH_LOCK_001](../locks/sentinel/DETERMINEX_LOCAL_PACKAGE_DRY_RUN_BATCH_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_LOCAL_PACKAGE_DRY_RUN_HARDENING_BATCH_LOCK_001](../locks/sentinel/DETERMINEX_LOCAL_PACKAGE_DRY_RUN_HARDENING_BATCH_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_LOCAL_PREVIEW_EXACT_CELL_GATE_COMPLETION_OR_DEMOTION_LOCK_001](../locks/sentinel/DETERMINEX_LOCAL_PREVIEW_EXACT_CELL_GATE_COMPLETION_OR_DEMOTION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_015_canoni…` |
| [DETERMINEX_LOCAL_PREVIEW_PACKAGE_BOUNDARY_HARDENING_LOCK_001](../locks/sentinel/DETERMINEX_LOCAL_PREVIEW_PACKAGE_BOUNDARY_HARDENING_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_019_execut…` |
| [DETERMINEX_LOCAL_PREVIEW_PACKAGE_PROMOTION_READINESS_WITHOUT_PROMOTION_LOCK_001](../locks/sentinel/DETERMINEX_LOCAL_PREVIEW_PACKAGE_PROMOTION_READINESS_WITHOUT_PROMOTION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_017_canoni…` |
| [DETERMINEX_LOCAL_PREVIEW_VS_RELEASE_SUPPORTED_BOUNDARY_LOCK_001](../locks/sentinel/DETERMINEX_LOCAL_PREVIEW_VS_RELEASE_SUPPORTED_BOUNDARY_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_016_canoni…` |
| [DETERMINEX_LOCAL_PROOF_REPORT_EXPORT_CELL_CERTIFICATION_LOCK_001](../locks/sentinel/DETERMINEX_LOCAL_PROOF_REPORT_EXPORT_CELL_CERTIFICATION_LOCK_001.json) | 36 | 36 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_local_proof_rep…` |
| [DETERMINEX_LOCAL_PROOF_REPORT_EXPORT_CELL_OPERATOR_APPROVAL_LOCK_001](../locks/sentinel/DETERMINEX_LOCAL_PROOF_REPORT_EXPORT_CELL_OPERATOR_APPROVAL_LOCK_001.json) | 28 | 28 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_local_proof_rep…` |
| [DETERMINEX_LOCAL_RAG_QUERY_SMOKE_LOCK_001](../locks/sentinel/DETERMINEX_LOCAL_RAG_QUERY_SMOKE_LOCK_001.json) | 17 | 949 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_local_rag_query…` |
| [DETERMINEX_LOCAL_SMOKE_AFTER_BUILD_ARTIFACT_LOCK_001](../locks/sentinel/DETERMINEX_LOCAL_SMOKE_AFTER_BUILD_ARTIFACT_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_local_smoke_aft…` |
| [DETERMINEX_LOCAL_SMOKE_AFTER_FASTEMBED_BINDING_RETRY_LOCK_001](../locks/sentinel/DETERMINEX_LOCAL_SMOKE_AFTER_FASTEMBED_BINDING_RETRY_LOCK_001.json) | 11 | 891 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_local_smoke_aft…` |
| [DETERMINEX_LOCAL_SMOKE_AFTER_NSIS_ARTIFACT_LOCK_001](../locks/sentinel/DETERMINEX_LOCAL_SMOKE_AFTER_NSIS_ARTIFACT_LOCK_001.json) | 13 | 13 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_local_smoke_aft…` |
| [DETERMINEX_MACHINE_AUTHORITY_PROMOTION_RULES_LOCK_001](../locks/sentinel/DETERMINEX_MACHINE_AUTHORITY_PROMOTION_RULES_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_MAINTENANCE_BAY_DRY_RUN_UPDATE_SPLASH_DEMO_LOCK_001](../locks/sentinel/DETERMINEX_MAINTENANCE_BAY_DRY_RUN_UPDATE_SPLASH_DEMO_LOCK_001.json) | 13 | 13 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_determinex_mainten…` |
| [DETERMINEX_MAINTENANCE_BAY_WORKFLOW_LOCK_001](../locks/sentinel/DETERMINEX_MAINTENANCE_BAY_WORKFLOW_LOCK_001.json) | 19 | 19 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_maintenance_bay_wo…` |
| [DETERMINEX_MARCH_DASHBOARD_ADMITTED_CLEAN_RUNNER_UPDATE_LOCK_001](../locks/sentinel/DETERMINEX_MARCH_DASHBOARD_ADMITTED_CLEAN_RUNNER_UPDATE_LOCK_001.json) | 18 | 1 | `e4ff17592c` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_admitted_clean_…` |
| [DETERMINEX_MATRIX_PROBE_RUNNER_LOCK_001](../locks/sentinel/DETERMINEX_MATRIX_PROBE_RUNNER_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_determinex_univers…` |
| [DETERMINEX_MAX_SAFE_FAMILY_BOUNDED_EXECUTION_LOCK_001](../locks/sentinel/DETERMINEX_MAX_SAFE_FAMILY_BOUNDED_EXECUTION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_MAX_SAFE_FAMILY_CAPABILITY_PROMOTION_LOCK_001](../locks/sentinel/DETERMINEX_MAX_SAFE_FAMILY_CAPABILITY_PROMOTION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_MAX_SAFE_FAMILY_CLEAN_GUI_INSTALLER_PREP_LOCK_001](../locks/sentinel/DETERMINEX_MAX_SAFE_FAMILY_CLEAN_GUI_INSTALLER_PREP_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_MAX_SAFE_FAMILY_EXECUTION_SELECTION_LOCK_001](../locks/sentinel/DETERMINEX_MAX_SAFE_FAMILY_EXECUTION_SELECTION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_MAX_SAFE_FAMILY_MARCH_PLAN_DASHBOARD_LOCK_001](../locks/sentinel/DETERMINEX_MAX_SAFE_FAMILY_MARCH_PLAN_DASHBOARD_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_MAX_SAFE_FAMILY_QUEUE_EXPANSION_LOCK_001](../locks/sentinel/DETERMINEX_MAX_SAFE_FAMILY_QUEUE_EXPANSION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_MAX_SAFE_FAMILY_REPAIR_RERUN_LOOP_LOCK_001](../locks/sentinel/DETERMINEX_MAX_SAFE_FAMILY_REPAIR_RERUN_LOOP_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_MAX_SAFE_FAMILY_SBOM_GATE_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_MAX_SAFE_FAMILY_SBOM_GATE_RECONCILIATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_MAX_SAFE_FAMILY_SBOM_ONE_TIME_SPEND_LOCK_001](../locks/sentinel/DETERMINEX_MAX_SAFE_FAMILY_SBOM_ONE_TIME_SPEND_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_MAX_SAFE_FAMILY_SBOM_PACKET_RUNTIME_ADMISSION_LOCK_001](../locks/sentinel/DETERMINEX_MAX_SAFE_FAMILY_SBOM_PACKET_RUNTIME_ADMISSION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_MAX_SAFE_FAMILY_SBOM_POST_SPEND_VERIFICATION_LOCK_001](../locks/sentinel/DETERMINEX_MAX_SAFE_FAMILY_SBOM_POST_SPEND_VERIFICATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_MAX_SAFE_FAMILY_SBOM_SCOPED_EXECUTION_LOCK_001](../locks/sentinel/DETERMINEX_MAX_SAFE_FAMILY_SBOM_SCOPED_EXECUTION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_MAX_SAFE_FAMILY_SCORE_DISCIPLINE_LOCK_001](../locks/sentinel/DETERMINEX_MAX_SAFE_FAMILY_SCORE_DISCIPLINE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_MEANINGFUL_GUI_FLOW_IDEA_LAB_PROMPT_TO_PLAN_PROOF_LOCK_001](../locks/sentinel/DETERMINEX_MEANINGFUL_GUI_FLOW_IDEA_LAB_PROMPT_TO_PLAN_PROOF_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_meaningful_gui_…` |
| [DETERMINEX_MEANINGFUL_GUI_FLOW_PRIORITY_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_MEANINGFUL_GUI_FLOW_PRIORITY_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_meaningful_gui_…` |
| [DETERMINEX_MEANINGFUL_GUI_FLOW_PROGRAMBENCH_COCKPIT_PROOF_LOCK_001](../locks/sentinel/DETERMINEX_MEANINGFUL_GUI_FLOW_PROGRAMBENCH_COCKPIT_PROOF_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_meaningful_gui_…` |
| [DETERMINEX_MERGE_POINT_FINAL_STATE_LOCK_001](../locks/sentinel/DETERMINEX_MERGE_POINT_FINAL_STATE_LOCK_001.json) | 4 | 4 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_determinex_merge_p…` |
| [DETERMINEX_MINIMUM_GUI_FLOW_PROOF_CONTRACT_AND_FIRST_PAINT_SMOKE_LOCK_001](../locks/sentinel/DETERMINEX_MINIMUM_GUI_FLOW_PROOF_CONTRACT_AND_FIRST_PAINT_SMOKE_LOCK_001.json) | 28 | 28 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_minimum_gui_flo…` |
| [DETERMINEX_ML_INFERENCE_AUTHORITY_GATE_LOCK_001](../locks/sentinel/DETERMINEX_ML_INFERENCE_AUTHORITY_GATE_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_MOBILE_NATIVE_AUTHORITY_GATE_LOCK_001](../locks/sentinel/DETERMINEX_MOBILE_NATIVE_AUTHORITY_GATE_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_MSEDGEDRIVER_ADMISSION_AFTER_REAL_SIGNATURE_LOCK_001](../locks/sentinel/DETERMINEX_MSEDGEDRIVER_ADMISSION_AFTER_REAL_SIGNATURE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_MSEDGEDRIVER_ADMISSION_EXECUTION_IF_SIGNED_LOCK_001](../locks/sentinel/DETERMINEX_MSEDGEDRIVER_ADMISSION_EXECUTION_IF_SIGNED_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_MSEDGEDRIVER_ADMISSION_WITH_RUNTIME_APPROVAL_LOCK_001](../locks/sentinel/DETERMINEX_MSEDGEDRIVER_ADMISSION_WITH_RUNTIME_APPROVAL_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_MSEDGEDRIVER_BOUNDED_DOWNLOAD_OPERATOR_APPROVAL_LOCK_001](../locks/sentinel/DETERMINEX_MSEDGEDRIVER_BOUNDED_DOWNLOAD_OPERATOR_APPROVAL_LOCK_001.json) | 22 | 22 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_msedgedriver_bo…` |
| [DETERMINEX_MSEDGEDRIVER_GUI_FIRST_PAINT_READINESS_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_MSEDGEDRIVER_GUI_FIRST_PAINT_READINESS_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_msedgedriver_gu…` |
| [DETERMINEX_MSFG_CLAUDE_EVIDENCE_INDEX_GUARDS_REVIEW_001](../locks/sentinel/DETERMINEX_MSFG_CLAUDE_EVIDENCE_INDEX_GUARDS_REVIEW_001.json) | 1 | 1 | `20f0d41887` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_msfg_claude_evi…` |
| [DETERMINEX_MSFG_CLAUDE_EXACT_LOCAL_NOT_FAMILY_SUPPORT_REVIEW_001](../locks/sentinel/DETERMINEX_MSFG_CLAUDE_EXACT_LOCAL_NOT_FAMILY_SUPPORT_REVIEW_001.json) | 1 | 1 | `20f0d41887` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_msfg_claude_exa…` |
| [DETERMINEX_MSFG_CLAUDE_FAMILIES_EXECUTED_REVIEW_001](../locks/sentinel/DETERMINEX_MSFG_CLAUDE_FAMILIES_EXECUTED_REVIEW_001.json) | 1 | 1 | `20f0d41887` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_msfg_claude_fam…` |
| [DETERMINEX_MSFG_CLAUDE_FAMILIES_SELECTED_REVIEW_001](../locks/sentinel/DETERMINEX_MSFG_CLAUDE_FAMILIES_SELECTED_REVIEW_001.json) | 1 | 1 | `20f0d41887` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_msfg_claude_fam…` |
| [DETERMINEX_MSFG_CLAUDE_FAMILY_MAP_COVERAGE_REVIEW_001](../locks/sentinel/DETERMINEX_MSFG_CLAUDE_FAMILY_MAP_COVERAGE_REVIEW_001.json) | 1 | 1 | `20f0d41887` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_msfg_claude_fam…` |
| [DETERMINEX_MSFG_CLAUDE_FAMILY_PROMOTIONS_REVIEW_001](../locks/sentinel/DETERMINEX_MSFG_CLAUDE_FAMILY_PROMOTIONS_REVIEW_001.json) | 1 | 1 | `20f0d41887` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_msfg_claude_fam…` |
| [DETERMINEX_MSFG_CLAUDE_FAMILY_REPAIR_DISCIPLINE_REVIEW_001](../locks/sentinel/DETERMINEX_MSFG_CLAUDE_FAMILY_REPAIR_DISCIPLINE_REVIEW_001.json) | 1 | 1 | `20f0d41887` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_msfg_claude_fam…` |
| [DETERMINEX_MSFG_CLAUDE_FAMILY_SELECTION_REVIEW_001](../locks/sentinel/DETERMINEX_MSFG_CLAUDE_FAMILY_SELECTION_REVIEW_001.json) | 1 | 1 | `20f0d41887` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_msfg_claude_fam…` |
| [DETERMINEX_MSFG_CLAUDE_FAMILY_TRANSCRIPT_REVIEW_001](../locks/sentinel/DETERMINEX_MSFG_CLAUDE_FAMILY_TRANSCRIPT_REVIEW_001.json) | 1 | 1 | `20f0d41887` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_msfg_claude_fam…` |
| [DETERMINEX_MSFG_CLAUDE_FAMILY_VERIFICATION_VERDICTS_REVIEW_001](../locks/sentinel/DETERMINEX_MSFG_CLAUDE_FAMILY_VERIFICATION_VERDICTS_REVIEW_001.json) | 1 | 1 | `20f0d41887` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_msfg_claude_fam…` |
| [DETERMINEX_MSFG_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001](../locks/sentinel/DETERMINEX_MSFG_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001.json) | 1 | 1 | `20f0d41887` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_msfg_claude_for…` |
| [DETERMINEX_MSFG_CLAUDE_FULL_STATUS_TIMEOUT_REVIEW_001](../locks/sentinel/DETERMINEX_MSFG_CLAUDE_FULL_STATUS_TIMEOUT_REVIEW_001.json) | 1 | 1 | `20f0d41887` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_msfg_claude_ful…` |
| [DETERMINEX_MSFG_CLAUDE_MARCH_PLAN_DASHBOARD_REVIEW_001](../locks/sentinel/DETERMINEX_MSFG_CLAUDE_MARCH_PLAN_DASHBOARD_REVIEW_001.json) | 1 | 1 | `20f0d41887` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_msfg_claude_mar…` |
| [DETERMINEX_MSFG_CLAUDE_NEW_STATUS_SUMMARY_REVIEW_001](../locks/sentinel/DETERMINEX_MSFG_CLAUDE_NEW_STATUS_SUMMARY_REVIEW_001.json) | 1 | 1 | `20f0d41887` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_msfg_claude_new…` |
| [DETERMINEX_MSFG_CLAUDE_NONLV_FAMILY_NEXT_ACTION_REVIEW_001](../locks/sentinel/DETERMINEX_MSFG_CLAUDE_NONLV_FAMILY_NEXT_ACTION_REVIEW_001.json) | 1 | 1 | `20f0d41887` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_msfg_claude_non…` |
| [DETERMINEX_MSFG_CLAUDE_NO_BINARY_MUTATION_REVIEW_001](../locks/sentinel/DETERMINEX_MSFG_CLAUDE_NO_BINARY_MUTATION_REVIEW_001.json) | 1 | 1 | `20f0d41887` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_msfg_claude_no_…` |
| [DETERMINEX_MSFG_CLAUDE_NO_LOCKFILE_MUTATION_REVIEW_001](../locks/sentinel/DETERMINEX_MSFG_CLAUDE_NO_LOCKFILE_MUTATION_REVIEW_001.json) | 1 | 1 | `20f0d41887` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_msfg_claude_no_…` |
| [DETERMINEX_MSFG_CLAUDE_NO_TEST_MUTATION_REVIEW_001](../locks/sentinel/DETERMINEX_MSFG_CLAUDE_NO_TEST_MUTATION_REVIEW_001.json) | 1 | 1 | `20f0d41887` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_msfg_claude_no_…` |
| [DETERMINEX_MSFG_CLAUDE_NO_UNIVERSAL_SUPPORT_REVIEW_001](../locks/sentinel/DETERMINEX_MSFG_CLAUDE_NO_UNIVERSAL_SUPPORT_REVIEW_001.json) | 1 | 1 | `20f0d41887` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_msfg_claude_no_…` |
| [DETERMINEX_MSFG_CLAUDE_NO_VERIFIER_MUTATION_REVIEW_001](../locks/sentinel/DETERMINEX_MSFG_CLAUDE_NO_VERIFIER_MUTATION_REVIEW_001.json) | 1 | 1 | `20f0d41887` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_msfg_claude_no_…` |
| [DETERMINEX_MSFG_CLAUDE_OTHER_PACKETS_NOT_EXECUTED_REVIEW_001](../locks/sentinel/DETERMINEX_MSFG_CLAUDE_OTHER_PACKETS_NOT_EXECUTED_REVIEW_001.json) | 1 | 1 | `20f0d41887` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_msfg_claude_oth…` |
| [DETERMINEX_MSFG_CLAUDE_PREVIOUS_STATUS_SUMMARY_REVIEW_001](../locks/sentinel/DETERMINEX_MSFG_CLAUDE_PREVIOUS_STATUS_SUMMARY_REVIEW_001.json) | 1 | 1 | `20f0d41887` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_msfg_claude_pre…` |
| [DETERMINEX_MSFG_CLAUDE_RELEASE_INVARIANTS_REVIEW_001](../locks/sentinel/DETERMINEX_MSFG_CLAUDE_RELEASE_INVARIANTS_REVIEW_001.json) | 1 | 1 | `20f0d41887` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_msfg_claude_rel…` |
| [DETERMINEX_MSFG_CLAUDE_REMAINING_NONLV_COUNT_REVIEW_001](../locks/sentinel/DETERMINEX_MSFG_CLAUDE_REMAINING_NONLV_COUNT_REVIEW_001.json) | 1 | 1 | `20f0d41887` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_msfg_claude_rem…` |
| [DETERMINEX_MSFG_CLAUDE_RUNTIME_QUEUE_REVIEW_001](../locks/sentinel/DETERMINEX_MSFG_CLAUDE_RUNTIME_QUEUE_REVIEW_001.json) | 1 | 1 | `20f0d41887` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_msfg_claude_run…` |
| [DETERMINEX_MSFG_CLAUDE_SBOM_BLOCKER_HONEST_REVIEW_001](../locks/sentinel/DETERMINEX_MSFG_CLAUDE_SBOM_BLOCKER_HONEST_REVIEW_001.json) | 1 | 1 | `20f0d41887` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_msfg_claude_sbo…` |
| [DETERMINEX_MSFG_CLAUDE_SBOM_EXECUTION_REVIEW_001](../locks/sentinel/DETERMINEX_MSFG_CLAUDE_SBOM_EXECUTION_REVIEW_001.json) | 1 | 1 | `20f0d41887` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_msfg_claude_sbo…` |
| [DETERMINEX_MSFG_CLAUDE_SBOM_PACKET_REVIEW_001](../locks/sentinel/DETERMINEX_MSFG_CLAUDE_SBOM_PACKET_REVIEW_001.json) | 1 | 1 | `20f0d41887` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_msfg_claude_sbo…` |
| [DETERMINEX_MSFG_CLAUDE_SBOM_QUEUE_ADMISSION_REVIEW_001](../locks/sentinel/DETERMINEX_MSFG_CLAUDE_SBOM_QUEUE_ADMISSION_REVIEW_001.json) | 1 | 1 | `20f0d41887` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_msfg_claude_sbo…` |
| [DETERMINEX_MSFG_CLAUDE_SBOM_SPEND_REUSE_REVIEW_001](../locks/sentinel/DETERMINEX_MSFG_CLAUDE_SBOM_SPEND_REUSE_REVIEW_001.json) | 1 | 1 | `20f0d41887` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_msfg_claude_sbo…` |
| [DETERMINEX_MSFG_CLAUDE_SBOM_SPEND_REVIEW_001](../locks/sentinel/DETERMINEX_MSFG_CLAUDE_SBOM_SPEND_REVIEW_001.json) | 1 | 1 | `20f0d41887` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_msfg_claude_sbo…` |
| [DETERMINEX_MSFG_CLAUDE_SCORE_MOVEMENT_EVIDENCE_BOUND_REVIEW_001](../locks/sentinel/DETERMINEX_MSFG_CLAUDE_SCORE_MOVEMENT_EVIDENCE_BOUND_REVIEW_001.json) | 1 | 1 | `20f0d41887` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_msfg_claude_sco…` |
| [DETERMINEX_MSFG_CLAUDE_SIGNED_SPEND_REVIEW_001](../locks/sentinel/DETERMINEX_MSFG_CLAUDE_SIGNED_SPEND_REVIEW_001.json) | 1 | 1 | `20f0d41887` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_msfg_claude_sig…` |
| [DETERMINEX_MSFG_CLAUDE_SYNTHESIS_REVIEW_001](../locks/sentinel/DETERMINEX_MSFG_CLAUDE_SYNTHESIS_REVIEW_001.json) | 1 | 1 | `20f0d41887` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_msfg_claude_syn…` |
| [DETERMINEX_MULTI_FAMILY_REPAIR_EXPANSION_LOCK_001](../locks/sentinel/DETERMINEX_MULTI_FAMILY_REPAIR_EXPANSION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_under…` |
| [DETERMINEX_NATIVE_WEBDRIVER_ADMISSION_FOR_TAURI_DRIVER_LOCK_001](../locks/sentinel/DETERMINEX_NATIVE_WEBDRIVER_ADMISSION_FOR_TAURI_DRIVER_LOCK_001.json) | 32 | 32 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_native_webdrive…` |
| [DETERMINEX_NEXT_CHEAP_RELEASE_CELL_CANDIDATE_QUEUE_LOCK_001](../locks/sentinel/DETERMINEX_NEXT_CHEAP_RELEASE_CELL_CANDIDATE_QUEUE_LOCK_001.json) | 28 | 28 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_next_cheap_rele…` |
| [DETERMINEX_NEXT_HARD_FLOOR_AUTHORITY_PACKET_SELECTION_LOCK_001](../locks/sentinel/DETERMINEX_NEXT_HARD_FLOOR_AUTHORITY_PACKET_SELECTION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_first_authority…` |
| [DETERMINEX_NEXT_HARD_FLOOR_PACKET_AFTER_FIRST_SPEND_LOCK_001](../locks/sentinel/DETERMINEX_NEXT_HARD_FLOOR_PACKET_AFTER_FIRST_SPEND_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_signature_spend…` |
| [DETERMINEX_NEXT_WAVE_CLAUDE_AUTHORITY_BOUNDARY_PRESERVATION_REVIEW_001](../locks/sentinel/DETERMINEX_NEXT_WAVE_CLAUDE_AUTHORITY_BOUNDARY_PRESERVATION_REVIEW_001.json) | 1 | 1 | `717ffbeb8f` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_next_wave_claud…` |
| [DETERMINEX_NEXT_WAVE_CLAUDE_FAMILY_SUPPORT_PROMOTION_REVIEW_001](../locks/sentinel/DETERMINEX_NEXT_WAVE_CLAUDE_FAMILY_SUPPORT_PROMOTION_REVIEW_001.json) | 1 | 1 | `717ffbeb8f` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_next_wave_claud…` |
| [DETERMINEX_NEXT_WAVE_CLAUDE_FIRST_SPEND_SYNTHESIS_REVIEW_001](../locks/sentinel/DETERMINEX_NEXT_WAVE_CLAUDE_FIRST_SPEND_SYNTHESIS_REVIEW_001.json) | 1 | 1 | `717ffbeb8f` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_next_wave_claud…` |
| [DETERMINEX_NEXT_WAVE_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001](../locks/sentinel/DETERMINEX_NEXT_WAVE_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001.json) | 1 | 1 | `717ffbeb8f` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_next_wave_claud…` |
| [DETERMINEX_NEXT_WAVE_CLAUDE_NEXT_HARD_FLOOR_PACKET_REVIEW_001](../locks/sentinel/DETERMINEX_NEXT_WAVE_CLAUDE_NEXT_HARD_FLOOR_PACKET_REVIEW_001.json) | 1 | 1 | `717ffbeb8f` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_next_wave_claud…` |
| [DETERMINEX_NEXT_WAVE_CLAUDE_REACT_VITE_ADMISSION_VERDICT_REVIEW_001](../locks/sentinel/DETERMINEX_NEXT_WAVE_CLAUDE_REACT_VITE_ADMISSION_VERDICT_REVIEW_001.json) | 1 | 1 | `717ffbeb8f` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_next_wave_claud…` |
| [DETERMINEX_NEXT_WAVE_CLAUDE_REACT_VITE_PACKET_VALIDATION_REVIEW_001](../locks/sentinel/DETERMINEX_NEXT_WAVE_CLAUDE_REACT_VITE_PACKET_VALIDATION_REVIEW_001.json) | 1 | 1 | `717ffbeb8f` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_next_wave_claud…` |
| [DETERMINEX_NEXT_WAVE_CLAUDE_REACT_VITE_TRANSCRIPT_REVIEW_001](../locks/sentinel/DETERMINEX_NEXT_WAVE_CLAUDE_REACT_VITE_TRANSCRIPT_REVIEW_001.json) | 1 | 1 | `717ffbeb8f` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_next_wave_claud…` |
| [DETERMINEX_NEXT_WAVE_CLAUDE_SCORE_BASELINE_RECONCILIATION_REVIEW_001](../locks/sentinel/DETERMINEX_NEXT_WAVE_CLAUDE_SCORE_BASELINE_RECONCILIATION_REVIEW_001.json) | 1 | 1 | `717ffbeb8f` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_next_wave_claud…` |
| [DETERMINEX_NEXT_WAVE_CLAUDE_SCORE_MOVEMENT_EVIDENCE_REVIEW_001](../locks/sentinel/DETERMINEX_NEXT_WAVE_CLAUDE_SCORE_MOVEMENT_EVIDENCE_REVIEW_001.json) | 1 | 1 | `717ffbeb8f` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_next_wave_claud…` |
| [DETERMINEX_NEXT_WAVE_CLAUDE_SIGNED_APPROVAL_VERDICT_REVIEW_001](../locks/sentinel/DETERMINEX_NEXT_WAVE_CLAUDE_SIGNED_APPROVAL_VERDICT_REVIEW_001.json) | 1 | 1 | `717ffbeb8f` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_next_wave_claud…` |
| [DETERMINEX_NEXT_WAVE_CLAUDE_SIGNED_SPEND_COUNT_REVIEW_001](../locks/sentinel/DETERMINEX_NEXT_WAVE_CLAUDE_SIGNED_SPEND_COUNT_REVIEW_001.json) | 1 | 1 | `717ffbeb8f` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_next_wave_claud…` |
| [DETERMINEX_NEXT_WAVE_CLAUDE_TIER1_COVERAGE_REVIEW_001](../locks/sentinel/DETERMINEX_NEXT_WAVE_CLAUDE_TIER1_COVERAGE_REVIEW_001.json) | 1 | 1 | `717ffbeb8f` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_next_wave_claud…` |
| [DETERMINEX_NEXT_WAVE_CLAUDE_TIMER_AND_MARKER_REVIEW_001](../locks/sentinel/DETERMINEX_NEXT_WAVE_CLAUDE_TIMER_AND_MARKER_REVIEW_001.json) | 1 | 1 | `717ffbeb8f` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_next_wave_claud…` |
| [DETERMINEX_NEXT_WAVE_REVIEW_READY_PROTOCOL_LOCK_001](../locks/sentinel/DETERMINEX_NEXT_WAVE_REVIEW_READY_PROTOCOL_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_first_authority…` |
| [DETERMINEX_NIGHT_CLAUDE_OVERNIGHT_FINAL_SYNTHESIS_001](../locks/sentinel/DETERMINEX_NIGHT_CLAUDE_OVERNIGHT_FINAL_SYNTHESIS_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_night_claude_ov…` |
| [DETERMINEX_NIGHT_CLAUDE_SYNTHESIS_AND_CODEX_PRESSURE_QUEUE_001](../locks/sentinel/DETERMINEX_NIGHT_CLAUDE_SYNTHESIS_AND_CODEX_PRESSURE_QUEUE_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_night_claude_sy…` |
| [DETERMINEX_NIGHT_CLAUDE_SYNTHESIS_AND_CODEX_PRESSURE_QUEUE_002](../locks/sentinel/DETERMINEX_NIGHT_CLAUDE_SYNTHESIS_AND_CODEX_PRESSURE_QUEUE_002.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_night_claude_sy…` |
| [DETERMINEX_NIGHT_CLAUDE_SYNTHESIS_AND_CODEX_PRESSURE_QUEUE_003](../locks/sentinel/DETERMINEX_NIGHT_CLAUDE_SYNTHESIS_AND_CODEX_PRESSURE_QUEUE_003.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_night_claude_sy…` |
| [DETERMINEX_NIGHT_GULP_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_NIGHT_GULP_RECONCILIATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_NIGHT_GULP_RECONCILIATION_LOCK_002](../locks/sentinel/DETERMINEX_NIGHT_GULP_RECONCILIATION_LOCK_002.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_NIGHT_GULP_RECONCILIATION_LOCK_003](../locks/sentinel/DETERMINEX_NIGHT_GULP_RECONCILIATION_LOCK_003.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_NIGHT_GULP_RECONCILIATION_LOCK_004](../locks/sentinel/DETERMINEX_NIGHT_GULP_RECONCILIATION_LOCK_004.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_NONCODER_PRODUCT_REPORT_COMPLETION_LOCK_001](../locks/sentinel/DETERMINEX_NONCODER_PRODUCT_REPORT_COMPLETION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_under…` |
| [DETERMINEX_NONCODER_PROGRAM_AUTHORITY_REPORT_LOCK_002](../locks/sentinel/DETERMINEX_NONCODER_PROGRAM_AUTHORITY_REPORT_LOCK_002.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_NONCODER_PROGRAM_PROOF_REPORT_LOCK_001](../locks/sentinel/DETERMINEX_NONCODER_PROGRAM_PROOF_REPORT_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_NONCODER_RELEASE_READINESS_REPORT_LOCK_001](../locks/sentinel/DETERMINEX_NONCODER_RELEASE_READINESS_REPORT_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_NONCODER_REPORT_RENDERED_OUTPUTS_VERIFIED_LOCK_001](../locks/sentinel/DETERMINEX_NONCODER_REPORT_RENDERED_OUTPUTS_VERIFIED_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_NO_SUCCESS_WITHOUT_VERIFIER_POLICY_LOCK_001](../locks/sentinel/DETERMINEX_NO_SUCCESS_WITHOUT_VERIFIER_POLICY_LOCK_001.json) | 17 | 17 | `cd3a6d5322` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_determinex_unified…` |
| [DETERMINEX_NSIS_BOUNDED_EXTRACT_OR_OPERATOR_INSTALL_UNINSTALL_LOCK_001](../locks/sentinel/DETERMINEX_NSIS_BOUNDED_EXTRACT_OR_OPERATOR_INSTALL_UNINSTALL_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_nsis_bounded_ex…` |
| [DETERMINEX_NSIS_INSTALLER_EXECUTION_READINESS_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_NSIS_INSTALLER_EXECUTION_READINESS_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_nsis_installer_…` |
| [DETERMINEX_NSIS_INSTALL_SMOKE_EXECUTION_IF_SIGNED_LOCK_001](../locks/sentinel/DETERMINEX_NSIS_INSTALL_SMOKE_EXECUTION_IF_SIGNED_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_NSIS_INSTALL_SMOKE_WITH_RUNTIME_APPROVAL_LOCK_001](../locks/sentinel/DETERMINEX_NSIS_INSTALL_SMOKE_WITH_RUNTIME_APPROVAL_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_NSIS_OPERATOR_APPROVED_INSTALL_LAUNCH_UNINSTALL_SMOKE_LOCK_001](../locks/sentinel/DETERMINEX_NSIS_OPERATOR_APPROVED_INSTALL_LAUNCH_UNINSTALL_SMOKE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_nsis_operator_a…` |
| [DETERMINEX_NSIS_OPERATOR_APPROVED_INSTALL_UNINSTALL_SMOKE_LOCK_001](../locks/sentinel/DETERMINEX_NSIS_OPERATOR_APPROVED_INSTALL_UNINSTALL_SMOKE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_nsis_operator_a…` |
| [DETERMINEX_NSIS_SINGLE_EVENT_APPROVAL_AND_INSTALL_LAUNCH_UNINSTALL_EXECUTION_LOCK_001](../locks/sentinel/DETERMINEX_NSIS_SINGLE_EVENT_APPROVAL_AND_INSTALL_LAUNCH_UNINSTALL_EXECUTION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_nsis_single_eve…` |
| [DETERMINEX_OARG_CLAUDE_APPEND_ONLY_COUNT_DRIFT_GUARDS_REVIEW_001](../locks/sentinel/DETERMINEX_OARG_CLAUDE_APPEND_ONLY_COUNT_DRIFT_GUARDS_REVIEW_001.json) | 1 | 1 | `846bb1d14e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_oarg_claude_app…` |
| [DETERMINEX_OARG_CLAUDE_BETA_DASHBOARD_NO_PUBLIC_RELEASE_REVIEW_001](../locks/sentinel/DETERMINEX_OARG_CLAUDE_BETA_DASHBOARD_NO_PUBLIC_RELEASE_REVIEW_001.json) | 1 | 1 | `846bb1d14e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_oarg_claude_bet…` |
| [DETERMINEX_OARG_CLAUDE_CLAIM_SCANNER_OVERCLAIM_REVIEW_001](../locks/sentinel/DETERMINEX_OARG_CLAUDE_CLAIM_SCANNER_OVERCLAIM_REVIEW_001.json) | 1 | 1 | `846bb1d14e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_oarg_claude_cla…` |
| [DETERMINEX_OARG_CLAUDE_CLEAN_HOST_IN_SCOPE_OR_BLOCKED_REVIEW_001](../locks/sentinel/DETERMINEX_OARG_CLAUDE_CLEAN_HOST_IN_SCOPE_OR_BLOCKED_REVIEW_001.json) | 1 | 1 | `846bb1d14e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_oarg_claude_cle…` |
| [DETERMINEX_OARG_CLAUDE_DIRTY_STATE_REPORTED_REVIEW_001](../locks/sentinel/DETERMINEX_OARG_CLAUDE_DIRTY_STATE_REPORTED_REVIEW_001.json) | 1 | 1 | `846bb1d14e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_oarg_claude_dir…` |
| [DETERMINEX_OARG_CLAUDE_EVIDENCE_INDEX_CLEAN_REVIEW_001](../locks/sentinel/DETERMINEX_OARG_CLAUDE_EVIDENCE_INDEX_CLEAN_REVIEW_001.json) | 1 | 1 | `846bb1d14e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_oarg_claude_evi…` |
| [DETERMINEX_OARG_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001](../locks/sentinel/DETERMINEX_OARG_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001.json) | 1 | 1 | `846bb1d14e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_oarg_claude_for…` |
| [DETERMINEX_OARG_CLAUDE_GUI_BUILD_IN_SCOPE_OR_BLOCKED_REVIEW_001](../locks/sentinel/DETERMINEX_OARG_CLAUDE_GUI_BUILD_IN_SCOPE_OR_BLOCKED_REVIEW_001.json) | 1 | 1 | `846bb1d14e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_oarg_claude_gui…` |
| [DETERMINEX_OARG_CLAUDE_INSTALLER_RELEASE_IN_SCOPE_OR_BLOCKED_REVIEW_001](../locks/sentinel/DETERMINEX_OARG_CLAUDE_INSTALLER_RELEASE_IN_SCOPE_OR_BLOCKED_REVIEW_001.json) | 1 | 1 | `846bb1d14e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_oarg_claude_ins…` |
| [DETERMINEX_OARG_CLAUDE_NO_FAKE_SIGNATURE_OR_APPROVAL_REVIEW_001](../locks/sentinel/DETERMINEX_OARG_CLAUDE_NO_FAKE_SIGNATURE_OR_APPROVAL_REVIEW_001.json) | 1 | 1 | `846bb1d14e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_oarg_claude_no_…` |
| [DETERMINEX_OARG_CLAUDE_NO_FAMILY_SUPPORT_CLAIM_REVIEW_001](../locks/sentinel/DETERMINEX_OARG_CLAUDE_NO_FAMILY_SUPPORT_CLAIM_REVIEW_001.json) | 1 | 1 | `846bb1d14e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_oarg_claude_no_…` |
| [DETERMINEX_OARG_CLAUDE_NO_PROTECTED_ACTION_WITHOUT_PACKET_SPEND_REVIEW_001](../locks/sentinel/DETERMINEX_OARG_CLAUDE_NO_PROTECTED_ACTION_WITHOUT_PACKET_SPEND_REVIEW_001.json) | 1 | 1 | `846bb1d14e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_oarg_claude_no_…` |
| [DETERMINEX_OARG_CLAUDE_NO_RELEASE_READY_WITHOUT_GATES_REVIEW_001](../locks/sentinel/DETERMINEX_OARG_CLAUDE_NO_RELEASE_READY_WITHOUT_GATES_REVIEW_001.json) | 1 | 1 | `846bb1d14e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_oarg_claude_no_…` |
| [DETERMINEX_OARG_CLAUDE_NO_VALIDATOR_BYPASS_REVIEW_001](../locks/sentinel/DETERMINEX_OARG_CLAUDE_NO_VALIDATOR_BYPASS_REVIEW_001.json) | 1 | 1 | `846bb1d14e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_oarg_claude_no_…` |
| [DETERMINEX_OARG_CLAUDE_OP_AUTH_MATERIALIZED_AS_MACHINE_CHECKABLE_REVIEW_001](../locks/sentinel/DETERMINEX_OARG_CLAUDE_OP_AUTH_MATERIALIZED_AS_MACHINE_CHECKABLE_REVIEW_001.json) | 1 | 1 | `846bb1d14e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_oarg_claude_op_…` |
| [DETERMINEX_OARG_CLAUDE_PACKETS_SCOPED_ONE_ACTION_REVIEW_001](../locks/sentinel/DETERMINEX_OARG_CLAUDE_PACKETS_SCOPED_ONE_ACTION_REVIEW_001.json) | 1 | 1 | `846bb1d14e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_oarg_claude_pac…` |
| [DETERMINEX_OARG_CLAUDE_PACKET_HASH_BINDING_REVIEW_001](../locks/sentinel/DETERMINEX_OARG_CLAUDE_PACKET_HASH_BINDING_REVIEW_001.json) | 1 | 1 | `846bb1d14e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_oarg_claude_pac…` |
| [DETERMINEX_OARG_CLAUDE_QUEUE_ONLY_FROM_VALID_PACKETS_REVIEW_001](../locks/sentinel/DETERMINEX_OARG_CLAUDE_QUEUE_ONLY_FROM_VALID_PACKETS_REVIEW_001.json) | 1 | 1 | `846bb1d14e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_oarg_claude_que…` |
| [DETERMINEX_OARG_CLAUDE_REACT_VITE_IN_SCOPE_REVIEW_001](../locks/sentinel/DETERMINEX_OARG_CLAUDE_REACT_VITE_IN_SCOPE_REVIEW_001.json) | 1 | 1 | `846bb1d14e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_oarg_claude_rea…` |
| [DETERMINEX_OARG_CLAUDE_REJECTION_CORPUS_COVERAGE_REVIEW_001](../locks/sentinel/DETERMINEX_OARG_CLAUDE_REJECTION_CORPUS_COVERAGE_REVIEW_001.json) | 1 | 1 | `846bb1d14e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_oarg_claude_rej…` |
| [DETERMINEX_OARG_CLAUDE_RELEASE_CELLS_CANONICAL_REVIEW_001](../locks/sentinel/DETERMINEX_OARG_CLAUDE_RELEASE_CELLS_CANONICAL_REVIEW_001.json) | 1 | 1 | `846bb1d14e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_oarg_claude_rel…` |
| [DETERMINEX_OARG_CLAUDE_RELEASE_FAMILIES_CANONICAL_REVIEW_001](../locks/sentinel/DETERMINEX_OARG_CLAUDE_RELEASE_FAMILIES_CANONICAL_REVIEW_001.json) | 1 | 1 | `846bb1d14e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_oarg_claude_rel…` |
| [DETERMINEX_OARG_CLAUDE_SBOM_IN_SCOPE_OR_BLOCKED_REVIEW_001](../locks/sentinel/DETERMINEX_OARG_CLAUDE_SBOM_IN_SCOPE_OR_BLOCKED_REVIEW_001.json) | 1 | 1 | `846bb1d14e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_oarg_claude_sbo…` |
| [DETERMINEX_OARG_CLAUDE_SCORE_CHANGES_EVIDENCE_BOUND_REVIEW_001](../locks/sentinel/DETERMINEX_OARG_CLAUDE_SCORE_CHANGES_EVIDENCE_BOUND_REVIEW_001.json) | 1 | 1 | `846bb1d14e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_oarg_claude_sco…` |
| [DETERMINEX_OARG_CLAUDE_SPEND_ONE_TIME_USE_REVIEW_001](../locks/sentinel/DETERMINEX_OARG_CLAUDE_SPEND_ONE_TIME_USE_REVIEW_001.json) | 1 | 1 | `846bb1d14e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_oarg_claude_spe…` |
| [DETERMINEX_OARG_CLAUDE_SYNTHESIS_REVIEW_001](../locks/sentinel/DETERMINEX_OARG_CLAUDE_SYNTHESIS_REVIEW_001.json) | 1 | 1 | `846bb1d14e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_oarg_claude_syn…` |
| [DETERMINEX_OARG_CLAUDE_TIMEOUT_NOT_HIDDEN_BY_SKIPS_REVIEW_001](../locks/sentinel/DETERMINEX_OARG_CLAUDE_TIMEOUT_NOT_HIDDEN_BY_SKIPS_REVIEW_001.json) | 1 | 1 | `846bb1d14e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_oarg_claude_tim…` |
| [DETERMINEX_OMG_DEMO_EXECUTION_METHODOLOGY_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_OMG_DEMO_EXECUTION_METHODOLOGY_RECONCILIATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_OMG_DEMO_PATH_END_TO_END_SCRIPT_LOCK_001](../locks/sentinel/DETERMINEX_OMG_DEMO_PATH_END_TO_END_SCRIPT_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_omg_demo_path_e…` |
| [DETERMINEX_OMG_DEMO_PATH_EXECUTION_CLAUDE_REVIEW_002](../locks/sentinel/DETERMINEX_OMG_DEMO_PATH_EXECUTION_CLAUDE_REVIEW_002.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_omg_demo_path_e…` |
| [DETERMINEX_OMG_DEMO_PATH_EXECUTION_LOCK_002](../locks/sentinel/DETERMINEX_OMG_DEMO_PATH_EXECUTION_LOCK_002.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_OMG_DEMO_SCORE_METHODOLOGY_ATTACK_REVIEW_CLAUDE_001](../locks/sentinel/DETERMINEX_OMG_DEMO_SCORE_METHODOLOGY_ATTACK_REVIEW_CLAUDE_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_007_omg_de…` |
| [DETERMINEX_OMG_FIVE_FIELD_SCORE_SCHEMA_AND_QUOTING_LINTER_LOCK_001](../locks/sentinel/DETERMINEX_OMG_FIVE_FIELD_SCORE_SCHEMA_AND_QUOTING_LINTER_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_OMG_FIVE_FIELD_SCORE_TIGHTENING_LOCK_001](../locks/sentinel/DETERMINEX_OMG_FIVE_FIELD_SCORE_TIGHTENING_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_OMG_SCORE_DEFINITION_BINDING_AND_LINTER_EXPANSION_LOCK_001](../locks/sentinel/DETERMINEX_OMG_SCORE_DEFINITION_BINDING_AND_LINTER_EXPANSION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_ONNXRUNTIME_LOCAL_IMPORT_LIB_GENERATION_LOCK_001](../locks/sentinel/DETERMINEX_ONNXRUNTIME_LOCAL_IMPORT_LIB_GENERATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_onnxruntime_loc…` |
| [DETERMINEX_ONNXRUNTIME_NATIVE_LINKAGE_REQUIREMENTS_LOCK_001](../locks/sentinel/DETERMINEX_ONNXRUNTIME_NATIVE_LINKAGE_REQUIREMENTS_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_onnxruntime_nat…` |
| [DETERMINEX_ONNXRUNTIME_RUNTIME_API_ALIGNMENT_LOCK_001](../locks/sentinel/DETERMINEX_ONNXRUNTIME_RUNTIME_API_ALIGNMENT_LOCK_001.json) | 14 | 917 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_onnxruntime_run…` |
| [DETERMINEX_OPEN_AVAILABILITY_ASCENT_MASTER_PLAN_LOCK_001](../locks/sentinel/DETERMINEX_OPEN_AVAILABILITY_ASCENT_MASTER_PLAN_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_open_availabili…` |
| [DETERMINEX_OPEN_AVAILABILITY_PARALLEL_RELEASE_CRITIQUE_AND_CLAUDE_QUEUE_001](../locks/sentinel/DETERMINEX_OPEN_AVAILABILITY_PARALLEL_RELEASE_CRITIQUE_AND_CLAUDE_QUEUE_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_open_availabili…` |
| [DETERMINEX_OPERATOR_ACTION_PACKET_FOR_FIRST_SPEND_LOCK_001](../locks/sentinel/DETERMINEX_OPERATOR_ACTION_PACKET_FOR_FIRST_SPEND_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_OPERATOR_APPROVAL_SIGNATURE_LEDGER_GENERALIZATION_LOCK_001](../locks/sentinel/DETERMINEX_OPERATOR_APPROVAL_SIGNATURE_LEDGER_GENERALIZATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_operator_approv…` |
| [DETERMINEX_OPERATOR_AUTHORITY_RELEASE_GATE_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_OPERATOR_AUTHORITY_RELEASE_GATE_RECONCILIATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_OPERATOR_AUTHORIZATION_MATERIALIZATION_LOCK_001](../locks/sentinel/DETERMINEX_OPERATOR_AUTHORIZATION_MATERIALIZATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_OPERATOR_DECISION_LEDGER_AND_SINGLE_EVENT_APPROVAL_LOCK_001](../locks/sentinel/DETERMINEX_OPERATOR_DECISION_LEDGER_AND_SINGLE_EVENT_APPROVAL_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_operator_decisi…` |
| [DETERMINEX_OPERATOR_SIGNATURE_CAPTURE_MECHANISM_COMPLETION_LOCK_001](../locks/sentinel/DETERMINEX_OPERATOR_SIGNATURE_CAPTURE_MECHANISM_COMPLETION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_OPERATOR_SIGNATURE_CAPTURE_MECHANISM_LOCK_001](../locks/sentinel/DETERMINEX_OPERATOR_SIGNATURE_CAPTURE_MECHANISM_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_OPERATOR_SIGNATURE_CAPTURE_MECHANISM_LOCK_002](../locks/sentinel/DETERMINEX_OPERATOR_SIGNATURE_CAPTURE_MECHANISM_LOCK_002.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_OPERATOR_SIGNATURE_DELIVERY_CHANNEL_LOCK_001](../locks/sentinel/DETERMINEX_OPERATOR_SIGNATURE_DELIVERY_CHANNEL_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_signature_deliv…` |
| [DETERMINEX_OPERATOR_SIGNATURE_MATERIAL_TEMPLATE_LOCK_001](../locks/sentinel/DETERMINEX_OPERATOR_SIGNATURE_MATERIAL_TEMPLATE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_signature_deliv…` |
| [DETERMINEX_OPERATOR_SIGNATURE_MATERIAL_VALIDATOR_LOCK_001](../locks/sentinel/DETERMINEX_OPERATOR_SIGNATURE_MATERIAL_VALIDATOR_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_signature_deliv…` |
| [DETERMINEX_OPERATOR_SIGNATURE_MECHANISM_ATTACK_REVIEW_CLAUDE_001](../locks/sentinel/DETERMINEX_OPERATOR_SIGNATURE_MECHANISM_ATTACK_REVIEW_CLAUDE_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_007_operat…` |
| [DETERMINEX_OPERATOR_SIGNATURE_MECHANISM_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_OPERATOR_SIGNATURE_MECHANISM_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_operator_signat…` |
| [DETERMINEX_OPERATOR_TOOL_ACQUISITION_AUTHORIZATION_LOCK_001](../locks/sentinel/DETERMINEX_OPERATOR_TOOL_ACQUISITION_AUTHORIZATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_OPTIONAL_REAL_SIGNATURE_QUEUE_IMPORT_LOCK_001](../locks/sentinel/DETERMINEX_OPTIONAL_REAL_SIGNATURE_QUEUE_IMPORT_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_signature_deliv…` |
| [DETERMINEX_OPTIONAL_VECTOR_ENGINE_STARTUP_GUARD_LOCK_001](../locks/sentinel/DETERMINEX_OPTIONAL_VECTOR_ENGINE_STARTUP_GUARD_LOCK_001.json) | 12 | 903 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_optional_vector…` |
| [DETERMINEX_ORACLE_REGISTRY_COMPLETION_LOCK_001](../locks/sentinel/DETERMINEX_ORACLE_REGISTRY_COMPLETION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_under…` |
| [DETERMINEX_OVERNIGHT_BROWSER_TAURI_GUI_PACKET_STAGE_LOCK_001](../locks/sentinel/DETERMINEX_OVERNIGHT_BROWSER_TAURI_GUI_PACKET_STAGE_LOCK_001.json) | 10 | 10 | `5f55031806` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_7_hou…` |
| [DETERMINEX_OVERNIGHT_CLAIM_SCANNER_PUBLIC_NARRATIVE_HARDENING_LOCK_001](../locks/sentinel/DETERMINEX_OVERNIGHT_CLAIM_SCANNER_PUBLIC_NARRATIVE_HARDENING_LOCK_001.json) | 10 | 10 | `5f55031806` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_7_hou…` |
| [DETERMINEX_OVERNIGHT_CLAUDE_ALL_FAMILY_ADAPTER_STUB_COVERAGE_REVIEW_001](../locks/sentinel/DETERMINEX_OVERNIGHT_CLAUDE_ALL_FAMILY_ADAPTER_STUB_COVERAGE_REVIEW_001.json) | 1 | 1 | `deb544e5db` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_claud…` |
| [DETERMINEX_OVERNIGHT_CLAUDE_AUTHORITY_BOUNDARY_PRESERVATION_REVIEW_001](../locks/sentinel/DETERMINEX_OVERNIGHT_CLAUDE_AUTHORITY_BOUNDARY_PRESERVATION_REVIEW_001.json) | 1 | 1 | `deb544e5db` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_claud…` |
| [DETERMINEX_OVERNIGHT_CLAUDE_CURRENT_STATE_SOURCE_TRUTH_REVIEW_001](../locks/sentinel/DETERMINEX_OVERNIGHT_CLAUDE_CURRENT_STATE_SOURCE_TRUTH_REVIEW_001.json) | 1 | 1 | `deb544e5db` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_claud…` |
| [DETERMINEX_OVERNIGHT_CLAUDE_DAY1_IDE_DASHBOARD_REVIEW_001](../locks/sentinel/DETERMINEX_OVERNIGHT_CLAUDE_DAY1_IDE_DASHBOARD_REVIEW_001.json) | 1 | 1 | `deb544e5db` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_claud…` |
| [DETERMINEX_OVERNIGHT_CLAUDE_EXTERNAL_AUTHORITY_PACKET_REVIEW_001](../locks/sentinel/DETERMINEX_OVERNIGHT_CLAUDE_EXTERNAL_AUTHORITY_PACKET_REVIEW_001.json) | 1 | 1 | `deb544e5db` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_claud…` |
| [DETERMINEX_OVERNIGHT_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001](../locks/sentinel/DETERMINEX_OVERNIGHT_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001.json) | 1 | 1 | `deb544e5db` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_claud…` |
| [DETERMINEX_OVERNIGHT_CLAUDE_IDEA_LAB_E2E_PIPELINE_REVIEW_001](../locks/sentinel/DETERMINEX_OVERNIGHT_CLAUDE_IDEA_LAB_E2E_PIPELINE_REVIEW_001.json) | 1 | 1 | `deb544e5db` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_claud…` |
| [DETERMINEX_OVERNIGHT_CLAUDE_MULTI_FAMILY_REPAIR_EXPANSION_REVIEW_001](../locks/sentinel/DETERMINEX_OVERNIGHT_CLAUDE_MULTI_FAMILY_REPAIR_EXPANSION_REVIEW_001.json) | 1 | 1 | `deb544e5db` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_claud…` |
| [DETERMINEX_OVERNIGHT_CLAUDE_NONCODER_PRODUCT_REPORT_REVIEW_001](../locks/sentinel/DETERMINEX_OVERNIGHT_CLAUDE_NONCODER_PRODUCT_REPORT_REVIEW_001.json) | 1 | 1 | `deb544e5db` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_claud…` |
| [DETERMINEX_OVERNIGHT_CLAUDE_ORACLE_REGISTRY_COMPLETION_REVIEW_001](../locks/sentinel/DETERMINEX_OVERNIGHT_CLAUDE_ORACLE_REGISTRY_COMPLETION_REVIEW_001.json) | 1 | 1 | `deb544e5db` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_claud…` |
| [DETERMINEX_OVERNIGHT_CLAUDE_OVERCLAIM_SCANNER_HARDENING_REVIEW_001](../locks/sentinel/DETERMINEX_OVERNIGHT_CLAUDE_OVERCLAIM_SCANNER_HARDENING_REVIEW_001.json) | 1 | 1 | `deb544e5db` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_claud…` |
| [DETERMINEX_OVERNIGHT_CLAUDE_REPO_CLINIC_E2E_PIPELINE_REVIEW_001](../locks/sentinel/DETERMINEX_OVERNIGHT_CLAUDE_REPO_CLINIC_E2E_PIPELINE_REVIEW_001.json) | 1 | 1 | `deb544e5db` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_claud…` |
| [DETERMINEX_OVERNIGHT_CLAUDE_REVIEW_READY_PROTOCOL_REVIEW_001](../locks/sentinel/DETERMINEX_OVERNIGHT_CLAUDE_REVIEW_READY_PROTOCOL_REVIEW_001.json) | 1 | 1 | `deb544e5db` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_claud…` |
| [DETERMINEX_OVERNIGHT_CLAUDE_SCORE_MOVEMENT_EVIDENCE_REVIEW_001](../locks/sentinel/DETERMINEX_OVERNIGHT_CLAUDE_SCORE_MOVEMENT_EVIDENCE_REVIEW_001.json) | 1 | 1 | `deb544e5db` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_claud…` |
| [DETERMINEX_OVERNIGHT_CLAUDE_TIER1_PROGRAM_FAMILY_COVERAGE_REVIEW_001](../locks/sentinel/DETERMINEX_OVERNIGHT_CLAUDE_TIER1_PROGRAM_FAMILY_COVERAGE_REVIEW_001.json) | 1 | 1 | `deb544e5db` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_claud…` |
| [DETERMINEX_OVERNIGHT_CLAUDE_UNDER_THE_HOOD_SYNTHESIS_REVIEW_001](../locks/sentinel/DETERMINEX_OVERNIGHT_CLAUDE_UNDER_THE_HOOD_SYNTHESIS_REVIEW_001.json) | 1 | 1 | `deb544e5db` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_claud…` |
| [DETERMINEX_OVERNIGHT_CLEAN_RUNNER_SBOM_CONTINUITY_LOCK_001](../locks/sentinel/DETERMINEX_OVERNIGHT_CLEAN_RUNNER_SBOM_CONTINUITY_LOCK_001.json) | 10 | 10 | `5f55031806` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_7_hou…` |
| [DETERMINEX_OVERNIGHT_COMPANION_RAG_BOUNDARY_RECHECK_LOCK_001](../locks/sentinel/DETERMINEX_OVERNIGHT_COMPANION_RAG_BOUNDARY_RECHECK_LOCK_001.json) | 1 | 1 | `90971e6528` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_companion_rag_a…` |
| [DETERMINEX_OVERNIGHT_COORDINATION_STATUS_LOCK_001](../locks/sentinel/DETERMINEX_OVERNIGHT_COORDINATION_STATUS_LOCK_001.json) | 10 | 10 | `5f55031806` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_7_hou…` |
| [DETERMINEX_OVERNIGHT_FULL_STATUS_SEGMENT_EXECUTION_LOCK_001](../locks/sentinel/DETERMINEX_OVERNIGHT_FULL_STATUS_SEGMENT_EXECUTION_LOCK_001.json) | 10 | 10 | `5f55031806` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_7_hou…` |
| [DETERMINEX_OVERNIGHT_HIGH_RISK_FAMILY_AUTHORITY_PACKET_LOCK_001](../locks/sentinel/DETERMINEX_OVERNIGHT_HIGH_RISK_FAMILY_AUTHORITY_PACKET_LOCK_001.json) | 10 | 10 | `5f55031806` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_7_hou…` |
| [DETERMINEX_OVERNIGHT_INSTALLER_RELEASE_PACKET_PREPARATION_LOCK_001](../locks/sentinel/DETERMINEX_OVERNIGHT_INSTALLER_RELEASE_PACKET_PREPARATION_LOCK_001.json) | 10 | 10 | `6349cd7a0a` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_7_hou…` |
| [DETERMINEX_OVERNIGHT_KNOWN_WORLD_DETECTOR_SEGMENT_2_LOCK_001](../locks/sentinel/DETERMINEX_OVERNIGHT_KNOWN_WORLD_DETECTOR_SEGMENT_2_LOCK_001.json) | 10 | 10 | `5f55031806` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_7_hou…` |
| [DETERMINEX_OVERNIGHT_KNOWN_WORLD_DETECTOR_SEGMENT_3_LOCK_001](../locks/sentinel/DETERMINEX_OVERNIGHT_KNOWN_WORLD_DETECTOR_SEGMENT_3_LOCK_001.json) | 10 | 10 | `5f55031806` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_7_hou…` |
| [DETERMINEX_OVERNIGHT_PHP_RUBY_TOOLCHAIN_GATE_LOCK_001](../locks/sentinel/DETERMINEX_OVERNIGHT_PHP_RUBY_TOOLCHAIN_GATE_LOCK_001.json) | 10 | 10 | `5f55031806` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_7_hou…` |
| [DETERMINEX_OVERNIGHT_PROOF_DASHBOARD_OPERATOR_CENTER_READINESS_LOCK_001](../locks/sentinel/DETERMINEX_OVERNIGHT_PROOF_DASHBOARD_OPERATOR_CENTER_READINESS_LOCK_001.json) | 10 | 10 | `5f55031806` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_7_hou…` |
| [DETERMINEX_OVERNIGHT_RELEASE_CELL_CERTIFICATION_CANDIDATES_LOCK_001](../locks/sentinel/DETERMINEX_OVERNIGHT_RELEASE_CELL_CERTIFICATION_CANDIDATES_LOCK_001.json) | 10 | 10 | `5f55031806` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_7_hou…` |
| [DETERMINEX_OVERNIGHT_REVIEW_READY_PROTOCOL_LOCK_001](../locks/sentinel/DETERMINEX_OVERNIGHT_REVIEW_READY_PROTOCOL_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_under…` |
| [DETERMINEX_OVERNIGHT_SBOM_BYTE_NORMALIZATION_LOCK_001](../locks/sentinel/DETERMINEX_OVERNIGHT_SBOM_BYTE_NORMALIZATION_LOCK_001.json) | 10 | 10 | `5f55031806` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_7_hou…` |
| [DETERMINEX_OVERNIGHT_SCOPED_BROADER_SBOM_SEGMENTS_LOCK_001](../locks/sentinel/DETERMINEX_OVERNIGHT_SCOPED_BROADER_SBOM_SEGMENTS_LOCK_001.json) | 10 | 10 | `5f55031806` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_7_hou…` |
| [DETERMINEX_OVERNIGHT_T_DRIVE_CARGO_BUILD_CACHE_RELOCATION_LOCK_001](../locks/sentinel/DETERMINEX_OVERNIGHT_T_DRIVE_CARGO_BUILD_CACHE_RELOCATION_LOCK_001.json) | 10 | 10 | `5f55031806` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_7_hou…` |
| [DETERMINEX_OVERNIGHT_UNDER_THE_HOOD_COMPLETION_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_OVERNIGHT_UNDER_THE_HOOD_COMPLETION_RECONCILIATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_under…` |
| [DETERMINEX_PACKAGE_DRY_RUN_PUBLICATION_READINESS_HARDENING_LOCK_001](../locks/sentinel/DETERMINEX_PACKAGE_DRY_RUN_PUBLICATION_READINESS_HARDENING_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_PACKAGE_LICENSE_METADATA_HYGIENE_LOCK_001](../locks/sentinel/DETERMINEX_PACKAGE_LICENSE_METADATA_HYGIENE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_PACKAGE_LICENSE_METADATA_LOCAL_PREVIEW_BOUNDARY_LOCK_001](../locks/sentinel/DETERMINEX_PACKAGE_LICENSE_METADATA_LOCAL_PREVIEW_BOUNDARY_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_014_signed…` |
| [DETERMINEX_PACKAGE_LOCKFILE_MUTATION_BOUNDARY_GUARD_LOCK_001](../locks/sentinel/DETERMINEX_PACKAGE_LOCKFILE_MUTATION_BOUNDARY_GUARD_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_PACKAGE_METADATA_LICENSE_README_BOUNDARY_COMPLETION_LOCK_001](../locks/sentinel/DETERMINEX_PACKAGE_METADATA_LICENSE_README_BOUNDARY_COMPLETION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_015_canoni…` |
| [DETERMINEX_PACKAGING_FRESH_INSTALL_REQUIREMENTS_NORMALIZATION_LOCK_001](../locks/sentinel/DETERMINEX_PACKAGING_FRESH_INSTALL_REQUIREMENTS_NORMALIZATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_packaging_fresh…` |
| [DETERMINEX_PACKAGING_NATIVE_PROOF_OPEN_AVAILABILITY_CLAUDE_CRITIQUE_001](../locks/sentinel/DETERMINEX_PACKAGING_NATIVE_PROOF_OPEN_AVAILABILITY_CLAUDE_CRITIQUE_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_packaging_nativ…` |
| [DETERMINEX_PACKET_RUNTIME_FIRST_ONE_TIME_SPEND_LOCK_001](../locks/sentinel/DETERMINEX_PACKET_RUNTIME_FIRST_ONE_TIME_SPEND_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_PACKET_RUNTIME_FIRST_QUEUE_ADMISSION_LOCK_001](../locks/sentinel/DETERMINEX_PACKET_RUNTIME_FIRST_QUEUE_ADMISSION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_PACKET_RUNTIME_FULL_STATUS_TIMEOUT_REPAIR_CONTINUATION_LOCK_001](../locks/sentinel/DETERMINEX_PACKET_RUNTIME_FULL_STATUS_TIMEOUT_REPAIR_CONTINUATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_PACKET_RUNTIME_OTHER_PACKET_STATUS_REPORT_LOCK_001](../locks/sentinel/DETERMINEX_PACKET_RUNTIME_OTHER_PACKET_STATUS_REPORT_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_PACKET_RUNTIME_PACKET_DISCOVERY_HASH_VERIFICATION_LOCK_001](../locks/sentinel/DETERMINEX_PACKET_RUNTIME_PACKET_DISCOVERY_HASH_VERIFICATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_PACKET_RUNTIME_POST_SPEND_VERIFICATION_LOCK_001](../locks/sentinel/DETERMINEX_PACKET_RUNTIME_POST_SPEND_VERIFICATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_PACKET_RUNTIME_QUEUE_ADMISSION_BRIDGE_LOCK_001](../locks/sentinel/DETERMINEX_PACKET_RUNTIME_QUEUE_ADMISSION_BRIDGE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_PACKET_RUNTIME_REACT_VITE_SCOPED_EXECUTION_LOCK_001](../locks/sentinel/DETERMINEX_PACKET_RUNTIME_REACT_VITE_SCOPED_EXECUTION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_PACKET_RUNTIME_RECONCILIATION_SCORE_DISCIPLINE_LOCK_001](../locks/sentinel/DETERMINEX_PACKET_RUNTIME_RECONCILIATION_SCORE_DISCIPLINE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_PER_FAMILY_BUILD_TEST_SMOKE_COMMAND_MAPPING_LOCK_001](../locks/sentinel/DETERMINEX_PER_FAMILY_BUILD_TEST_SMOKE_COMMAND_MAPPING_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_PER_FAMILY_FIXTURE_ROUTE_EXECUTION_TESTS_LOCK_001](../locks/sentinel/DETERMINEX_PER_FAMILY_FIXTURE_ROUTE_EXECUTION_TESTS_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_014_signed…` |
| [DETERMINEX_PER_FAMILY_SAFE_FIXTURE_EXECUTION_EXPANSION_LOCK_001](../locks/sentinel/DETERMINEX_PER_FAMILY_SAFE_FIXTURE_EXECUTION_EXPANSION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_015_canoni…` |
| [DETERMINEX_PHP_STRUCTURAL_MAPPING_BOUNDARY_GUARD_LOCK_001](../locks/sentinel/DETERMINEX_PHP_STRUCTURAL_MAPPING_BOUNDARY_GUARD_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_PHP_TOOLCHAIN_ABSENCE_GATE_LOCK_001](../locks/sentinel/DETERMINEX_PHP_TOOLCHAIN_ABSENCE_GATE_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_PLAYWRIGHT_TAURI_DRIVER_HARNESS_ADMISSION_LOCK_001](../locks/sentinel/DETERMINEX_PLAYWRIGHT_TAURI_DRIVER_HARNESS_ADMISSION_LOCK_001.json) | 37 | 1165 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_playwright_taur…` |
| [DETERMINEX_PRIVACY_AND_TRAINING_DISCLOSURE_LOCK_001](../locks/sentinel/DETERMINEX_PRIVACY_AND_TRAINING_DISCLOSURE_LOCK_001.json) | 10 | 10 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_privacy_and_tra…` |
| [DETERMINEX_PROGRAMBENCH_COCKPIT_FIXTURE_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_PROGRAMBENCH_COCKPIT_FIXTURE_BINDING_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_PROGRAMBENCH_COCKPIT_FIXTURE_WIRE_AND_DRILLDOWN_LOCK_001](../locks/sentinel/DETERMINEX_PROGRAMBENCH_COCKPIT_FIXTURE_WIRE_AND_DRILLDOWN_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_PROGRAMBENCH_COCKPIT_VISUAL_PROOF_IF_FIRST_PAINT_PASSED_LOCK_001](../locks/sentinel/DETERMINEX_PROGRAMBENCH_COCKPIT_VISUAL_PROOF_IF_FIRST_PAINT_PASSED_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_PROGRAMBENCH_COCKPIT_WIREUP_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_PROGRAMBENCH_COCKPIT_WIREUP_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_programbench_co…` |
| [DETERMINEX_PROGRAMBENCH_COMPILER_LOOP_COCKPIT_POST_CERTIFICATION_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_PROGRAMBENCH_COMPILER_LOOP_COCKPIT_POST_CERTIFICATION_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_programbench_co…` |
| [DETERMINEX_PROGRAMBENCH_COMPILER_LOOP_COCKPIT_VISIBILITY_CELL_LOCK_001](../locks/sentinel/DETERMINEX_PROGRAMBENCH_COMPILER_LOOP_COCKPIT_VISIBILITY_CELL_LOCK_001.json) | 14 | 14 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_programbench_co…` |
| [DETERMINEX_PROGRAMBENCH_COMPILER_LOOP_MOAT_VISIBILITY_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_PROGRAMBENCH_COMPILER_LOOP_MOAT_VISIBILITY_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_programbench_co…` |
| [DETERMINEX_PROGRAMBENCH_FORBIDDEN_BOUNDARY_GUARD_LOCK_001](../locks/sentinel/DETERMINEX_PROGRAMBENCH_FORBIDDEN_BOUNDARY_GUARD_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_PROGRAMBENCH_PER_TARGET_UNIFIED_GRAPH_EXPANSION_LOCK_001](../locks/sentinel/DETERMINEX_PROGRAMBENCH_PER_TARGET_UNIFIED_GRAPH_EXPANSION_LOCK_001.json) | 5 | 5 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_determinex_program…` |
| [DETERMINEX_PROGRAMBENCH_WAL_VISUAL_MOAT_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_PROGRAMBENCH_WAL_VISUAL_MOAT_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_007_progra…` |
| [DETERMINEX_PROGRAMMING_LANGUAGE_UNIVERSE_AUDIT_LOCK_001](../locks/sentinel/DETERMINEX_PROGRAMMING_LANGUAGE_UNIVERSE_AUDIT_LOCK_001.json) | 18 | 18 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_programming_lan…` |
| [DETERMINEX_PROGRAM_AUTHORITY_PROMOTION_HARDENING_LOCK_001](../locks/sentinel/DETERMINEX_PROGRAM_AUTHORITY_PROMOTION_HARDENING_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_PROGRAM_AUTHORITY_RECORD_CONSUMPTION_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_PROGRAM_AUTHORITY_RECORD_CONSUMPTION_BINDING_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_PROGRAM_FAMILY_ADAPTER_INTERFACE_LOCK_001](../locks/sentinel/DETERMINEX_PROGRAM_FAMILY_ADAPTER_INTERFACE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_PROGRAM_NEGATIVE_SIGNAL_REGISTRY_LOCK_001](../locks/sentinel/DETERMINEX_PROGRAM_NEGATIVE_SIGNAL_REGISTRY_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_PROMOTE_TRUE_LOCAL_INSTALL_EXACT_CELLS_LOCK_001](../locks/sentinel/DETERMINEX_PROMOTE_TRUE_LOCAL_INSTALL_EXACT_CELLS_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_014_signed…` |
| [DETERMINEX_PROMOTION_GATE_NEGATIVE_FIXTURES_BLOCKING_CI_LOCK_001](../locks/sentinel/DETERMINEX_PROMOTION_GATE_NEGATIVE_FIXTURES_BLOCKING_CI_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_018_canoni…` |
| [DETERMINEX_PROMOTION_NEGATIVE_FIXTURE_CORPUS_PER_CATEGORY_EXERCISE_LOCK_001](../locks/sentinel/DETERMINEX_PROMOTION_NEGATIVE_FIXTURE_CORPUS_PER_CATEGORY_EXERCISE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_PROOF_CENTER_INSTALLED_APP_GUI_SMOKE_LOCK_001](../locks/sentinel/DETERMINEX_PROOF_CENTER_INSTALLED_APP_GUI_SMOKE_LOCK_001.json) | 6 | 6 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_proof_center_in…` |
| [DETERMINEX_PROOF_CENTER_INSTALLED_APP_ROUTE_MOUNT_LOCK_001](../locks/sentinel/DETERMINEX_PROOF_CENTER_INSTALLED_APP_ROUTE_MOUNT_LOCK_001.json) | 5 | 5 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide_frontend/test_proof_cen…` |
| [DETERMINEX_PROOF_CENTER_RELEASE_FOOTHOLD_CLAUDE_CRITIQUE_001](../locks/sentinel/DETERMINEX_PROOF_CENTER_RELEASE_FOOTHOLD_CLAUDE_CRITIQUE_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_proof_center_re…` |
| [DETERMINEX_PROOF_CONTROL_PLANE_FINAL_STATE_LOCK_001](../locks/sentinel/DETERMINEX_PROOF_CONTROL_PLANE_FINAL_STATE_LOCK_001.json) | 2 | 2 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/proof/test_determinex_proof_co…` |
| [DETERMINEX_PROOF_CONTROL_READINESS_AUDIT_LOCK_001](../locks/sentinel/DETERMINEX_PROOF_CONTROL_READINESS_AUDIT_LOCK_001.json) | 4 | 4 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/proof/test_determinex_proof_co…` |
| [DETERMINEX_PROOF_DISCOVERY_ORCHESTRATOR_LOCK_001](../locks/sentinel/DETERMINEX_PROOF_DISCOVERY_ORCHESTRATOR_LOCK_001.json) | 4 | 4 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/proof/test_determinex_proof_di…` |
| [DETERMINEX_PROOF_EXECUTION_AUDIT_REPAIR_LOCK_001](../locks/sentinel/DETERMINEX_PROOF_EXECUTION_AUDIT_REPAIR_LOCK_001.json) | 5 | 5 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/proof/test_determinex_proof_ex…` |
| [DETERMINEX_PROOF_GAP_PACKET_LOCK_001](../locks/sentinel/DETERMINEX_PROOF_GAP_PACKET_LOCK_001.json) | 4 | 4 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/proof/test_determinex_proof_ga…` |
| [DETERMINEX_PROOF_GENERATION_TOOL_ADMISSION_LOCK_001](../locks/sentinel/DETERMINEX_PROOF_GENERATION_TOOL_ADMISSION_LOCK_001.json) | 4 | 4 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/proof/test_determinex_proof_ge…` |
| [DETERMINEX_PROOF_OPERATOR_CENTER_MILESTONE_DASHBOARD_LOCK_001](../locks/sentinel/DETERMINEX_PROOF_OPERATOR_CENTER_MILESTONE_DASHBOARD_LOCK_001.json) | 12 | 12 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_determinex_proof_o…` |
| [DETERMINEX_PROOF_OPERATOR_CENTER_VIEWMODEL_LOCK_001](../locks/sentinel/DETERMINEX_PROOF_OPERATOR_CENTER_VIEWMODEL_LOCK_001.json) | 16 | 16 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_proof_operator_cen…` |
| [DETERMINEX_PROOF_REPORT_AND_CLAIM_SCANNER_BACKFILL_LOCK_001](../locks/sentinel/DETERMINEX_PROOF_REPORT_AND_CLAIM_SCANNER_BACKFILL_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_016_canoni…` |
| [DETERMINEX_PROOF_REPORT_CAPABILITY_ANCHORS_AND_BLOCKED_EXAMPLES_LOCK_002](../locks/sentinel/DETERMINEX_PROOF_REPORT_CAPABILITY_ANCHORS_AND_BLOCKED_EXAMPLES_LOCK_002.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_015_canoni…` |
| [DETERMINEX_PROOF_REPORT_CAPABILITY_COVERAGE_LOCK_001](../locks/sentinel/DETERMINEX_PROOF_REPORT_CAPABILITY_COVERAGE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_PROOF_REPORT_CAPABILITY_COVERAGE_SECTION_LOCK_001](../locks/sentinel/DETERMINEX_PROOF_REPORT_CAPABILITY_COVERAGE_SECTION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_PROOF_REPORT_CLAIM_SCANNER_FINAL_BACKFILL_CHECK_LOCK_001](../locks/sentinel/DETERMINEX_PROOF_REPORT_CLAIM_SCANNER_FINAL_BACKFILL_CHECK_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_017_canoni…` |
| [DETERMINEX_PROOF_REPORT_FIRST_LOCAL_INSTALL_AND_EXPORT_LOCK_001](../locks/sentinel/DETERMINEX_PROOF_REPORT_FIRST_LOCAL_INSTALL_AND_EXPORT_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_PROOF_REPORT_HTML_BOUND_TO_RELEASE_REGISTRY_LOCK_001](../locks/sentinel/DETERMINEX_PROOF_REPORT_HTML_BOUND_TO_RELEASE_REGISTRY_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_018_canoni…` |
| [DETERMINEX_PROOF_REPORT_HTML_HARDENING_AND_INTEGRITY_STAMP_LOCK_001](../locks/sentinel/DETERMINEX_PROOF_REPORT_HTML_HARDENING_AND_INTEGRITY_STAMP_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_PROOF_REPORT_HTML_INTEGRITY_SANITIZATION_PER_CLAIM_LINKS_LOCK_001](../locks/sentinel/DETERMINEX_PROOF_REPORT_HTML_INTEGRITY_SANITIZATION_PER_CLAIM_LINKS_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_PROOF_REPORT_LOCAL_INSTALL_AND_EXPORT_LOCK_001](../locks/sentinel/DETERMINEX_PROOF_REPORT_LOCAL_INSTALL_AND_EXPORT_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_PROOF_REPORT_PDF_HTML_EXPORT_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_PROOF_REPORT_PDF_HTML_EXPORT_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_proof_report_pd…` |
| [DETERMINEX_PROOF_REPORT_PDF_HTML_EXPORT_LOCK_001](../locks/sentinel/DETERMINEX_PROOF_REPORT_PDF_HTML_EXPORT_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_PROOF_REPORT_PER_CAPABILITY_EVIDENCE_ANCHORS_LOCK_001](../locks/sentinel/DETERMINEX_PROOF_REPORT_PER_CAPABILITY_EVIDENCE_ANCHORS_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_014_signed…` |
| [DETERMINEX_PROOF_REPORT_RELEASE_BOUNDARY_REFRESH_LOCK_001](../locks/sentinel/DETERMINEX_PROOF_REPORT_RELEASE_BOUNDARY_REFRESH_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_019_execut…` |
| [DETERMINEX_PROOF_REPORT_SUBPACKAGE_FEASIBILITY_AND_SCAFFOLD_LOCK_001](../locks/sentinel/DETERMINEX_PROOF_REPORT_SUBPACKAGE_FEASIBILITY_AND_SCAFFOLD_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_PROOF_SOURCE_REGISTRY_LOCK_001](../locks/sentinel/DETERMINEX_PROOF_SOURCE_REGISTRY_LOCK_001.json) | 4 | 4 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/proof/test_determinex_proof_so…` |
| [DETERMINEX_PROOF_TYPE_AUTHORITY_MATRIX_LOCK_001](../locks/sentinel/DETERMINEX_PROOF_TYPE_AUTHORITY_MATRIX_LOCK_001.json) | 6 | 6 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/proof/test_determinex_proof_ty…` |
| [DETERMINEX_PUBLIC_BETA_READINESS_DASHBOARD_HARDENING_LOCK_001](../locks/sentinel/DETERMINEX_PUBLIC_BETA_READINESS_DASHBOARD_HARDENING_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_PUBLIC_DISTRIBUTION_CHANNEL_FEASIBILITY_LOCK_001](../locks/sentinel/DETERMINEX_PUBLIC_DISTRIBUTION_CHANNEL_FEASIBILITY_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_public_distribu…` |
| [DETERMINEX_PUBLIC_DOCS_LICENSE_SECURITY_HYGIENE_APPLY_LOCK_001](../locks/sentinel/DETERMINEX_PUBLIC_DOCS_LICENSE_SECURITY_HYGIENE_APPLY_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_public_docs_lic…` |
| [DETERMINEX_PUBLIC_DOCS_LICENSE_SECURITY_HYGIENE_RETRY_LOCK_001](../locks/sentinel/DETERMINEX_PUBLIC_DOCS_LICENSE_SECURITY_HYGIENE_RETRY_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_public_docs_lic…` |
| [DETERMINEX_PUBLIC_MESSAGING_CLAIM_SCANNER_AND_LAUNCH_LANGUAGE_GUARD_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_PUBLIC_MESSAGING_CLAIM_SCANNER_AND_LAUNCH_LANGUAGE_GUARD_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_public_messagin…` |
| [DETERMINEX_PUBLIC_MESSAGING_PHRASE_GATE_MAP_LOCK_001](../locks/sentinel/DETERMINEX_PUBLIC_MESSAGING_PHRASE_GATE_MAP_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_public_messagin…` |
| [DETERMINEX_PUBLIC_PRIOR_ART_AND_ADJACENT_MARKET_AUDIT_LOCK_001](../locks/sentinel/DETERMINEX_PUBLIC_PRIOR_ART_AND_ADJACENT_MARKET_AUDIT_LOCK_001.json) | 18 | 18 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_public_prior_ar…` |
| [DETERMINEX_PUBLIC_PROOF_BETA_READINESS_DASHBOARD_LOCK_001](../locks/sentinel/DETERMINEX_PUBLIC_PROOF_BETA_READINESS_DASHBOARD_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_PUBLIC_PROOF_REPORT_EXPORT_LOCK_001](../locks/sentinel/DETERMINEX_PUBLIC_PROOF_REPORT_EXPORT_LOCK_001.json) | 9 | 9 | `pending_co` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_public_proof_re…` |
| [DETERMINEX_PUBLIC_REVEAL_PREFLIGHT_BOARD_LOCK_001](../locks/sentinel/DETERMINEX_PUBLIC_REVEAL_PREFLIGHT_BOARD_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_PUBLIC_REVEAL_PREFLIGHT_TIER_HARDENING_LOCK_001](../locks/sentinel/DETERMINEX_PUBLIC_REVEAL_PREFLIGHT_TIER_HARDENING_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_PUBLIC_SBOM_LICENSE_RELEASE_HYGIENE_LOCK_001](../locks/sentinel/DETERMINEX_PUBLIC_SBOM_LICENSE_RELEASE_HYGIENE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_public_sbom_lic…` |
| [DETERMINEX_PUBLIC_SHOCK_NARRATIVE_AND_CLAIM_GATE_REVIEW_CLAUDE_001](../locks/sentinel/DETERMINEX_PUBLIC_SHOCK_NARRATIVE_AND_CLAIM_GATE_REVIEW_CLAUDE_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_007_public…` |
| [DETERMINEX_PUBLIC_SHOCK_NARRATIVE_AND_CLAIM_SAFETY_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_PUBLIC_SHOCK_NARRATIVE_AND_CLAIM_SAFETY_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_public_shock_na…` |
| [DETERMINEX_PUBLIC_SHOCK_NARRATIVE_FINALIZATION_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_PUBLIC_SHOCK_NARRATIVE_FINALIZATION_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_public_shock_na…` |
| [DETERMINEX_PUBLIC_SHOCK_NARRATIVE_RUNG_REVIEW_001](../locks/sentinel/DETERMINEX_PUBLIC_SHOCK_NARRATIVE_RUNG_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_public_shock_na…` |
| [DETERMINEX_PUBLIC_TIDAL_WAVE_FLAGSHIP_FLOW_CERTIFICATION_LOCK_001](../locks/sentinel/DETERMINEX_PUBLIC_TIDAL_WAVE_FLAGSHIP_FLOW_CERTIFICATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_public_tidal_wa…` |
| [DETERMINEX_PUBLIC_UPLOAD_FORBIDDEN_BOUNDARY_GUARD_LOCK_001](../locks/sentinel/DETERMINEX_PUBLIC_UPLOAD_FORBIDDEN_BOUNDARY_GUARD_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_PYTHON_CLI_ACCEPTANCE_AND_SMOKE_PLAN_LOCK_001](../locks/sentinel/DETERMINEX_PYTHON_CLI_ACCEPTANCE_AND_SMOKE_PLAN_LOCK_001.json) | 15 | 15 | `e113efbd6e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_determinex_splash_…` |
| [DETERMINEX_PYTHON_CLI_FILE_DATA_SCAFFOLD_SPEC_LOCK_001](../locks/sentinel/DETERMINEX_PYTHON_CLI_FILE_DATA_SCAFFOLD_SPEC_LOCK_001.json) | 15 | 15 | `e113efbd6e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_determinex_splash_…` |
| [DETERMINEX_PYTHON_GOD_SCRIPT_AND_NATIVE_ARCHITECTURE_AUDIT_LOCK_001](../locks/sentinel/DETERMINEX_PYTHON_GOD_SCRIPT_AND_NATIVE_ARCHITECTURE_AUDIT_LOCK_001.json) | 13 | 13 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_python_god_scri…` |
| [DETERMINEX_PYTHON_STATUS_SCRIPT_DECOMPOSITION_AND_ANTI_GOD_SCRIPT_RULE_LOCK_001](../locks/sentinel/DETERMINEX_PYTHON_STATUS_SCRIPT_DECOMPOSITION_AND_ANTI_GOD_SCRIPT_RULE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_anti_god_script…` |
| [DETERMINEX_RAG_100_FIXTURE_RETRIEVAL_CORRECTNESS_SECURITY_GATE_LOCK_001](../locks/sentinel/DETERMINEX_RAG_100_FIXTURE_RETRIEVAL_CORRECTNESS_SECURITY_GATE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_RAG_50_FIXTURE_AND_CELL_5_CLASSIFICATION_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_RAG_50_FIXTURE_AND_CELL_5_CLASSIFICATION_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rag_50_fixture_…` |
| [DETERMINEX_RAG_50_FIXTURE_RETRIEVAL_CORRECTNESS_SECURITY_GATE_LOCK_001](../locks/sentinel/DETERMINEX_RAG_50_FIXTURE_RETRIEVAL_CORRECTNESS_SECURITY_GATE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rag_50_fixture_…` |
| [DETERMINEX_RAG_GUI_FIXTURE_LADDER_CELL5_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_RAG_GUI_FIXTURE_LADDER_CELL5_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rag_gui_fixture…` |
| [DETERMINEX_RAG_GUI_PANEL_AND_CELL_5_CLASSIFICATION_RESOLUTION_LOCK_001](../locks/sentinel/DETERMINEX_RAG_GUI_PANEL_AND_CELL_5_CLASSIFICATION_RESOLUTION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_RAG_NATURAL_LANGUAGE_QUERY_EVAL_LOCK_001](../locks/sentinel/DETERMINEX_RAG_NATURAL_LANGUAGE_QUERY_EVAL_LOCK_001.json) | 17 | 966 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rag_natural_lan…` |
| [DETERMINEX_RAG_PANEL_CELL5_FINAL_CLASSIFICATION_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_RAG_PANEL_CELL5_FINAL_CLASSIFICATION_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_007_rag_pa…` |
| [DETERMINEX_RAG_PRODUCTIZATION_FIXTURE_EXPANSION_CORRECTNESS_GATE_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_RAG_PRODUCTIZATION_FIXTURE_EXPANSION_CORRECTNESS_GATE_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rag_productizat…` |
| [DETERMINEX_RAG_SIGNED_RUN_EXPORT_OR_CELL5_CORRECTION_LOCK_001](../locks/sentinel/DETERMINEX_RAG_SIGNED_RUN_EXPORT_OR_CELL5_CORRECTION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_RC_PROOF_MAP_CLAUDE_APPEND_ONLY_COUNT_DRIFT_GUARDS_REVIEW_001](../locks/sentinel/DETERMINEX_RC_PROOF_MAP_CLAUDE_APPEND_ONLY_COUNT_DRIFT_GUARDS_REVIEW_001.json) | 1 | 1 | `3e99d21979` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rc_proof_map_cl…` |
| [DETERMINEX_RC_PROOF_MAP_CLAUDE_BETA_DASHBOARD_REVIEW_001](../locks/sentinel/DETERMINEX_RC_PROOF_MAP_CLAUDE_BETA_DASHBOARD_REVIEW_001.json) | 1 | 1 | `3e99d21979` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rc_proof_map_cl…` |
| [DETERMINEX_RC_PROOF_MAP_CLAUDE_CLAIM_SCANNER_OVERCLAIM_REVIEW_001](../locks/sentinel/DETERMINEX_RC_PROOF_MAP_CLAUDE_CLAIM_SCANNER_OVERCLAIM_REVIEW_001.json) | 1 | 1 | `3e99d21979` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rc_proof_map_cl…` |
| [DETERMINEX_RC_PROOF_MAP_CLAUDE_DIRTY_STATE_REPORTED_REVIEW_001](../locks/sentinel/DETERMINEX_RC_PROOF_MAP_CLAUDE_DIRTY_STATE_REPORTED_REVIEW_001.json) | 1 | 1 | `3e99d21979` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rc_proof_map_cl…` |
| [DETERMINEX_RC_PROOF_MAP_CLAUDE_EVIDENCE_INDEX_CLEAN_REVIEW_001](../locks/sentinel/DETERMINEX_RC_PROOF_MAP_CLAUDE_EVIDENCE_INDEX_CLEAN_REVIEW_001.json) | 1 | 1 | `3e99d21979` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rc_proof_map_cl…` |
| [DETERMINEX_RC_PROOF_MAP_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001](../locks/sentinel/DETERMINEX_RC_PROOF_MAP_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001.json) | 1 | 1 | `3e99d21979` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rc_proof_map_cl…` |
| [DETERMINEX_RC_PROOF_MAP_CLAUDE_NONCODER_REPORT_REVIEW_001](../locks/sentinel/DETERMINEX_RC_PROOF_MAP_CLAUDE_NONCODER_REPORT_REVIEW_001.json) | 1 | 1 | `3e99d21979` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rc_proof_map_cl…` |
| [DETERMINEX_RC_PROOF_MAP_CLAUDE_NO_FAKE_SIGNATURE_REVIEW_001](../locks/sentinel/DETERMINEX_RC_PROOF_MAP_CLAUDE_NO_FAKE_SIGNATURE_REVIEW_001.json) | 1 | 1 | `3e99d21979` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rc_proof_map_cl…` |
| [DETERMINEX_RC_PROOF_MAP_CLAUDE_NO_QUEUE_WITHOUT_MATERIAL_REVIEW_001](../locks/sentinel/DETERMINEX_RC_PROOF_MAP_CLAUDE_NO_QUEUE_WITHOUT_MATERIAL_REVIEW_001.json) | 1 | 1 | `3e99d21979` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rc_proof_map_cl…` |
| [DETERMINEX_RC_PROOF_MAP_CLAUDE_NO_SPEND_WITHOUT_APPROVAL_REVIEW_001](../locks/sentinel/DETERMINEX_RC_PROOF_MAP_CLAUDE_NO_SPEND_WITHOUT_APPROVAL_REVIEW_001.json) | 1 | 1 | `3e99d21979` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rc_proof_map_cl…` |
| [DETERMINEX_RC_PROOF_MAP_CLAUDE_PACKETS_NOT_EXECUTED_REVIEW_001](../locks/sentinel/DETERMINEX_RC_PROOF_MAP_CLAUDE_PACKETS_NOT_EXECUTED_REVIEW_001.json) | 1 | 1 | `3e99d21979` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rc_proof_map_cl…` |
| [DETERMINEX_RC_PROOF_MAP_CLAUDE_PATH_DECISION_REVIEW_001](../locks/sentinel/DETERMINEX_RC_PROOF_MAP_CLAUDE_PATH_DECISION_REVIEW_001.json) | 1 | 1 | `3e99d21979` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rc_proof_map_cl…` |
| [DETERMINEX_RC_PROOF_MAP_CLAUDE_PROOF_MAP_COMPLETENESS_REVIEW_001](../locks/sentinel/DETERMINEX_RC_PROOF_MAP_CLAUDE_PROOF_MAP_COMPLETENESS_REVIEW_001.json) | 1 | 1 | `3e99d21979` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rc_proof_map_cl…` |
| [DETERMINEX_RC_PROOF_MAP_CLAUDE_REACT_VITE_NOT_ADMITTED_REVIEW_001](../locks/sentinel/DETERMINEX_RC_PROOF_MAP_CLAUDE_REACT_VITE_NOT_ADMITTED_REVIEW_001.json) | 1 | 1 | `3e99d21979` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rc_proof_map_cl…` |
| [DETERMINEX_RC_PROOF_MAP_CLAUDE_RELEASE_CELLS_INVARIANT_REVIEW_001](../locks/sentinel/DETERMINEX_RC_PROOF_MAP_CLAUDE_RELEASE_CELLS_INVARIANT_REVIEW_001.json) | 1 | 1 | `3e99d21979` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rc_proof_map_cl…` |
| [DETERMINEX_RC_PROOF_MAP_CLAUDE_RELEASE_FAMILIES_INVARIANT_REVIEW_001](../locks/sentinel/DETERMINEX_RC_PROOF_MAP_CLAUDE_RELEASE_FAMILIES_INVARIANT_REVIEW_001.json) | 1 | 1 | `3e99d21979` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rc_proof_map_cl…` |
| [DETERMINEX_RC_PROOF_MAP_CLAUDE_SCORES_UNCHANGED_REVIEW_001](../locks/sentinel/DETERMINEX_RC_PROOF_MAP_CLAUDE_SCORES_UNCHANGED_REVIEW_001.json) | 1 | 1 | `3e99d21979` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rc_proof_map_cl…` |
| [DETERMINEX_RC_PROOF_MAP_CLAUDE_SYNTHESIS_REVIEW_001](../locks/sentinel/DETERMINEX_RC_PROOF_MAP_CLAUDE_SYNTHESIS_REVIEW_001.json) | 1 | 1 | `3e99d21979` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rc_proof_map_cl…` |
| [DETERMINEX_RC_PROOF_MAP_CLAUDE_TIMEOUT_DIAGNOSTIC_REVIEW_001](../locks/sentinel/DETERMINEX_RC_PROOF_MAP_CLAUDE_TIMEOUT_DIAGNOSTIC_REVIEW_001.json) | 1 | 1 | `3e99d21979` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rc_proof_map_cl…` |
| [DETERMINEX_REACT_DEMO_NAVIGATION_HAPPY_BLOCKED_PATH_LOCK_001](../locks/sentinel/DETERMINEX_REACT_DEMO_NAVIGATION_HAPPY_BLOCKED_PATH_LOCK_001.json) | 20 | 20 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_demo_navigat…` |
| [DETERMINEX_REACT_IDEA_LAB_PANEL_LOCK_001](../locks/sentinel/DETERMINEX_REACT_IDEA_LAB_PANEL_LOCK_001.json) | 15 | 15 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_idea_lab_pan…` |
| [DETERMINEX_REACT_IDEA_LAB_VERIFIED_DEMO_STATUS_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_IDEA_LAB_VERIFIED_DEMO_STATUS_BINDING_LOCK_001.json) | 24 | 24 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_idea_lab_ver…` |
| [DETERMINEX_REACT_LEARNING_STUDIO_PANEL_LOCK_001](../locks/sentinel/DETERMINEX_REACT_LEARNING_STUDIO_PANEL_LOCK_001.json) | 16 | 16 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_learning_stu…` |
| [DETERMINEX_REACT_LEARNING_STUDIO_VERIFIED_DEMO_STATUS_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_LEARNING_STUDIO_VERIFIED_DEMO_STATUS_BINDING_LOCK_001.json) | 52 | 52 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_learning_stu…` |
| [DETERMINEX_REACT_MAINTENANCE_BAY_PANEL_LOCK_001](../locks/sentinel/DETERMINEX_REACT_MAINTENANCE_BAY_PANEL_LOCK_001.json) | 14 | 14 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_maintenance_…` |
| [DETERMINEX_REACT_MAINTENANCE_BAY_VERIFIED_DEMO_STATUS_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_MAINTENANCE_BAY_VERIFIED_DEMO_STATUS_BINDING_LOCK_001.json) | 35 | 35 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_maintenance_…` |
| [DETERMINEX_REACT_PRODUCT_SHELL_BROWSER_SNAPSHOT_LOCK_001](../locks/sentinel/DETERMINEX_REACT_PRODUCT_SHELL_BROWSER_SNAPSHOT_LOCK_001.json) | 18 | 18 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_product_shel…` |
| [DETERMINEX_REACT_PROOF_OPERATOR_CENTER_MILESTONE_DASHBOARD_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_PROOF_OPERATOR_CENTER_MILESTONE_DASHBOARD_BINDING_LOCK_001.json) | 62 | 62 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_proof_operat…` |
| [DETERMINEX_REACT_PROOF_OPERATOR_CENTER_PANEL_LOCK_001](../locks/sentinel/DETERMINEX_REACT_PROOF_OPERATOR_CENTER_PANEL_LOCK_001.json) | 14 | 14 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_proof_operat…` |
| [DETERMINEX_REACT_PUBLIC_AUTHORITY_BOUNDARY_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_PUBLIC_AUTHORITY_BOUNDARY_BINDING_LOCK_001.json) | 24 | 24 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_public_autho…` |
| [DETERMINEX_REACT_PUBLIC_FALSE_CLAIM_SCANNER_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_PUBLIC_FALSE_CLAIM_SCANNER_BINDING_LOCK_001.json) | 17 | 17 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_public_false…` |
| [DETERMINEX_REACT_PUBLIC_PROOF_REPORT_EXPORT_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_PUBLIC_PROOF_REPORT_EXPORT_BINDING_LOCK_001.json) | 27 | 27 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_public_proof…` |
| [DETERMINEX_REACT_PUBLIC_PROOF_REPORT_SAMPLE_REPORTS_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_PUBLIC_PROOF_REPORT_SAMPLE_REPORTS_BINDING_LOCK_001.json) | 17 | 17 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_public_proof…` |
| [DETERMINEX_REACT_PUBLIC_READINESS_SPINE_DASHBOARD_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_PUBLIC_READINESS_SPINE_DASHBOARD_BINDING_LOCK_001.json) | 21 | 21 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_public_readi…` |
| [DETERMINEX_REACT_PUBLIC_TIDAL_WAVE_FLAGSHIP_FLOW_CERTIFICATION_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_PUBLIC_TIDAL_WAVE_FLAGSHIP_FLOW_CERTIFICATION_BINDING_LOCK_001.json) | 32 | 32 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_public_tidal…` |
| [DETERMINEX_REACT_PUBLIC_UNKNOWN_NOVEL_ROUTE_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_PUBLIC_UNKNOWN_NOVEL_ROUTE_BINDING_LOCK_001.json) | 19 | 19 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_public_unkno…` |
| [DETERMINEX_REACT_RELEASE_READINESS_BLOCKER_PANEL_LOCK_001](../locks/sentinel/DETERMINEX_REACT_RELEASE_READINESS_BLOCKER_PANEL_LOCK_001.json) | 23 | 23 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_release_read…` |
| [DETERMINEX_REACT_REPO_CLINIC_PANEL_LOCK_001](../locks/sentinel/DETERMINEX_REACT_REPO_CLINIC_PANEL_LOCK_001.json) | 15 | 15 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_repo_clinic_…` |
| [DETERMINEX_REACT_REPO_CLINIC_VERIFIED_DEMO_STATUS_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_REPO_CLINIC_VERIFIED_DEMO_STATUS_BINDING_LOCK_001.json) | 29 | 29 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_repo_clinic_…` |
| [DETERMINEX_REACT_SPLASH_DEMO_PANEL_LOCK_001](../locks/sentinel/DETERMINEX_REACT_SPLASH_DEMO_PANEL_LOCK_001.json) | 15 | 15 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_splash_demo_…` |
| [DETERMINEX_REACT_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_005_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_005_BINDING_LOCK_001.json) | 25 | 25 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_tandem_post_…` |
| [DETERMINEX_REACT_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_007_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_007_BINDING_LOCK_001.json) | 25 | 25 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_tandem_post_…` |
| [DETERMINEX_REACT_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_008_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_008_BINDING_LOCK_001.json) | 25 | 25 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_tandem_post_…` |
| [DETERMINEX_REACT_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_009_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_009_BINDING_LOCK_001.json) | 25 | 25 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_tandem_post_…` |
| [DETERMINEX_REACT_UNIFIED_NAVIGATION_PANEL_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIFIED_NAVIGATION_PANEL_LOCK_001.json) | 18 | 18 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_unified_navi…` |
| [DETERMINEX_REACT_UNIVERSAL_100_ALL_SECTOR_TAXONOMY_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_ALL_SECTOR_TAXONOMY_BINDING_LOCK_001.json) | 22 | 22 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_CONVEYOR_BACKLOG_AND_DEPTH_QUEUE_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_CONVEYOR_BACKLOG_AND_DEPTH_QUEUE_BINDING_LOCK_001.json) | 22 | 22 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_DEPTH_PROMOTION_BATCH_017_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_DEPTH_PROMOTION_BATCH_017_BINDING_LOCK_001.json) | 24 | 24 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_DEPTH_PROMOTION_BATCH_018_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_DEPTH_PROMOTION_BATCH_018_BINDING_LOCK_001.json) | 24 | 24 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_DEPTH_PROMOTION_BATCH_019_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_DEPTH_PROMOTION_BATCH_019_BINDING_LOCK_001.json) | 24 | 24 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_DEPTH_PROMOTION_CANDIDATE_INVENTORY_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_DEPTH_PROMOTION_CANDIDATE_INVENTORY_BINDING_LOCK_001.json) | 23 | 23 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_DEPTH_PROMOTION_SCOREBOARD_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_DEPTH_PROMOTION_SCOREBOARD_BINDING_LOCK_001.json) | 25 | 25 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_DEPTH_PROMOTION_WAVE_001_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_DEPTH_PROMOTION_WAVE_001_BINDING_LOCK_001.json) | 24 | 24 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_MATRIX_PROBE_EXECUTION_BATCH_002_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_MATRIX_PROBE_EXECUTION_BATCH_002_BINDING_LOCK_001.json) | 21 | 21 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_MATRIX_PROBE_EXECUTION_BATCH_003_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_MATRIX_PROBE_EXECUTION_BATCH_003_BINDING_LOCK_001.json) | 30 | 30 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_MATRIX_PROBE_EXECUTION_BATCH_004_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_MATRIX_PROBE_EXECUTION_BATCH_004_BINDING_LOCK_001.json) | 32 | 32 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_MATRIX_PROBE_EXECUTION_BATCH_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_MATRIX_PROBE_EXECUTION_BATCH_BINDING_LOCK_001.json) | 42 | 42 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_005_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_005_BINDING_LOCK_001.json) | 24 | 24 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_006_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_006_BINDING_LOCK_001.json) | 24 | 24 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_007_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_007_BINDING_LOCK_001.json) | 24 | 24 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_008_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_008_BINDING_LOCK_001.json) | 24 | 24 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_009_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_009_BINDING_LOCK_001.json) | 24 | 24 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_010_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_010_BINDING_LOCK_001.json) | 24 | 24 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_011_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_011_BINDING_LOCK_001.json) | 24 | 24 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_012_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_012_BINDING_LOCK_001.json) | 24 | 24 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_013_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_013_BINDING_LOCK_001.json) | 24 | 24 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_SECTOR_STATE_LADDER_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_SECTOR_STATE_LADDER_BINDING_LOCK_001.json) | 22 | 22 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_DEPTH_LEDGER_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_DEPTH_LEDGER_BINDING_LOCK_001.json) | 22 | 22 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_002_VISUAL_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_002_VISUAL_BINDING_LOCK_001.json) | 17 | 17 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_003_VISUAL_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_003_VISUAL_BINDING_LOCK_001.json) | 24 | 24 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_004_VISUAL_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_004_VISUAL_BINDING_LOCK_001.json) | 23 | 23 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_005_VISUAL_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_005_VISUAL_BINDING_LOCK_001.json) | 12 | 12 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_006_VISUAL_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_006_VISUAL_BINDING_LOCK_001.json) | 12 | 12 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_007_VISUAL_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_007_VISUAL_BINDING_LOCK_001.json) | 12 | 12 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_008_VISUAL_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_008_VISUAL_BINDING_LOCK_001.json) | 12 | 12 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_009_VISUAL_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_009_VISUAL_BINDING_LOCK_001.json) | 12 | 12 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_010_VISUAL_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_010_VISUAL_BINDING_LOCK_001.json) | 12 | 12 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_011_VISUAL_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_011_VISUAL_BINDING_LOCK_001.json) | 12 | 12 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_012_VISUAL_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_012_VISUAL_BINDING_LOCK_001.json) | 12 | 12 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_013_VISUAL_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_013_VISUAL_BINDING_LOCK_001.json) | 12 | 12 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_014_VISUAL_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_014_VISUAL_BINDING_LOCK_001.json) | 14 | 14 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_015_VISUAL_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_015_VISUAL_BINDING_LOCK_001.json) | 14 | 14 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_016_VISUAL_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_016_VISUAL_BINDING_LOCK_001.json) | 14 | 14 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_017_VISUAL_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_017_VISUAL_BINDING_LOCK_001.json) | 14 | 14 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_018_VISUAL_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_018_VISUAL_BINDING_LOCK_001.json) | 14 | 14 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_019_VISUAL_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_019_VISUAL_BINDING_LOCK_001.json) | 14 | 14 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_TOP_LEVEL_BLOCKER_INVENTORY_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_TOP_LEVEL_BLOCKER_INVENTORY_BINDING_LOCK_001.json) | 22 | 22 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_TOP_LEVEL_GAP_CLOSURE_BATCH_014_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_TOP_LEVEL_GAP_CLOSURE_BATCH_014_BINDING_LOCK_001.json) | 23 | 23 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_TOP_LEVEL_GAP_CLOSURE_BATCH_015_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_TOP_LEVEL_GAP_CLOSURE_BATCH_015_BINDING_LOCK_001.json) | 23 | 23 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_TOP_LEVEL_GAP_CLOSURE_BATCH_016_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_TOP_LEVEL_GAP_CLOSURE_BATCH_016_BINDING_LOCK_001.json) | 23 | 23 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_TOP_LEVEL_SECTOR_COMPLETION_CAMPAIGN_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_TOP_LEVEL_SECTOR_COMPLETION_CAMPAIGN_BINDING_LOCK_001.json) | 25 | 25 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_TOP_LEVEL_SECTOR_COVERAGE_SCOREBOARD_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_TOP_LEVEL_SECTOR_COVERAGE_SCOREBOARD_BINDING_LOCK_001.json) | 22 | 22 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_TOP_LEVEL_SECTOR_GAP_CLOSURE_WAVE_001_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_TOP_LEVEL_SECTOR_GAP_CLOSURE_WAVE_001_BINDING_LOCK_001.json) | 23 | 23 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_universal_10…` |
| [DETERMINEX_REACT_UNIVERSAL_100_VISUAL_WATCH_AND_BINDING_PREP_LOCK_001](../locks/sentinel/DETERMINEX_REACT_UNIVERSAL_100_VISUAL_WATCH_AND_BINDING_PREP_LOCK_001.json) | 33 | 36 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_v…` |
| [DETERMINEX_REACT_USER_LEVEL_TEACHING_MODE_LOCK_001](../locks/sentinel/DETERMINEX_REACT_USER_LEVEL_TEACHING_MODE_LOCK_001.json) | 14 | 14 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_react_user_level_t…` |
| [DETERMINEX_REACT_VITE_AUTHORITY_PACKET_VALIDATION_LOCK_001](../locks/sentinel/DETERMINEX_REACT_VITE_AUTHORITY_PACKET_VALIDATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_first_authority…` |
| [DETERMINEX_REACT_VITE_BOUNDED_REPAIR_GUARD_LOCK_001](../locks/sentinel/DETERMINEX_REACT_VITE_BOUNDED_REPAIR_GUARD_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_REACT_VITE_BOUNDED_SOURCE_REPAIR_LOCK_001](../locks/sentinel/DETERMINEX_REACT_VITE_BOUNDED_SOURCE_REPAIR_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_REACT_VITE_FAILURE_CLASSIFICATION_REPAIR_AUTHORIZATION_LOCK_001](../locks/sentinel/DETERMINEX_REACT_VITE_FAILURE_CLASSIFICATION_REPAIR_AUTHORIZATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_REACT_VITE_FULL_STATUS_TIMEOUT_CONTINUATION_LOCK_001](../locks/sentinel/DETERMINEX_REACT_VITE_FULL_STATUS_TIMEOUT_CONTINUATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_REACT_VITE_LOCAL_VERIFICATION_EXECUTION_LOCK_001](../locks/sentinel/DETERMINEX_REACT_VITE_LOCAL_VERIFICATION_EXECUTION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_REACT_VITE_LOCAL_VERIFICATION_PLAN_LOCK_001](../locks/sentinel/DETERMINEX_REACT_VITE_LOCAL_VERIFICATION_PLAN_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_REACT_VITE_LOCAL_VERIFICATION_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_REACT_VITE_LOCAL_VERIFICATION_RECONCILIATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_REACT_VITE_OTHER_PROTECTED_PACKETS_UNTOUCHED_LOCK_001](../locks/sentinel/DETERMINEX_REACT_VITE_OTHER_PROTECTED_PACKETS_UNTOUCHED_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_REACT_VITE_POST_ADMISSION_LOCAL_TRANSCRIPT_LOCK_001](../locks/sentinel/DETERMINEX_REACT_VITE_POST_ADMISSION_LOCAL_TRANSCRIPT_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_first_authority…` |
| [DETERMINEX_REACT_VITE_POST_SPEND_LOCAL_VERIFICATION_LOCK_001](../locks/sentinel/DETERMINEX_REACT_VITE_POST_SPEND_LOCAL_VERIFICATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_real_signature_…` |
| [DETERMINEX_REACT_VITE_POST_VERIFICATION_EVIDENCE_AUDIT_LOCK_001](../locks/sentinel/DETERMINEX_REACT_VITE_POST_VERIFICATION_EVIDENCE_AUDIT_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_REACT_VITE_PRIOR_SPEND_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_REACT_VITE_PRIOR_SPEND_BINDING_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_REACT_VITE_REPAIR_MARCH_PLAN_DASHBOARD_LOCK_001](../locks/sentinel/DETERMINEX_REACT_VITE_REPAIR_MARCH_PLAN_DASHBOARD_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_REACT_VITE_REPAIR_SCORE_DISCIPLINE_LOCK_001](../locks/sentinel/DETERMINEX_REACT_VITE_REPAIR_SCORE_DISCIPLINE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_REACT_VITE_REPAIR_UNIVERSAL_ACCOUNTING_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_REACT_VITE_REPAIR_UNIVERSAL_ACCOUNTING_RECONCILIATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_REACT_VITE_SCAFFOLD_BUILD_TEST_SMOKE_RELEASE_CELL_LOCK_001](../locks/sentinel/DETERMINEX_REACT_VITE_SCAFFOLD_BUILD_TEST_SMOKE_RELEASE_CELL_LOCK_001.json) | 34 | 34 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_react_vite_scaf…` |
| [DETERMINEX_REACT_VITE_SCORE_DISCIPLINE_LOCK_001](../locks/sentinel/DETERMINEX_REACT_VITE_SCORE_DISCIPLINE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_REACT_VITE_SIGNED_DEPENDENCY_OR_STRUCTURAL_TRANSCRIPT_LOCK_001](../locks/sentinel/DETERMINEX_REACT_VITE_SIGNED_DEPENDENCY_OR_STRUCTURAL_TRANSCRIPT_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_REACT_VITE_SPEND_ELIGIBILITY_GATE_LOCK_001](../locks/sentinel/DETERMINEX_REACT_VITE_SPEND_ELIGIBILITY_GATE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_real_signature_…` |
| [DETERMINEX_REACT_VITE_SPEND_ELIGIBILITY_RECHECK_LOCK_001](../locks/sentinel/DETERMINEX_REACT_VITE_SPEND_ELIGIBILITY_RECHECK_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_signature_deliv…` |
| [DETERMINEX_REACT_VITE_TIER1_PROMOTION_AFTER_REPAIR_LOCK_001](../locks/sentinel/DETERMINEX_REACT_VITE_TIER1_PROMOTION_AFTER_REPAIR_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_REACT_VITE_TIER1_PROMOTION_DECISION_LOCK_001](../locks/sentinel/DETERMINEX_REACT_VITE_TIER1_PROMOTION_DECISION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_REACT_VITE_VERIFICATION_RETRY_AFTER_REPAIR_LOCK_001](../locks/sentinel/DETERMINEX_REACT_VITE_VERIFICATION_RETRY_AFTER_REPAIR_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_REAL_APPROVAL_RESOLUTION_SWEEP_LOCK_001](../locks/sentinel/DETERMINEX_REAL_APPROVAL_RESOLUTION_SWEEP_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_REAL_LOCAL_INSTALL_MOMENTS_INSTALLED_ENTRYPOINTS_LOCK_001](../locks/sentinel/DETERMINEX_REAL_LOCAL_INSTALL_MOMENTS_INSTALLED_ENTRYPOINTS_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_REAL_OPERATOR_SIGNATURE_IMPORT_AND_FIRST_SPEND_LOCK_001](../locks/sentinel/DETERMINEX_REAL_OPERATOR_SIGNATURE_IMPORT_AND_FIRST_SPEND_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_REAL_OPERATOR_SIGNATURE_IMPORT_LOCK_001](../locks/sentinel/DETERMINEX_REAL_OPERATOR_SIGNATURE_IMPORT_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_signature_spend…` |
| [DETERMINEX_REAL_OPERATOR_SIGNATURE_IMPORT_PREP_LOCK_001](../locks/sentinel/DETERMINEX_REAL_OPERATOR_SIGNATURE_IMPORT_PREP_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_REAL_OPERATOR_SIGNATURE_IMPORT_PROCEDURE_DOCUMENTED_AND_FIRST_SIGNATURE_LANDED_LOCK_001](../locks/sentinel/DETERMINEX_REAL_OPERATOR_SIGNATURE_IMPORT_PROCEDURE_DOCUMENTED_AND_FIRST_SIGNATURE_LANDED_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_REAL_OPERATOR_SIGNATURE_IMPORT_PROCEDURE_LOCK_001](../locks/sentinel/DETERMINEX_REAL_OPERATOR_SIGNATURE_IMPORT_PROCEDURE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_REAL_SIGNATURE_IMPORT_AND_FIRST_AUTHORITY_SPEND_LOCK_002](../locks/sentinel/DETERMINEX_REAL_SIGNATURE_IMPORT_AND_FIRST_AUTHORITY_SPEND_LOCK_002.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_014_signed…` |
| [DETERMINEX_REAL_SIGNATURE_IMPORT_VALIDATE_AND_FIRST_SPEND_LOCK_003](../locks/sentinel/DETERMINEX_REAL_SIGNATURE_IMPORT_VALIDATE_AND_FIRST_SPEND_LOCK_003.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_015_canoni…` |
| [DETERMINEX_REAL_SIGNATURE_INGEST_AND_REACT_VITE_SPEND_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_REAL_SIGNATURE_INGEST_AND_REACT_VITE_SPEND_RECONCILIATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_real_signature_…` |
| [DETERMINEX_REAL_SIGNATURE_MATERIAL_SCAN_LOCK_001](../locks/sentinel/DETERMINEX_REAL_SIGNATURE_MATERIAL_SCAN_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_real_signature_…` |
| [DETERMINEX_REAL_SIGNATURE_VALIDATION_LOCK_001](../locks/sentinel/DETERMINEX_REAL_SIGNATURE_VALIDATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_real_signature_…` |
| [DETERMINEX_REAL_SIG_SPEND_CLAUDE_CHANGED_FILES_REVIEW_001](../locks/sentinel/DETERMINEX_REAL_SIG_SPEND_CLAUDE_CHANGED_FILES_REVIEW_001.json) | 1 | 1 | `2fe755665e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_real_sig_spend_…` |
| [DETERMINEX_REAL_SIG_SPEND_CLAUDE_COMMAND_MATCH_REVIEW_001](../locks/sentinel/DETERMINEX_REAL_SIG_SPEND_CLAUDE_COMMAND_MATCH_REVIEW_001.json) | 1 | 1 | `2fe755665e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_real_sig_spend_…` |
| [DETERMINEX_REAL_SIG_SPEND_CLAUDE_CURRENT_SOURCE_TRUTH_REVIEW_001](../locks/sentinel/DETERMINEX_REAL_SIG_SPEND_CLAUDE_CURRENT_SOURCE_TRUTH_REVIEW_001.json) | 1 | 1 | `2fe755665e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_real_sig_spend_…` |
| [DETERMINEX_REAL_SIG_SPEND_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001](../locks/sentinel/DETERMINEX_REAL_SIG_SPEND_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001.json) | 1 | 1 | `2fe755665e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_real_sig_spend_…` |
| [DETERMINEX_REAL_SIG_SPEND_CLAUDE_HARD_FLOOR_BOUNDARY_REVIEW_001](../locks/sentinel/DETERMINEX_REAL_SIG_SPEND_CLAUDE_HARD_FLOOR_BOUNDARY_REVIEW_001.json) | 1 | 1 | `2fe755665e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_real_sig_spend_…` |
| [DETERMINEX_REAL_SIG_SPEND_CLAUDE_MARKER_HASH_STABILITY_HARDENING_REVIEW_001](../locks/sentinel/DETERMINEX_REAL_SIG_SPEND_CLAUDE_MARKER_HASH_STABILITY_HARDENING_REVIEW_001.json) | 1 | 1 | `2fe755665e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_real_sig_spend_…` |
| [DETERMINEX_REAL_SIG_SPEND_CLAUDE_MARKER_VALIDITY_REVIEW_001](../locks/sentinel/DETERMINEX_REAL_SIG_SPEND_CLAUDE_MARKER_VALIDITY_REVIEW_001.json) | 1 | 1 | `2fe755665e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_real_sig_spend_…` |
| [DETERMINEX_REAL_SIG_SPEND_CLAUDE_QUEUE_COUNT_REVIEW_001](../locks/sentinel/DETERMINEX_REAL_SIG_SPEND_CLAUDE_QUEUE_COUNT_REVIEW_001.json) | 1 | 1 | `2fe755665e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_real_sig_spend_…` |
| [DETERMINEX_REAL_SIG_SPEND_CLAUDE_QUEUE_IMPORT_LEGITIMACY_REVIEW_001](../locks/sentinel/DETERMINEX_REAL_SIG_SPEND_CLAUDE_QUEUE_IMPORT_LEGITIMACY_REVIEW_001.json) | 1 | 1 | `2fe755665e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_real_sig_spend_…` |
| [DETERMINEX_REAL_SIG_SPEND_CLAUDE_REACT_VITE_VERIFICATION_REVIEW_001](../locks/sentinel/DETERMINEX_REAL_SIG_SPEND_CLAUDE_REACT_VITE_VERIFICATION_REVIEW_001.json) | 1 | 1 | `2fe755665e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_real_sig_spend_…` |
| [DETERMINEX_REAL_SIG_SPEND_CLAUDE_ROLLBACK_RECORD_REVIEW_001](../locks/sentinel/DETERMINEX_REAL_SIG_SPEND_CLAUDE_ROLLBACK_RECORD_REVIEW_001.json) | 1 | 1 | `2fe755665e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_real_sig_spend_…` |
| [DETERMINEX_REAL_SIG_SPEND_CLAUDE_SBOM_PACKET_CARRY_REVIEW_001](../locks/sentinel/DETERMINEX_REAL_SIG_SPEND_CLAUDE_SBOM_PACKET_CARRY_REVIEW_001.json) | 1 | 1 | `2fe755665e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_real_sig_spend_…` |
| [DETERMINEX_REAL_SIG_SPEND_CLAUDE_SCORE_MOVEMENT_EVIDENCE_REVIEW_001](../locks/sentinel/DETERMINEX_REAL_SIG_SPEND_CLAUDE_SCORE_MOVEMENT_EVIDENCE_REVIEW_001.json) | 1 | 1 | `2fe755665e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_real_sig_spend_…` |
| [DETERMINEX_REAL_SIG_SPEND_CLAUDE_SIGNATURE_MATERIAL_SCAN_REVIEW_001](../locks/sentinel/DETERMINEX_REAL_SIG_SPEND_CLAUDE_SIGNATURE_MATERIAL_SCAN_REVIEW_001.json) | 1 | 1 | `2fe755665e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_real_sig_spend_…` |
| [DETERMINEX_REAL_SIG_SPEND_CLAUDE_SIGNATURE_VALIDATION_REVIEW_001](../locks/sentinel/DETERMINEX_REAL_SIG_SPEND_CLAUDE_SIGNATURE_VALIDATION_REVIEW_001.json) | 1 | 1 | `2fe755665e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_real_sig_spend_…` |
| [DETERMINEX_REAL_SIG_SPEND_CLAUDE_SPEND_ELIGIBILITY_REVIEW_001](../locks/sentinel/DETERMINEX_REAL_SIG_SPEND_CLAUDE_SPEND_ELIGIBILITY_REVIEW_001.json) | 1 | 1 | `2fe755665e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_real_sig_spend_…` |
| [DETERMINEX_REAL_SIG_SPEND_CLAUDE_SPEND_OCCURRED_REVIEW_001](../locks/sentinel/DETERMINEX_REAL_SIG_SPEND_CLAUDE_SPEND_OCCURRED_REVIEW_001.json) | 1 | 1 | `2fe755665e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_real_sig_spend_…` |
| [DETERMINEX_REAL_SIG_SPEND_CLAUDE_SYNTHESIS_REVIEW_001](../locks/sentinel/DETERMINEX_REAL_SIG_SPEND_CLAUDE_SYNTHESIS_REVIEW_001.json) | 1 | 1 | `2fe755665e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_real_sig_spend_…` |
| [DETERMINEX_REAL_SIG_SPEND_CLAUDE_TIER1_COVERAGE_REVIEW_001](../locks/sentinel/DETERMINEX_REAL_SIG_SPEND_CLAUDE_TIER1_COVERAGE_REVIEW_001.json) | 1 | 1 | `2fe755665e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_real_sig_spend_…` |
| [DETERMINEX_REAL_SIG_SPEND_CLAUDE_TIMER_PROTOCOL_REVIEW_001](../locks/sentinel/DETERMINEX_REAL_SIG_SPEND_CLAUDE_TIMER_PROTOCOL_REVIEW_001.json) | 1 | 1 | `2fe755665e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_real_sig_spend_…` |
| [DETERMINEX_REAL_USER_REPO_MUTATION_FORBIDDEN_GUARD_LOCK_001](../locks/sentinel/DETERMINEX_REAL_USER_REPO_MUTATION_FORBIDDEN_GUARD_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_REEVALUATE_THREE_LOCAL_PREVIEW_PACKAGE_CELLS_LOCK_001](../locks/sentinel/DETERMINEX_REEVALUATE_THREE_LOCAL_PREVIEW_PACKAGE_CELLS_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_016_canoni…` |
| [DETERMINEX_RELEASE_AUTHORITY_PACKET_SCHEMA_LOCK_001](../locks/sentinel/DETERMINEX_RELEASE_AUTHORITY_PACKET_SCHEMA_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_RELEASE_AUTHORITY_QUEUE_SPEND_SYSTEM_LOCK_001](../locks/sentinel/DETERMINEX_RELEASE_AUTHORITY_QUEUE_SPEND_SYSTEM_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_RELEASE_AUTHORITY_VALIDATOR_REJECTION_CORPUS_LOCK_001](../locks/sentinel/DETERMINEX_RELEASE_AUTHORITY_VALIDATOR_REJECTION_CORPUS_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_RELEASE_CAMPAIGN_LOCK_STAGING_LOCK_001](../locks/sentinel/DETERMINEX_RELEASE_CAMPAIGN_LOCK_STAGING_LOCK_001.json) | 18 | 1 | `e4ff17592c` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_admitted_clean_…` |
| [DETERMINEX_RELEASE_CANDIDATE_GUARDS_AND_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_RELEASE_CANDIDATE_GUARDS_AND_RECONCILIATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_RELEASE_CANDIDATE_PROOF_MAP_LOCK_001](../locks/sentinel/DETERMINEX_RELEASE_CANDIDATE_PROOF_MAP_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_RELEASE_CANDIDATE_SIGNATURE_RECHECK_BRANCH_DECISION_LOCK_001](../locks/sentinel/DETERMINEX_RELEASE_CANDIDATE_SIGNATURE_RECHECK_BRANCH_DECISION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_RELEASE_CELL_DECERTIFICATION_AND_ROLLBACK_PROCEDURE_LOCK_001](../locks/sentinel/DETERMINEX_RELEASE_CELL_DECERTIFICATION_AND_ROLLBACK_PROCEDURE_LOCK_001.json) | 24 | 24 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_release_cell_de…` |
| [DETERMINEX_RELEASE_CELL_DRIFT_DETECTOR_GITHUB_WORKFLOW_LOCK_001](../locks/sentinel/DETERMINEX_RELEASE_CELL_DRIFT_DETECTOR_GITHUB_WORKFLOW_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_018_canoni…` |
| [DETERMINEX_RELEASE_CELL_PROMOTION_REQUIRES_SIGNOFF_AND_ANCHOR_LOCK_001](../locks/sentinel/DETERMINEX_RELEASE_CELL_PROMOTION_REQUIRES_SIGNOFF_AND_ANCHOR_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_016_canoni…` |
| [DETERMINEX_RELEASE_CELL_SIGNOFF_GATE_ENFORCEMENT_CI_LOCK_001](../locks/sentinel/DETERMINEX_RELEASE_CELL_SIGNOFF_GATE_ENFORCEMENT_CI_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_019_execut…` |
| [DETERMINEX_RELEASE_CELL_VERIFIER_SIGNOFF_SCHEMA_LOCK_001](../locks/sentinel/DETERMINEX_RELEASE_CELL_VERIFIER_SIGNOFF_SCHEMA_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_016_canoni…` |
| [DETERMINEX_RELEASE_GATE_BETA_DASHBOARD_PUBLICATION_GATE_LOCK_001](../locks/sentinel/DETERMINEX_RELEASE_GATE_BETA_DASHBOARD_PUBLICATION_GATE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_RELEASE_GATE_CLEAN_HOST_PACKET_CERTIFICATION_LOCK_001](../locks/sentinel/DETERMINEX_RELEASE_GATE_CLEAN_HOST_PACKET_CERTIFICATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_RELEASE_GATE_FULL_STATUS_TIMEOUT_REPAIR_PLAN_LOCK_001](../locks/sentinel/DETERMINEX_RELEASE_GATE_FULL_STATUS_TIMEOUT_REPAIR_PLAN_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_RELEASE_GATE_GUI_BUILD_PACKET_CERTIFICATION_LOCK_001](../locks/sentinel/DETERMINEX_RELEASE_GATE_GUI_BUILD_PACKET_CERTIFICATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_RELEASE_GATE_INSTALLER_RELEASE_PACKET_CERTIFICATION_LOCK_001](../locks/sentinel/DETERMINEX_RELEASE_GATE_INSTALLER_RELEASE_PACKET_CERTIFICATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_RELEASE_GATE_REACT_VITE_DEPENDENCY_ADMISSION_LOCK_001](../locks/sentinel/DETERMINEX_RELEASE_GATE_REACT_VITE_DEPENDENCY_ADMISSION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_RELEASE_GATE_SBOM_PACKET_CERTIFICATION_LOCK_001](../locks/sentinel/DETERMINEX_RELEASE_GATE_SBOM_PACKET_CERTIFICATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_RELEASE_HYGIENE_SBOM_LICENSE_SECURITY_SIGNING_EXECUTION_LOCK_001](../locks/sentinel/DETERMINEX_RELEASE_HYGIENE_SBOM_LICENSE_SECURITY_SIGNING_EXECUTION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_release_hygiene…` |
| [DETERMINEX_RELEASE_INSTALL_PACKAGING_GAP_AUDIT_001](../locks/sentinel/DETERMINEX_RELEASE_INSTALL_PACKAGING_GAP_AUDIT_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_release_install…` |
| [DETERMINEX_RELEASE_PROMOTION_GATE_NEGATIVE_TESTS_LOCK_001](../locks/sentinel/DETERMINEX_RELEASE_PROMOTION_GATE_NEGATIVE_TESTS_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_017_canoni…` |
| [DETERMINEX_RELEASE_REGISTRY_MUTATION_SIGNOFF_LOCK_001](../locks/sentinel/DETERMINEX_RELEASE_REGISTRY_MUTATION_SIGNOFF_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_RELEASE_SUPPORTED_CELL_CONVEYOR_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_RELEASE_SUPPORTED_CELL_CONVEYOR_BINDING_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_016_canoni…` |
| [DETERMINEX_RELEASE_SUPPORTED_CELL_DRIFT_DETECTOR_CI_LOCK_001](../locks/sentinel/DETERMINEX_RELEASE_SUPPORTED_CELL_DRIFT_DETECTOR_CI_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_016_canoni…` |
| [DETERMINEX_REMAINING_FAMILY_AUTHORITY_BATCH_GATE_LOCK_001](../locks/sentinel/DETERMINEX_REMAINING_FAMILY_AUTHORITY_BATCH_GATE_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_REMAINING_FAMILY_BROWSER_TAURI_COMPRESSION_LOCK_001](../locks/sentinel/DETERMINEX_REMAINING_FAMILY_BROWSER_TAURI_COMPRESSION_LOCK_001.json) | 18 | 1 | `e4ff17592c` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_admitted_clean_…` |
| [DETERMINEX_REMAINING_FAMILY_COMPLETION_SURGE_LOCK_001](../locks/sentinel/DETERMINEX_REMAINING_FAMILY_COMPLETION_SURGE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_REMAINING_FAMILY_HIGH_RISK_BOUNDARY_LOCK_001](../locks/sentinel/DETERMINEX_REMAINING_FAMILY_HIGH_RISK_BOUNDARY_LOCK_001.json) | 21 | 21 | `pending-fi` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_runner_sa…` |
| [DETERMINEX_REMAINING_FAMILY_HIGH_RISK_COMPRESSION_LOCK_001](../locks/sentinel/DETERMINEX_REMAINING_FAMILY_HIGH_RISK_COMPRESSION_LOCK_001.json) | 18 | 1 | `e4ff17592c` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_admitted_clean_…` |
| [DETERMINEX_REMAINING_FAMILY_KOTLIN_SWIFT_GATE_LOCK_001](../locks/sentinel/DETERMINEX_REMAINING_FAMILY_KOTLIN_SWIFT_GATE_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_REMAINING_FAMILY_PHP_RUBY_COMPRESSION_LOCK_001](../locks/sentinel/DETERMINEX_REMAINING_FAMILY_PHP_RUBY_COMPRESSION_LOCK_001.json) | 18 | 1 | `e4ff17592c` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_admitted_clean_…` |
| [DETERMINEX_REMAINING_FAMILY_PHP_RUBY_GATE_LOCK_001](../locks/sentinel/DETERMINEX_REMAINING_FAMILY_PHP_RUBY_GATE_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_REMAINING_FAMILY_SAFE_EXECUTION_BATCH_LOCK_001](../locks/sentinel/DETERMINEX_REMAINING_FAMILY_SAFE_EXECUTION_BATCH_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_REMAINING_FAMILY_STATUS_EXPANSION_LOCK_001](../locks/sentinel/DETERMINEX_REMAINING_FAMILY_STATUS_EXPANSION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_REMAINING_FAMILY_STRUCTURAL_GATE_LOCK_001](../locks/sentinel/DETERMINEX_REMAINING_FAMILY_STRUCTURAL_GATE_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_REPAIR_LOOP_READINESS_MAP_LOCK_001](../locks/sentinel/DETERMINEX_REPAIR_LOOP_READINESS_MAP_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_019_execut…` |
| [DETERMINEX_REPO_CLINIC_FIXTURE_REPAIR_SPLASH_DEMO_LOCK_001](../locks/sentinel/DETERMINEX_REPO_CLINIC_FIXTURE_REPAIR_SPLASH_DEMO_LOCK_001.json) | 12 | 12 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_determinex_repo_cl…` |
| [DETERMINEX_REPO_CLINIC_PROGRAM_AUTHORITY_INTAKE_LOCK_001](../locks/sentinel/DETERMINEX_REPO_CLINIC_PROGRAM_AUTHORITY_INTAKE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_REPO_CLINIC_REPAIR_LOOP_SECOND_FAMILY_LOCK_001](../locks/sentinel/DETERMINEX_REPO_CLINIC_REPAIR_LOOP_SECOND_FAMILY_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_REPO_CLINIC_UNDER_THE_HOOD_E2E_PIPELINE_LOCK_001](../locks/sentinel/DETERMINEX_REPO_CLINIC_UNDER_THE_HOOD_E2E_PIPELINE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_under…` |
| [DETERMINEX_REPO_CLINIC_WORKFLOW_LOCK_001](../locks/sentinel/DETERMINEX_REPO_CLINIC_WORKFLOW_LOCK_001.json) | 18 | 18 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_repo_clinic_workfl…` |
| [DETERMINEX_REVIEW_MARKER_HASH_AND_STABILITY_HARDENING_LOCK_001](../locks/sentinel/DETERMINEX_REVIEW_MARKER_HASH_AND_STABILITY_HARDENING_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_real_signature_…` |
| [DETERMINEX_RUBY_STRUCTURAL_MAPPING_BOUNDARY_GUARD_LOCK_001](../locks/sentinel/DETERMINEX_RUBY_STRUCTURAL_MAPPING_BOUNDARY_GUARD_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_RUBY_TOOLCHAIN_ABSENCE_GATE_LOCK_001](../locks/sentinel/DETERMINEX_RUBY_TOOLCHAIN_ABSENCE_GATE_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_RUNTIME_APPROVAL_HARDENING_BACKFILL_LOCK_002](../locks/sentinel/DETERMINEX_RUNTIME_APPROVAL_HARDENING_BACKFILL_LOCK_002.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_017_canoni…` |
| [DETERMINEX_RUNTIME_APPROVAL_HARDENING_BEFORE_FIRST_SPEND_LOCK_001](../locks/sentinel/DETERMINEX_RUNTIME_APPROVAL_HARDENING_BEFORE_FIRST_SPEND_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_016_canoni…` |
| [DETERMINEX_RUNTIME_APPROVAL_HARDENING_COMPLETION_LOCK_003](../locks/sentinel/DETERMINEX_RUNTIME_APPROVAL_HARDENING_COMPLETION_LOCK_003.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_018_canoni…` |
| [DETERMINEX_RUNTIME_APPROVAL_HARDENING_TESTS_LIVE_LOCK_001](../locks/sentinel/DETERMINEX_RUNTIME_APPROVAL_HARDENING_TESTS_LIVE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_019_execut…` |
| [DETERMINEX_RVREP_CLAUDE_BETA_DASHBOARD_NOT_PUBLISHED_REVIEW_001](../locks/sentinel/DETERMINEX_RVREP_CLAUDE_BETA_DASHBOARD_NOT_PUBLISHED_REVIEW_001.json) | 1 | 1 | `96368312fc` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rvrep_claude_be…` |
| [DETERMINEX_RVREP_CLAUDE_BINARY_MUTATION_REVIEW_001](../locks/sentinel/DETERMINEX_RVREP_CLAUDE_BINARY_MUTATION_REVIEW_001.json) | 1 | 1 | `96368312fc` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rvrep_claude_bi…` |
| [DETERMINEX_RVREP_CLAUDE_BOUNDED_REPAIR_GUARD_REVIEW_001](../locks/sentinel/DETERMINEX_RVREP_CLAUDE_BOUNDED_REPAIR_GUARD_REVIEW_001.json) | 1 | 1 | `96368312fc` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rvrep_claude_bo…` |
| [DETERMINEX_RVREP_CLAUDE_BUILD_RETRY_REVIEW_001](../locks/sentinel/DETERMINEX_RVREP_CLAUDE_BUILD_RETRY_REVIEW_001.json) | 1 | 1 | `96368312fc` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rvrep_claude_bu…` |
| [DETERMINEX_RVREP_CLAUDE_CHANGED_SOURCE_FILES_REVIEW_001](../locks/sentinel/DETERMINEX_RVREP_CLAUDE_CHANGED_SOURCE_FILES_REVIEW_001.json) | 1 | 1 | `96368312fc` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rvrep_claude_ch…` |
| [DETERMINEX_RVREP_CLAUDE_CLEAN_HOST_NOT_EXECUTED_REVIEW_001](../locks/sentinel/DETERMINEX_RVREP_CLAUDE_CLEAN_HOST_NOT_EXECUTED_REVIEW_001.json) | 1 | 1 | `96368312fc` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rvrep_claude_cl…` |
| [DETERMINEX_RVREP_CLAUDE_EVIDENCE_INDEX_GUARDS_REVIEW_001](../locks/sentinel/DETERMINEX_RVREP_CLAUDE_EVIDENCE_INDEX_GUARDS_REVIEW_001.json) | 1 | 1 | `96368312fc` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rvrep_claude_ev…` |
| [DETERMINEX_RVREP_CLAUDE_FAMILY_STATUSES_SAFE_REVIEW_001](../locks/sentinel/DETERMINEX_RVREP_CLAUDE_FAMILY_STATUSES_SAFE_REVIEW_001.json) | 1 | 1 | `96368312fc` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rvrep_claude_fa…` |
| [DETERMINEX_RVREP_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001](../locks/sentinel/DETERMINEX_RVREP_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001.json) | 1 | 1 | `96368312fc` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rvrep_claude_fo…` |
| [DETERMINEX_RVREP_CLAUDE_GUI_BUILD_NOT_EXECUTED_REVIEW_001](../locks/sentinel/DETERMINEX_RVREP_CLAUDE_GUI_BUILD_NOT_EXECUTED_REVIEW_001.json) | 1 | 1 | `96368312fc` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rvrep_claude_gu…` |
| [DETERMINEX_RVREP_CLAUDE_INSTALLER_RELEASE_NOT_EXECUTED_REVIEW_001](../locks/sentinel/DETERMINEX_RVREP_CLAUDE_INSTALLER_RELEASE_NOT_EXECUTED_REVIEW_001.json) | 1 | 1 | `96368312fc` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rvrep_claude_in…` |
| [DETERMINEX_RVREP_CLAUDE_LINT_CLASSIFICATION_REVIEW_001](../locks/sentinel/DETERMINEX_RVREP_CLAUDE_LINT_CLASSIFICATION_REVIEW_001.json) | 1 | 1 | `96368312fc` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rvrep_claude_li…` |
| [DETERMINEX_RVREP_CLAUDE_LINT_CONFIG_MUTATION_REVIEW_001](../locks/sentinel/DETERMINEX_RVREP_CLAUDE_LINT_CONFIG_MUTATION_REVIEW_001.json) | 1 | 1 | `96368312fc` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rvrep_claude_li…` |
| [DETERMINEX_RVREP_CLAUDE_LINT_RETRY_REVIEW_001](../locks/sentinel/DETERMINEX_RVREP_CLAUDE_LINT_RETRY_REVIEW_001.json) | 1 | 1 | `96368312fc` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rvrep_claude_li…` |
| [DETERMINEX_RVREP_CLAUDE_LOCKFILE_MUTATION_REVIEW_001](../locks/sentinel/DETERMINEX_RVREP_CLAUDE_LOCKFILE_MUTATION_REVIEW_001.json) | 1 | 1 | `96368312fc` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rvrep_claude_lo…` |
| [DETERMINEX_RVREP_CLAUDE_MARCH_PLAN_DASHBOARD_REVIEW_001](../locks/sentinel/DETERMINEX_RVREP_CLAUDE_MARCH_PLAN_DASHBOARD_REVIEW_001.json) | 1 | 1 | `96368312fc` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rvrep_claude_ma…` |
| [DETERMINEX_RVREP_CLAUDE_NO_MUTATION_GUARD_REVIEW_001](../locks/sentinel/DETERMINEX_RVREP_CLAUDE_NO_MUTATION_GUARD_REVIEW_001.json) | 1 | 1 | `96368312fc` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rvrep_claude_no…` |
| [DETERMINEX_RVREP_CLAUDE_REACT_VITE_VERIFICATION_REVIEW_001](../locks/sentinel/DETERMINEX_RVREP_CLAUDE_REACT_VITE_VERIFICATION_REVIEW_001.json) | 1 | 1 | `96368312fc` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rvrep_claude_re…` |
| [DETERMINEX_RVREP_CLAUDE_RELEASE_INVARIANTS_REVIEW_001](../locks/sentinel/DETERMINEX_RVREP_CLAUDE_RELEASE_INVARIANTS_REVIEW_001.json) | 1 | 1 | `96368312fc` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rvrep_claude_re…` |
| [DETERMINEX_RVREP_CLAUDE_RUNTIME_QUEUE_CONSISTENCY_REVIEW_001](../locks/sentinel/DETERMINEX_RVREP_CLAUDE_RUNTIME_QUEUE_CONSISTENCY_REVIEW_001.json) | 1 | 1 | `96368312fc` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rvrep_claude_ru…` |
| [DETERMINEX_RVREP_CLAUDE_SBOM_NOT_EXECUTED_REVIEW_001](../locks/sentinel/DETERMINEX_RVREP_CLAUDE_SBOM_NOT_EXECUTED_REVIEW_001.json) | 1 | 1 | `96368312fc` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rvrep_claude_sb…` |
| [DETERMINEX_RVREP_CLAUDE_SCORE_MOVEMENT_REVIEW_001](../locks/sentinel/DETERMINEX_RVREP_CLAUDE_SCORE_MOVEMENT_REVIEW_001.json) | 1 | 1 | `96368312fc` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rvrep_claude_sc…` |
| [DETERMINEX_RVREP_CLAUDE_SIGNED_SPEND_CONSISTENCY_REVIEW_001](../locks/sentinel/DETERMINEX_RVREP_CLAUDE_SIGNED_SPEND_CONSISTENCY_REVIEW_001.json) | 1 | 1 | `96368312fc` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rvrep_claude_si…` |
| [DETERMINEX_RVREP_CLAUDE_SMOKE_RETRY_REVIEW_001](../locks/sentinel/DETERMINEX_RVREP_CLAUDE_SMOKE_RETRY_REVIEW_001.json) | 1 | 1 | `96368312fc` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rvrep_claude_sm…` |
| [DETERMINEX_RVREP_CLAUDE_SOURCE_REPAIR_BOUNDED_REVIEW_001](../locks/sentinel/DETERMINEX_RVREP_CLAUDE_SOURCE_REPAIR_BOUNDED_REVIEW_001.json) | 1 | 1 | `96368312fc` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rvrep_claude_so…` |
| [DETERMINEX_RVREP_CLAUDE_SYNTHESIS_REVIEW_001](../locks/sentinel/DETERMINEX_RVREP_CLAUDE_SYNTHESIS_REVIEW_001.json) | 1 | 1 | `96368312fc` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rvrep_claude_sy…` |
| [DETERMINEX_RVREP_CLAUDE_TEST_MUTATION_REVIEW_001](../locks/sentinel/DETERMINEX_RVREP_CLAUDE_TEST_MUTATION_REVIEW_001.json) | 1 | 1 | `96368312fc` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rvrep_claude_te…` |
| [DETERMINEX_RVREP_CLAUDE_TEST_RETRY_REVIEW_001](../locks/sentinel/DETERMINEX_RVREP_CLAUDE_TEST_RETRY_REVIEW_001.json) | 1 | 1 | `96368312fc` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rvrep_claude_te…` |
| [DETERMINEX_RVREP_CLAUDE_TIER1_PROMOTION_CANONICAL_REVIEW_001](../locks/sentinel/DETERMINEX_RVREP_CLAUDE_TIER1_PROMOTION_CANONICAL_REVIEW_001.json) | 1 | 1 | `96368312fc` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rvrep_claude_ti…` |
| [DETERMINEX_RVREP_CLAUDE_UNIVERSAL_ACCOUNTING_MAP_REVIEW_001](../locks/sentinel/DETERMINEX_RVREP_CLAUDE_UNIVERSAL_ACCOUNTING_MAP_REVIEW_001.json) | 1 | 1 | `96368312fc` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rvrep_claude_un…` |
| [DETERMINEX_RVREP_CLAUDE_VERIFICATION_WITH_CAPABILITY_REVIEW_001](../locks/sentinel/DETERMINEX_RVREP_CLAUDE_VERIFICATION_WITH_CAPABILITY_REVIEW_001.json) | 1 | 1 | `96368312fc` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rvrep_claude_ve…` |
| [DETERMINEX_RVREP_CLAUDE_VERIFIER_ORACLE_MUTATION_REVIEW_001](../locks/sentinel/DETERMINEX_RVREP_CLAUDE_VERIFIER_ORACLE_MUTATION_REVIEW_001.json) | 1 | 1 | `96368312fc` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rvrep_claude_ve…` |
| [DETERMINEX_RV_VERIFY_CLAUDE_ADMISSION_VS_VERIFICATION_BOUNDARY_REVIEW_001](../locks/sentinel/DETERMINEX_RV_VERIFY_CLAUDE_ADMISSION_VS_VERIFICATION_BOUNDARY_REVIEW_001.json) | 1 | 1 | `c789a83198` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rv_verify_claud…` |
| [DETERMINEX_RV_VERIFY_CLAUDE_APPEND_ONLY_COUNT_DRIFT_REVIEW_001](../locks/sentinel/DETERMINEX_RV_VERIFY_CLAUDE_APPEND_ONLY_COUNT_DRIFT_REVIEW_001.json) | 1 | 1 | `c789a83198` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rv_verify_claud…` |
| [DETERMINEX_RV_VERIFY_CLAUDE_BETA_DASHBOARD_NOT_PUBLISHED_REVIEW_001](../locks/sentinel/DETERMINEX_RV_VERIFY_CLAUDE_BETA_DASHBOARD_NOT_PUBLISHED_REVIEW_001.json) | 1 | 1 | `c789a83198` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rv_verify_claud…` |
| [DETERMINEX_RV_VERIFY_CLAUDE_BUILD_RESULT_ACCURATE_REVIEW_001](../locks/sentinel/DETERMINEX_RV_VERIFY_CLAUDE_BUILD_RESULT_ACCURATE_REVIEW_001.json) | 1 | 1 | `c789a83198` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rv_verify_claud…` |
| [DETERMINEX_RV_VERIFY_CLAUDE_CHANGED_FILES_ALLOWED_REVIEW_001](../locks/sentinel/DETERMINEX_RV_VERIFY_CLAUDE_CHANGED_FILES_ALLOWED_REVIEW_001.json) | 1 | 1 | `c789a83198` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rv_verify_claud…` |
| [DETERMINEX_RV_VERIFY_CLAUDE_CLAIM_OVERCLAIM_SCANNER_REVIEW_001](../locks/sentinel/DETERMINEX_RV_VERIFY_CLAUDE_CLAIM_OVERCLAIM_SCANNER_REVIEW_001.json) | 1 | 1 | `c789a83198` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rv_verify_claud…` |
| [DETERMINEX_RV_VERIFY_CLAUDE_CLEAN_HOST_NOT_EXECUTED_REVIEW_001](../locks/sentinel/DETERMINEX_RV_VERIFY_CLAUDE_CLEAN_HOST_NOT_EXECUTED_REVIEW_001.json) | 1 | 1 | `c789a83198` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rv_verify_claud…` |
| [DETERMINEX_RV_VERIFY_CLAUDE_DIRTY_STATE_REPORTED_REVIEW_001](../locks/sentinel/DETERMINEX_RV_VERIFY_CLAUDE_DIRTY_STATE_REPORTED_REVIEW_001.json) | 1 | 1 | `c789a83198` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rv_verify_claud…` |
| [DETERMINEX_RV_VERIFY_CLAUDE_EVIDENCE_INDEX_CLEAN_REVIEW_001](../locks/sentinel/DETERMINEX_RV_VERIFY_CLAUDE_EVIDENCE_INDEX_CLEAN_REVIEW_001.json) | 1 | 1 | `c789a83198` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rv_verify_claud…` |
| [DETERMINEX_RV_VERIFY_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001](../locks/sentinel/DETERMINEX_RV_VERIFY_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001.json) | 1 | 1 | `c789a83198` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rv_verify_claud…` |
| [DETERMINEX_RV_VERIFY_CLAUDE_GUI_BUILD_NOT_EXECUTED_REVIEW_001](../locks/sentinel/DETERMINEX_RV_VERIFY_CLAUDE_GUI_BUILD_NOT_EXECUTED_REVIEW_001.json) | 1 | 1 | `c789a83198` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rv_verify_claud…` |
| [DETERMINEX_RV_VERIFY_CLAUDE_INSTALLER_RELEASE_NOT_EXECUTED_REVIEW_001](../locks/sentinel/DETERMINEX_RV_VERIFY_CLAUDE_INSTALLER_RELEASE_NOT_EXECUTED_REVIEW_001.json) | 1 | 1 | `c789a83198` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rv_verify_claud…` |
| [DETERMINEX_RV_VERIFY_CLAUDE_NO_FORBIDDEN_PROTECTED_ACTION_REVIEW_001](../locks/sentinel/DETERMINEX_RV_VERIFY_CLAUDE_NO_FORBIDDEN_PROTECTED_ACTION_REVIEW_001.json) | 1 | 1 | `c789a83198` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rv_verify_claud…` |
| [DETERMINEX_RV_VERIFY_CLAUDE_NO_UNRELATED_DRIFT_REVIEW_001](../locks/sentinel/DETERMINEX_RV_VERIFY_CLAUDE_NO_UNRELATED_DRIFT_REVIEW_001.json) | 1 | 1 | `c789a83198` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rv_verify_claud…` |
| [DETERMINEX_RV_VERIFY_CLAUDE_PRIOR_SPEND_BINDING_REVIEW_001](../locks/sentinel/DETERMINEX_RV_VERIFY_CLAUDE_PRIOR_SPEND_BINDING_REVIEW_001.json) | 1 | 1 | `c789a83198` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rv_verify_claud…` |
| [DETERMINEX_RV_VERIFY_CLAUDE_RELEASE_CELLS_CANONICAL_REVIEW_001](../locks/sentinel/DETERMINEX_RV_VERIFY_CLAUDE_RELEASE_CELLS_CANONICAL_REVIEW_001.json) | 1 | 1 | `c789a83198` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rv_verify_claud…` |
| [DETERMINEX_RV_VERIFY_CLAUDE_RELEASE_FAMILIES_CANONICAL_REVIEW_001](../locks/sentinel/DETERMINEX_RV_VERIFY_CLAUDE_RELEASE_FAMILIES_CANONICAL_REVIEW_001.json) | 1 | 1 | `c789a83198` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rv_verify_claud…` |
| [DETERMINEX_RV_VERIFY_CLAUDE_RUNTIME_QUEUE_SPEND_CONSISTENCY_REVIEW_001](../locks/sentinel/DETERMINEX_RV_VERIFY_CLAUDE_RUNTIME_QUEUE_SPEND_CONSISTENCY_REVIEW_001.json) | 1 | 1 | `c789a83198` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rv_verify_claud…` |
| [DETERMINEX_RV_VERIFY_CLAUDE_SBOM_NOT_EXECUTED_REVIEW_001](../locks/sentinel/DETERMINEX_RV_VERIFY_CLAUDE_SBOM_NOT_EXECUTED_REVIEW_001.json) | 1 | 1 | `c789a83198` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rv_verify_claud…` |
| [DETERMINEX_RV_VERIFY_CLAUDE_SCORE_MOVEMENT_EVIDENCE_BOUND_REVIEW_001](../locks/sentinel/DETERMINEX_RV_VERIFY_CLAUDE_SCORE_MOVEMENT_EVIDENCE_BOUND_REVIEW_001.json) | 1 | 1 | `c789a83198` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rv_verify_claud…` |
| [DETERMINEX_RV_VERIFY_CLAUDE_SMOKE_LINT_RESULT_ACCURATE_REVIEW_001](../locks/sentinel/DETERMINEX_RV_VERIFY_CLAUDE_SMOKE_LINT_RESULT_ACCURATE_REVIEW_001.json) | 1 | 1 | `c789a83198` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rv_verify_claud…` |
| [DETERMINEX_RV_VERIFY_CLAUDE_SYNTHESIS_REVIEW_001](../locks/sentinel/DETERMINEX_RV_VERIFY_CLAUDE_SYNTHESIS_REVIEW_001.json) | 1 | 1 | `c789a83198` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rv_verify_claud…` |
| [DETERMINEX_RV_VERIFY_CLAUDE_TEST_RESULT_ACCURATE_REVIEW_001](../locks/sentinel/DETERMINEX_RV_VERIFY_CLAUDE_TEST_RESULT_ACCURATE_REVIEW_001.json) | 1 | 1 | `c789a83198` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rv_verify_claud…` |
| [DETERMINEX_RV_VERIFY_CLAUDE_TIER1_PROMOTION_CANONICAL_REVIEW_001](../locks/sentinel/DETERMINEX_RV_VERIFY_CLAUDE_TIER1_PROMOTION_CANONICAL_REVIEW_001.json) | 1 | 1 | `c789a83198` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rv_verify_claud…` |
| [DETERMINEX_RV_VERIFY_CLAUDE_TIMEOUT_NOT_HIDDEN_REVIEW_001](../locks/sentinel/DETERMINEX_RV_VERIFY_CLAUDE_TIMEOUT_NOT_HIDDEN_REVIEW_001.json) | 1 | 1 | `c789a83198` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rv_verify_claud…` |
| [DETERMINEX_RV_VERIFY_CLAUDE_VERIFICATION_COMMANDS_BOUNDED_REVIEW_001](../locks/sentinel/DETERMINEX_RV_VERIFY_CLAUDE_VERIFICATION_COMMANDS_BOUNDED_REVIEW_001.json) | 1 | 1 | `c789a83198` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rv_verify_claud…` |
| [DETERMINEX_RV_VERIFY_CLAUDE_VERIFICATION_PLAN_REAL_SCRIPTS_REVIEW_001](../locks/sentinel/DETERMINEX_RV_VERIFY_CLAUDE_VERIFICATION_PLAN_REAL_SCRIPTS_REVIEW_001.json) | 1 | 1 | `c789a83198` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rv_verify_claud…` |
| [DETERMINEX_RV_VERIFY_CLAUDE_VERIFICATION_TRANSCRIPTS_EXIST_REVIEW_001](../locks/sentinel/DETERMINEX_RV_VERIFY_CLAUDE_VERIFICATION_TRANSCRIPTS_EXIST_REVIEW_001.json) | 1 | 1 | `c789a83198` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_rv_verify_claud…` |
| [DETERMINEX_SBOM_BLOCKER_REVALIDATION_LOCK_001](../locks/sentinel/DETERMINEX_SBOM_BLOCKER_REVALIDATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_SBOM_BYTE_EXACT_POLICY_LOCK_001](../locks/sentinel/DETERMINEX_SBOM_BYTE_EXACT_POLICY_LOCK_001.json) | 18 | 1 | `e4ff17592c` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_admitted_clean_…` |
| [DETERMINEX_SBOM_EXECUTION_RETRY_LOCK_001](../locks/sentinel/DETERMINEX_SBOM_EXECUTION_RETRY_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_SBOM_EXECUTION_VERIFICATION_LOCK_001](../locks/sentinel/DETERMINEX_SBOM_EXECUTION_VERIFICATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_SBOM_FAMILY_SURGE_CAPABILITY_SCORE_DISCIPLINE_LOCK_001](../locks/sentinel/DETERMINEX_SBOM_FAMILY_SURGE_CAPABILITY_SCORE_DISCIPLINE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_SBOM_FAMILY_SURGE_MARCH_PLAN_DASHBOARD_LOCK_001](../locks/sentinel/DETERMINEX_SBOM_FAMILY_SURGE_MARCH_PLAN_DASHBOARD_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_SBOM_LICENSE_SECURITY_SIGNING_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_SBOM_LICENSE_SECURITY_SIGNING_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_sbom_license_se…` |
| [DETERMINEX_SBOM_LICENSE_SECURITY_SIGNING_TRUST_CHAIN_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_SBOM_LICENSE_SECURITY_SIGNING_TRUST_CHAIN_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_sbom_license_se…` |
| [DETERMINEX_SBOM_LICENSE_SECURITY_TRUST_SPINE_LOCK_001](../locks/sentinel/DETERMINEX_SBOM_LICENSE_SECURITY_TRUST_SPINE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_SBOM_NEXT_GATE_AFTER_CLEAN_HOST_RUNTIME_LOCK_001](../locks/sentinel/DETERMINEX_SBOM_NEXT_GATE_AFTER_CLEAN_HOST_RUNTIME_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_SBOM_PACKET_CARRY_AFTER_SIGNATURE_CHANNEL_LOCK_001](../locks/sentinel/DETERMINEX_SBOM_PACKET_CARRY_AFTER_SIGNATURE_CHANNEL_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_real_signature_…` |
| [DETERMINEX_SBOM_PACKET_HARDENING_LOCK_001](../locks/sentinel/DETERMINEX_SBOM_PACKET_HARDENING_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_SBOM_ROUTE_DECISION_LOCK_001](../locks/sentinel/DETERMINEX_SBOM_ROUTE_DECISION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_SBOM_SIGNING_INSTALLER_TRUST_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_SBOM_SIGNING_INSTALLER_TRUST_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_007_sbom_s…` |
| [DETERMINEX_SBOM_TOOL_ADMISSION_AND_STANDARDS_SBOM_GENERATION_LOCK_001](../locks/sentinel/DETERMINEX_SBOM_TOOL_ADMISSION_AND_STANDARDS_SBOM_GENERATION_LOCK_001.json) | 12 | 12 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_sbom_tool_admis…` |
| [DETERMINEX_SBOM_TOOL_ADMISSION_DECISION_LOCK_001](../locks/sentinel/DETERMINEX_SBOM_TOOL_ADMISSION_DECISION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_SBOM_TOOL_FAMILY_SURGE_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_SBOM_TOOL_FAMILY_SURGE_RECONCILIATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_SBOM_TOOL_INSTALL_OR_ALTERNATIVE_VERIFICATION_LOCK_001](../locks/sentinel/DETERMINEX_SBOM_TOOL_INSTALL_OR_ALTERNATIVE_VERIFICATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_SBOM_TOOL_RUNTIME_ADMISSION_SPEND_LOCK_001](../locks/sentinel/DETERMINEX_SBOM_TOOL_RUNTIME_ADMISSION_SPEND_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_SCAFFOLD_BUILD_TEST_SMOKE_EXPANSION_LOCK_001](../locks/sentinel/DETERMINEX_SCAFFOLD_BUILD_TEST_SMOKE_EXPANSION_LOCK_001.json) | 20 | 20 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_scaffold_build_…` |
| [DETERMINEX_SCORE_BASELINE_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_SCORE_BASELINE_RECONCILIATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_first_authority…` |
| [DETERMINEX_SCORE_DEFINITION_BINDING_AND_EVIDENCE_DELTA_CI_LOCK_001](../locks/sentinel/DETERMINEX_SCORE_DEFINITION_BINDING_AND_EVIDENCE_DELTA_CI_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_SCORE_DELTA_CI_AND_PUBLIC_CLAIM_LINTER_EXPANSION_LOCK_001](../locks/sentinel/DETERMINEX_SCORE_DELTA_CI_AND_PUBLIC_CLAIM_LINTER_EXPANSION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_014_signed…` |
| [DETERMINEX_SCORE_DELTA_CI_AND_PUBLIC_CLAIM_SCANNER_CLOSURE_LOCK_002](../locks/sentinel/DETERMINEX_SCORE_DELTA_CI_AND_PUBLIC_CLAIM_SCANNER_CLOSURE_LOCK_002.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_015_canoni…` |
| [DETERMINEX_SCORE_RELEASE_DISCIPLINE_LOCK_001](../locks/sentinel/DETERMINEX_SCORE_RELEASE_DISCIPLINE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_SCORE_RISE_REQUIRES_EVIDENCE_DELTA_CI_LOCK_001](../locks/sentinel/DETERMINEX_SCORE_RISE_REQUIRES_EVIDENCE_DELTA_CI_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_SIGNABLE_APPROVAL_PACKET_FINALIZATION_SWEEP_LOCK_001](../locks/sentinel/DETERMINEX_SIGNABLE_APPROVAL_PACKET_FINALIZATION_SWEEP_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_SIGNATURE_DELIVERY_CHANNEL_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_SIGNATURE_DELIVERY_CHANNEL_RECONCILIATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_signature_deliv…` |
| [DETERMINEX_SIGNATURE_DELIVERY_CURRENT_STATE_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_SIGNATURE_DELIVERY_CURRENT_STATE_RECONCILIATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_signature_deliv…` |
| [DETERMINEX_SIGNATURE_DELIVERY_REVIEW_READY_PROTOCOL_LOCK_001](../locks/sentinel/DETERMINEX_SIGNATURE_DELIVERY_REVIEW_READY_PROTOCOL_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_signature_deliv…` |
| [DETERMINEX_SIGNATURE_INGEST_CURRENT_STATE_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_SIGNATURE_INGEST_CURRENT_STATE_RECONCILIATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_real_signature_…` |
| [DETERMINEX_SIGNATURE_INGEST_SPEND_SCORE_BOUNDARY_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_SIGNATURE_INGEST_SPEND_SCORE_BOUNDARY_RECONCILIATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_real_signature_…` |
| [DETERMINEX_SIGNATURE_SPEND_CURRENT_STATE_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_SIGNATURE_SPEND_CURRENT_STATE_RECONCILIATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_signature_spend…` |
| [DETERMINEX_SIGNATURE_SPEND_REVIEW_READY_PROTOCOL_LOCK_001](../locks/sentinel/DETERMINEX_SIGNATURE_SPEND_REVIEW_READY_PROTOCOL_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_signature_spend…` |
| [DETERMINEX_SIGNATURE_SPEND_SCORE_AND_COVERAGE_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_SIGNATURE_SPEND_SCORE_AND_COVERAGE_RECONCILIATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_signature_spend…` |
| [DETERMINEX_SIGNED_APPROVAL_OPERATOR_AUTHORITY_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_SIGNED_APPROVAL_OPERATOR_AUTHORITY_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_signed_approval…` |
| [DETERMINEX_SIGNED_GUI_DRIVER_FIRST_VISUAL_PROOF_LOCK_002](../locks/sentinel/DETERMINEX_SIGNED_GUI_DRIVER_FIRST_VISUAL_PROOF_LOCK_002.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_015_canoni…` |
| [DETERMINEX_SIGNED_GUI_DRIVER_FIRST_VISUAL_SPEND_LOCK_001](../locks/sentinel/DETERMINEX_SIGNED_GUI_DRIVER_FIRST_VISUAL_SPEND_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_014_signed…` |
| [DETERMINEX_SIGNED_MSEDGEDRIVER_ADMISSION_AND_GUI_FIRST_PAINT_EXECUTION_LOCK_001](../locks/sentinel/DETERMINEX_SIGNED_MSEDGEDRIVER_ADMISSION_AND_GUI_FIRST_PAINT_EXECUTION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_signed_msedgedr…` |
| [DETERMINEX_SIGNED_MSEDGEDRIVER_AND_GUI_FIRST_PAINT_EXECUTION_LOCK_002](../locks/sentinel/DETERMINEX_SIGNED_MSEDGEDRIVER_AND_GUI_FIRST_PAINT_EXECUTION_LOCK_002.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_SIGNED_MSEDGEDRIVER_AND_GUI_FIRST_PAINT_EXECUTION_LOCK_003](../locks/sentinel/DETERMINEX_SIGNED_MSEDGEDRIVER_AND_GUI_FIRST_PAINT_EXECUTION_LOCK_003.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_SIGNED_NSIS_APPROVAL_AND_INSTALL_LAUNCH_UNINSTALL_RETRY_LOCK_001](../locks/sentinel/DETERMINEX_SIGNED_NSIS_APPROVAL_AND_INSTALL_LAUNCH_UNINSTALL_RETRY_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_signed_nsis_app…` |
| [DETERMINEX_SIGNED_NSIS_APPROVAL_AND_INSTALL_SMOKE_EXECUTION_LOCK_002](../locks/sentinel/DETERMINEX_SIGNED_NSIS_APPROVAL_AND_INSTALL_SMOKE_EXECUTION_LOCK_002.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_SIGNED_QUEUE_SPEND_ELIGIBILITY_GATE_LOCK_001](../locks/sentinel/DETERMINEX_SIGNED_QUEUE_SPEND_ELIGIBILITY_GATE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_signature_spend…` |
| [DETERMINEX_SIGNED_SPEND_AUDIT_AND_BOUNDARY_LOCK_001](../locks/sentinel/DETERMINEX_SIGNED_SPEND_AUDIT_AND_BOUNDARY_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_signature_spend…` |
| [DETERMINEX_SIGNED_VALID_APPROVAL_QUEUE_MATERIALIZATION_LOCK_001](../locks/sentinel/DETERMINEX_SIGNED_VALID_APPROVAL_QUEUE_MATERIALIZATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_SIGNED_VALID_QUEUE_IMPORT_REACT_VITE_LOCK_001](../locks/sentinel/DETERMINEX_SIGNED_VALID_QUEUE_IMPORT_REACT_VITE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_real_signature_…` |
| [DETERMINEX_SIG_DELIVERY_CLAUDE_AUTHORITY_BOUNDARY_REVIEW_001](../locks/sentinel/DETERMINEX_SIG_DELIVERY_CLAUDE_AUTHORITY_BOUNDARY_REVIEW_001.json) | 1 | 1 | `961ddbdaa4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_sig_delivery_cl…` |
| [DETERMINEX_SIG_DELIVERY_CLAUDE_CANONICAL_INBOX_PATH_REVIEW_001](../locks/sentinel/DETERMINEX_SIG_DELIVERY_CLAUDE_CANONICAL_INBOX_PATH_REVIEW_001.json) | 1 | 1 | `961ddbdaa4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_sig_delivery_cl…` |
| [DETERMINEX_SIG_DELIVERY_CLAUDE_CURRENT_SOURCE_TRUTH_REVIEW_001](../locks/sentinel/DETERMINEX_SIG_DELIVERY_CLAUDE_CURRENT_SOURCE_TRUTH_REVIEW_001.json) | 1 | 1 | `961ddbdaa4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_sig_delivery_cl…` |
| [DETERMINEX_SIG_DELIVERY_CLAUDE_DELIVERY_CHANNEL_REVIEW_001](../locks/sentinel/DETERMINEX_SIG_DELIVERY_CLAUDE_DELIVERY_CHANNEL_REVIEW_001.json) | 1 | 1 | `961ddbdaa4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_sig_delivery_cl…` |
| [DETERMINEX_SIG_DELIVERY_CLAUDE_DRY_RUN_IMPORT_REVIEW_001](../locks/sentinel/DETERMINEX_SIG_DELIVERY_CLAUDE_DRY_RUN_IMPORT_REVIEW_001.json) | 1 | 1 | `961ddbdaa4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_sig_delivery_cl…` |
| [DETERMINEX_SIG_DELIVERY_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001](../locks/sentinel/DETERMINEX_SIG_DELIVERY_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001.json) | 1 | 1 | `961ddbdaa4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_sig_delivery_cl…` |
| [DETERMINEX_SIG_DELIVERY_CLAUDE_INVALID_REJECTION_CORPUS_REVIEW_001](../locks/sentinel/DETERMINEX_SIG_DELIVERY_CLAUDE_INVALID_REJECTION_CORPUS_REVIEW_001.json) | 1 | 1 | `961ddbdaa4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_sig_delivery_cl…` |
| [DETERMINEX_SIG_DELIVERY_CLAUDE_MARKER_VALIDITY_REVIEW_001](../locks/sentinel/DETERMINEX_SIG_DELIVERY_CLAUDE_MARKER_VALIDITY_REVIEW_001.json) | 1 | 1 | `961ddbdaa4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_sig_delivery_cl…` |
| [DETERMINEX_SIG_DELIVERY_CLAUDE_OPERATOR_INSTRUCTIONS_REVIEW_001](../locks/sentinel/DETERMINEX_SIG_DELIVERY_CLAUDE_OPERATOR_INSTRUCTIONS_REVIEW_001.json) | 1 | 1 | `961ddbdaa4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_sig_delivery_cl…` |
| [DETERMINEX_SIG_DELIVERY_CLAUDE_OPTIONAL_QUEUE_IMPORT_REVIEW_001](../locks/sentinel/DETERMINEX_SIG_DELIVERY_CLAUDE_OPTIONAL_QUEUE_IMPORT_REVIEW_001.json) | 1 | 1 | `961ddbdaa4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_sig_delivery_cl…` |
| [DETERMINEX_SIG_DELIVERY_CLAUDE_QUEUE_MUTATION_REVIEW_001](../locks/sentinel/DETERMINEX_SIG_DELIVERY_CLAUDE_QUEUE_MUTATION_REVIEW_001.json) | 1 | 1 | `961ddbdaa4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_sig_delivery_cl…` |
| [DETERMINEX_SIG_DELIVERY_CLAUDE_REACT_VITE_ELIGIBILITY_REVIEW_001](../locks/sentinel/DETERMINEX_SIG_DELIVERY_CLAUDE_REACT_VITE_ELIGIBILITY_REVIEW_001.json) | 1 | 1 | `961ddbdaa4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_sig_delivery_cl…` |
| [DETERMINEX_SIG_DELIVERY_CLAUDE_SCORE_MOVEMENT_EVIDENCE_REVIEW_001](../locks/sentinel/DETERMINEX_SIG_DELIVERY_CLAUDE_SCORE_MOVEMENT_EVIDENCE_REVIEW_001.json) | 1 | 1 | `961ddbdaa4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_sig_delivery_cl…` |
| [DETERMINEX_SIG_DELIVERY_CLAUDE_SIGNATURE_SCHEMA_REVIEW_001](../locks/sentinel/DETERMINEX_SIG_DELIVERY_CLAUDE_SIGNATURE_SCHEMA_REVIEW_001.json) | 1 | 1 | `961ddbdaa4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_sig_delivery_cl…` |
| [DETERMINEX_SIG_DELIVERY_CLAUDE_SIGNED_SPEND_COUNT_REVIEW_001](../locks/sentinel/DETERMINEX_SIG_DELIVERY_CLAUDE_SIGNED_SPEND_COUNT_REVIEW_001.json) | 1 | 1 | `961ddbdaa4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_sig_delivery_cl…` |
| [DETERMINEX_SIG_DELIVERY_CLAUDE_SYNTHESIS_REVIEW_001](../locks/sentinel/DETERMINEX_SIG_DELIVERY_CLAUDE_SYNTHESIS_REVIEW_001.json) | 1 | 1 | `961ddbdaa4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_sig_delivery_cl…` |
| [DETERMINEX_SIG_DELIVERY_CLAUDE_TEMPLATE_REJECTION_REVIEW_001](../locks/sentinel/DETERMINEX_SIG_DELIVERY_CLAUDE_TEMPLATE_REJECTION_REVIEW_001.json) | 1 | 1 | `961ddbdaa4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_sig_delivery_cl…` |
| [DETERMINEX_SIG_DELIVERY_CLAUDE_TIMER_PROTOCOL_REVIEW_001](../locks/sentinel/DETERMINEX_SIG_DELIVERY_CLAUDE_TIMER_PROTOCOL_REVIEW_001.json) | 1 | 1 | `961ddbdaa4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_sig_delivery_cl…` |
| [DETERMINEX_SIG_DELIVERY_CLAUDE_VALIDATOR_BEHAVIOR_REVIEW_001](../locks/sentinel/DETERMINEX_SIG_DELIVERY_CLAUDE_VALIDATOR_BEHAVIOR_REVIEW_001.json) | 1 | 1 | `961ddbdaa4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_sig_delivery_cl…` |
| [DETERMINEX_SIG_SPEND_CLAUDE_CHANGED_FILES_REVIEW_001](../locks/sentinel/DETERMINEX_SIG_SPEND_CLAUDE_CHANGED_FILES_REVIEW_001.json) | 1 | 1 | `f8d33cfd91` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_sig_spend_claud…` |
| [DETERMINEX_SIG_SPEND_CLAUDE_COMMAND_MATCH_REVIEW_001](../locks/sentinel/DETERMINEX_SIG_SPEND_CLAUDE_COMMAND_MATCH_REVIEW_001.json) | 1 | 1 | `f8d33cfd91` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_sig_spend_claud…` |
| [DETERMINEX_SIG_SPEND_CLAUDE_CURRENT_SOURCE_TRUTH_REVIEW_001](../locks/sentinel/DETERMINEX_SIG_SPEND_CLAUDE_CURRENT_SOURCE_TRUTH_REVIEW_001.json) | 1 | 1 | `f8d33cfd91` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_sig_spend_claud…` |
| [DETERMINEX_SIG_SPEND_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001](../locks/sentinel/DETERMINEX_SIG_SPEND_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001.json) | 1 | 1 | `f8d33cfd91` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_sig_spend_claud…` |
| [DETERMINEX_SIG_SPEND_CLAUDE_HARD_FLOOR_BOUNDARY_REVIEW_001](../locks/sentinel/DETERMINEX_SIG_SPEND_CLAUDE_HARD_FLOOR_BOUNDARY_REVIEW_001.json) | 1 | 1 | `f8d33cfd91` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_sig_spend_claud…` |
| [DETERMINEX_SIG_SPEND_CLAUDE_MARKER_VALIDITY_REVIEW_001](../locks/sentinel/DETERMINEX_SIG_SPEND_CLAUDE_MARKER_VALIDITY_REVIEW_001.json) | 1 | 1 | `f8d33cfd91` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_sig_spend_claud…` |
| [DETERMINEX_SIG_SPEND_CLAUDE_NEXT_PACKET_REVIEW_001](../locks/sentinel/DETERMINEX_SIG_SPEND_CLAUDE_NEXT_PACKET_REVIEW_001.json) | 1 | 1 | `f8d33cfd91` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_sig_spend_claud…` |
| [DETERMINEX_SIG_SPEND_CLAUDE_REACT_VITE_VERIFICATION_REVIEW_001](../locks/sentinel/DETERMINEX_SIG_SPEND_CLAUDE_REACT_VITE_VERIFICATION_REVIEW_001.json) | 1 | 1 | `f8d33cfd91` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_sig_spend_claud…` |
| [DETERMINEX_SIG_SPEND_CLAUDE_ROLLBACK_RECORD_REVIEW_001](../locks/sentinel/DETERMINEX_SIG_SPEND_CLAUDE_ROLLBACK_RECORD_REVIEW_001.json) | 1 | 1 | `f8d33cfd91` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_sig_spend_claud…` |
| [DETERMINEX_SIG_SPEND_CLAUDE_SCORE_MOVEMENT_EVIDENCE_REVIEW_001](../locks/sentinel/DETERMINEX_SIG_SPEND_CLAUDE_SCORE_MOVEMENT_EVIDENCE_REVIEW_001.json) | 1 | 1 | `f8d33cfd91` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_sig_spend_claud…` |
| [DETERMINEX_SIG_SPEND_CLAUDE_SIGNATURE_IMPORT_VALIDITY_REVIEW_001](../locks/sentinel/DETERMINEX_SIG_SPEND_CLAUDE_SIGNATURE_IMPORT_VALIDITY_REVIEW_001.json) | 1 | 1 | `f8d33cfd91` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_sig_spend_claud…` |
| [DETERMINEX_SIG_SPEND_CLAUDE_SIGNED_QUEUE_MUTATION_REVIEW_001](../locks/sentinel/DETERMINEX_SIG_SPEND_CLAUDE_SIGNED_QUEUE_MUTATION_REVIEW_001.json) | 1 | 1 | `f8d33cfd91` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_sig_spend_claud…` |
| [DETERMINEX_SIG_SPEND_CLAUDE_SIGNED_SPEND_AUDIT_REVIEW_001](../locks/sentinel/DETERMINEX_SIG_SPEND_CLAUDE_SIGNED_SPEND_AUDIT_REVIEW_001.json) | 1 | 1 | `f8d33cfd91` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_sig_spend_claud…` |
| [DETERMINEX_SIG_SPEND_CLAUDE_SPEND_ELIGIBILITY_GATE_REVIEW_001](../locks/sentinel/DETERMINEX_SIG_SPEND_CLAUDE_SPEND_ELIGIBILITY_GATE_REVIEW_001.json) | 1 | 1 | `f8d33cfd91` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_sig_spend_claud…` |
| [DETERMINEX_SIG_SPEND_CLAUDE_SPEND_OCCURRED_REVIEW_001](../locks/sentinel/DETERMINEX_SIG_SPEND_CLAUDE_SPEND_OCCURRED_REVIEW_001.json) | 1 | 1 | `f8d33cfd91` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_sig_spend_claud…` |
| [DETERMINEX_SIG_SPEND_CLAUDE_SYNTHESIS_REVIEW_001](../locks/sentinel/DETERMINEX_SIG_SPEND_CLAUDE_SYNTHESIS_REVIEW_001.json) | 1 | 1 | `f8d33cfd91` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_sig_spend_claud…` |
| [DETERMINEX_SIG_SPEND_CLAUDE_TIER1_STATUS_REVIEW_001](../locks/sentinel/DETERMINEX_SIG_SPEND_CLAUDE_TIER1_STATUS_REVIEW_001.json) | 1 | 1 | `f8d33cfd91` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_sig_spend_claud…` |
| [DETERMINEX_SIG_SPEND_CLAUDE_TIMER_PROTOCOL_REVIEW_001](../locks/sentinel/DETERMINEX_SIG_SPEND_CLAUDE_TIMER_PROTOCOL_REVIEW_001.json) | 1 | 1 | `f8d33cfd91` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_sig_spend_claud…` |
| [DETERMINEX_SPLASH_TARGET_REQUIREMENTS_PACKET_LOCK_001](../locks/sentinel/DETERMINEX_SPLASH_TARGET_REQUIREMENTS_PACKET_LOCK_001.json) | 15 | 15 | `e113efbd6e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_determinex_splash_…` |
| [DETERMINEX_STATUS_PROOF_CENTER_EVIDENCE_VIEW_WORKFLOW_EXECUTION_LOCK_001](../locks/sentinel/DETERMINEX_STATUS_PROOF_CENTER_EVIDENCE_VIEW_WORKFLOW_EXECUTION_LOCK_001.json) | 42 | 42 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_status_proof_ce…` |
| [DETERMINEX_STATUS_PROOF_CENTER_REPORT_WORKFLOW_CELL_CERTIFICATION_LOCK_001](../locks/sentinel/DETERMINEX_STATUS_PROOF_CENTER_REPORT_WORKFLOW_CELL_CERTIFICATION_LOCK_001.json) | 35 | 35 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_status_proof_ce…` |
| [DETERMINEX_STATUS_PROOF_CENTER_REPORT_WORKFLOW_CELL_OPERATOR_APPROVAL_LOCK_001](../locks/sentinel/DETERMINEX_STATUS_PROOF_CENTER_REPORT_WORKFLOW_CELL_OPERATOR_APPROVAL_LOCK_001.json) | 28 | 28 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_status_proof_ce…` |
| [DETERMINEX_STATUS_RUNTIME_CLOSURE_BATCH_003_LOCK](../locks/sentinel/DETERMINEX_STATUS_RUNTIME_CLOSURE_BATCH_003_LOCK.json) | 6 | 6 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_status_runtime_…` |
| [DETERMINEX_STATUS_SCRIPTS_EVIDENCE_VALIDATION_CELL_CERTIFICATION_LOCK_001](../locks/sentinel/DETERMINEX_STATUS_SCRIPTS_EVIDENCE_VALIDATION_CELL_CERTIFICATION_LOCK_001.json) | 27 | 27 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_status_scripts_…` |
| [DETERMINEX_STATUS_SCRIPTS_EVIDENCE_VALIDATION_CELL_OPERATOR_APPROVAL_LOCK_001](../locks/sentinel/DETERMINEX_STATUS_SCRIPTS_EVIDENCE_VALIDATION_CELL_OPERATOR_APPROVAL_LOCK_001.json) | 21 | 21 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_status_scripts_…` |
| [DETERMINEX_STATUS_SUITE_RUNTIME_SEGMENTATION_AND_MONOLITHIC_CLOSURE_LOCK_001](../locks/sentinel/DETERMINEX_STATUS_SUITE_RUNTIME_SEGMENTATION_AND_MONOLITHIC_CLOSURE_LOCK_001.json) | 5 | 5 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_status_suite_ru…` |
| [DETERMINEX_STFS_CLAUDE_APPEND_ONLY_COUNT_DRIFT_GUARDS_REVIEW_001](../locks/sentinel/DETERMINEX_STFS_CLAUDE_APPEND_ONLY_COUNT_DRIFT_GUARDS_REVIEW_001.json) | 1 | 1 | `56e0310d2e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_stfs_claude_app…` |
| [DETERMINEX_STFS_CLAUDE_BETA_DASHBOARD_NOT_PUBLISHED_REVIEW_001](../locks/sentinel/DETERMINEX_STFS_CLAUDE_BETA_DASHBOARD_NOT_PUBLISHED_REVIEW_001.json) | 1 | 1 | `56e0310d2e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_stfs_claude_bet…` |
| [DETERMINEX_STFS_CLAUDE_CAPABILITY_PROMOTION_EVIDENCE_BOUND_REVIEW_001](../locks/sentinel/DETERMINEX_STFS_CLAUDE_CAPABILITY_PROMOTION_EVIDENCE_BOUND_REVIEW_001.json) | 1 | 1 | `56e0310d2e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_stfs_claude_cap…` |
| [DETERMINEX_STFS_CLAUDE_CLAIM_SCANNER_DAY1_OVERCLAIM_REVIEW_001](../locks/sentinel/DETERMINEX_STFS_CLAUDE_CLAIM_SCANNER_DAY1_OVERCLAIM_REVIEW_001.json) | 1 | 1 | `56e0310d2e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_stfs_claude_cla…` |
| [DETERMINEX_STFS_CLAUDE_CLEAN_HOST_NOT_EXECUTED_REVIEW_001](../locks/sentinel/DETERMINEX_STFS_CLAUDE_CLEAN_HOST_NOT_EXECUTED_REVIEW_001.json) | 1 | 1 | `56e0310d2e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_stfs_claude_cle…` |
| [DETERMINEX_STFS_CLAUDE_DIRTY_UNTRACKED_STATE_REVIEW_001](../locks/sentinel/DETERMINEX_STFS_CLAUDE_DIRTY_UNTRACKED_STATE_REVIEW_001.json) | 1 | 1 | `56e0310d2e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_stfs_claude_dir…` |
| [DETERMINEX_STFS_CLAUDE_EVERY_NONLV_NEXT_ACTION_REVIEW_001](../locks/sentinel/DETERMINEX_STFS_CLAUDE_EVERY_NONLV_NEXT_ACTION_REVIEW_001.json) | 1 | 1 | `56e0310d2e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_stfs_claude_eve…` |
| [DETERMINEX_STFS_CLAUDE_EVIDENCE_INDEX_CLEAN_REVIEW_001](../locks/sentinel/DETERMINEX_STFS_CLAUDE_EVIDENCE_INDEX_CLEAN_REVIEW_001.json) | 1 | 1 | `56e0310d2e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_stfs_claude_evi…` |
| [DETERMINEX_STFS_CLAUDE_EXACT_LOCAL_NOT_FAMILY_SUPPORT_REVIEW_001](../locks/sentinel/DETERMINEX_STFS_CLAUDE_EXACT_LOCAL_NOT_FAMILY_SUPPORT_REVIEW_001.json) | 1 | 1 | `56e0310d2e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_stfs_claude_exa…` |
| [DETERMINEX_STFS_CLAUDE_FAMILY_EXEC_TRANSCRIPTS_REVIEW_001](../locks/sentinel/DETERMINEX_STFS_CLAUDE_FAMILY_EXEC_TRANSCRIPTS_REVIEW_001.json) | 1 | 1 | `56e0310d2e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_stfs_claude_fam…` |
| [DETERMINEX_STFS_CLAUDE_FAMILY_MAP_COVERAGE_REVIEW_001](../locks/sentinel/DETERMINEX_STFS_CLAUDE_FAMILY_MAP_COVERAGE_REVIEW_001.json) | 1 | 1 | `56e0310d2e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_stfs_claude_fam…` |
| [DETERMINEX_STFS_CLAUDE_FAMILY_REPAIR_SCOPE_REVIEW_001](../locks/sentinel/DETERMINEX_STFS_CLAUDE_FAMILY_REPAIR_SCOPE_REVIEW_001.json) | 1 | 1 | `56e0310d2e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_stfs_claude_fam…` |
| [DETERMINEX_STFS_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001](../locks/sentinel/DETERMINEX_STFS_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001.json) | 1 | 1 | `56e0310d2e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_stfs_claude_for…` |
| [DETERMINEX_STFS_CLAUDE_FULL_STATUS_TIMEOUT_REVIEW_001](../locks/sentinel/DETERMINEX_STFS_CLAUDE_FULL_STATUS_TIMEOUT_REVIEW_001.json) | 1 | 1 | `56e0310d2e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_stfs_claude_ful…` |
| [DETERMINEX_STFS_CLAUDE_GUI_BUILD_NOT_EXECUTED_REVIEW_001](../locks/sentinel/DETERMINEX_STFS_CLAUDE_GUI_BUILD_NOT_EXECUTED_REVIEW_001.json) | 1 | 1 | `56e0310d2e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_stfs_claude_gui…` |
| [DETERMINEX_STFS_CLAUDE_INSTALLER_RELEASE_NOT_EXECUTED_REVIEW_001](../locks/sentinel/DETERMINEX_STFS_CLAUDE_INSTALLER_RELEASE_NOT_EXECUTED_REVIEW_001.json) | 1 | 1 | `56e0310d2e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_stfs_claude_ins…` |
| [DETERMINEX_STFS_CLAUDE_MARCH_PLAN_DASHBOARD_REVIEW_001](../locks/sentinel/DETERMINEX_STFS_CLAUDE_MARCH_PLAN_DASHBOARD_REVIEW_001.json) | 1 | 1 | `56e0310d2e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_stfs_claude_mar…` |
| [DETERMINEX_STFS_CLAUDE_NO_FAKE_SBOM_OUTPUT_REVIEW_001](../locks/sentinel/DETERMINEX_STFS_CLAUDE_NO_FAKE_SBOM_OUTPUT_REVIEW_001.json) | 1 | 1 | `56e0310d2e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_stfs_claude_no_…` |
| [DETERMINEX_STFS_CLAUDE_NO_LOCKFILE_MUTATION_REVIEW_001](../locks/sentinel/DETERMINEX_STFS_CLAUDE_NO_LOCKFILE_MUTATION_REVIEW_001.json) | 1 | 1 | `56e0310d2e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_stfs_claude_no_…` |
| [DETERMINEX_STFS_CLAUDE_NO_TEST_MUTATION_REVIEW_001](../locks/sentinel/DETERMINEX_STFS_CLAUDE_NO_TEST_MUTATION_REVIEW_001.json) | 1 | 1 | `56e0310d2e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_stfs_claude_no_…` |
| [DETERMINEX_STFS_CLAUDE_NO_UNAUTHORIZED_INSTALL_REVIEW_001](../locks/sentinel/DETERMINEX_STFS_CLAUDE_NO_UNAUTHORIZED_INSTALL_REVIEW_001.json) | 1 | 1 | `56e0310d2e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_stfs_claude_no_…` |
| [DETERMINEX_STFS_CLAUDE_NO_UNIVERSAL_SUPPORT_CLAIM_REVIEW_001](../locks/sentinel/DETERMINEX_STFS_CLAUDE_NO_UNIVERSAL_SUPPORT_CLAIM_REVIEW_001.json) | 1 | 1 | `56e0310d2e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_stfs_claude_no_…` |
| [DETERMINEX_STFS_CLAUDE_NO_VERIFIER_ORACLE_MUTATION_REVIEW_001](../locks/sentinel/DETERMINEX_STFS_CLAUDE_NO_VERIFIER_ORACLE_MUTATION_REVIEW_001.json) | 1 | 1 | `56e0310d2e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_stfs_claude_no_…` |
| [DETERMINEX_STFS_CLAUDE_PRIOR_SBOM_BLOCKER_REVALIDATED_REVIEW_001](../locks/sentinel/DETERMINEX_STFS_CLAUDE_PRIOR_SBOM_BLOCKER_REVALIDATED_REVIEW_001.json) | 1 | 1 | `56e0310d2e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_stfs_claude_pri…` |
| [DETERMINEX_STFS_CLAUDE_RELEASE_CELLS_CANONICAL_REVIEW_001](../locks/sentinel/DETERMINEX_STFS_CLAUDE_RELEASE_CELLS_CANONICAL_REVIEW_001.json) | 1 | 1 | `56e0310d2e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_stfs_claude_rel…` |
| [DETERMINEX_STFS_CLAUDE_RELEASE_FAMILIES_CANONICAL_REVIEW_001](../locks/sentinel/DETERMINEX_STFS_CLAUDE_RELEASE_FAMILIES_CANONICAL_REVIEW_001.json) | 1 | 1 | `56e0310d2e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_stfs_claude_rel…` |
| [DETERMINEX_STFS_CLAUDE_RUNTIME_QUEUE_SPEND_ACCURATE_REVIEW_001](../locks/sentinel/DETERMINEX_STFS_CLAUDE_RUNTIME_QUEUE_SPEND_ACCURATE_REVIEW_001.json) | 1 | 1 | `56e0310d2e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_stfs_claude_run…` |
| [DETERMINEX_STFS_CLAUDE_SAFE_FAMILY_EXEC_REVIEW_001](../locks/sentinel/DETERMINEX_STFS_CLAUDE_SAFE_FAMILY_EXEC_REVIEW_001.json) | 1 | 1 | `56e0310d2e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_stfs_claude_saf…` |
| [DETERMINEX_STFS_CLAUDE_SBOM_EXECUTION_RETRY_SCOPE_REVIEW_001](../locks/sentinel/DETERMINEX_STFS_CLAUDE_SBOM_EXECUTION_RETRY_SCOPE_REVIEW_001.json) | 1 | 1 | `56e0310d2e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_stfs_claude_sbo…` |
| [DETERMINEX_STFS_CLAUDE_SBOM_OUTPUT_BLOCKER_REVIEW_001](../locks/sentinel/DETERMINEX_STFS_CLAUDE_SBOM_OUTPUT_BLOCKER_REVIEW_001.json) | 1 | 1 | `56e0310d2e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_stfs_claude_sbo…` |
| [DETERMINEX_STFS_CLAUDE_SBOM_TOOL_ADMISSION_PACKET_SPEND_REVIEW_001](../locks/sentinel/DETERMINEX_STFS_CLAUDE_SBOM_TOOL_ADMISSION_PACKET_SPEND_REVIEW_001.json) | 1 | 1 | `56e0310d2e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_stfs_claude_sbo…` |
| [DETERMINEX_STFS_CLAUDE_SCORE_MOVEMENT_EVIDENCE_BOUND_REVIEW_001](../locks/sentinel/DETERMINEX_STFS_CLAUDE_SCORE_MOVEMENT_EVIDENCE_BOUND_REVIEW_001.json) | 1 | 1 | `56e0310d2e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_stfs_claude_sco…` |
| [DETERMINEX_STFS_CLAUDE_SYNTHESIS_REVIEW_001](../locks/sentinel/DETERMINEX_STFS_CLAUDE_SYNTHESIS_REVIEW_001.json) | 1 | 1 | `56e0310d2e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_stfs_claude_syn…` |
| [DETERMINEX_STFS_CLAUDE_VERIFIER_NOT_FAKE_REVIEW_001](../locks/sentinel/DETERMINEX_STFS_CLAUDE_VERIFIER_NOT_FAKE_REVIEW_001.json) | 1 | 1 | `56e0310d2e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_stfs_claude_ver…` |
| [DETERMINEX_SUBPACKAGE_DISTRIBUTION_FEASIBILITY_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_SUBPACKAGE_DISTRIBUTION_FEASIBILITY_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_subpackage_dist…` |
| [DETERMINEX_SUBPACKAGE_DRY_RUN_DISTRIBUTION_PATH_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_SUBPACKAGE_DRY_RUN_DISTRIBUTION_PATH_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_007_subpac…` |
| [DETERMINEX_SUBPACKAGE_FIRST_COMMAND_VIA_INSTALLED_ENTRY_POINT_LOCK_001](../locks/sentinel/DETERMINEX_SUBPACKAGE_FIRST_COMMAND_VIA_INSTALLED_ENTRY_POINT_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_SUBPACKAGE_PIP_BUILD_INSTALL_DEPRECATION_FIX_LOCK_001](../locks/sentinel/DETERMINEX_SUBPACKAGE_PIP_BUILD_INSTALL_DEPRECATION_FIX_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_SUPPORT_CELL_PROMOTION_GATE_LOCK_001](../locks/sentinel/DETERMINEX_SUPPORT_CELL_PROMOTION_GATE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_determinex_univers…` |
| [DETERMINEX_SUPPORT_LADDER_RUNG_ORDER_ENFORCEMENT_LOCK_001](../locks/sentinel/DETERMINEX_SUPPORT_LADDER_RUNG_ORDER_ENFORCEMENT_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_SUPPORT_MATRIX_BOUNDARY_DRIFT_GUARD_LOCK_001](../locks/sentinel/DETERMINEX_SUPPORT_MATRIX_BOUNDARY_DRIFT_GUARD_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_SUPPORT_MATRIX_CONVEYOR_LOCK_001](../locks/sentinel/DETERMINEX_SUPPORT_MATRIX_CONVEYOR_LOCK_001.json) | 13 | 13 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_support_matrix_…` |
| [DETERMINEX_SUPPORT_MATRIX_VIEWER_44_FAMILY_BOUNDARY_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_SUPPORT_MATRIX_VIEWER_44_FAMILY_BOUNDARY_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_support_matrix_…` |
| [DETERMINEX_SUPPORT_MATRIX_VIEWER_BOUNDARY_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_SUPPORT_MATRIX_VIEWER_BOUNDARY_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_007_suppor…` |
| [DETERMINEX_SUPPORT_MATRIX_VIEWER_PANEL_AND_44_FAMILY_BOUNDARY_LOCK_001](../locks/sentinel/DETERMINEX_SUPPORT_MATRIX_VIEWER_PANEL_AND_44_FAMILY_BOUNDARY_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_SUPPORT_MATRIX_VIEWER_VISUAL_COMPONENT_PROOF_LOCK_001](../locks/sentinel/DETERMINEX_SUPPORT_MATRIX_VIEWER_VISUAL_COMPONENT_PROOF_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_SUPPORT_MATRIX_ZERO_FAMILY_BADGE_AND_44_LANGUAGE_GATE_LOCK_001](../locks/sentinel/DETERMINEX_SUPPORT_MATRIX_ZERO_FAMILY_BADGE_AND_44_LANGUAGE_GATE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_SWIFT_TOOLCHAIN_PLATFORM_GATE_LOCK_001](../locks/sentinel/DETERMINEX_SWIFT_TOOLCHAIN_PLATFORM_GATE_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_SYFT_ADMISSION_AND_SBOM_COVERAGE_AFTER_SIGNATURE_LOCK_001](../locks/sentinel/DETERMINEX_SYFT_ADMISSION_AND_SBOM_COVERAGE_AFTER_SIGNATURE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_SYFT_SBOM_EMISSION_IF_SIGNED_LOCK_001](../locks/sentinel/DETERMINEX_SYFT_SBOM_EMISSION_IF_SIGNED_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_SYFT_SBOM_EMISSION_WITH_RUNTIME_APPROVAL_LOCK_001](../locks/sentinel/DETERMINEX_SYFT_SBOM_EMISSION_WITH_RUNTIME_APPROVAL_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_SYFT_SBOM_SIGNED_ADMISSION_AND_STANDARDS_SBOM_GENERATION_LOCK_001](../locks/sentinel/DETERMINEX_SYFT_SBOM_SIGNED_ADMISSION_AND_STANDARDS_SBOM_GENERATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_syft_sbom_signe…` |
| [DETERMINEX_SYFT_SIGNED_ADMISSION_AND_SBOM_EMISSION_LOCK_002](../locks/sentinel/DETERMINEX_SYFT_SIGNED_ADMISSION_AND_SBOM_EMISSION_LOCK_002.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_SYFT_SIGNED_SBOM_EMISSION_LOCK_003](../locks/sentinel/DETERMINEX_SYFT_SIGNED_SBOM_EMISSION_LOCK_003.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_LOCK_002](../locks/sentinel/DETERMINEX_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_LOCK_002.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_tandem_post_cla…` |
| [DETERMINEX_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_LOCK_003](../locks/sentinel/DETERMINEX_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_LOCK_003.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_tandem_post_cla…` |
| [DETERMINEX_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_LOCK_004](../locks/sentinel/DETERMINEX_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_LOCK_004.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_tandem_post_cla…` |
| [DETERMINEX_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_LOCK_005](../locks/sentinel/DETERMINEX_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_LOCK_005.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_tandem_post_cla…` |
| [DETERMINEX_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_LOCK_006](../locks/sentinel/DETERMINEX_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_LOCK_006.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_tandem_post_cla…` |
| [DETERMINEX_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_LOCK_007](../locks/sentinel/DETERMINEX_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_LOCK_007.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_tandem_post_cla…` |
| [DETERMINEX_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_LOCK_008](../locks/sentinel/DETERMINEX_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_LOCK_008.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_tandem_post_cla…` |
| [DETERMINEX_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_LOCK_009](../locks/sentinel/DETERMINEX_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_LOCK_009.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_tandem_post_cla…` |
| [DETERMINEX_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_LOCK_010](../locks/sentinel/DETERMINEX_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_LOCK_010.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_tandem_post_cla…` |
| [DETERMINEX_TANDEM_POST_CLAUDE_PUBLIC_PROOF_REPORT_BINDING_RECONCILIATION_LOCK_011](../locks/sentinel/DETERMINEX_TANDEM_POST_CLAUDE_PUBLIC_PROOF_REPORT_BINDING_RECONCILIATION_LOCK_011.json) | 9 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_tandem_post_cla…` |
| [DETERMINEX_TANDEM_STATUS_CHANNEL_LOCK_001](../locks/sentinel/DETERMINEX_TANDEM_STATUS_CHANNEL_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_TAURI_DESKTOP_BUILD_PROOF_LOCK_001](../locks/sentinel/DETERMINEX_TAURI_DESKTOP_BUILD_PROOF_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_tauri_desktop_b…` |
| [DETERMINEX_TAURI_DESKTOP_BUILD_PROOF_RETRY_WITH_LOCAL_ORT_LINK_LOCK_001](../locks/sentinel/DETERMINEX_TAURI_DESKTOP_BUILD_PROOF_RETRY_WITH_LOCAL_ORT_LINK_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_tauri_desktop_b…` |
| [DETERMINEX_TAURI_DESKTOP_BUILD_PROOF_WAVE_008_LOCK_001](../locks/sentinel/DETERMINEX_TAURI_DESKTOP_BUILD_PROOF_WAVE_008_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_TAURI_DESKTOP_RELEASE_BUILD_ARTIFACT_LOCK_001](../locks/sentinel/DETERMINEX_TAURI_DESKTOP_RELEASE_BUILD_ARTIFACT_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_TAURI_DRIVER_GUI_E2E_HARNESS_IMPLEMENTATION_LOCK_001](../locks/sentinel/DETERMINEX_TAURI_DRIVER_GUI_E2E_HARNESS_IMPLEMENTATION_LOCK_001.json) | 30 | 30 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_tauri_driver_gu…` |
| [DETERMINEX_TAURI_DRIVER_GUI_HARNESS_INSTALL_AND_ADMISSION_LOCK_001](../locks/sentinel/DETERMINEX_TAURI_DRIVER_GUI_HARNESS_INSTALL_AND_ADMISSION_LOCK_001.json) | 37 | 1243 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_tauri_driver_gu…` |
| [DETERMINEX_TAURI_ELECTRON_AUTHORITY_GATE_LOCK_001](../locks/sentinel/DETERMINEX_TAURI_ELECTRON_AUTHORITY_GATE_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_TAURI_NSIS_FALLBACK_PACKAGING_PROOF_LOCK_001](../locks/sentinel/DETERMINEX_TAURI_NSIS_FALLBACK_PACKAGING_PROOF_LOCK_001.json) | 36 | 36 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_tauri_nsis_fall…` |
| [DETERMINEX_TAURI_RELEASE_BUILD_FAILURE_REPAIR_PLAN_LOCK_001](../locks/sentinel/DETERMINEX_TAURI_RELEASE_BUILD_FAILURE_REPAIR_PLAN_LOCK_001.json) | 24 | 24 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_tauri_release_b…` |
| [DETERMINEX_TAURI_RELEASE_BUILD_PROOF_LOCK_001](../locks/sentinel/DETERMINEX_TAURI_RELEASE_BUILD_PROOF_LOCK_001.json) | 30 | 30 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_tauri_release_b…` |
| [DETERMINEX_TAURI_UNIFIED_PRODUCT_COMMAND_SURFACE_LOCK_001](../locks/sentinel/DETERMINEX_TAURI_UNIFIED_PRODUCT_COMMAND_SURFACE_LOCK_001.json) | 12 | 12 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_tauri_unified_prod…` |
| [DETERMINEX_TEST_SMOKE_INSTALL_VERIFIER_CLASS_EXPANSION_LOCK_001](../locks/sentinel/DETERMINEX_TEST_SMOKE_INSTALL_VERIFIER_CLASS_EXPANSION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_TIER1_ADAPTER_EXPANSION_BATCH_002_LOCK_001](../locks/sentinel/DETERMINEX_TIER1_ADAPTER_EXPANSION_BATCH_002_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_TIER1_ADAPTER_EXPANSION_BATCH_002_PER_FAMILY_VERIFIED_PROMOTION_LOCK_001](../locks/sentinel/DETERMINEX_TIER1_ADAPTER_EXPANSION_BATCH_002_PER_FAMILY_VERIFIED_PROMOTION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_TIER1_FIFTH_FAMILY_ADAPTER_VERIFIED_TRANSCRIPT_LOCK_001](../locks/sentinel/DETERMINEX_TIER1_FIFTH_FAMILY_ADAPTER_VERIFIED_TRANSCRIPT_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_TIER1_FIRST_FAMILY_BUILD_TEST_SMOKE_TRANSCRIPT_LOCK_001](../locks/sentinel/DETERMINEX_TIER1_FIRST_FAMILY_BUILD_TEST_SMOKE_TRANSCRIPT_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_018_canoni…` |
| [DETERMINEX_TIER1_FOUR_VERIFIED_FAMILIES_ADAPTER_PORT_LOCK_001](../locks/sentinel/DETERMINEX_TIER1_FOUR_VERIFIED_FAMILIES_ADAPTER_PORT_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_TIER1_PROGRAM_FAMILY_COVERAGE_COMPLETION_LOCK_001](../locks/sentinel/DETERMINEX_TIER1_PROGRAM_FAMILY_COVERAGE_COMPLETION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_under…` |
| [DETERMINEX_TIER1_SAFE_FIXTURE_EXECUTION_EXPANSION_LOCK_001](../locks/sentinel/DETERMINEX_TIER1_SAFE_FIXTURE_EXECUTION_EXPANSION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_017_canoni…` |
| [DETERMINEX_TIER1_SECOND_THIRD_FAMILY_TRANSCRIPTS_LOCK_001](../locks/sentinel/DETERMINEX_TIER1_SECOND_THIRD_FAMILY_TRANSCRIPTS_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_019_execut…` |
| [DETERMINEX_TOOLCHAIN_AUTHORITY_FAMILY_PACKET_PREP_LOCK_001](../locks/sentinel/DETERMINEX_TOOLCHAIN_AUTHORITY_FAMILY_PACKET_PREP_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_TOOLCHAIN_BATCH_EXECUTION_LOCK_001](../locks/sentinel/DETERMINEX_TOOLCHAIN_BATCH_EXECUTION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_TOOLCHAIN_CLASSIFIER_STATE_EXPANSION_LOCK_001](../locks/sentinel/DETERMINEX_TOOLCHAIN_CLASSIFIER_STATE_EXPANSION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_014_signed…` |
| [DETERMINEX_TOOLCHAIN_DETECTOR_AND_BUILD_COMMAND_SATURATION_LOCK_001](../locks/sentinel/DETERMINEX_TOOLCHAIN_DETECTOR_AND_BUILD_COMMAND_SATURATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_TOOL_ACQUISITION_EXECUTION_LOCK_001](../locks/sentinel/DETERMINEX_TOOL_ACQUISITION_EXECUTION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_TOOL_ACQUISITION_QUEUE_ADMISSION_SPEND_LOCK_001](../locks/sentinel/DETERMINEX_TOOL_ACQUISITION_QUEUE_ADMISSION_SPEND_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_TRAINING_ROWS_FORBIDDEN_BOUNDARY_GUARD_LOCK_001](../locks/sentinel/DETERMINEX_TRAINING_ROWS_FORBIDDEN_BOUNDARY_GUARD_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_TRUE_100_DEFICIENCY_DECOMPOSITION_AUDIT_001](../locks/sentinel/DETERMINEX_TRUE_100_DEFICIENCY_DECOMPOSITION_AUDIT_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_true_100_defici…` |
| [DETERMINEX_TRUE_100_PERCENT_INTRINSIC_IDE_GAP_AUDIT_001](../locks/sentinel/DETERMINEX_TRUE_100_PERCENT_INTRINSIC_IDE_GAP_AUDIT_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_true_100_percen…` |
| [DETERMINEX_TRUE_USER_PRODUCT_CAPABILITY_BASELINE_LOCK_001](../locks/sentinel/DETERMINEX_TRUE_USER_PRODUCT_CAPABILITY_BASELINE_LOCK_001.json) | 17 | 17 | `cd3a6d5322` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_determinex_unified…` |
| [DETERMINEX_TYPESCRIPT_NODE_CLI_ADAPTER_LOCK_001](../locks/sentinel/DETERMINEX_TYPESCRIPT_NODE_CLI_ADAPTER_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_typescript_node…` |
| [DETERMINEX_T_DRIVE_BUILD_CACHE_RELOCATION_POLICY_LOCK_001](../locks/sentinel/DETERMINEX_T_DRIVE_BUILD_CACHE_RELOCATION_POLICY_LOCK_001.json) | 21 | 21 | `pending-fi` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_runner_sa…` |
| [DETERMINEX_T_DRIVE_STORAGE_INVENTORY_LOCK_001](../locks/sentinel/DETERMINEX_T_DRIVE_STORAGE_INVENTORY_LOCK_001.json) | 18 | 1 | `e4ff17592c` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_admitted_clean_…` |
| [DETERMINEX_T_DRIVE_STORAGE_RELIEF_EXECUTION_LOCK_001](../locks/sentinel/DETERMINEX_T_DRIVE_STORAGE_RELIEF_EXECUTION_LOCK_001.json) | 18 | 1 | `e4ff17592c` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_admitted_clean_…` |
| [DETERMINEX_T_DRIVE_STORAGE_RELOCATION_PLAN_LOCK_001](../locks/sentinel/DETERMINEX_T_DRIVE_STORAGE_RELOCATION_PLAN_LOCK_001.json) | 18 | 1 | `e4ff17592c` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_admitted_clean_…` |
| [DETERMINEX_UNDER_THE_HOOD_SCORE_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_UNDER_THE_HOOD_SCORE_RECONCILIATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_overnight_under…` |
| [DETERMINEX_UNIFIED_CAPABILITY_GAP_GRAPH_LOCK_001](../locks/sentinel/DETERMINEX_UNIFIED_CAPABILITY_GAP_GRAPH_LOCK_001.json) | 17 | 17 | `cd3a6d5322` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_determinex_unified…` |
| [DETERMINEX_UNIFIED_PRODUCT_NAVIGATION_MODEL_LOCK_001](../locks/sentinel/DETERMINEX_UNIFIED_PRODUCT_NAVIGATION_MODEL_LOCK_001.json) | 21 | 21 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_unified_product_na…` |
| [DETERMINEX_UNIFIED_PRODUCT_SPLASH_DEMO_SPEC_LOCK_001](../locks/sentinel/DETERMINEX_UNIFIED_PRODUCT_SPLASH_DEMO_SPEC_LOCK_001.json) | 21 | 21 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_unified_product…` |
| [DETERMINEX_UNIFIED_PRODUCT_SURFACE_TAXONOMY_LOCK_001](../locks/sentinel/DETERMINEX_UNIFIED_PRODUCT_SURFACE_TAXONOMY_LOCK_001.json) | 17 | 17 | `cd3a6d5322` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_determinex_unified…` |
| [DETERMINEX_UNIFIED_PRODUCT_UX_FINAL_STATE_LOCK_001](../locks/sentinel/DETERMINEX_UNIFIED_PRODUCT_UX_FINAL_STATE_LOCK_001.json) | 13 | 13 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_unified_product…` |
| [DETERMINEX_UNIFIED_SPLASH_SPRINT_DECISION_LOCK_001](../locks/sentinel/DETERMINEX_UNIFIED_SPLASH_SPRINT_DECISION_LOCK_001.json) | 17 | 17 | `cd3a6d5322` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_determinex_unified…` |
| [DETERMINEX_UNIFIED_STATUS_SURFACE_AND_EVIDENCE_GRAPH_LOCK_001](../locks/sentinel/DETERMINEX_UNIFIED_STATUS_SURFACE_AND_EVIDENCE_GRAPH_LOCK_001.json) | 6 | 6 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_determinex_unified…` |
| [DETERMINEX_UNIFIED_USER_LEVELS_AND_TEACHING_WINDOWS_LOCK_001](../locks/sentinel/DETERMINEX_UNIFIED_USER_LEVELS_AND_TEACHING_WINDOWS_LOCK_001.json) | 19 | 19 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_user_levels_and_te…` |
| [DETERMINEX_UNIVERSAL_100_ALL_SECTOR_TAXONOMY_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_ALL_SECTOR_TAXONOMY_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_a…` |
| [DETERMINEX_UNIVERSAL_100_CLAUDE_BINDING_HANDOFF_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_CLAUDE_BINDING_HANDOFF_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_UNIVERSAL_100_CONVEYOR_BACKLOG_AND_DEPTH_QUEUE_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_CONVEYOR_BACKLOG_AND_DEPTH_QUEUE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_c…` |
| [DETERMINEX_UNIVERSAL_100_DEPTH_PROMOTION_BATCH_017_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_DEPTH_PROMOTION_BATCH_017_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_d…` |
| [DETERMINEX_UNIVERSAL_100_DEPTH_PROMOTION_BATCH_018_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_DEPTH_PROMOTION_BATCH_018_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_d…` |
| [DETERMINEX_UNIVERSAL_100_DEPTH_PROMOTION_BATCH_019_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_DEPTH_PROMOTION_BATCH_019_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_d…` |
| [DETERMINEX_UNIVERSAL_100_DEPTH_PROMOTION_CANDIDATE_INVENTORY_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_DEPTH_PROMOTION_CANDIDATE_INVENTORY_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_d…` |
| [DETERMINEX_UNIVERSAL_100_DEPTH_PROMOTION_SCOREBOARD_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_DEPTH_PROMOTION_SCOREBOARD_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_d…` |
| [DETERMINEX_UNIVERSAL_100_DEPTH_PROMOTION_WAVE_001_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_DEPTH_PROMOTION_WAVE_001_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_d…` |
| [DETERMINEX_UNIVERSAL_100_EDGE_CASE_EXPANSION_ROADMAP_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_EDGE_CASE_EXPANSION_ROADMAP_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_e…` |
| [DETERMINEX_UNIVERSAL_100_MATRIX_PROBE_BATCH_001_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_MATRIX_PROBE_BATCH_001_RECONCILIATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_UNIVERSAL_100_MATRIX_PROBE_EXECUTION_BATCH_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_MATRIX_PROBE_EXECUTION_BATCH_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_determinex_univers…` |
| [DETERMINEX_UNIVERSAL_100_MATRIX_PROBE_EXECUTION_BATCH_002](../locks/sentinel/DETERMINEX_UNIVERSAL_100_MATRIX_PROBE_EXECUTION_BATCH_002.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_UNIVERSAL_100_MATRIX_PROBE_EXECUTION_BATCH_003](../locks/sentinel/DETERMINEX_UNIVERSAL_100_MATRIX_PROBE_EXECUTION_BATCH_003.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_m…` |
| [DETERMINEX_UNIVERSAL_100_MATRIX_PROBE_EXECUTION_BATCH_004](../locks/sentinel/DETERMINEX_UNIVERSAL_100_MATRIX_PROBE_EXECUTION_BATCH_004.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_m…` |
| [DETERMINEX_UNIVERSAL_100_SECTOR_CONVEYOR_ENGINE_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_SECTOR_CONVEYOR_ENGINE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_s…` |
| [DETERMINEX_UNIVERSAL_100_SECTOR_GULP_BATCH_005_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_SECTOR_GULP_BATCH_005_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_s…` |
| [DETERMINEX_UNIVERSAL_100_SECTOR_GULP_BATCH_006_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_SECTOR_GULP_BATCH_006_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_s…` |
| [DETERMINEX_UNIVERSAL_100_SECTOR_GULP_BATCH_007_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_SECTOR_GULP_BATCH_007_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_s…` |
| [DETERMINEX_UNIVERSAL_100_SECTOR_GULP_BATCH_008_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_SECTOR_GULP_BATCH_008_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_s…` |
| [DETERMINEX_UNIVERSAL_100_SECTOR_GULP_BATCH_009_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_SECTOR_GULP_BATCH_009_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_s…` |
| [DETERMINEX_UNIVERSAL_100_SECTOR_GULP_BATCH_010_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_SECTOR_GULP_BATCH_010_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_s…` |
| [DETERMINEX_UNIVERSAL_100_SECTOR_GULP_BATCH_011_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_SECTOR_GULP_BATCH_011_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_s…` |
| [DETERMINEX_UNIVERSAL_100_SECTOR_GULP_BATCH_012_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_SECTOR_GULP_BATCH_012_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_s…` |
| [DETERMINEX_UNIVERSAL_100_SECTOR_GULP_BATCH_013_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_SECTOR_GULP_BATCH_013_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_s…` |
| [DETERMINEX_UNIVERSAL_100_SECTOR_STATE_AND_INGESTION_LADDER_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_SECTOR_STATE_AND_INGESTION_LADDER_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_s…` |
| [DETERMINEX_UNIVERSAL_100_SUPPORT_DEPTH_LEDGER_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_SUPPORT_DEPTH_LEDGER_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_s…` |
| [DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_002_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_002_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_003_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_003_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_m…` |
| [DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_004_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_004_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_m…` |
| [DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_005_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_005_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_s…` |
| [DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_006_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_006_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_s…` |
| [DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_007_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_007_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_s…` |
| [DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_008_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_008_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_s…` |
| [DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_009_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_009_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_s…` |
| [DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_010_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_010_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_s…` |
| [DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_011_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_011_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_s…` |
| [DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_012_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_012_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_s…` |
| [DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_013_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_013_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_s…` |
| [DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_014_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_014_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_t…` |
| [DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_015_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_015_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_t…` |
| [DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_016_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_016_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_t…` |
| [DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_017_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_017_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_d…` |
| [DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_018_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_018_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_d…` |
| [DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_019_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_019_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_d…` |
| [DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_determinex_univers…` |
| [DETERMINEX_UNIVERSAL_100_TOP_LEVEL_BLOCKER_INVENTORY_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_TOP_LEVEL_BLOCKER_INVENTORY_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_t…` |
| [DETERMINEX_UNIVERSAL_100_TOP_LEVEL_GAP_CLOSURE_BATCH_014_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_TOP_LEVEL_GAP_CLOSURE_BATCH_014_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_t…` |
| [DETERMINEX_UNIVERSAL_100_TOP_LEVEL_GAP_CLOSURE_BATCH_015_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_TOP_LEVEL_GAP_CLOSURE_BATCH_015_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_t…` |
| [DETERMINEX_UNIVERSAL_100_TOP_LEVEL_GAP_CLOSURE_BATCH_016_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_TOP_LEVEL_GAP_CLOSURE_BATCH_016_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_t…` |
| [DETERMINEX_UNIVERSAL_100_TOP_LEVEL_SECTOR_COMPLETION_CAMPAIGN_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_TOP_LEVEL_SECTOR_COMPLETION_CAMPAIGN_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_t…` |
| [DETERMINEX_UNIVERSAL_100_TOP_LEVEL_SECTOR_COVERAGE_SCOREBOARD_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_TOP_LEVEL_SECTOR_COVERAGE_SCOREBOARD_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_t…` |
| [DETERMINEX_UNIVERSAL_100_TOP_LEVEL_SECTOR_GAP_CLOSURE_WAVE_001_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_100_TOP_LEVEL_SECTOR_GAP_CLOSURE_WAVE_001_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_universal_100_t…` |
| [DETERMINEX_UNIVERSAL_DIGITAL_INFRASTRUCTURE_ACCOUNTING_CONVEYOR_001](../locks/sentinel/DETERMINEX_UNIVERSAL_DIGITAL_INFRASTRUCTURE_ACCOUNTING_CONVEYOR_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_UNIVERSAL_FAMILY_ACCOUNTING_STATUS_MAP_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_FAMILY_ACCOUNTING_STATUS_MAP_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_UNIVERSAL_PROGRAM_AUTHORITY_MATRIX_SCHEMA_LOCK_001](../locks/sentinel/DETERMINEX_UNIVERSAL_PROGRAM_AUTHORITY_MATRIX_SCHEMA_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_UNKNOWN_NOVEL_FAMILY_HANDLER_LOCK_001](../locks/sentinel/DETERMINEX_UNKNOWN_NOVEL_FAMILY_HANDLER_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_UNKNOWN_NOVEL_FIXTURE_EXECUTION_LOCK_001](../locks/sentinel/DETERMINEX_UNKNOWN_NOVEL_FIXTURE_EXECUTION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_UNKNOWN_NOVEL_FIXTURE_PATH_LOCK_001](../locks/sentinel/DETERMINEX_UNKNOWN_NOVEL_FIXTURE_PATH_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_UNKNOWN_NOVEL_RUNTIME_DETECTION_AND_INTAKE_LOCK_001](../locks/sentinel/DETERMINEX_UNKNOWN_NOVEL_RUNTIME_DETECTION_AND_INTAKE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_014_signed…` |
| [DETERMINEX_UNKNOWN_NOVEL_RUNTIME_INTAKE_AND_UNIVERSAL_WORDING_GUARD_LOCK_002](../locks/sentinel/DETERMINEX_UNKNOWN_NOVEL_RUNTIME_INTAKE_AND_UNIVERSAL_WORDING_GUARD_LOCK_002.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_015_canoni…` |
| [DETERMINEX_USER_FACING_PROOF_REPORT_EXPORT_CELL_CERTIFICATION_LOCK_001](../locks/sentinel/DETERMINEX_USER_FACING_PROOF_REPORT_EXPORT_CELL_CERTIFICATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_user_facing_pro…` |
| [DETERMINEX_USER_FACING_RELEASE_CELL_RESERVATION_AND_CERTIFICATION_BATCH_LOCK_001](../locks/sentinel/DETERMINEX_USER_FACING_RELEASE_CELL_RESERVATION_AND_CERTIFICATION_BATCH_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_user_facing_rel…` |
| [DETERMINEX_VERIFICATION_WITH_CAPABILITY_RULE_LOCK_001](../locks/sentinel/DETERMINEX_VERIFICATION_WITH_CAPABILITY_RULE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_VERIFIER_FAKE_TRANSCRIPT_REJECTION_AND_PROMOTION_SIGNOFF_LOCK_001](../locks/sentinel/DETERMINEX_VERIFIER_FAKE_TRANSCRIPT_REJECTION_AND_PROMOTION_SIGNOFF_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_014_signed…` |
| [DETERMINEX_VERIFIER_ORACLE_MUTATION_BOUNDARY_GUARD_LOCK_001](../locks/sentinel/DETERMINEX_VERIFIER_ORACLE_MUTATION_BOUNDARY_GUARD_LOCK_001.json) | 15 | 1 | `4ed2aab17d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_clean_host_runt…` |
| [DETERMINEX_VERIFIER_PORTFOLIO_COMPLETION_MAP_LOCK_001](../locks/sentinel/DETERMINEX_VERIFIER_PORTFOLIO_COMPLETION_MAP_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_VERIFIER_PORTFOLIO_EXPANSION_LOCK_001](../locks/sentinel/DETERMINEX_VERIFIER_PORTFOLIO_EXPANSION_LOCK_001.json) | 13 | 13 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_verifier_portfo…` |
| [DETERMINEX_VERIFIER_REJECTION_CORPUS_AND_SIGNOFF_BINDING_LOCK_001](../locks/sentinel/DETERMINEX_VERIFIER_REJECTION_CORPUS_AND_SIGNOFF_BINDING_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_015_canoni…` |
| [DETERMINEX_VERIFIER_REQUIRED_FAMILY_IMPLEMENTATION_LOCK_001](../locks/sentinel/DETERMINEX_VERIFIER_REQUIRED_FAMILY_IMPLEMENTATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_WAVE008_CLAUDE_SYNTHESIS_AND_WAVE009_PRESSURE_QUEUE_001](../locks/sentinel/DETERMINEX_WAVE008_CLAUDE_SYNTHESIS_AND_WAVE009_PRESSURE_QUEUE_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_008_claude…` |
| [DETERMINEX_WAVE008_CLOAK_CRYPTO_LEAK_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE008_CLOAK_CRYPTO_LEAK_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_008_cloak_…` |
| [DETERMINEX_WAVE008_DAY_ONE_CLAIM_SCANNER_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE008_DAY_ONE_CLAIM_SCANNER_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_008_day_on…` |
| [DETERMINEX_WAVE008_HTML_PROOF_REPORT_INVESTOR_READINESS_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE008_HTML_PROOF_REPORT_INVESTOR_READINESS_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_008_html_p…` |
| [DETERMINEX_WAVE008_OMG_FIVE_FIELD_SCORE_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE008_OMG_FIVE_FIELD_SCORE_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_008_omg_fi…` |
| [DETERMINEX_WAVE008_OPERATOR_SIGNATURE_HARDENING_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE008_OPERATOR_SIGNATURE_HARDENING_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_008_operat…` |
| [DETERMINEX_WAVE008_PACKAGE_DRY_RUN_DISTRIBUTION_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE008_PACKAGE_DRY_RUN_DISTRIBUTION_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_008_packag…` |
| [DETERMINEX_WAVE008_PROGRAMBENCH_WAL_MOAT_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE008_PROGRAMBENCH_WAL_MOAT_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_008_progra…` |
| [DETERMINEX_WAVE008_RAG_EXPORT_CELL5_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE008_RAG_EXPORT_CELL5_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_008_rag_ex…` |
| [DETERMINEX_WAVE008_REAL_SIGNATURE_IMPORT_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE008_REAL_SIGNATURE_IMPORT_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_008_real_s…` |
| [DETERMINEX_WAVE008_SBOM_SIGNING_INSTALLER_TRUST_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE008_SBOM_SIGNING_INSTALLER_TRUST_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_008_sbom_s…` |
| [DETERMINEX_WAVE008_SUPPORT_MATRIX_BOUNDARY_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE008_SUPPORT_MATRIX_BOUNDARY_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_008_suppor…` |
| [DETERMINEX_WAVE008_TAURI_FIRST_PAINT_GUI_VISUAL_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE008_TAURI_FIRST_PAINT_GUI_VISUAL_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_008_tauri_…` |
| [DETERMINEX_WAVE009_CLAUDE_SYNTHESIS_AND_WAVE010_PRESSURE_QUEUE_001](../locks/sentinel/DETERMINEX_WAVE009_CLAUDE_SYNTHESIS_AND_WAVE010_PRESSURE_QUEUE_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_009_claude…` |
| [DETERMINEX_WAVE009_CLOAK_HASH_CHAIN_LEAK_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE009_CLOAK_HASH_CHAIN_LEAK_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_009_cloak_…` |
| [DETERMINEX_WAVE009_DAY_ONE_CLAIM_SCANNER_CI_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE009_DAY_ONE_CLAIM_SCANNER_CI_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_009_day_on…` |
| [DETERMINEX_WAVE009_EXECUTOR_VALIDATOR_WIRING_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE009_EXECUTOR_VALIDATOR_WIRING_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_009_execut…` |
| [DETERMINEX_WAVE009_HTML_REPORT_SHAREABILITY_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE009_HTML_REPORT_SHAREABILITY_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_009_html_r…` |
| [DETERMINEX_WAVE009_OMG_FIVE_FIELD_SCORE_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE009_OMG_FIVE_FIELD_SCORE_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_009_omg_fi…` |
| [DETERMINEX_WAVE009_PACKAGE_PUBLICATION_READINESS_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE009_PACKAGE_PUBLICATION_READINESS_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_009_packag…` |
| [DETERMINEX_WAVE009_PROGRAMBENCH_WAL_DATABINDING_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE009_PROGRAMBENCH_WAL_DATABINDING_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_009_progra…` |
| [DETERMINEX_WAVE009_RAG_SIGNED_EXPORT_CELL5_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE009_RAG_SIGNED_EXPORT_CELL5_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_009_rag_si…` |
| [DETERMINEX_WAVE009_SBOM_SIGNING_INSTALLER_WORDING_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE009_SBOM_SIGNING_INSTALLER_WORDING_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_009_sbom_s…` |
| [DETERMINEX_WAVE009_SIGNED_QUEUE_AUDIT_IMPORT_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE009_SIGNED_QUEUE_AUDIT_IMPORT_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_009_signed…` |
| [DETERMINEX_WAVE009_SUPPORT_MATRIX_DRIFT_PHRASE_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE009_SUPPORT_MATRIX_DRIFT_PHRASE_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_009_suppor…` |
| [DETERMINEX_WAVE009_TAURI_BUILD_FIRST_PAINT_PATH_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE009_TAURI_BUILD_FIRST_PAINT_PATH_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_009_tauri_…` |
| [DETERMINEX_WAVE010_CLAUDE_SYNTHESIS_AND_WAVE011_PRESSURE_QUEUE_001](../locks/sentinel/DETERMINEX_WAVE010_CLAUDE_SYNTHESIS_AND_WAVE011_PRESSURE_QUEUE_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_010_claude…` |
| [DETERMINEX_WAVE010_CLEAN_HOST_FRESH_INSTALL_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE010_CLEAN_HOST_FRESH_INSTALL_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_010_clean_…` |
| [DETERMINEX_WAVE010_FIVE_FIELD_SCORE_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE010_FIVE_FIELD_SCORE_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_010_five_f…` |
| [DETERMINEX_WAVE010_GUI_FIRST_PAINT_MOAT_VISUAL_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE010_GUI_FIRST_PAINT_MOAT_VISUAL_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_010_gui_fi…` |
| [DETERMINEX_WAVE010_LOCAL_INSTALL_MOMENT_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE010_LOCAL_INSTALL_MOMENT_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_010_local_…` |
| [DETERMINEX_WAVE010_NSIS_INSTALLER_RUNTIME_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE010_NSIS_INSTALLER_RUNTIME_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_010_nsis_i…` |
| [DETERMINEX_WAVE010_PROOF_REPORT_REVEAL_ASSET_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE010_PROOF_REPORT_REVEAL_ASSET_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_010_proof_…` |
| [DETERMINEX_WAVE010_PUBLIC_REVEAL_PREFLIGHT_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE010_PUBLIC_REVEAL_PREFLIGHT_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_010_public…` |
| [DETERMINEX_WAVE010_RUNTIME_AUTHORITY_SPEND_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE010_RUNTIME_AUTHORITY_SPEND_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_010_runtim…` |
| [DETERMINEX_WAVE010_SBOM_RUNTIME_TRUST_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE010_SBOM_RUNTIME_TRUST_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_010_sbom_r…` |
| [DETERMINEX_WAVE011_CLAUDE_SYNTHESIS_AND_WAVE012_PRESSURE_QUEUE_001](../locks/sentinel/DETERMINEX_WAVE011_CLAUDE_SYNTHESIS_AND_WAVE012_PRESSURE_QUEUE_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_011_claude…` |
| [DETERMINEX_WAVE011_CLEAN_RUNNER_FRESH_INSTALL_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE011_CLEAN_RUNNER_FRESH_INSTALL_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_011_clean_…` |
| [DETERMINEX_WAVE011_FIRST_ADMISSION_RUNTIME_SPEND_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE011_FIRST_ADMISSION_RUNTIME_SPEND_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_011_first_…` |
| [DETERMINEX_WAVE011_GUI_LAUNCH_FIRST_PAINT_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE011_GUI_LAUNCH_FIRST_PAINT_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_011_gui_la…` |
| [DETERMINEX_WAVE011_HTML_PROOF_REPORT_SHAREABILITY_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE011_HTML_PROOF_REPORT_SHAREABILITY_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_011_html_p…` |
| [DETERMINEX_WAVE011_NSIS_INSTALL_SMOKE_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE011_NSIS_INSTALL_SMOKE_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_011_nsis_i…` |
| [DETERMINEX_WAVE011_OMG_SCORE_DEFINITION_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE011_OMG_SCORE_DEFINITION_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_011_omg_sc…` |
| [DETERMINEX_WAVE011_PUBLIC_REVEAL_TIER_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE011_PUBLIC_REVEAL_TIER_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_011_public…` |
| [DETERMINEX_WAVE011_SYFT_SBOM_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE011_SYFT_SBOM_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_011_syft_s…` |
| [DETERMINEX_WAVE011_TRUE_LOCAL_INSTALL_MOMENT_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE011_TRUE_LOCAL_INSTALL_MOMENT_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_011_true_l…` |
| [DETERMINEX_WAVE012_BUILD_TEST_SMOKE_LADDER_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE012_BUILD_TEST_SMOKE_LADDER_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_012_build_…` |
| [DETERMINEX_WAVE012_CAPABILITY_UNIVERSE_MATRIX_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE012_CAPABILITY_UNIVERSE_MATRIX_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_012_capabi…` |
| [DETERMINEX_WAVE012_CLAUDE_SYNTHESIS_AND_WAVE013_PRESSURE_QUEUE_001](../locks/sentinel/DETERMINEX_WAVE012_CLAUDE_SYNTHESIS_AND_WAVE013_PRESSURE_QUEUE_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_012_claude…` |
| [DETERMINEX_WAVE012_CLEAN_HOST_ROUTE_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE012_CLEAN_HOST_ROUTE_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_012_clean_…` |
| [DETERMINEX_WAVE012_DRY_RUN_INFLATION_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE012_DRY_RUN_INFLATION_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_012_dry_ru…` |
| [DETERMINEX_WAVE012_EXACT_CELL_PROMOTION_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE012_EXACT_CELL_PROMOTION_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_012_exact_…` |
| [DETERMINEX_WAVE012_GUI_AUTOMATION_FIRST_PAINT_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE012_GUI_AUTOMATION_FIRST_PAINT_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_012_gui_au…` |
| [DETERMINEX_WAVE012_PROOF_REPORT_CAPABILITY_COVERAGE_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE012_PROOF_REPORT_CAPABILITY_COVERAGE_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_012_proof_…` |
| [DETERMINEX_WAVE012_REAL_LOCAL_INSTALL_MOMENT_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE012_REAL_LOCAL_INSTALL_MOMENT_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_012_real_l…` |
| [DETERMINEX_WAVE012_SBOM_LICENSE_SECURITY_TRUST_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE012_SBOM_LICENSE_SECURITY_TRUST_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_012_sbom_l…` |
| [DETERMINEX_WAVE012_SCORE_EVIDENCE_DELTA_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE012_SCORE_EVIDENCE_DELTA_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_012_score_…` |
| [DETERMINEX_WAVE012_TOOLCHAIN_DETECTOR_BUILD_COMMAND_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE012_TOOLCHAIN_DETECTOR_BUILD_COMMAND_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_012_toolch…` |
| [DETERMINEX_WAVE012_VERIFIER_PORTFOLIO_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE012_VERIFIER_PORTFOLIO_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_012_verifi…` |
| [DETERMINEX_WAVE013_CLAUDE_SYNTHESIS_AND_WAVE014_PRESSURE_QUEUE_001](../locks/sentinel/DETERMINEX_WAVE013_CLAUDE_SYNTHESIS_AND_WAVE014_PRESSURE_QUEUE_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_013_claude…` |
| [DETERMINEX_WAVE013_CLEAN_HOST_ROUTE_TRANSCRIPT_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE013_CLEAN_HOST_ROUTE_TRANSCRIPT_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_013_clean_…` |
| [DETERMINEX_WAVE013_DETECTOR_RUNTIME_PROBE_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE013_DETECTOR_RUNTIME_PROBE_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_013_detect…` |
| [DETERMINEX_WAVE013_EXACT_CELL_PROMOTION_GATE_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE013_EXACT_CELL_PROMOTION_GATE_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_013_exact_…` |
| [DETERMINEX_WAVE013_FOUR_STATE_TOOLCHAIN_CLASSIFIER_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE013_FOUR_STATE_TOOLCHAIN_CLASSIFIER_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_013_four_s…` |
| [DETERMINEX_WAVE013_GUI_VISUAL_PROOF_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE013_GUI_VISUAL_PROOF_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_013_gui_vi…` |
| [DETERMINEX_WAVE013_INSTALLED_ENTRY_POINT_AND_PIP_PATH_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE013_INSTALLED_ENTRY_POINT_AND_PIP_PATH_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_013_instal…` |
| [DETERMINEX_WAVE013_LADDER_RUNG_ENFORCEMENT_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE013_LADDER_RUNG_ENFORCEMENT_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_013_ladder…` |
| [DETERMINEX_WAVE013_PACKAGE_METADATA_LICENSE_HYGIENE_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE013_PACKAGE_METADATA_LICENSE_HYGIENE_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_013_packag…` |
| [DETERMINEX_WAVE013_PER_FAMILY_COMMAND_MAPPING_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE013_PER_FAMILY_COMMAND_MAPPING_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_013_per_fa…` |
| [DETERMINEX_WAVE013_PROOF_REPORT_CAPABILITY_COVERAGE_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE013_PROOF_REPORT_CAPABILITY_COVERAGE_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_013_proof_…` |
| [DETERMINEX_WAVE013_REAL_SIGNATURE_RUNTIME_SPEND_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE013_REAL_SIGNATURE_RUNTIME_SPEND_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_013_real_s…` |
| [DETERMINEX_WAVE013_SBOM_LICENSE_SECURITY_TRUST_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE013_SBOM_LICENSE_SECURITY_TRUST_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_013_sbom_l…` |
| [DETERMINEX_WAVE013_SCORE_EVIDENCE_DELTA_CI_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE013_SCORE_EVIDENCE_DELTA_CI_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_013_score_…` |
| [DETERMINEX_WAVE013_UNKNOWN_NOVEL_FAMILY_HANDLER_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE013_UNKNOWN_NOVEL_FAMILY_HANDLER_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_013_unknow…` |
| [DETERMINEX_WAVE013_VERIFIER_CLASS_EXPANSION_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE013_VERIFIER_CLASS_EXPANSION_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_013_verifi…` |
| [DETERMINEX_WAVE014_CLASSIFIER_STATE_EXPANSION_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE014_CLASSIFIER_STATE_EXPANSION_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_014_classi…` |
| [DETERMINEX_WAVE014_CLAUDE_SYNTHESIS_AND_WAVE015_PRESSURE_QUEUE_001](../locks/sentinel/DETERMINEX_WAVE014_CLAUDE_SYNTHESIS_AND_WAVE015_PRESSURE_QUEUE_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_014_claude…` |
| [DETERMINEX_WAVE014_CLEAN_HOST_RUNNER_TRANSCRIPT_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE014_CLEAN_HOST_RUNNER_TRANSCRIPT_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_014_clean_…` |
| [DETERMINEX_WAVE014_DETECTOR_FIXTURE_CORPUS_CI_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE014_DETECTOR_FIXTURE_CORPUS_CI_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_014_detect…` |
| [DETERMINEX_WAVE014_FAKE_TRANSCRIPT_REJECTION_VERIFIER_SIGNOFF_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE014_FAKE_TRANSCRIPT_REJECTION_VERIFIER_SIGNOFF_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_014_fake_t…` |
| [DETERMINEX_WAVE014_FIRST_ADMISSION_RUNTIME_SPEND_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE014_FIRST_ADMISSION_RUNTIME_SPEND_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_014_first_…` |
| [DETERMINEX_WAVE014_FIRST_SBOM_TOOL_ADMISSION_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE014_FIRST_SBOM_TOOL_ADMISSION_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_014_first_…` |
| [DETERMINEX_WAVE014_GUI_FIRST_VISUAL_PROOF_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE014_GUI_FIRST_VISUAL_PROOF_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_014_gui_fi…` |
| [DETERMINEX_WAVE014_LADDER_INVERSION_CI_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE014_LADDER_INVERSION_CI_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_014_ladder…` |
| [DETERMINEX_WAVE014_LOCAL_INSTALL_EXACT_CELL_PROMOTION_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE014_LOCAL_INSTALL_EXACT_CELL_PROMOTION_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_014_local_…` |
| [DETERMINEX_WAVE014_PACKAGE_LICENSE_METADATA_BOUNDARY_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE014_PACKAGE_LICENSE_METADATA_BOUNDARY_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_014_packag…` |
| [DETERMINEX_WAVE014_PER_FAMILY_FIXTURE_ROUTE_EXECUTION_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE014_PER_FAMILY_FIXTURE_ROUTE_EXECUTION_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_014_per_fa…` |
| [DETERMINEX_WAVE014_PROOF_REPORT_EVIDENCE_ANCHOR_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE014_PROOF_REPORT_EVIDENCE_ANCHOR_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_014_proof_…` |
| [DETERMINEX_WAVE014_SCORE_DELTA_PUBLIC_CLAIM_LINTER_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE014_SCORE_DELTA_PUBLIC_CLAIM_LINTER_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_014_score_…` |
| [DETERMINEX_WAVE014_UNKNOWN_NOVEL_RUNTIME_INTAKE_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE014_UNKNOWN_NOVEL_RUNTIME_INTAKE_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_014_unknow…` |
| [DETERMINEX_WAVE015_CANONICAL_RELEASE_CELL_RECONCILIATION_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE015_CANONICAL_RELEASE_CELL_RECONCILIATION_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_015_canoni…` |
| [DETERMINEX_WAVE015_CANONICAL_RELEASE_CELL_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_WAVE015_CANONICAL_RELEASE_CELL_RECONCILIATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_015_canoni…` |
| [DETERMINEX_WAVE015_CLASSIFIER_STATE_SAFETY_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE015_CLASSIFIER_STATE_SAFETY_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_015_classi…` |
| [DETERMINEX_WAVE015_CLAUDE_SYNTHESIS_AND_WAVE016_PRESSURE_QUEUE_001](../locks/sentinel/DETERMINEX_WAVE015_CLAUDE_SYNTHESIS_AND_WAVE016_PRESSURE_QUEUE_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_015_claude…` |
| [DETERMINEX_WAVE015_CLEAN_HOST_TRANSCRIPT_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE015_CLEAN_HOST_TRANSCRIPT_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_015_clean_…` |
| [DETERMINEX_WAVE015_DETECTOR_FIXTURE_CI_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE015_DETECTOR_FIXTURE_CI_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_015_detect…` |
| [DETERMINEX_WAVE015_FIRST_ADMISSION_RUNTIME_SPEND_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE015_FIRST_ADMISSION_RUNTIME_SPEND_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_015_first_…` |
| [DETERMINEX_WAVE015_FIRST_SBOM_ARTIFACT_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE015_FIRST_SBOM_ARTIFACT_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_015_first_…` |
| [DETERMINEX_WAVE015_GUI_FIRST_VISUAL_PROOF_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE015_GUI_FIRST_VISUAL_PROOF_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_015_gui_fi…` |
| [DETERMINEX_WAVE015_LADDER_INVERSION_CI_BLOCKING_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE015_LADDER_INVERSION_CI_BLOCKING_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_015_ladder…` |
| [DETERMINEX_WAVE015_LOCAL_PREVIEW_FULL_GATE_PROMOTION_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE015_LOCAL_PREVIEW_FULL_GATE_PROMOTION_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_015_local_…` |
| [DETERMINEX_WAVE015_PACKAGE_METADATA_LICENSE_README_BOUNDARY_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE015_PACKAGE_METADATA_LICENSE_README_BOUNDARY_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_015_packag…` |
| [DETERMINEX_WAVE015_PER_FAMILY_SAFE_FIXTURE_EXECUTION_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE015_PER_FAMILY_SAFE_FIXTURE_EXECUTION_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_015_per_fa…` |
| [DETERMINEX_WAVE015_PROOF_REPORT_CAPABILITY_ANCHORS_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE015_PROOF_REPORT_CAPABILITY_ANCHORS_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_015_proof_…` |
| [DETERMINEX_WAVE015_SCORE_DELTA_PUBLIC_CLAIM_SCANNER_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE015_SCORE_DELTA_PUBLIC_CLAIM_SCANNER_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_015_score_…` |
| [DETERMINEX_WAVE015_UNKNOWN_NOVEL_RUNTIME_INTAKE_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE015_UNKNOWN_NOVEL_RUNTIME_INTAKE_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_015_unknow…` |
| [DETERMINEX_WAVE015_VERIFIER_REJECTION_SIGNOFF_BINDING_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE015_VERIFIER_REJECTION_SIGNOFF_BINDING_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_015_verifi…` |
| [DETERMINEX_WAVE016_CANONICAL_CELL_CONSTANT_CONVEYOR_BINDING_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE016_CANONICAL_CELL_CONSTANT_CONVEYOR_BINDING_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_016_canoni…` |
| [DETERMINEX_WAVE016_CLAUDE_SYNTHESIS_AND_WAVE017_PRESSURE_QUEUE_001](../locks/sentinel/DETERMINEX_WAVE016_CLAUDE_SYNTHESIS_AND_WAVE017_PRESSURE_QUEUE_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_016_claude…` |
| [DETERMINEX_WAVE016_CLEAN_HOST_RUNNER_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE016_CLEAN_HOST_RUNNER_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_016_clean_…` |
| [DETERMINEX_WAVE016_DETECTOR_CLASSIFIER_FIXTURE_CI_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE016_DETECTOR_CLASSIFIER_FIXTURE_CI_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_016_detect…` |
| [DETERMINEX_WAVE016_FIRST_REAL_SIGNATURE_SPEND_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE016_FIRST_REAL_SIGNATURE_SPEND_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_016_first_…` |
| [DETERMINEX_WAVE016_FIRST_SBOM_ARTIFACT_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE016_FIRST_SBOM_ARTIFACT_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_016_first_…` |
| [DETERMINEX_WAVE016_GUI_FIRST_VISUAL_PROOF_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE016_GUI_FIRST_VISUAL_PROOF_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_016_gui_fi…` |
| [DETERMINEX_WAVE016_LOCAL_PREVIEW_PROMOTION_FULL_GATE_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE016_LOCAL_PREVIEW_PROMOTION_FULL_GATE_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_016_local_…` |
| [DETERMINEX_WAVE016_LOCAL_PREVIEW_RELEASE_CLEANHOST_FAMILY_BOUNDARY_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE016_LOCAL_PREVIEW_RELEASE_CLEANHOST_FAMILY_BOUNDARY_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_016_local_…` |
| [DETERMINEX_WAVE016_PROOF_REPORT_CLAIM_SCANNER_BACKFILL_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE016_PROOF_REPORT_CLAIM_SCANNER_BACKFILL_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_016_proof_…` |
| [DETERMINEX_WAVE016_RELEASE_CELL_DRIFT_DETECTOR_CI_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE016_RELEASE_CELL_DRIFT_DETECTOR_CI_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_016_releas…` |
| [DETERMINEX_WAVE016_RUNTIME_APPROVAL_HARDENING_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE016_RUNTIME_APPROVAL_HARDENING_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_016_runtim…` |
| [DETERMINEX_WAVE016_VERIFIER_SIGNOFF_SCHEMA_PROMOTION_BINDING_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE016_VERIFIER_SIGNOFF_SCHEMA_PROMOTION_BINDING_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_016_verifi…` |
| [DETERMINEX_WAVE017_CANONICAL_DRIFT_DETECTOR_LIVE_CI_LOCK_001](../locks/sentinel/DETERMINEX_WAVE017_CANONICAL_DRIFT_DETECTOR_LIVE_CI_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_017_canoni…` |
| [DETERMINEX_WAVE017_CANONICAL_REGISTRY_CONSUMPTION_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE017_CANONICAL_REGISTRY_CONSUMPTION_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_017_canoni…` |
| [DETERMINEX_WAVE017_CANONICAL_REGISTRY_CONSUMPTION_VERIFICATION_LOCK_001](../locks/sentinel/DETERMINEX_WAVE017_CANONICAL_REGISTRY_CONSUMPTION_VERIFICATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_017_canoni…` |
| [DETERMINEX_WAVE017_CLAUDE_SYNTHESIS_AND_WAVE018_PRESSURE_QUEUE_001](../locks/sentinel/DETERMINEX_WAVE017_CLAUDE_SYNTHESIS_AND_WAVE018_PRESSURE_QUEUE_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_017_claude…` |
| [DETERMINEX_WAVE017_CLEAN_HOST_FIRST_TRANSCRIPT_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE017_CLEAN_HOST_FIRST_TRANSCRIPT_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_017_clean_…` |
| [DETERMINEX_WAVE017_CLEAN_HOST_FIRST_TRANSCRIPT_IF_ADMITTED_LOCK_006](../locks/sentinel/DETERMINEX_WAVE017_CLEAN_HOST_FIRST_TRANSCRIPT_IF_ADMITTED_LOCK_006.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_017_canoni…` |
| [DETERMINEX_WAVE017_DRIFT_DETECTOR_LIVE_CI_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE017_DRIFT_DETECTOR_LIVE_CI_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_017_drift_…` |
| [DETERMINEX_WAVE017_FAMILY_SUPPORT_READINESS_MATRIX_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE017_FAMILY_SUPPORT_READINESS_MATRIX_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_017_family…` |
| [DETERMINEX_WAVE017_FIRST_REAL_SIGNATURE_SPEND_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE017_FIRST_REAL_SIGNATURE_SPEND_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_017_first_…` |
| [DETERMINEX_WAVE017_FIRST_REAL_SIGNATURE_SPEND_IF_PRESENT_LOCK_002](../locks/sentinel/DETERMINEX_WAVE017_FIRST_REAL_SIGNATURE_SPEND_IF_PRESENT_LOCK_002.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_017_canoni…` |
| [DETERMINEX_WAVE017_FIRST_SBOM_ARTIFACT_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE017_FIRST_SBOM_ARTIFACT_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_017_first_…` |
| [DETERMINEX_WAVE017_FIRST_SBOM_IF_TOOL_ADMITTED_LOCK_007](../locks/sentinel/DETERMINEX_WAVE017_FIRST_SBOM_IF_TOOL_ADMITTED_LOCK_007.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_017_canoni…` |
| [DETERMINEX_WAVE017_GUI_FIRST_VISUAL_PROOF_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE017_GUI_FIRST_VISUAL_PROOF_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_017_gui_fi…` |
| [DETERMINEX_WAVE017_GUI_FIRST_VISUAL_PROOF_IF_APPROVED_LOCK_004](../locks/sentinel/DETERMINEX_WAVE017_GUI_FIRST_VISUAL_PROOF_IF_APPROVED_LOCK_004.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_017_canoni…` |
| [DETERMINEX_WAVE017_LEGACY_SIGNOFF_BACKFILL_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE017_LEGACY_SIGNOFF_BACKFILL_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_017_legacy…` |
| [DETERMINEX_WAVE017_LOCAL_PREVIEW_PACKAGE_READINESS_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE017_LOCAL_PREVIEW_PACKAGE_READINESS_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_017_local_…` |
| [DETERMINEX_WAVE017_PROOF_REPORT_ANCHOR_BACKFILL_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE017_PROOF_REPORT_ANCHOR_BACKFILL_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_017_proof_…` |
| [DETERMINEX_WAVE017_PROOF_REPORT_CLAIM_SCANNER_FINAL_CHECK_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE017_PROOF_REPORT_CLAIM_SCANNER_FINAL_CHECK_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_017_proof_…` |
| [DETERMINEX_WAVE017_RELEASE_PROMOTION_NEGATIVE_TESTS_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE017_RELEASE_PROMOTION_NEGATIVE_TESTS_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_017_releas…` |
| [DETERMINEX_WAVE017_RUNTIME_APPROVAL_HARDENING_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE017_RUNTIME_APPROVAL_HARDENING_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_017_runtim…` |
| [DETERMINEX_WAVE017_TIER1_FIXTURE_EXECUTION_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE017_TIER1_FIXTURE_EXECUTION_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_017_tier1_…` |
| [DETERMINEX_WAVE018_ALL_READERS_BIND_TO_REGISTRY_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE018_ALL_READERS_BIND_TO_REGISTRY_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_018_all_re…` |
| [DETERMINEX_WAVE018_BROKEN_CANONICAL_PROOF_ANCHOR_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE018_BROKEN_CANONICAL_PROOF_ANCHOR_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_018_broken…` |
| [DETERMINEX_WAVE018_CLAIM_SCANNER_FINAL_CI_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE018_CLAIM_SCANNER_FINAL_CI_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_018_claim_…` |
| [DETERMINEX_WAVE018_CLAUDE_SYNTHESIS_AND_WAVE019_PRESSURE_QUEUE_001](../locks/sentinel/DETERMINEX_WAVE018_CLAUDE_SYNTHESIS_AND_WAVE019_PRESSURE_QUEUE_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_018_claude…` |
| [DETERMINEX_WAVE018_CLEAN_HOST_FIRST_TRANSCRIPT_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE018_CLEAN_HOST_FIRST_TRANSCRIPT_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_018_clean_…` |
| [DETERMINEX_WAVE018_CLEAN_HOST_FIRST_TRANSCRIPT_IF_ADMITTED_LOCK_007](../locks/sentinel/DETERMINEX_WAVE018_CLEAN_HOST_FIRST_TRANSCRIPT_IF_ADMITTED_LOCK_007.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_018_canoni…` |
| [DETERMINEX_WAVE018_DRIFT_DETECTOR_WORKFLOW_STATUS_GUARD_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE018_DRIFT_DETECTOR_WORKFLOW_STATUS_GUARD_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_018_drift_…` |
| [DETERMINEX_WAVE018_FAKE_TRANSCRIPT_REJECTION_COVERAGE_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE018_FAKE_TRANSCRIPT_REJECTION_COVERAGE_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_018_fake_t…` |
| [DETERMINEX_WAVE018_FAMILY_READINESS_MATRIX_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE018_FAMILY_READINESS_MATRIX_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_018_family…` |
| [DETERMINEX_WAVE018_FIRST_REAL_SIGNATURE_SPEND_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE018_FIRST_REAL_SIGNATURE_SPEND_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_018_first_…` |
| [DETERMINEX_WAVE018_FIRST_REAL_SIGNATURE_SPEND_IF_PRESENT_LOCK_003](../locks/sentinel/DETERMINEX_WAVE018_FIRST_REAL_SIGNATURE_SPEND_IF_PRESENT_LOCK_003.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_018_canoni…` |
| [DETERMINEX_WAVE018_FIRST_SBOM_ARTIFACT_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE018_FIRST_SBOM_ARTIFACT_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_018_first_…` |
| [DETERMINEX_WAVE018_FIRST_SBOM_IF_TOOL_ADMITTED_LOCK_008](../locks/sentinel/DETERMINEX_WAVE018_FIRST_SBOM_IF_TOOL_ADMITTED_LOCK_008.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_018_canoni…` |
| [DETERMINEX_WAVE018_GUI_FIRST_VISUAL_PROOF_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE018_GUI_FIRST_VISUAL_PROOF_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_018_gui_fi…` |
| [DETERMINEX_WAVE018_GUI_FIRST_VISUAL_PROOF_IF_APPROVED_LOCK_005](../locks/sentinel/DETERMINEX_WAVE018_GUI_FIRST_VISUAL_PROOF_IF_APPROVED_LOCK_005.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_018_canoni…` |
| [DETERMINEX_WAVE018_LEGACY_SIGNOFF_BACKFILL_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE018_LEGACY_SIGNOFF_BACKFILL_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_018_legacy…` |
| [DETERMINEX_WAVE018_PROMOTION_NEGATIVE_FIXTURE_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE018_PROMOTION_NEGATIVE_FIXTURE_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_018_promot…` |
| [DETERMINEX_WAVE018_PROOF_REPORT_REGISTRY_BINDING_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE018_PROOF_REPORT_REGISTRY_BINDING_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_018_proof_…` |
| [DETERMINEX_WAVE018_RUNTIME_APPROVAL_HARDENING_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE018_RUNTIME_APPROVAL_HARDENING_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_018_runtim…` |
| [DETERMINEX_WAVE018_TIER1_FIRST_FAMILY_TRANSCRIPT_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE018_TIER1_FIRST_FAMILY_TRANSCRIPT_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_018_tier1_…` |
| [DETERMINEX_WAVE019_CAPABILITY_SCORE_DELTA_GUARD_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE019_CAPABILITY_SCORE_DELTA_GUARD_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_019_capabi…` |
| [DETERMINEX_WAVE019_CLAIM_SCANNER_CI_EXPANSION_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE019_CLAIM_SCANNER_CI_EXPANSION_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_019_claim_…` |
| [DETERMINEX_WAVE019_CLAUDE_SYNTHESIS_AND_WAVE020_PRESSURE_QUEUE_001](../locks/sentinel/DETERMINEX_WAVE019_CLAUDE_SYNTHESIS_AND_WAVE020_PRESSURE_QUEUE_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_019_claude…` |
| [DETERMINEX_WAVE019_FAMILY_SUPPORT_GATE_DEFINITION_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE019_FAMILY_SUPPORT_GATE_DEFINITION_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_019_family…` |
| [DETERMINEX_WAVE019_FIRST_CLEAN_HOST_TRANSCRIPT_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE019_FIRST_CLEAN_HOST_TRANSCRIPT_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_019_first_…` |
| [DETERMINEX_WAVE019_FIRST_GUI_VISUAL_PROOF_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE019_FIRST_GUI_VISUAL_PROOF_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_019_first_…` |
| [DETERMINEX_WAVE019_FIRST_REAL_SIGNATURE_IMPORT_SPEND_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE019_FIRST_REAL_SIGNATURE_IMPORT_SPEND_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_019_first_…` |
| [DETERMINEX_WAVE019_FIRST_SBOM_ARTIFACT_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE019_FIRST_SBOM_ARTIFACT_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_019_first_…` |
| [DETERMINEX_WAVE019_LEGACY_FULL_VERIFIER_SIGNOFF_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE019_LEGACY_FULL_VERIFIER_SIGNOFF_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_019_legacy…` |
| [DETERMINEX_WAVE019_LOCAL_PREVIEW_PACKAGE_BOUNDARY_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE019_LOCAL_PREVIEW_PACKAGE_BOUNDARY_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_019_local_…` |
| [DETERMINEX_WAVE019_PROOF_REPORT_RELEASE_BOUNDARY_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE019_PROOF_REPORT_RELEASE_BOUNDARY_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_019_proof_…` |
| [DETERMINEX_WAVE019_REPAIR_LOOP_READINESS_MAP_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE019_REPAIR_LOOP_READINESS_MAP_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_019_repair…` |
| [DETERMINEX_WAVE019_RUNTIME_APPROVAL_HARDENING_TESTS_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE019_RUNTIME_APPROVAL_HARDENING_TESTS_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_019_runtim…` |
| [DETERMINEX_WAVE019_SIGNOFF_GATE_ENFORCEMENT_CI_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE019_SIGNOFF_GATE_ENFORCEMENT_CI_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_019_signof…` |
| [DETERMINEX_WAVE019_TIER1_SECOND_THIRD_FAMILY_TRANSCRIPTS_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE019_TIER1_SECOND_THIRD_FAMILY_TRANSCRIPTS_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_019_tier1_…` |
| [DETERMINEX_WAVE020A_CLAIM_SCANNER_CI_FINAL_STATE_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE020A_CLAIM_SCANNER_CI_FINAL_STATE_CLAUDE_REVIEW_001.json) | 1 | 1 | `c3233ca50f` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020A_claim…` |
| [DETERMINEX_WAVE020A_CLAUDE_W019_FINDING_RECONCILIATION_001](../locks/sentinel/DETERMINEX_WAVE020A_CLAUDE_W019_FINDING_RECONCILIATION_001.json) | 1 | 1 | `c3233ca50f` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020A_claud…` |
| [DETERMINEX_WAVE020A_FINAL_COMMIT_EVIDENCE_SPINE_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE020A_FINAL_COMMIT_EVIDENCE_SPINE_CLAUDE_REVIEW_001.json) | 1 | 1 | `c3233ca50f` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020A_final…` |
| [DETERMINEX_WAVE020A_PROOF_REPORT_BOUNDARY_FINAL_STATE_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE020A_PROOF_REPORT_BOUNDARY_FINAL_STATE_CLAUDE_REVIEW_001.json) | 1 | 1 | `c3233ca50f` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020A_proof…` |
| [DETERMINEX_WAVE020A_RUNTIME_HARDENING_FINAL_STATE_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE020A_RUNTIME_HARDENING_FINAL_STATE_CLAUDE_REVIEW_001.json) | 1 | 1 | `c3233ca50f` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020A_runti…` |
| [DETERMINEX_WAVE020A_SCORE_DELTA_FINAL_STATE_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE020A_SCORE_DELTA_FINAL_STATE_CLAUDE_REVIEW_001.json) | 1 | 1 | `c3233ca50f` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020A_score…` |
| [DETERMINEX_WAVE020A_SIGNOFF_GATE_INJECTION_FINAL_STATE_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE020A_SIGNOFF_GATE_INJECTION_FINAL_STATE_CLAUDE_REVIEW_001.json) | 1 | 1 | `c3233ca50f` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020A_signo…` |
| [DETERMINEX_WAVE020A_SYNTHESIS_AND_WAVE020B_PRESSURE_QUEUE_001](../locks/sentinel/DETERMINEX_WAVE020A_SYNTHESIS_AND_WAVE020B_PRESSURE_QUEUE_001.json) | 1 | 1 | `c3233ca50f` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020A_synth…` |
| [DETERMINEX_WAVE020A_TIER1_TRANSCRIPT_FINAL_STATE_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE020A_TIER1_TRANSCRIPT_FINAL_STATE_CLAUDE_REVIEW_001.json) | 1 | 1 | `c3233ca50f` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020A_tier1…` |
| [DETERMINEX_WAVE020B5_CODEX_EXECUTION_CONTRACT_WRITER_CLAUDE_001](../locks/sentinel/DETERMINEX_WAVE020B5_CODEX_EXECUTION_CONTRACT_WRITER_CLAUDE_001.json) | 1 | 1 | `8a55871fdd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020B5_code…` |
| [DETERMINEX_WAVE020B5_ENFORCEMENT_COMPLETENESS_CLAUDE_001](../locks/sentinel/DETERMINEX_WAVE020B5_ENFORCEMENT_COMPLETENESS_CLAUDE_001.json) | 1 | 1 | `8a55871fdd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020B5_enfo…` |
| [DETERMINEX_WAVE020B5_HARD_FLOOR_STATUS_CLAUDE_001](../locks/sentinel/DETERMINEX_WAVE020B5_HARD_FLOOR_STATUS_CLAUDE_001.json) | 1 | 1 | `8a55871fdd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020B5_hard…` |
| [DETERMINEX_WAVE020B5_LATEST_STATE_VERIFICATION_CLAUDE_001](../locks/sentinel/DETERMINEX_WAVE020B5_LATEST_STATE_VERIFICATION_CLAUDE_001.json) | 1 | 1 | `8a55871fdd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020B5_late…` |
| [DETERMINEX_WAVE020B5_PRODUCTION_PROOF_REPORT_CURRENT_STATE_CLAUDE_001](../locks/sentinel/DETERMINEX_WAVE020B5_PRODUCTION_PROOF_REPORT_CURRENT_STATE_CLAUDE_001.json) | 1 | 1 | `8a55871fdd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020B5_prod…` |
| [DETERMINEX_WAVE020B5_REPAIR_CAPABILITY_CURRENT_STATE_CLAUDE_001](../locks/sentinel/DETERMINEX_WAVE020B5_REPAIR_CAPABILITY_CURRENT_STATE_CLAUDE_001.json) | 1 | 1 | `8a55871fdd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020B5_repa…` |
| [DETERMINEX_WAVE020B5_SCORE_AND_MOVEMENT_AUDIT_CLAUDE_001](../locks/sentinel/DETERMINEX_WAVE020B5_SCORE_AND_MOVEMENT_AUDIT_CLAUDE_001.json) | 1 | 1 | `8a55871fdd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020B5_scor…` |
| [DETERMINEX_WAVE020B5_SYNTHESIS_AND_CODEX_HANDOFF_CLAUDE_001](../locks/sentinel/DETERMINEX_WAVE020B5_SYNTHESIS_AND_CODEX_HANDOFF_CLAUDE_001.json) | 1 | 1 | `8a55871fdd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020B5_synt…` |
| [DETERMINEX_WAVE020B5_TIER1_TRANSCRIPT_CURRENT_STATE_CLAUDE_001](../locks/sentinel/DETERMINEX_WAVE020B5_TIER1_TRANSCRIPT_CURRENT_STATE_CLAUDE_001.json) | 1 | 1 | `8a55871fdd` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020B5_tier…` |
| [DETERMINEX_WAVE020C5_BOUNDED_REPAIR_VERIFY_LOCK_001](../locks/sentinel/DETERMINEX_WAVE020C5_BOUNDED_REPAIR_VERIFY_LOCK_001.json) | 1 | 1 | `6aac2b31a5` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020C5_boun…` |
| [DETERMINEX_WAVE020C5_CODEX_CLAIM_VERIFICATION_LOCK_001](../locks/sentinel/DETERMINEX_WAVE020C5_CODEX_CLAIM_VERIFICATION_LOCK_001.json) | 1 | 1 | `6aac2b31a5` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020C5_code…` |
| [DETERMINEX_WAVE020C5_ENFORCEMENT_BACKFILL_VERIFY_LOCK_001](../locks/sentinel/DETERMINEX_WAVE020C5_ENFORCEMENT_BACKFILL_VERIFY_LOCK_001.json) | 1 | 1 | `6aac2b31a5` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020C5_enfo…` |
| [DETERMINEX_WAVE020C5_EXACT_CODEX_COMMIT_REVIEW_LOCK_001](../locks/sentinel/DETERMINEX_WAVE020C5_EXACT_CODEX_COMMIT_REVIEW_LOCK_001.json) | 1 | 1 | `6aac2b31a5` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020C5_exac…` |
| [DETERMINEX_WAVE020C5_HARD_FLOOR_BOUNDARY_VERIFY_LOCK_001](../locks/sentinel/DETERMINEX_WAVE020C5_HARD_FLOOR_BOUNDARY_VERIFY_LOCK_001.json) | 1 | 1 | `6aac2b31a5` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020C5_hard…` |
| [DETERMINEX_WAVE020C5_PROOF_REPORT_AND_SCORE_DASHBOARD_VERIFY_LOCK_001](../locks/sentinel/DETERMINEX_WAVE020C5_PROOF_REPORT_AND_SCORE_DASHBOARD_VERIFY_LOCK_001.json) | 1 | 1 | `6aac2b31a5` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020C5_proo…` |
| [DETERMINEX_WAVE020C5_SCORE_DELTA_VERIFY_LOCK_001](../locks/sentinel/DETERMINEX_WAVE020C5_SCORE_DELTA_VERIFY_LOCK_001.json) | 1 | 1 | `6aac2b31a5` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020C5_scor…` |
| [DETERMINEX_WAVE020C5_SYNTHESIS_AND_WAVE021_CORRECTIVE_QUEUE_LOCK_001](../locks/sentinel/DETERMINEX_WAVE020C5_SYNTHESIS_AND_WAVE021_CORRECTIVE_QUEUE_LOCK_001.json) | 1 | 1 | `6aac2b31a5` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020C5_synt…` |
| [DETERMINEX_WAVE020C5_TIER1_GITHUB_ACTIONS_VERIFY_LOCK_001](../locks/sentinel/DETERMINEX_WAVE020C5_TIER1_GITHUB_ACTIONS_VERIFY_LOCK_001.json) | 1 | 1 | `6aac2b31a5` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020C5_tier…` |
| [DETERMINEX_WAVE020C_CLAIM_SCANNER_EXPANSION_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE020C_CLAIM_SCANNER_EXPANSION_CLAUDE_REVIEW_001.json) | 1 | 1 | `1bafcc410b` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020C_claim…` |
| [DETERMINEX_WAVE020C_CLAIM_SCANNER_FORBIDDEN_PHRASE_EXPANSION_LOCK_001](../locks/sentinel/DETERMINEX_WAVE020C_CLAIM_SCANNER_FORBIDDEN_PHRASE_EXPANSION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020c_contr…` |
| [DETERMINEX_WAVE020C_CLAUDE_SYNTHESIS_AND_WAVE021_QUEUE_001](../locks/sentinel/DETERMINEX_WAVE020C_CLAUDE_SYNTHESIS_AND_WAVE021_QUEUE_001.json) | 1 | 1 | `1bafcc410b` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020C_claud…` |
| [DETERMINEX_WAVE020C_CONDITIONAL_HARD_FLOOR_EXECUTION_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE020C_CONDITIONAL_HARD_FLOOR_EXECUTION_CLAUDE_REVIEW_001.json) | 1 | 1 | `1bafcc410b` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020C_condi…` |
| [DETERMINEX_WAVE020C_CONDITIONAL_HARD_FLOOR_EXECUTION_IF_APPROVED_LOCK_001](../locks/sentinel/DETERMINEX_WAVE020C_CONDITIONAL_HARD_FLOOR_EXECUTION_IF_APPROVED_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020c_contr…` |
| [DETERMINEX_WAVE020C_CONSUME_CLAUDE_020B5_CONTRACT_LOCK_001](../locks/sentinel/DETERMINEX_WAVE020C_CONSUME_CLAUDE_020B5_CONTRACT_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020c_contr…` |
| [DETERMINEX_WAVE020C_CONTRACT_CONSUMPTION_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE020C_CONTRACT_CONSUMPTION_CLAUDE_REVIEW_001.json) | 1 | 1 | `1bafcc410b` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020C_contr…` |
| [DETERMINEX_WAVE020C_CONTRACT_EXECUTION_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_WAVE020C_CONTRACT_EXECUTION_RECONCILIATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020c_contr…` |
| [DETERMINEX_WAVE020C_FIRST_BOUNDED_REPAIR_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE020C_FIRST_BOUNDED_REPAIR_CLAUDE_REVIEW_001.json) | 1 | 1 | `1bafcc410b` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020C_first…` |
| [DETERMINEX_WAVE020C_FIRST_BOUNDED_REPAIR_FIXTURE_LOCK_001](../locks/sentinel/DETERMINEX_WAVE020C_FIRST_BOUNDED_REPAIR_FIXTURE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020c_contr…` |
| [DETERMINEX_WAVE020C_LEGACY_EXECUTION_RUNG_SIGNOFF_BACKFILL_LOCK_001](../locks/sentinel/DETERMINEX_WAVE020C_LEGACY_EXECUTION_RUNG_SIGNOFF_BACKFILL_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020c_contr…` |
| [DETERMINEX_WAVE020C_LEGACY_EXECUTION_RUNG_SIGNOFF_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE020C_LEGACY_EXECUTION_RUNG_SIGNOFF_CLAUDE_REVIEW_001.json) | 1 | 1 | `1bafcc410b` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020C_legac…` |
| [DETERMINEX_WAVE020C_PRODUCTION_PROOF_REPORT_HTML_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE020C_PRODUCTION_PROOF_REPORT_HTML_CLAUDE_REVIEW_001.json) | 1 | 1 | `1bafcc410b` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020C_produ…` |
| [DETERMINEX_WAVE020C_PRODUCTION_PROOF_REPORT_HTML_REGENERATION_LOCK_001](../locks/sentinel/DETERMINEX_WAVE020C_PRODUCTION_PROOF_REPORT_HTML_REGENERATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020c_contr…` |
| [DETERMINEX_WAVE020C_REAL_SIGNATURE_IMPORT_PROCEDURE_AND_FIRST_PACKET_LOCK_001](../locks/sentinel/DETERMINEX_WAVE020C_REAL_SIGNATURE_IMPORT_PROCEDURE_AND_FIRST_PACKET_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020c_contr…` |
| [DETERMINEX_WAVE020C_RUNTIME_HARDENING_FULL_TEN_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE020C_RUNTIME_HARDENING_FULL_TEN_CLAUDE_REVIEW_001.json) | 1 | 1 | `1bafcc410b` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020C_runti…` |
| [DETERMINEX_WAVE020C_RUNTIME_HARDENING_REMAINING_FOUR_LOCK_001](../locks/sentinel/DETERMINEX_WAVE020C_RUNTIME_HARDENING_REMAINING_FOUR_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020c_contr…` |
| [DETERMINEX_WAVE020C_SCORE_DASHBOARD_AND_DELTA_GUARD_CI_LOCK_001](../locks/sentinel/DETERMINEX_WAVE020C_SCORE_DASHBOARD_AND_DELTA_GUARD_CI_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020c_contr…` |
| [DETERMINEX_WAVE020C_SCORE_DASHBOARD_DELTA_GUARD_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE020C_SCORE_DASHBOARD_DELTA_GUARD_CLAUDE_REVIEW_001.json) | 1 | 1 | `1bafcc410b` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020C_score…` |
| [DETERMINEX_WAVE020C_SIGNATURE_IMPORT_SPEND_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE020C_SIGNATURE_IMPORT_SPEND_CLAUDE_REVIEW_001.json) | 1 | 1 | `1bafcc410b` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020C_signa…` |
| [DETERMINEX_WAVE020C_SIGNOFF_GATE_FULL_NINE_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE020C_SIGNOFF_GATE_FULL_NINE_CLAUDE_REVIEW_001.json) | 1 | 1 | `1bafcc410b` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020C_signo…` |
| [DETERMINEX_WAVE020C_SIGNOFF_GATE_REMAINING_FOUR_LOCK_001](../locks/sentinel/DETERMINEX_WAVE020C_SIGNOFF_GATE_REMAINING_FOUR_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020c_contr…` |
| [DETERMINEX_WAVE020C_TIER1_FOURTH_FAMILY_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE020C_TIER1_FOURTH_FAMILY_CLAUDE_REVIEW_001.json) | 1 | 1 | `1bafcc410b` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020C_tier1…` |
| [DETERMINEX_WAVE020C_TIER1_GITHUB_ACTIONS_CI_CONFIG_TRANSCRIPT_LOCK_001](../locks/sentinel/DETERMINEX_WAVE020C_TIER1_GITHUB_ACTIONS_CI_CONFIG_TRANSCRIPT_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020c_contr…` |
| [DETERMINEX_WAVE021_ADAPTER_INTERFACE_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE021_ADAPTER_INTERFACE_CLAUDE_REVIEW_001.json) | 1 | 1 | `be94416e06` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_021_adapte…` |
| [DETERMINEX_WAVE021_CANONICAL_FAMILY_REGISTRY_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE021_CANONICAL_FAMILY_REGISTRY_CLAUDE_REVIEW_001.json) | 1 | 1 | `be94416e06` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_021_canoni…` |
| [DETERMINEX_WAVE021_CONTRACT_RECEIPT_AND_START_STATE_LOCK_001](../locks/sentinel/DETERMINEX_WAVE021_CONTRACT_RECEIPT_AND_START_STATE_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_WAVE021_CONTRACT_RECEIPT_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE021_CONTRACT_RECEIPT_CLAUDE_REVIEW_001.json) | 1 | 1 | `be94416e06` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_021_contra…` |
| [DETERMINEX_WAVE021_EXTERNAL_AUTHORITY_TRACK_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE021_EXTERNAL_AUTHORITY_TRACK_CLAUDE_REVIEW_001.json) | 1 | 1 | `be94416e06` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_021_extern…` |
| [DETERMINEX_WAVE021_FIFTH_FAMILY_ADAPTER_TRANSCRIPT_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE021_FIFTH_FAMILY_ADAPTER_TRANSCRIPT_CLAUDE_REVIEW_001.json) | 1 | 1 | `be94416e06` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_021_fifth_…` |
| [DETERMINEX_WAVE021_FOUR_VERIFIED_FAMILY_ADAPTER_PORT_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE021_FOUR_VERIFIED_FAMILY_ADAPTER_PORT_CLAUDE_REVIEW_001.json) | 1 | 1 | `be94416e06` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_021_four_v…` |
| [DETERMINEX_WAVE021_MACHINE_PROMOTION_RULES_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE021_MACHINE_PROMOTION_RULES_CLAUDE_REVIEW_001.json) | 1 | 1 | `be94416e06` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_021_machin…` |
| [DETERMINEX_WAVE021_NONCODER_PROOF_REPORT_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE021_NONCODER_PROOF_REPORT_CLAUDE_REVIEW_001.json) | 1 | 1 | `be94416e06` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_021_noncod…` |
| [DETERMINEX_WAVE021_PROGRAM_AUTHORITY_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_WAVE021_PROGRAM_AUTHORITY_RECONCILIATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_WAVE021_PROGRAM_AUTHORITY_SCHEMA_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE021_PROGRAM_AUTHORITY_SCHEMA_CLAUDE_REVIEW_001.json) | 1 | 1 | `be94416e06` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_021_progra…` |
| [DETERMINEX_WAVE021_PROGRAM_AUTHORITY_SYNTHESIS_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE021_PROGRAM_AUTHORITY_SYNTHESIS_CLAUDE_REVIEW_001.json) | 1 | 1 | `be94416e06` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_021_progra…` |
| [DETERMINEX_WAVE021_PROGRAM_NEGATIVE_SIGNAL_REGISTRY_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE021_PROGRAM_NEGATIVE_SIGNAL_REGISTRY_CLAUDE_REVIEW_001.json) | 1 | 1 | `be94416e06` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_021_progra…` |
| [DETERMINEX_WAVE022_DAY1_STRUCTURAL_COVERAGE_DASHBOARD_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE022_DAY1_STRUCTURAL_COVERAGE_DASHBOARD_REVIEW_001.json) | 1 | 1 | `8f0873491d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_022_day1_s…` |
| [DETERMINEX_WAVE022_EXTERNAL_AUTHORITY_UNLOCK_PLAN_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE022_EXTERNAL_AUTHORITY_UNLOCK_PLAN_REVIEW_001.json) | 1 | 1 | `8f0873491d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_022_extern…` |
| [DETERMINEX_WAVE022_IDEA_LAB_ACCEPTANCE_TEST_GENERATOR_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE022_IDEA_LAB_ACCEPTANCE_TEST_GENERATOR_REVIEW_001.json) | 1 | 1 | `8f0873491d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_022_idea_l…` |
| [DETERMINEX_WAVE022_NONCODER_PROGRAM_AUTHORITY_REPORT_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE022_NONCODER_PROGRAM_AUTHORITY_REPORT_REVIEW_001.json) | 1 | 1 | `8f0873491d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_022_noncod…` |
| [DETERMINEX_WAVE022_PROGRAM_AUTHORITY_PRODUCT_BINDING_SYNTHESIS_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE022_PROGRAM_AUTHORITY_PRODUCT_BINDING_SYNTHESIS_REVIEW_001.json) | 1 | 1 | `8f0873491d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_022_progra…` |
| [DETERMINEX_WAVE022_PROGRAM_AUTHORITY_RECORD_CONSUMPTION_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE022_PROGRAM_AUTHORITY_RECORD_CONSUMPTION_REVIEW_001.json) | 1 | 1 | `8f0873491d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_022_progra…` |
| [DETERMINEX_WAVE022_PROMOTION_AND_NEGATIVE_ENFORCEMENT_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE022_PROMOTION_AND_NEGATIVE_ENFORCEMENT_REVIEW_001.json) | 1 | 1 | `8f0873491d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_022_promot…` |
| [DETERMINEX_WAVE022_REPO_CLINIC_AUTHORITY_INTAKE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE022_REPO_CLINIC_AUTHORITY_INTAKE_REVIEW_001.json) | 1 | 1 | `8f0873491d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_022_repo_c…` |
| [DETERMINEX_WAVE022_TIER1_ADAPTER_EXPANSION_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE022_TIER1_ADAPTER_EXPANSION_REVIEW_001.json) | 1 | 1 | `8f0873491d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_022_tier1_…` |
| [DETERMINEX_WAVE022_W021_FINAL_STATE_RECONCILIATION_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE022_W021_FINAL_STATE_RECONCILIATION_REVIEW_001.json) | 1 | 1 | `8f0873491d` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_022_w021_f…` |
| [DETERMINEX_WAVE023_CODEX_COMMITS_BEFORE_REVIEW_PROTOCOL_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE023_CODEX_COMMITS_BEFORE_REVIEW_PROTOCOL_REVIEW_001.json) | 1 | 1 | `86bc1446f4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_023_codex_…` |
| [DETERMINEX_WAVE023_DAY1_PRODUCT_SPINE_SYNTHESIS_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE023_DAY1_PRODUCT_SPINE_SYNTHESIS_REVIEW_001.json) | 1 | 1 | `86bc1446f4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_023_day1_p…` |
| [DETERMINEX_WAVE023_DAY1_STRUCTURAL_DASHBOARD_RENDERED_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE023_DAY1_STRUCTURAL_DASHBOARD_RENDERED_REVIEW_001.json) | 1 | 1 | `86bc1446f4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_023_day1_s…` |
| [DETERMINEX_WAVE023_IDEA_LAB_ACCEPTANCE_TEST_EXECUTION_PIPELINE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE023_IDEA_LAB_ACCEPTANCE_TEST_EXECUTION_PIPELINE_REVIEW_001.json) | 1 | 1 | `86bc1446f4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_023_idea_l…` |
| [DETERMINEX_WAVE023_NONCODER_REPORT_RENDERED_OUTPUTS_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE023_NONCODER_REPORT_RENDERED_OUTPUTS_REVIEW_001.json) | 1 | 1 | `86bc1446f4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_023_noncod…` |
| [DETERMINEX_WAVE023_PROMOTION_NEGATIVE_FIXTURE_CORPUS_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE023_PROMOTION_NEGATIVE_FIXTURE_CORPUS_REVIEW_001.json) | 1 | 1 | `86bc1446f4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_023_promot…` |
| [DETERMINEX_WAVE023_REACT_VITE_SIGNED_DEPENDENCY_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE023_REACT_VITE_SIGNED_DEPENDENCY_REVIEW_001.json) | 1 | 1 | `86bc1446f4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_023_react_…` |
| [DETERMINEX_WAVE023_REAL_OPERATOR_SIGNATURE_IMPORT_PREP_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE023_REAL_OPERATOR_SIGNATURE_IMPORT_PREP_REVIEW_001.json) | 1 | 1 | `86bc1446f4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_023_real_o…` |
| [DETERMINEX_WAVE023_REPO_CLINIC_SECOND_FAMILY_REPAIR_LOOP_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE023_REPO_CLINIC_SECOND_FAMILY_REPAIR_LOOP_REVIEW_001.json) | 1 | 1 | `86bc1446f4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_023_repo_c…` |
| [DETERMINEX_WAVE023_TIER1_BATCH002_PER_FAMILY_VERIFIED_PROMOTION_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE023_TIER1_BATCH002_PER_FAMILY_VERIFIED_PROMOTION_REVIEW_001.json) | 1 | 1 | `86bc1446f4` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_023_tier1_…` |
| [DETERMINEX_WAVE_004_CELL_MIX_AND_USER_FACING_REALITY_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE_004_CELL_MIX_AND_USER_FACING_REALITY_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_004_cell_m…` |
| [DETERMINEX_WAVE_006_CLAUDE_SYNTHESIS_AND_WAVE_007_PRESSURE_QUEUE_001](../locks/sentinel/DETERMINEX_WAVE_006_CLAUDE_SYNTHESIS_AND_WAVE_007_PRESSURE_QUEUE_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_006_claude…` |
| [DETERMINEX_WAVE_006_SHOCK_DEMO_EXECUTION_GAP_CLAUDE_REVIEW_001](../locks/sentinel/DETERMINEX_WAVE_006_SHOCK_DEMO_EXECUTION_GAP_CLAUDE_REVIEW_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_006_shock_…` |
| [DETERMINEX_WAVE_007_CLAUDE_SYNTHESIS_AND_WAVE_008_PRESSURE_QUEUE_001](../locks/sentinel/DETERMINEX_WAVE_007_CLAUDE_SYNTHESIS_AND_WAVE_008_PRESSURE_QUEUE_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_007_claude…` |
| [DETERMINEX_WAVE_012_CAPABILITY_SATURATION_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_WAVE_012_CAPABILITY_SATURATION_RECONCILIATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_WAVE_013_EXECUTION_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_WAVE_013_EXECUTION_RECONCILIATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_WAVE_014_SIGNED_EXECUTION_AND_CAPABILITY_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_WAVE_014_SIGNED_EXECUTION_AND_CAPABILITY_RECONCILIATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_014_signed…` |
| [DETERMINEX_WAVE_015_CANONICAL_AND_HARD_FLOOR_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_WAVE_015_CANONICAL_AND_HARD_FLOOR_RECONCILIATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_015_canoni…` |
| [DETERMINEX_WAVE_016_CANONICAL_PROMOTION_AND_HARD_FLOOR_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_WAVE_016_CANONICAL_PROMOTION_AND_HARD_FLOOR_RECONCILIATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_016_canoni…` |
| [DETERMINEX_WAVE_017_CANONICAL_SIGNOFF_AND_HARD_FLOOR_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_WAVE_017_CANONICAL_SIGNOFF_AND_HARD_FLOOR_RECONCILIATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_017_canoni…` |
| [DETERMINEX_WAVE_018_CANONICAL_BACKFILL_AND_FIRST_FAMILY_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_WAVE_018_CANONICAL_BACKFILL_AND_FIRST_FAMILY_RECONCILIATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_018_canoni…` |
| [DETERMINEX_WAVE_019_EXECUTION_FLOOR_AND_FAMILY_EXPANSION_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_WAVE_019_EXECUTION_FLOOR_AND_FAMILY_EXPANSION_RECONCILIATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_019_execut…` |
| [DETERMINEX_WAVE_020A_FINAL_STATE_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_WAVE_020A_FINAL_STATE_RECONCILIATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wave_020a_final…` |
| [DETERMINEX_WAVE_021_FINAL_STATE_RECONCILIATION_RECEIPT_LOCK_001](../locks/sentinel/DETERMINEX_WAVE_021_FINAL_STATE_RECONCILIATION_RECEIPT_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_WAVE_022_PROGRAM_AUTHORITY_PRODUCT_BINDING_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_WAVE_022_PROGRAM_AUTHORITY_PRODUCT_BINDING_RECONCILIATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_WAVE_023_DAY1_PRODUCT_SPINE_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_WAVE_023_DAY1_PRODUCT_SPINE_RECONCILIATION_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [DETERMINEX_WINDOWS_FIRST_LOCAL_DEPENDENCY_CHECK_LOCK_001](../locks/sentinel/DETERMINEX_WINDOWS_FIRST_LOCAL_DEPENDENCY_CHECK_LOCK_001.json) | 1 | 1 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_windows_first_l…` |
| [DETERMINEX_WINDOWS_LONG_PATH_CHECKOUT_REMEDIATION_LOCK_001](../locks/sentinel/DETERMINEX_WINDOWS_LONG_PATH_CHECKOUT_REMEDIATION_LOCK_001.json) | 32 | 32 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_windows_long_pa…` |
| [DETERMINEX_WIX_LIGHT_FAILURE_DIAGNOSTIC_AND_REPAIR_LOCK_001](../locks/sentinel/DETERMINEX_WIX_LIGHT_FAILURE_DIAGNOSTIC_AND_REPAIR_LOCK_001.json) | 36 | 36 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_wix_light_failu…` |
| [DETERMINEX_WORKSPACE_EVIDENCE_RECONCILIATION_LOCK_001](../locks/sentinel/DETERMINEX_WORKSPACE_EVIDENCE_RECONCILIATION_LOCK_001.json) | 15 | 15 | `e113efbd6e` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_determinex_splash_…` |
| [DETERMINEX_WORKSPACE_EVIDENCE_RECONCILIATION_LOCK_002](../locks/sentinel/DETERMINEX_WORKSPACE_EVIDENCE_RECONCILIATION_LOCK_002.json) | 7 | 7 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/status/test_determinex_workspa…` |
| [CI_LOCK_001](../locks/sentinel/CI_LOCK_001.json) | 1 | 1 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [CI_QUALITY_GATE_LOCK_001](../locks/sentinel/CI_QUALITY_GATE_LOCK_001.json) | 1 | 1 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [CLAUDE_APPROVAL_REPLAY_AND_STALENESS_LOCK_001](../locks/sentinel/CLAUDE_APPROVAL_REPLAY_AND_STALENESS_LOCK_001.json) | 22 | 22 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_approval_replay…` |
| [CLAUDE_AUTHORITY_LEAK_REMEDIATION_FINAL_STATE_LOCK_001](../locks/sentinel/CLAUDE_AUTHORITY_LEAK_REMEDIATION_FINAL_STATE_LOCK_001.json) | 10 | 10 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_claude_authorit…` |
| [CLAUDE_AUTH_005_READY_AUTHORIZED_LANGUAGE_LOCK_001](../locks/sentinel/CLAUDE_AUTH_005_READY_AUTHORIZED_LANGUAGE_LOCK_001.json) | 14 | 14 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_ready_authorize…` |
| [CLAUDE_CONFIG_ROOT_ALLOWLIST_LOCK_001](../locks/sentinel/CLAUDE_CONFIG_ROOT_ALLOWLIST_LOCK_001.json) | 17 | 17 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_config_root_allowl…` |
| [CLAUDE_FRONTEND_AUTHORITY_VISUAL_AUDIT_LOCK_001](../locks/sentinel/CLAUDE_FRONTEND_AUTHORITY_VISUAL_AUDIT_LOCK_001.json) | 19 | 19 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_frontend_authority…` |
| [CLAUDE_IDE_HYGIENE_FINAL_STATE_LOCK_001](../locks/sentinel/CLAUDE_IDE_HYGIENE_FINAL_STATE_LOCK_001.json) | 13 | 13 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_claude_ide_hygi…` |
| [CLAUDE_LANE_LIVE_MODEL_READY_FINAL_STATE_LOCK_001](../locks/sentinel/CLAUDE_LANE_LIVE_MODEL_READY_FINAL_STATE_LOCK_001.json) | 24 | 24 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/dev/test_claude_lane_live_m…` |
| [CLAUDE_OPERATOR_IDENTITY_BOUNDING_LOCK_001](../locks/sentinel/CLAUDE_OPERATOR_IDENTITY_BOUNDING_LOCK_001.json) | 19 | 19 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_operator_identity_…` |
| [CLAUDE_PRE_APPLY_CONFIRMATION_PANEL_LOCK_001](../locks/sentinel/CLAUDE_PRE_APPLY_CONFIRMATION_PANEL_LOCK_001.json) | 22 | 22 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_pre_apply_confirma…` |
| [CLAUDE_PROOF_BEFORE_MUTATION_DEMO_SCRIPT_LOCK_001](../locks/sentinel/CLAUDE_PROOF_BEFORE_MUTATION_DEMO_SCRIPT_LOCK_001.json) | 22 | 22 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_proof_before_mu…` |
| [CLAUDE_PUBLIC_CLAIMS_LEDGER_LOCK_001](../locks/sentinel/CLAUDE_PUBLIC_CLAIMS_LEDGER_LOCK_001.json) | 21 | 21 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_public_claims_l…` |
| [CLAUDE_REAL_MODEL_VERIFIER_READY_FINAL_STATE_LOCK_001](../locks/sentinel/CLAUDE_REAL_MODEL_VERIFIER_READY_FINAL_STATE_LOCK_001.json) | 16 | 16 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/dev/test_claude_real_model_…` |
| [CLOAK_LOCK_001](../locks/sentinel/CLOAK_LOCK_001.json) | 11 | 862 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/test_cloak_smoke.py -q --tb…` |
| [CLOAK_THREAT_MODEL_LOCK_001](../locks/sentinel/CLOAK_THREAT_MODEL_LOCK_001.json) | 1 | 1 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [CODEBASE_EXPLORER_SMOKE_LOCK_001](../locks/sentinel/CODEBASE_EXPLORER_SMOKE_LOCK_001.json) | 12 | 12 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/intake/test_codebase_explor…` |
| [CONFIG_SPINE_LOCK_001](../locks/sentinel/CONFIG_SPINE_LOCK_001.json) | 31 | 31 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/test_settings.py -q --tb=sh…` |
| [CORPUS_COVERAGE_LOCK_001](../locks/sentinel/CORPUS_COVERAGE_LOCK_001.json) | 7 | 732 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/test_corpus_coverage…` |
| [CORPUS_ELIGIBILITY_REPAIR_TRACE_GUARD_LOCK_001](../locks/sentinel/CORPUS_ELIGIBILITY_REPAIR_TRACE_GUARD_LOCK_001.json) | 20 | 20 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/test_corpus_eligibil…` |
| [CORPUS_LICENSE_LOCK_001](../locks/sentinel/CORPUS_LICENSE_LOCK_001.json) | 53 | 53 | `0a3d1150e9` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/test_license_gate.py…` |
| [CORPUS_MIGRATION_LOCK_001](../locks/sentinel/CORPUS_MIGRATION_LOCK_001.json) | 20 | 862 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/test_schema_registry…` |
| [CORPUS_SCHEMA_MATURITY_LOCK_001](../locks/sentinel/CORPUS_SCHEMA_MATURITY_LOCK_001.json) | 8 | 740 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/test_corpus_schema_m…` |
| [CORPUS_WRITE_GUARD_LOCK_001](../locks/sentinel/CORPUS_WRITE_GUARD_LOCK_001.json) | 20 | 20 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/test_immutability_guard.py …` |
| [DIAGNOSE_PROMPT_OPACITY_ENFORCEMENT_LOCK_001](../locks/sentinel/DIAGNOSE_PROMPT_OPACITY_ENFORCEMENT_LOCK_001.json) | 11 | 11 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/models/test_diagnose_prompt…` |
| [DISTILLATION_LOCK_001](../locks/sentinel/DISTILLATION_LOCK_001.json) | 18 | 722 | `0a3d1150e9` | `.\.venv\Scripts\python.exe -m pytest tests/locks/test_distillation_loc…` |
| [EVIDENCE_IMMUTABILITY_GUARD_LOCK_001](../locks/sentinel/EVIDENCE_IMMUTABILITY_GUARD_LOCK_001.json) | 20 | 20 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/test_immutability_guard.py …` |
| [EVIDENCE_INDEX_LOCK_001](../locks/sentinel/EVIDENCE_INDEX_LOCK_001.json) | 5 | 772 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/locks/test_evidence_index_l…` |
| [FRONTEND_APPROVAL_PACKET_ROUNDTRIP_LOCK_001](../locks/sentinel/FRONTEND_APPROVAL_PACKET_ROUNDTRIP_LOCK_001.json) | 12 | 12 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide_frontend/test_frontend_…` |
| [FRONTEND_COMMAND_INVOKE_CLIENT_LOCK_001](../locks/sentinel/FRONTEND_COMMAND_INVOKE_CLIENT_LOCK_001.json) | 11 | 11 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide_frontend/test_frontend_…` |
| [FRONTEND_DIAGNOSE_AND_PATCH_PLAN_FLOW_LOCK_001](../locks/sentinel/FRONTEND_DIAGNOSE_AND_PATCH_PLAN_FLOW_LOCK_001.json) | 11 | 11 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide_frontend/test_frontend_…` |
| [FRONTEND_END_TO_END_REPAIR_FLOW_SMOKE_LOCK_001](../locks/sentinel/FRONTEND_END_TO_END_REPAIR_FLOW_SMOKE_LOCK_001.json) | 12 | 12 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide_frontend/test_frontend_…` |
| [FRONTEND_EVIDENCE_VIEWER_LOCK_001](../locks/sentinel/FRONTEND_EVIDENCE_VIEWER_LOCK_001.json) | 11 | 11 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide_frontend/test_frontend_…` |
| [FRONTEND_HUMAN_APPROVAL_PANEL_LOCK_001](../locks/sentinel/FRONTEND_HUMAN_APPROVAL_PANEL_LOCK_001.json) | 13 | 13 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide_frontend/test_frontend_…` |
| [FRONTEND_LIVE_DIAGNOSE_OPT_IN_SMOKE_LOCK_001](../locks/sentinel/FRONTEND_LIVE_DIAGNOSE_OPT_IN_SMOKE_LOCK_001.json) | 11 | 11 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide_frontend/test_frontend_…` |
| [FRONTEND_MODEL_ROUTE_PANEL_LOCK_001](../locks/sentinel/FRONTEND_MODEL_ROUTE_PANEL_LOCK_001.json) | 11 | 11 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide_frontend/test_frontend_…` |
| [FRONTEND_PANEL_COMMAND_WIRING_LOCK_001](../locks/sentinel/FRONTEND_PANEL_COMMAND_WIRING_LOCK_001.json) | 10 | 10 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide_frontend/test_frontend_…` |
| [FRONTEND_QUALITY_RAILS_LOCK_001](../locks/sentinel/FRONTEND_QUALITY_RAILS_LOCK_001.json) | 10 | 10 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [FRONTEND_REAL_FLOW_E2E_LOCK_001](../locks/sentinel/FRONTEND_REAL_FLOW_E2E_LOCK_001.json) | 11 | 11 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide_frontend/test_frontend_…` |
| [FRONTEND_REPAIR_PANEL_SHELL_LOCK_001](../locks/sentinel/FRONTEND_REPAIR_PANEL_SHELL_LOCK_001.json) | 16 | 16 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide_frontend/test_frontend_…` |
| [FRONTEND_SOURCE_APPLY_DRY_RUN_PANEL_LOCK_001](../locks/sentinel/FRONTEND_SOURCE_APPLY_DRY_RUN_PANEL_LOCK_001.json) | 10 | 10 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide_frontend/test_frontend_…` |
| [FRONTEND_TEMP_VERIFY_PANEL_LOCK_001](../locks/sentinel/FRONTEND_TEMP_VERIFY_PANEL_LOCK_001.json) | 11 | 11 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide_frontend/test_frontend_…` |
| [FRONTEND_WORKSPACE_STATUS_PANEL_LOCK_001](../locks/sentinel/FRONTEND_WORKSPACE_STATUS_PANEL_LOCK_001.json) | 10 | 10 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide_frontend/test_frontend_…` |
| [GO_REPAIR_LOCK_001](../locks/sentinel/GO_REPAIR_LOCK_001.json) | 27 | 617 | `0a3d1150e9` | `.\.venv\Scripts\python.exe -m pytest tests/locks/test_go_repair_lock.p…` |
| [HARDENED_INTAKE_EXECUTION_RUNNER_LOCK_001](../locks/sentinel/HARDENED_INTAKE_EXECUTION_RUNNER_LOCK_001.json) | 47 | 47 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/intake/test_hardened_intake…` |
| [HARDENED_REPAIR_PIPELINE_EXECUTORS_LOCK_001](../locks/sentinel/HARDENED_REPAIR_PIPELINE_EXECUTORS_LOCK_001.json) | 73 | 73 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_hardened_repair…` |
| [HARDENED_VERIFIED_TASK_AND_CODECLASH_LOCK_001](../locks/sentinel/HARDENED_VERIFIED_TASK_AND_CODECLASH_LOCK_001.json) | 30 | 30 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_hardened_verifi…` |
| [HIVE_LOCK_001](../locks/sentinel/HIVE_LOCK_001.json) | 12 | 862 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/test_hive_core.py -q --tb=s…` |
| [HUMAN_APPROVAL_PACKET_UI_MODEL_LOCK_001](../locks/sentinel/HUMAN_APPROVAL_PACKET_UI_MODEL_LOCK_001.json) | 12 | 12 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_human_approval_pac…` |
| [HUMAN_APPROVAL_SOURCE_MUTATION_GATE_LOCK_001](../locks/sentinel/HUMAN_APPROVAL_SOURCE_MUTATION_GATE_LOCK_001.json) | 16 | 16 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_human_approval_…` |
| [IDE_APPROVAL_UX_COPY_LOCK_001](../locks/sentinel/IDE_APPROVAL_UX_COPY_LOCK_001.json) | 10 | 10 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_ide_approval_ux_co…` |
| [IDE_BACKEND_COMMAND_SURFACE_LOCK_001](../locks/sentinel/IDE_BACKEND_COMMAND_SURFACE_LOCK_001.json) | 16 | 16 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_ide_backend_comman…` |
| [IDE_CONSUMER_FLOW_TRACE_LOCK_001](../locks/sentinel/IDE_CONSUMER_FLOW_TRACE_LOCK_001.json) | 8 | 8 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_ide_consumer_flow_…` |
| [IDE_DIAGNOSE_FLOW_LOCK_001](../locks/sentinel/IDE_DIAGNOSE_FLOW_LOCK_001.json) | 10 | 10 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_ide_diagnose_flow_…` |
| [IDE_END_TO_END_UI_FLOW_TRACE_LOCK_001](../locks/sentinel/IDE_END_TO_END_UI_FLOW_TRACE_LOCK_001.json) | 8 | 8 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_ide_end_to_end_ui_…` |
| [IDE_FRONTEND_STATE_CONTRACT_LOCK_001](../locks/sentinel/IDE_FRONTEND_STATE_CONTRACT_LOCK_001.json) | 12 | 12 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_ide_frontend_state…` |
| [IDE_HUMAN_APPROVAL_SIGNING_FLOW_LOCK_001](../locks/sentinel/IDE_HUMAN_APPROVAL_SIGNING_FLOW_LOCK_001.json) | 12 | 12 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_ide_human_approval…` |
| [IDE_LIVE_MODEL_REPAIR_FLOW_STATE_LOCK_001](../locks/sentinel/IDE_LIVE_MODEL_REPAIR_FLOW_STATE_LOCK_001.json) | 13 | 13 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_ide_live_model_rep…` |
| [IDE_MODEL_ROUTE_PANEL_LOCK_001](../locks/sentinel/IDE_MODEL_ROUTE_PANEL_LOCK_001.json) | 12 | 12 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_ide_model_route_pa…` |
| [IDE_PATCH_PLAN_FLOW_LOCK_001](../locks/sentinel/IDE_PATCH_PLAN_FLOW_LOCK_001.json) | 11 | 11 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_ide_patch_plan_flo…` |
| [IDE_REPAIR_STATE_MODEL_LOCK_001](../locks/sentinel/IDE_REPAIR_STATE_MODEL_LOCK_001.json) | 17 | 17 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_ide_repair_state_m…` |
| [IDE_SOURCE_APPLY_GATE_FLOW_LOCK_001](../locks/sentinel/IDE_SOURCE_APPLY_GATE_FLOW_LOCK_001.json) | 11 | 11 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_ide_source_apply_g…` |
| [IDE_TEMP_VERIFY_FLOW_LOCK_001](../locks/sentinel/IDE_TEMP_VERIFY_FLOW_LOCK_001.json) | 9 | 9 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_ide_temp_verify_fl…` |
| [IDE_WORKSPACE_OPEN_FLOW_LOCK_001](../locks/sentinel/IDE_WORKSPACE_OPEN_FLOW_LOCK_001.json) | 14 | 14 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_ide_workspace_open…` |
| [JAVA_CORPUS_LOCK_001](../locks/sentinel/JAVA_CORPUS_LOCK_001.json) | 7 | 7 | `0a3d1150e9` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/test_java_junit_trac…` |
| [JAVA_REPAIR_LOCK_001](../locks/sentinel/JAVA_REPAIR_LOCK_001.json) | 67 | 67 | `0a3d1150e9` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/java_repair/test_jav…` |
| [LEGACY_CORPUS_RECOVERY_LOCK_001](../locks/sentinel/LEGACY_CORPUS_RECOVERY_LOCK_001.json) | 9 | 1025 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/test_legacy_corpus_r…` |
| [LEGACY_REPLAY_PROMOTION_LOCK_001](../locks/sentinel/LEGACY_REPLAY_PROMOTION_LOCK_001.json) | 7 | 1025 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/test_legacy_replay_p…` |
| [LIVE_MODEL_DIAGNOSE_ONLY_TRACE_LOCK_001](../locks/sentinel/LIVE_MODEL_DIAGNOSE_ONLY_TRACE_LOCK_001.json) | 14 | 14 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_live_model_diag…` |
| [LIVE_MODEL_MOCK_COMPATIBILITY_HARNESS_LOCK_001](../locks/sentinel/LIVE_MODEL_MOCK_COMPATIBILITY_HARNESS_LOCK_001.json) | 17 | 17 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/models/test_live_model_mock…` |
| [LIVE_MODEL_PATCH_PLAN_QUARANTINE_LOCK_001](../locks/sentinel/LIVE_MODEL_PATCH_PLAN_QUARANTINE_LOCK_001.json) | 19 | 19 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_live_model_patc…` |
| [LIVE_MODEL_TEMP_PATCH_VERIFIER_GATE_LOCK_001](../locks/sentinel/LIVE_MODEL_TEMP_PATCH_VERIFIER_GATE_LOCK_001.json) | 11 | 11 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_live_model_temp…` |
| [LLM_MOCKED_INTAKE_REPAIR_LOCK_001](../locks/sentinel/LLM_MOCKED_INTAKE_REPAIR_LOCK_001.json) | 25 | 25 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/intake/test_llm_mocked_inta…` |
| [LOCAL_LEGACY_CORPUS_QUARANTINE_LOCK_001](../locks/sentinel/LOCAL_LEGACY_CORPUS_QUARANTINE_LOCK_001.json) | 1 | 772 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [LOCAL_MODEL_ADMISSION_POLICY_LOCK_001](../locks/sentinel/LOCAL_MODEL_ADMISSION_POLICY_LOCK_001.json) | 19 | 19 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/models/test_local_model_adm…` |
| [LOCAL_MODEL_CONFIG_WIZARD_LOCK_001](../locks/sentinel/LOCAL_MODEL_CONFIG_WIZARD_LOCK_001.json) | 15 | 15 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/models/test_local_model_con…` |
| [LOCAL_MODEL_LIVE_ADMISSION_LOCK_001](../locks/sentinel/LOCAL_MODEL_LIVE_ADMISSION_LOCK_001.json) | 23 | 23 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/models/test_local_model_liv…` |
| [LOCAL_MODEL_SETTINGS_PANEL_LOCK_001](../locks/sentinel/LOCAL_MODEL_SETTINGS_PANEL_LOCK_001.json) | 14 | 14 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide_frontend/test_local_mod…` |
| [LOCAL_PROVIDER_SMOKE_TEST_LOCK_001](../locks/sentinel/LOCAL_PROVIDER_SMOKE_TEST_LOCK_001.json) | 13 | 13 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/models/test_local_provider_…` |
| [MODEL_ADMISSION_NO_BYPASS_LOCK_001](../locks/sentinel/MODEL_ADMISSION_NO_BYPASS_LOCK_001.json) | 17 | 17 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_real_model_patc…` |
| [MODEL_ROUTER_LOCK_001](../locks/sentinel/MODEL_ROUTER_LOCK_001.json) | 78 | 78 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/models/test_model_router_lo…` |
| [NATIVE_C_CPP_REPAIR_LOCK_001](../locks/sentinel/NATIVE_C_CPP_REPAIR_LOCK_001.json) | 24 | 641 | `0a3d1150e9` | `.\.venv\Scripts\python.exe -m pytest tests/locks/test_native_c_cpp_rep…` |
| [NO_LOOSE_BENCH_ARTIFACTS_LOCK_001](../locks/sentinel/NO_LOOSE_BENCH_ARTIFACTS_LOCK_001.json) | 5 | 772 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/test_no_loose_bench_artifac…` |
| [OBSERVABILITY_LOCK_001](../locks/sentinel/OBSERVABILITY_LOCK_001.json) | 25 | 887 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/observability/test_event_lo…` |
| [OLLAMA_LOCAL_PROVIDER_SMOKE_LOCK_001](../locks/sentinel/OLLAMA_LOCAL_PROVIDER_SMOKE_LOCK_001.json) | 12 | 12 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/models/test_ollama_local_pr…` |
| [OLLAMA_MODEL_PULL_OPERATOR_GUIDE_LOCK_001](../locks/sentinel/OLLAMA_MODEL_PULL_OPERATOR_GUIDE_LOCK_001.json) | 14 | 14 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/models/test_ollama_model_pu…` |
| [OPT_IN_LIVE_DIAGNOSE_COMMAND_LOCK_001](../locks/sentinel/OPT_IN_LIVE_DIAGNOSE_COMMAND_LOCK_001.json) | 11 | 11 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_opt_in_live_dia…` |
| [OPT_IN_PATCH_PLAN_COMMAND_LOCK_001](../locks/sentinel/OPT_IN_PATCH_PLAN_COMMAND_LOCK_001.json) | 11 | 11 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_opt_in_patch_pl…` |
| [PARALLEL_EXECUTION_LAYER_AUDIT_LOCK_001](../locks/sentinel/PARALLEL_EXECUTION_LAYER_AUDIT_LOCK_001.json) | 27 | 27 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/dev/test_parallel_execution…` |
| [PATH_PORTABILITY_LOCK_001](../locks/sentinel/PATH_PORTABILITY_LOCK_001.json) | 31 | 31 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/test_settings.py -q --tb=sh…` |
| [POST_APPLY_VERIFIER_LOCK_001](../locks/sentinel/POST_APPLY_VERIFIER_LOCK_001.json) | 11 | 11 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_post_apply_veri…` |
| [POST_APPLY_VERIFIER_NO_DEFAULT_PASS_LOCK_001](../locks/sentinel/POST_APPLY_VERIFIER_NO_DEFAULT_PASS_LOCK_001.json) | 14 | 14 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_post_apply_veri…` |
| [PROGRAMBENCH_ALTERNATE_CLEANROOM_IMAGE_PROVENANCE_LOCK_001](../locks/sentinel/PROGRAMBENCH_ALTERNATE_CLEANROOM_IMAGE_PROVENANCE_LOCK_001.json) | 18 | 18 | `607665753e` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_APPROVED_SCANNER_SETUP_LOCK_001](../locks/sentinel/PROGRAMBENCH_APPROVED_SCANNER_SETUP_LOCK_001.json) | 16 | 1339 | `d390e5c881` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_ARTIFACT_IMPORT_OPERATOR_GUIDE_LOCK_001](../locks/sentinel/PROGRAMBENCH_ARTIFACT_IMPORT_OPERATOR_GUIDE_LOCK_001.json) | 6 | 6 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_ARTIFACT_SOURCE_ESCALATION_LOCK_001](../locks/sentinel/PROGRAMBENCH_ARTIFACT_SOURCE_ESCALATION_LOCK_001.json) | 11 | 1083 | `71be79941e` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BATCH001_ARTIFACT_IMPORT_PREFLIGHT_LOCK_001](../locks/sentinel/PROGRAMBENCH_BATCH001_ARTIFACT_IMPORT_PREFLIGHT_LOCK_001.json) | 10 | 10 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BATCH001_ARTIFACT_IMPORT_REQUEST_PACKET_LOCK_001](../locks/sentinel/PROGRAMBENCH_BATCH001_ARTIFACT_IMPORT_REQUEST_PACKET_LOCK_001.json) | 10 | 10 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BATCH001_EXACT_ARTIFACT_IMPORT_GATE_LOCK_001](../locks/sentinel/PROGRAMBENCH_BATCH001_EXACT_ARTIFACT_IMPORT_GATE_LOCK_001.json) | 10 | 10 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BATCH001_EXACT_MANIFEST_METADATA_PLAN_LOCK_001](../locks/sentinel/PROGRAMBENCH_BATCH001_EXACT_MANIFEST_METADATA_PLAN_LOCK_001.json) | 10 | 381 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BATCH001_IMAGE_NAME_DERIVATION_LOCK_001](../locks/sentinel/PROGRAMBENCH_BATCH001_IMAGE_NAME_DERIVATION_LOCK_001.json) | 10 | 381 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BATCH001_IMPORT_SCAN_CAMPAIGN_FINAL_STATE_LOCK_001](../locks/sentinel/PROGRAMBENCH_BATCH001_IMPORT_SCAN_CAMPAIGN_FINAL_STATE_LOCK_001.json) | 10 | 10 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BATCH001_IMPORT_SCAN_PLANNING_LOCK_001](../locks/sentinel/PROGRAMBENCH_BATCH001_IMPORT_SCAN_PLANNING_LOCK_001.json) | 8 | 8 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BATCH001_LIVE_MANIFEST_METADATA_LOOKUP_LOCK_001](../locks/sentinel/PROGRAMBENCH_BATCH001_LIVE_MANIFEST_METADATA_LOOKUP_LOCK_001.json) | 8 | 8 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BATCH001_LOOKUP_CAMPAIGN_FINAL_STATE_LOCK_001](../locks/sentinel/PROGRAMBENCH_BATCH001_LOOKUP_CAMPAIGN_FINAL_STATE_LOCK_001.json) | 8 | 8 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BATCH001_MANIFEST_DIGEST_ADMISSION_LOCK_001](../locks/sentinel/PROGRAMBENCH_BATCH001_MANIFEST_DIGEST_ADMISSION_LOCK_001.json) | 10 | 381 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BATCH001_METADATA_CAMPAIGN_FINAL_STATE_LOCK_001](../locks/sentinel/PROGRAMBENCH_BATCH001_METADATA_CAMPAIGN_FINAL_STATE_LOCK_001.json) | 10 | 381 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BATCH001_METADATA_DIGEST_ADMISSION_FROM_LIVE_LOOKUP_LOCK_001](../locks/sentinel/PROGRAMBENCH_BATCH001_METADATA_DIGEST_ADMISSION_FROM_LIVE_LOOKUP_LOCK_001.json) | 8 | 8 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BATCH001_METADATA_RECOVERY_QUEUE_LOCK_001](../locks/sentinel/PROGRAMBENCH_BATCH001_METADATA_RECOVERY_QUEUE_LOCK_001.json) | 16 | 353 | `c5cffdb154` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BATCH001_METADATA_STATE_REFRESH_LOCK_001](../locks/sentinel/PROGRAMBENCH_BATCH001_METADATA_STATE_REFRESH_LOCK_001.json) | 10 | 381 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BATCH001_OPERATOR_ACTION_REFRESH_LOCK_001](../locks/sentinel/PROGRAMBENCH_BATCH001_OPERATOR_ACTION_REFRESH_LOCK_001.json) | 10 | 381 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BATCH001_OPERATOR_ARTIFACT_IMPORT_PACKET_BUNDLE_LOCK_001](../locks/sentinel/PROGRAMBENCH_BATCH001_OPERATOR_ARTIFACT_IMPORT_PACKET_BUNDLE_LOCK_001.json) | 10 | 10 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BATCH001_OPERATOR_PACKET_BUNDLE_LOCK_001](../locks/sentinel/PROGRAMBENCH_BATCH001_OPERATOR_PACKET_BUNDLE_LOCK_001.json) | 16 | 353 | `c5cffdb154` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BATCH001_OPERATOR_PACKET_REFRESH_AFTER_LOOKUP_LOCK_001](../locks/sentinel/PROGRAMBENCH_BATCH001_OPERATOR_PACKET_REFRESH_AFTER_LOOKUP_LOCK_001.json) | 8 | 8 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BATCH001_POST_LOOKUP_STATE_REFRESH_LOCK_001](../locks/sentinel/PROGRAMBENCH_BATCH001_POST_LOOKUP_STATE_REFRESH_LOCK_001.json) | 8 | 8 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BATCH001_SAFE_MANIFEST_LOOKUP_LOCK_001](../locks/sentinel/PROGRAMBENCH_BATCH001_SAFE_MANIFEST_LOOKUP_LOCK_001.json) | 10 | 381 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BATCH001_SCAN_POLICY_PRECHECK_LOCK_001](../locks/sentinel/PROGRAMBENCH_BATCH001_SCAN_POLICY_PRECHECK_LOCK_001.json) | 10 | 10 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BATCH001_SCAN_QUEUE_LOCK_001](../locks/sentinel/PROGRAMBENCH_BATCH001_SCAN_QUEUE_LOCK_001.json) | 10 | 10 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BATCH001_SCAN_REQUIREMENTS_QUEUE_LOCK_001](../locks/sentinel/PROGRAMBENCH_BATCH001_SCAN_REQUIREMENTS_QUEUE_LOCK_001.json) | 10 | 381 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BATCH001_STATE_AGGREGATOR_LOCK_001](../locks/sentinel/PROGRAMBENCH_BATCH001_STATE_AGGREGATOR_LOCK_001.json) | 15 | 337 | `7be2155dec` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BATCH001_UNBLOCK_PRIORITY_LOCK_001](../locks/sentinel/PROGRAMBENCH_BATCH001_UNBLOCK_PRIORITY_LOCK_001.json) | 4 | 371 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BATCH001_UNBLOCK_PRIORITY_REFRESH_LOCK_001](../locks/sentinel/PROGRAMBENCH_BATCH001_UNBLOCK_PRIORITY_REFRESH_LOCK_001.json) | 10 | 381 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BATCH001_UNBLOCK_SIMULATION_LOCK_001](../locks/sentinel/PROGRAMBENCH_BATCH001_UNBLOCK_SIMULATION_LOCK_001.json) | 16 | 353 | `c5cffdb154` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BATCH_SKIP_DECISION_LOCK_001](../locks/sentinel/PROGRAMBENCH_BATCH_SKIP_DECISION_LOCK_001.json) | 15 | 337 | `7be2155dec` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BOUNDED_RERUN_EXECUTION_LOCK_001](../locks/sentinel/PROGRAMBENCH_BOUNDED_RERUN_EXECUTION_LOCK_001.json) | 10 | 1025 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_CAMPAIGN_REPORTING_API_LOCK_001](../locks/sentinel/PROGRAMBENCH_CAMPAIGN_REPORTING_API_LOCK_001.json) | 15 | 337 | `7be2155dec` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_CAMPAIGN_STATUS_BOARD_LOCK_001](../locks/sentinel/PROGRAMBENCH_CAMPAIGN_STATUS_BOARD_LOCK_001.json) | 11 | 322 | `87eff77039` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_CLEANROOM_BUILD_RECIPE_PROVENANCE_GAP_LOCK_001](../locks/sentinel/PROGRAMBENCH_CLEANROOM_BUILD_RECIPE_PROVENANCE_GAP_LOCK_001.json) | 18 | 1510 | `9e01593db6` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_CLEANROOM_BUILD_RECIPE_RECOVERY_LOCK_001](../locks/sentinel/PROGRAMBENCH_CLEANROOM_BUILD_RECIPE_RECOVERY_LOCK_001.json) | 16 | 1500 | `fac45c4dbc` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_CLEANROOM_IMAGE_HYDRATION_LOCK_001](../locks/sentinel/PROGRAMBENCH_CLEANROOM_IMAGE_HYDRATION_LOCK_001.json) | 12 | 1236 | `da82a95a82` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_CLEANROOM_IMAGE_IMPORT_LOCK_001](../locks/sentinel/PROGRAMBENCH_CLEANROOM_IMAGE_IMPORT_LOCK_001.json) | 12 | 1236 | `da82a95a82` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_CLEANROOM_IMAGE_REMEDIATION_PLAN_LOCK_001](../locks/sentinel/PROGRAMBENCH_CLEANROOM_IMAGE_REMEDIATION_PLAN_LOCK_001.json) | 17 | 1448 | `b13f3aaba1` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_CLEANROOM_IMAGE_SCANNER_ADMISSION_LOCK_001](../locks/sentinel/PROGRAMBENCH_CLEANROOM_IMAGE_SCANNER_ADMISSION_LOCK_001.json) | 15 | 1251 | `d390e5c881` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_CLEANROOM_IMAGE_SCAN_LOCK_001](../locks/sentinel/PROGRAMBENCH_CLEANROOM_IMAGE_SCAN_LOCK_001.json) | 14 | 1236 | `da82a95a82` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_CLEANROOM_IMAGE_SCAN_TRIAGE_LOCK_001](../locks/sentinel/PROGRAMBENCH_CLEANROOM_IMAGE_SCAN_TRIAGE_LOCK_001.json) | 15 | 1358 | `d390e5c881` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_CLEANROOM_RECIPE_PROVENANCE_RECOVERY_LOCK_001](../locks/sentinel/PROGRAMBENCH_CLEANROOM_RECIPE_PROVENANCE_RECOVERY_LOCK_001.json) | 20 | 1624 | `607665753e` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_CODEX_LANE_FINAL_STATE_LOCK_001](../locks/sentinel/PROGRAMBENCH_CODEX_LANE_FINAL_STATE_LOCK_001.json) | 15 | 337 | `7be2155dec` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_CODEX_OPERATOR_READY_FINAL_STATE_LOCK_001](../locks/sentinel/PROGRAMBENCH_CODEX_OPERATOR_READY_FINAL_STATE_LOCK_001.json) | 16 | 353 | `c5cffdb154` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_COMMIT_PROVENANCE_REPAIR_AUDIT_LOCK_001](../locks/sentinel/PROGRAMBENCH_COMMIT_PROVENANCE_REPAIR_AUDIT_LOCK_001.json) | 5 | 5 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_DOCKERHUB_MANIFEST_PROVENANCE_LOCK_001](../locks/sentinel/PROGRAMBENCH_DOCKERHUB_MANIFEST_PROVENANCE_LOCK_001.json) | 10 | 1236 | `da82a95a82` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_DOXYGEN_LANE_FINAL_STATE_LOCK_001](../locks/sentinel/PROGRAMBENCH_DOXYGEN_LANE_FINAL_STATE_LOCK_001.json) | 11 | 322 | `87eff77039` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_EVIDENCE_GRAPH_INTEGRITY_GUARD_LOCK_001](../locks/sentinel/PROGRAMBENCH_EVIDENCE_GRAPH_INTEGRITY_GUARD_LOCK_001.json) | 16 | 353 | `c5cffdb154` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_EVIDENCE_GRAPH_LOCK_001](../locks/sentinel/PROGRAMBENCH_EVIDENCE_GRAPH_LOCK_001.json) | 15 | 337 | `7be2155dec` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_EXACT_PROVIDER_PROBE_PLAN_LOCK_001](../locks/sentinel/PROGRAMBENCH_EXACT_PROVIDER_PROBE_PLAN_LOCK_001.json) | 16 | 353 | `c5cffdb154` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_GENERIC_EXECUTION_PREFLIGHT_LOCK_001](../locks/sentinel/PROGRAMBENCH_GENERIC_EXECUTION_PREFLIGHT_LOCK_001.json) | 15 | 337 | `7be2155dec` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_GENERIC_OPERATOR_POLICY_ADMISSION_LOCK_001](../locks/sentinel/PROGRAMBENCH_GENERIC_OPERATOR_POLICY_ADMISSION_LOCK_001.json) | 15 | 337 | `7be2155dec` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_INFRA_FAILURE_TRIAGE_LOCK_001](../locks/sentinel/PROGRAMBENCH_INFRA_FAILURE_TRIAGE_LOCK_001.json) | 13 | 1058 | `1891191f9f` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_INSTANCE_STATE_SCHEMA_LOCK_001](../locks/sentinel/PROGRAMBENCH_INSTANCE_STATE_SCHEMA_LOCK_001.json) | 15 | 337 | `7be2155dec` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_NEXT_UNBLOCK_DECISION_LOCK_001](../locks/sentinel/PROGRAMBENCH_NEXT_UNBLOCK_DECISION_LOCK_001.json) | 5 | 5 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_OFFICIAL_ARTIFACT_EXECUTION_PREFLIGHT_LOCK_001](../locks/sentinel/PROGRAMBENCH_OFFICIAL_ARTIFACT_EXECUTION_PREFLIGHT_LOCK_001.json) | 11 | 322 | `87eff77039` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_OFFICIAL_ARTIFACT_SANDBOX_REQUIREMENTS_LOCK_001](../locks/sentinel/PROGRAMBENCH_OFFICIAL_ARTIFACT_SANDBOX_REQUIREMENTS_LOCK_001.json) | 11 | 322 | `87eff77039` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_OFFICIAL_ARTIFACT_SECURITY_DECISION_LOCK_001](../locks/sentinel/PROGRAMBENCH_OFFICIAL_ARTIFACT_SECURITY_DECISION_LOCK_001.json) | 8 | 311 | `87eff77039` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_ONLINE_ARTIFACT_DISCOVERY_LOCK_001](../locks/sentinel/PROGRAMBENCH_ONLINE_ARTIFACT_DISCOVERY_LOCK_001.json) | 10 | 1025 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/test_programbench_on…` |
| [PROGRAMBENCH_ONLINE_PROVIDER_REGISTRY_LOCK_001](../locks/sentinel/PROGRAMBENCH_ONLINE_PROVIDER_REGISTRY_LOCK_001.json) | 7 | 1025 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/test_programbench_on…` |
| [PROGRAMBENCH_OPERATOR_ACTION_QUEUE_LOCK_001](../locks/sentinel/PROGRAMBENCH_OPERATOR_ACTION_QUEUE_LOCK_001.json) | 15 | 337 | `7be2155dec` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_OPERATOR_ARTIFACT_ADMISSION_LOCK_001](../locks/sentinel/PROGRAMBENCH_OPERATOR_ARTIFACT_ADMISSION_LOCK_001.json) | 14 | 1072 | `1891191f9f` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_OPERATOR_CLI_LOCK_001](../locks/sentinel/PROGRAMBENCH_OPERATOR_CLI_LOCK_001.json) | 16 | 353 | `c5cffdb154` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_OPERATOR_INBOX_SCANNER_LOCK_001](../locks/sentinel/PROGRAMBENCH_OPERATOR_INBOX_SCANNER_LOCK_001.json) | 16 | 353 | `c5cffdb154` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_OPERATOR_OUTBOX_LOCK_001](../locks/sentinel/PROGRAMBENCH_OPERATOR_OUTBOX_LOCK_001.json) | 16 | 353 | `c5cffdb154` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_OPERATOR_PACKET_ADMISSION_LIVE_PACKET_REVIEW_LOCK_001](../locks/sentinel/PROGRAMBENCH_OPERATOR_PACKET_ADMISSION_LIVE_PACKET_REVIEW_LOCK_001.json) | 4 | 363 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_OPERATOR_PACKET_ADMISSION_PROCESSING_LOCK_001](../locks/sentinel/PROGRAMBENCH_OPERATOR_PACKET_ADMISSION_PROCESSING_LOCK_001.json) | 4 | 4 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_OPERATOR_PACKET_ADMISSION_ROUTER_LOCK_001](../locks/sentinel/PROGRAMBENCH_OPERATOR_PACKET_ADMISSION_ROUTER_LOCK_001.json) | 16 | 353 | `c5cffdb154` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_OPERATOR_PACKET_TEMPLATES_LOCK_001](../locks/sentinel/PROGRAMBENCH_OPERATOR_PACKET_TEMPLATES_LOCK_001.json) | 16 | 353 | `c5cffdb154` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_OPERATOR_PACKET_VALIDATOR_LOCK_001](../locks/sentinel/PROGRAMBENCH_OPERATOR_PACKET_VALIDATOR_LOCK_001.json) | 16 | 353 | `c5cffdb154` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_OPERATOR_PROVENANCE_REQUEST_PACKET_LOCK_001](../locks/sentinel/PROGRAMBENCH_OPERATOR_PROVENANCE_REQUEST_PACKET_LOCK_001.json) | 19 | 19 | `607665753e` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_OPERATOR_READY_AUDIT_LOCK_001](../locks/sentinel/PROGRAMBENCH_OPERATOR_READY_AUDIT_LOCK_001.json) | 4 | 367 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_PLATFORM_COMPLETION_SCORECARD_LOCK_001](../locks/sentinel/PROGRAMBENCH_PLATFORM_COMPLETION_SCORECARD_LOCK_001.json) | 16 | 353 | `c5cffdb154` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_REAL_BOUNDED_RERUN_LOCK_001](../locks/sentinel/PROGRAMBENCH_REAL_BOUNDED_RERUN_LOCK_001.json) | 11 | 1025 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_REBUILD_PROVENANCE_QUARANTINE_DECISION_LOCK_001](../locks/sentinel/PROGRAMBENCH_REBUILD_PROVENANCE_QUARANTINE_DECISION_LOCK_001.json) | 18 | 18 | `607665753e` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_REPLAY_HYDRATION_LOCK_001](../locks/sentinel/PROGRAMBENCH_REPLAY_HYDRATION_LOCK_001.json) | 10 | 1025 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/test_programbench_re…` |
| [PROGRAMBENCH_REPLAY_IMAGE_HYDRATION_LOCK_001](../locks/sentinel/PROGRAMBENCH_REPLAY_IMAGE_HYDRATION_LOCK_001.json) | 10 | 1025 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/test_programbench_re…` |
| [PROGRAMBENCH_REPLAY_METADATA_RECOVERY_LOCK_001](../locks/sentinel/PROGRAMBENCH_REPLAY_METADATA_RECOVERY_LOCK_001.json) | 8 | 1025 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/legacy_recovery/test…` |
| [PROGRAMBENCH_REPLAY_VERIFIER_LOCK_001](../locks/sentinel/PROGRAMBENCH_REPLAY_VERIFIER_LOCK_001.json) | 7 | 1025 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/test_programbench_re…` |
| [PROGRAMBENCH_RERUN_READINESS_MATRIX_LOCK_001](../locks/sentinel/PROGRAMBENCH_RERUN_READINESS_MATRIX_LOCK_001.json) | 11 | 322 | `87eff77039` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_ROOT_CAUSE_PACKET_LOCK_001](../locks/sentinel/PROGRAMBENCH_ROOT_CAUSE_PACKET_LOCK_001.json) | 10 | 1025 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_ROOT_DISAMBIGUATION_LOCK_001](../locks/sentinel/PROGRAMBENCH_ROOT_DISAMBIGUATION_LOCK_001.json) | 9 | 1025 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/test_programbench_ro…` |
| [PROGRAMBENCH_SAFE_REGISTRY_MANIFEST_CLIENT_LOCK_001](../locks/sentinel/PROGRAMBENCH_SAFE_REGISTRY_MANIFEST_CLIENT_LOCK_001.json) | 8 | 8 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_SECURITY_POLICY_ADMISSION_GATE_LOCK_001](../locks/sentinel/PROGRAMBENCH_SECURITY_POLICY_ADMISSION_GATE_LOCK_001.json) | 11 | 322 | `87eff77039` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_SECURITY_POLICY_EXCEPTION_REQUEST_LOCK_001](../locks/sentinel/PROGRAMBENCH_SECURITY_POLICY_EXCEPTION_REQUEST_LOCK_001.json) | 11 | 322 | `87eff77039` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_SKIP_REASON_TAXONOMY_LOCK_001](../locks/sentinel/PROGRAMBENCH_SKIP_REASON_TAXONOMY_LOCK_001.json) | 15 | 337 | `7be2155dec` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_TASK_ROOT_RESOLUTION_LOCK_001](../locks/sentinel/PROGRAMBENCH_TASK_ROOT_RESOLUTION_LOCK_001.json) | 9 | 1025 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/test_programbench_ta…` |
| [PROGRAMBENCH_TASK_SKIP_WITH_PROVENANCE_REASON_LOCK_001](../locks/sentinel/PROGRAMBENCH_TASK_SKIP_WITH_PROVENANCE_REASON_LOCK_001.json) | 11 | 322 | `87eff77039` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_TRAINING_ELIGIBILITY_NEGATIVE_GUARD_LOCK_001](../locks/sentinel/PROGRAMBENCH_TRAINING_ELIGIBILITY_NEGATIVE_GUARD_LOCK_001.json) | 11 | 322 | `87eff77039` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_UPSTREAM_ARTIFACT_AUTHORITY_RECHECK_LOCK_001](../locks/sentinel/PROGRAMBENCH_UPSTREAM_ARTIFACT_AUTHORITY_RECHECK_LOCK_001.json) | 14 | 303 | `87eff77039` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PYTHON_REPAIR_LOCK_001](../locks/sentinel/PYTHON_REPAIR_LOCK_001.json) | 41 | 590 | `0a3d1150e9` | `.\.venv\Scripts\python.exe -m pytest tests/locks/test_python_repair_lo…` |
| [REAL_APPROVAL_APPLY_POST_VERIFY_TRACE_LOCK_001](../locks/sentinel/REAL_APPROVAL_APPLY_POST_VERIFY_TRACE_LOCK_001.json) | 12 | 12 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_real_approval_a…` |
| [REAL_APPROVAL_DIFF_BODY_CONTENT_BINDING_LOCK_001](../locks/sentinel/REAL_APPROVAL_DIFF_BODY_CONTENT_BINDING_LOCK_001.json) | 13 | 13 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_patch_body_hash…` |
| [REAL_BUILD_ADAPTER_TEMP_VERIFY_TRACE_LOCK_001](../locks/sentinel/REAL_BUILD_ADAPTER_TEMP_VERIFY_TRACE_LOCK_001.json) | 10 | 10 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_real_build_adap…` |
| [REAL_HUMAN_APPROVAL_ADMISSION_LOCK_001](../locks/sentinel/REAL_HUMAN_APPROVAL_ADMISSION_LOCK_001.json) | 16 | 16 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_real_human_approva…` |
| [REAL_LIVE_DIAGNOSE_ONLY_LOCK_001](../locks/sentinel/REAL_LIVE_DIAGNOSE_ONLY_LOCK_001.json) | 15 | 15 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/models/test_real_live_diagn…` |
| [REAL_LOCAL_MODEL_ADMISSION_LOCK_001](../locks/sentinel/REAL_LOCAL_MODEL_ADMISSION_LOCK_001.json) | 16 | 16 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/models/test_real_local_mode…` |
| [REAL_LOCAL_MODEL_HEALTHCHECK_LOCK_001](../locks/sentinel/REAL_LOCAL_MODEL_HEALTHCHECK_LOCK_001.json) | 15 | 15 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/models/test_real_local_mode…` |
| [REAL_LOCAL_MODEL_PROVIDER_CONFIG_LOCK_001](../locks/sentinel/REAL_LOCAL_MODEL_PROVIDER_CONFIG_LOCK_001.json) | 13 | 13 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/models/test_real_local_mode…` |
| [REAL_MODEL_DIAGNOSE_WITH_BUILD_VERIFIER_LOCK_001](../locks/sentinel/REAL_MODEL_DIAGNOSE_WITH_BUILD_VERIFIER_LOCK_001.json) | 15 | 15 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/models/test_real_model_diag…` |
| [REAL_MODEL_PATCH_PLAN_WITH_VERIFIER_CONTEXT_LOCK_001](../locks/sentinel/REAL_MODEL_PATCH_PLAN_WITH_VERIFIER_CONTEXT_LOCK_001.json) | 14 | 14 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_real_model_patc…` |
| [REAL_OLLAMA_PROVIDER_DETECTION_LOCK_001](../locks/sentinel/REAL_OLLAMA_PROVIDER_DETECTION_LOCK_001.json) | 13 | 13 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/models/test_real_ollama_pro…` |
| [REAL_PATCH_PLAN_QUARANTINE_LOCK_001](../locks/sentinel/REAL_PATCH_PLAN_QUARANTINE_LOCK_001.json) | 18 | 18 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_real_patch_plan…` |
| [REAL_REPAIR_FLOW_FINAL_STATE_LOCK_001](../locks/sentinel/REAL_REPAIR_FLOW_FINAL_STATE_LOCK_001.json) | 18 | 18 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/dev/test_real_repair_flow_f…` |
| [REAL_TEMP_PATCH_VERIFY_LOCK_001](../locks/sentinel/REAL_TEMP_PATCH_VERIFY_LOCK_001.json) | 12 | 12 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_real_temp_patch…` |
| [REPRODUCIBLE_DEV_LOCK_001](../locks/sentinel/REPRODUCIBLE_DEV_LOCK_001.json) | 1 | 1 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [ROLLBACK_SYMLINK_SEMANTICS_LOCK_001](../locks/sentinel/ROLLBACK_SYMLINK_SEMANTICS_LOCK_001.json) | 14 | 14 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_rollback_symlin…` |
| [ROSETTA_LOCK_001](../locks/sentinel/ROSETTA_LOCK_001.json) | 13 | 862 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/test_rosetta_smoke.py -q --…` |
| [RUST_REPAIR_LOCK_001](../locks/sentinel/RUST_REPAIR_LOCK_001.json) | 45 | 549 | `0a3d1150e9` | `.\.venv\Scripts\python.exe -m pytest tests/locks/test_rust_repair_lock…` |
| [SAFE_PATCH_DIFF_ROLLBACK_LOCK_001](../locks/sentinel/SAFE_PATCH_DIFF_ROLLBACK_LOCK_001.json) | 22 | 22 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_safe_patch_diff…` |
| [SCRIPT_HELPER_EXECUTION_CLASSIFICATION_SWEEP_LOCK_001](../locks/sentinel/SCRIPT_HELPER_EXECUTION_CLASSIFICATION_SWEEP_LOCK_001.json) | 67 | 67 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/dev/test_script_helper_exec…` |
| [SENTINEL_LOCK_001](../locks/sentinel/SENTINEL_LOCK_001.json) | 121 | 121 | `0a3d1150e9` | `.\.venv\Scripts\python.exe -m pytest tests/sentinelbench/test_refusal_…` |
| [SOURCE_MUTATION_APPLY_AFTER_APPROVAL_LOCK_001](../locks/sentinel/SOURCE_MUTATION_APPLY_AFTER_APPROVAL_LOCK_001.json) | 14 | 14 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_source_mutation…` |
| [SOURCE_MUTATION_APPLY_DRY_RUN_LOCK_001](../locks/sentinel/SOURCE_MUTATION_APPLY_DRY_RUN_LOCK_001.json) | 11 | 11 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_source_mutation…` |
| [SOURCE_MUTATION_ROLLBACK_EXECUTION_LOCK_001](../locks/sentinel/SOURCE_MUTATION_ROLLBACK_EXECUTION_LOCK_001.json) | 11 | 11 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_source_mutation…` |
| [SOURCE_MUTATION_ROLLBACK_SNAPSHOT_LOCK_001](../locks/sentinel/SOURCE_MUTATION_ROLLBACK_SNAPSHOT_LOCK_001.json) | 12 | 12 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_source_mutation…` |
| [SQL_ORACLE_LOCK_001](../locks/sentinel/SQL_ORACLE_LOCK_001.json) | 22 | 686 | `0a3d1150e9` | `.\.venv\Scripts\python.exe -m pytest tests/locks/test_sql_oracle_lock.…` |
| [STORAGE_OPERATIONS_LOCK_001](../locks/sentinel/STORAGE_OPERATIONS_LOCK_001.json) | 1 | 1 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [SUPPLY_CHAIN_LOCK_001](../locks/sentinel/SUPPLY_CHAIN_LOCK_001.json) | 133 | 133 | `0a3d1150e9` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/test_license_gate.py…` |
| [TAURI_BACKEND_COMMAND_BRIDGE_LOCK_001](../locks/sentinel/TAURI_BACKEND_COMMAND_BRIDGE_LOCK_001.json) | 13 | 13 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_tauri_backend_comm…` |
| [TAURI_COMMAND_VERB_ALIGNMENT_LOCK_001](../locks/sentinel/TAURI_COMMAND_VERB_ALIGNMENT_LOCK_001.json) | 7 | 7 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_tauri_command_verb…` |
| [TAURI_LIB_RS_COMMAND_WIRING_LOCK_001](../locks/sentinel/TAURI_LIB_RS_COMMAND_WIRING_LOCK_001.json) | 10 | 10 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide_frontend/test_tauri_lib…` |
| [TAURI_RUST_COMMAND_BRIDGE_LOCK_001](../locks/sentinel/TAURI_RUST_COMMAND_BRIDGE_LOCK_001.json) | 17 | 17 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide_frontend/test_tauri_rus…` |
| [TEMP_PATCH_VERIFY_COMMAND_LOCK_001](../locks/sentinel/TEMP_PATCH_VERIFY_COMMAND_LOCK_001.json) | 9 | 9 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_temp_patch_veri…` |
| [TRAINING_CORPUS_DASHBOARD_LOCK_001](../locks/sentinel/TRAINING_CORPUS_DASHBOARD_LOCK_001.json) | 4 | 772 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/test_training_corpus…` |
| [TYPESCRIPT_REPAIR_LOCK_001](../locks/sentinel/TYPESCRIPT_REPAIR_LOCK_001.json) | 23 | 664 | `0a3d1150e9` | `.\.venv\Scripts\python.exe -m pytest tests/locks/test_typescript_repai…` |
| [VERIFIED_REPAIR_TRACE_LOCK_001](../locks/sentinel/VERIFIED_REPAIR_TRACE_LOCK_001.json) | 13 | 13 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_verified_repair…` |
| [VERIFIER_COVERAGE_MATRIX_LOCK_001](../locks/sentinel/VERIFIER_COVERAGE_MATRIX_LOCK_001.json) | 39 | 39 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/intake/test_verifier_covera…` |
| [VISUAL_REPAIR_LOCK_001](../locks/sentinel/VISUAL_REPAIR_LOCK_001.json) | 21 | 21 | `0a3d1150e9` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [WORKSPACE_ESCAPE_LOCK_001](../locks/sentinel/WORKSPACE_ESCAPE_LOCK_001.json) | 12 | 862 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/security/test_workspace_sym…` |

### What Each Lock Proves

#### ACTION_GOVERNOR_LOCK_001

**Proves:** ACTION_GOVERNOR_LOCK_001

**Does not prove:** Does not prove the governor is wired into every agent controller. The lock proves the gate logic is correct; call-site coverage must be verified separately.

#### AIDER_POLYGLOT_TRACE_HARNESS_LOCK_001

**Proves:** Turn Aider Polyglot / Exercism-style benchmark attempts into signed, schema-complete corpus traces across locked languages.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### APPLY_GATE_FIXTURE_REFUSAL_LOCK_001

**Proves:** Rung 2 of the Claude authority leak remediation campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### APPROVAL_SIGNATURE_CRYPTOGRAPHIC_BINDING_LOCK_001

**Proves:** Rung 7 of the Claude authority leak remediation campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### ARBITRARY_REPO_READINESS_MATRIX_LOCK_001

**Proves:** Rung 9 of the verified-repair campaign. Surfaces a precise, machine-readable picture of where the apparatus is — and is not — ready. The IDE / CLI / audit tools consume this directly. Unsupported rows are explicitly BLOCKED_UNSUPPORTED; no row is marked ready that isn't.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### ARCH_GAUNTLET_CI_LOCK_001

**Proves:** Rung 7 of the post-audit Claude-lane sequence. With MUST_MIGRATE=0 and BLOCKED_UNSAFE=0 from rung 6, the architecture lane is at the cleanest possible baseline for CI witness wiring. Going forward, every push/PR that touches scripts/, tests/, locks/, or the workflow itself runs the gauntlet on Ubuntu and proves the invariants survive an environment Ryan has never personally observed.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### BENCH_TO_CORPUS_ELIGIBILITY_LOCK_001

**Proves:** Require new benchmark traces to be schema-complete before they can become training-eligible corpus rows.

**Does not prove:** Does not prove corpus balance, training effectiveness, or public benchmark dominance by itself.

#### BROWSER_AGENT_LOCK_001

**Proves:** BROWSER_AGENT_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### BUILD_ADAPTER_BACKED_VERIFIER_SELECTION_LOCK_001

**Proves:** Rung 4 of the real-model + build-adapter-verifier campaign (subordinate to Codex audit repair).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### BUILD_ADAPTER_REGISTRY_LOCK_001

**Proves:** Rung 2 of the post-audit Claude-lane sequence. Establishes the adapter contract that real arbitrary-repo intake needs (monorepos, polyglot trees, custom test commands) without redesigning ShadowCompiler or moving the LLM-dependent paths. ShadowCompiler-vs-hive/compiler.py unification is reserved for PARALLEL_EXECUTION_LAYER_AUDIT_LOCK_001.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### CANONICAL_LOCAL_MODEL_ID_SELECTION_LOCK_001

**Proves:** Rung 1 of the real-model + build-adapter-verifier campaign (subordinate to Codex audit repair).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_40_FAMILY_EVIDENCE_FOOTHOLD_EXPANSION_LOCK_001

**Proves:** Establish or account for evidence footholds across the canonical 40-family board while separating real evidence artifacts and fixtures from classification, routing, documentation-only notes, blockers, and roadmap entries.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_44_FAMILY_EXACT_CELL_EXPANSION_PRESSURE_CLAUDE_REVIEW_001

**Proves:** Gulp Wave 005 Claude Lane T. 44-family taxonomy + 45-cell board target (25 user-visible + 10 install + 10 governance). Current 5 cells; gap = 40.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACRTDSK_CLAUDE_APPEND_ONLY_COUNT_DRIFT_ANTI_GOD_REVIEW_001

**Proves:** ACRTDSK Claude Lane AG. Append-only / count-drift / anti-god guards hold.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACRTDSK_CLAUDE_BROADER_REPO_SBOM_PACKET_READY_REVIEW_001

**Proves:** ACRTDSK Claude Lane P. Broader repo SBOM packet ready, NOT executed (separate spend required).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACRTDSK_CLAUDE_CLAIM_SCANNER_DAY1_OVERCLAIM_REVIEW_001

**Proves:** ACRTDSK Claude Lane AH. Claim scanner / Day-1 overclaim pass.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACRTDSK_CLAUDE_CLEAN_RUNNER_BLOCKER_HONESTLY_SHARPENED_REVIEW_001

**Proves:** ACRTDSK Claude Lane J. admitted_clean_runner_verified=FALSE; exact_blocker captured; no fake proof.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACRTDSK_CLAUDE_CLEAN_RUNNER_EXECUTION_REVIEW_001

**Proves:** ACRTDSK Claude Lane H. Clean-runner execution attempted; 6 commands logged.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACRTDSK_CLAUDE_CLEAN_RUNNER_ONE_TIME_SPEND_REVIEW_001

**Proves:** ACRTDSK Claude Lane G. Clean-runner one-time spend consumed (4→5); reuse rejected.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACRTDSK_CLAUDE_CLEAN_RUNNER_PACKET_VALIDATION_REVIEW_001

**Proves:** ACRTDSK Claude Lane E. ADMITTED_CLEAN_RUNNER packet validates; materially_distinct=true.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACRTDSK_CLAUDE_CLEAN_RUNNER_QUEUE_ADMISSION_REVIEW_001

**Proves:** ACRTDSK Claude Lane F. Clean-runner packet admitted to queue (4→5).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACRTDSK_CLAUDE_CLEAN_RUNNER_TRANSCRIPTS_REVIEW_001

**Proves:** ACRTDSK Claude Lane K. Execution transcript + post-execution verification transcript present.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACRTDSK_CLAUDE_C_STORAGE_INVENTORY_REVIEW_001

**Proves:** ACRTDSK Claude Lane B. C: storage inventory captured (10 large paths).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACRTDSK_CLAUDE_EVIDENCE_INDEX_CLEAN_REVIEW_001

**Proves:** ACRTDSK Claude Lane AF. Evidence index clean (1784 entries; Δ=+53).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACRTDSK_CLAUDE_FAMILY_CONVEYOR_BROWSER_TAURI_REVIEW_001

**Proves:** ACRTDSK Claude Lane T. Browser/Tauri packets ready; not executed.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACRTDSK_CLAUDE_FAMILY_CONVEYOR_HIGH_RISK_REVIEW_001

**Proves:** ACRTDSK Claude Lane U. ML/Mobile/Hardware/Kotlin/Swift sharpened with exact_blocker; none executed.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACRTDSK_CLAUDE_FAMILY_CONVEYOR_PHP_RUBY_REVIEW_001

**Proves:** ACRTDSK Claude Lane S. PHP/Ruby families sharpened to EXACT_FIXTURE_OR_TOOLCHAIN_GATE; no global install.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACRTDSK_CLAUDE_FORBIDDEN_ACTIONS_DIRTY_STATE_REVIEW_001

**Proves:** ACRTDSK Claude Lane AJ. 25 forbidden actions avoided; dirty_untracked_state empty.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACRTDSK_CLAUDE_FULL_STATUS_SEGMENTATION_REVIEW_001

**Proves:** ACRTDSK Claude Lane AE. Full-status segmentation plan recorded; no tests disabled/skipped/deleted.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACRTDSK_CLAUDE_GUI_BUILD_INSTALLER_BETA_NOT_EXECUTED_REVIEW_001

**Proves:** ACRTDSK Claude Lane AD. GUI/build / installer/release / beta not executed; ProgramBench/public upload/training rows absent.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACRTDSK_CLAUDE_KNOWN_WORLD_CAPABILITY_REGISTRY_REVIEW_001

**Proves:** ACRTDSK Claude Lane Q. Known-world registry LANDED: 18 categories, 267 entries; ACCOUNTING not support.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACRTDSK_CLAUDE_KNOWN_WORLD_DETECTOR_GAP_QUEUE_REVIEW_001

**Proves:** ACRTDSK Claude Lane R. Detector gap queue: 13 prioritized gaps with next-action per gap.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACRTDSK_CLAUDE_NO_C_PATH_MOVED_NO_DELETION_REVIEW_001

**Proves:** ACRTDSK Claude Lane D. No C: paths moved/deleted; runner+probe materialized on T: only.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACRTDSK_CLAUDE_NO_FAKE_CLEAN_RUNNER_PROOF_REVIEW_001

**Proves:** ACRTDSK Claude Lane L. clean_runner_release_ready_claimed=FALSE; runner context not inflated.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACRTDSK_CLAUDE_NO_FAMILY_PROMOTION_NO_OVERCLAIM_REVIEW_001

**Proves:** ACRTDSK Claude Lane V. 0 families executed; 0 promoted; LV count unchanged.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACRTDSK_CLAUDE_NO_RELEASE_READY_NO_BETA_CLAIM_REVIEW_001

**Proves:** ACRTDSK Claude Lane AC. No release-ready / beta-ready / installer-ready claim.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACRTDSK_CLAUDE_NO_SILENT_HASH_MISMATCH_ACCEPTANCE_REVIEW_001

**Proves:** ACRTDSK Claude Lane O. silent_hash_mismatch_accepted=FALSE; previous_sbom_truth_replaced=FALSE.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACRTDSK_CLAUDE_NO_TEST_VERIFIER_LOCKFILE_MUTATION_REVIEW_001

**Proves:** ACRTDSK Claude Lane AI. Test/verifier/oracle/compiler/binary + package/lockfile NOT mutated.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACRTDSK_CLAUDE_QUEUE_SPEND_CONSERVATION_REVIEW_001

**Proves:** ACRTDSK Claude Lane Y. Queue/spend conservation Δ=1/Δ=1 preserved.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACRTDSK_CLAUDE_RELEASE_CAMPAIGN_STAGING_REVIEW_001

**Proves:** ACRTDSK Claude Lane X. 4-checklist release campaign staging prepared; public_launch_executed=FALSE.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACRTDSK_CLAUDE_RELEASE_CELLS_CANONICAL_REVIEW_001

**Proves:** ACRTDSK Claude Lane Z. Release-supported exact cells canonical (10).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACRTDSK_CLAUDE_RELEASE_FAMILIES_CANONICAL_REVIEW_001

**Proves:** ACRTDSK Claude Lane AA. Release-supported families canonical (0).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACRTDSK_CLAUDE_REMAINING_NLV_FAMILIES_REVIEW_001

**Proves:** ACRTDSK Claude Lane W. 9 remaining NLV families with active next action.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACRTDSK_CLAUDE_RUNNER_CONTEXT_MATERIALLY_DISTINCT_REVIEW_001

**Proves:** ACRTDSK Claude Lane I. Runner context = ADMITTED_CLEAN_RUNNER on T:; not a local worktree.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACRTDSK_CLAUDE_SAFE_RELOCATION_PLAN_REVIEW_001

**Proves:** ACRTDSK Claude Lane C. Safe relocation plan with T:/DeterminexCleanRunner/DeterminexTemp categories.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACRTDSK_CLAUDE_SBOM_BYTE_EXACT_GITATTRIBUTES_REVIEW_001

**Proves:** ACRTDSK Claude Lane M. .gitattributes rule for assurance/sbom/*.json -text+eol-lf landed.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACRTDSK_CLAUDE_SBOM_MAIN_WORKTREE_HASH_STABLE_REVIEW_001

**Proves:** ACRTDSK Claude Lane N. SBOM main-worktree hash stable; matches marker exactly.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACRTDSK_CLAUDE_SCORE_MOVEMENT_ZERO_EVIDENCE_BOUND_REVIEW_001

**Proves:** ACRTDSK Claude Lane AB. Scores ALL unchanged; clean-runner blocker carried; score_delta_guard passed.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACRTDSK_CLAUDE_SYNTHESIS_REVIEW_001

**Proves:** ACRTDSK Claude Lane AK. Synthesis + final report.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACRTDSK_CLAUDE_T_DRIVE_DETECTION_WRITABILITY_REVIEW_001

**Proves:** ACRTDSK Claude Lane A. T: drive detected, writable, free-space recorded.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACTIVE_UNIVERSAL_FAMILY_BOUNDED_EXECUTION_LOCK_001

**Proves:** DETERMINEX_ACTIVE_UNIVERSAL_FAMILY_BOUNDED_EXECUTION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACTIVE_UNIVERSAL_FAMILY_CAPABILITY_PROMOTION_RULE_LOCK_001

**Proves:** DETERMINEX_ACTIVE_UNIVERSAL_FAMILY_CAPABILITY_PROMOTION_RULE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACTIVE_UNIVERSAL_FAMILY_CONVEYOR_SCHEMA_LOCK_001

**Proves:** DETERMINEX_ACTIVE_UNIVERSAL_FAMILY_CONVEYOR_SCHEMA_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACTIVE_UNIVERSAL_FAMILY_MARCH_PLAN_DASHBOARD_LOCK_001

**Proves:** DETERMINEX_ACTIVE_UNIVERSAL_FAMILY_MARCH_PLAN_DASHBOARD_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACTIVE_UNIVERSAL_FAMILY_PRIORITIZATION_LOCK_001

**Proves:** DETERMINEX_ACTIVE_UNIVERSAL_FAMILY_PRIORITIZATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACTIVE_UNIVERSAL_FAMILY_RECONCILIATION_LOCK_001

**Proves:** DETERMINEX_ACTIVE_UNIVERSAL_FAMILY_RECONCILIATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACTIVE_UNIVERSAL_FAMILY_REPAIR_DISCIPLINE_GUARD_LOCK_001

**Proves:** DETERMINEX_ACTIVE_UNIVERSAL_FAMILY_REPAIR_DISCIPLINE_GUARD_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACTIVE_UNIVERSAL_FAMILY_SBOM_NEXT_ACTION_PREP_LOCK_001

**Proves:** DETERMINEX_ACTIVE_UNIVERSAL_FAMILY_SBOM_NEXT_ACTION_PREP_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACTIVE_UNIVERSAL_FAMILY_SCORE_CANONICALIZATION_DECISION_LOCK_001

**Proves:** DETERMINEX_ACTIVE_UNIVERSAL_FAMILY_SCORE_CANONICALIZATION_DECISION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ACTIVE_UNIVERSAL_FAMILY_STATUS_UPDATE_LOCK_001

**Proves:** DETERMINEX_ACTIVE_UNIVERSAL_FAMILY_STATUS_UPDATE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ADMITTED_CLEAN_RUNNER_EXECUTION_LOCK_001

**Proves:** Admitted Clean-Runner Execution

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ADMITTED_CLEAN_RUNNER_PACKET_LOCK_001

**Proves:** Admitted Clean-Runner Packet

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ADMITTED_CLEAN_RUNNER_QUEUE_SPEND_LOCK_001

**Proves:** Admitted Clean-Runner Queue Spend

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ADMITTED_CLEAN_RUNNER_RECONCILIATION_LOCK_001

**Proves:** Admitted Clean-Runner Reconciliation

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ADMITTED_CLEAN_RUNNER_SAFE_CLONE_RETRY_LOCK_001

**Proves:** ADMITTED_CLEAN_RUNNER_SAFE_CLONE_RETRY_RECORDED for DETERMINEX_CLEAN_RUNNER_SAFE_CLONE_BROADER_SBOM_T_DRIVE_RELOCATION_AND_DETECTOR_EXPANSION_WAVE_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_AFR_CLAUDE_ACTIVE_CONVEYOR_SCHEMA_REVIEW_001

**Proves:** AFR Claude Lane E. Active conveyor schema exists with remediation fields.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_AFR_CLAUDE_BLOCKED_IS_ACCOUNTING_REVIEW_001

**Proves:** AFR Claude Lane O. Blocked treated as temporary accounting, not destination.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_AFR_CLAUDE_CAPABILITY_WITH_VERIFICATION_REVIEW_001

**Proves:** AFR Claude Lane V. Capability-with-verification rule in place.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_AFR_CLAUDE_EVERY_NONVERIFIED_NEXT_ACTION_REVIEW_001

**Proves:** AFR Claude Lane P. Every non-verified family has next action.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_AFR_CLAUDE_EVIDENCE_INDEX_GUARDS_REVIEW_001

**Proves:** AFR Claude Lane AD. Evidence index clean; guards hold.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_AFR_CLAUDE_FAMILIES_SELECTED_REVIEW_001

**Proves:** AFR Claude Lane I. Families selected for execution = 4 safe candidates.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_AFR_CLAUDE_FAMILY_COUNT_MAPPED_REVIEW_001

**Proves:** AFR Claude Lane F. Family count mapped = 31.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_AFR_CLAUDE_FAMILY_EXECUTION_VERDICTS_REVIEW_001

**Proves:** AFR Claude Lane J. Family execution verdicts = 4/4 verified.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_AFR_CLAUDE_FAMILY_PRIORITIZATION_REVIEW_001

**Proves:** AFR Claude Lane H. Family prioritization is evidence-based.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_AFR_CLAUDE_FAMILY_PROMOTIONS_REVIEW_001

**Proves:** AFR Claude Lane M. Family promotions are evidence-bound exact local capabilities.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_AFR_CLAUDE_FAMILY_REPAIR_VERDICTS_REVIEW_001

**Proves:** AFR Claude Lane K. Family repair verdicts = 0 needed (verification passed without repair).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_AFR_CLAUDE_FAMILY_STATUS_SUMMARY_REVIEW_001

**Proves:** AFR Claude Lane N. Family status before/after summary tracks correctly.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_AFR_CLAUDE_FAMILY_VERIFICATION_VERDICTS_REVIEW_001

**Proves:** AFR Claude Lane L. Family verification verdicts = 4 LOCAL_VERIFIED.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_AFR_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001

**Proves:** AFR Claude Lane AE. 17 forbidden actions avoided.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_AFR_CLAUDE_MARCH_PLAN_DASHBOARD_REVIEW_001

**Proves:** AFR Claude Lane AC. March-plan dashboard accurate, not release hype.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_AFR_CLAUDE_NO_BINARY_MUTATION_REVIEW_001

**Proves:** AFR Claude Lane T. Binaries not mutated.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_AFR_CLAUDE_NO_FAMILY_SUPPORT_REVIEW_001

**Proves:** AFR Claude Lane Y. No family-support claim from exact-cell verification.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_AFR_CLAUDE_NO_LADDER_INVERSION_REVIEW_001

**Proves:** AFR Claude Lane W. Ladder inversion blocked (mapped ≠ verified ≠ support ≠ release).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_AFR_CLAUDE_NO_LOCKFILE_MUTATION_REVIEW_001

**Proves:** AFR Claude Lane U. Package manifests/lockfiles not mutated without spend.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_AFR_CLAUDE_NO_TEST_MUTATION_REVIEW_001

**Proves:** AFR Claude Lane R. Tests not edited to hide failures.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_AFR_CLAUDE_NO_UNIVERSAL_SUPPORT_REVIEW_001

**Proves:** AFR Claude Lane X. No universal support overclaim.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_AFR_CLAUDE_NO_VERIFIER_MUTATION_REVIEW_001

**Proves:** AFR Claude Lane S. Verifiers/oracles not weakened.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_AFR_CLAUDE_OTHER_PACKETS_NOT_EXECUTED_REVIEW_001

**Proves:** AFR Claude Lane AA. Clean-host/GUI/installer/beta-dashboard not executed.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_AFR_CLAUDE_REACT_VITE_EVIDENCE_NOT_OVERSTATED_REVIEW_001

**Proves:** AFR Claude Lane C. React/Vite verification evidence not overstated.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_AFR_CLAUDE_RELEASE_INVARIANTS_REVIEW_001

**Proves:** AFR Claude Lane AB. Release cells (10) and families (0) canonical.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_AFR_CLAUDE_REMEDIATION_QUEUE_COUNT_REVIEW_001

**Proves:** AFR Claude Lane G. Remediation queue count documented (27).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_AFR_CLAUDE_REPAIR_DISCIPLINE_REVIEW_001

**Proves:** AFR Claude Lane Q. Repair discipline guard in place.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_AFR_CLAUDE_SBOM_NOT_EXECUTED_REVIEW_001

**Proves:** AFR Claude Lane Z. SBOM not executed; next-action prepared only.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_AFR_CLAUDE_SCORE_BEFORE_AFTER_REVIEW_001

**Proves:** AFR Claude Lane B. Score before/after evidence-bound.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_AFR_CLAUDE_SCORE_CANONICALIZATION_REVIEW_001

**Proves:** AFR Claude Lane A. Score canonicalization justified (React/Vite Tier-1 promotion).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_AFR_CLAUDE_SYNTHESIS_REVIEW_001

**Proves:** AFR Claude Lane AF. Synthesis + 57-item final report.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_AFR_CLAUDE_TIER1_STATUS_REVIEW_001

**Proves:** AFR Claude Lane D. Tier-1 status 9/10 local + 1/10 typed-blocked.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ALL_CURRENT_RELEASE_CELL_READERS_BIND_TO_REGISTRY_LOCK_001

**Proves:** All Current Readers Bind to Registry

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ALL_FAMILY_ADAPTER_STUB_COMPLETION_LOCK_001

**Proves:** DETERMINEX_ALL_FAMILY_ADAPTER_STUB_COMPLETION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ALL_GAP_CLOSURE_BATCH_002_LOCK

**Proves:** Bind Proof Center route and status-suite segmented runtime evidence into every all-gap row without false support promotion.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ALL_GAP_CLOSURE_BATCH_003_LOCK

**Proves:** Convert a meaningful Batch 003 all-gap subset from generic blockers to exact executable next locks without false promotion.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_APPEND_ONLY_EVIDENCE_LEDGER_LOCK_001

**Proves:** Create an append-only hash-chain evidence ledger snapshot over the evidence index manifests.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_APPROVAL_AUDIT_LOG_APPEND_ONLY_WRITER_LOCK_001

**Proves:** DETERMINEX_APPROVAL_AUDIT_LOG_APPEND_ONLY_WRITER_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_APPROVAL_PACKET_SIGNING_SIMULATION_DRY_RUN_LOCK_001

**Proves:** DETERMINEX_APPROVAL_PACKET_SIGNING_SIMULATION_DRY_RUN_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_APPROVAL_RESOLUTION_MATRIX_CLAUDE_REVIEW_001

**Proves:** Wave 007 Claude Lane Y. Approval resolution per packet (NSIS / msedgedriver / Syft / GUI launch / Idea Lab GUI / local package dry-run) with simulated-vs-signed classification and execution-from-simulated detector.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_APPROVAL_VALIDATOR_AT_EXECUTION_SITE_WIRING_LOCK_001

**Proves:** DETERMINEX_APPROVAL_VALIDATOR_AT_EXECUTION_SITE_WIRING_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_APP_CLASS_LANGUAGE_AND_WORKFLOW_SUPPORT_MATRIX_LOCK_001

**Proves:** Create a machine-readable support matrix separating greenfield creation, existing-repo repair, maintenance/update, learning, and proof/operator control support.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_APP_CREATION_BENCH_SEED_LOCK_001

**Proves:** Define claim-safe seed tasks for a future app creation benchmark.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ARCHITECTURE_REGRESSION_GAUNTLET_LOCK_001

**Proves:** Catch any regression in the 6-rung architecture sprint with one invocation: `python scripts/dev/architecture_regression_gauntlet.py --strict`. Runs in CI alongside the other quality gates.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ATASFC_CLAUDE_APPEND_ONLY_COUNT_DRIFT_GUARDS_REVIEW_001

**Proves:** ATASFC Claude Lane AG. Append-only and count-drift guards hold.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ATASFC_CLAUDE_AUTHORITY_REQUIRED_EXECUTION_SCOPED_REVIEW_001

**Proves:** ATASFC Claude Lane N. Authority-required execution scoped + authorized (none occurred this wave).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ATASFC_CLAUDE_BETA_DASHBOARD_NOT_PUBLISHED_REVIEW_001

**Proves:** ATASFC Claude Lane Y. Beta dashboard did not publish.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ATASFC_CLAUDE_CAPABILITY_PROMOTION_EVIDENCE_BOUND_REVIEW_001

**Proves:** ATASFC Claude Lane S. Capability promotions evidence-bound.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ATASFC_CLAUDE_CLAIM_SCANNER_DAY1_OVERCLAIM_REVIEW_001

**Proves:** ATASFC Claude Lane AH. Claim scanner and Day-1 overclaim scanner pass.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ATASFC_CLAUDE_CLEAN_HOST_NOT_EXECUTED_REVIEW_001

**Proves:** ATASFC Claude Lane V. Clean-host did not execute (packet ready next).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ATASFC_CLAUDE_DIRTY_UNTRACKED_STATE_REVIEW_001

**Proves:** ATASFC Claude Lane AI. Dirty/untracked state reported (empty).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ATASFC_CLAUDE_EVERY_REMAINING_FAMILY_ADVANCED_OR_SHARPENED_REVIEW_001

**Proves:** ATASFC Claude Lane L. Every remaining family was advanced or given sharper gate.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ATASFC_CLAUDE_EVIDENCE_INDEX_CLEAN_REVIEW_001

**Proves:** ATASFC Claude Lane AF. Evidence index clean (1640 entries).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ATASFC_CLAUDE_EXACT_LOCAL_NOT_FAMILY_SUPPORT_REVIEW_001

**Proves:** ATASFC Claude Lane T. Exact local capability NOT framed as family support.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ATASFC_CLAUDE_FAMILY_REPAIR_SCOPE_REVIEW_001

**Proves:** ATASFC Claude Lane P. Family repairs touched only Determinex-owned structure (0 repairs this wave).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ATASFC_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001

**Proves:** ATASFC Claude Lane AJ. 20 forbidden actions avoided.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ATASFC_CLAUDE_FULL_STATUS_TIMEOUT_REVIEW_001

**Proves:** ATASFC Claude Lane AE. Full-status timeout work did not disable/skip/delete tests.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ATASFC_CLAUDE_GUI_BUILD_NOT_EXECUTED_REVIEW_001

**Proves:** ATASFC Claude Lane W. GUI/build did not execute.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ATASFC_CLAUDE_INSTALLER_RELEASE_NOT_EXECUTED_REVIEW_001

**Proves:** ATASFC Claude Lane X. Installer/release did not execute.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ATASFC_CLAUDE_MARCH_PLAN_DASHBOARD_REVIEW_001

**Proves:** ATASFC Claude Lane AD. March-plan dashboard accurate and not release hype.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ATASFC_CLAUDE_MISSING_TOOLS_CONVERTED_TO_PACKETS_REVIEW_001

**Proves:** ATASFC Claude Lane B. Missing tools converted into packets instead of passive blockers.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ATASFC_CLAUDE_NO_FAKE_SBOM_REVIEW_001

**Proves:** ATASFC Claude Lane J. No fake SBOM produced (blocker=null because real generation succeeded).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ATASFC_CLAUDE_NO_TEST_MUTATION_REVIEW_001

**Proves:** ATASFC Claude Lane Q. Tests not edited to hide failures.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ATASFC_CLAUDE_NO_UNCONTROLLED_INSTALL_REVIEW_001

**Proves:** ATASFC Claude Lane D. No uncontrolled install occurred.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ATASFC_CLAUDE_NO_UNIVERSAL_SUPPORT_CLAIM_REVIEW_001

**Proves:** ATASFC Claude Lane U. Universal support not claimed.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ATASFC_CLAUDE_NO_VERIFIER_ORACLE_MUTATION_REVIEW_001

**Proves:** ATASFC Claude Lane R. Verifiers/oracles/compilers/binaries not weakened.

**Does not prove:** Does not prove broad real-world repair coverage beyond the locked acceptance tests.

#### DETERMINEX_ATASFC_CLAUDE_NPM_DEPENDENCY_REPAIR_REVIEW_001

**Proves:** ATASFC Claude Lane G. npm dependency repair narrow + authorized (NOT_SELECTED — lockfile mutation avoided).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ATASFC_CLAUDE_OPERATOR_TOOL_ACQUISITION_AUTHORIZATION_SCOPED_REVIEW_001

**Proves:** ATASFC Claude Lane A. Operator tool-acquisition authorization scoped, not blanket.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ATASFC_CLAUDE_PACKAGE_LOCKFILE_AUTHORITY_REVIEW_001

**Proves:** ATASFC Claude Lane H. Package/lockfile changes authorized if any (none occurred).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ATASFC_CLAUDE_RELEASE_CELLS_CANONICAL_REVIEW_001

**Proves:** ATASFC Claude Lane AA. Release-supported exact cells canonical (10).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ATASFC_CLAUDE_RELEASE_FAMILIES_CANONICAL_REVIEW_001

**Proves:** ATASFC Claude Lane AB. Release-supported families canonical (0).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ATASFC_CLAUDE_REPO_LOCAL_PATH_PREFERRED_REVIEW_001

**Proves:** ATASFC Claude Lane E. Repo-local/local-bin/tool-cache path preferred where possible.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ATASFC_CLAUDE_RUNTIME_QUEUE_SPEND_ACCURATE_REVIEW_001

**Proves:** ATASFC Claude Lane Z. Runtime queue/spend before/after accurate (2→3).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ATASFC_CLAUDE_SBOM_BLOCKER_NARROWER_REVIEW_001

**Proves:** ATASFC Claude Lane K. SBOM blocker, if any, narrower than before — N/A SBOM verified.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ATASFC_CLAUDE_SBOM_OUTPUT_EXISTS_HASHED_REVIEW_001

**Proves:** ATASFC Claude Lane I. SBOM output exists and is hashed (CycloneDX, 63 components, real hash).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ATASFC_CLAUDE_SCORE_MOVEMENT_EVIDENCE_BOUND_REVIEW_001

**Proves:** ATASFC Claude Lane AC. Score movement evidence-bound (packaging moved because SBOM verified).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ATASFC_CLAUDE_SYFT_ADMISSION_LEGITIMATE_REVIEW_001

**Proves:** ATASFC Claude Lane F. Syft (or equivalent) admission legitimate (packet+spend+repo-local).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ATASFC_CLAUDE_SYNTHESIS_REVIEW_001

**Proves:** ATASFC Claude Lane AK. Synthesis + 75-item final report.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ATASFC_CLAUDE_TOOLCHAIN_ACQUISITION_SCOPED_AUTHORIZED_REVIEW_001

**Proves:** ATASFC Claude Lane M. Toolchain acquisition, if any, was scoped + authorized.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ATASFC_CLAUDE_TOOL_ACQUISITION_QUEUE_SPEND_BEFORE_EXEC_REVIEW_001

**Proves:** ATASFC Claude Lane C. Tool acquisition used queue/spend before execution.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ATASFC_CLAUDE_UNKNOWN_NOVEL_NO_BROAD_CLAIM_REVIEW_001

**Proves:** ATASFC Claude Lane O. Unknown/novel fixture path did not claim broad unknown support.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_AUTHORITY_BATCH_EXECUTION_LOCK_001

**Proves:** DETERMINEX_AUTHORITY_BATCH_EXECUTION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_AUTHORIZED_TOOL_ACQUISITION_RECONCILIATION_LOCK_001

**Proves:** DETERMINEX_AUTHORIZED_TOOL_ACQUISITION_RECONCILIATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_AUTHORIZED_TOOL_DASHBOARD_MARCH_PLAN_LOCK_001

**Proves:** DETERMINEX_AUTHORIZED_TOOL_DASHBOARD_MARCH_PLAN_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_BRIDGE_CLAUDE_APPEND_ONLY_COUNT_DRIFT_REVIEW_001

**Proves:** Bridge Claude Lane V. Append-only and count-drift guards hold.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_BRIDGE_CLAUDE_BETA_DASHBOARD_NO_PUBLISH_REVIEW_001

**Proves:** Bridge Claude Lane S. Beta dashboard did not publish publicly.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_BRIDGE_CLAUDE_BRIDGE_REJECTION_CORPUS_REVIEW_001

**Proves:** Bridge Claude Lane D. Bridge-specific rejection corpus covers attacks: hash-change/wrong-commit/reuse/etc.

**Does not prove:** Does not prove corpus balance, training effectiveness, or public benchmark dominance by itself.

#### DETERMINEX_BRIDGE_CLAUDE_CLAIM_SCANNER_OVERCLAIM_REVIEW_001

**Proves:** Bridge Claude Lane W. Claim scanner + Day 1 overclaim scanner pass.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_BRIDGE_CLAUDE_CLEAN_HOST_NO_SEPARATE_SPEND_REVIEW_001

**Proves:** Bridge Claude Lane P. Clean-host did not run; no separate spend.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_BRIDGE_CLAUDE_COMMAND_MATCHES_APPROVED_REVIEW_001

**Proves:** Bridge Claude Lane L. Actual commands match approved packet commands.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_BRIDGE_CLAUDE_DIRTY_STATE_REPORTED_REVIEW_001

**Proves:** Bridge Claude Lane AA. Dirty/untracked state reported.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_BRIDGE_CLAUDE_EVIDENCE_INDEX_CLEAN_REVIEW_001

**Proves:** Bridge Claude Lane U. Evidence index clean at 1382 entries.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_BRIDGE_CLAUDE_EXACTLY_ONE_ADMITTED_FIRST_REVIEW_001

**Proves:** Bridge Claude Lane E. Exactly one packet admitted first.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_BRIDGE_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001

**Proves:** Bridge Claude Lane AB. All forbidden actions audited and avoided.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_BRIDGE_CLAUDE_GUI_BUILD_NO_SEPARATE_SPEND_REVIEW_001

**Proves:** Bridge Claude Lane Q. GUI/build did not run; no separate spend.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_BRIDGE_CLAUDE_INSTALLER_RELEASE_NO_SEPARATE_SPEND_REVIEW_001

**Proves:** Bridge Claude Lane R. Installer/release did not run; PREREQS_BLOCKED.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_BRIDGE_CLAUDE_NO_FORBIDDEN_PROTECTED_ACTION_REVIEW_001

**Proves:** Bridge Claude Lane M. No forbidden protected action ran.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_BRIDGE_CLAUDE_OARG_PACKET_DISCOVERY_REVIEW_001

**Proves:** Bridge Claude Lane A. OARG packets discovered correctly (6 packets from prior wave).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_BRIDGE_CLAUDE_OTHER_PACKETS_NOT_EXECUTED_REVIEW_001

**Proves:** Bridge Claude Lane N. Other five packets NOT executed.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_BRIDGE_CLAUDE_PACKET_HASH_VERIFICATION_REVIEW_001

**Proves:** Bridge Claude Lane B. Packet hashes verified.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_BRIDGE_CLAUDE_QUEUE_BEFORE_AFTER_REVIEW_001

**Proves:** Bridge Claude Lane G. Queue before=0 after=1 (first-ever admission).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_BRIDGE_CLAUDE_REACT_VITE_FIRST_TARGETED_REVIEW_001

**Proves:** Bridge Claude Lane F. React/Vite was the first packet targeted (per prompt).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_BRIDGE_CLAUDE_REACT_VITE_IN_SCOPE_REVIEW_001

**Proves:** Bridge Claude Lane K. React/Vite execution stayed inside approved scope.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_BRIDGE_CLAUDE_RELEASE_CELLS_CANONICAL_REVIEW_001

**Proves:** Bridge Claude Lane X. Release-supported exact cells canonical (10).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_BRIDGE_CLAUDE_RELEASE_FAMILIES_CANONICAL_REVIEW_001

**Proves:** Bridge Claude Lane Y. Release-supported families canonical (0).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_BRIDGE_CLAUDE_RUNTIME_QUEUE_BRIDGE_REVIEW_001

**Proves:** Bridge Claude Lane C. Runtime queue bridge does not admit invalid packets.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_BRIDGE_CLAUDE_SBOM_NO_SEPARATE_SPEND_REVIEW_001

**Proves:** Bridge Claude Lane O. SBOM did not run; no separate spend.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_BRIDGE_CLAUDE_SCORES_EVIDENCE_BOUND_REVIEW_001

**Proves:** Bridge Claude Lane Z. Scores unchanged; movement explicitly rejected (admission ≠ local-verified support).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_BRIDGE_CLAUDE_SPEND_BEFORE_AFTER_REVIEW_001

**Proves:** Bridge Claude Lane H. Spend before=0 after=1 (first-ever spend).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_BRIDGE_CLAUDE_SPEND_ONE_ENTRY_CONSUMED_REVIEW_001

**Proves:** Bridge Claude Lane I. Spend consumed exactly one queue entry.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_BRIDGE_CLAUDE_SPEND_REUSE_REJECTED_REVIEW_001

**Proves:** Bridge Claude Lane J. Spend reuse is rejected by tests.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_BRIDGE_CLAUDE_SYNTHESIS_REVIEW_001

**Proves:** Bridge Claude Lane AC. Synthesis + 45-item final report.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_BRIDGE_CLAUDE_TIMEOUT_NOT_HIDDEN_REVIEW_001

**Proves:** Bridge Claude Lane T. Full-status timeout repair did not disable/skip/delete tests.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_BROADER_REPO_SBOM_AUTHORITY_GUARD_LOCK_001

**Proves:** Broader Repo SBOM Authority Guard

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_BROADER_REPO_SBOM_EXECUTION_LOCK_001

**Proves:** BROADER_REPO_SBOM_EXECUTION_RECORDED for DETERMINEX_CLEAN_RUNNER_SAFE_CLONE_BROADER_SBOM_T_DRIVE_RELOCATION_AND_DETECTOR_EXPANSION_WAVE_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_BROADER_REPO_SBOM_PACKET_LOCK_001

**Proves:** Broader Repo SBOM Packet

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_BROWSER_EXTENSION_AUTHORITY_GATE_LOCK_001

**Proves:** Browser Extension Authority Gate

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_BROWSER_TAURI_HARNESS_PACKET_STAGING_LOCK_001

**Proves:** BROWSER_TAURI_HARNESS_PACKETS_STAGED for DETERMINEX_CLEAN_RUNNER_SAFE_CLONE_BROADER_SBOM_T_DRIVE_RELOCATION_AND_DETECTOR_EXPANSION_WAVE_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_BUILD_TEST_SMOKE_LADDER_EXPANSION_LOCK_001

**Proves:** DETERMINEX_BUILD_TEST_SMOKE_LADDER_EXPANSION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CANONICAL_CELLS_FAKE_TRANSCRIPT_REJECTION_COVERAGE_LOCK_001

**Proves:** Fake Transcript Rejection Coverage for Canonical Cells

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CANONICAL_CELL_PROOF_REPORT_ANCHOR_BACKFILL_LOCK_001

**Proves:** Proof-Report Anchors for 10 Canonical Cells

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CANONICAL_FAMILY_REGISTRY_ALIAS_RECONCILIATION_LOCK_001

**Proves:** DETERMINEX_CANONICAL_FAMILY_REGISTRY_ALIAS_RECONCILIATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CANONICAL_RELEASE_SUPPORTED_CELLS_SINGLE_SOURCE_LOCK_001

**Proves:** Canonical Release Cell Single Source

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CANONICAL_TAXONOMY_EXPANSION_40_TO_44_LOCK_001

**Proves:** Preserve the canonical 40 launch taxonomy and add four tracked v2 families without support overclaim.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CANONICAL_TAXONOMY_EXPANSION_AND_MISSING_LANES_CLAUDE_REVIEW_001

**Proves:** Gulp Wave 004 Claude Lane T. Canonical taxonomy expansion + missing lanes. Recommends adding 4 high-priority families (model training, compiler/DSL, CMS plugins, media) -> 44. Names 11 missing lanes with owners. Catch-all sector usage is doing too much work.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CAPABILITY_SCORE_DELTA_GUARD_LOCK_001

**Proves:** Capability Score Delta Guard

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CAPABILITY_SUPPORT_MATRIX_EXPANSION_SPRINT_LOCK_001

**Proves:** Expand capability/support matrix and route next proof-bearing locks.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CAPABILITY_UNIVERSE_EXHAUSTIVE_MATRIX_LOCK_001

**Proves:** DETERMINEX_CAPABILITY_UNIVERSE_EXHAUSTIVE_MATRIX_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CATHEDRAL_INDEX_FOUNDATION_LOCK_001

**Proves:** Create the machine-readable Cathedral Index foundation for surfaces, app classes, languages, platforms, workflows, oracles, claims, support states, cost/setup, release gates, and Universal 100 routing.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CHRFSF_CLAUDE_APPEND_ONLY_COUNT_DRIFT_ANTI_GOD_REVIEW_001

**Proves:** CHRFSF Claude Lane AG. Append-only / count-drift / anti-god guards hold.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CHRFSF_CLAUDE_AUTHORITY_BATCH_GATE_REVIEW_001

**Proves:** CHRFSF Claude Lane T. 5 AR families sharpened with exact blockers; none executed.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CHRFSF_CLAUDE_CLAIM_SCANNER_DAY1_OVERCLAIM_REVIEW_001

**Proves:** CHRFSF Claude Lane AH. Claim scanner / Day-1 overclaim pass.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CHRFSF_CLAUDE_CLEAN_HOST_BLOCKER_SHARPENED_HONEST_REVIEW_001

**Proves:** CHRFSF Claude Lane G. Clean-host blocker honestly sharpened (LOCAL_CLEAN_WORKTREE_NOT_CLEAN_HOST); no fake proof.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CHRFSF_CLAUDE_CLEAN_HOST_DEPENDENCY_CHECKS_REVIEW_001

**Proves:** CHRFSF Claude Lane F. Dependency checks captured.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CHRFSF_CLAUDE_CLEAN_HOST_ENVIRONMENT_FINGERPRINT_REVIEW_001

**Proves:** CHRFSF Claude Lane E. Environment fingerprint captured.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CHRFSF_CLAUDE_CLEAN_HOST_EXECUTION_TRANSCRIPT_REVIEW_001

**Proves:** CHRFSF Claude Lane D. Clean-host execution transcript present; commands logged.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CHRFSF_CLAUDE_CLEAN_HOST_ONE_TIME_SPEND_REVIEW_001

**Proves:** CHRFSF Claude Lane C. Clean-host one-time spend consumed (3→4); reuse rejected.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CHRFSF_CLAUDE_CLEAN_HOST_PACKET_REPAIR_REVIEW_001

**Proves:** CHRFSF Claude Lane A. Clean-host packet repaired/validated + admitted.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CHRFSF_CLAUDE_CLEAN_HOST_QUEUE_ADMISSION_REVIEW_001

**Proves:** CHRFSF Claude Lane B. Clean-host packet admitted into queue (3→4).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CHRFSF_CLAUDE_CLEAN_HOST_RELEASE_PROOF_NOT_CLAIMED_REVIEW_001

**Proves:** CHRFSF Claude Lane H. Clean-host release proof NOT claimed from local worktree (claim boundary held).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CHRFSF_CLAUDE_EVERY_NONLV_ADVANCED_OR_SHARPENED_REVIEW_001

**Proves:** CHRFSF Claude Lane W. Every remaining non-LV family advanced or sharpened.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CHRFSF_CLAUDE_EVIDENCE_INDEX_CLEAN_REVIEW_001

**Proves:** CHRFSF Claude Lane AF. Evidence index clean (1731 entries; Δ=+91).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CHRFSF_CLAUDE_FAMILY_MAP_COVERAGE_REVIEW_001

**Proves:** CHRFSF Claude Lane X. Family map covers 31/31; conservation OK.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CHRFSF_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001

**Proves:** CHRFSF Claude Lane AI. 21 forbidden actions avoided.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CHRFSF_CLAUDE_FULL_STATUS_SEGMENTED_REVIEW_001

**Proves:** CHRFSF Claude Lane AE. Full-status segmentation plan recorded; no tests disabled/skipped/deleted.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CHRFSF_CLAUDE_GUI_BUILD_INSTALLER_BETA_NOT_EXECUTED_REVIEW_001

**Proves:** CHRFSF Claude Lane AD. GUI/build / installer/release / beta not executed.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CHRFSF_CLAUDE_KOTLIN_SWIFT_GATE_REVIEW_001

**Proves:** CHRFSF Claude Lane R. Kotlin/Swift TM → EXACT_TOOLCHAIN_GATE_REQUIRED (no global install attempted).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CHRFSF_CLAUDE_NO_FAMILY_PROMOTION_NO_SUPPORT_OVERCLAIM_REVIEW_001

**Proves:** CHRFSF Claude Lane U. 0 family promotions; no exact-local-as-family-support overclaim.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CHRFSF_CLAUDE_NO_PACKAGE_LOCKFILE_MUTATION_REVIEW_001

**Proves:** CHRFSF Claude Lane L. No package/lockfile mutation.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CHRFSF_CLAUDE_NO_RELEASE_READY_CLAIM_REVIEW_001

**Proves:** CHRFSF Claude Lane AC. No release-ready / beta-ready / installer-ready claim.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CHRFSF_CLAUDE_NO_TEST_OR_VERIFIER_MUTATION_REVIEW_001

**Proves:** CHRFSF Claude Lane M. No test/verifier/oracle/compiler/binary mutation.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CHRFSF_CLAUDE_NO_UNCONTROLLED_INSTALL_REVIEW_001

**Proves:** CHRFSF Claude Lane K. No uncontrolled global install during clean-host or family gates.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CHRFSF_CLAUDE_NO_UNIVERSAL_SUPPORT_CLAIM_REVIEW_001

**Proves:** CHRFSF Claude Lane V. No universal support claim.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CHRFSF_CLAUDE_PHP_RUBY_GATE_REVIEW_001

**Proves:** CHRFSF Claude Lane S. PHP/Ruby gate recorded; no install.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CHRFSF_CLAUDE_POST_EXECUTION_VERIFICATION_REVIEW_001

**Proves:** CHRFSF Claude Lane I. Post-execution verification artifact present.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CHRFSF_CLAUDE_QUEUE_SPEND_CONSERVATION_REVIEW_001

**Proves:** CHRFSF Claude Lane J. Queue/spend conservation (Δqueue=1, Δspend=1) preserved.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CHRFSF_CLAUDE_RELEASE_CELLS_CANONICAL_REVIEW_001

**Proves:** CHRFSF Claude Lane Z. Release-supported exact cells canonical (10).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CHRFSF_CLAUDE_RELEASE_FAMILIES_CANONICAL_REVIEW_001

**Proves:** CHRFSF Claude Lane AA. Release-supported families canonical (0).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CHRFSF_CLAUDE_RUNTIME_QUEUE_SPEND_ACCURATE_REVIEW_001

**Proves:** CHRFSF Claude Lane Y. Runtime queue/spend ledger accurate (rows 4/71).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CHRFSF_CLAUDE_SBOM_BROADER_REPO_NEXT_GATE_REVIEW_001

**Proves:** CHRFSF Claude Lane P. Broader repo SBOM packet ready, NOT executed (separate spend required).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CHRFSF_CLAUDE_SBOM_CONTINUITY_INNER_WORKTREE_CRLF_REVIEW_001

**Proves:** CHRFSF Claude Lane O. Inner-worktree SBOM hash differed (CRLF artifact); honestly noted, not silently accepted.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CHRFSF_CLAUDE_SBOM_CONTINUITY_MAIN_WORKTREE_REVIEW_001

**Proves:** CHRFSF Claude Lane N. SBOM main-worktree hash stable; on-disk SHA256 matches marker.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CHRFSF_CLAUDE_SCORE_MOVEMENT_ZERO_EVIDENCE_BOUND_REVIEW_001

**Proves:** CHRFSF Claude Lane AB. Scores ALL unchanged (no canonical movement; score_delta_guard passed).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CHRFSF_CLAUDE_STRUCTURAL_FAMILY_GATE_REVIEW_001

**Proves:** CHRFSF Claude Lane Q. STRUCTURALLY_MAPPED php/ruby converted to EXACT_FIXTURE_OR_TOOLCHAIN_GATE (no support claim).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CHRFSF_CLAUDE_SYNTHESIS_REVIEW_001

**Proves:** CHRFSF Claude Lane AJ. Synthesis + final report.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_DETERMINEX_CLI_FIRST_LOCAL_INSTALL_AND_COMMAND_LOCK_001

**Proves:** DETERMINEX_DETERMINEX_CLI_FIRST_LOCAL_INSTALL_AND_COMMAND_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_DETERMINEX_CLI_LOCAL_INSTALL_MOMENT_LOCK_001

**Proves:** DETERMINEX_DETERMINEX_CLI_LOCAL_INSTALL_MOMENT_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_DETERMINEX_CLI_PYPI_FEASIBILITY_AND_PACKAGE_SCAFFOLD_LOCK_001

**Proves:** DETERMINEX_DETERMINEX_CLI_PYPI_FEASIBILITY_AND_PACKAGE_SCAFFOLD_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_DETERMINEX_CLI_SUBPACKAGE_FEASIBILITY_CLAUDE_REVIEW_001

**Proves:** Overnight Lane 10. determinex-cli PyPI feasibility. FEASIBLE in 2-3 weeks; not started.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_DETERMINEX_CLOAK_FIRST_LOCAL_INSTALL_AND_FIXTURE_LOCK_001

**Proves:** DETERMINEX_DETERMINEX_CLOAK_FIRST_LOCAL_INSTALL_AND_FIXTURE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_DETERMINEX_CLOAK_LOCAL_INSTALL_AND_FIXTURE_LOCK_001

**Proves:** DETERMINEX_DETERMINEX_CLOAK_LOCAL_INSTALL_AND_FIXTURE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_DETERMINEX_CLOAK_SUBPACKAGE_FEASIBILITY_AND_SCAFFOLD_LOCK_001

**Proves:** DETERMINEX_DETERMINEX_CLOAK_SUBPACKAGE_FEASIBILITY_AND_SCAFFOLD_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_DETERMINEX_CLOAK_SUBPACKAGE_FEASIBILITY_CLAUDE_REVIEW_001

**Proves:** Overnight Lane 11. determinex-cloak feasibility. 3-4 weeks; high claim risk.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_DETERMINEX_PROOF_REPORT_SUBPACKAGE_FEASIBILITY_CLAUDE_REVIEW_001

**Proves:** Overnight Lane 12. determinex-proof-report PyPI feasibility. 3-4 weeks; sanitization + integrity required.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLAIM_SCANNER_CI_EXPANSION_LOCK_001

**Proves:** Claim Scanner CI Expansion

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLASSIFIER_STATE_SAFETY_AND_PROBE_TRANSCRIPTS_LOCK_001

**Proves:** Classifier State Safety and Probe Transcripts

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLEAN_HOST_ANTI_GOD_GUARD_EXPECTED_PASS_LOCK_001

**Proves:** Clean-Host Anti-God Guard Expected Pass

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLEAN_HOST_APPEND_ONLY_LEDGER_EXPECTED_PASS_GUARD_LOCK_001

**Proves:** Clean-Host Append-Only Ledger Expected Pass Guard

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLEAN_HOST_AUDIT_LOG_ENTRY_GUARD_LOCK_001

**Proves:** Clean-Host Audit Log Entry Guard

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLEAN_HOST_BETA_READINESS_BOUNDARY_GUARD_LOCK_001

**Proves:** Clean-Host Beta Readiness Boundary Guard

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLEAN_HOST_CLAIM_SCANNER_EXPECTED_PASS_GUARD_LOCK_001

**Proves:** Clean-Host Claim Scanner Expected Pass Guard

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLEAN_HOST_COUNT_DRIFT_EXPECTED_PASS_GUARD_LOCK_001

**Proves:** Clean-Host Count Drift Expected Pass Guard

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLEAN_HOST_DAY1_OVERCLAIM_EXPECTED_PASS_GUARD_LOCK_001

**Proves:** Clean-Host Day-1 Overclaim Expected Pass Guard

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLEAN_HOST_DEPENDENCY_CHECKS_GUARD_LOCK_001

**Proves:** Clean-Host Dependency Checks Guard

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLEAN_HOST_FAMILY_SUPPORT_BOUNDARY_GUARD_LOCK_001

**Proves:** Clean-Host Family Support Boundary Guard

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLEAN_HOST_FRESH_INSTALL_RUNNER_EXECUTION_LOCK_001

**Proves:** DETERMINEX_CLEAN_HOST_FRESH_INSTALL_RUNNER_EXECUTION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLEAN_HOST_MUTATION_BOUNDARY_GUARD_LOCK_001

**Proves:** Clean-Host Mutation Boundary Guard

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLEAN_HOST_NEXT_GATE_ESCALATION_LOCK_001

**Proves:** DETERMINEX_CLEAN_HOST_NEXT_GATE_ESCALATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLEAN_HOST_PACKET_FIELDS_GUARD_LOCK_001

**Proves:** Clean-Host Packet Fields Guard

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLEAN_HOST_PACKET_HARDENING_LOCK_001

**Proves:** DETERMINEX_CLEAN_HOST_PACKET_HARDENING_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLEAN_HOST_PACKET_TARGET_COMMIT_GUARD_LOCK_001

**Proves:** Clean-Host Packet Target Commit Guard

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLEAN_HOST_QUEUE_CONSERVATION_GUARD_LOCK_001

**Proves:** Clean-Host Queue Conservation Guard

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLEAN_HOST_RELEASE_READINESS_BOUNDARY_GUARD_LOCK_001

**Proves:** Clean-Host Release Readiness Boundary Guard

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLEAN_HOST_RELEASE_REGISTRY_INVARIANT_GUARD_LOCK_001

**Proves:** Clean-Host Release Registry Invariant Guard

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLEAN_HOST_REPO_STATUS_GUARD_LOCK_001

**Proves:** Clean-Host Repo Status Guard

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLEAN_HOST_ROUTE_SELECTION_AND_FIRST_EXECUTION_LOCK_001

**Proves:** DETERMINEX_CLEAN_HOST_ROUTE_SELECTION_AND_FIRST_EXECUTION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLEAN_HOST_RUNNER_ADMISSION_AND_EXECUTION_LOCK_003

**Proves:** Clean-Host Runner Admission and First Transcript

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLEAN_HOST_RUNNER_ADMISSION_AND_FIRST_TRANSCRIPT_LOCK_004

**Proves:** Clean-Host Runner Admission and First Transcript

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLEAN_HOST_RUNNER_DECISION_AND_FIRST_TRANSCRIPT_LOCK_001

**Proves:** DETERMINEX_CLEAN_HOST_RUNNER_DECISION_AND_FIRST_TRANSCRIPT_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLEAN_HOST_RUNNER_IF_ADMITTED_LOCK_005

**Proves:** Clean-Host Runner If Admitted

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLEAN_HOST_RUNTIME_EXECUTION_LOCK_001

**Proves:** Clean-Host Runtime Execution

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLEAN_HOST_RUNTIME_PACKET_FINALIZATION_LOCK_001

**Proves:** Clean-Host Runtime Packet Finalization

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLEAN_HOST_RUNTIME_QUEUE_ADMISSION_LOCK_001

**Proves:** Clean-Host Runtime Queue Admission

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLEAN_HOST_RUNTIME_SCORE_RELEASE_DISCIPLINE_LOCK_001

**Proves:** Clean-Host Runtime Score and Release Discipline

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLEAN_HOST_RUNTIME_SIGNED_SPEND_LOCK_001

**Proves:** Clean-Host Runtime Signed Spend

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLEAN_HOST_RUNTIME_SURGE_RECONCILIATION_LOCK_001

**Proves:** Clean-Host Runtime Surge Reconciliation

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLEAN_HOST_RUNTIME_VERIFICATION_LOCK_001

**Proves:** Clean-Host Runtime Verification

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLEAN_HOST_SBOM_CONTINUITY_GUARD_LOCK_001

**Proves:** Clean-Host SBOM Continuity Guard

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLEAN_HOST_SPEND_CONSERVATION_GUARD_LOCK_001

**Proves:** Clean-Host Spend Conservation Guard

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLEAN_HOST_SPEND_REUSE_REJECTION_GUARD_LOCK_001

**Proves:** Clean-Host Spend Reuse Rejection Guard

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLEAN_HOST_TRANSCRIPT_ENVIRONMENT_GUARD_LOCK_001

**Proves:** Clean-Host Transcript Environment Guard

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLEAN_HOST_UNIVERSAL_SUPPORT_BOUNDARY_GUARD_LOCK_001

**Proves:** Clean-Host Universal Support Boundary Guard

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLEAN_RUNNER_ADMISSION_AND_FIRST_TRANSCRIPT_LOCK_001

**Proves:** DETERMINEX_CLEAN_RUNNER_ADMISSION_AND_FIRST_TRANSCRIPT_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLEAN_RUNNER_SAFE_CLONE_GIT_DIAGNOSIS_LOCK_001

**Proves:** CLEAN_RUNNER_GIT_BLOCKER_DIAGNOSED for DETERMINEX_CLEAN_RUNNER_SAFE_CLONE_BROADER_SBOM_T_DRIVE_RELOCATION_AND_DETECTOR_EXPANSION_WAVE_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLEAN_RUNNER_SAFE_CLONE_RECONCILIATION_LOCK_001

**Proves:** CLEAN_RUNNER_SAFE_CLONE_WAVE_RECONCILED for DETERMINEX_CLEAN_RUNNER_SAFE_CLONE_BROADER_SBOM_T_DRIVE_RELOCATION_AND_DETECTOR_EXPANSION_WAVE_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLI_LOCK_001

**Proves:** DETERMINEX_CLI_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLOAK_CRYPTO_PROOF_AND_LEAK_REVIEW_LOCK_001

**Proves:** DETERMINEX_CLOAK_CRYPTO_PROOF_AND_LEAK_REVIEW_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLOAK_DEMO_PANEL_AND_THREE_FIXTURES_LOCK_001

**Proves:** DETERMINEX_CLOAK_DEMO_PANEL_AND_THREE_FIXTURES_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLOAK_DEMO_PANEL_PRIVACY_PROOF_CLAUDE_REVIEW_001

**Proves:** Overnight Lane 7. Cloak demo panel + privacy proof. 5/13 covered; 8 missing.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLOAK_DEMO_PANEL_VISUAL_COMPONENT_PROOF_LOCK_001

**Proves:** DETERMINEX_CLOAK_DEMO_PANEL_VISUAL_COMPONENT_PROOF_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLOAK_HASH_CHAIN_AND_LEAK_AUDIT_LOCK_001

**Proves:** DETERMINEX_CLOAK_HASH_CHAIN_AND_LEAK_AUDIT_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLOAK_PANEL_PRIVACY_BOUNDARY_CLAUDE_REVIEW_001

**Proves:** Wave 007 Claude Lane C. CloakDemoPanel component proof, Python/Rust/TS fixtures, obfuscate/restore evidence, privacy boundary, raw-source export gate, cloud-boundary wording, side channels, NL leak, subpackage relation.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLOAK_PRIVACY_DEMO_POST_CERTIFICATION_CLAUDE_REVIEW_001

**Proves:** Wave 006 Lane C. Cloak post-cert review. 4 of 12 inventory items covered; 8 missing including panel + 3 fixtures + cryptographic proof artifact + subpackage.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLOAK_PRODUCTIZATION_AND_PRIVACY_CLAIM_CLAUDE_REVIEW_001

**Proves:** Gulp Wave 005 Claude Lane C. Cloak productization + privacy claim review. 10 evidence items mapped; 8 privacy layers; 10 Codex locks queued. Real moat with no user-facing proof path.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLOAK_USER_FACING_PROOF_PATH_AND_DEMO_CELL_LOCK_001

**Proves:** Certify an exact synthetic Cloak user-facing proof demo cell without broad privacy or repo claims.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CODEX_COMMITS_BEFORE_CLAUDE_REVIEW_PROTOCOL_LOCK_001

**Proves:** DETERMINEX_CODEX_COMMITS_BEFORE_CLAUDE_REVIEW_PROTOCOL_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CODEX_STATUS_SUBPROCESS_CLASSIFICATION_REPAIR_PLAN_LOCK_001

**Proves:** Classify the two deferred Codex-lane subprocess.run sites under scripts/status without loosening helper execution policy.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CODE_SIGNING_ROUTE_AND_INSTALLER_WORDING_LINTER_LOCK_001

**Proves:** DETERMINEX_CODE_SIGNING_ROUTE_AND_INSTALLER_WORDING_LINTER_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CODE_SIGNING_SMARTSCREEN_PUBLIC_INSTALLER_TRUST_BOARD_LOCK_001

**Proves:** DETERMINEX_CODE_SIGNING_SMARTSCREEN_PUBLIC_INSTALLER_TRUST_BOARD_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_COMMERCIAL_LICENSE_TRIGGER_LOCK_001

**Proves:** Define Determinex's commercial-use trigger model and public license-boundary disclosure without claiming final legal terms, enforcement, payment, enterprise deployment, release readiness, production readiness, source mutation authority, training eligibility, broad claims, or universal support.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_COMPANION_RAG_ANSWER_BOUNDARY_AND_OBSERVABILITY_LOCK_001

**Proves:** Prove Companion RAG cite-or-refuse answer boundary and retrieval trace observability without answer-correctness or release claims.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_COMPANION_RAG_DESKTOP_E2E_BLOCKER_AND_OPERATOR_ROUTE_LOCK_001

**Proves:** Convert Companion RAG desktop GUI e2e blocker into actionable operator and harness routes.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_COMPANION_RAG_DESKTOP_E2E_SMOKE_LOCK_001

**Proves:** Bounded Companion RAG desktop command-boundary smoke through the project-local Tauri route.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_COMPANION_RAG_FIXTURE_EXPANSION_AND_PRODUCT_GATE_LOCK_001

**Proves:** Expand Companion RAG cite/refuse fixtures and product gate without claiming answer correctness or readiness.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_COMPANION_RAG_NON_GUI_REPORT_CELL_APPROVAL_AND_CERTIFICATION_LOCK_001

**Proves:** Approve and certify the exact Companion RAG non-GUI citation report/export cell without product-readiness or answer-correctness claims.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_COMPANION_RAG_PRODUCTIZATION_AND_ANSWER_CORRECTNESS_BOUNDARY_CLAUDE_REVIEW_001

**Proves:** Gulp Wave 004 Claude Lane R. Companion RAG productization + answer correctness boundary. Reviews 5-layer product surface; fixture expansion thresholds (50/200/500); non-GUI cell classification = internal_observability_only; training boundary; sanitization.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_COMPANION_RAG_PRODUCT_CELL_PREREQUISITE_GATE_LOCK_001

**Proves:** Classify Companion RAG product-cell prerequisites and select whether a separate non-GUI RAG report cell can proceed toward exact-cell certification.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_COMPANION_RAG_PRODUCT_SMOKE_LOCK_001

**Proves:** Prove bounded Companion RAG product-surface query/rendering without claiming answer quality or release support.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_COMPANION_RAG_REPORT_EXPORT_WITH_CITATIONS_LOCK_001

**Proves:** Export Companion RAG known-good citation reports and known-bad refusal reports as bounded proof artifacts without answer-correctness, product-readiness, or release-support claims.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_COMPANION_RAG_REPORT_PANEL_VISUAL_COMPONENT_PROOF_LOCK_001

**Proves:** DETERMINEX_COMPANION_RAG_REPORT_PANEL_VISUAL_COMPONENT_PROOF_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_COMPANION_RAG_SIGNED_USER_FACING_EXPORT_PROOF_LOCK_001

**Proves:** DETERMINEX_COMPANION_RAG_SIGNED_USER_FACING_EXPORT_PROOF_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_COMPANION_RAG_UI_ANSWER_OBSERVABILITY_BINDING_LOCK_001

**Proves:** Bind Companion RAG answer text, retrieved source IDs, citations, refusals, retrieval trace, and boundaries into a bounded user-visible report surface.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_COMPANION_RAG_UI_BINDING_LOCK_001

**Proves:** Bind local companion RAG retrieval into the Knowledge Base panel without claiming answer quality.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_COMPANION_SEEDER_RESOURCE_PATH_ALIGNMENT_LOCK_001

**Proves:** Align companion seeder docs/app-data paths and prove local vector seeding of companion docs.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_COMPILER_LOOP_WAL_ATTEMPT_TRACE_RENDER_LOCK_001

**Proves:** DETERMINEX_COMPILER_LOOP_WAL_ATTEMPT_TRACE_RENDER_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_COMPILER_LOOP_WAL_TRACE_BINDING_LOCK_001

**Proves:** DETERMINEX_COMPILER_LOOP_WAL_TRACE_BINDING_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CONDITIONAL_REACT_VITE_LOCAL_VERIFICATION_LOCK_001

**Proves:** DETERMINEX_CONDITIONAL_REACT_VITE_LOCAL_VERIFICATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CONDITIONAL_REACT_VITE_SIGNATURE_IMPORT_LOCK_001

**Proves:** DETERMINEX_CONDITIONAL_REACT_VITE_SIGNATURE_IMPORT_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CONDITIONAL_REACT_VITE_SIGNED_SPEND_LOCK_001

**Proves:** DETERMINEX_CONDITIONAL_REACT_VITE_SIGNED_SPEND_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CONDITIONAL_SIGNATURE_CURRENT_STATE_RECHECK_LOCK_001

**Proves:** DETERMINEX_CONDITIONAL_SIGNATURE_CURRENT_STATE_RECHECK_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CONDITIONAL_SIGNATURE_OR_RELEASE_SUBSTRATE_RECONCILIATION_LOCK_001

**Proves:** DETERMINEX_CONDITIONAL_SIGNATURE_OR_RELEASE_SUBSTRATE_RECONCILIATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CONDITIONAL_SIGNATURE_OR_RELEASE_SUBSTRATE_REVIEW_READY_LOCK_001

**Proves:** DETERMINEX_CONDITIONAL_SIGNATURE_OR_RELEASE_SUBSTRATE_REVIEW_READY_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CONDITIONAL_SIGNATURE_RELEASE_SUBSTRATE_SCORE_RECONCILIATION_LOCK_001

**Proves:** DETERMINEX_CONDITIONAL_SIGNATURE_RELEASE_SUBSTRATE_SCORE_RECONCILIATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_AUTHORITY_BOUNDARY_REVIEW_001

**Proves:** Conditional-sig-release Claude Lane O. All 13 Codex lanes authority/protected_external_action=false; 24-wave boundary.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_BETA_DASHBOARD_REVIEW_001

**Proves:** Conditional-sig-release Claude Lane L. Codex Lane J: PUBLIC_PROOF_BETA_READINESS_DASHBOARD_RECORDED with safe wording and unsafe-wording rejection; no public upload.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_CLEAN_HOST_PACKET_HARDENING_REVIEW_001

**Proves:** Conditional-sig-release Claude Lane I. Codex Lane G: CLEAN_HOST_PACKET_HARDENED_UNSIGNED (no execution); runner assumptions + evidence requirements documented.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_CURRENT_SOURCE_TRUTH_REVIEW_001

**Proves:** Conditional-sig-release Claude Lane C. Current state bound: HEAD/spine/queue/audit/packet/registry/Tier-1.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001

**Proves:** Conditional-sig-release Claude Lane P. All forbidden actions audited and avoided.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_GUI_BUILD_PACKET_HARDENING_REVIEW_001

**Proves:** Conditional-sig-release Claude Lane J. Codex Lane H: GUI_BUILD_PACKET_HARDENED_UNSIGNED (no GUI launch); driver requirements + screenshot evidence requirements documented.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_INSTALLER_RELEASE_PACKET_HARDENING_REVIEW_001

**Proves:** Conditional-sig-release Claude Lane K. Codex Lane I: INSTALLER_RELEASE_PACKET_HARDENED_UNSIGNED (no execution); artifact hash + SBOM relationship + claim boundaries documented.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_MARKER_HASH_STABILITY_REVIEW_001

**Proves:** Conditional-sig-release Claude Lane B. Marker hash 40 chars, stable=true, successor policy applied — protocol hardening from prior wave continuing to work as intended.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_OPERATOR_ACTION_PACKET_REVIEW_001

**Proves:** Conditional-sig-release Claude Lane M. Codex Lane K: OPERATOR_ACTION_PACKET_FOR_FIRST_SPEND_RECORDED with canonical inbox path + required fields + warnings; not itself an approval.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_QUEUE_COUNT_REVIEW_001

**Proves:** Conditional-sig-release Claude Lane E. signed_valid_queue before=0 after=0.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_REACT_VITE_SPEND_VERIFY_REVIEW_001

**Proves:** Conditional-sig-release Claude Lane G. Codex Lane D NOT_RUN; Lane E BLOCKED; no React/Vite admission claimed.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_SBOM_PACKET_HARDENING_REVIEW_001

**Proves:** Conditional-sig-release Claude Lane H. Codex Lane F: SBOM_PACKET_HARDENED_UNSIGNED (no execution); validator fixtures + command scope + signature requirements documented.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_SCORE_MOVEMENT_REVIEW_001

**Proves:** Conditional-sig-release Claude Lane N. Codex Lane L: SCORE_RECONCILED with no movement; baseline preserved; packaging/release blocked.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_SIGNATURE_SCAN_IMPORT_REVIEW_001

**Proves:** Conditional-sig-release Claude Lane D. Codex Lane C: BLOCKED_NO_MATERIAL; signature inbox scanned, no real material.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_SPEND_COUNT_REVIEW_001

**Proves:** Conditional-sig-release Claude Lane F. signed_spend before=0 after=0 (Path A not triggered).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_SYNTHESIS_REVIEW_001

**Proves:** Conditional-sig-release Claude Lane Q. Synthesis + 33-item final report. Path B verified: Codex advanced release-facing substrate without spend or protected execution.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CONDITIONAL_SIG_RELEASE_CLAUDE_TIMER_REVIEW_001

**Proves:** Conditional-sig-release Claude Lane A. Timer + stability check applied; 8 rechecks; marker arrived #7, stability passed #8.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CONTRACT_CONSUMPTION_RECEIPT_PER_WAVE_LOCK_001

**Proves:** Require a Claude contract consumption receipt before every future Codex wave.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_COST_LOCAL_COMPUTE_AND_SETUP_DISCLOSURE_POLICY_LOCK_001

**Proves:** Make open/local/near-zero software cost claims honest by requiring hardware, setup, cloud, hosting, and toolchain caveats.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CROSS_LANE_AUTHORITY_BOUNDARY_LOCK_001

**Proves:** Confirm Claude and Codex lanes can join under a non-authorizing cross-lane authority boundary.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CRSBST_CLAUDE_APPEND_ONLY_COUNT_DRIFT_ANTI_GOD_REVIEW_001

**Proves:** CRSBST Claude Lane AE. Append-only ledger / count-drift / anti-god / release-registry guards all pass.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CRSBST_CLAUDE_BROADER_REPO_SBOM_BLOCKER_SHARPENED_REVIEW_001

**Proves:** CRSBST Claude Lane J. Broader repo SBOM BLOCKER_SHARPENED; output file absent; no fake CycloneDX.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CRSBST_CLAUDE_BROADER_REPO_SBOM_PACKET_ADMISSION_REVIEW_001

**Proves:** CRSBST Claude Lane I. Broader repo SBOM packet admitted as separate spend (queue 6→7).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CRSBST_CLAUDE_BROWSER_TAURI_HARNESS_PACKETS_REVIEW_001

**Proves:** CRSBST Claude Lane S. Browser extension / Tauri / Electron GUI-build packets prepared, NOT EXECUTED.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CRSBST_CLAUDE_CLAIM_SCANNER_DAY1_OVERCLAIM_REVIEW_001

**Proves:** CRSBST Claude Lane AF. Claim scanner / Day-1 overclaim scanner pass.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CRSBST_CLAUDE_CLEAN_RUNNER_BLOCKER_REDUCED_HONEST_REVIEW_001

**Proves:** CRSBST Claude Lane G. Clean-runner blocker REDUCED (not verified); no fake clean-runner proof.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CRSBST_CLAUDE_CLEAN_RUNNER_GIT_BLOCKER_DIAGNOSIS_REVIEW_001

**Proves:** CRSBST Claude Lane A. Clean-runner Git blocker diagnosis recorded with candidate fix.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CRSBST_CLAUDE_CLEAN_RUNNER_RETRY_EXECUTION_REVIEW_001

**Proves:** CRSBST Claude Lane F. Clean-runner retry execution attempted; transcript present.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CRSBST_CLAUDE_CLEAN_RUNNER_RETRY_ONE_TIME_SPEND_REVIEW_001

**Proves:** CRSBST Claude Lane E. Clean-runner retry one-time spend consumed; reuse rejected.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CRSBST_CLAUDE_CLEAN_RUNNER_RETRY_PACKET_VALIDATION_REVIEW_001

**Proves:** CRSBST Claude Lane D. ADMITTED_CLEAN_RUNNER_SAFE_CLONE_RETRY packet validated and admitted.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CRSBST_CLAUDE_EVIDENCE_PATH_INTEGRITY_REVIEW_001

**Proves:** CRSBST Claude Lane P. Evidence index 1821 entries clean; all referenced files present.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CRSBST_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001

**Proves:** CRSBST Claude Lane AH. 26 forbidden actions avoided.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CRSBST_CLAUDE_FULL_STATUS_NOT_RUN_HONEST_REVIEW_001

**Proves:** CRSBST Claude Lane AD. Full-suite NOT run; no full-suite pass claimed; no tests disabled.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CRSBST_CLAUDE_GUI_BUILD_INSTALLER_BETA_NOT_EXECUTED_REVIEW_001

**Proves:** CRSBST Claude Lane AC. GUI/build / installer/release / beta / ProgramBench / public upload / training rows absent.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CRSBST_CLAUDE_HIGH_RISK_GATES_UNCHANGED_REVIEW_001

**Proves:** CRSBST Claude Lane U. ML/Mobile/Hardware/Kotlin/Swift exact_blocker per family; none promoted.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CRSBST_CLAUDE_KNOWN_WORLD_DETECTOR_SEGMENT_1_REVIEW_001

**Proves:** CRSBST Claude Lane Q. Known-world detector segment 1 expansion landed (count = 6).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CRSBST_CLAUDE_KNOWN_WORLD_REGISTRY_STILL_ACCOUNTING_REVIEW_001

**Proves:** CRSBST Claude Lane R. Known-world registry remains ACCOUNTING; no support promotion without verifier.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CRSBST_CLAUDE_NO_C_PATH_MOVED_NO_DELETION_REVIEW_001

**Proves:** CRSBST Claude Lane O. executed_moves=[]; deletion_or_pruning_performed=false; evidence_moved=false.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CRSBST_CLAUDE_NO_FAMILY_PROMOTION_NO_OVERCLAIM_REVIEW_001

**Proves:** CRSBST Claude Lane V. 0 families executed; 0 promoted; LV 22 unchanged.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CRSBST_CLAUDE_NO_RELEASE_READY_NO_BETA_NO_INSTALLER_CLAIM_REVIEW_001

**Proves:** CRSBST Claude Lane AB. No release-ready / beta-ready / installer-ready / universal / broad-family-support claim.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CRSBST_CLAUDE_NO_SILENT_HASH_MISMATCH_REVIEW_001

**Proves:** CRSBST Claude Lane M. silent_hash_mismatch_accepted=FALSE; previous_sbom_truth_replaced=FALSE.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CRSBST_CLAUDE_NO_TEST_VERIFIER_LOCKFILE_MUTATION_REVIEW_001

**Proves:** CRSBST Claude Lane AG. Test/verifier/oracle/compiler/binary + package/lockfile NOT mutated.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CRSBST_CLAUDE_PHP_RUBY_GATES_UNCHANGED_REVIEW_001

**Proves:** CRSBST Claude Lane T. PHP/Ruby still EXACT_FIXTURE_OR_TOOLCHAIN_GATE; no global install.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CRSBST_CLAUDE_QUEUE_SPEND_CONSERVATION_REVIEW_001

**Proves:** CRSBST Claude Lane X. Queue/spend conservation Δqueue=2 / Δspend=2 (two new spends; preserved).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CRSBST_CLAUDE_RELEASE_CELLS_CANONICAL_REVIEW_001

**Proves:** CRSBST Claude Lane Y. Release-supported exact cells canonical (10).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CRSBST_CLAUDE_RELEASE_FAMILIES_CANONICAL_REVIEW_001

**Proves:** CRSBST Claude Lane Z. Release-supported families canonical (0).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CRSBST_CLAUDE_REMAINING_NLV_FAMILIES_REVIEW_001

**Proves:** CRSBST Claude Lane W. 9 remaining NLV families with active next action.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CRSBST_CLAUDE_RUNNER_CONTEXT_DISTINCT_REVIEW_001

**Proves:** CRSBST Claude Lane H. New runner path materially distinct from prior failed admitted_runner_wave_001.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CRSBST_CLAUDE_RUNNER_SAFE_CLONE_POLICY_REVIEW_001

**Proves:** CRSBST Claude Lane C. Runner-safe clone policy applied with new unique T: path.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CRSBST_CLAUDE_SAFE_DIRECTORY_SCOPED_NOT_GLOBAL_REVIEW_001

**Proves:** CRSBST Claude Lane B. safe.directory used command-scoped; NO global Git config mutated.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CRSBST_CLAUDE_SBOM_BYTE_EXACT_MISMATCH_DIAGNOSIS_REVIEW_001

**Proves:** CRSBST Claude Lane L. SBOM byte-exact mismatch honestly diagnosed (runner CRLF/LF vs main); next packet recorded.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CRSBST_CLAUDE_SBOM_FRONTEND_CONTINUITY_REVIEW_001

**Proves:** CRSBST Claude Lane K. Frontend SBOM continuity preserved; canonical hash unchanged.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CRSBST_CLAUDE_SCORE_OPEN_AVAILABILITY_MOVED_EVIDENCE_BOUND_REVIEW_001

**Proves:** CRSBST Claude Lane AA. open_availability +1pp; other scores unchanged; score_delta_guard via detector evidence.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CRSBST_CLAUDE_SYNTHESIS_REVIEW_001

**Proves:** CRSBST Claude Lane AI. Synthesis + final report.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CRSBST_CLAUDE_T_DRIVE_RELOCATION_PACKETS_PREPARED_REVIEW_001

**Proves:** CRSBST Claude Lane N. T-drive relocation packets (tauri/cargo + temp/log/cache) PREPARED, NOT EXECUTED.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CURRENT_STATE_SOURCE_TRUTH_RECONCILIATION_LOCK_001

**Proves:** DETERMINEX_CURRENT_STATE_SOURCE_TRUTH_RECONCILIATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_DAY1_IDE_DASHBOARD_COMPLETION_LOCK_001

**Proves:** DETERMINEX_DAY1_IDE_DASHBOARD_COMPLETION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_DAY1_OVERCLAIM_SCANNER_HARDENING_LOCK_001

**Proves:** DETERMINEX_DAY1_OVERCLAIM_SCANNER_HARDENING_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_DAY1_STRUCTURAL_COVERAGE_DASHBOARD_BINDING_LOCK_001

**Proves:** DETERMINEX_DAY1_STRUCTURAL_COVERAGE_DASHBOARD_BINDING_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_DAY1_STRUCTURAL_DASHBOARD_RENDERED_LOCK_001

**Proves:** DETERMINEX_DAY1_STRUCTURAL_DASHBOARD_RENDERED_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_DAY_ONE_CLAIM_SCANNER_AND_SAFE_SHOCK_TEMPLATE_LOCK_001

**Proves:** DETERMINEX_DAY_ONE_CLAIM_SCANNER_AND_SAFE_SHOCK_TEMPLATE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_DAY_ONE_CLAIM_SCANNER_CI_ENFORCEMENT_LOCK_001

**Proves:** DETERMINEX_DAY_ONE_CLAIM_SCANNER_CI_ENFORCEMENT_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_DAY_ONE_PUBLIC_CLAIM_REMEDIATION_APPLY_LOCK_001

**Proves:** Apply and record minimal public claim wording fixes until the day-one claim scanner reaches zero violations or emits residuals.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_DAY_ONE_PUBLIC_CLAIM_SCANNER_LOCK_001

**Proves:** Create the static day-one public claim scanner with known-good/known-bad fixtures and a current public-doc scan.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_DEPENDENCY_BLOCKER_RECONCILIATION_LOCK_001

**Proves:** Reconcile dependency blockers without installing, fetching, building, or granting release authority.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_DESKTOP_COCKPIT_GUI_E2E_REALITY_CLAUDE_REVIEW_001

**Proves:** Gulp Wave 005 Claude Lane Z. Cockpit reality + GUI e2e. 14 panels mapped; 11-rung proof ladder; 3 GUI flows ranked (first_paint -> ProgramBenchCockpit -> Idea Lab plan).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_DESKTOP_FIRST_PAINT_AFTER_DRIVER_ADMISSION_LOCK_001

**Proves:** DETERMINEX_DESKTOP_FIRST_PAINT_AFTER_DRIVER_ADMISSION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_DESKTOP_GUI_E2E_AND_COCKPIT_REALITY_CLAUDE_REVIEW_001

**Proves:** Gulp Wave 004 Claude Lane Z. Desktop GUI e2e + cockpit reality. Defines what counts as desktop_gui_e2e_proven, names the minimum proof contract (first_paint_smoke), and ranks 5 candidate flows. The engine is real; the cockpit is unfinished.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_DESKTOP_GUI_E2E_DRIVER_ADMISSION_AND_BOUNDED_PROOF_LOCK_001

**Proves:** Prepare or execute a bounded desktop GUI e2e proof only when driver admission and single-event launch approval exist.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_DETECTOR_CLASSIFIER_FIXTURE_CI_BACKFILL_LOCK_001

**Proves:** Detector / Classifier / Fixture CI Backfill

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_DETECTOR_FIXTURE_CORPUS_AND_CI_ASSERTION_LOCK_001

**Proves:** Detector Fixture Corpus and CI Assertion

**Does not prove:** Does not prove corpus balance, training effectiveness, or public benchmark dominance by itself.

#### DETERMINEX_DETECTOR_FIXTURE_CORPUS_CI_HARDENING_LOCK_002

**Proves:** Detector Fixture Corpus CI Hardening

**Does not prove:** Does not prove corpus balance, training effectiveness, or public benchmark dominance by itself.

#### DETERMINEX_DETECTOR_FOUR_STATE_TOOLCHAIN_CLASSIFIER_LOCK_001

**Proves:** DETERMINEX_DETECTOR_FOUR_STATE_TOOLCHAIN_CLASSIFIER_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_DETECTOR_RUNTIME_PROBE_IMPLEMENTATION_LOCK_001

**Proves:** DETERMINEX_DETECTOR_RUNTIME_PROBE_IMPLEMENTATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_DOCS_STATIC_CELL_SMOKE_PROOF_LOCK_001

**Proves:** Produce the exact docs_static_smoke_cell smoke proof packet from the passing local docs/static verifier.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_DOCS_STATIC_FIRST_RELEASE_SUPPORTED_CELL_CERTIFICATION_LOCK_001

**Proves:** Attempt first exact docs_static_smoke_cell release-supported certification and block truthfully on missing rungs.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_DOCS_STATIC_FIRST_RELEASE_SUPPORTED_CELL_CERTIFICATION_RETRY_LOCK_001

**Proves:** Retry exact docs_static_smoke_cell release-supported certification after operator approval and fresh clone retry proof.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_DOCS_STATIC_LINK_CHECK_AND_VERIFIER_LOCK_001

**Proves:** Implement and run a local no-network docs/static verifier for the exact docs_static_smoke_cell candidate.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_DOCS_STATIC_OPERATOR_APPROVAL_RECORD_LOCK_001

**Proves:** Record exact operator approval for docs_static_smoke_cell only before certification retry.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_DOCS_STATIC_RELEASE_SUPPORTED_CELL_PREREQUISITE_LOCK_001

**Proves:** Prepare the docs/static docs exact cell as the fastest honest first release-supported candidate without certifying it prematurely.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_DRY_RUN_INSTALL_MISLABEL_KILL_SWITCH_LOCK_001

**Proves:** DETERMINEX_DRY_RUN_INSTALL_MISLABEL_KILL_SWITCH_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_DRY_RUN_SIGNATURE_IMPORT_LOCK_001

**Proves:** DETERMINEX_DRY_RUN_SIGNATURE_IMPORT_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_EMBEDDED_HARDWARE_AUTHORITY_GATE_LOCK_001

**Proves:** Embedded Hardware Authority Gate

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ENVISIONED_IDE_CAPABILITY_COMPLETION_MAP_LOCK_001

**Proves:** Create the master source-truth capability completion map from current proof state to full envisioned IDE readiness.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ENVISIONED_IDE_COMPLETION_CLAUDE_CRITIQUE_AND_QUEUE_001

**Proves:** Read-only critique mapping the fastest path from current proof infrastructure to the envisioned full native IDE/workbench. 12 gap reviews + 9 master outputs. No Codex source truth mutated. No claim broadened. No release support granted.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_EVIDENCE_COUNT_DRIFT_GUARD_LOCK_001

**Proves:** Prevent evidence count drift and validation ambiguity by reconciling the evidence index with the append-only ledger snapshot.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_EXACT_CELL_PROMOTION_GATE_EXPANSION_LOCK_001

**Proves:** DETERMINEX_EXACT_CELL_PROMOTION_GATE_EXPANSION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_EXACT_CELL_PROMOTION_REQUIRES_LADDER_AND_VERIFIER_SIGNOFF_LOCK_001

**Proves:** DETERMINEX_EXACT_CELL_PROMOTION_REQUIRES_LADDER_AND_VERIFIER_SIGNOFF_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_EXISTING_CAPABILITY_HARVEST_LOCK_001

**Proves:** Harvest existing evidence-backed and code-backed Determinex capabilities without widening claims.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_EXTERNAL_AUTHORITY_HARD_FLOOR_UNLOCK_PACKET_LOCK_001

**Proves:** DETERMINEX_EXTERNAL_AUTHORITY_HARD_FLOOR_UNLOCK_PACKET_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_EXTERNAL_AUTHORITY_TRACK_CARRY_LOCK_001

**Proves:** DETERMINEX_EXTERNAL_AUTHORITY_TRACK_CARRY_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_EXTERNAL_AUTHORITY_UNLOCK_PLAN_LOCK_001

**Proves:** DETERMINEX_EXTERNAL_AUTHORITY_UNLOCK_PLAN_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_FAMILY_READINESS_MATRIX_AND_GATE_DEFINITION_LOCK_001

**Proves:** Family Readiness Matrix

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_FAMILY_SUPPORT_GATE_DEFINITION_AND_CI_INVARIANT_LOCK_001

**Proves:** Family Support Gate Definition and CI Invariant

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_FAMILY_SUPPORT_READINESS_MATRIX_LOCK_001

**Proves:** Family Support Readiness Matrix

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_FASTEMBED_MODEL_ASSET_BINDING_LOCK_001

**Proves:** Bind a pre-existing local fastembed all-MiniLM-L6-v2 model asset into source truth and add a local env-var loading path for the Tauri vector engine.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_FINAL_OMG_DEMO_PROOF_EXPORT_ATTEMPT_LOCK_001

**Proves:** DETERMINEX_FINAL_OMG_DEMO_PROOF_EXPORT_ATTEMPT_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_FIRST_AUTHORITY_SPEND_AND_BASELINE_RECONCILIATION_LOCK_001

**Proves:** DETERMINEX_FIRST_AUTHORITY_SPEND_AND_BASELINE_RECONCILIATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_FIRST_CLEAN_HOST_TRANSCRIPT_IF_RUNNER_ADMITTED_LOCK_001

**Proves:** Clean-Host First Transcript If Runner Admitted

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_FIRST_EXACT_SUPPORT_DEPTH_PROMOTION_ATTEMPT_LOCK_001

**Proves:** Attempt first exact support-depth promotion and promote only the evidence-validation status cell.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_FIRST_FAMILY_SUPPORT_PROMOTION_ELIGIBILITY_REVIEW_LOCK_001

**Proves:** DETERMINEX_FIRST_FAMILY_SUPPORT_PROMOTION_ELIGIBILITY_REVIEW_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_FIRST_GUI_VISUAL_PROOF_IF_APPROVED_LOCK_001

**Proves:** GUI First Visual Proof If Approved

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_FIRST_REACT_VITE_SIGNED_SPEND_LOCK_001

**Proves:** DETERMINEX_FIRST_REACT_VITE_SIGNED_SPEND_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_FIRST_REAL_SIGNATURE_BOUNDED_GUI_LAUNCH_LOCK_001

**Proves:** DETERMINEX_FIRST_REAL_SIGNATURE_BOUNDED_GUI_LAUNCH_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_FIRST_REAL_SIGNATURE_IMPORT_AND_SPEND_IF_PRESENT_LOCK_001

**Proves:** First Real Signature Import and Spend If Present

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_FIRST_REAL_SIGNATURE_MSEDGEDRIVER_DOWNLOAD_ADMISSION_LOCK_001

**Proves:** DETERMINEX_FIRST_REAL_SIGNATURE_MSEDGEDRIVER_DOWNLOAD_ADMISSION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_FIRST_REAL_SIGNATURE_NSIS_INSTALL_LAUNCH_UNINSTALL_LOCK_001

**Proves:** DETERMINEX_FIRST_REAL_SIGNATURE_NSIS_INSTALL_LAUNCH_UNINSTALL_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_FIRST_REAL_SIGNATURE_SPEND_IF_PRESENT_LOCK_001

**Proves:** First Real Signature Spend If Present

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_FIRST_REAL_SIGNATURE_SYFT_SBOM_TOOL_ADMISSION_LOCK_001

**Proves:** DETERMINEX_FIRST_REAL_SIGNATURE_SYFT_SBOM_TOOL_ADMISSION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_FIRST_RUN_INSTALL_AND_DEMO_BUNDLE_PROOF_LOCK_001

**Proves:** Define and verify a bounded first-run install/demo bundle proof path so a new user or reviewer can inspect a local-first proof-governed journey without granting launch readiness, release support, production readiness, source mutation authority, proof execution authority, training eligibility, commercial enforcement, broad claims, or universal support.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_FIRST_SBOM_ARTIFACT_IF_SYFT_ADMITTED_LOCK_001

**Proves:** First SBOM Artifact If Syft Is Admitted

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_FIRST_SBOM_ARTIFACT_IF_TOOL_ADMITTED_LOCK_006

**Proves:** First SBOM Artifact If Tool Admitted

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_FIRST_SBOM_OR_EXACT_TOOL_ADMISSION_PACKET_LOCK_001

**Proves:** DETERMINEX_FIRST_SBOM_OR_EXACT_TOOL_ADMISSION_PACKET_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_FIRST_SBOM_TOOL_ADMISSION_AND_ARTIFACT_LOCK_005

**Proves:** First SBOM Tool Admission and Artifact

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_FIRST_SBOM_TOOL_ADMISSION_AND_EMISSION_LOCK_004

**Proves:** First SBOM Tool Admission and Emission

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_FIRST_SIGNATURE_SPEND_RECONCILIATION_LOCK_001

**Proves:** DETERMINEX_FIRST_SIGNATURE_SPEND_RECONCILIATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_FIRST_SIGNED_AUTHORITY_SPEND_REACT_VITE_DEPENDENCY_ADMISSION_LOCK_001

**Proves:** DETERMINEX_FIRST_SIGNED_AUTHORITY_SPEND_REACT_VITE_DEPENDENCY_ADMISSION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_FIRST_SIGNED_AUTHORITY_SPEND_REACT_VITE_LOCK_001

**Proves:** DETERMINEX_FIRST_SIGNED_AUTHORITY_SPEND_REACT_VITE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_FIRST_USER_VISIBLE_IDE_WORKFLOW_PROOF_CANDIDATE_LOCK_001

**Proves:** Select the fastest honest first user-visible IDE workflow candidate and define its proof contract.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_FIXTURE_ADMISSION_PIPELINE_LOCK_001

**Proves:** Define how fixtures become admissible evidence inputs for verifier slots without executing unsafe projects, installing toolchains, reducing blockers, or granting support/release/source/proof/training authority.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_FIXTURE_FACTORY_SEED_LOCK_001

**Proves:** Seed fixture factory definitions for future app/language/workflow probes without creating fake passes.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_FIX_BROKEN_CANONICAL_CELL_PROOF_ANCHOR_LOCK_001

**Proves:** Fix Broken Canonical Proof Anchor

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_FRESH_CLONE_BOOTSTRAP_PROOF_LOCK_001

**Proves:** Prove or block fresh local clone bootstrap without dependency install.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_FRESH_CLONE_BOOTSTRAP_PROOF_RETRY_LOCK_001

**Proves:** Retry fresh clone/bootstrap using command-scoped Windows longpaths and local no-network clone.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_FRESH_INSTALL_PROOF_PATH_SPLIT_LOCK_001

**Proves:** Separate fresh clone, bootstrap, installer smoke, installer install/uninstall, and fresh install gates without broad readiness claims.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_FULL_STATUS_SEGMENTATION_REPAIR_LOCK_001

**Proves:** Full-Status Segmentation Repair

**Does not prove:** Does not prove broad real-world repair coverage beyond the locked acceptance tests.

#### DETERMINEX_FULL_STATUS_SEGMENTED_TIMING_REPAIR_LOCK_001

**Proves:** Full-Status Segmented Timing Repair

**Does not prove:** Does not prove broad real-world repair coverage beyond the locked acceptance tests.

#### DETERMINEX_FULL_STATUS_TIMEOUT_DIAGNOSTIC_LOCK_001

**Proves:** DETERMINEX_FULL_STATUS_TIMEOUT_DIAGNOSTIC_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_FULL_SYSTEM_OMG_DEMO_GAP_CLAUDE_REVIEW_001

**Proves:** Gulp Wave 005 Claude Lane X. 10-step OMG demo gap review. Scores 3.7/10 average; lists top 20 Codex deltas; identifies load-bearing step (compiler-loop GUI) and missing panels.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_GLOBAL_OPERATOR_ACTION_QUEUE_DEDUP_RECONCILIATION_LOCK_001

**Proves:** Deduplicate and clarify the global operator action queue without granting authority.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_GLOBAL_OPERATOR_ACTION_QUEUE_LOCK_001

**Proves:** Create a unified, prioritized operator action queue across Claude, Codex, and Proof Control Plane evidence without authorizing any action.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_GLOBAL_TRAINING_ELIGIBILITY_GUARD_LOCK_001

**Proves:** Create a unified negative training eligibility guard across Claude, Codex, and Proof Control Plane evidence.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_GLOBAL_TRAINING_POSITIVE_GATE_DESIGN_LOCK_001

**Proves:** Define the positive global training eligibility gate without enabling training or writing corpus rows.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_GO_TOOLCHAIN_REPAIR_AND_VITE_STATIC_SMOKE_LOCK_001

**Proves:** go toolchain repair and vite static smoke

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_GUI_AUTOMATION_AND_FIRST_PAINT_CAPABILITY_ROUTE_LOCK_001

**Proves:** DETERMINEX_GUI_AUTOMATION_AND_FIRST_PAINT_CAPABILITY_ROUTE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_GUI_BUILD_PACKET_HARDENING_LOCK_001

**Proves:** DETERMINEX_GUI_BUILD_PACKET_HARDENING_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_GUI_BUILD_SMOKE_INSTALLER_AND_RELEASE_CELL_CERTIFICATION_WAVE_001

**Proves:** GUI/build smoke, installer packet execution, release-cell candidate certification, scoped SBOM policy, fresh-run replay, and release claim boundaries.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_GUI_E2E_DRIVER_AUTHORIZATION_REFRESH_LOCK_001

**Proves:** Refresh the bounded msedgedriver authorization packet for desktop GUI e2e without download, install, or GUI launch.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_GUI_E2E_HARNESS_REQUIREMENTS_LOCK_001

**Proves:** Define deterministic GUI e2e harness requirements without installing dependencies or launching GUI.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_GUI_E2E_ROUTE_HARDENING_OR_FALLBACK_LOCK_001

**Proves:** Convert blocked Tauri GUI e2e route into exact hardening and fallback paths.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_GUI_FIRST_PAINT_AFTER_RUNTIME_APPROVAL_LOCK_001

**Proves:** DETERMINEX_GUI_FIRST_PAINT_AFTER_RUNTIME_APPROVAL_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_GUI_FIRST_PAINT_EXECUTION_IF_AUTHORIZED_LOCK_001

**Proves:** DETERMINEX_GUI_FIRST_PAINT_EXECUTION_IF_AUTHORIZED_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_GUI_FIRST_PAINT_EXECUTION_WITH_ADMITTED_DRIVER_LOCK_001

**Proves:** DETERMINEX_GUI_FIRST_PAINT_EXECUTION_WITH_ADMITTED_DRIVER_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_GUI_FIRST_PAINT_VISUAL_PROOF_CLAUDE_REVIEW_001

**Proves:** Wave 007 Claude Lane Z. GUI first paint vs meaningful flow distinction; driver presence, screenshot evidence, orphan cleanup, overstatement risks.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_GUI_FIRST_VISUAL_PROOF_BATCH_OR_APPROVAL_PACKET_LOCK_001

**Proves:** DETERMINEX_GUI_FIRST_VISUAL_PROOF_BATCH_OR_APPROVAL_PACKET_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_GUI_FIRST_VISUAL_PROOF_IF_APPROVED_LOCK_003

**Proves:** GUI First Visual Proof If Approved

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_GUI_HARNESS_DEPENDENCY_AUTHORIZATION_LOCK_001

**Proves:** Authorize exact GUI harness dependency scope without installing dependencies.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_GUI_IDEA_LAB_PROMPT_TO_PLAN_FLOW_EXECUTION_LOCK_001

**Proves:** DETERMINEX_GUI_IDEA_LAB_PROMPT_TO_PLAN_FLOW_EXECUTION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_GUI_MOAT_VISUAL_FLOW_BATCH_LOCK_001

**Proves:** DETERMINEX_GUI_MOAT_VISUAL_FLOW_BATCH_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_GUI_NOT_EXECUTED_BOUNDARY_GUARD_LOCK_001

**Proves:** GUI Not Executed Boundary Guard

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_GUI_PANEL_VISUAL_PROOF_BATCH_LOCK_001

**Proves:** DETERMINEX_GUI_PANEL_VISUAL_PROOF_BATCH_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_GUI_PROGRAMBENCH_COCKPIT_FLOW_EXECUTION_LOCK_001

**Proves:** DETERMINEX_GUI_PROGRAMBENCH_COCKPIT_FLOW_EXECUTION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_GUI_PROOF_LADDER_FIRST_PAINT_MEANINGFUL_FLOW_CLAUDE_REVIEW_001

**Proves:** Wave 006 Lane Z. GUI proof ladder + first-paint + meaningful flow. 3/14 rungs PASSED; 11 NOT_STARTED. First meaningful flow recommendation: ProgramBenchCockpit smoke.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_GULP_WAVE_001_RECONCILIATION_AND_NEXT_WAVE_LOCK_001

**Proves:** Reconcile Codex Gulp Wave 001 outputs and queue Gulp Wave 002 without broadening release claims.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_GULP_WAVE_002_RECONCILIATION_AND_NEXT_WAVE_LOCK_001

**Proves:** Reconcile Codex Gulp Wave 002, aggregate exact release-supported cells, refresh claim safety, and queue Wave 003.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_GULP_WAVE_003_RECONCILIATION_AND_NEXT_WAVE_LOCK_001

**Proves:** Reconcile Codex Gulp Wave 003, confirm exact fourth release-supported cell, preserve installer/fresh-install/GUI/RAG boundaries, and queue Wave 004.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_GULP_WAVE_004_CLAUDE_SYNTHESIS_AND_CODEX_DELTA_QUEUE_001

**Proves:** Gulp Wave 004 Claude synthesis lane. Aggregates X/Y/Z/R/T/P verdicts; ranks 15 Codex deltas; maps 10 public claim risks; 12 open-availability blockers; 12 day-one envisioned-system gaps; 8 Wave 005 Claude lane recommendations.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_GULP_WAVE_004_RECONCILIATION_AND_WAVE_005_GENERATOR_LOCK_001

**Proves:** Reconcile Gulp Wave 004 lanes, update exact release-supported counts, and generate Wave 005.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_GULP_WAVE_005_CLAUDE_SYNTHESIS_AND_CODEX_PRESSURE_QUEUE_001

**Proves:** Wave 005 synthesis. 9 lanes verdicts; 25 ranked Codex deltas; 20 full-system blockers; 20 wow-perception blockers; 10 public claim risks; Wave 006 lane/Codex queue.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_GULP_WAVE_005_RECONCILIATION_AND_WAVE_006_GENERATOR_LOCK_001

**Proves:** Reconcile Gulp Wave 005 lanes and generate Wave 006 without broadening readiness claims.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_GULP_WAVE_006_RECONCILIATION_AND_WAVE_007_GENERATOR_LOCK_001

**Proves:** DETERMINEX_GULP_WAVE_006_RECONCILIATION_AND_WAVE_007_GENERATOR_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_GULP_WAVE_007_RECONCILIATION_AND_WAVE_008_GENERATOR_LOCK_001

**Proves:** DETERMINEX_GULP_WAVE_007_RECONCILIATION_AND_WAVE_008_GENERATOR_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_GULP_WAVE_008_RECONCILIATION_AND_WAVE_009_QUEUE_LOCK_001

**Proves:** DETERMINEX_GULP_WAVE_008_RECONCILIATION_AND_WAVE_009_QUEUE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_GULP_WAVE_009_RECONCILIATION_AND_WAVE_010_QUEUE_LOCK_001

**Proves:** DETERMINEX_GULP_WAVE_009_RECONCILIATION_AND_WAVE_010_QUEUE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_GULP_WAVE_010_RECONCILIATION_AND_WAVE_011_QUEUE_LOCK_001

**Proves:** DETERMINEX_GULP_WAVE_010_RECONCILIATION_AND_WAVE_011_QUEUE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_GULP_WAVE_011_RECONCILIATION_AND_WAVE_012_QUEUE_LOCK_001

**Proves:** DETERMINEX_GULP_WAVE_011_RECONCILIATION_AND_WAVE_012_QUEUE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_HIVE_BUILD_LOOP_WAL_PANEL_WIRE_LOCK_001

**Proves:** DETERMINEX_HIVE_BUILD_LOOP_WAL_PANEL_WIRE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_HIVE_BUILD_LOOP_WAL_RENDER_CONTRACT_LOCK_001

**Proves:** DETERMINEX_HIVE_BUILD_LOOP_WAL_RENDER_CONTRACT_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_HIVE_BUILD_LOOP_WAL_VISIBILITY_CLAUDE_REVIEW_001

**Proves:** Overnight Lane 6. HiveBuildLoop WAL visibility. 6/12 inventory covered; 6 render-side missing. Engine moat stays CLI-only without WAL render.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_HTML_PROOF_REPORT_ATTACK_REVIEW_CLAUDE_001

**Proves:** Wave 007 Claude Lane H. Readability, per-claim evidence link, integrity stamp, versioning, sanitization/XSS, disclaimer footer, release boundary, authority boundary, investor/media usefulness, PDF readiness.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_HTML_PROOF_REPORT_INVESTOR_SHAREABILITY_FINALIZATION_LOCK_001

**Proves:** DETERMINEX_HTML_PROOF_REPORT_INVESTOR_SHAREABILITY_FINALIZATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_HTML_PROOF_REPORT_SHAREABILITY_HARDENING_LOCK_001

**Proves:** DETERMINEX_HTML_PROOF_REPORT_SHAREABILITY_HARDENING_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_IDEA_LAB_ACCEPTANCE_TEST_EXECUTION_PIPELINE_LOCK_001

**Proves:** DETERMINEX_IDEA_LAB_ACCEPTANCE_TEST_EXECUTION_PIPELINE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_IDEA_LAB_CERTIFICATION_AND_PRODUCT_SURFACE_CLAUDE_REVIEW_001

**Proves:** Wave 006 Lane I. Idea Lab cert + product surface. Blocked on approval + GUI binding + claim boundary.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_IDEA_LAB_DETERMINISTIC_ARTIFACT_RELEASE_SUPPORTED_CELL_CERTIFICATION_LOCK_001

**Proves:** Certify the exact Idea Lab deterministic prompt-to-plan sandbox artifact cell only if evidence gates and exact operator approval pass.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_IDEA_LAB_END_TO_END_ARTIFACT_PROOF_LOCK_001

**Proves:** DETERMINEX_IDEA_LAB_END_TO_END_ARTIFACT_PROOF_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_IDEA_LAB_EXACT_CELL_CERTIFICATION_RETRY_LOCK_001

**Proves:** DETERMINEX_IDEA_LAB_EXACT_CELL_CERTIFICATION_RETRY_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_IDEA_LAB_FREEFORM_ACCEPTANCE_TEST_GENERATOR_LOCK_001

**Proves:** DETERMINEX_IDEA_LAB_FREEFORM_ACCEPTANCE_TEST_GENERATOR_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_IDEA_LAB_PROMPT_TO_PLAN_DETERMINISM_LOCK_001

**Proves:** DETERMINEX_IDEA_LAB_PROMPT_TO_PLAN_DETERMINISM_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_IDEA_LAB_PYTHON_CLI_VERIFIED_SPLASH_DEMO_LOCK_001

**Proves:** Execute the first narrow Idea Lab splash path: a beginner-style Python CLI/file-data tool fixture with build/test and smoke verification before any scoped working-app claim.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_IDEA_LAB_PYTHON_CLI_VERIFIED_SPLASH_DEMO_READINESS_LOCK_001

**Proves:** Decide whether the first real Python CLI/file-data Idea Lab splash implementation lock is ready to run, without executing it.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_IDEA_LAB_UNDER_THE_HOOD_E2E_PIPELINE_LOCK_001

**Proves:** DETERMINEX_IDEA_LAB_UNDER_THE_HOOD_E2E_PIPELINE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_IDEA_LAB_WORKFLOW_LOCK_001

**Proves:** Rung 2 of DETERMINEX_UNIFIED_PRODUCT_UX_SHELL_SERIES.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_IDE_BACKEND_FINAL_STATE_LOCK_001

**Proves:** Rung 10 of the verified-repair campaign — the campaign finale. Pins the equilibrium state the apparatus reached: clean execution surface, dry-run model routing, mocked end-to-end loop, temp-only safe patch, source mutation blocked pending human approval, IDE backend state ready, NO live model calls, training eligibility BLOCKED, NOT RELEASED. The next unblocker is LOCAL_MODEL_LIVE_ADMISSION_AND_IDE_UI_FLOW.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_IDE_CONSUMER_READY_FINAL_STATE_LOCK_001

**Proves:** Campaign finale for the IDE consumer-ready work.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_IDE_FRONTEND_READY_FINAL_STATE_LOCK_001

**Proves:** Campaign finale for REAL_FRONTEND_IMPLEMENTATION_AND_REAL_LOCAL_MODEL_CONFIG.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_IDE_RELEASE_ASCENT_RECONCILIATION_AND_NEXT_PROOF_LOCK_001

**Proves:** Reconcile current IDE release-ascent state and prove the project-local Tauri CLI route without release claims.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_IDE_TAURI_INTEGRATED_FINAL_STATE_LOCK_001

**Proves:** Campaign finale for REAL_TAURI_LIB_RS_WIRING_AND_LIVE_LOCAL_MODEL_PROVIDER.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_IDE_UI_READY_FINAL_STATE_LOCK_001

**Proves:** Campaign finale for the IDE frontend/approval work.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_IMPORT_REAL_SIGNED_APPROVALS_AND_SPEND_QUEUE_LOCK_001

**Proves:** DETERMINEX_IMPORT_REAL_SIGNED_APPROVALS_AND_SPEND_QUEUE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_INSTALLER_DISTRIBUTION_TRUST_CHAIN_CLAUDE_REVIEW_001

**Proves:** Gulp Wave 005 Claude Lane Y. Installer + distribution + trust chain. 10-layer trust chain map; 8 ranked channels; subpackage parallel path (determinex-cli on PyPI ranked 1).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_INSTALLER_INSTALL_LAUNCH_UNINSTALL_RELEASE_SIGNOFF_WAVE_001

**Proves:** DETERMINEX_INSTALLER_INSTALL_LAUNCH_UNINSTALL_RELEASE_SIGNOFF_WAVE_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_INSTALLER_NOT_EXECUTED_BOUNDARY_GUARD_LOCK_001

**Proves:** Installer Not Executed Boundary Guard

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_INSTALLER_REALITY_SBOM_SIGNING_PUBLIC_DISTRIBUTION_CLAUDE_REVIEW_001

**Proves:** Gulp Wave 004 Claude Lane Y. Installer reality + SBOM + signing + public distribution channel review. Reviews exact path from artifact to beta-distribution candidate. Adds subpackage distribution as parallel low-risk user-adoption path.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_INSTALLER_RELEASE_PACKET_HARDENING_LOCK_001

**Proves:** DETERMINEX_INSTALLER_RELEASE_PACKET_HARDENING_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_INTERNAL_PREVIEW_AND_SUBPACKAGE_DISTRIBUTION_CLAUDE_REVIEW_001

**Proves:** Wave 006 Lane D. Internal preview + subpackage distribution. 7 options ranked; 0 started.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_INTERNAL_PREVIEW_DISTRIBUTION_PACKET_LOCK_001

**Proves:** DETERMINEX_INTERNAL_PREVIEW_DISTRIBUTION_PACKET_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_INVALID_SIGNATURE_REJECTION_CORPUS_LOCK_001

**Proves:** DETERMINEX_INVALID_SIGNATURE_REJECTION_CORPUS_LOCK_001

**Does not prove:** Does not prove corpus balance, training effectiveness, or public benchmark dominance by itself.

#### DETERMINEX_KNOWN_WORLD_CAPABILITY_UNIVERSE_REGISTRY_LOCK_001

**Proves:** Known-World Capability Universe Registry

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_KNOWN_WORLD_DETECTOR_GAP_QUEUE_LOCK_001

**Proves:** Known-World Detector Gap Queue

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_KNOWN_WORLD_DETECTOR_SEGMENT_1_LOCK_001

**Proves:** KNOWN_WORLD_DETECTOR_SEGMENT_1_RECORDED for DETERMINEX_CLEAN_RUNNER_SAFE_CLONE_BROADER_SBOM_T_DRIVE_RELOCATION_AND_DETECTOR_EXPANSION_WAVE_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_KOTLIN_TOOLCHAIN_GLOBAL_GATE_LOCK_001

**Proves:** Kotlin Toolchain Global Gate

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_LADDER_INVERSION_CI_BLOCKING_LOCK_002

**Proves:** Ladder Inversion CI Blocking

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_LADDER_RUNG_INVERSION_CI_LOCK_001

**Proves:** Ladder Rung Inversion CI

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_LANGUAGE_FRAMEWORK_ADAPTER_REGISTRY_LOCK_001

**Proves:** Normalize language/framework adapter and verifier coverage into a routing registry.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_LANGUAGE_TOOLCHAIN_DETECTOR_MATRIX_LOCK_001

**Proves:** Create source-truth detector rules for languages, frameworks, package managers, build systems, test systems, runtimes, platforms, repository shapes, blockers, and nearest supported cells without executing or verifying projects.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_LANGUAGE_TOOLCHAIN_DETECTOR_MATRIX_RECONCILIATION_LOCK_002

**Proves:** Join the 157-entry programming language universe catalog to the existing 37-entry detector matrix, surfacing detector states, verifier gaps, blockers, and nearest supported cells without treating detection or routing as support.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_LEARNING_STUDIO_TEACHING_SPLASH_DEMO_LOCK_001

**Proves:** Create a non-authorizing Learning Studio teaching splash demo grounded in existing verified Repo Clinic and Maintenance Bay fixture evidence.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_LEARNING_STUDIO_WORKFLOW_LOCK_001

**Proves:** Rung 5 of DETERMINEX_UNIFIED_PRODUCT_UX_SHELL_SERIES.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_LEGACY_FULL_VERIFIER_SIGNOFF_COMPLETION_LOCK_001

**Proves:** Legacy Full Verifier Signoff Completion

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_LEGACY_RELEASE_CELL_SIGNOFF_BACKFILL_LOCK_001

**Proves:** Legacy Signoff Backfill for 10 Canonical Cells

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_LEGACY_TEN_RELEASE_CELLS_SIGNOFF_BACKFILL_LOCK_002

**Proves:** Legacy Signoff Backfill for 10 Canonical Cells

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_LICENSE_SECURITY_SIGNING_POSTURE_DECISION_LOCK_001

**Proves:** DETERMINEX_LICENSE_SECURITY_SIGNING_POSTURE_DECISION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_LICENSE_SECURITY_SIGNING_ROUTE_EXECUTION_BOARD_LOCK_001

**Proves:** DETERMINEX_LICENSE_SECURITY_SIGNING_ROUTE_EXECUTION_BOARD_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_LINUX_CI_FRESH_INSTALL_CANDIDATE_PROOF_LOCK_001

**Proves:** Define the Linux CI fresh-install candidate path without claiming fresh install.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_LINUX_CI_FRESH_INSTALL_EXECUTION_LOCK_001

**Proves:** Execute Linux CI fresh-install path if available; otherwise emit exact runner/workflow blocker.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_LINUX_CLEAN_RUNNER_EXECUTION_LOCK_001

**Proves:** DETERMINEX_LINUX_CLEAN_RUNNER_EXECUTION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_LINUX_CLEAN_RUNNER_TOOLING_UNBLOCK_LOCK_001

**Proves:** DETERMINEX_LINUX_CLEAN_RUNNER_TOOLING_UNBLOCK_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_LIVE_REACT_PRODUCT_SHELL_DEMO_READINESS_FINAL_STATE_LOCK_001

**Proves:** Rung 5 (finale) of DETERMINEX_LIVE_REACT_PRODUCT_SHELL_DEMO_READINESS_SERIES.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_LIVE_REACT_UNIFIED_PRODUCT_SHELL_FINAL_STATE_LOCK_001

**Proves:** Rung 10 (finale) of DETERMINEX_LIVE_REACT_UNIFIED_PRODUCT_SHELL_SERIES.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_LOCAL_PACKAGE_DRY_RUN_BATCH_LOCK_001

**Proves:** DETERMINEX_LOCAL_PACKAGE_DRY_RUN_BATCH_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_LOCAL_PACKAGE_DRY_RUN_HARDENING_BATCH_LOCK_001

**Proves:** DETERMINEX_LOCAL_PACKAGE_DRY_RUN_HARDENING_BATCH_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_LOCAL_PREVIEW_EXACT_CELL_GATE_COMPLETION_OR_DEMOTION_LOCK_001

**Proves:** Local-Preview Exact Cell Gate Completion or Demotion

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_LOCAL_PREVIEW_PACKAGE_BOUNDARY_HARDENING_LOCK_001

**Proves:** Local Preview Package Boundary Hardening

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_LOCAL_PREVIEW_PACKAGE_PROMOTION_READINESS_WITHOUT_PROMOTION_LOCK_001

**Proves:** Local-Preview Package Promotion Readiness Without Promotion

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_LOCAL_PREVIEW_VS_RELEASE_SUPPORTED_BOUNDARY_LOCK_001

**Proves:** Local-Preview vs Release-Supported Boundary

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_LOCAL_PROOF_REPORT_EXPORT_CELL_CERTIFICATION_LOCK_001

**Proves:** Certify exact local_proof_report_export_cell if local proof report export evidence and exact operator approval pass.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_LOCAL_PROOF_REPORT_EXPORT_CELL_OPERATOR_APPROVAL_LOCK_001

**Proves:** Record exact-cell operator approval for local_proof_report_export_cell certification.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_LOCAL_RAG_QUERY_SMOKE_LOCK_001

**Proves:** Prove local companion RAG vector-index queryability without claiming answer quality.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_LOCAL_SMOKE_AFTER_BUILD_ARTIFACT_LOCK_001

**Proves:** Attempt bounded local smoke of the no-bundle Tauri release executable and record the early-exit blocker truthfully.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_LOCAL_SMOKE_AFTER_FASTEMBED_BINDING_RETRY_LOCK_001

**Proves:** Rebuild the Tauri release executable after local fastembed binding and record the bounded smoke retry blocker truthfully.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_LOCAL_SMOKE_AFTER_NSIS_ARTIFACT_LOCK_001

**Proves:** Verify the NSIS artifact hash and perform bounded metadata-only local smoke without installer execution.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MACHINE_AUTHORITY_PROMOTION_RULES_LOCK_001

**Proves:** DETERMINEX_MACHINE_AUTHORITY_PROMOTION_RULES_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MAINTENANCE_BAY_DRY_RUN_UPDATE_SPLASH_DEMO_LOCK_001

**Proves:** Execute the third verified splash path: a Python Maintenance Bay fixture with dry-run test configuration/documentation update, quarantined change, fixture-only compatibility workspace application, and compatibility verifier evidence.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MAINTENANCE_BAY_WORKFLOW_LOCK_001

**Proves:** Rung 4 of DETERMINEX_UNIFIED_PRODUCT_UX_SHELL_SERIES.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MARCH_DASHBOARD_ADMITTED_CLEAN_RUNNER_UPDATE_LOCK_001

**Proves:** March Dashboard Admitted Clean-Runner Update

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MATRIX_PROBE_RUNNER_LOCK_001

**Proves:** Create a no-network, no-Docker matrix probe plan/result model that separates missing setup from unsupported capability.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MAX_SAFE_FAMILY_BOUNDED_EXECUTION_LOCK_001

**Proves:** DETERMINEX_MAX_SAFE_FAMILY_BOUNDED_EXECUTION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MAX_SAFE_FAMILY_CAPABILITY_PROMOTION_LOCK_001

**Proves:** DETERMINEX_MAX_SAFE_FAMILY_CAPABILITY_PROMOTION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MAX_SAFE_FAMILY_CLEAN_GUI_INSTALLER_PREP_LOCK_001

**Proves:** DETERMINEX_MAX_SAFE_FAMILY_CLEAN_GUI_INSTALLER_PREP_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MAX_SAFE_FAMILY_EXECUTION_SELECTION_LOCK_001

**Proves:** DETERMINEX_MAX_SAFE_FAMILY_EXECUTION_SELECTION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MAX_SAFE_FAMILY_MARCH_PLAN_DASHBOARD_LOCK_001

**Proves:** DETERMINEX_MAX_SAFE_FAMILY_MARCH_PLAN_DASHBOARD_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MAX_SAFE_FAMILY_QUEUE_EXPANSION_LOCK_001

**Proves:** DETERMINEX_MAX_SAFE_FAMILY_QUEUE_EXPANSION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MAX_SAFE_FAMILY_REPAIR_RERUN_LOOP_LOCK_001

**Proves:** DETERMINEX_MAX_SAFE_FAMILY_REPAIR_RERUN_LOOP_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MAX_SAFE_FAMILY_SBOM_GATE_RECONCILIATION_LOCK_001

**Proves:** DETERMINEX_MAX_SAFE_FAMILY_SBOM_GATE_RECONCILIATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MAX_SAFE_FAMILY_SBOM_ONE_TIME_SPEND_LOCK_001

**Proves:** DETERMINEX_MAX_SAFE_FAMILY_SBOM_ONE_TIME_SPEND_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MAX_SAFE_FAMILY_SBOM_PACKET_RUNTIME_ADMISSION_LOCK_001

**Proves:** DETERMINEX_MAX_SAFE_FAMILY_SBOM_PACKET_RUNTIME_ADMISSION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MAX_SAFE_FAMILY_SBOM_POST_SPEND_VERIFICATION_LOCK_001

**Proves:** DETERMINEX_MAX_SAFE_FAMILY_SBOM_POST_SPEND_VERIFICATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MAX_SAFE_FAMILY_SBOM_SCOPED_EXECUTION_LOCK_001

**Proves:** DETERMINEX_MAX_SAFE_FAMILY_SBOM_SCOPED_EXECUTION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MAX_SAFE_FAMILY_SCORE_DISCIPLINE_LOCK_001

**Proves:** DETERMINEX_MAX_SAFE_FAMILY_SCORE_DISCIPLINE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MEANINGFUL_GUI_FLOW_IDEA_LAB_PROMPT_TO_PLAN_PROOF_LOCK_001

**Proves:** DETERMINEX_MEANINGFUL_GUI_FLOW_IDEA_LAB_PROMPT_TO_PLAN_PROOF_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MEANINGFUL_GUI_FLOW_PRIORITY_CLAUDE_REVIEW_001

**Proves:** Overnight Lane 4. Meaningful GUI flow priority. 8 flows ranked. 4 of 8 panels in repo; 4 missing. Top 3 recommended: PB cockpit + WAL render + Idea Lab plan.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MEANINGFUL_GUI_FLOW_PROGRAMBENCH_COCKPIT_PROOF_LOCK_001

**Proves:** DETERMINEX_MEANINGFUL_GUI_FLOW_PROGRAMBENCH_COCKPIT_PROOF_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MERGE_POINT_FINAL_STATE_LOCK_001

**Proves:** Write the non-authorizing merge-point final state after Claude remediation and Codex queue/graph remediation.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MINIMUM_GUI_FLOW_PROOF_CONTRACT_AND_FIRST_PAINT_SMOKE_LOCK_001

**Proves:** Define desktop_gui_e2e_proven versus lesser first-paint smoke proof, and block first-paint execution on driver admission.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ML_INFERENCE_AUTHORITY_GATE_LOCK_001

**Proves:** ML Inference Authority Gate

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MOBILE_NATIVE_AUTHORITY_GATE_LOCK_001

**Proves:** Mobile Native Authority Gate

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MSEDGEDRIVER_ADMISSION_AFTER_REAL_SIGNATURE_LOCK_001

**Proves:** DETERMINEX_MSEDGEDRIVER_ADMISSION_AFTER_REAL_SIGNATURE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MSEDGEDRIVER_ADMISSION_EXECUTION_IF_SIGNED_LOCK_001

**Proves:** DETERMINEX_MSEDGEDRIVER_ADMISSION_EXECUTION_IF_SIGNED_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MSEDGEDRIVER_ADMISSION_WITH_RUNTIME_APPROVAL_LOCK_001

**Proves:** DETERMINEX_MSEDGEDRIVER_ADMISSION_WITH_RUNTIME_APPROVAL_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MSEDGEDRIVER_BOUNDED_DOWNLOAD_OPERATOR_APPROVAL_LOCK_001

**Proves:** Gate msedgedriver bounded download on exact signed operator approval, source URL, version, and SHA-256 integrity requirements.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MSEDGEDRIVER_GUI_FIRST_PAINT_READINESS_CLAUDE_REVIEW_001

**Proves:** Overnight Lane 3. msedgedriver + first-paint readiness. 12 gates: 2 PASSED + 3 PARTIAL + 1 BLOCKED + 5 NOT_STARTED + 1 MISSING.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MSFG_CLAUDE_EVIDENCE_INDEX_GUARDS_REVIEW_001

**Proves:** MSFG Claude Lane AF. Evidence index clean; guards hold.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MSFG_CLAUDE_EXACT_LOCAL_NOT_FAMILY_SUPPORT_REVIEW_001

**Proves:** MSFG Claude Lane N. Exact-local NOT framed as family support.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MSFG_CLAUDE_FAMILIES_EXECUTED_REVIEW_001

**Proves:** MSFG Claude Lane E. 5 families executed.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MSFG_CLAUDE_FAMILIES_SELECTED_REVIEW_001

**Proves:** MSFG Claude Lane D. 5 families selected.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MSFG_CLAUDE_FAMILY_MAP_COVERAGE_REVIEW_001

**Proves:** MSFG Claude Lane A. 31-family map covered with current state rows.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MSFG_CLAUDE_FAMILY_PROMOTIONS_REVIEW_001

**Proves:** MSFG Claude Lane M. 5 EXACT_LOCAL_CAPABILITY promotions; family_support_claimed=false on each.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MSFG_CLAUDE_FAMILY_REPAIR_DISCIPLINE_REVIEW_001

**Proves:** MSFG Claude Lane G. 0 repairs needed (verification passed); discipline guard in place.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MSFG_CLAUDE_FAMILY_SELECTION_REVIEW_001

**Proves:** MSFG Claude Lane C. Max safe execution selection no-install/no-authority.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MSFG_CLAUDE_FAMILY_TRANSCRIPT_REVIEW_001

**Proves:** MSFG Claude Lane F. Family transcripts exist.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MSFG_CLAUDE_FAMILY_VERIFICATION_VERDICTS_REVIEW_001

**Proves:** MSFG Claude Lane L. 5 verifications PASSED, all evidence-bound.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MSFG_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001

**Proves:** MSFG Claude Lane AG. 16 forbidden actions avoided.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MSFG_CLAUDE_FULL_STATUS_TIMEOUT_REVIEW_001

**Proves:** MSFG Claude Lane AE. Full-status timeout collect-only; 9587 tests; no tests disabled.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MSFG_CLAUDE_MARCH_PLAN_DASHBOARD_REVIEW_001

**Proves:** MSFG Claude Lane AD. March-plan dashboard accurate.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MSFG_CLAUDE_NEW_STATUS_SUMMARY_REVIEW_001

**Proves:** MSFG Claude Lane Q. New status summary: LV 13, SM 3, AR 5, TM 5, VR 4, UN 1.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MSFG_CLAUDE_NONLV_FAMILY_NEXT_ACTION_REVIEW_001

**Proves:** MSFG Claude Lane B. Every non-LV family has active next action.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MSFG_CLAUDE_NO_BINARY_MUTATION_REVIEW_001

**Proves:** MSFG Claude Lane J. Binaries not mutated.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MSFG_CLAUDE_NO_LOCKFILE_MUTATION_REVIEW_001

**Proves:** MSFG Claude Lane K. Package/lockfile not mutated without spend.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MSFG_CLAUDE_NO_TEST_MUTATION_REVIEW_001

**Proves:** MSFG Claude Lane H. Tests not mutated.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MSFG_CLAUDE_NO_UNIVERSAL_SUPPORT_REVIEW_001

**Proves:** MSFG Claude Lane O. No universal support claim.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MSFG_CLAUDE_NO_VERIFIER_MUTATION_REVIEW_001

**Proves:** MSFG Claude Lane I. Verifiers/oracles not weakened.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MSFG_CLAUDE_OTHER_PACKETS_NOT_EXECUTED_REVIEW_001

**Proves:** MSFG Claude Lane AA. Clean-host/GUI/installer/beta-dashboard not executed.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MSFG_CLAUDE_PREVIOUS_STATUS_SUMMARY_REVIEW_001

**Proves:** MSFG Claude Lane P. Previous status summary correct.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MSFG_CLAUDE_RELEASE_INVARIANTS_REVIEW_001

**Proves:** MSFG Claude Lane AB. Release cells 10/10; families 0/0 canonical.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MSFG_CLAUDE_REMAINING_NONLV_COUNT_REVIEW_001

**Proves:** MSFG Claude Lane R. Remaining non-LV families = 18.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MSFG_CLAUDE_RUNTIME_QUEUE_REVIEW_001

**Proves:** MSFG Claude Lane S. Runtime queue 1→2 (SBOM admission).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MSFG_CLAUDE_SBOM_BLOCKER_HONEST_REVIEW_001

**Proves:** MSFG Claude Lane Y. TOOL_MISSING blocker honest; no Syft pretend.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MSFG_CLAUDE_SBOM_EXECUTION_REVIEW_001

**Proves:** MSFG Claude Lane X. SBOM execution TOOL_MISSING_BLOCKER; no fake output.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MSFG_CLAUDE_SBOM_PACKET_REVIEW_001

**Proves:** MSFG Claude Lane U. SBOM packet validation correct.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MSFG_CLAUDE_SBOM_QUEUE_ADMISSION_REVIEW_001

**Proves:** MSFG Claude Lane V. SBOM queue admission correct.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MSFG_CLAUDE_SBOM_SPEND_REUSE_REVIEW_001

**Proves:** MSFG Claude Lane Z. SBOM spend reuse rejected.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MSFG_CLAUDE_SBOM_SPEND_REVIEW_001

**Proves:** MSFG Claude Lane W. SBOM spend consumed exactly one queue entry.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MSFG_CLAUDE_SCORE_MOVEMENT_EVIDENCE_BOUND_REVIEW_001

**Proves:** MSFG Claude Lane AC. Score movements evidence-bound.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MSFG_CLAUDE_SIGNED_SPEND_REVIEW_001

**Proves:** MSFG Claude Lane T. Signed spend 1→2 (SBOM spend).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MSFG_CLAUDE_SYNTHESIS_REVIEW_001

**Proves:** MSFG Claude Lane AH. Synthesis + 61-item final report.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_MULTI_FAMILY_REPAIR_EXPANSION_LOCK_001

**Proves:** DETERMINEX_MULTI_FAMILY_REPAIR_EXPANSION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_NATIVE_WEBDRIVER_ADMISSION_FOR_TAURI_DRIVER_LOCK_001

**Proves:** Admit or route the native WebDriver binary required by the tauri-driver GUI e2e path.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_NEXT_CHEAP_RELEASE_CELL_CANDIDATE_QUEUE_LOCK_001

**Proves:** Rank cheap next release-cell candidates and queue cells 2, 3, and 4 without certifying release support.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_NEXT_HARD_FLOOR_AUTHORITY_PACKET_SELECTION_LOCK_001

**Proves:** DETERMINEX_NEXT_HARD_FLOOR_AUTHORITY_PACKET_SELECTION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_NEXT_HARD_FLOOR_PACKET_AFTER_FIRST_SPEND_LOCK_001

**Proves:** DETERMINEX_NEXT_HARD_FLOOR_PACKET_AFTER_FIRST_SPEND_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_NEXT_WAVE_CLAUDE_AUTHORITY_BOUNDARY_PRESERVATION_REVIEW_001

**Proves:** Next-wave Claude Lane L. All 8 Codex lanes authority/protected_external_action=false; signed_queue=0; audit unchanged; 20-wave boundary check.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_NEXT_WAVE_CLAUDE_FAMILY_SUPPORT_PROMOTION_REVIEW_001

**Proves:** Next-wave Claude Lane J. 0 families promoted; release_supported_families remains 0; every required gate must close before any family-support promotion.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_NEXT_WAVE_CLAUDE_FIRST_SPEND_SYNTHESIS_REVIEW_001

**Proves:** Next-wave Claude Lane Q. Synthesis + 29-item final report. Codex correctly did NOT spend without signed approval. React/Vite remains blocked. Baseline reconciled. Hard floor held 20 waves. Next wave: import real signature.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_NEXT_WAVE_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001

**Proves:** Next-wave Claude Lane M. No ProgramBench / no training rows / no real-user mutation / no public upload / no install / no GUI / no installer / no protected execution / no universal support / no release/production ready claims.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_NEXT_WAVE_CLAUDE_NEXT_HARD_FLOOR_PACKET_REVIEW_001

**Proves:** Next-wave Claude Lane I. Next-packet ranking selected React/Vite again (rank-1 of risk/value/proof/rollback); selection rational; SBOM/clean-host/GUI/installer candidates ranked below.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_NEXT_WAVE_CLAUDE_REACT_VITE_ADMISSION_VERDICT_REVIEW_001

**Proves:** Next-wave Claude Lane F. REACT_VITE_DEPENDENCY_ADMISSION_NO_SPEND_BLOCKED — no execution; dependency state not changed; no broad install / no GUI / no installer.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_NEXT_WAVE_CLAUDE_REACT_VITE_PACKET_VALIDATION_REVIEW_001

**Proves:** Next-wave Claude Lane C. PACKET_COMPLETE_UNSIGNED_NO_SPEND_AUTHORITY; 12 required fields present; 0 signer admissions; typed blocker BLOCKED_NO_REAL_SIGNATURE emitted.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_NEXT_WAVE_CLAUDE_REACT_VITE_TRANSCRIPT_REVIEW_001

**Proves:** Next-wave Claude Lane G. REACT_VITE_LOCAL_TRANSCRIPT_BLOCKED_NO_ADMISSION; no transcript claimed without execution; family stays typed-blocked.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_NEXT_WAVE_CLAUDE_SCORE_BASELINE_RECONCILIATION_REVIEW_001

**Proves:** Next-wave Claude Lane B. Mismatch I flagged is RESOLVED: shorthand drift in Claude-synthesis payload, not evidence-delta error. Continuity proven (all 5 scores). Source-of-truth chain documented.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_NEXT_WAVE_CLAUDE_SCORE_MOVEMENT_EVIDENCE_REVIEW_001

**Proves:** Next-wave Claude Lane K. Scores unchanged (no movement claimed). Baseline reconciliation does not constitute a score rise. score_delta_guard updated.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_NEXT_WAVE_CLAUDE_SIGNED_APPROVAL_VERDICT_REVIEW_001

**Proves:** Next-wave Claude Lane D. signed_valid_queue=0 (verified); no signed approval imported across 20 waves; exact_missing fields = signed_operator_approval + signed_valid_queue_record.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_NEXT_WAVE_CLAUDE_SIGNED_SPEND_COUNT_REVIEW_001

**Proves:** Next-wave Claude Lane E. signed_spend before=0 after=0 (no change); marker authority_boundary confirms signed_spend=0; D lane verdict NO_SPEND_BLOCKED.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_NEXT_WAVE_CLAUDE_TIER1_COVERAGE_REVIEW_001

**Proves:** Next-wave Claude Lane H. Tier-1 coverage did NOT inflate. Verified count and typed-blocked count unchanged from overnight. react_vite + tauri still typed-blocked.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_NEXT_WAVE_CLAUDE_TIMER_AND_MARKER_REVIEW_001

**Proves:** Next-wave Claude Lane A. Timer protocol applied; marker schema+draft+final present; ready=true; reviewed commit reachable; marker policy honored.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_NEXT_WAVE_REVIEW_READY_PROTOCOL_LOCK_001

**Proves:** DETERMINEX_NEXT_WAVE_REVIEW_READY_PROTOCOL_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_NIGHT_CLAUDE_OVERNIGHT_FINAL_SYNTHESIS_001

**Proves:** Final overnight synthesis. All 16 lanes + 3 prior syntheses. 30 top deltas; morning report ready.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_NIGHT_CLAUDE_SYNTHESIS_AND_CODEX_PRESSURE_QUEUE_001

**Proves:** Overnight Synthesis 1 (after lanes 1-5). 30 ranked Codex deltas; 20+20+20 blockers; 10 claim risks; 5 next Claude lanes.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_NIGHT_CLAUDE_SYNTHESIS_AND_CODEX_PRESSURE_QUEUE_002

**Proves:** Overnight Synthesis 2 (after lanes 6-10). 30 next deltas; 6 next Claude lanes.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_NIGHT_CLAUDE_SYNTHESIS_AND_CODEX_PRESSURE_QUEUE_003

**Proves:** Overnight Synthesis 3 (after lanes 11-15). 15 next ranked deltas.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_NIGHT_GULP_RECONCILIATION_LOCK_001

**Proves:** DETERMINEX_NIGHT_GULP_RECONCILIATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_NIGHT_GULP_RECONCILIATION_LOCK_002

**Proves:** DETERMINEX_NIGHT_GULP_RECONCILIATION_LOCK_002

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_NIGHT_GULP_RECONCILIATION_LOCK_003

**Proves:** DETERMINEX_NIGHT_GULP_RECONCILIATION_LOCK_003

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_NIGHT_GULP_RECONCILIATION_LOCK_004

**Proves:** DETERMINEX_NIGHT_GULP_RECONCILIATION_LOCK_004

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_NONCODER_PRODUCT_REPORT_COMPLETION_LOCK_001

**Proves:** DETERMINEX_NONCODER_PRODUCT_REPORT_COMPLETION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_NONCODER_PROGRAM_AUTHORITY_REPORT_LOCK_002

**Proves:** DETERMINEX_NONCODER_PROGRAM_AUTHORITY_REPORT_LOCK_002

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_NONCODER_PROGRAM_PROOF_REPORT_LOCK_001

**Proves:** DETERMINEX_NONCODER_PROGRAM_PROOF_REPORT_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_NONCODER_RELEASE_READINESS_REPORT_LOCK_001

**Proves:** DETERMINEX_NONCODER_RELEASE_READINESS_REPORT_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_NONCODER_REPORT_RENDERED_OUTPUTS_VERIFIED_LOCK_001

**Proves:** DETERMINEX_NONCODER_REPORT_RENDERED_OUTPUTS_VERIFIED_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_NO_SUCCESS_WITHOUT_VERIFIER_POLICY_LOCK_001

**Proves:** Apply no success without verifier across creation, existing-repo repair, maintenance, learning, and proof/operator surfaces.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_NSIS_BOUNDED_EXTRACT_OR_OPERATOR_INSTALL_UNINSTALL_LOCK_001

**Proves:** Reverify the NSIS artifact, probe bounded extraction, and prepare operator install/uninstall packet without executing the installer.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_NSIS_INSTALLER_EXECUTION_READINESS_CLAUDE_REVIEW_001

**Proves:** Overnight Lane 2. NSIS execution readiness. 12 layers: 2 PASSED + 1 BLOCKED + 6 NOT_STARTED + 3 MISSING.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_NSIS_INSTALL_SMOKE_EXECUTION_IF_SIGNED_LOCK_001

**Proves:** DETERMINEX_NSIS_INSTALL_SMOKE_EXECUTION_IF_SIGNED_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_NSIS_INSTALL_SMOKE_WITH_RUNTIME_APPROVAL_LOCK_001

**Proves:** DETERMINEX_NSIS_INSTALL_SMOKE_WITH_RUNTIME_APPROVAL_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_NSIS_OPERATOR_APPROVED_INSTALL_LAUNCH_UNINSTALL_SMOKE_LOCK_001

**Proves:** Reverify NSIS artifact and execute bounded install/launch/uninstall only if exact single-event operator approval exists.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_NSIS_OPERATOR_APPROVED_INSTALL_UNINSTALL_SMOKE_LOCK_001

**Proves:** Verify NSIS artifact and run bounded install/launch/uninstall/cleanup only if explicit operator approval evidence exists.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_NSIS_SINGLE_EVENT_APPROVAL_AND_INSTALL_LAUNCH_UNINSTALL_EXECUTION_LOCK_001

**Proves:** Run bounded NSIS install, launch smoke, uninstall, and cleanup only after exact signed single-event operator approval.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OARG_CLAUDE_APPEND_ONLY_COUNT_DRIFT_GUARDS_REVIEW_001

**Proves:** OARG Claude Lane T. Append-only and count-drift guards hold.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OARG_CLAUDE_BETA_DASHBOARD_NO_PUBLIC_RELEASE_REVIEW_001

**Proves:** OARG Claude Lane O. Beta dashboard NOT publicly published (NOT_READY_BLOCKED_BY_REQUIRED_GATES).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OARG_CLAUDE_CLAIM_SCANNER_OVERCLAIM_REVIEW_001

**Proves:** OARG Claude Lane U. Claim scanner + Day 1 overclaim scanner pass.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OARG_CLAUDE_CLEAN_HOST_IN_SCOPE_OR_BLOCKED_REVIEW_001

**Proves:** OARG Claude Lane L. Clean-host stayed in scope OR honestly blocked (packet certified; execution blocked).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OARG_CLAUDE_DIRTY_STATE_REPORTED_REVIEW_001

**Proves:** OARG Claude Lane Y. Dirty/untracked state reported (0 pre-Claude).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OARG_CLAUDE_EVIDENCE_INDEX_CLEAN_REVIEW_001

**Proves:** OARG Claude Lane S. Evidence index validates clean at 1346 entries.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OARG_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001

**Proves:** OARG Claude Lane Z. All forbidden actions audited and avoided per marker.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OARG_CLAUDE_GUI_BUILD_IN_SCOPE_OR_BLOCKED_REVIEW_001

**Proves:** OARG Claude Lane M. GUI/build stayed in scope OR honestly blocked (packet certified; execution blocked).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OARG_CLAUDE_INSTALLER_RELEASE_IN_SCOPE_OR_BLOCKED_REVIEW_001

**Proves:** OARG Claude Lane N. Installer/release stayed in scope OR honestly blocked (prereqs blocked).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OARG_CLAUDE_NO_FAKE_SIGNATURE_OR_APPROVAL_REVIEW_001

**Proves:** OARG Claude Lane C. No fake signature or fake approval was created.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OARG_CLAUDE_NO_FAMILY_SUPPORT_CLAIM_REVIEW_001

**Proves:** OARG Claude Lane Q. No family-support claim made.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OARG_CLAUDE_NO_PROTECTED_ACTION_WITHOUT_PACKET_SPEND_REVIEW_001

**Proves:** OARG Claude Lane I. No protected action executed without packet+spend.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OARG_CLAUDE_NO_RELEASE_READY_WITHOUT_GATES_REVIEW_001

**Proves:** OARG Claude Lane P. No release-ready claim made; required gates not all passed.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OARG_CLAUDE_NO_VALIDATOR_BYPASS_REVIEW_001

**Proves:** OARG Claude Lane B. No validator bypass occurred.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OARG_CLAUDE_OP_AUTH_MATERIALIZED_AS_MACHINE_CHECKABLE_REVIEW_001

**Proves:** OARG Claude Lane A. Op authorization materialized as scoped machine-checkable packets, not blanket approval.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OARG_CLAUDE_PACKETS_SCOPED_ONE_ACTION_REVIEW_001

**Proves:** OARG Claude Lane D. Each packet scoped to one protected action.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OARG_CLAUDE_PACKET_HASH_BINDING_REVIEW_001

**Proves:** OARG Claude Lane E. Each packet has deterministic hash binding.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OARG_CLAUDE_QUEUE_ONLY_FROM_VALID_PACKETS_REVIEW_001

**Proves:** OARG Claude Lane G. Queue entries created only from valid packets (0 queued; 0 invalid admissions).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OARG_CLAUDE_REACT_VITE_IN_SCOPE_REVIEW_001

**Proves:** OARG Claude Lane J. React/Vite admission stayed in scope (packet certified; execution blocked).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OARG_CLAUDE_REJECTION_CORPUS_COVERAGE_REVIEW_001

**Proves:** OARG Claude Lane F. Rejection corpus covers template/stale/blanket/wrong-scope/replay/hash mismatch/malformed.

**Does not prove:** Does not prove corpus balance, training effectiveness, or public benchmark dominance by itself.

#### DETERMINEX_OARG_CLAUDE_RELEASE_CELLS_CANONICAL_REVIEW_001

**Proves:** OARG Claude Lane V. release_supported_exact_cells: 10 (canonical).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OARG_CLAUDE_RELEASE_FAMILIES_CANONICAL_REVIEW_001

**Proves:** OARG Claude Lane W. release_supported_families: 0 (canonical).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OARG_CLAUDE_SBOM_IN_SCOPE_OR_BLOCKED_REVIEW_001

**Proves:** OARG Claude Lane K. SBOM stayed in scope OR honestly blocked (packet certified; execution blocked).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OARG_CLAUDE_SCORE_CHANGES_EVIDENCE_BOUND_REVIEW_001

**Proves:** OARG Claude Lane X. Score changes evidence-bound; rejected/no movement this wave.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OARG_CLAUDE_SPEND_ONE_TIME_USE_REVIEW_001

**Proves:** OARG Claude Lane H. Spend consumed exactly one queue entry each (N/A: 0 spends).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OARG_CLAUDE_SYNTHESIS_REVIEW_001

**Proves:** OARG Claude Lane AA. Synthesis + 42-item final report.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OARG_CLAUDE_TIMEOUT_NOT_HIDDEN_BY_SKIPS_REVIEW_001

**Proves:** OARG Claude Lane R. Full-status timeout repair plan recorded; no tests disabled/skipped/erased.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OMG_DEMO_EXECUTION_METHODOLOGY_RECONCILIATION_LOCK_001

**Proves:** DETERMINEX_OMG_DEMO_EXECUTION_METHODOLOGY_RECONCILIATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OMG_DEMO_PATH_END_TO_END_SCRIPT_LOCK_001

**Proves:** Define the full user-facing OMG demo path and exact blockers without claiming it has passed.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OMG_DEMO_PATH_EXECUTION_CLAUDE_REVIEW_002

**Proves:** Overnight Lane 15. OMG demo execution 2nd pass. Codex 81.8% (packet); Claude 43.6% (execution). 0 user-executable.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OMG_DEMO_PATH_EXECUTION_LOCK_002

**Proves:** DETERMINEX_OMG_DEMO_PATH_EXECUTION_LOCK_002

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OMG_DEMO_SCORE_METHODOLOGY_ATTACK_REVIEW_CLAUDE_001

**Proves:** Wave 007 Claude Lane O. Codex packet score vs user-executable vs proof-backed vs investor-demo vs public-reveal. Separate score fields; unlock conditions per field; '86%' overclaim audit.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OMG_FIVE_FIELD_SCORE_SCHEMA_AND_QUOTING_LINTER_LOCK_001

**Proves:** DETERMINEX_OMG_FIVE_FIELD_SCORE_SCHEMA_AND_QUOTING_LINTER_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OMG_FIVE_FIELD_SCORE_TIGHTENING_LOCK_001

**Proves:** DETERMINEX_OMG_FIVE_FIELD_SCORE_TIGHTENING_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OMG_SCORE_DEFINITION_BINDING_AND_LINTER_EXPANSION_LOCK_001

**Proves:** DETERMINEX_OMG_SCORE_DEFINITION_BINDING_AND_LINTER_EXPANSION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ONNXRUNTIME_LOCAL_IMPORT_LIB_GENERATION_LOCK_001

**Proves:** Generate a local ONNX Runtime Windows import library from the existing local wheel DLL without fetching, installing, or proving release build success.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ONNXRUNTIME_NATIVE_LINKAGE_REQUIREMENTS_LOCK_001

**Proves:** Normalize ONNX Runtime native linkage requirements without generating binaries or granting release support.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ONNXRUNTIME_RUNTIME_API_ALIGNMENT_LOCK_001

**Proves:** Align the runtime ONNX Runtime API used by fastembed with the ort crate API 23 requirement through local DLL co-location.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OPEN_AVAILABILITY_ASCENT_MASTER_PLAN_LOCK_001

**Proves:** Create the canonical open-availability ascent plan without granting release authority.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OPEN_AVAILABILITY_PARALLEL_RELEASE_CRITIQUE_AND_CLAUDE_QUEUE_001

**Proves:** Parallel-acceleration audit while Codex pushes GUI/build/capability proof locks. Identifies the shortest path to open availability without fake claims; emits concrete handoff artifacts (Codex consolidation queue, claim-scanner refresh queue, public docs/license/security deltas, capability gap critique, first release-supported cell + first support-depth promotion candidate reviews, GUI e2e evidence packet review).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OPERATOR_ACTION_PACKET_FOR_FIRST_SPEND_LOCK_001

**Proves:** DETERMINEX_OPERATOR_ACTION_PACKET_FOR_FIRST_SPEND_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OPERATOR_APPROVAL_SIGNATURE_LEDGER_GENERALIZATION_LOCK_001

**Proves:** Generalize the Wave004 operator decision ledger into a signature-capable approval ledger with exact per-lane approval resolution.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OPERATOR_AUTHORITY_RELEASE_GATE_RECONCILIATION_LOCK_001

**Proves:** DETERMINEX_OPERATOR_AUTHORITY_RELEASE_GATE_RECONCILIATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OPERATOR_AUTHORIZATION_MATERIALIZATION_LOCK_001

**Proves:** DETERMINEX_OPERATOR_AUTHORIZATION_MATERIALIZATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OPERATOR_DECISION_LEDGER_AND_SINGLE_EVENT_APPROVAL_LOCK_001

**Proves:** Create a central non-inheriting operator-decision ledger schema and single-event approval template.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OPERATOR_SIGNATURE_CAPTURE_MECHANISM_COMPLETION_LOCK_001

**Proves:** DETERMINEX_OPERATOR_SIGNATURE_CAPTURE_MECHANISM_COMPLETION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OPERATOR_SIGNATURE_CAPTURE_MECHANISM_LOCK_001

**Proves:** DETERMINEX_OPERATOR_SIGNATURE_CAPTURE_MECHANISM_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OPERATOR_SIGNATURE_CAPTURE_MECHANISM_LOCK_002

**Proves:** DETERMINEX_OPERATOR_SIGNATURE_CAPTURE_MECHANISM_LOCK_002

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OPERATOR_SIGNATURE_DELIVERY_CHANNEL_LOCK_001

**Proves:** DETERMINEX_OPERATOR_SIGNATURE_DELIVERY_CHANNEL_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OPERATOR_SIGNATURE_MATERIAL_TEMPLATE_LOCK_001

**Proves:** DETERMINEX_OPERATOR_SIGNATURE_MATERIAL_TEMPLATE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OPERATOR_SIGNATURE_MATERIAL_VALIDATOR_LOCK_001

**Proves:** DETERMINEX_OPERATOR_SIGNATURE_MATERIAL_VALIDATOR_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OPERATOR_SIGNATURE_MECHANISM_ATTACK_REVIEW_CLAUDE_001

**Proves:** Wave 007 Claude Lane X. Operator signature mechanism — signer identity, hash binding, expiration, revocation, audit log, allowed/forbidden, rollback, detector, inheritance blocker, simulated-vs-real distinction.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OPERATOR_SIGNATURE_MECHANISM_CLAUDE_REVIEW_001

**Proves:** Overnight Lane 1. Operator signature mechanism audit. 9 of 10 requirements UNSATISFIED. 4 packets blocked on this single layer.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OPERATOR_TOOL_ACQUISITION_AUTHORIZATION_LOCK_001

**Proves:** DETERMINEX_OPERATOR_TOOL_ACQUISITION_AUTHORIZATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OPTIONAL_REAL_SIGNATURE_QUEUE_IMPORT_LOCK_001

**Proves:** DETERMINEX_OPTIONAL_REAL_SIGNATURE_QUEUE_IMPORT_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OPTIONAL_VECTOR_ENGINE_STARTUP_GUARD_LOCK_001

**Proves:** Make vector engine startup optional so app startup can be proven while ONNX Runtime API alignment remains blocked.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ORACLE_REGISTRY_COMPLETION_LOCK_001

**Proves:** DETERMINEX_ORACLE_REGISTRY_COMPLETION_LOCK_001

**Does not prove:** Does not prove broad real-world repair coverage beyond the locked acceptance tests.

#### DETERMINEX_OVERNIGHT_BROWSER_TAURI_GUI_PACKET_STAGE_LOCK_001

**Proves:** Browser extension and Tauri/Electron GUI-build packet staging without execution.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OVERNIGHT_CLAIM_SCANNER_PUBLIC_NARRATIVE_HARDENING_LOCK_001

**Proves:** Day-one claim scanner hardening for supplement overclaims without public launch or release claims.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OVERNIGHT_CLAUDE_ALL_FAMILY_ADAPTER_STUB_COVERAGE_REVIEW_001

**Proves:** Overnight Claude Lane D. 31 families with adapter or typed blocker; missing_capability_matrix + claim boundary + next proof rung per family. Reject silent gaps.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OVERNIGHT_CLAUDE_AUTHORITY_BOUNDARY_PRESERVATION_REVIEW_001

**Proves:** Overnight Claude Lane N. AUTHORITY_FALSE across all lanes; signed_queue=0; audit log unchanged-or-append-only; no protected execution observed. 19-wave boundary check.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OVERNIGHT_CLAUDE_CURRENT_STATE_SOURCE_TRUTH_REVIEW_001

**Proves:** Overnight Claude Lane B. HEAD + spine + registry + family universe + signed queue + SBOM/clean-host/GUI/installer state. Reject stale numbers.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OVERNIGHT_CLAUDE_DAY1_IDE_DASHBOARD_REVIEW_001

**Proves:** Overnight Claude Lane J. 31-family structural + Tier-1 transcript + adapter + oracle + repair + Idea Lab + Repo Clinic + noncoder + blockers + cells + families + boundary + next rungs. Unsafe wording rejected.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OVERNIGHT_CLAUDE_EXTERNAL_AUTHORITY_PACKET_REVIEW_001

**Proves:** Overnight Claude Lane L. Hard-floor unlock packet with target/commands/scope/rollback/timeout/files/risk/signer/no-spend-before-signature. Reject packet-as-authority.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OVERNIGHT_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001

**Proves:** Overnight Claude Lane O. No ProgramBench run / no training rows / no real-user repo mutation / no public upload / no installs / no GUI / no installer / no protected execution / no universal support / no release ready / no production ready claims.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OVERNIGHT_CLAUDE_IDEA_LAB_E2E_PIPELINE_REVIEW_001

**Proves:** Overnight Claude Lane F. Idea Lab: ProgramBrief + ProgramParts + family + file plan + acceptance/test/smoke + implementation + blocked + decisions + ProgramAuthorityRecord + report.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OVERNIGHT_CLAUDE_MULTI_FAMILY_REPAIR_EXPANSION_REVIEW_001

**Proves:** Overnight Claude Lane H. ≥3 family bounded repair fixtures with failing/transcript/repair-diff/post-transcript/fake-rejection/boundary. Reject failed-repair-as-support.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OVERNIGHT_CLAUDE_NONCODER_PRODUCT_REPORT_REVIEW_001

**Proves:** Overnight Claude Lane I. Reports per major flow with required sections, derived from records. Reject hand-written.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OVERNIGHT_CLAUDE_ORACLE_REGISTRY_COMPLETION_REVIEW_001

**Proves:** Overnight Claude Lane E. Oracle roles per family (detect/parse/build/test/smoke/repair/promotion/clean-host/release). Reject command map as execution.

**Does not prove:** Does not prove broad real-world repair coverage beyond the locked acceptance tests.

#### DETERMINEX_OVERNIGHT_CLAUDE_OVERCLAIM_SCANNER_HARDENING_REVIEW_001

**Proves:** Overnight Claude Lane K. Rejection rules for 11+ unsafe phrases; allowed safe wording; status guard binding. Reject any path where unsafe wording would pass.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OVERNIGHT_CLAUDE_REPO_CLINIC_E2E_PIPELINE_REVIEW_001

**Proves:** Overnight Claude Lane G. Repo Clinic: detect + classify + safe-commands + blockers + safe-checks + failure-transcript + repair-candidate + verify + reject-fake + record + report. Reject real-user repo mutation.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OVERNIGHT_CLAUDE_REVIEW_READY_PROTOCOL_REVIEW_001

**Proves:** Overnight Claude Lane A. Marker schema + draft + final marker + ready=true + reviewed commit reachable; Claude wait + recheck cadence + no stale review.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OVERNIGHT_CLAUDE_SCORE_MOVEMENT_EVIDENCE_REVIEW_001

**Proves:** Overnight Claude Lane M. Each score delta cites evidence; score_guard rejects local-only-as-clean-host, structural-as-family, packet-only-as-packaging, stale-snapshot, packet-only-rise.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OVERNIGHT_CLAUDE_TIER1_PROGRAM_FAMILY_COVERAGE_REVIEW_001

**Proves:** Overnight Claude Lane C. Tier-1 family completion: canonical row, adapter, detector, oracle, command map, transcript-or-typed-blocker. Reject install without signed approval.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OVERNIGHT_CLAUDE_UNDER_THE_HOOD_SYNTHESIS_REVIEW_001

**Proves:** Overnight Claude Lane Q. Synthesis + 31-item final report. 15 attack lanes confirmed; overnight push moves Determinex materially closer to Day 1 IDE substrate without crossing unsupported authority boundaries.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OVERNIGHT_CLEAN_RUNNER_SBOM_CONTINUITY_LOCK_001

**Proves:** Fresh T: admitted clean-runner SBOM byte continuity retry.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OVERNIGHT_COMPANION_RAG_BOUNDARY_RECHECK_LOCK_001

**Proves:** Reverify Companion RAG citation/refusal boundary during the overnight sprint without behavior changes, score movement, release support, or readiness claims.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OVERNIGHT_COORDINATION_STATUS_LOCK_001

**Proves:** Shared overnight coordination status and no-overclaim boundary.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OVERNIGHT_FULL_STATUS_SEGMENT_EXECUTION_LOCK_001

**Proves:** Bounded family/known-world full-status segment execution without full-suite pass claim.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OVERNIGHT_HIGH_RISK_FAMILY_AUTHORITY_PACKET_LOCK_001

**Proves:** ML/mobile/hardware/Kotlin/Swift authority packets and exact blockers without installs, downloads, drivers, or promotion.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OVERNIGHT_INSTALLER_RELEASE_PACKET_PREPARATION_LOCK_001

**Proves:** Installer/release packet preparation without GUI/build, installer execution, public upload, registry mutation, or readiness claims.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OVERNIGHT_KNOWN_WORLD_DETECTOR_SEGMENT_2_LOCK_001

**Proves:** Known-world detector segment 2 fixtures and manifest-only accounting without support promotion.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OVERNIGHT_KNOWN_WORLD_DETECTOR_SEGMENT_3_LOCK_001

**Proves:** Known-world detector segment 3 fixtures and manifest-only accounting without support promotion.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OVERNIGHT_PHP_RUBY_TOOLCHAIN_GATE_LOCK_001

**Proves:** PHP/Ruby exact local toolchain probes and no-install blocker packet.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OVERNIGHT_PROOF_DASHBOARD_OPERATOR_CENTER_READINESS_LOCK_001

**Proves:** Proof / Operator Center overnight sprint status panel and component test without authority or release claims.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OVERNIGHT_RELEASE_CELL_CERTIFICATION_CANDIDATES_LOCK_001

**Proves:** Release-cell certification candidate matrix without registry mutation or certification.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OVERNIGHT_REVIEW_READY_PROTOCOL_LOCK_001

**Proves:** DETERMINEX_OVERNIGHT_REVIEW_READY_PROTOCOL_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OVERNIGHT_SBOM_BYTE_NORMALIZATION_LOCK_001

**Proves:** SBOM byte normalization repair packet, historical truth preservation, and LF byte-stable successor.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OVERNIGHT_SCOPED_BROADER_SBOM_SEGMENTS_LOCK_001

**Proves:** Segmented SBOM/inventory outputs after full-repo Syft timeout.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OVERNIGHT_T_DRIVE_CARGO_BUILD_CACHE_RELOCATION_LOCK_001

**Proves:** T: Cargo target pathing probe for future Tauri/Rust build-cache relief without deleting existing C: target.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_OVERNIGHT_UNDER_THE_HOOD_COMPLETION_RECONCILIATION_LOCK_001

**Proves:** DETERMINEX_OVERNIGHT_UNDER_THE_HOOD_COMPLETION_RECONCILIATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PACKAGE_DRY_RUN_PUBLICATION_READINESS_HARDENING_LOCK_001

**Proves:** DETERMINEX_PACKAGE_DRY_RUN_PUBLICATION_READINESS_HARDENING_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PACKAGE_LICENSE_METADATA_HYGIENE_LOCK_001

**Proves:** DETERMINEX_PACKAGE_LICENSE_METADATA_HYGIENE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PACKAGE_LICENSE_METADATA_LOCAL_PREVIEW_BOUNDARY_LOCK_001

**Proves:** Package License Metadata and Local Preview Boundary

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PACKAGE_LOCKFILE_MUTATION_BOUNDARY_GUARD_LOCK_001

**Proves:** Package/Lockfile Mutation Boundary Guard

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PACKAGE_METADATA_LICENSE_README_BOUNDARY_COMPLETION_LOCK_001

**Proves:** Package Metadata, License, README, and Boundary Completion

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PACKAGING_FRESH_INSTALL_REQUIREMENTS_NORMALIZATION_LOCK_001

**Proves:** Normalize packaging and fresh-install proof contracts without implementing an installer or granting release support.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PACKAGING_NATIVE_PROOF_OPEN_AVAILABILITY_CLAUDE_CRITIQUE_001

**Proves:** Parallel Claude critique of Codex's latest sprint. Reviews WiX/Tauri packaging failure, Windows long-path blocker, native WebDriver admission, docs/static first release-supported cell path, public docs/license/security hygiene, day-one claim scanner refresh, model/build-flow backward audit, support-matrix UI binding risks, and Companion RAG GUI evidence packet. Emits top 20 ranked Codex actions, top 10 public claim risks, and top 3 Codex follow-on prompts.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PACKET_RUNTIME_FIRST_ONE_TIME_SPEND_LOCK_001

**Proves:** DETERMINEX_PACKET_RUNTIME_FIRST_ONE_TIME_SPEND_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PACKET_RUNTIME_FIRST_QUEUE_ADMISSION_LOCK_001

**Proves:** DETERMINEX_PACKET_RUNTIME_FIRST_QUEUE_ADMISSION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PACKET_RUNTIME_FULL_STATUS_TIMEOUT_REPAIR_CONTINUATION_LOCK_001

**Proves:** DETERMINEX_PACKET_RUNTIME_FULL_STATUS_TIMEOUT_REPAIR_CONTINUATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PACKET_RUNTIME_OTHER_PACKET_STATUS_REPORT_LOCK_001

**Proves:** DETERMINEX_PACKET_RUNTIME_OTHER_PACKET_STATUS_REPORT_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PACKET_RUNTIME_PACKET_DISCOVERY_HASH_VERIFICATION_LOCK_001

**Proves:** DETERMINEX_PACKET_RUNTIME_PACKET_DISCOVERY_HASH_VERIFICATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PACKET_RUNTIME_POST_SPEND_VERIFICATION_LOCK_001

**Proves:** DETERMINEX_PACKET_RUNTIME_POST_SPEND_VERIFICATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PACKET_RUNTIME_QUEUE_ADMISSION_BRIDGE_LOCK_001

**Proves:** DETERMINEX_PACKET_RUNTIME_QUEUE_ADMISSION_BRIDGE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PACKET_RUNTIME_REACT_VITE_SCOPED_EXECUTION_LOCK_001

**Proves:** DETERMINEX_PACKET_RUNTIME_REACT_VITE_SCOPED_EXECUTION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PACKET_RUNTIME_RECONCILIATION_SCORE_DISCIPLINE_LOCK_001

**Proves:** DETERMINEX_PACKET_RUNTIME_RECONCILIATION_SCORE_DISCIPLINE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PER_FAMILY_BUILD_TEST_SMOKE_COMMAND_MAPPING_LOCK_001

**Proves:** DETERMINEX_PER_FAMILY_BUILD_TEST_SMOKE_COMMAND_MAPPING_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PER_FAMILY_FIXTURE_ROUTE_EXECUTION_TESTS_LOCK_001

**Proves:** Per-Family Fixture Route Execution Tests

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PER_FAMILY_SAFE_FIXTURE_EXECUTION_EXPANSION_LOCK_001

**Proves:** Per-Family Safe Fixture Execution Expansion

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PHP_STRUCTURAL_MAPPING_BOUNDARY_GUARD_LOCK_001

**Proves:** PHP Structural Mapping Boundary Guard

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PHP_TOOLCHAIN_ABSENCE_GATE_LOCK_001

**Proves:** PHP Toolchain Absence Gate

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PLAYWRIGHT_TAURI_DRIVER_HARNESS_ADMISSION_LOCK_001

**Proves:** Admit the exact Playwright/Tauri-driver GUI harness route without installation or GUI launch.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PRIVACY_AND_TRAINING_DISCLOSURE_LOCK_001

**Proves:** Make Determinex's privacy, source-control, local-first, and training boundaries explicit, machine-checkable, user-readable, and report-integrated without granting training, telemetry, source mutation, release support, broad claims, or universal support.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROGRAMBENCH_COCKPIT_FIXTURE_BINDING_LOCK_001

**Proves:** DETERMINEX_PROGRAMBENCH_COCKPIT_FIXTURE_BINDING_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROGRAMBENCH_COCKPIT_FIXTURE_WIRE_AND_DRILLDOWN_LOCK_001

**Proves:** DETERMINEX_PROGRAMBENCH_COCKPIT_FIXTURE_WIRE_AND_DRILLDOWN_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROGRAMBENCH_COCKPIT_VISUAL_PROOF_IF_FIRST_PAINT_PASSED_LOCK_001

**Proves:** DETERMINEX_PROGRAMBENCH_COCKPIT_VISUAL_PROOF_IF_FIRST_PAINT_PASSED_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROGRAMBENCH_COCKPIT_WIREUP_CLAUDE_REVIEW_001

**Proves:** Overnight Lane 5. ProgramBench cockpit wireup. 2 of 10 wire items covered. Panel exists but not wired.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROGRAMBENCH_COMPILER_LOOP_COCKPIT_POST_CERTIFICATION_CLAUDE_REVIEW_001

**Proves:** Wave 006 Lane P. ProgramBench cockpit post-cert. 5 of 12 covered; 7 missing including panel-to-fixture wire, drill-down, WAL render.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROGRAMBENCH_COMPILER_LOOP_COCKPIT_VISIBILITY_CELL_LOCK_001

**Proves:** Certify exact compiler-loop and ProgramBench cockpit visibility without executing ProgramBench or broadening support claims.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROGRAMBENCH_COMPILER_LOOP_MOAT_VISIBILITY_CLAUDE_REVIEW_001

**Proves:** Gulp Wave 005 Claude Lane P. ProgramBench + compiler-loop moat visibility. 8 moat assets / 0 user-facing today. 4 cockpit render contracts + 2 demo seeds required.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROGRAMBENCH_FORBIDDEN_BOUNDARY_GUARD_LOCK_001

**Proves:** ProgramBench Forbidden Boundary Guard

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROGRAMBENCH_PER_TARGET_UNIFIED_GRAPH_EXPANSION_LOCK_001

**Proves:** Expand ProgramBench unified graph coverage to Doxygen plus each of the 10 metadata-admitted Batch001 targets.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROGRAMBENCH_WAL_VISUAL_MOAT_CLAUDE_REVIEW_001

**Proves:** Wave 007 Claude Lane P. ProgramBenchCockpit fixture wiring, per-tool drill-down, compiler-loop WAL render, failed/repair/pass trace, solved/SOTA claim gate.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROGRAMMING_LANGUAGE_UNIVERSE_AUDIT_LOCK_001

**Proves:** Identify, tag, normalize, classify, and route known language-like software surfaces into Determinex-owned taxonomy categories without treating discovery, detection, classification, or routing as support.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROGRAM_AUTHORITY_PROMOTION_HARDENING_LOCK_001

**Proves:** DETERMINEX_PROGRAM_AUTHORITY_PROMOTION_HARDENING_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROGRAM_AUTHORITY_RECORD_CONSUMPTION_BINDING_LOCK_001

**Proves:** DETERMINEX_PROGRAM_AUTHORITY_RECORD_CONSUMPTION_BINDING_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROGRAM_FAMILY_ADAPTER_INTERFACE_LOCK_001

**Proves:** DETERMINEX_PROGRAM_FAMILY_ADAPTER_INTERFACE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROGRAM_NEGATIVE_SIGNAL_REGISTRY_LOCK_001

**Proves:** DETERMINEX_PROGRAM_NEGATIVE_SIGNAL_REGISTRY_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROMOTE_TRUE_LOCAL_INSTALL_EXACT_CELLS_LOCK_001

**Proves:** Promote True Local Install Exact Cells

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROMOTION_GATE_NEGATIVE_FIXTURES_BLOCKING_CI_LOCK_001

**Proves:** Promotion Gate Negative Fixtures Blocking CI

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROMOTION_NEGATIVE_FIXTURE_CORPUS_PER_CATEGORY_EXERCISE_LOCK_001

**Proves:** DETERMINEX_PROMOTION_NEGATIVE_FIXTURE_CORPUS_PER_CATEGORY_EXERCISE_LOCK_001

**Does not prove:** Does not prove corpus balance, training effectiveness, or public benchmark dominance by itself.

#### DETERMINEX_PROOF_CENTER_INSTALLED_APP_GUI_SMOKE_LOCK_001

**Proves:** Prove the mounted Proof Center route inside a rebuilt installed Tauri app with screenshot and transcript hashes.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROOF_CENTER_INSTALLED_APP_ROUTE_MOUNT_LOCK_001

**Proves:** Mount the read-only Proof / Operator Center at an installed-app route path and preserve GUI-smoke boundaries.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROOF_CENTER_RELEASE_FOOTHOLD_CLAUDE_CRITIQUE_001

**Proves:** Read-only Claude critique of Codex's next-sprint path: selected workflow (status_proof_center_evidence_view), docs/static release-cell certification chain, claim-safe public wording for first release_supported cell, Proof Center UX risks, fresh-clone retry contract, NSIS fallback packaging, Companion RAG answer boundary. Emits 20 ranked Codex actions, 10 claim risks, 5 follow-on prompts.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROOF_CONTROL_PLANE_FINAL_STATE_LOCK_001

**Proves:** Write final non-authorizing state for the Determinex proof-control foundation.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROOF_CONTROL_READINESS_AUDIT_LOCK_001

**Proves:** Audit that the Determinex proof-control plane is ready for unified status consumption without starting unified status while Claude/Tauri work may be in flight.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROOF_DISCOVERY_ORCHESTRATOR_LOCK_001

**Proves:** Create the non-executing decision engine that maps proof gaps to discover, generate, request-operator, or block plans.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROOF_EXECUTION_AUDIT_REPAIR_LOCK_001

**Proves:** Repair proof-control execution audit regression by narrowly classifying the proof readiness git-status probe and proving scripts/proof has no unsafe, must-migrate, or unknown execution sites.

**Does not prove:** Does not prove broad real-world repair coverage beyond the locked acceptance tests.

#### DETERMINEX_PROOF_GAP_PACKET_LOCK_001

**Proves:** Create normalized non-authorizing proof gap packets for missing or insufficient proof.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROOF_GENERATION_TOOL_ADMISSION_LOCK_001

**Proves:** Define admission policy for external proof-generation and verification tools without installing or running them.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROOF_OPERATOR_CENTER_MILESTONE_DASHBOARD_LOCK_001

**Proves:** Create the Proof / Operator Center source-of-truth milestone dashboard evidence model for verified rooms, bindings, blocked paths, roadmap inputs, authority state, release gates, and evidence health.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROOF_OPERATOR_CENTER_VIEWMODEL_LOCK_001

**Proves:** Rung 6 of DETERMINEX_UNIFIED_PRODUCT_UX_SHELL_SERIES.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROOF_REPORT_AND_CLAIM_SCANNER_BACKFILL_LOCK_001

**Proves:** Proof Report / Claim Scanner Backfill

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROOF_REPORT_CAPABILITY_ANCHORS_AND_BLOCKED_EXAMPLES_LOCK_002

**Proves:** Proof Report Capability Anchors and Blocked Examples

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROOF_REPORT_CAPABILITY_COVERAGE_LOCK_001

**Proves:** DETERMINEX_PROOF_REPORT_CAPABILITY_COVERAGE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROOF_REPORT_CAPABILITY_COVERAGE_SECTION_LOCK_001

**Proves:** DETERMINEX_PROOF_REPORT_CAPABILITY_COVERAGE_SECTION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROOF_REPORT_CLAIM_SCANNER_FINAL_BACKFILL_CHECK_LOCK_001

**Proves:** Proof Report and Claim Scanner Final Backfill Check

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROOF_REPORT_FIRST_LOCAL_INSTALL_AND_EXPORT_LOCK_001

**Proves:** DETERMINEX_PROOF_REPORT_FIRST_LOCAL_INSTALL_AND_EXPORT_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROOF_REPORT_HTML_BOUND_TO_RELEASE_REGISTRY_LOCK_001

**Proves:** Proof Report HTML Bound to Registry

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROOF_REPORT_HTML_HARDENING_AND_INTEGRITY_STAMP_LOCK_001

**Proves:** DETERMINEX_PROOF_REPORT_HTML_HARDENING_AND_INTEGRITY_STAMP_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROOF_REPORT_HTML_INTEGRITY_SANITIZATION_PER_CLAIM_LINKS_LOCK_001

**Proves:** DETERMINEX_PROOF_REPORT_HTML_INTEGRITY_SANITIZATION_PER_CLAIM_LINKS_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROOF_REPORT_LOCAL_INSTALL_AND_EXPORT_LOCK_001

**Proves:** DETERMINEX_PROOF_REPORT_LOCAL_INSTALL_AND_EXPORT_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROOF_REPORT_PDF_HTML_EXPORT_CLAUDE_REVIEW_001

**Proves:** Overnight Lane 14. Proof report PDF/HTML export. 3/10 dimensions at target.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROOF_REPORT_PDF_HTML_EXPORT_LOCK_001

**Proves:** DETERMINEX_PROOF_REPORT_PDF_HTML_EXPORT_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROOF_REPORT_PER_CAPABILITY_EVIDENCE_ANCHORS_LOCK_001

**Proves:** Proof Report Per-Capability Evidence Anchors

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROOF_REPORT_RELEASE_BOUNDARY_REFRESH_LOCK_001

**Proves:** Proof Report Release Boundary Refresh

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROOF_REPORT_SUBPACKAGE_FEASIBILITY_AND_SCAFFOLD_LOCK_001

**Proves:** DETERMINEX_PROOF_REPORT_SUBPACKAGE_FEASIBILITY_AND_SCAFFOLD_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROOF_SOURCE_REGISTRY_LOCK_001

**Proves:** Define Determinex-wide proof sources and closed authority defaults.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PROOF_TYPE_AUTHORITY_MATRIX_LOCK_001

**Proves:** Define what each proof type can and cannot authorize.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PUBLIC_BETA_READINESS_DASHBOARD_HARDENING_LOCK_001

**Proves:** DETERMINEX_PUBLIC_BETA_READINESS_DASHBOARD_HARDENING_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PUBLIC_DISTRIBUTION_CHANNEL_FEASIBILITY_LOCK_001

**Proves:** Classify public distribution channels and next locks without publishing or claiming distribution readiness.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PUBLIC_DOCS_LICENSE_SECURITY_HYGIENE_APPLY_LOCK_001

**Proves:** Review/apply minimum public docs license security hygiene; apply deferred when public docs are outside this lane ownership.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PUBLIC_DOCS_LICENSE_SECURITY_HYGIENE_RETRY_LOCK_001

**Proves:** Retry public docs/license/security hygiene after public claim remediation.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PUBLIC_MESSAGING_CLAIM_SCANNER_AND_LAUNCH_LANGUAGE_GUARD_CLAUDE_REVIEW_001

**Proves:** Gulp Wave 004 Claude Lane P. Public messaging + claim scanner + launch language guard. Maps 18 phrases (allowed / gated / permanently forbidden) against gate state. Defines messaging strategy beyond binary claim-scanner gate.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PUBLIC_MESSAGING_PHRASE_GATE_MAP_LOCK_001

**Proves:** Enforce public messaging phrase gates without unlocking release, installer, product, or open availability claims.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PUBLIC_PRIOR_ART_AND_ADJACENT_MARKET_AUDIT_LOCK_001

**Proves:** Create a machine-checkable, dated audit of adjacent products, patents, benchmarks, research papers, and market sectors, distinguishing crowded claims from Determinex's narrow defensible claim candidates. Red-team market-landscape pull only. Not a legal freedom-to-operate opinion. Not a patent clearance search. Not a provisional filing. Not marketing collateral. Grants no authority.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PUBLIC_PROOF_BETA_READINESS_DASHBOARD_LOCK_001

**Proves:** DETERMINEX_PUBLIC_PROOF_BETA_READINESS_DASHBOARD_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PUBLIC_PROOF_REPORT_EXPORT_LOCK_001

**Proves:** Make Determinex's proof report model exportable, durable, machine-checkable, and user-readable without granting release, production, source mutation, proof execution, training, or broad support authority.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PUBLIC_REVEAL_PREFLIGHT_BOARD_LOCK_001

**Proves:** DETERMINEX_PUBLIC_REVEAL_PREFLIGHT_BOARD_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PUBLIC_REVEAL_PREFLIGHT_TIER_HARDENING_LOCK_001

**Proves:** DETERMINEX_PUBLIC_REVEAL_PREFLIGHT_TIER_HARDENING_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PUBLIC_SBOM_LICENSE_RELEASE_HYGIENE_LOCK_001

**Proves:** Start public SBOM, license, security, signing, and artifact provenance release hygiene without claiming release readiness.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PUBLIC_SHOCK_NARRATIVE_AND_CLAIM_GATE_REVIEW_CLAUDE_001

**Proves:** Wave 007 Claude Lane M. What can be said now, after first-paint, after installer smoke, after SBOM, after subpackage dry-run, after visual cockpit proof, permanently forbidden phrases.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PUBLIC_SHOCK_NARRATIVE_AND_CLAIM_SAFETY_CLAUDE_REVIEW_001

**Proves:** Gulp Wave 005 Claude Lane M. Public shock narrative + claim safety. 10-rung reveal readiness ladder. Per-audience narrative. Phrase-gate enforcement.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PUBLIC_SHOCK_NARRATIVE_FINALIZATION_CLAUDE_REVIEW_001

**Proves:** Overnight Lane 16. Public shock narrative finalization. 15-phrase unlock map; one-liner + 'WHAT?' safe draft ready.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PUBLIC_SHOCK_NARRATIVE_RUNG_REVIEW_001

**Proves:** Wave 006 Lane M. Reveal rung assessment post phrase-gates landing. Rung 1 CURRENT; rungs 5,6 PASSED; rungs 2/3/4/7 PARTIAL; 3 NOT_YET.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PUBLIC_TIDAL_WAVE_FLAGSHIP_FLOW_CERTIFICATION_LOCK_001

**Proves:** Certify the public flagship user journey model and claim boundaries without claiming launch, release, production, source mutation, training, or universal support.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PUBLIC_UPLOAD_FORBIDDEN_BOUNDARY_GUARD_LOCK_001

**Proves:** Public Upload Forbidden Boundary Guard

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PYTHON_CLI_ACCEPTANCE_AND_SMOKE_PLAN_LOCK_001

**Proves:** Define measurable acceptance and smoke tests for the first Python CLI/file-data splash target.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PYTHON_CLI_FILE_DATA_SCAFFOLD_SPEC_LOCK_001

**Proves:** Define the safe scaffold specification for the first Python CLI/file-data splash target without creating the real scaffold.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PYTHON_GOD_SCRIPT_AND_NATIVE_ARCHITECTURE_AUDIT_LOCK_001

**Proves:** Audit Python drift, god-script risk, JSON theater, authority leaks, and native boundary bypass risk after scaffold/build/test/smoke expansion.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_PYTHON_STATUS_SCRIPT_DECOMPOSITION_AND_ANTI_GOD_SCRIPT_RULE_LOCK_001

**Proves:** Contain Python status-script drift by extracting shared policy data and enforcing a permanent anti-god-script rule.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RAG_100_FIXTURE_RETRIEVAL_CORRECTNESS_SECURITY_GATE_LOCK_001

**Proves:** DETERMINEX_RAG_100_FIXTURE_RETRIEVAL_CORRECTNESS_SECURITY_GATE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RAG_50_FIXTURE_AND_CELL_5_CLASSIFICATION_CLAUDE_REVIEW_001

**Proves:** Wave 006 Lane R. RAG 25 -> 50 + cell 5 classification (3rd reaffirmation: internal_observability_only).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RAG_50_FIXTURE_RETRIEVAL_CORRECTNESS_SECURITY_GATE_LOCK_001

**Proves:** DETERMINEX_RAG_50_FIXTURE_RETRIEVAL_CORRECTNESS_SECURITY_GATE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RAG_GUI_FIXTURE_LADDER_CELL5_CLAUDE_REVIEW_001

**Proves:** Overnight Lane 8. RAG 50 + cell 5 round 4 dispute + GUI panel missing.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RAG_GUI_PANEL_AND_CELL_5_CLASSIFICATION_RESOLUTION_LOCK_001

**Proves:** DETERMINEX_RAG_GUI_PANEL_AND_CELL_5_CLASSIFICATION_RESOLUTION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RAG_NATURAL_LANGUAGE_QUERY_EVAL_LOCK_001

**Proves:** Prove local companion natural-language retrieval top-k behavior without claiming answer quality.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RAG_PANEL_CELL5_FINAL_CLASSIFICATION_CLAUDE_REVIEW_001

**Proves:** Wave 007 Claude Lane R. CompanionRagReportPanel component proof, RAG 100 fixture gate, citation/report export surface, answer correctness boundary, product readiness, training boundary, Cell 5 final classification.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RAG_PRODUCTIZATION_FIXTURE_EXPANSION_CORRECTNESS_GATE_CLAUDE_REVIEW_001

**Proves:** Gulp Wave 005 Claude Lane R. RAG productization + fixture expansion + correctness gate. Disputes Codex cell-5 user-visible classification. Defines 5/25/50/200/500 fixture ladder.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RAG_SIGNED_RUN_EXPORT_OR_CELL5_CORRECTION_LOCK_001

**Proves:** DETERMINEX_RAG_SIGNED_RUN_EXPORT_OR_CELL5_CORRECTION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RC_PROOF_MAP_CLAUDE_APPEND_ONLY_COUNT_DRIFT_GUARDS_REVIEW_001

**Proves:** RC-proof-map Claude Lane O. Codex Lane F: append-only + count-drift guards in place.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RC_PROOF_MAP_CLAUDE_BETA_DASHBOARD_REVIEW_001

**Proves:** RC-proof-map Claude Lane H. Codex Lane C: dashboard HARDENED with proven/prepared/blocked separation; no public upload.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RC_PROOF_MAP_CLAUDE_CLAIM_SCANNER_OVERCLAIM_REVIEW_001

**Proves:** RC-proof-map Claude Lane P. Claim scanner + Day 1 overclaim scanner both pass.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RC_PROOF_MAP_CLAUDE_DIRTY_STATE_REPORTED_REVIEW_001

**Proves:** RC-proof-map Claude Lane Q. Dirty/untracked state reported (ledger auto-regen only).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RC_PROOF_MAP_CLAUDE_EVIDENCE_INDEX_CLEAN_REVIEW_001

**Proves:** RC-proof-map Claude Lane N. Evidence index validates at 1315; no count drift; no validation errors.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RC_PROOF_MAP_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001

**Proves:** RC-proof-map Claude Lane R. All forbidden actions audited and avoided per marker declaration.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RC_PROOF_MAP_CLAUDE_NONCODER_REPORT_REVIEW_001

**Proves:** RC-proof-map Claude Lane I. Codex Lane D: plain-English report RECORDED; clear what Determinex can/cannot do; no overclaim.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RC_PROOF_MAP_CLAUDE_NO_FAKE_SIGNATURE_REVIEW_001

**Proves:** RC-proof-map Claude Lane B. No fake signature material accepted; no template treated as real.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RC_PROOF_MAP_CLAUDE_NO_QUEUE_WITHOUT_MATERIAL_REVIEW_001

**Proves:** RC-proof-map Claude Lane C. signed_valid_queue 0→0; no record created without valid material.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RC_PROOF_MAP_CLAUDE_NO_SPEND_WITHOUT_APPROVAL_REVIEW_001

**Proves:** RC-proof-map Claude Lane D. signed_spend 0→0; no spend without signed approval.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RC_PROOF_MAP_CLAUDE_PACKETS_NOT_EXECUTED_REVIEW_001

**Proves:** RC-proof-map Claude Lane F. SBOM/clean-host/GUI/installer packets all HARDENED_UNSIGNED_NOT_EXECUTED.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RC_PROOF_MAP_CLAUDE_PATH_DECISION_REVIEW_001

**Proves:** RC-proof-map Claude Lane A. Codex Lane A: PATH_B selected (no signature material); branch decision artifact.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RC_PROOF_MAP_CLAUDE_PROOF_MAP_COMPLETENESS_REVIEW_001

**Proves:** RC-proof-map Claude Lane G. Codex Lane B: release-candidate proof map RECORDED with blockers + required authority + required proof + current artifact + next operator action.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RC_PROOF_MAP_CLAUDE_REACT_VITE_NOT_ADMITTED_REVIEW_001

**Proves:** RC-proof-map Claude Lane E. React/Vite still blocked; no dependency admission.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RC_PROOF_MAP_CLAUDE_RELEASE_CELLS_INVARIANT_REVIEW_001

**Proves:** RC-proof-map Claude Lane K. release_supported_exact_cells: 10 unchanged (canonical registry).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RC_PROOF_MAP_CLAUDE_RELEASE_FAMILIES_INVARIANT_REVIEW_001

**Proves:** RC-proof-map Claude Lane L. release_supported_families: 0 unchanged.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RC_PROOF_MAP_CLAUDE_SCORES_UNCHANGED_REVIEW_001

**Proves:** RC-proof-map Claude Lane M. All scores unchanged; no score-delta artifact this wave.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RC_PROOF_MAP_CLAUDE_SYNTHESIS_REVIEW_001

**Proves:** RC-proof-map Claude Lane S. Synthesis + 34-item final report. PATH B substrate verified; no spend; boundary held 25 waves.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RC_PROOF_MAP_CLAUDE_TIMEOUT_DIAGNOSTIC_REVIEW_001

**Proves:** RC-proof-map Claude Lane J. Codex Lane E: FULL_STATUS_TIMEOUT_DIAGNOSTIC RECORDED; bounded timing artifact; no tests disabled/skipped/erased; future repair recommendation.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_DEMO_NAVIGATION_HAPPY_BLOCKED_PATH_LOCK_001

**Proves:** Rung 3 of DETERMINEX_LIVE_REACT_PRODUCT_SHELL_DEMO_READINESS_SERIES.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_IDEA_LAB_PANEL_LOCK_001

**Proves:** Rung 3 of DETERMINEX_LIVE_REACT_UNIFIED_PRODUCT_SHELL_SERIES.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_IDEA_LAB_VERIFIED_DEMO_STATUS_BINDING_LOCK_001

**Proves:** Rung 2 of DETERMINEX_LIVE_REACT_PRODUCT_SHELL_DEMO_READINESS_SERIES.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_LEARNING_STUDIO_PANEL_LOCK_001

**Proves:** Rung 6 of DETERMINEX_LIVE_REACT_UNIFIED_PRODUCT_SHELL_SERIES.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_LEARNING_STUDIO_VERIFIED_DEMO_STATUS_BINDING_LOCK_001

**Proves:** Bind the verified Learning Studio teaching splash demo evidence into the live React Learning Studio panel as a non-authorizing teaching status.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_MAINTENANCE_BAY_PANEL_LOCK_001

**Proves:** Rung 5 of DETERMINEX_LIVE_REACT_UNIFIED_PRODUCT_SHELL_SERIES.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_MAINTENANCE_BAY_VERIFIED_DEMO_STATUS_BINDING_LOCK_001

**Proves:** Bind the verified Maintenance Bay dry-run/update evidence into the live React Maintenance Bay panel.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_PRODUCT_SHELL_BROWSER_SNAPSHOT_LOCK_001

**Proves:** Rung 1 of DETERMINEX_LIVE_REACT_PRODUCT_SHELL_DEMO_READINESS_SERIES.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_PROOF_OPERATOR_CENTER_MILESTONE_DASHBOARD_BINDING_LOCK_001

**Proves:** Bind the verified Proof / Operator Center milestone dashboard evidence into the live React Proof / Operator Center panel as a non-authorizing, scope-disciplined view-model.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_PROOF_OPERATOR_CENTER_PANEL_LOCK_001

**Proves:** Rung 7 of DETERMINEX_LIVE_REACT_UNIFIED_PRODUCT_SHELL_SERIES.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_PUBLIC_AUTHORITY_BOUNDARY_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex combined authority-boundary preservation across flagship + export evidence. Refuses any authority flag true, release overclaim, and broken preservation polarity.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_PUBLIC_FALSE_CLAIM_SCANNER_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex combined false-claim scanner evidence (9 flagship + 11 export forbidden claims). Refuses scanner-count drift, action mismatch, current_claim_allowed=true, and required-block phrase coverage gap.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_PUBLIC_PROOF_REPORT_EXPORT_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex public proof report export (25 contract fields, 5 sample reports, 7 route outcomes, 11 forbidden claims). Refuses count drift, authority broadening, release-readiness overclaim, runtime-proof overclaim, and forbidden broad-claim phrases.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_PUBLIC_PROOF_REPORT_SAMPLE_REPORTS_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex public proof report sample-report evidence (5 archetype reports). Refuses sample count mismatch, authority flags in samples, and forbidden broad-claim phrases.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_PUBLIC_READINESS_SPINE_DASHBOARD_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Determinex's public readiness spine dashboard (live evidence_index + reconciliation 010 integrity). Refuses validation_errors non-empty, authority broadening, release overclaim.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_PUBLIC_TIDAL_WAVE_FLAGSHIP_FLOW_CERTIFICATION_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex public flagship flow certification (10 flagship journeys, 9 false-claim scanner phrases, 12 proof report fields). Refuses authority broadening, count drift, universal support claim, release overclaim, and forbidden broad-claim phrases. Certification covers routing/reporting/blocker-accounting only; NOT release support or production readiness.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_PUBLIC_UNKNOWN_NOVEL_ROUTE_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex unknown/novel intake-route preservation. Refuses cell_id/claim_state/missing_rung_key/route_status drift and any promoted/support_claimed/release_supported truthy flag.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_RELEASE_READINESS_BLOCKER_PANEL_LOCK_001

**Proves:** Rung 4 of DETERMINEX_LIVE_REACT_PRODUCT_SHELL_DEMO_READINESS_SERIES.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_REPO_CLINIC_PANEL_LOCK_001

**Proves:** Rung 4 of DETERMINEX_LIVE_REACT_UNIFIED_PRODUCT_SHELL_SERIES.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_REPO_CLINIC_VERIFIED_DEMO_STATUS_BINDING_LOCK_001

**Proves:** Bind the verified Repo Clinic fixture-repair evidence into the live React Repo Clinic panel.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_SPLASH_DEMO_PANEL_LOCK_001

**Proves:** Rung 9 of DETERMINEX_LIVE_REACT_UNIFIED_PRODUCT_SHELL_SERIES.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_005_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex tandem post-Claude-binding reconciliation 005. Displays preserved absorbed checkpoint (354/354/354), reconciled spine (>= 355), ledger chain valid, mutation_detected false, evidence_index clean, absorbed Claude binding locks, and subprocess classification status. Reconciliation absorbs display evidence; it does not promote capability.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_007_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex tandem post-Claude-binding reconciliation 007. Displays absorbed Claude commit, prior Codex source-truth checkpoint (370), Claude display checkpoint (379), reconciled spine (380+), 9 absorbed Claude binding locks, and source-truth locks preserved. Reconciliation absorbs display evidence; it does not promote capability.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_008_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex tandem post-Claude-binding reconciliation 008. Displays absorbed Claude commit, prior Codex source-truth checkpoint (387), Claude display checkpoint (395), reconciled spine (396+), 8 absorbed Claude binding locks, and source-truth locks preserved. Reconciliation absorbs display evidence; it does not promote capability.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_009_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex tandem post-Claude-binding reconciliation 009. Displays absorbed Claude commit, prior Codex source-truth checkpoint (405), Claude display checkpoint (415), reconciled spine (416+), 10 absorbed Claude binding locks, and source-truth locks preserved. Reconciliation absorbs display evidence; it does not promote capability.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIFIED_NAVIGATION_PANEL_LOCK_001

**Proves:** Rung 2 of DETERMINEX_LIVE_REACT_UNIFIED_PRODUCT_SHELL_SERIES.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_ALL_SECTOR_TAXONOMY_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 all-sector taxonomy (40 sectors, 40 top-level families). Routing only — every sector defaults to NOT_CLAIMED / classified. Refuses sectors that default to capability support states (build_supported and above) or to capability claim states (IMPLEMENTED, IMPLEMENTED_WITH_CAVEATS, PARTIAL).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_CONVEYOR_BACKLOG_AND_DEPTH_QUEUE_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 conveyor backlog and depth queue. Planning surface only — displays next-action queues (sector gulp, depth promotion, verifier-building, fixture-building, packaging/fresh install, user-ready-with-caveats candidates), blocked/roadmap/forbidden cells by exact missing rung, Claude visual binding backlog, and Codex safe parallel work queue. Refuses authority broadening, broad-claim phrases, and empty next-gulp queue.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_DEPTH_PROMOTION_BATCH_017_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 depth promotion Batch 017. Refuses authority broadening, release/user-ready overclaim, missing blocked_cells/promoted_cells/depth_promotion_plan, unknown support_states, and forbidden broad-claim phrases. Depth promotion is bounded fixture-local probe proof.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_DEPTH_PROMOTION_BATCH_018_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 depth promotion Batch 018. Refuses authority broadening, release/user-ready overclaim, missing blocked_cells/promoted_cells/depth_promotion_plan, unknown support_states, and forbidden broad-claim phrases. Depth promotion is bounded fixture-local probe proof.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_DEPTH_PROMOTION_BATCH_019_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 depth promotion Batch 019. Refuses authority broadening, release/user-ready overclaim, missing blocked_cells/promoted_cells/depth_promotion_plan, unknown support_states, and forbidden broad-claim phrases. Depth promotion is bounded fixture-local probe proof.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_DEPTH_PROMOTION_CANDIDATE_INVENTORY_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 depth promotion candidate inventory (40 sector families annotated with current depth, easiest next rung, missing rung, local-proof feasibility, and per-batch targets). Refuses family_count drift, missing batch targets, missing candidate keys, authority broadening, and forbidden broad-claim phrases.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_DEPTH_PROMOTION_SCOREBOARD_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 depth promotion scoreboard (post-wave 40-family aggregates, families_with_any_evidence 18 -> 26, depth distribution, release_supported = 0). Refuses families_total != 40, Level_1 drift, release overclaim, missing aggregates, and forbidden broad-claim phrases.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_DEPTH_PROMOTION_WAVE_001_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 depth promotion Wave 001 (batches 017/018/019 aggregate). Refuses authority broadening, release/user-ready overclaim, missing batches/deltas/blocked_cells, and forbidden broad-claim phrases. Wave aggregation does not promote cells.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_MATRIX_PROBE_EXECUTION_BATCH_002_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 Matrix Probe Batch 002 evidence (15 cells probed, 15 promoted, 14 smoke_supported, 1 test_supported, 0 release_supported, 0 blocked). Same invariants as Batch 001: no authority grant, no overclaim, blocked cells stay visible, fixture-local caveats required.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_MATRIX_PROBE_EXECUTION_BATCH_003_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 Matrix Probe Batch 003 evidence (12 cells probed, 11 promoted, 8 smoke + 3 test + 1 roadmap, 0 release_supported, 1 blocked: typescript_node_cli_build with missing rung DETERMINEX_TYPESCRIPT_NODE_CLI_ADAPTER_LOCK_001). Same invariants as Batch 001/002.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_MATRIX_PROBE_EXECUTION_BATCH_004_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 Matrix Probe Batch 004 evidence (10 cells probed, 10 promoted, 10 smoke_supported, 0 release_supported, 0 blocked). Unlocked by DETERMINEX_TYPESCRIPT_NODE_CLI_ADAPTER_LOCK_001 (local tsc + ambient declarations; no network/npm/Docker). Same invariants as Batch 001-003.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_MATRIX_PROBE_EXECUTION_BATCH_BINDING_LOCK_001

**Proves:** Read-only React visual binding of the Codex Universal 100 Matrix Probe Execution Batch 001 evidence. Display batch counts, promoted cells, blocked cells (visible with exact missing rung), evidence caveats, strongest truthful claim, forbidden claims, and required captions. Refuse authority broadening, broad-claim phrases, release_supported overclaim, blocked-cell hiding, fixture caveat absence, and malformed evidence.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_005_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 Sector Gulp Batch 005: sectors ['cli_file_data_sector', 'node_typescript_cli_sector'], 12/12/12 cells tagged/classified/routed, 12 promoted, 0 blocked, 0 release_supported.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_006_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 Sector Gulp Batch 006: sectors ['react_vite_static_app_sector', 'static_web_sector', 'python_fastapi_local_api_sector'], 18/18/18 cells tagged/classified/routed, 18 promoted, 0 blocked, 0 release_supported.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_007_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 Sector Gulp Batch 007: sectors ['go_utility_sector', 'maintenance_repair_sector', 'rust_utility_sector'], 16/16/16 cells tagged/classified/routed, 16 promoted, 0 blocked, 0 release_supported.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_008_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 Sector Gulp Batch 008: sectors ['learning_teaching_sector', 'packaging_fresh_install_sector', 'user_ready_with_caveats_depth_pass'], 10/10/10 cells tagged/classified/routed, 9 promoted, 1 blocked, 0 release_supported.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_009_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 Sector Gulp Batch 009: sectors ['local_database_sqlite_sector', 'node_typescript_cli_sector', 'python_package_library_sector'], 9/9/9 cells tagged/classified/routed, 9 promoted, 0 blocked, 0 release_supported.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_010_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 Sector Gulp Batch 010: sectors ['browser_extension_sector', 'documentation_static_docs_sector', 'tauri_electron_desktop_sector'], 9/9/9 cells tagged/classified/routed, 7 promoted, 2 blocked, 0 release_supported.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_011_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 Sector Gulp Batch 011: sectors ['csharp_dotnet_sector', 'java_jvm_sector', 'ruby_php_sector'], 9/9/9 cells tagged/classified/routed, 6 promoted, 3 blocked, 0 release_supported.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_012_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 Sector Gulp Batch 012: sectors ['devops_ci_sector', 'package_library_project_sector', 'testing_qa_tools_sector'], 9/9/9 cells tagged/classified/routed, 8 promoted, 1 blocked, 0 release_supported.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_SECTOR_GULP_BATCH_013_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 Sector Gulp Batch 013: sectors ['agent_workflow_automation_sector', 'plugin_addon_systems_sector', 'security_audit_compliance_support_sector'], 9/9/9 cells tagged/classified/routed, 6 promoted, 3 blocked, 0 release_supported.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_SECTOR_STATE_LADDER_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 Sector State and Ingestion Ladder evidence (11 sectors, 24 lifecycle states, 14 blocker missing-rung states). Displays sector registry + lifecycle ladder; does not promote any sector. Refuses authority broadening, broad-claim phrases, and sectors targeting RELEASE_SUPPORTED without packaging/fresh-install proof.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_DEPTH_LEDGER_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 support-depth ledger. Displays per-cell support accounting (totals + per-sector/language/app-class/platform/workflow/product-room breakdowns + blocker buckets + metadata gaps). Refuses release_supported > 0 without release-proof path; refuses user_ready_with_caveats > 0 without user-ready-proof path. Ledger is accounting, not promotion.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_002_VISUAL_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 Support Map Delta Batch 002 evidence. Display promoted cells, blocked cells, claim/support state counts, delta sources, and strongest truthful claim. Refuse authority broadening, release_supported overclaim, blocked-cell hiding, and broad-claim phrases as current state.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_003_VISUAL_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 Support Map Delta Batch 003 evidence. Display promoted cells, blocked cells, claim/support state counts, blockers_by_category, delta sources, and strongest truthful claim. Refuse authority broadening, release_supported overclaim, blocked-cell hiding, and broad-claim phrases as current state.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_004_VISUAL_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 Support Map Delta Batch 004 evidence. Display promoted cells (grouped by language/runtime), blocked cells, claim/support state counts, delta sources, and strongest truthful claim. Refuse authority broadening, release_supported overclaim, blocked-cell hiding, and broad-claim phrases as current state.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_005_VISUAL_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 Support Map Delta Batch 005 (12 promoted / 0 blocked / 0 release_supported).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_006_VISUAL_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 Support Map Delta Batch 006 (18 promoted / 0 blocked / 0 release_supported).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_007_VISUAL_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 Support Map Delta Batch 007 (16 promoted / 0 blocked / 0 release_supported).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_008_VISUAL_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 Support Map Delta Batch 008 (0 promoted / 1 blocked / 0 release_supported).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_009_VISUAL_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 Support Map Delta Batch 009 (0 promoted / 0 blocked / 0 release_supported).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_010_VISUAL_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 Support Map Delta Batch 010 (0 promoted / 2 blocked / 0 release_supported).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_011_VISUAL_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 Support Map Delta Batch 011 (0 promoted / 3 blocked / 0 release_supported).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_012_VISUAL_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 Support Map Delta Batch 012 (0 promoted / 1 blocked / 0 release_supported).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_013_VISUAL_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 Support Map Delta Batch 013 (0 promoted / 3 blocked / 0 release_supported).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_014_VISUAL_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 support map delta Batch 014. Refuses authority broadening, release overclaim, hidden blocked cells, unknown support_states, and forbidden broad-claim phrases. Delta is layered display; not promotion.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_015_VISUAL_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 support map delta Batch 015. Refuses authority broadening, release overclaim, hidden blocked cells, unknown support_states, and forbidden broad-claim phrases. Delta is layered display; not promotion.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_016_VISUAL_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 support map delta Batch 016. Refuses authority broadening, release overclaim, hidden blocked cells, unknown support_states, and forbidden broad-claim phrases. Delta is layered display; not promotion.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_017_VISUAL_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 support map delta Batch 017 (depth-promotion mode). Refuses authority broadening, release overclaim, hidden blocked cells, unknown support_states, and forbidden broad-claim phrases.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_018_VISUAL_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 support map delta Batch 018 (depth-promotion mode). Refuses authority broadening, release overclaim, hidden blocked cells, unknown support_states, and forbidden broad-claim phrases.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_019_VISUAL_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 support map delta Batch 019 (depth-promotion mode). Refuses authority broadening, release overclaim, hidden blocked cells, unknown support_states, and forbidden broad-claim phrases.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_TOP_LEVEL_BLOCKER_INVENTORY_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 top-level blocker inventory evidence (10 blockers classified by category, family, sector, local resolvability, safe next rung, forbidden shortcut). Refuses authority broadening, missing blocker fields, missing category/resolvability counts, and forbidden broad-claim phrases. Inventory classifies; it does not promote.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_TOP_LEVEL_GAP_CLOSURE_BATCH_014_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 top-level gap closure Batch 014. Refuses authority broadening, release/user-ready overclaim, missing blocker progress fields, missing blocked_cells, unknown support_states, and forbidden broad-claim phrases. Gap closure is bounded fixture-local probe proof; partial closure stays partial.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_TOP_LEVEL_GAP_CLOSURE_BATCH_015_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 top-level gap closure Batch 015. Refuses authority broadening, release/user-ready overclaim, missing blocker progress fields, missing blocked_cells, unknown support_states, and forbidden broad-claim phrases. Gap closure is bounded fixture-local probe proof; partial closure stays partial.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_TOP_LEVEL_GAP_CLOSURE_BATCH_016_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 top-level gap closure Batch 016. Refuses authority broadening, release/user-ready overclaim, missing blocker progress fields, missing blocked_cells, unknown support_states, and forbidden broad-claim phrases. Gap closure is bounded fixture-local probe proof; partial closure stays partial.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_TOP_LEVEL_SECTOR_COMPLETION_CAMPAIGN_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 top-level sector completion campaign evidence (40-family scoreboard + execution plan). Refuses Level 1 coverage != 40/40, any family missing identified/classified/represented_in_completion_campaign_ledger, release_supported overclaim, authority broadening, and forbidden broad-claim phrases. Routing/accounting only — not support promotion.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_TOP_LEVEL_SECTOR_COVERAGE_SCOREBOARD_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 top-level sector coverage scoreboard (40-family Level 1 + per-depth aggregates + blockers_remaining_by_category + next_top_level_targets). Refuses families_total != 40, level_1_covered drift, release overclaim, missing aggregates, and forbidden broad-claim phrases. Coverage = routing/accounting only.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_TOP_LEVEL_SECTOR_GAP_CLOSURE_WAVE_001_BINDING_LOCK_001

**Proves:** Read-only React visual binding of Codex Universal 100 top-level sector gap closure Wave 001 (batches 014/015/016 aggregate). Refuses authority broadening, release/user-ready overclaim, missing batches/deltas, and forbidden broad-claim phrases. Wave aggregation does not promote cells.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_UNIVERSAL_100_VISUAL_WATCH_AND_BINDING_PREP_LOCK_001

**Proves:** Build the read-only Claude visual-binding-lane watcher for Codex Universal 100 data-plane evidence. Detect WAITING / PRESENT_BUT_NOT_VALIDATED / VALID_READY_FOR_BINDING / BOUND_READ_ONLY / BLOCKED_REASON without grabbing authority.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_USER_LEVEL_TEACHING_MODE_LOCK_001

**Proves:** Rung 8 of DETERMINEX_LIVE_REACT_UNIFIED_PRODUCT_SHELL_SERIES.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_VITE_AUTHORITY_PACKET_VALIDATION_LOCK_001

**Proves:** DETERMINEX_REACT_VITE_AUTHORITY_PACKET_VALIDATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_VITE_BOUNDED_REPAIR_GUARD_LOCK_001

**Proves:** DETERMINEX_REACT_VITE_BOUNDED_REPAIR_GUARD_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_VITE_BOUNDED_SOURCE_REPAIR_LOCK_001

**Proves:** DETERMINEX_REACT_VITE_BOUNDED_SOURCE_REPAIR_LOCK_001

**Does not prove:** Does not prove broad real-world repair coverage beyond the locked acceptance tests.

#### DETERMINEX_REACT_VITE_FAILURE_CLASSIFICATION_REPAIR_AUTHORIZATION_LOCK_001

**Proves:** DETERMINEX_REACT_VITE_FAILURE_CLASSIFICATION_REPAIR_AUTHORIZATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_VITE_FULL_STATUS_TIMEOUT_CONTINUATION_LOCK_001

**Proves:** DETERMINEX_REACT_VITE_FULL_STATUS_TIMEOUT_CONTINUATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_VITE_LOCAL_VERIFICATION_EXECUTION_LOCK_001

**Proves:** DETERMINEX_REACT_VITE_LOCAL_VERIFICATION_EXECUTION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_VITE_LOCAL_VERIFICATION_PLAN_LOCK_001

**Proves:** DETERMINEX_REACT_VITE_LOCAL_VERIFICATION_PLAN_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_VITE_LOCAL_VERIFICATION_RECONCILIATION_LOCK_001

**Proves:** DETERMINEX_REACT_VITE_LOCAL_VERIFICATION_RECONCILIATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_VITE_OTHER_PROTECTED_PACKETS_UNTOUCHED_LOCK_001

**Proves:** DETERMINEX_REACT_VITE_OTHER_PROTECTED_PACKETS_UNTOUCHED_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_VITE_POST_ADMISSION_LOCAL_TRANSCRIPT_LOCK_001

**Proves:** DETERMINEX_REACT_VITE_POST_ADMISSION_LOCAL_TRANSCRIPT_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_VITE_POST_SPEND_LOCAL_VERIFICATION_LOCK_001

**Proves:** DETERMINEX_REACT_VITE_POST_SPEND_LOCAL_VERIFICATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_VITE_POST_VERIFICATION_EVIDENCE_AUDIT_LOCK_001

**Proves:** DETERMINEX_REACT_VITE_POST_VERIFICATION_EVIDENCE_AUDIT_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_VITE_PRIOR_SPEND_BINDING_LOCK_001

**Proves:** DETERMINEX_REACT_VITE_PRIOR_SPEND_BINDING_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_VITE_REPAIR_MARCH_PLAN_DASHBOARD_LOCK_001

**Proves:** DETERMINEX_REACT_VITE_REPAIR_MARCH_PLAN_DASHBOARD_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_VITE_REPAIR_SCORE_DISCIPLINE_LOCK_001

**Proves:** DETERMINEX_REACT_VITE_REPAIR_SCORE_DISCIPLINE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_VITE_REPAIR_UNIVERSAL_ACCOUNTING_RECONCILIATION_LOCK_001

**Proves:** DETERMINEX_REACT_VITE_REPAIR_UNIVERSAL_ACCOUNTING_RECONCILIATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_VITE_SCAFFOLD_BUILD_TEST_SMOKE_RELEASE_CELL_LOCK_001

**Proves:** Certify the exact bounded React/Vite scaffold build/test/smoke user-visible fixture cell without broad frontend or release-readiness claims.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_VITE_SCORE_DISCIPLINE_LOCK_001

**Proves:** DETERMINEX_REACT_VITE_SCORE_DISCIPLINE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_VITE_SIGNED_DEPENDENCY_OR_STRUCTURAL_TRANSCRIPT_LOCK_001

**Proves:** DETERMINEX_REACT_VITE_SIGNED_DEPENDENCY_OR_STRUCTURAL_TRANSCRIPT_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_VITE_SPEND_ELIGIBILITY_GATE_LOCK_001

**Proves:** DETERMINEX_REACT_VITE_SPEND_ELIGIBILITY_GATE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_VITE_SPEND_ELIGIBILITY_RECHECK_LOCK_001

**Proves:** DETERMINEX_REACT_VITE_SPEND_ELIGIBILITY_RECHECK_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_VITE_TIER1_PROMOTION_AFTER_REPAIR_LOCK_001

**Proves:** DETERMINEX_REACT_VITE_TIER1_PROMOTION_AFTER_REPAIR_LOCK_001

**Does not prove:** Does not prove broad real-world repair coverage beyond the locked acceptance tests.

#### DETERMINEX_REACT_VITE_TIER1_PROMOTION_DECISION_LOCK_001

**Proves:** DETERMINEX_REACT_VITE_TIER1_PROMOTION_DECISION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REACT_VITE_VERIFICATION_RETRY_AFTER_REPAIR_LOCK_001

**Proves:** DETERMINEX_REACT_VITE_VERIFICATION_RETRY_AFTER_REPAIR_LOCK_001

**Does not prove:** Does not prove broad real-world repair coverage beyond the locked acceptance tests.

#### DETERMINEX_REAL_APPROVAL_RESOLUTION_SWEEP_LOCK_001

**Proves:** DETERMINEX_REAL_APPROVAL_RESOLUTION_SWEEP_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REAL_LOCAL_INSTALL_MOMENTS_INSTALLED_ENTRYPOINTS_LOCK_001

**Proves:** DETERMINEX_REAL_LOCAL_INSTALL_MOMENTS_INSTALLED_ENTRYPOINTS_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REAL_OPERATOR_SIGNATURE_IMPORT_AND_FIRST_SPEND_LOCK_001

**Proves:** DETERMINEX_REAL_OPERATOR_SIGNATURE_IMPORT_AND_FIRST_SPEND_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REAL_OPERATOR_SIGNATURE_IMPORT_LOCK_001

**Proves:** DETERMINEX_REAL_OPERATOR_SIGNATURE_IMPORT_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REAL_OPERATOR_SIGNATURE_IMPORT_PREP_LOCK_001

**Proves:** DETERMINEX_REAL_OPERATOR_SIGNATURE_IMPORT_PREP_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REAL_OPERATOR_SIGNATURE_IMPORT_PROCEDURE_DOCUMENTED_AND_FIRST_SIGNATURE_LANDED_LOCK_001

**Proves:** DETERMINEX_REAL_OPERATOR_SIGNATURE_IMPORT_PROCEDURE_DOCUMENTED_AND_FIRST_SIGNATURE_LANDED_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REAL_OPERATOR_SIGNATURE_IMPORT_PROCEDURE_LOCK_001

**Proves:** DETERMINEX_REAL_OPERATOR_SIGNATURE_IMPORT_PROCEDURE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REAL_SIGNATURE_IMPORT_AND_FIRST_AUTHORITY_SPEND_LOCK_002

**Proves:** Real Signature Import and First Authority Spend

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REAL_SIGNATURE_IMPORT_VALIDATE_AND_FIRST_SPEND_LOCK_003

**Proves:** Real Signature Import, Validation, and First Spend

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REAL_SIGNATURE_INGEST_AND_REACT_VITE_SPEND_RECONCILIATION_LOCK_001

**Proves:** DETERMINEX_REAL_SIGNATURE_INGEST_AND_REACT_VITE_SPEND_RECONCILIATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REAL_SIGNATURE_MATERIAL_SCAN_LOCK_001

**Proves:** DETERMINEX_REAL_SIGNATURE_MATERIAL_SCAN_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REAL_SIGNATURE_VALIDATION_LOCK_001

**Proves:** DETERMINEX_REAL_SIGNATURE_VALIDATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REAL_SIG_SPEND_CLAUDE_CHANGED_FILES_REVIEW_001

**Proves:** Real-sig-spend Claude Lane L. 0 unexpected file changes due to spend (spend did not occur).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REAL_SIG_SPEND_CLAUDE_COMMAND_MATCH_REVIEW_001

**Proves:** Real-sig-spend Claude Lane K. N/A (no spend); approved command unused; no broad install attempted.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REAL_SIG_SPEND_CLAUDE_CURRENT_SOURCE_TRUTH_REVIEW_001

**Proves:** Real-sig-spend Claude Lane D. Current state: HEAD/spine/queue/audit/packet/registry/Tier-1 bound.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REAL_SIG_SPEND_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001

**Proves:** Real-sig-spend Claude Lane S. All forbidden actions audited and avoided.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REAL_SIG_SPEND_CLAUDE_HARD_FLOOR_BOUNDARY_REVIEW_001

**Proves:** Real-sig-spend Claude Lane Q. All hard-floor gates false; signed_spend=0; 23-wave boundary.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REAL_SIG_SPEND_CLAUDE_MARKER_HASH_STABILITY_HARDENING_REVIEW_001

**Proves:** Real-sig-spend Claude Lane B. Codex Lane A hardened marker validator (40-char hash) + stability check + marker successor policy; tests verify malformed/behind/stable cases.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REAL_SIG_SPEND_CLAUDE_MARKER_VALIDITY_REVIEW_001

**Proves:** Real-sig-spend Claude Lane C. Marker valid: ready=true, target matches, hash 40-char, reviewed commit reachable from HEAD via marker successor.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REAL_SIG_SPEND_CLAUDE_QUEUE_COUNT_REVIEW_001

**Proves:** Real-sig-spend Claude Lane H. signed_valid_queue before=0 after=0; no admission.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REAL_SIG_SPEND_CLAUDE_QUEUE_IMPORT_LEGITIMACY_REVIEW_001

**Proves:** Real-sig-spend Claude Lane G. Codex Lane E import BLOCKED; no queue record created without valid material.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REAL_SIG_SPEND_CLAUDE_REACT_VITE_VERIFICATION_REVIEW_001

**Proves:** Real-sig-spend Claude Lane N. Codex Lane H verification BLOCKED; no transcript without execution.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REAL_SIG_SPEND_CLAUDE_ROLLBACK_RECORD_REVIEW_001

**Proves:** Real-sig-spend Claude Lane M. Rollback plan documented; not exercised (no spend).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REAL_SIG_SPEND_CLAUDE_SBOM_PACKET_CARRY_REVIEW_001

**Proves:** Real-sig-spend Claude Lane P. Codex Lane I SBOM packet CARRIED_UNSIGNED; next-floor packet prepared; no execution.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REAL_SIG_SPEND_CLAUDE_SCORE_MOVEMENT_EVIDENCE_REVIEW_001

**Proves:** Real-sig-spend Claude Lane R. Codex Lane J no score movement; scores unchanged.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REAL_SIG_SPEND_CLAUDE_SIGNATURE_MATERIAL_SCAN_REVIEW_001

**Proves:** Real-sig-spend Claude Lane E. Codex Lane C scan BLOCKED_MISSING; canonical inbox scanned; no material present.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REAL_SIG_SPEND_CLAUDE_SIGNATURE_VALIDATION_REVIEW_001

**Proves:** Real-sig-spend Claude Lane F. Codex Lane D verdict BLOCKED_MISSING_MATERIAL; no fake validation.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REAL_SIG_SPEND_CLAUDE_SPEND_ELIGIBILITY_REVIEW_001

**Proves:** Real-sig-spend Claude Lane I. Codex Lane F eligibility BLOCKED; queue empty → no spend authority.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REAL_SIG_SPEND_CLAUDE_SPEND_OCCURRED_REVIEW_001

**Proves:** Real-sig-spend Claude Lane J. Codex Lane G spend BLOCKED; no execution; signed_spend remains 0.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REAL_SIG_SPEND_CLAUDE_SYNTHESIS_REVIEW_001

**Proves:** Real-sig-spend Claude Lane T. Synthesis + 35-item final report. Acceptable blocked case verified; marker hardening successful; channel ready for real signature material.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REAL_SIG_SPEND_CLAUDE_TIER1_COVERAGE_REVIEW_001

**Proves:** Real-sig-spend Claude Lane O. Tier-1 unchanged; react_vite still typed-blocked; tauri still typed-blocked.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REAL_SIG_SPEND_CLAUDE_TIMER_PROTOCOL_REVIEW_001

**Proves:** Real-sig-spend Claude Lane A. Timer protocol applied with NEW stability requirement; 9 rechecks; 2-recheck stability check passed at af5d2d1be.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REAL_USER_REPO_MUTATION_FORBIDDEN_GUARD_LOCK_001

**Proves:** Real-User Repo Mutation Forbidden Guard

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REEVALUATE_THREE_LOCAL_PREVIEW_PACKAGE_CELLS_LOCK_001

**Proves:** Re-Evaluate Three Local-Preview Package Cells

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RELEASE_AUTHORITY_PACKET_SCHEMA_LOCK_001

**Proves:** DETERMINEX_RELEASE_AUTHORITY_PACKET_SCHEMA_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RELEASE_AUTHORITY_QUEUE_SPEND_SYSTEM_LOCK_001

**Proves:** DETERMINEX_RELEASE_AUTHORITY_QUEUE_SPEND_SYSTEM_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RELEASE_AUTHORITY_VALIDATOR_REJECTION_CORPUS_LOCK_001

**Proves:** DETERMINEX_RELEASE_AUTHORITY_VALIDATOR_REJECTION_CORPUS_LOCK_001

**Does not prove:** Does not prove corpus balance, training effectiveness, or public benchmark dominance by itself.

#### DETERMINEX_RELEASE_CAMPAIGN_LOCK_STAGING_LOCK_001

**Proves:** Release Campaign Lock Staging

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RELEASE_CANDIDATE_GUARDS_AND_RECONCILIATION_LOCK_001

**Proves:** DETERMINEX_RELEASE_CANDIDATE_GUARDS_AND_RECONCILIATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RELEASE_CANDIDATE_PROOF_MAP_LOCK_001

**Proves:** DETERMINEX_RELEASE_CANDIDATE_PROOF_MAP_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RELEASE_CANDIDATE_SIGNATURE_RECHECK_BRANCH_DECISION_LOCK_001

**Proves:** DETERMINEX_RELEASE_CANDIDATE_SIGNATURE_RECHECK_BRANCH_DECISION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RELEASE_CELL_DECERTIFICATION_AND_ROLLBACK_PROCEDURE_LOCK_001

**Proves:** Define release-cell decertification triggers, downgrade statuses, rollback reports, and paired counter behavior.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RELEASE_CELL_DRIFT_DETECTOR_GITHUB_WORKFLOW_LOCK_001

**Proves:** Drift Detector GitHub Workflow / Status Guard

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RELEASE_CELL_PROMOTION_REQUIRES_SIGNOFF_AND_ANCHOR_LOCK_001

**Proves:** Promotion Requires Signoff and Proof Anchor

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RELEASE_CELL_SIGNOFF_GATE_ENFORCEMENT_CI_LOCK_001

**Proves:** Signoff Gate Enforcement CI

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RELEASE_CELL_VERIFIER_SIGNOFF_SCHEMA_LOCK_001

**Proves:** Verifier Signoff Schema for Release Promotion

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RELEASE_GATE_BETA_DASHBOARD_PUBLICATION_GATE_LOCK_001

**Proves:** DETERMINEX_RELEASE_GATE_BETA_DASHBOARD_PUBLICATION_GATE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RELEASE_GATE_CLEAN_HOST_PACKET_CERTIFICATION_LOCK_001

**Proves:** DETERMINEX_RELEASE_GATE_CLEAN_HOST_PACKET_CERTIFICATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RELEASE_GATE_FULL_STATUS_TIMEOUT_REPAIR_PLAN_LOCK_001

**Proves:** DETERMINEX_RELEASE_GATE_FULL_STATUS_TIMEOUT_REPAIR_PLAN_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RELEASE_GATE_GUI_BUILD_PACKET_CERTIFICATION_LOCK_001

**Proves:** DETERMINEX_RELEASE_GATE_GUI_BUILD_PACKET_CERTIFICATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RELEASE_GATE_INSTALLER_RELEASE_PACKET_CERTIFICATION_LOCK_001

**Proves:** DETERMINEX_RELEASE_GATE_INSTALLER_RELEASE_PACKET_CERTIFICATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RELEASE_GATE_REACT_VITE_DEPENDENCY_ADMISSION_LOCK_001

**Proves:** DETERMINEX_RELEASE_GATE_REACT_VITE_DEPENDENCY_ADMISSION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RELEASE_GATE_SBOM_PACKET_CERTIFICATION_LOCK_001

**Proves:** DETERMINEX_RELEASE_GATE_SBOM_PACKET_CERTIFICATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RELEASE_HYGIENE_SBOM_LICENSE_SECURITY_SIGNING_EXECUTION_LOCK_001

**Proves:** Execute release hygiene gate setup for SBOM, license, security, signing, and public installer wording without claiming release readiness.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RELEASE_INSTALL_PACKAGING_GAP_AUDIT_001

**Proves:** Audit/planning lock that attacks dimension I (release / install / packaging) of the true-100 deficiency decomposition. Maps every missing rung before any release-supported cell can exist, ranks candidate cells by release distance, and emits a 7-lock Codex zero-to-nonzero plan plus follow-on prompts and claim-boundary warnings.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RELEASE_PROMOTION_GATE_NEGATIVE_TESTS_LOCK_001

**Proves:** Release Promotion Gate End-to-End Negative Tests

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RELEASE_REGISTRY_MUTATION_SIGNOFF_LOCK_001

**Proves:** DETERMINEX_RELEASE_REGISTRY_MUTATION_SIGNOFF_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RELEASE_SUPPORTED_CELL_CONVEYOR_BINDING_LOCK_001

**Proves:** Release Cell Conveyor Binding

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RELEASE_SUPPORTED_CELL_DRIFT_DETECTOR_CI_LOCK_001

**Proves:** Release Cell Drift Detector CI

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REMAINING_FAMILY_AUTHORITY_BATCH_GATE_LOCK_001

**Proves:** Remaining Family Authority Batch Gate

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REMAINING_FAMILY_BROWSER_TAURI_COMPRESSION_LOCK_001

**Proves:** Remaining Family Browser/Tauri Compression

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REMAINING_FAMILY_COMPLETION_SURGE_LOCK_001

**Proves:** DETERMINEX_REMAINING_FAMILY_COMPLETION_SURGE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REMAINING_FAMILY_HIGH_RISK_BOUNDARY_LOCK_001

**Proves:** REMAINING_FAMILY_HIGH_RISK_BOUNDARIES_RECORDED for DETERMINEX_CLEAN_RUNNER_SAFE_CLONE_BROADER_SBOM_T_DRIVE_RELOCATION_AND_DETECTOR_EXPANSION_WAVE_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REMAINING_FAMILY_HIGH_RISK_COMPRESSION_LOCK_001

**Proves:** Remaining Family ML/Mobile/Hardware/Kotlin/Swift Compression

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REMAINING_FAMILY_KOTLIN_SWIFT_GATE_LOCK_001

**Proves:** Remaining Family Kotlin/Swift Gate

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REMAINING_FAMILY_PHP_RUBY_COMPRESSION_LOCK_001

**Proves:** Remaining Family PHP/Ruby Compression

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REMAINING_FAMILY_PHP_RUBY_GATE_LOCK_001

**Proves:** Remaining Family PHP/Ruby Gate

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REMAINING_FAMILY_SAFE_EXECUTION_BATCH_LOCK_001

**Proves:** DETERMINEX_REMAINING_FAMILY_SAFE_EXECUTION_BATCH_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REMAINING_FAMILY_STATUS_EXPANSION_LOCK_001

**Proves:** DETERMINEX_REMAINING_FAMILY_STATUS_EXPANSION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REMAINING_FAMILY_STRUCTURAL_GATE_LOCK_001

**Proves:** Remaining Family Structural Gate

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REPAIR_LOOP_READINESS_MAP_LOCK_001

**Proves:** Repair Loop Readiness Map

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REPO_CLINIC_FIXTURE_REPAIR_SPLASH_DEMO_LOCK_001

**Proves:** Execute the second verified splash path: a Python Repo Clinic fixture repo with a baseline failing verifier, quarantined one-file repair patch, fixture-only application, and post-patch verifier evidence.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REPO_CLINIC_PROGRAM_AUTHORITY_INTAKE_LOCK_001

**Proves:** DETERMINEX_REPO_CLINIC_PROGRAM_AUTHORITY_INTAKE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REPO_CLINIC_REPAIR_LOOP_SECOND_FAMILY_LOCK_001

**Proves:** DETERMINEX_REPO_CLINIC_REPAIR_LOOP_SECOND_FAMILY_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REPO_CLINIC_UNDER_THE_HOOD_E2E_PIPELINE_LOCK_001

**Proves:** DETERMINEX_REPO_CLINIC_UNDER_THE_HOOD_E2E_PIPELINE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REPO_CLINIC_WORKFLOW_LOCK_001

**Proves:** Rung 3 of DETERMINEX_UNIFIED_PRODUCT_UX_SHELL_SERIES.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_REVIEW_MARKER_HASH_AND_STABILITY_HARDENING_LOCK_001

**Proves:** DETERMINEX_REVIEW_MARKER_HASH_AND_STABILITY_HARDENING_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RUBY_STRUCTURAL_MAPPING_BOUNDARY_GUARD_LOCK_001

**Proves:** Ruby Structural Mapping Boundary Guard

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RUBY_TOOLCHAIN_ABSENCE_GATE_LOCK_001

**Proves:** Ruby Toolchain Absence Gate

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RUNTIME_APPROVAL_HARDENING_BACKFILL_LOCK_002

**Proves:** Runtime Approval Hardening Backfill

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RUNTIME_APPROVAL_HARDENING_BEFORE_FIRST_SPEND_LOCK_001

**Proves:** Runtime Approval Hardening Before First Spend

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RUNTIME_APPROVAL_HARDENING_COMPLETION_LOCK_003

**Proves:** Runtime Approval Hardening Completion

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RUNTIME_APPROVAL_HARDENING_TESTS_LIVE_LOCK_001

**Proves:** Runtime Approval Hardening Tests Live

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RVREP_CLAUDE_BETA_DASHBOARD_NOT_PUBLISHED_REVIEW_001

**Proves:** RV-repair Claude Lane W. Beta dashboard did not publish.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RVREP_CLAUDE_BINARY_MUTATION_REVIEW_001

**Proves:** RV-repair Claude Lane G. Binaries NOT edited.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RVREP_CLAUDE_BOUNDED_REPAIR_GUARD_REVIEW_001

**Proves:** RV-repair Claude Lane I. Bounded repair guard in place.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RVREP_CLAUDE_BUILD_RETRY_REVIEW_001

**Proves:** RV-repair Claude Lane M. Build retry verdict PASSED.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RVREP_CLAUDE_CHANGED_SOURCE_FILES_REVIEW_001

**Proves:** RV-repair Claude Lane C. Changed source files = 3 frontend components only.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RVREP_CLAUDE_CLEAN_HOST_NOT_EXECUTED_REVIEW_001

**Proves:** RV-repair Claude Lane T. Clean-host did not execute.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RVREP_CLAUDE_EVIDENCE_INDEX_GUARDS_REVIEW_001

**Proves:** RV-repair Claude Lane AD. Evidence index clean; append-only + count-drift guards hold.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RVREP_CLAUDE_FAMILY_STATUSES_SAFE_REVIEW_001

**Proves:** RV-repair Claude Lane Y. Family statuses claim-safe; 31 families with status codes.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RVREP_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001

**Proves:** RV-repair Claude Lane AE. 17 forbidden actions all avoided per marker.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RVREP_CLAUDE_GUI_BUILD_NOT_EXECUTED_REVIEW_001

**Proves:** RV-repair Claude Lane U. GUI/build did not execute.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RVREP_CLAUDE_INSTALLER_RELEASE_NOT_EXECUTED_REVIEW_001

**Proves:** RV-repair Claude Lane V. Installer/release did not execute.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RVREP_CLAUDE_LINT_CLASSIFICATION_REVIEW_001

**Proves:** RV-repair Claude Lane A. Lint failure correctly classified as SOURCE_LINT_ERROR_REPAIR_AUTHORIZED.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RVREP_CLAUDE_LINT_CONFIG_MUTATION_REVIEW_001

**Proves:** RV-repair Claude Lane F. Lint config NOT modified.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RVREP_CLAUDE_LINT_RETRY_REVIEW_001

**Proves:** RV-repair Claude Lane K. Lint retry verdict PASSED.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RVREP_CLAUDE_LOCKFILE_MUTATION_REVIEW_001

**Proves:** RV-repair Claude Lane H. Package manifests/lockfiles NOT changed without spend.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RVREP_CLAUDE_MARCH_PLAN_DASHBOARD_REVIEW_001

**Proves:** RV-repair Claude Lane AA. March-plan dashboard accurate; not release hype.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RVREP_CLAUDE_NO_MUTATION_GUARD_REVIEW_001

**Proves:** RV-repair Claude Lane J. No-test/verifier/binary-mutation guard in place.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RVREP_CLAUDE_REACT_VITE_VERIFICATION_REVIEW_001

**Proves:** RV-repair Claude Lane O. React/Vite local verification verdict = PASSED.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RVREP_CLAUDE_RELEASE_INVARIANTS_REVIEW_001

**Proves:** RV-repair Claude Lane AB. Release cells (10) and families (0) remain canonical.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RVREP_CLAUDE_RUNTIME_QUEUE_CONSISTENCY_REVIEW_001

**Proves:** RV-repair Claude Lane Q. Runtime queue did not mutate unexpectedly (1→1).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RVREP_CLAUDE_SBOM_NOT_EXECUTED_REVIEW_001

**Proves:** RV-repair Claude Lane S. SBOM did not execute.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RVREP_CLAUDE_SCORE_MOVEMENT_REVIEW_001

**Proves:** RV-repair Claude Lane AC. Score movement proposed but not canonicalized (evidence-bound).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RVREP_CLAUDE_SIGNED_SPEND_CONSISTENCY_REVIEW_001

**Proves:** RV-repair Claude Lane R. Signed spend did not mutate unexpectedly (1→1; spend not reused).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RVREP_CLAUDE_SMOKE_RETRY_REVIEW_001

**Proves:** RV-repair Claude Lane N. Static export smoke retry verdict PASSED.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RVREP_CLAUDE_SOURCE_REPAIR_BOUNDED_REVIEW_001

**Proves:** RV-repair Claude Lane B. Repair touched only Determinex-owned source needed for lint errors.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RVREP_CLAUDE_SYNTHESIS_REVIEW_001

**Proves:** RV-repair Claude Lane AF. Synthesis + 57-item final report.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RVREP_CLAUDE_TEST_MUTATION_REVIEW_001

**Proves:** RV-repair Claude Lane D. Tests NOT edited to hide failure.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RVREP_CLAUDE_TEST_RETRY_REVIEW_001

**Proves:** RV-repair Claude Lane L. Test retry verdict PASSED.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RVREP_CLAUDE_TIER1_PROMOTION_CANONICAL_REVIEW_001

**Proves:** RV-repair Claude Lane P. Tier-1 promotion follows canonical rules (8→9 local).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RVREP_CLAUDE_UNIVERSAL_ACCOUNTING_MAP_REVIEW_001

**Proves:** RV-repair Claude Lane X. Universal family accounting conveyor is a MAP, not support claim.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RVREP_CLAUDE_VERIFICATION_WITH_CAPABILITY_REVIEW_001

**Proves:** RV-repair Claude Lane Z. Verification-with-capability rule prevents ladder inversion.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RVREP_CLAUDE_VERIFIER_ORACLE_MUTATION_REVIEW_001

**Proves:** RV-repair Claude Lane E. Verifier/oracle/lint config NOT weakened.

**Does not prove:** Does not prove broad real-world repair coverage beyond the locked acceptance tests.

#### DETERMINEX_RV_VERIFY_CLAUDE_ADMISSION_VS_VERIFICATION_BOUNDARY_REVIEW_001

**Proves:** RV-verify Claude Lane B. Dependency admission was NOT confused with local verification.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RV_VERIFY_CLAUDE_APPEND_ONLY_COUNT_DRIFT_REVIEW_001

**Proves:** RV-verify Claude Lane W. Append-only and count-drift guards hold.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RV_VERIFY_CLAUDE_BETA_DASHBOARD_NOT_PUBLISHED_REVIEW_001

**Proves:** RV-verify Claude Lane P. Beta dashboard not published.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RV_VERIFY_CLAUDE_BUILD_RESULT_ACCURATE_REVIEW_001

**Proves:** RV-verify Claude Lane F. Build result accurately reported (exit=0, Next.js compiled, static pages generated).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RV_VERIFY_CLAUDE_CHANGED_FILES_ALLOWED_REVIEW_001

**Proves:** RV-verify Claude Lane I. Changed files allowed: empty list; lockfile hash matches before/after.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RV_VERIFY_CLAUDE_CLAIM_OVERCLAIM_SCANNER_REVIEW_001

**Proves:** RV-verify Claude Lane X. Claim scanner + Day 1 overclaim scanner pass.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RV_VERIFY_CLAUDE_CLEAN_HOST_NOT_EXECUTED_REVIEW_001

**Proves:** RV-verify Claude Lane M. Clean-host not executed.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RV_VERIFY_CLAUDE_DIRTY_STATE_REPORTED_REVIEW_001

**Proves:** RV-verify Claude Lane Z. Dirty/untracked state reported.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RV_VERIFY_CLAUDE_EVIDENCE_INDEX_CLEAN_REVIEW_001

**Proves:** RV-verify Claude Lane V. Evidence index clean at 1411 entries.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RV_VERIFY_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001

**Proves:** RV-verify Claude Lane AA. All forbidden actions audited and avoided.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RV_VERIFY_CLAUDE_GUI_BUILD_NOT_EXECUTED_REVIEW_001

**Proves:** RV-verify Claude Lane N. GUI/build not executed.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RV_VERIFY_CLAUDE_INSTALLER_RELEASE_NOT_EXECUTED_REVIEW_001

**Proves:** RV-verify Claude Lane O. Installer/release not executed.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RV_VERIFY_CLAUDE_NO_FORBIDDEN_PROTECTED_ACTION_REVIEW_001

**Proves:** RV-verify Claude Lane K. No forbidden protected action ran (no SBOM/clean-host/GUI/installer/public-upload).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RV_VERIFY_CLAUDE_NO_UNRELATED_DRIFT_REVIEW_001

**Proves:** RV-verify Claude Lane J. No unrelated dependency drift; package.json + package-lock.json unchanged hashes.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RV_VERIFY_CLAUDE_PRIOR_SPEND_BINDING_REVIEW_001

**Proves:** RV-verify Claude Lane A. Prior React/Vite spend evidence was bound correctly.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RV_VERIFY_CLAUDE_RELEASE_CELLS_CANONICAL_REVIEW_001

**Proves:** RV-verify Claude Lane R. Release-supported exact cells canonical (10).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RV_VERIFY_CLAUDE_RELEASE_FAMILIES_CANONICAL_REVIEW_001

**Proves:** RV-verify Claude Lane S. Release-supported families canonical (0).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RV_VERIFY_CLAUDE_RUNTIME_QUEUE_SPEND_CONSISTENCY_REVIEW_001

**Proves:** RV-verify Claude Lane Y. Runtime queue/spend consistency holds (queue=1, spend=1; one-to-one).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RV_VERIFY_CLAUDE_SBOM_NOT_EXECUTED_REVIEW_001

**Proves:** RV-verify Claude Lane L. SBOM not executed.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RV_VERIFY_CLAUDE_SCORE_MOVEMENT_EVIDENCE_BOUND_REVIEW_001

**Proves:** RV-verify Claude Lane T. Score movement, if any, is evidence-bound (rejected_no_evidence_delta this wave).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RV_VERIFY_CLAUDE_SMOKE_LINT_RESULT_ACCURATE_REVIEW_001

**Proves:** RV-verify Claude Lane H. Lint/smoke result accurately reported (exit=1, 5 errors + 55 warnings; FAILED).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RV_VERIFY_CLAUDE_SYNTHESIS_REVIEW_001

**Proves:** RV-verify Claude Lane AB. Synthesis + 46-item final report.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RV_VERIFY_CLAUDE_TEST_RESULT_ACCURATE_REVIEW_001

**Proves:** RV-verify Claude Lane G. Test result accurately reported (exit=0, 17/17 vitest tests passed).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RV_VERIFY_CLAUDE_TIER1_PROMOTION_CANONICAL_REVIEW_001

**Proves:** RV-verify Claude Lane Q. Tier-1 promotion correctly NOT performed (verification blocked = no promotion).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RV_VERIFY_CLAUDE_TIMEOUT_NOT_HIDDEN_REVIEW_001

**Proves:** RV-verify Claude Lane U. Full-status timeout work did not disable/skip/delete tests.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RV_VERIFY_CLAUDE_VERIFICATION_COMMANDS_BOUNDED_REVIEW_001

**Proves:** RV-verify Claude Lane D. Verification commands were bounded (only 3 commands; explicit cwd; timeout-aware).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RV_VERIFY_CLAUDE_VERIFICATION_PLAN_REAL_SCRIPTS_REVIEW_001

**Proves:** RV-verify Claude Lane C. Verification plan used real project scripts (npm run lint/test/build).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_RV_VERIFY_CLAUDE_VERIFICATION_TRANSCRIPTS_EXIST_REVIEW_001

**Proves:** RV-verify Claude Lane E. Verification transcripts exist.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SBOM_BLOCKER_REVALIDATION_LOCK_001

**Proves:** DETERMINEX_SBOM_BLOCKER_REVALIDATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SBOM_BYTE_EXACT_POLICY_LOCK_001

**Proves:** SBOM Byte-Exact Policy

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SBOM_EXECUTION_RETRY_LOCK_001

**Proves:** DETERMINEX_SBOM_EXECUTION_RETRY_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SBOM_EXECUTION_VERIFICATION_LOCK_001

**Proves:** DETERMINEX_SBOM_EXECUTION_VERIFICATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SBOM_FAMILY_SURGE_CAPABILITY_SCORE_DISCIPLINE_LOCK_001

**Proves:** DETERMINEX_SBOM_FAMILY_SURGE_CAPABILITY_SCORE_DISCIPLINE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SBOM_FAMILY_SURGE_MARCH_PLAN_DASHBOARD_LOCK_001

**Proves:** DETERMINEX_SBOM_FAMILY_SURGE_MARCH_PLAN_DASHBOARD_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SBOM_LICENSE_SECURITY_SIGNING_CLAUDE_REVIEW_001

**Proves:** Wave 006 Lane S. 12-layer trust chain post packet-prep. 1 PASSED + 1 PREPARED + 6 NOT_STARTED + 4 MISSING.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SBOM_LICENSE_SECURITY_SIGNING_TRUST_CHAIN_CLAUDE_REVIEW_001

**Proves:** Overnight Lane 9. 13-layer trust chain: 3 PASSED + 2 BLOCKED + 4 NOT_STARTED + 4 MISSING.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SBOM_LICENSE_SECURITY_TRUST_SPINE_LOCK_001

**Proves:** DETERMINEX_SBOM_LICENSE_SECURITY_TRUST_SPINE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SBOM_NEXT_GATE_AFTER_CLEAN_HOST_RUNTIME_LOCK_001

**Proves:** SBOM Next Gate After Clean-Host Runtime

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SBOM_PACKET_CARRY_AFTER_SIGNATURE_CHANNEL_LOCK_001

**Proves:** DETERMINEX_SBOM_PACKET_CARRY_AFTER_SIGNATURE_CHANNEL_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SBOM_PACKET_HARDENING_LOCK_001

**Proves:** DETERMINEX_SBOM_PACKET_HARDENING_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SBOM_ROUTE_DECISION_LOCK_001

**Proves:** DETERMINEX_SBOM_ROUTE_DECISION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SBOM_SIGNING_INSTALLER_TRUST_CLAUDE_REVIEW_001

**Proves:** Wave 007 Claude Lane S. Syft signed admission, SBOM emission, license review, security scan route, code-signing posture, SmartScreen guidance, public-installer wording linter, internal preview trust chain.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SBOM_TOOL_ADMISSION_AND_STANDARDS_SBOM_GENERATION_LOCK_001

**Proves:** Generate standards SBOM with an available local tool or emit exact SBOM tool admission packet.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SBOM_TOOL_ADMISSION_DECISION_LOCK_001

**Proves:** DETERMINEX_SBOM_TOOL_ADMISSION_DECISION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SBOM_TOOL_FAMILY_SURGE_RECONCILIATION_LOCK_001

**Proves:** DETERMINEX_SBOM_TOOL_FAMILY_SURGE_RECONCILIATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SBOM_TOOL_INSTALL_OR_ALTERNATIVE_VERIFICATION_LOCK_001

**Proves:** DETERMINEX_SBOM_TOOL_INSTALL_OR_ALTERNATIVE_VERIFICATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SBOM_TOOL_RUNTIME_ADMISSION_SPEND_LOCK_001

**Proves:** DETERMINEX_SBOM_TOOL_RUNTIME_ADMISSION_SPEND_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SCAFFOLD_BUILD_TEST_SMOKE_EXPANSION_LOCK_001

**Proves:** Define deterministic metadata-only scaffold/build/test/smoke candidate expansion after fixture admission while preserving blockers and keeping execution, support-depth promotion, release support, source mutation, proof execution, and training authority closed.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SCORE_BASELINE_RECONCILIATION_LOCK_001

**Proves:** DETERMINEX_SCORE_BASELINE_RECONCILIATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SCORE_DEFINITION_BINDING_AND_EVIDENCE_DELTA_CI_LOCK_001

**Proves:** DETERMINEX_SCORE_DEFINITION_BINDING_AND_EVIDENCE_DELTA_CI_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SCORE_DELTA_CI_AND_PUBLIC_CLAIM_LINTER_EXPANSION_LOCK_001

**Proves:** Score Delta CI and Public Claim Linter Expansion

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SCORE_DELTA_CI_AND_PUBLIC_CLAIM_SCANNER_CLOSURE_LOCK_002

**Proves:** Score Delta CI and Public Claim Scanner Closure

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SCORE_RELEASE_DISCIPLINE_LOCK_001

**Proves:** DETERMINEX_SCORE_RELEASE_DISCIPLINE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SCORE_RISE_REQUIRES_EVIDENCE_DELTA_CI_LOCK_001

**Proves:** DETERMINEX_SCORE_RISE_REQUIRES_EVIDENCE_DELTA_CI_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIGNABLE_APPROVAL_PACKET_FINALIZATION_SWEEP_LOCK_001

**Proves:** DETERMINEX_SIGNABLE_APPROVAL_PACKET_FINALIZATION_SWEEP_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIGNATURE_DELIVERY_CHANNEL_RECONCILIATION_LOCK_001

**Proves:** DETERMINEX_SIGNATURE_DELIVERY_CHANNEL_RECONCILIATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIGNATURE_DELIVERY_CURRENT_STATE_RECONCILIATION_LOCK_001

**Proves:** DETERMINEX_SIGNATURE_DELIVERY_CURRENT_STATE_RECONCILIATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIGNATURE_DELIVERY_REVIEW_READY_PROTOCOL_LOCK_001

**Proves:** DETERMINEX_SIGNATURE_DELIVERY_REVIEW_READY_PROTOCOL_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIGNATURE_INGEST_CURRENT_STATE_RECONCILIATION_LOCK_001

**Proves:** DETERMINEX_SIGNATURE_INGEST_CURRENT_STATE_RECONCILIATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIGNATURE_INGEST_SPEND_SCORE_BOUNDARY_RECONCILIATION_LOCK_001

**Proves:** DETERMINEX_SIGNATURE_INGEST_SPEND_SCORE_BOUNDARY_RECONCILIATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIGNATURE_SPEND_CURRENT_STATE_RECONCILIATION_LOCK_001

**Proves:** DETERMINEX_SIGNATURE_SPEND_CURRENT_STATE_RECONCILIATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIGNATURE_SPEND_REVIEW_READY_PROTOCOL_LOCK_001

**Proves:** DETERMINEX_SIGNATURE_SPEND_REVIEW_READY_PROTOCOL_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIGNATURE_SPEND_SCORE_AND_COVERAGE_RECONCILIATION_LOCK_001

**Proves:** DETERMINEX_SIGNATURE_SPEND_SCORE_AND_COVERAGE_RECONCILIATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIGNED_APPROVAL_OPERATOR_AUTHORITY_CLAUDE_REVIEW_001

**Proves:** Wave 006 Lane Y. Signed approval / operator authority review. 5 packets inventoried; 1 landed; 4 prepared/blocked. 5 procedural gaps named.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIGNED_GUI_DRIVER_FIRST_VISUAL_PROOF_LOCK_002

**Proves:** Signed GUI Driver and First Visual Proof

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIGNED_GUI_DRIVER_FIRST_VISUAL_SPEND_LOCK_001

**Proves:** Signed GUI Driver First Visual Spend

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIGNED_MSEDGEDRIVER_ADMISSION_AND_GUI_FIRST_PAINT_EXECUTION_LOCK_001

**Proves:** DETERMINEX_SIGNED_MSEDGEDRIVER_ADMISSION_AND_GUI_FIRST_PAINT_EXECUTION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIGNED_MSEDGEDRIVER_AND_GUI_FIRST_PAINT_EXECUTION_LOCK_002

**Proves:** DETERMINEX_SIGNED_MSEDGEDRIVER_AND_GUI_FIRST_PAINT_EXECUTION_LOCK_002

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIGNED_MSEDGEDRIVER_AND_GUI_FIRST_PAINT_EXECUTION_LOCK_003

**Proves:** DETERMINEX_SIGNED_MSEDGEDRIVER_AND_GUI_FIRST_PAINT_EXECUTION_LOCK_003

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIGNED_NSIS_APPROVAL_AND_INSTALL_LAUNCH_UNINSTALL_RETRY_LOCK_001

**Proves:** DETERMINEX_SIGNED_NSIS_APPROVAL_AND_INSTALL_LAUNCH_UNINSTALL_RETRY_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIGNED_NSIS_APPROVAL_AND_INSTALL_SMOKE_EXECUTION_LOCK_002

**Proves:** DETERMINEX_SIGNED_NSIS_APPROVAL_AND_INSTALL_SMOKE_EXECUTION_LOCK_002

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIGNED_QUEUE_SPEND_ELIGIBILITY_GATE_LOCK_001

**Proves:** DETERMINEX_SIGNED_QUEUE_SPEND_ELIGIBILITY_GATE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIGNED_SPEND_AUDIT_AND_BOUNDARY_LOCK_001

**Proves:** DETERMINEX_SIGNED_SPEND_AUDIT_AND_BOUNDARY_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIGNED_VALID_APPROVAL_QUEUE_MATERIALIZATION_LOCK_001

**Proves:** DETERMINEX_SIGNED_VALID_APPROVAL_QUEUE_MATERIALIZATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIGNED_VALID_QUEUE_IMPORT_REACT_VITE_LOCK_001

**Proves:** DETERMINEX_SIGNED_VALID_QUEUE_IMPORT_REACT_VITE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIG_DELIVERY_CLAUDE_AUTHORITY_BOUNDARY_REVIEW_001

**Proves:** Sig-delivery Claude Lane P. All 10 Codex lanes authority/protected_external_action=false; 22-wave boundary.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIG_DELIVERY_CLAUDE_CANONICAL_INBOX_PATH_REVIEW_001

**Proves:** Sig-delivery Claude Lane E. Canonical inbox path defined; existing candidate dirs reconciled.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIG_DELIVERY_CLAUDE_CURRENT_SOURCE_TRUTH_REVIEW_001

**Proves:** Sig-delivery Claude Lane C. Current state: HEAD/spine/queue/audit/packet/registry/Tier-1 source-truth bound.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIG_DELIVERY_CLAUDE_DELIVERY_CHANNEL_REVIEW_001

**Proves:** Sig-delivery Claude Lane D. Channel spec / canonical inbox path / quarantine / archive / audit behavior all documented.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIG_DELIVERY_CLAUDE_DRY_RUN_IMPORT_REVIEW_001

**Proves:** Sig-delivery Claude Lane J. Dry-run import BLOCKED_NO_REAL_MATERIAL; queue unchanged; audit no-spend event recorded.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIG_DELIVERY_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001

**Proves:** Sig-delivery Claude Lane R. All forbidden actions audited and avoided.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIG_DELIVERY_CLAUDE_INVALID_REJECTION_CORPUS_REVIEW_001

**Proves:** Sig-delivery Claude Lane I. 14 invalid fixtures each rejected with typed reason.

**Does not prove:** Does not prove corpus balance, training effectiveness, or public benchmark dominance by itself.

#### DETERMINEX_SIG_DELIVERY_CLAUDE_MARKER_VALIDITY_REVIEW_001

**Proves:** Sig-delivery Claude Lane B. Marker validity AFTER amend; HISTORICAL FINDING: initial marker hash invalid (41 chars vs 40); Codex amended commit and re-emitted; tests now 12/12 pass.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIG_DELIVERY_CLAUDE_OPERATOR_INSTRUCTIONS_REVIEW_001

**Proves:** Sig-delivery Claude Lane G. Operator-facing instructions documented.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIG_DELIVERY_CLAUDE_OPTIONAL_QUEUE_IMPORT_REVIEW_001

**Proves:** Sig-delivery Claude Lane L. Queue import BLOCKED (no real material exists); queue remains 0.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIG_DELIVERY_CLAUDE_QUEUE_MUTATION_REVIEW_001

**Proves:** Sig-delivery Claude Lane M. Queue before=0 after=0; no admission row added in this wave.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIG_DELIVERY_CLAUDE_REACT_VITE_ELIGIBILITY_REVIEW_001

**Proves:** Sig-delivery Claude Lane O. Eligibility recheck BLOCKED; React/Vite stays typed-blocked.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIG_DELIVERY_CLAUDE_SCORE_MOVEMENT_EVIDENCE_REVIEW_001

**Proves:** Sig-delivery Claude Lane Q. No score movement claimed (channel build is not capability rise).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIG_DELIVERY_CLAUDE_SIGNATURE_SCHEMA_REVIEW_001

**Proves:** Sig-delivery Claude Lane F. Required fields (signer_identity/signature/signed_at/expires_at/packet_hash/command/scope/rollback/timeout/files/risk/one_time_spend) enumerated.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIG_DELIVERY_CLAUDE_SIGNED_SPEND_COUNT_REVIEW_001

**Proves:** Sig-delivery Claude Lane N. signed_spend 0→0; no spend in delivery-channel wave (correct).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIG_DELIVERY_CLAUDE_SYNTHESIS_REVIEW_001

**Proves:** Sig-delivery Claude Lane S. Synthesis + 35-item final report. Acceptable blocked case verified; channel ready for real signature material; historical marker-hash defect documented.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIG_DELIVERY_CLAUDE_TEMPLATE_REJECTION_REVIEW_001

**Proves:** Sig-delivery Claude Lane K. Template artifact present with warnings; validator rejects template as non-real material.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIG_DELIVERY_CLAUDE_TIMER_PROTOCOL_REVIEW_001

**Proves:** Sig-delivery Claude Lane A. Timer protocol applied; 7 rechecks; deadline 60 min respected.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIG_DELIVERY_CLAUDE_VALIDATOR_BEHAVIOR_REVIEW_001

**Proves:** Sig-delivery Claude Lane H. Validator rejects malformed / wrong-hash / broadened command / missing identity / expired / unsigned / placeholder material.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIG_SPEND_CLAUDE_CHANGED_FILES_REVIEW_001

**Proves:** Sig-spend Claude Lane I. 0 unexpected file changes due to spend (spend did not occur).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIG_SPEND_CLAUDE_COMMAND_MATCH_REVIEW_001

**Proves:** Sig-spend Claude Lane H. N/A (no spend); approved command unused; no broad install attempted.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIG_SPEND_CLAUDE_CURRENT_SOURCE_TRUTH_REVIEW_001

**Proves:** Sig-spend Claude Lane C. HEAD/spine/queue/audit/packet/registry/Tier-1/baseline current.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIG_SPEND_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001

**Proves:** Sig-spend Claude Lane Q. All forbidden actions audited and avoided.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIG_SPEND_CLAUDE_HARD_FLOOR_BOUNDARY_REVIEW_001

**Proves:** Sig-spend Claude Lane N. All hard-floor gates still false; signed_spend=0; 21-wave boundary.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIG_SPEND_CLAUDE_MARKER_VALIDITY_REVIEW_001

**Proves:** Sig-spend Claude Lane B. Marker valid; target wave matches; reviewed commit = HEAD.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIG_SPEND_CLAUDE_NEXT_PACKET_REVIEW_001

**Proves:** Sig-spend Claude Lane O. Lane-H next packet prepared; rank order documented.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIG_SPEND_CLAUDE_REACT_VITE_VERIFICATION_REVIEW_001

**Proves:** Sig-spend Claude Lane K. Lane-F BLOCKED_NO_SPEND; no transcript claimed without execution.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIG_SPEND_CLAUDE_ROLLBACK_RECORD_REVIEW_001

**Proves:** Sig-spend Claude Lane J. Rollback plan documented in packet; not exercised (no spend).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIG_SPEND_CLAUDE_SCORE_MOVEMENT_EVIDENCE_REVIEW_001

**Proves:** Sig-spend Claude Lane P. Lane-I no score movement; scores unchanged.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIG_SPEND_CLAUDE_SIGNATURE_IMPORT_VALIDITY_REVIEW_001

**Proves:** Sig-spend Claude Lane D. Lane-C verdict BLOCKED_MISSING_MATERIAL; 4 inbox dirs empty; exact required fields enumerated; no fake signature.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIG_SPEND_CLAUDE_SIGNED_QUEUE_MUTATION_REVIEW_001

**Proves:** Sig-spend Claude Lane E. Queue before=0 after=0; no admission row added.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIG_SPEND_CLAUDE_SIGNED_SPEND_AUDIT_REVIEW_001

**Proves:** Sig-spend Claude Lane M. Lane-G audit confirms no spend; boundary matrix consistent.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIG_SPEND_CLAUDE_SPEND_ELIGIBILITY_GATE_REVIEW_001

**Proves:** Sig-spend Claude Lane F. Lane-D INELIGIBLE_BLOCKED; gate refused authorization.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIG_SPEND_CLAUDE_SPEND_OCCURRED_REVIEW_001

**Proves:** Sig-spend Claude Lane G. Lane-E NO_SPEND_BLOCKED; no execution performed.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIG_SPEND_CLAUDE_SYNTHESIS_REVIEW_001

**Proves:** Sig-spend Claude Lane Z. Synthesis + 34-item final report. Acceptable blocked case verified.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIG_SPEND_CLAUDE_TIER1_STATUS_REVIEW_001

**Proves:** Sig-spend Claude Lane L. Tier-1 coverage unchanged; react_vite still typed-blocked.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SIG_SPEND_CLAUDE_TIMER_PROTOCOL_REVIEW_001

**Proves:** Sig-spend Claude Lane A. Timer protocol applied; 6 rechecks; deadline 60 min.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SPLASH_TARGET_REQUIREMENTS_PACKET_LOCK_001

**Proves:** Convert the selected Python CLI/file-data Idea Lab splash target into an exact implementation requirements packet without implementing it.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_STATUS_PROOF_CENTER_EVIDENCE_VIEW_WORKFLOW_EXECUTION_LOCK_001

**Proves:** Execute the first selected user-visible proof center evidence-view workflow as a bounded rendered report path.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_STATUS_PROOF_CENTER_REPORT_WORKFLOW_CELL_CERTIFICATION_LOCK_001

**Proves:** Certify exact status_proof_center_report_workflow_cell if Proof Center report evidence and exact operator approval pass.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_STATUS_PROOF_CENTER_REPORT_WORKFLOW_CELL_OPERATOR_APPROVAL_LOCK_001

**Proves:** Record exact-cell operator approval for status_proof_center_report_workflow_cell certification.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_STATUS_RUNTIME_CLOSURE_BATCH_003_LOCK

**Proves:** Advance status runtime closure with focused execution, bottleneck inventory, and terminal anti-god guard preservation.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_STATUS_SCRIPTS_EVIDENCE_VALIDATION_CELL_CERTIFICATION_LOCK_001

**Proves:** Certify status_scripts_evidence_validation_cell as the second exact release-supported cell if prerequisite gates pass.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_STATUS_SCRIPTS_EVIDENCE_VALIDATION_CELL_OPERATOR_APPROVAL_LOCK_001

**Proves:** Record exact operator approval for status_scripts_evidence_validation_cell only before second-cell certification.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_STATUS_SUITE_RUNTIME_SEGMENTATION_AND_MONOLITHIC_CLOSURE_LOCK_001

**Proves:** Record a real segmented status-suite runtime path while preserving the monolithic full-suite blocker.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_STFS_CLAUDE_APPEND_ONLY_COUNT_DRIFT_GUARDS_REVIEW_001

**Proves:** STFS Claude Lane AD. Append-only and count-drift guards hold.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_STFS_CLAUDE_BETA_DASHBOARD_NOT_PUBLISHED_REVIEW_001

**Proves:** STFS Claude Lane V. Beta dashboard did not publish.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_STFS_CLAUDE_CAPABILITY_PROMOTION_EVIDENCE_BOUND_REVIEW_001

**Proves:** STFS Claude Lane P. Capability promotions evidence-bound.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_STFS_CLAUDE_CLAIM_SCANNER_DAY1_OVERCLAIM_REVIEW_001

**Proves:** STFS Claude Lane AE. Claim scanner and Day-1 overclaim scanner pass.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_STFS_CLAUDE_CLEAN_HOST_NOT_EXECUTED_REVIEW_001

**Proves:** STFS Claude Lane S. Clean-host did not execute.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_STFS_CLAUDE_DIRTY_UNTRACKED_STATE_REVIEW_001

**Proves:** STFS Claude Lane AF. Dirty/untracked state reported.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_STFS_CLAUDE_EVERY_NONLV_NEXT_ACTION_REVIEW_001

**Proves:** STFS Claude Lane H. Every non-LV family has active next action.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_STFS_CLAUDE_EVIDENCE_INDEX_CLEAN_REVIEW_001

**Proves:** STFS Claude Lane AC. Evidence index clean (1580 entries).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_STFS_CLAUDE_EXACT_LOCAL_NOT_FAMILY_SUPPORT_REVIEW_001

**Proves:** STFS Claude Lane Q. Exact local capability NOT framed as family support.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_STFS_CLAUDE_FAMILY_EXEC_TRANSCRIPTS_REVIEW_001

**Proves:** STFS Claude Lane J. Family execution transcripts exist.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_STFS_CLAUDE_FAMILY_MAP_COVERAGE_REVIEW_001

**Proves:** STFS Claude Lane G. Family map still covers all 31 families.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_STFS_CLAUDE_FAMILY_REPAIR_SCOPE_REVIEW_001

**Proves:** STFS Claude Lane L. Family repairs, if any, touched only Determinex-owned structure (0 done this wave).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_STFS_CLAUDE_FORBIDDEN_ACTIONS_AVOIDED_REVIEW_001

**Proves:** STFS Claude Lane AG. 16 forbidden actions avoided.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_STFS_CLAUDE_FULL_STATUS_TIMEOUT_REVIEW_001

**Proves:** STFS Claude Lane AB. Full-status timeout work did not disable/skip/delete tests.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_STFS_CLAUDE_GUI_BUILD_NOT_EXECUTED_REVIEW_001

**Proves:** STFS Claude Lane T. GUI/build did not execute.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_STFS_CLAUDE_INSTALLER_RELEASE_NOT_EXECUTED_REVIEW_001

**Proves:** STFS Claude Lane U. Installer/release did not execute.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_STFS_CLAUDE_MARCH_PLAN_DASHBOARD_REVIEW_001

**Proves:** STFS Claude Lane AA. March-plan dashboard accurate and not release hype.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_STFS_CLAUDE_NO_FAKE_SBOM_OUTPUT_REVIEW_001

**Proves:** STFS Claude Lane B. No fake SBOM output created (output null/null).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_STFS_CLAUDE_NO_LOCKFILE_MUTATION_REVIEW_001

**Proves:** STFS Claude Lane O. Package/lockfiles not mutated without spend.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_STFS_CLAUDE_NO_TEST_MUTATION_REVIEW_001

**Proves:** STFS Claude Lane M. Tests not edited to hide failures.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_STFS_CLAUDE_NO_UNAUTHORIZED_INSTALL_REVIEW_001

**Proves:** STFS Claude Lane D. No unauthorized install occurred.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_STFS_CLAUDE_NO_UNIVERSAL_SUPPORT_CLAIM_REVIEW_001

**Proves:** STFS Claude Lane R. Universal support not claimed.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_STFS_CLAUDE_NO_VERIFIER_ORACLE_MUTATION_REVIEW_001

**Proves:** STFS Claude Lane N. Verifiers/oracles/compilers/binaries not weakened.

**Does not prove:** Does not prove broad real-world repair coverage beyond the locked acceptance tests.

#### DETERMINEX_STFS_CLAUDE_PRIOR_SBOM_BLOCKER_REVALIDATED_REVIEW_001

**Proves:** STFS Claude Lane A. Prior SBOM missing-tool blocker revalidated.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_STFS_CLAUDE_RELEASE_CELLS_CANONICAL_REVIEW_001

**Proves:** STFS Claude Lane X. Release-supported exact cells canonical (10).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_STFS_CLAUDE_RELEASE_FAMILIES_CANONICAL_REVIEW_001

**Proves:** STFS Claude Lane Y. Release-supported families canonical (0).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_STFS_CLAUDE_RUNTIME_QUEUE_SPEND_ACCURATE_REVIEW_001

**Proves:** STFS Claude Lane W. Runtime queue/spend before/after accurate (2→2).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_STFS_CLAUDE_SAFE_FAMILY_EXEC_REVIEW_001

**Proves:** STFS Claude Lane I. Safe family execution did not require unauthorized installs/authority.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_STFS_CLAUDE_SBOM_EXECUTION_RETRY_SCOPE_REVIEW_001

**Proves:** STFS Claude Lane E. SBOM execution retry, if any, matched scope.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_STFS_CLAUDE_SBOM_OUTPUT_BLOCKER_REVIEW_001

**Proves:** STFS Claude Lane F. SBOM output exists+hashed OR honest blocker captured.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_STFS_CLAUDE_SBOM_TOOL_ADMISSION_PACKET_SPEND_REVIEW_001

**Proves:** STFS Claude Lane C. SBOM tool admission used valid packet/spend or none required.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_STFS_CLAUDE_SCORE_MOVEMENT_EVIDENCE_BOUND_REVIEW_001

**Proves:** STFS Claude Lane Z. Score movement evidence-bound.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_STFS_CLAUDE_SYNTHESIS_REVIEW_001

**Proves:** STFS Claude Lane AH. Synthesis + 66-item final report.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_STFS_CLAUDE_VERIFIER_NOT_FAKE_REVIEW_001

**Proves:** STFS Claude Lane K. Verifier implementations are not fake always-pass gates.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SUBPACKAGE_DISTRIBUTION_FEASIBILITY_CLAUDE_REVIEW_001

**Proves:** Gulp Wave 005 Claude Lane S. 7 subpackage candidates per-feature scored. Top 3: determinex-cli (PyPI), determinex-cloak (npm), determinex-proof-report (PyPI). 2-3 week path to first user touch.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SUBPACKAGE_DRY_RUN_DISTRIBUTION_PATH_CLAUDE_REVIEW_001

**Proves:** Wave 007 Claude Lane D. determinex-cli, determinex-cloak, determinex-proof-report — local package dry-run, metadata, license/security inheritance, publication blockers, install-moment credibility, wording risks.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SUBPACKAGE_FIRST_COMMAND_VIA_INSTALLED_ENTRY_POINT_LOCK_001

**Proves:** DETERMINEX_SUBPACKAGE_FIRST_COMMAND_VIA_INSTALLED_ENTRY_POINT_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SUBPACKAGE_PIP_BUILD_INSTALL_DEPRECATION_FIX_LOCK_001

**Proves:** DETERMINEX_SUBPACKAGE_PIP_BUILD_INSTALL_DEPRECATION_FIX_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SUPPORT_CELL_PROMOTION_GATE_LOCK_001

**Proves:** Lock promotion rules so support cells cannot be upgraded above available evidence.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SUPPORT_LADDER_RUNG_ORDER_ENFORCEMENT_LOCK_001

**Proves:** DETERMINEX_SUPPORT_LADDER_RUNG_ORDER_ENFORCEMENT_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SUPPORT_MATRIX_BOUNDARY_DRIFT_GUARD_LOCK_001

**Proves:** DETERMINEX_SUPPORT_MATRIX_BOUNDARY_DRIFT_GUARD_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SUPPORT_MATRIX_CONVEYOR_LOCK_001

**Proves:** Define the repeatable support-cell promotion machine that moves Determinex from universal intake/routing toward proof-backed utility across families, languages, tools, programs, frameworks, systems, and edge cases.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SUPPORT_MATRIX_VIEWER_44_FAMILY_BOUNDARY_CLAUDE_REVIEW_001

**Proves:** Overnight Lane 13. SupportMatrixViewer + 44-family boundary. Panel missing; 10/10 requirements unmet.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SUPPORT_MATRIX_VIEWER_BOUNDARY_CLAUDE_REVIEW_001

**Proves:** Wave 007 Claude Lane V. 44-family rendering, exact-cell rendering, release-supported families = 0 invariant, unsupported/candidate/blocked statuses, inference of '44-family support', phrase gate coverage.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SUPPORT_MATRIX_VIEWER_PANEL_AND_44_FAMILY_BOUNDARY_LOCK_001

**Proves:** DETERMINEX_SUPPORT_MATRIX_VIEWER_PANEL_AND_44_FAMILY_BOUNDARY_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SUPPORT_MATRIX_VIEWER_VISUAL_COMPONENT_PROOF_LOCK_001

**Proves:** DETERMINEX_SUPPORT_MATRIX_VIEWER_VISUAL_COMPONENT_PROOF_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SUPPORT_MATRIX_ZERO_FAMILY_BADGE_AND_44_LANGUAGE_GATE_LOCK_001

**Proves:** DETERMINEX_SUPPORT_MATRIX_ZERO_FAMILY_BADGE_AND_44_LANGUAGE_GATE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SWIFT_TOOLCHAIN_PLATFORM_GATE_LOCK_001

**Proves:** Swift Toolchain Platform Gate

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SYFT_ADMISSION_AND_SBOM_COVERAGE_AFTER_SIGNATURE_LOCK_001

**Proves:** DETERMINEX_SYFT_ADMISSION_AND_SBOM_COVERAGE_AFTER_SIGNATURE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SYFT_SBOM_EMISSION_IF_SIGNED_LOCK_001

**Proves:** DETERMINEX_SYFT_SBOM_EMISSION_IF_SIGNED_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SYFT_SBOM_EMISSION_WITH_RUNTIME_APPROVAL_LOCK_001

**Proves:** DETERMINEX_SYFT_SBOM_EMISSION_WITH_RUNTIME_APPROVAL_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SYFT_SBOM_SIGNED_ADMISSION_AND_STANDARDS_SBOM_GENERATION_LOCK_001

**Proves:** DETERMINEX_SYFT_SBOM_SIGNED_ADMISSION_AND_STANDARDS_SBOM_GENERATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SYFT_SIGNED_ADMISSION_AND_SBOM_EMISSION_LOCK_002

**Proves:** DETERMINEX_SYFT_SIGNED_ADMISSION_AND_SBOM_EMISSION_LOCK_002

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_SYFT_SIGNED_SBOM_EMISSION_LOCK_003

**Proves:** DETERMINEX_SYFT_SIGNED_SBOM_EMISSION_LOCK_003

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_LOCK_001

**Proves:** Reconcile global evidence spine after Claude read-only Universal 100 matrix probe binding.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_LOCK_002

**Proves:** Reconcile Claude Universal 100 visual binding evidence and classify new Codex status subprocess sites without loosening policy.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_LOCK_003

**Proves:** Reconcile Claude Batch 003 Universal 100 visual binding evidence into the append-only evidence spine.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_LOCK_004

**Proves:** Reconcile Claude Batch 004 Universal 100 visual binding evidence into the append-only evidence spine.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_LOCK_005

**Proves:** Reconcile Claude Universal 100 sector ladder and Batch 005/006 visual binding evidence into the append-only evidence spine.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_LOCK_006

**Proves:** Reconcile Claude support-depth and all-sector taxonomy visual binding evidence into the append-only evidence spine.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_LOCK_007

**Proves:** Reconcile Claude full sector wave visual binding evidence into the append-only evidence spine.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_LOCK_008

**Proves:** Reconcile Claude campaign and Batch 011-013 visual binding evidence into the append-only evidence spine.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_LOCK_009

**Proves:** Reconcile Claude Wave 10 visual binding evidence into the append-only evidence spine.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_TANDEM_POST_CLAUDE_BINDING_RECONCILIATION_LOCK_010

**Proves:** Reconcile Claude Wave 11 read-only depth-promotion visual binding evidence into the append-only evidence spine.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_TANDEM_POST_CLAUDE_PUBLIC_PROOF_REPORT_BINDING_RECONCILIATION_LOCK_011

**Proves:** Reconcile Claude Wave 12 public proof/report read-only bindings into the Codex evidence spine and repair stale count/doc expectations.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_TANDEM_STATUS_CHANNEL_LOCK_001

**Proves:** codex claude tandem status channel

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_TAURI_DESKTOP_BUILD_PROOF_LOCK_001

**Proves:** Attempt and record a bounded Tauri release build proof without installer, network fetch, or release claim.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_TAURI_DESKTOP_BUILD_PROOF_RETRY_WITH_LOCAL_ORT_LINK_LOCK_001

**Proves:** Prove a local no-bundle Tauri release build with ORT_LIB_LOCATION pointed at the generated local ONNX Runtime import library.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_TAURI_DESKTOP_BUILD_PROOF_WAVE_008_LOCK_001

**Proves:** DETERMINEX_TAURI_DESKTOP_BUILD_PROOF_WAVE_008_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_TAURI_DESKTOP_RELEASE_BUILD_ARTIFACT_LOCK_001

**Proves:** DETERMINEX_TAURI_DESKTOP_RELEASE_BUILD_ARTIFACT_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_TAURI_DRIVER_GUI_E2E_HARNESS_IMPLEMENTATION_LOCK_001

**Proves:** Attempt bounded tauri-driver desktop GUI harness implementation without faking GUI e2e.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_TAURI_DRIVER_GUI_HARNESS_INSTALL_AND_ADMISSION_LOCK_001

**Proves:** Install or admit the authorized tauri-driver GUI harness dependency without claiming GUI e2e proof.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_TAURI_ELECTRON_AUTHORITY_GATE_LOCK_001

**Proves:** Tauri/Electron Authority Gate

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_TAURI_NSIS_FALLBACK_PACKAGING_PROOF_LOCK_001

**Proves:** Attempt a bounded Tauri NSIS fallback packaging proof without dependency install or WiX release claim.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_TAURI_RELEASE_BUILD_FAILURE_REPAIR_PLAN_LOCK_001

**Proves:** Classify Tauri release build failure and choose exact repair route.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_TAURI_RELEASE_BUILD_PROOF_LOCK_001

**Proves:** Attempt actual project-local Tauri release build proof with bounded offline guards.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_TAURI_UNIFIED_PRODUCT_COMMAND_SURFACE_LOCK_001

**Proves:** Rung 1 of DETERMINEX_LIVE_REACT_UNIFIED_PRODUCT_SHELL_SERIES.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_TEST_SMOKE_INSTALL_VERIFIER_CLASS_EXPANSION_LOCK_001

**Proves:** DETERMINEX_TEST_SMOKE_INSTALL_VERIFIER_CLASS_EXPANSION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_TIER1_ADAPTER_EXPANSION_BATCH_002_LOCK_001

**Proves:** DETERMINEX_TIER1_ADAPTER_EXPANSION_BATCH_002_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_TIER1_ADAPTER_EXPANSION_BATCH_002_PER_FAMILY_VERIFIED_PROMOTION_LOCK_001

**Proves:** DETERMINEX_TIER1_ADAPTER_EXPANSION_BATCH_002_PER_FAMILY_VERIFIED_PROMOTION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_TIER1_FIFTH_FAMILY_ADAPTER_VERIFIED_TRANSCRIPT_LOCK_001

**Proves:** DETERMINEX_TIER1_FIFTH_FAMILY_ADAPTER_VERIFIED_TRANSCRIPT_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_TIER1_FIRST_FAMILY_BUILD_TEST_SMOKE_TRANSCRIPT_LOCK_001

**Proves:** Tier-1 First Family Transcript

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_TIER1_FOUR_VERIFIED_FAMILIES_ADAPTER_PORT_LOCK_001

**Proves:** DETERMINEX_TIER1_FOUR_VERIFIED_FAMILIES_ADAPTER_PORT_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_TIER1_PROGRAM_FAMILY_COVERAGE_COMPLETION_LOCK_001

**Proves:** DETERMINEX_TIER1_PROGRAM_FAMILY_COVERAGE_COMPLETION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_TIER1_SAFE_FIXTURE_EXECUTION_EXPANSION_LOCK_001

**Proves:** Tier-1 Safe Fixture Execution Expansion

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_TIER1_SECOND_THIRD_FAMILY_TRANSCRIPTS_LOCK_001

**Proves:** Tier-1 Second and Third Family Build/Test/Smoke Transcripts

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_TOOLCHAIN_AUTHORITY_FAMILY_PACKET_PREP_LOCK_001

**Proves:** DETERMINEX_TOOLCHAIN_AUTHORITY_FAMILY_PACKET_PREP_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_TOOLCHAIN_BATCH_EXECUTION_LOCK_001

**Proves:** DETERMINEX_TOOLCHAIN_BATCH_EXECUTION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_TOOLCHAIN_CLASSIFIER_STATE_EXPANSION_LOCK_001

**Proves:** Toolchain Classifier State Expansion

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_TOOLCHAIN_DETECTOR_AND_BUILD_COMMAND_SATURATION_LOCK_001

**Proves:** DETERMINEX_TOOLCHAIN_DETECTOR_AND_BUILD_COMMAND_SATURATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_TOOL_ACQUISITION_EXECUTION_LOCK_001

**Proves:** DETERMINEX_TOOL_ACQUISITION_EXECUTION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_TOOL_ACQUISITION_QUEUE_ADMISSION_SPEND_LOCK_001

**Proves:** DETERMINEX_TOOL_ACQUISITION_QUEUE_ADMISSION_SPEND_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_TRAINING_ROWS_FORBIDDEN_BOUNDARY_GUARD_LOCK_001

**Proves:** Training Rows Forbidden Boundary Guard

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_TRUE_100_DEFICIENCY_DECOMPOSITION_AUDIT_001

**Proves:** Decompose the 42.35 % true-100 intrinsic IDE readiness score into a blocker -> lock map, score-dimension decomposition, parallel lane plan, score-band plan, and forbidden-work list. Codex remains the source-truth lane; Claude remains the audit/planning/read-only-binding lane.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_TRUE_100_PERCENT_INTRINSIC_IDE_GAP_AUDIT_001

**Proves:** Truth audit of how close Determinex is to the full intrinsic IDE vision. Reports weighted dimension scores, blockers, and the next-lock roadmap. Grants no authority, promotes no support cell, marks no family release-supported, does not change training eligibility, and does not claim universal support.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_TRUE_USER_PRODUCT_CAPABILITY_BASELINE_LOCK_001

**Proves:** Freeze the truthful product baseline across all surfaces so public and internal text cannot overclaim beyond evidence-scoped support.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_TYPESCRIPT_NODE_CLI_ADAPTER_LOCK_001

**Proves:** Establish a no-network, fixture-local TypeScript Node CLI adapter using local tsc and scoped ambient Node globals.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_T_DRIVE_BUILD_CACHE_RELOCATION_POLICY_LOCK_001

**Proves:** T_DRIVE_RELOCATION_POLICY_RECORDED for DETERMINEX_CLEAN_RUNNER_SAFE_CLONE_BROADER_SBOM_T_DRIVE_RELOCATION_AND_DETECTOR_EXPANSION_WAVE_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_T_DRIVE_STORAGE_INVENTORY_LOCK_001

**Proves:** T Drive Storage Inventory

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_T_DRIVE_STORAGE_RELIEF_EXECUTION_LOCK_001

**Proves:** T Drive Storage Relief Execution

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_T_DRIVE_STORAGE_RELOCATION_PLAN_LOCK_001

**Proves:** T Drive Storage Relocation Plan

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNDER_THE_HOOD_SCORE_RECONCILIATION_LOCK_001

**Proves:** DETERMINEX_UNDER_THE_HOOD_SCORE_RECONCILIATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIFIED_CAPABILITY_GAP_GRAPH_LOCK_001

**Proves:** Turn the unified support matrix into a buildable gap graph with first public splash, existing-repo, maintenance, and learning path recommendations.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIFIED_PRODUCT_NAVIGATION_MODEL_LOCK_001

**Proves:** Rung 1 of DETERMINEX_UNIFIED_PRODUCT_UX_SHELL_SERIES.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIFIED_PRODUCT_SPLASH_DEMO_SPEC_LOCK_001

**Proves:** Rung 8 of DETERMINEX_UNIFIED_PRODUCT_UX_SHELL_SERIES.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIFIED_PRODUCT_SURFACE_TAXONOMY_LOCK_001

**Proves:** Define Determinex as a unified multi-surface software factory with Idea Lab, Repo Clinic, Maintenance Bay, Learning Studio, and Proof / Operator Center sharing one authority and evidence spine.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIFIED_PRODUCT_UX_FINAL_STATE_LOCK_001

**Proves:** Rung 9 (finale) of DETERMINEX_UNIFIED_PRODUCT_UX_SHELL_SERIES.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIFIED_SPLASH_SPRINT_DECISION_LOCK_001

**Proves:** Select first release-splash demo targets for all five surfaces without authorizing implementation, training, release, proof execution, ProgramBench execution, artifact import, or source mutation.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIFIED_STATUS_SURFACE_AND_EVIDENCE_GRAPH_LOCK_001

**Proves:** Create the first read-only unified Determinex status and evidence graph that consumes Claude and Codex lane evidence without mutating either lane.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIFIED_USER_LEVELS_AND_TEACHING_WINDOWS_LOCK_001

**Proves:** Rung 7 of DETERMINEX_UNIFIED_PRODUCT_UX_SHELL_SERIES.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_ALL_SECTOR_TAXONOMY_LOCK_001

**Proves:** Create broad Universal 100 sector taxonomy for classification/routing without support overclaim.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_CLAUDE_BINDING_HANDOFF_LOCK_001

**Proves:** universal 100 claude binding handoff

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_CONVEYOR_BACKLOG_AND_DEPTH_QUEUE_LOCK_001

**Proves:** Queue Universal 100 sector gulps, depth promotions, verifier/fixture work, packaging/fresh-install work, Claude bindings, and safe Codex parallel work without promoting support.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_DEPTH_PROMOTION_BATCH_017_LOCK_001

**Proves:** universal 100 depth promotion batch 017

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_DEPTH_PROMOTION_BATCH_018_LOCK_001

**Proves:** universal 100 depth promotion batch 018

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_DEPTH_PROMOTION_BATCH_019_LOCK_001

**Proves:** universal 100 depth promotion batch 019

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_DEPTH_PROMOTION_CANDIDATE_INVENTORY_LOCK_001

**Proves:** universal 100 depth promotion candidate inventory

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_DEPTH_PROMOTION_SCOREBOARD_LOCK_001

**Proves:** universal 100 depth promotion scoreboard

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_DEPTH_PROMOTION_WAVE_001_LOCK_001

**Proves:** universal 100 depth promotion wave 001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_EDGE_CASE_EXPANSION_ROADMAP_LOCK_001

**Proves:** Define universal edge-case intake, routing, missing-rung, fixture admission, and promotion discipline without claiming universal support.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_MATRIX_PROBE_BATCH_001_RECONCILIATION_LOCK_001

**Proves:** universal 100 matrix probe batch 001 reconciliation

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_MATRIX_PROBE_EXECUTION_BATCH_001

**Proves:** Run the first bounded executable Universal 100 matrix probe batch over fixture-only cells and promote only cells with local verifier/smoke evidence.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_MATRIX_PROBE_EXECUTION_BATCH_002

**Proves:** universal 100 matrix probe execution batch 002

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_MATRIX_PROBE_EXECUTION_BATCH_003

**Proves:** Run the third bounded executable Universal 100 matrix probe batch over adjacent fixture-local support cells.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_MATRIX_PROBE_EXECUTION_BATCH_004

**Proves:** Run the fourth bounded executable Universal 100 matrix probe batch over TypeScript, JavaScript, Vite, React/Vite, and static HTML fixture-local cells.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_SECTOR_CONVEYOR_ENGINE_LOCK_001

**Proves:** Manage Universal 100 sector gulp backlog, Claude binding queue, Codex next gulp queue, and no-overclaim conveyor rules.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_SECTOR_GULP_BATCH_005_LOCK_001

**Proves:** Gulp CLI/file-data and Node/TypeScript CLI sectors through fixture-local tagging, classification, routing, and build/test/smoke probes.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_SECTOR_GULP_BATCH_006_LOCK_001

**Proves:** Gulp React/Vite static app, static web, and Python FastAPI local API sectors through fixture-local build/test/smoke probes.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_SECTOR_GULP_BATCH_007_LOCK_001

**Proves:** Gulp Rust utility, Go utility, and maintenance/repair sectors with fixture-local build/test/smoke evidence.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_SECTOR_GULP_BATCH_008_LOCK_001

**Proves:** Run fixture-local Universal 100 sector gulp Batch 008.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_SECTOR_GULP_BATCH_009_LOCK_001

**Proves:** Run fixture-local Universal 100 sector gulp Batch 009.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_SECTOR_GULP_BATCH_010_LOCK_001

**Proves:** Run fixture-local Universal 100 sector gulp Batch 010.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_SECTOR_GULP_BATCH_011_LOCK_001

**Proves:** Run Universal 100 sector gulp batch 011 breadth probes with fixture-local evidence and exact blockers.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_SECTOR_GULP_BATCH_012_LOCK_001

**Proves:** Run Universal 100 sector gulp batch 012 breadth probes with fixture-local evidence and exact blockers.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_SECTOR_GULP_BATCH_013_LOCK_001

**Proves:** Run Universal 100 sector gulp batch 013 breadth probes with fixture-local evidence and exact blockers.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_SECTOR_STATE_AND_INGESTION_LADDER_LOCK_001

**Proves:** Define Universal 100 sector lifecycle states, blocker states, promotion rules, and sector registry without broadening claims.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_SUPPORT_DEPTH_LEDGER_LOCK_001

**Proves:** Create a derived support-depth ledger that prevents support inflation across Universal 100 cells.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_002_LOCK_001

**Proves:** universal 100 support map delta batch 002

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_003_LOCK_001

**Proves:** Append Batch 003 evidence-backed support-cell promotions as a claim-safe support-map delta.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_004_LOCK_001

**Proves:** Record the support-map delta created by Universal 100 matrix probe execution Batch 004.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_005_LOCK_001

**Proves:** Record the support map delta created by Universal 100 sector gulp Batch 005.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_006_LOCK_001

**Proves:** Record the support map delta created by Universal 100 sector gulp Batch 006.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_007_LOCK_001

**Proves:** Record evidence-backed support map delta from Universal 100 sector gulp Batch 007.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_008_LOCK_001

**Proves:** Emit Universal 100 support-map delta for sector gulp Batch 008.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_009_LOCK_001

**Proves:** Emit Universal 100 support-map delta for sector gulp Batch 009.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_010_LOCK_001

**Proves:** Emit Universal 100 support-map delta for sector gulp Batch 010.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_011_LOCK_001

**Proves:** Emit Universal 100 support map delta for sector gulp batch 011.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_012_LOCK_001

**Proves:** Emit Universal 100 support map delta for sector gulp batch 012.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_013_LOCK_001

**Proves:** Emit Universal 100 support map delta for sector gulp batch 013.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_014_LOCK_001

**Proves:** Emit support map delta for gap closure batch 014.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_015_LOCK_001

**Proves:** Emit support map delta for gap closure batch 015.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_016_LOCK_001

**Proves:** Emit support map delta for gap closure batch 016.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_017_LOCK_001

**Proves:** universal 100 support map delta batch 017

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_018_LOCK_001

**Proves:** universal 100 support map delta batch 018

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_DELTA_BATCH_019_LOCK_001

**Proves:** universal 100 support map delta batch 019

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_SUPPORT_MAP_LOCK_001

**Proves:** Aggregate support cells into the Universal 100 map: universal intake and routing, bounded verified execution, honest refusal.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_TOP_LEVEL_BLOCKER_INVENTORY_LOCK_001

**Proves:** universal 100 top-level blocker inventory

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_TOP_LEVEL_GAP_CLOSURE_BATCH_014_LOCK_001

**Proves:** Attempt safe top-level blocker gap closure batch 014.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_TOP_LEVEL_GAP_CLOSURE_BATCH_015_LOCK_001

**Proves:** Attempt safe top-level blocker gap closure batch 015.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_TOP_LEVEL_GAP_CLOSURE_BATCH_016_LOCK_001

**Proves:** Attempt safe top-level blocker gap closure batch 016.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_TOP_LEVEL_SECTOR_COMPLETION_CAMPAIGN_LOCK_001

**Proves:** Create the top-level Universal 100 sector completion scoreboard and execution plan without promoting support.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_TOP_LEVEL_SECTOR_COVERAGE_SCOREBOARD_LOCK_001

**Proves:** universal 100 top-level sector coverage scoreboard update

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_100_TOP_LEVEL_SECTOR_GAP_CLOSURE_WAVE_001_LOCK_001

**Proves:** universal 100 top-level sector gap closure wave 001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_DIGITAL_INFRASTRUCTURE_ACCOUNTING_CONVEYOR_001

**Proves:** DETERMINEX_UNIVERSAL_DIGITAL_INFRASTRUCTURE_ACCOUNTING_CONVEYOR_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_FAMILY_ACCOUNTING_STATUS_MAP_LOCK_001

**Proves:** DETERMINEX_UNIVERSAL_FAMILY_ACCOUNTING_STATUS_MAP_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNIVERSAL_PROGRAM_AUTHORITY_MATRIX_SCHEMA_LOCK_001

**Proves:** DETERMINEX_UNIVERSAL_PROGRAM_AUTHORITY_MATRIX_SCHEMA_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNKNOWN_NOVEL_FAMILY_HANDLER_LOCK_001

**Proves:** DETERMINEX_UNKNOWN_NOVEL_FAMILY_HANDLER_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNKNOWN_NOVEL_FIXTURE_EXECUTION_LOCK_001

**Proves:** DETERMINEX_UNKNOWN_NOVEL_FIXTURE_EXECUTION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNKNOWN_NOVEL_FIXTURE_PATH_LOCK_001

**Proves:** DETERMINEX_UNKNOWN_NOVEL_FIXTURE_PATH_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNKNOWN_NOVEL_RUNTIME_DETECTION_AND_INTAKE_LOCK_001

**Proves:** Unknown Novel Runtime Detection and Intake

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_UNKNOWN_NOVEL_RUNTIME_INTAKE_AND_UNIVERSAL_WORDING_GUARD_LOCK_002

**Proves:** Unknown / Novel Runtime Intake and Universal Wording Guard

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_USER_FACING_PROOF_REPORT_EXPORT_CELL_CERTIFICATION_LOCK_001

**Proves:** DETERMINEX_USER_FACING_PROOF_REPORT_EXPORT_CELL_CERTIFICATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_USER_FACING_RELEASE_CELL_RESERVATION_AND_CERTIFICATION_BATCH_LOCK_001

**Proves:** Reserve next release-cell slots for user-facing cells and certify exact passing user-facing cells only when evidence and exact operator approval are present.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_VERIFICATION_WITH_CAPABILITY_RULE_LOCK_001

**Proves:** DETERMINEX_VERIFICATION_WITH_CAPABILITY_RULE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_VERIFIER_FAKE_TRANSCRIPT_REJECTION_AND_PROMOTION_SIGNOFF_LOCK_001

**Proves:** Verifier Fake Transcript Rejection and Promotion Signoff

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_VERIFIER_ORACLE_MUTATION_BOUNDARY_GUARD_LOCK_001

**Proves:** Verifier/Oracle Mutation Boundary Guard

**Does not prove:** Does not prove broad real-world repair coverage beyond the locked acceptance tests.

#### DETERMINEX_VERIFIER_PORTFOLIO_COMPLETION_MAP_LOCK_001

**Proves:** DETERMINEX_VERIFIER_PORTFOLIO_COMPLETION_MAP_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_VERIFIER_PORTFOLIO_EXPANSION_LOCK_001

**Proves:** Build one non-authorizing verifier portfolio entry for every reconciled language/toolchain detector matrix entry, preserving all blocker counts and authority boundaries while preparing later fixture, toolchain, review, and gate-specific proof locks.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_VERIFIER_REJECTION_CORPUS_AND_SIGNOFF_BINDING_LOCK_001

**Proves:** Verifier Rejection Corpus and Signoff Binding

**Does not prove:** Does not prove corpus balance, training effectiveness, or public benchmark dominance by itself.

#### DETERMINEX_VERIFIER_REQUIRED_FAMILY_IMPLEMENTATION_LOCK_001

**Proves:** DETERMINEX_VERIFIER_REQUIRED_FAMILY_IMPLEMENTATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE008_CLAUDE_SYNTHESIS_AND_WAVE009_PRESSURE_QUEUE_001

**Proves:** Wave 008 Claude Lane Q2. Wave 008 synthesis. Rank top Codex deltas, packet-vs-execution gaps, full-system / trust / wow blockers, public claim risks. Generate Wave 009 Claude lanes + Codex pressure queue.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE008_CLOAK_CRYPTO_LEAK_CLAUDE_REVIEW_001

**Proves:** Wave 008 Claude Lane C2. CloakDemoPanel component_render_record landed; verify cryptographic obfuscate/restore proof, side-channel + NL leak review, raw-source export gate, cloud-boundary wording, subpackage boundary.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE008_DAY_ONE_CLAIM_SCANNER_CLAUDE_REVIEW_001

**Proves:** Wave 008 Claude Lane M2. Day-One claim scanner — forbidden + gated phrase scanners; safe-shock one-liner, technical/user/investor/media versions; release/open/beta readiness implication audit.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE008_HTML_PROOF_REPORT_INVESTOR_READINESS_CLAUDE_REVIEW_001

**Proves:** Wave 008 Claude Lane H2. Integrity stamp SHA256 landed; inline_script_tags=false noted; verify input-bundle hash, per-claim evidence links, full sanitization audit, disclaimer footer, release/authority boundary in HTML, versioning, print/PDF route, investor-summary paragraph, shareability.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE008_OMG_FIVE_FIELD_SCORE_CLAUDE_REVIEW_001

**Proves:** Wave 008 Claude Lane O2. Demo methodology reconciliation emitted packet=86 / proof_backed=86 / user_executable=27 / investor=55; verify public_reveal score present, quoting linter, unlock conditions, single-score overstatement remaining.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE008_OPERATOR_SIGNATURE_HARDENING_CLAUDE_REVIEW_001

**Proves:** Wave 008 Claude Lane X2. Operator signature mechanism hardening — module landed; verify mechanism can SAFELY unlock execution at real call sites.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE008_PACKAGE_DRY_RUN_DISTRIBUTION_CLAUDE_REVIEW_001

**Proves:** Wave 008 Claude Lane D2. compileall + module-invocation dry-runs PASSED for determinex-cli/cloak/proof-report; verify metadata, version policy, dependency list, namespace squat check, PyPI trusted publisher route, npm/crates provenance, wording risks.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE008_PROGRAMBENCH_WAL_MOAT_CLAUDE_REVIEW_001

**Proves:** Wave 008 Claude Lane P2. ProgramBench cockpit + Hive WAL panel wire landed; verify fixture binding, per-tool drill-down, per-attempt failed/repair/pass trace, proof-report integration, no SOTA claim.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE008_RAG_EXPORT_CELL5_CLAUDE_REVIEW_001

**Proves:** Wave 008 Claude Lane R2. CompanionRagReportPanel component_render_record landed; verify real user-facing export under signed run, citation file, sanitization, answer correctness boundary, product readiness false, Cell 5 classification.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE008_REAL_SIGNATURE_IMPORT_CLAUDE_REVIEW_001

**Proves:** Wave 008 Claude Lane Y2. Real signature import — sweep classified 6/6 'unsigned'; verify no execution path consumed bad approval state.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE008_SBOM_SIGNING_INSTALLER_TRUST_CLAUDE_REVIEW_001

**Proves:** Wave 008 Claude Lane S2. Syft admission still blocked unsigned; verify SBOM coverage, license/security route, code-signing decision, SmartScreen guidance, installer wording linter, MSI path status.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE008_SUPPORT_MATRIX_BOUNDARY_CLAUDE_REVIEW_001

**Proves:** Wave 008 Claude Lane V2. SupportMatrixViewerPanel renders_release_supported_families_zero=true landed; verify zero-family badge visible, 44-family tracking language, exact-cell rendering, candidate/blocked statuses, phrase gate CI, drift guard against canonical source.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE008_TAURI_FIRST_PAINT_GUI_VISUAL_CLAUDE_REVIEW_001

**Proves:** Wave 008 Claude Lane Z2. Tauri build / msedgedriver admission / first-paint screenshot / DOM evidence / orphan cleanup / first-paint vs meaningful flow distinction.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE009_CLAUDE_SYNTHESIS_AND_WAVE010_PRESSURE_QUEUE_001

**Proves:** Wave 009 Claude Lane Q3. Wave 009 synthesis. Rank executor-wiring gaps, packet-vs-execution gaps, full-system / trust / wow blockers, public claim risks. Generate Wave 010 Claude lanes + Codex pressure queue.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE009_CLOAK_HASH_CHAIN_LEAK_CLAUDE_REVIEW_001

**Proves:** Wave 009 Claude Lane C3. Hash chain input/obfuscated/restored, Python/Rust/TS coverage, side-channel review, NL leak review, raw-source export gate, cloud-boundary wording, panel/proof-report binding, privacy overclaim.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE009_DAY_ONE_CLAIM_SCANNER_CI_CLAUDE_REVIEW_001

**Proves:** Wave 009 Claude Lane M3. CI/status-test wiring, all forbidden + gated phrase groups, violation fixtures, safe-shock templates, no release/open/beta drift.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE009_EXECUTOR_VALIDATOR_WIRING_CLAUDE_REVIEW_001

**Proves:** Wave 009 Claude Lane X3. All executor sites — is validator called at runtime? Is unsigned/simulated/expired/revoked/malformed denied? Is denial logged? Any executor bypass remaining?

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE009_HTML_REPORT_SHAREABILITY_CLAUDE_REVIEW_001

**Proves:** Wave 009 Claude Lane H3. Embedded integrity stamp, input bundle hash, per-claim links, sanitization/XSS, disclaimer footer, authority/release boundary, versioning, print/PDF route, investor summary, shareability decision.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE009_OMG_FIVE_FIELD_SCORE_CLAUDE_REVIEW_001

**Proves:** Wave 009 Claude Lane O3. All five fields present, proof-backed not loosened, user-executable tied to actual execution, investor-demo honest, public-reveal present, quoting linter active, single-score overstatement impossible.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE009_PACKAGE_PUBLICATION_READINESS_CLAUDE_REVIEW_001

**Proves:** Wave 009 Claude Lane D3. determinex-cli / determinex-cloak / determinex-proof-report: metadata, deps, license/security inheritance, namespace squat, PyPI OIDC, npm provenance, crates provenance, version policy, wording risks.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE009_PROGRAMBENCH_WAL_DATABINDING_CLAUDE_REVIEW_001

**Proves:** Wave 009 Claude Lane P3. ProgramBench fixture binding implementation, per-tool drill-down, WAL failed/repair/pass trace, compiler oracle evidence, proof-report integration, no SOTA claim.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE009_RAG_SIGNED_EXPORT_CELL5_CLAUDE_REVIEW_001

**Proves:** Wave 009 Claude Lane R3. Signed-valid RAG export approval, actual RAG query/export if executed, citation report file, cockpit/panel/export binding, sanitization, answer-correctness boundary, product readiness false, Cell 5 classification.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE009_SBOM_SIGNING_INSTALLER_WORDING_CLAUDE_REVIEW_001

**Proves:** Wave 009 Claude Lane S3. Syft admission, SBOM coverage, license/security state, code-signing route, SmartScreen guidance, installer wording linter, MSI status, internal preview trust chain.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE009_SIGNED_QUEUE_AUDIT_IMPORT_CLAUDE_REVIEW_001

**Proves:** Wave 009 Claude Lane Y3. Signed-valid queue materialization, empty-queue correctness, invalid-queue rejection, audit-log append-only, real-signature import procedure, revocation, expiration, malformed handling.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE009_SUPPORT_MATRIX_DRIFT_PHRASE_CLAUDE_REVIEW_001

**Proves:** Wave 009 Claude Lane V3. Visible zero-family badge, exact-cell rollup, canonical-source drift guard, 44-language/family phrase gate, support-status legend, overinference risk.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE009_TAURI_BUILD_FIRST_PAINT_PATH_CLAUDE_REVIEW_001

**Proves:** Wave 009 Claude Lane Z3. Tauri target-dir remediation (T:\determinex-target Access is denied), release artifact, msedgedriver, GUI launch approval, first-paint evidence, orphan cleanup, overstatement check.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE010_CLAUDE_SYNTHESIS_AND_WAVE011_PRESSURE_QUEUE_001

**Proves:** Wave 010 Claude Lane Q4. Wave 010 synthesis. Rank top Codex deltas, runtime-spend blockers, first-install blockers, GUI blockers, trust blockers, wow blockers, public claim risks. Generate Wave 011 Claude + Codex queues.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE010_CLEAN_HOST_FRESH_INSTALL_CLAUDE_REVIEW_001

**Proves:** Wave 010 Claude Lane F4. Clean runner, Docker/runner assumptions, clean checkout, dependency probe, bootstrap, build/test/smoke, real vs planned.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE010_FIVE_FIELD_SCORE_CLAUDE_REVIEW_001

**Proves:** Wave 010 Claude Lane O4. Packet/proof-backed/user-executable/investor-demo/public-reveal scores; user_executable improvement from 27→29 audit; proof-backed still counts packets?; score linter held?

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE010_GUI_FIRST_PAINT_MOAT_VISUAL_CLAUDE_REVIEW_001

**Proves:** Wave 010 Claude Lane Z4. Driver admission, GUI launch approval, first-paint evidence, screenshot/DOM, orphan cleanup, ProgramBench/WAL/Cloak/RAG/SupportMatrix visual flow, overstatement check.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE010_LOCAL_INSTALL_MOMENT_CLAUDE_REVIEW_001

**Proves:** Wave 010 Claude Lane D4. determinex-cli/determinex-cloak/determinex-proof-report local build+install transcript, first useful command transcript, package boundaries, license/security inheritance, public wording risk, install moment vs dry-run.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE010_NSIS_INSTALLER_RUNTIME_CLAUDE_REVIEW_001

**Proves:** Wave 010 Claude Lane N4. Signed-valid NSIS approval, install/launch/uninstall transcripts, cleanup diff, public installer wording, SmartScreen/signing trust gaps.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE010_PROOF_REPORT_REVEAL_ASSET_CLAUDE_REVIEW_001

**Proves:** Wave 010 Claude Lane H4. Proof report sample, integrity stamp, per-claim links, boundary text, investor readability, public reveal preflight board, shareability overstatement check.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE010_PUBLIC_REVEAL_PREFLIGHT_CLAUDE_REVIEW_001

**Proves:** Wave 010 Claude Lane M4. Internal-only / private demo / investor demo candidate / public reveal candidate; gates still false; safe language; reveal language too-strong audit.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE010_RUNTIME_AUTHORITY_SPEND_CLAUDE_REVIEW_001

**Proves:** Wave 010 Claude Lane X4. Real signature import, signed-valid queue spent, executor-without-validator detection, denial logging, append-only audit log, simulated/unsigned approvals stayed blocked.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE010_SBOM_RUNTIME_TRUST_CLAUDE_REVIEW_001

**Proves:** Wave 010 Claude Lane S4. Signed-valid Syft approval, SBOM emission, SBOM coverage, license/security review, signing route, overstatement check.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE011_CLAUDE_SYNTHESIS_AND_WAVE012_PRESSURE_QUEUE_001

**Proves:** Wave 011 Claude Lane Q5. Wave 011 synthesis. Rank top Codex deltas, runtime-spend / first-install / GUI / trust / wow blockers, public claim risks. Generate Wave 012 Claude + Codex queues.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE011_CLEAN_RUNNER_FRESH_INSTALL_CLAUDE_REVIEW_001

**Proves:** Wave 011 Claude Lane F5. Runner type, clean checkout, dependency probe, bootstrap, build/test/smoke, clean-host vs local-simulation, missing assumptions.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE011_FIRST_ADMISSION_RUNTIME_SPEND_CLAUDE_REVIEW_001

**Proves:** Wave 011 Claude Lane X5. Real signatures imported / signed-valid queue / approval spent / admission count / denial count / audit log / validator usage / execution bypass. Verdict distinguishes 4 levels: queue-exists, queue-has-signed-records, approval-consumed, execution-happened.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE011_GUI_LAUNCH_FIRST_PAINT_CLAUDE_REVIEW_001

**Proves:** Wave 011 Claude Lane G5. GUI launch signature, msedgedriver signature, driver admission, app launch, first-paint screenshot/DOM/anchor, cleanup, GUI e2e overstatement.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE011_HTML_PROOF_REPORT_SHAREABILITY_CLAUDE_REVIEW_001

**Proves:** Wave 011 Claude Lane H5. Integrity stamp, input hash, per-claim links, disclaimer footer, schema version, investor summary, sanitization, PDF route, actually-shareable verdict.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE011_NSIS_INSTALL_SMOKE_CLAUDE_REVIEW_001

**Proves:** Wave 011 Claude Lane N5. NSIS signature, artifact hash, install/launch/uninstall transcripts, cleanup diff, public installer wording, trust gates.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE011_OMG_SCORE_DEFINITION_CLAUDE_REVIEW_001

**Proves:** Wave 011 Claude Lane O5. 5 score fields; definition-bound or definition-loosening; quoting linter prevents single-score claims.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE011_PUBLIC_REVEAL_TIER_CLAUDE_REVIEW_001

**Proves:** Wave 011 Claude Lane M5. internal-only / private demo / investor demo / public reveal / open availability; exact unlock conditions; phrase drift; safe language.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE011_SYFT_SBOM_CLAUDE_REVIEW_001

**Proves:** Wave 011 Claude Lane S5. Syft signature, tool admission, SBOM artifact, ecosystem coverage, license/security claims, trust-board update.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE011_TRUE_LOCAL_INSTALL_MOMENT_CLAUDE_REVIEW_001

**Proves:** Wave 011 Claude Lane D5. determinex-cli / determinex-proof-report / determinex-cloak: build transcript, local install transcript (pip install — not dry-run), first useful command transcript, cleanup transcript, dependency list, version policy, license/security inheritance, true install vs dry-run.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE012_BUILD_TEST_SMOKE_LADDER_CLAUDE_REVIEW_001

**Proves:** Wave 012 Claude Lane B6. Support-depth ladder. Rungs: detect / scaffold / build / test / smoke / package-install / clean-host / release-supported.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE012_CAPABILITY_UNIVERSE_MATRIX_CLAUDE_REVIEW_001

**Proves:** Wave 012 Claude Lane X6. Family / language / build / test / smoke / install / GUI / clean-host / SBOM coverage. Verdict distinguishes: listed / detected / scaffolded / built / tested / smoked / installed / clean-host-proven / release-supported.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE012_CLAUDE_SYNTHESIS_AND_WAVE013_PRESSURE_QUEUE_001

**Proves:** Wave 012 Claude Lane Q6. Wave 012 synthesis. Rank top Codex deltas, capability / install / toolchain / verifier / GUI / clean-host / SBOM / claim risk blockers. Generate Wave 013 Claude + Codex queues.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE012_CLEAN_HOST_ROUTE_CLAUDE_REVIEW_001

**Proves:** Wave 012 Claude Lane F6. Runner type, clean checkout, dependency probe, bootstrap, build/test/smoke transcript, local simulation vs clean host, exact assumptions, claim boundary. Reject clean-host based on local simulation.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE012_DRY_RUN_INFLATION_CLAUDE_REVIEW_001

**Proves:** Wave 012 Claude Lane D6. All local install statuses; dry-run wording; failed-dry-run treatment; PASSED labels; source-tree import leakage; installed-entry-point proof.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE012_EXACT_CELL_PROMOTION_CLAUDE_REVIEW_001

**Proves:** Wave 012 Claude Lane P6. Promoted cells; denied promotions; release-supported delta; family support claims; per-rung requirements; install/GUI/clean-host evidence where claimed. Reject family-level overclaiming.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE012_GUI_AUTOMATION_FIRST_PAINT_CLAUDE_REVIEW_001

**Proves:** Wave 012 Claude Lane G6. GUI approval, driver admission, launch transcript, screenshot/DOM/anchor, process cleanup, first-paint vs GUI e2e wording, cockpit visual proof, panel coverage. Reject GUI claims based only on built artifact.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE012_PROOF_REPORT_CAPABILITY_COVERAGE_CLAUDE_REVIEW_001

**Proves:** Wave 012 Claude Lane R6. Proof-report schema, per-capability coverage, per-claim evidence links, blocked/not-claimed examples, schema version, PDF/print route, sanitization, investor/public wording.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE012_REAL_LOCAL_INSTALL_MOMENT_CLAUDE_REVIEW_001

**Proves:** Wave 012 Claude Lane I6. determinex-cli / determinex-proof-report / determinex-cloak. Verdict per package: TRUE_INSTALL_PROVEN / BLOCKED_WITH_EXACT_RUNG / DRY_RUN_ONLY / SOURCE_TREE_ONLY / FAILED_MISLABELED.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE012_SBOM_LICENSE_SECURITY_TRUST_CLAUDE_REVIEW_001

**Proves:** Wave 012 Claude Lane S6. SBOM tool admission, SBOM artifact, license inventory, security scan, package metadata, installer trust, code-signing, release/public-installer wording. Reject SBOM/security/license claims based on plans or packets.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE012_SCORE_EVIDENCE_DELTA_CLAUDE_REVIEW_001

**Proves:** Wave 012 Claude Lane O6. Score changes, evidence deltas, predicate bindings, CI enforcement, quoting linter, single-score claim prevention. Reject score rises without matching evidence deltas.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE012_TOOLCHAIN_DETECTOR_BUILD_COMMAND_CLAUDE_REVIEW_001

**Proves:** Wave 012 Claude Lane T6. Detector matrix, manifest coverage, command mapping, installed/project-local/global-missing/network-gated distinctions, fixture coverage, blocker code precision. Detector vs build.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE012_VERIFIER_PORTFOLIO_CLAUDE_REVIEW_001

**Proves:** Wave 012 Claude Lane V6. Compiler / test / smoke / package-install / GUI-e2e / SBOM-license-security / proof-report / clean-host verifiers. Promotion block rules.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE013_CLAUDE_SYNTHESIS_AND_WAVE014_PRESSURE_QUEUE_001

**Proves:** Wave 013 Claude Lane Q7. Wave 013 synthesis. Distinguish real execution from docs/maps/packets. Rank top Codex deltas, runtime-spend / install / detector-toolchain / verifier / ladder-promotion / clean-host / GUI / SBOM-security-license / proof-report / score-claim risk blockers. Generate Wave 014 Claude + Codex queues.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE013_CLEAN_HOST_ROUTE_TRANSCRIPT_CLAUDE_REVIEW_001

**Proves:** Wave 013 Claude Lane F7. Runner decision, admission, clean checkout, dependency probe, bootstrap, build/test/smoke, local-simulation distinction, exact missing assumptions. Reject clean-host based on developer-host venv.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE013_DETECTOR_RUNTIME_PROBE_CLAUDE_REVIEW_001

**Proves:** Wave 013 Claude Lane T7. Detector implementation, fixture scanning, manifest discovery, project-family classification, generated detection records, runtime invocation in tests, docs-vs-runtime distinction, blocker codes.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE013_EXACT_CELL_PROMOTION_GATE_CLAUDE_REVIEW_001

**Proves:** Wave 013 Claude Lane P7. 10 existing release-supported cells; candidate cells; fixture / detector / build / test / smoke / proof-report / verifier signoff / install / GUI / clean-host evidence; family inference guard. Reject promotions without full ladder + verifier signoff.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE013_FOUR_STATE_TOOLCHAIN_CLASSIFIER_CLAUDE_REVIEW_001

**Proves:** Wave 013 Claude Lane C7. global installed / project-local / globally missing / network-gated / hardware-gated / unknown-blocked states; probe transcripts; classification consistency. Reject free-text blocker codes.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE013_GUI_VISUAL_PROOF_CLAUDE_REVIEW_001

**Proves:** Wave 013 Claude Lane G7. Signed GUI approval, driver approval, driver admission, launch transcript, screenshot, DOM/anchor, process metadata, cleanup, first-paint vs e2e wording, panel coverage. Reject GUI proof based only on built artifact.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE013_INSTALLED_ENTRY_POINT_AND_PIP_PATH_CLAUDE_REVIEW_001

**Proves:** Wave 013 Claude Lane D7. determinex-cli / determinex-cloak / determinex-proof-report: build path, install path, wheel/PEP517 vs setup.py, isolated env, outside-source-tree, PYTHONPATH leakage, installed script path, first useful command, cleanup, metadata. Per-package verdict.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE013_LADDER_RUNG_ENFORCEMENT_CLAUDE_REVIEW_001

**Proves:** Wave 013 Claude Lane B7. Rung order detected → scaffolded → built → tested → smoked → packaged/installed → clean-host → release-supported. Check inversion fixtures, corrected statuses, CI enforcement, exceptions.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE013_PACKAGE_METADATA_LICENSE_HYGIENE_CLAUDE_REVIEW_001

**Proves:** Wave 013 Claude Lane H7. determinex-cli / cloak / proof-report: names, versions, descriptions, entry points, deps, license files, README, namespace collision, PyPI/OIDC blockers, public upload boundaries.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE013_PER_FAMILY_COMMAND_MAPPING_CLAUDE_REVIEW_001

**Proves:** Wave 013 Claude Lane M7. manifest → family mapping; family → build/test/smoke route; command candidates; unsafe execution boundaries; fixture route tests. Reject conversion of command mapping into capability proof.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE013_PROOF_REPORT_CAPABILITY_COVERAGE_CLAUDE_REVIEW_001

**Proves:** Wave 013 Claude Lane R7. Per-capability coverage section, per-claim evidence anchors, blocked/not-claimed examples, schema version, sanitization, PDF/print route, investor/public wording, score evidence links.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE013_REAL_SIGNATURE_RUNTIME_SPEND_CLAUDE_REVIEW_001

**Proves:** Wave 013 Claude Lane X7. Real signature inventory, signed queue, validation, self-hash, execution_allowed events, denials, admissions, bypass. Verdict distinguishes: template exists / signed record exists / approval validated / approval spent / execution happened / admission happened.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE013_SBOM_LICENSE_SECURITY_TRUST_CLAUDE_REVIEW_001

**Proves:** Wave 013 Claude Lane S7. Syft approval, admission, SBOM artifact, ecosystem coverage, license inventory, security scan, package metadata, code-signing, public-installer wording. Reject SBOM/security/license claims based only on packets.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE013_SCORE_EVIDENCE_DELTA_CI_CLAUDE_REVIEW_001

**Proves:** Wave 013 Claude Lane O7. Score predicate map, evidence-delta schema, score recomputation, fake-rise fixtures, legitimate-rise fixtures, CI enforcement, quote/claim linter, single-number score prevention.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE013_UNKNOWN_NOVEL_FAMILY_HANDLER_CLAUDE_REVIEW_001

**Proves:** Wave 013 Claude Lane U7. Unknown project detection; unknown manifest routing; fixture admission; detector/parser/verifier admission; operator-facing explanation; universal-support wording guard.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE013_VERIFIER_CLASS_EXPANSION_CLAUDE_REVIEW_001

**Proves:** Wave 013 Claude Lane V7. test / smoke / package_install / compiler verifiers; proof records; verifier rejection of fake/missing transcripts; promotion gate binding. Reject verifier claims that are only enums or docs.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE014_CLASSIFIER_STATE_EXPANSION_CLAUDE_REVIEW_001

**Proves:** Wave 014 Claude Lane C8. INSTALLED_GLOBAL / INSTALLED_PROJECT_LOCAL / MISSING_GLOBAL / NETWORK_GATED / HARDWARE_GATED / UNKNOWN_BLOCKED states; per-tool transcripts; blocker enum; network/hardware-gated safety; consistency tests. Reject free-text or untested states.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE014_CLAUDE_SYNTHESIS_AND_WAVE015_PRESSURE_QUEUE_001

**Proves:** Wave 014 Claude Lane Q8. Wave 014 synthesis. Distinguish packets / specs / maps / probes / executions / admissions / promotions. Rank top Codex deltas, runtime-spend / local-install-promotion / detector-classifier / fixture-execution / verifier-promotion / clean-host / GUI / SBOM-security-license / package-metadata / proof-report / score-claim risk blockers. Generate Wave 015 Claude lanes + Codex pressure queue.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE014_CLEAN_HOST_RUNNER_TRANSCRIPT_CLAUDE_REVIEW_001

**Proves:** Wave 014 Claude Lane F8. runner route matrix; runner context schema; admitted clean runner status; local simulation distinction; clean checkout; dependency probe; bootstrap transcript; build/test/smoke transcript; missing assumptions; runner admission packet if blocked. Reject clean-host based on local simulation.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE014_DETECTOR_FIXTURE_CORPUS_CI_CLAUDE_REVIEW_001

**Proves:** Wave 014 Claude Lane T8. fixture corpus; detector runtime invocation; per-target detection records; manifest discovery; expected family/toolchain/route assertions; blocker enum; unknown/novel fixture; CI tests proving detector runs. Reject detector claims based on static matrix files alone.

**Does not prove:** Does not prove corpus balance, training effectiveness, or public benchmark dominance by itself.

#### DETERMINEX_WAVE014_FAKE_TRANSCRIPT_REJECTION_VERIFIER_SIGNOFF_CLAUDE_REVIEW_001

**Proves:** Wave 014 Claude Lane V8. verifier rejection of: missing/malformed transcript, dry-run-as-install, source-tree-command-as-entry-point, command-map-as-execution, local-simulation-as-clean-host, built-artifact-as-GUI-launch, SBOM-packet-as-SBOM. Verifier signoff schema; promotion gate binding; test coverage. Reject happy-path-only verifiers.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE014_FIRST_ADMISSION_RUNTIME_SPEND_CLAUDE_REVIEW_001

**Proves:** Wave 014 Claude Lane X8. real signature inventory; signed-valid queue; approval schema; self-hash; packet-/target-/command-scope hash binding; expiration/revocation; audit log; execution_allowed events; admissions; denials; whether execution bypassed approval. Verdict distinguishes: packet emitted / real signature present / signature validated / approval queued / approval spent / admission happened / execution happened.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE014_FIRST_SBOM_TOOL_ADMISSION_CLAUDE_REVIEW_001

**Proves:** Wave 014 Claude Lane S8. Syft/tool approval; approval spend; tool admission; tool version/hash/source; SBOM artifact; ecosystem coverage; trust board update; license/security boundary. Reject SBOM claims without emitted artifact.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE014_GUI_FIRST_VISUAL_PROOF_CLAUDE_REVIEW_001

**Proves:** Wave 014 Claude Lane G8. driver approval / GUI launch approval / approval spend / driver admission / Tauri artifact hash / GUI launch transcript / screenshot / DOM-anchor / process metadata / stdout-stderr / cleanup-orphan / first-paint vs GUI e2e wording. Reject GUI claims based on specs or built artifacts.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE014_LADDER_INVERSION_CI_CLAUDE_REVIEW_001

**Proves:** Wave 014 Claude Lane B8. rung inversion fixtures; CI failure on out-of-order ladder; release-supported prior-rung requirements; install-before-test/smoke handling; clean-host local-simulation rejection; GUI built-artifact rejection; current release-supported cells. Reject hidden rung inversions.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE014_LOCAL_INSTALL_EXACT_CELL_PROMOTION_CLAUDE_REVIEW_001

**Proves:** Wave 014 Claude Lane L8. determinex-cli / determinex-proof-report / determinex-cloak: fixture / detector / wheel-build / isolated install / installed entry-point / source-tree leakage / test verifier / smoke verifier / install verifier / proof-report anchor / package metadata / local-preview boundary / score evidence-delta / release-supported cell decision. Reject clean-host or family-support inference.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE014_PACKAGE_LICENSE_METADATA_BOUNDARY_CLAUDE_REVIEW_001

**Proves:** Wave 014 Claude Lane H8. determinex-cli / determinex-proof-report / determinex-cloak: names / versions / descriptions / entry points / dependencies / license files / README files / homepage-documentation metadata / namespace collision risk / PyPI-OIDC blockers / local-preview boundary / public upload boundary. Reject public-package or installability claims beyond local-preview proof.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE014_PER_FAMILY_FIXTURE_ROUTE_EXECUTION_CLAUDE_REVIEW_001

**Proves:** Wave 014 Claude Lane E8. detector → route resolver → verifier pipeline; selected safe fixtures; build/test/smoke transcripts; blocked-rung report; unsafe execution boundaries; whether command maps are counted as execution. Reject unsupported family execution claims.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE014_PROOF_REPORT_EVIDENCE_ANCHOR_CLAUDE_REVIEW_001

**Proves:** Wave 014 Claude Lane R8. per-capability coverage section; per-family status; per-claim evidence anchors; blocked/not-claimed examples; schema version; score evidence-delta links; sanitization status; PDF/print route; whether anchors point to actual evidence rather than narrative. Reject proof-report claims without hard evidence anchors.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE014_SCORE_DELTA_PUBLIC_CLAIM_LINTER_CLAUDE_REVIEW_001

**Proves:** Wave 014 Claude Lane O8. score-delta schema; fake-score-rise fixture; legitimate-score-rise fixture; score recomputation; single-number score quote prevention; forbidden phrase expansion; safe language examples; claim scanner CI. Reject score rises or public language not bound to evidence.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE014_UNKNOWN_NOVEL_RUNTIME_INTAKE_CLAUDE_REVIEW_001

**Proves:** Wave 014 Claude Lane U8. unknown fixture; detector transcript; intake routing record; operator explanation; fixture admission requirement; detector/parser/verifier requirement; universal-support wording guard. Reject unknown/novel support without fixture/verifier admission.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE015_CANONICAL_RELEASE_CELL_RECONCILIATION_CLAUDE_REVIEW_001

**Proves:** Wave 015 Claude Lane A9. Canonical release-supported cell count: read every authoritative source and reconcile the 10-vs-13 discrepancy. Verdict must be one canonical number with exact rationale.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE015_CANONICAL_RELEASE_CELL_RECONCILIATION_LOCK_001

**Proves:** Canonical Wave 014 Reconciliation: 10 vs 13 Cells

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE015_CLASSIFIER_STATE_SAFETY_CLAUDE_REVIEW_001

**Proves:** Wave 015 Claude Lane C9. INSTALLED_GLOBAL / INSTALLED_PROJECT_LOCAL / MISSING_GLOBAL / NETWORK_GATED / HARDWARE_GATED / UNKNOWN_BLOCKED; fixtures/mocks; per-tool transcripts; typed blocker enum; network/hardware safety; cross-state consistency.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE015_CLAUDE_SYNTHESIS_AND_WAVE016_PRESSURE_QUEUE_001

**Proves:** Wave 015 Claude Lane Q9. Wave 015 synthesis: canonical cell count + 10-vs-13 verdict + rank top Codex deltas + rank blockers across 11 categories + generate Wave 016 Claude + Codex queues.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE015_CLEAN_HOST_TRANSCRIPT_CLAUDE_REVIEW_001

**Proves:** Wave 015 Claude Lane F9. Runner route matrix; runner context schema; admitted clean runner status; local simulation distinction; clean checkout; dependency probe; bootstrap transcript; build/test/smoke transcript; missing assumptions; runner admission packet. Reject clean-host from local simulation.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE015_DETECTOR_FIXTURE_CI_CLAUDE_REVIEW_001

**Proves:** Wave 015 Claude Lane T9. Fixture expected JSON; detector runtime invocation; per-target records; manifest discovery; expected family/toolchain/route assertions; typed blocker enum; unknown fixture; CI tests proving detector runs. Reject detector claims from static matrix files alone.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE015_FIRST_ADMISSION_RUNTIME_SPEND_CLAUDE_REVIEW_001

**Proves:** Wave 015 Claude Lane X9. Real signature inventory; signed-valid queue; approval schema; self-hash; hash binding; command scope binding; expiration/revocation; audit log tamper guard; execution_allowed events; admissions; denials; bypass detection. Verdict distinguishes 7 levels.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE015_FIRST_SBOM_ARTIFACT_CLAUDE_REVIEW_001

**Proves:** Wave 015 Claude Lane S9. Syft approval, spend, admission, version/hash/source recording, SBOM artifact, ecosystem coverage, trust board update, license/security boundary. Reject SBOM claims without emitted artifact.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE015_GUI_FIRST_VISUAL_PROOF_CLAUDE_REVIEW_001

**Proves:** Wave 015 Claude Lane G9. Driver approval, GUI launch approval, approval spend, driver admission, Tauri artifact hash, GUI launch transcript, screenshot, DOM/anchor, process metadata, stdout/stderr, cleanup, first-paint vs e2e wording. Reject GUI proof from packet/spec/built artifact.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE015_LADDER_INVERSION_CI_BLOCKING_CLAUDE_REVIEW_001

**Proves:** Wave 015 Claude Lane B9. Rung inversion fixtures; CI failure on out-of-order ladder; release-supported prior-rung requirements; install-before-test/smoke handling; local-preview exception; clean-host local-simulation rejection; GUI built-artifact rejection.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE015_LOCAL_PREVIEW_FULL_GATE_PROMOTION_CLAUDE_REVIEW_001

**Proves:** Wave 015 Claude Lane L9. Per package (determinex-cli, determinex-proof-report, determinex-cloak): fixture / detector / wheel build / isolated install / installed entry-point / source-tree leakage / test+smoke+install verifier signoff / fake-transcript rejection coverage / proof-report anchor / local-preview boundary / metadata / score evidence-delta / release-supported cell status. Reject clean-host, public-package, or family-support inference.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE015_PACKAGE_METADATA_LICENSE_README_BOUNDARY_CLAUDE_REVIEW_001

**Proves:** Wave 015 Claude Lane H9. determinex-cli / determinex-proof-report / determinex-cloak: names / versions / descriptions / entry points / deps / LICENSE / README / homepage-docs / namespace collision / PyPI OIDC / local-preview boundary / public upload boundary.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE015_PER_FAMILY_SAFE_FIXTURE_EXECUTION_CLAUDE_REVIEW_001

**Proves:** Wave 015 Claude Lane E9. Detector → route resolver → verifier pipeline; selected safe fixtures; build/test/smoke transcripts; blocked-rung report; unsafe execution boundaries; whether command maps are counted as execution.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE015_PROOF_REPORT_CAPABILITY_ANCHORS_CLAUDE_REVIEW_001

**Proves:** Wave 015 Claude Lane R9. Per-capability coverage; per-family status; per-claim evidence anchors; blocked/not-claimed examples; schema version; score evidence-delta links; sanitization; PDF route; whether anchors point to actual evidence rather than narrative.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE015_SCORE_DELTA_PUBLIC_CLAIM_SCANNER_CLAUDE_REVIEW_001

**Proves:** Wave 015 Claude Lane O9. Score-delta schema; fake-rise fixture; legitimate-rise fixture; score recomputation; single-number quote prevention; forbidden phrase expansion; claim scanner CI; safe language examples.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE015_UNKNOWN_NOVEL_RUNTIME_INTAKE_CLAUDE_REVIEW_001

**Proves:** Wave 015 Claude Lane U9. Unknown fixture transcript; detector routing; intake routing record; operator explanation; fixture admission requirement; detector/parser/verifier requirement; universal-support wording guard.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE015_VERIFIER_REJECTION_SIGNOFF_BINDING_CLAUDE_REVIEW_001

**Proves:** Wave 015 Claude Lane V9. Rejection of: missing/malformed transcript, dry-run-as-install, source-tree-command-as-entry-point, command-map-as-execution, local-sim-as-clean-host, built-artifact-as-GUI-launch, SBOM-packet-as-SBOM. Signoff schema; promotion-gate binding; test coverage.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE016_CANONICAL_CELL_CONSTANT_CONVEYOR_BINDING_CLAUDE_REVIEW_001

**Proves:** Wave 016 Claude Lane A10. Canonical release-supported cell source; all consumers; conveyor binding; wave-common consumers; proof reports; reconciliation packets; status artifacts; historical/current labeling; family count invariant. Verdict: is there exactly one canonical current source; does every reader consume it; does conveyor fail on mismatch.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE016_CLAUDE_SYNTHESIS_AND_WAVE017_PRESSURE_QUEUE_001

**Proves:** Wave 016 Claude Lane Q10. Synthesis. Answer: canonical promotion authority fixed? 10 or 13 canonical? local-preview = release-supported? any hard execution floor crossed? Rank top Codex deltas + 7 blocker categories. Generate Wave 017 Claude + Codex queues.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE016_CLEAN_HOST_RUNNER_CLAUDE_REVIEW_001

**Proves:** Wave 016 Claude Lane F10. Runner approval/admission; runner context (ADMITTED_CLEAN_RUNNER / LOCAL_SIMULATION / BLOCKED); clean checkout; dependency probe; bootstrap; build/test/smoke transcript; package cell clean-host transcript if claimed. Reject clean-host claims from local simulation.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE016_DETECTOR_CLASSIFIER_FIXTURE_CI_CLAUDE_REVIEW_001

**Proves:** Wave 016 Claude Lane T10. Per-fixture expected JSON; detector CI invocation; per-target detection records; typed blocker enum; classifier state fixtures (PROJECT_LOCAL / NETWORK_GATED / HARDWARE_GATED / UNKNOWN_BLOCKED); network/hardware safety tests; unknown fixture route.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE016_FIRST_REAL_SIGNATURE_SPEND_CLAUDE_REVIEW_001

**Proves:** Wave 016 Claude Lane Y10. signed-valid queue; operator approval files; validation result; import result; spend result; execution_allowed event; admission/execution transcript; rollback/cleanup; audit chain. Verdict distinguishes 6 levels.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE016_FIRST_SBOM_ARTIFACT_CLAUDE_REVIEW_001

**Proves:** Wave 016 Claude Lane S10. Syft approval; tool admission; tool version/hash/source; SBOM artifact; ecosystem coverage; trust board update; license/security boundary. Reject SBOM claims without artifact.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE016_GUI_FIRST_VISUAL_PROOF_CLAUDE_REVIEW_001

**Proves:** Wave 016 Claude Lane G10. MSEdgeDriver approval; GUI launch approval; driver admission; Tauri artifact hash; launch transcript; screenshot; DOM/anchor; process metadata; stdout/stderr; cleanup/orphan transcript; first-paint vs e2e wording.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE016_LOCAL_PREVIEW_PROMOTION_FULL_GATE_CLAUDE_REVIEW_001

**Proves:** Wave 016 Claude Lane L10. Per package: wheel/PEP517 + isolated install + installed entry point + source-tree leakage rejection + detector + fixture + 3 verifier signoffs + fake-transcript rejection + proof-report anchor + metadata + local-preview boundary + score evidence-delta + canonical release-supported status. Per-package verdict.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE016_LOCAL_PREVIEW_RELEASE_CLEANHOST_FAMILY_BOUNDARY_CLAUDE_REVIEW_001

**Proves:** Wave 016 Claude Lane P10. 5 distinct statuses (LOCAL_PREVIEW_PROVEN / RELEASE_SUPPORTED_EXACT_CELL / CLEAN_HOST_PROVEN / PUBLIC_PACKAGE_READY / FAMILY_SUPPORTED); per-package status; unsafe wording fixtures; safe wording examples; proof-report language; release registry language. Reject category bleed.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE016_PROOF_REPORT_CLAIM_SCANNER_BACKFILL_CLAUDE_REVIEW_001

**Proves:** Wave 016 Claude Lane R10. Per-capability coverage; per-family status; per-claim evidence anchors; blocked/not-claimed examples; schema_version; score evidence-delta links; fake/legit rise fixtures; single-number quote prevention; forbidden phrase expansion; claim scanner CI.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE016_RELEASE_CELL_DRIFT_DETECTOR_CI_CLAUDE_REVIEW_001

**Proves:** Wave 016 Claude Lane B10. Drift detector implementation; scan coverage; failing/passing fixtures; current artifact scan; CI invocation; historical/current classification; whether Codex/Claude/report disagreement would now fail CI. Reject detector that only documents mismatch.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE016_RUNTIME_APPROVAL_HARDENING_CLAUDE_REVIEW_001

**Proves:** Wave 016 Claude Lane X10. Real operator signature import procedure; self-hash bug fix; target/command-scope hash binding tests; expiration/revocation tests; malformed-signature rejection test; audit-log tamper guard; ready-to-sign packets; signed-valid queue status.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE016_VERIFIER_SIGNOFF_SCHEMA_PROMOTION_BINDING_CLAUDE_REVIEW_001

**Proves:** Wave 016 Claude Lane V10. Signoff schema; valid/missing/malformed/narrative-only fixtures; promotion gate binding; existing release cell audit; local-preview candidate audit. Reject schema not enforced by promotion logic.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE017_CANONICAL_DRIFT_DETECTOR_LIVE_CI_LOCK_001

**Proves:** Canonical Drift Detector CI Live-Run

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE017_CANONICAL_REGISTRY_CONSUMPTION_CLAUDE_REVIEW_001

**Proves:** Wave 017 Claude Lane A11. Registry single source; every current reader consumption; conveyor binding; proof report; reconciliation packets; status artifacts; historical labels; hardcoded stale constants; family invariant.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE017_CANONICAL_REGISTRY_CONSUMPTION_VERIFICATION_LOCK_001

**Proves:** Verify Canonical Registry Consumption Everywhere

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE017_CLAUDE_SYNTHESIS_AND_WAVE018_PRESSURE_QUEUE_001

**Proves:** Wave 017 Claude Lane Q11. Synthesis. Answer: registry truly fixed? legacy signoff backfilled? local-preview properly bounded? hard floor crossed? Tier-1 fixture execution expanded? family support remains false? Rank deltas + 8 blocker categories. Generate Wave 018 queues.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE017_CLEAN_HOST_FIRST_TRANSCRIPT_CLAUDE_REVIEW_001

**Proves:** Wave 017 Claude Lane F12. Runner approval/admission; context (ADMITTED_CLEAN_RUNNER / LOCAL_SIMULATION / BLOCKED); clean checkout; dependency probe; bootstrap; build/test/smoke transcript; canonical cell transcript when claimed; local-preview transcript when claimed.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE017_CLEAN_HOST_FIRST_TRANSCRIPT_IF_ADMITTED_LOCK_006

**Proves:** Clean-Host First Transcript If Runner Admitted

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE017_DRIFT_DETECTOR_LIVE_CI_CLAUDE_REVIEW_001

**Proves:** Wave 017 Claude Lane B11. Drift detector script; live transcript; failing/passing fixtures; historical skip fixture; CI workflow binding; current artifact scan; whether Codex/Claude/proof-report disagreement would fail.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE017_FAMILY_SUPPORT_READINESS_MATRIX_CLAUDE_REVIEW_001

**Proves:** Wave 017 Claude Lane M11. Family readiness matrix; detector coverage; parser/manifest; fixture count; command routing; build/test/smoke; repair-loop; verifier coverage; clean-host; anchors; exact cell count; blockers; no-family-support invariant.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE017_FIRST_REAL_SIGNATURE_SPEND_CLAUDE_REVIEW_001

**Proves:** Wave 017 Claude Lane Y11. signed-valid queue; operator approval files; validation result; import result; spend result; execution_allowed event; admission/execution transcript; rollback/cleanup; audit chain. Verdict distinguishes 6 levels.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE017_FIRST_REAL_SIGNATURE_SPEND_IF_PRESENT_LOCK_002

**Proves:** First Real Signature Spend If Present

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE017_FIRST_SBOM_ARTIFACT_CLAUDE_REVIEW_001

**Proves:** Wave 017 Claude Lane S11. Syft approval; resolution; admission; version/hash/source; SBOM artifact; ecosystem coverage; trust board update; license/security boundary.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE017_FIRST_SBOM_IF_TOOL_ADMITTED_LOCK_007

**Proves:** First SBOM If Tool Admitted

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE017_GUI_FIRST_VISUAL_PROOF_CLAUDE_REVIEW_001

**Proves:** Wave 017 Claude Lane G11. MSEdgeDriver approval; GUI launch approval; driver admission; Tauri artifact hash; launch transcript; screenshot; DOM/anchor; process metadata; stdout/stderr; cleanup/orphan transcript; first-paint vs e2e wording.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE017_GUI_FIRST_VISUAL_PROOF_IF_APPROVED_LOCK_004

**Proves:** GUI First Visual Proof If Approved

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE017_LEGACY_SIGNOFF_BACKFILL_CLAUDE_REVIEW_001

**Proves:** Wave 017 Claude Lane C11. 10 canonical cells; signoff records; detector/fixture/build/test/smoke/install evidence; proof-report anchor; claim-boundary; fake-transcript rejection coverage; missing-rung classification. Per-cell verdict.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE017_LOCAL_PREVIEW_PACKAGE_READINESS_CLAUDE_REVIEW_001

**Proves:** Wave 017 Claude Lane E11. Per package: status remains LOCAL_PREVIEW_PROVEN_NOT_RELEASE_SUPPORTED; wheel + isolated install + entry point + leakage rejection + detector + fixture + 3 verifier signoffs + fake-rejection coverage + anchor + metadata + boundary + score evidence-delta.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE017_PROOF_REPORT_ANCHOR_BACKFILL_CLAUDE_REVIEW_001

**Proves:** Wave 017 Claude Lane D11. 10 canonical cells; per-cell proof-report anchors; whether anchors point to hard evidence; missing-anchor classifications; exact cell language; family boundary; local-preview boundary; schema version; evidence hash.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE017_PROOF_REPORT_CLAIM_SCANNER_FINAL_CHECK_CLAUDE_REVIEW_001

**Proves:** Wave 017 Claude Lane R11. Per-capability coverage; per-family status; per-claim anchors; blocked/not-claimed; schema version; score evidence-delta links; fake/legit rise fixtures; single-number quote prevention; expanded forbidden phrases; claim scanner CI.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE017_RELEASE_PROMOTION_NEGATIVE_TESTS_CLAUDE_REVIEW_001

**Proves:** Wave 017 Claude Lane F11. Rejection fixtures: cell not in registry / missing signoff / malformed signoff / narrative-only anchor / local-preview promoted without gate / family inference / public package implication / clean-host implication without transcript / stale 13 read as current / score rise without evidence-delta.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE017_RUNTIME_APPROVAL_HARDENING_CLAUDE_REVIEW_001

**Proves:** Wave 017 Claude Lane X11. Operator signature import procedure; self-hash bug fix; target/command-scope hash binding tests; expiration/revocation tests; malformed signature rejection test; audit-log tamper guard; signed-valid queue status; ready-to-sign packets.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE017_TIER1_FIXTURE_EXECUTION_CLAUDE_REVIEW_001

**Proves:** Wave 017 Claude Lane T11. Tier-1 families: Python pkg/CLI, Node/TS, React/Vite, Rust CLI, Go CLI, static docs/web, local API, SQLite, Tauri shell, GH Actions. Detector→route→verifier pipeline; safe boundaries; build/test/smoke transcripts; blocked-rung reports.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE018_ALL_READERS_BIND_TO_REGISTRY_CLAUDE_REVIEW_001

**Proves:** Wave 018 Claude Lane A12. Every current reader/asserter of release-supported cell count; wave common (Codex + Claude); conveyor; proof report; reconciliation; drift detector; status guards; stale 13 literals; hardcoded current 10 readers; historical/current classification. Verdict: do all current readers consume registry; can stale 13 be read as current.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE018_BROKEN_CANONICAL_PROOF_ANCHOR_CLAUDE_REVIEW_001

**Proves:** Wave 018 Claude Lane C12. 10 canonical cells; source_artifact paths; previously broken anchor; repair or blocker classification; test coverage; proof-report impact.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE018_CLAIM_SCANNER_FINAL_CI_CLAUDE_REVIEW_001

**Proves:** Wave 018 Claude Lane R12. Claim scanner CI; single-number quote prevention; expanded forbidden phrases; safe wording examples; proof-report public language; local-preview language; release-supported language; family-support language; score evidence-delta links.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE018_CLAUDE_SYNTHESIS_AND_WAVE019_PRESSURE_QUEUE_001

**Proves:** Wave 018 Claude Lane Q12. Synthesis. 9 headline questions. Rank top Codex deltas + 7 blocker categories. Generate Wave 019 queues. Score progression with evidence-delta binding.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE018_CLEAN_HOST_FIRST_TRANSCRIPT_CLAUDE_REVIEW_001

**Proves:** Wave 018 Claude Lane F13. Runner approval/admission; context (ADMITTED/LOCAL_SIM/BLOCKED); clean checkout; dependency probe; bootstrap; build/test/smoke transcript; canonical cell + local-preview package transcripts when claimed.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE018_CLEAN_HOST_FIRST_TRANSCRIPT_IF_ADMITTED_LOCK_007

**Proves:** Clean-Host First Transcript If Runner Admitted

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE018_DRIFT_DETECTOR_WORKFLOW_STATUS_GUARD_CLAUDE_REVIEW_001

**Proves:** Wave 018 Claude Lane B12. .github/workflows/*.yml binding (if present); fallback status guard binding; live transcript; failing/passing/historical fixtures; explicit historical field use; whether developer skipping full pytest still caught.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE018_FAKE_TRANSCRIPT_REJECTION_COVERAGE_CLAUDE_REVIEW_001

**Proves:** Wave 018 Claude Lane E12. Coverage for: missing/malformed transcript, dry-run-as-install, source-tree-command-as-entry-point, command-map-as-execution, local-simulation-as-clean-host, built-artifact-as-GUI-launch, SBOM-packet-as-SBOM. Linkage to applicable canonical cells.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE018_FAMILY_READINESS_MATRIX_CLAUDE_REVIEW_001

**Proves:** Wave 018 Claude Lane M12. Family readiness matrix; family support gate definition; detector coverage; parser/manifest; fixture count; command routing; build/test/smoke; repair-loop; verifier coverage; clean-host; anchors; exact cell count; blocked rungs; no-family-support invariant.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE018_FIRST_REAL_SIGNATURE_SPEND_CLAUDE_REVIEW_001

**Proves:** Wave 018 Claude Lane Y12. signed-valid queue; operator approval files; validation/import/spend results; execution_allowed event; admission/execution transcript; rollback/cleanup; audit chain. 6-level verdict.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE018_FIRST_REAL_SIGNATURE_SPEND_IF_PRESENT_LOCK_003

**Proves:** First Real Signature Spend If Present

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE018_FIRST_SBOM_ARTIFACT_CLAUDE_REVIEW_001

**Proves:** Wave 018 Claude Lane S12. Syft approval; resolution; admission; version/hash/source; SBOM artifact; ecosystem coverage; trust board; license/security boundary.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE018_FIRST_SBOM_IF_TOOL_ADMITTED_LOCK_008

**Proves:** First SBOM If Tool Admitted

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE018_GUI_FIRST_VISUAL_PROOF_CLAUDE_REVIEW_001

**Proves:** Wave 018 Claude Lane G13. MSEdgeDriver approval; GUI launch approval; driver admission; Tauri artifact hash; launch transcript; screenshot; DOM/anchor; process metadata; stdout/stderr; cleanup; first-paint vs e2e wording.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE018_GUI_FIRST_VISUAL_PROOF_IF_APPROVED_LOCK_005

**Proves:** GUI First Visual Proof If Approved

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE018_LEGACY_SIGNOFF_BACKFILL_CLAUDE_REVIEW_001

**Proves:** Wave 018 Claude Lane D12. All 10 canonical cells: detector/fixture/build/test/smoke/install signoff; proof-report anchor signoff; claim-boundary signoff; fake-transcript rejection coverage; missing-rung classification. Per-cell verdict.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE018_PROMOTION_NEGATIVE_FIXTURE_CLAUDE_REVIEW_001

**Proves:** Wave 018 Claude Lane F12. Rejection fixtures: cell-not-in-registry / missing/malformed signoff / narrative-only-anchor / local-preview-promoted-without-gate / family-support-inference / public-package-implication / clean-host-implication-without-transcript / stale-historical-13-as-current / score-rise-without-evidence-delta.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE018_PROOF_REPORT_REGISTRY_BINDING_CLAUDE_REVIEW_001

**Proves:** Wave 018 Claude Lane G12. Proof report binds to canonical registry; per-cell anchor section; per-family status section; local-preview boundary section; blocked/not-claimed section; schema_version; evidence hash; stale-count rejection; safe wording.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE018_RUNTIME_APPROVAL_HARDENING_CLAUDE_REVIEW_001

**Proves:** Wave 018 Claude Lane X12. Operator signature import procedure; self-hash bug fix; target/command-scope hash binding tests; expiration/revocation tests; malformed signature rejection test; audit-log tamper guard; signed-valid queue status; ready-to-sign packets.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE018_TIER1_FIRST_FAMILY_TRANSCRIPT_CLAUDE_REVIEW_001

**Proves:** Wave 018 Claude Lane T12. Tier-1 candidates (Python pkg/CLI, Node/TS, React/Vite, Rust, Go, static docs, local API, SQLite, Tauri, GH Actions); selected family rationale; detector→route→verifier pipeline; safe boundary; build/test/smoke transcript if executed; blocked-rung report for others; no-family-support boundary.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE019_CAPABILITY_SCORE_DELTA_GUARD_CLAUDE_REVIEW_001

**Proves:** Wave 019 Claude Lane V13. Reject score rise from: packet-only / historical / local-preview-as-release / one-fixture-as-family / packet-without-spend / SBOM-packet-without-artifact / GUI-packet-without-launch / clean-host-packet-without-transcript / docs-without-CI. Require evidence-delta object per movement.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE019_CLAIM_SCANNER_CI_EXPANSION_CLAUDE_REVIEW_001

**Proves:** Wave 019 Claude Lane R13. Scanner coverage for: all programming languages / all programmatic things / production ready / public installer ready / release ready / family supported / clean-host proven / GUI proven / SBOM complete / secure / fully autonomous / training eligible / single-number score quotes / local-preview implying public.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE019_CLAUDE_SYNTHESIS_AND_WAVE020_PRESSURE_QUEUE_001

**Proves:** Wave 019 Claude Lane Q13. Synthesis. 15 questions. Rank blockers across 9 categories. Generate Wave 020 queues. Required next hard floor.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE019_FAMILY_SUPPORT_GATE_DEFINITION_CLAUDE_REVIEW_001

**Proves:** Wave 019 Claude Lane M13. 16 family-support gates documented? CI invariant `release_supported_families == 0 unless every gate closes`?

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE019_FIRST_CLEAN_HOST_TRANSCRIPT_CLAUDE_REVIEW_001

**Proves:** Wave 019 Claude Lane F15. Clean-runner admission; environment classification; clean checkout; dependency probe; bootstrap; build/test/smoke transcript; selected target; transcript integrity; local-simulation boundary. ADMITTED/SIM/BLOCKED verdict.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE019_FIRST_GUI_VISUAL_PROOF_CLAUDE_REVIEW_001

**Proves:** Wave 019 Claude Lane G15. Driver approval; GUI launch approval; Tauri artifact hash; driver admission; bounded launch transcript; screenshot; DOM/anchor; process metadata; stdout/stderr; cleanup; first-paint vs e2e boundary.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE019_FIRST_REAL_SIGNATURE_IMPORT_SPEND_CLAUDE_REVIEW_001

**Proves:** Wave 019 Claude Lane C13. signed-valid queue; operator approval files; audit log; validation; target/command-scope hash binding; expiration/revocation; one-time spend rule; execution_allowed event; execution transcript; rollback/cleanup. 5-level verdict.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE019_FIRST_SBOM_ARTIFACT_CLAUDE_REVIEW_001

**Proves:** Wave 019 Claude Lane S13. Syft approval; tool admission; binary/source hash; version; SBOM artifact; ecosystem coverage; trust-board update; license/security boundary. SBOM requires emitted artifact.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE019_LEGACY_FULL_VERIFIER_SIGNOFF_CLAUDE_REVIEW_001

**Proves:** Wave 019 Claude Lane A13. All 10 canonical cells: per-rung signoff (detector/fixture/build/test/smoke/install) + proof-report anchor + claim-boundary + fake-transcript rejection + score/evidence-delta + family-support boundary. Per-cell verdict.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE019_LOCAL_PREVIEW_PACKAGE_BOUNDARY_CLAUDE_REVIEW_001

**Proves:** Wave 019 Claude Lane L13. 3 packages: local proof specific; public availability FALSE unless proven; clean-host FALSE unless proven; release-supported FALSE unless promoted; install proof FALSE unless transcript; proof-report boundary present; claim scanner fixtures present.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE019_PROOF_REPORT_RELEASE_BOUNDARY_CLAUDE_REVIEW_001

**Proves:** Wave 019 Claude Lane P13. Proof report renders: exact cells=10 / families=0 / local-preview pkgs / Tier-1 coverage / SBOM status / clean-host status / GUI status / signed approval status / family-support status / blocked/not-claimed section / evidence-delta score basis / schema_version / evidence hash.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE019_REPAIR_LOOP_READINESS_MAP_CLAUDE_REVIEW_001

**Proves:** Wave 019 Claude Lane U13. Known failure fixtures; detector status; build/test/smoke routing; repair-loop availability; bounded repair policy; verifier after repair; fake repair rejection; training eligibility boundary; corpus eligibility boundary; blocked rungs; Wave 020 repair queue.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE019_RUNTIME_APPROVAL_HARDENING_TESTS_CLAUDE_REVIEW_001

**Proves:** Wave 019 Claude Lane D13. Live tests for rejection of: malformed sig / expired / revoked / wrong target hash / wrong command scope / replayed spend / tampered log / unsigned / missing operator identity / missing target artifact.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE019_SIGNOFF_GATE_ENFORCEMENT_CI_CLAUDE_REVIEW_001

**Proves:** Wave 019 Claude Lane B13. Whether CI/status guards REJECT (with injection transcript): missing anchor / unresolved anchor / missing claim-boundary / missing fake-rejection / build-test-smoke without transcript / local-preview-as-release / exact-cell-as-family / historical-as-current / score rise without evidence-delta.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE019_TIER1_SECOND_THIRD_FAMILY_TRANSCRIPTS_CLAUDE_REVIEW_001

**Proves:** Wave 019 Claude Lane T13. Did Codex expand beyond docs_static? Candidates: Python pkg/CLI, Node/TS, React/Vite, Rust CLI, Go CLI, local API, SQLite, Tauri shell, GH Actions. Per-family check; no-family-support; no clean-host implication.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020A_CLAIM_SCANNER_CI_FINAL_STATE_CLAUDE_REVIEW_001

**Proves:** Wave 020A Claude Lane E14. 14 phrases: scanner script exists / unsafe fixtures / safe wording examples / CI binding / failure transcripts.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020A_CLAUDE_W019_FINDING_RECONCILIATION_001

**Proves:** Wave 020A Claude Lane G14. Classify 12 W019 findings as STILL_TRUE / STALE_AFTER_CODEX_FINAL_COMMIT / PARTIALLY_TRUE / FALSE_ON_FINAL_COMMIT / NEEDS_CODEX_DELTA.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020A_FINAL_COMMIT_EVIDENCE_SPINE_CLAUDE_REVIEW_001

**Proves:** Wave 020A Claude Lane A14. HEAD hash; branch sync; c3233ca50 reachable; working tree clean; evidence index 1011; Wave 019 artifacts present. STALE_REVIEW_AVOIDED verdict.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020A_PROOF_REPORT_BOUNDARY_FINAL_STATE_CLAUDE_REVIEW_001

**Proves:** Wave 020A Claude Lane F14. 13 axes: exact cells=10, families=0, local-preview, Tier-1, SBOM blocked, clean-host blocked, GUI blocked, signed spend absent, family gate false, blocked/not-claimed, evidence-delta basis, schema, hash.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020A_RUNTIME_HARDENING_FINAL_STATE_CLAUDE_REVIEW_001

**Proves:** Wave 020A Claude Lane C14. 10 rejection cases: live test file / fixture / expected rejection / actual test result. Live enforcement vs packet-only vs absent vs partial verdict.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020A_SCORE_DELTA_FINAL_STATE_CLAUDE_REVIEW_001

**Proves:** Wave 020A Claude Lane H14. under-the-hood 49.0%→55.0% / full envisioned IDE 79-81% / open-availability unchanged / packaging unchanged / Companion RAG unchanged. Reject score from stale snapshot. Require evidence-delta object.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020A_SIGNOFF_GATE_INJECTION_FINAL_STATE_CLAUDE_REVIEW_001

**Proves:** Wave 020A Claude Lane D14. 9 fixtures: fixture path / gate invoked / failure transcript / expected failure reason / CI binding.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020A_SYNTHESIS_AND_WAVE020B_PRESSURE_QUEUE_001

**Proves:** Wave 020A Claude Lane Q14. Synthesis. 15 questions. Wave 020B Codex queue + Claude lanes. Next hard floor + next Tier-1 target.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020A_TIER1_TRANSCRIPT_FINAL_STATE_CLAUDE_REVIEW_001

**Proves:** Wave 020A Claude Lane B14. docs_static + python_apps + sqlite_local_db — per family: evidence path / detector transcript / route resolver / verifier / build / test / smoke / exit codes / local-vs-clean-host / no-family-support boundary.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020B5_CODEX_EXECUTION_CONTRACT_WRITER_CLAUDE_001

**Proves:** Wave 020B.5 Claude Lane H. Produce CODEX_WAVE020B_EXECUTION_CONTRACT_READY with: baseline + blockers + target movement + ranked lanes + acceptance criteria per lane + required artifacts + failure conditions + score rules + authority boundaries + forbidden actions + final report schema.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020B5_ENFORCEMENT_COMPLETENESS_CLAUDE_001

**Proves:** Wave 020B.5 Claude Lane D. Runtime hardening 6/10 → remaining 4; signoff gate 5/9 → remaining 4; claim scanner phrase expansion; proof report production HTML. COMPLETE / PARTIAL / PACKET_ONLY / ABSENT / BLOCKED.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020B5_HARD_FLOOR_STATUS_CLAUDE_001

**Proves:** Wave 020B.5 Claude Lane C. signed-valid queue; approval files; audit log; real signature; spend; execution_allowed; SBOM; clean-host; GUI; installer. Per-row classify.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020B5_LATEST_STATE_VERIFICATION_CLAUDE_001

**Proves:** Wave 020B.5 Claude Lane A. HEAD; branch; sync; tree; latest Codex commit; evidence spine; CLI validate; release cell registry count; families count. Classify FINAL_STATE_VERIFIED / MOVING_TARGET_DETECTED / STALE_REVIEW_NOT_ALLOWED / REQUIRES_CODEX_CLOSEOUT.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020B5_PRODUCTION_PROOF_REPORT_CURRENT_STATE_CLAUDE_001

**Proves:** Wave 020B.5 Claude Lane F. Production HTML regenerated from canonical registry? Renders 13 axes: cells=10, families=0, local-preview, Tier-1, SBOM, clean-host, GUI, signed-spend, family gate, blocked/not-claimed, evidence-delta basis, schema, hash.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020B5_REPAIR_CAPABILITY_CURRENT_STATE_CLAUDE_001

**Proves:** Wave 020B.5 Claude Lane E. Broken fixture; failing transcript; repair action transcript; exact diff; post-repair verifier; fake-repair rejection; no-broad-repair boundary; training/corpus eligibility boundary.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020B5_SCORE_AND_MOVEMENT_AUDIT_CLAUDE_001

**Proves:** Wave 020B.5 Claude Lane G. Per metric: before/after/delta/packet/blocked-non-movement-rationale. Reject score rise from packet-only/local-as-family/packet-as-spend/sample-as-production.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020B5_SYNTHESIS_AND_CODEX_HANDOFF_CLAUDE_001

**Proves:** Wave 020B.5 Claude Lane Q. Synthesis. 20 questions. Codex handoff. Next Codex queue + next Claude verification lanes.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020B5_TIER1_TRANSCRIPT_CURRENT_STATE_CLAUDE_001

**Proves:** Wave 020B.5 Claude Lane B. Per family: evidence path, detector/route/verifier transcript, build/test/smoke, exit codes, local-vs-clean-host, no-family-support boundary. Did any new Tier-1 family land?

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020C5_BOUNDED_REPAIR_VERIFY_LOCK_001

**Proves:** Wave 020C.5 Claude Lane D. Broken fixture; failing verifier transcript; repair action; exact diff; post-repair verifier; fake-repair rejection; training/corpus eligibility; no-broad-repair boundary.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020C5_CODEX_CLAIM_VERIFICATION_LOCK_001

**Proves:** Wave 020C.5 Claude Lane B. 20 Codex W020C claims classified VERIFIED / PARTIALLY_VERIFIED / NOT_VERIFIED / ABSENT / CONTRADICTED against commit 6aac2b31a state.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020C5_ENFORCEMENT_BACKFILL_VERIFY_LOCK_001

**Proves:** Wave 020C.5 Claude Lane F. Runtime hardening 10/10 live; signoff gate 9/9 real; claim scanner expansion includes new phrases.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020C5_EXACT_CODEX_COMMIT_REVIEW_LOCK_001

**Proves:** Wave 020C.5 Claude Lane A. HEAD; reachability; target commit equals HEAD; commits between prior and target. TARGET_COMMIT_REVIEWED classification.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020C5_HARD_FLOOR_BOUNDARY_VERIFY_LOCK_001

**Proves:** Wave 020C.5 Claude Lane G. BOUNDARY_HELD verification: signed_valid_queue=0; audit log unchanged; no SBOM/clean-host/GUI/installer execution; no unauthorized execution.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020C5_PROOF_REPORT_AND_SCORE_DASHBOARD_VERIFY_LOCK_001

**Proves:** Wave 020C.5 Claude Lane E. docs/proof_report/index.html renders 13 axes; docs/score_dashboard.md shows 5 metrics with before/after/delta/evidence/non-movement-rationale.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020C5_SCORE_DELTA_VERIFY_LOCK_001

**Proves:** Wave 020C.5 Claude Lane H. Under-the-hood 55→59 (+4pp) verified evidence-bound; other 4 metrics unchanged with rationale.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020C5_SYNTHESIS_AND_WAVE021_CORRECTIVE_QUEUE_LOCK_001

**Proves:** Wave 020C.5 Claude Lane Q. Synthesis. Corrected baseline. Wave 021 queue (signature import + remaining gates).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020C5_TIER1_GITHUB_ACTIONS_VERIFY_LOCK_001

**Proves:** Wave 020C.5 Claude Lane C. github_actions_ci_config: evidence path / detector / route / verifier / YAML or workflow structure validation / triggers-jobs-steps / exit codes / local-only / no family-support.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020C_CLAIM_SCANNER_EXPANSION_CLAUDE_REVIEW_001

**Proves:** Wave 020C Claude Lane H20C. 18 unsafe/safe fixture pairs + CI/status binding.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020C_CLAIM_SCANNER_FORBIDDEN_PHRASE_EXPANSION_LOCK_001

**Proves:** Claim Scanner Forbidden Phrase Expansion

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020C_CLAUDE_SYNTHESIS_AND_WAVE021_QUEUE_001

**Proves:** Wave 020C Claude Lane Q20C. Synthesis. Wave 021 carry queue (every W020B contract item still rank-equivalent).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020C_CONDITIONAL_HARD_FLOOR_EXECUTION_CLAUDE_REVIEW_001

**Proves:** Wave 020C Claude Lane K20C. If no approval: verify blocked + no unauthorized execution. If approval: verify target + transcript + no scope creep. Check SBOM/clean-host/GUI/installer.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020C_CONDITIONAL_HARD_FLOOR_EXECUTION_IF_APPROVED_LOCK_001

**Proves:** Conditional Hard Floor Execution If Approved

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020C_CONSUME_CLAUDE_020B5_CONTRACT_LOCK_001

**Proves:** Consume Claude 020B.5 Contract

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020C_CONTRACT_CONSUMPTION_CLAUDE_REVIEW_001

**Proves:** Wave 020C Claude Lane A20C. Did Codex read the contract; did execution lanes match; did stale assumptions stay rejected; did cells stay 10 / families stay 0.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020C_CONTRACT_EXECUTION_RECONCILIATION_LOCK_001

**Proves:** Wave 020C Contract Execution Reconciliation

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020C_FIRST_BOUNDED_REPAIR_CLAUDE_REVIEW_001

**Proves:** Wave 020C Claude Lane D20C. Broken fixture / failing transcript / repair action / exact diff / post-repair transcript / fake-repair rejection / boundary.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020C_FIRST_BOUNDED_REPAIR_FIXTURE_LOCK_001

**Proves:** First Bounded Repair Fixture

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020C_LEGACY_EXECUTION_RUNG_SIGNOFF_BACKFILL_LOCK_001

**Proves:** Legacy Execution-Rung Signoff Backfill

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020C_LEGACY_EXECUTION_RUNG_SIGNOFF_CLAUDE_REVIEW_001

**Proves:** Wave 020C Claude Lane J20C. 10 cells × 6 missing rungs (detector/fixture/build/test/smoke/install). Reject invented historical evidence.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020C_PRODUCTION_PROOF_REPORT_HTML_CLAUDE_REVIEW_001

**Proves:** Wave 020C Claude Lane E20C. docs/proof_report/index.html present and renders 13 axes from registry.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020C_PRODUCTION_PROOF_REPORT_HTML_REGENERATION_LOCK_001

**Proves:** Production Proof Report HTML Regeneration

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020C_REAL_SIGNATURE_IMPORT_PROCEDURE_AND_FIRST_PACKET_LOCK_001

**Proves:** Real Signature Import Procedure And First Packet

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020C_RUNTIME_HARDENING_FULL_TEN_CLAUDE_REVIEW_001

**Proves:** Wave 020C Claude Lane F20C. 10 rejection cases all live with real validator invocation + rejection transcript.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020C_RUNTIME_HARDENING_REMAINING_FOUR_LOCK_001

**Proves:** Runtime Hardening Remaining Four

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020C_SCORE_DASHBOARD_AND_DELTA_GUARD_CI_LOCK_001

**Proves:** Score Dashboard And Delta Guard CI

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020C_SCORE_DASHBOARD_DELTA_GUARD_CLAUDE_REVIEW_001

**Proves:** Wave 020C Claude Lane I20C. Dashboard exists / per-movement before+after+delta+evidence+reason / blocked non-movement / guard rejects inflated rise.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020C_SIGNATURE_IMPORT_SPEND_CLAUDE_REVIEW_001

**Proves:** Wave 020C Claude Lane B20C. signed-valid queue / approval files / import procedure / signing packet / signature / target hash / command scope / expiration / spend / execution_allowed / audit log.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020C_SIGNOFF_GATE_FULL_NINE_CLAUDE_REVIEW_001

**Proves:** Wave 020C Claude Lane G20C. 9 injection cases all real with gate injection + rejection transcript.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020C_SIGNOFF_GATE_REMAINING_FOUR_LOCK_001

**Proves:** Signoff Gate Remaining Four

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020C_TIER1_FOURTH_FAMILY_CLAUDE_REVIEW_001

**Proves:** Wave 020C Claude Lane C20C. Expected target: github_actions_ci_config. Detector/route/verifier/YAML transcript/exit codes/local-only/no-family-support boundary.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE020C_TIER1_GITHUB_ACTIONS_CI_CONFIG_TRANSCRIPT_LOCK_001

**Proves:** Tier-1 GitHub Actions CI Config Transcript

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE021_ADAPTER_INTERFACE_CLAUDE_REVIEW_001

**Proves:** Wave 021 Claude Lane D. 10 interface methods; result schemas; detector-only-cannot-promote; command-map-cannot-count-as-execution; local-only-cannot-count-as-clean-host.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE021_CANONICAL_FAMILY_REGISTRY_CLAUDE_REVIEW_001

**Proves:** Wave 021 Claude Lane C. 31 families with canonical IDs + 5 known aliases (python_apps/python_package + docs_static/static_web_docs + tauri_desktop/tauri_electron_desktop + node_typescript_package/node_typescript_apps + github_actions_ci_config/devops_ci_projects). Drift resolution test required.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE021_CONTRACT_RECEIPT_AND_START_STATE_LOCK_001

**Proves:** DETERMINEX_WAVE021_CONTRACT_RECEIPT_AND_START_STATE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE021_CONTRACT_RECEIPT_CLAUDE_REVIEW_001

**Proves:** Wave 021 Claude Lane A. Verify contract_consumption_receipt_per_wave exists; cites W021; records baseline+lanes+deferrals+authority split. HEAD recheck per W020C.5 rank-10.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE021_EXTERNAL_AUTHORITY_TRACK_CLAUDE_REVIEW_001

**Proves:** Wave 021 Claude Lane J. signature state; SBOM/clean-host/GUI state; operator gates separate; no protected execution without approval. Boundary held check.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE021_FIFTH_FAMILY_ADAPTER_TRANSCRIPT_CLAUDE_REVIEW_001

**Proves:** Wave 021 Claude Lane F. 5th family chosen from {Node/TS, Rust, Go, React/Vite, local API}; adapter row + detector + build/test/smoke or exact blocker; ProgramAuthorityRecord.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE021_FOUR_VERIFIED_FAMILY_ADAPTER_PORT_CLAUDE_REVIEW_001

**Proves:** Wave 021 Claude Lane E. Per-family adapter port for docs_static/python_apps/sqlite_local_db/github_actions_ci_config; detector bound; transcript linked; ProgramAuthorityRecord emitted.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE021_MACHINE_PROMOTION_RULES_CLAUDE_REVIEW_001

**Proves:** Wave 021 Claude Lane I. Machine CAN promote 8 categories (parse/build/test/smoke/repaired-then-pass/exact-local-cell/negative-signal/blocked-missing-tool); CANNOT promote 9 categories (family/release/clean-host/GUI/SBOM/installer/training/real-user-source-mutation/public-readiness).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE021_NONCODER_PROOF_REPORT_CLAUDE_REVIEW_001

**Proves:** Wave 021 Claude Lane H. Reports rendered from ProgramAuthorityRecord; 11 required narrative sections; at least 1 verified + 1 repaired + 1 blocked example. Reject hand-written.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE021_PROGRAM_AUTHORITY_RECONCILIATION_LOCK_001

**Proves:** DETERMINEX_WAVE021_PROGRAM_AUTHORITY_RECONCILIATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE021_PROGRAM_AUTHORITY_SCHEMA_CLAUDE_REVIEW_001

**Proves:** Wave 021 Claude Lane B. scripts/proof/program_authority/ presence + 8 required files + 12 required dataclasses. ABSENT = ABSENT.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE021_PROGRAM_AUTHORITY_SYNTHESIS_CLAUDE_REVIEW_001

**Proves:** Wave 021 Claude Lane Q. Synthesis. Wave 022 carry queue (entire W021 contract unchanged + signature rank-1 still bottleneck).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE021_PROGRAM_NEGATIVE_SIGNAL_REGISTRY_CLAUDE_REVIEW_001

**Proves:** Wave 021 Claude Lane G. 13 typed signals (SYNTAX_FAIL/PARSE_FAIL/BUILD_FAIL/TEST_FAIL/SMOKE_FAIL/MISSING_TOOL/MISSING_DEPENDENCY/UNSUPPORTED_STRUCTURE/REPAIR_FAILED/REPAIRED_THEN_PASS/BLOCKED_REQUIRES_OPERATOR_AUTHORITY/BLOCKED_EXTERNAL_ACTION/NOT_CLAIMED) + free-text mapping + cannot-promote-support rule.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE022_DAY1_STRUCTURAL_COVERAGE_DASHBOARD_REVIEW_001

**Proves:** Wave 022 Claude Lane H. All 31 families × 14 columns (canonical ID, aliases, adapter, detector, oracle, verifier, repair, local transcript, clean-host, external authority, exact-cell, family-support, claim boundary, next proof rung). Reject 'all represented = all supported'.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE022_EXTERNAL_AUTHORITY_UNLOCK_PLAN_REVIEW_001

**Proves:** Wave 022 Claude Lane I. signed_valid_queue / signature packets / SBOM / clean-host / GUI / installer / blockers / operator-action packet / no protected execution without approval. 17-wave boundary held check.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE022_IDEA_LAB_ACCEPTANCE_TEST_GENERATOR_REVIEW_001

**Proves:** Wave 022 Claude Lane D. 6 freeform idea fixtures produce ProgramBrief + target family candidates + acceptance criteria + tests + smoke + blocked + decisions + authority matrix target rows + noncoder explanation. Reject prose-only.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE022_NONCODER_PROGRAM_AUTHORITY_REPORT_REVIEW_001

**Proves:** Wave 022 Claude Lane F. 7 report types (verified / Node-TS / missing-tool / failed-repair / repaired-then-pass / external-authority / unknown-novel) × 12 required sections, derived from authority records (not hand-written).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE022_PROGRAM_AUTHORITY_PRODUCT_BINDING_SYNTHESIS_REVIEW_001

**Proves:** Wave 022 Claude Lane Q. Synthesis. W021 fully landed; W022 product binding IN_FLIGHT_UNCOMMITTED. Wave 023 carry queue.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE022_PROGRAM_AUTHORITY_RECORD_CONSUMPTION_REVIEW_001

**Proves:** Wave 022 Claude Lane B. Do family readiness / product surfaces consume ProgramAuthorityRecord? Reject parallel stale truth / detector-as-support / local-as-clean-host / exact-cell-as-family / command-map-as-execution.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE022_PROMOTION_AND_NEGATIVE_ENFORCEMENT_REVIEW_001

**Proves:** Wave 022 Claude Lane G. 5 positive allowed (parse/build/test/smoke/repaired-then-pass) and 8 negative forbidden (detector-only / command-map / local-only-as-clean-host / exact-as-family / blocked-as-pass / failed-repair-as-support / missing-approval-as-protected / registry-row-as-verified) enforced as fixtures.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE022_REPO_CLINIC_AUTHORITY_INTAKE_REVIEW_001

**Proves:** Wave 022 Claude Lane E. 7 existing-repo fixtures intake into same authority matrix. Detected family + file roles + toolchain + command roles + safe/blocked + failures + repair candidates + negative signals + decisions + ProgramAuthorityRecord + noncoder summary.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE022_TIER1_ADAPTER_EXPANSION_REVIEW_001

**Proves:** Wave 022 Claude Lane C. rust_cli / go_cli / react_vite_apps / local_api_services / tauri_desktop_apps — adapter record, detector, oracle, command roles, transcript-or-blocker, negative signal, promotion rule, report sample.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE022_W021_FINAL_STATE_RECONCILIATION_REVIEW_001

**Proves:** Wave 022 Claude Lane A. Wave 021 final commit recognized; W021 reconciliation receipt + contract receipt present; prior Claude stale findings classified; receipt cites target wave.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE023_CODEX_COMMITS_BEFORE_REVIEW_PROTOCOL_REVIEW_001

**Proves:** Wave 023 Claude Lane A. Codex review-ready marker schema + emission + Claude-wait-guard tests + post-marker HEAD lock. Historical schema/test divergence detected at initial marker; Codex fix commit resolved.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE023_DAY1_PRODUCT_SPINE_SYNTHESIS_REVIEW_001

**Proves:** Wave 023 Claude Lane Q. Synthesis. Timer protocol validated. Day 1 product spine landed at HEAD. 3/5 batch 002 verified + 2/5 typed-blocked. Boundary held 18 waves. Wave 024 queue.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE023_DAY1_STRUCTURAL_DASHBOARD_RENDERED_REVIEW_001

**Proves:** Wave 023 Claude Lane G. Dashboard renders 31 families × 14 columns with safe wording artifact + unsafe-wording rejection fixtures. Reject 'all families represented = all families supported' / structural coverage as functional support / dashboard claim beyond record state.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE023_IDEA_LAB_ACCEPTANCE_TEST_EXECUTION_PIPELINE_REVIEW_001

**Proves:** Wave 023 Claude Lane C. 6 idea fixtures × {ProgramBrief, family candidates, acceptance tests, execution records, human decision points, noncoder explanation, claim boundary}. Reject prose-only / unbounded execution / family-support inference.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE023_NONCODER_REPORT_RENDERED_OUTPUTS_REVIEW_001

**Proves:** Wave 023 Claude Lane F. 7 report types rendered with required sections, derived from ProgramAuthorityRecord. Reject hand-written reports / report-without-record / verified-claims-in-blocked-record.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE023_PROMOTION_NEGATIVE_FIXTURE_CORPUS_REVIEW_001

**Proves:** Wave 023 Claude Lane H. 5 allowed positive categories + 8 forbidden negative categories each exercised by fixture with expected rejection transcript. Reject any forbidden promotion path / any rejection-bypass / any silent skip.

**Does not prove:** Does not prove corpus balance, training effectiveness, or public benchmark dominance by itself.

#### DETERMINEX_WAVE023_REACT_VITE_SIGNED_DEPENDENCY_REVIEW_001

**Proves:** Wave 023 Claude Lane E. Verify Codex correctly emitted BLOCKED_UNSIGNED for react_vite_apps (no signed approval). Reject any structural-only acceptance as transcript-equivalent / MISSING_DEPENDENCY auto-promotion / claim of release-supported.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE023_REAL_OPERATOR_SIGNATURE_IMPORT_PREP_REVIEW_001

**Proves:** Wave 023 Claude Lane I. Signature packet prepared with required signer fields + exact approval packet + command list if-later-approved; protected_execution_performed=false; authority_spent=false. Reject packet-as-authority / list-as-execution / import-as-admission.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE023_REPO_CLINIC_SECOND_FAMILY_REPAIR_LOOP_REVIEW_001

**Proves:** Wave 023 Claude Lane D. Bounded repair on second family fixture: broken/diff/repaired/before/after/fake-rejection/boundary. Verify ProgramAuthorityRecord + post-repair verifier + noncoder summary. Reject failed-repair-as-support / fake-repair-acceptance.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE023_TIER1_BATCH002_PER_FAMILY_VERIFIED_PROMOTION_REVIEW_001

**Proves:** Wave 023 Claude Lane B. 5 families × {adapter, oracle, detector, command roles, transcript-or-blocker, negative signal, machine promotion, claim boundary, noncoder report}. Verify 3/5 LOCAL_ONLY_VERIFIED, 2/5 typed-blocked. Reject any family-support / clean-host promotion.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE_004_CELL_MIX_AND_USER_FACING_REALITY_CLAUDE_REVIEW_001

**Proves:** Gulp Wave 004 Claude Lane X. Cell mix + user-facing reality. Cell 4 (local_proof_report_export_cell) added as internal_infrastructure_with_report_visibility. Non-user-facing streak now 3 of 5. Pressures Codex to reserve next cert slot for a user-visible candidate. Provides ranked candidate list with idea_lab_deterministic_prompt_to_plan as cheapest.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE_006_CLAUDE_SYNTHESIS_AND_WAVE_007_PRESSURE_QUEUE_001

**Proves:** Wave 006 synthesis. 10 lanes; 30 ranked Codex deltas; 20 full-system + 20 trust + 20 wow blockers; 12 claim risks; Wave 007 queue.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE_006_SHOCK_DEMO_EXECUTION_GAP_CLAUDE_REVIEW_001

**Proves:** Wave 006 Lane X. 11-step demo execution audit. 0 of 11 executable; 5/11 partially proved via cells; OMG contract defined, not executed.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE_007_CLAUDE_SYNTHESIS_AND_WAVE_008_PRESSURE_QUEUE_001

**Proves:** Wave 007 Claude Lane Q. Synthesize all Wave 007 Claude reviews; rank top 30 Codex deltas; top 20 full-system / trust / wow blockers; public claim risks; Wave 008 Claude lanes; Wave 008 Codex pressure queue.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE_012_CAPABILITY_SATURATION_RECONCILIATION_LOCK_001

**Proves:** DETERMINEX_WAVE_012_CAPABILITY_SATURATION_RECONCILIATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE_013_EXECUTION_RECONCILIATION_LOCK_001

**Proves:** DETERMINEX_WAVE_013_EXECUTION_RECONCILIATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE_014_SIGNED_EXECUTION_AND_CAPABILITY_RECONCILIATION_LOCK_001

**Proves:** Wave 014 Signed Execution and Capability Reconciliation

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE_015_CANONICAL_AND_HARD_FLOOR_RECONCILIATION_LOCK_001

**Proves:** Wave 015 Canonical and Hard-Floor Reconciliation

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE_016_CANONICAL_PROMOTION_AND_HARD_FLOOR_RECONCILIATION_LOCK_001

**Proves:** Wave 016 Reconciliation

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE_017_CANONICAL_SIGNOFF_AND_HARD_FLOOR_RECONCILIATION_LOCK_001

**Proves:** Wave 017 Reconciliation

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE_018_CANONICAL_BACKFILL_AND_FIRST_FAMILY_RECONCILIATION_LOCK_001

**Proves:** Wave 018 Reconciliation

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE_019_EXECUTION_FLOOR_AND_FAMILY_EXPANSION_RECONCILIATION_LOCK_001

**Proves:** Wave 019 Reconciliation

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE_020A_FINAL_STATE_RECONCILIATION_LOCK_001

**Proves:** Wave 020A Final-State Reconciliation

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE_021_FINAL_STATE_RECONCILIATION_RECEIPT_LOCK_001

**Proves:** DETERMINEX_WAVE_021_FINAL_STATE_RECONCILIATION_RECEIPT_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE_022_PROGRAM_AUTHORITY_PRODUCT_BINDING_RECONCILIATION_LOCK_001

**Proves:** DETERMINEX_WAVE_022_PROGRAM_AUTHORITY_PRODUCT_BINDING_RECONCILIATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WAVE_023_DAY1_PRODUCT_SPINE_RECONCILIATION_LOCK_001

**Proves:** DETERMINEX_WAVE_023_DAY1_PRODUCT_SPINE_RECONCILIATION_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WINDOWS_FIRST_LOCAL_DEPENDENCY_CHECK_LOCK_001

**Proves:** Record Windows-first local dependency readiness without installing dependencies or proving release support.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WINDOWS_LONG_PATH_CHECKOUT_REMEDIATION_LOCK_001

**Proves:** Classify and remediate the Windows long-path checkout blocker from the fresh-clone bootstrap proof.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WIX_LIGHT_FAILURE_DIAGNOSTIC_AND_REPAIR_LOCK_001

**Proves:** Diagnose the concrete WiX light.exe MSI linker failure and determine the next safe repair route.

**Does not prove:** Does not prove broad real-world repair coverage beyond the locked acceptance tests.

#### DETERMINEX_WORKSPACE_EVIDENCE_RECONCILIATION_LOCK_001

**Proves:** Reconcile the mixed Claude/Codex workspace and evidence state before preparing the first verified splash implementation path.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_WORKSPACE_EVIDENCE_RECONCILIATION_LOCK_002

**Proves:** Reconcile the combined workspace and evidence state after the Codex Idea Lab Python CLI verified splash demo and the Claude live React unified product shell.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### CI_LOCK_001

**Proves:** CI_LOCK_001

**Does not prove:** Does not prove all test paths run in CI. Only the paths listed in test.yml trigger; the filter may miss novel file locations.

#### CI_QUALITY_GATE_LOCK_001

**Proves:** CI_QUALITY_GATE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### CLAUDE_APPROVAL_REPLAY_AND_STALENESS_LOCK_001

**Proves:** Rung 3 of DETERMINEX_CLAUDE_IDE_AUTHORITY_AND_CLAIMS_HYGIENE_SERIES.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### CLAUDE_AUTHORITY_LEAK_REMEDIATION_FINAL_STATE_LOCK_001

**Proves:** Rung 9 (finale) of the Claude authority leak remediation campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### CLAUDE_AUTH_005_READY_AUTHORIZED_LANGUAGE_LOCK_001

**Proves:** Rung 1 of DETERMINEX_CLAUDE_IDE_AUTHORITY_AND_CLAIMS_HYGIENE_SERIES.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### CLAUDE_CONFIG_ROOT_ALLOWLIST_LOCK_001

**Proves:** Rung 5 of DETERMINEX_CLAUDE_IDE_AUTHORITY_AND_CLAIMS_HYGIENE_SERIES.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### CLAUDE_FRONTEND_AUTHORITY_VISUAL_AUDIT_LOCK_001

**Proves:** Rung 6 of DETERMINEX_CLAUDE_IDE_AUTHORITY_AND_CLAIMS_HYGIENE_SERIES.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### CLAUDE_IDE_HYGIENE_FINAL_STATE_LOCK_001

**Proves:** Rung 9 (finale) of DETERMINEX_CLAUDE_IDE_AUTHORITY_AND_CLAIMS_HYGIENE_SERIES.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### CLAUDE_LANE_LIVE_MODEL_READY_FINAL_STATE_LOCK_001

**Proves:** Campaign finale for the live-local-model work. Pins the equilibrium: live admission is opt-in local-only, network models blocked by default, diagnose-only and patch-plan and temp-patch verifier surfaces are READY, source mutation remains BLOCKED pending human approval, training eligibility blocked by default, NOT RELEASED. Next unblocker: REAL_LOCAL_MODEL_CONFIG_AND_HUMAN_APPROVAL_UI.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### CLAUDE_OPERATOR_IDENTITY_BOUNDING_LOCK_001

**Proves:** Rung 2 of DETERMINEX_CLAUDE_IDE_AUTHORITY_AND_CLAIMS_HYGIENE_SERIES.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### CLAUDE_PRE_APPLY_CONFIRMATION_PANEL_LOCK_001

**Proves:** Rung 4 of DETERMINEX_CLAUDE_IDE_AUTHORITY_AND_CLAIMS_HYGIENE_SERIES.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### CLAUDE_PROOF_BEFORE_MUTATION_DEMO_SCRIPT_LOCK_001

**Proves:** Rung 8 of DETERMINEX_CLAUDE_IDE_AUTHORITY_AND_CLAIMS_HYGIENE_SERIES.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### CLAUDE_PUBLIC_CLAIMS_LEDGER_LOCK_001

**Proves:** Rung 7 of DETERMINEX_CLAUDE_IDE_AUTHORITY_AND_CLAIMS_HYGIENE_SERIES.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### CLAUDE_REAL_MODEL_VERIFIER_READY_FINAL_STATE_LOCK_001

**Proves:** Campaign finale for REAL_LOCAL_MODEL_AVAILABLE_AND_BUILD_ADAPTER_VERIFIER_LOCK_SERIES.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### CLOAK_LOCK_001

**Proves:** CLOAK_LOCK_001

**Does not prove:** Does not prove zero leakage across all 10 languages — smoke tests cover Python only. Full multi-language privacy audit requires the B-Uncloaked clean rerun.

#### CLOAK_THREAT_MODEL_LOCK_001

**Proves:** CLOAK_THREAT_MODEL_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### CODEBASE_EXPLORER_SMOKE_LOCK_001

**Proves:** First test coverage for the largest untested module in the repo. Establishes a regression floor for the arbitrary-repo intake path. Does NOT redesign codebase_explorer — that is the next rung (BUILD_ADAPTER_REGISTRY_LOCK_001).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### CONFIG_SPINE_LOCK_001

**Proves:** CONFIG_SPINE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### CORPUS_COVERAGE_LOCK_001

**Proves:** CORPUS_COVERAGE_LOCK_001

**Does not prove:** Does not prove corpus balance, training effectiveness, or public benchmark dominance by itself.

#### CORPUS_ELIGIBILITY_REPAIR_TRACE_GUARD_LOCK_001

**Proves:** Rung 7 of the verified-repair campaign. The boundary between 'we ran this' and 'this teaches the model.' Pins the policy that no evidence produced under mocked / fixture conditions ever flows into training. Sets up LOCAL_MODEL_ADMISSION_POLICY (next rung) to start defeating the NO_LIVE_MODEL_CALL reason.

**Does not prove:** Does not prove corpus balance, training effectiveness, or public benchmark dominance by itself.

#### CORPUS_LICENSE_LOCK_001

**Proves:** CORPUS_LICENSE_LOCK_001

**Does not prove:** Does not prove corpus balance, training effectiveness, or public benchmark dominance by itself.

#### CORPUS_MIGRATION_LOCK_001

**Proves:** CORPUS_MIGRATION_LOCK_001

**Does not prove:** Does not prove v2/v3 migrations are correct (they are not yet written). Proves the registry rejects unknown versions and the v1 schema is stable.

#### CORPUS_SCHEMA_MATURITY_LOCK_001

**Proves:** Separate durable corpus integrity from schema-complete training eligibility.

**Does not prove:** Does not prove corpus balance, training effectiveness, or public benchmark dominance by itself.

#### CORPUS_WRITE_GUARD_LOCK_001

**Proves:** CORPUS_WRITE_GUARD_LOCK_001

**Does not prove:** Does not prove corpus balance, training effectiveness, or public benchmark dominance by itself.

#### DIAGNOSE_PROMPT_OPACITY_ENFORCEMENT_LOCK_001

**Proves:** Rung 6 of the Claude authority leak remediation campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DISTILLATION_LOCK_001

**Proves:** DISTILLATION_LOCK_001

**Does not prove:** Does not prove a deployed specialist model beats baseline without a later eval card.

#### EVIDENCE_IMMUTABILITY_GUARD_LOCK_001

**Proves:** EVIDENCE_IMMUTABILITY_GUARD_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### EVIDENCE_INDEX_LOCK_001

**Proves:** Generate a reproducible evidence index for every named lock and drain artifact before external preview packaging.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### FRONTEND_APPROVAL_PACKET_ROUNDTRIP_LOCK_001

**Proves:** Rung 7 of the Tauri-integrated frontend campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### FRONTEND_COMMAND_INVOKE_CLIENT_LOCK_001

**Proves:** Rung 2 of the Tauri-integrated frontend campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### FRONTEND_DIAGNOSE_AND_PATCH_PLAN_FLOW_LOCK_001

**Proves:** Rung 5 of the real frontend campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### FRONTEND_END_TO_END_REPAIR_FLOW_SMOKE_LOCK_001

**Proves:** Rung 11 of the real frontend campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### FRONTEND_EVIDENCE_VIEWER_LOCK_001

**Proves:** Rung 9 of the real frontend campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### FRONTEND_HUMAN_APPROVAL_PANEL_LOCK_001

**Proves:** Rung 7 of the real frontend campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### FRONTEND_LIVE_DIAGNOSE_OPT_IN_SMOKE_LOCK_001

**Proves:** Rung 6 of the Tauri-integrated frontend campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### FRONTEND_MODEL_ROUTE_PANEL_LOCK_001

**Proves:** Rung 4 of the real frontend campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### FRONTEND_PANEL_COMMAND_WIRING_LOCK_001

**Proves:** Rung 3 of the Tauri-integrated frontend campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### FRONTEND_QUALITY_RAILS_LOCK_001

**Proves:** FRONTEND_QUALITY_RAILS_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### FRONTEND_REAL_FLOW_E2E_LOCK_001

**Proves:** Rung 8 of the Tauri-integrated frontend campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### FRONTEND_REPAIR_PANEL_SHELL_LOCK_001

**Proves:** Rung 2 of the real frontend campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### FRONTEND_SOURCE_APPLY_DRY_RUN_PANEL_LOCK_001

**Proves:** Rung 8 of the real frontend campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### FRONTEND_TEMP_VERIFY_PANEL_LOCK_001

**Proves:** Rung 6 of the real frontend campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### FRONTEND_WORKSPACE_STATUS_PANEL_LOCK_001

**Proves:** Rung 3 of the real frontend campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### GO_REPAIR_LOCK_001

**Proves:** GO_REPAIR_LOCK_001

**Does not prove:** Does not prove broad real-world repair coverage beyond the locked acceptance tests.

#### HARDENED_INTAKE_EXECUTION_RUNNER_LOCK_001

**Proves:** Rung 5 of the post-audit Claude-lane sequence. Consumes the MUST_MIGRATE target list from PARALLEL_EXECUTION_LAYER_AUDIT_LOCK_001 (rung 4). After this rung, arbitrary-repo intake CANNOT accidentally invoke shell=True, escape the workspace, invoke Docker, or run with code-injection env vars present. The repair-pipeline migration is the explicit target of a follow-up rung.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### HARDENED_REPAIR_PIPELINE_EXECUTORS_LOCK_001

**Proves:** Rung 6 of the post-audit Claude-lane sequence. Consumes the deferred-by-design 5 sites from HARDENED_INTAKE_EXECUTION_RUNNER_LOCK_001 so the next rung (ARCH_GAUNTLET_CI_LOCK_001) can wire the architecture gauntlet into CI with a clean must-migrate=0 / blocked-unsafe=0 baseline.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### HARDENED_VERIFIED_TASK_AND_CODECLASH_LOCK_001

**Proves:** Rung 9 of the post-audit Claude-lane sequence. Seals the two safety findings surfaced by the rung-8 classification sweep. After this rung lands, the Claude lane is at the cleanest possible state for MODEL_ROUTER_LOCK_001 work to begin.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### HIVE_LOCK_001

**Proves:** HIVE_LOCK_001

**Does not prove:** Does not prove end-to-end session correctness at scale. Tests cover DAG, WAL, and workspace isolation primitives. Full session tests require live compilers.

#### HUMAN_APPROVAL_PACKET_UI_MODEL_LOCK_001

**Proves:** Rung 6 of the IDE consumer campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### HUMAN_APPROVAL_SOURCE_MUTATION_GATE_LOCK_001

**Proves:** Rung 5 of the verified-repair campaign. Pins the invariant that source mutation remains BLOCKED by default and can only be opened by a packet that references an exactly-matching verified trace. The next rungs (IDE state model, corpus guard, local model admission, readiness matrix, final state) compose against this gate; nothing in the apparatus ever writes to the user's original repo without a downstream consumer producing an ACCEPTED decision first.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### IDE_APPROVAL_UX_COPY_LOCK_001

**Proves:** Rung 10 of the IDE frontend/approval campaign. The apparatus must not encourage blind approval.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### IDE_BACKEND_COMMAND_SURFACE_LOCK_001

**Proves:** Rung 7 of the IDE consumer campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### IDE_CONSUMER_FLOW_TRACE_LOCK_001

**Proves:** Rung 9 of the IDE consumer campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### IDE_DIAGNOSE_FLOW_LOCK_001

**Proves:** Rung 3 of the IDE frontend/approval campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### IDE_END_TO_END_UI_FLOW_TRACE_LOCK_001

**Proves:** Rung 11 of the IDE frontend/approval campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### IDE_FRONTEND_STATE_CONTRACT_LOCK_001

**Proves:** Rung 9 of the IDE frontend/approval campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### IDE_HUMAN_APPROVAL_SIGNING_FLOW_LOCK_001

**Proves:** Rung 6 of the IDE frontend/approval campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### IDE_LIVE_MODEL_REPAIR_FLOW_STATE_LOCK_001

**Proves:** Rung 6 of the live-local-model campaign. Exposes the live-model repair flow state to the IDE backend without building UI. Sets up CLAUDE_LANE_LIVE_MODEL_READY_FINAL_STATE_LOCK_001 (the campaign finale).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### IDE_MODEL_ROUTE_PANEL_LOCK_001

**Proves:** Rung 2 of the IDE frontend/approval campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### IDE_PATCH_PLAN_FLOW_LOCK_001

**Proves:** Rung 4 of the IDE frontend/approval campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### IDE_REPAIR_STATE_MODEL_LOCK_001

**Proves:** Rung 6 of the verified-repair campaign. Decouples the frontend from the internals of the four prior rungs: an IDE can consume a single JSON record and render the current state without touching trace internals. Sets up DETERMINEX_IDE_BACKEND_FINAL_STATE_LOCK_001 (the campaign-finale rung) to roll up the full backend state into a single packet.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### IDE_SOURCE_APPLY_GATE_FLOW_LOCK_001

**Proves:** Rung 7 of the IDE frontend/approval campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### IDE_TEMP_VERIFY_FLOW_LOCK_001

**Proves:** Rung 5 of the IDE frontend/approval campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### IDE_WORKSPACE_OPEN_FLOW_LOCK_001

**Proves:** Rung 1 of the IDE frontend/approval campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### JAVA_CORPUS_LOCK_001

**Proves:** JAVA_CORPUS_LOCK_001

**Does not prove:** Does not prove corpus balance, training effectiveness, or public benchmark dominance by itself.

#### JAVA_REPAIR_LOCK_001

**Proves:** JAVA_REPAIR_LOCK_001

**Does not prove:** Does not prove broad real-world repair coverage beyond the locked acceptance tests.

#### LEGACY_CORPUS_RECOVERY_LOCK_001

**Proves:** Exploit quarantined legacy corpus as mined evidence, replay planning, and failure taxonomy without promoting dirty rows into training.

**Does not prove:** Does not prove corpus balance, training effectiveness, or public benchmark dominance by itself.

#### LEGACY_REPLAY_PROMOTION_LOCK_001

**Proves:** Prove quarantined legacy replay candidates can produce new signed active_training_eligible rows only after fresh verifier evidence, without mutating the legacy source.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### LIVE_MODEL_DIAGNOSE_ONLY_TRACE_LOCK_001

**Proves:** Rung 3 of the live-local-model campaign. Opens the smallest live-model surface (diagnosis) without giving the model any patching authority. Sets up LIVE_MODEL_PATCH_PLAN_QUARANTINE_LOCK_001 to extend the surface to patch *plans* (still untrusted).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### LIVE_MODEL_MOCK_COMPATIBILITY_HARNESS_LOCK_001

**Proves:** Rung 2 of the live-local-model campaign. Proves the model-call interface is structurally compatible with the repair apparatus without trusting any real provider.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### LIVE_MODEL_PATCH_PLAN_QUARANTINE_LOCK_001

**Proves:** Rung 4 of the live-local-model campaign. Extends the live-model surface to patch plans while keeping the actual application gated. Sets up LIVE_MODEL_TEMP_PATCH_VERIFIER_GATE_LOCK_001 to consume quarantined plans and apply them to temp workspaces only.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### LIVE_MODEL_TEMP_PATCH_VERIFIER_GATE_LOCK_001

**Proves:** Rung 5 of the live-local-model campaign. Closes the loop from quarantined plan → temp-applied + verified. Sets up IDE_LIVE_MODEL_REPAIR_FLOW_STATE_LOCK_001 to expose this state to the frontend.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### LLM_MOCKED_INTAKE_REPAIR_LOCK_001

**Proves:** Rung 2 of the verified-repair campaign. Proves the apparatus *shape* end-to-end without trusting a live model. The next rungs (SAFE_PATCH_DIFF_ROLLBACK, VERIFIED_REPAIR_TRACE) will replace the canned patch with a temp-workspace application and a fully signed trace; this rung pins the seams.

**Does not prove:** Does not prove broad real-world repair coverage beyond the locked acceptance tests.

#### LOCAL_LEGACY_CORPUS_QUARANTINE_LOCK_001

**Proves:** Prevent unsigned/malformed local ProgramBench legacy rows from being confused with the active signed T: corpus or future training-eligible data.

**Does not prove:** Does not prove corpus balance, training effectiveness, or public benchmark dominance by itself.

#### LOCAL_MODEL_ADMISSION_POLICY_LOCK_001

**Proves:** Rung 8 of the verified-repair campaign. Closes the policy-shape gap for the BLOCKED_NO_LIVE_MODEL_CALL reason in CORPUS_ELIGIBILITY_REPAIR_TRACE_GUARD_LOCK_001 — by spelling out exactly what a candidate would have to declare to be admissible, without yet doing the admission. The metadata-only admission is a precursor: a future LOCAL_MODEL_LIVE_ADMISSION rung would consume METADATA_ADMITTED decisions and attempt a probe.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### LOCAL_MODEL_CONFIG_WIZARD_LOCK_001

**Proves:** Rung 1 of the IDE consumer campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### LOCAL_MODEL_LIVE_ADMISSION_LOCK_001

**Proves:** First rung of the live-local-model campaign. Defeats the BLOCKED_NO_LIVE_MODEL_CALL reason in the corpus eligibility guard for opt-in callers, while keeping every other safety default closed. Sets up LIVE_MODEL_MOCK_COMPATIBILITY_HARNESS_LOCK_001 to exercise the live-model interface against fixture providers.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### LOCAL_MODEL_SETTINGS_PANEL_LOCK_001

**Proves:** Rung 10 of the real frontend campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### LOCAL_PROVIDER_SMOKE_TEST_LOCK_001

**Proves:** Rung 2 of the IDE consumer campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### MODEL_ADMISSION_NO_BYPASS_LOCK_001

**Proves:** Rung 4 of the Claude authority leak remediation campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### MODEL_ROUTER_LOCK_001

**Proves:** Rung 10 of the post-audit Claude-lane sequence. With BLOCKED_UNSAFE=0, MUST_MIGRATE=0, UNKNOWN=0, PROGRAMBENCH=56 preserved, and the architecture gauntlet wired into CI, the apparatus is at the cleanest possible state to start *deciding* when a model is allowed to participate. The router is the gatekeeper that the next rungs (LLM_MOCKED_INTAKE_REPAIR_LOCK_001, SAFE_PATCH_DIFF_ROLLBACK_LOCK_001, VERIFIED_REPAIR_TRACE_LOCK_001) will compose against. Also cleans up the stale v10/v5 default ids in scripts/codebase_explorer.py lines 58-59 surfaced during the gap-to-100 audit.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### NATIVE_C_CPP_REPAIR_LOCK_001

**Proves:** NATIVE_C_CPP_REPAIR_LOCK_001

**Does not prove:** Does not prove broad real-world repair coverage beyond the locked acceptance tests.

#### NO_LOOSE_BENCH_ARTIFACTS_LOCK_001

**Proves:** Ensure benchmark outputs resolve into a corpus-visible status instead of becoming orphan eval JSON, logs, shards, or local-only accept/reject artifacts.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### OBSERVABILITY_LOCK_001

**Proves:** OBSERVABILITY_LOCK_001

**Does not prove:** Does not prove event consumers exist. Proves the emitter works correctly and is fail-silent. UI / tail tooling is a future surface.

#### OLLAMA_LOCAL_PROVIDER_SMOKE_LOCK_001

**Proves:** Rung 5 of the Tauri-integrated frontend campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### OLLAMA_MODEL_PULL_OPERATOR_GUIDE_LOCK_001

**Proves:** Rung 2 of the real-model + build-adapter-verifier campaign (subordinate to Codex audit repair).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### OPT_IN_LIVE_DIAGNOSE_COMMAND_LOCK_001

**Proves:** Rung 3 of the IDE consumer campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### OPT_IN_PATCH_PLAN_COMMAND_LOCK_001

**Proves:** Rung 4 of the IDE consumer campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PARALLEL_EXECUTION_LAYER_AUDIT_LOCK_001

**Proves:** Rung 4 of the post-audit Claude-lane sequence. Closes the gap-to-100 audit's hidden-assumption #3 ('parallel execution layers; only one hardened'). The output is the target list for HARDENED_INTAKE_EXECUTION_RUNNER_LOCK_001 (the next rung). Audit is intentionally read-only: never executes a discovered command, never mutates source or signed evidence, never imports the scanned modules.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PATH_PORTABILITY_LOCK_001

**Proves:** PATH_PORTABILITY_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### POST_APPLY_VERIFIER_LOCK_001

**Proves:** Rung 9 of the real repair flow campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### POST_APPLY_VERIFIER_NO_DEFAULT_PASS_LOCK_001

**Proves:** Rung 3 of the Claude authority leak remediation campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_ALTERNATE_CLEANROOM_IMAGE_PROVENANCE_LOCK_001

**Proves:** Determine whether a safer provenance-admissible alternate Doxygen cleanroom image path exists without pulling, hydrating, rebuilding, executing Docker, or running ProgramBench.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_APPROVED_SCANNER_SETUP_LOCK_001

**Proves:** Configure or admit an approved scanner installation path before cleanroom image scanning can be retried.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_ARTIFACT_IMPORT_OPERATOR_GUIDE_LOCK_001

**Proves:** Write an operator-facing guide and machine-readable checklist for supplying exact artifact import provenance for the 10 Batch001 metadata-admitted ProgramBench targets.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_ARTIFACT_SOURCE_ESCALATION_LOCK_001

**Proves:** Generate a precise operator checklist when ProgramBench cleanroom image provenance is missing and block hydration until real provenance is supplied.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_BATCH001_ARTIFACT_IMPORT_PREFLIGHT_LOCK_001

**Proves:** Determine whether exact-digest artifact import is locally supported and authorized without execution.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_BATCH001_ARTIFACT_IMPORT_REQUEST_PACKET_LOCK_001

**Proves:** Generate exact artifact import request packets for ten Batch001 images with metadata-only digest admission.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_BATCH001_EXACT_ARTIFACT_IMPORT_GATE_LOCK_001

**Proves:** Create the gate that can accept or reject exact imported artifact evidence for the ten Batch001 targets.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_BATCH001_EXACT_MANIFEST_METADATA_PLAN_LOCK_001

**Proves:** Create a per-target exact DockerHub manifest metadata plan for derived Batch001 image names without searching, pulling, or running.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_BATCH001_IMAGE_NAME_DERIVATION_LOCK_001

**Proves:** Derive expected official ProgramBench task_cleanroom image names for top Batch001 metadata-only targets using the established owner__repo.sha naming rule.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_BATCH001_IMPORT_SCAN_CAMPAIGN_FINAL_STATE_LOCK_001

**Proves:** Write final state for the Batch001 import/scan planning campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_BATCH001_IMPORT_SCAN_PLANNING_LOCK_001

**Proves:** Write non-executing import and scan requirements for Batch001 targets with metadata-only digest admission.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_BATCH001_LIVE_MANIFEST_METADATA_LOOKUP_LOCK_001

**Proves:** Use the safe registry manifest client to perform exact metadata-only DockerHub manifest lookup for ten derived Batch001 ProgramBench image references.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_BATCH001_LOOKUP_CAMPAIGN_FINAL_STATE_LOCK_001

**Proves:** Write final state for the Batch001 safe manifest lookup campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_BATCH001_MANIFEST_DIGEST_ADMISSION_LOCK_001

**Proves:** Admit exact manifest digests as metadata-only artifact evidence where safe lookup found digests.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_BATCH001_METADATA_CAMPAIGN_FINAL_STATE_LOCK_001

**Proves:** Write final state for the Batch001 metadata campaign after derivation, exact lookup planning, safe lookup support check, digest admission, refreshes, and scan requirements.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_BATCH001_METADATA_DIGEST_ADMISSION_FROM_LIVE_LOOKUP_LOCK_001

**Proves:** Admit exact manifest digests found by live lookup as metadata-only ProgramBench artifact authority.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_BATCH001_METADATA_RECOVERY_QUEUE_LOCK_001

**Proves:** Build a Batch 001 metadata and provenance recovery queue from current evidence.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_BATCH001_METADATA_STATE_REFRESH_LOCK_001

**Proves:** Refresh Batch001 metadata state after derivation, manifest lookup, and digest admission.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_BATCH001_OPERATOR_ACTION_REFRESH_LOCK_001

**Proves:** Refresh Batch001 operator actions after metadata derivation and digest admission results.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_BATCH001_OPERATOR_ARTIFACT_IMPORT_PACKET_BUNDLE_LOCK_001

**Proves:** Generate operator packet templates for supplying exact artifact tars for Batch001 metadata-admitted targets.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_BATCH001_OPERATOR_PACKET_BUNDLE_LOCK_001

**Proves:** Generate Batch 001 operator packet template bundle for current next actions.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_BATCH001_OPERATOR_PACKET_REFRESH_AFTER_LOOKUP_LOCK_001

**Proves:** Refresh operator packet needs after Batch001 live manifest lookup and metadata-only digest admission.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_BATCH001_POST_LOOKUP_STATE_REFRESH_LOCK_001

**Proves:** Refresh Batch001 state after live manifest lookup and metadata-only digest admission.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_BATCH001_SAFE_MANIFEST_LOOKUP_LOCK_001

**Proves:** Determine whether existing policy and code support exact metadata-only manifest lookup for derived Batch001 image names.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_BATCH001_SCAN_POLICY_PRECHECK_LOCK_001

**Proves:** Define Batch001 scan policy thresholds and routing before any artifact scan is performed.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_BATCH001_SCAN_QUEUE_LOCK_001

**Proves:** Create a scan queue for Batch001 targets with metadata-only digests and pending artifact import requirements.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_BATCH001_SCAN_REQUIREMENTS_QUEUE_LOCK_001

**Proves:** Generate scan/import requirements for Batch001 targets with admitted metadata digests before any execution.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_BATCH001_STATE_AGGREGATOR_LOCK_001

**Proves:** Aggregate known Batch 001 and Doxygen ProgramBench state into the common instance schema.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_BATCH001_UNBLOCK_PRIORITY_LOCK_001

**Proves:** Rank known Batch001 ProgramBench instances by easiest safe path to real runnable evidence using existing evidence only.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_BATCH001_UNBLOCK_PRIORITY_REFRESH_LOCK_001

**Proves:** Recompute Batch001 unblock priority after metadata derivation and attempted manifest/digest admission.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_BATCH001_UNBLOCK_SIMULATION_LOCK_001

**Proves:** Dry-run what would change if specific operator packets were supplied.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_BATCH_SKIP_DECISION_LOCK_001

**Proves:** Apply the skip reason taxonomy to all known Batch 001 and Doxygen ProgramBench rows.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_BOUNDED_RERUN_EXECUTION_LOCK_001

**Proves:** Only execute ProgramBench reruns authorized by a ROOT_CAUSE_PACKET_READY packet, and only within the exact bounded rerun_scope.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_CAMPAIGN_REPORTING_API_LOCK_001

**Proves:** Create a read-only deterministic ProgramBench campaign reporting API.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_CAMPAIGN_STATUS_BOARD_LOCK_001

**Proves:** Produce a machine-readable ProgramBench campaign status board without executing any task.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_CLEANROOM_BUILD_RECIPE_PROVENANCE_GAP_LOCK_001

**Proves:** Turn quarantine-only Doxygen cleanroom build recipe reconstruction into a signed provenance-gap packet before any rebuild, hydration, execution, or ProgramBench rerun can be considered.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_CLEANROOM_BUILD_RECIPE_RECOVERY_LOCK_001

**Proves:** Recover or reconstruct the Doxygen cleanroom image build recipe from local evidence only, without rebuilding, pulling, hydrating, executing Docker, or rerunning ProgramBench.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_CLEANROOM_IMAGE_HYDRATION_LOCK_001

**Proves:** Hydrate an admitted ProgramBench cleanroom image into quarantine/cache only after digest verification, scan pass, and policy admission, while still refusing execution and training promotion.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_CLEANROOM_IMAGE_IMPORT_LOCK_001

**Proves:** Import only exact digest-pinned ProgramBench cleanroom image artifacts into quarantine, verify digest provenance, require scan evidence, and still refuse execution and training promotion.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_CLEANROOM_IMAGE_REMEDIATION_PLAN_LOCK_001

**Proves:** Plan a reproducible remediation or safer-equivalent-image path for the Doxygen cleanroom image without rebuilding, hydrating, executing, or rerunning ProgramBench.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_CLEANROOM_IMAGE_SCANNER_ADMISSION_LOCK_001

**Proves:** Admit approved cleanroom image scanners by identity, version, and non-executing archive-scan capability before the scan gate may use them.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_CLEANROOM_IMAGE_SCAN_LOCK_001

**Proves:** Produce signed scan evidence for quarantined ProgramBench cleanroom image artifacts, or fail closed with signed scanner-unavailable evidence when no approved scanner exists.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_CLEANROOM_IMAGE_SCAN_TRIAGE_LOCK_001

**Proves:** Triage signed Trivy scan findings for the Doxygen cleanroom image into actionable remediation, alternate-source, or review categories before any policy exception or rerun.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_CLEANROOM_RECIPE_PROVENANCE_RECOVERY_LOCK_001

**Proves:** Attempt to close Doxygen cleanroom recipe provenance gaps by finding exact original recipe provenance and pinned base-image digest evidence without rebuilding, pulling, hydrating, executing Docker, or rerunning ProgramBench.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_CODEX_LANE_FINAL_STATE_LOCK_001

**Proves:** Write the final machine-checkable Codex ProgramBench platform lane state.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_CODEX_OPERATOR_READY_FINAL_STATE_LOCK_001

**Proves:** Write the final operator-ready ProgramBench Codex lane state.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_COMMIT_PROVENANCE_REPAIR_AUDIT_LOCK_001

**Proves:** Audit the mixed frontend-labeled commit that contains ProgramBench Batch001 import/scan planning artifacts and confirm the ProgramBench evidence chain remains self-contained and non-authorizing.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_DOCKERHUB_MANIFEST_PROVENANCE_LOCK_001

**Proves:** Convert exact Docker Hub manifest metadata for a missing ProgramBench cleanroom image into a signed provenance candidate without pulling layers or executing the image.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_DOXYGEN_LANE_FINAL_STATE_LOCK_001

**Proves:** Write the final machine-checkable Doxygen cleanroom lane state after the Codex non-executing security campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_EVIDENCE_GRAPH_INTEGRITY_GUARD_LOCK_001

**Proves:** Harden the ProgramBench evidence graph against invalid authorization paths.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_EVIDENCE_GRAPH_LOCK_001

**Proves:** Build a machine-readable ProgramBench evidence graph linking state, blockers, actions, and denials.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_EXACT_PROVIDER_PROBE_PLAN_LOCK_001

**Proves:** Create a non-executing exact-provider probe plan for missing Batch 001 images.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_GENERIC_EXECUTION_PREFLIGHT_LOCK_001

**Proves:** Generalize execution preflight for ProgramBench official artifact reruns.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_GENERIC_OPERATOR_POLICY_ADMISSION_LOCK_001

**Proves:** Generalize operator policy admission for scan-failed ProgramBench artifacts.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_INFRA_FAILURE_TRIAGE_LOCK_001

**Proves:** Convert ProgramBench real bounded rerun infrastructure failures into deterministic recovery records without unsafe pulls, guessed execution, or broad online search.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_INSTANCE_STATE_SCHEMA_LOCK_001

**Proves:** Create a common machine-readable ProgramBench instance state schema.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_NEXT_UNBLOCK_DECISION_LOCK_001

**Proves:** Choose the next ProgramBench unblock path without executing, importing, scanning, approving, or writing training rows.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_OFFICIAL_ARTIFACT_EXECUTION_PREFLIGHT_LOCK_001

**Proves:** Preflight official Doxygen artifact execution prerequisites without running Docker or ProgramBench.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_OFFICIAL_ARTIFACT_SANDBOX_REQUIREMENTS_LOCK_001

**Proves:** Define exact non-executing sandbox requirements for any future Doxygen official upstream ProgramBench artifact run while preserving the current scan-failed execution block.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_OFFICIAL_ARTIFACT_SECURITY_DECISION_LOCK_001

**Proves:** Decide the Doxygen official upstream ProgramBench artifact security posture after authority recheck without granting policy exceptions, stronger sandbox approval, Docker execution, ProgramBench rerun, cache readiness, or training eligibility.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_ONLINE_ARTIFACT_DISCOVERY_LOCK_001

**Proves:** Add a discovery-only online artifact lane for missing ProgramBench replay images and artifacts without trusting online sources by default.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_ONLINE_PROVIDER_REGISTRY_LOCK_001

**Proves:** Constrain online artifact discovery to allowlisted providers and exact reference modes before any provider search can be wired.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_OPERATOR_ACTION_QUEUE_LOCK_001

**Proves:** Generate a non-executing operator action queue from ProgramBench batch state and skip decisions.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_OPERATOR_ARTIFACT_ADMISSION_LOCK_001

**Proves:** Allow an operator to supply exact artifact provenance for a ProgramBench missing cleanroom image while preventing hydration, execution, or training promotion.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_OPERATOR_CLI_LOCK_001

**Proves:** Add a read-only operator-facing CLI for ProgramBench status, actions, packets, inbox scans, simulations, and graph views.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_OPERATOR_INBOX_SCANNER_LOCK_001

**Proves:** Scan local ProgramBench operator inbox packets and validate them without mutation or approval.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_OPERATOR_OUTBOX_LOCK_001

**Proves:** Generate an operator outbox of fillable ProgramBench packet templates.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_OPERATOR_PACKET_ADMISSION_LIVE_PACKET_REVIEW_LOCK_001

**Proves:** Review ProgramBench operator inbox packets after the operator-ready prerequisites exist, without granting approval or executing anything.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_OPERATOR_PACKET_ADMISSION_PROCESSING_LOCK_001

**Proves:** Process validated ProgramBench operator inbox packets into non-executing gate-review routes.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_OPERATOR_PACKET_ADMISSION_ROUTER_LOCK_001

**Proves:** Route validated operator packets to the correct non-executing admission path.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_OPERATOR_PACKET_TEMPLATES_LOCK_001

**Proves:** Generate reusable operator packet templates for ProgramBench human-supplied evidence without creating approvals.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_OPERATOR_PACKET_VALIDATOR_LOCK_001

**Proves:** Validate operator-supplied ProgramBench packets without granting execution.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_OPERATOR_PROVENANCE_REQUEST_PACKET_LOCK_001

**Proves:** Generate a signed operator-facing provenance request packet that states exactly what external evidence is required before Doxygen cleanroom image rebuild authority can be considered.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_OPERATOR_READY_AUDIT_LOCK_001

**Proves:** Audit the ProgramBench operator-ready lane for consistency, stale references, and accidental authority escalation without advancing to live gate review.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_PLATFORM_COMPLETION_SCORECARD_LOCK_001

**Proves:** Score Codex ProgramBench platform completion without inflating blocked dimensions.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_REAL_BOUNDED_RERUN_LOCK_001

**Proves:** Execute exactly one live ProgramBench rerun from one still-valid authorized packet, then record the outcome as signed eval evidence.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_REBUILD_PROVENANCE_QUARANTINE_DECISION_LOCK_001

**Proves:** Convert partial Doxygen cleanroom recipe provenance recovery into a signed quarantine decision that distinguishes technical remediation possibility from benchmark-faithful rebuild authority.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_REPLAY_HYDRATION_LOCK_001

**Proves:** Preflight selected legacy ProgramBench replay candidates by locating task root, candidate root, task image, eval harness, baseline artifact, eval command, expected result path, language guess, and workspace checksum before replay execution.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_REPLAY_IMAGE_HYDRATION_LOCK_001

**Proves:** Resolve ProgramBench replay task images or explicit local no-image verifier mode before replay execution.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_REPLAY_METADATA_RECOVERY_LOCK_001

**Proves:** Recover or reconstruct ProgramBench replay metadata for Batch 001 candidates without executing guessed metadata.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_REPLAY_VERIFIER_LOCK_001

**Proves:** Take selected legacy ProgramBench replay candidates, reconstruct/hydrate replay context, run a fresh verifier through an injectable runner, and emit exactly one signed outcome row per candidate.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_RERUN_READINESS_MATRIX_LOCK_001

**Proves:** Write the operator-facing ProgramBench rerun readiness matrix without executing anything.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_ROOT_CAUSE_PACKET_LOCK_001

**Proves:** Fresh ProgramBench reruns require a structured root-cause packet before any drain attempt.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_ROOT_DISAMBIGUATION_LOCK_001

**Proves:** Given multiple local roots for a ProgramBench tool, select the canonical runnable root using deterministic precedence and evidence-backed manual overrides.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_SAFE_REGISTRY_MANIFEST_CLIENT_LOCK_001

**Proves:** Implement an exact-reference, metadata-only Docker Registry manifest client for admitted ProgramBench DockerHub image references.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_SECURITY_POLICY_ADMISSION_GATE_LOCK_001

**Proves:** Create the gate for operator-supplied security policy admission, while recording that no real live approval exists.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_SECURITY_POLICY_EXCEPTION_REQUEST_LOCK_001

**Proves:** Write a signed operator policy-exception request packet for the scan-failed official Doxygen artifact without granting an exception.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_SKIP_REASON_TAXONOMY_LOCK_001

**Proves:** Create a generic skip/block taxonomy for ProgramBench infrastructure, security, and provenance blockers.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_TASK_ROOT_RESOLUTION_LOCK_001

**Proves:** Map legacy candidate/tool/cluster metadata to concrete ProgramBench task roots, source roots, or benchmark fixture roots before hydration and replay execution.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_TASK_SKIP_WITH_PROVENANCE_REASON_LOCK_001

**Proves:** Write a signed Doxygen skip decision caused by required policy admission, without classifying it as model failure, benchmark failure, or training data.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_TRAINING_ELIGIBILITY_NEGATIVE_GUARD_LOCK_001

**Proves:** Harden the rule that metadata-only, scan-failed, policy-required, skipped, and partial-provenance Doxygen records cannot become training rows.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_UPSTREAM_ARTIFACT_AUTHORITY_RECHECK_LOCK_001

**Proves:** Reconcile Doxygen ProgramBench task_cleanroom upstream artifact authority with Determinex's separate rebuild, remediation, execution-security, cache-readiness, and training-eligibility gates without running Docker or ProgramBench.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PYTHON_REPAIR_LOCK_001

**Proves:** PYTHON_REPAIR_LOCK_001

**Does not prove:** Does not prove broad real-world repair coverage beyond the locked acceptance tests.

#### REAL_APPROVAL_APPLY_POST_VERIFY_TRACE_LOCK_001

**Proves:** Rung 8 of the real-model + build-adapter-verifier campaign (subordinate to Codex audit repair).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### REAL_APPROVAL_DIFF_BODY_CONTENT_BINDING_LOCK_001

**Proves:** Rung 1 of the Claude authority leak remediation campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### REAL_BUILD_ADAPTER_TEMP_VERIFY_TRACE_LOCK_001

**Proves:** Rung 7 of the real-model + build-adapter-verifier campaign (subordinate to Codex audit repair).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### REAL_HUMAN_APPROVAL_ADMISSION_LOCK_001

**Proves:** Rung 6 of the real repair flow campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### REAL_LIVE_DIAGNOSE_ONLY_LOCK_001

**Proves:** Rung 3 of the real repair flow campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### REAL_LOCAL_MODEL_ADMISSION_LOCK_001

**Proves:** Rung 2 of the real repair flow campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### REAL_LOCAL_MODEL_HEALTHCHECK_LOCK_001

**Proves:** Rung 3 of the real-model + build-adapter-verifier campaign (subordinate to Codex audit repair).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### REAL_LOCAL_MODEL_PROVIDER_CONFIG_LOCK_001

**Proves:** Rung 4 of the Tauri-integrated frontend campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### REAL_MODEL_DIAGNOSE_WITH_BUILD_VERIFIER_LOCK_001

**Proves:** Rung 5 of the real-model + build-adapter-verifier campaign (subordinate to Codex audit repair).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### REAL_MODEL_PATCH_PLAN_WITH_VERIFIER_CONTEXT_LOCK_001

**Proves:** Rung 6 of the real-model + build-adapter-verifier campaign (subordinate to Codex audit repair).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### REAL_OLLAMA_PROVIDER_DETECTION_LOCK_001

**Proves:** Rung 1 of the real repair flow campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### REAL_PATCH_PLAN_QUARANTINE_LOCK_001

**Proves:** Rung 4 of the real repair flow campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### REAL_REPAIR_FLOW_FINAL_STATE_LOCK_001

**Proves:** Campaign finale for the real local-model + real human-approval source-apply path.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### REAL_TEMP_PATCH_VERIFY_LOCK_001

**Proves:** Rung 5 of the real repair flow campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### REPRODUCIBLE_DEV_LOCK_001

**Proves:** REPRODUCIBLE_DEV_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### ROLLBACK_SYMLINK_SEMANTICS_LOCK_001

**Proves:** Rung 8 of the Claude authority leak remediation campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### ROSETTA_LOCK_001

**Proves:** ROSETTA_LOCK_001

**Does not prove:** Smoke tests cover the pure-Python layer only (no PyTorch). Projection accuracy and semantic preservation tests require rosetta_v1.pt and GPU.

#### RUST_REPAIR_LOCK_001

**Proves:** RUST_REPAIR_LOCK_001

**Does not prove:** Does not prove broad real-world repair coverage beyond the locked acceptance tests.

#### SAFE_PATCH_DIFF_ROLLBACK_LOCK_001

**Proves:** Rung 3 of the verified-repair campaign. Gives the apparatus a bounded surface for *applying* a candidate patch without ever touching the user's repo. Sets up VERIFIED_REPAIR_TRACE_LOCK_001 to compose a real verifier on top, and HUMAN_APPROVAL_SOURCE_MUTATION_GATE_LOCK_001 to gate the eventual original-repo write.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### SCRIPT_HELPER_EXECUTION_CLASSIFICATION_SWEEP_LOCK_001

**Proves:** Rung 8 of the post-audit Claude-lane sequence. Per directive: 'before routing models or allowing broader repair orchestration, Claude needs to know which helper scripts are harmless read-only orchestration, which are already sandboxed, which belong to Codex, and which must migrate.' This rung closes that triage gap. Migration of the 1 MUST_MIGRATE site and the 1 BLOCKED_UNSAFE file is the next rung's scope; this rung is classification only.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### SENTINEL_LOCK_001

**Proves:** SENTINEL_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### SOURCE_MUTATION_APPLY_AFTER_APPROVAL_LOCK_001

**Proves:** Rung 8 of the real repair flow campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### SOURCE_MUTATION_APPLY_DRY_RUN_LOCK_001

**Proves:** Rung 8 of the IDE consumer campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### SOURCE_MUTATION_ROLLBACK_EXECUTION_LOCK_001

**Proves:** Rung 10 of the real repair flow campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### SOURCE_MUTATION_ROLLBACK_SNAPSHOT_LOCK_001

**Proves:** Rung 7 of the real repair flow campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### SQL_ORACLE_LOCK_001

**Proves:** SQL_ORACLE_LOCK_001

**Does not prove:** Does not prove broad real-world repair coverage beyond the locked acceptance tests.

#### STORAGE_OPERATIONS_LOCK_001

**Proves:** STORAGE_OPERATIONS_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### SUPPLY_CHAIN_LOCK_001

**Proves:** SUPPLY_CHAIN_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### TAURI_BACKEND_COMMAND_BRIDGE_LOCK_001

**Proves:** Rung 8 of the IDE frontend/approval campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### TAURI_COMMAND_VERB_ALIGNMENT_LOCK_001

**Proves:** Rung 5 of the Claude authority leak remediation campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### TAURI_LIB_RS_COMMAND_WIRING_LOCK_001

**Proves:** Rung 1 of the Tauri-integrated frontend campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### TAURI_RUST_COMMAND_BRIDGE_LOCK_001

**Proves:** Rung 1 of the real frontend campaign. Produces the Rust seam without touching the frontend team's wire-up.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### TEMP_PATCH_VERIFY_COMMAND_LOCK_001

**Proves:** Rung 5 of the IDE consumer campaign.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### TRAINING_CORPUS_DASHBOARD_LOCK_001

**Proves:** Track active_training_eligible corpus growth separately from active_eval_evidence so corpus maturity cannot be hidden by signed row volume.

**Does not prove:** Does not prove corpus balance, training effectiveness, or public benchmark dominance by itself.

#### TYPESCRIPT_REPAIR_LOCK_001

**Proves:** TYPESCRIPT_REPAIR_LOCK_001

**Does not prove:** Does not prove broad real-world repair coverage beyond the locked acceptance tests.

#### VERIFIED_REPAIR_TRACE_LOCK_001

**Proves:** Rung 4 of the verified-repair campaign. This is the apparatus proof — the moment the four pillars compose cleanly. Sets up HUMAN_APPROVAL_SOURCE_MUTATION_GATE_LOCK_001 (the next rung) to gate the eventual original-repo write against a trace_id + diff hash + verifier-passed evidence packet.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### VERIFIER_COVERAGE_MATRIX_LOCK_001

**Proves:** Rung 3 of the post-audit Claude-lane sequence. Closes the 'what does verifier-governed actually mean' credibility gap identified in the gap-to-100 audit. Provides the truth layer for any future claim about language coverage and gives the next adapter expansion (Ruby/PHP/Swift/Kotlin/Scala/Elixir/.NET) a clear scope.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### VISUAL_REPAIR_LOCK_001

**Proves:** VISUAL_REPAIR_LOCK_001

**Does not prove:** Does not prove broad real-world repair coverage beyond the locked acceptance tests.

#### WORKSPACE_ESCAPE_LOCK_001

**Proves:** WORKSPACE_ESCAPE_LOCK_001

**Does not prove:** Symlink creation tests skip on Windows without Developer Mode. Junction escape coverage is OS-dependent. The path traversal and absolute path tests run everywhere.

## Drain Results (ProgramBench)

| Artifact | Tests | Decision | Commit |
|----------|------:|---------|--------|
| [CLOSE_LOCK_V7_DOXYGEN_RICHGO_RESULT_20260527](../locks/drain/CLOSE_LOCK_V7_DOXYGEN_RICHGO_RESULT_20260527.json) | 1 | CLOSE_LOCK_V7_DOXYGEN_RICHGO_RESULT_20260527 decision result:  | `unrecorded` |
| [DOXYGEN_V6_RESULT_20260527](../locks/drain/DOXYGEN_V6_RESULT_20260527.json) | 250 | doxygen__doxygen.966d98e reject result: passed delta = -1 (baseline 249 -> candi | `unrecorded` |
| [RICHGO_V6_RESULT_20260527](../locks/drain/RICHGO_V6_RESULT_20260527.json) | 786 | kyoh86__richgo.313114f reject result: passed delta = -3 (baseline 775 -> candida | `unrecorded` |
| [SEVENZIP_V5_RESULT_20260527](../locks/drain/SEVENZIP_V5_RESULT_20260527.json) | 1 | SEVENZIP_V5_RESULT_20260527 decision result:  | `unrecorded` |

## Validation

> All entries passed validation.

