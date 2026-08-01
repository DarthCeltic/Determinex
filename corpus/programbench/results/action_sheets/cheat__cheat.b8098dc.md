# Action Sheet — cheat__cheat.b8098dc

**Current:** 14.98%  (46/307)
**Pass / Fail / Skip:** 46 / 260 / 1
**Gap to 100%:** 85.02 percentage points (261 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_errors.test_permission_denied_on_cheatsheet`
  - reason: gold-env-limitation: test runs as root, chmod 0o000 doesn't prevent reads

## Failure clusters

260 failed tests grouped into 13 buckets (sorted by count).

### `string_output_mismatch` — 127 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_completions.test_invalid_shell_error_message`
  > AssertionError: assert '' == 'unsupported ...powershell)\n'
  >   
  >   - unsupported shell: invalid (valid: bash, zsh, fish, powershell)
- `tests.test_completions.test_case_sensitive_shell_names_uppercase`
  > AssertionError: assert '' == 'unsupported ...powershell)\n'
  >   
  >   - unsupported shell: BASH (valid: bash, zsh, fish, powershell)
- `tests.test_completions.test_case_sensitive_shell_names_mixed_case`
  > AssertionError: assert '' == 'unsupported ...powershell)\n'
  >   
  >   - unsupported shell: Bash (valid: bash, zsh, fish, powershell)
- *(... 124 more in this cluster)*

### `other_assertion` — 84 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic.test_invalid_flag`
  > AssertionError: Error message does not match expected: ''
  > assert '' == 'unknown flag...s-not-exist\n'
  >   
  >   - unknown flag: --this-flag-does-not-exist
- `tests.test_clone_installer.test_installer_clone_yes`
  > AssertionError: Config directory should exist
  > assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/pytest-of-root/pytest-0/test_installer_clone_yes2/home/.config/cheat').exists
- `tests.test_clone_installer.test_installer_clone_no`
  > AssertionError: Should NOT see clone message when user declines
  > assert 'Cloning com... cheatsheets' not in 'Would you l...nfig file:\n'
  >   
  >   'Cloning community cheatsheets' is contained here:
  >     Would you like to create one now?
  >     Would you like to download the community cheatsheets?
  >     Cloning community cheatsheets
  >     Created config file:
- *(... 81 more in this cluster)*

### `rc_mismatch_got0_want1` — 16 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_completions.test_empty_shell_name_error`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--completion', ''], returncode=0, stdout=b'# powershell completion for cheat                                -*- shell-script -*-\n\nfunct
- `tests.test_completions.test_very_long_shell_name`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--completion', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
- `tests.test_edit_remove.test_readonly_path_no_writeable`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-e', 'newsheet'], returncode=0, stdout=b'failed to get writeable path: no writeable cheatpaths found\n', stderr=b'').returncode
- *(... 13 more in this cluster)*

### `boolean_false` — 11 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_edit_remove.test_create_new_cheatsheet`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/pytest-of-root/pytest-0/test_create_new_cheatsheet2/cheatsheets/newsheet').exists
- `tests.test_edit_remove.test_create_nested_cheatsheet`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/pytest-of-root/pytest-0/test_create_nested_cheatsheet2/cheatsheets/foo/bar/nested').exists
- `tests.test_edit_remove.test_edit_readonly_sheet_copies_to_writeable`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/pytest-of-root/pytest-0/test_edit_readonly_sheet_copie2/cheatsheets_rw/existing').exists
- *(... 8 more in this cluster)*

### `type_error` — 10 test(s)

**Quick patch ideas:**
- Specific TypeError; check arg types vs expected

**Sample failures:**

- `tests.test_config.test_init_cheatpaths_structure`
  > TypeError: 'NoneType' object is not subscriptable
- `tests.test_config.test_init_has_personal_and_work_paths`
  > TypeError: 'NoneType' object is not subscriptable
- `tests.test_config.test_init_personal_path_is_writable`
  > TypeError: 'NoneType' object is not subscriptable
- *(... 7 more in this cluster)*

### `missing_file` — 3 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_edit_remove.test_visual_env_var_takes_priority`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_visual_env_var_takes_prio2/which_editor'
- `tests.test_edit_remove.test_editor_with_arguments`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_editor_with_arguments2/editor_args'
- `tests.test_edit_remove.test_edit_creates_empty_file_before_editor`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_edit_creates_empty_file_b2/editor_check'

### `empty_list_or_string` — 2 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_config.test_pager_with_pager_env_set`
  > IndexError: list index out of range
- `tests.test_config.test_pager_with_no_pager_on_path`
  > IndexError: list index out of range

### `rc_mismatch_got0_want2` — 2 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_errors.test_empty_cheatpath_directory`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-l'], returncode=0, stdout=b'Would you like to create one now?\nWould you like to download the community cheatsheets?\nCloning community 
- `tests.test_list.test_list_empty_tag_filter`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-l', '-t', ''], returncode=0, stdout=b'title:  file:                                                                 tags:\ndocker  $WORK

### `returned_none` — 1 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_config.test_init_generates_valid_yaml`
  > assert None is not None

### `uncategorized` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_config.test_init_contains_required_sections`
  > AttributeError: 'NoneType' object has no attribute 'get'

### `bytes_output_mismatch` — 1 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_errors.test_binary_file_as_cheatsheet`
  > AssertionError: assert b'' == b'\x00\x01\x0...x0c\r\x0e\x0f'
  >   
  >   Full diff:
  >   - (b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f')
  >   + b''

### `rc_mismatch_got1_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_tags.test_filter_list_by_scripting_tag`
  > AssertionError: assert 1 == 3
  >  +  where 1 = len([''])

### `rc_mismatch_got2_want20` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_update.test_update_large_number_of_repos`
  > AssertionError: assert 2 == 20
  >  +  where 2 = len(['repo1: ok', 'nonrepo: skipped (not a git repository)'])

