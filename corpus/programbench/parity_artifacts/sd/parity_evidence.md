# ProgramBench Parity Evidence - sd

- generated_at: `2026-06-11T22:59:00+00:00`
- raw_report: `corpus\programbench\locked\chmln__sd.87d1ba5\eval_report.json`
- raw_report_sha256: `e8717c076ca339f6e6d587d407d7571a28dc9e5bcac7a37022d1b747f95fce0e`
- upstream_commit: `87d1ba5b3401329a07c1874e49a822026e1cbf3f`
- verdict: `TIER_B_NEEDS_REFERENCE_RUN`
- counts: passed `1728`, skipped `10`, failed/error `0`, not_run `0`, total `1738`

## Skip Census

| test id | condition | file:line | tier |
|---|---|---|---|
| `08a92821049f/tests.test_harvest.test_ambiguous_replace_ensure_styling` | Original test is ignored - TODO: wait for proper colorization | `/workspace/eval/tests/test_harvest.py:217` | TIER B |
| `08a92821049f/tests.test_harvest.test_correctly_fails_on_unreadable_file` | Test requires non-root user for permission checks | `/workspace/eval/tests/test_harvest.py:330` | TIER B |
| `08a92821049f/tests.test_harvest.test_reports_errors_on_atomic_file_swap_creation_failure` | Test requires non-root user for permission checks | `/workspace/eval/tests/test_harvest.py:374` | TIER B |
| `08a92821049f/eval.tests.test_harvest.test_ambiguous_replace_ensure_styling` | Original test is ignored - TODO: wait for proper colorization | `/workspace/eval/tests/test_harvest.py:217` | TIER B |
| `08a92821049f/eval.tests.test_harvest.test_correctly_fails_on_unreadable_file` | Test requires non-root user for permission checks | `/workspace/eval/tests/test_harvest.py:330` | TIER B |
| `08a92821049f/eval.tests.test_harvest.test_reports_errors_on_atomic_file_swap_creation_failure` | Test requires non-root user for permission checks | `/workspace/eval/tests/test_harvest.py:374` | TIER B |
| `e7da309aed82/eval.tests.test_cli.test_correctly_fails_on_unreadable_file` | root bypasses file permission restrictions | `/workspace/eval/tests/test_cli.py:161` | TIER B |
| `e7da309aed82/eval.tests.test_cli.test_reports_errors_on_atomic_file_swap_creation_failure` | root bypasses file permission restrictions | `/workspace/eval/tests/test_cli.py:186` | TIER B |
| `e7da309aed82/tests.test_cli.test_correctly_fails_on_unreadable_file` | root bypasses file permission restrictions | `/workspace/eval/tests/test_cli.py:161` | TIER B |
| `e7da309aed82/tests.test_cli.test_reports_errors_on_atomic_file_swap_creation_failure` | root bypasses file permission restrictions | `/workspace/eval/tests/test_cli.py:186` | TIER B |
