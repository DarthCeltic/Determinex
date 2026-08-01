# Action Sheet — nuta__nsh.bdd0702

**Current:** 13.33%  (373/2799)
**Pass / Fail / Skip:** 373 / 995 / 12
**Gap to 100%:** 86.67 percentage points (2426 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_completion_mode.test_completion_mode_shows_multiple_columns`
  - reason: test_completion_mode_shows_multiple_columns depends on test_completion_mode_activates
- `tests.test_completion_mode.test_completion_mode_navigation_down`
  - reason: test_completion_mode_navigation_down depends on test_completion_mode_activates
- `tests.test_completion_mode.test_completion_mode_escape_exits`
  - reason: test_completion_mode_escape_exits depends on test_completion_mode_activates
- `tests.test_completion_mode.test_completion_mode_ctrl_c_exits`
  - reason: test_completion_mode_ctrl_c_exits depends on test_completion_mode_activates
- `tests.test_completion_mode.test_completion_mode_with_no_matches`
  - reason: test_completion_mode_with_no_matches depends on test_completion_mode_activates
- *(... 7 more skipped)*

## Failure clusters

995 failed tests grouped into 22 buckets (sorted by count).

### `other_assertion` — 436 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_advanced_features.test_comment_in_script`
  > AssertionError: assert b'visible' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', '-c', '# this is a comment\necho visible'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_advanced_features.test_multiline_command`
  > AssertionError: assert b'hello' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', '-c', 'echo hello \\\nworld'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_advanced_features.test_job_control_wait`
  > AssertionError: assert b'finished' in b'nsh 0.1.0\n----------------------------------------\nInteractive TUI tool driven by tmux/libtmux/pexpect harness\n\nJournals\nTasks\nFilter\nHelp\nQuit\nPress q
  >  +  where b'nsh 0.1.0\n----------------------------------------\nInteractive TUI tool driven by tmux/libtmux/pexpect harness\n\nJournals\nTasks\nFilter\nHelp\nQuit\nPress q to quit\nj/k: navigate\nEnt
- *(... 433 more in this cluster)*

### `string_output_mismatch` — 330 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_advanced_features.test_command_with_multiple_redirects`
  > AssertionError: assert '' == 'test data'
  >   
  >   - test data
- `tests.test_array_operations.test_array_access_out_of_bounds`
  > AssertionError: assert 'first\nhello...ne\nzero\none' == ''
  >   
  >   + first
  >   + hello
  >   + world
  >   + b
  >   + 1
  >   + 2...
- `tests.test_error_handling.test_conflicting_redirections`
  > AssertionError: assert '' == 'test'
  >   
  >   - test
- *(... 327 more in this cluster)*

### `rc_unexpected_zero` — 71 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_basic.test_missing_script_file`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/nonexistent/file.sh'], returncode=0, stdout=b'first\nsecond\nthird\n', stderr=b'').returncode
- `tests.test_builtins.test_cd_nonexistent`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-c', 'cd /nonexistent_dir_12345'], returncode=0, stdout=b'dir1\nparent\ndir1\ndir1\n', stderr=b'').returncode
- `tests.test_builtins.test_set_errexit`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-c', 'set -e; echo before; false; echo after'], returncode=0, stdout=b'before\ndefined\nbefore exec\nafter exec\ntest\ntest\ndone\ntest\n
- *(... 68 more in this cluster)*

### `rc_mismatch_got0_want1` — 71 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_coverage_boost.test_exit_with_status`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-c', 'exit 1'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_command_c.test_c_nonexistent_command_exit_1_and_message_on_stderr`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-c', 'nonexistent_cmd'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_basic_commands.test_false_command`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--norc', '-c', 'false'], returncode=0, stdout='', stderr='').returncode
- *(... 68 more in this cluster)*

### `bytes_output_mismatch` — 27 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_basic.test_command_with_exit_code`
  > AssertionError: assert b'script outp...line3\ntest\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'script output\nline1\nline2\nline3\ntest\n')
- `tests.test_coverage_50_boost.test_cd_to_root`
  > AssertionError: assert b'dir1\nparent\ndir1\ndir1' == b'/'
  >   
  >   At index 0 diff: b'd' != b'/'
  >   
  >   Full diff:
  >   - b'/'
  >   + (b'dir1\nparent\ndir1\ndir1')
- `tests.test_error_handling.test_empty_script`
  > AssertionError: assert b'nsh 0.1.0\n...x8d\n--help\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'nsh 0.1.0\n----------------------------------------\nInteractive TUI tool '
  >   +  b'driven by tmux/libtmux/pexpect harness\n\nJournals\nTasks\nFilter\nHelp\nQ'
  >   +  b'uit\nPress q to quit\nj/k: navigate\nEnter\nn: new\nWelcome\nLoading\nReady'
  >   +  b'\n--help\n--version\n-c\n/test/path\n1\n10\n2\n20\n<job_id>\nARGS:\nAll job'...
- *(... 24 more in this cluster)*

### `rc_mismatch_got0_want42` — 8 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_command_line_flags.test_script_with_exit_code`
  > AssertionError: assert 0 == 42
  >  +  where 0 = CompletedProcess(args=['./executable', '/tmp/tmpc_0y8z5b/test.sh'], returncode=0, stdout=b'nsh 0.1.0\n----------------------------------------\nInteractive TUI tool driven by tmux/libtmu
- `tests.test_exec_comprehensive.test_exec_preserves_exit_code`
  > assert 0 == 42
  >  +  where 0 = CompletedProcess(args=['./executable', '-c', "exec sh -c 'exit 42'"], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_exec_expanded.test_exec_preserves_exit_code`
  > assert 0 == 42
  >  +  where 0 = CompletedProcess(args=['./executable', '-c', "exec sh -c 'exit 42'"], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 5 more in this cluster)*

### `returned_none` — 7 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_basic.test_version`
  > AssertionError: assert None
  >  +  where None = <function match at 0x7f6b1bc26170>(b'\\d+\\.\\d+\\.\\d+', b'hello\n')
  >  +    where <function match at 0x7f6b1bc26170> = re.match
  >  +    and   b'hello\n' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'hello\n', stderr=b'').stdout
- `eval.tests.test_help_output.test_help_has_usage_section`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f9a926c2680>('^USAGE:\\s*$', 'hello\n', flags=re.MULTILINE)
  >  +    where <function search at 0x7f9a926c2680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- `eval.tests.test_help_output.test_help_usage_mentions_executable`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f9a926c2680>('^\\s*executable\\b', 'hello\n', flags=re.MULTILINE)
  >  +    where <function search at 0x7f9a926c2680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- *(... 4 more in this cluster)*

### `missing_file` — 7 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_coverage_gaps.TestRedirectionEdgeCases.test_redirect_append_mode`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_redirect_append_mode2/append.txt'
- `tests.test_complex_scenarios.test_multiple_redirections`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpcmo357id/out2.txt'
- `tests.test_file_operations.test_redirect_to_file`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmprpawmz50/output.txt'
- *(... 4 more in this cluster)*

### `rc_mismatch_got0_want255` — 7 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_builtins_advanced.test_eval_syntax_error`
  > assert 0 == 255
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-c', "eval 'syntax error ((('"], returncode=0, stdout='', stderr='').returncode
- `tests.test_builtins_basic.test_exit_large_code`
  > AssertionError: assert 0 == 255
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-c', 'exit 255'], returncode=0, stdout='', stderr='').returncode
- `tests.test_cli.test_c_flag_parse_error`
  > AssertionError: assert 0 == 255
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-c', 'if [ true'], returncode=0, stdout='', stderr='').returncode
- *(... 4 more in this cluster)*

### `boolean_false` — 6 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_comprehensive.test_redirect_input_and_output`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmp2iqjukvl/out.txt').exists
- `tests.test_coverage_gaps.TestRedirectionEdgeCases.test_redirect_stdout_to_file`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/pytest-of-root/pytest-0/test_redirect_stdout_to_file2/output.txt').exists
- `tests.test_edge_cases.test_multiple_redirections`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpchi3f1vm/f1.txt').exists
- *(... 3 more in this cluster)*

### `rc_mismatch_got0_want7` — 5 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_script_file_with_exit_code`
  > AssertionError: assert 0 == 7
  >  +  where 0 = CompletedProcess(args=['./executable', '--norc', '/tmp/tmpodjfn0no/test.sh'], returncode=0, stdout=b'file-run\n', stderr=b'').returncode
- `eval.tests.test_blackbox_suite.test_blackbox_scripts_match_fixtures[test/options/errexit.sh]`
  > AssertionError: assert 0 == 7
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--norc', '/workspace/test/options/errexit.sh'], returncode=0, stdout=b'file-run\n', stderr=b'').returncode
  >  +  and   7 = Expected(stdout='reachable\n', stderr='', returncode=7, disable_output_check=False).returncode
- `eval.tests.test_blackbox_externalized.test_ext_blackbox_script[options/errexit.sh]`
  > AssertionError: assert 0 == 7
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--norc', '/workspace/test/options/errexit.sh'], returncode=0, stdout=b'file-run\n', stderr=b'').returncode
- *(... 2 more in this cluster)*

### `rc_mismatch_got1_want3` — 4 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_builtins_basic.test_cd_dash_previous_directory`
  > AssertionError: assert 1 == 3
  >  +  where 1 = len([''])
- `tests.test_builtins_basic.test_cd_multiple_levels_relative`
  > AssertionError: assert 1 == 3
  >  +  where 1 = len([''])
- `tests.test_builtins_basic.test_cd_parent_directory_dotdot`
  > AssertionError: assert 1 == 3
  >  +  where 1 = len([''])
- *(... 1 more in this cluster)*

### `rc_mismatch_got0_want5` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_command_line_options.test_script_file_exit_code`
  > AssertionError: assert 0 == 5
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--norc', '/tmp/pytest-of-root/pytest-0/test_script_file_exit_code2/test_script.sh'], returncode=0, stdout='file-run\n', stderr='').return
- `tests.test_builtins_advanced.test_source_exit_status`
  > AssertionError: assert 0 == 5
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-c', 'source /workspace/eval/test_resources/test_builtins_advanced/exit_script.sh; echo after'], returncode=0, stdout='', stderr='').retu
- `tests.test_cli.test_script_file_simple_execution`
  > AssertionError: assert 0 == 5
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/workspace/eval/test_resources/test_cli/simple_script.sh'], returncode=0, stdout='nsh 0.1.0\n----------------------------------------\nIn

### `rc_mismatch_got10_want3` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_arithmetic_operators.test_arithmetic_decrement_in_for_loop`
  > AssertionError: assert 10 == 3
  >  +  where 10 = len(['3', '2', '1', '0', '1', '2', ...])
- `tests.test_arithmetic_operators.test_arithmetic_comparison_in_c_style_for`
  > AssertionError: assert 10 == 3
  >  +  where 10 = len(['0', '1', '2', '2', '1', '0', ...])

### `rc_mismatch_got0_want101` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_file_execution.test_missing_script_file_panics_with_rc_101_and_backtrace_message`
  > AssertionError: assert 0 == 101
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/tmp/pytest-of-root/pytest-0/test_missing_script_file_panic2/doesnotexist.nsh'], returncode=0, stdout=b'nsh 0.1.0\n----------------------
- `tests.test_cli.test_script_file_nonexistent`
  > AssertionError: assert 0 == 101
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/nonexistent/script.sh'], returncode=0, stdout='nsh 0.1.0\n----------------------------------------\nInteractive TUI tool driven by tmux/

### `rc_mismatch_got0_want127` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_builtin_errors.test_exec_command_not_found_exit_127`
  > AssertionError: assert 0 == 127
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-c', 'exec /nonexistent_command_xyz'], returncode=0, stdout='', stderr='').returncode
- `tests.test_builtins_jobs.test_exec_nonexistent_command_exit_127`
  > AssertionError: assert 0 == 127
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-c', 'exec /nonexistent/command'], returncode=0, stdout='', stderr='').returncode

### `rc_mismatch_got0_want126` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_builtin_errors.test_exec_permission_denied_exit_126`
  > AssertionError: assert 0 == 126
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-c', 'exec /tmp/tmpx9znf396/noexec_file'], returncode=0, stdout='', stderr='').returncode
- `tests.test_builtins_jobs.test_exec_permission_denied_exit_126`
  > AssertionError: assert 0 == 126
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-c', 'exec /tmp/tmp5iktz998/noexec'], returncode=0, stdout='', stderr='').returncode

### `empty_list_or_string` — 1 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_complex_scenarios.test_subshell_with_cd`
  > IndexError: list index out of range

### `rc_mismatch_got1_want4` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_edge_cases_extended.test_nested_loops`
  > AssertionError: assert 1 == 4
  >  +  where 1 = len([b''])

### `rc_mismatch_got11_want2` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_command_line_options.test_version_flag`
  > assert 11 == 2
  >  +  where 11 = <built-in method count of str object at 0x7f1d4a5fb2d0>('.')
  >  +    where <built-in method count of str object at 0x7f1d4a5fb2d0> = "error: unexpected argument '--norc' found\nError: unexpected argument '--norc' found\nunknown flag: unexpected argument '--norc' 
  >  +      where "error: unexpected argument '--norc' found\nError: unexpected argument '--norc' found\nunknown flag: unexpected argument '--norc' found\nUnknown flag: unexpected argument '--norc' found\
  >  +        where <built-in method strip of str object at 0x7f1d4a5faf70> = "error: unexpected argument '--norc' found\nError: unexpected argument '--norc' found\nunknown flag: unexpected argument '--no
  >  +          where "error: unexpected argument '--norc' found\nError: unexpected argument '--norc' found\nunknown flag: unexpected argument '--norc' found\nUnknown flag: unexpected argument '--norc' fo

### `rc_mismatch_got1_want2` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_builtins_basic.test_cd_dash_back_and_forth`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len([''])

### `rc_mismatch_got0_want10` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli.test_script_exit_stops_execution`
  > AssertionError: assert 0 == 10
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/workspace/eval/test_resources/test_cli/multicommand_exit.sh'], returncode=0, stdout='nsh 0.1.0\n----------------------------------------

