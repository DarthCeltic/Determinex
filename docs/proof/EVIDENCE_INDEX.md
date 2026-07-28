# Determinex Evidence Index

> Machine-generated from `locks/sentinel/` and `locks/drain/` manifests.
> Regenerate with: `python scripts/evidence_index.py --md docs/EVIDENCE_INDEX.md`

**150 entries** | Schema: `determinex-evidence-index-v1`

## Sentinel Locks

| Lock | Tests | Full Suite | Commit | Reproduction |
|------|------:|----------:|--------|-------------|
| [ACTION_GOVERNOR_LOCK_001](locks/sentinel/ACTION_GOVERNOR_LOCK_001.json) | 28 | 862 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/agents/test_action_safety_g…` |
| [AIDER_POLYGLOT_TRACE_HARNESS_LOCK_001](locks/sentinel/AIDER_POLYGLOT_TRACE_HARNESS_LOCK_001.json) | 8 | 772 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/test_aider_polyglot_trace_h…` |
| [ARBITRARY_REPO_READINESS_MATRIX_LOCK_001](locks/sentinel/ARBITRARY_REPO_READINESS_MATRIX_LOCK_001.json) | 13 | 13 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/intake/test_arbitrary_repo_…` |
| [ARCH_GAUNTLET_CI_LOCK_001](locks/sentinel/ARCH_GAUNTLET_CI_LOCK_001.json) | 35 | 35 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/dev/test_arch_gauntlet_ci_l…` |
| [BENCH_TO_CORPUS_ELIGIBILITY_LOCK_001](locks/sentinel/BENCH_TO_CORPUS_ELIGIBILITY_LOCK_001.json) | 10 | 750 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/test_bench_to_corpus…` |
| [BROWSER_AGENT_LOCK_001](locks/sentinel/BROWSER_AGENT_LOCK_001.json) | 18 | 704 | `0a3d1150e9` | `.\.venv\Scripts\python.exe -m pytest tests/locks/test_browser_agent_lo…` |
| [BUILD_ADAPTER_REGISTRY_LOCK_001](locks/sentinel/BUILD_ADAPTER_REGISTRY_LOCK_001.json) | 36 | 36 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/intake/test_build_adapter_r…` |
| [DETERMINEX_ARCHITECTURE_REGRESSION_GAUNTLET_LOCK_001](locks/sentinel/DETERMINEX_ARCHITECTURE_REGRESSION_GAUNTLET_LOCK_001.json) | 16 | 16 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/dev/test_architecture_regre…` |
| [DETERMINEX_CLI_LOCK_001](locks/sentinel/DETERMINEX_CLI_LOCK_001.json) | 13 | 13 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/test_determinex_cli.py -q --tb…` |
| [DETERMINEX_IDE_BACKEND_FINAL_STATE_LOCK_001](locks/sentinel/DETERMINEX_IDE_BACKEND_FINAL_STATE_LOCK_001.json) | 31 | 31 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/dev/test_determinex_ide_backen…` |
| [CI_LOCK_001](locks/sentinel/CI_LOCK_001.json) | 1 | 1 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [CI_QUALITY_GATE_LOCK_001](locks/sentinel/CI_QUALITY_GATE_LOCK_001.json) | 1 | 1 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [CLAUDE_LANE_LIVE_MODEL_READY_FINAL_STATE_LOCK_001](locks/sentinel/CLAUDE_LANE_LIVE_MODEL_READY_FINAL_STATE_LOCK_001.json) | 24 | 24 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/dev/test_claude_lane_live_m…` |
| [CLOAK_LOCK_001](locks/sentinel/CLOAK_LOCK_001.json) | 11 | 862 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/test_cloak_smoke.py -q --tb…` |
| [CLOAK_THREAT_MODEL_LOCK_001](locks/sentinel/CLOAK_THREAT_MODEL_LOCK_001.json) | 1 | 1 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [CODEBASE_EXPLORER_SMOKE_LOCK_001](locks/sentinel/CODEBASE_EXPLORER_SMOKE_LOCK_001.json) | 12 | 12 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/intake/test_codebase_explor…` |
| [CONFIG_SPINE_LOCK_001](locks/sentinel/CONFIG_SPINE_LOCK_001.json) | 31 | 31 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/test_settings.py -q --tb=sh…` |
| [CORPUS_COVERAGE_LOCK_001](locks/sentinel/CORPUS_COVERAGE_LOCK_001.json) | 7 | 732 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/test_corpus_coverage…` |
| [CORPUS_ELIGIBILITY_REPAIR_TRACE_GUARD_LOCK_001](locks/sentinel/CORPUS_ELIGIBILITY_REPAIR_TRACE_GUARD_LOCK_001.json) | 20 | 20 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/test_corpus_eligibil…` |
| [CORPUS_LICENSE_LOCK_001](locks/sentinel/CORPUS_LICENSE_LOCK_001.json) | 53 | 53 | `0a3d1150e9` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/test_license_gate.py…` |
| [CORPUS_MIGRATION_LOCK_001](locks/sentinel/CORPUS_MIGRATION_LOCK_001.json) | 20 | 862 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/test_schema_registry…` |
| [CORPUS_SCHEMA_MATURITY_LOCK_001](locks/sentinel/CORPUS_SCHEMA_MATURITY_LOCK_001.json) | 8 | 740 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/test_corpus_schema_m…` |
| [CORPUS_WRITE_GUARD_LOCK_001](locks/sentinel/CORPUS_WRITE_GUARD_LOCK_001.json) | 20 | 20 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/test_immutability_guard.py …` |
| [DISTILLATION_LOCK_001](locks/sentinel/DISTILLATION_LOCK_001.json) | 18 | 722 | `0a3d1150e9` | `.\.venv\Scripts\python.exe -m pytest tests/locks/test_distillation_loc…` |
| [EVIDENCE_IMMUTABILITY_GUARD_LOCK_001](locks/sentinel/EVIDENCE_IMMUTABILITY_GUARD_LOCK_001.json) | 20 | 20 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/test_immutability_guard.py …` |
| [EVIDENCE_INDEX_LOCK_001](locks/sentinel/EVIDENCE_INDEX_LOCK_001.json) | 5 | 772 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/locks/test_evidence_index_l…` |
| [FRONTEND_QUALITY_RAILS_LOCK_001](locks/sentinel/FRONTEND_QUALITY_RAILS_LOCK_001.json) | 10 | 10 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [GO_REPAIR_LOCK_001](locks/sentinel/GO_REPAIR_LOCK_001.json) | 27 | 617 | `0a3d1150e9` | `.\.venv\Scripts\python.exe -m pytest tests/locks/test_go_repair_lock.p…` |
| [HARDENED_INTAKE_EXECUTION_RUNNER_LOCK_001](locks/sentinel/HARDENED_INTAKE_EXECUTION_RUNNER_LOCK_001.json) | 47 | 47 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/intake/test_hardened_intake…` |
| [HARDENED_REPAIR_PIPELINE_EXECUTORS_LOCK_001](locks/sentinel/HARDENED_REPAIR_PIPELINE_EXECUTORS_LOCK_001.json) | 73 | 73 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_hardened_repair…` |
| [HARDENED_VERIFIED_TASK_AND_CODECLASH_LOCK_001](locks/sentinel/HARDENED_VERIFIED_TASK_AND_CODECLASH_LOCK_001.json) | 30 | 30 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_hardened_verifi…` |
| [HIVE_LOCK_001](locks/sentinel/HIVE_LOCK_001.json) | 12 | 862 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/test_hive_core.py -q --tb=s…` |
| [HUMAN_APPROVAL_SOURCE_MUTATION_GATE_LOCK_001](locks/sentinel/HUMAN_APPROVAL_SOURCE_MUTATION_GATE_LOCK_001.json) | 16 | 16 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_human_approval_…` |
| [IDE_LIVE_MODEL_REPAIR_FLOW_STATE_LOCK_001](locks/sentinel/IDE_LIVE_MODEL_REPAIR_FLOW_STATE_LOCK_001.json) | 13 | 13 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_ide_live_model_rep…` |
| [IDE_REPAIR_STATE_MODEL_LOCK_001](locks/sentinel/IDE_REPAIR_STATE_MODEL_LOCK_001.json) | 17 | 17 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/ide/test_ide_repair_state_m…` |
| [JAVA_CORPUS_LOCK_001](locks/sentinel/JAVA_CORPUS_LOCK_001.json) | 7 | 7 | `0a3d1150e9` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/test_java_junit_trac…` |
| [JAVA_REPAIR_LOCK_001](locks/sentinel/JAVA_REPAIR_LOCK_001.json) | 67 | 67 | `0a3d1150e9` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/java_repair/test_jav…` |
| [LEGACY_CORPUS_RECOVERY_LOCK_001](locks/sentinel/LEGACY_CORPUS_RECOVERY_LOCK_001.json) | 9 | 1025 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/test_legacy_corpus_r…` |
| [LEGACY_REPLAY_PROMOTION_LOCK_001](locks/sentinel/LEGACY_REPLAY_PROMOTION_LOCK_001.json) | 7 | 1025 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/test_legacy_replay_p…` |
| [LIVE_MODEL_DIAGNOSE_ONLY_TRACE_LOCK_001](locks/sentinel/LIVE_MODEL_DIAGNOSE_ONLY_TRACE_LOCK_001.json) | 14 | 14 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_live_model_diag…` |
| [LIVE_MODEL_MOCK_COMPATIBILITY_HARNESS_LOCK_001](locks/sentinel/LIVE_MODEL_MOCK_COMPATIBILITY_HARNESS_LOCK_001.json) | 17 | 17 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/models/test_live_model_mock…` |
| [LIVE_MODEL_PATCH_PLAN_QUARANTINE_LOCK_001](locks/sentinel/LIVE_MODEL_PATCH_PLAN_QUARANTINE_LOCK_001.json) | 19 | 19 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_live_model_patc…` |
| [LIVE_MODEL_TEMP_PATCH_VERIFIER_GATE_LOCK_001](locks/sentinel/LIVE_MODEL_TEMP_PATCH_VERIFIER_GATE_LOCK_001.json) | 11 | 11 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_live_model_temp…` |
| [LLM_MOCKED_INTAKE_REPAIR_LOCK_001](locks/sentinel/LLM_MOCKED_INTAKE_REPAIR_LOCK_001.json) | 25 | 25 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/intake/test_llm_mocked_inta…` |
| [LOCAL_LEGACY_CORPUS_QUARANTINE_LOCK_001](locks/sentinel/LOCAL_LEGACY_CORPUS_QUARANTINE_LOCK_001.json) | 1 | 772 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [LOCAL_MODEL_ADMISSION_POLICY_LOCK_001](locks/sentinel/LOCAL_MODEL_ADMISSION_POLICY_LOCK_001.json) | 19 | 19 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/models/test_local_model_adm…` |
| [LOCAL_MODEL_CONFIG_WIZARD_LOCK_001](locks/sentinel/LOCAL_MODEL_CONFIG_WIZARD_LOCK_001.json) | 15 | 15 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/models/test_local_model_con…` |
| [LOCAL_MODEL_LIVE_ADMISSION_LOCK_001](locks/sentinel/LOCAL_MODEL_LIVE_ADMISSION_LOCK_001.json) | 23 | 23 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/models/test_local_model_liv…` |
| [LOCAL_PROVIDER_SMOKE_TEST_LOCK_001](locks/sentinel/LOCAL_PROVIDER_SMOKE_TEST_LOCK_001.json) | 13 | 13 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/models/test_local_provider_…` |
| [MODEL_ROUTER_LOCK_001](locks/sentinel/MODEL_ROUTER_LOCK_001.json) | 78 | 78 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/models/test_model_router_lo…` |
| [NATIVE_C_CPP_REPAIR_LOCK_001](locks/sentinel/NATIVE_C_CPP_REPAIR_LOCK_001.json) | 24 | 641 | `0a3d1150e9` | `.\.venv\Scripts\python.exe -m pytest tests/locks/test_native_c_cpp_rep…` |
| [NO_LOOSE_BENCH_ARTIFACTS_LOCK_001](locks/sentinel/NO_LOOSE_BENCH_ARTIFACTS_LOCK_001.json) | 5 | 772 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/test_no_loose_bench_artifac…` |
| [OBSERVABILITY_LOCK_001](locks/sentinel/OBSERVABILITY_LOCK_001.json) | 25 | 887 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/observability/test_event_lo…` |
| [PARALLEL_EXECUTION_LAYER_AUDIT_LOCK_001](locks/sentinel/PARALLEL_EXECUTION_LAYER_AUDIT_LOCK_001.json) | 27 | 27 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/dev/test_parallel_execution…` |
| [PATH_PORTABILITY_LOCK_001](locks/sentinel/PATH_PORTABILITY_LOCK_001.json) | 31 | 31 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/test_settings.py -q --tb=sh…` |
| [PROGRAMBENCH_ALTERNATE_CLEANROOM_IMAGE_PROVENANCE_LOCK_001](locks/sentinel/PROGRAMBENCH_ALTERNATE_CLEANROOM_IMAGE_PROVENANCE_LOCK_001.json) | 18 | 18 | `607665753e` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_APPROVED_SCANNER_SETUP_LOCK_001](locks/sentinel/PROGRAMBENCH_APPROVED_SCANNER_SETUP_LOCK_001.json) | 16 | 1339 | `d390e5c881` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_ARTIFACT_SOURCE_ESCALATION_LOCK_001](locks/sentinel/PROGRAMBENCH_ARTIFACT_SOURCE_ESCALATION_LOCK_001.json) | 11 | 1083 | `71be79941e` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BATCH001_EXACT_MANIFEST_METADATA_PLAN_LOCK_001](locks/sentinel/PROGRAMBENCH_BATCH001_EXACT_MANIFEST_METADATA_PLAN_LOCK_001.json) | 10 | 381 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BATCH001_IMAGE_NAME_DERIVATION_LOCK_001](locks/sentinel/PROGRAMBENCH_BATCH001_IMAGE_NAME_DERIVATION_LOCK_001.json) | 10 | 381 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BATCH001_MANIFEST_DIGEST_ADMISSION_LOCK_001](locks/sentinel/PROGRAMBENCH_BATCH001_MANIFEST_DIGEST_ADMISSION_LOCK_001.json) | 10 | 381 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BATCH001_METADATA_CAMPAIGN_FINAL_STATE_LOCK_001](locks/sentinel/PROGRAMBENCH_BATCH001_METADATA_CAMPAIGN_FINAL_STATE_LOCK_001.json) | 10 | 381 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BATCH001_METADATA_RECOVERY_QUEUE_LOCK_001](locks/sentinel/PROGRAMBENCH_BATCH001_METADATA_RECOVERY_QUEUE_LOCK_001.json) | 16 | 353 | `c5cffdb154` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BATCH001_METADATA_STATE_REFRESH_LOCK_001](locks/sentinel/PROGRAMBENCH_BATCH001_METADATA_STATE_REFRESH_LOCK_001.json) | 10 | 381 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BATCH001_OPERATOR_ACTION_REFRESH_LOCK_001](locks/sentinel/PROGRAMBENCH_BATCH001_OPERATOR_ACTION_REFRESH_LOCK_001.json) | 10 | 381 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BATCH001_OPERATOR_PACKET_BUNDLE_LOCK_001](locks/sentinel/PROGRAMBENCH_BATCH001_OPERATOR_PACKET_BUNDLE_LOCK_001.json) | 16 | 353 | `c5cffdb154` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BATCH001_SAFE_MANIFEST_LOOKUP_LOCK_001](locks/sentinel/PROGRAMBENCH_BATCH001_SAFE_MANIFEST_LOOKUP_LOCK_001.json) | 10 | 381 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BATCH001_SCAN_REQUIREMENTS_QUEUE_LOCK_001](locks/sentinel/PROGRAMBENCH_BATCH001_SCAN_REQUIREMENTS_QUEUE_LOCK_001.json) | 10 | 381 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BATCH001_STATE_AGGREGATOR_LOCK_001](locks/sentinel/PROGRAMBENCH_BATCH001_STATE_AGGREGATOR_LOCK_001.json) | 15 | 337 | `7be2155dec` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BATCH001_UNBLOCK_PRIORITY_LOCK_001](locks/sentinel/PROGRAMBENCH_BATCH001_UNBLOCK_PRIORITY_LOCK_001.json) | 4 | 371 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BATCH001_UNBLOCK_PRIORITY_REFRESH_LOCK_001](locks/sentinel/PROGRAMBENCH_BATCH001_UNBLOCK_PRIORITY_REFRESH_LOCK_001.json) | 10 | 381 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BATCH001_UNBLOCK_SIMULATION_LOCK_001](locks/sentinel/PROGRAMBENCH_BATCH001_UNBLOCK_SIMULATION_LOCK_001.json) | 16 | 353 | `c5cffdb154` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BATCH_SKIP_DECISION_LOCK_001](locks/sentinel/PROGRAMBENCH_BATCH_SKIP_DECISION_LOCK_001.json) | 15 | 337 | `7be2155dec` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_BOUNDED_RERUN_EXECUTION_LOCK_001](locks/sentinel/PROGRAMBENCH_BOUNDED_RERUN_EXECUTION_LOCK_001.json) | 10 | 1025 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_CAMPAIGN_REPORTING_API_LOCK_001](locks/sentinel/PROGRAMBENCH_CAMPAIGN_REPORTING_API_LOCK_001.json) | 15 | 337 | `7be2155dec` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_CAMPAIGN_STATUS_BOARD_LOCK_001](locks/sentinel/PROGRAMBENCH_CAMPAIGN_STATUS_BOARD_LOCK_001.json) | 11 | 322 | `87eff77039` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_CLEANROOM_BUILD_RECIPE_PROVENANCE_GAP_LOCK_001](locks/sentinel/PROGRAMBENCH_CLEANROOM_BUILD_RECIPE_PROVENANCE_GAP_LOCK_001.json) | 18 | 1510 | `9e01593db6` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_CLEANROOM_BUILD_RECIPE_RECOVERY_LOCK_001](locks/sentinel/PROGRAMBENCH_CLEANROOM_BUILD_RECIPE_RECOVERY_LOCK_001.json) | 16 | 1500 | `fac45c4dbc` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_CLEANROOM_IMAGE_HYDRATION_LOCK_001](locks/sentinel/PROGRAMBENCH_CLEANROOM_IMAGE_HYDRATION_LOCK_001.json) | 12 | 1236 | `da82a95a82` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_CLEANROOM_IMAGE_IMPORT_LOCK_001](locks/sentinel/PROGRAMBENCH_CLEANROOM_IMAGE_IMPORT_LOCK_001.json) | 12 | 1236 | `da82a95a82` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_CLEANROOM_IMAGE_REMEDIATION_PLAN_LOCK_001](locks/sentinel/PROGRAMBENCH_CLEANROOM_IMAGE_REMEDIATION_PLAN_LOCK_001.json) | 17 | 1448 | `b13f3aaba1` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_CLEANROOM_IMAGE_SCANNER_ADMISSION_LOCK_001](locks/sentinel/PROGRAMBENCH_CLEANROOM_IMAGE_SCANNER_ADMISSION_LOCK_001.json) | 15 | 1251 | `d390e5c881` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_CLEANROOM_IMAGE_SCAN_LOCK_001](locks/sentinel/PROGRAMBENCH_CLEANROOM_IMAGE_SCAN_LOCK_001.json) | 14 | 1236 | `da82a95a82` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_CLEANROOM_IMAGE_SCAN_TRIAGE_LOCK_001](locks/sentinel/PROGRAMBENCH_CLEANROOM_IMAGE_SCAN_TRIAGE_LOCK_001.json) | 15 | 1358 | `d390e5c881` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_CLEANROOM_RECIPE_PROVENANCE_RECOVERY_LOCK_001](locks/sentinel/PROGRAMBENCH_CLEANROOM_RECIPE_PROVENANCE_RECOVERY_LOCK_001.json) | 20 | 1624 | `607665753e` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_CODEX_LANE_FINAL_STATE_LOCK_001](locks/sentinel/PROGRAMBENCH_CODEX_LANE_FINAL_STATE_LOCK_001.json) | 15 | 337 | `7be2155dec` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_CODEX_OPERATOR_READY_FINAL_STATE_LOCK_001](locks/sentinel/PROGRAMBENCH_CODEX_OPERATOR_READY_FINAL_STATE_LOCK_001.json) | 16 | 353 | `c5cffdb154` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_DOCKERHUB_MANIFEST_PROVENANCE_LOCK_001](locks/sentinel/PROGRAMBENCH_DOCKERHUB_MANIFEST_PROVENANCE_LOCK_001.json) | 10 | 1236 | `da82a95a82` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_DOXYGEN_LANE_FINAL_STATE_LOCK_001](locks/sentinel/PROGRAMBENCH_DOXYGEN_LANE_FINAL_STATE_LOCK_001.json) | 11 | 322 | `87eff77039` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_EVIDENCE_GRAPH_INTEGRITY_GUARD_LOCK_001](locks/sentinel/PROGRAMBENCH_EVIDENCE_GRAPH_INTEGRITY_GUARD_LOCK_001.json) | 16 | 353 | `c5cffdb154` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_EVIDENCE_GRAPH_LOCK_001](locks/sentinel/PROGRAMBENCH_EVIDENCE_GRAPH_LOCK_001.json) | 15 | 337 | `7be2155dec` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_EXACT_PROVIDER_PROBE_PLAN_LOCK_001](locks/sentinel/PROGRAMBENCH_EXACT_PROVIDER_PROBE_PLAN_LOCK_001.json) | 16 | 353 | `c5cffdb154` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_GENERIC_EXECUTION_PREFLIGHT_LOCK_001](locks/sentinel/PROGRAMBENCH_GENERIC_EXECUTION_PREFLIGHT_LOCK_001.json) | 15 | 337 | `7be2155dec` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_GENERIC_OPERATOR_POLICY_ADMISSION_LOCK_001](locks/sentinel/PROGRAMBENCH_GENERIC_OPERATOR_POLICY_ADMISSION_LOCK_001.json) | 15 | 337 | `7be2155dec` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_INFRA_FAILURE_TRIAGE_LOCK_001](locks/sentinel/PROGRAMBENCH_INFRA_FAILURE_TRIAGE_LOCK_001.json) | 13 | 1058 | `1891191f9f` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_INSTANCE_STATE_SCHEMA_LOCK_001](locks/sentinel/PROGRAMBENCH_INSTANCE_STATE_SCHEMA_LOCK_001.json) | 15 | 337 | `7be2155dec` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_OFFICIAL_ARTIFACT_EXECUTION_PREFLIGHT_LOCK_001](locks/sentinel/PROGRAMBENCH_OFFICIAL_ARTIFACT_EXECUTION_PREFLIGHT_LOCK_001.json) | 11 | 322 | `87eff77039` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_OFFICIAL_ARTIFACT_SANDBOX_REQUIREMENTS_LOCK_001](locks/sentinel/PROGRAMBENCH_OFFICIAL_ARTIFACT_SANDBOX_REQUIREMENTS_LOCK_001.json) | 11 | 322 | `87eff77039` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_OFFICIAL_ARTIFACT_SECURITY_DECISION_LOCK_001](locks/sentinel/PROGRAMBENCH_OFFICIAL_ARTIFACT_SECURITY_DECISION_LOCK_001.json) | 8 | 311 | `87eff77039` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_ONLINE_ARTIFACT_DISCOVERY_LOCK_001](locks/sentinel/PROGRAMBENCH_ONLINE_ARTIFACT_DISCOVERY_LOCK_001.json) | 10 | 1025 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/test_programbench_on…` |
| [PROGRAMBENCH_ONLINE_PROVIDER_REGISTRY_LOCK_001](locks/sentinel/PROGRAMBENCH_ONLINE_PROVIDER_REGISTRY_LOCK_001.json) | 7 | 1025 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/test_programbench_on…` |
| [PROGRAMBENCH_OPERATOR_ACTION_QUEUE_LOCK_001](locks/sentinel/PROGRAMBENCH_OPERATOR_ACTION_QUEUE_LOCK_001.json) | 15 | 337 | `7be2155dec` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_OPERATOR_ARTIFACT_ADMISSION_LOCK_001](locks/sentinel/PROGRAMBENCH_OPERATOR_ARTIFACT_ADMISSION_LOCK_001.json) | 14 | 1072 | `1891191f9f` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_OPERATOR_CLI_LOCK_001](locks/sentinel/PROGRAMBENCH_OPERATOR_CLI_LOCK_001.json) | 16 | 353 | `c5cffdb154` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_OPERATOR_INBOX_SCANNER_LOCK_001](locks/sentinel/PROGRAMBENCH_OPERATOR_INBOX_SCANNER_LOCK_001.json) | 16 | 353 | `c5cffdb154` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_OPERATOR_OUTBOX_LOCK_001](locks/sentinel/PROGRAMBENCH_OPERATOR_OUTBOX_LOCK_001.json) | 16 | 353 | `c5cffdb154` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_OPERATOR_PACKET_ADMISSION_LIVE_PACKET_REVIEW_LOCK_001](locks/sentinel/PROGRAMBENCH_OPERATOR_PACKET_ADMISSION_LIVE_PACKET_REVIEW_LOCK_001.json) | 4 | 363 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_OPERATOR_PACKET_ADMISSION_PROCESSING_LOCK_001](locks/sentinel/PROGRAMBENCH_OPERATOR_PACKET_ADMISSION_PROCESSING_LOCK_001.json) | 4 | 4 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_OPERATOR_PACKET_ADMISSION_ROUTER_LOCK_001](locks/sentinel/PROGRAMBENCH_OPERATOR_PACKET_ADMISSION_ROUTER_LOCK_001.json) | 16 | 353 | `c5cffdb154` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_OPERATOR_PACKET_TEMPLATES_LOCK_001](locks/sentinel/PROGRAMBENCH_OPERATOR_PACKET_TEMPLATES_LOCK_001.json) | 16 | 353 | `c5cffdb154` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_OPERATOR_PACKET_VALIDATOR_LOCK_001](locks/sentinel/PROGRAMBENCH_OPERATOR_PACKET_VALIDATOR_LOCK_001.json) | 16 | 353 | `c5cffdb154` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_OPERATOR_PROVENANCE_REQUEST_PACKET_LOCK_001](locks/sentinel/PROGRAMBENCH_OPERATOR_PROVENANCE_REQUEST_PACKET_LOCK_001.json) | 19 | 19 | `607665753e` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_OPERATOR_READY_AUDIT_LOCK_001](locks/sentinel/PROGRAMBENCH_OPERATOR_READY_AUDIT_LOCK_001.json) | 4 | 367 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_PLATFORM_COMPLETION_SCORECARD_LOCK_001](locks/sentinel/PROGRAMBENCH_PLATFORM_COMPLETION_SCORECARD_LOCK_001.json) | 16 | 353 | `c5cffdb154` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_REAL_BOUNDED_RERUN_LOCK_001](locks/sentinel/PROGRAMBENCH_REAL_BOUNDED_RERUN_LOCK_001.json) | 11 | 1025 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_REBUILD_PROVENANCE_QUARANTINE_DECISION_LOCK_001](locks/sentinel/PROGRAMBENCH_REBUILD_PROVENANCE_QUARANTINE_DECISION_LOCK_001.json) | 18 | 18 | `607665753e` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_REPLAY_HYDRATION_LOCK_001](locks/sentinel/PROGRAMBENCH_REPLAY_HYDRATION_LOCK_001.json) | 10 | 1025 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/test_programbench_re…` |
| [PROGRAMBENCH_REPLAY_IMAGE_HYDRATION_LOCK_001](locks/sentinel/PROGRAMBENCH_REPLAY_IMAGE_HYDRATION_LOCK_001.json) | 10 | 1025 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/test_programbench_re…` |
| [PROGRAMBENCH_REPLAY_METADATA_RECOVERY_LOCK_001](locks/sentinel/PROGRAMBENCH_REPLAY_METADATA_RECOVERY_LOCK_001.json) | 8 | 1025 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/legacy_recovery/test…` |
| [PROGRAMBENCH_REPLAY_VERIFIER_LOCK_001](locks/sentinel/PROGRAMBENCH_REPLAY_VERIFIER_LOCK_001.json) | 7 | 1025 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/test_programbench_re…` |
| [PROGRAMBENCH_RERUN_READINESS_MATRIX_LOCK_001](locks/sentinel/PROGRAMBENCH_RERUN_READINESS_MATRIX_LOCK_001.json) | 11 | 322 | `87eff77039` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_ROOT_CAUSE_PACKET_LOCK_001](locks/sentinel/PROGRAMBENCH_ROOT_CAUSE_PACKET_LOCK_001.json) | 10 | 1025 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_ROOT_DISAMBIGUATION_LOCK_001](locks/sentinel/PROGRAMBENCH_ROOT_DISAMBIGUATION_LOCK_001.json) | 9 | 1025 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/test_programbench_ro…` |
| [PROGRAMBENCH_SECURITY_POLICY_ADMISSION_GATE_LOCK_001](locks/sentinel/PROGRAMBENCH_SECURITY_POLICY_ADMISSION_GATE_LOCK_001.json) | 11 | 322 | `87eff77039` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_SECURITY_POLICY_EXCEPTION_REQUEST_LOCK_001](locks/sentinel/PROGRAMBENCH_SECURITY_POLICY_EXCEPTION_REQUEST_LOCK_001.json) | 11 | 322 | `87eff77039` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_SKIP_REASON_TAXONOMY_LOCK_001](locks/sentinel/PROGRAMBENCH_SKIP_REASON_TAXONOMY_LOCK_001.json) | 15 | 337 | `7be2155dec` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_TASK_ROOT_RESOLUTION_LOCK_001](locks/sentinel/PROGRAMBENCH_TASK_ROOT_RESOLUTION_LOCK_001.json) | 9 | 1025 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/test_programbench_ta…` |
| [PROGRAMBENCH_TASK_SKIP_WITH_PROVENANCE_REASON_LOCK_001](locks/sentinel/PROGRAMBENCH_TASK_SKIP_WITH_PROVENANCE_REASON_LOCK_001.json) | 11 | 322 | `87eff77039` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_TRAINING_ELIGIBILITY_NEGATIVE_GUARD_LOCK_001](locks/sentinel/PROGRAMBENCH_TRAINING_ELIGIBILITY_NEGATIVE_GUARD_LOCK_001.json) | 11 | 322 | `87eff77039` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PROGRAMBENCH_UPSTREAM_ARTIFACT_AUTHORITY_RECHECK_LOCK_001](locks/sentinel/PROGRAMBENCH_UPSTREAM_ARTIFACT_AUTHORITY_RECHECK_LOCK_001.json) | 14 | 303 | `87eff77039` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/programbench/test_pr…` |
| [PYTHON_REPAIR_LOCK_001](locks/sentinel/PYTHON_REPAIR_LOCK_001.json) | 41 | 590 | `0a3d1150e9` | `.\.venv\Scripts\python.exe -m pytest tests/locks/test_python_repair_lo…` |
| [REPRODUCIBLE_DEV_LOCK_001](locks/sentinel/REPRODUCIBLE_DEV_LOCK_001.json) | 1 | 1 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [ROSETTA_LOCK_001](locks/sentinel/ROSETTA_LOCK_001.json) | 13 | 862 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/test_rosetta_smoke.py -q --…` |
| [RUST_REPAIR_LOCK_001](locks/sentinel/RUST_REPAIR_LOCK_001.json) | 45 | 549 | `0a3d1150e9` | `.\.venv\Scripts\python.exe -m pytest tests/locks/test_rust_repair_lock…` |
| [SAFE_PATCH_DIFF_ROLLBACK_LOCK_001](locks/sentinel/SAFE_PATCH_DIFF_ROLLBACK_LOCK_001.json) | 22 | 22 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_safe_patch_diff…` |
| [SCRIPT_HELPER_EXECUTION_CLASSIFICATION_SWEEP_LOCK_001](locks/sentinel/SCRIPT_HELPER_EXECUTION_CLASSIFICATION_SWEEP_LOCK_001.json) | 67 | 67 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/dev/test_script_helper_exec…` |
| [SENTINEL_LOCK_001](locks/sentinel/SENTINEL_LOCK_001.json) | 121 | 121 | `0a3d1150e9` | `.\.venv\Scripts\python.exe -m pytest tests/sentinelbench/test_refusal_…` |
| [SQL_ORACLE_LOCK_001](locks/sentinel/SQL_ORACLE_LOCK_001.json) | 22 | 686 | `0a3d1150e9` | `.\.venv\Scripts\python.exe -m pytest tests/locks/test_sql_oracle_lock.…` |
| [STORAGE_OPERATIONS_LOCK_001](locks/sentinel/STORAGE_OPERATIONS_LOCK_001.json) | 1 | 1 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [SUPPLY_CHAIN_LOCK_001](locks/sentinel/SUPPLY_CHAIN_LOCK_001.json) | 133 | 133 | `0a3d1150e9` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/test_license_gate.py…` |
| [TRAINING_CORPUS_DASHBOARD_LOCK_001](locks/sentinel/TRAINING_CORPUS_DASHBOARD_LOCK_001.json) | 4 | 772 | `unrecorded` | `.\.venv\Scripts\python.exe -m pytest tests/corpus/test_training_corpus…` |
| [TYPESCRIPT_REPAIR_LOCK_001](locks/sentinel/TYPESCRIPT_REPAIR_LOCK_001.json) | 23 | 664 | `0a3d1150e9` | `.\.venv\Scripts\python.exe -m pytest tests/locks/test_typescript_repai…` |
| [VERIFIED_REPAIR_TRACE_LOCK_001](locks/sentinel/VERIFIED_REPAIR_TRACE_LOCK_001.json) | 13 | 13 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/repair/test_verified_repair…` |
| [VERIFIER_COVERAGE_MATRIX_LOCK_001](locks/sentinel/VERIFIER_COVERAGE_MATRIX_LOCK_001.json) | 39 | 39 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/intake/test_verifier_covera…` |
| [VISUAL_REPAIR_LOCK_001](locks/sentinel/VISUAL_REPAIR_LOCK_001.json) | 21 | 21 | `0a3d1150e9` | `.\.venv\Scripts\python.exe -m pytest tests -q --tb=short…` |
| [WORKSPACE_ESCAPE_LOCK_001](locks/sentinel/WORKSPACE_ESCAPE_LOCK_001.json) | 12 | 862 | `clean-main` | `.\.venv\Scripts\python.exe -m pytest tests/security/test_workspace_sym…` |

### What Each Lock Proves

#### ACTION_GOVERNOR_LOCK_001

**Proves:** ACTION_GOVERNOR_LOCK_001

**Does not prove:** Does not prove the governor is wired into every agent controller. The lock proves the gate logic is correct; call-site coverage must be verified separately.

#### AIDER_POLYGLOT_TRACE_HARNESS_LOCK_001

**Proves:** Turn Aider Polyglot / Exercism-style benchmark attempts into signed, schema-complete corpus traces across locked languages.

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

#### BUILD_ADAPTER_REGISTRY_LOCK_001

**Proves:** Rung 2 of the post-audit Claude-lane sequence. Establishes the adapter contract that real arbitrary-repo intake needs (monorepos, polyglot trees, custom test commands) without redesigning ShadowCompiler or moving the LLM-dependent paths. ShadowCompiler-vs-hive/compiler.py unification is reserved for PARALLEL_EXECUTION_LAYER_AUDIT_LOCK_001.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_ARCHITECTURE_REGRESSION_GAUNTLET_LOCK_001

**Proves:** Catch any regression in the 6-rung architecture sprint with one invocation: `python scripts/dev/architecture_regression_gauntlet.py --strict`. Runs in CI alongside the other quality gates.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_CLI_LOCK_001

**Proves:** DETERMINEX_CLI_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### DETERMINEX_IDE_BACKEND_FINAL_STATE_LOCK_001

**Proves:** Rung 10 of the verified-repair campaign — the campaign finale. Pins the equilibrium state the apparatus reached: clean execution surface, dry-run model routing, mocked end-to-end loop, temp-only safe patch, source mutation blocked pending human approval, IDE backend state ready, NO live model calls, training eligibility BLOCKED, NOT RELEASED. The next unblocker is LOCAL_MODEL_LIVE_ADMISSION_AND_IDE_UI_FLOW.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### CI_LOCK_001

**Proves:** CI_LOCK_001

**Does not prove:** Does not prove all test paths run in CI. Only the paths listed in test.yml trigger; the filter may miss novel file locations.

#### CI_QUALITY_GATE_LOCK_001

**Proves:** CI_QUALITY_GATE_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### CLAUDE_LANE_LIVE_MODEL_READY_FINAL_STATE_LOCK_001

**Proves:** Campaign finale for the live-local-model work. Pins the equilibrium: live admission is opt-in local-only, network models blocked by default, diagnose-only and patch-plan and temp-patch verifier surfaces are READY, source mutation remains BLOCKED pending human approval, training eligibility blocked by default, NOT RELEASED. Next unblocker: REAL_LOCAL_MODEL_CONFIG_AND_HUMAN_APPROVAL_UI.

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

#### DISTILLATION_LOCK_001

**Proves:** DISTILLATION_LOCK_001

**Does not prove:** Does not prove a deployed specialist model beats baseline without a later eval card.

#### EVIDENCE_IMMUTABILITY_GUARD_LOCK_001

**Proves:** EVIDENCE_IMMUTABILITY_GUARD_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### EVIDENCE_INDEX_LOCK_001

**Proves:** Generate a reproducible evidence index for every named lock and drain artifact before external preview packaging.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### FRONTEND_QUALITY_RAILS_LOCK_001

**Proves:** FRONTEND_QUALITY_RAILS_LOCK_001

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

#### HUMAN_APPROVAL_SOURCE_MUTATION_GATE_LOCK_001

**Proves:** Rung 5 of the verified-repair campaign. Pins the invariant that source mutation remains BLOCKED by default and can only be opened by a packet that references an exactly-matching verified trace. The next rungs (IDE state model, corpus guard, local model admission, readiness matrix, final state) compose against this gate; nothing in the apparatus ever writes to the user's original repo without a downstream consumer producing an ACCEPTED decision first.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### IDE_LIVE_MODEL_REPAIR_FLOW_STATE_LOCK_001

**Proves:** Rung 6 of the live-local-model campaign. Exposes the live-model repair flow state to the IDE backend without building UI. Sets up CLAUDE_LANE_LIVE_MODEL_READY_FINAL_STATE_LOCK_001 (the campaign finale).

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### IDE_REPAIR_STATE_MODEL_LOCK_001

**Proves:** Rung 6 of the verified-repair campaign. Decouples the frontend from the internals of the four prior rungs: an IDE can consume a single JSON record and render the current state without touching trace internals. Sets up DETERMINEX_IDE_BACKEND_FINAL_STATE_LOCK_001 (the campaign-finale rung) to roll up the full backend state into a single packet.

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

#### LOCAL_PROVIDER_SMOKE_TEST_LOCK_001

**Proves:** Rung 2 of the IDE consumer campaign.

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

#### PARALLEL_EXECUTION_LAYER_AUDIT_LOCK_001

**Proves:** Rung 4 of the post-audit Claude-lane sequence. Closes the gap-to-100 audit's hidden-assumption #3 ('parallel execution layers; only one hardened'). The output is the target list for HARDENED_INTAKE_EXECUTION_RUNNER_LOCK_001 (the next rung). Audit is intentionally read-only: never executes a discovered command, never mutates source or signed evidence, never imports the scanned modules.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PATH_PORTABILITY_LOCK_001

**Proves:** PATH_PORTABILITY_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_ALTERNATE_CLEANROOM_IMAGE_PROVENANCE_LOCK_001

**Proves:** Determine whether a safer provenance-admissible alternate Doxygen cleanroom image path exists without pulling, hydrating, rebuilding, executing Docker, or running ProgramBench.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_APPROVED_SCANNER_SETUP_LOCK_001

**Proves:** Configure or admit an approved scanner installation path before cleanroom image scanning can be retried.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_ARTIFACT_SOURCE_ESCALATION_LOCK_001

**Proves:** Generate a precise operator checklist when ProgramBench cleanroom image provenance is missing and block hydration until real provenance is supplied.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_BATCH001_EXACT_MANIFEST_METADATA_PLAN_LOCK_001

**Proves:** Create a per-target exact DockerHub manifest metadata plan for derived Batch001 image names without searching, pulling, or running.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_BATCH001_IMAGE_NAME_DERIVATION_LOCK_001

**Proves:** Derive expected official ProgramBench task_cleanroom image names for top Batch001 metadata-only targets using the established owner__repo.sha naming rule.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_BATCH001_MANIFEST_DIGEST_ADMISSION_LOCK_001

**Proves:** Admit exact manifest digests as metadata-only artifact evidence where safe lookup found digests.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_BATCH001_METADATA_CAMPAIGN_FINAL_STATE_LOCK_001

**Proves:** Write final state for the Batch001 metadata campaign after derivation, exact lookup planning, safe lookup support check, digest admission, refreshes, and scan requirements.

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

#### PROGRAMBENCH_BATCH001_OPERATOR_PACKET_BUNDLE_LOCK_001

**Proves:** Generate Batch 001 operator packet template bundle for current next actions.

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### PROGRAMBENCH_BATCH001_SAFE_MANIFEST_LOOKUP_LOCK_001

**Proves:** Determine whether existing policy and code support exact metadata-only manifest lookup for derived Batch001 image names.

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

#### REPRODUCIBLE_DEV_LOCK_001

**Proves:** REPRODUCIBLE_DEV_LOCK_001

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

#### SQL_ORACLE_LOCK_001

**Proves:** SQL_ORACLE_LOCK_001

**Does not prove:** Does not prove broad real-world repair coverage beyond the locked acceptance tests.

#### STORAGE_OPERATIONS_LOCK_001

**Proves:** STORAGE_OPERATIONS_LOCK_001

**Does not prove:** Does not prove claims outside the manifest's tested control surface.

#### SUPPLY_CHAIN_LOCK_001

**Proves:** SUPPLY_CHAIN_LOCK_001

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
| [CLOSE_LOCK_V7_DOXYGEN_RICHGO_RESULT_20260527](locks/drain/CLOSE_LOCK_V7_DOXYGEN_RICHGO_RESULT_20260527.json) | 1 | CLOSE_LOCK_V7_DOXYGEN_RICHGO_RESULT_20260527 decision result:  | `unrecorded` |
| [DOXYGEN_V6_RESULT_20260527](locks/drain/DOXYGEN_V6_RESULT_20260527.json) | 250 | doxygen__doxygen.966d98e reject result: passed delta = -1 (baseline 249 -> candi | `unrecorded` |
| [RICHGO_V6_RESULT_20260527](locks/drain/RICHGO_V6_RESULT_20260527.json) | 786 | kyoh86__richgo.313114f reject result: passed delta = -3 (baseline 775 -> candida | `unrecorded` |
| [SEVENZIP_V5_RESULT_20260527](locks/drain/SEVENZIP_V5_RESULT_20260527.json) | 1 | SEVENZIP_V5_RESULT_20260527 decision result:  | `unrecorded` |

## Validation

> All entries passed validation.

