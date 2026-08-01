# Ceiling Evidence Draft - json-tui

- generated_at: `2026-06-11T22:40:45+00:00`
- eval_index_tool: `json-tui`
- eval_index_status: `ceiling_confirmed`
- best_raw_report: `T:\determinex-programbench\determinex_pb_json-tui_vbidir8\arthursonzogni__json-tui.17a22b6\arthursonzogni__json-tui.17a22b6.eval.json`
- best_raw_report_sha256: `1a19b61d245bceaac9a26d362a5a12784c8890e9032bb8e11a509504036675d8`
- best_score: `1786/1788`
- nonpassing: failed/error `2`, skipped `0`, not_run `0`

## Blocker Evidence

- Draft blocker: raw report still has nonpassing rows; examples below are evidence for driver adjudication, not final admission.

| branch | test id | status | excerpt |
|---|---|---|---|
| `fcf880d70098` | `eval.tests.test_tui_interactive.test_navigation_j_k_changes_highlight_or_cursor` | `failure` | assert 'cd /workspace\nprintf \'%s\' \'{"a":1,"b":2,"c":3,"d":4}\' / /workspace/executable\nroot@84fbfb6de5fa:/workspace# cd /workspace\nroot@84fbfb6de5fa:/workspace# printf \'%s\' \'{"a":1,"b":2,"c":3,"d":4}\' / /workspace/executable\n{\n "a": 1,\n "b": 2,\n "c": 3,\n "d": 4\n}\ |
| `fcf880d70098` | `tests.test_tui_interactive.test_navigation_j_k_changes_highlight_or_cursor` | `failure` | assert 'cd /workspace\nprintf \'%s\' \'{"a":1,"b":2,"c":3,"d":4}\' / /workspace/executable\nroot@84fbfb6de5fa:/workspace# cd /workspace\nroot@84fbfb6de5fa:/workspace# printf \'%s\' \'{"a":1,"b":2,"c":3,"d":4}\' / /workspace/executable\n{\n "a": 1,\n "b": 2,\n "c": 3,\n "d": 4\n}\ |

## Draft Verdict

- proposed_status: `ceiling_evidence_draft`
- admission_owner: `Claude/driver`
- strict_count_effect: `none`
