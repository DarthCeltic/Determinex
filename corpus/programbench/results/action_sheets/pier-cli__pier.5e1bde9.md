# Action Sheet — pier-cli__pier.5e1bde9

**Current:** 9.29%  (100/1076)
**Pass / Fail / Skip:** 100 / 675 / 0
**Gap to 100%:** 90.71 percentage points (976 tests)

## Failure clusters

675 failed tests grouped into 17 buckets (sorted by count).

### `rc_mismatch_got1_want0` — 418 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_add_command.test_add_script_basic`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-c', '/tmp/tmp7u4ng9hf/test_config.toml', 'add', '--alias', 'test1', 'echo hello'], returncode=1, stdout=b'Error: AliasNotFound: -c\n', s
- `tests.test_add_command.test_add_script_with_description`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-c', '/tmp/tmpkog4_2q3/test_config.toml', 'add', '--alias', 'test2', '--description', 'Test description', 'echo test2'], returncode=1, st
- `tests.test_add_command.test_add_script_with_single_tag`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-c', '/tmp/tmp10i_u0jq/test_config.toml', 'add', '--alias', 'test3', '--tag', 'test', '--', 'echo test3'], returncode=1, stdout=b'Error: 
- *(... 415 more in this cluster)*

### `other_assertion` — 170 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_add_command.test_add_duplicate_alias_fails`
  > AssertionError: assert (b'already exists' in b'error: aliasnotfound: -c\n' or b'exists' in b'error: aliasnotfound: -c\n')
  >  +  where b'error: aliasnotfound: -c\n' = <built-in method lower of bytes object at 0x7f252a0c2e70>()
  >  +    where <built-in method lower of bytes object at 0x7f252a0c2e70> = b'Error: AliasNotFound: -c\n'.lower
  >  +      where b'Error: AliasNotFound: -c\n' = CompletedProcess(args=['/workspace/executable', '-c', '/tmp/tmplzw2ofan/test_config.toml', 'add', '--alias', 'dup', 'echo 2'], returncode=1, stdout=b'Erro
  >  +  and   b'error: aliasnotfound: -c\n' = <built-in method lower of bytes object at 0x7f252a0c2e70>()
  >  +    where <built-in method lower of bytes object at 0x7f252a0c2e70> = b'Error: AliasNotFound: -c\n'.lower
  >  +      where b'Error: AliasNotFound: -c\n' = CompletedProcess(args=['/workspace/executable', '-c', '/tmp/tmplzw2ofan/test_config.toml', 'add', '--alias', 'dup', 'echo 2'], returncode=1, stdout=b'Erro
- `tests.test_basic_invocation.test_help_flag`
  > AssertionError: assert b'A simple script management CLI' in b'pier 0.1.5\nManage CLI script aliases.\n\nUsage: pier [OPTIONS] [SUBCOMMAND]\n\nSubcommands:\n  add        Add a new alias\n  remove     R
  >  +  where b'pier 0.1.5\nManage CLI script aliases.\n\nUsage: pier [OPTIONS] [SUBCOMMAND]\n\nSubcommands:\n  add        Add a new alias\n  remove     Remove an alias\n  show       Show alias definition
- `tests.test_basic_invocation.test_help_short_flag`
  > AssertionError: assert b'A simple script management CLI' in b'pier 0.1.5\nManage CLI script aliases.\n\nUsage: pier [OPTIONS] [SUBCOMMAND]\n\nSubcommands:\n  add        Add a new alias\n  remove     R
  >  +  where b'pier 0.1.5\nManage CLI script aliases.\n\nUsage: pier [OPTIONS] [SUBCOMMAND]\n\nSubcommands:\n  add        Add a new alias\n  remove     Remove an alias\n  show       Show alias definition
- *(... 167 more in this cluster)*

### `string_output_mismatch` — 42 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_add_remove.test_copy_to_existing_alias_fails`
  > AssertionError: assert 'Error: AliasNotFound: -c' == 'error: Alias...ts:  existing'
  >   
  >   - error: AliasAlreadyExists:  existing
  >   + Error: AliasNotFound: -c
- `tests.test_add_remove.test_copy_nonexistent_source_fails`
  > AssertionError: assert 'Error: AliasNotFound: -c' == 'error: Alias...s nonexistent'
  >   
  >   - error: AliasNotFound: No script found by alias nonexistent
  >   + Error: AliasNotFound: -c
- `tests.test_config.test_empty_config_vs_no_scripts`
  > AssertionError: assert 'Error: AliasNotFound: -c' == 'error: No sc...a new script?'
  >   
  >   - error: No scripts exist. Would you like to add a new script?
  >   + Error: AliasNotFound: -c
- *(... 39 more in this cluster)*

### `rc_unexpected_zero` — 12 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_basic_invocation.test_no_arguments_shows_error`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable'], returncode=0, stdout=b'pier 0.1.5\nManage CLI script aliases.\n\nUsage: pier [OPTIONS] [SUBCOMMAND]\n\nSubcommands:\n  add        Add a n
- `tests.test_basic_invocation.test_no_arguments`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable'], returncode=0, stdout=b'pier 0.1.5\nManage CLI script aliases.\n\nUsage: pier [OPTIONS] [SUBCOMMAND]\n\nSubcommands:\n  add        Add a n
- `eval.tests.test_argparse_validation.test_missing_required_args_and_unknown_flags[args0-expected_substrings0]`
  > assert 0 != 0
- *(... 9 more in this cluster)*

### `rc_mismatch_got0_want1` — 11 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_errors.test_config_file_not_found_with_path`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'list'], returncode=0, stdout='No aliases configured.\n', stderr='').returncode
- `tests.test_errors.test_no_default_config_exists`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'list'], returncode=0, stdout='No aliases configured.\n', stderr='').returncode
- `tests.test_errors.test_malformed_toml_syntax`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'list'], returncode=0, stdout='No aliases configured.\n', stderr='').returncode
- *(... 8 more in this cluster)*

### `rc_mismatch_got2_want0` — 8 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_cli_combinations.test_help_for_all_subcommands`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'add', '--help'], returncode=2, stdout=b'Error: --alias NAME and -- COMMAND required\n', stderr=b'Error: --alias NAME and -- COMMAND requi
- `tests.test_cli_combinations.test_short_help_for_all_subcommands`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'add', '-h'], returncode=2, stdout=b'Error: --alias NAME and -- COMMAND required\n', stderr=b'Error: --alias NAME and -- COMMAND required\
- `tests.test_cli_combinations.test_version_for_all_subcommands`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'add', '--version'], returncode=2, stdout=b'Error: --alias NAME and -- COMMAND required\n', stderr=b'Error: --alias NAME and -- COMMAND re
- *(... 5 more in this cluster)*

### `rc_mismatch_got1_want100` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_run_command.test_run_script_exit_custom_code`
  > AssertionError: assert 1 == 100
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-c', '/tmp/tmpxkx16knw/test_config.toml', 'run', 'exit100'], returncode=1, stdout=b'Error: AliasNotFound: -c\n', stderr=b'Error: AliasNot
- `tests.test_run.test_run_script_with_custom_exit_code`
  > AssertionError: assert 1 == 100
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-c', '/tmp/tmpsxdxp_em/pier.toml', 'run', 'exit_100'], returncode=1, stdout=b'Error: AliasNotFound: -c\n', stderr=b'Error: AliasNotFound:
- `tests.test_harvest.test_run_custom_exit_code`
  > AssertionError: assert 1 == 100
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-c', '/tmp/pytest-of-root/pytest-0/test_run_custom_exit_code2/pier_config.toml', 'run', 'test_exit_with_100'], returncode=1, stdout='Erro

### `rc_mismatch_got1_want42` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_run.test_exit_code_propagation_custom`
  > AssertionError: assert 1 == 42
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-c', '/tmp/pytest-of-root/pytest-0/test_exit_code_propagation_cus2/pier_config.toml', 'exit_custom'], returncode=1, stdout='Error: AliasN
- `tests.test_run.test_run_custom_exit_code`
  > AssertionError: assert 1 == 42
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-c', '/tmp/tmplhie326r.toml', 'run', 'exit_42'], returncode=1, stdout='Error: AliasNotFound: -c\n', stderr='Error: AliasNotFound: -c\n').

### `missing_dict_key` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_add_remove.test_add_multiple_scripts_in_sequence`
  > KeyError: 'first'

### `rc_mismatch_got0_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_add_remove.test_add_force_preserves_other_scripts`
  > assert 0 == 3
  >  +  where 0 = len({})

### `rc_mismatch_got1_want99` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_run.test_shebang_script_exit_code`
  > AssertionError: assert 1 == 99
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-c', '/tmp/pytest-of-root/pytest-0/test_shebang_script_exit_code2/pier_config.toml', 'shebang_exit'], returncode=1, stdout='Error: AliasN

### `rc_mismatch_got1_want127` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_run.test_exit_code_127`
  > AssertionError: assert 1 == 127
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-c', '/tmp/pytest-of-root/pytest-0/test_exit_code_1272/pier_config.toml', 'exit_127'], returncode=1, stdout='Error: AliasNotFound: -c\n',

### `rc_mismatch_got1_want2` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_run.test_exit_code_2`
  > AssertionError: assert 1 == 2
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-c', '/tmp/pytest-of-root/pytest-0/test_exit_code_22/pier_config.toml', 'exit_2'], returncode=1, stdout='Error: AliasNotFound: -c\n', std

### `rc_mismatch_got127_want0` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_add_show_remove_and_run.test_run_via_subcommand_and_direct_alias_equivalent`
  > assert 127 == 0
  >  +  where 127 = CompletedProcess(args=['/workspace/executable', 'args', 'a', 'b'], returncode=127, stdout=b'', stderr=b'sh: 1: %s": not found\n').returncode

### `rc_mismatch_got2_want7` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_add_show_remove_and_run.test_exit_code_and_stdout_stderr_passthrough_from_script`
  > assert 2 == 7
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'run', 'fail'], returncode=2, stdout=b'', stderr=b'OUT: 1: Syntax error: Unterminated quoted string\nERR\nsh: 1: exit: Illegal number: 7"\

### `returned_none` — 1 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_pier_executable.test_version`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f62ee042680>('\\b0\\.1\\.6\\b', 'pier 0.1.5\n')
  >  +    where <function search at 0x7f62ee042680> = re.search
  >  +    and   'pier 0.1.5\n' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout='pier 0.1.5\n', stderr='').stdout

### `boolean_false` — 1 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `eval.tests.test_pier_executable.test_help_header`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7f62ec3bd480>('pier 0.1.6\n')
  >  +    where <built-in method startswith of str object at 0x7f62ec3bd480> = 'pier 0.1.5\nManage CLI script aliases.\n\nUsage: pier [OPTIONS] [SUBCOMMAND]\n\nSubcommands:\n  add        Add a new alias\n
  >  +      where 'pier 0.1.5\nManage CLI script aliases.\n\nUsage: pier [OPTIONS] [SUBCOMMAND]\n\nSubcommands:\n  add        Add a new alias\n  remove     Remove an alias\n  show       Show alias definit

