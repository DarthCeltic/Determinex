# Ceiling Evidence Draft - doxygen

- generated_at: `2026-06-11T22:40:45+00:00`
- eval_index_tool: `doxygen__doxygen`
- eval_index_status: `ceiling_confirmed`
- best_raw_report: `T:\determinex-staging\pb_doxygen_input_warning_filter_v8\doxygen__doxygen.966d98e\doxygen__doxygen.966d98e.eval.json`
- best_raw_report_sha256: `679a72ee8911707d62da66628402169154e7e89ac1d9f3576f5218dfc6d73221`
- best_score: `250/261`
- nonpassing: failed/error `0`, skipped `1`, not_run `10`

## Blocker Evidence

- Draft blocker: raw report still has nonpassing rows; examples below are evidence for driver adjudication, not final admission.

| branch | test id | status | excerpt |
|---|---|---|---|
| `ffcc3ee94dc7` | `eval.tests.test_doxygen_testing_suite_externalized.test_ext_internal_dox_test_via_cli[012_012_cite.dox]` | `skipped` | Requires external 'bibtex' executable not available in this environment /workspace/eval/tests/test_doxygen_testing_suite_externalized.py:83: Requires external 'bibtex' executable not available in this environment |
| `8c618fb31ebb` | `eval.tests.test_dispatch_routing.test_generate_config_custom_name_routes_to_file_creation` | `not_run` |  |
| `8c618fb31ebb` | `eval.tests.test_dispatch_routing.test_generate_config_default_name_routes_to_doxyfile_creation` | `not_run` |  |
| `8c618fb31ebb` | `eval.tests.test_dispatch_routing.test_help_flag_equivalences` | `not_run` |  |
| `8c618fb31ebb` | `eval.tests.test_dispatch_routing.test_help_mentions_usage_patterns` | `not_run` |  |
| `8c618fb31ebb` | `eval.tests.test_dispatch_routing.test_layout_generation_dash_writes_to_stdout` | `not_run` |  |
| `8c618fb31ebb` | `eval.tests.test_dispatch_routing.test_layout_generation_default_name` | `not_run` |  |
| `8c618fb31ebb` | `eval.tests.test_dispatch_routing.test_no_args_shows_usage_or_version` | `not_run` |  |
| `8c618fb31ebb` | `eval.tests.test_dispatch_routing.test_unknown_flag_is_error` | `not_run` |  |
| `8c618fb31ebb` | `eval.tests.test_dispatch_routing.test_unknown_subcommand_like_arg_is_error` | `not_run` |  |

## Draft Verdict

- proposed_status: `ceiling_evidence_draft`
- admission_owner: `Claude/driver`
- strict_count_effect: `none`
