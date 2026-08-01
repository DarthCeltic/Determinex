# Action Sheet — sibprogrammer__xq.b89f681

**Current:** 21.54%  (240/1114)
**Pass / Fail / Skip:** 240 / 636 / 3
**Gap to 100%:** 78.46 percentage points (874 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_xq_behavior.test_xml_format_from_stdin_matches_fixture`
  - reason: test_xml_format_from_stdin_matches_fixture depends on test_xml_format_from_file_matches_fixture
- `eval.tests.test_e2e_xq.test_ext_format_xml_matches_golden_files[unformatted6.xml-formatted6.xml]`
  - reason: HTML-ish XML formatting differs in CLI build
- `eval.tests.test_e2e_xq.test_ext_process_as_json_plain_text_wraps_in_text_key`
  - reason: -j on plain text not supported by current CLI

## Failure clusters

636 failed tests grouped into 12 buckets (sorted by count).

### `string_output_mismatch` — 224 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_argparse_validation.test_query_accepts_space_and_equals_forms[args0-1]`
  > AssertionError: assert 'text\ntext\n...ript\ncontent' == '1'
  >   
  >   - 1
  >   + text
  >   + text
  >   + foo.js
  >   + bar.js
  >   + baz.js...
- `eval.tests.test_argparse_validation.test_query_accepts_space_and_equals_forms[args1-1]`
  > AssertionError: assert 'text\nfoo.js...content\ntext' == '1'
  >   
  >   - 1
  >   + text
  >   + foo.js
  >   + bar.js
  >   + baz.js
  >   + https://example.com...
- `eval.tests.test_argparse_validation.test_query_accepts_space_and_equals_forms[args2-1]`
  > AssertionError: assert '--help\n--ve...lville\nCDATA' == '1'
  >   
  >   - 1
  >   + --help
  >   + --version
  >   + 1.4.0
  >   + 1234 Main Road
  >   + 3...
- *(... 221 more in this cluster)*

### `other_assertion` — 215 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_additional_coverage.test_malformed_json_error`
  > AssertionError: assert (b'error' in b'--help\n--version\n1.4.0\n1234 main road\n3\n<!-- this is a comment -->\n<!-- this is not a real user. -->\n</body>\n</head>\n</html>\n</root>\n<?xml version=\n<a
  >  +  where b'--help\n--version\n1.4.0\n1234 main road\n3\n<!-- this is a comment -->\n<!-- this is not a real user. -->\n</body>\n</head>\n</html>\n</root>\n<?xml version=\n<a>\n<body>\n<body></body>\n
  >  +    where <built-in method lower of bytes object at 0x55cbf0e8cfe0> = b'--help\n--version\n1.4.0\n1234 Main Road\n3\n<!-- This is a comment -->\n<!-- This is not a real user. -->\n</body>\n</head>\n
  >  +  and   b'--help\n--version\n1.4.0\n1234 main road\n3\n<!-- this is a comment -->\n<!-- this is not a real user. -->\n</body>\n</head>\n</html>\n</root>\n<?xml version=\n<a>\n<body>\n<body></body>\n
  >  +    where <built-in method lower of bytes object at 0x55cbf0e8cfe0> = b'--help\n--version\n1.4.0\n1234 Main Road\n3\n<!-- This is a comment -->\n<!-- This is not a real user. -->\n</body>\n</head>\n
- `tests.test_additional_coverage.test_html_with_scripts_and_styles`
  > AssertionError: assert b'content' in b'<html>\n<body>\n<p>test</p>\n<html>\n<html>\n    <\n<html>\n'
  >  +  where b'<html>\n<body>\n<p>test</p>\n<html>\n<html>\n    <\n<html>\n' = CompletedProcess(args=['./executable', '-m'], returncode=0, stdout=b'<html>\n<body>\n<p>test</p>\n<html>\n<html>\n    <\n<ht
- `tests.test_additional_coverage.test_xpath_with_predicate`
  > assert b'first' in b'<html>\nBellville\n<root>\n<item>content</item>\n'
  >  +  where b'<html>\nBellville\n<root>\n<item>content</item>\n' = CompletedProcess(args=['./executable', '-x', "//item[@id='1']"], returncode=0, stdout=b'<html>\nBellville\n<root>\n<item>content</item>
- *(... 212 more in this cluster)*

### `json_output_missing_or_bad` — 78 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `tests.test_additional_coverage.test_xml_to_json_with_mixed_content`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_additional_coverage.test_xml_to_json_depth_zero`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_xml_to_json.test_xml_to_json_basic`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- *(... 75 more in this cluster)*

### `bytes_output_mismatch` — 37 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_additional_coverage.test_malformed_xml_error`
  > AssertionError: assert (0 == 1 or b'unclosed' in b'--help\n--version\n1.4.0\n1234 Main Road\n3\n<!-- This is a comment -->\n<!-- This is not a real user. -->\n</body>\n</head>\n</html>\n</root>\n<?xml
  >  +  where 0 = CompletedProcess(args=['./executable'], returncode=0, stdout=b'--help\n--version\n1.4.0\n1234 Main Road\n3\n<!-- This is a comment -->\n<!-- This is not a real user. -->\n</body>\n</head
  >  +  and   b'--help\n--version\n1.4.0\n1234 Main Road\n3\n<!-- This is a comment -->\n<!-- This is not a real user. -->\n</body>\n</head>\n</html>\n</root>\n<?xml version=\n<a>\n<body>\n<body></body>\n
  >  +  and   b'--help\n--version\n1.4.0\n1234 main road\n3\n<!-- this is a comment -->\n<!-- this is not a real user. -->\n</body>\n</head>\n</html>\n</root>\n<?xml version=\n<a>\n<body>\n<body></body>\n
  >  +    where <built-in method lower of bytes object at 0x55cbf0e8c590> = b'--help\n--version\n1.4.0\n1234 Main Road\n3\n<!-- This is a comment -->\n<!-- This is not a real user. -->\n</body>\n</head>\n
  >  +      where b'--help\n--version\n1.4.0\n1234 Main Road\n3\n<!-- This is a comment -->\n<!-- This is not a real user. -->\n</body>\n</head>\n</html>\n</root>\n<?xml version=\n<a>\n<body>\n<body></bod
- `tests.test_additional_coverage.test_xpath_no_matches`
  > AssertionError: assert (b'<html>\nBel...tent</item>\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'<html>\nBellville\n<root>\n<item>content</item>\n') or b'<html>\nBel...tent</item>\n' == b'\n'
  >   
  >   At index 0 diff: b'<' != b'\n'
  >   
- `tests.test_additional_coverage.test_css_query_no_matches`
  > AssertionError: assert (b'<html>\nBel...tent</item>\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'<html>\nBellville\n<root>\n<item>content</item>\n') or b'<html>\nBel...tent</item>\n' == b'\n'
  >   
  >   At index 0 diff: b'<' != b'\n'
  >   
- *(... 34 more in this cluster)*

### `rc_mismatch_got0_want1` — 30 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_file_operations.test_in_place_with_multiple_files_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', '-i', '/tmp/tmpcybwvz04/test1.xml', '/tmp/tmpcybwvz04/test2.xml'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_file_operations.test_in_place_with_no_files_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', '-i'], returncode=0, stdout=b'', stderr=b'').returncode
- `eval.tests.test_xq_io.test_missing_file_errors_to_stdout_and_exit1`
  > AssertionError: assert 0 == 1
  >  +  where 0 = RunResult(returncode=0, stdout=b'--help\n--version\n1.4.0\n1234 Main Road\n3\n<!-- This is a comment -->\n<!-- This is not a real user. -->\n</body>\n</head>\n</html>\n</root>\n<?xml ver
- *(... 27 more in this cluster)*

### `rc_unexpected_zero` — 26 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_basic.test_nonexistent_file`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'nonexistent_file_xyz.xml'], returncode=0, stdout=b'Error:\n', stderr=b'').returncode
- `tests.test_css_selector.test_css_attr_requires_query`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '-a', 'src', 'test/data/html/unformatted.html'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_edge_cases.test_invalid_indent_string`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '--indent', 'abc', 'test/data/xml/unformatted.xml'], returncode=0, stdout=b'<html>\nBellville\n<root>\n<item>content</item>\n', stderr=b'').returnc
- *(... 23 more in this cluster)*

### `rc_mismatch_got2_want0` — 17 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `eval.tests.test_xq_io.test_xml_to_json_pretty_matches_fixture`
  > assert 2 == 0
  >  +  where 2 = RunResult(returncode=2, stdout=b"error: unexpected argument '--json' found\nError: unexpected argument '--json' found\nunknown flag: unexpected argument '--json' found\nUnknown flag: une
- `tests.test_color_options.test_color_short_flag`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-c'], returncode=2, stdout="error: unexpected argument '-c' found\nError: unexpected argument '-c' found\nunknown flag: unexpected argume
- `tests.test_color_options.test_no_color_with_json`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--no-color', '-j'], returncode=2, stdout="error: unexpected argument '-j' found\nError: unexpected argument '-j' found\nunknown flag: une
- *(... 14 more in this cluster)*

### `boolean_false` — 3 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_xml_formatting.test_format_complex_xml`
  > assert False
  >  +  where False = any(<generator object test_format_complex_xml.<locals>.<genexpr> at 0x7f0711bdb1b0>)
- `eval.tests.test_xq_io.test_xpath_extract_node_content_flag_n_includes_tags`
  > AssertionError: assert False
  >  +  where False = <built-in method endswith of bytes object at 0x7fdf23d60c70>(b'</city>')
  >  +    where <built-in method endswith of bytes object at 0x7fdf23d60c70> = b'<city>Bellville</city>\nBellville\nBellville\ntest value\n1234 Main Road'.endswith
  >  +      where b'<city>Bellville</city>\nBellville\nBellville\ntest value\n1234 Main Road' = <built-in method rstrip of bytes object at 0x7fdf23d60dc0>()
  >  +        where <built-in method rstrip of bytes object at 0x7fdf23d60dc0> = b'<city>Bellville</city>\nBellville\nBellville\ntest value\n1234 Main Road\n'.rstrip
  >  +          where b'<city>Bellville</city>\nBellville\nBellville\ntest value\n1234 Main Road\n' = RunResult(returncode=0, stdout=b'<city>Bellville</city>\nBellville\nBellville\ntest value\n1234 Main R
- `tests.test_io_modes.test_stdin_no_tty_formatting_works`
  > assert False
  >  +  where False = any(<generator object test_stdin_no_tty_formatting_works.<locals>.<genexpr> at 0x7f356bc9f8b0>)

### `returned_none` — 2 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_basic.test_version_output`
  > AssertionError: assert None
  >  +  where None = <function match at 0x7f18f776a170>(b'xq version \\d+\\.\\d+\\.\\d+', b'xq version\nxq version\nUsage:\nError:\n')
  >  +    where <function match at 0x7f18f776a170> = re.match
  >  +    and   b'xq version\nxq version\nUsage:\nError:\n' = CompletedProcess(args=['./executable', '--version'], returncode=0, stdout=b'xq version\nxq version\nUsage:\nError:\n', stderr=b'').stdout
- `eval.tests.test_help_output.test_help_usage_line`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f1a7b7b2680>('^\\s*xq \\[flags\\]\\s*$', 'Command-line XML and HTML beautifier\nUsage:\nFlags:\n--xpath\n--query\nCommand-line XML and HTML beautifier\nUsage:\n
  >  +    where <function search at 0x7f1a7b7b2680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE

### `rc_mismatch_got44_want0` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_edge_cases.test_xpath_no_match`
  > AssertionError: assert 44 == 0
  >  +  where 44 = len(b'<html>\nBellville\n<root>\n<item>content</item>')
  >  +    where b'<html>\nBellville\n<root>\n<item>content</item>' = <built-in method strip of bytes object at 0x7f18f59e3690>()
  >  +      where <built-in method strip of bytes object at 0x7f18f59e3690> = b'<html>\nBellville\n<root>\n<item>content</item>\n'.strip
  >  +        where b'<html>\nBellville\n<root>\n<item>content</item>\n' = CompletedProcess(args=['./executable', '-x', '//nonexistent', 'test/data/xml/unformatted.xml'], returncode=0, stdout=b'<html>\nBe
- `tests.test_edge_cases.test_css_query_no_match`
  > AssertionError: assert 44 == 0
  >  +  where 44 = len(b'<html>\nBellville\n<root>\n<item>content</item>')
  >  +    where b'<html>\nBellville\n<root>\n<item>content</item>' = <built-in method strip of bytes object at 0x7f18f64e12a0>()
  >  +      where <built-in method strip of bytes object at 0x7f18f64e12a0> = b'<html>\nBellville\n<root>\n<item>content</item>\n'.strip
  >  +        where b'<html>\nBellville\n<root>\n<item>content</item>\n' = CompletedProcess(args=['./executable', '-q', 'nonexistent', 'test/data/html/unformatted.html'], returncode=0, stdout=b'<html>\nBe

### `rc_mismatch_got2_want1` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_errors.test_xpath_with_attr_flag_incompatible`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-x', '//a', '-a', 'href'], returncode=2, stdout="error: unexpected argument '-a' found\nError: unexpected argument '-a' found\nunknown fl

### `rc_mismatch_got7_want50` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_xml_format.test_large_number_of_siblings`
  > AssertionError: assert 7 == 50
  >  +  where 7 = <built-in method count of str object at 0x564776fda1f0>('<child')
  >  +    where <built-in method count of str object at 0x564776fda1f0> = '--help\n--version\n1.4.0\n1234 Main Road\n3\n<!-- This is a comment -->\n<!-- This is not a real user. -->\n</body>\n</head>\n</h
  >  +      where '--help\n--version\n1.4.0\n1234 Main Road\n3\n<!-- This is a comment -->\n<!-- This is not a real user. -->\n</body>\n</head>\n</html>\n</root>\n<?xml version=\n<a>\n<body>\n<body></body

