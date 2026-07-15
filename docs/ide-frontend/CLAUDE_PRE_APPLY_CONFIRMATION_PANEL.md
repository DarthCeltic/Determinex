# Pre-Apply Confirmation Panel

> Locked under `locks/sentinel/CLAUDE_PRE_APPLY_CONFIRMATION_PANEL_LOCK_001.json`.

Remediates **CLAUDE-AUTH-015**: previously there was no clear
"this will write files" confirmation panel before source mutation.

## Five distinct UI states

| State | Means |
|---|---|
| `PRE_APPLY_UI_PREVIEW` | Show only — no execution |
| `PRE_APPLY_UI_DRY_RUN` | Temp verifier ran; real workspace untouched |
| `PRE_APPLY_UI_APPROVED` | Operator approved; no write yet |
| `PRE_APPLY_UI_SOURCE_MUTATION_AUTHORIZED` | Apply gate green-lit |
| `PRE_APPLY_UI_SOURCE_MUTATION_APPLIED` | Post-fact: write happened |

`source_mutation_authorized=True` is **only valid** in the last two
states. In any other state it triggers `BLOCKED_AUTHORITY_AMBIGUITY`.

## Required panel fields

`ui_state`, `files_affected`, `canonical_patch_body_hash`,
`diff_hash`, `verifier_status`, `rollback_snapshot_ref`,
`source_mutation_consequence_text`, `training_eligibility_text`.

When `source_mutation_authorized=True`:

- `source_mutation_consequence_text` must contain "source mutation"
  and "will write".
- `training_eligibility_text` must contain "training" and "false".

## Training never opens through the panel

`panel.training_eligible=True` → `BLOCKED_TRAINING_OPENED`.
`build_view_model()` always sets `training_eligible=False`.

## Refusal codes

| Decision | Cause |
|---|---|
| `BLOCKED_MISSING_HASH` | empty canonical_patch_body_hash or diff_hash |
| `BLOCKED_MISSING_VERIFIER` | empty verifier_status |
| `BLOCKED_MISSING_SNAPSHOT` | empty rollback_snapshot_ref past DRY_RUN |
| `BLOCKED_AUTHORITY_AMBIGUITY` | unknown ui_state, flag/state mismatch, weak warning text |
| `BLOCKED_TRAINING_OPENED` | `panel.training_eligible == True` |
