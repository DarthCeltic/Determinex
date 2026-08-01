# Action Sheet — xampprocky__tokei.505d648

**Current:** 5.74%  (51/888)
**Pass / Fail / Skip:** 51 / 493 / 2
**Gap to 100%:** 94.26 percentage points (837 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_config_input.test_input_from_file_adds_to_scan`
  - reason: --input functionality not working in current build - needs investigation
- `tests.test_config_input.test_input_from_stdin`
  - reason: --input functionality not working in current build - needs investigation

## Failure clusters

493 failed tests grouped into 9 buckets (sorted by count).

### `other_assertion` — 285 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_version_output`
  > AssertionError: assert b'tokei' in b''
  >  +  where b'' = <built-in method lower of bytes object at 0x7f9c509bc030>()
  >  +    where <built-in method lower of bytes object at 0x7f9c509bc030> = b''.lower
  >  +      where b'' = CompletedProcess(args=['./executable', '--version'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_basic_invocation.test_help_output`
  > AssertionError: assert b'Count your code, quickly' in b''
  >  +  where b'' = CompletedProcess(args=['./executable', '--help'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_basic_invocation.test_help_short`
  > AssertionError: assert b'Usage:' in b''
  >  +  where b'' = CompletedProcess(args=['./executable', '-h'], returncode=0, stdout=b'', stderr=b'').stdout
- *(... 282 more in this cluster)*

### `rc_mismatch_got1_want0` — 74 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_output_formats.test_json_output_short`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', 'tests/data/c.c', '-o', 'json'], returncode=1, stdout=b'', stderr=b'').returncode
- `tests.test_cli_utils.test_default_num_format_no_flag`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '/workspace/eval/test_resources/test_cli_utils/sample.rs'], returncode=1, stdout='', stderr='').returncode
- `tests.test_config_input.test_config_hidden_files_option`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '/tmp/pytest-of-root/pytest-0/test_config_hidden_files_optio2', '-o', 'json'], returncode=1, stdout='', stderr='').returncode
- *(... 71 more in this cluster)*

### `json_output_missing_or_bad` — 54 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `tests.test_configuration.test_config_file_docstrings_setting`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_edge_cases.test_very_long_line`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_edge_cases.test_unicode_in_file`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- *(... 51 more in this cluster)*

### `string_output_mismatch` — 37 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_cli_basic.test_languages_list_comprehensive`
  > AssertionError: assert '' == '━━━━━━━━━━━━...━━━━━━━━━\n\n'
  >   
  >   - ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  >   - ┃ Language                              Extensions                     ┃
  >   - ┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃
  >   - ┃ ABNF                                  abnf                           ┃
  >   - ┃ AWK                                   awk                            ┃
  >   - ┃ ABAP                                  abap                           ┃...
- `tests.test_cli_basic.test_streaming_simple_format`
  > AssertionError: assert 'Rust\n' == '# language  ...          1\n'
  >   
  >   + Rust
  >   - # language                                        path                                          lines         code       comments      blanks   
  >   - ########## ################################################################################ ############ ############ ############ ############
  >   -          C /workspace/eval/test_resources/test_cli_basic/multi_lang/code.c                             8            5            2            1
  >   -     Python /workspace/eval/test_resources/test_cli_basic/multi_lang/code.py                            7            4            2            1
- `tests.test_cli_basic.test_streaming_json_format`
  > assert 'Rust\n' == '{"language":...ments":2}}}\n'
  >   
  >   + Rust
  >   - {"language":"C","stats":{"name":"/workspace/eval/test_resources/test_cli_basic/multi_lang/code.c","stats":{"blanks":1,"blobs":{},"code":5,"comments":2}}}
  >   - {"language":"Python","stats":{"name":"/workspace/eval/test_resources/test_cli_basic/multi_lang/code.py","stats":{"blanks":1,"blobs":{},"code":4,"comments":2}}}
- *(... 34 more in this cluster)*

### `rc_mismatch_got2_want0` — 24 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_basic_invocation.test_languages_short_flag`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '-l'], returncode=2, stdout=b"error: unexpected argument '-l' found\nError: unexpected argument '-l' found\nunknown flag: unexpected argument '-l' 
- `tests.test_filtering.test_types_short_flag`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', 'tests/data', '-t', 'C'], returncode=2, stdout=b"error: unexpected argument '-t' found\nError: unexpected argument '-t' found\nunknown flag: unexpe
- `tests.test_filtering.test_exclude_multiple_patterns`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '/tmp/tmpg2na1ila', '--exclude', '*.rs', '--exclude', '*.py'], returncode=2, stdout=b"error: unexpected argument '--exclude' found\nError: unexpect
- *(... 21 more in this cluster)*

### `boolean_false` — 6 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_streaming.test_streaming_simple_parses_correctly`
  > assert False
  >  +  where False = any(<generator object test_streaming_simple_parses_correctly.<locals>.<genexpr> at 0x7f9c4ea62d50>)
- `tests.test_error_handling.test_compact_flag_format`
  > assert False
- `eval.tests.test_args_parsing_validation.test_output_value_forms_are_accepted[args0]`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7f49bfdb1330>('{')
  >  +    where <built-in method startswith of str object at 0x7f49bfdb1330> = 'main.rs\napp.py\n'.startswith
  >  +      where 'main.rs\napp.py\n' = <built-in method lstrip of str object at 0x7f49bfdb1330>()
  >  +        where <built-in method lstrip of str object at 0x7f49bfdb1330> = 'main.rs\napp.py\n'.lstrip
- *(... 3 more in this cluster)*

### `rc_unexpected_zero` — 6 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `eval.tests.test_exclude_and_errors.test_nonexistent_path_exits_nonzero_and_reports_error`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'this_path_should_not_exist_12345'], returncode=0, stdout=b'{\n  "BASH": "",\n  "CSS": "",\n  "Dockerfile": "",\n  "Fish": "",\n  "Go": ""
- `eval.tests.test_executable_behavior.test_nonexistent_path_errors`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/definitely/does/not/exist'], returncode=0, stdout='{\n  "BASH": "",\n  "CSS": "",\n  "Dockerfile": "",\n  "Fish": "",\n  "Go": "",\n  "H
- `eval.tests.test_executable_behavior.test_invalid_enum_values_error[args0]`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--sort', 'nope'], returncode=0, stdout='', stderr='').returncode
- *(... 3 more in this cluster)*

### `rc_mismatch_got0_want2` — 4 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `eval.tests.test_args_parsing_validation.test_output_cannot_be_specified_twice`
  > assert 0 == 2
- `eval.tests.test_args_parsing_validation.test_num_format_conflicts_with_output`
  > assert 0 == 2
- `eval.tests.test_args_parsing_validation.test_sort_rejects_invalid_choice`
  > assert 0 == 2
- *(... 1 more in this cluster)*

### `rc_mismatch_got0_want1` — 3 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_error_handling.test_input_file_malformed_data`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--input', '/tmp/pytest-of-root/pytest-0/test_input_file_malformed_data2/bad.txt'], returncode=0, stdout='', stderr='').returncode
- `tests.test_error_handling.test_multiple_paths_with_one_nonexistent`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/tmp/pytest-of-root/pytest-0/test_multiple_paths_with_one_n2', '/nonexistent/path'], returncode=0, stdout='{\n  "BASH": "",\n  "CSS": "",
- `eval.tests.test_args_parsing_validation.test_double_dash_makes_dashy_path_positional`
  > assert 0 == 1

