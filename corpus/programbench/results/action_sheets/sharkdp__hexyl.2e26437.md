# Action Sheet — sharkdp__hexyl.2e26437

**Current:** 6.93%  (88/1270)
**Pass / Fail / Skip:** 88 / 792 / 16
**Gap to 100%:** 93.07 percentage points (1182 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_hexyl_behavior.test_stdin_equals_file`
  - reason: test_stdin_equals_file depends on test_hex_dump_known_bytes_exact
- `eval.tests.test_hexyl_behavior.test_length_limits_bytes[16-00000000]`
  - reason: test_length_limits_bytes[16-00000000] depends on test_hex_dump_known_bytes_exact
- `eval.tests.test_hexyl_behavior.test_length_limits_bytes[0x10-00000000]`
  - reason: test_length_limits_bytes[0x10-00000000] depends on test_hex_dump_known_bytes_exact
- `eval.tests.test_hexyl_behavior.test_length_limits_bytes[1kiB-00000000]`
  - reason: test_length_limits_bytes[1kiB-00000000] depends on test_hex_dump_known_bytes_exact
- `eval.tests.test_hexyl_behavior.test_skip_positive`
  - reason: test_skip_positive depends on test_hex_dump_known_bytes_exact
- *(... 11 more skipped)*

## Failure clusters

792 failed tests grouped into 7 buckets (sorted by count).

### `rc_mismatch_got2_want0` — 558 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_base_display.test_base_hexadecimal`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--base=hexadecimal', '--color=never'], returncode=2, stdout=b'', stderr=b"hexyl: unknown option: --base=hexadecimal\nusage: hexyl [OPTIONS] [ARGS]
- `tests.test_base_display.test_base_decimal`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--base=decimal', '--color=never'], returncode=2, stdout=b'', stderr=b"hexyl: unknown option: --base=decimal\nusage: hexyl [OPTIONS] [ARGS]\nTry 'h
- `tests.test_base_display.test_base_octal`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--base=octal', '--color=never'], returncode=2, stdout=b'', stderr=b"hexyl: unknown option: --base=octal\nusage: hexyl [OPTIONS] [ARGS]\nTry 'hexyl
- *(... 555 more in this cluster)*

### `other_assertion` — 164 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_version_flag`
  > AssertionError: assert b'0.16.0' in b'hexyl 0.14.0\n'
  >  +  where b'hexyl 0.14.0\n' = CompletedProcess(args=['./executable', '--version'], returncode=0, stdout=b'hexyl 0.14.0\n', stderr=b'').stdout
- `tests.test_basic_invocation.test_version_short_flag`
  > AssertionError: assert b'0.16.0' in b'hexyl 0.14.0\n'
  >  +  where b'hexyl 0.14.0\n' = CompletedProcess(args=['./executable', '-V'], returncode=0, stdout=b'hexyl 0.14.0\n', stderr=b'').stdout
- `tests.test_basic_invocation.test_help_flag`
  > AssertionError: assert b'Usage:' in b'hexyl 0.14.0\nA command-line hex viewer.\n\nUSAGE:\n    hexyl [FLAGS] [OPTIONS] [--] [FILE]\n\nFLAGS:\n    -h, --help       Prints help information\n    -V, --ver
  >  +  where b'hexyl 0.14.0\nA command-line hex viewer.\n\nUSAGE:\n    hexyl [FLAGS] [OPTIONS] [--] [FILE]\n\nFLAGS:\n    -h, --help       Prints help information\n    -V, --version    Prints version inf
- *(... 161 more in this cluster)*

### `rc_mismatch_got2_want1` — 53 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_hexyl_io.test_nonexistent_file_errors_to_stderr_exit1`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--plain', 'does-not-exist.bin'], returncode=2, stdout=b'', stderr=b"hexyl: unknown option: --plain\nusage: hexyl [OPTIONS] [ARGS]\nTry 'h
- `tests.test_error_diagnostics.test_invalid_unit_shows_actual_unit`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--skip=5xyz'], returncode=2, stdout=b'', stderr=b"hexyl: unknown option: --skip=5xyz\nusage: hexyl [OPTIONS] [ARGS]\nTry 'hexyl --help' f
- `tests.test_error_diagnostics.test_negative_length_explains_context_restriction`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--length=-5'], returncode=2, stdout=b'', stderr=b"hexyl: unknown option: --length=-5\nusage: hexyl [OPTIONS] [ARGS]\nTry 'hexyl --help' f
- *(... 50 more in this cluster)*

### `string_output_mismatch` — 10 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_usage.test_help_has_description_line`
  > AssertionError: assert 'hexyl 0.14.0' == 'A command-line hex viewer'
  >   
  >   - A command-line hex viewer
  >   + hexyl 0.14.0
- `eval.tests.test_hexyl_behavior.test_help_exact_snapshot`
  > AssertionError: assert 'hexyl 0.14.0...ds from STDIN' == 'A command-li...Print version'
  >   
  >   - A command-line hex viewer Usage: executable [OPTIONS] [FILE] Arguments: [FILE] The file to display. If no FILE argument is given, read from STDIN Options: -n, --length <N> Only read N bytes from t
  >   
  >   ...Full output truncated (2 lines hidden), use '-vv' to show
- `tests.test_display.test_version_output`
  > AssertionError: assert 'hexyl 0.14.0\n' == 'hexyl 0.16.0\n'
  >   
  >   - hexyl 0.16.0
  >   ?          ^
  >   + hexyl 0.14.0
  >   ?          ^
- *(... 7 more in this cluster)*

### `returned_none` — 4 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_args_parsing.test_double_dash_treats_following_as_positional_and_fails_for_missing_file`
  > assert None
  >  +  where None = <function search at 0x7fb96ccaa680>('(No such file|no such file|cannot open|failed to open)', "hexyl: unknown option: --\nusage: hexyl [OPTIONS] [ARGS]\nTry 'hexyl --help' for more in
  >  +    where <function search at 0x7fb96ccaa680> = re.search
- `eval.tests.test_help_usage.test_help_has_arguments_section`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7fb1a89ba680>('^Arguments:\\s*$', 'hexyl 0.14.0\nA command-line hex viewer.\n\nUSAGE:\n    hexyl [FLAGS] [OPTIONS] [--] [FILE]\n\nFLAGS:\n    -h, --help       Pr
  >  +    where <function search at 0x7fb1a89ba680> = re.search
  >  +    and   'hexyl 0.14.0\nA command-line hex viewer.\n\nUSAGE:\n    hexyl [FLAGS] [OPTIONS] [--] [FILE]\n\nFLAGS:\n    -h, --help       Prints help information\n    -V, --version    Prints version in
  >  +    and   re.MULTILINE = re.MULTILINE
- `eval.tests.test_help_usage.test_help_has_options_section`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7fb1a89ba680>('^Options:\\s*$', 'hexyl 0.14.0\nA command-line hex viewer.\n\nUSAGE:\n    hexyl [FLAGS] [OPTIONS] [--] [FILE]\n\nFLAGS:\n    -h, --help       Prin
  >  +    where <function search at 0x7fb1a89ba680> = re.search
  >  +    and   'hexyl 0.14.0\nA command-line hex viewer.\n\nUSAGE:\n    hexyl [FLAGS] [OPTIONS] [--] [FILE]\n\nFLAGS:\n    -h, --help       Prints help information\n    -V, --version    Prints version in
  >  +    and   re.MULTILINE = re.MULTILINE
- *(... 1 more in this cluster)*

### `test_timeout` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_input_edges.test_fifo_positive_skip_via_try_skip`
  > subprocess.TimeoutExpired: Command '['sh', '-c', "echo '0123456789abcdef' > /tmp/tmp18u0q2f8/test.fifo"]' timed out after 1 seconds
- `tests.test_input_edges.test_fifo_negative_skip_error`
  > subprocess.TimeoutExpired: Command '['sh', '-c', "echo 'test data' > /tmp/tmp5d_91nxj/test.fifo"]' timed out after 1 seconds

### `bytes_output_mismatch` — 1 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `eval.tests.test_hexyl_behavior.test_version_exact`
  > AssertionError: assert b'hexyl 0.14.0\n' == b'hexyl 0.16.0\n'
  >   
  >   At index 9 diff: b'4' != b'6'
  >   
  >   Full diff:
  >   - (b'hexyl 0.16.0\n')
  >   ?             ^
  >   + (b'hexyl 0.14.0\n')

