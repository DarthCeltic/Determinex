# Claude Real Model + Verifier Ready Final State

> Locked under `locks/sentinel/CLAUDE_REAL_MODEL_VERIFIER_READY_FINAL_STATE_LOCK_001.json`.

Campaign finale for the real-model + build-adapter-verifier campaign.
**Subordinate to** Codex's proof-control audit repair: this lock does
NOT claim full-suite clean.

## Rungs

1. `CANONICAL_LOCAL_MODEL_ID_SELECTION_LOCK_001` — pick canonical id, classify host
2. `OLLAMA_MODEL_PULL_OPERATOR_GUIDE_LOCK_001` — emit `ollama pull <id>` (never auto-pull)
3. `REAL_LOCAL_MODEL_HEALTHCHECK_LOCK_001` — trivial-prompt liveness
4. `BUILD_ADAPTER_BACKED_VERIFIER_SELECTION_LOCK_001` — derive real verifier argv
5. `REAL_MODEL_DIAGNOSE_WITH_BUILD_VERIFIER_LOCK_001` — advisory diagnose w/ verifier ctx
6. `REAL_MODEL_PATCH_PLAN_WITH_VERIFIER_CONTEXT_LOCK_001` — quarantine + ctx
7. `REAL_BUILD_ADAPTER_TEMP_VERIFY_TRACE_LOCK_001` — real pytest on temp through hardened runner
8. `REAL_APPROVAL_APPLY_POST_VERIFY_TRACE_LOCK_001` — end-to-end orchestrator

## Final dimensions

| Dimension | Value |
|---|---|
| `canonical_model_id` | READY |
| `model_available` | READY_OR_BLOCKED_WITH_REASON |
| `model_healthcheck` | READY_OR_BLOCKED_WITH_REASON |
| `build_adapter_verifier` | READY |
| `real_model_diagnose` | READY_ADVISORY_ONLY |
| `real_patch_plan_quarantine` | READY |
| `temp_verify_trace` | READY_HUMAN_APPROVAL_REQUIRED |
| `real_approval_apply` | READY_GATED |
| `post_apply_verifier` | READY |
| `source_mutation` | GATED_BY_REAL_APPROVAL |
| `training_eligibility` | BLOCKED_BY_DEFAULT |
| `next_unblocker` | CODEX_AUDIT_REPAIR_THEN_PROGRAMBENCH_REGRESSION_PARITY |

## Scope discipline

- training eligibility BLOCKED; no training row
- no network provider admitted; no Docker; no release workflow
- no Codex/ProgramBench/proof-control files touched
- canonical model is NOT auto-pulled by any rung
- source mutation only through the already-locked approval/apply gate

## What this campaign does NOT claim

Full-suite clean. Three pre-existing audit failures remain from the
unrelated PB lane proof-control commit (`22d0087c6`):

- `tests/models/test_local_model_live_admission_lock.py::test_audit_counts_invariants_preserved`
- `tests/models/test_model_router_lock.py::test_audit_counts_invariants_preserved`
- `tests/repair/test_hardened_verified_task_and_codeclash_lock.py::test_audit_unknown_is_zero`

These are caused by a subprocess call in `scripts/proof/proof_control_readiness_audit.py:140`
that the parallel-execution-layer audit classifies as
`UNKNOWN_REQUIRES_REVIEW`. Resolving them is Codex's responsibility.
