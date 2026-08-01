# Action Sheet — cslarsen__jp2a.61d205f

**Current:** 14.95%  (139/930)
**Pass / Fail / Skip:** 139 / 572 / 3
**Gap to 100%:** 85.05 percentage points (791 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_errors.test_chars_exceeding_buffer_causes_crash`
  - reason: Coverage instrumentation masks buffer overflow - test passes on original binary
- `tests.test_harvest.test_curl_download_sourceforge`
  - reason: Network test - requires downloading from URL, may be flaky in CI
- `tests.test_harvest.test_curl_download_sf`
  - reason: Network test - requires downloading from URL, may be flaky in CI

## Failure clusters

572 failed tests grouped into 16 buckets (sorted by count).

### `other_assertion` — 293 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_jp2a.test_help_output`
  > AssertionError: assert b'jp2a' in b''
  >  +  where b'' = CompletedProcess(args=['./executable', '--help'], returncode=0, stdout=b'', stderr=b'').stderr
- `tests.test_jp2a.test_help_short_flag`
  > AssertionError: assert b'jp2a' in b''
  >  +  where b'' = CompletedProcess(args=['./executable', '-h'], returncode=0, stdout=b'', stderr=b'').stderr
- `tests.test_jp2a.test_version_output`
  > AssertionError: assert b'jp2a' in b''
  >  +  where b'' = CompletedProcess(args=['./executable', '--version'], returncode=0, stdout=b'', stderr=b'').stderr
- *(... 290 more in this cluster)*

### `string_output_mismatch` — 138 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_externalized_jp2a.test_ext_height_grayscale_logo`
  > assert b"'''..,;'::d...;;ccccll:::\n" == b"MMMMMMMMMMM...MMMMMMMMMMM\n"
  >   
  >   At index 0 diff: b"'" != b'M'
  >   
  >   Full diff:
  >   - (b'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM'
  >   -  b'MMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM'
  >   -  b'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMM'...
- `eval.tests.test_externalized_jp2a.test_ext_ansi_colors_fill`
  > assert b"..',;\x1b[4...47m:\x1b[0m\n" == b"'''..,,,;\x...47m:\x1b[0m\n"
  >   
  >   At index 0 diff: b'.' != b"'"
  >   
  >   Full diff:
  >   - (b"'''..,,,;\x1b[43ml\x1b[0m\x1b[43mx\x1b[0m\x1b[43mo\x1b[0m\x1b[43mx\x1b[0"
  >   ?    ---  ^^          ^                               ^            ----------
  >   + (b"..',;\x1b[43mo\x1b[0m\x1b[43mx\x1b[0m\x1b[43mk\x1b[0mW\x1b[47mM\x1b[0m\x1b["...
- `tests.test_basic.test_width_only_80`
  > AssertionError: assert 'MMMMMMMMMMMM...MMMMMMMMMMM\n' == 'MMMMMMMMMMMM...MMMMMMMMMMM\n'
  >   
  >   + MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
  >   + MMNNMMMMMMMMMMMMNKXMMMMMMMMMMM
  >   + MW;lMMMMMMMMMMx.   '0MMMMMMMMM
  >   + MO.,NO..;,.,xW00NK. cMk:::',kM
  >   + Mx .Xk  kWo  kMMNl ;NMKkxl. 'W
  >   + Mx .Xk  ck, .KWO. .cc0c .k, .0...
- *(... 135 more in this cluster)*

### `bytes_output_mismatch` — 61 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_terminal_fitting.test_term_fit_short_flag`
  > AssertionError: assert (b'TERM' in b'' or 1 == 0)
  >  +  where 1 = CompletedProcess(args=['./executable', '-f', 'tests/jp2a.jpg'], returncode=1, stdout=b'', stderr=b'').returncode
- `tests.test_terminal_fitting.test_term_zoom_short_flag`
  > AssertionError: assert (b'TERM' in b'' or 1 == 0)
  >  +  where 1 = CompletedProcess(args=['./executable', '-z', 'tests/jp2a.jpg'], returncode=1, stdout=b'', stderr=b'').returncode
- `eval.tests.test_jp2a_io.test_single_file_stdout_exact_fixture`
  > assert b'' == b"MMMMMMMMMMM...MMMMMMMMMMM\n"
  >   
  >   Full diff:
  >   + b''
  >   - (b'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM'
  >   -  b'MM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM'
  >   -  b'MMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM'
  >   -  b'MMMMMMMMMMMMMMMM\nMMMMMMWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWWMMMMMMM'...
- *(... 58 more in this cluster)*

### `rc_mismatch_got0_want1` — 23 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_jp2a.test_no_arguments_shows_help`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable'], returncode=0, stdout=b' \n--blue=N.N    Set RGB to grayscale conversion weight\n--colors\n--green=N.N   Set RGB to grayscale conversion weigh
- `tests.test_jp2a_coverage.test_too_many_chars_in_palette`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', '--width=40', '--chars=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
- `tests.test_basic_invocation.test_no_arguments_shows_help`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable'], returncode=0, stdout=b' \n--blue=N.N    Set RGB to grayscale conversion weight\n--colors\n--green=N.N   Set RGB to grayscale conversion weigh
- *(... 20 more in this cluster)*

### `returned_none` — 16 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_html.test_html_default_fontsize`
  > assert None is not None
- `tests.test_html.test_html_custom_fontsize`
  > assert None is not None
- `tests.test_html.test_html_custom_title`
  > assert None is not None
- *(... 13 more in this cluster)*

### `rc_unexpected_zero` — 12 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_jp2a.test_invalid_option`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '--invalid-option-xyz'], returncode=0, stdout=b'M\nM\n', stderr=b'').returncode
- `tests.test_no_subcommands.TestNoSubcommands.test_no_args_shows_error_not_subcommand_list`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable'], returncode=0, stdout=b' \n--blue=N.N    Set RGB to grayscale conversion weight\n--colors\n--green=N.N   Set RGB to grayscale conversion weigh
- `tests.test_no_subcommands.TestFlagBasedInterface.test_invalid_flag_produces_error`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '--nonexistent-flag-xyz'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 9 more in this cluster)*

### `boolean_false` — 10 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_jp2a.test_output_file_overwrite`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpdwditk1g/output.txt').exists
- `tests.test_jp2a_coverage.test_output_to_file_multiple_images`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpxe2463aq/multi.txt').exists
- `tests.test_output_control.test_output_to_file`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpf9il4igv/output.txt').exists
- *(... 7 more in this cluster)*

### `rc_mismatch_got1_want0` — 10 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_dimensions.test_width_various_values`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '--width=30', 'tests/jp2a.jpg'], returncode=1, stdout=b"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMM0KMMMMMMMMMMMXOkONMMMMMMMMMM\nMX,cWN00X00NMMd.,'  xMMNK00
- `tests.test_edge_cases.test_multiple_images_in_sequence`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '--width=30', 'tests/jp2a.jpg', 'tests/dalsnuten-640x480-gray-low.jpg'], returncode=1, stdout=b"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMM0KMMMMMMMMMMMXOkO
- `tests.test_input_handling.test_multiple_files_same_file`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '--width=30', 'tests/jp2a.jpg', 'tests/jp2a.jpg'], returncode=1, stdout=b"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMM0KMMMMMMMMMMMXOkONMMMMMMMMMM\nMX,cWN00X
- *(... 7 more in this cluster)*

### `uncategorized` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_html.test_html_css_ascii_class`
  > AttributeError: 'NoneType' object has no attribute 'string'
- `tests.test_html.test_html_multiple_flag_combination`
  > AttributeError: 'NoneType' object has no attribute 'string'

### `rc_mismatch_got11_want1` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_jp2a.test_flipx`
  > assert 11 == 1
  >  +  where 11 = len([b'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM', b'MMNNMMMMMMMMMMMMNKXMMMMMMMMMMM', b"MW;lMMMMMMMMMMx.   '0MMMMMMMMM", b"MO.,NO..;,.,xW00NK. cMk:::',kM", b"Mx .Xk  kWo  kMMNl ;NMKkxl. 'W", b'Mx 
  >  +  and   1 = len([b''])

### `rc_mismatch_got28635_want0` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_jp2a.test_output_to_file`
  > AssertionError: assert 28635 == 0
  >  +  where 28635 = len(b'\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd\x00\x10JFIF\x00\x01\x02\x01\x00H\x00H\x00\x00\xef\xbf\xbd\xef\xbf\xbd\x08/Exif\x00\x00MM\x00*\x00\x00\x00\x08\x00\x07\x01\x12\x
  >  +    where b'\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd\x00\x10JFIF\x00\x01\x02\x01\x00H\x00H\x00\x00\xef\xbf\xbd\xef\xbf\xbd\x08/Exif\x00\x00MM\x00*\x00\x00\x00\x08\x00\x07\x01\x12\x00\x03\x00

### `empty_list_or_string` — 1 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_subcommand_analysis.TestSingleModeOperation.test_no_mode_switching_via_arguments`
  > IndexError: list index out of range

### `missing_file` — 1 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `eval.tests.test_externalized_jp2a.test_ext_output_file_option_writes_expected`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_ext_output_file_option_wr2/out.txt'

### `rc_mismatch_got0_want8004000` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_externalized_jp2a.test_ext_big_size_bytecount`
  > assert 0 == 8004000

### `rc_mismatch_got50_want14` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic.test_multiple_input_files`
  > AssertionError: assert 50 == 14
  >  +  where 50 = len(['MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM', 'MMMMMMMMMMMMMMM

### `rc_mismatch_got160_want120` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic.test_very_wide_aspect_ratio`
  > AssertionError: assert 160 == 120
  >  +  where 160 = len('MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM')

