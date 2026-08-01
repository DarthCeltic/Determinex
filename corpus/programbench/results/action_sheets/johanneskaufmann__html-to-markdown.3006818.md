# Action Sheet — johanneskaufmann__html-to-markdown.3006818

**Current:** 13.08%  (171/1307)
**Pass / Fail / Skip:** 171 / 801 / 0
**Gap to 100%:** 86.92 percentage points (1136 tests)

## Failure clusters

801 failed tests grouped into 12 buckets (sorted by count).

### `other_assertion` — 425 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_advanced_features.TestAdvancedConversion.test_link_inside_strong`
  > AssertionError: assert ('[**Bold Link**](https://example.com)' in '![Alt](image.png\n![image](https://example.com/img.png)\n# Article Title\n## Section 1\n&\n>\n<\n* * *\n**\n**Bold**\n**and bol
- `tests.test_advanced_features.TestAdvancedConversion.test_code_block_with_language`
  > assert ('print("hello")' in '![Alt](image.png\n![image](https://example.com/img.png)\n# Article Title\n## Section 1\n&\n>\n<\n* * *\n**\n**Bold**\n**and bold**\n**bold**\n**deeply nested**\n**te
- `tests.test_advanced_features.TestAdvancedConversion.test_multiple_blockquotes`
  > AssertionError: assert 'Quote 1' in '![Alt](image.png\n![image](https://example.com/img.png)\n# Article Title\n## Section 1\n&\n>\n<\n* * *\n**\n**Bold**\n**and bold**\n**bold**\n**deeply nested
- *(... 422 more in this cluster)*

### `string_output_mismatch` — 186 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_args.test_input_accepts_equals_form`
  > AssertionError: assert '![Alt](image...y\nCol1\nCol2' == 'Hello'
  >   
  >   - Hello
  >   + ![Alt](image.png
  >   + ![image](https://example.com/img.png)
  >   + # Article Title
  >   + ## Section 1
  >   + &...
- `eval.tests.test_args.test_domain_when_provided_affects_output`
  > AssertionError: assert '' == '[X](/x)'
  >   
  >   - [X](/x)
- `eval.tests.test_help_output.test_baseline_help_output_matches_fixture_exactly`
  > AssertionError: assert '' == '\n# html2mar...-markdown\n\n'
  >   
  >   - 
  >   - # html2markdown - convert html to markdown [version dev]
  >   - 
  >   - Convert HTML to Markdown. Even works with entire websites!
  >   - 
  >   - ## Basics...
- *(... 183 more in this cluster)*

### `bytes_output_mismatch` — 79 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_basic_invocation.TestBasicConversion.test_empty_input`
  > AssertionError: assert (b'![Alt](imag...nCol1\nCol2\n' == b'\n'
  >   
  >   At index 0 diff: b'!' != b'\n'
  >   
  >   Full diff:
  >   - b'\n'
  >   + (b'![Alt](image.png\n![image](https://example.com/img.png)\n# Article Title\n#'
  >   +  b'# Section 1\n&\n>\n<\n* * *\n**\n**Bold**\n**and bold**\n**bold**\n'...
- `tests.test_basic_invocation.test_stdin_empty_input`
  > AssertionError: assert (b'![Alt](imag...nCol1\nCol2\n' == b'\n'
  >   
  >   At index 0 diff: b'!' != b'\n'
  >   
  >   Full diff:
  >   - b'\n'
  >   + (b'![Alt](image.png\n![image](https://example.com/img.png)\n# Article Title\n#'
  >   +  b'# Section 1\n&\n>\n<\n* * *\n**\n**Bold**\n**and bold**\n**bold**\n'...
- `eval.tests.test_html2markdown_cli.test_default_output_matches_reference[index.html-index.html.default.md]`
  > AssertionError: assert [] == [b'# State of...rs', b'', ...]
  >   
  >   Right contains 1651 more items, first extra item: b'# State of Applied AI in 2025'
  >   
  >   Full diff:
  >   + []
  >   - [
  >   -     b'# State of Applied AI in 2025',...
- *(... 76 more in this cluster)*

### `rc_unexpected_zero` — 55 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_basic_invocation.TestBasicConversion.test_no_args_no_stdin_shows_error`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable'], returncode=0, stdout=b'![Alt](image.png\n![image](https://example.com/img.png)\n# Article Title\n## Section 1\n&\n>\n<\n* * *\n**\n
- `tests.test_error_handling.TestErrorHandling.test_invalid_flag`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--invalid-flag'], returncode=0, stdout=b'__test__\nLink\n', stderr=b'').returncode
- `tests.test_error_handling.TestErrorHandling.test_table_options_require_table_plugin`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--opt-table-skip-empty-rows'], returncode=0, stdout=b'Link\n', stderr=b'').returncode
- *(... 52 more in this cluster)*

### `boolean_false` — 25 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_error_handling.TestErrorHandling.test_output_to_nonexistent_directory`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmppj8xcz1y/nonexistent/deep/path/output.md').exists
- `tests.test_file_io.TestFileOutput.test_output_to_file`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpc4blzgzp/output.md').exists
- `tests.test_file_io.TestFileOutput.test_input_file_to_output_file`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpxebgjzpf/output.md').exists
- *(... 22 more in this cluster)*

### `rc_mismatch_got0_want1` — 18 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `eval.tests.test_args.test_unknown_flag_exits_1_and_mentions_unknown_flag`
  > assert 0 == 1
- `eval.tests.test_args.test_missing_value_for_value_flag_exits_1[--input]`
  > assert 0 == 1
- `eval.tests.test_args.test_missing_value_for_value_flag_exits_1[--output]`
  > assert 0 == 1
- *(... 15 more in this cluster)*

### `missing_file` — 7 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `eval.tests.test_args.test_multi_input_glob_with_output_dir_slash_succeeds`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_multi_input_glob_with_out2/out/a.md'
- `eval.tests.test_files_and_dirs.test_input_file_to_output_file_no_trailing_newline`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_input_file_to_output_file2/out.md'
- `eval.tests.test_files_and_dirs.test_glob_input_to_output_directory_creates_md_files`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_glob_input_to_output_dire2/dist/a.md'
- *(... 4 more in this cluster)*

### `rc_mismatch_got0_want2` — 2 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_file_io.test_duplicate_basenames_different_paths`
  > assert 0 == 2
  >  +  where 0 = len([])
- `tests.test_file_io.test_dot_files_in_glob`
  > assert 0 == 2
  >  +  where 0 = len([])

### `rc_mismatch_got398_want0` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_stdin_whitespace_only`
  > AssertionError: assert 398 == 0
  >  +  where 398 = len(b'![Alt](image.png\n![image](https://example.com/img.png)\n# Article Title\n## Section 1\n&\n>\n<\n* * *\n**\n**Bold**\n**and bold**\n**bold**\n**deeply nested**\n**test**\n*
  >  +    where b'![Alt](image.png\n![image](https://example.com/img.png)\n# Article Title\n## Section 1\n&\n>\n<\n* * *\n**\n**Bold**\n**and bold**\n**bold**\n**deeply nested**\n**test**\n**text**\
  >  +      where <built-in method strip of bytes object at 0x7fc6a854a040> = b'![Alt](image.png\n![image](https://example.com/img.png)\n# Article Title\n## Section 1\n&\n&gt;\n&lt;\n* * *\n**\n**Bold**\n
  >  +        where b'![Alt](image.png\n![image](https://example.com/img.png)\n# Article Title\n## Section 1\n&\n&gt;\n&lt;\n* * *\n**\n**Bold**\n**and bold**\n**bold**\n**deeply nested**\n**test**\n**tex

### `returned_none` — 1 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_output.test_help_version_bracket_present_but_not_asserting_version_value`
  > assert None is not None

### `rc_mismatch_got0_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_file_io.test_mixed_extensions_in_glob`
  > assert 0 == 3
  >  +  where 0 = len([])

### `rc_mismatch_got64_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_options_flags.test_multiple_table_options_combined`
  > AssertionError: assert 64 == 3
  >  +  where 64 = len(['<table>', '  <tr>', '    <td>Cell 1</td>', '    <td>Cell 2</td>', '  </tr>', '  <tr>', ...])

