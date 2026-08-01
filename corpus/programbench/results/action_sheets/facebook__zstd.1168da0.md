# Action Sheet — facebook__zstd.1168da0

**Current:** 6.85%  (191/2788)
**Pass / Fail / Skip:** 191 / 1502 / 11
**Gap to 100%:** 93.15 percentage points (2597 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_error_paths.test_compress_read_permission_denied`
  - reason: Behavior varies
- `tests.test_error_paths.test_compress_write_permission_denied`
  - reason: Behavior varies
- `tests.test_error_paths.test_compress_symlink`
  - reason: Behavior varies
- `tests.test_error_paths.test_invalid_long_value`
  - reason: Behavior varies
- `tests.test_extended_coverage.test_decompress_multiple_files`
  - reason: Byte formatting issue
- *(... 6 more skipped)*

## Failure clusters

1502 failed tests grouped into 16 buckets (sorted by count).

### `rc_mismatch_got2_want0` — 615 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_01_basic_invocation.test_help_short_flag`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-H'], returncode=2, stdout=b'', stderr=b"zstd: unknown option: -H\nusage: zstd [OPTIONS] [ARGS]\nTry 'zstd --help' for more information.\
- `tests.test_01_basic_invocation.test_no_arguments_with_empty_stdin`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b"usage: zstd [OPTIONS] [ARGS]\nTry 'zstd --help' for more information.\n").returncode
- `tests.test_02_compression.test_compress_to_stdout`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-c', '/tmp/tmpiopyyjq0/sample.txt'], returncode=2, stdout=b'', stderr=b"shell-init: error retrieving current directory: getcwd: cannot ac
- *(... 612 more in this cluster)*

### `other_assertion` — 515 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_01_basic_invocation.test_help_flag`
  > AssertionError: assert b'compress' in b'zstd 0.1.0 - bootstrap scaffold\n\nusage: zstd [options] [args]\n\noptions:\n  -h, --help     print help\n  -v, --version  print version\n'
  >  +  where b'zstd 0.1.0 - bootstrap scaffold\n\nusage: zstd [options] [args]\n\noptions:\n  -h, --help     print help\n  -v, --version  print version\n' = <built-in method lower of bytes object at 0x7f
  >  +    where <built-in method lower of bytes object at 0x7f9ac67e7ec0> = b'zstd 0.1.0 - bootstrap scaffold\n\nUsage: zstd [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Pri
  >  +      where b'zstd 0.1.0 - bootstrap scaffold\n\nUsage: zstd [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['/workspace/executa
- `tests.test_18_error_handling.test_invalid_dictionary_file`
  > assert (b'Dictionary' in b"shell-init: error retrieving current directory: getcwd: cannot access parent directories: No such file or directory\nzstd: unknown option: -D\nusage: zstd [OPTIONS] [ARGS]\n
  >  +  where b"shell-init: error retrieving current directory: getcwd: cannot access parent directories: No such file or directory\nzstd: unknown option: -D\nusage: zstd [OPTIONS] [ARGS]\nTry 'zstd --hel
  >  +  and   b"shell-init: error retrieving current directory: getcwd: cannot access parent directories: No such file or directory\nzstd: unknown option: -D\nusage: zstd [OPTIONS] [ARGS]\nTry 'zstd --hel
  >  +  and   b"shell-init: error retrieving current directory: getcwd: cannot access parent directories: No such file or directory\nzstd: unknown option: -D\nusage: zstd [OPTIONS] [ARGS]\nTry 'zstd --hel
- `tests.test_18_error_handling.test_invalid_compression_level_beyond_ultra`
  > assert (b'Warning' in b"shell-init: error retrieving current directory: getcwd: cannot access parent directories: No such file or directory\nzstd: unknown option: -25\nusage: zstd [OPTIONS] [ARGS]\nTr
  >  +  where b"shell-init: error retrieving current directory: getcwd: cannot access parent directories: No such file or directory\nzstd: unknown option: -25\nusage: zstd [OPTIONS] [ARGS]\nTry 'zstd --he
  >  +  and   b"shell-init: error retrieving current directory: getcwd: cannot access parent directories: No such file or directory\nzstd: unknown option: -25\nusage: zstd [OPTIONS] [ARGS]\nTry 'zstd --he
  >  +  and   b"shell-init: error retrieving current directory: getcwd: cannot access parent directories: No such file or directory\nzstd: unknown option: -25\nusage: zstd [OPTIONS] [ARGS]\nTry 'zstd --he
  >  +  and   2 = CompletedProcess(args=['/workspace/executable', '-25'], returncode=2, stdout=b'', stderr=b"shell-init: error retrieving current directory: getcwd: cannot access parent directories: No su
- *(... 512 more in this cluster)*

### `subprocess_failed` — 201 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_advanced_compression.test_patch_from_d_equivalent_to_patch_apply`
  > subprocess.CalledProcessError: Command '['/workspace/executable', '--patch-from=/workspace/eval/test_resources/test_advanced_compression/reference.bin', '/workspace/eval/test_resources/test_advanced_c
- `tests.test_advanced_compression.test_rsyncable_round_trip_identical`
  > subprocess.CalledProcessError: Command '['/workspace/executable', '--rsyncable', '/tmp/tmpfcufwm3x/input.bin', '-o', '/tmp/tmpfcufwm3x/rsync.zst']' returned non-zero exit status 2.
- `tests.test_dictionaries.test_decompress_without_dictionary_fails`
  > subprocess.CalledProcessError: Command '['/workspace/executable', '-D', '/tmp/pytest-of-root/pytest-0/test_decompress_without_dictio2/dict.zst', '/tmp/pytest-of-root/pytest-0/test_decompress_without_d
- *(... 198 more in this cluster)*

### `boolean_false` — 52 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_02_compression.test_compress_single_file`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpzaxkecm9/sample.txt.zst').exists
- `tests.test_02_compression.test_compress_with_output_flag`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmplwd6uth4/output.zst').exists
- `tests.test_02_compression.test_compress_multiple_files_improved`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpkt2tm_7y/file1.txt.zst').exists
- *(... 49 more in this cluster)*

### `rc_mismatch_got2_want1` — 52 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_args_parsing.test_unknown_flag_errors_and_exit_nonzero[args0]`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--unknown'], returncode=2, stdout=b'', stderr=b"zstd: unknown option: --unknown\nusage: zstd [OPTIONS] [ARGS]\nTry 'zstd --help' for more
- `eval.tests.test_args_parsing.test_unknown_flag_errors_and_exit_nonzero[args1]`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--nonexistent-flag'], returncode=2, stdout=b'', stderr=b"zstd: unknown option: --nonexistent-flag\nusage: zstd [OPTIONS] [ARGS]\nTry 'zst
- `eval.tests.test_args_parsing.test_missing_value_for_o_errors`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-o'], returncode=2, stdout=b'', stderr=b"zstd: unknown option: -o\nusage: zstd [OPTIONS] [ARGS]\nTry 'zstd --help' for more information.\
- *(... 49 more in this cluster)*

### `missing_file` — 26 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_07_dictionaries.test_train_dictionary_basic`
  > FileNotFoundError: [Errno 2] No such file or directory
- `tests.test_07_dictionaries.test_compress_with_dictionary`
  > FileNotFoundError: [Errno 2] No such file or directory
- `tests.test_07_dictionaries.test_decompress_with_dictionary`
  > FileNotFoundError: [Errno 2] No such file or directory
- *(... 23 more in this cluster)*

### `rc_unexpected_zero` — 14 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_02_compression.test_compress_nonexistent_file`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'nonexistent_file_12345.txt'], returncode=0, stdout=b'', stderr=b'shell-init: error retrieving current directory: getcwd: cannot access pa
- `tests.test_18_error_handling.test_nonexistent_file`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'nonexistent_file.txt'], returncode=0, stdout=b'', stderr=b'shell-init: error retrieving current directory: getcwd: cannot access parent d
- `tests.test_18_error_handling.test_read_from_directory`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/tmp/tmpskffd9dg/test_dir'], returncode=0, stdout=b'', stderr=b'shell-init: error retrieving current directory: getcwd: cannot access par
- *(... 11 more in this cluster)*

### `rc_mismatch_got0_want1` — 9 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `eval.tests.test_args_parsing.test_output_equals_form_is_not_supported_for_o`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/tmp/pytest-of-root/pytest-0/test_output_equals_form_is_not2/in.txt', '--output=/tmp/pytest-of-root/pytest-0/test_output_equals_form_is_n
- `eval.tests.test_file_io.test_missing_file_is_error_exit_1_and_message_on_stderr`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'no_such_file'], returncode=0, stdout='', stderr='').returncode
- `tests.test_error_paths_gap.test_compress_dev_null`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/dev/null'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 6 more in this cluster)*

### `string_output_mismatch` — 4 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_advanced_cli.test_test_flag_integrity_check_corrupted`
  > AssertionError: assert 'zstd: unknow...nformation.\n' == '/tmp/test_fi... parameter \n'
  >   
  >   - /tmp/test_fix/corrupted.zst : Decoding error (36) : Unsupported frame parameter 
  >   + zstd: unknown option: --test
  >   + usage: zstd [OPTIONS] [ARGS]
  >   + Try 'zstd --help' for more information.
- `tests.test_benchmark_gap.test_benchmark_decode_only_mode_with_corrupt_data`
  > AssertionError: assert 'zstd: unknow... information.' == 'Error 32 : E...ay be invalid'
  >   
  >   - Error 32 : Error while trying to assess decompressed size: data may be invalid
  >   + zstd: unknown option: -bd
  >   + usage: zstd [OPTIONS] [ARGS]
  >   + Try 'zstd --help' for more information.
- `tests.test_benchmark_gap.test_benchmark_directory_input_error`
  > AssertionError: assert 'zstd: unknow... information.' == 'Error loading files'
  >   
  >   - Error loading files
  >   + zstd: unknown option: -b
  >   + usage: zstd [OPTIONS] [ARGS]
  >   + Try 'zstd --help' for more information.
- *(... 1 more in this cluster)*

### `rc_mismatch_got2_want31` — 4 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_dictionaries.test_missing_dictionary_file_compress`
  > assert 2 == 31
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-D', '/tmp/pytest-of-root/pytest-0/test_missing_dictionary_file_c2/nonexistent.dict', '/workspace/eval/test_resources/test_dictionaries/i
- `tests.test_dictionaries.test_missing_dictionary_file_decompress`
  > assert 2 == 31
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-D', '/tmp/pytest-of-root/pytest-0/test_missing_dictionary_file_d2/nonexistent.dict', '-d', '/workspace/eval/test_resources/test_dictiona
- `tests.test_error_paths_gap.test_dictionary_not_found`
  > assert 2 == 31
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-D', '/nonexistent/dict.dict', '/tmp/pytest-of-root/pytest-0/test_dictionary_not_found2/test.txt'], returncode=2, stdout=b'', stderr=b"zs
- *(... 1 more in this cluster)*

### `rc_mismatch_got2_want14` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_dictionaries.test_train_insufficient_samples`
  > assert 2 == 14
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--train', '/workspace/eval/test_resources/test_dictionaries/sample1.txt', '/workspace/eval/test_resources/test_dictionaries/sample2.txt',
- `tests.test_dictionaries.test_train_with_split_parameter`
  > assert 2 == 14
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--train', '/workspace/eval/test_resources/test_dictionaries/sample1.txt', '/workspace/eval/test_resources/test_dictionaries/sample2.txt',
- `tests.test_error_paths_gap.test_train_too_few_samples`
  > assert 2 == 14
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--train', '/tmp/pytest-of-root/pytest-0/test_train_too_few_samples2/sample.txt'], returncode=2, stdout=b'', stderr=b"zstd: unknown option

### `bytes_output_mismatch` — 3 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `eval.tests.test_zstd_cli.test_version_snapshot`
  > AssertionError: assert b'zstd 0.1.0\n' == b'*** Zstanda... Collet ***\n'
  >   
  >   At index 0 diff: b'z' != b'*'
  >   
  >   Full diff:
  >   - (b'*** Zstandard CLI (64-bit) v1.6.0, by Yann Collet ***\n')
  >   + (b'zstd 0.1.0\n')
- `tests.test_determinism.TestExactOutputMatching.test_version_output_exact`
  > AssertionError: assert b'zstd 0.1.0\n' == b'*** Zstanda... Collet ***\n'
  >   
  >   At index 0 diff: b'z' != b'*'
  >   
  >   Full diff:
  >   - (b'*** Zstandard CLI (64-bit) v1.6.0, by Yann Collet ***\n')
  >   + (b'zstd 0.1.0\n')
- `tests.test_determinism.TestExactOutputMatching.test_version_long_output_exact`
  > AssertionError: assert b'zstd 0.1.0\n' == b'*** Zstanda... Collet ***\n'
  >   
  >   At index 0 diff: b'z' != b'*'
  >   
  >   Full diff:
  >   - (b'*** Zstandard CLI (64-bit) v1.6.0, by Yann Collet ***\n')
  >   + (b'zstd 0.1.0\n')

### `uncategorized` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic.test_version_long`
  > NameError: name 'output' is not defined

### `rc_mismatch_got2_want11` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_parsing_gap.test_short_M_memlimit`
  > assert 2 == 11
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-M100', '-d', '/tmp/pytest-of-root/pytest-0/test_short_M_memlimit2/test.zst'], returncode=2, stdout=b'', stderr=b"zstd: unknown option: -

### `rc_mismatch_got2_want34` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_error_paths_gap.test_dictionary_too_large`
  > assert 2 == 34
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-D', '/tmp/pytest-of-root/pytest-0/test_dictionary_too_large2/huge_dict.dict', '/tmp/pytest-of-root/pytest-0/test_dictionary_too_large2/t

### `rc_mismatch_got2_want15` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_error_paths_gap.test_benchmark_missing_file`
  > assert 2 == 15
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-b', '/nonexistent/file.txt'], returncode=2, stdout=b'', stderr=b"zstd: unknown option: -b\nusage: zstd [OPTIONS] [ARGS]\nTry 'zstd --hel

