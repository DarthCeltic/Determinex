# Determinex Evidence Count Drift Guard

`DETERMINEX_EVIDENCE_COUNT_DRIFT_GUARD_LOCK_001` reconciles the evidence index with
the append-only ledger snapshot.

The guard records:

- expected evidence count
- actual evidence count
- added records
- removed records
- changed records
- validation errors
- dirty workspace state

Current state:

```text
status: EVIDENCE_COUNT_DRIFT_GUARD_PASSED
expected_evidence_count: matches actual_evidence_count
dirty_state_recorded: true
```

Dirty state is allowed only when it is visible in the evidence health record.
The guard does not require a clean workspace; it prevents silent count drift.
