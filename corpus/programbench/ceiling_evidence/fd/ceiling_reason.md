# Ceiling Evidence Draft - fd

- generated_at: `2026-06-11T22:40:44+00:00`
- eval_index_tool: `sharkdp__fd`
- eval_index_status: `ceiling_confirmed`
- best_raw_report: `T:\determinex-programbench\hetzner_results\hetzner_fd_argv_001\results\sharkdp__fd.40d8eb3.eval.json`
- best_raw_report_sha256: `6cabcbbd071ec0727c3bed59ce3f82135dfc71a7c9b428b01cbe23635e17042e`
- best_score: `1262/1825`
- nonpassing: failed/error `9`, skipped `7`, not_run `547`

## Blocker Evidence

- Draft blocker: raw report still has nonpassing rows; examples below are evidence for driver adjudication, not final admission.

| branch | test id | status | excerpt |
|---|---|---|---|
| `035fc64252a5` | `eval.tests.test_basic_invocation.test_empty_directory` | `not_run` |  |
| `035fc64252a5` | `eval.tests.test_basic_invocation.test_empty_pattern_matches_all` | `not_run` |  |
| `035fc64252a5` | `eval.tests.test_basic_invocation.test_help_output` | `not_run` |  |
| `035fc64252a5` | `eval.tests.test_basic_invocation.test_help_short_flag` | `not_run` |  |
| `035fc64252a5` | `eval.tests.test_basic_invocation.test_multiple_path_arguments` | `not_run` |  |
| `035fc64252a5` | `eval.tests.test_basic_invocation.test_no_arguments_lists_files` | `not_run` |  |
| `035fc64252a5` | `eval.tests.test_basic_invocation.test_nonexistent_directory` | `not_run` |  |
| `035fc64252a5` | `eval.tests.test_basic_invocation.test_pattern_and_path_search` | `not_run` |  |
| `035fc64252a5` | `eval.tests.test_basic_invocation.test_pattern_only_search` | `not_run` |  |
| `035fc64252a5` | `eval.tests.test_basic_invocation.test_pattern_starting_with_dash` | `not_run` |  |

## Draft Verdict

- proposed_status: `ceiling_evidence_draft`
- admission_owner: `Claude/driver`
- strict_count_effect: `none`
