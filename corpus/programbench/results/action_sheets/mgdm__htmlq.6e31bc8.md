# Action Sheet — mgdm__htmlq.6e31bc8

**Current:** 30.61%  (630/2058)
**Pass / Fail / Skip:** 630 / 1427 / 1
**Gap to 100%:** 69.39 percentage points (1428 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_15_final_massive_push.test_flag_combinations_matrix[True-True]`
  - reason: Incompatible flags

## Failure clusters

1427 failed tests grouped into 15 buckets (sorted by count).

### `other_assertion` — 1031 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_01_basic.test_help_flag`
  > AssertionError: assert b'USAGE:' in b'htmlq 0.1.0\n\nusage: htmlq [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --verbose  Verbose\n  -q, --quiet    
  >  +  where b'htmlq 0.1.0\n\nusage: htmlq [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --verbose  Verbose\n  -q, --quiet    Quiet\n\n' = CompletedProc
- `eval.tests.test_01_basic.test_selector_basic`
  > AssertionError: assert b'<p>text</p>' in b''
  >  +  where b'' = CompletedProcess(args=['./executable', 'p'], returncode=0, stdout=b'', stderr=b'').stdout
- `eval.tests.test_01_basic.test_selector_class`
  > assert b'class="test"' in b''
  >  +  where b'' = CompletedProcess(args=['./executable', '.test'], returncode=0, stdout=b'', stderr=b'').stdout
- *(... 1028 more in this cluster)*

### `string_output_mismatch` — 268 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_cli_edge.test_help_flag`
  > AssertionError: assert 'htmlq 0.1.0\...    Quiet\n\n' == 'htmlq 0.4.0\...ault: html]\n'
  >   
  >   - htmlq 0.4.0
  >   ?         ^
  >   + htmlq 0.1.0
  >   ?         ^
  >   - Michael Maclean <michael@mgdm.net>
  >   - Runs CSS selectors on HTML...
- `tests.test_cli_edge.test_help_flag_short`
  > AssertionError: assert 'htmlq 0.1.0\...    Quiet\n\n' == 'htmlq 0.4.0\...ault: html]\n'
  >   
  >   - htmlq 0.4.0
  >   ?         ^
  >   + htmlq 0.1.0
  >   ?         ^
  >   - Michael Maclean <michael@mgdm.net>
  >   - Runs CSS selectors on HTML...
- `tests.test_cli_edge.test_version_flag`
  > AssertionError: assert 'htmlq 0.1.0\n' == 'htmlq 0.4.0\n'
  >   
  >   - htmlq 0.4.0
  >   ?         ^
  >   + htmlq 0.1.0
  >   ?         ^
- *(... 265 more in this cluster)*

### `rc_mismatch_got2_want0` — 78 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `eval.tests.test_01_basic.test_no_args_empty_stdin`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable'], returncode=2, stdout=b'', stderr=b'usage: htmlq [OPTIONS] [ARGS]\n').returncode
- `eval.tests.test_01_basic.test_simple_html`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable'], returncode=2, stdout=b'', stderr=b'usage: htmlq [OPTIONS] [ARGS]\n').returncode
- `eval.tests.test_04_flags.test_text_flag`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--text', 'p'], returncode=2, stdout=b'', stderr=b'htmlq: error: unrecognized argument: --text\n').returncode
- *(... 75 more in this cluster)*

### `rc_mismatch_got1_want2` — 13 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_output.test_multiple_elements_attribute_extraction`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len([''])
- `tests.test_output.test_data_attribute_extraction`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len([''])
- `tests.test_output.test_multiple_elements_text_extraction`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len([''])
- *(... 10 more in this cluster)*

### `rc_unexpected_zero` — 10 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `eval.tests.test_06_error_conditions.test_invalid_selector`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'p[[['], returncode=0, stdout=b'', stderr=b'').returncode
- `eval.tests.test_06_error_conditions.test_nonexistent_file`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '-f', '/nonexistent/file.html', 'p'], returncode=0, stdout=b'', stderr=b'').returncode
- `eval.tests.test_06_error_conditions.test_invalid_output_directory`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '-o', '/nonexistent/dir/file.html', 'p'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 7 more in this cluster)*

### `boolean_false` — 8 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `eval.tests.test_combined_flags.test_file_input_output_with_processing`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpivd9waom/output.html').exists
- `eval.tests.test_combined_flags.test_all_flags_together`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmptmkkfeqd/output.html').exists
- `eval.tests.test_input_output.test_file_output`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmptopti5pw/output.html').exists
- *(... 5 more in this cluster)*

### `subprocess_failed` — 5 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_edge.test_empty_stdin`
  > subprocess.CalledProcessError: Command '['/workspace/executable']' returned non-zero exit status 2.
- `tests.test_gaps.test_no_selector_defaults_to_html`
  > subprocess.CalledProcessError: Command '['/workspace/executable']' returned non-zero exit status 2.
- `tests.test_gaps.test_pretty_print_with_comments`
  > subprocess.CalledProcessError: Command '['/workspace/executable', '--pretty']' returned non-zero exit status 2.
- *(... 2 more in this cluster)*

### `missing_file` — 4 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `eval.tests.test_04_flags.test_file_output_short`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpbwiuobgh/out.html'
- `tests.test_integration.test_filename_output_text`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/test_integration_out.txt'
- `eval.tests.test_argparse_validation.test_output_file_option_accepts_value`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_output_file_option_accept2/out.txt'
- *(... 1 more in this cluster)*

### `rc_mismatch_got1_want3` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_output.test_list_items_text_extraction`
  > AssertionError: assert 1 == 3
  >  +  where 1 = len([''])
- `tests.test_output.test_pre_element_text_extraction_preserves_formatting`
  > AssertionError: assert 1 == 3
  >  +  where 1 = len([''])

### `rc_mismatch_got0_want101` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_selectors.test_invalid_selector_error`
  > AssertionError: assert 0 == 101
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '###invalid'], returncode=0, stdout='', stderr='').returncode
- `tests.test_selectors.test_nonexistent_file_error`
  > AssertionError: assert 0 == 101
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-f', '/nonexistent_file_12345.html', 'div'], returncode=0, stdout='', stderr='').returncode

### `bytes_output_mismatch` — 2 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `eval.tests.test_cli_externalized.test_ext_find_by_class`
  > assert b'' == b'<div class=...o</a></div>\n'
  >   
  >   Full diff:
  >   - (b'<div class="hi"><a href="/foo/bar">Hello</a></div>\n')
  >   + b''
- `eval.tests.test_cli_externalized.test_ext_find_by_id`
  > assert b'' == b'<div id="my...o</a></div>\n'
  >   
  >   Full diff:
  >   - (b'<div id="my-id"><a href="/foo/bar">Hello</a></div>\n')
  >   + b''

### `rc_mismatch_got1_want10000` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_edge.test_very_large_stdin_input`
  > AssertionError: assert 1 == 10000
  >  +  where 1 = len([''])

### `rc_mismatch_got0_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_output.test_empty_elements_text_extraction`
  > assert 0 == 3
  >  +  where 0 = len([])

### `rc_mismatch_got0_want2` — 1 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_output.test_mixed_present_and_missing_attributes`
  > assert 0 == 2
  >  +  where 0 = len([])

### `rc_mismatch_got2_want101` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_htmlq_io.test_nonexistent_input_file_panics_and_exit_code_is_101_and_message_on_stderr`
  > AssertionError: assert 2 == 101
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--filename', '/tmp/pytest-of-root/pytest-0/test_nonexistent_input_file_pa2/nope.html'], returncode=2, stdout=b'', stderr=b'htmlq: error: 

