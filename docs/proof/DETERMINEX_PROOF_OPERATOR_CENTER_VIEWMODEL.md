# Proof / Operator Center View-Model

> Locked under
> `locks/sentinel/DETERMINEX_PROOF_OPERATOR_CENTER_VIEWMODEL_LOCK_001.json`.

Read-only, non-authorizing operator surface.

## 10 required sections

- `evidence_ledger`
- `current_workspace_status`
- `source_mutation_gates`
- `verifier_status`
- `rollback_status`
- `operator_actions`
- `programbench_provenance_status_read_only`
- `training_eligibility_status`
- `claim_safety_status`
- `blocked_actions`

## Hard rules

| Rule | Refusal |
|---|---|
| `training_eligible_now=True` | `BLOCKED_TRAINING_CONFUSION` |
| `training_status_text` missing "false" / "remains false" | `BLOCKED_TRAINING_CONFUSION` |
| `blocked_actions_visible=False` | `BLOCKED_ACTION_HIDDEN` |
| Empty `blocked_actions_text` | `BLOCKED_ACTION_HIDDEN` |
| `OperatorAction.kind="grant"` | `BLOCKED_AUTHORITY_CONFUSION` |
| Visible action without `routes_to` external workflow | `BLOCKED_AUTHORITY_CONFUSION` |
| `source_mutation_authorized_now=True` on this surface | `BLOCKED_AUTHORITY_CONFUSION` |
| `programbench_provenance_read_only=False` | `BLOCKED_AUTHORITY_CONFUSION` |

The operator center **shows** state; it does not change it. Apply
gates are authoritative. ProgramBench/provenance is a read-only
mirror from the Codex lane.
