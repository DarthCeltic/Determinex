# Claude IDE Hygiene — Final State

> Locked under `locks/sentinel/CLAUDE_IDE_HYGIENE_FINAL_STATE_LOCK_001.json`.

Finale of `DETERMINEX_CLAUDE_IDE_AUTHORITY_AND_CLAIMS_HYGIENE_SERIES`.

`scripts/repair/claude_ide_hygiene_final_state.evaluate(repo_root)`
reads the eight prior rungs' lock manifests on disk and produces
the campaign's terminal state record.

## Eight dimensions

| Dimension | Lock |
|---|---|
| `ready_authorized_language` | `CLAUDE_AUTH_005_READY_AUTHORIZED_LANGUAGE_LOCK_001` |
| `operator_identity_bounding` | `CLAUDE_OPERATOR_IDENTITY_BOUNDING_LOCK_001` |
| `approval_replay_staleness` | `CLAUDE_APPROVAL_REPLAY_AND_STALENESS_LOCK_001` |
| `pre_apply_confirmation` | `CLAUDE_PRE_APPLY_CONFIRMATION_PANEL_LOCK_001` |
| `config_root_allowlist` | `CLAUDE_CONFIG_ROOT_ALLOWLIST_LOCK_001` |
| `frontend_authority_visuals` | `CLAUDE_FRONTEND_AUTHORITY_VISUAL_AUDIT_LOCK_001` |
| `public_claims_ledger` | `CLAUDE_PUBLIC_CLAIMS_LEDGER_LOCK_001` |
| `demo_script` | `CLAUDE_PROOF_BEFORE_MUTATION_DEMO_SCRIPT_LOCK_001` |

## Aggregate invariants

- `source_mutation_authorized: false` (gates remain in place)
- `training_eligible: false` (no Claude lane lock opens training)
- `release_ready: false` — `public_release_scrub_required`
- `demo_ready: true` (rung-8 demo script is locked and passes)
- `forge_status: planned_research_track`
- `mobile_console_status: planned_research_track`

## Deferred findings

- `CLAUDE-AUTH-010` — evidence index in-place mutability (Codex lane)
- `CLAUDE-AUTH-017` — cross-lane operator action queue (Codex lane)

## Next recommended rung

`release_readiness_install_demo_scrub`.
