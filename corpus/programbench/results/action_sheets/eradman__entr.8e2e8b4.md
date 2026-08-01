# Action Sheet — eradman__entr.8e2e8b4

**Current:** 32.34%  (217/671)
**Pass / Fail / Skip:** 217 / 393 / 1
**Gap to 100%:** 67.66 percentage points (454 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_harvest.test_exec_when_symlink_changed`
  - reason: Symlink watching behavior varies

## Failure clusters

393 failed tests grouped into 29 buckets (sorted by count).

### `other_assertion` — 134 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_no_arguments`
  > AssertionError: assert b'[-acdnprsxz]' in b'usage: entr [-hV] [-c] [-d] [-p] [-r] [-s] utility [argument ...]\n'
  >  +  where b'usage: entr [-hV] [-c] [-d] [-p] [-r] [-s] utility [argument ...]\n' = CompletedProcess(args=['/workspace/executable'], returncode=1, stdout=b'', stderr=b'usage: entr [-hV] [-c] [-d] [-p] 
- `tests.test_basic_invocation.test_invalid_option`
  > AssertionError: assert b'invalid option' in b'entr: no input files\n'
  >  +  where b'entr: no input files\n' = CompletedProcess(args=['/workspace/executable', '--invalid'], returncode=1, stdout=b'', stderr=b'entr: no input files\n').stderr
- `tests.test_edge_cases.test_utility_exit_code_propagation`
  > AssertionError: Exit code 0 not propagated correctly
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-z', '-n', '-s', 'exit 0'], returncode=1, stdout=b'', stderr=b'entr: utility "exit 0" not found\n').returncode
- *(... 131 more in this cluster)*

### `rc_mismatch_got1_want0` — 65 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_edge_cases.test_stdout_stderr_separation`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-z', '-n', '-s', 'echo stdout; echo stderr >&2'], returncode=1, stdout=b'', stderr=b'entr: utility "echo stdout; echo stderr >&2" not fou
- `tests.test_environment_variables.test_shell_env_var`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-z', '-n', '-s', 'echo shell_test'], returncode=1, stdout=b'', stderr=b'entr: utility "echo shell_test" not found\n').returncode
- `tests.test_execution_modes.test_shell_mode_with_s_flag`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-z', '-n', '-s', 'echo hello | tr a-z A-Z'], returncode=1, stdout=b'', stderr=b'entr: utility "echo hello | tr a-z A-Z" not found\n').ret
- *(... 62 more in this cluster)*

### `rc_mismatch_got0_want1` — 50 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_basic_invocation.test_help_flag`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-h'], returncode=0, stdout=b'entr 0.1.0\n\nUsage: usage: entr [-hV] [-c] [-d] [-p] [-r] [-s] utility [argument ...]\n\nRun a utility when
- `tests.test_environment_variables.test_invalid_restart_signal`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-n', 'echo', 'test'], returncode=0, stdout=b'test\n', stderr=b'').returncode
- `tests.test_environment_variables.test_empty_restart_signal`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-n', 'echo', 'test'], returncode=0, stdout=b'test\n', stderr=b'').returncode
- *(... 47 more in this cluster)*

### `string_output_mismatch` — 42 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_argparse_validation.test_placeholder_slash_underscore_is_replaced_with_first_path`
  > AssertionError: assert '/_ HI\n' == '/tmp/pytest-...atch.txt HI\n'
  >   
  >   - /tmp/pytest-of-root/pytest-0/test_placeholder_slash_undersc2/watch.txt HI
  >   + /_ HI
- `eval.tests.test_system_externalized.test_ext_install_default_status_script`
  > assert (('' == 'entr: create...exit code 0\n'
  >   
  >   - entr: created '/tmp/pytest-of-root/pytest-0/test_ext_install_default_statu2/status.awk'
  >   - true returned exit code 0) or 'awk: not an option' in "entr: invalid option -- 'x'\nusage: entr [-hV] [-c] [-d] [-p] [-r] [-s] utility [argument ...]\n")
- `eval.tests.test_system_externalized.test_ext_custom_status_script_formats_exit_code`
  > assert ('entr: invali...gument ...]\n' == ''
  >   
  >   + entr: invalid option -- 'x'
  >   + usage: entr [-hV] [-c] [-d] [-p] [-r] [-s] utility [argument ...] or 'awk: not an option' in "entr: invalid option -- 'x'\nusage: entr [-hV] [-c] [-d] [-p] [-r] [-s] utility [argument ...]\n")
- *(... 39 more in this cluster)*

### `rc_mismatch_got2_want0` — 34 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_additional_coverage.test_utility_writes_to_file`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-n', '-z', 'sh', '-c', 'echo hello > /tmp/tmp1mb89j5v/output.txt'], returncode=2, stdout=b'', stderr=b'/usr/bin/sh: 0: cannot open echo h
- `tests.test_aggressive_mode.test_aggressive_mode_flag`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-n', '-z', '-a', 'echo', 'aggressive'], returncode=2, stdout=b'', stderr=b"entr: invalid option -- 'a'\nusage: entr [-hV] [-c] [-d] [-p] 
- `tests.test_aggressive_mode.test_aggressive_mode_with_clear`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-n', '-z', '-a', '-c', 'echo', 'clear-aggressive'], returncode=2, stdout=b'', stderr=b"entr: invalid option -- 'a'\nusage: entr [-hV] [-c
- *(... 31 more in this cluster)*

### `rc_mismatch_got2_want1` — 16 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_edge_cases.test_invalid_flag_combination`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-Q', 'echo', 'test'], returncode=2, stdout=b'', stderr=b"entr: invalid option -- 'Q'\nusage: entr [-hV] [-c] [-d] [-p] [-r] [-s] utility 
- `tests.test_status_formatting.test_status_script_incompatible_with_restart`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-r', '-x', '-n', 'echo', 'test'], returncode=2, stdout=b'', stderr=b"entr: invalid option -- 'x'\nusage: entr [-hV] [-c] [-d] [-p] [-r] [
- `tests.test_basic_invocation.test_invalid_flag`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-q'], returncode=2, stdout=b'', stderr=b"entr: invalid option -- 'q'\nusage: entr [-hV] [-c] [-d] [-p] [-r] [-s] utility [argument ...]\n
- *(... 13 more in this cluster)*

### `boolean_false` — 9 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_restart_mode.test_restart_basic`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmp7sqg2j2j/output.txt').exists
- `tests.test_file_modification.test_file_modification_with_oneshot`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpgz1vw8o6/output.txt').exists
- `tests.test_watch_loop.test_watch_loop_with_file_modification`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpr_vlbrg0/output.txt').exists
- *(... 6 more in this cluster)*

### `rc_mismatch_got2_want42` — 6 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_strengthened.test_utility_nonzero_exit_code_strong`
  > AssertionError: assert 2 == 42
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-n', '-z', 'sh', '-c', 'exit 42'], returncode=2, stdout=b'', stderr=b'/usr/bin/sh: 0: cannot open exit 42: No such file\n').returncode
- `tests.test_cli.test_z_flag_propagates_utility_exit_code`
  > AssertionError: assert 2 == 42
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-n', '-z', 'sh', '-c', 'exit 42'], returncode=2, stdout='', stderr='/usr/bin/sh: 0: cannot open exit 42: No such file\n').returncode
- `tests.test_env_status.test_status_filter_exit_custom_code`
  > assert 2 == 42
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-n', '-z', '-xx', '/tmp/pytest-of-root/pytest-0/test_status_filter_exit_custom2/exit_42.sh'], returncode=2, stdout='', stderr="entr: inva
- *(... 3 more in this cluster)*

### `rc_mismatch_got130_want0` — 4 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_environment_variables.test_entr_restart_signal_env_var`
  > AssertionError: assert 130 == 0
  >  +  where 130 = <Popen: returncode: 130 args: ['/workspace/executable', '-r', '-n', 'sleep',...>.returncode
- `tests.test_signal_handling.test_child_process_group_in_restart_mode`
  > AssertionError: assert 130 == 0
  >  +  where 130 = <Popen: returncode: 130 args: ['/workspace/executable', '-r', '-n', '/tmp/tm...>.returncode
- `eval.tests.test_system_externalized.test_ext_one_shot_exec_cat_first_changed_file`
  > AssertionError: assert 130 == 0
  >  +  where 130 = <Popen: returncode: 130 args: ['/workspace/executable', '-n', '-p', 'cat', '...>.returncode
- *(... 1 more in this cluster)*

### `rc_unexpected_zero` — 4 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_subcommand_dispatch.TestSingleModeOperation.test_help_flag_works_globally`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '-h'], returncode=0, stdout=b'entr 0.1.0\n\nUsage: usage: entr [-hV] [-c] [-d] [-p] [-r] [-s] utility [argument ...]\n\nRun a utility when files ch
- `eval.tests.test_env_and_config.test_env_entr_restart_signal_invalid_rejected`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-n', '/bin/echo', 'ok'], returncode=0, stdout='ok\n', stderr='').returncode
- `eval.tests.test_env_and_config.test_env_entr_restart_signal_usr1_current_behavior_is_error`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-n', '/bin/echo', 'ok'], returncode=0, stdout='ok\n', stderr='').returncode
- *(... 1 more in this cluster)*

### `rc_mismatch_got1_want42` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_signal_handling.test_child_normal_exit_code_with_z`
  > assert 1 == 42
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-z', '-n', '-s', 'exit 42'], returncode=1, stdout=b'', stderr=b'entr: utility "exit 42" not found\n').returncode
- `tests.test_shell_mode.test_shell_exit_code`
  > assert 1 == 42
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-n', '-z', '-s', 'exit 42'], returncode=1, stdout=b'', stderr=b'entr: utility "exit 42" not found\n').returncode
- `tests.test_strengthened.test_shell_mode_exit_code_strong`
  > assert 1 == 42
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-n', '-z', '-s', 'exit 42'], returncode=1, stdout=b'', stderr=b'entr: utility "exit 42" not found\n').returncode

### `rc_mismatch_got2_want7` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_exit_status.test_exit_status_with_z_flag`
  > AssertionError: assert 2 == 7
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-n', '-z', 'sh', '-c', 'exit 7'], returncode=2, stdout=b'', stderr=b'/usr/bin/sh: 0: cannot open exit 7: No such file\n').returncode
- `tests.test_strengthened.test_exit_status_with_z_flag_strong`
  > AssertionError: assert 2 == 7
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-n', '-z', 'sh', '-c', 'exit 7'], returncode=2, stdout=b'', stderr=b'/usr/bin/sh: 0: cannot open exit 7: No such file\n').returncode
- `tests.test_status_gaps.test_status_filter_command_name_extraction`
  > assert 2 == 7
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-xx', '-z', '-n', '/tmp/pytest-of-root/pytest-0/test_status_filter_command_nam2/scripts/subdir/my_test_script.sh'], returncode=2, stdout=

### `rc_mismatch_got1_want137` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_signal_handling.test_child_signal_exit_code_with_z`
  > assert 1 == 137
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-z', '-n', '-s', 'kill -9 $$'], returncode=1, stdout=b'', stderr=b'entr: utility "kill -9 $$" not found\n').returncode
- `tests.test_harvest.test_exec_command_oneshot_shell_return_signal`
  > AssertionError: assert 1 == 137
  >  +  where 1 = CompletedProcess(args=['./executable', '-n', '-z', '-s', 'kill -9 $$'], returncode=1, stdout=b'').returncode

### `uncategorized` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_help_usage.test_usage_synopsis_matches_expected_shape`
  > StopIteration
- `tests.test_signals.test_restart_mode_waits_for_first_change_with_postpone`
  > AttributeError: '_io.TextIOWrapper' object has no attribute 'read1'. Did you mean: 'read'?

### `rc_mismatch_got2_want143` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_env_status.test_status_filter_signal_termination`
  > assert 2 == 143
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-n', '-z', '-xx', '/tmp/pytest-of-root/pytest-0/test_status_filter_signal_term2/sigterm.sh'], returncode=2, stdout='', stderr="entr: inva
- `tests.test_status_gaps.test_status_filter_with_signal_termination`
  > assert 2 == 143
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-xx', '-z', '-n', '/workspace/eval/test_resources/test_status_gaps/sigterm.sh'], returncode=2, stdout='', stderr="entr: invalid option --

### `rc_mismatch_got2_want130` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_env_status.test_status_filter_different_signals`
  > assert 2 == 130
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-n', '-z', '-xx', '/tmp/pytest-of-root/pytest-0/test_status_filter_different_s2/sigint.sh'], returncode=2, stdout='', stderr="entr: inval
- `tests.test_status_gaps.test_status_filter_sigint`
  > assert 2 == 130
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-xx', '-z', '-n', '/workspace/eval/test_resources/test_status_gaps/sigint.sh'], returncode=2, stdout='', stderr="entr: invalid option -- 

### `rc_mismatch_got2_want137` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_harvest.test_exec_command_oneshot_return_signal_number`
  > AssertionError: assert 2 == 137
  >  +  where 2 = CompletedProcess(args=['./executable', '-n', '-z', 'sh', '-c', 'kill -9 $$'], returncode=2, stdout=b'', stderr=b'/usr/bin/sh: 0: cannot open kill -9 $$: No such file\n').returncode
- `tests.test_status_gaps.test_status_filter_with_sigkill`
  > assert 2 == 137
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-xx', '-z', '-n', '/workspace/eval/test_resources/test_status_gaps/sigkill.sh'], returncode=2, stdout='', stderr="entr: invalid option --

### `rc_mismatch_got2_want5` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_signals.test_oneshot_exits_immediately_after_child_completes`
  > AssertionError: assert 2 == 5
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-n', '-z', 'sh', '-c', 'echo TEST; sleep 0.1; exit 5'], returncode=2, stdout='', stderr='/usr/bin/sh: 0: cannot open echo TEST; sleep 0.1
- `tests.test_status_gaps.test_status_filter_preserves_stdout_from_command`
  > assert 2 == 5
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-xx', '-z', '-n', '/tmp/pytest-of-root/pytest-0/test_status_filter_preserves_s2/stdout.sh'], returncode=2, stdout='', stderr="entr: inval

### `test_timeout` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_restart_mode.test_restart_with_long_running_process`
  > subprocess.TimeoutExpired: Command '['/workspace/executable', '-r', '-n', '/tmp/tmpql2_70pa/counter.sh']' timed out after 3 seconds

### `rc_mismatch_got1_want5` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_additional_coverage.test_shell_with_exit_in_middle`
  > assert 1 == 5
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-n', '-z', '-s', 'echo first && exit 5 && echo second'], returncode=1, stdout=b'', stderr=b'entr: utility "echo first && exit 5 && echo s

### `empty_list_or_string` — 1 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `eval.tests.test_help_usage.test_dash_h_stderr_has_release_and_usage_first_two_lines`
  > IndexError: list index out of range

### `returned_none` — 1 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_usage.test_docs_section_contains_man_entr`
  > AssertionError: assert None is not None
  >  +  where None = <function search at 0x7f7d73eda680>('^docs:\\s*$', 'entr 0.1.0\n\nUsage: usage: entr [-hV] [-c] [-d] [-p] [-r] [-s] utility [argument ...]\n\nRun a utility when files change.\n\nOptio
  >  +    where <function search at 0x7f7d73eda680> = re.search
  >  +    and   'entr 0.1.0\n\nUsage: usage: entr [-hV] [-c] [-d] [-p] [-r] [-s] utility [argument ...]\n\nRun a utility when files change.\n\nOptions:\n  -h, --help     Print this help\n  -V, --version  
  >  +    and   re.MULTILINE = re.M

### `rc_mismatch_got2_want139` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli.test_utility_killed_by_signal_exit_code`
  > AssertionError: assert 2 == 139
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-n', '-z', 'sh', '-c', 'kill -SEGV $$'], returncode=2, stdout='', stderr='/usr/bin/sh: 0: cannot open kill -SEGV $$: No such file\n').ret

### `rc_mismatch_got2_want131` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_env_status.test_status_filter_common_signals`
  > assert 2 == 131
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-n', '-z', '-xx', '/tmp/pytest-of-root/pytest-0/test_status_filter_common_sign2/sigquit.sh'], returncode=2, stdout='', stderr="entr: inva

### `rc_mismatch_got2_want4` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_harvest.test_exec_command_oneshot_exit_code_from_child`
  > AssertionError: assert 2 == 4
  >  +  where 2 = CompletedProcess(args=['./executable', '-n', '-z', 'sh', '-c', 'exit 4'], returncode=2).returncode

### `rc_mismatch_got241_want143` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_signals.test_oneshot_signal_exit`
  > AssertionError: assert 241 == 143
  >  +  where 241 = CompletedProcess(args=['/workspace/executable', '-n', '-z', '/tmp/pytest-of-root/pytest-0/test_oneshot_signal_exit2/killer.sh'], returncode=241, stdout='starting\n', stderr='').returnc

### `rc_mismatch_got2_want255` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_status_gaps.test_status_filter_exit_255`
  > assert 2 == 255
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-xx', '-z', '-n', '/tmp/pytest-of-root/pytest-0/test_status_filter_exit_2552/exit255.sh'], returncode=2, stdout='', stderr="entr: invalid

### `rc_mismatch_got2_want13` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_status_gaps.test_status_filter_with_shell_mode`
  > assert 2 == 13
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-xx', '-z', '-n', '-s', 'exit 13'], returncode=2, stdout='', stderr="entr: invalid option -- 'x'\nusage: entr [-hV] [-c] [-d] [-p] [-r] [

### `rc_mismatch_got2_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_status_gaps.test_status_filter_with_stderr_output`
  > assert 2 == 3
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-xx', '-z', '-n', '/tmp/pytest-of-root/pytest-0/test_status_filter_with_stderr2/stderr.sh'], returncode=2, stdout='', stderr="entr: inval

