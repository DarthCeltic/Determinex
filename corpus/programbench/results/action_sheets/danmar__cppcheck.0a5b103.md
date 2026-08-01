# Action Sheet — danmar__cppcheck.0a5b103

**Current:** 3.93%  (100/2544)
**Pass / Fail / Skip:** 100 / 889 / 28
**Gap to 100%:** 96.07 percentage points (2444 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.helloworld_test.test_cppcheck_project_local_path_select_one`
  - reason: <no-reason>
- `tests.helloworld_test.test_cppcheck_project_local_path_select_one_multiple`
  - reason: <no-reason>
- `tests.inline_suppress_test.test_compile_commands_unused_function_j`
  - reason: unconditional skip
- `tests.inline_suppress_test.test_compile_commands_unused_function_suppression_j`
  - reason: unconditional skip
- `tests.inline_suppress_test.test_duplicate`
  - reason: unconditional skip
- *(... 23 more skipped)*

## Failure clusters

889 failed tests grouped into 17 buckets (sorted by count).

### `other_assertion` — 685 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_additional_coverage.test_complex_pointer_error`
  > AssertionError: assert b'Checking' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', '/tmp/tmp4nkxqbvf/test.c'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_additional_coverage.test_array_out_of_bounds`
  > AssertionError: assert b'Checking' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', '/tmp/tmpewqpasls/test.c'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_additional_coverage.test_include_with_defines`
  > AssertionError: assert b'Checking' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', '-I', '/tmp/tmp69kney3s', '/tmp/tmp69kney3s/test.c'], returncode=0, stdout=b'', stderr=b'').stdout
- *(... 682 more in this cluster)*

### `string_output_mismatch` — 117 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_help_baseline.test_help_stdout_matches_baseline_exact`
  > AssertionError: assert '' == 'Cppcheck - A...ed in GUI\n\n'
  >   
  >   - Cppcheck - A tool for static C/C++ code analysis
  >   - 
  >   - Syntax:
  >   -     cppcheck [OPTIONS] [files or paths]
  >   - 
  >   - If a directory is given instead of a filename, *.cpp, *.cxx, *.cc, *.c++, *.c, *.ipp,...
- `tests.test_cppcheck_cli.test_default_run_prints_progress_on_stdout`
  > AssertionError: assert '' == 'Checking /tm...re2/t.c ...\n'
  >   
  >   - Checking /tmp/pytest-of-root/pytest-0/test_default_run_prints_progre2/t.c ...
- `tests.test_cppcheck_cli.test_quiet_suppresses_progress_but_keeps_diagnostics`
  > AssertionError: assert '' == 'uninitvar:er...riable: x\n\n'
  >   
  >   - uninitvar:error:/tmp/pytest-of-root/pytest-0/test_quiet_suppresses_progress2/t.c:1:27:Uninitialized variable: x
  >   -
- *(... 114 more in this cluster)*

### `rc_mismatch_got0_want1` — 29 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_basic.test_invalid_file`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', '/nonexistent/file.c'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_file_handling.test_nonexistent_path`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', '/nonexistent/path/file.c'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_argparse_validation.test_invalid_or_missing_option_values[args0-unrecognized command line option: "--unknown"-1]`
  > AssertionError: assert 0 == 1
  >  +  where 0 = RunResult(code=0, out='', err='').code
- *(... 26 more in this cluster)*

### `missing_file` — 21 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.dumpfile_test.test_language_c`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_language_c2/test.c.dump'
- `tests.dumpfile_test.test_language_c_force_c`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_language_c_force_c2/test.c.dump'
- `tests.dumpfile_test.test_language_c_force_cpp`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_language_c_force_cpp2/test.c.dump'
- *(... 18 more in this cluster)*

### `uncategorized` — 10 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.helloworld_test.test_xml_checkers_report`
  > xml.etree.ElementTree.ParseError: no element found: line 1, column 0
- `tests.lookup_test.test_lib_lookup`
  > ValueError: list.remove(x): x not in list
- `tests.lookup_test.test_lib_lookup_ext`
  > ValueError: list.remove(x): x not in list
- *(... 7 more in this cluster)*

### `boolean_false` — 8 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_advanced_features.test_checkers_report`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpyb8bn1aa/checkers.txt').exists
- `tests.test_help_and_version.test_version_prints_version_prefix`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7f387dc24030>('Cppcheck ')
  >  +    where <built-in method startswith of str object at 0x7f387dc24030> = ''.startswith
- `tests.test_help_usage.test_help_ends_with_newline`
  > AssertionError: assert False
  >  +  where False = <built-in method endswith of str object at 0x7f7e8ba9c030>('\n')
  >  +    where <built-in method endswith of str object at 0x7f7e8ba9c030> = ''.endswith
- *(... 5 more in this cluster)*

### `rc_mismatch_got0_want3` — 5 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_checkfunctions_gaps.test_memset_zero_bytes`
  > AssertionError: assert 0 == 3
  >  +  where 0 = <built-in method count of str object at 0x7fb892e94030>('memsetZeroBytes')
  >  +    where <built-in method count of str object at 0x7fb892e94030> = ''.count
  >  +      where '' = CompletedProcess(args=['./executable', '--enable=warning', '/workspace/eval/test_resources/test_checkfunctions_gaps/memset_zero_bytes.c'], returncode=0, stdout='', stderr='').combin
- `tests.test_checkfunctions_gaps.test_memset_float_portability`
  > AssertionError: assert 0 == 3
  >  +  where 0 = <built-in method count of str object at 0x7fb892e94030>('memsetFloat')
  >  +    where <built-in method count of str object at 0x7fb892e94030> = ''.count
  >  +      where '' = CompletedProcess(args=['./executable', '--enable=warning,portability', '/workspace/eval/test_resources/test_checkfunctions_gaps/memset_float.c'], returncode=0, stdout='', stderr='')
- `tests.test_checkfunctions_gaps.test_sqrt_acos_asin_domain_errors`
  > AssertionError: assert 0 == 3
  >  +  where 0 = <built-in method count of str object at 0x7fb892e94030>('invalidFunctionArg')
  >  +    where <built-in method count of str object at 0x7fb892e94030> = ''.count
  >  +      where '' = CompletedProcess(args=['./executable', '--enable=warning', '/workspace/eval/test_resources/test_checkfunctions_gaps/invalid_sqrt_acos.c'], returncode=0, stdout='', stderr='').combin
- *(... 2 more in this cluster)*

### `rc_unexpected_zero` — 3 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_subcommand_dispatch.TestArgumentParsing.test_unknown_flag_error`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--this-flag-does-not-exist'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_subcommand_dispatch.TestErrorMessages.test_invalid_flag_error_pattern`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--invalid-flag-xyz'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_no_subcommands_dispatch.test_unknown_subcommand_is_treated_as_path_or_errors_cleanly`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'nonexistent_subcommand_12345'], returncode=0, stdout='', stderr='').returncode

### `rc_mismatch_got0_want42` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic.test_exit_code_with_errors`
  > AssertionError: assert 0 == 42
  >  +  where 0 = CompletedProcess(args=['./executable', '--error-exitcode=42', '/tmp/tmpgz2rj8gz/test.c'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_cppcheck_cli.test_error_exit_code_is_used_when_findings_exist`
  > AssertionError: assert 0 == 42
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--error-exitcode=42', '/tmp/pytest-of-root/pytest-0/test_error_exit_code_is_used_w2/t.c'], returncode=0, stdout='', stderr='').returncode

### `returned_none` — 2 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_help_usage.test_help_includes_severity_bullets_under_enable`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f7e8ba0e680>('^\\s*\\*\\s+warning\\b', '', re.MULTILINE)
  >  +    where <function search at 0x7f7e8ba0e680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- `tests.test_cppcheck_cli.test_version_output_and_exit_code`
  > AssertionError: assert None
  >  +  where None = <function fullmatch at 0x7f65e94efe20>('Cppcheck [^\\n]+\\n?', '')
  >  +    where <function fullmatch at 0x7f65e94efe20> = re.fullmatch
  >  +    and   '' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout='', stderr='').stdout

### `rc_mismatch_got0_want4` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_checkfunctions_gaps.test_c99_math_precision_suggestions`
  > AssertionError: assert 0 == 4
  >  +  where 0 = <built-in method count of str object at 0x7fb892e94030>('unpreciseMathCall')
  >  +    where <built-in method count of str object at 0x7fb892e94030> = ''.count
  >  +      where '' = CompletedProcess(args=['./executable', '--enable=style', '--std=c99', '/workspace/eval/test_resources/test_checkfunctions_gaps/math_c99_precision.c'], returncode=0, stdout='', stder

### `rc_mismatch_got0_want2` — 1 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_checkfunctions_gaps.test_memset_boundary_values`
  > AssertionError: assert 0 == 2
  >  +  where 0 = <built-in method count of str object at 0x7fb892e94030>('memsetValueOutOfRange')
  >  +    where <built-in method count of str object at 0x7fb892e94030> = ''.count
  >  +      where '' = CompletedProcess(args=['./executable', '--enable=warning', '/workspace/eval/test_resources/test_checkfunctions_gaps/memset_edge_cases.c'], returncode=0, stdout='', stderr='').combin

### `rc_mismatch_got0_want6` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_checkfunctions_gaps.test_all_log_function_variants`
  > AssertionError: assert 0 == 6
  >  +  where 0 = <built-in method count of str object at 0x7fb892e94030>('invalidFunctionArg')
  >  +    where <built-in method count of str object at 0x7fb892e94030> = ''.count
  >  +      where '' = CompletedProcess(args=['./executable', '--enable=warning', '/workspace/eval/test_resources/test_checkfunctions_gaps/multiple_log_variants.c'], returncode=0, stdout='', stderr='').co

### `bytes_output_mismatch` — 1 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_config_and_env.test_cppcheck_cfg_next_to_executable_overrides_product_name`
  > AssertionError: assert b'' == b'MyProduct 9.9'
  >   
  >   Full diff:
  >   - (b'MyProduct 9.9')
  >   + b''

### `empty_list_or_string` — 1 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_help_usage.test_help_has_title_line`
  > IndexError: list index out of range

### `json_output_missing_or_bad` — 1 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `tests.helloworld_test.test_sarif`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

### `rc_mismatch_got0_want7` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.other_test.test_showtime_top5_file`
  > assert 0 == 7
  >  +  where 0 = len([])

