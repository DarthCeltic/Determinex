# Action Sheet — kisielk__errcheck.dacab89

**Current:** 17.61%  (100/568)
**Pass / Fail / Skip:** 100 / 428 / 4
**Gap to 100%:** 82.39 percentage points (468 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_errcheck_behavior.test_ignoretests_removes_test_file_findings_and_matches_golden`
  - reason: test_ignoretests_removes_test_file_findings_and_matches_golden depends on test_check_testdata_matches_golden_output
- `eval.tests.test_errcheck_behavior.test_abspath_makes_paths_absolute`
  - reason: test_abspath_makes_paths_absolute depends on test_check_testdata_matches_golden_output
- `eval.tests.test_errcheck_behavior.test_exclude_file_filters_specific_function`
  - reason: test_exclude_file_filters_specific_function depends on test_check_testdata_matches_golden_output
- `eval.tests.test_errcheck_behavior.test_excludeonly_matches_golden_and_contains_excluded_lines`
  - reason: test_excludeonly_matches_golden_and_contains_excluded_lines depends on test_check_testdata_matches_golden_output

## Failure clusters

428 failed tests grouped into 16 buckets (sorted by count).

### `other_assertion` — 170 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_asserts_flag.test_asserts_flag_checks_type_assertions`
  > AssertionError: assert 0 > 0
  >  +  where 0 = len('')
- `tests.test_asserts_flag.test_asserts_flag_with_blank`
  > assert 0 > 0
  >  +  where 0 = len([])
- `tests.test_basic_invocation.test_help_flag_displays_usage`
  > AssertionError: assert b'Usage of' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', '--help'], returncode=2, stdout=b'main_test.go\nUNCHECKED\ntestdata/main.go\n', stderr=b'').stderr
- *(... 167 more in this cluster)*

### `string_output_mismatch` — 83 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_usage.test_help_and_h_outputs_match_exactly`
  > AssertionError: assert 'main_test.go...ata/main.go\n' == 'errcheck 0.1...int version\n'
  >   
  >   + main_test.go
  >   + UNCHECKED
  >   + testdata/main.go
  >   - errcheck 0.1.0
  >   - Format files or stdin
  >   - ...
- `eval.tests.test_errcheck_behavior.test_check_testdata_matches_golden_output`
  > AssertionError: assert '' == 'testdata/mai...eNilError()\n'
  >   
  >   - testdata/main.go:29:10:	recover()     // UNCHECKED
  >   - testdata/main.go:32:15:	defer recover() // UNCHECKED
  >   - testdata/main.go:80:3:	a()     // UNCHECKED
  >   - testdata/main.go:84:3:	b()        // UNCHECKED
  >   - testdata/main.go:88:13:	customError()     // UNCHECKED
  >   - testdata/main.go:92:21:	customConcreteError()             // UNCHECKED...
- `tests.test_build_tags.test_single_build_tag_includes_file`
  > AssertionError: assert 'custom1.go:9...rintln(nil)\n' == 'custom1.go:9...rintln(nil)\n'
  >   
  >     custom1.go:9:14:	fmt.Fprintln(nil)
  >   + custom2.go:9:14:	fmt.Fprintln(nil)
- *(... 80 more in this cluster)*

### `rc_mismatch_got0_want1` — 81 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_basic_invocation.test_no_arguments_checks_current_directory`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable'], returncode=0, stdout=b'\n', stderr=b'').returncode
- `tests.test_errcheck.test_exit_code_unchecked_errors`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'github.com/kisielk/errcheck/testdata'], returncode=0, stdout=b"[scaffold-recover] FileNotFoundError: [Errno 2] No such file or directory:
- `tests.test_errcheck.test_single_package_path`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'github.com/kisielk/errcheck/testdata'], returncode=0, stdout=b"[scaffold-recover] FileNotFoundError: [Errno 2] No such file or directory:
- *(... 78 more in this cluster)*

### `rc_mismatch_got2_want1` — 30 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_ignore_flag.test_ignore_empty_value`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-ignore', '', './testdata'], returncode=2, stdout=b'UNCHECKED\n', stderr=b'').returncode
- `tests.test_errcheck.test_exclude_with_comments`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-exclude', '/tmp/tmp62fdwzod/excludes.txt', 'github.com/kisielk/errcheck/testdata'], returncode=2, stdout=b'', stderr=b'').returncode
- `tests.test_errcheck.test_ignore_pattern_deprecated_still_works`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-ignore', ':recover.*', 'github.com/kisielk/errcheck/testdata'], returncode=2, stdout=b'UNCHECKED\n', stderr=b'').returncode
- *(... 27 more in this cluster)*

### `rc_mismatch_got0_want2` — 14 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `eval.tests.test_argparse_validation.test_basic_flag_parse_errors_and_exit_codes[args1-2-flag provided but not defined]`
  > assert 0 == 2
- `eval.tests.test_argparse_validation.test_basic_flag_parse_errors_and_exit_codes[args2-2-flag provided but not defined]`
  > assert 0 == 2
- `eval.tests.test_argparse_validation.test_basic_flag_parse_errors_and_exit_codes[args4-2-invalid boolean value "foo" for -verbose]`
  > assert 0 == 2
- *(... 11 more in this cluster)*

### `rc_mismatch_got1_want0` — 13 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `eval.tests.test_argparse_validation.test_repeatable_flag_ignore_can_be_specified_multiple_times`
  > assert 1 == 0
- `eval.tests.test_argparse_validation.test_comma_list_flag_ignorepkg_accepts_commas`
  > assert 1 == 0
- `eval.tests.test_argparse_validation.test_mod_flag_invalid_value_is_not_a_flag_parse_error_and_exit_code_is_zero`
  > assert 1 == 0
- *(... 10 more in this cluster)*

### `rc_unexpected_zero` — 13 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `eval.tests.test_help_usage.test_help_with_dashdash_still_shows_usage`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--', '-h'], returncode=0, stdout="[scaffold-recover] FileNotFoundError: [Errno 2] No such file or directory: '-h'\n(*command-line-argumen
- `tests.test_subcommands.TestNoSubcommandAliases.test_no_subcommand_aliases[ls]`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'ls'], returncode=0, stdout="[scaffold-recover] FileNotFoundError: [Errno 2] No such file or directory: 'ls'\n(*command-line-arguments.MyStruct).Po
- `tests.test_subcommands.TestNoSubcommandAliases.test_no_subcommand_aliases[list]`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'list'], returncode=0, stdout="[scaffold-recover] FileNotFoundError: [Errno 2] No such file or directory: 'list'\n(*command-line-arguments.MyStruct
- *(... 10 more in this cluster)*

### `boolean_false` — 6 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_abspath_flag.test_abspath_default_relative_paths`
  > assert False
  >  +  where False = any(<generator object test_abspath_default_relative_paths.<locals>.<genexpr> at 0x7fdeba85f5a0>)
- `tests.test_abspath_flag.test_abspath_flag_shows_absolute_paths`
  > assert False
  >  +  where False = any(<generator object test_abspath_flag_shows_absolute_paths.<locals>.<genexpr> at 0x7fdeba85f760>)
- `tests.test_errcheck.test_abspath_prints_absolute_paths`
  > assert False
  >  +  where False = any(<generator object test_abspath_prints_absolute_paths.<locals>.<genexpr> at 0x7f04d5b0fdf0>)
- *(... 3 more in this cluster)*

### `rc_mismatch_got1_want2` — 6 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_errcheck.TestEdgeCases.test_syntax_error_in_code`
  > assert 1 == 2
- `eval.tests.test_errcheck_behavior.test_invalid_mod_value_reports_error_and_exit_code_is_two`
  > assert 1 == 2
- `tests.test_cli_flags.test_blank_and_asserts_combined`
  > assert 1 == 2
  >  +  where 1 = len(['multiple_errors.go:8:16:\tos.ReadFile("file3.txt")'])
- *(... 3 more in this cluster)*

### `rc_mismatch_got2_want0` — 5 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_errcheck.TestBasicExecution.test_h_flag`
  > assert 2 == 0
- `tests.test_errcheck.TestExcludeFlag.test_exclude_with_comments`
  > assert 2 == 0
- `tests.test_errcheck.TestIgnoreFlag.test_ignore_flag_basic`
  > assert 2 == 0
- *(... 2 more in this cluster)*

### `rc_mismatch_got0_want29` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_errcheck_externalized.test_ext_check_testdata_markers_counts[args1-54-25-0]`
  > AssertionError: assert 0 == 29
  >  +  where 0 = <built-in method count of str object at 0x7f352e068030>('UNCHECKED')
  >  +    where <built-in method count of str object at 0x7f352e068030> = ''.count
- `tests.test_errcheck_externalized.test_ext_check_testdata_markers_counts[args2-62-25-8]`
  > AssertionError: assert 0 == 29
  >  +  where 0 = <built-in method count of str object at 0x7f352cdb58e0>('UNCHECKED')
  >  +    where <built-in method count of str object at 0x7f352cdb58e0> = 'ReadFile\nFprintln\nm1\n'.count

### `returned_none` — 1 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_output_format.test_output_contains_line_numbers`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7fdebc3bf760>(':\\d+:', '')
  >  +    where <function search at 0x7fdebc3bf760> = re.search

### `rc_mismatch_got3_want64` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_errcheck_externalized.test_ext_parseFlags_effect_via_behavior_on_testdata_dir[args1-64]`
  > AssertionError: assert 3 == 64
  >  +  where 3 = len(['ReadFile', 'Fprintln', 'm1'])

### `rc_mismatch_got0_want50` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_flags.test_large_file_with_many_errors`
  > assert 0 == 50
  >  +  where 0 = len([])

### `rc_mismatch_got3_want2` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_flags.test_package_with_multiple_files`
  > AssertionError: assert 3 == 2
  >  +  where 3 = len(['.go:', 'main.go', 'UNCHECKED'])

### `rc_mismatch_got0_want30` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_stress.test_stress_combination_abspath_verbose`
  > assert 0 == 30
  >  +  where 0 = len([])

