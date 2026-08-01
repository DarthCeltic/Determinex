# Action Sheet — lua__lua.c6b4848

**Current:** 6.82%  (117/1715)
**Pass / Fail / Skip:** 117 / 910 / 2
**Gap to 100%:** 93.18 percentage points (1598 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_cli_basics.test_unknown_option_usage_and_exit_code`
  - reason: test_unknown_option_usage_and_exit_code depends on test_version_flag_exact
- `eval.tests.test_modules_and_env.test_l_flag_with_assignment_sets_custom_global_name`
  - reason: test_l_flag_with_assignment_sets_custom_global_name depends on test_l_flag_requires_module_and_sets_global

## Failure clusters

910 failed tests grouped into 19 buckets (sorted by count).

### `other_assertion` — 434 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_additional_coverage.test_string_library_functions`
  > assert b'he' in b'test\n'
  >  +  where b'test\n' = CompletedProcess(args=['./executable', '-e', "\nprint(string.sub('hello', 1, 2))\nprint(string.find('hello', 'l'))\nprint(string.gsub('hello', 'l', 'L'))\nprint(string.reverse('h
- `tests.test_additional_coverage.test_table_library_operations`
  > assert b'4' in b'table: 0x0\n'
  >  +  where b'table: 0x0\n' = CompletedProcess(args=['./executable', '-e', "\nlocal t = {1, 2, 3}\ntable.insert(t, 4)\nprint(t[4])\ntable.remove(t, 2)\nprint(#t)\nprint(table.concat({'a', 'b', 'c'}, ','
- `tests.test_additional_coverage.test_os_library_operations`
  > assert b'20' in b'nil\n'
  >  +  where b'nil\n' = CompletedProcess(args=['./executable', '-e', "\nprint(os.date('%Y'))\nprint(os.clock())\nlocal t = os.time()\nprint(type(t))\n"], returncode=0, stdout=b'nil\n', stderr=b'').stdout
- *(... 431 more in this cluster)*

### `string_output_mismatch` — 255 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_lua_language_features.test_comparison_operations`
  > AssertionError: assert 'true' in '5 > 3, 5 < 3, 5 == 5, 5 ~= 3\n'
- `tests.test_env_vars.test_lua_init_file`
  > AssertionError: assert '' == '10'
  >   
  >   - 10
- `tests.test_language.test_math_basic_arithmetic`
  > AssertionError: assert ['2+3,', '10-...*7,', '15//4'] == ['5', '6', '21', '3']
  >   
  >   At index 0 diff: '2+3,' != '5'
  >   
  >   Full diff:
  >     [
  >   -     '5',
  >   -     '6',...
- *(... 252 more in this cluster)*

### `rc_mismatch_got1_want0` — 61 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_additional_coverage.test_xpcall_function`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '-e', "\nlocal function errhandler(err)\n  return 'caught: ' .. tostring(err)\nend\nlocal ok, result = xpcall(function() error('test') end, errhand
- `tests.test_script_execution.test_stdin_mode_with_dash`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '-'], returncode=1, stdout=b'', stderr=b'lua: cannot open -: No such file or directory\n').returncode
- `tests.test_standard_libraries.test_pcall_error_handling`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '-e', "\nlocal ok, err = pcall(function() error('test') end)\nprint(ok, type(err))\n"], returncode=1, stdout=b'', stderr=b'error: test error\n').re
- *(... 58 more in this cluster)*

### `rc_mismatch_got2_want0` — 40 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_basic_invocation.test_no_arguments_stdin`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable'], returncode=2, stdout=b'', stderr=b"usage: lua [OPTIONS] [ARGS]\nTry 'lua --help' for more information.\n").returncode
- `tests.test_basic_invocation.test_execute_simple_print`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable'], returncode=2, stdout=b'', stderr=b"usage: lua [OPTIONS] [ARGS]\nTry 'lua --help' for more information.\n").returncode
- `tests.test_basic_invocation.test_execute_multiple_statements`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable'], returncode=2, stdout=b'', stderr=b"usage: lua [OPTIONS] [ARGS]\nTry 'lua --help' for more information.\n").returncode
- *(... 37 more in this cluster)*

### `rc_unexpected_zero` — 35 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_basic.test_invalid_option_shows_usage`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '--help'], returncode=0, stdout=b'lua 0.1.0 - bootstrap scaffold\n\nUsage: lua [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --v
- `tests.test_basic.test_execute_string_syntax_error`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '-e', 'print('], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_errors.test_nil_arithmetic_error`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '-e', 'print(nil + 1)'], returncode=0, stdout=b'nil + 1\n', stderr=b'').returncode
- *(... 32 more in this cluster)*

### `rc_mismatch_got0_want1` — 26 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_basic_invocation.test_invalid_option_shows_usage`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', '--help'], returncode=0, stdout=b'lua 0.1.0 - bootstrap scaffold\n\nUsage: lua [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --v
- `tests.test_command_options.test_e_flag_syntax_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', '-e', 'print('], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_command_options.test_l_flag_missing_library`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', '-l', 'nonexistent_module'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 23 more in this cluster)*

### `bytes_output_mismatch` — 16 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_edge_cases.test_empty_table_concat`
  > AssertionError: assert (b'table.concat({})\n' == b'\n'
  >   
  >   At index 0 diff: b't' != b'\n'
  >   
  >   Full diff:
  >   - b'\n'
  >   + (b'table.concat({})\n') or b'table.concat({})\n' == b''
  >   
- `tests.test_edge_cases.test_comparison_operators`
  > AssertionError: assert b'true' in b'5 > 3, 5 < 3, 5 == 5, 5 ~= 5\n'
  >  +  where b'5 > 3, 5 < 3, 5 == 5, 5 ~= 5\n' = CompletedProcess(args=['./executable', '-e', 'print(5 > 3, 5 < 3, 5 == 5, 5 ~= 5)'], returncode=0, stdout=b'5 > 3, 5 < 3, 5 == 5, 5 ~= 5\n', stderr=b'').s
- `tests.test_env_vars.test_lua_path`
  > AssertionError: assert b'package.path' == b'x'
  >   
  >   At index 0 diff: b'p' != b'x'
  >   
  >   Full diff:
  >   - b'x'
  >   + (b'package.path')
- *(... 13 more in this cluster)*

### `rc_mismatch_got2_want1` — 10 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_unknown_short_option`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['./executable', '-x'], returncode=2, stdout=b'', stderr=b"lua: unknown option: -x\nusage: lua [OPTIONS] [ARGS]\nTry 'lua --help' for more information.\n").returnco
- `eval.tests.test_argparse_validation.test_unknown_options_error[argv0-1-err_substrings0]`
  > assert 2 == 1
- `eval.tests.test_argparse_validation.test_unknown_options_error[argv1-1-err_substrings1]`
  > assert 2 == 1
- *(... 7 more in this cluster)*

### `boolean_false` — 8 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `eval.tests.test_argparse_validation.test_version_flag_prints_to_stdout_and_exit_success`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7f1f4300fc70>('Lua ')
  >  +    where <built-in method startswith of str object at 0x7f1f4300fc70> = 'lua 0.1.0\n'.startswith
- `eval.tests.test_env_and_config.test_lua_path_double_semicolon_inserts_default_in_between`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7fa9e54f4070>('X;')
  >  +    where <built-in method startswith of str object at 0x7fa9e54f4070> = 'package.path'.startswith
- `eval.tests.test_help_usage.test_help_starts_with_unrecognized_option_line`
  > assert False
  >  +  where False = <built-in method endswith of str object at 0x7f2c699df4b0>("unrecognized option '--help'")
  >  +    where <built-in method endswith of str object at 0x7f2c699df4b0> = 'lua 0.1.0 - bootstrap scaffold'.endswith
- *(... 5 more in this cluster)*

### `empty_list_or_string` — 5 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_lua_language_features.test_local_variables`
  > IndexError: list index out of range
- `tests.test_baselib.test_loadfile_syntax_error`
  > IndexError: list index out of range
- `tests.test_baselib.test_print_with_table`
  > IndexError: list index out of range
- *(... 2 more in this cluster)*

### `missing_file` — 5 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_io.test_io_input_output`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpc_m4hw6f/out.txt'
- `tests.test_stdin_scripts.test_close_with_open_file`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpxgjiwwga/out.txt'
- `tests.test_file_io.test_io_open_write`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_io_open_write2/output.txt'
- *(... 2 more in this cluster)*

### `rc_mismatch_got1_want5` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_baselib.test_tonumber_basic_conversions`
  > AssertionError: assert 1 == 5
  >  +  where 1 = len(['0'])
- `tests.test_baselib.test_tonumber_with_bases`
  > AssertionError: assert 1 == 5
  >  +  where 1 = len(['0'])
- `tests.test_baselib.test_ipairs_array_iteration`
  > AssertionError: assert 1 == 5
  >  +  where 1 = len([''])

### `rc_mismatch_got1_want3` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_baselib.test_pairs_basic_iteration`
  > AssertionError: assert 1 == 3
  >  +  where 1 = len(['table: 0x0'])
- `tests.test_baselib.test_pairs_with_metamethod`
  > AssertionError: assert 1 == 3
  >  +  where 1 = len(['table: 0x0'])
- `tests.test_iolib.test_file_lines_iterator`
  > AssertionError: assert 1 == 3
  >  +  where 1 = len([''])

### `rc_mismatch_got1_want7` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_baselib.test_type_all_lua_types`
  > AssertionError: assert 1 == 7
  >  +  where 1 = len(['nil'])
- `tests.test_corolib.test_basic_yield_resume_cycle`
  > AssertionError: assert 1 == 7
  >  +  where 1 = len([''])

### `rc_mismatch_got1_want2` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_baselib.test_next_empty_table`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len([''])
- `tests.test_corolib.test_isyieldable_with_optional_argument`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len([''])

### `rc_mismatch_got1_want4` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_baselib.test_tonumber_negative_numbers`
  > AssertionError: assert 1 == 4
  >  +  where 1 = len(['0'])
- `tests.test_corolib.test_yield_and_return_table`
  > AssertionError: assert 1 == 4
  >  +  where 1 = len(['table: 0xADDRESS'])

### `uncategorized` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_language.test_math_minmax_integer`
  > ValueError: invalid literal for int() with base 10: 'math.maxinteger,'

### `rc_mismatch_got1_want6` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_baselib.test_tostring_basic_types`
  > AssertionError: assert 1 == 6
  >  +  where 1 = len(['test'])

### `rc_mismatch_got0_want42` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_libraries.test_os_exit_with_nonzero_code`
  > assert 0 == 42

