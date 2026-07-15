# Frontend Authority Visual Audit

> Locked under
> `locks/sentinel/CLAUDE_FRONTEND_AUTHORITY_VISUAL_AUDIT_LOCK_001.json`.

Remediates **CLAUDE-AUTH-012**: panels mixed authority signals.

## Eight required sections

`diagnosis`, `patch_preview`, `verifier_result`,
`approval_request`, `source_mutation_status`, `rollback_status`,
`evidence_status`, `training_eligibility_status`.

## Audit rules

| Rule | Refusal |
|---|---|
| Required section missing | `BLOCKED_AMBIGUOUS_STATE` |
| Unknown section present | `BLOCKED_AMBIGUOUS_STATE` |
| Compound section name (`+`, `/`, `&`) | `BLOCKED_SECTION_MERGE` |
| Blocked state with `visible=False` | `BLOCKED_BLOCKED_STATE_HIDDEN` |
| Blocked state with empty `blocked_text` | `BLOCKED_BLOCKED_STATE_HIDDEN` |
| Success state in a required-caption section with empty caption | `BLOCKED_MISSING_NEGATIVE_AUTHORITY` |

## Sections that MUST carry a "does NOT authorize" caption

- `diagnosis` — "diagnosis ≠ approval"
- `patch_preview` — "preview ≠ apply"
- `verifier_result` — "verifier ran on temp workspace"
- `approval_request` — "approval ≠ source mutation"
- `evidence_status` — "evidence is a record"
- `training_eligibility_status` — "training remains FALSE"

## Sections exempted from the caption rule

- `source_mutation_status` — its green state IS the answer
- `rollback_status` — its green state IS the answer

## Scope

The audit operates on a backend-supplied list of `SectionState`
entries. It does NOT render or screenshot the frontend. A separate
wiring rung builds those entries from real React components.
