# Action Sheet — jesseduffield__lazygit.1d0db51

**Current:** 26.25%  (315/1200)
**Pass / Fail / Skip:** 315 / 444 / 13
**Gap to 100%:** 73.75 percentage points (885 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_cli_behavior.test_print_config_dir_aliases_equivalent[-cd]`
  - reason: test_print_config_dir_aliases_equivalent[-cd] depends on test_print_config_dir_default
- `eval.tests.test_cli_behavior.test_print_config_dir_aliases_equivalent[--print-config-dir]`
  - reason: test_print_config_dir_aliases_equivalent[--print-config-dir] depends on test_print_config_dir_default
- `eval.tests.test_cli_behavior.test_use_config_dir_ordering_invariant`
  - reason: test_use_config_dir_ordering_invariant depends on test_use_config_dir_overrides_print_config_dir
- `eval.tests.test_cli_behavior.test_unknown_flag_prints_help_and_error_message`
  - reason: test_unknown_flag_prints_help_and_error_message depends on test_help_exact_snapshot
- `eval.tests.test_cli_behavior.test_missing_value_for_use_config_dir_errors`
  - reason: test_missing_value_for_use_config_dir_errors depends on test_help_exact_snapshot
- *(... 8 more skipped)*

## Failure clusters

444 failed tests grouped into 11 buckets (sorted by count).

### `other_assertion` — 295 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_cli.test_help_flag`
  > AssertionError: assert (b'executable' in b'' or b'executable' in b'')
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', '--help'], returncode=0, stdout=b'', stderr=b'').stdout
  >  +  and   b'' = CompletedProcess(args=['/workspace/executable', '--help'], returncode=0, stdout=b'', stderr=b'').stderr
- `tests.test_basic_cli.test_help_flag_short`
  > AssertionError: assert (b'Usage:' in b'' or b'Usage:' in b'')
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', '-h'], returncode=0, stdout=b'', stderr=b'').stdout
  >  +  and   b'' = CompletedProcess(args=['/workspace/executable', '-h'], returncode=0, stdout=b'', stderr=b'').stderr
- `tests.test_basic_cli.test_version_flag`
  > AssertionError: assert 'commit=' in ''
- *(... 292 more in this cluster)*

### `rc_unexpected_zero` — 45 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_basic_cli.test_invalid_flag`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--invalid-flag-that-does-not-exist'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_basic_cli.test_conflicting_path_options`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--path=/tmp', '--work-tree=/tmp'], returncode=0, stdout=b'version=\nUsage:\nlazygit\n', stderr=b'').returncode
- `tests.test_daemon_comprehensive.test_daemon_exit_immediately_missing_instruction`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable'], returncode=0, stdout=b"error: the following required arguments were not provided: <PATTERN>\nError: the following required arguments were
- *(... 42 more in this cluster)*

### `string_output_mismatch` — 25 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_args_parsing.test_print_config_dir_flag_prints_path_only`
  > AssertionError: assert '' == '/root/.config/lazygit'
  >   
  >   - /root/.config/lazygit
- `eval.tests.test_config_handling.test_print_config_dir_default_uses_xdg_config_home`
  > AssertionError: assert '' == '/tmp/tmpkt1j...onfig/lazygit'
  >   
  >   - /tmp/tmpkt1jfp30/.config/lazygit
- `eval.tests.test_config_handling.test_config_dir_prefers_legacy_jesseduffield_path_over_new_path_when_both_exist`
  > AssertionError: assert '' == '/tmp/tmpj5ej...field/lazygit'
  >   
  >   - /tmp/tmpj5ej9m5j/.config/jesseduffield/lazygit
- *(... 22 more in this cluster)*

### `boolean_false` — 22 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `eval.tests.test_args_parsing.test_config_flag_prints_yaml_header_key`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7f5ffed64030>('gui:')
  >  +    where <built-in method startswith of str object at 0x7f5ffed64030> = ''.startswith
  >  +      where '' = <built-in method lstrip of str object at 0x7f5ffed64030>()
  >  +        where <built-in method lstrip of str object at 0x7f5ffed64030> = ''.lstrip
- `eval.tests.test_args_parsing.test_value_flags_accept_space_and_equals_forms[args0]`
  > assert False
  >  +  where False = <built-in method startswith of str object at 0x7f5ffceda700>('gui:')
  >  +    where <built-in method startswith of str object at 0x7f5ffceda700> = "error: unexpected argument '-p' found\nError: unexpected argument '-p' found\nunknown flag: unexpected argument '-p' found\n
  >  +      where "error: unexpected argument '-p' found\nError: unexpected argument '-p' found\nunknown flag: unexpected argument '-p' found\nUnknown flag: unexpected argument '-p' found\nUsage: lazygit 
  >  +        where <built-in method lstrip of str object at 0x7f5ffceda700> = "error: unexpected argument '-p' found\nError: unexpected argument '-p' found\nunknown flag: unexpected argument '-p' found\n
- `eval.tests.test_args_parsing.test_value_flags_accept_space_and_equals_forms[args1]`
  > assert False
  >  +  where False = <built-in method startswith of str object at 0x7f5ffcedb120>('gui:')
  >  +    where <built-in method startswith of str object at 0x7f5ffcedb120> = "error: unexpected argument '-p=.' found\nError: unexpected argument '-p=.' found\nunknown flag: unexpected argument '-p=.' f
  >  +      where "error: unexpected argument '-p=.' found\nError: unexpected argument '-p=.' found\nunknown flag: unexpected argument '-p=.' found\nUnknown flag: unexpected argument '-p=.' found\nUsage: 
  >  +        where <built-in method lstrip of str object at 0x7f5ffcedb120> = "error: unexpected argument '-p=.' found\nError: unexpected argument '-p=.' found\nunknown flag: unexpected argument '-p=.' f
- *(... 19 more in this cluster)*

### `rc_mismatch_got0_want2` — 18 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `eval.tests.test_args_parsing.test_missing_value_for_value_taking_flags_shows_usage_and_message[args0-Expected a following arg for flag nonexistent-flag]`
  > assert 0 == 2
- `eval.tests.test_args_parsing.test_missing_value_for_value_taking_flags_shows_usage_and_message[args1-Unknown flag: --nonexistent-flag]`
  > assert 0 == 2
- `eval.tests.test_args_parsing.test_missing_value_for_value_taking_flags_shows_usage_and_message[args2-Expected a following arg for flag p]`
  > assert 0 == 2
- *(... 15 more in this cluster)*

### `rc_mismatch_got0_want1` — 16 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `eval.tests.test_args_parsing.test_invalid_git_arg_value_is_rejected_with_specific_message`
  > assert 0 == 1
- `eval.tests.test_args_parsing.test_screen_mode_accepts_allowed_values_but_program_fails_later_without_tty[normal]`
  > assert 0 == 1
- `eval.tests.test_args_parsing.test_screen_mode_accepts_allowed_values_but_program_fails_later_without_tty[half]`
  > assert 0 == 1
- *(... 13 more in this cluster)*

### `uncategorized` — 11 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_help_output.test_help_has_program_name_header`
  > StopIteration
- `tests.test_harvest_branch.test_rebase_and_drop`
  > Exception: Command failed: ('git', 'log', '-10', '--format=%s', 'current-branch')
  > stdout: 
  > stderr: fatal: ambiguous argument 'current-branch': unknown revision or path not in the working tree.
  > Use '--' to separate paths from revisions, like this:
  > 'git <command> [<revision>...] -- [<file>...]'
- `tests.test_harvest_commit_rebase.test_commit_rebase_discard_old_file_changes`
  > RuntimeError: Git command failed: ['commit', '-m', 'remove four files from this commit']
- *(... 8 more in this cluster)*

### `returned_none` — 7 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_output.test_help_usage_line_mentions_git_arg`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7fd425a76680>('^\\s*executable\\s+\\[git-arg\\]\\s*$', '', re.MULTILINE)
  >  +    where <function search at 0x7fd425a76680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- `eval.tests.test_help_output.test_help_lists_flags_section`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7fd425a76680>('^\\s*flags:\\s*$', '', re.MULTILINE)
  >  +    where <function search at 0x7fd425a76680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- `eval.tests.test_cli_io.test_version_flag_format_and_exit_0`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7fc87e8f2680>('\\bcommit=[0-9a-f]{7,40}\\b', '')
  >  +    where <function search at 0x7fc87e8f2680> = re.search
- *(... 4 more in this cluster)*

### `bytes_output_mismatch` — 3 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_daemon_comprehensive.test_daemon_exit_immediately_clean_exit`
  > assert b"error: the ...nformation.\n" == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'error: the following required arguments were not provided: <PATTERN>\nErr'
  >   +  b'or: the following required arguments were not provided: <PATTERN>\nunknow'
  >   +  b'n flag: the following required arguments were not provided: <PATTERN>\nUn'
  >   +  b'known flag: the following required arguments were not provided: <PATTERN'...
- `tests.test_daemon_comprehensive.test_daemon_exit_immediately_with_extra_fields`
  > assert b"error: the ...nformation.\n" == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'error: the following required arguments were not provided: <PATTERN>\nErr'
  >   +  b'or: the following required arguments were not provided: <PATTERN>\nunknow'
  >   +  b'n flag: the following required arguments were not provided: <PATTERN>\nUn'
  >   +  b'known flag: the following required arguments were not provided: <PATTERN'...
- `eval.tests.test_cli_io.test_use_config_dir_overrides_print_config_dir`
  > assert b"error: unex...nformation.\n" == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b"error: unexpected argument '-ucd' found\nError: unexpected argument '-ucd"
  >   +  b"' found\nunknown flag: unexpected argument '-ucd' found\nUnknown flag: une"
  >   +  b"xpected argument '-ucd' found\n\nUsage: lazygit [OPTIONS] [ARGS]...\nUSAGE:"
  >   +  b' lazygit [OPTIONS] [ARGS]...\nusage: lazygit [OPTIONS] [ARGS]...\n\nFor mor'

### `rc_mismatch_got1_want2` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_args_parsing.test_missing_value_for_value_taking_flags_shows_usage_and_message[args3-Expected a following arg for flag path]`
  > assert 1 == 2

### `rc_mismatch_got1_want0` — 1 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `eval.tests.test_args_parsing.test_double_dash_is_respected_and_allows_dash_prefixed_work_tree_value`
  > assert 1 == 0

