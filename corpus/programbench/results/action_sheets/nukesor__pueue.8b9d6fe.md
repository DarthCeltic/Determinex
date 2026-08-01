# Action Sheet — nukesor__pueue.8b9d6fe

**Current:** 1.39%  (14/1009)
**Pass / Fail / Skip:** 14 / 428 / 13
**Gap to 100%:** 98.61 percentage points (995 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_configuration.test_profile_loads_different_socket_path`
  - reason: gold-env-limitation: requires daemon binary not available in gold environment
- `tests.test_configuration.test_pueue_directory_setting_creates_directory`
  - reason: gold-env-limitation: requires daemon binary not available in gold environment
- `tests.test_configuration.test_unix_socket_path_setting_exact`
  - reason: gold-env-limitation: requires daemon binary not available in gold environment
- `tests.test_configuration.test_default_parallel_tasks_setting_enforced`
  - reason: gold-env-limitation: requires daemon binary not available in gold environment
- `tests.test_configuration.test_boolean_setting_false_parsed_correctly`
  - reason: gold-env-limitation: requires daemon binary not available in gold environment
- *(... 8 more skipped)*

## Failure clusters

428 failed tests grouped into 12 buckets (sorted by count).

### `rc_mismatch_got2_want0` — 185 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_basic_invocation.TestHelp.test_help_parallel_subcommand`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'parallel', '--help'], returncode=2, stdout=b'', stderr=b"error: no such command: parallel\nusage: pueue [OPTIONS] [ARGS]\nTry 'pueue --he
- `tests.test_basic_invocation.TestHelp.test_help_completions_subcommand`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'completions', '--help'], returncode=2, stdout=b'', stderr=b"error: no such command: completions\nusage: pueue [OPTIONS] [ARGS]\nTry 'pueu
- `tests.test_basic_invocation.TestHelp.test_help_env_subcommand`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'env', '--help'], returncode=2, stdout=b'', stderr=b"error: no such command: env\nusage: pueue [OPTIONS] [ARGS]\nTry 'pueue --help' for mo
- *(... 182 more in this cluster)*

### `other_assertion` — 73 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.TestHelp.test_help_add_subcommand`
  > AssertionError: assert b'COMMAND' in b'New task added (id 1): --help\n'
  >  +  where b'New task added (id 1): --help\n' = CompletedProcess(args=['/workspace/executable', 'add', '--help'], returncode=0, stdout=b'New task added (id 1): --help\n', stderr=b'').stdout
- `tests.test_basic_invocation.TestHelp.test_help_remove_subcommand`
  > assert b'TASK_IDS' in b"Command 'remove' executed successfully\n"
  >  +  where b"Command 'remove' executed successfully\n" = CompletedProcess(args=['/workspace/executable', 'remove', '--help'], returncode=0, stdout=b"Command 'remove' executed successfully\n", stderr=b'
- `tests.test_basic_invocation.TestHelp.test_help_status_subcommand`
  > AssertionError: assert (b'--json' in b'' or b'json' in b'')
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', 'status', '--help'], returncode=0, stdout=b'', stderr=b'Queue is empty\n').stdout
  >  +  and   b'' = CompletedProcess(args=['/workspace/executable', 'status', '--help'], returncode=0, stdout=b'', stderr=b'Queue is empty\n').stdout
- *(... 70 more in this cluster)*

### `missing_file` — 63 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_additional_coverage.TestCallbackCoverage.test_callback_with_stash_count_template`
  > FileNotFoundError: [Errno 2] No such file or directory: '/workspace/target/release/pueued'
- `tests.test_additional_coverage.TestDaemonModCoverage.test_daemon_with_profile_loads_correctly`
  > FileNotFoundError: [Errno 2] No such file or directory: '/workspace/target/release/pueued'
- `tests.test_additional_coverage.TestSettingsSave.test_daemon_creates_config_in_xdg_dir`
  > FileNotFoundError: [Errno 2] No such file or directory: '/workspace/target/release/pueued'
- *(... 60 more in this cluster)*

### `string_output_mismatch` — 56 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_cli_basic.test_main_help_long`
  > AssertionError: assert 'pueue 0.1.0\...int version\n' == 'Interact wit...int version\n'
  >   
  >   - Interact with the Pueue daemon
  >   + pueue 0.1.0
  >   + A command-line task runner
  >     
  >   - Use the `--help` long form to get detailed help output on each subcommand!
  >   - ...
- `tests.test_cli_basic.test_main_help_short`
  > AssertionError: assert 'pueue 0.1.0\...int version\n' == 'Interact wit...int version\n'
  >   
  >   - Interact with the Pueue daemon
  >   + pueue 0.1.0
  >   + A command-line task runner
  >     
  >   - Use the `--help` long form to get detailed help output on each subcommand!
  >   - ...
- `tests.test_cli_basic.test_version_long`
  > AssertionError: assert 'pueue 0.1.0\n' == 'pueue 4.0.4\n'
  >   
  >   - pueue 4.0.4
  >   ?       ^  --
  >   + pueue 0.1.0
  >   ?       ^^^
- *(... 53 more in this cluster)*

### `rc_mismatch_got2_want1` — 15 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_aliasing.test_alias_empty_value`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-c', '/tmp/pytest-of-root/pytest-0/test_alias_empty_value2/config/pueue.yml', 'add', 'empty arg1 arg2'], returncode=2, stdout='', stderr=
- `tests.test_errors_edge_cases.test_non_existent_task_remove`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-c', '/tmp/pytest-of-root/pytest-0/test_non_existent_task_remove2/config/pueue.yml', 'remove', '999999'], returncode=2, stdout='', stderr
- `tests.test_errors_edge_cases.test_remove_running_task_without_kill`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-c', '/tmp/pytest-of-root/pytest-0/test_remove_running_task_witho2/config/pueue.yml', 'remove', '0'], returncode=2, stdout='', stderr="er
- *(... 12 more in this cluster)*

### `json_output_missing_or_bad` — 12 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `tests.test_aliasing.test_multiple_aliases`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_aliasing.test_alias_with_quotes`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_aliasing.test_alias_restart_command`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- *(... 9 more in this cluster)*

### `test_timeout` — 12 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_daemon_handlers.test_log_group_selection`
  > TimeoutError: Task 0 did not complete within 10s
- `tests.test_daemon_handlers.test_log_all_tasks`
  > TimeoutError: Task 0 did not complete within 10s
- `tests.test_daemon_handlers.test_log_json_with_group`
  > TimeoutError: Task 0 did not complete within 10s
- *(... 9 more in this cluster)*

### `rc_unexpected_zero` — 8 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_cli_basic.test_remove_missing_ids`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'remove'], returncode=0, stdout="Command 'remove' executed successfully\n", stderr='').returncode
- `tests.test_cli_basic.test_add_invalid_flag`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'add', '--invalid-flag', 'echo', 'test'], returncode=0, stdout='New task added (id 1): --invalid-flag echo test\n', stderr='').returncode
- `tests.test_cli_basic.test_add_conflicting_immediate_stashed`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'add', '--immediate', '--stashed', 'echo', 'test'], returncode=0, stdout='New task added (id 1): --immediate --stashed echo test\n', stder
- *(... 5 more in this cluster)*

### `rc_mismatch_got0_want10` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_errors_edge_cases.test_many_simultaneous_tasks`
  > assert 0 == 10
  >  +  where 0 = len({})

### `rc_mismatch_got0_want2` — 1 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_errors_edge_cases.test_reset_command_clears_all_state`
  > assert 0 == 2
  >  +  where 0 = len({})

### `returned_none` — 1 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_groups_advanced.test_wait_for_specific_tasks`
  > assert None

### `rc_mismatch_got0_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_groups_advanced.test_kill_group_tasks`
  > assert 0 == 3

