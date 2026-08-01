# Action Sheet — blacknon__hwatch.edfcb62

**Current:** 29.06%  (483/1662)
**Pass / Fail / Skip:** 483 / 704 / 3
**Gap to 100%:** 70.94 percentage points (1179 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_basic_tui.test_help_screen_opens`
  - reason: test_help_screen_opens depends on test_tui_launches
- `tests.test_basic_tui.test_help_screen_closes`
  - reason: test_help_screen_closes depends on test_help_screen_opens
- `tests.test_basic_tui.test_quit_with_q`
  - reason: test_quit_with_q depends on test_tui_launches

## Failure clusters

704 failed tests grouped into 16 buckets (sorted by count).

### `other_assertion` — 371 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_aftercommand_shell.test_precise_interval_timing`
  > AssertionError: assert 0 >= 2
  >  +  where 0 = <built-in method count of bytes object at 0x7f35d9562dd0>(b'====')
  >  +    where <built-in method count of bytes object at 0x7f35d9562dd0> = b'PRECISE\nSLOW\nUNLIMITED\nLIMITED\nHUGE\nA\nB\n'.count
  >  +      where b'PRECISE\nSLOW\nUNLIMITED\nLIMITED\nHUGE\nA\nB\n' = <conftest.run.<locals>.Result object at 0x7f35d94dad70>.stdout
- `tests.test_aftercommand_shell.test_very_short_interval`
  > AssertionError: assert 0 >= 5
  >  +  where 0 = <built-in method count of bytes object at 0x7f35d96193e0>(b'====')
  >  +    where <built-in method count of bytes object at 0x7f35d96193e0> = b'SLOW\nUNLIMITED\nLIMITED\nHUGE\nA\nB\n'.count
  >  +      where b'SLOW\nUNLIMITED\nLIMITED\nHUGE\nA\nB\n' = <conftest.run.<locals>.Result object at 0x7f35da74ceb0>.stdout
- `tests.test_basic_invocation.test_help_flag`
  > AssertionError: assert b'Usage:' in b'hwatch\n'
  >  +  where b'hwatch\n' = <conftest.run.<locals>.Result object at 0x7f35d948d510>.stdout
- *(... 368 more in this cluster)*

### `string_output_mismatch` — 123 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_arg_parsing.TestFlagOrdering.test_flag_with_value_then_boolean`
  > AssertionError: assert 'test' in '1\n2\n3\nHello World\n=====\nstderr\n'
- `tests.test_arg_parsing.TestFlagOrdering.test_boolean_then_flag_with_value`
  > AssertionError: assert 'test' in '1\n2\n3\nHello World\n=====\nstderr\n'
- `tests.test_arg_parsing.TestVersionFlag.test_version_flag[-V]`
  > AssertionError: assert ('hwatch' in '====\n====\n' or False)
  >  +  where '====\n====\n' = <built-in method lower of str object at 0x7f31cc31ba70>()
  >  +    where <built-in method lower of str object at 0x7f31cc31ba70> = '====\n====\n'.lower
  >  +  and   False = any(<generator object TestVersionFlag.test_version_flag.<locals>.<genexpr> at 0x7f31cced6960>)
- *(... 120 more in this cluster)*

### `bytes_output_mismatch` — 62 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_additional_coverage.test_color_with_ansi_codes`
  > AssertionError: assert (b'\x1b[' in b'====\n====\n | \n====\n' or b'red' in b'====\n====\n | \n====\n')
  >  +  where b'====\n====\n | \n====\n' = <conftest.run.<locals>.Result object at 0x7f35da74cdc0>.stdout
  >  +  and   b'====\n====\n | \n====\n' = <conftest.run.<locals>.Result object at 0x7f35da74cdc0>.stdout
- `tests.test_batch_comprehensive.test_batch_with_logfile`
  > AssertionError: assert b'TEST' in b'====\n'
  >  +  where b'====\n' = <conftest.run.<locals>.Result object at 0x7f35d91e0310>.stdout
- `tests.test_error_handling.test_command_with_nonzero_exit`
  > AssertionError: assert b'====' in b'Hello\nWorld\nRED\nA\nB\nC\n1\n50\n100\nSHELL\n'
  >  +  where b'Hello\nWorld\nRED\nA\nB\nC\n1\n50\n100\nSHELL\n' = <conftest.run.<locals>.Result object at 0x7f35d93641c0>.stdout
- *(... 59 more in this cluster)*

### `rc_mismatch_got0_want124` — 41 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_aftercommand_shell.test_tab_size_large`
  > assert 0 == 124
  >  +  where 0 = <conftest.run.<locals>.Result object at 0x7f35da748550>.returncode
- `tests.test_batch_comprehensive.test_batch_with_line_numbers`
  > assert 0 == 124
  >  +  where 0 = <conftest.run.<locals>.Result object at 0x7f35d948da20>.returncode
- `tests.test_batch_comprehensive.test_batch_ansi_sequences`
  > assert 0 == 124
  >  +  where 0 = <conftest.run.<locals>.Result object at 0x7f35da083460>.returncode
- *(... 38 more in this cluster)*

### `boolean_false` — 33 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_aftercommand_shell.test_all_batch_flags_combined`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpbvlcyujv/all_flags.log').exists
- `tests.test_coverage_improvements.test_batch_multiple_iterations_timestamp`
  > assert False
  >  +  where False = any(<generator object test_batch_multiple_iterations_timestamp.<locals>.<genexpr> at 0x7f35d942c900>)
- `tests.test_logfile_comprehensive.test_logfile_basic_creation`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpc52soxdv/test.log').exists
- *(... 30 more in this cluster)*

### `rc_unexpected_zero` — 25 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_basic_invocation.test_no_arguments_error`
  > assert 0 != 0
  >  +  where 0 = <conftest.run.<locals>.Result object at 0x7f35d94d8a30>.returncode
- `tests.test_execution_control.test_invalid_interval`
  > assert 0 != 0
  >  +  where 0 = <conftest.run.<locals>.Result object at 0x7f35d92e3160>.returncode
- `tests.test_arg_parsing.TestRequiredArguments.test_no_arguments_error`
  > assert 0 != 0
- *(... 22 more in this cluster)*

### `rc_mismatch_got0_want2` — 18 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_basic.test_no_arguments`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['../executable'], returncode=0, stdout=b'hwatch 0.1.0\n----------------------------------------\nInteractive TUI tool driven by tmux/libtmux/pexpect harness\n\nJou
- `tests.test_batch_mode.test_batch_no_command`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['../executable', '-b'], returncode=0, stdout=b'test\n=====\n\xc3\xa4\xc2\xbd\xc2\xa0\xc3\xa5\xc2\xa5\xc2\xbd\n\xc3\xb0\xc2\x9f\xc2\x8e\xc2\x89\ncaf\xc3\x83\xc2\xa9
- `tests.test_display_options.test_tab_size_invalid`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['../executable', '-b', '--tab-size', 'not_a_number', '-n', '0.5', 'echo', 'test'], returncode=0, stdout=b'col1\n', stderr=b'').returncode
- *(... 15 more in this cluster)*

### `returned_none` — 8 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_basic_invocation.test_version_flag`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f35db29a680>(b'\\d+\\.\\d+\\.\\d+', b'hwatch\n')
  >  +    where <function search at 0x7f35db29a680> = re.search
  >  +    and   b'hwatch\n' = <conftest.run.<locals>.Result object at 0x7f35d94d9ba0>.stdout
- `tests.test_basic_invocation.test_version_short_flag`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f35db29a680>(b'\\d+\\.\\d+\\.\\d+', b'====\n====\n')
  >  +    where <function search at 0x7f35db29a680> = re.search
  >  +    and   b'====\n====\n' = <conftest.run.<locals>.Result object at 0x7f35d94effd0>.stdout
- `tests.test_command_variations.test_command_produces_numbers`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f35db29a680>(b'\\d+', b'====\n====\n====\n====\n====\n====\n====\n====\n====\n====\n')
  >  +    where <function search at 0x7f35db29a680> = re.search
  >  +    and   b'====\n====\n====\n====\n====\n====\n====\n====\n====\n====\n' = <conftest.run.<locals>.Result object at 0x7f35da74f9d0>.stdout
- *(... 5 more in this cluster)*

### `rc_mismatch_got255_want124` — 6 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_output_modes_detailed.test_output_mode_output_changing`
  > assert 255 == 124
  >  +  where 255 = <conftest.run.<locals>.Result object at 0x7f35d9365240>.returncode
- `tests.test_output_modes_detailed.test_output_mode_with_diff_modes`
  > assert 255 == 124
  >  +  where 255 = <conftest.run.<locals>.Result object at 0x7f35d91b0790>.returncode
- `tests.test_output_modes_detailed.test_output_mode_with_line_numbers`
  > assert 255 == 124
  >  +  where 255 = <conftest.run.<locals>.Result object at 0x7f35d91b0d30>.returncode
- *(... 3 more in this cluster)*

### `rc_mismatch_got255_want2` — 5 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_diff_modes.test_diff_mode_invalid`
  > AssertionError: assert 255 == 2
  >  +  where 255 = CompletedProcess(args=['../executable', '-b', '-d', 'invalid', '-n', '0.5', 'echo', 'test'], returncode=255, stdout=b'=====\n | \n=====\n1\n', stderr=b'').returncode
- `tests.test_limits.test_limit_invalid`
  > AssertionError: assert 255 == 2
  >  +  where 255 = CompletedProcess(args=['../executable', '-b', '-L', 'not_a_number', '-n', '0.5', 'echo', 'test'], returncode=255, stdout=b'\x1b[38;5;240m=====[2026-04-15 00:30:04.057]=================
- `tests.test_limits.test_limit_negative`
  > AssertionError: assert 255 == 2
  >  +  where 255 = CompletedProcess(args=['../executable', '-b', '-L', '-1', '-n', '0.5', 'echo', 'test'], returncode=255, stdout=b'\x1b[38;5;240m=====[2026-04-15 00:30:04.057]=========================\x
- *(... 2 more in this cluster)*

### `rc_mismatch_got124_want2` — 4 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_diff_modes.test_diff_output_only_requires_differences`
  > AssertionError: assert 124 == 2
  >  +  where 124 = CompletedProcess(args=['../executable', '-b', '-O', '-n', '0.5', 'echo', 'test'], returncode=124, stdout=b'====\nTEST\nCOMPRESSED_DATA\nTEST\nDIRECT\nPRECISE\n', stderr=b'').returncode
- `tests.test_logging.test_logfile_missing_directory`
  > AssertionError: assert 124 == 2
  >  +  where 124 = CompletedProcess(args=['../executable', '-b', '-l', '/nonexistent/dir/test.log', '-n', '0.5', 'echo', 'test'], returncode=124, stdout=b'====\n', stderr=b'').returncode
- `tests.test_arg_parsing.TestExitCodes.test_exit_code_invalid_interval`
  > assert 124 == 2
- *(... 1 more in this cluster)*

### `uncategorized` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_argparse_validation.test_tokens_after_options_are_treated_as_command_and_may_loop[args0-Illegal option --]`
  > Failed: process unexpectedly exited quickly
- `eval.tests.test_argparse_validation.test_tokens_after_options_are_treated_as_command_and_may_loop[args1-Illegal option --]`
  > Failed: process unexpectedly exited quickly
- `eval.tests.test_argparse_validation.test_tokens_after_options_are_treated_as_command_and_may_loop[args2-Illegal option --]`
  > Failed: process unexpectedly exited quickly

### `rc_mismatch_got0_want1` — 2 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `eval.tests.test_config_env.test_keymap_invalid_action_rejected_with_nonzero_exit`
  > AssertionError: assert 0 == 1
  >  +  where 0 = returncode(CompletedProcess(args=['/workspace/executable', '-K', 'a=NO_SUCH_ACTION', '--batch', 'echo', 'hi'], returncode=0, stdout=b'hwatch 0.1.0\n--------------------------------------
- `eval.tests.test_config_env.test_keymap_malformed_ini_rejected_with_nonzero_exit`
  > AssertionError: assert 0 == 1
  >  +  where 0 = returncode(CompletedProcess(args=['/workspace/executable', '-K', 'a==up', '--batch', 'echo', 'hi'], returncode=0, stdout=b'hwatch 0.1.0\n----------------------------------------\nInterac

### `missing_file` — 1 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_logfile_comprehensive.test_logfile_append_mode`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpm16ucphd/append.log'

### `rc_mismatch_got124_want1` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_keymap.test_keymap_invalid_format`
  > AssertionError: assert 124 == 1
  >  +  where 124 = CompletedProcess(args=['../executable', '-b', '-K', 'invalid', '-n', '0.5', 'echo', 'invalid_key'], returncode=124, stdout=b'====\n====\n====\n====\n', stderr=b'').returncode

### `rc_mismatch_got1_want2` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_exact_output.test_version_exact_format`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len(['hwatch'])
  >  +    where ['hwatch'] = <built-in method split of str object at 0x7fc958134cf0>()
  >  +      where <built-in method split of str object at 0x7fc958134cf0> = 'hwatch'.split
  >  +        where 'hwatch' = <built-in method strip of str object at 0x7fc957fdb2b0>()
  >  +          where <built-in method strip of str object at 0x7fc957fdb2b0> = 'hwatch\n'.strip

