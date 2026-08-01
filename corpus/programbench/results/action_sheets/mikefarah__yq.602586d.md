# Action Sheet — mikefarah__yq.602586d

**Current:** 0.35%  (8/2307)
**Pass / Fail / Skip:** 8 / 649 / 0
**Gap to 100%:** 99.65 percentage points (2299 tests)

## Failure clusters

649 failed tests grouped into 13 buckets (sorted by count).

### `rc_mismatch_got2_want0` — 211 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_advanced_features.test_load_yaml_file`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-n', 'load("/tmp/tmp_6n31a_8/loaded.yaml").x'], returncode=2, stdout=b'', stderr=b"yq: unknown option: -n\nusage: yq [OPTIONS] [ARGS]\nTr
- `tests.test_advanced_features.test_load_json_file`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-n', 'load("/tmp/tmpfynz889y/loaded.json").x'], returncode=2, stdout=b'', stderr=b"yq: unknown option: -n\nusage: yq [OPTIONS] [ARGS]\nTr
- `tests.test_advanced_features.test_strload_file`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-n', 'strload("/tmp/tmpvbw75ak8/loaded.txt")'], returncode=2, stdout=b'', stderr=b"yq: unknown option: -n\nusage: yq [OPTIONS] [ARGS]\nTr
- *(... 208 more in this cluster)*

### `other_assertion` — 196 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_advanced_features.test_multiple_doc_read_all`
  > AssertionError: assert b'first' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', '.a'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_advanced_features.test_multiple_doc_separator_present`
  > AssertionError: assert b'---' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', '.'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_advanced_features.test_multiple_doc_select`
  > AssertionError: assert b'second' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', 'select(documentIndex == 1) | .a'], returncode=0, stdout=b'', stderr=b'').stdout
- *(... 193 more in this cluster)*

### `string_output_mismatch` — 184 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_operators.test_sort_array`
  > AssertionError: assert [] == ['1', '2', '3']
  >   
  >   Right contains 3 more items, first extra item: '1'
  >   
  >   Full diff:
  >   + []
  >   - [
  >   -     '1',...
- `tests.test_advanced_operators.test_path_nested_field`
  > AssertionError: assert '{}\n' == '- address\n-...tion\n- lat\n'
  >   
  >   + {}
  >   - - address
  >   - - location
  >   - - lat
- `tests.test_advanced_operators.test_path_array_index`
  > AssertionError: assert '{}\n' == '- hobbies\n- 1\n'
  >   
  >   + {}
  >   - - hobbies
  >   - - 1
- *(... 181 more in this cluster)*

### `rc_mismatch_got2_want1` — 17 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_flags_color_print.test_exit_status_flag_no_match`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-e', '.missing', '/tmp/pytest-of-root/pytest-0/test_exit_status_flag_no_match2/test.yaml'], returncode=2, stdout='', stderr="yq: unknown 
- `tests.test_cli_flags_color_print.test_exit_status_with_false_value`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-e', '.value', '/tmp/pytest-of-root/pytest-0/test_exit_status_with_false_va2/test.yaml'], returncode=2, stdout='', stderr="yq: unknown op
- `tests.test_cli_flags_color_print.test_exit_status_with_null_value`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-e', 'null', '/tmp/pytest-of-root/pytest-0/test_exit_status_with_null_val2/test.yaml'], returncode=2, stdout='', stderr="yq: unknown opti
- *(... 14 more in this cluster)*

### `rc_unexpected_zero` — 12 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_error_handling.test_invalid_expression`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '[[invalid'], returncode=0, stdout=b'a: 1\n', stderr=b'').returncode
- `tests.test_error_handling.test_syntax_error_expression`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '.a ='], returncode=0, stdout=b'a: 1\n', stderr=b'').returncode
- `tests.test_error_handling.test_incomplete_expression`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '.a |'], returncode=0, stdout=b'a: 1\n', stderr=b'').returncode
- *(... 9 more in this cluster)*

### `rc_mismatch_got0_want1` — 11 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_operators.test_unique_by`
  > AssertionError: assert 0 == 1
  >  +  where 0 = <built-in method count of str object at 0x7f9f93cb4030>('name: a')
  >  +    where <built-in method count of str object at 0x7f9f93cb4030> = ''.count
- `tests.test_advanced_operators.test_to_number_error_on_non_numeric`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '.non_numeric | to_number', '/workspace/eval/test_resources/test_advanced_operators/numbers.yaml'], returncode=0, stdout='{}\n', stderr=''
- `tests.test_advanced_operators.test_setpath_error_on_non_array_path`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'setpath("a"; 42)'], returncode=0, stdout='', stderr='').returncode
- *(... 8 more in this cluster)*

### `boolean_false` — 7 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_flags_and_options.test_split_by_field`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpt84z9rzp/doc1.yml').exists
- `tests.test_flags_and_options.test_split_exp_file`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpszthbbb9/doc1.yml').exists
- `tests.test_cli_flags_color_print.test_invalid_flag_produces_error`
  > assert False
  >  +  where False = <built-in method startswith of str object at 0x7f28991be6b0>('Error: unknown flag: --invalid-flag-that-does-not-exist\n')
  >  +    where <built-in method startswith of str object at 0x7f28991be6b0> = "yq: unknown option: --invalid-flag-that-does-not-exist\nusage: yq [OPTIONS] [ARGS]\nTry 'yq --help' for more information.\n"
  >  +      where "yq: unknown option: --invalid-flag-that-does-not-exist\nusage: yq [OPTIONS] [ARGS]\nTry 'yq --help' for more information.\n" = CompletedProcess(args=['/workspace/executable', '--invalid
- *(... 4 more in this cluster)*

### `bytes_output_mismatch` — 4 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_advanced_features.test_empty_doc`
  > AssertionError: assert (b'{}\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + b'{}\n' or b'{}\n' == b'\n'
  >   
  >   At index 0 diff: b'{' != b'\n'
  >   
- `tests.test_advanced_features.test_empty_yaml_file`
  > AssertionError: assert (b'{}\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + b'{}\n' or b'{}\n' == b'\n'
  >   
  >   At index 0 diff: b'{' != b'\n'
  >   
- `tests.test_error_handling.test_invalid_xml_input`
  > assert (2 == 0 or b'Error' in b"yq: unknown option: -p\nusage: yq [OPTIONS] [ARGS]\nTry 'yq --help' for more information.\n")
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-p', 'xml', '.'], returncode=2, stdout=b'', stderr=b"yq: unknown option: -p\nusage: yq [OPTIONS] [ARGS]\nTry 'yq --help' for more informa
  >  +  and   b"yq: unknown option: -p\nusage: yq [OPTIONS] [ARGS]\nTry 'yq --help' for more information.\n" = CompletedProcess(args=['/workspace/executable', '-p', 'xml', '.'], returncode=2, stdout=b'', 
- *(... 1 more in this cluster)*

### `returned_none` — 2 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_basic_invocation.test_version_flag`
  > AssertionError: assert None is not None
  >  +  where None = <function search at 0x7f9f93ab3760>(b'v\\d+\\.\\d+\\.\\d+', b'yq 0.1.0\n')
  >  +    where <function search at 0x7f9f93ab3760> = re.search
  >  +    and   b'yq 0.1.0\n' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'yq 0.1.0\n', stderr=b'').stdout
- `tests.test_basic_invocation.test_version_short_flag`
  > AssertionError: assert None is not None
  >  +  where None = <function search at 0x7f9f93ab3760>(b'v\\d+\\.\\d+\\.\\d+', b'yq 0.1.0\n')
  >  +    where <function search at 0x7f9f93ab3760> = re.search
  >  +    and   b'yq 0.1.0\n' = CompletedProcess(args=['/workspace/executable', '-V'], returncode=0, stdout=b'yq 0.1.0\n', stderr=b'').stdout

### `uncategorized` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_datetime_vars_anchors.test_to_unix_timestamp_conversion`
  > ValueError: invalid literal for int() with base 10: '{}'
- `tests.test_datetime_vars_anchors.test_sort_keys_with_nested_arrays`
  > ValueError: substring not found

### `rc_mismatch_got0_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_operators.test_unique_array`
  > assert 0 == 3
  >  +  where 0 = len([])

### `json_output_missing_or_bad` — 1 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `tests.test_array_operators.test_shuffle_produces_array_same_length`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

### `rc_mismatch_got1_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_datetime_vars_anchors.test_variable_simple_assignment`
  > AssertionError: assert 1 == 3
  >  +  where 1 = len([''])

