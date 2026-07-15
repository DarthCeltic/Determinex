# React Proof / Operator Center Panel

> Locked under
> `locks/sentinel/DETERMINEX_REACT_PROOF_OPERATOR_CENTER_PANEL_LOCK_001.json`.

Rung 7. Read-only operator surface at
`frontend/src/components/ide-product-shell/ProofOperatorCenterPanel.tsx`.

## Required sections (10)

`evidence-ledger-status`, `workspace-status`,
`source-mutation-gates`, `verifier-status`, `rollback-status`,
`operator-actions`, `programbench-status`, `training-status`,
`claim-safety-status`, `blocked-actions`.

## Hard rules

- Training badge: `data-training-eligible="false"` and reads
  `training_eligible: false (remains false)`.
- Operator actions list items: `data-kind="request"` + explicit
  `data-routes-to`. No `data-kind="grant"` anywhere.
- ProgramBench / provenance text: "read-only mirror from Codex lane",
  with caption "ProgramBench / provenance is read-only from the
  Claude lane."
- Blocked actions text (default) mentions: source apply blocked,
  training blocked, ProgramBench writes blocked.
- Source-mutation gate list visible: "approval + verifier + snapshot
  + body hash + symlink refusal".
- Caption "Operator queue request is a REQUEST, not a grant."
