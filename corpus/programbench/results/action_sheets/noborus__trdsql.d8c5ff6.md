# Action Sheet — noborus__trdsql.d8c5ff6

**Current:** 3.91%  (69/1764)
**Pass / Fail / Skip:** 69 / 930 / 1
**Gap to 100%:** 96.09 percentage points (1695 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_trdsql_behavior.test_csv_with_ih_and_oh_outputs_header_row`
  - reason: test_csv_with_ih_and_oh_outputs_header_row depends on test_csv_with_header_flag_ih_allows_select_by_name

## Failure clusters

930 failed tests grouped into 12 buckets (sorted by count).

### `rc_mismatch_got1_want0` — 372 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_advanced_features.test_json_nested_structure`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '-ijson', 'SELECT * FROM /tmp/tmp7gx56mpq/nested.json'], returncode=1, stdout=b'', stderr=b'Traceback (most recent call last):\n  File "/workspace/
- `tests.test_advanced_features.test_json_array_values`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '-ijson', 'SELECT * FROM /tmp/tmpiamf9x8q/arrays.json'], returncode=1, stdout=b'', stderr=b'Traceback (most recent call last):\n  File "/workspace/
- `tests.test_advanced_features.test_json_boolean_values`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '-ijson', 'SELECT * FROM /tmp/tmp4m3sdkiu/bool.json'], returncode=1, stdout=b'', stderr=b'Traceback (most recent call last):\n  File "/workspace/ma
- *(... 369 more in this cluster)*

### `other_assertion` — 244 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_advanced_features.test_multiple_output_formats_same_data`
  > AssertionError: Failed for format -ocsv
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '-ocsv', 'SELECT * FROM /tmp/tmpbgvkni7t/data.csv'], returncode=1, stdout=b'', stderr=b'Traceback (most recent call last):\n  File "/workspace/main
- `tests.test_basic_invocation.test_help_short_flag`
  > assert b'trdsql - Execute SQL queries' in b"trdsql: unknown option: -help\nusage: trdsql [OPTIONS] [ARGS]\nTry 'trdsql --help' for more information.\n"
  >  +  where b"trdsql: unknown option: -help\nusage: trdsql [OPTIONS] [ARGS]\nTry 'trdsql --help' for more information.\n" = CompletedProcess(args=['./executable', '-help'], returncode=2, stdout=b'', std
- `tests.test_database_drivers.test_dblist_flag`
  > assert (2 == 0 or 2 == 1)
  >  +  where 2 = CompletedProcess(args=['./executable', '-dblist'], returncode=2, stdout=b'', stderr=b"trdsql: unknown option: -dblist\nusage: trdsql [OPTIONS] [ARGS]\nTry 'trdsql --help' for more inform
  >  +  and   2 = CompletedProcess(args=['./executable', '-dblist'], returncode=2, stdout=b'', stderr=b"trdsql: unknown option: -dblist\nusage: trdsql [OPTIONS] [ARGS]\nTry 'trdsql --help' for more inform
- *(... 241 more in this cluster)*

### `rc_mismatch_got2_want0` — 205 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_advanced_features.test_yaml_nested_structure`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '-iyaml', 'SELECT * FROM /tmp/tmpfzwv37uk/nested.yaml'], returncode=2, stdout=b'', stderr=b"trdsql: unknown option: -iyaml\nusage: trdsql [OPTIONS]
- `tests.test_advanced_features.test_custom_delimiter_output`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '-oraw', '-od', ';;', 'SELECT * FROM /tmp/tmp2zly5bdn/test.csv'], returncode=2, stdout=b'', stderr=b"trdsql: unknown option: -oraw\nusage: trdsql [
- `tests.test_analyze.test_analyze_csv_file`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '-a', '/tmp/tmp7w47oa61/test.csv'], returncode=2, stdout=b'', stderr=b"trdsql: unknown option: -a\nusage: trdsql [OPTIONS] [ARGS]\nTry 'trdsql --he
- *(... 202 more in this cluster)*

### `returned_none` — 50 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_output.test_help_has_usage_header`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7fec04b16680>('^Usage\\s*$', '', re.MULTILINE)
  >  +    where <function search at 0x7fec04b16680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- `eval.tests.test_help_output.test_help_has_options_section_header`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7fec04b16680>('^Options:\\s*$', '', re.MULTILINE)
  >  +    where <function search at 0x7fec04b16680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- `eval.tests.test_help_output.test_main_option_flags_are_documented[-A]`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7fec04b16680>('^\\s*\\-A(\\s|$)', '', re.MULTILINE)
  >  +    where <function search at 0x7fec04b16680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- *(... 47 more in this cluster)*

### `string_output_mismatch` — 27 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_stdin_stdout.test_stdin_with_sql_operations`
  > assert 'Error: near ... syntax error' == '1,Orange'
  >   
  >   - 1,Orange
  >   + Error: near "-": syntax error
- `eval.tests.test_help_output.test_help_prints_to_stderr_not_stdout_for_dash_help`
  > AssertionError: assert 'trdsql 0.1.0...put file path' == ''
  >   
  >   + trdsql 0.1.0 - bootstrap scaffold
  >   + 
  >   + Usage: trdsql [OPTIONS] [ARGS]
  >   + 
  >   + Options:
  >   +   -h, --help     Print help...
- `eval.tests.test_help_output.test_dash_help_output_exact_match_fixture`
  > assert '' == 'trdsql - Exe...,c2 FROM -"\n'
  >   
  >   - trdsql - Execute SQL queries on CSV, LTSV, JSON, YAML and TBLN.
  >   - 
  >   - Usage
  >   - 	trdsql [OPTIONS] [SQL(SELECT...)]
  >   - 
  >   - Options:...
- *(... 24 more in this cluster)*

### `rc_mismatch_got2_want1` — 17 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_argparse_validation.test_bool_with_space_is_not_taken_as_value_and_changes_positional_interpretation`
  > assert 2 == 1
  >  +  where 2 = RunResult(rc=2, out='', err="trdsql: unknown option: -ig\nusage: trdsql [OPTIONS] [ARGS]\nTry 'trdsql --help' for more information.\n").rc
- `eval.tests.test_config_handling.test_invalid_json_config_with_config_flag_is_fatal_and_mentions_config_error`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-config', '/tmp/trdsql-home-vq382kjd/bad.json', '-dblist'], returncode=2, stdout=b'', stderr=b"trdsql: unknown option: -dblist\nusage: tr
- `tests.test_ext_readers_writers.test_ext_analyze_missing_file_errors`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-a', 'testdata/nofile'], returncode=2, stdout=b'', stderr=b"trdsql: unknown option: -a\nusage: trdsql [OPTIONS] [ARGS]\nTry 'trdsql --hel
- *(... 14 more in this cluster)*

### `rc_mismatch_got0_want2` — 5 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_basic_invocation.test_help_flag`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['./executable', '--help'], returncode=0, stdout=b'trdsql 0.1.0 - bootstrap scaffold\n\nUsage: trdsql [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -
- `eval.tests.test_help_output.test_help_exit_code_is_two_for_dash_help`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--help'], returncode=0, stdout='trdsql 0.1.0 - bootstrap scaffold\n\nUsage: trdsql [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print h
- `eval.tests.test_help_output.test_help_with_invalid_argument_still_shows_usage`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--help', '--definitely-not-a-flag'], returncode=0, stdout='trdsql 0.1.0 - bootstrap scaffold\n\nUsage: trdsql [OPTIONS] [ARGS]\n\nOptions
- *(... 2 more in this cluster)*

### `bytes_output_mismatch` — 3 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_basic.TestStdinInput.test_stdin_with_query`
  > assert b'Error: near... syntax error' == b'Orange\nMelon\nApple\n'
  >   
  >   At index 0 diff: b'E' != b'O'
  >   
  >   Full diff:
  >   - (b'Orange\nMelon\nApple\n')
  >   + (b'Error: near "-": syntax error')
- `tests.test_ext_readers_writers.test_ext_json_object_single_row`
  > assert b'Error: near... syntax error' == b'b\n'
  >   
  >   At index 0 diff: b'E' != b'b'
  >   
  >   Full diff:
  >   - b'b\n'
  >   + (b'Error: near "-": syntax error')
- `tests.test_ext_readers_writers.test_ext_json_null_literal_becomes_empty_line`
  > assert b'Error: near... syntax error' == b'1\n\n3\n'
  >   
  >   At index 0 diff: b'E' != b'1'
  >   
  >   Full diff:
  >   - (b'1\n\n3\n')
  >   + (b'Error: near "-": syntax error')

### `rc_unexpected_zero` — 2 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `eval.tests.test_argparse_validation.test_bool_with_equals_is_accepted[args0]`
  > assert 2 != 2
  >  +  where 2 = RunResult(rc=2, out='', err="trdsql: unknown option: -ig=false\nusage: trdsql [OPTIONS] [ARGS]\nTry 'trdsql --help' for more information.\n").rc
- `eval.tests.test_argparse_validation.test_bool_with_equals_is_accepted[args1]`
  > assert 2 != 2
  >  +  where 2 = RunResult(rc=2, out='', err="trdsql: unknown option: -ig=true\nusage: trdsql [OPTIONS] [ARGS]\nTry 'trdsql --help' for more information.\n").rc

### `boolean_false` — 2 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `eval.tests.test_help_output.test_help_ends_with_newline`
  > AssertionError: assert False
  >  +  where False = <built-in method endswith of str object at 0x7fec04ba0030>('\n')
  >  +    where <built-in method endswith of str object at 0x7fec04ba0030> = ''.endswith
- `eval.tests.test_io_behavior.test_version_flag_prints_version_and_exit_0`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7fa47c6ac670>('trdsql version')
  >  +    where <built-in method startswith of str object at 0x7fa47c6ac670> = 'trdsql 0.1.0\n'.startswith
  >  +      where 'trdsql 0.1.0\n' = <built-in method decode of bytes object at 0x7fa47cb6ca20>('utf-8', errors='replace')
  >  +        where <built-in method decode of bytes object at 0x7fa47cb6ca20> = b'trdsql 0.1.0\n'.decode
  >  +          where b'trdsql 0.1.0\n' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'trdsql 0.1.0\n', stderr=b'').stdout

### `rc_mismatch_got0_want1` — 2 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_ext_readers_writers.test_ext_json_invalid_json_errors`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-ijson', 'SELECT * FROM -'], returncode=0, stdout=b'Error: near "-": syntax error', stderr=b'').returncode
- `tests.test_ext_readers_writers.test_ext_ltsv_invalid_column_errors`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-iltsv', 'SELECT * FROM -'], returncode=0, stdout=b'Error: near "-": syntax error', stderr=b'').returncode

### `json_output_missing_or_bad` — 1 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `tests.test_cmd_gaps.test_multiple_output_format_flags_priority`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

