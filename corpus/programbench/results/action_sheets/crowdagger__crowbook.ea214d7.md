# Action Sheet — crowdagger__crowbook.ea214d7

**Current:** 11.81%  (126/1067)
**Pass / Fail / Skip:** 126 / 605 / 0
**Gap to 100%:** 88.19 percentage points (941 tests)

## Failure clusters

605 failed tests grouped into 9 buckets (sorted by count).

### `other_assertion` — 261 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_actual_rendering.test_render_to_stdout`
  > AssertionError: assert 'Stdout Test' in '<!DOCTYPE html>\n<html>\n<head>\n<title>Test Book</title>\n</head>\n<body>\n<h1>Test Book</h1>\n<p>Hello, World!</p>\n</body>\n</html>\n'
- `tests.test_actual_rendering.test_render_error_missing_chapter`
  > AssertionError: assert ('error' in '' or 'missing' in '' or 'not' in '')
- `tests.test_basic_invocation.test_help_shows_all_options`
  > AssertionError: Flag b'--single' not found in help
  > assert b'--single' in b'crowbook\nUSAGE:\nOPTIONS:\nRender a Markdown book\ncrowbook\n'
  >  +  where b'crowbook\nUSAGE:\nOPTIONS:\nRender a Markdown book\ncrowbook\n' = CompletedProcess(args=['/workspace/executable', '--help'], returncode=0, stdout=b'crowbook\nUSAGE:\nOPTIONS:\nRender a Mar
- *(... 258 more in this cluster)*

### `missing_file` — 217 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_actual_rendering.test_render_with_chapters_numbering`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpn22uy6aa/numbered.html'
- `tests.test_actual_rendering.test_render_with_inline_toc`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmp0cx673z6/toc.html'
- `tests.test_actual_rendering.test_render_with_metadata`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmp88jxdqqw/meta.html'
- *(... 214 more in this cluster)*

### `boolean_false` — 65 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_actual_rendering.test_render_html_basic`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmp43b1eg88/output.html').exists
- `tests.test_actual_rendering.test_render_epub_basic`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpk_yb58s1/book.epub').exists
- `tests.test_actual_rendering.test_render_multiple_formats`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmp6up1g2a4/multi.html').exists
- *(... 62 more in this cluster)*

### `rc_mismatch_got2_want0` — 30 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_basic_invocation.test_no_arguments_shows_error`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b"You must pass a book file or a command\nUsage: crowbook [OPTIONS] [BOOK_FILE]\nTry 'crowbook --help' f
- `tests.test_create_book.test_create_book_with_filename`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '/tmp/tmpw26yw5n6/mybook.book', '--create', '/tmp/tmpw26yw5n6/chapter.md'], returncode=2, stdout=b'', stderr=b"Error: Could not find file 
- `tests.test_argument_parsing.TestBasicExecution.test_nonexistent_file_shows_error`
  > assert 2 == 0
- *(... 27 more in this cluster)*

### `string_output_mismatch` — 18 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_argument_parsing.TestSetFlag.test_set_flag_two_values`
  > assert ('You must pass' in "Error: Could not find file 'key'\nError: No such file or directory (os error 2)\n" or 2 == 0)
- `eval.tests.test_help_output.test_dash_h_output_matches_double_dash_help`
  > AssertionError: assert 'crowbook\nUS...k\ncrowbook\n' == 'crowbook\nUS...rkdown book\n'
  >   
  >   - crowbook
  >   - USAGE:
  >   - OPTIONS:
  >   - --help
  >   - --version
  >   - --single...
- `eval.tests.test_help_output.test_baseline_help_text_matches_fixture_exactly`
  > AssertionError: assert 'crowbook\nUS...k\ncrowbook\n' == 'crowbook 0.1...th --single\n'
  >   
  >   + crowbook
  >   - crowbook 0.17.0 by Élisabeth Henry <liz.henry@ouvaton.org>
  >   - Render a Markdown book in EPUB, PDF or HTML.
  >   -   
  >     USAGE:
  >   -     executable [OPTIONS] [BOOK]...
- *(... 15 more in this cluster)*

### `rc_mismatch_got0_want2` — 5 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_errors.test_invalid_to_format`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'chapter.md', '--to', 'invalid_format'], returncode=0, stdout='<!DOCTYPE html>\n<html>\n<head>\n<title>Test Book</title>\n</head>\n<body>\
- `tests.test_errors.test_output_without_to_flag`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'chapter.md', '-o', 'output.html'], returncode=0, stdout='<!DOCTYPE html>\n<html>\n<head>\n<title>Test Book</title>\n</head>\n<body>\n<h1>
- `tests.test_errors.test_invalid_flag`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--invalid-flag'], returncode=0, stdout='<!DOCTYPE html>\n<html>\n<head>\n<title>Test Book</title>\n</head>\n<body>\n<h1>Test Book</h1>\n<
- *(... 2 more in this cluster)*

### `returned_none` — 4 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_basic_invocation.test_version_short_flag`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f951784f760>(b'crowbook\\s+\\d+\\.\\d+\\.\\d+', b'crowbook\n')
  >  +    where <function search at 0x7f951784f760> = re.search
  >  +    and   b'crowbook\n' = CompletedProcess(args=['/workspace/executable', '-V'], returncode=0, stdout=b'crowbook\n', stderr=b'').stdout
- `tests.test_basic_invocation.test_version_long_flag`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f951784f760>(b'\\d+\\.\\d+\\.\\d+', b'crowbook\n')
  >  +    where <function search at 0x7f951784f760> = re.search
  >  +    and   b'crowbook\n' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'crowbook\n', stderr=b'').stdout
- `eval.tests.test_help_output.test_help_usage_line_mentions_options_and_book`
  > AssertionError: assert None is not None
  >  +  where None = <function search at 0x7f3dfd74e680>('^\\s*executable\\s+\\[OPTIONS\\]\\s+\\[BOOK\\]\\s*$', 'crowbook\nUSAGE:\nOPTIONS:\nRender a Markdown book\ncrowbook\n', re.MULTILINE)
  >  +    where <function search at 0x7f3dfd74e680> = re.search
  >  +    and   re.MULTILINE = re.M
- *(... 1 more in this cluster)*

### `rc_unexpected_zero` — 3 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_basic_invocation.test_invalid_option_shows_error`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--invalid-option-xyz'], returncode=0, stdout=b'<!DOCTYPE html>\n<html>\n<head>\n<title>Test Book</title>\n</head>\n<body>\n<h1>Test Book<
- `tests.test_subcommand_routing.TestArgumentHandling.test_unknown_flag_produces_error`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--nonexistent-flag'], returncode=0, stdout='<!DOCTYPE html>\n<html>\n<head>\n<title>Test Book</title>\n</head>\n<body>\n<h1>Test Book</h1
- `tests.test_subcommand_routing.TestSingleCommandInterface.test_invalid_format_to_flag`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--to', 'invalid_format', '/tmp/pytest-of-root/pytest-0/test_invalid_format_to_flag2/test.book'], returncode=0, stdout='<!DOCTYPE html>\n<

### `bytes_output_mismatch` — 2 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `eval.tests.test_single_render_io.test_single_html_with_output_file_creates_file_no_stdout`
  > AssertionError: assert b'<!DOCTYPE h...y>\n</html>\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'<!DOCTYPE html>\n<html>\n<head>\n<title>Test Book</title>\n</head>\n<body'
  >   +  b'>\n<h1>Test Book</h1>\n<p>Hello, World!</p>\n</body>\n</html>\n')
- `eval.tests.test_single_render_io.test_single_epub_to_stdout_is_zip_bytes_and_warns_on_stderr`
  > AssertionError: assert b'<!' == b'PK'
  >   
  >   At index 0 diff: b'<' != b'P'
  >   
  >   Full diff:
  >   - b'PK'
  >   + b'<!'

