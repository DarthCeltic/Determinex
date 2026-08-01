# Action Sheet — tarka__xcp.5e5b448

**Current:** 1.36%  (20/1473)
**Pass / Fail / Skip:** 20 / 821 / 2
**Gap to 100%:** 98.64 percentage points (1453 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_config_gaps.test_ownership_flag_non_root_warning`
  - reason: Test requires non-root execution
- `eval.tests.test_xcp_behavior.test_version_output`
  - reason: test_version_output depends on test_help_output

## Failure clusters

821 failed tests grouped into 13 buckets (sorted by count).

### `missing_file` — 268 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_advanced_options.test_block_size_option`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_block_size_option2/dest.txt'
- `tests.test_advanced_options.test_block_size_megabytes`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_block_size_megabytes2/dest.txt'
- `tests.test_advanced_options.test_reflink_auto`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_reflink_auto2/dest.txt'
- *(... 265 more in this cluster)*

### `other_assertion` — 218 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_help_flag`
  > AssertionError: assert b'Usage: executable [OPTIONS] [PATHS]...' in b''
  >  +  where b'' = CompletedProcess(args=['./executable', '--help'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_basic_invocation.test_help_short_flag`
  > AssertionError: assert b'Usage: executable [OPTIONS] [PATHS]...' in b''
  >  +  where b'' = CompletedProcess(args=['./executable', '-h'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_basic_invocation.test_no_arguments`
  > AssertionError: assert b'Insufficient arguments' in b'Usage: xcp [OPTIONS] <source> <destination>\nCopy files and directories.\n\nOptions:\n  -r, --recursive    Copy directories recursively\n  -v, --v
  >  +  where b'Usage: xcp [OPTIONS] <source> <destination>\nCopy files and directories.\n\nOptions:\n  -r, --recursive    Copy directories recursively\n  -v, --verbose      Verbose output\n  --no-clobber
- *(... 215 more in this cluster)*

### `boolean_false` — 168 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_advanced_options.test_parfile_driver`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/pytest-of-root/pytest-0/test_parfile_driver2/dest.txt').exists
- `tests.test_advanced_options.test_workers_option`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/pytest-of-root/pytest-0/test_workers_option2/dest.txt').exists
- `tests.test_advanced_options.test_workers_auto_detect`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/pytest-of-root/pytest-0/test_workers_auto_detect2/dest.txt').exists
- *(... 165 more in this cluster)*

### `rc_unexpected_zero` — 66 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_directory_operations.test_directory_copy_requires_recursive`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '/tmp/pytest-of-root/pytest-0/test_directory_copy_requires_r2/source', '/tmp/pytest-of-root/pytest-0/test_directory_copy_requires_r2/dest'], return
- `tests.test_edge_cases.test_copy_file_to_itself_different_path`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '/tmp/pytest-of-root/pytest-0/test_copy_file_to_itself_diffe2/file.txt', '/tmp/pytest-of-root/pytest-0/test_copy_file_to_itself_diffe2/file.txt'], 
- `tests.test_error_conditions.test_source_does_not_exist`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '/tmp/pytest-of-root/pytest-0/test_source_does_not_exist2/nonexistent.txt', '/tmp/pytest-of-root/pytest-0/test_source_does_not_exist2/dest.txt'], r
- *(... 63 more in this cluster)*

### `string_output_mismatch` — 51 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_advanced_scenarios.test_empty_backup_option`
  > AssertionError: assert 'old' == 'new'
  >   
  >   - new
  >   + old
- `tests.test_backup_modes.test_backup_none`
  > AssertionError: assert 'old content' == 'new content'
  >   
  >   - new content
  >   + old content
- `tests.test_backup_modes.test_backup_numbered`
  > AssertionError: assert 'old content' == 'new content'
  >   
  >   - new content
  >   + old content
- *(... 48 more in this cluster)*

### `rc_mismatch_got0_want1` — 27 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `eval.tests.test_argparse.test_workers_accepts_zero_and_positive_int[0]`
  > assert 0 == 1
- `eval.tests.test_argparse.test_workers_accepts_zero_and_positive_int[1]`
  > assert 0 == 1
- `eval.tests.test_argparse.test_workers_accepts_zero_and_positive_int[8]`
  > assert 0 == 1
- *(... 24 more in this cluster)*

### `rc_mismatch_got1_want0` — 9 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_advanced_options.test_target_directory_option`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '--target-directory', '/tmp/pytest-of-root/pytest-0/test_target_directory_option2/dest', '/tmp/pytest-of-root/pytest-0/test_target_directory_option
- `tests.test_coverage_improvements.test_target_directory_with_flag`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '--target-directory', '/tmp/pytest-of-root/pytest-0/test_target_directory_with_fla2/target', '/tmp/pytest-of-root/pytest-0/test_target_directory_wi
- `tests.test_coverage_improvements.test_large_block_size`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '--block-size', '1GB', '/tmp/pytest-of-root/pytest-0/test_large_block_size2/source.txt', '/tmp/pytest-of-root/pytest-0/test_large_block_size2/dest.
- *(... 6 more in this cluster)*

### `rc_mismatch_got0_want2` — 5 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `eval.tests.test_argparse.test_workers_negative_is_not_accepted_as_value`
  > assert 0 == 2
- `eval.tests.test_argparse.test_driver_rejects_unknown_value`
  > assert 0 == 2
- `eval.tests.test_argparse.test_reflink_rejects_unknown_value`
  > assert 0 == 2
- *(... 2 more in this cluster)*

### `rc_mismatch_got2_want1` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_harvest.test_no_args`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout='', stderr='Usage: xcp [OPTIONS] <source> <destination>\nCopy files and directories.\n\nOptions:\n  -r, --recursive 
- `eval.tests.test_xcp_behavior.test_no_args_errors`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b'Usage: xcp [OPTIONS] <source> <destination>\nCopy files and directories.\n\nOptions:\n  -r, --recursiv
- `eval.tests.test_externalized.test_ext_no_args`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b'Usage: xcp [OPTIONS] <source> <destination>\nCopy files and directories.\n\nOptions:\n  -r, --recursiv

### `rc_mismatch_got1_want2` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_argparse.test_workers_rejects_non_integer`
  > assert 1 == 2
- `eval.tests.test_argparse.test_block_size_rejects_garbage`
  > assert 1 == 2

### `returned_none` — 2 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_behavior.test_help_has_arguments_section`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7ffac045a680>('^Arguments:\\s*$', '', flags=re.MULTILINE)
  >  +    where <function search at 0x7ffac045a680> = re.search
  >  +    and   '' = CompletedProcess(args=['/workspace/executable', '--help'], returncode=0, stdout='', stderr='').stdout
  >  +    and   re.MULTILINE = re.MULTILINE
- `eval.tests.test_help_behavior.test_help_has_options_section`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7ffac045a680>('^Options:\\s*$', '', flags=re.MULTILINE)
  >  +    where <function search at 0x7ffac045a680> = re.search
  >  +    and   '' = CompletedProcess(args=['/workspace/executable', '--help'], returncode=0, stdout='', stderr='').stdout
  >  +    and   re.MULTILINE = re.MULTILINE

### `bytes_output_mismatch` — 1 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_file_operations.test_overwrite_existing_file`
  > AssertionError: assert b'Old content' == b'New content'
  >   
  >   At index 0 diff: b'O' != b'N'
  >   
  >   Full diff:
  >   - (b'New content')
  >   ?    ^^^
  >   + (b'Old content')

### `rc_mismatch_got0_want100` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_xcp_edge_cases.TestBoundaryConditions.test_directory_with_many_files`
  > AssertionError: assert 0 == 100
  >  +  where 0 = len([])
  >  +    where [] = list(<generator object Path.glob at 0x7f0460b25c40>)
  >  +      where <generator object Path.glob at 0x7f0460b25c40> = glob('*.txt')
  >  +        where glob = PosixPath('/tmp/tmpop05b8kh/many_dest').glob

