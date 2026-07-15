# Determinex Global Operator Action Queue Dedup Reconciliation

`DETERMINEX_GLOBAL_OPERATOR_ACTION_QUEUE_DEDUP_RECONCILIATION_LOCK_001` is a
read-only reconciliation layer over the existing global operator action queue.

It does not approve packets, execute tools, mutate source, import artifacts, or
write training rows. It groups duplicate actions by lane, subject, action type,
and next gate, then preserves all source action ids and evidence references on a
single consolidated action.

Current reconciliation:

```text
actions_before: 17
actions_after: 16
deduplicated_groups: 1
can_execute_any: false
can_mutate_source_any: false
can_write_training_row_any: false
```

The duplicate group is the Doxygen security policy admission request. It remains
a request, not an approval grant.
