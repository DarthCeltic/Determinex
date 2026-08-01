# Action Sheet — miserlou__loop.209927c

**Current:** 20.2%  (226/1119)
**Pass / Fail / Skip:** 226 / 552 / 0
**Gap to 100%:** 79.80 percentage points (893 tests)

## Failure clusters

552 failed tests grouped into 44 buckets (sorted by count).

### `string_output_mismatch` — 203 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_conditional_stopping.test_until_contains_partial_match`
  > AssertionError: assert '' == 'testing'
  >   
  >   - testing
- `tests.test_conditional_stopping.test_until_changes_single_item`
  > AssertionError: assert '' == 'a'
  >   
  >   - a
- `tests.test_counter.test_count_with_items`
  > AssertionError: assert '2' == '1'
  >   
  >   - 1
  >   + 2
- *(... 200 more in this cluster)*

### `other_assertion` — 103 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_command_execution.test_command_environment_variables`
  > AssertionError: assert 'C=0 I=x' in 'hello world'
- `tests.test_command_execution.test_command_actualcount_variable`
  > AssertionError: assert '0 0' in 'hello world'
- `tests.test_command_execution.test_command_multiple_statements`
  > AssertionError: assert 'first' in 'done\n'
- *(... 100 more in this cluster)*

### `bytes_output_mismatch` — 57 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_command_execution.test_exit_code_success`
  > AssertionError: assert b'*\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + b'*\n'
- `tests.test_command_execution.test_exit_code_failure`
  > AssertionError: assert b'*\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + b'*\n'
- `tests.test_command_execution.test_command_with_redirects`
  > AssertionError: assert b'hello world\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'hello world\n')
- *(... 54 more in this cluster)*

### `rc_mismatch_got0_want1` — 32 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_comprehensive_coverage.test_only_last_captures_final_iteration`
  > AssertionError: assert 0 == 1
  >  +  where 0 = <built-in method count of bytes object at 0x7fa9c2137ea0>(b'final')
  >  +    where <built-in method count of bytes object at 0x7fa9c2137ea0> = b'110\nx\n'.count
  >  +      where b'110\nx\n' = CompletedProcess(args=['./executable', '--num', '5', '--only-last', '--', 'echo', 'final'], returncode=0, stdout=b'110\nx\n', stderr=b'').stdout
- `tests.test_comprehensive_coverage.test_combination_summary_and_only_last`
  > AssertionError: assert 0 == 1
  >  +  where 0 = <built-in method count of bytes object at 0x7fa9c3472160>(b'final')
  >  +    where <built-in method count of bytes object at 0x7fa9c3472160> = b'110\nx\n'.count
  >  +      where b'110\nx\n' = CompletedProcess(args=['./executable', '--num', '3', '--summary', '--only-last', '--', 'echo', 'final'], returncode=0, stdout=b'110\nx\n', stderr=b'').stdout
- `tests.test_flag_combinations.test_only_last_with_every`
  > AssertionError: assert 0 == 1
  >  +  where 0 = <built-in method count of bytes object at 0x7fa9c34729d0>(b'2')
  >  +    where <built-in method count of bytes object at 0x7fa9c34729d0> = b'b\nx\n50\n'.count
  >  +      where b'b\nx\n50\n' = CompletedProcess(args=['./executable', '--num', '3', '--only-last', '--every', '10ms', '--', 'echo', '$COUNT'], returncode=0, stdout=b'b\nx\n50\n', stderr=b'').stdout
- *(... 29 more in this cluster)*

### `rc_mismatch_got1_want3` — 27 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_command_execution.test_command_with_arithmetic`
  > AssertionError: assert 1 == 3
  >  +  where 1 = len(['done'])
- `tests.test_command_execution.test_command_with_conditionals`
  > AssertionError: assert 1 == 3
  >  +  where 1 = len(['done'])
- `tests.test_conditional_stopping.test_until_contains_basic`
  > AssertionError: assert 1 == 3
  >  +  where 1 = len([''])
- *(... 24 more in this cluster)*

### `rc_unexpected_zero` — 17 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_error_handling.test_invalid_flag`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '--invalid-flag'], returncode=0, stdout=b'No command supplied\ntest\na\n', stderr=b'').returncode
- `tests.test_error_handling.test_invalid_every_duration`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '--every', 'invalid', '--num', '1', '--', 'echo test'], returncode=0, stdout=b'No command supplied\ntest\na\n', stderr=b'').returncode
- `tests.test_error_handling.test_invalid_num_value`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '--num', 'abc', '--', 'echo test'], returncode=0, stdout=b'No command supplied\ntest\na\n', stderr=b'').returncode
- *(... 14 more in this cluster)*

### `rc_mismatch_got1_want2` — 16 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_command_execution.test_simple_command`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len(['hello world'])
- `tests.test_conditional_stopping.test_until_changes_immediate`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len([''])
- `tests.test_conditional_stopping.test_until_contains_case_sensitive`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len([''])
- *(... 13 more in this cluster)*

### `rc_mismatch_got0_want2` — 14 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_additional_coverage.test_stdin_empty_with_num`
  > AssertionError: assert 0 == 2
  >  +  where 0 = <built-in method count of bytes object at 0x7fa9c4214030>(b'test')
  >  +    where <built-in method count of bytes object at 0x7fa9c4214030> = b''.count
  >  +      where b'' = CompletedProcess(args=['./executable', '--num', '2', '--', 'echo', 'test'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_basic_invocation.test_command_without_separator`
  > AssertionError: assert 0 == 2
  >  +  where 0 = <built-in method count of bytes object at 0x7fa9c4214030>(b'test')
  >  +    where <built-in method count of bytes object at 0x7fa9c4214030> = b''.count
  >  +      where b'' = CompletedProcess(args=['./executable', '--num', '2', 'echo test'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_comprehensive_coverage.test_combined_time_units`
  > AssertionError: assert 0 == 2
  >  +  where 0 = <built-in method count of bytes object at 0x7fa9c2dfbf50>(b'combined')
  >  +    where <built-in method count of bytes object at 0x7fa9c2dfbf50> = b'key=value\nfoo=bar\nhttp://example.com\nftp://test.com\n/tmp/file1.txt\n/home/user/file2.txt\n./relative.txt\na\nb\nc[d]e\n'.c
  >  +      where b'key=value\nfoo=bar\nhttp://example.com\nftp://test.com\n/tmp/file1.txt\n/home/user/file2.txt\n./relative.txt\na\nb\nc[d]e\n' = CompletedProcess(args=['./executable', '--num', '2', '--e
- *(... 11 more in this cluster)*

### `rc_mismatch_got1_want4` — 12 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_conditional_stopping.test_until_changes_basic`
  > AssertionError: assert 1 == 4
  >  +  where 1 = len([''])
- `tests.test_termination.test_multiple_until_conditions_first_wins`
  > AssertionError: assert 1 == 4
  >  +  where 1 = len([''])
- `tests.test_termination.test_until_contains_multiline_output`
  > AssertionError: assert 1 == 4
  >  +  where 1 = len([''])
- *(... 9 more in this cluster)*

### `rc_mismatch_got1_want5` — 9 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_edge_cases.test_until_changes_no_change`
  > AssertionError: assert 1 == 5
  >  +  where 1 = len([''])
- `tests.test_comprehensive_coverage.test_for_with_duplicate_values`
  > AssertionError: assert 1 == 5
  >  +  where 1 = len([b''])
- `tests.test_termination.test_until_contains_not_found`
  > AssertionError: assert 1 == 5
  >  +  where 1 = len([''])
- *(... 6 more in this cluster)*

### `boolean_false` — 8 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_command_execution.test_command_file_creation`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpv_dhnqz6/file0.txt').exists
  >  +      where PosixPath('/tmp/tmpv_dhnqz6/file0.txt') = Path('/tmp/tmpv_dhnqz6/file0.txt')
- `tests.test_edge_cases.test_until_time_future`
  > assert False
  >  +  where False = all(<generator object test_until_time_future.<locals>.<genexpr> at 0x7f004fc86500>)
- `tests.test_edge_cases.test_zero_count_by`
  > assert False
  >  +  where False = all(<generator object test_zero_count_by.<locals>.<genexpr> at 0x7fa9c218bd10>)
- *(... 5 more in this cluster)*

### `rc_mismatch_got0_want3` — 7 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_basic_echo_loop`
  > AssertionError: assert 0 == 3
  >  +  where 0 = <built-in method count of bytes object at 0x7fa9c4214030>(b'hello')
  >  +    where <built-in method count of bytes object at 0x7fa9c4214030> = b''.count
  >  +      where b'' = CompletedProcess(args=['./executable', '--num', '3', '--', 'echo', 'hello'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_comprehensive_coverage.test_until_changes_with_countdown`
  > AssertionError: assert 0 == 3
  >  +  where 0 = <built-in method count of bytes object at 0x7fa9c353e280>(b'3')
  >  +    where <built-in method count of bytes object at 0x7fa9c353e280> = b'a\nb\n'.count
  >  +      where b'a\nb\n' = CompletedProcess(args=['./executable', '--for', '3,3,3,2,1,1', '--until-changes', '--', 'echo', '$ITEM'], returncode=0, stdout=b'a\nb\n', stderr=b'').stdout
- `tests.test_comprehensive_coverage.test_until_match_no_match`
  > AssertionError: assert 0 == 3
  >  +  where 0 = <built-in method count of bytes object at 0x7fa9c211bc00>(b'abc')
  >  +    where <built-in method count of bytes object at 0x7fa9c211bc00> = b'110\n'.count
  >  +      where b'110\n' = CompletedProcess(args=['./executable', '--num', '3', '--until-match', 'xyz', '--', 'echo', 'abc'], returncode=0, stdout=b'110\n', stderr=b'').stdout
- *(... 4 more in this cluster)*

### `returned_none` — 3 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_basic_invocation.test_version_flag`
  > AssertionError: assert None
  >  +  where None = <function match at 0x7f00518cd120>(b'loop \\d+\\.\\d+\\.\\d+', b'loop\n0.6.1\nloop\n0.6.1')
  >  +    where <function match at 0x7f00518cd120> = re.match
  >  +    and   b'loop\n0.6.1\nloop\n0.6.1' = <built-in method strip of bytes object at 0x7f004fc8d070>()
  >  +      where <built-in method strip of bytes object at 0x7f004fc8d070> = b'loop\n0.6.1\nloop\n0.6.1\n'.strip
  >  +        where b'loop\n0.6.1\nloop\n0.6.1\n' = CompletedProcess(args=['./executable', '--version'], returncode=0, stdout=b'loop\n0.6.1\nloop\n0.6.1\n', stderr=b'').stdout
- `eval.tests.test_help_output.test_usage_line_mentions_executable_and_placeholders`
  > AssertionError: assert None is not None
  >  +  where None = <function search at 0x7f7972166680>('^\\s*executable\\s+\\[FLAGS\\]\\s+\\[OPTIONS\\]\\s+\\[input\\]\\.\\.\\.\\s*$', 'USAGE:\nFLAGS:\nOPTIONS:\nARGS:\nloop\n--version\n--help\nUSAGE:\n
  >  +    where <function search at 0x7f7972166680> = re.search
  >  +    and   re.MULTILINE = re.M
- `eval.tests.test_help_output.test_help_documents_args_input_variadic`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f7972166680>('^\\s*<input>\\.\\.\\.\\s+The command to be looped\\s*$', 'USAGE:\nFLAGS:\nOPTIONS:\nARGS:\nloop\n--version\n--help\nUSAGE:\nFLAGS:\nOPTIONS:\n', r
  >  +    where <function search at 0x7f7972166680> = re.search
  >  +    and   re.MULTILINE = re.M

### `rc_mismatch_got1_want10` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_edge_cases.test_multiple_stdin_lines_with_count`
  > AssertionError: assert 1 == 10
  >  +  where 1 = len([''])
- `tests.test_termination.test_until_match_case_sensitive`
  > AssertionError: assert 1 == 10
  >  +  where 1 = len(['110'])
- `tests.test_termination.test_until_contains_case_sensitive`
  > AssertionError: assert 1 == 10
  >  +  where 1 = len([''])

### `rc_mismatch_got0_want124` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_errors_and_exit_codes.test_duration_error_flag_exits_124_when_for_duration_elapsed`
  > AssertionError: assert 0 == 124
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--for-duration', '1ms', '-D', '--every', '1us', '--', 'false'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_timing.TestForDuration.test_for_duration_with_error_flag`
  > assert 0 == 124
- `tests.test_timing.test_error_duration_exit_code_124`
  > AssertionError: assert 0 == 124
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--for-duration', '100ms', '--error-duration', '--', 'echo', 'timeout'], returncode=0, stdout='', stderr='').returncode

### `rc_mismatch_got1_want6` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_termination.test_until_error_multiple_different_codes`
  > AssertionError: assert 1 == 6
  >  +  where 1 = len([''])
- `tests.test_termination.test_termination_with_offset_counter`
  > AssertionError: assert 1 == 6
  >  +  where 1 = len([''])
- `tests.test_termination.test_termination_with_count_by_fractional`
  > AssertionError: assert 1 == 6
  >  +  where 1 = len([''])

### `rc_mismatch_got3_want2` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_counter.test_offset_negative`
  > AssertionError: assert 3 == 2
  >  +  where 3 = len(['0', '1', '2'])
- `tests.test_additional_coverage.test_count_by_very_small`
  > AssertionError: assert 3 == 2
  >  +  where 3 = len([b'0.00000', b'0.00001', b'running'])

### `rc_mismatch_got50_want3` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_edge_cases.test_for_newline_separated`
  > AssertionError: assert 50 == 3
  >  +  where 50 = len(['(', '*', '-1', '-4', '-7', '0', ...])
- `tests.test_error_handling.test_for_with_newlines`
  > AssertionError: assert 50 == 3
  >  +  where 50 = len(['(', '*', '-1', '-4', '-7', '0', ...])

### `rc_mismatch_got10_want3` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_comprehensive_coverage.test_regex_with_groups`
  > AssertionError: assert 10 == 3
  >  +  where 10 = len([b'hello', b'x', b'y', b'key=value', b'foo=bar', b'http://example.com', ...])
- `tests.test_termination.test_until_conditions_with_for_iterations`
  > AssertionError: assert 10 == 3
  >  +  where 10 = len(['a', 'b', 'c[d]e', 'a', 'b', 'c', ...])

### `rc_mismatch_got5_want2` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_comprehensive_coverage.test_stdin_with_counter_mods`
  > AssertionError: assert 5 == 2
  >  +  where 5 = len(['110', 'x', '0', '1000000', '2000000'])
- `tests.test_edge_cases.test_special_shell_chars_in_items`
  > AssertionError: assert 5 == 2
  >  +  where 5 = len([b'0', b'1000000', b'0.0000', b'0.0001', b'start0'])

### `rc_mismatch_got0_want5` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_comprehensive_coverage.test_every_minimal_delay`
  > AssertionError: assert 0 == 5
  >  +  where 0 = <built-in method count of bytes object at 0x7fa9c2fc5ca0>(b'fast')
  >  +    where <built-in method count of bytes object at 0x7fa9c2fc5ca0> = b'a\nb\nc\ncat\ndog\nbird\nabc\nABC\ntest\ntesting\n'.count
  >  +      where b'a\nb\nc\ncat\ndog\nbird\nabc\nABC\ntest\ntesting\n' = CompletedProcess(args=['./executable', '--num', '5', '--', 'echo', 'fast'], returncode=0, stdout=b'a\nb\nc\ncat\ndog\nbird\nabc\nA
- `eval.tests.test_until_conditions.test_until_changes_and_same_basic[--until-changes-echo 1-5]`
  > AssertionError: assert 0 == 5
  >  +  where 0 = len([])
  >  +    where [] = <built-in method splitlines of bytes object at 0x7f20e5db0030>()
  >  +      where <built-in method splitlines of bytes object at 0x7f20e5db0030> = b''.splitlines
  >  +        where b'' = CompletedProcess(args=['/workspace/executable', '--until-changes', '--num', '5', '--', 'sh', '-c', 'echo 1'], returncode=0, stdout=b'', stderr=b'').stdout

### `rc_mismatch_got1_want11` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_termination.test_until_match_complex_regex`
  > AssertionError: assert 1 == 11
  >  +  where 1 = len(['110'])
- `tests.test_termination.test_infinite_loop_with_until_condition`
  > AssertionError: assert 1 == 11
  >  +  where 1 = len([''])

### `rc_mismatch_got1_want200` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_termination.test_until_changes_with_very_long_output`
  > AssertionError: assert 1 == 200
  >  +  where 1 = len(['hello world'])
- `tests.test_termination.test_until_same_with_very_long_identical_output`
  > AssertionError: assert 1 == 200
  >  +  where 1 = len([''])

### `rc_mismatch_got1_want50` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_edge_cases.test_stdin_many_lines`
  > AssertionError: assert 1 == 50
  >  +  where 1 = len([''])

### `rc_mismatch_got3_want4` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_iteration.test_num_iterations`
  > AssertionError: assert 3 == 4
  >  +  where 3 = len(['a', 'b', 'c'])

### `rc_mismatch_got3_want5` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_iteration.test_num_with_count`
  > AssertionError: assert 3 == 5
  >  +  where 3 = len(['a', 'b', 'c'])

### `rc_mismatch_got50_want20` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_iteration.test_for_many_items`
  > AssertionError: assert 50 == 20
  >  +  where 50 = len(['(', '*', '-1', '-4', '-7', '0', ...])

### `uncategorized` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_timing.test_for_duration_with_only_last`
  > ValueError: invalid literal for int() with base 10: ''

### `rc_mismatch_got5_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_additional_coverage.test_precision_with_scientific_notation`
  > AssertionError: assert 5 == 3
  >  +  where 5 = len(['0.0', '0.1', '0.00000', '0.00001', 'running'])

### `rc_mismatch_got8_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_comprehensive_coverage.test_offset_with_floats`
  > AssertionError: assert 8 == 3
  >  +  where 8 = len(['2.0', '-7', '-4', '-1', 'arg1 arg2 arg3 arg4 arg5', 'test with spaces', ...])

### `rc_mismatch_got6_want100` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_comprehensive_coverage.test_count_with_many_iterations`
  > AssertionError: assert 6 == 100
  >  +  where 6 = len([b'0', b'1000000', b'2000000', b'test', b'0.000000000', b'0.123456789'])

### `rc_mismatch_got3_want50` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_comprehensive_coverage.test_for_with_many_items`
  > AssertionError: assert 3 == 50
  >  +  where 3 = len([b'red', b'green', b'blue'])

### `rc_mismatch_got10_want2` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_comprehensive_coverage.test_regex_case_sensitivity`
  > AssertionError: assert 10 == 2
  >  +  where 10 = len([b'abc', b'ABC', b'test', b'testing', b'test123', b'word1', ...])

### `rc_mismatch_got1_want20` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_comprehensive_coverage.test_very_fast_iterations`
  > AssertionError: assert 1 == 20
  >  +  where 1 = len([b''])

### `rc_mismatch_got4_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_flag_combinations.test_count_by_negative`
  > AssertionError: assert 4 == 3
  >  +  where 4 = len(['test', 'test', 'B', 'test'])

### `rc_mismatch_got7_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_flag_combinations.test_for_empty_item`
  > AssertionError: assert 7 == 3
  >  +  where 7 = len([b'test', b'test', b'B', b'test', b'cat', b'dog', ...])

### `rc_mismatch_got3_want200` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_flag_combinations.test_very_long_for_list`
  > AssertionError: assert 3 == 200
  >  +  where 3 = len([b'red', b'green', b'blue'])

### `rc_mismatch_got0_want7` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_iteration_control.test_num_iterations`
  > AssertionError: assert 0 == 7
  >  +  where 0 = <built-in method count of bytes object at 0x7fa9c2f84780>(b'x')
  >  +    where <built-in method count of bytes object at 0x7fa9c2f84780> = b'test\ntest\n'.count
  >  +      where b'test\ntest\n' = CompletedProcess(args=['./executable', '--num', '7', '--', 'echo', 'x'], returncode=0, stdout=b'test\ntest\n', stderr=b'').stdout

### `missing_file` — 1 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_integration.TestRealWorldScenarios.test_retry_logic`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmp8w_q7sy5/counter.txt'

### `empty_list_or_string` — 1 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_output.TestSummary.test_summary_format`
  > IndexError: list index out of range

### `rc_mismatch_got0_want10` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_termination.test_until_same_with_whitespace_differences`
  > assert 0 == 10
  >  +  where 0 = len([])

### `rc_mismatch_got7_want1` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_termination.test_until_fail_immediate`
  > AssertionError: assert 7 == 1
  >  +  where 7 = len(['same', 'different', '1', '2', 'a', 'd', ...])

### `rc_mismatch_got7_want5` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_termination.test_until_fail_all_succeed`
  > AssertionError: assert 7 == 5
  >  +  where 7 = len(['same', 'different', '1', '2', 'a', 'd', ...])

### `rc_mismatch_got1_want24` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_termination.test_until_match_multiline_output`
  > AssertionError: assert 1 == 24
  >  +  where 1 = len(['110'])

