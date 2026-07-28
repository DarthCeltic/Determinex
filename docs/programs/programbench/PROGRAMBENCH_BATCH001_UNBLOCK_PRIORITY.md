# ProgramBench Batch001 Unblock Priority

`PROGRAMBENCH_BATCH001_UNBLOCK_PRIORITY_LOCK_001` ranks known Batch001 instances by the easiest safe next evidence step. It is a read-only priority record: it does not run Docker, pull images, execute ProgramBench, approve Doxygen, or create training rows.

## Result

The priority record consumes the Batch001 state aggregator, metadata recovery queue, exact provider probe plan, operator action queue, campaign status board, rerun readiness matrix, evidence graph, and Doxygen final state.

Current conclusion:

- Doxygen has the strongest artifact authority, but it is scan-failed and blocked pending real operator security policy admission.
- The safest next Codex work is not Doxygen execution. It is exact image metadata/provenance recovery for Batch001 rows that are currently missing image metadata.
- Metadata-recovery rows can progress through operator image metadata packets without security policy admission for that metadata step only. They still cannot execute until manifest, scan, policy, and bounded-rerun gates are satisfied.

## Evidence

Signed evidence:

```text
assurance/evidence/programbench_batch001_unblock_priority/programbench_batch001_unblock_priority_run_20260528.BATCH001_UNBLOCK_PRIORITY_WRITTEN.json
```

Focused tests:

```text
tests/corpus/programbench/test_programbench_batch001_unblock_priority_lock.py
```

## Safety Closure

The record keeps these closed:

- `docker_run_performed: false`
- `docker_pull_performed: false`
- `programbench_rerun_performed: false`
- `policy_exception_granted: false`
- `training_rows_written: false`
- `training_eligible: false`
- `cache_ready: false`
- `executable: false`
