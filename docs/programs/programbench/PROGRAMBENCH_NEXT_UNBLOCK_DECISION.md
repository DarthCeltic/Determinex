# ProgramBench Next Unblock Decision

`PROGRAMBENCH_NEXT_UNBLOCK_DECISION_LOCK_001` compares the next non-executing
ProgramBench unblock paths.

Compared options:

- Doxygen security policy admission.
- Batch001 one-target artifact import / scan / policy path.
- Holding ProgramBench until evidence ledger hardening is complete.

Current recommendation:

```text
status: PROGRAMBENCH_NEXT_UNBLOCK_RECOMMENDS_BATCH001_ONE_TARGET
recommended_path: batch001_one_target_artifact_import_scan_policy
next_required_operator_packet: artifact_import_provenance_packet
execution_authorized: false
artifact_import_authorized: false
scan_authorized: false
training_eligible: false
```

The recommended path exercises the solved Batch001 metadata authority with lower
policy burden than Doxygen, while still stopping before import, scan, execution,
or training.
