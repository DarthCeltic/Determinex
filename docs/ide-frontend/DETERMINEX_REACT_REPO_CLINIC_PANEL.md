# React Repo Clinic Panel

> Locked under `locks/sentinel/DETERMINEX_REACT_REPO_CLINIC_PANEL_LOCK_001.json`.

Rung 4. Existing-repo diagnose / repair / refactor / update panel
at `frontend/src/components/ide-product-shell/RepoClinicPanel.tsx`.

## Required sections (12)

`repo-analysis-status`, `toolchain-status`, `verifier-status`,
`diagnosis-status`, `quarantined-patch-status`, `temp-verifier-status`,
`approval-requirement`, `source-mutation-status`,
`post-apply-verifier-status`, `rollback-status`, `evidence-status`,
`training-eligibility-status`.

## Hard rules

- `REPAIR_VERIFIED` badge requires **both** `sourceMutationApplied`
  AND `postApplyVerifierPassed`; otherwise reads
  `FIXED_LABEL_DISABLED_NO_POST_APPLY_EVIDENCE`.
- Caption: **"Diagnosis does NOT authorize source mutation."**
- Caption: **"Local model admission does NOT authorize source mutation."**
- Approval status rendered with **"distinct from approval status"** wording.
- `VERIFIER_MISSING` / `TOOLCHAIN_MISSING` badges visible when applicable.
- Training status reads `training_eligible: false (remains false)`.
