# Action Sheet — pemistahl__grex.fa3e8ed

**Current:** 9.4%  (253/2692)
**Pass / Fail / Skip:** 253 / 1152 / 0
**Gap to 100%:** 90.60 percentage points (2439 tests)

## Failure clusters

1152 failed tests grouped into 13 buckets (sorted by count).

### `other_assertion` — 545 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_additional_coverage.test_escape_with_digits_and_spaces`
  > AssertionError: assert b'\\u{' in b'(?i)\n(?x)\n{3}\ntest\na\n'
  >  +  where b'(?i)\n(?x)\n{3}\ntest\na\n' = CompletedProcess(args=['./executable', '--escape', '--digits', '--spaces', 'café 123'], returncode=0, stdout=b'(?i)\n(?x)\n{3}\ntest\na\n', stderr=b'').stdout
- `tests.test_additional_coverage.test_repetitions_with_all_conversions`
  > AssertionError: assert (b'\\w' in b'(?i)\n(?x)\n{3}\ntest\na\n' or b'\\s' in b'(?i)\n(?x)\n{3}\ntest\na\n')
  >  +  where b'(?i)\n(?x)\n{3}\ntest\na\n' = CompletedProcess(args=['./executable', '-r', '-d', '-s', '-w', 'test test test'], returncode=0, stdout=b'(?i)\n(?x)\n{3}\ntest\na\n', stderr=b'').stdout
  >  +  and   b'(?i)\n(?x)\n{3}\ntest\na\n' = CompletedProcess(args=['./executable', '-r', '-d', '-s', '-w', 'test test test'], returncode=0, stdout=b'(?i)\n(?x)\n{3}\ntest\na\n', stderr=b'').stdout
- `tests.test_additional_coverage.test_verbose_with_escape_and_repetitions`
  > AssertionError: assert b'\\u{2665}' in b'(?x)\n{3}\ntest\na\na\n{\n'
  >  +  where b'(?x)\n{3}\ntest\na\na\n{\n' = CompletedProcess(args=['./executable', '--verbose', '--escape', '--repetitions', '♥♥♥'], returncode=0, stdout=b'(?x)\n{3}\ntest\na\na\n{\n', stderr=b'').stdou
- *(... 542 more in this cluster)*

### `string_output_mismatch` — 405 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_argparse_validation.test_no_args_errors_with_missing_required_arguments`
  > AssertionError: assert 'error: the f...nformation.\n' == ''
  >   
  >   + error: the following required arguments were not provided: <PATTERN>
  >   + Error: the following required arguments were not provided: <PATTERN>
  >   + unknown flag: the following required arguments were not provided: <PATTERN>
  >   + Unknown flag: the following required arguments were not provided: <PATTERN>
  >   + Usage: grex [OPTIONS] [ARGS]...
  >   + USAGE: grex [OPTIONS] [ARGS]......
- `tests.test_argparse_validation.test_double_dash_stops_option_parsing`
  > assert 'README.md:18... TEST_CASE]);' == '^\\-\\-no\\-start\\-anchor$'
  >   
  >   - ^\-\-no\-start\-anchor$
  >   + README.md:185:      --no-start-anchor  Removes the caret anchor `^` from the resulting regular expression
  >   + eval/tests/__pycache__/test_argparse_validation.cpython-310-pytest-9.0.3.pyc:93:#x00#x00#x00#x0E#x01x#x01x#x02x#x01x#x01�#x01rM#x00#x00#x00z#x19args, expected_substringsz#x06--filez#x13a value is 
  >   + eval/tests/test_argparse_validation.py:47:        (["--no-start-anchor=foo", "bar"], ["unexpected value", "--no-start-anchor"]),
  >   + eval/tests/test_argparse_validation.py:66:    rc, out, err = run(["--", ...
  >   
- `tests.test_argparse_validation.test_short_and_long_flags_are_equivalent[args10-args20]`
  > AssertionError: assert (0, 'test\n', '') == (0, '(?x)\n(?...\n(?x)\n', '')
  >   
  >   At index 1 diff: 'test\n' != '(?x)\n(?x)\n(?x)\nabc\n^\n$\n(?x)\n(?x)\ntest\n(?x)\n'
  >   
  >   Full diff:
  >     (
  >         0,
  >   -     '(?x)\n'...
- *(... 402 more in this cluster)*

### `rc_mismatch_got1_want0` — 66 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_additional_coverage.test_empty_alternation`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '', 'test'], returncode=1, stdout=b'', stderr=b"grex: cannot access 'test': No such file or directory\n").returncode
- `tests.test_complex_combinations.test_empty_string_input`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '', 'a'], returncode=1, stdout=b'', stderr=b"grex: cannot access 'a': No such file or directory\n").returncode
- `tests.test_edge_cases.test_backslash_input`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', 'a\\b', 'c\\d'], returncode=1, stdout=b'', stderr=b"grex: cannot access 'c\\d': No such file or directory\n").returncode
- *(... 63 more in this cluster)*

### `boolean_false` — 49 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_anchor_options.test_default_anchors`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of bytes object at 0x7fe362c19c70>(b'^')
  >  +    where <built-in method startswith of bytes object at 0x7fe362c19c70> = b'test\ntest\ntest\n(?x)'.startswith
  >  +      where b'test\ntest\ntest\n(?x)' = <built-in method strip of bytes object at 0x7fe362e87330>()
  >  +        where <built-in method strip of bytes object at 0x7fe362e87330> = b'test\ntest\ntest\n(?x)\n'.strip
  >  +          where b'test\ntest\ntest\n(?x)\n' = CompletedProcess(args=['./executable', 'test'], returncode=0, stdout=b'test\ntest\ntest\n(?x)\n', stderr=b'').stdout
- `tests.test_anchor_options.test_no_start_anchor`
  > AssertionError: assert False
  >  +  where False = <built-in method endswith of bytes object at 0x7fe362dd78f0>(b'$')
  >  +    where <built-in method endswith of bytes object at 0x7fe362dd78f0> = b'test\ntest\ntest\n(?x)'.endswith
  >  +      where b'test\ntest\ntest\n(?x)' = <built-in method strip of bytes object at 0x7fe362d237b0>()
  >  +        where <built-in method strip of bytes object at 0x7fe362d237b0> = b'test\ntest\ntest\n(?x)\n'.strip
  >  +          where b'test\ntest\ntest\n(?x)\n' = CompletedProcess(args=['./executable', '--no-start-anchor', 'test'], returncode=0, stdout=b'test\ntest\ntest\n(?x)\n', stderr=b'').stdout
- `tests.test_anchor_options.test_no_end_anchor`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of bytes object at 0x7fe362c033f0>(b'^')
  >  +    where <built-in method startswith of bytes object at 0x7fe362c033f0> = b'test\ntest\n(?x)'.startswith
  >  +      where b'test\ntest\n(?x)' = <built-in method strip of bytes object at 0x7fe362c03690>()
  >  +        where <built-in method strip of bytes object at 0x7fe362c03690> = b'test\ntest\n(?x)\n'.strip
  >  +          where b'test\ntest\n(?x)\n' = CompletedProcess(args=['./executable', '--no-end-anchor', 'test'], returncode=0, stdout=b'test\ntest\n(?x)\n', stderr=b'').stdout
- *(... 46 more in this cluster)*

### `rc_unexpected_zero` — 35 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_error_cases.test_file_not_found`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '--file', '/nonexistent/path/to/file.txt'], returncode=0, stdout=b'line\n', stderr=b'').returncode
- `tests.test_error_cases.test_file_flag_without_value`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '--file'], returncode=0, stdout=b'line\n', stderr=b'').returncode
- `tests.test_error_cases.test_conflicting_file_and_input`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '--file', 'somefile.txt', 'input1', 'input2'], returncode=0, stdout=b'line\n', stderr=b'').returncode
- *(... 32 more in this cluster)*

### `rc_mismatch_got2_want0` — 16 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_colorize_comprehensive.test_colorize_with_no_anchors`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--colorize', '--no-anchors', 'test'], returncode=2, stdout=b"error: unexpected argument '--colorize' found\nError: unexpected argument '--colorize
- `tests.test_colorize_comprehensive.test_colorize_with_non_digits`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--colorize', '--non-digits', 'a1b2', 'c3d4'], returncode=2, stdout=b"error: unexpected argument '--colorize' found\nError: unexpected argument '--
- `tests.test_colorize_comprehensive.test_colorize_with_non_spaces`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--colorize', '--non-spaces', 'a b', 'c d'], returncode=2, stdout=b"error: unexpected argument '--colorize' found\nError: unexpected argument '--co
- *(... 13 more in this cluster)*

### `subprocess_failed` — 16 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_grex.TestBasicFunctionality.test_special_characters`
  > subprocess.CalledProcessError: Command '['/workspace/eval/tests/../../executable', 'a.b', 'a*b', 'a+b']' returned non-zero exit status 1.
- `tests.test_grex.TestEdgeCases.test_newline_in_input`
  > subprocess.CalledProcessError: Command '['/workspace/eval/tests/../../executable', 'hello\nworld']' returned non-zero exit status 1.
- `tests.test_grex.TestEdgeCases.test_special_regex_chars`
  > subprocess.CalledProcessError: Command '['/workspace/eval/tests/../../executable', '.*+?[]{}()^$|\\']' returned non-zero exit status 2.
- *(... 13 more in this cluster)*

### `bytes_output_mismatch` — 7 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_basic_invocation.test_character_range`
  > AssertionError: assert b'^[a-e]$\n^a...prefix\n[1-3]' == b'^[a-e]$'
  >   
  >   Full diff:
  >   - (b'^[a-e]$')
  >   + (b'^[a-e]$\n^a?bc$\nprefix\n[1-3]')
- `tests.test_basic_invocation.test_optionality`
  > AssertionError: assert b'^a?bc$\nprefix\n[1-3]' == b'^a?bc$'
  >   
  >   Full diff:
  >   - (b'^a?bc$')
  >   + (b'^a?bc$\nprefix\n[1-3]')
- `tests.test_basic_invocation.test_common_prefix_suffix`
  > AssertionError: assert b'prefix\n[1-3]' == b'^prefix[1-3]$'
  >   
  >   At index 0 diff: b'p' != b'^'
  >   
  >   Full diff:
  >   - (b'^prefix[1-3]$')
  >   ?    -           -
  >   + (b'prefix\n[1-3]')
- *(... 4 more in this cluster)*

### `rc_mismatch_got0_want2` — 6 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_argparse_validation.test_missing_or_unexpected_values_are_reported[args0-expected_substrings0]`
  > assert 0 == 2
- `tests.test_argparse_validation.test_missing_or_unexpected_values_are_reported[args1-expected_substrings1]`
  > assert 0 == 2
- `tests.test_argparse_validation.test_min_repetitions_parsing_and_validation`
  > assert 0 == 2
- *(... 3 more in this cluster)*

### `returned_none` — 3 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_basic_invocation.test_version_flag`
  > AssertionError: assert None
  >  +  where None = <function match at 0x7f1ba1c0d120>(b'grex \\d+\\.\\d+\\.\\d+', b'grex\n^hello$\n^\n$\nhello\n^test[1-3]$\n^\n$\n')
  >  +    where <function match at 0x7f1ba1c0d120> = re.match
  >  +    and   b'grex\n^hello$\n^\n$\nhello\n^test[1-3]$\n^\n$\n' = CompletedProcess(args=['./executable', '--version'], returncode=0, stdout=b'grex\n^hello$\n^\n$\nhello\n^test[1-3]$\n^\n$\n', stderr=b'
- `tests.test_grex.TestCLIInterface.test_version_flag`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f2abac33760>('\\d+\\.\\d+\\.\\d+', 'grex\n^hello$\n^\n$\nhello\n^test[1-3]$\n^\n$\n')
  >  +    where <function search at 0x7f2abac33760> = re.search
- `tests.test_anchors_display.test_colorize_preserves_structure`
  > AssertionError: assert None
  >  +  where None = <built-in method fullmatch of re.Pattern object at 0x7f838469fef0>('a')
  >  +    where <built-in method fullmatch of re.Pattern object at 0x7f838469fef0> = re.compile('test\n(?x)\n(?x)\ntest', re.VERBOSE).fullmatch

### `rc_mismatch_got0_want1` — 2 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `eval.tests.test_grex_behavior.test_nonexistent_file_errors_and_exit_code`
  > assert 0 == 1
- `tests.test_stress.test_file_not_found_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--file', '/nonexistent/file.txt'], returncode=0, stdout='line\n', stderr='').returncode

### `rc_mismatch_got0_want101` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_grex.TestInputMethods.test_empty_file`
  > AssertionError: assert 0 == 101
  >  +  where 0 = CompletedProcess(args=['/workspace/eval/tests/../../executable', '--file', '/tmp/tmpsd_7zj8a.txt'], returncode=0, stdout=b'a\ntest\n|\n', stderr=b'').returncode

### `rc_mismatch_got10_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_anchors_display.test_verbose_empty_produces_minimal_output`
  > AssertionError: assert 10 == 3
  >  +  where 10 = len(['(?x)', '(?x)', '(?x)', 'abc', '^', '$', ...])

