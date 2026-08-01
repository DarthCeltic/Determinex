# Action Sheet — ariga__atlas.6d81150

**Current:** 21.93%  (388/1769)
**Pass / Fail / Skip:** 388 / 864 / 3
**Gap to 100%:** 78.07 percentage points (1381 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_atlas_cli.test_version_output`
  - reason: test_version_output depends on test_help_exact
- `eval.tests.test_atlas_cli.test_license_output`
  - reason: test_license_output depends on test_help_exact
- `eval.tests.test_atlas_cli.test_schema_fmt_idempotent_prints_nothing`
  - reason: test_schema_fmt_idempotent_prints_nothing depends on test_schema_fmt_formats_file_and_prints_path

## Failure clusters

864 failed tests grouped into 14 buckets (sorted by count).

### `other_assertion` — 352 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_no_arguments_shows_help`
  > AssertionError: assert b'Manage your database schema as code' in b'# bash completion\n# fish completion\n# powershell completion\n#compdef atlas\n${__atlasCompleterBlock}\n-- 1 migration\n-- 1 migrati
  >  +  where b'# bash completion\n# fish completion\n# powershell completion\n#compdef atlas\n${__atlasCompleterBlock}\n-- 1 migration\n-- 1 migration\\n\n-- 1 sql statement\n-- 1 sql statement\\n\n-- 3 
- `tests.test_basic_invocation.test_help_flag`
  > AssertionError: assert b'completion' in b'Manage your database schema as code\nUsage:\nAvailable Commands:\nManage your database schema as code\nUsage:\nManage your database schema as code\nUsage:\nat
  >  +  where b'Manage your database schema as code\nUsage:\nAvailable Commands:\nManage your database schema as code\nUsage:\nManage your database schema as code\nUsage:\natlas\nversion\ngithub.com\n' = 
- `tests.test_basic_invocation.test_help_flag_short`
  > AssertionError: assert b'Available Commands:' in b'Manage your database schema as code\nUsage:\nManage your database schema as code\nUsage:\natlas\nversion\ngithub.com\nLICENSE\nApache\ngithub.com/ari
  >  +  where b'Manage your database schema as code\nUsage:\nManage your database schema as code\nUsage:\natlas\nversion\ngithub.com\nLICENSE\nApache\ngithub.com/ariga/atlas\n' = CompletedProcess(args=['.
- *(... 349 more in this cluster)*

### `rc_unexpected_zero` — 289 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_basic_invocation.test_invalid_command`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'invalid_command_xyz'], returncode=0, stdout=b'Manage your database schema as code\nUsage:\nversion\nUsage:\n', stderr=b'').returncode
- `tests.test_basic_invocation.test_unknown_flag`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '--unknown-flag-xyz'], returncode=0, stdout=b'# bash completion\n# fish completion\n# powershell completion\n#compdef atlas\n${__atlasCompleterBloc
- `tests.test_error_conditions.test_invalid_url_format`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'schema', 'inspect', '--url', 'invalid://url'], returncode=0, stdout=b'schema\nAvailable Commands\nmigrate\nAvailable Commands\ncompletion\nAvailab
- *(... 286 more in this cluster)*

### `string_output_mismatch` — 132 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_help_output.TestMainHelp.test_help_flag_matches_short_flag`
  > AssertionError: assert 'Manage your ...ngithub.com\n' == 'Manage your ...ariga/atlas\n'
  >   
  >   + Manage your database schema as code
  >   + Usage:
  >   + Available Commands:
  >     Manage your database schema as code
  >     Usage:
  >     Manage your database schema as code...
- `tests.test_help_output.TestMainHelp.test_help_flag_matches_help_command`
  > AssertionError: assert 'Manage your ...ngithub.com\n' == 'Manage your ...rate\napply\n'
  >   
  >   + Manage your database schema as code
  >   + Usage:
  >   + Available Commands:
  >   + Manage your database schema as code
  >   + Usage:
  >     Manage your database schema as code...
- `tests.test_help_output.TestBaselineComparison.test_main_help_exact_output`
  > AssertionError: assert 'Manage your ...ngithub.com\n' == 'Manage your ... a command.\n'
  >   
  >     Manage your database schema as code
  >   - 
  >     Usage:
  >   -   atlas [command]
  >   - 
  >     Available Commands:...
- *(... 129 more in this cluster)*

### `boolean_false` — 29 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_migrate_hash.test_migrate_hash_creates_sum_file`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmp72lh_j4v/migrations/atlas.sum').exists
- `tests.test_migrate_hash.test_migrate_hash_with_multiple_files`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpwrryduid/migrations/atlas.sum').exists
- `tests.test_flags_and_options.test_migrate_hash_dir_format_flag`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = (PosixPath('/tmp/tmphm2c1bkv/migrations') / 'atlas.sum').exists
- *(... 26 more in this cluster)*

### `rc_mismatch_got1_want0` — 23 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_config_env.TestConfigVariables.test_config_with_variables_override`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'schema', 'inspect', '--config', 'file:///tmp/tmpgwiyksac/atlas.hcl', '--env', 'test', '--var', 'db_name=custom.db'], returncode=1, stdout
- `tests.test_config_env.TestConfigurationPrecedence.test_var_flag_overrides_default`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'schema', 'inspect', '--config', 'file:///tmp/tmpn7p6qpz1/atlas.hcl', '--env', 'test', '--var', 'test_var=override_value'], returncode=1, 
- `tests.test_cmdlog_reader.test_cmdlog_migrate_status_json_format_structure`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'migrate', 'status', '--url', 'sqlite://file?mode=memory', '--dir', 'file:///tmp/tmpmfbevo8_/migrations', '--format', '{{ json . }}'], ret
- *(... 20 more in this cluster)*

### `rc_mismatch_got0_want1` — 9 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_migrate_new.test_migrate_new_name_with_spaces`
  > assert 0 == 1
  >  +  where 0 = len([])
- `tests.test_migrate_new.test_migrate_new_empty_file_created`
  > assert 0 == 1
  >  +  where 0 = len([])
- `tests.test_schema_fmt.test_schema_fmt_nonexistent_file`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'schema', 'fmt', '/nonexistent/file.hcl'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 6 more in this cluster)*

### `json_output_missing_or_bad` — 8 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `tests.test_cmdlog_advanced.test_status_template_json_with_indent_argument`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_cmdlog_advanced.test_schema_inspect_template_json_format`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_cmdlog_advanced.test_status_template_json_merge_overlapping_keys`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- *(... 5 more in this cluster)*

### `missing_file` — 7 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_migrate_hash.test_migrate_hash_updates_existing_sum`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmp0wqs6ebz/migrations/atlas.sum'
- `tests.test_special_cases.test_migrate_hash_updates_existing_sum`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpuhlf1izg/migrations/atlas.sum'
- `tests.test_file_operations.test_migrate_hash_updates_sum_file`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpomr58tc9/migrations/atlas.sum'
- *(... 4 more in this cluster)*

### `empty_list_or_string` — 6 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_exit_codes.test_validation_error_exit_nonzero`
  > IndexError: list index out of range
- `tests.test_migrate_hash.test_migrate_hash_after_manual_edit`
  > IndexError: list index out of range
- `tests.test_migrate_validate.test_migrate_validate_after_manual_edit`
  > IndexError: list index out of range
- *(... 3 more in this cluster)*

### `uncategorized` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_migrate_apply.test_apply_to_database_with_existing_migrations`
  > sqlite3.OperationalError: no such table: atlas_schema_revisions
- `tests.test_migrate_apply.test_migration_version_ordering`
  > sqlite3.OperationalError: no such table: atlas_schema_revisions
- `tests.test_migrate_apply.test_apply_only_up_to_amount_when_more_pending`
  > sqlite3.OperationalError: no such table: atlas_schema_revisions

### `bytes_output_mismatch` — 2 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_schema_fmt.test_schema_fmt_valid_hcl`
  > AssertionError: assert (b'schema.hcl' in b'schema\napply\nclean\ndiff\nfmt\ninspect\ncompletion\nbash\nzsh\nfish\n' or b'schema\napp...\nzsh\nfish\n' == b''
  >  +  where b'schema.hcl' = <built-in method encode of str object at 0x7f7e974c08b0>()
  >  +    where <built-in method encode of str object at 0x7f7e974c08b0> = 'schema.hcl'.encode
  >  +      where 'schema.hcl' = PosixPath('/tmp/tmpl3ngcbci/schema.hcl').name
  >  +  and   b'schema\napply\nclean\ndiff\nfmt\ninspect\ncompletion\nbash\nzsh\nfish\n' = CompletedProcess(args=['./executable', 'schema', 'fmt', '/tmp/tmpl3ngcbci/schema.hcl'], returncode=0, stdout=b'sc
  >   
  >   Full diff:
  >   - b''
- `tests.test_schema_fmt.test_schema_fmt_current_directory_with_no_hcl`
  > AssertionError: assert b'schema\napp...\nzsh\nfish\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'schema\napply\nclean\ndiff\nfmt\ninspect\ncompletion\nbash\nzsh\nfish\n')

### `rc_mismatch_got0_want2` — 2 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_migrate_new.test_migrate_new_multiple_migrations`
  > assert 0 == 2
  >  +  where 0 = len([])
- `tests.test_migrate_new.test_migrate_new_timestamps_sequential`
  > assert 0 == 2
  >  +  where 0 = len([])

### `returned_none` — 1 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_main.test_help_has_usage_section_and_synopsis`
  > AssertionError: assert None is not None
  >  +  where None = <function search at 0x7fc16ecb2680>('^Usage:\\n\\s+atlas \\[command\\]$', 'Manage your database schema as code\nUsage:\nAvailable Commands:\nManage your database schema as code\nUsage
  >  +    where <function search at 0x7fc16ecb2680> = re.search
  >  +    and   re.MULTILINE = re.M

### `rc_mismatch_got10_want2` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cmdlog_advanced.test_status_template_nested_range_with_field_access`
  > AssertionError: assert 10 == 2
  >  +  where 10 = len(['migrate', 'apply', 'diff', 'hash', 'lint', 'new', ...])

