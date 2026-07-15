# React Demo Navigation — Happy / Blocked Path

> Locked under
> `locks/sentinel/DETERMINEX_REACT_DEMO_NAVIGATION_HAPPY_BLOCKED_PATH_LOCK_001.json`.

Rung 3. Cross-panel coverage that asserts the live shell shows
BOTH paths clearly.

## Happy path

- **Idea Lab** workflow panel surfaces `VERIFIED_WORKING_LOCAL_APP`.
- **Idea Lab verified-demo-status** renders "verified ONLY for this
  fixture demo path" when Codex evidence is available, or an
  "Awaiting Codex reconciliation" banner when it is not.
- **Splash demo** marks 2 happy steps (`idea_lab`, `repo_clinic`).

## Blocked path

- **Idea Lab**: `WORKING_DISABLED_NO_VERIFIER_EVIDENCE` when verifier
  evidence is missing.
- **Repo Clinic**: `VERIFIER_MISSING` badge.
- **Maintenance Bay**: `UPDATED_LABEL_DISABLED_NO_VERIFIER`.
- **Splash demo**: blocked-marker step (`maintenance_bay`).
- **Loader**: rejects pre-smoke verified-working-local-app claims;
  rejects broad-claim phrase insertions anywhere in evidence.

## Teaching note

`LearningStudioPanel` exposes `teaching-window-blocked-reason` and
the captions "Learning cannot approve a patch", "Learning cannot
mark repair success", "Learning cannot mutate source".

## Proof view

`ProofOperatorCenterPanel` surfaces evidence ledger, training-false
badge (`data-training-eligible="false"`), operator actions with
`data-kind="request"` (never grant), and a visible blocked-actions
list.
