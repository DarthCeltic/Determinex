# React Idea Lab Panel

> Locked under `locks/sentinel/DETERMINEX_REACT_IDEA_LAB_PANEL_LOCK_001.json`.

Rung 3. New-project workflow at
`frontend/src/components/ide-product-shell/IdeaLabPanel.tsx`.

## Required sections

- `idea-lab-idea-intake-status`
- `idea-lab-support-check-status`
- `idea-lab-blueprint-status`
- `idea-lab-scaffold-status`
- `idea-lab-tests-status`
- `idea-lab-build-test-verifier-status`
- `idea-lab-smoke-status`
- `idea-lab-evidence-status`
- `idea-lab-training-eligibility-status`
- `idea-lab-unsupported-caveat-status`

## Hard rules

- **Build It** button is `disabled={!buildItEnabled}` where
  `buildItEnabled = supportCheckPassed`.
- **Working** label requires `buildVerifierPassed && testsPassed && smokePassed`;
  otherwise reads `WORKING_DISABLED_NO_VERIFIER_EVIDENCE`.
- Generated-but-unverified state visible as `GENERATED_UNVERIFIED`.
- Cost/setup caveats visible: external setup is the operator's responsibility.
- Training status always reads `training_eligible: false (remains false)`.
- Forbidden text refused by tests: "your app is working", "fixed!",
  "deployment ready", "production-ready", "all apps supported".
