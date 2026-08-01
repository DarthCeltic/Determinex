# Action Sheet — stathissideris__ditaa.f2286c4

**Current:** 0.44%  (3/687)
**Pass / Fail / Skip:** 3 / 424 / 0
**Gap to 100%:** 99.56 percentage points (684 tests)

## Failure clusters

424 failed tests grouped into 8 buckets (sorted by count).

### `other_assertion` — 233 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_ditaa.TestBasicInvocation.test_help_flag`
  > AssertionError: assert b'usage:' in b'ditaa 0.1.0 - bootstrap scaffold\n\nUsage: ditaa [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n'
  >  +  where b'ditaa 0.1.0 - bootstrap scaffold\n\nUsage: ditaa [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['/workspace/executabl
- `tests.test_ditaa.TestBasicInvocation.test_help_contains_all_options`
  > AssertionError: Expected b'-A' in help output
  > assert b'-A' in b'ditaa 0.1.0 - bootstrap scaffold\n\nUsage: ditaa [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n'
  >  +  where b'ditaa 0.1.0 - bootstrap scaffold\n\nUsage: ditaa [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['/workspace/executabl
- `tests.test_ditaa.TestBasicInvocation.test_basic_png_conversion`
  > AssertionError: assert b'Reading file:' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', '/tmp/tmpszsvks75/diagram.txt', '/tmp/tmpszsvks75/output.png'], returncode=0, stdout=b'', stderr=b'').stdout
- *(... 230 more in this cluster)*

### `boolean_false` — 120 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_ditaa.TestBasicInvocation.test_file_to_stdout`
  > AssertionError: assert False
  >  +  where False = is_valid_png(b'')
  >  +    where b'' = CompletedProcess(args=['/workspace/executable', '/tmp/tmpgz48pas0/diagram.txt', '-'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_ditaa.TestBasicInvocation.test_stdin_to_stdout`
  > AssertionError: assert False
  >  +  where False = is_valid_png(b'')
  >  +    where b'' = CompletedProcess(args=['/workspace/executable', '-', '-'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_ditaa.TestHtmlMode.test_html_mode_auto_output_name`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmp0qdjxil0/myfile_processed.html').exists
- *(... 117 more in this cluster)*

### `rc_mismatch_got2_want0` — 38 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_ditaa.TestBasicInvocation.test_no_args_shows_help`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b"usage: ditaa [OPTIONS] [ARGS]\nTry 'ditaa --help' for more information.\n").returncode
- `tests.test_ditaa.TestInputOutput.test_svg_output_mode`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--svg', '/tmp/tmp41q5wk8f/diagram.txt', '/tmp/tmp41q5wk8f/output.svg'], returncode=2, stdout=b'', stderr=b"ditaa: unknown option: --svg\n
- `tests.test_ditaa.TestInputOutput.test_svg_auto_extension`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--svg', '/tmp/tmpv5g08_53/mydiagram.txt'], returncode=2, stdout=b'', stderr=b"ditaa: unknown option: --svg\nusage: ditaa [OPTIONS] [ARGS]
- *(... 35 more in this cluster)*

### `string_output_mismatch` — 14 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_diagramshape_edges.test_identical_shapes_rendering`
  > AssertionError: assert '\nditaa vers...one in Xsec\n' == ''
  >   
  >   + 
  >   + ditaa version 0.11, Copyright (C) 2004--2017  Efstathios (Stathis) Sideris
  >   + 
  >   + Running with options:
  >   + Reading file: identical_shapes.txt
  >   + Rendering to file: OUTPUT_FILE
- `tests.test_diagramshape_edges.test_fractional_scale_half`
  > AssertionError: assert '\nditaa vers...one in Xsec\n' == ''
  >   
  >   + 
  >   + ditaa version 0.11, Copyright (C) 2004--2017  Efstathios (Stathis) Sideris
  >   + 
  >   + Running with options:
  >   + scale = 0.5
  >   + Reading file: scale_test.txt
- `tests.test_diagramshape_edges.test_large_scale_factor`
  > AssertionError: assert '\nditaa vers...one in Xsec\n' == ''
  >   
  >   + 
  >   + ditaa version 0.11, Copyright (C) 2004--2017  Efstathios (Stathis) Sideris
  >   + 
  >   + Running with options:
  >   + scale = 5.0
  >   + Reading file: scale_test.txt
- *(... 11 more in this cluster)*

### `missing_file` — 11 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_ditaa.TestInputOutput.test_overwrite_flag_overwrites_existing_file`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmppjeu34m1/output.png'
- `tests.test_ditaa.TestInputOutput.test_png_is_default_format`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpo1ajynj9/output.png'
- `tests.test_ditaa.TestHtmlMode.test_html_mode_generates_img_tags`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmp0ch5d68d/out.html'
- *(... 8 more in this cluster)*

### `rc_mismatch_got0_want1` — 3 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_ditaa.TestInputOutput.test_missing_input_file_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/nonexistent/path/diagram.txt', '/tmp/output.png'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_ditaa.TestErrorHandling.test_error_message_format_missing_file`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/definitely/does/not/exist.txt', '/tmp/output.png'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_errors.test_nonexistent_input_file`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/nonexistent/file.txt'], returncode=0, stdout='', stderr='').returncode

### `rc_mismatch_got2_want1` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_errors.test_negative_scale_causes_error`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-s', '-1', '/tmp/tmpqge1gnry/test.txt', '/tmp/tmpqge1gnry/out.png'], returncode=2, stdout='', stderr="ditaa: unknown option: -s\nusage: d
- `tests.test_errors.test_zero_scale_causes_error`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-s', '0', '/tmp/tmpuj3buikl/test.txt', '/tmp/tmpuj3buikl/out.png'], returncode=2, stdout='', stderr="ditaa: unknown option: -s\nusage: di
- `tests.test_errors.test_svg_format_with_nonexistent_file`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--svg', '/nonexistent/file.txt'], returncode=2, stdout='', stderr="ditaa: unknown option: --svg\nusage: ditaa [OPTIONS] [ARGS]\nTry 'dita

### `bytes_output_mismatch` — 2 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_ditaa.TestOutputFormatVerification.test_stdout_produces_binary_png_data`
  > AssertionError: assert b'' == b'\x89PNG\r\n\x1a\n'
  >   
  >   Full diff:
  >   - (b'\x89PNG\r\n\x1a\n')
  >   + b''
- `tests.test_errors.test_stdin_to_stdout_binary`
  > AssertionError: assert b'' == b'\x89PNG\r\n\x1a\n'
  >   
  >   Full diff:
  >   - (b'\x89PNG\r\n\x1a\n')
  >   + b''

