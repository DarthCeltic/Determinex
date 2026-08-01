# Action Sheet — bensadeh__tailspin.6278437

**Current:** 19.59%  (201/1026)
**Pass / Fail / Skip:** 201 / 537 / 0
**Gap to 100%:** 80.41 percentage points (825 tests)

## Failure clusters

537 failed tests grouped into 10 buckets (sorted by count).

### `other_assertion` — 361 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_help_flag`
  > AssertionError: assert b'--follow' in b'A log file highlighter\nUsage: executable [OPTIONS] [FILE]\ntspin\nnull\n123\nnull\nERROR\n2023\n'
  >  +  where b'A log file highlighter\nUsage: executable [OPTIONS] [FILE]\ntspin\nnull\n123\nnull\nERROR\n2023\n' = CompletedProcess(args=['./executable', '--help'], returncode=0, stdout=b'A log file hig
- `tests.test_basic_invocation.test_stdin_with_no_args`
  > AssertionError: assert b'\x1b[' in b'tailspin 0.1.0\n----------------------------------------\nInteractive TUI tool driven by tmux/libtmux/pexpect harness\n\nJournals\nTasks\nFilter\nHelp\nQuit\nPress
  >  +  where b'tailspin 0.1.0\n----------------------------------------\nInteractive TUI tool driven by tmux/libtmux/pexpect harness\n\nJournals\nTasks\nFilter\nHelp\nQuit\nPress q to quit\nj/k: navigate
- `tests.test_configuration.test_config_path_valid`
  > AssertionError: assert b'CUSTOM' in b'Started\napplication\nBOLD\nITALIC\nTEST\nmessage\ntest\n'
  >  +  where b'Started\napplication\nBOLD\nITALIC\nTEST\nmessage\ntest\n' = CompletedProcess(args=['./executable', '--config-path', '/tmp/tmp77m182cv/config.toml'], returncode=0, stdout=b'Started\napplic
- *(... 358 more in this cluster)*

### `string_output_mismatch` — 83 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_baseline.test_help_long_matches_baseline_file_normalized`
  > AssertionError: assert 'A log file h...ERROR\n2023\n' == 'A log file h...int version\n'
  >   
  >     A log file highlighter
  >   - 
  >     Usage: executable [OPTIONS] [FILE]
  >   + tspin
  >   + null
  >   + 123...
- `eval.tests.test_help_output.test_help_long_and_short_have_same_usage_synopsis`
  > AssertionError: assert 'Usage: execu...TIONS] [FILE]' == 'Usage:'
  >   
  >   - Usage:
  >   + Usage: executable [OPTIONS] [FILE]
- `eval.tests.test_help_output.test_dash_dash_help_separator_ignored`
  > AssertionError: assert 'tailspin 0.1...int version\n' == 'A log file h...ERROR\n2023\n'
  >   
  >   - A log file highlighter
  >   - Usage: executable [OPTIONS] [FILE]
  >   - tspin
  >   - null
  >   - 123
  >   - null...
- *(... 80 more in this cluster)*

### `bytes_output_mismatch` — 35 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_basic_invocation.test_empty_stdin`
  > AssertionError: assert b'tailspin 0....og\n$dollar\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'tailspin 0.1.0\n----------------------------------------\nInteractive TUI '
  >   +  b'tool driven by tmux/libtmux/pexpect harness\n\nJournals\nTasks\nFilter\nH'
  >   +  b'elp\nQuit\nPress q to quit\nj/k: navigate\nEnter\nn: new\nWelcome\nLoading\n'
  >   +  b'Ready\n$dollar\n--config-path\n--exec\n--follow\n--help\n--listen-command\n'...
- `tests.test_basic.test_empty_stdin`
  > AssertionError: assert b'null\n123\n...ERROR\n2023\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'null\n123\nnull\nERROR\n2023\n')
- `eval.tests.test_io_behavior.test_disable_builtin_keywords_removes_highlighting_from_stdin`
  > AssertionError: assert b'null\ntrue\...\n123\n2024\n' == b'a null b\n'
  >   
  >   At index 0 diff: b'n' != b'a'
  >   
  >   Full diff:
  >   - (b'a null b\n')
  >   + (b'null\ntrue\nfalse\nGET\n123\n123\nnull\nhello\n123\n2024\n')
- *(... 32 more in this cluster)*

### `rc_unexpected_zero` — 27 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_basic_invocation.test_invalid_flag`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '--invalid-flag-xyz'], returncode=0, stdout=b'Usage:\n', stderr=b'').returncode
- `tests.test_configuration.test_config_path_invalid_toml`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '--config-path', '/tmp/tmpv218uhwb/bad_config.toml'], returncode=0, stdout=b'Started\napplication\nBOLD\nITALIC\nTEST\nmessage\ntest\n', stderr=b''
- `tests.test_enable_disable.test_enable_invalid_group`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '--enable=invalid_group'], returncode=0, stdout=b'123\nnull\nhello\n123\n2024\n03\nvar\nlog\nsyslog\n192\n', stderr=b'').returncode
- *(... 24 more in this cluster)*

### `rc_mismatch_got0_want1` — 11 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `eval.tests.test_io_behavior.test_missing_file_is_error_on_stderr_and_exit1`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--print', '/tmp/this_file_should_not_exist_tailspin'], returncode=0, stdout=b'null\n123\nnull\nERROR\n2023\n', stderr=b'').returncode
- `tests.test_advanced_modes.test_file_not_exist_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/tmp/pytest-of-root/pytest-0/test_file_not_exist_error2/nonexistent_file_xyz12345.log', '--follow', '--print'], returncode=0, stdout=b'',
- `tests.test_advanced_modes.test_follow_and_exec_conflict_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/tmp/pytest-of-root/pytest-0/test_follow_and_exec_conflict_2/test.log', '--follow', '--exec', 'echo hello', '--print'], returncode=0, std
- *(... 8 more in this cluster)*

### `rc_mismatch_got0_want2` — 10 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_argument_parsing.TestExecFlag.test_exec_without_value`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['./executable', '--exec'], returncode=0, stdout='', stderr='').returncode
- `tests.test_argument_parsing.TestConfigPathFlag.test_config_path_without_value`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['./executable', '--config-path'], returncode=0, stdout='CUSTOM\nStarted\napplication\nBOLD\nITALIC\nTEST\nmessage\n', stderr='').returncode
- `tests.test_argument_parsing.TestMisspelledFlags.test_misspelled_flags[--prints]`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['./executable', '--prints'], returncode=0, stdout='tailspin 0.1.0\n----------------------------------------\nInteractive TUI tool driven by tmux/libtmux/pexpect ha
- *(... 7 more in this cluster)*

### `returned_none` — 5 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_basic_invocation.test_version_flag`
  > AssertionError: assert None
  >  +  where None = <function match at 0x7f9842abd120>(b'tspin \\d+\\.\\d+\\.\\d+', b'tspin\nnull\n123\nnull\nERROR\n2023\n')
  >  +    where <function match at 0x7f9842abd120> = re.match
  >  +    and   b'tspin\nnull\n123\nnull\nERROR\n2023\n' = CompletedProcess(args=['./executable', '--version'], returncode=0, stdout=b'tspin\nnull\n123\nnull\nERROR\n2023\n', stderr=b'').stdout
- `tests.test_basic_invocation.test_version_short_flag`
  > AssertionError: assert None
  >  +  where None = <function match at 0x7f9842abd120>(b'tspin \\d+\\.\\d+\\.\\d+', b'tspin\nHello\nUsage:\n')
  >  +    where <function match at 0x7f9842abd120> = re.match
  >  +    and   b'tspin\nHello\nUsage:\n' = CompletedProcess(args=['./executable', '-V'], returncode=0, stdout=b'tspin\nHello\nUsage:\n', stderr=b'').stdout
- `tests.test_basic.test_version_short_flag`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f9b6c5e2680>(b'\\d+\\.\\d+\\.\\d+', b'tspin\nHello\nUsage:\n')
  >  +    where <function search at 0x7f9b6c5e2680> = re.search
  >  +    and   b'tspin\nHello\nUsage:\n' = CompletedProcess(args=['./executable', '-V'], returncode=0, stdout=b'tspin\nHello\nUsage:\n', stderr=b'').stdout
- *(... 2 more in this cluster)*

### `boolean_false` — 3 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `eval.tests.test_io_behavior.test_version_stdout_exit0`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of bytes object at 0x7f0e561e6170>(b'tspin ')
  >  +    where <built-in method startswith of bytes object at 0x7f0e561e6170> = b'tspin\nnull\n123\nnull\nERROR\n2023\n'.startswith
  >  +      where b'tspin\nnull\n123\nnull\nERROR\n2023\n' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'tspin\nnull\n123\nnull\nERROR\n2023\n', stderr=b'').stdout
- `tests.test_pager.test_custom_pager`
  > AssertionError: assert False
  >  +  where False = wait_for('PAGER_TEST_CONTENT')
  >  +    where wait_for = <test_pager.TmuxTestHarness object at 0x7f5fbe9ecd60>.wait_for
- `tests.test_cli_basic.test_stdin_with_trailing_newlines`
  > AssertionError: assert False
  >  +  where False = <built-in method endswith of str object at 0x7fd7bcbcff00>('\n\n\n')
  >  +    where <built-in method endswith of str object at 0x7fd7bcbcff00> = 'null\n123\nnull\nERROR\n2023\n'.endswith

### `rc_mismatch_got5_want4` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_file_input.test_file_with_newlines_only`
  > AssertionError: assert 5 == 4
  >  +  where 5 = <built-in method count of bytes object at 0x7f9b6b378930>(b'\n')
  >  +    where <built-in method count of bytes object at 0x7f9b6b378930> = b'null\n123\nnull\nERROR\n2023\n'.count
  >  +      where b'null\n123\nnull\nERROR\n2023\n' = CompletedProcess(args=['./executable', '/tmp/tmpa9zpsava/newlines.log', '--print'], returncode=0, stdout=b'null\n123\nnull\nERROR\n2023\n', stderr=b''

### `rc_mismatch_got2_want0` — 1 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `eval.tests.test_config_env.test_cli_pager_overrides_tailspin_pager_env_var`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--pager', 'cat -n [FILE]', '/tmp/tmphak0qsno/a.log'], returncode=2, stdout=b'', stderr=b'').returncode

