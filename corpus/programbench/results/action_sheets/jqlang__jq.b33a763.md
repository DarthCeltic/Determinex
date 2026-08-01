# Action Sheet — jqlang__jq.b33a763

**Current:** 2.13%  (133/6249)
**Pass / Fail / Skip:** 133 / 1368 / 0
**Gap to 100%:** 97.87 percentage points (6116 tests)

## Failure clusters

1368 failed tests grouped into 32 buckets (sorted by count).

### `other_assertion` — 586 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_absolute_final_70.test_complex_conditional`
  > assert b'"positive"' in b'5'
  >  +  where b'5' = CompletedProcess(args=['/workspace/executable', 'if . < 0 then "negative" elif . == 0 then "zero" else "positive" end'], returncode=0, stdout=b'5', stderr=b'').stdout
- `tests.test_absolute_final_70.test_array_update_with_filter`
  > AssertionError: assert [1, 6, 3, 8, 2] == [1, 12, 3, 16, 2]
  >   
  >   At index 1 diff: 6 != 12
  >   
  >   Full diff:
  >     [
  >         1,
  >   -     12,...
- `tests.test_absolute_final_70.test_walk_with_complex_structure`
  > AssertionError: assert [3, 1, 2] == [1, 2, 3]
  >   
  >   At index 0 diff: 3 != 1
  >   
  >   Full diff:
  >     [
  >   +     3,
  >         1,...
- *(... 583 more in this cluster)*

### `string_output_mismatch` — 293 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_absolute_final_70.test_test_negative`
  > AssertionError: assert 'abcdef' == False
- `tests.test_absolute_final_70.test_capture_no_match`
  > AssertionError: assert 'abcdef' == {}
- `tests.test_absolute_final_70.test_startswith_false`
  > AssertionError: assert 'hello' == False
- *(... 290 more in this cluster)*

### `rc_mismatch_got2_want0` — 152 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_advanced_coverage.TestSpecialInputModes.test_raw_input_mode`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-R', '.'], returncode=2, stdout=b'', stderr=b"jq: unknown option: -R\nusage: jq [OPTIONS] [ARGS]\nTry 'jq --help' for more information.\n
- `tests.test_advanced_coverage.TestSpecialInputModes.test_null_input_generator`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-n', 'range(5)'], returncode=2, stdout=b'', stderr=b"jq: unknown option: -n\nusage: jq [OPTIONS] [ARGS]\nTry 'jq --help' for more informa
- `tests.test_arguments.test_arg_flag`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--arg', 'name', 'John', '.name = $name'], returncode=2, stdout=b'', stderr=b"jq: unknown option: --arg\nusage: jq [OPTIONS] [ARGS]\nTry '
- *(... 149 more in this cluster)*

### `bytes_output_mismatch` — 148 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_absolute_final_70.test_recursive_function_factorial`
  > AssertionError: assert b'6' == b'720'
  >   
  >   At index 0 diff: b'6' != b'7'
  >   
  >   Full diff:
  >   - b'720'
  >   + b'6'
- `tests.test_absolute_final_70.test_getpath_with_nested_arrays`
  > AssertionError: assert b'[[0, [1, 2]], [3, [4, 5]]]' == b'1'
  >   
  >   At index 0 diff: b'[' != b'1'
  >   
  >   Full diff:
  >   - b'1'
  >   + (b'[[0, [1, 2]], [3, [4, 5]]]')
- `tests.test_absolute_final_70.test_first_with_select`
  > AssertionError: assert b'[1, 2, 3, 6, 7, 8]' == b'6'
  >   
  >   At index 0 diff: b'[' != b'6'
  >   
  >   Full diff:
  >   - b'6'
  >   + (b'[1, 2, 3, 6, 7, 8]')
- *(... 145 more in this cluster)*

### `rc_unexpected_zero` — 90 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_basic.test_type_error_array_index_on_object`
  > assert 0 != 0
- `tests.test_basic.test_type_error_field_access_on_array`
  > assert 0 != 0
- `tests.test_basic.test_division_by_zero_error`
  > assert 0 != 0
- *(... 87 more in this cluster)*

### `type_error` — 26 test(s)

**Quick patch ideas:**
- Specific TypeError; check arg types vs expected

**Sample failures:**

- `tests.test_absolute_final_70.test_paths_with_arrays`
  > TypeError: unhashable type: 'list'
- `tests.test_absolute_final_70.test_limit_with_infinite_stream`
  > TypeError: object of type 'NoneType' has no len()
- `tests.test_absolute_final_70.test_now_timestamp`
  > TypeError: '>' not supported between instances of 'NoneType' and 'int'
- *(... 23 more in this cluster)*

### `returned_none` — 19 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_absolute_final_70.test_until_fibonacci`
  > assert None == 34
- `tests.test_absolute_final_70.test_inside_false`
  > assert None == False
- `tests.test_absolute_push_70.test_object_multiply`
  > AssertionError: assert None == {'a': 1, 'b': 2}
- *(... 16 more in this cluster)*

### `boolean_false` — 8 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_additional_builtins.test_split_regex`
  > AssertionError: assert False
  >  +  where False = isinstance('a,b;c', list)
- `tests.test_basic.test_logical_not_false`
  > assert False is True
- `tests.test_basic.test_alternative_operator_false_left`
  > AssertionError: assert False == 'default'
- *(... 5 more in this cluster)*

### `missing_dict_key` — 5 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_absolute_final_70.test_setpath_create_nested`
  > KeyError: 'a'
- `tests.test_absolute_push_70.test_setpath_with_variable`
  > KeyError: 'a'
- `tests.test_advanced_coverage.TestAdvancedSyntax.test_object_construction_computed_keys`
  > KeyError: 'mykey'
- *(... 2 more in this cluster)*

### `rc_mismatch_got1_want3` — 5 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic.test_array_iterate_simple`
  > AssertionError: assert 1 == 3
  >  +  where 1 = len(['[1, 2, 3]'])
- `tests.test_basic.test_object_iterate_values`
  > assert 1 == 3
  >  +  where 1 = len(['{"a": 1, "b": 2, "c": 3}'])
- `tests.test_basic.test_comma_operator_with_expressions`
  > assert 1 == 3
  >  +  where 1 = len(['{"a": 5, "b": 3, "c": "text"}'])
- *(... 2 more in this cluster)*

### `rc_mismatch_got1_want2` — 4 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_absolute_push_70.test_recursive_find`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len({'a': {'b': 'target', 'c': {'d': 'target'}}})
- `tests.test_advanced_coverage.TestAdvancedBuiltins.test_with_entries`
  > assert 1 == 2
- `tests.test_basic.test_comma_operator_multiple_outputs`
  > assert 1 == 2
  >  +  where 1 = len(['{"a": 1, "b": 2}'])
- *(... 1 more in this cluster)*

### `uncategorized` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_additional_builtins.test_until_iteration`
  > ValueError: invalid literal for int() with base 10: b'null'
- `tests.test_additional_builtins.test_rindex_string`
  > ValueError: invalid literal for int() with base 10: b'"hello world"'
- `tests.test_additional_builtins.test_add_nulls`
  > ValueError: invalid literal for int() with base 10: b'[1, null, 2, null, 3]'

### `rc_mismatch_got2_want1` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_args_parsing.test_exit_status_flag_parsing_accepts_long_and_short`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-ne', 'false'], returncode=2, stdout=b'', stderr=b"jq: unknown option: -ne\nusage: jq [OPTIONS] [ARGS]\nTry 'jq --help' for more informat
- `tests.test_cli_options.TestExitStatus.test_exit_status_false`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-e', 'false'], returncode=2, stdout=b'', stderr=b"jq: unknown option: -e\nusage: jq [OPTIONS] [ARGS]\nTry 'jq --help' for more informatio
- `tests.test_cli_options.TestExitStatus.test_exit_status_null`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-e', 'null'], returncode=2, stdout=b'', stderr=b"jq: unknown option: -e\nusage: jq [OPTIONS] [ARGS]\nTry 'jq --help' for more information

### `rc_mismatch_got5_want15` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_absolute_final_70.test_complex_object_update`
  > assert 5 == 15
- `tests.test_advanced_coverage.TestAssignmentOperators.test_plus_assignment`
  > assert 5 == 15

### `rc_mismatch_got6_want3` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_absolute_final_70.test_group_by_with_expression`
  > assert 6 == 3
  >  +  where 6 = len([5, 15, 25, 8, 18, 28])
- `tests.test_absolute_final_70.test_unique_by_with_expression`
  > assert 6 == 3
  >  +  where 6 = len([5, 15, 25, 8, 18, 28])

### `rc_mismatch_got42_want99` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_absolute_push_70.test_deep_path_update`
  > assert 42 == 99
- `tests.test_functions.TestPathFunctions.test_setpath`
  > assert 42 == 99

### `rc_mismatch_got5_want10` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_advanced_coverage.TestAssignmentOperators.test_update_assignment`
  > assert 5 == 10
- `tests.test_advanced.TestAssignment.test_update_operator`
  > assert 5 == 10

### `rc_mismatch_got3_want2` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_advanced_filters.test_group_by_function`
  > AssertionError: assert 3 == 2
  >  +  where 3 = len([{'type': 'a', 'val': 1}, {'type': 'b', 'val': 2}, {'type': 'a', 'val': 3}])
- `tests.test_functions.TestArrayFunctions.test_group_by`
  > AssertionError: assert 3 == 2
  >  +  where 3 = len([{'type': 'a', 'val': 1}, {'type': 'b', 'val': 2}, {'type': 'a', 'val': 3}])

### `rc_mismatch_got2_want4` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_jq_io.test_exit_status_flag_e_empty_is_exit_4`
  > assert 2 == 4
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-e', '-n', 'empty'], returncode=2, stdout=b'', stderr=b"jq: unknown option: -e\nusage: jq [OPTIONS] [ARGS]\nTry 'jq --help' for more info
- `tests.test_cli_options.TestExitStatus.test_exit_status_no_output`
  > assert 2 == 4
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-e', 'empty'], returncode=2, stdout=b'', stderr=b"jq: unknown option: -e\nusage: jq [OPTIONS] [ARGS]\nTry 'jq --help' for more informatio

### `rc_mismatch_got0_want5` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic.TestFieldAccess.test_field_on_array_error`
  > AssertionError: assert 0 == 5
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '.foo'], returncode=0, stdout=b'[1, 2, 3]', stderr=b'').returncode
- `tests.test_exact_output.TestExitCodes.test_exit_code_type_error`
  > assert 0 == 5
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '."foo"'], returncode=0, stdout=b'"string"', stderr=b'').returncode

### `rc_mismatch_got9_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_absolute_final_70.test_match_all_flag`
  > AssertionError: assert 9 == 3
  >  +  where 9 = len('a1b22c333')

### `rc_mismatch_got3_want8` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_absolute_final_70.test_combinations_multiple_arrays`
  > assert 3 == 8
  >  +  where 3 = len([[1, 2], [3, 4], [5, 6]])

### `rc_mismatch_got4_want2` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_absolute_push_70.test_select_objects`
  > AssertionError: assert 4 == 2
  >  +  where 4 = len([{'x': 1}, {'x': 6}, {'x': 3}, {'x': 8}])

### `rc_mismatch_got1_want11` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_absolute_push_70.test_update_all_leaves`
  > assert 1 == 11

### `rc_mismatch_got3_want1` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_absolutely_final.test_limit_one`
  > assert 3 == 1
  >  +  where 3 = len([1, 2, 3])

### `rc_mismatch_got1_want99` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_additional_builtins.test_setpath_overwrite`
  > assert 1 == 99

### `rc_mismatch_got2_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_args_parsing.test_double_dash_terminates_option_parsing_even_if_next_arg_looks_like_flag`
  > assert 2 == 3
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--', '-r', '.'], returncode=2, stdout=b'', stderr=b"jq: unknown option: --\nusage: jq [OPTIONS] [ARGS]\nTry 'jq --help' for more informat

### `rc_mismatch_got1_want4` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic.test_nested_comma_operators`
  > assert 1 == 4
  >  +  where 1 = len(['{"a": 1, "b": 2, "c": 3, "d": 4}'])

### `rc_mismatch_got1_want10000` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic.test_very_long_string`
  > AssertionError: assert 1 == 10000
  >  +  where 1 = len({'text': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

### `rc_mismatch_got0_want2` — 1 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `eval.tests.test_jq_io.test_file_not_found_is_exit_2_and_goes_to_stderr_only`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '.', '/tmp/pytest-of-root/pytest-0/test_file_not_found_is_exit_2_2/missing.json'], returncode=0, stdout=b'[]', stderr=b'').returncode

### `rc_mismatch_got1_want10` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_advanced.TestAssignment.test_update_assignment`
  > assert 1 == 10

### `rc_mismatch_got1_want0` — 1 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_edge_cases.TestUnicodeHandling.test_bom`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '.'], returncode=1, stdout=b'', stderr=b'jq: error parsing JSON\n').returncode

