# IDE Frontend State Contract

> Locked under `locks/sentinel/IDE_FRONTEND_STATE_CONTRACT_LOCK_001.json`.

JSON shape the UI must render. 12 required sections. Validator surfaces
missing fields and ensures risk warnings and source-mutation-blocked
status are visible.

## Sections

`workspace`, `adapter`, `verifier`, `model_route`, `diagnosis`,
`patch_plan`, `temp_verifier`, `human_approval`, `source_apply`,
`corpus_eligibility`, `evidence`, `risk_warnings`.
