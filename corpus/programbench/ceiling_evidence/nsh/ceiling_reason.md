# Ceiling Evidence Draft - nsh

- generated_at: `2026-06-11T22:40:45+00:00`
- eval_index_tool: `nsh`
- eval_index_status: `ceiling_confirmed`
- best_raw_report: `T:\determinex-programbench\determinex_pb_nsh_vbidir5\nuta__nsh.bdd0702\nuta__nsh.bdd0702.eval.json`
- best_raw_report_sha256: `c531e7e3b7ba4e2e3f12702b459651cba2e51be95a2e625c9cbc2a8f6148aeb8`
- best_score: `3740/3778`
- nonpassing: failed/error `0`, skipped `0`, not_run `38`

## Blocker Evidence

- Draft blocker: raw report still has nonpassing rows; examples below are evidence for driver adjudication, not final admission.

| branch | test id | status | excerpt |
|---|---|---|---|
| `77c6dc146522` | `eval.tests.test_interactive_features.test_interactive_cd` | `not_run` |  |
| `77c6dc146522` | `eval.tests.test_interactive_features.test_interactive_echo` | `not_run` |  |
| `77c6dc146522` | `eval.tests.test_interactive_features.test_interactive_multiline` | `not_run` |  |
| `77c6dc146522` | `eval.tests.test_interactive_features.test_interactive_pwd` | `not_run` |  |
| `77c6dc146522` | `eval.tests.test_interactive_features.test_interactive_variable` | `not_run` |  |
| `7a4302453af8` | `tests.test_tui_completion.test_history_down_arrow_navigation` | `not_run` |  |
| `7a4302453af8` | `tests.test_tui_completion.test_history_ignores_duplicate_consecutive` | `not_run` |  |
| `7a4302453af8` | `tests.test_tui_completion.test_history_ignores_short_commands` | `not_run` |  |
| `7a4302453af8` | `tests.test_tui_completion.test_history_preserves_user_input` | `not_run` |  |
| `7a4302453af8` | `tests.test_tui_completion.test_history_up_arrow_navigation` | `not_run` |  |

## Draft Verdict

- proposed_status: `ceiling_evidence_draft`
- admission_owner: `Claude/driver`
- strict_count_effect: `none`
