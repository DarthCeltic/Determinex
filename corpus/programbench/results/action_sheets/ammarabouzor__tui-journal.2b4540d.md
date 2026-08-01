# Action Sheet — ammarabouzor__tui-journal.2b4540d

**Current:** 22.87%  (518/2265)
**Pass / Fail / Skip:** 518 / 967 / 8
**Gap to 100%:** 77.13 percentage points (1747 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_cli_behavior.test_theme_print_path_uses_isolated_home`
  - reason: test_theme_print_path_uses_isolated_home depends on test_print_config_defaults_in_isolated_home
- `eval.tests.test_cli_behavior.test_theme_write_defaults_creates_file`
  - reason: test_theme_write_defaults_creates_file depends on test_theme_print_path_uses_isolated_home
- `eval.tests.test_cli_behavior.test_theme_print_path_uses_isolated_home`
  - reason: test_theme_print_path_uses_isolated_home depends on test_print_config_defaults_in_isolated_home
- `eval.tests.test_cli_behavior.test_theme_write_defaults_creates_file`
  - reason: test_theme_write_defaults_creates_file depends on test_theme_print_path_uses_isolated_home
- `eval.tests.test_subcommand_dispatch.test_subcommand_help_recognized[NOTSET]`
  - reason: got empty parameter set for (subcmd)
- *(... 3 more skipped)*

## Failure clusters

967 failed tests grouped into 19 buckets (sorted by count).

### `other_assertion` — 512 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_additional_coverage.test_backend_switching_sequence`
  > AssertionError: assert b'Json' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', '-j', '/tmp/tmp65af3oem/test.json', '-b', 'json', 'pc'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_additional_coverage.test_backend_with_relative_paths`
  > AssertionError: assert ('/tmp/tmp0a50q11f' in '' or '/' in '')
  >  +  where '/tmp/tmp0a50q11f' = str(PosixPath('/tmp/tmp0a50q11f'))
- `tests.test_additional_coverage.test_all_help_aliases`
  > AssertionError: assert 'pc]' in 'Usage:\n'
- *(... 509 more in this cluster)*

### `string_output_mismatch` — 98 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_cli.test_help`
  > AssertionError: assert 'Usage:\n' == 'Tui app allo...int version\n'
  >   
  >   + Usage:
  >   - Tui app allows writing and managing journals/notes from within the terminal With different local back-ends
  >   - 
  >   - Usage: executable [OPTIONS] [COMMAND]
  >   - 
  >   - Commands:...
- `eval.tests.test_cli.test_theme_help`
  > AssertionError: assert 'themes and s...te-defaults\n' == 'Provides com... Print help\n'
  >   
  >   + themes and styles
  >   - Provides commands regarding changing themes and styles of the app
  >   - 
  >     Usage: executable theme <COMMAND>
  >   - 
  >     Commands:...
- `eval.tests.test_cli_basics.TestHelpVersion.test_help_flag`
  > AssertionError: assert 'Usage:\n' == 'Tui app allo...int version\n'
  >   
  >   + Usage:
  >   - Tui app allows writing and managing journals/notes from within the terminal With different local back-ends
  >   - 
  >   - Usage: executable [OPTIONS] [COMMAND]
  >   - 
  >   - Commands:...
- *(... 95 more in this cluster)*

### `boolean_false` — 60 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_additional_coverage.test_log_with_print_config`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmptpctg4de/app.log').exists
- `tests.test_additional_coverage.test_log_with_theme_commands`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmp0j6_6mnm/theme.log').exists
- `tests.test_backend_logging.test_json_backend_creates_directory`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmp5lu83qa1/nested/dir').exists
  >  +      where PosixPath('/tmp/tmp5lu83qa1/nested/dir') = PosixPath('/tmp/tmp5lu83qa1/nested/dir/journals.json').parent
- *(... 57 more in this cluster)*

### `rc_unexpected_zero` — 56 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_basic_invocation.test_invalid_flag`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--invalid-flag'], returncode=0, stdout=b'--json-file-path\n--sqlite-file-path\n--backend-type\n--config\n--verbose\n--log\n-j\n-s\n-b\n-c
- `tests.test_basic_invocation.test_invalid_short_flag`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-x'], returncode=0, stdout=b'--json-file-path\n--sqlite-file-path\n--backend-type\n--config\n--verbose\n--log\n-j\n-s\n-b\n-c\n', stderr=
- `tests.test_import_assign.test_assign_priority_invalid_string`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'assign-priority', 'invalid'], returncode=0, stdout=b'Assign priority\nempty priority field\nUsage: executable assign-priority <PRIORITY>\
- *(... 53 more in this cluster)*

### `rc_mismatch_got1_want0` — 41 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_additional_coverage.test_theme_write_with_existing_directory`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-c', '/tmp/tmpv3s0ohys/config', 'theme', 'write-defaults'], returncode=1, stdout=b'', stderr=b'').returncode
- `tests.test_additional_coverage.test_config_path_normalization`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-c', '/tmp/tmpy3bn8_m4/config/', 'print-config'], returncode=1, stdout=b'', stderr=b'').returncode
- `tests.test_additional_coverage.test_theme_write_creates_directory`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-c', '/tmp/tmp97dxoo86/new_config', 'theme', 'write-defaults'], returncode=1, stdout=b'', stderr=b'').returncode
- *(... 38 more in this cluster)*

### `uncategorized` — 39 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_backend_logging.test_backend_type_json_flag`
  > toml.decoder.TomlDecodeError: Key name found without value. Reached end of line. (line 1 column 13 char 12)
- `tests.test_backend_logging.test_backend_type_sqlite_flag`
  > toml.decoder.TomlDecodeError: Key name found without value. Reached end of line. (line 1 column 13 char 12)
- `tests.test_backend_logging.test_backend_type_short_flag`
  > toml.decoder.TomlDecodeError: Key name found without value. Reached end of line. (line 1 column 13 char 12)
- *(... 36 more in this cluster)*

### `rc_mismatch_got0_want2` — 28 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_argument_parsing.TestBasicFlags.test_invalid_flag`
  > assert 0 == 2
- `tests.test_argument_parsing.TestBasicFlags.test_invalid_short_flag`
  > assert 0 == 2
- `tests.test_argument_parsing.TestBackendTypeFlag.test_backend_type_invalid`
  > assert 0 == 2
- *(... 25 more in this cluster)*

### `subprocess_failed` — 26 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_editor_global_gap.test_cycle_forward_tab`
  > subprocess.CalledProcessError: Command '['tmux', 'send-keys', '-t', 'test_cycle_fwd_test_cycle_forward_tab2', 'q']' returned non-zero exit status 1.
- `tests.test_editor_global_gap.test_cycle_backward_tab_then_forward`
  > subprocess.CalledProcessError: Command '['tmux', 'send-keys', '-t', 'test_cycle_back_test_cycle_backward_tab_then_f2', 'q']' returned non-zero exit status 1.
- `tests.test_editor_global_gap.test_show_help_from_entries_list`
  > subprocess.CalledProcessError: Command '['tmux', 'send-keys', '-t', 'test_help_global_test_show_help_from_entries_li2', 'q']' returned non-zero exit status 1.
- *(... 23 more in this cluster)*

### `missing_file` — 23 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_app_state.test_state_file_default_content`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tj_state_0gnegdia/.local/state/tui-journal/state.json'
- `tests.test_app_state.test_state_file_pretty_printed`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tj_state_uhn9eti0/.local/state/tui-journal/state.json'
- `tests.test_app_state.test_legacy_migration_preserves_custom_criteria`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tj_state_oz6dl541/.local/state/tui-journal/state.json'
- *(... 20 more in this cluster)*

### `missing_dict_key` — 21 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_backend_logging.test_json_backend_flag`
  > KeyError: 'json_backend'
- `tests.test_backend_logging.test_json_backend_short_flag`
  > KeyError: 'json_backend'
- `tests.test_backend_logging.test_sqlite_backend_flag`
  > KeyError: 'sqlite_backend'
- *(... 18 more in this cluster)*

### `rc_mismatch_got0_want1` — 20 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `eval.tests.test_data_cli.test_import_json`
  > assert 0 == 1
  >  +  where 0 = len([])
- `eval.tests.test_theme.TestThemeWriteDefaults.test_theme_write_defaults_file_exists`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--config', '/tmp/pytest-of-root/pytest-0/test_theme_write_defaults_file2/config', 'theme', 'write-defaults'], returncode=0, stdout='', st
- `eval.tests.test_data_cli.test_import_json`
  > assert 0 == 1
  >  +  where 0 = len([])
- *(... 17 more in this cluster)*

### `returned_none` — 15 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_basic_invocation.test_version_flag`
  > AssertionError: assert None
  >  +  where None = <function match at 0x7fbeeb396170>(b'tui-journal \\d+\\.\\d+\\.\\d+', b'tui-journal\n')
  >  +    where <function match at 0x7fbeeb396170> = re.match
  >  +    and   b'tui-journal\n' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'tui-journal\n', stderr=b'').stdout
- `tests.test_basic_invocation.test_version_short_flag`
  > AssertionError: assert None
  >  +  where None = <function match at 0x7fbeeb396170>(b'tui-journal \\d+\\.\\d+\\.\\d+', b'tui-journal\n')
  >  +    where <function match at 0x7fbeeb396170> = re.match
  >  +    and   b'tui-journal\n' = CompletedProcess(args=['/workspace/executable', '-V'], returncode=0, stdout=b'tui-journal\n', stderr=b'').stdout
- `tests.test_basic_invocation.test_version_flag`
  > AssertionError: assert None
  >  +  where None = <function match at 0x7f7acea25120>(b'tui-journal \\d+\\.\\d+\\.\\d+', b'tui-journal\n')
  >  +    where <function match at 0x7f7acea25120> = re.match
  >  +    and   b'tui-journal\n' = CompletedProcess(args=['./executable', '--version'], returncode=0, stdout=b'tui-journal\n', stderr=b'').stdout
- *(... 12 more in this cluster)*

### `bytes_output_mismatch` — 15 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_output_consistency.test_help_output_consistent`
  > AssertionError: assert b'Usage:\n' == b'Tui app all...int version\n'
  >   
  >   At index 0 diff: b'U' != b'T'
  >   
  >   Full diff:
  >   + (b'Usage:\n')
  >   - (b'Tui app allows writing and managing journals/notes from within the terminal '
  >   -  b'With different local back-ends\n\nUsage: executable [OPTIONS] [COMMAND]\n\nC'...
- `tests.test_output_consistency.test_version_output_consistent`
  > AssertionError: assert b'tui-journal\n' == b'tui-journal 0.16.1\n'
  >   
  >   At index 11 diff: b'\n' != b' '
  >   
  >   Full diff:
  >   - (b'tui-journal 0.16.1\n')
  >   ?               -------
  >   + (b'tui-journal\n')
- `tests.test_output_consistency.test_theme_default_output_consistent`
  > assert b'[\n]\n=\n[\n[general\nfg\n' == b'[general.in...ightBlue"\n\n'
  >   
  >   At index 1 diff: b'\n' != b'g'
  >   
  >   Full diff:
  >   + (b'[\n]\n=\n[\n[general\nfg\n')
  >   - (b'[general.input_block_active]\nfg = "LightYellow"\nmodifiers = ""\n\n[general'
  >   -  b'.input_block_invalid]\nfg = "LightRed"\nmodifiers = ""\n\n[general.input_cor'...
- *(... 12 more in this cluster)*

### `rc_mismatch_got1_want2` — 6 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_edge_cases.test_version_output_format`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len(['tui-journal'])
- `eval.tests.test_cli_basics.TestHelpVersion.test_version_format`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len(['tui-journal'])
- `eval.tests.test_cli_basics.TestHelpVersion.test_version_format`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len(['tui-journal'])
- *(... 3 more in this cluster)*

### `empty_list_or_string` — 3 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `eval.tests.test_data_cli.test_assign_priority`
  > IndexError: list index out of range
- `eval.tests.test_data_cli.test_assign_priority`
  > IndexError: list index out of range
- `tests.test_data_cli.test_assign_priority`
  > IndexError: list index out of range

### `rc_mismatch_got10_want1` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_edge_cases.test_theme_path_output_format`
  > AssertionError: assert 10 == 1
  >  +  where 10 = len(['themes.toml', 'themes.toml', 'themes.toml', 'themes.toml', '[', ']', ...])

### `rc_mismatch_got2_want0` — 1 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `eval.tests.test_args_parsing.test_backend_type_accepts_short_long_and_equals_forms[args4-backend_type = "Json"]`
  > assert 2 == 0

### `json_output_missing_or_bad` — 1 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `tests.test_app_state.test_corrupt_state_file_fallback_to_default`
  > json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 3 (char 2)

### `rc_mismatch_got1_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_operations.test_import_journals_into_existing_backend`
  > AssertionError: assert 1 == 3
  >  +  where 1 = len([{'content': 'Already here', 'date': '2023-12-01T10:00:00Z', 'id': 0, 'priority': 1, ...}])

