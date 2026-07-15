# User Levels & Teaching Windows

> Locked under
> `locks/sentinel/DETERMINEX_UNIFIED_USER_LEVELS_AND_TEACHING_WINDOWS_LOCK_001.json`.

Eight user levels. Each declares: default explanations, level of
detail, warnings/caveats, UI complexity (minimal / moderate /
full), teaching windows, suggested next action, what NOT to hide,
what NOT to over-explain, and the three flags that the hard rules
test against.

## Eight levels

`beginner_no_experience`, `learner`, `vibe_coder`,
`junior_developer`, `professional_developer`, `maintainer`,
`security_conscious_operator`, `power_user`.

## Hard rules (all 8 levels)

- `proof_status_visible = True`
- `authority_gates_active = True`
- `teaching_window_explains_blocked_reason = True`
- `what_not_to_hide` mentions "training" and "false"

| Refusal | Cause |
|---|---|
| `BLOCKED_PROOF_HIDDEN` | a level hides proof status, drops training-stays-false from what_not_to_hide, or is missing entirely |
| `BLOCKED_AUTHORITY_BYPASS` | a level disables authority gates or teaching windows that explain why something is blocked |

Beginner mode does NOT hide proof. Power-user mode does NOT
loosen gates. Professional mode does NOT bypass proof.
