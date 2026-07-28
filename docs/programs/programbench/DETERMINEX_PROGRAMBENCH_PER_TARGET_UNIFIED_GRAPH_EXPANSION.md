# Determinex ProgramBench Per-Target Unified Graph Expansion

`DETERMINEX_PROGRAMBENCH_PER_TARGET_UNIFIED_GRAPH_EXPANSION_LOCK_001` expands the
Codex ProgramBench portion of the unified graph from aggregate Batch001 state
into per-target nodes.

The graph includes:

- Doxygen, with artifact authority present and execution blocked pending
  operator security policy admission.
- Ten Batch001 targets with exact manifest digest metadata admitted,
  artifact import still required, scan pending artifact import, execution
  false, and training eligibility false.

Integrity checks:

```text
metadata_to_execution_blocked: true
import_request_to_authorization_blocked: true
scan_queue_to_execution_blocked: true
blocked_task_to_training_blocked: true
```

This lock does not import artifacts, run scans, run ProgramBench, authorize
execution, grant approvals, or create training rows.
