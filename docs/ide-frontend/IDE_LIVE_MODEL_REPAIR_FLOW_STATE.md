# IDE Live Model Repair Flow State

> Locked under `locks/sentinel/IDE_LIVE_MODEL_REPAIR_FLOW_STATE_LOCK_001.json`.

Backend state model the IDE renders to show the live-model repair
flow. Composes the four upstream live records into a single flat JSON.

## Dimensions

| Dimension              | Values                                                          |
|------------------------|-----------------------------------------------------------------|
| `live_admission`       | `LIVE_MODEL_ADMITTED` / `LIVE_MODEL_NOT_ADMITTED`               |
| `diagnosis_advisory`   | `DIAGNOSIS_ADVISORY_AVAILABLE` / `LIVE_MODEL_NOT_ADMITTED`      |
| `patch_plan`           | `PATCH_PLAN_QUARANTINED` / `LIVE_MODEL_NOT_ADMITTED`            |
| `temp_patch_verifier`  | `TEMP_PATCH_VERIFIER_PASSED` / `TEMP_PATCH_VERIFIER_FAILED` / `LIVE_MODEL_NOT_ADMITTED` |
| `human_approval`       | always `HUMAN_APPROVAL_REQUIRED`                                |
| `source_mutation`      | always `SOURCE_MUTATION_BLOCKED`                                |
| `training_eligibility` | always `TRAINING_ELIGIBLE_FALSE`                                |

Even `TEMP_PATCH_VERIFIER_PASSED` does NOT open source mutation.
