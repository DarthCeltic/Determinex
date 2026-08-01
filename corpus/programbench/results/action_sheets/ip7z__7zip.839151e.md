# Action Sheet — ip7z__7zip.839151e

**Current:** 3.0%  (37/1234)
**Pass / Fail / Skip:** 37 / 489 / 0
**Gap to 100%:** 97.00 percentage points (1197 tests)

## Failure clusters

489 failed tests grouped into 11 buckets (sorted by count).

### `other_assertion` — 237 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_7zip.test_help_shows_all_commands`
  > AssertionError: assert b'7-Zip' in b'7zip 0.1.0 - bootstrap scaffold\n\nUsage: 7zip [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n'
  >  +  where b'7zip 0.1.0 - bootstrap scaffold\n\nUsage: 7zip [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['/workspace/executable'
- `tests.test_7zip.test_version_info_in_header`
  > assert b'26.00' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b"usage: 7zip [OPTIONS] [ARGS]\nTry '7zip --help' for more information.\n").stdout
- `tests.test_7zip.test_help_shows_switches`
  > AssertionError: assert b'-mx[N]' in b'7zip 0.1.0 - bootstrap scaffold\n\nUsage: 7zip [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n'
  >  +  where b'7zip 0.1.0 - bootstrap scaffold\n\nUsage: 7zip [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['/workspace/executable'
- *(... 234 more in this cluster)*

### `boolean_false` — 110 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_7zip.test_add_single_file_7z`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpvjvqjcvl/test.7z').exists
- `tests.test_7zip.test_add_with_compression_level_mx1`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmp67g9imdb/test.7z').exists
- `tests.test_7zip.test_add_with_compression_level_mx9`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmp_xi7q2f0/test.7z').exists
- *(... 107 more in this cluster)*

### `missing_file` — 42 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_7zip.test_add_bzip2_format`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpf4gdip0y/test.bz2'
- `tests.test_7zip.test_add_tar_format`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmp3u9yw3v0/test.tar'
- `tests.test_7zip.test_add_xz_format`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpjyyyf7j7/test.xz'
- *(... 39 more in this cluster)*

### `rc_mismatch_got0_want7` — 30 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_7zip.test_invalid_command_returns_error`
  > AssertionError: assert 0 == 7
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'badcmd', 'archive.7z'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_7zip.test_error_invalid_command`
  > AssertionError: assert 0 == 7
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'zzz', 'archive.7z'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_commandline_parsing.test_conflicting_archive_types`
  > assert 0 == 7
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'a', '-t7z', '-tzip', '/tmp/tmph2fnp96p/test.7z', '/tmp/tmph2fnp96p/file.txt'], returncode=0, stdout="b'Everything is Ok'\n", stderr='').r
- *(... 27 more in this cluster)*

### `bytes_output_mismatch` — 23 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_7zip.test_extract_to_stdout_so`
  > assert b"b'Everything is Ok'\n" == b'stdout content\n'
  >   
  >   At index 0 diff: b'b' != b's'
  >   
  >   Full diff:
  >   - (b'stdout content\n')
  >   + (b"b'Everything is Ok'\n")
- `tests.test_7zip.test_extract_to_stdout`
  > assert b"b'Everything is Ok'\n" == b'Extract to stdout test\n'
  >   
  >   At index 0 diff: b'b' != b'E'
  >   
  >   Full diff:
  >   - (b'Extract to stdout test\n')
  >   + (b"b'Everything is Ok'\n")
- `tests.test_advanced_flags.test_scrc_hash_functions_crc32`
  > assert "b'Everything is Ok'\n" == '\n7-Zip (a) ...thing is Ok\n'
  >   
  >   - 
  >   - 7-Zip (a) 26.00 (x64) : Copyright (c) 1999-2026 Igor Pavlov : 2026-02-12
  >   -  64-bit locale=C.UTF-8 Threads:64 OPEN_MAX:1024
  >   - 
  >   - Scanning
  >   - 1 file, 21 bytes (1 KiB)...
- *(... 20 more in this cluster)*

### `rc_mismatch_got0_want2` — 19 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_7zip.test_list_nonexistent_archive`
  > assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'l', '/nonexistent/path/archive.7z'], returncode=0, stdout=b"b'Everything is Ok'\n", stderr=b'').returncode
- `tests.test_7zip.test_error_missing_archive_file`
  > assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'l', '/tmp/nonexistent_archive_xyz.7z'], returncode=0, stdout=b"b'Everything is Ok'\n", stderr=b'').returncode
- `tests.test_7zip.test_error_missing_extract_source`
  > assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'e', '/tmp/nonexistent_xyz.7z', '-o/tmp/', '-y'], returncode=0, stdout=b"b'Everything is Ok'\n", stderr=b'').returncode
- *(... 16 more in this cluster)*

### `rc_unexpected_zero` — 9 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_7zip.test_list_corrupt_archive`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'l', '/tmp/tmpgqd3stf9/corrupt.7z'], returncode=0, stdout=b"b'Everything is Ok'\n", stderr=b'').returncode
- `tests.test_7zip.test_extract_with_wrong_password`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'e', '/tmp/tmp3u4pk6m4/secret.7z', '-o/tmp/tmp3u4pk6m4/dest', '-pWRONG', '-y'], returncode=0, stdout=b"b'Everything is Ok'\n", stderr=b'')
- `tests.test_7zip.test_test_corrupt_archive`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 't', '/tmp/tmpnm0fdls7/corrupt.7z'], returncode=0, stdout=b"b'Everything is Ok'\n", stderr=b'').returncode
- *(... 6 more in this cluster)*

### `rc_mismatch_got0_want1` — 7 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_7zip.test_add_missing_file_with_warning`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'a', '/tmp/tmp3vxseu9r/test.7z', '/tmp/tmp3vxseu9r/exists.txt', '/nonexistent_xyz_file'], returncode=0, stdout=b"b'Everything is Ok'\n", s
- `tests.test_7z_update_advanced.test_update_nonexistent_file_warning`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'u', '/tmp/tmpv5tulwdc/test.7z', '/tmp/tmpv5tulwdc/nonexistent.txt'], returncode=0, stdout="b'Everything is Ok'\n", stderr='').returncode
- `tests.test_advanced_flags.test_sse_exit_code_changes_with_multiple_missing_files`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'a', '-sse', '/tmp/tmpv92_tr30/archive.7z', '/tmp/tmpv92_tr30/exists.txt', '/tmp/tmpv92_tr30/missing1.txt', '/tmp/tmpv92_tr30/missing2.txt
- *(... 4 more in this cluster)*

### `returned_none` — 7 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_cab_format.test_list_multiple_files_cab`
  > AssertionError: assert None == 'Cab'
  >  +  where None = <built-in method get of dict object at 0x7f3daa674400>('Type')
  >  +    where <built-in method get of dict object at 0x7f3daa674400> = {}.get
- `tests.test_cab_format.test_list_cab_with_directory_structure`
  > AssertionError: assert None == 'Cab'
  >  +  where None = <built-in method get of dict object at 0x7f3da9fbb7c0>('Type')
  >  +    where <built-in method get of dict object at 0x7f3da9fbb7c0> = {}.get
- `tests.test_cab_format.test_list_empty_file_cab`
  > AssertionError: assert None == 'Cab'
  >  +  where None = <built-in method get of dict object at 0x7f3daa062000>('Type')
  >  +    where <built-in method get of dict object at 0x7f3daa062000> = {}.get
- *(... 4 more in this cluster)*

### `string_output_mismatch` — 3 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_7zip.test_overwrite_rename_aot`
  > AssertionError: assert 'existing' == 'from archive'
  >   
  >   - from archive
  >   + existing
- `tests.test_extract.test_extract_overwrite_all`
  > AssertionError: assert 'This is exis...e overwritten' == 'This is file... 2 of file1\n'
  >   
  >   + This is existing content that should be overwritten
  >   - This is file1.txt
  >   - Line 2 of file1
- `tests.test_extract.test_extract_auto_rename`
  > AssertionError: assert 'This is existing content' == 'This is file... 2 of file1\n'
  >   
  >   + This is existing content
  >   - This is file1.txt
  >   - Line 2 of file1

### `rc_mismatch_got2_want0` — 2 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_7zip.test_no_args_shows_usage`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b"usage: 7zip [OPTIONS] [ARGS]\nTry '7zip --help' for more information.\n").returncode
- `tests.test_errors.test_no_arguments_shows_help`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout='', stderr="usage: 7zip [OPTIONS] [ARGS]\nTry '7zip --help' for more information.\n").returncode

