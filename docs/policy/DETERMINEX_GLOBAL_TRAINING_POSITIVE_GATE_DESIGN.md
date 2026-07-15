# Determinex Global Training Positive Gate Design

`DETERMINEX_GLOBAL_TRAINING_POSITIVE_GATE_DESIGN_LOCK_001` defines the future
positive gate for training eligibility without enabling training.

The positive gate requires:

- verified repair success
- explicit verifier
- post-apply verifier
- rollback safety
- source provenance
- operator authorization
- no fixture approval
- no synthetic model admission
- no benchmark artifact ambiguity
- no blocked ProgramBench target
- no failed repair mislabeled as success
- privacy classification
- corpus destination
- revocation/supersession policy
- evidence ledger chain validity

Current state:

```text
status: TRAINING_POSITIVE_GATE_DRY_RUN_ALL_BLOCKED
training_eligible: false
can_write_training_row_any: false
training_rows_written: false
production_training_writer_created: false
```

All current records remain blocked from training. This lock is a design/spec
gate only.
