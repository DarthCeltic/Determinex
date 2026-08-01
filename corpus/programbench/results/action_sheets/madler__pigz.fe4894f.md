# Action Sheet — madler__pigz.fe4894f

**Current:** 29.83%  (321/1076)
**Pass / Fail / Skip:** 321 / 516 / 2
**Gap to 100%:** 70.17 percentage points (755 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_list_and_test_modes.test_test_mode_corrupt_returns_nonzero`
  - reason: test_test_mode_corrupt_returns_nonzero depends on test_test_mode_valid_returns_zero
- `tests.test_harvest.test_unix_compress_interop`
  - reason: compress utility not available

## Failure clusters

516 failed tests grouped into 17 buckets (sorted by count).

### `other_assertion` — 180 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic.test_version_verbose`
  > AssertionError: assert b'zlib' in b'pigz 2.8\n'
  >  +  where b'pigz 2.8\n' = CompletedProcess(args=['./executable', '-vV'], returncode=0, stdout=b'pigz 2.8\n', stderr=b'').stdout
- `tests.test_compression.test_compress_file_in_place`
  > AssertionError: assert not True
  >  +  where True = exists()
  >  +    where exists = PosixPath('/tmp/tmpapp8fkox/test.txt').exists
- `tests.test_decompression.test_decompress_file_in_place`
  > AssertionError: assert not True
  >  +  where True = exists()
  >  +    where exists = PosixPath('/tmp/tmpprz7ouae/test.txt.gz').exists
- *(... 177 more in this cluster)*

### `rc_mismatch_got22_want0` — 164 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic.test_license_output`
  > assert 22 == 0
  >  +  where 22 = CompletedProcess(args=['./executable', '--license'], returncode=22, stdout=b'', stderr=b"pigz: unknown option: --license\nusage: pigz [OPTIONS] [ARGS]\nTry 'pigz --help' for more inform
- `tests.test_basic.test_license_short`
  > assert 22 == 0
  >  +  where 22 = CompletedProcess(args=['./executable', '-L'], returncode=22, stdout=b'', stderr=b"pigz: unknown option: -L\nusage: pigz [OPTIONS] [ARGS]\nTry 'pigz --help' for more information.\n").ret
- `tests.test_edge_cases.test_very_large_blocksize`
  > assert 22 == 0
  >  +  where 22 = CompletedProcess(args=['./executable', '-b', '512', '-c'], returncode=22, stdout=b'', stderr=b"pigz: unknown option: -b\nusage: pigz [OPTIONS] [ARGS]\nTry 'pigz --help' for more informa
- *(... 161 more in this cluster)*

### `rc_mismatch_got1_want0` — 70 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_decompression.test_test_integrity`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '-t'], returncode=1, stdout=b'', stderr=b'').returncode
- `tests.test_decompression.test_test_integrity_verbose`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '-t', '-v', '/tmp/tmpxu8d4oa1/test.gz'], returncode=1, stdout=b'', stderr=b'/tmp/tmpxu8d4oa1/test.gz: invalid compressed data--format violated\n').
- `tests.test_decompression.test_test_integrity_file`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '-t', '/tmp/tmpsmw3cd1_/test.gz'], returncode=1, stdout=b'', stderr=b'/tmp/tmpsmw3cd1_/test.gz: invalid compressed data--format violated\n').return
- *(... 67 more in this cluster)*

### `subprocess_failed` — 20 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_pigz.TestBasicInfo.test_license_output`
  > subprocess.CalledProcessError: Command '['./executable', '--license']' returned non-zero exit status 22.
- `tests.test_pigz.TestCustomSuffix.test_custom_suffix`
  > subprocess.CalledProcessError: Command '['./executable', '-S', '.custom', '/tmp/pytest-of-root/pytest-0/test_custom_suffix2/test_suffix.txt']' returned non-zero exit status 22.
- `tests.test_pigz.TestFormats.test_decompress_zlib`
  > subprocess.CalledProcessError: Command '['./executable', '-z', '-d', '-c']' returned non-zero exit status 1.
- *(... 17 more in this cluster)*

### `boolean_false` — 19 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_compression.test_multiple_files`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmp9li6lg7h/file2.txt.gz').exists
- `tests.test_formats.test_zlib_file_extension`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpdwekavlt/test.txt.zz').exists
- `tests.test_advanced_features.test_compress_from_directory_with_files`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmppxwzydob/file2.txt.gz').exists
- *(... 16 more in this cluster)*

### `string_output_mismatch` — 12 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_output.test_help_is_printed_to_stderr_for_this_program`
  > AssertionError: assert 'pigz 2.8\npa...mpression\n\n' == ''
  >   
  >   + pigz 2.8
  >   + parallel implementation of gzip
  >   + 
  >   + Usage: pigz [OPTIONS] [ARGS]
  >   + 
  >   + Options:...
- `eval.tests.test_help_output.test_help_has_usage_header`
  > AssertionError: assert 'pigz 2.8' == 'Usage: pigz ...] [files ...]'
  >   
  >   - Usage: pigz [options] [files ...]
  >   + pigz 2.8
- `eval.tests.test_help_output.test_baseline_full_help_output_matches_fixture_exactly`
  > AssertionError: assert 'pigz 2.8\npa...mpression\n\n' == 'Usage: pigz ...ed as files\n'
  >   
  >   - Usage: pigz [options] [files ...]
  >   -   will compress files in place, adding the suffix '.gz'. If no files are
  >   -   specified, stdin will be compressed to stdout. pigz does what gzip does,
  >   -   but spreads the work over multiple processors and cores when compressing.
  >   + pigz 2.8
  >   + parallel implementation of gzip...
- *(... 9 more in this cluster)*

### `rc_mismatch_got0_want1` — 11 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_compression.test_skip_existing_gz_without_force_flag`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/tmp/pytest-of-root/pytest-0/test_skip_existing_gz_without_2/test.txt'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_compression.test_symlink_skipped_without_force`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/tmp/pytest-of-root/pytest-0/test_symlink_skipped_without_f2/link.txt'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_compression.test_multiple_files_with_one_failing`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-k', '/tmp/pytest-of-root/pytest-0/test_multiple_files_with_one_f2/good1.txt', '/tmp/pytest-of-root/pytest-0/test_multiple_files_with_one
- *(... 8 more in this cluster)*

### `uncategorized` — 8 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_pigz.TestFormats.test_zlib_format`
  > zlib.error: Error -3 while decompressing data: incorrect header check
- `tests.test_formats.test_zlib_stdin_stdout`
  > zlib.error: Error -3 while decompressing data: incorrect header check
- `tests.test_formats.test_zlib_different_compression_levels`
  > zlib.error: Error -3 while decompressing data: incorrect header check
- *(... 5 more in this cluster)*

### `rc_mismatch_got0_want22` — 7 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_argparse_validation.test_missing_required_value_after_flag[-p]`
  > AssertionError: assert 0 == 22
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-p'], returncode=0, stdout=b'\x1f\x8b\x08\x006P\nj\x00\xff\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00', stderr=b'').returncode
- `eval.tests.test_argparse_validation.test_processes_validation[args0-invalid number of processes: 0]`
  > AssertionError: assert 0 == 22
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-p', '0'], returncode=0, stdout=b'\x1f\x8b\x08\x00AP\nj\x00\xff\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00', stderr=b'').returncode
- `eval.tests.test_argparse_validation.test_processes_validation[args1-missing parameter after -p]`
  > AssertionError: assert 0 == 22
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-p', '-1'], returncode=0, stdout=b'\x1f\x8b\x08\x00CP\nj\x00\xff\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00', stderr=b'').returncode
- *(... 4 more in this cluster)*

### `bytes_output_mismatch` — 6 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_formats.test_zlib_format`
  > AssertionError: assert b'\x1f' == b'x'
  >   
  >   At index 0 diff: b'\x1f' != b'x'
  >   
  >   Full diff:
  >   - b'x'
  >   + b'\x1f'
- `tests.test_verbose_quiet.test_quiet_on_error`
  > AssertionError: assert b'pigz: nonex...r directory\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'pigz: nonexistent.gz: No such file or directory\n')
- `eval.tests.test_cli_outputs.test_help_exact`
  > AssertionError: assert b'pigz 2.8\np...mpression\n\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'pigz 2.8\nparallel implementation of gzip\n\nUsage: pigz [OPTIONS] [ARG'
  >   +  b'S]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print vers'
  >   +  b'ion\n  -0 to -9       Compression level (default 6)\n  -c, --stdout   Writ'
  >   +  b'e to stdout\n  -d, --decompress  Decompress\n  -f, --force    Force overwr'...
- *(... 3 more in this cluster)*

### `rc_mismatch_got2_want0` — 4 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_basic.test_no_args_stdin_compression`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable'], returncode=2, stdout=b'', stderr=b"usage: pigz [OPTIONS] [ARGS]\nTry 'pigz --help' for more information.\n").returncode
- `eval.tests.test_stdin_stdout_roundtrip.test_stdin_compress_to_stdout_and_roundtrip_decompress`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b"usage: pigz [OPTIONS] [ARGS]\nTry 'pigz --help' for more information.\n").returncode
- `tests.test_compression.test_stdin_compression_to_file`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b"usage: pigz [OPTIONS] [ARGS]\nTry 'pigz --help' for more information.\n").returncode
- *(... 1 more in this cluster)*

### `missing_file` — 4 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_decompression.test_decompress_multiple_files`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmplqsrhl85/file2'
- `tests.test_decompression.test_unpigz_decompresses_by_default`
  > FileNotFoundError: [Errno 2] No such file or directory: '/workspace/unpigz'
- `tests.test_subcommand_dispatch.TestProgramNameDispatch.test_decompress_via_unpigz_name`
  > FileNotFoundError: [Errno 2] No such file or directory: '/workspace/unpigz'
- *(... 1 more in this cluster)*

### `rc_unexpected_zero` — 4 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `eval.tests.test_env_config.test_env_options_cannot_include_files_errors`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-c'], returncode=0, stdout=b'\x1f\x8b\x08\x00XP\nj\x00\xff\xcbH\xcd\xc9\xc9\xe7\x02\x00 0:6\x06\x00\x00\x00', stderr=b'').returncode
- `eval.tests.test_env_config.test_env_unknown_option_errors`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-c'], returncode=0, stdout=b'\x1f\x8b\x08\x00ZP\nj\x00\xff\xcbH\xcd\xc9\xc9\xe7\x02\x00 0:6\x06\x00\x00\x00', stderr=b'').returncode
- `eval.tests.test_env_config.test_env_missing_parameter_errors`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-c'], returncode=0, stdout=b'\x1f\x8b\x08\x00\\P\nj\x00\xff\xcbH\xcd\xc9\xc9\xe7\x02\x00 0:6\x06\x00\x00\x00', stderr=b'').returncode
- *(... 1 more in this cluster)*

### `rc_mismatch_got31_want120` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_output_formats.test_zlib_format`
  > assert 31 == 120
- `tests.test_output_formats.test_zlib_format_long_flag`
  > assert 31 == 120
- `tests.test_formats.test_zlib_header_format`
  > assert 31 == 120

### `rc_mismatch_got2_want22` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_errors.test_environment_gzip_with_file`
  > assert 2 == 22
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b"usage: pigz [OPTIONS] [ARGS]\nTry 'pigz --help' for more information.\n").returncode
- `tests.test_errors.test_environment_pigz_with_file`
  > assert 2 == 22
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b"usage: pigz [OPTIONS] [ARGS]\nTry 'pigz --help' for more information.\n").returncode

### `rc_mismatch_got49_want0` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_pigz.TestVerbosity.test_quiet_mode`
  > AssertionError: assert 49 == 0
  >  +  where 49 = len(b'pigz: nonexistent.txt: No such file or directory\n')
  >  +    where b'pigz: nonexistent.txt: No such file or directory\n' = CompletedProcess(args=['./executable', '-q', 'nonexistent.txt'], returncode=1, stdout=b'', stderr=b'pigz: nonexistent.txt: No such f

### `rc_mismatch_got1779061286_want1705314600` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_metadata.test_time_restoration_on_decompression`
  > assert 1779061286 == 1705314600

