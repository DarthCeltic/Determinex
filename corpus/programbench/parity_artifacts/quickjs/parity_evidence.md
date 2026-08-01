# ProgramBench Parity Evidence - quickjs

- generated_at: `2026-06-11T22:58:57+00:00`
- raw_report: `corpus\programbench\locked\quickjs\eval_report.json`
- raw_report_sha256: `40f71a86edee9429cf748b58f0b1f4a1377c68b73169c93937f93c61c892171b`
- upstream_commit: `d7ae12ae71dfd6ab2997527d295014a8996fa0f9`
- verdict: `TIER_B_NEEDS_REFERENCE_RUN`
- counts: passed `3038`, skipped `6`, failed/error `0`, not_run `0`, total `3044`

## Skip Census

| test id | condition | file:line | tier |
|---|---|---|---|
| `e1d7a4e20e53/tests.test_harvest.test_bjson` | bjson.so not available - shared library not built | `/workspace/eval/tests/test_harvest.py:151` | TIER B |
| `e1d7a4e20e53/tests.test_libc_http_url_gaps.test_basic_http_get` | gold-env-limitation: requires reliable HTTP server for status code testing (200, 404) | `/workspace/eval/tests/test_libc_http_url_gaps.py:117` | TIER B |
| `e1d7a4e20e53/tests.test_libc_http_url_gaps.test_http_status_codes` | gold-env-limitation: requires reliable HTTP server for status code testing (200, 404) | `/workspace/eval/tests/test_libc_http_url_gaps.py:279` | TIER B |
| `e1d7a4e20e53/tests.test_libc_http_url_gaps.test_header_parsing` | gold-env-limitation: requires reliable HTTP server for header parsing testing | `/workspace/eval/tests/test_libc_http_url_gaps.py:324` | TIER B |
| `e1d7a4e20e53/tests.test_libc_http_url_gaps.test_url_formats` | gold-env-limitation: requires reliable HTTP server for URL format testing | `/workspace/eval/tests/test_libc_http_url_gaps.py:532` | TIER B |
| `e1d7a4e20e53/tests.test_libc_workers_timers_async.test_timer_and_handler_interaction` | gold-env-limitation: test times out in gold environment due to event loop interaction timing | `/workspace/eval/tests/test_libc_workers_timers_async.py:528` | TIER B |
