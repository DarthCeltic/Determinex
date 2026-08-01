# Action Sheet — tinycc__tinycc.9b8765d

**Current:** 0.56%  (13/2341)
**Pass / Fail / Skip:** 13 / 1584 / 2
**Gap to 100%:** 99.44 percentage points (2328 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_ar.test_ar_extract_to_readonly_directory`
  - reason: Test requires non-root user
- `tests.test_harvest.test_harvest_tests2[113_btdll-source_file24-expect_file24]`
  - reason: Test 113_btdll requires complex DLL setup not suitable for simple wrapper

## Failure clusters

1584 failed tests grouped into 17 buckets (sorted by count).

### `other_assertion` — 764 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_tcc.test_help_flag`
  > AssertionError: assert b'Tiny C Compiler' in b'tinycc 0.1.0 - bootstrap scaffold\n\nUsage: tinycc [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n'
  >  +  where b'tinycc 0.1.0 - bootstrap scaffold\n\nUsage: tinycc [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['/workspace/executa
- `tests.test_tcc.test_help_long_flag`
  > AssertionError: assert b'Tiny C Compiler' in b'tinycc 0.1.0 - bootstrap scaffold\n\nUsage: tinycc [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n'
  >  +  where b'tinycc 0.1.0 - bootstrap scaffold\n\nUsage: tinycc [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['/workspace/executa
- `tests.test_tcc.test_version_flag`
  > AssertionError: assert b'tcc version' in b'tinycc 0.1.0\n'
  >  +  where b'tinycc 0.1.0\n' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'tinycc 0.1.0\n', stderr=b'').stdout
- *(... 761 more in this cluster)*

### `rc_mismatch_got2_want0` — 516 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_tcc.test_no_args_shows_help`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b"usage: tinycc [OPTIONS] [ARGS]\nTry 'tinycc --help' for more information.\n").returncode
- `tests.test_tcc.test_help_hh_flag`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-hh'], returncode=2, stdout=b'', stderr=b"tinycc: unknown option: -hh\nusage: tinycc [OPTIONS] [ARGS]\nTry 'tinycc --help' for more infor
- `tests.test_tcc.test_version_short_flag`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-v'], returncode=2, stdout=b'', stderr=b"tinycc: unknown option: -v\nusage: tinycc [OPTIONS] [ARGS]\nTry 'tinycc --help' for more informa
- *(... 513 more in this cluster)*

### `string_output_mismatch` — 87 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_ar.test_ar_error_missing_archive_file`
  > assert 'tinycc: unkn...nformation.\n' == "tcc: ar: can...nexistent.a\n"
  >   
  >   - tcc: ar: can't open file nonexistent.a
  >   + tinycc: unknown option: -ar
  >   + usage: tinycc [OPTIONS] [ARGS]
  >   + Try 'tinycc --help' for more information.
- `tests.test_ar.test_ar_error_invalid_archive_format`
  > AssertionError: assert 'tinycc: unkn...nformation.\n' == 'tcc: ar: not...ive_2/bad.a\n'
  >   
  >   - tcc: ar: not an ar archive /tmp/pytest-of-root/pytest-0/test_ar_error_invalid_archive_2/bad.a
  >   + tinycc: unknown option: -ar
  >   + usage: tinycc [OPTIONS] [ARGS]
  >   + Try 'tinycc --help' for more information.
- `tests.test_ar.test_ar_error_missing_input_object`
  > assert 'tinycc: unkn...nformation.\n' == "tcc: ar: can...existent.o \n"
  >   
  >   - tcc: ar: can't open file nonexistent.o 
  >   + tinycc: unknown option: -ar
  >   + usage: tinycc [OPTIONS] [ARGS]
  >   + Try 'tinycc --help' for more information.
- *(... 84 more in this cluster)*

### `rc_mismatch_got0_want1` — 44 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_codegen.test_assign_to_void_return_value_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/workspace/eval/test_resources/test_codegen/assign_to_void.c'], returncode=0, stdout='', stderr='').returncode
- `tests.test_errors.test_missing_input_file`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'nonexistent.c'], returncode=0, stdout='', stderr='').returncode
- `tests.test_errors.test_syntax_error_missing_semicolon`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/tmp/pytest-of-root/pytest-0/test_syntax_error_missing_semi2/test.c'], returncode=0, stdout='', stderr='').returncode
- *(... 41 more in this cluster)*

### `rc_mismatch_got2_want1` — 39 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_tcc.test_compile_error_exit_one`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-c', '/tmp/tmpyxhuues2/bad.c'], returncode=2, stdout=b'', stderr=b"tinycc: unknown option: -c\nusage: tinycc [OPTIONS] [ARGS]\nTry 'tinyc
- `tests.test_ar.test_ar_usage_message`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-ar'], returncode=2, stdout='', stderr="tinycc: unknown option: -ar\nusage: tinycc [OPTIONS] [ARGS]\nTry 'tinycc --help' for more informa
- `tests.test_ar.test_ar_error_invalid_flag_format`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-ar', '-x.y', 'test.a'], returncode=2, stdout='', stderr="tinycc: unknown option: -ar\nusage: tinycc [OPTIONS] [ARGS]\nTry 'tinycc --help
- *(... 36 more in this cluster)*

### `subprocess_failed` — 33 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_ar.test_ar_list_archive_contents`
  > subprocess.CalledProcessError: Command '['/workspace/executable', '-c', '/workspace/eval/test_resources/test_ar/add.c', '-o', '/tmp/pytest-of-root/pytest-0/test_ar_list_archive_contents2/add.o']' retu
- `tests.test_ar.test_ar_verbose_create`
  > subprocess.CalledProcessError: Command '['/workspace/executable', '-c', '/workspace/eval/test_resources/test_ar/add.c', '-o', '/tmp/pytest-of-root/pytest-0/test_ar_verbose_create2/add.o']' returned no
- `tests.test_ar.test_ar_extract_members`
  > subprocess.CalledProcessError: Command '['/workspace/executable', '-c', '/workspace/eval/test_resources/test_ar/add.c', '-o', '/tmp/pytest-of-root/pytest-0/test_ar_extract_members2/add.o']' returned n
- *(... 30 more in this cluster)*

### `rc_mismatch_got2_want255` — 31 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_run_mode.test_run_exit_code_255`
  > assert 2 == 255
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-run', '/tmp/pytest-of-root/pytest-0/test_run_exit_code_2552/exit255.c'], returncode=2, stdout='', stderr="tinycc: unknown option: -run\n
- `tests.test_run_mode.test_run_negative_exit_code`
  > assert 2 == 255
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-run', '/tmp/pytest-of-root/pytest-0/test_run_negative_exit_code2/negative.c'], returncode=2, stdout='', stderr="tinycc: unknown option: 
- `tests.test_runtime_backtrace.test_deep_call_stack_backtrace`
  > assert 2 == 255
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-bt', '-run', '/tmp/pytest-of-root/pytest-0/test_deep_call_stack_backtrace2/deep_stack.c'], returncode=2, stdout='', stderr="tinycc: unkn
- *(... 28 more in this cluster)*

### `rc_unexpected_zero` — 30 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_tcc.test_file_not_found_error`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'nonexistent_file.c'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_codegen.test_integer_division_by_zero_in_constant`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/workspace/eval/test_resources/test_codegen/int_div_zero.c'], returncode=0, stdout='', stderr='').returncode
- `tests.test_codegen.test_integer_modulo_by_zero_in_constant`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/workspace/eval/test_resources/test_codegen/int_mod_zero.c'], returncode=0, stdout='', stderr='').returncode
- *(... 27 more in this cluster)*

### `missing_file` — 22 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_compilation.test_basic_compile_single_file`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_basic_compile_single_file2/factorial'
- `tests.test_compilation.test_multifile_compile_direct`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_multifile_compile_direct2/calc'
- `tests.test_compilation.test_stdin_input_compilation`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_stdin_input_compilation2/stdin_test'
- *(... 19 more in this cluster)*

### `rc_mismatch_got2_want42` — 6 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_tcc.test_run_exit_code`
  > assert 2 == 42
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-run', '/tmp/tmphirrel_z/exit.c'], returncode=2, stdout=b'', stderr=b"tinycc: unknown option: -run\nusage: tinycc [OPTIONS] [ARGS]\nTry '
- `tests.test_libtcc.test_compile_from_stdin`
  > assert 2 == 42
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-run', '-'], returncode=2, stdout='', stderr="tinycc: unknown option: -run\nusage: tinycc [OPTIONS] [ARGS]\nTry 'tinycc --help' for more 
- `tests.test_run_mode.test_run_exit_code_42`
  > assert 2 == 42
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-run', '/workspace/eval/test_resources/test_run_mode/exit_codes.c'], returncode=2, stdout='', stderr="tinycc: unknown option: -run\nusage
- *(... 3 more in this cluster)*

### `boolean_false` — 4 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_tcc.test_default_output_aout`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpr9_3rniv/a.out').exists
- `tests.test_tcc.test_listfile`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpgslgbx1m/test_list').exists
- `tests.test_libtcc.test_listfile_argument_expansion`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/pytest-of-root/pytest-0/test_listfile_argument_expansi2/test_from_list').exists
- *(... 1 more in this cluster)*

### `rc_mismatch_got2_want123` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_tcc.test_run_with_return_value`
  > assert 2 == 123
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-run', '/tmp/tmpx5d0e15l/exit_rv123.c'], returncode=2, stdout=b'', stderr=b"tinycc: unknown option: -run\nusage: tinycc [OPTIONS] [ARGS]\
- `tests.test_runtime_edge.test_nonzero_exit_code_propagation`
  > assert 2 == 123
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-run', '/workspace/eval/test_resources/test_runtime_edge/exit_codes.c', '123'], returncode=2, stdout='', stderr="tinycc: unknown option: 

### `bytes_output_mismatch` — 2 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_tcc.test_type_incompatibility_warning`
  > assert (2 == 0 or b'warning' in b"tinycc: unknown option: -c\nusage: tinycc [options] [args]\ntry 'tinycc --help' for more information.\n")
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-c', '/tmp/tmpzm1ql1je/typecomp.c'], returncode=2, stdout=b'', stderr=b"tinycc: unknown option: -c\nusage: tinycc [OPTIONS] [ARGS]\nTry '
  >  +  and   b"tinycc: unknown option: -c\nusage: tinycc [options] [args]\ntry 'tinycc --help' for more information.\n" = <built-in method lower of bytes object at 0x7f40567946f0>()
  >  +    where <built-in method lower of bytes object at 0x7f40567946f0> = b"tinycc: unknown option: -c\nusage: tinycc [OPTIONS] [ARGS]\nTry 'tinycc --help' for more information.\n".lower
  >  +      where b"tinycc: unknown option: -c\nusage: tinycc [OPTIONS] [ARGS]\nTry 'tinycc --help' for more information.\n" = CompletedProcess(args=['/workspace/executable', '-c', '/tmp/tmpzm1ql1je/typec
- `tests.test_tcc.test_wdiscarded_qualifiers`
  > assert (2 == 0 or b'warning' in b"tinycc: unknown option: -c\nusage: tinycc [options] [args]\ntry 'tinycc --help' for more information.\n")
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-c', '-Wdiscarded-qualifiers', '/tmp/tmphwuq8jjb/quals.c'], returncode=2, stdout=b'', stderr=b"tinycc: unknown option: -c\nusage: tinycc 
  >  +  and   b"tinycc: unknown option: -c\nusage: tinycc [options] [args]\ntry 'tinycc --help' for more information.\n" = <built-in method lower of bytes object at 0x7f40567944b0>()
  >  +    where <built-in method lower of bytes object at 0x7f40567944b0> = b"tinycc: unknown option: -c\nusage: tinycc [OPTIONS] [ARGS]\nTry 'tinycc --help' for more information.\n".lower
  >  +      where b"tinycc: unknown option: -c\nusage: tinycc [OPTIONS] [ARGS]\nTry 'tinycc --help' for more information.\n" = CompletedProcess(args=['/workspace/executable', '-c', '-Wdiscarded-qualifiers

### `returned_none` — 1 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_tcc.test_version_format`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f4060726680>(b'tcc version \\d+\\.\\d+', b'tinycc 0.1.0\n')
  >  +    where <function search at 0x7f4060726680> = re.search
  >  +    and   b'tinycc 0.1.0\n' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'tinycc 0.1.0\n', stderr=b'').stdout

### `rc_mismatch_got2_want7` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_tcc.test_run_mode`
  > assert 2 == 7
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-run', '/tmp/tmpt11wxuxw/run_test.c'], returncode=2, stdout=b'', stderr=b"tinycc: unknown option: -run\nusage: tinycc [OPTIONS] [ARGS]\nT

### `rc_mismatch_got2_want5` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_tcc.test_stdin_with_run`
  > assert 2 == 5
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-run', '-'], returncode=2, stdout=b'', stderr=b"tinycc: unknown option: -run\nusage: tinycc [OPTIONS] [ARGS]\nTry 'tinycc --help' for mor

### `rc_mismatch_got2_want17` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_libtcc.test_file_type_override_c`
  > assert 2 == 17
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-xc', '/tmp/pytest-of-root/pytest-0/test_file_type_override_c2/source.txt', '-run'], returncode=2, stdout='', stderr="tinycc: unknown opt

