# Action Sheet — astro__deadnix.d590041

**Current:** 18.61%  (177/951)
**Pass / Fail / Skip:** 177 / 531 / 1
**Gap to 100%:** 81.39 percentage points (774 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_options_and_exit_codes.test_no_lambda_arg_flag_suppresses`
  - reason: test_no_lambda_arg_flag_suppresses depends on test_no_lambda_arg_default_finds_unused_arg

## Failure clusters

531 failed tests grouped into 15 buckets (sorted by count).

### `other_assertion` — 298 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_help_flag`
  > AssertionError: assert b'Find dead code in .nix files' in b'Warning:\nexample.nix\n'
  >  +  where b'Warning:\nexample.nix\n' = CompletedProcess(args=['/workspace/executable', '--help'], returncode=0, stdout=b'Warning:\nexample.nix\n', stderr=b'').stdout
- `tests.test_basic_invocation.test_version_flag`
  > AssertionError: assert b'deadnix' in b'Warning:\nexample.nix\n'
  >  +  where b'Warning:\nexample.nix\n' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'Warning:\nexample.nix\n', stderr=b'').stdout
- `tests.test_basic_invocation.test_no_arguments_scans_current_directory`
  > AssertionError: assert b'Unused declarations were found' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable'], returncode=0, stdout=b'', stderr=b'').stdout
- *(... 295 more in this cluster)*

### `string_output_mismatch` — 108 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_output.test_help_has_one_line_summary`
  > AssertionError: assert 'Warning:' == 'Find dead code in .nix files'
  >   
  >   - Find dead code in .nix files
  >   + Warning:
- `eval.tests.test_help_output.test_baseline_help_output_matches_fixture`
  > AssertionError: assert 'Warning:\nexample.nix\n' == 'Find dead co...int version\n'
  >   
  >   + Warning:
  >   + example.nix
  >   - Find dead code in .nix files
  >   - 
  >   - Usage: executable [OPTIONS] [FILE_PATHS]...
  >   - ...
- `tests.test_no_subcommands.TestSingleCommandBehavior.test_short_and_long_options_work_directly`
  > AssertionError: assert 'Usage: deadn...ting with _\n' == 'Find dead co...it\n--quiet\n'
  >   
  >   + Usage: deadnix [OPTIONS] [FILE_PATHS]...
  >     Find dead code in .nix files
  >   + 
  >     Options:
  >   - --no-lambda-arg
  >   - --edit...
- *(... 105 more in this cluster)*

### `rc_mismatch_got0_want1` — 55 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_basic_invocation.test_fail_flag_exit_code_one_with_dead_code`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--fail', '/tmp/tmpj_d47o2y/dirty.nix'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_basic_invocation.test_fail_flag_shorthand`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-f', '/tmp/tmpplgxuhn4/dirty.nix'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_editing.test_edit_with_fail_flag`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--edit', '--fail', '/tmp/tmp8tn7falq/test.nix'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 52 more in this cluster)*

### `json_output_missing_or_bad` — 23 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `eval.tests.test_argparse_validation.test_output_format_json_long_equals_form_outputs_json_on_stdout`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `eval.tests.test_argparse_validation.test_output_format_json_short_flag_space_value_equivalent`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `eval.tests.test_deadnix_io.test_output_format_json_is_valid_json_and_schema`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- *(... 20 more in this cluster)*

### `rc_mismatch_got0_want2` — 11 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_output_formats.test_json_output_multiple_issues`
  > assert 0 == 2
  >  +  where 0 = len([])
- `eval.tests.test_argparse_validation.test_unknown_flag_errors_and_exit_code_2`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--nonexistent-flag'], returncode=0, stdout='', stderr='').returncode
- `eval.tests.test_argparse_validation.test_invalid_enum_value_for_output_format_errors_and_exit_code_2`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--output-format', 'xml'], returncode=0, stdout='', stderr='').returncode
- *(... 8 more in this cluster)*

### `missing_dict_key` — 10 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_argparse_validation.test_flag_after_positional_is_accepted_and_changes_behavior`
  > KeyError: 'file'
- `tests.test_cli.test_json_output_complex_file`
  > KeyError: 'file'
- `tests.test_file_discovery.test_single_nix_file_explicit_path`
  > KeyError: 'file'
- *(... 7 more in this cluster)*

### `rc_unexpected_zero` — 6 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_no_subcommands.TestSingleCommandBehavior.test_unknown_flag_error_not_subcommand_error`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '--nonexistent-flag'], returncode=0, stdout='', stderr='').returncode
- `tests.test_basic_options.TestBasicOptions.test_invalid_option`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--invalid-option'], returncode=0, stdout='', stderr='').returncode
- `tests.test_output_formats.TestOutputFormats.test_invalid_output_format`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--output-format', 'invalid', '/workspace/eval/tests/fixtures/clean.nix'], returncode=0, stdout='', stderr='').returncode
- *(... 3 more in this cluster)*

### `boolean_false` — 6 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_specific_patterns.TestSpecificPatterns.test_unused_inherit`
  > assert False
  >  +  where False = any(<generator object TestSpecificPatterns.test_unused_inherit.<locals>.<genexpr> at 0x7f1434647a70>)
- `tests.test_specific_patterns.TestSpecificPatterns.test_lambda_pattern_vs_arg`
  > assert False
  >  +  where False = any(<generator object TestSpecificPatterns.test_lambda_pattern_vs_arg.<locals>.<genexpr> at 0x7f14346a0eb0>)
- `tests.test_specific_patterns.TestSpecificPatterns.test_shadowed_binding`
  > assert False
  >  +  where False = any(<generator object TestSpecificPatterns.test_shadowed_binding.<locals>.<genexpr> at 0x7f14346a26c0>)
- *(... 3 more in this cluster)*

### `rc_mismatch_got0_want3` — 4 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_core_analysis.test_let_multiple_unused_bindings`
  > assert 0 == 3
  >  +  where 0 = len([])
- `tests.test_core_analysis.test_let_recursive_dead_chain`
  > assert 0 == 3
  >  +  where 0 = len([])
- `tests.test_core_analysis.test_inherit_all_dead_attributes`
  > assert 0 == 3
  >  +  where 0 = len([])
- *(... 1 more in this cluster)*

### `rc_mismatch_got3_want1` — 4 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_file_operations.TestFileOperations.test_hidden_files_default`
  > assert 3 == 1
  >  +  where 3 = len(['{', '  "results": []', '}'])
- `tests.test_file_operations.TestFileOperations.test_exclude_single_file`
  > assert 3 == 1
  >  +  where 3 = len(['{', '  "results": []', '}'])
- `tests.test_file_operations.TestFileOperations.test_exclude_multiple_files`
  > assert 3 == 1
  >  +  where 3 = len(['{', '  "results": []', '}'])
- *(... 1 more in this cluster)*

### `rc_mismatch_got3_want2` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_core_analysis.test_multiple_files_separate_results`
  > assert 3 == 2
  >  +  where 3 = len(['{', '  "results": []', '}'])
- `tests.test_file_operations.TestFileOperations.test_multiple_files`
  > assert 3 == 2
  >  +  where 3 = len(['{', '  "results": []', '}'])

### `bytes_output_mismatch` — 1 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_output_formats.test_json_output_no_issues`
  > assert b'{\n  "results": []\n}\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'{\n  "results": []\n}\n')

### `returned_none` — 1 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_output.test_help_flag_is_documented_without_short_h`
  > AssertionError: assert None is not None
  >  +  where None = <function search at 0x7f170dfc2680>('^\\s*--help\\b', 'Warning:\nexample.nix\n', re.MULTILINE)
  >  +    where <function search at 0x7f170dfc2680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE

### `rc_mismatch_got15_want2` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_file_operations.TestFileOperations.test_hidden_flag`
  > AssertionError: assert 15 == 2
  >  +  where 15 = len(['Usage: deadnix [OPTIONS] [FILE_PATHS]...', 'Find dead code in .nix files', 'Options:', '  --edit              Edit files in place', '  --exclude <pattern> Exclude files matching p

### `rc_mismatch_got2_want1` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_help_version.test_version_prints_semverish`
  > AssertionError: assert 2 == 1
  >  +  where 2 = <built-in method count of str object at 0x7fabbeb50120>('\n')
  >  +    where <built-in method count of str object at 0x7fabbeb50120> = 'Warning:\nexample.nix\n'.count
  >  +      where 'Warning:\nexample.nix\n' = RunResult(args=['--version'], returncode=0, stdout='Warning:\nexample.nix\n', stderr='').stdout

