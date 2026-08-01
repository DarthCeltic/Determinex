# Action Sheet — pls-rs__pls.4e1ae50

**Current:** 9.04%  (32/354)
**Pass / Fail / Skip:** 32 / 312 / 6
**Gap to 100%:** 90.96 percentage points (322 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_symlinks.test_symlink_to_inaccessible_path_shows_error`
  - reason: testuser not available - required for symlink error testing
- `tests.test_symlinks.test_symlink_to_path_in_blocked_directory`
  - reason: testuser not available
- `tests.test_symlinks.test_symlink_error_with_detail_fields`
  - reason: testuser not available
- `tests.test_symlinks.test_multiple_symlink_error_types_in_same_directory`
  - reason: testuser not available
- `tests.test_symlinks.test_symlink_error_sorting_with_other_entries`
  - reason: testuser not available
- *(... 1 more skipped)*

## Failure clusters

312 failed tests grouped into 9 buckets (sorted by count).

### `string_output_mismatch` — 176 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_args_output.test_detail_view_long_filename_cell_formatting`
  > AssertionError: assert 'size:\npls: ... 0  visible\n' == '   Size Name...    visible\n'
  >   
  >   -    Size Name
  >   - 0.0   B   café_☕.txt
  >   - 0.0   B   file1.txt
  >   - 0.0   B   file2.txt
  >   - 0.0   B   .hidden1
  >   - 0.0   B   .hidden2...
- `tests.test_args_output.test_unicode_filename_cell_formatting`
  > AssertionError: assert 'perm:\npls: ...ncafé_☕.txt\n' == 'Permissions .../café_☕.txt\n'
  >   
  >   - Permissions Name
  >   + perm:
  >   + pls: cannot access 'perm': No such file or directory
  >   + 
  >   - rw- r-- r--  /workspace/eval/test_resources/test_args_output/stable_dir/café_☕.txt
  >   ? --------------...
- `tests.test_args_output.test_multiple_file_paths_in_args`
  > AssertionError: assert 'src/main.rs:...s:\ncell.rs\n' == '\ue68b src/m...put/cell.rs\n'
  >   
  >   -  src/main.rs
  >   ? --
  >   + src/main.rs:
  >   ?            +
  >   + main.rs
  >   + ...
- *(... 173 more in this cluster)*

### `other_assertion` — 106 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_args_output.test_detail_view_all_fields_single_file`
  > AssertionError: Expected header + 1 data line, got 5
  > assert 5 == 2
  >  +  where 5 = len(['all:', "pls: cannot access 'all': No such file or directory", '', 'README.md:', 'README.md'])
- `tests.test_args_output.test_no_common_ancestor_paths`
  > AssertionError: Expected exactly 2 file entries, got 4
  > assert 4 == 2
  >  +  where 4 = len(['README.md:', 'README.md', '/tmp/pytest-of-root/pytest-0/test_no_common_ancestor_paths2/test_file.txt:', 'test_file.txt'])
- `tests.test_basic.test_absolute_path_file`
  > AssertionError: Absolute path not in output: file1.txt
  >   
  > assert '/tmp/tmp4decmt0y/file1.txt' in 'file1.txt\n'
  >  +  where '/tmp/tmp4decmt0y/file1.txt' = str(PosixPath('/tmp/tmp4decmt0y/file1.txt'))
  >  +    where PosixPath('/tmp/tmp4decmt0y/file1.txt') = absolute()
  >  +      where absolute = PosixPath('/tmp/tmp4decmt0y/file1.txt').absolute
- *(... 103 more in this cluster)*

### `rc_mismatch_got0_want1` — 13 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_perm_exc.test_setuid_bit_without_execute_uppercase_S`
  > assert 0 == 1
  >  +  where 0 = len([])
- `tests.test_perm_exc.test_setgid_bit_with_execute_lowercase_s`
  > assert 0 == 1
  >  +  where 0 = len([])
- `tests.test_perm_exc.test_setgid_bit_without_execute_uppercase_S`
  > assert 0 == 1
  >  +  where 0 = len([])
- *(... 10 more in this cluster)*

### `rc_mismatch_got0_want2` — 11 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_errors.test_invalid_det_flag`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--det=invalid'], returncode=0, stdout='Cargo.lock\nCargo.toml\nLICENSE\nREADME.md\nambr -> /workspace/executable\nambs -> /workspace/exec
- `tests.test_errors.test_invalid_typ_flag`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--typ=badtype'], returncode=0, stdout='Cargo.lock\nCargo.toml\nLICENSE\nREADME.md\nambr -> /workspace/executable\nambs -> /workspace/exec
- `tests.test_errors.test_invalid_unit_flag`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--unit=invalid'], returncode=0, stdout='Cargo.lock\nCargo.toml\nLICENSE\nREADME.md\nambr -> /workspace/executable\nambs -> /workspace/exe
- *(... 8 more in this cluster)*

### `rc_unexpected_zero` — 2 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_sorting.test_sort_inode_reverse_causes_panic`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'eval/test_resources/test_sorting/sample_files', '--sort=inode_', '--det=ino'], returncode=0, stdout='01first.txt\n99bottles.txt\nAlpha.tx
- `tests.test_sorting.test_sort_nlinks_reverse_causes_panic`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'eval/test_resources/test_sorting/sample_files', '--sort=nlinks_', '--det=nlink'], returncode=0, stdout='01first.txt\n99bottles.txt\nAlpha

### `boolean_false` — 1 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_args_output.test_different_root_directories`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7f7b113f40d0>('\n/tmp:\n')
  >  +    where <built-in method startswith of str object at 0x7f7b113f40d0> = '/tmp:\npytest-of-root/\n\n/var/log:\nalternatives.log\napt/\nbootstrap.log\nbtmp\ndpkg.log\nfaillog\nlastlog\nwtmp\n'.starts
  >  +      where '/tmp:\npytest-of-root/\n\n/var/log:\nalternatives.log\napt/\nbootstrap.log\nbtmp\ndpkg.log\nfaillog\nlastlog\nwtmp\n' = CompletedProcess(args=['/workspace/executable', '/tmp', '/var/log

### `empty_list_or_string` — 1 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_detail_meta.test_det_special_permissions_setuid_setgid`
  > IndexError: list index out of range

### `uncategorized` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_detail_meta.test_det_field_order_preserves_command_line_order`
  > ValueError: substring not found

### `rc_mismatch_got5_want2` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_errors.test_multiple_file_paths`
  > AssertionError: assert 5 == 2
  >  +  where 5 = len(['/tmp/tmpidxgdi31/a.txt:', 'a.txt', '', '/tmp/tmpidxgdi31/b.txt:', 'b.txt'])

