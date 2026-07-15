# Live Model Diagnose-Only Trace

> Locked under `locks/sentinel/LIVE_MODEL_DIAGNOSE_ONLY_TRACE_LOCK_001.json`.

The smallest live-model surface in the apparatus: a model may
*diagnose*, but it may never patch. Only two task classes are
admitted: `BUILD_DIAGNOSIS` and `TEST_FAILURE_LOCALIZATION`.

## Statuses (closed set)

| Status                                                  | Meaning                                                |
|---------------------------------------------------------|--------------------------------------------------------|
| `LIVE_DIAGNOSE_TRACE_WRITTEN`                           | All checks passed; response captured as advisory       |
| `LIVE_DIAGNOSE_RESPONSE_CAPTURED_ADVISORY_ONLY`         | Appears in statuses_seen on every written trace        |
| `LIVE_DIAGNOSE_NO_SOURCE_MUTATION`                      | Always appears alongside WRITTEN                       |
| `LIVE_DIAGNOSE_BLOCKED_MODEL_NOT_ADMITTED`              | Admission record was not READY                         |
| `LIVE_DIAGNOSE_BLOCKED_UNSUPPORTED_TASK`                | task_class not in {BUILD_DIAGNOSIS, TEST_FAILURE_LOCALIZATION} |
| `LIVE_DIAGNOSE_BLOCKED_PROVIDER_REJECTED`               | Compat harness refused the response                    |

## Hard invariants

* `patch_generated=False` on every trace
* `source_mutation_authorized=False` on every trace
* `corpus_write_authorized=False` on every trace
* `training_eligible=False` on every trace
* `advisory_only=True` on every trace
* Workspace sha256 tree before == after
