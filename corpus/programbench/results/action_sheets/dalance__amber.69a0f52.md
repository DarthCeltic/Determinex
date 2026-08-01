# Action Sheet — dalance__amber.69a0f52

**Current:** 16.59%  (144/868)
**Pass / Fail / Skip:** 144 / 198 / 0
**Gap to 100%:** 83.41 percentage points (724 tests)

## Failure clusters

198 failed tests grouped into 8 buckets (sorted by count).

### `other_assertion` — 94 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_comprehensive.test_single_file_replacement`
  > AssertionError: assert 'hi world' in 'hello world\nhello again\n'
- `tests.test_comprehensive.test_multiple_file_paths`
  > AssertionError: assert 'TEST data' in 'test data\n'
  >  +  where 'test data\n' = read_text()
  >  +    where read_text = PosixPath('/tmp/tmp7q6c45je/file1.txt').read_text
- `tests.test_comprehensive.test_directory_recursive_search`
  > AssertionError: assert 'FOUND here' in 'target here\n'
  >  +  where 'target here\n' = read_text()
  >  +    where read_text = PosixPath('/tmp/tmp5suqibct/dir1/file1.txt').read_text
- *(... 91 more in this cluster)*

### `rc_unexpected_zero` — 51 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_comprehensive.test_no_args_error`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable'], returncode=0, stdout=b'--VERBOSE\n--Verbose\n--no-interactive\n--regex\n--size-per-thread\n--unknown-flag\n--verbos\n--verbose\n-5\n-v\n-
- `tests.test_comprehensive.test_missing_replacement_arg`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'keyword'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_comprehensive.test_key_from_empty_file_error`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--no-interactive', '--key-from-file', '/tmp/tmpt4lmollh/empty.txt', 'replacement', '/tmp/tmpt4lmollh/target.txt'], returncode=0, stdout=b
- *(... 48 more in this cluster)*

### `string_output_mismatch` — 24 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_comprehensive.test_regex_search_basic`
  > AssertionError: assert 'MATCH\nMATCH\n' == 'test123\ntest456\n'
  >   
  >   - test123
  >   - test456
  >   + MATCH
  >   + MATCH
- `tests.test_comprehensive.test_regex_capture_groups`
  > AssertionError: assert 'bbb aaa\n' == 'aaa bbb\n'
  >   
  >   - aaa bbb
  >   + bbb aaa
- `tests.test_comprehensive.test_regex_named_capture_groups`
  > AssertionError: assert 'bbb aaa\n' == 'aaa bbb\n'
  >   
  >   - aaa bbb
  >   + bbb aaa
- *(... 21 more in this cluster)*

### `rc_mismatch_got0_want1` — 22 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `eval.tests.test_ambr_cli.test_replace_command_exits_1_and_produces_no_output`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--no-interactive', 'world', 'earth', '/tmp/pytest-of-root/pytest-0/test_replace_command_exits_1_a2/a.txt'], returncode=0, stdout='', stde
- `tests.test_replace.TestAmbrBasic.test_ambr_missing_args`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable'], returncode=0, stdout='--VERBOSE\n--Verbose\n--no-interactive\n--regex\n--size-per-thread\n--unknown-flag\n--verbos\n--verbose\n-5\n-v\n-z
- `tests.test_replace.TestAmbrBasic.test_ambr_keyword_only`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'hello'], returncode=0, stdout='--VERBOSE\n--Verbose\n--no-interactive\n--regex\n--size-per-thread\n--unknown-flag\n--verbos\n--verbose\n-
- *(... 19 more in this cluster)*

### `returned_none` — 3 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_comprehensive.test_version_format`
  > AssertionError: assert None
  >  +  where None = <function match at 0x7f8fa9b19120>(b'ambr \\d+\\.\\d+\\.\\d+', b'ambr\nUSAGE:\nKEYWORD\nREPLACEMENT\nFLAGS\n')
  >  +    where <function match at 0x7f8fa9b19120> = re.match
  >  +    and   b'ambr\nUSAGE:\nKEYWORD\nREPLACEMENT\nFLAGS\n' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'ambr\nUSAGE:\nKEYWORD\nREPLACEMENT\nFLAGS\n', stderr=b
- `eval.tests.test_help_usage.test_help_has_program_name_and_version_line`
  > AssertionError: assert None
  >  +  where None = <function fullmatch at 0x7f4a5d657e20>('ambr\\s+\\d+\\.\\d+\\.\\d+', 'USAGE:')
  >  +    where <function fullmatch at 0x7f4a5d657e20> = re.fullmatch
- `eval.tests.test_help_usage.test_version_flag_output_format`
  > AssertionError: assert None
  >  +  where None = <function fullmatch at 0x7f4a5d657e20>('ambr\\s+\\d+\\.\\d+\\.\\d+\\n?', 'ambr\nUSAGE:\nKEYWORD\nREPLACEMENT\nFLAGS\n')
  >  +    where <function fullmatch at 0x7f4a5d657e20> = re.fullmatch
  >  +    and   'ambr\nUSAGE:\nKEYWORD\nREPLACEMENT\nFLAGS\n' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout='ambr\nUSAGE:\nKEYWORD\nREPLACEMENT\nFLAGS\n', stderr='')

### `rc_mismatch_got0_want3` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_comprehensive.test_multiline_content`
  > AssertionError: assert 0 == 3
  >  +  where 0 = <built-in method count of str object at 0x7f8fa88f5650>('REPLACED')
  >  +    where <built-in method count of str object at 0x7f8fa88f5650> = 'line1: test\nline2: test\nline3: test\n'.count
- `tests.test_comprehensive.test_mixed_line_endings`
  > AssertionError: assert 0 == 3
  >  +  where 0 = <built-in method count of str object at 0x7f8fa7cf6830>('LINE')
  >  +    where <built-in method count of str object at 0x7f8fa7cf6830> = 'line1\nline2\nline3\n'.count

### `type_error` — 1 test(s)

**Quick patch ideas:**
- Specific TypeError; check arg types vs expected

**Sample failures:**

- `tests.test_comprehensive.test_crlf_line_endings`
  > TypeError: 'in <string>' requires string as left operand, not bytes

### `bytes_output_mismatch` — 1 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_replace.test_regex_capture_replace`
  > AssertionError: assert 'aaa bbb' == 'bbb aaa'
  >   
  >   - bbb aaa
  >   + aaa bbb

