# Action Sheet — isona__dirble.e2dea9f

**Current:** 30.33%  (347/1144)
**Pass / Fail / Skip:** 347 / 759 / 2
**Gap to 100%:** 69.67 percentage points (797 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_scan_behavior.test_scrape_listable_discovers_subdir`
  - reason: test_scrape_listable_discovers_subdir depends on test_listable_directory_reports_L
- `eval.tests.test_scan_behavior.test_disable_recursion_prevents_scanning_detected_dir`
  - reason: test_disable_recursion_prevents_scanning_detected_dir depends on test_directory_detection_reports_D

## Failure clusters

759 failed tests grouped into 19 buckets (sorted by count).

### `other_assertion` — 465 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_help_flag_short`
  > AssertionError: assert b'Fast directory scanning and scraping tool' in b'Fast directory scanning\nUsage:\nOptions:\nDirble\ncommit\nDirble\nFast directory scanning\n'
  >  +  where b'Fast directory scanning\nUsage:\nOptions:\nDirble\ncommit\nDirble\nFast directory scanning\n' = CompletedProcess(args=['./executable', '-h'], returncode=0, stdout=b'Fast directory scanning
- `tests.test_basic_invocation.test_help_flag_long`
  > AssertionError: assert b'Fast directory scanning and scraping tool' in b'Usage:\nOptions:\nwordlist\nuri\nextension\n'
  >  +  where b'Usage:\nOptions:\nwordlist\nuri\nextension\n' = CompletedProcess(args=['./executable', '--help'], returncode=0, stdout=b'Usage:\nOptions:\nwordlist\nuri\nextension\n', stderr=b'').stdout
- `tests.test_basic_invocation.test_help_shows_all_major_options`
  > AssertionError: assert (b'--uri' in b'Usage:\nOptions:\nwordlist\nuri\nextension\n' or b'-u' in b'Usage:\nOptions:\nwordlist\nuri\nextension\n')
  >  +  where b'Usage:\nOptions:\nwordlist\nuri\nextension\n' = CompletedProcess(args=['./executable', '--help'], returncode=0, stdout=b'Usage:\nOptions:\nwordlist\nuri\nextension\n', stderr=b'').stdout
  >  +  and   b'Usage:\nOptions:\nwordlist\nuri\nextension\n' = CompletedProcess(args=['./executable', '--help'], returncode=0, stdout=b'Usage:\nOptions:\nwordlist\nuri\nextension\n', stderr=b'').stdout
- *(... 462 more in this cluster)*

### `rc_mismatch_got2_want0` — 79 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_actual_scanning.test_scan_with_silent_mode`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'http://localhost:48289', '-w', '/tmp/tmprnv06hwy/wordlist.txt', '-S', '--max-threads', '1', '--timeout', '2'], returncode=2, stdout=b'', 
- `tests.test_additional_coverage.test_htaccess_filtering`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'http://localhost:39875', '-w', '/tmp/tmp7judbnf_/wordlist.txt', '--max-threads', '1', '--timeout', '2', '-r'], returncode=2, stdout=b'', 
- `tests.test_additional_coverage.test_401_directory_scanning`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'http://localhost:55145', '-w', '/tmp/tmplydbl0zs/wordlist.txt', '--max-threads', '1', '--timeout', '2', '-v'], returncode=2, stdout=b'', 
- *(... 76 more in this cluster)*

### `string_output_mismatch` — 60 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_edge_cases.test_no_args_shows_help`
  > AssertionError: assert 'error: canno...on refused>\n' == 'Fast directo...u [address]\n'
  >   
  >   + error: cannot connect to http://127.0.0.1:8080/: <urlopen error [Errno 111] Connection refused>
  >   - Fast directory scanning and scraping tool
  >   - 
  >   - Usage: executable [OPTIONS] <uri|--uri-file <uri-file>|--uri <uri>>
  >   - 
  >   - Arguments:...
- `tests.test_edge_cases.test_zero_max_threads_rejected`
  > assert "error: inval...y '--help'.\n" == "error: inval...y '--help'.\n"
  >   
  >   - error: invalid value '0' for '--max-threads <max-threads>': 0 is not in 1..=4294967295
  >   + error: invalid value 'INVALID' for '--verb <http_verb>'
  >   +   [possible values: get, head, post]
  >     
  >     For more information, try '--help'.
- `tests.test_edge_cases.test_nonexistent_uri_file`
  > assert 'error: canno...on refused>\n' == "\nthread 'ma...a backtrace\n"
  >   
  >   + error: cannot connect to http://127.0.0.1:8080/: <urlopen error [Errno 111] Connection refused>
  >   - 
  >   - thread 'main' panicked at /workspace/src/wordlist.rs:112:37:
  >   - called `Result::unwrap()` on an `Err` value: Os { code: 2, kind: NotFound, message: "No such file or directory" }
  >   - note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
- *(... 57 more in this cluster)*

### `rc_mismatch_got22_want0` — 53 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_harvest.test_output_json_format`
  > AssertionError: assert 22 == 0
  >  +  where 22 = CompletedProcess(args=['/workspace/executable', 'http://localhost:34073', '-w', '/tmp/tmpapwfibmv.txt', '--json-file', '/tmp/tmp67cf66y2.json'], returncode=22, stdout='', stderr='HTTP 4
- `tests.test_harvest.test_output_xml_format`
  > AssertionError: assert 22 == 0
  >  +  where 22 = CompletedProcess(args=['/workspace/executable', 'http://localhost:32907', '-w', '/tmp/tmprw8lv95r.txt', '--xml-file', '/tmp/tmp15_rmsv9.xml'], returncode=22, stdout='', stderr='HTTP 404
- `tests.test_harvest.test_output_no_color`
  > AssertionError: assert 22 == 0
  >  +  where 22 = CompletedProcess(args=['/workspace/executable', 'http://localhost:41663', '-w', '/tmp/tmpkjk1julp.txt', '--no-color', '-o', '/tmp/tmp6tcnj14w.txt'], returncode=22, stdout='', stderr='HT
- *(... 50 more in this cluster)*

### `rc_unexpected_zero` — 37 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_extensions_prefixes.test_extension_file_not_found`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'http://example.com', '-w', '/tmp/tmpipk6ff3u/wordlist.txt', '-X', '/nonexistent/ext.txt'], returncode=0, stdout=b'\nthread \'main\' (5611) panicke
- `tests.test_extensions_prefixes.test_prefix_file_not_found`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'http://example.com', '-w', '/tmp/tmp6w1_ptar/wordlist.txt', '-P', '/nonexistent/prefix.txt'], returncode=0, stdout=b'\nthread \'main\' (5611) pani
- `tests.test_extensions_prefixes.test_empty_extension_file`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'http://example.com', '-w', '/tmp/tmpjnusgzea/wordlist.txt', '-X', '/tmp/tmpjnusgzea/empty_ext.txt', '-t', '1', '-T', '1', '--timeout', '1'], retur
- *(... 34 more in this cluster)*

### `rc_mismatch_got0_want3` — 14 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_error_handling.test_timeout_option_applied_quickly`
  > assert 0 == 3
  >  +  where 0 = len([])
- `tests.test_error_handling.test_special_characters_wordlist_handled`
  > assert 0 == 3
  >  +  where 0 = len([])
- `tests.test_error_handling.test_very_long_url_path_handled`
  > assert 0 == 3
  >  +  where 0 = len([])
- *(... 11 more in this cluster)*

### `rc_mismatch_got0_want2` — 13 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_target_specification.test_missing_uri_shows_help`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['./executable', '-w', '/tmp/tmpoq3296vn/wordlist.txt'], returncode=0, stdout=b'curl\ncurl\n', stderr=b'').returncode
- `eval.tests.test_argparse_validation.test_common_invalid_args_exit_2[args0-needles0]`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--nonexistent-flag'], returncode=0, stdout='Fast directory scanning\n', stderr='').returncode
- `eval.tests.test_argparse_validation.test_common_invalid_args_exit_2[args1-needles1]`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--uri', 'http://example.com', '--extensions', '.php', '--output-file'], returncode=0, stdout='', stderr='').returncode
- *(... 10 more in this cluster)*

### `boolean_false` — 13 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_actual_scanning.test_scan_with_text_output`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpn609xny0/output.txt').exists
- `tests.test_actual_scanning.test_scan_with_json_output`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmp10d9gs_i/output.json').exists
- `tests.test_actual_scanning.test_scan_with_xml_output`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmp2s72iy1o/output.xml').exists
- *(... 10 more in this cluster)*

### `returned_none` — 8 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_basic_invocation.test_version_flag_short`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f4dd43cf760>(b'\\d+\\.\\d+\\.\\d+', b'Dirble\nFast directory scanning\n')
  >  +    where <function search at 0x7f4dd43cf760> = re.search
  >  +    and   b'Dirble\nFast directory scanning\n' = CompletedProcess(args=['./executable', '-V'], returncode=0, stdout=b'Dirble\nFast directory scanning\n', stderr=b'').stdout
- `tests.test_basic_invocation.test_version_flag_long`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f4dd43cf760>(b'\\d+\\.\\d+\\.\\d+', b'Dirble\n.\nUsage:\nOptions:\nwordlist\nuri\nextension\n')
  >  +    where <function search at 0x7f4dd43cf760> = re.search
  >  +    and   b'Dirble\n.\nUsage:\nOptions:\nwordlist\nuri\nextension\n' = CompletedProcess(args=['./executable', '--version'], returncode=0, stdout=b'Dirble\n.\nUsage:\nOptions:\nwordlist\nuri\nextensi
- `tests.test_basic_invocation.test_version_flag`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7fec90ecf760>(b'Dirble\\s+\\d+\\.\\d+\\.\\d+', b'Dirble\n.\nUsage:\nOptions:\nwordlist\nuri\nextension\n')
  >  +    where <function search at 0x7fec90ecf760> = re.search
  >  +    and   b'Dirble\n.\nUsage:\nOptions:\nwordlist\nuri\nextension\n' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'Dirble\n.\nUsage:\nOptions:\nwordlist\nuri
- *(... 5 more in this cluster)*

### `rc_mismatch_got7_want2` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_no_arguments_shows_help`
  > AssertionError: assert 7 == 2
  >  +  where 7 = CompletedProcess(args=['./executable'], returncode=7, stdout=b'', stderr=b'error: cannot connect to http://127.0.0.1:8080/: <urlopen error [Errno 111] Connection refused>\n').returncode
- `tests.test_subcommand_dispatch.TestNoSubcommands.test_no_args_shows_help`
  > AssertionError: assert 7 == 2
  >  +  where 7 = CompletedProcess(args=['/workspace/executable'], returncode=7, stdout=b'', stderr=b'error: cannot connect to http://127.0.0.1:8080/: <urlopen error [Errno 111] Connection refused>\n').re
- `tests.test_subcommand_dispatch.TestUrlArgumentParsing.test_uri_required_error`
  > AssertionError: assert 7 == 2
  >  +  where 7 = CompletedProcess(args=['/workspace/executable'], returncode=7, stdout=b'', stderr=b'error: cannot connect to http://127.0.0.1:8080/: <urlopen error [Errno 111] Connection refused>\n').re

### `missing_file` — 3 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_output_formats.test_json_redirect_field_populated`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_json_redirect_field_popul2/redirect_test.json'
- `tests.test_output_formats.test_xml_redirect_attribute_populated`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_xml_redirect_attribute_po2/redirect_test.xml'
- `tests.test_output_formats.test_hide_lengths_affects_all_output_formats`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_hide_lengths_affects_all_2/lengths_test.json'

### `rc_mismatch_got7_want0` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_harvest.test_uri_file`
  > AssertionError: assert 7 == 0
  >  +  where 7 = CompletedProcess(args=['/workspace/executable', '-U', '/tmp/tmp1pfbehh8.txt', '-w', '/tmp/tmpt_a1zivs.txt', '-o', '/tmp/tmp6hf_z4fb.txt'], returncode=7, stdout='', stderr='error: cannot 
- `tests.test_advanced.test_uri_file`
  > AssertionError: assert 7 == 0
  >  +  where 7 = CompletedProcess(args=['../executable', '-U', '/tmp/tmpankuxnbf.txt', '-w', '/tmp/tmpeg0qua8x.txt', '-o', '/tmp/tmprzsg45cf.txt', '-r'], returncode=7, stdout='', stderr='error: cannot co

### `uncategorized` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_threading.test_max_errors_stops_thread_after_consecutive_failures`
  > OSError: [Errno 98] Address already in use
- `tests.test_basic.test_xml_output`
  > xml.etree.ElementTree.ParseError: no element found: line 1, column 0

### `rc_mismatch_got0_want101` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_argparse_validation.test_output_aliases_oN_oJ_oX_equals_value_panics_with_absolute_paths`
  > AssertionError: assert 0 == 101
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--uri', 'http://example.com', '--extensions', '.php', '-oN=/tmp/pytest-of-root/pytest-0/test_output_aliases_oN_oJ_oX_e2/report.txt'], ret
- `eval.tests.test_argparse_validation.test_output_alias_oA_equals_value_panics_with_absolute_path`
  > AssertionError: assert 0 == 101
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--uri', 'http://example.com', '--extensions', '.php', '-oA=/tmp/pytest-of-root/pytest-0/test_output_alias_oA_equals_va2/bundle'], returnc

### `test_timeout` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_target_specification.test_uri_with_port`
  > subprocess.TimeoutExpired: Command '['./executable', 'http://example.com:8080', '-w', '/tmp/tmpym9b1d6q/wordlist.txt', '-t', '1', '-T', '1', '--timeout', '1']' timed out after 5.0 seconds

### `bytes_output_mismatch` — 1 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_actual_scanning.test_scan_with_max_errors`
  > assert (b'localhost' in b'' or 2 == 0)
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', 'http://localhost:55733', '-w', '/tmp/tmp9nz_l23n/wordlist.txt', '--max-errors', '2', '--max-threads', '1', '--timeout', '2'], returncod
  >  +  and   2 = CompletedProcess(args=['/workspace/executable', 'http://localhost:55733', '-w', '/tmp/tmp9nz_l23n/wordlist.txt', '--max-errors', '2', '--max-threads', '1', '--timeout', '2'], returncode=

### `rc_mismatch_got2_want4` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_edge_cases.test_ipv6_localhost_address`
  > AssertionError: assert 2 == 4
  >  +  where 2 = len(['curl', 'curl'])

### `rc_mismatch_got101_want2` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_argparse_validation.test_output_aliases_oN_oJ_oX_require_equals_value_syntax`
  > AssertionError: assert 101 == 2
  >  +  where 101 = CompletedProcess(args=['/workspace/executable', '--uri', 'http://example.com', '--extensions', '.php', '-oN', 'out.txt'], returncode=101, stdout='', stderr='').returncode

### `json_output_missing_or_bad` — 1 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `tests.test_basic.test_json_output`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

