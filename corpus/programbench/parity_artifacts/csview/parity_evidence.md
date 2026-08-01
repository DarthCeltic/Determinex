# ProgramBench Parity Evidence - csview

- generated_at: `2026-06-11T22:58:56+00:00`
- raw_report: `corpus\programbench\locked\csview\eval_report.json`
- raw_report_sha256: `68ba45e2172e9b1d4f6bf23520816cf0a0bc79e5367ade2b2dfcbab39c563f11`
- upstream_commit: `8ac4de0ae4540461fd9e33c13e4b47ba21967995`
- verdict: `TIER_B_NEEDS_REFERENCE_RUN`
- counts: passed `347`, skipped `1`, failed/error `0`, not_run `0`, total `348`

## Skip Census

| test id | condition | file:line | tier |
|---|---|---|---|
| `b3b22ece5568/eval.tests.test_csview_io.test_unreadable_file_permission_denied_exit_1` | running as root; cannot reliably make file unreadable | `/workspace/eval/tests/test_csview_io.py:96` | TIER B |
