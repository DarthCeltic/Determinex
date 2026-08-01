# Action Sheet — lymphatus__caesium-clt.a529b2e

**Current:** 12.45%  (94/755)
**Pass / Fail / Skip:** 94 / 520 / 1
**Gap to 100%:** 87.55 percentage points (661 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_format_support.test_tiff_compression`
  - reason: TIFF has base path computation issue with some file systems

## Failure clusters

520 failed tests grouped into 12 buckets (sorted by count).

### `other_assertion` — 301 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_no_arguments_shows_error`
  > AssertionError: assert b'required arguments were not provided' in b'Usage: caesium-clt [OPTIONS] <INPUT> [OUTPUT]\n'
  >  +  where b'Usage: caesium-clt [OPTIONS] <INPUT> [OUTPUT]\n' = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b'Usage: caesium-clt [OPTIONS] <INPUT> [OUTPUT]\n').std
- `tests.test_basic_invocation.test_help_flag_shows_full_help`
  > AssertionError: assert b'fast and efficient' in b'caesium-clt 0.1.0\nUsage: caesium-clt [OPTIONS] <INPUT> [OUTPUT]\n\nOptions:\n  -h, --help            Print help\n  -V, --version         Print versio
  >  +  where b'caesium-clt 0.1.0\nUsage: caesium-clt [OPTIONS] <INPUT> [OUTPUT]\n\nOptions:\n  -h, --help            Print help\n  -V, --version         Print version\n  -v, --verbose         Verbose mod
- `tests.test_basic_invocation.test_version_flag_shows_version`
  > AssertionError: assert b'caesiumclt' in b'caesium-clt 0.1.0\n'
  >  +  where b'caesium-clt 0.1.0\n' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'caesium-clt 0.1.0\n', stderr=b'').stdout
- *(... 298 more in this cluster)*

### `rc_mismatch_got2_want0` — 116 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_compression_modes.test_max_size_bytes`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--max-size', '100000', '-o', '/tmp/tmpbvl0z5ry/output', '/workspace/samples/j0.JPG'], returncode=2, stdout=b'', stderr=b'caesium-clt: err
- `tests.test_compression_modes.test_max_size_kb`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--max-size', '100KB', '-o', '/tmp/tmpprlsjqq1/output', '/workspace/samples/j0.JPG'], returncode=2, stdout=b'', stderr=b'caesium-clt: erro
- `tests.test_compression_modes.test_max_size_mb`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--max-size', '0.5MB', '-o', '/tmp/tmp26c9yy6w/output', '/workspace/samples/j0.JPG'], returncode=2, stdout=b'', stderr=b'caesium-clt: erro
- *(... 113 more in this cluster)*

### `boolean_false` — 45 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_additional_formats.test_gif_lossy_compression`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpmk_4olkz/g1.gif').exists
- `tests.test_additional_formats.test_gif_format_conversion`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpdczntpll/output/test.png').exists
- `tests.test_additional_formats.test_gif_to_jpeg`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpbnum8ihc/output/test.jpg').exists
- *(... 42 more in this cluster)*

### `rc_unexpected_zero` — 16 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_error_cases.test_invalid_quality_over_100`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-q', '101', '-o', '/tmp/tmpkqc1mi8u/output', '/workspace/samples/j0.JPG'], returncode=0, stdout=b'Compressed: /workspace/samples/j0.JPG -
- `tests.test_error_cases.test_multiple_compression_modes`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-q', '80', '--lossless', '-o', '/tmp/tmpwkm31esi/output', '/workspace/samples/j0.JPG'], returncode=0, stdout=b'Compressed: /workspace/sam
- `tests.test_input_handling.test_nonexistent_file`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-q', '80', '-o', '/tmp/tmpdvfdmm59/output', 'nonexistent.jpg'], returncode=0, stdout=b'', stderr=b'caesium-clt: error: file not found: 80
- *(... 13 more in this cluster)*

### `missing_file` — 11 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_overwrite_policies.test_overwrite_bigger_policy_keeps_smaller`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpue7cr0c9/output/j0.JPG'
- `tests.test_compression.test_quality_progression_smaller_quality_smaller_size`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_quality_progression_small2/q0/j0.JPG'
- `tests.test_compression.test_lossless_larger_than_quality_mode`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_lossless_larger_than_qual2/lossy/j0.JPG'
- *(... 8 more in this cluster)*

### `string_output_mismatch` — 11 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_executable_cli.test_version_exact_match`
  > AssertionError: assert 'caesium-clt 0.1.0\n' == 'caesiumclt 1.3.0\n'
  >   
  >   - caesiumclt 1.3.0
  >   ?             --
  >   + caesium-clt 0.1.0
  >   ?        +    ++
- `eval.tests.test_executable_cli.test_help_exact_match`
  > AssertionError: assert 'caesium-clt ...JSON output\n' == 'A fast and e...int version\n'
  >   
  >   + caesium-clt 0.1.0
  >   + Usage: caesium-clt [OPTIONS] <INPUT> [OUTPUT]
  >   - A fast and efficient lossy and/or lossless image compression tool
  >   - 
  >   - Usage: executable [OPTIONS] <--quality <QUALITY>|--lossless|--max-size <MAX_SIZE>> <--output <OUTPUT>|--same-folder-as-input> [FILES]...
  >   - ...
- `eval.tests.test_executable_workflows.test_recursive_flag_changes_directory_traversal`
  > AssertionError: assert [] == ['j1.jpg']
  >   
  >   Right contains one more item: 'j1.jpg'
  >   
  >   Full diff:
  >   + []
  >   - [
  >   -     'j1.jpg',
- *(... 8 more in this cluster)*

### `rc_mismatch_got0_want2` — 9 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `eval.tests.test_io_behavior.test_requires_compression_mode_exit2`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-o', '/tmp/tmpyermpito/out', '/tmp/tmpyermpito/in.png'], returncode=0, stdout=b'Compressed: /tmp/tmpyermpito/in.png -> /tmp/tmpyermpito/o
- `eval.tests.test_io_behavior.test_requires_output_destination_exit2`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--lossless', '/tmp/tmpo1vykidy/in.png'], returncode=0, stdout=b'Compressed: /tmp/tmpo1vykidy/in.png -> /tmp/tmpo1vykidy/in.png.compressed
- `eval.tests.test_executable_cli.test_missing_required_mode_errors`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-o', 'out', 'samples/p0.png'], returncode=0, stdout='Compressed: samples/p0.png -> out\n', stderr='').returncode
- *(... 6 more in this cluster)*

### `bytes_output_mismatch` — 3 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_output_control.test_quiet_mode_long_flag`
  > AssertionError: assert (54 == 0 or b'Compressed:...1yxq4n/output' == b''
  >  +  where 54 = len(b'Compressed: samples/j0.JPG -> /tmp/tmpvo1yxq4n/output\n')
  >  +    where b'Compressed: samples/j0.JPG -> /tmp/tmpvo1yxq4n/output\n' = CompletedProcess(args=['./executable', '-q', '80', '--quiet', '-o', '/tmp/tmpvo1yxq4n/output', 'samples/j0.JPG'], returncode=0,
  >   
  >   Full diff:
  >   - b''
  >   + (b'Compressed: samples/j0.JPG -> /tmp/tmpvo1yxq4n/output'))
- `tests.test_output_control.test_verbose_level_0`
  > AssertionError: assert (54 == 0 or b'Compressed:...0urgr_/output' == b''
  >  +  where 54 = len(b'Compressed: samples/j0.JPG -> /tmp/tmpve0urgr_/output\n')
  >  +    where b'Compressed: samples/j0.JPG -> /tmp/tmpve0urgr_/output\n' = CompletedProcess(args=['./executable', '-q', '80', '--verbose', '0', '-o', '/tmp/tmpve0urgr_/output', 'samples/j0.JPG'], return
  >   
  >   Full diff:
  >   - b''
  >   + (b'Compressed: samples/j0.JPG -> /tmp/tmpve0urgr_/output'))
- `tests.test_output_control.test_dry_run_with_quiet`
  > AssertionError: assert (54 == 0 or b'Compressed:...sktbq9/output' == b''
  >  +  where 54 = len(b'Compressed: samples/j0.JPG -> /tmp/tmpwdsktbq9/output\n')
  >  +    where b'Compressed: samples/j0.JPG -> /tmp/tmpwdsktbq9/output\n' = CompletedProcess(args=['./executable', '-q', '80', '-d', '-Q', '-o', '/tmp/tmpwdsktbq9/output', 'samples/j0.JPG'], returncode=0
  >   
  >   Full diff:
  >   - b''
  >   + (b'Compressed: samples/j0.JPG -> /tmp/tmpwdsktbq9/output'))

### `rc_mismatch_got0_want255` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_io_behavior.test_nonexistent_input_exit255_and_error_to_stderr_only`
  > AssertionError: assert 0 == 255
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--lossless', '-o', '/tmp/tmp6tu_cl3x/out', '/tmp/tmp6tu_cl3x/nope.png'], returncode=0, stdout=b'', stderr=b'caesium-clt: error: file not 
- `tests.test_errors.test_non_existent_file`
  > AssertionError: assert 0 == 255
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--quality', '80', '/nonexistent/file.jpg', '-o', '/tmp/pytest-of-root/pytest-0/test_non_existent_file2'], returncode=0, stdout='', stderr
- `tests.test_errors.test_empty_directory_input`
  > assert 0 == 255
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--quality', '80', '/tmp/pytest-of-root/pytest-0/test_empty_directory_input5/empty', '-o', '/tmp/pytest-of-root/pytest-0/test_empty_direct

### `empty_list_or_string` — 2 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_output_control.test_overwrite_policy_all`
  > IndexError: list index out of range
- `tests.test_output_control.test_overwrite_policy_never`
  > IndexError: list index out of range

### `uncategorized` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_file_ops.test_overwrite_policy_all`
  > NotADirectoryError: [Errno 20] Not a directory: '/tmp/pytest-of-root/pytest-0/test_overwrite_policy_all2/overwrite_all/j0.JPG'
- `tests.test_file_ops.test_overwrite_policy_never`
  > NotADirectoryError: [Errno 20] Not a directory: '/tmp/pytest-of-root/pytest-0/test_overwrite_policy_never5/overwrite_never/j0.JPG'

### `returned_none` — 1 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_usage.test_help_has_arguments_section`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f9c69dda680>('^Arguments:\\s*$', 'caesium-clt 0.1.0\nUsage: caesium-clt [OPTIONS] <INPUT> [OUTPUT]\n\nOptions:\n  -h, --help            Print help\n  -V, --vers
  >  +    where <function search at 0x7f9c69dda680> = re.search
  >  +    and   'caesium-clt 0.1.0\nUsage: caesium-clt [OPTIONS] <INPUT> [OUTPUT]\n\nOptions:\n  -h, --help            Print help\n  -V, --version         Print version\n  -v, --verbose         Verbose mo
  >  +    and   re.MULTILINE = re.MULTILINE

