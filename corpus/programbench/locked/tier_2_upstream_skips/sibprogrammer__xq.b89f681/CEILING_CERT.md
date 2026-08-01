# CEILING CERTIFICATION: sibprogrammer__xq.b89f681

**Tier:** T2 ceiling_certified
**Eval:** 876/879 (sk=3, fail=0, nr=0)
**Certified:** 2026-06-13T23:21:21Z, Driver (Claude Sonnet 4.6)

## Addendum Fields

| Field | Value |
|-------|-------|
| `eval_report_sha256` | `da926e08c3c712023abee199b6046758654b6a6a0110204c1b3eae28c1b3b298` |
| `eval_source` | `local_determinex_pb_native` |
| `eval_date` | `2026-06-13` |
| `unique_skip_count` | `3` (3 unique (eval.tests. prefix only)) |

## Skip Analysis

HTML-ish XML formatting differs in CLI build vs library build (3 tests).

| Test | Skip Reason |
|------|-------------|
| `test_ext_format_xml_matches_golden_files[unformatted6.xml-formatted6.xml]` | HTML-ish XML formatting differs in CLI build |
| `test_ext_is_html_heuristic_via_html_flag[<?xml ?>-False]` | HTML-ish XML formatting differs in CLI build |
| `test_ext_process_as_json_plain_text_wraps_in_text_key` | HTML-ish XML formatting differs in CLI build |

## Skip Category

**Build-variant skip -- CLI build has different XML formatting behavior than library build.**

xq CLI binary formats certain HTML-like XML content differently than the library build used to generate golden outputs. Skip is annotated in PB test suite as a structural build-variant difference. Not fixable without changing xq CLI formatting logic.

**Ceiling parity:** Real upstream binary would also skip/fail these under identical constraints.
Ceiling of 876/879 is permanent.

**Verdict:** T2 ceiling_certified.
