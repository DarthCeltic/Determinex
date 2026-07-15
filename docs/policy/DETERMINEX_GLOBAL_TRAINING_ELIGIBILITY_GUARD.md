# Determinex Global Training Eligibility Guard

`DETERMINEX_GLOBAL_TRAINING_ELIGIBILITY_GUARD_LOCK_001` is a negative guard over
the unified Determinex status, unified evidence graph, global operator action
queue, and proof authority matrix.

The guard blocks training rows from metadata-only ProgramBench records,
skipped/blocked ProgramBench tasks, unscanned artifacts, operator actions,
packet templates, fixture approvals, model output alone, advisory diagnosis,
quarantined patch plans, temporary verifier state, failed verifier state,
missing approval, missing post-apply verification, proof gap packets, unified
status records, and evidence graph records.

Training eligibility can only become possible through a future positive
eligibility gate that proves all required source or artifact authority,
verifier success, security or policy admission, real approval where required,
post-action evidence, fresh references, non-fixture provenance, and explicit
corpus admission.

Current state:

```text
training_eligible: false
can_write_training_row_any: false
positive_gate_required: true
```
