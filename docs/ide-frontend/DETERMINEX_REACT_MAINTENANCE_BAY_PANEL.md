# React Maintenance Bay Panel

> Locked under
> `locks/sentinel/DETERMINEX_REACT_MAINTENANCE_BAY_PANEL_LOCK_001.json`.

Rung 5. Maintenance / update panel at
`frontend/src/components/ide-product-shell/MaintenanceBayPanel.tsx`.

## Required sections (9)

`request-type`, `risk-classification`, `impact-plan`,
`quarantined-changes`, `compatibility-verifier-required`,
`approval-requirement`, `post-apply-verifier`, `rollback-evidence`,
`training-eligibility`.

## Hard rules

- **UPDATED label** requires
  `compatibilityVerifierPresent && compatibilityVerifierPassed && approvalPresent && postApplyVerifierPassed`;
  otherwise reads `UPDATED_LABEL_DISABLED_NO_VERIFIER`.
- Risk classification must be visible for `dependency_update` and
  `security_fix`.
- Advisory / scanner status caveated; otherwise `ADVISORY_UNCAVEATED`
  is shown.
- Caption: "Proposed is NOT applied; quarantined is NOT verified."
- Training reads `false (remains false)`.
