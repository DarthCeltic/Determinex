# Action Sheet — bootandy__dust.62bf1e1

**Current:** 17.64%  (200/1134)
**Pass / Fail / Skip:** 200 / 749 / 16
**Gap to 100%:** 82.36 percentage points (934 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_exact_output.test_permission_normal`
  - reason: root bypasses file permission restrictions
- `tests.test_exact_output.test_permission_flag`
  - reason: root bypasses file permission restrictions
- `eval.tests.test_behavior_tree.test_skip_total_removes_total_row`
  - reason: test_skip_total_removes_total_row depends on test_basic_run_includes_root_and_children
- `eval.tests.test_behavior_tree.test_depth_limits_recursion`
  - reason: test_depth_limits_recursion depends on test_basic_run_includes_root_and_children
- `eval.tests.test_behavior_tree.test_number_of_lines_limits_output`
  - reason: test_number_of_lines_limits_output depends on test_basic_run_includes_root_and_children
- *(... 11 more skipped)*

## Failure clusters

749 failed tests grouped into 13 buckets (sorted by count).

### `rc_mismatch_got2_want0` — 450 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_advanced_features.test_collapse_option`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '-P', '--collapse', 'node_modules', '/tmp/tmpasphzo1q'], returncode=2, stdout=b'', stderr=b'dust: error: unrecognized argument: -P\n').returncode
- `tests.test_advanced_features.test_no_color_env_variable`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '-P', '/tmp/tmpcsu_8tln'], returncode=2, stdout=b'', stderr=b'dust: error: unrecognized argument: -P\n').returncode
- `tests.test_advanced_features.test_tree_visualization`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '-P', '-c', '/tmp/tmp40q0qv1j'], returncode=2, stdout=b'', stderr=b'dust: error: unrecognized argument: -P\n').returncode
- *(... 447 more in this cluster)*

### `other_assertion` — 214 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_help_flag`
  > AssertionError: assert b'Like du but more intuitive' in b'dust 0.8.6\nUsage: dust [OPTIONS] [PATH]...\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -d, --depth <DEPTH>  D
  >  +  where b'dust 0.8.6\nUsage: dust [OPTIONS] [PATH]...\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -d, --depth <DEPTH>  Depth to show\n  -t, --threads <THREADS>  Numbe
- `tests.test_basic_invocation.test_help_short_flag`
  > AssertionError: assert b'Like du but more intuitive' in b'dust 0.8.6\nUsage: dust [OPTIONS] [PATH]...\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -d, --depth <DEPTH>  D
  >  +  where b'dust 0.8.6\nUsage: dust [OPTIONS] [PATH]...\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -d, --depth <DEPTH>  Depth to show\n  -t, --threads <THREADS>  Numbe
- `tests.test_basic_invocation.test_version_flag`
  > AssertionError: assert b'Dust' in b'dust 0.8.6\n'
  >  +  where b'dust 0.8.6\n' = CompletedProcess(args=['./executable', '--version'], returncode=0, stdout=b'dust 0.8.6\n', stderr=b'').stdout
- *(... 211 more in this cluster)*

### `string_output_mismatch` — 30 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_argparse_validation.test_overflow_integer_errors`
  > AssertionError: assert '108.0KiB  sr... pytest.ini\n' == ''
  >   
  >   + 108.0KiB  src
  >   + 24.0KiB  display.rs
  >   + 16.0KiB  config.rs
  >   + 16.0KiB  dir_walker.rs
  >   + 16.0KiB  main.rs
  >   + 12.0KiB  platform.rs...
- `eval.tests.test_argparse_validation.test_non_repeatable_flags_rejected[args0]`
  > AssertionError: assert '108.0KiB  sr... pytest.ini\n' == ''
  >   
  >   + 108.0KiB  src
  >   + 24.0KiB  display.rs
  >   + 16.0KiB  config.rs
  >   + 16.0KiB  dir_walker.rs
  >   + 16.0KiB  main.rs
  >   + 12.0KiB  platform.rs...
- `eval.tests.test_help_baseline.test_help_long_matches_fixture_exactly`
  > AssertionError: assert 'dust 0.8.6\n...reference\n\n' == 'Like du but ...Print version'
  >   
  >   + dust 0.8.6
  >   - Like du but more intuitive
  >   - 
  >   - Usage: executable [OPTIONS] [PATH]...
  >   ?        ^^^^  ----
  >   + Usage: dust [OPTIONS] [PATH]......
- *(... 27 more in this cluster)*

### `rc_mismatch_got1_want0` — 25 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_arg_parsing.TestNumberOfLinesFlag.test_number_of_lines_short`
  > assert 1 == 0
- `tests.test_arg_parsing.TestStringValueFlags.test_invert_filter_flag`
  > assert 1 == 0
- `tests.test_arg_parsing.TestMultipleValueFlags.test_multiple_invert_filter_flags`
  > assert 1 == 0
- *(... 22 more in this cluster)*

### `rc_mismatch_got0_want2` — 7 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_arg_parsing.TestNumberOfLinesFlag.test_number_of_lines_missing_value`
  > assert 0 == 2
- `tests.test_arg_parsing.TestBooleanFlags.test_boolean_flag_short_and_long[-p---full-paths]`
  > assert 0 == 2
- `tests.test_arg_parsing.TestBooleanFlags.test_boolean_flag_short_and_long[-L---dereference-links]`
  > assert 0 == 2
- *(... 4 more in this cluster)*

### `rc_mismatch_got2_want1` — 6 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_argparse_validation.test_double_dash_makes_dashlike_value_positional_not_flag`
  > assert 2 == 1
- `tests.test_coverage_push.test_invalid_regex_filter_exits_with_error`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--filter', '[invalid'], returncode=2, stdout='', stderr='dust: error: unrecognized argument: --filter\n').returncode
- `tests.test_coverage_push.test_invalid_regex_invert_filter_exits_with_error`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--invert-filter', '(?P<unclosed'], returncode=2, stdout='', stderr='dust: error: unrecognized argument: --invert-filter\n').returncode
- *(... 3 more in this cluster)*

### `bytes_output_mismatch` — 5 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_error_handling.test_permission_denied_message`
  > AssertionError: assert (2 == 0 or b'permission' in b'dust: error: unrecognized argument: -p\n' or b'No such' in b'dust: error: unrecognized argument: -P\n' or 0 > 0)
  >  +  where 2 = CompletedProcess(args=['./executable', '-P', '/root'], returncode=2, stdout=b'', stderr=b'dust: error: unrecognized argument: -P\n').returncode
  >  +  and   b'dust: error: unrecognized argument: -p\n' = <built-in method lower of bytes object at 0x7f0384a880d0>()
  >  +    where <built-in method lower of bytes object at 0x7f0384a880d0> = b'dust: error: unrecognized argument: -P\n'.lower
  >  +      where b'dust: error: unrecognized argument: -P\n' = CompletedProcess(args=['./executable', '-P', '/root'], returncode=2, stdout=b'', stderr=b'dust: error: unrecognized argument: -P\n').stderr
  >  +  and   b'dust: error: unrecognized argument: -P\n' = CompletedProcess(args=['./executable', '-P', '/root'], returncode=2, stdout=b'', stderr=b'dust: error: unrecognized argument: -P\n').stderr
  >  +  and   0 = len(b'')
  >  +    where b'' = CompletedProcess(args=['./executable', '-P', '/root'], returncode=2, stdout=b'', stderr=b'dust: error: unrecognized argument: -P\n').stdout
- `tests.test_flags.test_basic_output`
  > AssertionError: assert b'dust: error...rgument: -P\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'dust: error: unrecognized argument: -P\n')
- `tests.test_flags.test_reverse_flag`
  > AssertionError: assert b'dust: error...rgument: -P\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'dust: error: unrecognized argument: -P\n')
- *(... 2 more in this cluster)*

### `rc_mismatch_got0_want1` — 4 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_error_paths.test_multiple_nonexistent_paths_comma_separated`
  > assert 0 == 1
  >  +  where 0 = <built-in method count of str object at 0x7f1376eb32d0>('No such file or directory:')
  >  +    where <built-in method count of str object at 0x7f1376eb32d0> = "dust: error: path '/path/one' does not exist\n".count
  >  +      where "dust: error: path '/path/one' does not exist\n" = CompletedProcess(args=['/workspace/executable', '/path/one', '/path/two', '/path/three'], returncode=1, stdout='', stderr="dust: error:
- `tests.test_error_paths.test_file_not_found_error_aggregation_order_independence`
  > assert 0 == 1
  >  +  where 0 = <built-in method count of str object at 0x7f1376eb2790>('No such file or directory:')
  >  +    where <built-in method count of str object at 0x7f1376eb2790> = "dust: error: path '/missing/0' does not exist\n".count
  >  +      where "dust: error: path '/missing/0' does not exist\n" = CompletedProcess(args=['/workspace/executable', '/missing/0', '/missing/1', '/missing/2', '/missing/3', '/missing/4'], returncode=1, s
- `tests.test_error_paths.test_nonexistent_paths_with_special_chars`
  > assert 0 == 1
  >  +  where 0 = <built-in method count of str object at 0x7f1377282720>('No such file or directory:')
  >  +    where <built-in method count of str object at 0x7f1377282720> = "dust: error: path '/path with spaces/missing' does not exist\n".count
  >  +      where "dust: error: path '/path with spaces/missing' does not exist\n" = CompletedProcess(args=['/workspace/executable', '/path with spaces/missing', "/path/with'quotes/missing", '/path/with"d
- *(... 1 more in this cluster)*

### `rc_mismatch_got1_want2` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_arg_parsing.TestNumberOfLinesFlag.test_number_of_lines_invalid_value`
  > assert 1 == 2
- `tests.test_cli.test_invalid_number_of_lines`
  > assert 1 == 2
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-n', 'invalid'], returncode=1, stdout='', stderr="dust: error: path 'invalid' does not exist\n").returncode

### `rc_unexpected_zero` — 2 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_edge_cases.test_terminal_width_panic_too_narrow`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-w', '5', '/tmp/pytest-of-root/pytest-0/test_terminal_width_panic_too_2/test'], returncode=0, stdout='4.0KiB  file.txt\n', stderr='').ret
- `tests.test_edge_cases.test_terminal_width_panic_narrow_for_tree`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-w', '10', '/tmp/pytest-of-root/pytest-0/test_terminal_width_panic_narr2/test'], returncode=0, stdout='4.0KiB  file.txt\n', stderr='').re

### `empty_list_or_string` — 2 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_error_paths.test_multiple_errors_exact_format_with_commas`
  > IndexError: list index out of range
- `tests.test_gap_fill.test_filecount_mode`
  > IndexError: list index out of range

### `returned_none` — 1 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_content.test_help_has_usage_line`
  > AssertionError: assert None is not None
  >  +  where None = <function search at 0x7fe5c0142680>('^Usage: executable \\[OPTIONS\\] \\[PATH\\]\\.\\.\\.$', 'dust 0.8.6\nUsage: dust [OPTIONS] [PATH]...\n\nOptions:\n  -h, --help     Print help\n  -
  >  +    where <function search at 0x7fe5c0142680> = re.search
  >  +    and   re.MULTILINE = re.M

### `boolean_false` — 1 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `eval.tests.test_io_behavior.test_version_to_stdout_and_exit0`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of bytes object at 0x7f6183f21380>(b'Dust ')
  >  +    where <built-in method startswith of bytes object at 0x7f6183f21380> = b'dust 0.8.6\n'.startswith
  >  +      where b'dust 0.8.6\n' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'dust 0.8.6\n', stderr=b'').stdout

