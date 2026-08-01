# ProgramBench Parity Evidence - ripgrep

- generated_at: `2026-06-11T22:58:55+00:00`
- raw_report: `corpus\programbench\locked\ripgrep\eval_report.json`
- raw_report_sha256: `8678dfec59ccf67933e594c47b0212790029e9e45c67ed65f48cb873cea8d7df`
- upstream_commit: `3b7fd442a6f3aa73f650e763d7cbb902c03d700e`
- verdict: `TIER_B_NEEDS_REFERENCE_RUN`
- counts: passed `2536`, skipped `2`, failed/error `0`, not_run `0`, total `2538`

## Skip Census

| test id | condition | file:line | tier |
|---|---|---|---|
| `d6be781e3e94/tests.test_walk_errors.test_files_with_no_read_permission_as_non_root` | Test requires non-root user (root bypasses permissions) | `/workspace/eval/tests/test_walk_errors.py:502` | TIER B |
| `f78add528cee/eval.tests.test_rg_behavior.test_line_number_default_and_no_filename_behavior` | test_line_number_default_and_no_filename_behavior depends on test_basic_recursive_search | `/usr/local/lib/python3.10/dist-packages/pytest_dependency.py:101` | TIER B |
