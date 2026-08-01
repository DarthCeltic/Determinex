# Ceiling Evidence Draft - igrep

- generated_at: `2026-06-11T22:40:45+00:00`
- eval_index_tool: `igrep`
- eval_index_status: `ceiling_confirmed`
- best_raw_report: `T:\determinex-programbench\determinex_pb_igrep_vbidir7\konradsz__igrep.aa75630\konradsz__igrep.aa75630.eval.json`
- best_raw_report_sha256: `b201e063a42ddf5fdc09dc1b16386199053cbaf8a9e994e26f8f880702ff5422`
- best_score: `1094/1153`
- nonpassing: failed/error `0`, skipped `0`, not_run `59`

## Blocker Evidence

- Pattern-002 check: `collection-wall-suspected`. not_run count is `59`; route to pattern lane unless driver has stronger non-collection proof.

| branch | test id | status | excerpt |
|---|---|---|---|
| `df37316a82f6` | `tests.test_tui_app_sorting.test_search_popup_arrow_navigation` | `not_run` |  |
| `df37316a82f6` | `tests.test_tui_app_sorting.test_search_popup_char_operations` | `not_run` |  |
| `df37316a82f6` | `tests.test_tui_app_sorting.test_search_popup_enter_applies_pattern` | `not_run` |  |
| `df37316a82f6` | `tests.test_tui_app_sorting.test_search_popup_f5_key` | `not_run` |  |
| `df37316a82f6` | `tests.test_tui_app_sorting.test_sort_by_atime` | `not_run` |  |
| `df37316a82f6` | `tests.test_tui_app_sorting.test_sort_by_ctime` | `not_run` |  |
| `df37316a82f6` | `tests.test_tui_app_sorting.test_sort_by_name_toggle` | `not_run` |  |
| `df37316a82f6` | `tests.test_tui_edge_cases.test_empty_directory` | `not_run` |  |
| `df37316a82f6` | `tests.test_tui_edge_cases.test_large_result_set_scrolling` | `not_run` |  |
| `df37316a82f6` | `tests.test_tui_edge_cases.test_no_matches_found` | `not_run` |  |

## Draft Verdict

- proposed_status: `ceiling_evidence_draft`
- admission_owner: `Claude/driver`
- strict_count_effect: `none`
