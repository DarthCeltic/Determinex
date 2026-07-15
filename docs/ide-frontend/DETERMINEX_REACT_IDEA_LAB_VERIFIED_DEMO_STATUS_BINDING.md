# React Idea Lab Verified Demo Status Binding

> Locked under
> `locks/sentinel/DETERMINEX_REACT_IDEA_LAB_VERIFIED_DEMO_STATUS_BINDING_LOCK_001.json`.

Rung 2. Binds the live React Idea Lab panel to the Codex Idea Lab
verified Python CLI splash demo evidence.

## Pieces

- **Loader**: `scripts/ide/idea_lab_verified_demo_status.py::load(evidence_dir=None)`
- **Tauri verb**: `get_idea_lab_verified_demo_status` (read-only)
- **React component**: `frontend/src/components/ide-product-shell/IdeaLabVerifiedDemoStatus.tsx`

## Hard rules (loader)

| Condition | Decision |
|---|---|
| Evidence file absent | `AWAITING_EVIDENCE` |
| `source_mutation_authorized: true` in evidence | `BLOCKED_AUTHORITY_CONFUSION` |
| `training_eligible: true` in evidence | `BLOCKED_AUTHORITY_CONFUSION` |
| `approval_authority_granted: true` in evidence | `BLOCKED_AUTHORITY_CONFUSION` |
| `claim_boundary` missing required statements | `BLOCKED_BROAD_CLAIM` |
| Affirmative broad-claim phrase outside `blocked_path_demo` | `BLOCKED_BROAD_CLAIM` |
| `verified_working_local_app=true` without tests+smoke | `BLOCKED_AUTHORITY_CONFUSION` |

Required boundary statements:

- `Python CLI/file-data demo only`
- `not all apps`
- `not any language`
- `training remains false`

## What the React component renders

- Demo title, app class (CLI/file-data tool), target language (Python)
- Acceptance tests + smoke + verified-for-fixture-only status
- Evidence reference (path)
- Claim boundary (enumerated)
- Training-false badge
- "Ready does NOT mean authorized." caption
- "Verified only for this fixture demo path — not all apps, not all languages, not production-ready arbitrary app creation." caption
- "Training stays false (training_eligible: false)." caption

## What it never renders

`all apps`, `any language`, `all codebases`, `production-ready arbitrary`,
`training enabled`, `source_mutation_authorized: true`, `no-followup support`,
`release_ready: true`.
