# Determinex Cross-Lane Authority Boundary

`DETERMINEX_CROSS_LANE_AUTHORITY_BOUNDARY_LOCK_001` joins the Claude and Codex
lanes under a read-only boundary check.

The boundary consumes:

- Claude authority leak remediation final state.
- Codex global operator queue dedup record.
- ProgramBench per-target graph.
- Unified status and unified evidence graph.
- Global training eligibility guard.
- Proof-control final state.

The lock verifies that readiness remains separate from authority. Human approval
does not authorize ProgramBench execution. ProgramBench policy admission does not
authorize IDE source mutation. Local model admission does not authorize source
mutation by itself. Artifact metadata and import requests do not authorize import,
scan, execution, or training.

Current state:

```text
status: CROSS_LANE_AUTHORITY_BOUNDARY_PASSED
source_mutation_authorized: false
artifact_import_authorized: false
programbench_execution_authorized: false
proof_execution_authorized: false
approval_authority_granted: false
training_eligible: false
can_write_training_row_any: false
```

Deferred Claude findings remain visible and non-authorizing.
