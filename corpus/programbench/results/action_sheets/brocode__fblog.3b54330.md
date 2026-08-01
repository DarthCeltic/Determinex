# Action Sheet — brocode__fblog.3b54330

**Current:** 19.08%  (307/1609)
**Pass / Fail / Skip:** 307 / 753 / 6
**Gap to 100%:** 80.92 percentage points (1302 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_fblog_behavior.test_with_prefix_snapshot`
  - reason: test_with_prefix_snapshot depends on test_sample_json_log_default_snapshot
- `eval.tests.test_fblog_behavior.test_dump_all_snapshot`
  - reason: test_dump_all_snapshot depends on test_sample_json_log_default_snapshot
- `eval.tests.test_fblog_behavior.test_additional_values_snapshot`
  - reason: test_additional_values_snapshot depends on test_sample_json_log_default_snapshot
- `eval.tests.test_fblog_behavior.test_filter_level_not_info_snapshot`
  - reason: test_filter_level_not_info_snapshot depends on test_sample_json_log_default_snapshot
- `eval.tests.test_fblog_behavior.test_no_implicit_filter_return_statement_snapshot`
  - reason: test_no_implicit_filter_return_statement_snapshot depends on test_sample_json_log_default_snapshot
- *(... 1 more skipped)*

## Failure clusters

753 failed tests grouped into 18 buckets (sorted by count).

### `other_assertion` — 374 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.TestBasicInvocation.test_help_flag`
  > AssertionError: assert b'json log viewer' in b''
  >  +  where b'' = CompletedProcess(args=['./executable', '--help'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_basic_invocation.TestBasicInvocation.test_help_short_flag`
  > AssertionError: assert b'json log viewer' in b''
  >  +  where b'' = CompletedProcess(args=['./executable', '-h'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_basic_invocation.TestBasicInvocation.test_stdin_with_simple_json_log`
  > AssertionError: assert b'test log' in b'#{key}\n&\n+10000-\n+11476-\n+17814-\n--dump-all\n--filter\n--help\n--nonexistent-flag\n--unknown-flag\n--version\n.\n1\n123abc\n19.99\n1969-12-31T23:59:59\n197
  >  +  where b'#{key}\n&\n+10000-\n+11476-\n+17814-\n--dump-all\n--filter\n--help\n--nonexistent-flag\n--unknown-flag\n--version\n.\n1\n123abc\n19.99\n1969-12-31T23:59:59\n1970-01-01T00:00:00\n1970-01-01
- *(... 371 more in this cluster)*

### `string_output_mismatch` — 268 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_config_env.test_xdg_config_home_is_used_for_default_config_path`
  > AssertionError: assert '#{key}\n&\n+...em details:\n' == 'CFG|hi\n'
  >   
  >   - CFG|hi
  >   + #{key}
  >   + &
  >   + +10000-
  >   + +11476-
  >   + +17814-...
- `tests.test_config_env.test_cli_main_line_format_overrides_config_file_value`
  > AssertionError: assert '\x1b[1m2024-...on starting\n' == 'CLI|hi\n'
  >   
  >   - CLI|hi
  >   + #x1B[1m2024-01-15T10:00:00#x1B[0m #x1B[1;32m INFO#x1B[0m: Application starting
  >   + [level] -> 30
  >   + [module] -> main
  >   + [msg] -> Application starting
- `eval.tests.test_externalized.test_ext_config_read_empty_level_map`
  > assert '{"message":"...Item details:' == 'info'
  >   
  >   - info
  >   + {"message":"x","time":"2017-07-06T15:21:16","level":"info"}
  >   + #{key}
  >   + &
  >   + +10000-
  >   + +11476-...
- *(... 265 more in this cluster)*

### `rc_mismatch_got0_want2` — 30 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_argument_parsing.TestBasicFlags.test_unknown_flag`
  > assert 0 == 2
- `tests.test_argument_parsing.TestBasicFlags.test_unknown_short_flag`
  > assert 0 == 2
- `tests.test_argument_parsing.TestBasicFlags.test_misspelled_flag`
  > assert 0 == 2
- *(... 27 more in this cluster)*

### `rc_unexpected_zero` — 26 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_configuration.TestConfiguration.test_missing_config_file_error`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '--config-file', '/nonexistent/config.toml'], returncode=0, stdout=b'from cli\n', stderr=b'').returncode
- `tests.test_error_handling.TestErrorHandling.test_conflicting_flags_additional_and_excluded`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '-a', 'field1', '-x', 'field2'], returncode=0, stdout=b'x\ntest\ntest\n', stderr=b'').returncode
- `tests.test_error_handling.TestErrorHandling.test_invalid_placeholder_format`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '-F', 'invalid'], returncode=0, stdout=b'x\ntest\ntest\nmessage\nmessage\n', stderr=b'').returncode
- *(... 23 more in this cluster)*

### `rc_mismatch_got101_want0` — 20 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_configuration.TestConfiguration.test_custom_config_file`
  > AssertionError: assert 101 == 0
  >  +  where 101 = CompletedProcess(args=['./executable', '--config-file', '/tmp/tmpj1btfv87/custom.toml'], returncode=101, stdout=b'\x1b[1m2024-01-01T10:00:00\x1b[0m \x1b[1;36mTRACE\x1b[0m: trace test\n
- `tests.test_configuration.TestConfiguration.test_config_with_level_map`
  > AssertionError: assert 101 == 0
  >  +  where 101 = CompletedProcess(args=['./executable', '--config-file', '/tmp/tmp7oiq4swm/config.toml'], returncode=101, stdout=b'\x1b[1m2024-01-01T10:00:00\x1b[0m \x1b[1;36mTRACE\x1b[0m: trace test\n
- `tests.test_configuration.TestConfiguration.test_config_with_custom_format`
  > AssertionError: assert 101 == 0
  >  +  where 101 = CompletedProcess(args=['./executable', '--config-file', '/tmp/tmpyyhivdst/format.toml'], returncode=101, stdout=b'\x1b[1m2024-01-01T10:00:00\x1b[0m \x1b[1;36mTRACE\x1b[0m: trace test\n
- *(... 17 more in this cluster)*

### `bytes_output_mismatch` — 11 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_basic_invocation.TestBasicInvocation.test_stdin_with_no_input`
  > AssertionError: assert b'#{key}\n&\n...em details:\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'#{key}\n&\n+10000-\n+11476-\n+17814-\n--dump-all\n--filter\n--help\n--nonexi'
  >   +  b'stent-flag\n--unknown-flag\n--version\n.\n1\n123abc\n19.99\n1969-12-31T23:5'
  >   +  b'9:59\n1970-01-01T00:00:00\n1970-01-01T00:00:01\n2023\n2023-01-01\n2023-06'
  >   +  b'-15T10:30:00\n2023-06-15T10:30:00Z\n2023-13-45T99:99:99\n2024-01-15\n2024-05'...
- `tests.test_file_input.TestFileInput.test_empty_file`
  > AssertionError: assert b'#{key}\n&\n...em details:\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'#{key}\n&\n+10000-\n+11476-\n+17814-\n--dump-all\n--filter\n--help\n--nonexi'
  >   +  b'stent-flag\n--unknown-flag\n--version\n.\n1\n123abc\n19.99\n1969-12-31T23:5'
  >   +  b'9:59\n1970-01-01T00:00:00\n1970-01-01T00:00:01\n2023\n2023-01-01\n2023-06'
  >   +  b'-15T10:30:00\n2023-06-15T10:30:00Z\n2023-13-45T99:99:99\n2024-01-15\n2024-05'...
- `tests.test_basic_invocation.test_empty_input`
  > AssertionError: assert b'#{key}\n&\n...em details:\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'#{key}\n&\n+10000-\n+11476-\n+17814-\n--dump-all\n--filter\n--help\n--nonexi'
  >   +  b'stent-flag\n--unknown-flag\n--version\n.\n1\n123abc\n19.99\n1969-12-31T23:5'
  >   +  b'9:59\n1970-01-01T00:00:00\n1970-01-01T00:00:01\n2023\n2023-01-01\n2023-06'
  >   +  b'-15T10:30:00\n2023-06-15T10:30:00Z\n2023-13-45T99:99:99\n2024-01-15\n2024-05'...
- *(... 8 more in this cluster)*

### `boolean_false` — 6 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_basic_invocation.TestBasicInvocation.test_version_flag`
  > assert False
  >  +  where False = any(<generator object TestBasicInvocation.test_version_flag.<locals>.<genexpr> at 0x7fbd2e77d310>)
- `eval.tests.test_help_output.test_help_ends_with_newline`
  > AssertionError: assert False
  >  +  where False = <built-in method endswith of str object at 0x7f7c6f87c030>('\n')
  >  +    where <built-in method endswith of str object at 0x7f7c6f87c030> = ''.endswith
  >  +      where '' = CompletedProcess(args=['/workspace/executable', '--help'], returncode=0, stdout='', stderr='').stdout
- `eval.tests.test_help_and_version.test_version_prints_fblog_and_semver_like`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7f858b02f8b0>('fblog ')
  >  +    where <built-in method startswith of str object at 0x7f858b02f8b0> = 'fblog'.startswith
- *(... 3 more in this cluster)*

### `returned_none` — 3 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_basic_invocation.test_version_output`
  > AssertionError: assert None
  >  +  where None = <function match at 0x7f3bde395120>(b'fblog \\d+\\.\\d+\\.\\d+', b'fblog\n')
  >  +    where <function match at 0x7f3bde395120> = re.match
  >  +    and   b'fblog\n' = CompletedProcess(args=['./executable', '--version'], returncode=0, stdout=b'fblog\n', stderr=b'').stdout
- `tests.test_basic_invocation.test_version_short_flag`
  > AssertionError: assert None
  >  +  where None = <function match at 0x7f3bde395120>(b'fblog \\d+\\.\\d+\\.\\d+', b'fblog\ntest log\nINFO\n2023-01-01\nfrom stdin\nfirst\nsecond\nnot valid json\n???\nnot json\n')
  >  +    where <function match at 0x7f3bde395120> = re.match
  >  +    and   b'fblog\ntest log\nINFO\n2023-01-01\nfrom stdin\nfirst\nsecond\nnot valid json\n???\nnot json\n' = CompletedProcess(args=['./executable', '-V'], returncode=0, stdout=b'fblog\ntest log\nINF
- `tests.test_edge_cases.test_version_flag_exit_zero`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f3ce2a6b760>('\\d+\\.\\d+\\.\\d+', 'fblog\n')
  >  +    where <function search at 0x7f3ce2a6b760> = <module 're' from '/usr/lib/python3.10/re.py'>.search

### `rc_mismatch_got0_want1` — 3 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_filtering.test_filter_boolean_and`
  > assert 0 == 1
  >  +  where 0 = len([])
- `tests.test_filtering.test_filter_nested_field`
  > assert 0 == 1
  >  +  where 0 = len([])
- `tests.test_filtering.test_filter_array_access`
  > assert 0 == 1
  >  +  where 0 = len([])

### `rc_mismatch_got0_want101` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_argument_parsing.TestPositionalArguments.test_nonexistent_file`
  > assert 0 == 101
- `tests.test_argument_parsing.TestPlaceholderFormatValidation.test_placeholder_format_missing_key`
  > assert 0 == 101
- `eval.tests.test_fblog_behavior.test_missing_file_panics_with_rc_101`
  > assert 0 == 101

### `uncategorized` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_help_output.test_help_has_program_title`
  > StopIteration
- `tests.test_edge_cases.test_dump_all_alphabetical_ordering`
  > ValueError: substring not found

### `rc_mismatch_got3_want2` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_filtering.test_filter_numeric_comparison`
  > AssertionError: assert 3 == 2
  >  +  where 3 = len(['INFO', 'prefix_test_suffix', 'with process'])

### `rc_mismatch_got10_want1` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_real_samples.test_sample_nested_with_filter`
  > AssertionError: assert 10 == 1
  >  +  where 10 = len(['test', '{', 'bartok', '0', 'Hello, world!', 'INFO', ...])

### `rc_mismatch_got101_want2` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_argument_parsing.TestFlagsWithValues.test_config_file_missing_value`
  > assert 101 == 2

### `rc_mismatch_got0_want1000` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_edge_cases.test_large_input`
  > AssertionError: assert 0 == 1000
  >  +  where 0 = len([])
  >  +    where [] = <built-in method splitlines of str object at 0x7f9732e7c030>()
  >  +      where <built-in method splitlines of str object at 0x7f9732e7c030> = ''.splitlines

### `empty_list_or_string` — 1 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_config.test_multiple_map_level_same_key_last_wins`
  > IndexError: list index out of range

### `rc_mismatch_got2049_want2000` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_stress.test_mixed_1k_valid_1k_invalid_interleaved_processing`
  > assert 2049 == 2000
  >  +  where 2049 = len(['{"message": "Valid entry 0", "level": "info"}', 'Invalid entry 0', '{"message": "Valid entry 1", "level": "info"}', 'Invalid entry 1', '{"message": "Valid entry 2", "level": "in

### `rc_mismatch_got60_want10` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_stress.test_50_map_level_flags_all_apply`
  > AssertionError: assert 60 == 10
  >  +  where 60 = len(['\x1b[1m                   \x1b[0m \x1b[1;35mMAPPE\x1b[0m: test 0', '\x1b[1m                   \x1b[0m \x1b[1;35mMAPPE\x1b[0m: test 1', '\x1b[1m                   \x1b[0m \x1b[1;35

