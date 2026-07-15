# React Release Readiness Blocker Panel

> Locked under
> `locks/sentinel/DETERMINEX_REACT_RELEASE_READINESS_BLOCKER_PANEL_LOCK_001.json`.

Rung 4. Surfaces every active release blocker instead of hiding it.

## Eleven flags (all compile-time constants)

- `releaseReady = false` + visible `release_ready: false` badge
- `publicReleaseScrubRequired = true`
- `installDemoWorkflowPending = true`
- `repoScrubPending = true`
- `claimLedgerActive = true` (references `CLAUDE_PUBLIC_CLAIMS_LEDGER_LOCK_001`)
- `evidenceReconciliationStatus` prop (default mentions `WORKSPACE_EVIDENCE_RECONCILIATION_PASSED`)
- `broadPublicClaimsGranted = false`
- `trainingEligible = false`
- `programbenchExecutedFromClaudeLane = false`
- `programbenchImportedFromClaudeLane = false`
- `programbenchScannedFromClaudeLane = false`
- `sourceMutationAuthorized = false`

## Captions

- "This panel REPORTS status. It does NOT authorize release, source mutation, or training."
- "Ready does NOT mean authorized."
- "Training stays false (training_eligible: false)."

## Hard rules

- Panel does NOT invoke `invokeUnifiedProductCommand` or any
  mutating verb.
- Panel does NOT allow `props.releaseReady` / `if (props.releaseReady)`
  / `releaseReadyProp` etc. to override the compile-time flag.
- `data-release-ready={releaseReady}` and `data-training-eligible="false"`
  are stable for snapshot inspection.
