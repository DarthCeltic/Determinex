# Real Repair Flow Final State

> Locked under `locks/sentinel/REAL_REPAIR_FLOW_FINAL_STATE_LOCK_001.json`.

Final state for the first real local-model + real human-approval
source-apply repair flow. Consolidates 10 upstream rungs into a
single `RealRepairFlowFinalState`.

## Rungs

1. `REAL_OLLAMA_PROVIDER_DETECTION_LOCK_001` — localhost-only daemon probe
2. `REAL_LOCAL_MODEL_ADMISSION_LOCK_001` — decision surface, opt-in required
3. `REAL_LIVE_DIAGNOSE_ONLY_LOCK_001` — advisory output only
4. `REAL_PATCH_PLAN_QUARANTINE_LOCK_001` — schema/path/op validation, no apply
5. `REAL_TEMP_PATCH_VERIFY_LOCK_001` — temp apply + verifier; original untouched
6. `REAL_HUMAN_APPROVAL_ADMISSION_LOCK_001` — strict real-vs-fixture gate
7. `SOURCE_MUTATION_ROLLBACK_SNAPSHOT_LOCK_001` — pre-apply snapshot writer
8. `SOURCE_MUTATION_APPLY_AFTER_APPROVAL_LOCK_001` — first real write, all gates re-checked
9. `POST_APPLY_VERIFIER_LOCK_001` — gate after real apply
10. `SOURCE_MUTATION_ROLLBACK_EXECUTION_LOCK_001` — safe restore on fail

## Final dimensions

| Dimension | Value |
|---|---|
| `real_local_model_provider` | `READY_OR_BLOCKED_WITH_REASON` |
| `real_model_admission` | `READY_OPT_IN` |
| `live_diagnose` | `READY_ADVISORY_ONLY` |
| `patch_plan_quarantine` | `READY` |
| `temp_patch_verifier` | `READY_HUMAN_APPROVAL_REQUIRED` |
| `human_approval` | `READY_REAL_SIGNED_ONLY` |
| `rollback_snapshot` | `READY` |
| `source_apply_after_approval` | `READY_GATED` |
| `post_apply_verifier` | `READY` |
| `rollback_status` | `READY_ON_FAIL` |
| `source_mutation` | `GATED_BY_REAL_APPROVAL` |
| `training_eligibility` | `BLOCKED_BY_DEFAULT` |
| `release_readiness` | `NOT_RELEASED` |
| `next_unblocker` | `REAL_BUILD_ADAPTER_BACKED_VERIFIER` (model-pull half resolved 2026-06-30, see below) |

## Scope discipline

- no training eligibility opened, no training row written
- no network provider admitted
- no Docker
- no release workflow
- no Codex/ProgramBench files touched

## What still gates real production

- the default verifier callable is `stub_verifier_pass`; production
  callers must pass a real `BuildAdapter`-backed verifier -- **still open**,
  the actual remaining next-unblocker.
- ~~the canonical `CURRENT_MODEL_IDS` must actually be pulled into
  Ollama~~ -- **RESOLVED 2026-06-30.** Live re-run of
  `scripts/models/real_ollama_provider_detection.detect()` +
  `scripts/models/canonical_local_model_id_selection.select()` against the
  real local Ollama daemon: `decision='REAL_OLLAMA_PROVIDER_DETECTED'`
  (16 models on daemon) -> `decision='CANONICAL_LOCAL_MODEL_SELECTED'`,
  `selected_model_id='determinex-engineer-v11-dsl'`, `host_state='MODEL_AVAILABLE'`.
  All three canonical ids (`determinex-engineer-v11-dsl`,
  `determinex-observer-v6-dsl`, `determinex-sentinel-v5-dsl`) are present and the
  daemon responds; the `BLOCKED_TIMEOUT` this doc originally described no
  longer reproduces. This section previously described a stale, lock-time
  snapshot as current fact -- the model-pull half of `next_unblocker` is
  done, only the verifier-adapter half remains.
