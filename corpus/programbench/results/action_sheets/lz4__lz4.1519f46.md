# Action Sheet — lz4__lz4.1519f46

**Current:** 5.49%  (99/1804)
**Pass / Fail / Skip:** 99 / 1013 / 2
**Gap to 100%:** 94.51 percentage points (1705 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_frames.test_sparse_decompress`
  - reason: --sparse decompression flag not supported by gold executable
- `tests.test_frames.test_sparse_block_sizes`
  - reason: --sparse decompression flag not supported by gold executable

## Failure clusters

1013 failed tests grouped into 17 buckets (sorted by count).

### `rc_mismatch_got2_want0` — 431 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_additional_coverage.test_fast_with_high_value`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/eval/tests/../../executable', '--fast=100', '/tmp/tmpda_4o2cq/input.txt', '/tmp/tmpda_4o2cq/output.lz4'], returncode=2, stdout=b'', stderr=b"lz4: unkno
- `tests.test_additional_coverage.test_block_size_custom_bytes`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/eval/tests/../../executable', '-B1024', '/tmp/tmpb5ktmpuf/input.txt', '/tmp/tmpb5ktmpuf/output.lz4'], returncode=2, stdout=b'', stderr=b"lz4: unknown o
- `tests.test_additional_coverage.test_block_size_large_custom`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/eval/tests/../../executable', '-B8192', '/tmp/tmpkak64zyf/input.txt', '/tmp/tmpkak64zyf/output.lz4'], returncode=2, stdout=b'', stderr=b"lz4: unknown o
- *(... 428 more in this cluster)*

### `other_assertion` — 249 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_additional_coverage.test_force_write_to_stdout_explicit`
  > assert 1328 < 1300
  >  +  where 1328 = len(b'\x04"M\x18`\x00\x00\x00 \x05\x00\x80\xf0\xefForce stdout\nForce stdout\nForce stdout\nForce stdout\nForce stdout\nForce stdout\nForce stdout\nForce stdout\nForce stdout\nForce s
  >  +    where b'\x04"M\x18`\x00\x00\x00 \x05\x00\x80\xf0\xefForce stdout\nForce stdout\nForce stdout\nForce stdout\nForce stdout\nForce stdout\nForce stdout\nForce stdout\nForce stdout\nForce stdout\nFo
  >  +  and   1300 = os.stat_result(st_mode=33188, st_ino=5240654, st_dev=71, st_nlink=1, st_uid=0, st_gid=0, st_size=1300, st_atime=1779060529, st_mtime=1779060529, st_ctime=1779060529).st_size
  >  +    where os.stat_result(st_mode=33188, st_ino=5240654, st_dev=71, st_nlink=1, st_uid=0, st_gid=0, st_size=1300, st_atime=1779060529, st_mtime=1779060529, st_ctime=1779060529) = stat()
  >  +      where stat = PosixPath('/tmp/tmpcpn08b73/input.txt').stat
- `tests.test_basic_invocation.test_help_short`
  > AssertionError: assert b'Usage' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/eval/tests/../../executable', '-h'], returncode=0, stdout=b'lz4 0.1.0 - LZ4 compression tool\n\nUsage: lz4 [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help
- `tests.test_basic_invocation.test_help_long`
  > AssertionError: assert b'Usage' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/eval/tests/../../executable', '--help'], returncode=0, stdout=b'lz4 0.1.0 - LZ4 compression tool\n\nUsage: lz4 [OPTIONS] [ARGS]\n\nOptions:\n  -h, --
- *(... 246 more in this cluster)*

### `rc_mismatch_got1_want0` — 145 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_additional_coverage.test_compress_level_10`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/eval/tests/../../executable', '-10', '/tmp/tmplct7zwgd/input.txt', '/tmp/tmplct7zwgd/output.lz4'], returncode=1, stdout=b'', stderr=b'lz4: /tmp/tmplct7
- `tests.test_additional_coverage.test_compress_level_11`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/eval/tests/../../executable', '-11', '/tmp/tmpjt97_lce/input.txt', '/tmp/tmpjt97_lce/output.lz4'], returncode=1, stdout=b'', stderr=b'lz4: /tmp/tmpjt97
- `tests.test_additional_coverage.test_compression_level_2_through_8`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/eval/tests/../../executable', '-2', '/tmp/tmplkr8zivd/input2.txt', '/tmp/tmplkr8zivd/output2.lz4'], returncode=1, stdout=b'', stderr=b'lz4: /tmp/tmplkr
- *(... 142 more in this cluster)*

### `subprocess_failed` — 69 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_compress.test_basic_compression_file_to_file`
  > subprocess.CalledProcessError: Command '['/workspace/executable', '/workspace/eval/test_resources/test_compress/small_text.txt', '/tmp/pytest-of-root/pytest-0/test_basic_compression_file_to2/output.lz
- `tests.test_compress.test_compression_with_explicit_output_name`
  > subprocess.CalledProcessError: Command '['/workspace/executable', '/workspace/eval/test_resources/test_compress/medium_text.txt', '/tmp/pytest-of-root/pytest-0/test_compression_with_explicit2/custom_n
- `tests.test_compress.test_compress_to_stdout`
  > subprocess.CalledProcessError: Command '['/workspace/executable', '-d', '/tmp/pytest-of-root/pytest-0/test_compress_to_stdout2/from_stdout.lz4', '/tmp/pytest-of-root/pytest-0/test_compress_to_stdout2/
- *(... 66 more in this cluster)*

### `missing_file` — 38 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_additional_coverage.test_test_mode_with_corrupted_data`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpk6awp28c/output.lz4'
- `tests.test_decompression.test_decompress_stdin_to_stdout`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpomoptn9a/compressed.lz4'
- `tests.test_list_mode.test_list_from_stdin`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpr4vy6dsk/compressed.lz4'
- *(... 35 more in this cluster)*

### `boolean_false` — 17 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_compression.test_compress_force_overwrite`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmp8r72ace_/output.lz4').exists
- `eval.tests.test_help_usage.test_h_and_H_share_same_prefix`
  > assert False
  >  +  where False = <built-in method startswith of str object at 0x7f03461bdce0>('lz4 0.1.0 - LZ4 compression tool\n\nUsage: lz4 [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --versio
  >  +    where <built-in method startswith of str object at 0x7f03461bdce0> = "lz4: unknown option: -H\nusage: lz4 [OPTIONS] [ARGS]\nTry 'lz4 --help' for more information.\n".startswith
  >  +      where "lz4: unknown option: -H\nusage: lz4 [OPTIONS] [ARGS]\nTry 'lz4 --help' for more information.\n" = combined_output(CompletedProcess(args=['/workspace/executable', '-H'], returncode=2, st
  >  +    and   'lz4 0.1.0 - LZ4 compression tool\n\nUsage: lz4 [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -c             Write to stdout\n  -d           
- `eval.tests.test_lz4_io.test_help_to_stdout_and_exit0`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of bytes object at 0x7f2b711be010>(b'*** lz4')
  >  +    where <built-in method startswith of bytes object at 0x7f2b711be010> = (b'lz4 0.1.0 - LZ4 compression tool\n\nUsage: lz4 [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --versio
  >  +      where b'lz4 0.1.0 - LZ4 compression tool\n\nUsage: lz4 [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -c             Write to stdout\n  -d        
  >  +      and   b'' = CompletedProcess(args=['/workspace/executable', '--help'], returncode=0, stdout=b'lz4 0.1.0 - LZ4 compression tool\n\nUsage: lz4 [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Prin
- *(... 14 more in this cluster)*

### `bytes_output_mismatch` — 16 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_edge_cases_comprehensive.TestStdinStdoutEdgeCases.test_decompress_stdin_to_stdout`
  > AssertionError: assert b'' == b'Decompress ...press stdin\n'
  >   
  >   Full diff:
  >   + b''
  >   - (b'Decompress stdin\nDecompress stdin\nDecompress stdin\nDecompress stdin\nDeco'
  >   -  b'mpress stdin\nDecompress stdin\nDecompress stdin\nDecompress stdin\nDecompre'
  >   -  b'ss stdin\nDecompress stdin\nDecompress stdin\nDecompress stdin\nDecompress s'
  >   -  b'tdin\nDecompress stdin\nDecompress stdin\nDecompress stdin\nDecompress stdin'...
- `tests.test_frames.test_pipe_console_compat`
  > AssertionError: assert b'Hello World !' == b'Hello World !\n'
  >   
  >   Full diff:
  >   - (b'Hello World !\n')
  >   ?                 --
  >   + (b'Hello World !')
- `eval.tests.test_argparse_validation.test_unknown_flag_is_silenced_with_double_q`
  > assert b"lz4: unknow...nformation.\n" == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'lz4: unknown option: -q\nlz4: unknown option: -q\nlz4: unknown option: --d'
  >   +  b"efinitely-not-a-real-flag\nusage: lz4 [OPTIONS] [ARGS]\nTry 'lz4 --help' f"
  >   +  b'or more information.\n')
- *(... 13 more in this cluster)*

### `string_output_mismatch` — 16 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_usage.test_baseline_short_help_matches_fixture_modulo_banner`
  > AssertionError: assert 'lz4 0.1.0 - ...upported)\n\n' == '*** lz4 v<ve...ault : 3s) \n'
  >   
  >   + lz4 0.1.0 - LZ4 compression tool
  >   - *** lz4 v<version> <build> ***
  >   - Usage : 
  >   -       executable [arg] [input] [output] 
  >     
  >   + Usage: lz4 [OPTIONS] [ARGS]...
- `tests.test_alt_names.test_unlz4_override_with_compress_flag`
  > AssertionError: assert '' == 'Compressed f...==> 176.00%\n'
  >   
  >   - Compressed filename will be : {tmpdir}/compress_override.txt.lz4 
  >   - 
  >   - Read : 0 MiB   ==> 176.00%   
  >   -                                                                                
  >   - Compressed 25 bytes into 44 bytes ==> 176.00%
- `tests.test_alt_names.test_lz4cat_multiple_inputs`
  > AssertionError: assert '' == 'First file\nSecond file\n'
  >   
  >   - First file
  >   - Second file
- *(... 13 more in this cluster)*

### `rc_unexpected_zero` — 13 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_error_handling.test_corrupted_file`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/eval/tests/../../executable', '-d', '/tmp/tmpcx7jbbkb/corrupted.lz4', '-c'], returncode=0, stdout=b'Not valid lz4 data at all!', stderr=b'').returncode
- `tests.test_error_handling.test_three_or_more_file_arguments_fails`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/eval/tests/../../executable', '/tmp/tmpnuw56jeb/file1.txt', '/tmp/tmpnuw56jeb/file2.txt', '/tmp/tmpnuw56jeb/file3.txt'], returncode=0, stdout=b'', stde
- `tests.test_test_mode.test_test_mode_invalid_file`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/eval/tests/../../executable', '-t', '/tmp/tmpeqo4f6ap/invalid.lz4'], returncode=0, stdout=b'', stderr=b'shell-init: error retrieving current directory:
- *(... 10 more in this cluster)*

### `returned_none` — 6 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_usage.test_usage_section_present`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f0347fb6680>('^Usage\\s*:\\s*$', 'lz4 0.1.0 - LZ4 compression tool\n\nUsage: lz4 [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Pri
  >  +    where <function search at 0x7f0347fb6680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- `eval.tests.test_help_usage.test_usage_synopsis_line`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f0347fb6680>('^\\s*executable \\[arg\\] \\[input\\] \\[output\\]\\s*$', 'lz4 0.1.0 - LZ4 compression tool\n\nUsage: lz4 [OPTIONS] [ARGS]\n\nOptions:\n  -h, --he
  >  +    where <function search at 0x7f0347fb6680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- `eval.tests.test_help_usage.test_arguments_section_present`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f0347fb6680>('^Arguments\\s*:\\s*$', 'lz4 0.1.0 - LZ4 compression tool\n\nUsage: lz4 [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version 
  >  +    where <function search at 0x7f0347fb6680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- *(... 3 more in this cluster)*

### `rc_mismatch_got2_want1` — 6 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_gaps.test_badusage_fast_flag_empty_value`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--fast='], returncode=2, stdout='', stderr="lz4: unknown option: --fast=\nusage: lz4 [OPTIONS] [ARGS]\nTry 'lz4 --help' for more informat
- `tests.test_cli_gaps.test_badusage_fast_flag_invalid_character`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--fastx'], returncode=2, stdout='', stderr="lz4: unknown option: --fastx\nusage: lz4 [OPTIONS] [ARGS]\nTry 'lz4 --help' for more informat
- `tests.test_cli_gaps.test_badusage_unrecognized_flag`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-Z'], returncode=2, stdout='', stderr="lz4: unknown option: -Z\nusage: lz4 [OPTIONS] [ARGS]\nTry 'lz4 --help' for more information.\n").r
- *(... 3 more in this cluster)*

### `rc_mismatch_got2_want27` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_dict.test_dict_file_not_found`
  > assert 2 == 27
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-D', '/tmp/pytest-of-root/pytest-0/test_dict_file_not_found2/nonexistent.txt', '/tmp/pytest-of-root/pytest-0/test_dict_file_not_found2/in
- `tests.test_dict.test_dict_missing_filename`
  > assert 2 == 27
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-D', '-c'], returncode=2, stdout=b'', stderr=b"lz4: unknown option: -D\nusage: lz4 [OPTIONS] [ARGS]\nTry 'lz4 --help' for more informatio

### `rc_mismatch_got0_want2560` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_decompress.test_decompress_stdout_binary_safe`
  > AssertionError: assert 0 == 2560
  >  +  where 0 = len(b'')

### `rc_mismatch_got1_want26` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_decompress.test_test_mode_exits_on_first_error_multiple_files`
  > AssertionError: assert 1 == 26
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-t', '/workspace/eval/test_resources/test_decompress/corrupted.lz4', '/workspace/eval/test_resources/test_decompress/input.txt.lz4'], ret

### `rc_mismatch_got0_want44` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_decompress.test_decompress_invalid_header`
  > AssertionError: assert 0 == 44
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-d', '/tmp/pytest-of-root/pytest-0/test_decompress_invalid_header2/invalid.lz4'], returncode=0, stdout=b'', stderr=b'').returncode

### `rc_mismatch_got0_want34` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_decompress.test_test_mode_bad_block_checksum`
  > AssertionError: assert 0 == 34
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-t', '/workspace/eval/test_resources/test_decompress/bad_checksum.lz4'], returncode=0, stdout=b'', stderr=b'').returncode

### `rc_mismatch_got2_want40` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_dict.test_dict_stdin_both_dict_and_input_fails`
  > assert 2 == 40
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-D', 'stdin', '-c'], returncode=2, stdout=b'', stderr=b"lz4: unknown option: -D\nusage: lz4 [OPTIONS] [ARGS]\nTry 'lz4 --help' for more i

