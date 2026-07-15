# Determinex Global Operator Action Queue

`DETERMINEX_GLOBAL_OPERATOR_ACTION_QUEUE_LOCK_001` normalizes the open operator work across Claude, Codex, and Proof Control Plane evidence.

This queue is read-only and non-authorizing. It cannot approve packets, execute Docker, run ProgramBench, import artifacts, scan artifacts, mutate source, create training rows, or create a release workflow.

## Current State

| Field | Value |
| --- | --- |
| queue status | `GLOBAL_OPERATOR_ACTION_QUEUE_WRITTEN` |
| integrity status | `GLOBAL_OPERATOR_ACTION_QUEUE_INTEGRITY_PASSED` |
| actions total | `17` |
| source action count | `17` |
| can execute any | `false` |
| can mutate source any | `false` |
| can write training row any | `false` |

## Priority Classes

- `P0_SECURITY_OR_AUTHORITY_BLOCKER`
- `P1_REAL_USER_UNBLOCKER`
- `P2_ARTIFACT_OR_PROVENANCE_INPUT`
- `P3_STATUS_OR_REVIEW`
- `P4_OPTIONAL_IMPROVEMENT`

## Top Current Actions

1. Supply Doxygen operator security policy admission.
2. Supply real human approval packet for the Claude source mutation path, still followed by rollback/apply gates.
3. Supply or confirm local model configuration for local-only model use.
4. Supply exact artifact import provenance packets for the 10 Batch001 metadata-admitted ProgramBench targets.
5. Resolve proof gaps such as SBOM and scan evidence after artifact import.

## Invariants

Every action has:

- `can_execute: false`
- `can_mutate_source: false`
- `can_write_training_row: false`
- explicit `authority_not_granted`
- a next gate that must run separately

Packet templates, proof gaps, and queue entries are requests or status objects only. They are not approvals.

## Reproduction

```powershell
.\.venv\Scripts\python.exe scripts\status\global_operator_action_queue.py --json
.\.venv\Scripts\python.exe -m pytest tests\status\test_determinex_global_operator_action_queue_lock.py -q
```
