# Ceiling Evidence Draft - richgo

- generated_at: `2026-06-11T22:40:45+00:00`
- eval_index_tool: `kyoh86__richgo`
- eval_index_status: `ceiling_confirmed`
- best_raw_report: `T:\determinex-staging\programbench_candidate\kyoh86__richgo.313114f\kyoh86__richgo.313114f.eval.json`
- best_raw_report_sha256: `f5e3afd557e978195f3da1d86987d442b88eff049067bade8c310d4994f61aba`
- best_score: `786/950`
- nonpassing: failed/error `0`, skipped `1`, not_run `163`

## Blocker Evidence

- Pattern-002 check: `collection-wall-suspected`. not_run count is `163`; route to pattern lane unless driver has stronger non-collection proof.

| branch | test id | status | excerpt |
|---|---|---|---|
| `7e3fefff015d` | `eval.tests.test_basic_invocation.TestBasicInvocation.test_help_flag_shows_go_help` | `not_run` |  |
| `7e3fefff015d` | `eval.tests.test_basic_invocation.TestBasicInvocation.test_help_test_command` | `not_run` |  |
| `7e3fefff015d` | `eval.tests.test_basic_invocation.TestBasicInvocation.test_no_arguments_shows_go_help` | `not_run` |  |
| `7e3fefff015d` | `eval.tests.test_basic_invocation.TestBasicInvocation.test_version_command_shows_go_version` | `not_run` |  |
| `7e3fefff015d` | `eval.tests.test_basic_invocation.TestPassthrough.test_fmt_command_passthrough` | `not_run` |  |
| `7e3fefff015d` | `eval.tests.test_basic_invocation.TestTestFilterMode.test_testfilter_basic_fail` | `not_run` |  |
| `7e3fefff015d` | `eval.tests.test_basic_invocation.TestTestFilterMode.test_testfilter_basic_pass` | `not_run` |  |
| `7e3fefff015d` | `eval.tests.test_basic_invocation.TestTestFilterMode.test_testfilter_build_error` | `not_run` |  |
| `7e3fefff015d` | `eval.tests.test_basic_invocation.TestTestFilterMode.test_testfilter_coverage_output` | `not_run` |  |
| `7e3fefff015d` | `eval.tests.test_basic_invocation.TestTestFilterMode.test_testfilter_multiline_output` | `not_run` |  |

## Draft Verdict

- proposed_status: `ceiling_evidence_draft`
- admission_owner: `Claude/driver`
- strict_count_effect: `none`
