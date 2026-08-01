# Action Sheet — sstadick__hck.b66c751

**Current:** 2.64%  (30/1138)
**Pass / Fail / Skip:** 30 / 825 / 1
**Gap to 100%:** 97.36 percentage points (1108 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_compression.test_zstd_decompression`
  - reason: zstd not available

## Failure clusters

825 failed tests grouped into 7 buckets (sorted by count).

### `rc_mismatch_got1_want0` — 424 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_advanced_features.test_reordering_with_overlapping_ranges`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '-f', '4,2,1-3'], returncode=1, stdout=b'', stderr=b'  File "/workspace/main.py", line 898\n    if output_file\n                  ^\nSyntaxError: e
- `tests.test_advanced_features.test_exclude_then_include_same_field`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '-f', '1-5', '-e', '3'], returncode=1, stdout=b'', stderr=b'  File "/workspace/main.py", line 898\n    if output_file\n                  ^\nSyntaxE
- `tests.test_advanced_features.test_header_selection_with_reordering`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '-F', 'city', '-F', 'name', '-F', 'age'], returncode=1, stdout=b'', stderr=b'  File "/workspace/main.py", line 898\n    if output_file\n           
- *(... 421 more in this cluster)*

### `subprocess_failed` — 298 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_delimiters.test_default_whitespace_delimiter`
  > subprocess.CalledProcessError: Command '['/workspace/executable', '-f', '1,3']' returned non-zero exit status 1.
- `tests.test_delimiters.test_regex_comma_delimiter`
  > subprocess.CalledProcessError: Command '['/workspace/executable', '-d', ',', '-f', '1,3']' returned non-zero exit status 1.
- `tests.test_delimiters.test_regex_multiple_commas`
  > subprocess.CalledProcessError: Command '['/workspace/executable', '-d', ',+', '-f', '1,3']' returned non-zero exit status 1.
- *(... 295 more in this cluster)*

### `other_assertion` — 80 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_input_handling.test_missing_file`
  > assert (b'nonexistent_file.txt' in b'  File "/workspace/main.py", line 898\n    if output_file\n                  ^\nSyntaxError: expected \':\'\n' or b'No such file' in b'  File "/workspace/main.py",
  >  +  where b'  File "/workspace/main.py", line 898\n    if output_file\n                  ^\nSyntaxError: expected \':\'\n' = CompletedProcess(args=['./executable', 'nonexistent_file.txt'], returncode=
  >  +  and   b'  File "/workspace/main.py", line 898\n    if output_file\n                  ^\nSyntaxError: expected \':\'\n' = CompletedProcess(args=['./executable', 'nonexistent_file.txt'], returncode=
- `tests.test_hck.test_nonexistent_file_error`
  > assert (b'nonexistent' in b'  File "/workspace/main.py", line 898\n    if output_file\n                  ^\nSyntaxError: expected \':\'\n' or b'No such file' in b'  File "/workspace/main.py", line 898
  >  +  where b'  File "/workspace/main.py", line 898\n    if output_file\n                  ^\nSyntaxError: expected \':\'\n' = CompletedProcess(args=['./executable', '/nonexistent/file/path.txt'], retur
  >  +  and   b'  File "/workspace/main.py", line 898\n    if output_file\n                  ^\nSyntaxError: expected \':\'\n' = CompletedProcess(args=['./executable', '/nonexistent/file/path.txt'], retur
  >  +  and   b'  file "/workspace/main.py", line 898\n    if output_file\n                  ^\nsyntaxerror: expected \':\'\n' = <built-in method lower of bytes object at 0x7f7af54516b0>()
  >  +    where <built-in method lower of bytes object at 0x7f7af54516b0> = b'  File "/workspace/main.py", line 898\n    if output_file\n                  ^\nSyntaxError: expected \':\'\n'.lower
  >  +      where b'  File "/workspace/main.py", line 898\n    if output_file\n                  ^\nSyntaxError: expected \':\'\n' = CompletedProcess(args=['./executable', '/nonexistent/file/path.txt'], r
- `tests.test_hck.test_nonexistent_header_error`
  > assert (b'nonexistent' in b'  File "/workspace/main.py", line 898\n    if output_file\n                  ^\nSyntaxError: expected \':\'\n' or b'header' in b'  file "/workspace/main.py", line 898\n    
  >  +  where b'  File "/workspace/main.py", line 898\n    if output_file\n                  ^\nSyntaxError: expected \':\'\n' = CompletedProcess(args=['./executable', '-F', 'nonexistent'], returncode=1, 
  >  +  and   b'  file "/workspace/main.py", line 898\n    if output_file\n                  ^\nsyntaxerror: expected \':\'\n' = <built-in method lower of bytes object at 0x7f7af6ad4e40>()
  >  +    where <built-in method lower of bytes object at 0x7f7af6ad4e40> = b'  File "/workspace/main.py", line 898\n    if output_file\n                  ^\nSyntaxError: expected \':\'\n'.lower
  >  +      where b'  File "/workspace/main.py", line 898\n    if output_file\n                  ^\nSyntaxError: expected \':\'\n' = CompletedProcess(args=['./executable', '-F', 'nonexistent'], returncode
- *(... 77 more in this cluster)*

### `rc_mismatch_got1_want2` — 11 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_argparse_validation.test_unknown_flag_errors_with_rc_2[--no-such-flag]`
  > assert 1 == 2
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '--no-such-flag'], returncode=1, stdout='', stderr='  File "/workspace/main.py", line 898\n    if output_file\n                  ^\nSyntax
- `eval.tests.test_argparse_validation.test_unknown_flag_errors_with_rc_2[--unknown]`
  > assert 1 == 2
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '--unknown'], returncode=1, stdout='', stderr='  File "/workspace/main.py", line 898\n    if output_file\n                  ^\nSyntaxError
- `eval.tests.test_argparse_validation.test_unknown_flag_errors_with_rc_2[--nonexistent-flag]`
  > assert 1 == 2
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '--nonexistent-flag'], returncode=1, stdout='', stderr='  File "/workspace/main.py", line 898\n    if output_file\n                  ^\nSy
- *(... 8 more in this cluster)*

### `string_output_mismatch` — 10 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_delimiters.test_invalid_regex_delimiter_error`
  > assert '  File "/wor...ected \':\'\n' == 'Error: regex...losed group\n'
  >   
  >   - Error: regex parse error:
  >   -     (
  >   -     ^
  >   - error: unclosed group
  >   +   File "/workspace/main.py", line 898
  >   +     if output_file
- `tests.test_delimiters.test_field_zero_error`
  > assert '  File "/wor...ected \':\'\n' == 'Fields and p...d from 1: 0\n'
  >   
  >   - Fields and positions are numbered from 1: 0
  >   +   File "/workspace/main.py", line 898
  >   +     if output_file
  >   +                   ^
  >   + SyntaxError: expected ':'
- `tests.test_edge_cases.test_invalid_regex_delimiter_error`
  > assert '  File "/wor...ected \':\'\n' == 'Error: regex...losed group\n'
  >   
  >   - Error: regex parse error:
  >   -     (
  >   -     ^
  >   - error: unclosed group
  >   +   File "/workspace/main.py", line 898
  >   +     if output_file
- *(... 7 more in this cluster)*

### `boolean_false` — 1 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `eval.tests.test_help_usage.test_help_outputs_end_with_newline`
  > assert False
  >  +  where False = <built-in method endswith of str object at 0x7f0e42cdc030>('\n')
  >  +    where <built-in method endswith of str object at 0x7f0e42cdc030> = ''.endswith
  >  +      where '' = normalize_newlines('')
  >  +        where '' = CompletedProcess(args=['/workspace/executable', '--help'], returncode=1, stdout='', stderr='  File "/workspace/main.py", line 898\n    if output_file\n                  ^\nSyntaxE

### `returned_none` — 1 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_usage.test_long_help_has_indented_multiline_argument_description`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f0e42c52680>('\\[INPUT\\]\\.\\.\\.\\n\\s+Input files to parse, defaults to stdin\\.', '')
  >  +    where <function search at 0x7f0e42c52680> = re.search

