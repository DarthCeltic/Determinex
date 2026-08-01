# Action Sheet — astaxie__bat.17d1080

**Current:** 26.45%  (464/1754)
**Pass / Fail / Skip:** 464 / 903 / 13
**Gap to 100%:** 73.55 percentage points (1290 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_coverage_investigation.TestUnreachableCodeDocumentation.test_bench_csv_mode_dead_code`
  - reason: Documented as dead code - no CLI trigger exists
- `tests.test_coverage_investigation.TestUnreachableCodeDocumentation.test_utils_to_real_type_parsing_bug`
  - reason: Documented as unreachable due to parsing bug
- `tests.test_coverage_investigation.TestUnreachableCodeDocumentation.test_filter_unreachable_control_flow`
  - reason: Documented as unreachable control flow
- `tests.test_coverage_investigation.TestUnreachableCodeDocumentation.test_windows_specific_code_platform_guard`
  - reason: Documented as platform-specific Windows code
- `tests.test_coverage_investigation.TestUnreachableCodeDocumentation.test_httplib_library_only_methods`
  - reason: Documented as library-only methods not exposed via CLI
- *(... 8 more skipped)*

## Failure clusters

903 failed tests grouped into 19 buckets (sorted by count).

### `other_assertion` — 477 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_additional_coverage.test_url_with_port`
  > AssertionError: assert b'args' in b'{\n{\ngzipped\n{\n{\nequation\n{\nX-URI\n'
  >  +  where b'{\n{\ngzipped\n{\n{\nequation\n{\nX-URI\n' = <conftest.RunResult object at 0x7f66958cd6f0>.stdout
- `tests.test_additional_coverage.test_long_field_value`
  > AssertionError: assert b'long' in b''
  >  +  where b'' = <conftest.RunResult object at 0x7f6696386b90>.stdout
- `tests.test_additional_coverage.test_many_fields`
  > AssertionError: assert b'field0' in b''
  >  +  where b'' = <conftest.RunResult object at 0x7f66956356f0>.stdout
- *(... 474 more in this cluster)*

### `json_output_missing_or_bad` — 130 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `tests.test_bat_final.test_url_with_host_only_normalizes_to_root_path`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_bat_final.test_custom_user_agent_header`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_bat_gaps.test_custom_header_in_request`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- *(... 127 more in this cluster)*

### `rc_mismatch_got7_want2` — 108 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic.test_no_arguments_shows_usage`
  > assert 7 == 2
  >  +  where 7 = <conftest.RunResult object at 0x7f669681c130>.returncode
- `tests.test_basic_invocation.test_no_args_shows_usage`
  > AssertionError: assert 7 == 2
  >  +  where 7 = CompletedProcess(args=['/workspace/executable'], returncode=7, stdout=b'', stderr=b'error: cannot connect to http://127.0.0.1:8080/: <urlopen error [Errno 111] Connection refused>\n').re
- `tests.test_argument_parsing.TestNoArguments.test_no_arguments_shows_help`
  > assert 7 == 2
- *(... 105 more in this cluster)*

### `rc_mismatch_got0_want2` — 54 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_argument_parsing.TestUnknownFlags.test_unknown_flag_shows_help`
  > assert 0 == 2
- `tests.test_argument_parsing.TestBooleanFlags.test_bench_flag_without_url[-bench]`
  > assert 0 == 2
- `tests.test_argument_parsing.TestBooleanFlags.test_bench_flag_without_url[-b]`
  > assert 0 == 2
- *(... 51 more in this cluster)*

### `rc_unexpected_zero` — 28 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_auth_ssl_proxy.test_proxy_flag_format`
  > assert 0 != 0
  >  +  where 0 = <conftest.RunResult object at 0x7f6695456a10>.returncode
- `tests.test_auth_ssl_proxy.test_proxy_with_credentials`
  > assert 0 != 0
  >  +  where 0 = <conftest.RunResult object at 0x7f66963a2140>.returncode
- `tests.test_edge_cases.test_connection_refused_error`
  > assert 0 != 0
  >  +  where 0 = <conftest.RunResult object at 0x7f6695505ff0>.returncode
- *(... 25 more in this cluster)*

### `rc_mismatch_got7_want0` — 21 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_http_methods.test_url_without_scheme`
  > assert 7 == 0
  >  +  where 7 = <conftest.RunResult object at 0x7f66958e4a30>.returncode
- `tests.test_stdin_body.test_body_flag_json_string`
  > assert 7 == 0
  >  +  where 7 = CompletedProcess(args=['/workspace/executable', '-body={"key": "value"}', 'POST', 'http://httpbin.org/post'], returncode=7, stdout=b'', stderr=b'shell-init: error retrieving current dire
- `tests.test_bench.test_bench_post_request`
  > AssertionError: assert 7 == 0
  >  +  where 7 = CompletedProcess(args=['/workspace/executable', '-print=b', '-b', '-b.N=8', '-b.C=2', 'POST', 'http://localhost:8899/post', 'data=test'], returncode=7, stdout=b'', stderr=b'error: cannot
- *(... 18 more in this cluster)*

### `missing_dict_key` — 15 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_http_methods.test_put_request`
  > KeyError: 'Content-Type'
- `tests.test_http_methods.test_custom_headers`
  > KeyError: 'X-Custom-Header'
- `tests.test_http_methods.test_multiple_headers_same_request`
  > KeyError: 'X-Header-One'
- *(... 12 more in this cluster)*

### `string_output_mismatch` — 11 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_usage.test_dash_h_matches_dash_dash_help_exactly`
  > AssertionError: assert 'bat is a Go ...\n-j, -json\n' == ''
  >   
  >   + bat is a Go implemented CLI cURL-like tool for humans
  >   + Usage:
  >   + Version:
  >   + 0.1.0
  >   + Version:
  >   + 0.1.0...
- `tests.test_filter_final.test_auto_post_on_file_upload_no_explicit_method`
  > AssertionError: assert 'GET' == 'POST'
  >   
  >   - POST
  >   + GET
- `tests.test_http_methods.test_get_simple_request`
  > AssertionError: assert 'Python-urllib/3.10' == 'bat/0.1.0'
  >   
  >   - bat/0.1.0
  >   + Python-urllib/3.10
- *(... 8 more in this cluster)*

### `rc_mismatch_got22_want0` — 10 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_edge_cases.test_very_long_url`
  > assert 22 == 0
  >  +  where 22 = <conftest.RunResult object at 0x7f669546c430>.returncode
- `tests.test_stdin_and_body.test_body_flag_with_newlines`
  > assert 22 == 0
  >  +  where 22 = <conftest.RunResult object at 0x7f66969fe6b0>.returncode
- `tests.test_stdin_and_body.test_long_body`
  > assert 22 == 0
  >  +  where 22 = <conftest.RunResult object at 0x7f6695886f80>.returncode
- *(... 7 more in this cluster)*

### `rc_mismatch_got2_want0` — 10 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_forms.test_short_form_flag`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-f', 'POST', 'http://httpbin.org/post', 'key=value'], returncode=2, stdout=b'usage\n', stderr=b'shell-init: error retrieving current dire
- `tests.test_http_methods.test_get_method_implicit`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'http://httpbin.org/get'], returncode=2, stdout=b'bat\nusage\nversion\n', stderr=b'shell-init: error retrieving current directory: getcwd:
- `tests.test_json.test_json_stdin`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'POST', 'http://httpbin.org/post'], returncode=2, stdout=b'usage\n', stderr=b'shell-init: error retrieving current directory: getcwd: cann
- *(... 7 more in this cluster)*

### `returned_none` — 7 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_basic_invocation.test_version_format`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f22d884f760>(b'Version:\\s*\\d+\\.\\d+\\.\\d+', b'-a, -auth\n-b, -bench\n-f, -form\n-j, -json\n-p, -pretty\n-i, -insecure\n-proxy\n-print\n-body\nMETHOD:\n')
  >  +    where <function search at 0x7f22d884f760> = re.search
  >  +    and   b'-a, -auth\n-b, -bench\n-f, -form\n-j, -json\n-p, -pretty\n-i, -insecure\n-proxy\n-print\n-body\nMETHOD:\n' = CompletedProcess(args=['/workspace/executable', '-version'], returncode=2, st
- `tests.test_benchmarking.test_bench_numeric_output`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f22d884f760>(b'\\d+\\.\\d+', b'Summary:\nSlowest:\nFastest:\nAverage:\nsecs\nRequests/sec:\nLatency distribution:\n%\nResponse time histogram:\nStatus code dist
  >  +    where <function search at 0x7f22d884f760> = re.search
  >  +    and   b'Summary:\nSlowest:\nFastest:\nAverage:\nsecs\nRequests/sec:\nLatency distribution:\n%\nResponse time histogram:\nStatus code distribution:\n' = CompletedProcess(args=['/workspace/executa
- `eval.tests.test_help_usage.test_help_has_usage_header`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7fbf1bb2a680>('^Usage:\\s*$', '', re.MULTILINE)
  >  +    where <function search at 0x7fbf1bb2a680> = re.search
  >  +    and   '' = CompletedProcess(args=['/workspace/executable', '--help'], returncode=2, stdout='', stderr='').stdout
  >  +    and   re.MULTILINE = re.MULTILINE
- *(... 4 more in this cluster)*

### `rc_mismatch_got7_want1` — 7 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_errors.test_connection_refused_error`
  > AssertionError: assert 7 == 1
  >  +  where 7 = CompletedProcess(args=['/workspace/executable', '-print=b', '-url', 'http://127.0.0.1:1'], returncode=7, stdout=b'', stderr=b'error: cannot connect to http://127.0.0.1:1: <urlopen error 
- `tests.test_errors.test_dns_resolution_failure`
  > AssertionError: assert 7 == 1
  >  +  where 7 = CompletedProcess(args=['/workspace/executable', '-print=b', '-url', 'http://this-domain-does-not-exist-23947291.invalid'], returncode=7, stdout=b'', stderr=b'error: cannot connect to htt
- `tests.test_errors.test_invalid_port_number`
  > AssertionError: assert 7 == 1
  >  +  where 7 = CompletedProcess(args=['/workspace/executable', '-print=b', '-url', 'http://localhost:99999'], returncode=7, stdout=b'', stderr=b'error: cannot connect to http://localhost:99999: <urlope
- *(... 4 more in this cluster)*

### `uncategorized` — 7 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_errors.test_invalid_json_response_with_pretty_print`
  > OSError: [Errno 98] Address already in use
- `eval.tests.test_bat.TestFormSubmission.test_form_flag`
  > Failed: Command failed: /workspace/executable -form=true -print=b POST http://localhost:18888 name=John
  > stdout: 
  > stderr: error: cannot connect to http://127.0.0.1:8080/: <urlopen error [Errno 111] Connection refused>
- `eval.tests.test_bat.TestFormSubmission.test_form_short_flag`
  > Failed: Command failed: /workspace/executable -f -print=b POST http://localhost:18888 name=John
  > stdout: 
  > stderr: error: cannot connect to http://127.0.0.1:8080/: <urlopen error [Errno 111] Connection refused>
- *(... 4 more in this cluster)*

### `bytes_output_mismatch` — 5 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_basic.test_version_flag_long`
  > AssertionError: assert b'Version:\n0...-i, -insecure' == b'Version: 0.1.0'
  >   
  >   At index 8 diff: b'\n' != b' '
  >   
  >   Full diff:
  >   - (b'Version: 0.1.0')
  >   + (b'Version:\n0.1.0\nVersion:\n0.1.0\n-a, -auth\n-b, -bench\n-f, -form\n-j, -js'
  >   +  b'on\n-p, -pretty\n-i, -insecure')
- `tests.test_httplib_final.test_response_body_nil_handling`
  > AssertionError: assert b'key\n' == b'\n'
  >   
  >   At index 0 diff: b'k' != b'\n'
  >   
  >   Full diff:
  >   - b'\n'
  >   + b'key\n'
  >   ?   +++
- `tests.test_httplib_gaps.test_empty_response_body_handling`
  > AssertionError: assert b'key\n' == b'\n'
  >   
  >   At index 0 diff: b'k' != b'\n'
  >   
  >   Full diff:
  >   - b'\n'
  >   + b'key\n'
  >   ?   +++
- *(... 2 more in this cluster)*

### `boolean_false` — 5 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_benchmarking.test_bench_shows_statistics`
  > assert False
  >  +  where False = any(<generator object test_bench_shows_statistics.<locals>.<genexpr> at 0x7f669559ece0>)
- `tests.test_ssl_proxy_download.test_download_filename_from_url`
  > assert False
  >  +  where False = any(<generator object test_download_filename_from_url.<locals>.<genexpr> at 0x7f22d6a6c430>)
- `eval.tests.test_help_usage.test_help_ends_with_newline`
  > AssertionError: assert False
  >  +  where False = <built-in method endswith of str object at 0x7fbf1bbb8030>('\n')
  >  +    where <built-in method endswith of str object at 0x7fbf1bbb8030> = ''.endswith
  >  +      where '' = CompletedProcess(args=['/workspace/executable', '--help'], returncode=2, stdout='', stderr='').stdout
- *(... 2 more in this cluster)*

### `rc_mismatch_got0_want1` — 4 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_errors.test_file_not_found_in_request_data`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-print=b', 'http://localhost:8899', 'key=@/nonexistent/file.txt'], returncode=0, stdout=b'key\n', stderr=b'').returncode
- `tests.test_errors.test_reading_directory_instead_of_file`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-print=b', 'http://localhost:8899', 'key=@/tmp/pytest-of-root/pytest-0/test_reading_directory_instead2/testdir'], returncode=0, stdout=b'
- `tests.test_errors.test_malformed_url_missing_scheme_ambiguous`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-print=b', ':8080'], returncode=0, stdout=b'key\n', stderr=b'').returncode
- *(... 1 more in this cluster)*

### `rc_mismatch_got22_want1` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_errors.test_malformed_proxy_url`
  > AssertionError: assert 22 == 1
  >  +  where 22 = CompletedProcess(args=['/workspace/executable', '-print=b', '-proxy', 'ht!tp://invalid', 'http://localhost:8899'], returncode=22, stdout=b'', stderr=b'HTTP 404 Not Found\n').returncode
- `tests.test_errors.test_file_upload_without_form_flag`
  > AssertionError: assert 22 == 1
  >  +  where 22 = CompletedProcess(args=['/workspace/executable', '-print=b', '-json=false', 'http://localhost:8899', 'file@/tmp/pytest-of-root/pytest-0/test_file_upload_without_form_2/test.txt'], return

### `empty_list_or_string` — 1 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_help_formatting.TestHelpFormatting.test_help_has_blank_line_after_description`
  > IndexError: list index out of range

### `rc_mismatch_got4_want10001` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_httplib_gaps.test_large_response_body_handling`
  > AssertionError: assert 4 == 10001
  >  +  where 4 = len(b'key\n')
  >  +    where b'key\n' = CompletedProcess(args=['/workspace/executable', '-print=b', 'http://localhost:8899/large'], returncode=0, stdout=b'key\n', stderr=b'').stdout

