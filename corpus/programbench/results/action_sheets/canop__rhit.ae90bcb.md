# Action Sheet — canop__rhit.ae90bcb

**Current:** 23.31%  (307/1317)
**Pass / Fail / Skip:** 307 / 688 / 0
**Gap to 100%:** 76.69 percentage points (1010 tests)

## Failure clusters

688 failed tests grouped into 20 buckets (sorted by count).

### `other_assertion` — 386 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_rhit.test_help_flag`
  > AssertionError: assert b'nginx' in b'rhit\nusage:\nrhit\nhits\nstatus\npath\n66,936 hits\n33,468 hits\n'
  >  +  where b'rhit\nusage:\nrhit\nhits\nstatus\npath\n66,936 hits\n33,468 hits\n' = <built-in method lower of bytes object at 0x7fe54b1943f0>()
  >  +    where <built-in method lower of bytes object at 0x7fe54b1943f0> = b'rhit\nUsage:\nrhit\nhits\nstatus\npath\n66,936 hits\n33,468 hits\n'.lower
  >  +      where b'rhit\nUsage:\nrhit\nhits\nstatus\npath\n66,936 hits\n33,468 hits\n' = CompletedProcess(args=['./executable', '--help'], returncode=0, stdout=b'rhit\nUsage:\nrhit\nhits\nstatus\npath\n6
- `tests.test_rhit.test_version_flag`
  > AssertionError: assert (b'2.0' in b'rhit\nhits\nstatus\npath\n66,936 hits\n33,468 hits\n' or b'1.' in b'rhit\nhits\nstatus\npath\n66,936 hits\n33,468 hits\n')
  >  +  where b'rhit\nhits\nstatus\npath\n66,936 hits\n33,468 hits\n' = CompletedProcess(args=['./executable', '--version'], returncode=0, stdout=b'rhit\nhits\nstatus\npath\n66,936 hits\n33,468 hits\n', s
  >  +  and   b'rhit\nhits\nstatus\npath\n66,936 hits\n33,468 hits\n' = CompletedProcess(args=['./executable', '--version'], returncode=0, stdout=b'rhit\nhits\nstatus\npath\n66,936 hits\n33,468 hits\n', s
- `tests.test_rhit.test_single_log_file`
  > AssertionError: assert b'hits' in b''
  >  +  where b'' = CompletedProcess(args=['./executable', 'test-data/access.log', '--silent-load'], returncode=0, stdout=b'', stderr=b'').stdout
- *(... 383 more in this cluster)*

### `string_output_mismatch` — 70 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_argparse_validation.test_combined_short_flags_can_consume_value_immediately_if_value_is_numeric`
  > AssertionError: assert 'error: unexp...nformation.\n' == ''
  >   
  >   + error: unexpected argument '-cl' found
  >   + Error: unexpected argument '-cl' found
  >   + unknown flag: unexpected argument '-cl' found
  >   + Unknown flag: unexpected argument '-cl' found
  >   + 
  >   + Usage: rhit [OPTIONS] [ARGS]......
- `eval.tests.test_help_baseline.test_help_plain_output_matches_baseline_exactly`
  > AssertionError: assert '' == '            ...┘\x1b[39m\n\n'
  >   
  >   -                     #x1B[38;5;204m#x1B[1m#x1B[4mrhit#x1B[0m#x1B[38;5;204m#x1B[1m#x1B[4m #x1B[0m#x1B[38;5;204m#x1B[1m#x1B[4m2.0.4#x1B[0m
  >   - 
  >   - #x1B[38;5;204m#x1B[1mRhit#x1B[0m analyzes your nginx logs.
  >   - 
  >   - Complete documentation at #x1B[4mhttps://dystroy.org/rhit#x1B[0m
  >   - ...
- `eval.tests.test_help_behavior.test_help_respects_color_no`
  > AssertionError: assert '' == '            ...┘\x1b[39m\n\n'
  >   
  >   -                     #x1B[38;5;204m#x1B[1m#x1B[4mrhit#x1B[0m#x1B[38;5;204m#x1B[1m#x1B[4m #x1B[0m#x1B[38;5;204m#x1B[1m#x1B[4m2.0.4#x1B[0m
  >   - 
  >   - #x1B[38;5;204m#x1B[1mRhit#x1B[0m analyzes your nginx logs.
  >   - 
  >   - Complete documentation at #x1B[4mhttps://dystroy.org/rhit#x1B[0m
  >   - ...
- *(... 67 more in this cluster)*

### `rc_unexpected_zero` — 57 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_rhit.test_no_arguments_fails`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable'], returncode=0, stdout=b'bytes_sent,date,initial,method,path,referer,remote_addr,status,test-data,time\n,,,,,,,,,\n', stderr=b'').returncode
- `tests.test_rhit.test_invalid_option`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'test-data/access.log', '--invalid-option'], returncode=0, stdout=b"error: unexpected argument '--invalid-option' found\nError: unexpected argument
- `tests.test_rhit.test_file_not_found`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '/nonexistent/path/to/log.txt'], returncode=0, stdout=b'query=value\nbe43:2e2f\n', stderr=b'').returncode
- *(... 54 more in this cluster)*

### `rc_mismatch_got0_want2` — 57 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_argument_parsing.TestUnknownFlags.test_unknown_flag_error[--invalid-flag]`
  > assert 0 == 2
- `tests.test_argument_parsing.TestUnknownFlags.test_unknown_flag_error[--unknown]`
  > assert 0 == 2
- `tests.test_argument_parsing.TestUnknownFlags.test_unknown_flag_error[--nonexistent]`
  > assert 0 == 2
- *(... 54 more in this cluster)*

### `json_output_missing_or_bad` — 27 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `tests.test_additional_coverage.test_output_json_with_filters`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_advanced_filters.test_status_range_custom`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_advanced_filters.test_status_5xx_range`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- *(... 24 more in this cluster)*

### `empty_list_or_string` — 18 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_display_options.test_fields_default`
  > IndexError: list index out of range
- `tests.test_display_options.test_fields_custom_selection`
  > IndexError: list index out of range
- `tests.test_display_options.test_fields_add_ip`
  > IndexError: list index out of range
- *(... 15 more in this cluster)*

### `missing_dict_key` — 17 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_date_time_filters.test_date_filter_specific_date_csv_output`
  > KeyError: 'date'
- `tests.test_date_time_filters.test_time_filter_after_specific_time`
  > KeyError: 'time'
- `tests.test_date_time_filters.test_time_filter_before_specific_time`
  > KeyError: 'time'
- *(... 14 more in this cluster)*

### `boolean_false` — 13 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_rhit.test_output_json`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of bytes object at 0x7fe54b12fdb0>(b'[')
  >  +    where <built-in method startswith of bytes object at 0x7fe54b12fdb0> = b'bytes_sent,date,initial,method,path,referer,remote_addr,status,test-data,time\n,,,,,,,,,\n'.startswith
  >  +      where b'bytes_sent,date,initial,method,path,referer,remote_addr,status,test-data,time\n,,,,,,,,,\n' = CompletedProcess(args=['./executable', 'test-data/access.log', '--silent-load', '--output'
- `tests.test_rhit.test_json_format_structure`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of bytes object at 0x7fe54d63c030>(b'[')
  >  +    where <built-in method startswith of bytes object at 0x7fe54d63c030> = b''.startswith
  >  +      where b'' = CompletedProcess(args=['./executable', 'test-data/access.log', '--silent-load', '-o', 'json', '-s', '200', '-l', '0', '-p', '^/login$'], returncode=0, stdout=b'', stderr=b'').stdou
- `eval.tests.test_argparse_validation.test_option_value_formats_space_and_equals_are_equivalent_for_output_raw`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7fce8ae58030>('be43:2e2f:ffb::ada:1f02 - - [22/Jan/2021:01:47:05 +0000]')
  >  +    where <built-in method startswith of str object at 0x7fce8ae58030> = ''.startswith
- *(... 10 more in this cluster)*

### `rc_mismatch_got0_want1` — 12 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_argument_parsing.TestPositionalArguments.test_no_files_uses_default_location`
  > assert 0 == 1
- `tests.test_argument_parsing.TestPositionalArguments.test_nonexistent_file`
  > assert 0 == 1
- `eval.tests.test_argparse_validation.test_double_dash_makes_unknown_flag_be_treated_as_positional_path`
  > assert 0 == 1
- *(... 9 more in this cluster)*

### `returned_none` — 9 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_behavior.test_help_contains_usage_line`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f3e5b506680>('^\\s*Usage:\\s+\\S+\\s+\\[options\\]\\s+\\[FILES\\]', 'rhit\nUsage:\nrhit\nhits\nstatus\npath\n66,936 hits\n33,468 hits\n', re.MULTILINE)
  >  +    where <function search at 0x7f3e5b506680> = re.search
  >  +    and   re.MULTILINE = re.M
- `eval.tests.test_help_and_version.test_version_flag_prints_version_like_semver`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7fbe1289a680>('\\b\\d+\\.\\d+\\.\\d+\\b', 'rhit\nhits\nstatus\npath\n66,936 hits\n33,468 hits')
  >  +    where <function search at 0x7fbe1289a680> = re.search
- `tests.test_filtering.test_filter_status_single`
  > assert None == 274
- *(... 6 more in this cluster)*

### `bytes_output_mismatch` — 9 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `eval.tests.test_externalized.test_ext_parse_nginx_date_iso_8601`
  > AssertionError: assert ['/test', '/a...'/millennium'] == ['/b', '/c']
  >   
  >   At index 0 diff: '/test' != '/b'
  >   Left contains one more item: '/millennium'
  >   
  >   Full diff:
  >     [
  >   +     '/test',...
- `eval.tests.test_externalized.test_ext_date_time_filter_precise_date`
  > AssertionError: assert ['/test', '/a...'/millennium'] == ['/b', '/c']
  >   
  >   At index 0 diff: '/test' != '/b'
  >   Left contains one more item: '/millennium'
  >   
  >   Full diff:
  >     [
  >   +     '/test',...
- `eval.tests.test_externalized.test_ext_date_time_filter_default_year_month_day`
  > AssertionError: assert ['/test', '/a...'/millennium'] == ['/b']
  >   
  >   At index 0 diff: '/test' != '/b'
  >   Left contains 2 more items, first extra item: '/api'
  >   
  >   Full diff:
  >     [
  >   +     '/test',...
- *(... 6 more in this cluster)*

### `rc_mismatch_got1_want5` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_date_parsing_comprehensive.test_iso_8601_date_parsing_various_dates`
  > AssertionError: assert 1 == 5
  >  +  where 1 = len([''])
- `tests.test_date_parsing_comprehensive.test_mixed_date_formats_same_log`
  > AssertionError: assert 1 == 5
  >  +  where 1 = len([''])

### `rc_mismatch_got22_want2` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_date_parsing_comprehensive.test_date_range_same_month_different_years`
  > assert 22 == 2
  >  +  where 22 = len(['[', '  {', '    "date": "2021/01/22",', '    "time": "01:47:05",', '    "remote_addr": "192.168.1.1",', '    "method": "GET",', ...])
- `tests.test_date_parsing_comprehensive.test_implicit_date_filter_same_year_same_month`
  > assert 22 == 2
  >  +  where 22 = len(['[', '  {', '    "date": "2021/01/22",', '    "time": "01:47:05",', '    "remote_addr": "192.168.1.1",', '    "method": "GET",', ...])

### `rc_mismatch_got1_want6` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_date_parsing_comprehensive.test_edge_case_days_in_month`
  > AssertionError: assert 1 == 6
  >  +  where 1 = len([''])
- `tests.test_output_formats.test_csv_basic_structure_parseable`
  > assert 1 == 6
  >  +  where 1 = len([[]])

### `rc_mismatch_got5_want1` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_output_formats.test_csv_empty_result_set`
  > assert 5 == 1
  >  +  where 5 = len(['192.168.1.1 - - [22/Jan/2021:01:47:05 +0000] "GET /test HTTP/1.1" 200 100 "-" "Mozilla/5.0"', 'be43:2e2f:ffb::ada:1f02 - - [22/Jan/2021:01:47:06 +0000] "POST /api/data HTTP/1.1" 20
- `tests.test_output_formats.test_raw_respects_status_filter`
  > assert 5 == 1
  >  +  where 5 = len(['192.168.1.1 - - [22/Jan/2021:01:47:05 +0000] "GET /test HTTP/1.1" 200 100 "-" "Mozilla/5.0"', 'be43:2e2f:ffb::ada:1f02 - - [22/Jan/2021:01:47:06 +0000] "POST /api/data HTTP/1.1" 20

### `rc_mismatch_got4_want8` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_output.test_output_csv`
  > AssertionError: assert 4 == 8
  >  +  where 4 = len(['2021/01/22', '01:47:05', '192.168.1.1', 'GET'])
  >  +  and   8 = len(['date', 'time', 'remote address', 'method', 'path', 'status', ...])

### `rc_mismatch_got3_want1` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_coverage_gaps.test_method_none_variant_empty_string`
  > AssertionError: assert 3 == 1
  >  +  where 3 = len([{'bytes_sent': 1234, 'date': '1977/04/22', 'method': 'GET', 'path': '/test', ...}, {'bytes_sent': 567, 'date': '2021/12/31', 'method': 'POST', 'path': '/api', ...}, {'bytes_sent': 9

### `rc_mismatch_got3_want9` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_coverage_gaps.test_method_display_formatting_all_standard_methods`
  > AssertionError: assert 3 == 9
  >  +  where 3 = len([{'bytes_sent': 1234, 'date': '1977/04/22', 'method': 'GET', 'path': '/test', ...}, {'bytes_sent': 567, 'date': '2021/12/31', 'method': 'POST', 'path': '/api', ...}, {'bytes_sent': 9

### `rc_mismatch_got1_want13` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_date_parsing_comprehensive.test_common_log_format_date_parsing`
  > AssertionError: assert 1 == 13
  >  +  where 1 = len([''])

### `rc_mismatch_got22_want4` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_date_parsing_comprehensive.test_date_filter_spanning_multiple_years`
  > assert 22 == 4
  >  +  where 22 = len(['[', '  {', '    "date": "2021/01/22",', '    "time": "01:47:05",', '    "remote_addr": "192.168.1.1",', '    "method": "GET",', ...])

