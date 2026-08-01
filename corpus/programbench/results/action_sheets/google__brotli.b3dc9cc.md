# Action Sheet — google__brotli.b3dc9cc

**Current:** 4.4%  (42/955)
**Pass / Fail / Skip:** 42 / 472 / 0
**Gap to 100%:** 95.60 percentage points (913 tests)

## Failure clusters

472 failed tests grouped into 13 buckets (sorted by count).

### `other_assertion` — 221 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_brotli.TestBasicInvocation.test_help_short_goes_to_stderr`
  > AssertionError: assert b'Usage:' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', '-h'], returncode=0, stdout=b'brotli 0.1.0 - bootstrap scaffold\n\nUsage: brotli [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print he
- `tests.test_brotli.TestBasicInvocation.test_help_long_goes_to_stderr`
  > AssertionError: assert b'Usage:' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', '--help'], returncode=0, stdout=b'brotli 0.1.0 - bootstrap scaffold\n\nUsage: brotli [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Prin
- `tests.test_brotli.TestBasicInvocation.test_help_mentions_coalesced_options`
  > AssertionError: assert (b'coalesced' in b'' or b'-9kf' in b'')
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', '--help'], returncode=0, stdout=b'brotli 0.1.0 - bootstrap scaffold\n\nUsage: brotli [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Prin
  >  +  and   b'' = CompletedProcess(args=['/workspace/executable', '--help'], returncode=0, stdout=b'brotli 0.1.0 - bootstrap scaffold\n\nUsage: brotli [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Prin
- *(... 218 more in this cluster)*

### `bytes_output_mismatch` — 94 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_brotli.TestStdinInput.test_compress_from_stdin_roundtrip`
  > AssertionError: assert b'' == b'Hello, worl... compression.'
  >   
  >   Full diff:
  >   - (b'Hello, world! This is test data for brotli compression.')
  >   + b''
- `tests.test_brotli.TestStdinInput.test_compress_from_explicit_dash_stdin`
  > AssertionError: assert b'' == b'Test with explicit stdin'
  >   
  >   Full diff:
  >   - (b'Test with explicit stdin')
  >   + b''
- `tests.test_brotli.TestStdinInput.test_stdin_binary_data_roundtrip`
  > assert b'' == b'\x00\x01\x0...c\xfd\xfe\xff'
  >   
  >   Full diff:
  >   + b''
  >   - (b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13'
  >   -  b'\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./01234567'
  >   -  b'89:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\x7f'
  >   -  b'\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f'...
- *(... 91 more in this cluster)*

### `rc_mismatch_got2_want0` — 61 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_brotli.TestBasicInvocation.test_no_args_with_piped_stdin`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b"usage: brotli [OPTIONS] [ARGS]\nTry 'brotli --help' for more information.\n").returncode
- `tests.test_brotli.TestOutputOptions.test_output_file_flag_long_equals`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--output=/tmp/tmp8g4m0n_x/output.br', '/tmp/tmp8g4m0n_x/input.txt'], returncode=2, stdout=b'', stderr=b"brotli: unknown option: --output=
- `tests.test_brotli.TestRemoveSource.test_compress_rm_removes_source_and_valid_output`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-j', '/tmp/tmphkrcugx9/test.txt'], returncode=2, stdout=b'', stderr=b"brotli: unknown option: -j\nusage: brotli [OPTIONS] [ARGS]\nTry 'br
- *(... 58 more in this cluster)*

### `rc_mismatch_got2_want1` — 33 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_edge_cases.test_duplicate_no_copy_stat_option`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['./executable', '-n', '-n'], returncode=2, stdout=b'', stderr=b"brotli: unknown option: -n\nusage: brotli [OPTIONS] [ARGS]\nTry 'brotli --help' for more informatio
- `tests.test_cli_edge_cases.test_duplicate_squash_option`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['./executable', '-s', '-s'], returncode=2, stdout=b'', stderr=b"brotli: unknown option: -s\nusage: brotli [OPTIONS] [ARGS]\nTry 'brotli --help' for more informatio
- `tests.test_cli_edge_cases.test_duplicate_concatenated_option`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['./executable', '-K', '-K'], returncode=2, stdout=b'', stderr=b"brotli: unknown option: -K\nusage: brotli [OPTIONS] [ARGS]\nTry 'brotli --help' for more informatio
- *(... 30 more in this cluster)*

### `rc_unexpected_zero` — 28 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_brotli.TestFileDecompression.test_decompress_suffix_mismatch_error`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-d', '/tmp/tmpe2j996bu/test.txt'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_brotli.TestOutputOptions.test_output_with_multiple_files_fails`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-o', '/tmp/tmpg6bmftpn/out.br', '/tmp/tmpg6bmftpn/a.txt', '/tmp/tmpg6bmftpn/b.txt'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_brotli.TestCompressionQuality.test_quality_invalid_too_high`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-q', '12', '-c'], returncode=0, stdout=b'\x0b\x02\x00t\x00e\x00s\x00t', stderr=b'').returncode
- *(... 25 more in this cluster)*

### `rc_mismatch_got0_want1` — 25 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_cli_edge_cases.test_duplicate_quality_option`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', '-q', '5', '-q', '6'], returncode=0, stdout=b'\x0b\x02\x00t\x00e\x00s\x00t', stderr=b'').returncode
- `tests.test_cli_edge_cases.test_duplicate_stdout_option`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', '-c', '-c'], returncode=0, stdout=b'\x0b\x02\x00t\x00e\x00s\x00t', stderr=b'').returncode
- `tests.test_cli_edge_cases.test_duplicate_decompress_command`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', '-d', '-d'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 22 more in this cluster)*

### `missing_file` — 2 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_brotli.TestFileCompression.test_compress_large_text_file_smaller`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpc6n60ha6/large.txt.br'
- `tests.test_brotli.TestMultipleInputFiles.test_decompress_multiple_files`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmp5cplf8q3/a'

### `rc_mismatch_got1_want0` — 2 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_brotli.TestMultipleInputFiles.test_multiple_files_roundtrip`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-d', '-f', '/tmp/tmp1sjdgb8t/first.txt.br', '/tmp/tmp1sjdgb8t/second.txt.br'], returncode=1, stdout=b'', stderr=b'brotli: /tmp/tmp1sjdgb8
- `tests.test_errors.test_empty_string_argument`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', ''], returncode=1, stdout=b'', stderr=b'brotli: : No such file or directory\n').returncode

### `boolean_false` — 2 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_compress_decompress.test_invalid_window_size_below_minimum`
  > assert False
  >  +  where False = <built-in method startswith of str object at 0x7f90713839b0>('lgwin parameter (9) smaller than the minimum (10)')
  >  +    where <built-in method startswith of str object at 0x7f90713839b0> = "brotli: unknown option: -w\nusage: brotli [OPTIONS] [ARGS]\nTry 'brotli --help' for more information.\n".startswith
  >  +      where "brotli: unknown option: -w\nusage: brotli [OPTIONS] [ARGS]\nTry 'brotli --help' for more information.\n" = <built-in method decode of bytes object at 0x7f9070f0b6c0>()
  >  +        where <built-in method decode of bytes object at 0x7f9070f0b6c0> = b"brotli: unknown option: -w\nusage: brotli [OPTIONS] [ARGS]\nTry 'brotli --help' for more information.\n".decode
  >  +          where b"brotli: unknown option: -w\nusage: brotli [OPTIONS] [ARGS]\nTry 'brotli --help' for more information.\n" = CompletedProcess(args=['./executable', '-w', '9', '-c'], returncode=2, st
- `tests.test_compress_decompress.test_invalid_window_size_above_maximum`
  > assert False
  >  +  where False = <built-in method startswith of str object at 0x7f90713832d0>('error parsing lgwin value [25]')
  >  +    where <built-in method startswith of str object at 0x7f90713832d0> = "brotli: unknown option: -w\nusage: brotli [OPTIONS] [ARGS]\nTry 'brotli --help' for more information.\n".startswith
  >  +      where "brotli: unknown option: -w\nusage: brotli [OPTIONS] [ARGS]\nTry 'brotli --help' for more information.\n" = <built-in method decode of bytes object at 0x7f9070f0b870>()
  >  +        where <built-in method decode of bytes object at 0x7f9070f0b870> = b"brotli: unknown option: -w\nusage: brotli [OPTIONS] [ARGS]\nTry 'brotli --help' for more information.\n".decode
  >  +          where b"brotli: unknown option: -w\nusage: brotli [OPTIONS] [ARGS]\nTry 'brotli --help' for more information.\n" = CompletedProcess(args=['./executable', '-w', '25', '-c'], returncode=2, s

### `string_output_mismatch` — 1 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_cli_edge_cases.test_missing_input_file`
  > AssertionError: assert 'brotli: none...r directory\n' == 'failed to op...r directory\n'
  >   
  >   - failed to open input file [nonexistent_file.txt]: No such file or directory
  >   + brotli: nonexistent_file.txt: No such file or directory

### `rc_mismatch_got0_want100001` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_decoder_edge_cases.test_large_100k_input`
  > AssertionError: assert 0 == 100001
  >  +  where 0 = len(b'')
  >  +    where b'' = CompletedProcess(args=['./executable', '-d'], returncode=0, stdout=b'', stderr=b'').stdout

### `rc_mismatch_got0_want10001` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_decoder_edge_cases.test_highly_compressible_all_zeros`
  > AssertionError: assert 0 == 10001
  >  +  where 0 = len(b'')
  >  +    where b'' = CompletedProcess(args=['./executable', '-d'], returncode=0, stdout=b'', stderr=b'').stdout

### `rc_mismatch_got0_want256` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_decoder_edge_cases.test_binary_data_all_byte_values`
  > AssertionError: assert 0 == 256
  >  +  where 0 = len(b'')
  >  +    where b'' = CompletedProcess(args=['./executable', '-d'], returncode=0, stdout=b'', stderr=b'').stdout

