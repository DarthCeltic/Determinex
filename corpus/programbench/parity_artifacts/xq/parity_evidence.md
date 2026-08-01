# ProgramBench Parity Evidence - xq

- generated_at: `2026-06-11T22:58:56+00:00`
- raw_report: `corpus\programbench\locked\xq\eval_report.json`
- raw_report_sha256: `da926e08c3c712023abee199b6046758654b6a6a0110204c1b3eae28c1b3b298`
- upstream_commit: `b89f6811d339cc491293c4147e13bb74324d49c5`
- verdict: `TIER_B_NEEDS_REFERENCE_RUN`
- counts: passed `876`, skipped `3`, failed/error `0`, not_run `0`, total `879`

## Skip Census

| test id | condition | file:line | tier |
|---|---|---|---|
| `007a233a3328/eval.tests.test_e2e_xq.test_ext_format_xml_matches_golden_files[unformatted6.xml-formatted6.xml]` | HTML-ish XML formatting differs in CLI build | `extra.message` | TIER B |
| `007a233a3328/eval.tests.test_e2e_xq.test_ext_is_html_heuristic_via_html_flag[<?xml ?>-False]` | stdin XML header can panic in current CLI | `extra.message` | TIER B |
| `007a233a3328/eval.tests.test_e2e_xq.test_ext_process_as_json_plain_text_wraps_in_text_key` | -j on plain text not supported by current CLI | `extra.message` | TIER B |
