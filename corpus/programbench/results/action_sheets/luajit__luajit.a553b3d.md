# Action Sheet — luajit__luajit.a553b3d

**Current:** 5.58%  (205/3674)
**Pass / Fail / Skip:** 205 / 917 / 0
**Gap to 100%:** 94.42 percentage points (3469 tests)

## Failure clusters

917 failed tests grouped into 14 buckets (sorted by count).

### `other_assertion` — 486 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_advanced_features.test_weak_tables`
  > assert b'true' in b'cafe\xc2\xa9'
  >  +  where b'cafe\xc2\xa9' = CompletedProcess(args=['/workspace/executable', '-e', "\n    local t = {}\n    setmetatable(t, {__mode = 'v'})\n    local obj = {}\n    t[1] = obj\n    print(t[1] ~= nil)\n
- `tests.test_advanced_features.test_metamethod_add`
  > AssertionError: assert b'15' in b'cafe\xc2\xa9'
  >  +  where b'cafe\xc2\xa9' = CompletedProcess(args=['/workspace/executable', '-e', '\n    local t1 = {value = 5}\n    local t2 = {value = 10}\n    setmetatable(t1, {__add = function(a, b) return a.valu
- `tests.test_advanced_features.test_metamethod_sub`
  > AssertionError: assert b'7' in b'cafe\xc2\xa9'
  >  +  where b'cafe\xc2\xa9' = CompletedProcess(args=['/workspace/executable', '-e', '\n    local t1 = {value = 10}\n    local t2 = {value = 3}\n    setmetatable(t1, {__sub = function(a, b) return a.valu
- *(... 483 more in this cluster)*

### `string_output_mismatch` — 159 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_args_parsing.test_e_flag_accepts_separate_or_concatenated_value[flag_form0]`
  > AssertionError: assert 'cafe©' == '42'
  >   
  >   - 42
  >   + cafe©
- `eval.tests.test_args_parsing.test_flags_after_script_name_are_not_parsed_as_options`
  > AssertionError: assert 'Mike Pall' == '-v'
  >   
  >   - -v
  >   + Mike Pall
- `eval.tests.test_args_parsing.test_l_requires_library_by_name`
  > AssertionError: assert '3.14\ntable\...true\n1\n2\n3' == 'function'
  >   
  >   + 3.14
  >   + table
  >   + HELLO
  >   - function
  >   + function
  >   ?         +...
- *(... 156 more in this cluster)*

### `bytes_output_mismatch` — 134 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_additional_coverage_boost.test_string_byte_out_of_range`
  > assert (b'cafe\xc2\xa9' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'cafe\xc2\xa9') or b'nil' in b'cafe\xc2\xa9')
  >  +  where b'cafe\xc2\xa9' = CompletedProcess(args=['./executable', '-e', "\n        local s = 'hello'\n        print(string.byte(s, 10))\n    "], returncode=0, stdout=b'cafe\xc2\xa9', stderr=b'').stdo
- `tests.test_basic_invocation.test_no_args_stdin_empty`
  > AssertionError: assert b'(command li...t available\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'(command line):1:\n-e chunk\n-l name\n0\n100\n12345\n2.71828\n3.14\n3.14'
  >   +  b'159\nAvailable options are:\nC function upvalue 1:\nC function upvalue 2:\nC'
  >   +  b'opyright\nCustom assertion message\nError in level3\nError:\nHANDLER:\nIn'
  >   +  b'tentional error during module load\nJIT:\nLoading circular_a\nLoading circu'...
- `tests.test_coverage_push_to_70.test_string_rep_zero`
  > AssertionError: assert b'cafe\xc2\xa9' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'cafe\xc2\xa9')
- *(... 131 more in this cluster)*

### `rc_unexpected_zero` — 77 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_coverage_boost.test_assert_with_false`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '-e', "assert(false, 'custom error message')"], returncode=0, stdout=b'cafe\xc2\xa9', stderr=b'').returncode
- `tests.test_coverage_boost.test_assert_with_nil`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '-e', 'assert(nil)'], returncode=0, stdout=b'a\n1\n1\n2\n3\nx\n1\n5\n42\n99\n', stderr=b'').returncode
- `tests.test_coverage_boost.test_error_function`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '-e', "error('explicit error')"], returncode=0, stdout=b'cafe\xc2\xa9', stderr=b'').returncode
- *(... 74 more in this cluster)*

### `boolean_false` — 25 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_bytecode.test_save_bytecode_raw`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpf_atatdc/test.out').exists
- `tests.test_bytecode.test_save_bytecode_with_debug`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmp4ousmzc5/test_debug.out').exists
- `tests.test_bytecode.test_bytecode_from_string`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpedl16mre/string.out').exists
- *(... 22 more in this cluster)*

### `rc_mismatch_got0_want1` — 16 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `eval.tests.test_args_parsing.test_e_missing_value_prints_usage_and_exits_zero`
  > assert 0 == 1
- `eval.tests.test_args_parsing.test_l_missing_value_prints_usage_and_exits_zero`
  > assert 0 == 1
- `eval.tests.test_help_usage.test_dash_h_exit_code_is_one`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-h'], returncode=0, stdout='LuaJIT\nCopyright\nMike Pall\nhttps://luajit.org\nLuaJIT\n', stderr='').returncode
- *(... 13 more in this cluster)*

### `rc_mismatch_got1_want2` — 5 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_base_lib_gaps.test_newproxy_without_metatable`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len([b'cafe\xc2\xa9'])
- `tests.test_base_lib_gaps.test_newproxy_with_true_creates_metatable`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len([b'cafe\xc2\xa9'])
- `tests.test_base_lib_gaps.test_gcinfo_returns_memory_kb`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len([b'cafe\xc2\xa9'])
- *(... 2 more in this cluster)*

### `rc_mismatch_got42_want0` — 4 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_coverage_boost_3.test_comment_single_line`
  > assert 42 == 0
  >  +  where 42 = CompletedProcess(args=['./executable', '-e', '-- comment\nprint(42)'], returncode=42, stdout=b"error: unexpected argument '-e' found\nError: unexpected argument '-e' found\nunknown flag
- `eval.tests.test_args_parsing.test_e_flag_accepts_separate_or_concatenated_value[flag_form1]`
  > assert 42 == 0
- `tests.test_cli.test_e_flag_inline_chunk`
  > assert 42 == 0
  >  +  where 42 = CompletedProcess(args=['/workspace/executable', '-eprint("inline")'], returncode=42, stdout=b'error: unexpected argument \'-eprint("inline")\' found\nError: unexpected argument \'-eprin
- *(... 1 more in this cluster)*

### `rc_mismatch_got1_want3` — 4 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_additional_coverage_boost.test_bit_operations_with_large_numbers`
  > AssertionError: assert 1 == 3
  >  +  where 1 = len([b'cafe\xc2\xa9'])
- `tests.test_base_lib_gaps.test_tonumber_base_conversion_edge_cases`
  > AssertionError: assert 1 == 3
  >  +  where 1 = len([b'cafe\xc2\xa9'])
- `tests.test_base_lib_gaps.test_tonumber_with_base_and_leading_zeros`
  > AssertionError: assert 1 == 3
  >  +  where 1 = len([b'cafe\xc2\xa9'])
- *(... 1 more in this cluster)*

### `rc_mismatch_got42_want1` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_args_parsing.test_unknown_long_option_prints_usage_and_exits_zero`
  > assert 42 == 1
- `eval.tests.test_args_parsing.test_j_missing_value_prints_usage_and_exits_zero`
  > assert 42 == 1

### `empty_list_or_string` — 2 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `eval.tests.test_help_usage.test_help_usage_line_present_and_normalized`
  > IndexError: list index out of range
- `eval.tests.test_bytecode_and_jit.test_bl_lists_bytecode_for_e_chunk`
  > IndexError: list index out of range

### `missing_file` — 1 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_bytecode.test_bytecode_deterministic`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpe065qjcd/det1.out'

### `rc_mismatch_got0_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_luajit_io.test_exit_code_propagates_from_os_exit`
  > AssertionError: assert 0 == 3
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-e', 'os.exit(3)'], returncode=0, stdout=b'cafe\xc2\xa9', stderr=b'').returncode

### `uncategorized` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_aux_lib_gaps.test_buffer_with_addvalue_via_concat`
  > ValueError: invalid literal for int() with base 10: b'local t = {}\nfor i = 1, 100 do\n    t[i] = tostring(i)\nend\nlocal result = table.concat(t, ",")\nprint(#result)\n(command line):1:\n-e chunk\n-l

