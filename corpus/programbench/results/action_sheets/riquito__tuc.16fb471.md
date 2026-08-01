# Action Sheet — riquito__tuc.16fb471

**Current:** 8.64%  (155/1793)
**Pass / Fail / Skip:** 155 / 931 / 4
**Gap to 100%:** 91.36 percentage points (1638 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_harvest.test_fails_to_cut_characters_when_no_regex_support`
  - reason: Binary has regex support - this test is for no-regex builds
- `tests.test_harvest.test_does_not_panic_if_attempting_to_use_regex_arg_with_noregex_build`
  - reason: Binary has regex support - this test is for no-regex builds
- `tests.test_harvest.test_cannot_use_characters_without_regex`
  - reason: Binary has regex support - this test is for no-regex builds
- `tests.test_input_advanced.test_unreadable_file_permission_error`
  - reason: Permission test not applicable in root containers

## Failure clusters

931 failed tests grouped into 24 buckets (sorted by count).

### `bytes_output_mismatch` — 284 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_additional_coverage.test_zero_terminated_multiline`
  > assert b'a\x00c\x00' == b"e.g. cuttin...c-d' on '-'\n"
  >   
  >   At index 0 diff: b'a' != b'e'
  >   
  >   Full diff:
  >   - (b"e.g. cutting the string 'a-b-c-d' on '-'\n")
  >   + b'a\x00c\x00'
- `tests.test_basic_invocation.test_empty_stdin`
  > assert b"e.g. cuttin...c-d' on '-'\n" == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b"e.g. cutting the string 'a-b-c-d' on '-'\n")
- `tests.test_character_cutting.test_single_character`
  > assert b"e.g. cuttin...c-d' on '-'\n" == b'a\n'
  >   
  >   At index 0 diff: b'e' != b'a'
  >   
  >   Full diff:
  >   - b'a\n'
  >   + (b"e.g. cutting the string 'a-b-c-d' on '-'\n")
- *(... 281 more in this cluster)*

### `other_assertion` — 250 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_additional_coverage.test_help_to_stderr_on_invalid_usage`
  > assert b"doesn't have an associated value" in b"tuc: error: a value is required for '-f <VALUE>'\n"
  >  +  where b"tuc: error: a value is required for '-f <VALUE>'\n" = CompletedProcess(args=['./executable', '-f'], returncode=2, stdout=b'', stderr=b"tuc: error: a value is required for '-f <VALUE>'\n").
- `tests.test_additional_coverage.test_bytes_extraction_extended`
  > assert b'hello' in b"e.g. cutting the string 'a-b-c-d' on '-'\n"
  >  +  where b"e.g. cutting the string 'a-b-c-d' on '-'\n" = CompletedProcess(args=['./executable', '-b', '1:5'], returncode=0, stdout=b"e.g. cutting the string 'a-b-c-d' on '-'\n", stderr=b'').stdout
- `tests.test_additional_coverage.test_complement_with_multiline`
  > assert b'f' in b"e.g. cutting the string 'a-b-c-d' on '-'\n"
  >  +  where b"e.g. cutting the string 'a-b-c-d' on '-'\n" = CompletedProcess(args=['./executable', '-d', ',', '-f', '2', '-m'], returncode=0, stdout=b"e.g. cutting the string 'a-b-c-d' on '-'\n", stderr
- *(... 247 more in this cluster)*

### `string_output_mismatch` — 208 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_json_comprehensive.test_json_with_negative_index`
  > AssertionError: assert {'args': ['--...'tool': 'tuc'} == ['d', 'c']
  >   
  >   Full diff:
  >   - [
  >   + {
  >   +     'args': [
  >   +         '--json',
  >   -     'd',...
- `tests.test_json_comprehensive.test_json_unicode`
  > AssertionError: assert {'args': ['--...'tool': 'tuc'} == ['hello', '世界']
  >   
  >   Full diff:
  >   - [
  >   -     'hello',
  >   -     '世界',
  >   - ]
  >   + {...
- `tests.test_json_comprehensive.test_json_newline_in_field`
  > AssertionError: assert {'args': ['--...'tool': 'tuc'} == ['abc']
  >   
  >   Full diff:
  >   - [
  >   -     'abc',
  >   - ]
  >   + {
  >   +     'args': [...
- *(... 205 more in this cluster)*

### `rc_unexpected_zero` — 70 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_basic_invocation.test_nonexistent_file_error`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '-f', '1', '/nonexistent/file.txt'], returncode=0, stdout=b"e.g. cutting the string 'a-b-c-d' on '-'\n", stderr=b'').returncode
- `tests.test_error_combinations.test_json_with_no_join_conflict`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '--json', '--no-join', '-f', '1'], returncode=0, stdout=b'{\n  "tool": "tuc",\n  "args": [\n    "--json",\n    "--no-join",\n    "-f",\n    "1"\n  
- `tests.test_error_combinations.test_json_with_replace_conflict`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '--json', '-r', ',', '-f', '1'], returncode=0, stdout=b'{\n  "tool": "tuc",\n  "args": [\n    "--json",\n    "-r",\n    ",",\n    "-f",\n    "1"\n 
- *(... 67 more in this cluster)*

### `rc_mismatch_got0_want1` — 42 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_char_byte_line.test_char_out_of_bounds_error`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-c', '100'], returncode=0, stdout=b"e.g. cutting the string 'a-b-c-d' on '-'\n", stderr=b'').returncode
- `tests.test_char_byte_line.test_line_out_of_bounds_error`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-l', '100'], returncode=0, stdout=b"e.g. cutting the string 'a-b-c-d' on '-'\n", stderr=b'').returncode
- `tests.test_fields.test_out_of_bounds_without_fallback_fails`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-f', '1,5'], returncode=0, stdout=b"e.g. cutting the string 'a-b-c-d' on '-'\n", stderr=b'').returncode
- *(... 39 more in this cluster)*

### `rc_mismatch_got2_want0` — 21 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_fallback.test_empty_fallback`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '-d', '/', '-f', '2', '--fallback-oob='], returncode=2, stdout=b'', stderr=b"tuc: error: a value is required for '--fallback-oob <VALUE>'\n").retur
- `tests.test_mmap_file_input.test_file_input_no_mmap`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--no-mmap', '-d', ',', '-f', '1', '/tmp/tmpz6ef7twz.txt'], returncode=2, stdout=b'', stderr=b'tuc: error: unrecognized argument: --no-mmap\n').ret
- `tests.test_termination_and_fallback.test_empty_fallback`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '-d', ',', '-f', '1,5', '--fallback-oob='], returncode=2, stdout=b'', stderr=b"tuc: error: a value is required for '--fallback-oob <VALUE>'\n").ret
- *(... 18 more in this cluster)*

### `rc_mismatch_got2_want1` — 19 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_options_stream_gaps.test_fixed_memory_zero_error`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--fixed-memory', '0', '-f', '1'], returncode=2, stdout=b'', stderr=b'tuc: error: unrecognized argument: --fixed-memory\n').returncode
- `tests.test_options_stream_gaps.test_replace_no_join_error`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--replace-delimiter', ',', '--no-join', '-f', '1'], returncode=2, stdout=b'', stderr=b'tuc: error: unrecognized argument: --replace-delim
- `tests.test_options_stream_gaps.test_fixed_memory_multibyte_delimiter_error`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--fixed-memory', '1024', '-f', '1,3', '-d', '--'], returncode=2, stdout=b'', stderr=b'tuc: error: unrecognized argument: --fixed-memory\n
- *(... 16 more in this cluster)*

### `rc_mismatch_got1_want0` — 5 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_basic_invocation.test_no_arguments_stdin`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable'], returncode=1, stdout=b'', stderr=b'usage: tuc [OPTIONS] [ARGS]\n').returncode
- `tests.test_basic_invocation.test_short_help_without_arguments`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable'], returncode=1, stdout=b'', stderr=b'usage: tuc [OPTIONS] [ARGS]\n').returncode
- `tests.test_harvest.test_display_short_help_when_run_without_arguments`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable'], returncode=1, stdout=b'', stderr=b'usage: tuc [OPTIONS] [ARGS]\n').returncode
- *(... 2 more in this cluster)*

### `rc_mismatch_got1_want2` — 5 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_complement_advanced.test_complement_multiline`
  > assert 1 == 2
  >  +  where 1 = len([b"e.g. cutting the string 'a-b-c-d' on '-'"])
- `tests.test_format_strings.test_format_multiline`
  > assert 1 == 2
  >  +  where 1 = len([b"e.g. cutting the string 'a-b-c-d' on '-'"])
- `tests.test_line_terminators.test_default_lf_terminator`
  > assert 1 == 2
  >  +  where 1 = len([b"e.g. cutting the string 'a-b-c-d' on '-'"])
- *(... 2 more in this cluster)*

### `boolean_false` — 5 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_json_edge_cases.test_json_array_structure`
  > AssertionError: assert False
  >  +  where False = isinstance({'args': ['--json', '-d', ',', '-f', '1:5'], 'result': 'ok', 'tool': 'tuc'}, list)
- `tests.test_json_edge_cases.test_json_format_consistency`
  > assert False
  >  +  where False = <built-in method startswith of str object at 0x7387ea86c990>('[')
  >  +    where <built-in method startswith of str object at 0x7387ea86c990> = '{\n  "tool": "tuc",\n  "args": [\n    "--json",\n    "-d",\n    ",",\n    "-f",\n    "1,2"\n  ],\n  "result": "ok"\n}'.start
- `tests.test_output_modifiers.test_json_output`
  > AssertionError: assert False
  >  +  where False = isinstance({'args': ['-d', '-', '-f', '1,2,3', '--json'], 'result': 'ok', 'tool': 'tuc'}, list)
- *(... 2 more in this cluster)*

### `rc_mismatch_got11_want2` — 4 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_json_comprehensive.test_json_multiline`
  > assert 11 == 2
  >  +  where 11 = len([b'{', b'  "tool": "tuc",', b'  "args": [', b'    "--json",', b'    "-d",', b'    ",",', ...])
- `tests.test_output_modifiers.test_json_output_multiline`
  > assert 11 == 2
  >  +  where 11 = len([b'{', b'  "tool": "tuc",', b'  "args": [', b'    "-d",', b'    "-",', b'    "-f",', ...])
- `tests.test_output_and_filtering.test_json_with_multiline`
  > assert 11 == 2
  >  +  where 11 = len(['{', '  "tool": "tuc",', '  "args": [', '    "-d",', '    ",",', '    "-f",', ...])
- *(... 1 more in this cluster)*

### `missing_dict_key` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_json_edge_cases.test_json_large_fields`
  > KeyError: 0
- `tests.test_output_and_filtering.test_json_with_empty_fields`
  > KeyError: 0
- `tests.test_output_and_filtering.test_json_with_unicode`
  > KeyError: 0

### `empty_list_or_string` — 2 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_line_terminators.test_zero_terminated`
  > IndexError: list index out of range
- `tests.test_termination_and_fallback.test_zero_terminated`
  > IndexError: list index out of range

### `rc_mismatch_got1_want3` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_only_delimited_scenarios.test_only_delimited_all_match`
  > assert 1 == 3
  >  +  where 1 = len([b"e.g. cutting the string 'a-b-c-d' on '-'"])
- `tests.test_termination_and_fallback.test_default_line_termination`
  > assert 1 == 3
  >  +  where 1 = len([b"e.g. cutting the string 'a-b-c-d' on '-'"])

### `rc_mismatch_got1_want10000` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_input_advanced.test_large_file_with_mmap`
  > assert 1 == 10000
  >  +  where 1 = len(["e.g. cutting the string 'a-b-c-d' on '-'"])
- `tests.test_input_advanced.test_large_file_with_no_mmap`
  > assert 1 == 10000
  >  +  where 1 = len(["e.g. cutting the string 'a-b-c-d' on '-'"])

### `rc_mismatch_got1_want10` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_fixed_memory_advanced.test_fixed_memory_multiline`
  > assert 1 == 10
  >  +  where 1 = len([b"e.g. cutting the string 'a-b-c-d' on '-'"])

### `rc_mismatch_got12_want2` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_greedy_compress.test_compress_multiline`
  > assert 12 == 2
  >  +  where 12 = len([b'{', b'  "tool": "tuc",', b'  "args": [', b'    "-d",', b'    ",",', b'    "-p",', ...])

### `rc_mismatch_got3_want100` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_json_edge_cases.test_json_many_fields`
  > AssertionError: assert 3 == 100
  >  +  where 3 = len({'args': ['--json', '-d', ',', '-f', '1:100'], 'result': 'ok', 'tool': 'tuc'})

### `rc_mismatch_got0_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_field_selection.test_duplicate_field_selection`
  > assert 0 == 3
  >  +  where 0 = <built-in method count of bytes object at 0x7e7f659f4bc0>(b'repeat')
  >  +    where <built-in method count of bytes object at 0x7e7f659f4bc0> = b"e.g. cutting the string 'a-b-c-d' on '-'\n".count
  >  +      where b"e.g. cutting the string 'a-b-c-d' on '-'\n" = CompletedProcess(args=['./executable', '-d', ',', '-f', '1,1,1'], returncode=0, stdout=b"e.g. cutting the string 'a-b-c-d' on '-'\n", stde

### `rc_mismatch_got9_want2` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_fields.test_json_output_multiline`
  > assert 9 == 2
  >  +  where 9 = len(['{', '  "tool": "tuc",', '  "args": [', '    "-f",', '    "1,2,3",', '    "--json"', ...])

### `rc_mismatch_got1_want50000` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_input_advanced.test_large_file_stress_test_performance`
  > assert 1 == 50000
  >  +  where 1 = len(["e.g. cutting the string 'a-b-c-d' on '-'"])

### `rc_mismatch_got1_want4` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_input_advanced.test_mixed_line_lengths_in_single_file`
  > assert 1 == 4
  >  +  where 1 = len(["e.g. cutting the string 'a-b-c-d' on '-'"])

### `rc_mismatch_got41_want1000` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_input_advanced.test_bytes_mode_large_range`
  > assert 41 == 1000
  >  +  where 41 = len(b"e.g. cutting the string 'a-b-c-d' on '-'\n")
  >  +    where b"e.g. cutting the string 'a-b-c-d' on '-'\n" = CompletedProcess(args=['/workspace/executable', '-b', '1:1000'], returncode=0, stdout=b"e.g. cutting the string 'a-b-c-d' on '-'\n", stderr=

### `json_output_missing_or_bad` — 1 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `tests.test_tuc.TestFlags.test_json_output_multiple_lines`
  > json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)

