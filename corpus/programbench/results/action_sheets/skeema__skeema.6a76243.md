# Action Sheet — skeema__skeema.6a76243

**Current:** 33.33%  (825/2475)
**Pass / Fail / Skip:** 825 / 722 / 80
**Gap to 100%:** 66.67 percentage points (1650 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_docker_workaround.test_skeema_works_with_local_mysql`
  - reason: gold-env-limitation: MySQL auth differs from dev environment (Error 1698)
- `tests.test_harvest.test_testinithandler_001`
  - reason: Docker required for integration tests
- `tests.test_harvest.test_testinithandler_002`
  - reason: Docker required for integration tests
- `tests.test_harvest.test_testinithandler_003`
  - reason: Docker required for integration tests
- `tests.test_harvest.test_testinithandler_004`
  - reason: Docker required for integration tests
- *(... 75 more skipped)*

## Failure clusters

722 failed tests grouped into 16 buckets (sorted by count).

### `other_assertion` — 479 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_add_env_options.test_add_env_requires_environment_name`
  > assert (b'environment' in b'' or b'required' in b'' or b'Usage:' in b'2026-04-13 14:49:48 [ERROR] Environment name "" is invalid\n')
  >  +  where b'' = <built-in method lower of bytes object at 0x7fe2b2ed4030>()
  >  +    where <built-in method lower of bytes object at 0x7fe2b2ed4030> = b''.lower
  >  +      where b'' = CompletedProcess(args=['/workspace/executable', 'add-environment'], returncode=78, stdout=b'2026-04-13 14:49:48 [ERROR] Environment name "" is invalid\n', stderr=b'').stderr
  >  +  and   b'' = <built-in method lower of bytes object at 0x7fe2b2ed4030>()
  >  +    where <built-in method lower of bytes object at 0x7fe2b2ed4030> = b''.lower
  >  +      where b'' = CompletedProcess(args=['/workspace/executable', 'add-environment'], returncode=78, stdout=b'2026-04-13 14:49:48 [ERROR] Environment name "" is invalid\n', stderr=b'').stderr
  >  +  and   b'2026-04-13 14:49:48 [ERROR] Environment name "" is invalid\n' = CompletedProcess(args=['/workspace/executable', 'add-environment'], returncode=78, stdout=b'2026-04-13 14:49:48 [ERROR] Envi
- `tests.test_add_env_options.test_add_env_dir_option`
  > AssertionError: assert b'--dir' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', 'help', 'add-environment'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_add_env_options.test_add_env_host_option`
  > AssertionError: assert b'--host' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', 'help', 'add-environment'], returncode=0, stdout=b'', stderr=b'').stdout
- *(... 476 more in this cluster)*

### `rc_mismatch_got78_want0` — 63 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_add_environment_command.test_add_environment_help`
  > AssertionError: assert 78 == 0
  >  +  where 78 = CompletedProcess(args=['/workspace/executable', 'add-environment', '--help'], returncode=78, stdout=b'--ssl-mode value\n', stderr=b'').returncode
- `tests.test_format.test_format_max_depth_error`
  > AssertionError: assert 78 == 0
  >  +  where 78 = CompletedProcess(args=['/workspace/executable', 'format'], returncode=78, stdout='', stderr='').returncode
- `tests.test_format.test_format_special_chars_in_config`
  > AssertionError: assert 78 == 0
  >  +  where 78 = CompletedProcess(args=['/workspace/executable', 'format'], returncode=78, stdout='', stderr='').returncode
- *(... 60 more in this cluster)*

### `rc_unexpected_zero` — 50 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_basic_invocation.test_invalid_command`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'invalid-command-xyz'], returncode=0, stdout=b'skeema.io\ndocs\nskeema.io/docs/commands/init\n', stderr=b'').returncode
- `tests.test_basic_invocation.test_invalid_global_flag`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--invalid-flag-xyz'], returncode=0, stdout=b'skeema.io\ndocs\nskeema.io/docs/commands/init\n', stderr=b'').returncode
- `tests.test_command_line_parsing.test_multiple_environments_not_allowed`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'diff', 'production', 'staging'], returncode=0, stdout=b'init\nUsage:\n--host\ndiff\nUsage:\npush\nUsage:\npull\nUsage:\nformat\n', stderr
- *(... 47 more in this cluster)*

### `string_output_mismatch` — 47 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_errors.test_unknown_command`
  > assert '' == '[ERROR] Unkn... "badcommand"'
  >   
  >   - [ERROR] Unknown command "badcommand"
- `tests.test_errors.test_unknown_global_option`
  > assert '' == '[ERROR] CLI:... "bad-option"'
  >   
  >   - [ERROR] CLI: Unknown option "bad-option"
- `tests.test_errors.test_init_missing_required_host`
  > AssertionError: assert '' == '[ERROR] Opti... command-line'
  >   
  >   - [ERROR] Option --host must be supplied on the command-line
- *(... 44 more in this cluster)*

### `rc_mismatch_got0_want78` — 21 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_comprehensive.test_invalid_command`
  > AssertionError: assert 0 == 78
  >  +  where 0 = CompletedProcess(args=['/workspace/eval/tests/../../executable', 'invalid-command'], returncode=0, stdout='(enabled by default; disable with --skip-format)\n, commit\n, released\n-- inst
- `tests.test_cli_comprehensive.test_global_host_option_restricted_in_lint`
  > AssertionError: assert 0 == 78
  >  +  where 0 = CompletedProcess(args=['/workspace/eval/tests/../../executable', '--host=localhost', 'lint'], returncode=0, stdout='(enabled by default; disable with --skip-format)\n, commit\n, released
- `tests.test_cli_comprehensive.test_global_schema_option_restricted_in_lint`
  > AssertionError: assert 0 == 78
  >  +  where 0 = CompletedProcess(args=['/workspace/eval/tests/../../executable', '--schema=mydb', 'lint'], returncode=0, stdout='(enabled by default; disable with --skip-format)\n, commit\n, released\n-
- *(... 18 more in this cluster)*

### `missing_file` — 16 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_columntype.test_unsigned_zerofill_attribute`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpru23n0a7/numeric_types.sql'
- `tests.test_columntype.test_decimal_precision_scale`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpidam08iw/numeric_types.sql'
- `tests.test_columntype.test_float_double_precision`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpaek6r361/numeric_types.sql'
- *(... 13 more in this cluster)*

### `boolean_false` — 14 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_db_commands.test_init_dir_option_creates_nested_path`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/pytest-of-root/pytest-0/test_init_dir_option_creates_n2/workspace/level1/level2/level3').exists
- `tests.test_db_commands.test_init_with_dir_default_uses_hostname`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/pytest-of-root/pytest-0/test_init_with_dir_default_use2/workspace/db.example.com').exists
- `tests.test_db_commands.test_init_dir_option_with_absolute_path`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/pytest-of-root/pytest-0/test_init_dir_option_with_abso2/workspace/absolute_test').exists
- *(... 11 more in this cluster)*

### `rc_mismatch_got0_want2` — 10 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_applier.test_push_modify_column_type_unsafe_blocked`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'push'], returncode=0, stdout='', stderr='').returncode
- `tests.test_diff.test_diff_with_schema_subdirectory`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/eval/tests/../../executable', 'diff'], returncode=0, stdout='', stderr='').returncode
- `tests.test_diff.test_diff_with_ignore_table_option`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/eval/tests/../../executable', 'diff'], returncode=0, stdout='', stderr='').returncode
- *(... 7 more in this cluster)*

### `rc_mismatch_got78_want2` — 6 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_filesystem_edge_cases.test_symlink_config_file_pointing_outside_repo`
  > AssertionError: assert 78 == 2
  >  +  where 78 = CompletedProcess(args=['/workspace/executable', 'format', '--skip-write'], returncode=78, stdout='', stderr='').returncode
- `tests.test_filesystem_edge_cases.test_skeema_symlink_to_symlink_is_rejected`
  > AssertionError: assert 78 == 2
  >  +  where 78 = CompletedProcess(args=['/workspace/executable', 'format', '--skip-write'], returncode=78, stdout='', stderr='').returncode
- `tests.test_filesystem_edge_cases.test_skeema_symlink_to_directory_is_rejected`
  > AssertionError: assert 78 == 2
  >  +  where 78 = CompletedProcess(args=['/workspace/executable', 'format', '--skip-write'], returncode=78, stdout='', stderr='').returncode
- *(... 3 more in this cluster)*

### `rc_mismatch_got2_want78` — 4 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_db_commands.test_init_environment_name_validated_for_brackets`
  > AssertionError: assert 2 == 78
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'init', '--host', 'localhost', '--dir', '/tmp/pytest-of-root/pytest-0/test_init_environment_name_val2/workspace', '[prod'], returncode=2, 
- `tests.test_db_commands.test_init_environment_name_validated_for_carriage_return`
  > AssertionError: assert 2 == 78
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'init', '--host', 'localhost', '--dir', '/tmp/pytest-of-root/pytest-0/test_init_environment_name_val5/workspace', 'pro\rd'], returncode=2,
- `tests.test_errors.test_init_dir_already_exists_with_skeema_file`
  > AssertionError: assert 2 == 78
  >  +  where 2 = CompletedProcess(args=['/workspace/eval/tests/../../executable', 'init', '--host', 'localhost', '--dir', '/tmp/tmpnfji7cn0/localhost'], returncode=2, stdout='', stderr='').returncode
- *(... 1 more in this cluster)*

### `test_timeout` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_harvest_unit.test_harvest_fs_ParseDir`
  > subprocess.TimeoutExpired: Command '['go', 'test', '-v', '-short', '-coverprofile=/tmp/go_unit_coverage/_internal_fs_TestParseDir.out', '-run', 'TestParseDir$', './internal/fs']' timed out after 10 se
- `tests.test_harvest_unit.test_harvest_fs_ParseDirErrors`
  > subprocess.TimeoutExpired: Command '['go', 'test', '-v', '-short', '-coverprofile=/tmp/go_unit_coverage/_internal_fs_TestParseDirErrors.out', '-run', 'TestParseDirErrors$', './internal/fs']' timed out
- `tests.test_harvest_unit.test_harvest_fs_ParseDirSymlinks`
  > subprocess.TimeoutExpired: Command '['go', 'test', '-v', '-short', '-coverprofile=/tmp/go_unit_coverage/_internal_fs_TestParseDirSymlinks.out', '-run', 'TestParseDirSymlinks$', './internal/fs']' timed

### `returned_none` — 3 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_cli_args.test_error_format_includes_timestamp_and_component_prefix_for_cli_errors`
  > assert None
  >  +  where None = <function search at 0x7f3ac01da680>('\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2} \\[ERROR\\] CLI:', "error: unexpected argument '--nope' found\nError: unexpected argument '--nope' found
  >  +    where <function search at 0x7f3ac01da680> = re.search
- `eval.tests.test_help_subcommands.test_subcommand_help_usage_line`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f4c81646680>('^Usage:\\s+skeema diff\\s+\\[<options>\\]\\s+\\[<environment>\\]\\s*$', 'diff\nUsage:\nUsage:\nhost-wrapper\ntemplate\n', re.MULTILINE)
  >  +    where <function search at 0x7f4c81646680> = re.search
  >  +    and   'diff\nUsage:\nUsage:\nhost-wrapper\ntemplate\n' = CompletedProcess(args=['/workspace/executable', '--help=diff'], returncode=0, stdout='diff\nUsage:\nUsage:\nhost-wrapper\ntemplate\n', st
  >  +    and   re.MULTILINE = re.MULTILINE
- `eval.tests.test_subcommand_dispatch.test_help_subcommand_routes_to_other_subcommand_help`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f5ba94b2680>('usage:\\s+skeema\\s+diff\\b', '')
  >  +    where <function search at 0x7f5ba94b2680> = re.search

### `rc_mismatch_got0_want1` — 2 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_applier.test_diff_dry_run_no_execution`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'diff'], returncode=0, stdout='', stderr='').returncode
- `tests.test_dumper.test_basic_schema_export`
  > assert 0 == 1
  >  +  where 0 = len([])

### `rc_mismatch_got2_want0` — 2 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `eval.tests.test_subcommand_dispatch.test_global_flags_before_subcommand[version-global_flag_variant3]`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--ssl-mode', 'preferred', 'version'], returncode=2, stdout='', stderr='').returncode
- `eval.tests.test_subcommand_dispatch.test_global_flags_after_subcommand[help-global_flag_variant3]`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'help', '--ssl-mode', 'preferred'], returncode=2, stdout='', stderr='').returncode

### `uncategorized` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_db_commands.test_add_environment_with_localhost_and_port_writes_tcp_config`
  > ValueError: substring not found

### `rc_mismatch_got78_want73` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_errors.test_empty_host_causes_dir_creation_error`
  > AssertionError: assert 78 == 73
  >  +  where 78 = CompletedProcess(args=['/workspace/eval/tests/../../executable', 'init', '--host', ''], returncode=78, stdout='', stderr='').returncode

