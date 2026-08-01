# Action Sheet — cweill__gotests.2a672c5

**Current:** 12.37%  (110/889)
**Pass / Fail / Skip:** 110 / 531 / 2
**Gap to 100%:** 87.63 percentage points (779 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_ai_feature.test_ai_integration_with_ollama`
  - reason: Ollama not running with model - skip in non-AI environments
- `tests.test_ai_feature.test_ai_warning_about_data_sent`
  - reason: Ollama not running - skip in non-AI environments

## Failure clusters

531 failed tests grouped into 6 buckets (sorted by count).

### `other_assertion` — 356 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_ai_generation.test_ai_flag_with_unreachable_endpoint`
  > assert (b'not available' in b'// generated tests for gotests.go\npackage main\n\nimport (\n\t"reflect"\n\t"testing"\n)\n\nfunc testgeneratetests(t *testing.t) {\n\ttests := []struct {\n\t\tname string
  >  +  where b'// generated tests for gotests.go\npackage main\n\nimport (\n\t"reflect"\n\t"testing"\n)\n\nfunc testgeneratetests(t *testing.t) {\n\ttests := []struct {\n\t\tname string\n\t\targs struct 
  >  +    where <built-in method lower of bytes object at 0x5648ad3650a0> = b'// Generated tests for gotests.go\npackage main\n\nimport (\n\t"reflect"\n\t"testing"\n)\n\nfunc TestGenerateTests(t *testing.
  >  +  and   b'// generated tests for gotests.go\npackage main\n\nimport (\n\t"reflect"\n\t"testing"\n)\n\nfunc testgeneratetests(t *testing.t) {\n\ttests := []struct {\n\t\tname string\n\t\targs struct 
  >  +    where <built-in method lower of bytes object at 0x5648ad3650a0> = b'// Generated tests for gotests.go\npackage main\n\nimport (\n\t"reflect"\n\t"testing"\n)\n\nfunc TestGenerateTests(t *testing.
- `tests.test_ai_generation.test_ai_model_flag`
  > assert b'TestAdd' in b'// Generated tests for gotests.go\npackage main\n\nimport (\n\t"reflect"\n\t"testing"\n)\n\nfunc TestGenerateTests(t *testing.T) {\n\ttests := []struct {\n\t\tname string\n\t\ta
  >  +  where b'// Generated tests for gotests.go\npackage main\n\nimport (\n\t"reflect"\n\t"testing"\n)\n\nfunc TestGenerateTests(t *testing.T) {\n\ttests := []struct {\n\t\tname string\n\t\targs struct 
- `tests.test_ai_generation.test_ai_min_cases_flag`
  > assert b'TestAdd' in b'// Generated tests for gotests.go\npackage main\n\nimport (\n\t"reflect"\n\t"testing"\n)\n\nfunc TestGenerateTests(t *testing.T) {\n\ttests := []struct {\n\t\tname string\n\t\ta
  >  +  where b'// Generated tests for gotests.go\npackage main\n\nimport (\n\t"reflect"\n\t"testing"\n)\n\nfunc TestGenerateTests(t *testing.T) {\n\ttests := []struct {\n\t\tname string\n\t\targs struct 
- *(... 353 more in this cluster)*

### `rc_mismatch_got1_want0` — 152 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_subcommand_dispatch.TestNoSubcommandStructure.test_no_args_shows_flag_requirement`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable'], returncode=1, stdout='', stderr='No Go files found\n').returncode
- `tests.test_ai_enhanced.test_ai_response_size_limit`
  > assert 1 == 0
- `tests.test_ai_enhanced.test_ai_duplicate_test_case_detection`
  > assert 1 == 0
- *(... 149 more in this cluster)*

### `string_output_mismatch` — 10 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_argparse_validation.test_double_dash_stops_flag_parsing_for_following_args`
  > AssertionError: assert 'flag provide...t defined: --' == ''
  >   
  >   + flag provided but not defined: --
- `tests.test_subcommand_dispatch.TestErrorHandling.test_mutually_exclusive_flags_handled`
  > AssertionError: assert (1 == 0 or 'error' in 'no go files found\n')
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-all', '-exported', '-only', 'test.*'], returncode=1, stdout='', stderr='No Go files found\n').returncode
  >  +  and   'no go files found\n' = <built-in method lower of str object at 0x7f0df45aeb00>()
  >  +    where <built-in method lower of str object at 0x7f0df45aeb00> = 'No Go files found\n'.lower
- `tests.test_gotests_externalized.test_ext_generate_function_with_no_receiver_params_results_matches_golden`
  > assert '// Generated...t})\n\t}\n}\n' == 'package test...1()\n\t}\n}\n'
  >   
  >   - package testdata
  >   + // Generated tests for gotests.go
  >   + package main
  >     
  >   - import "testing"
  >   + import (...
- *(... 7 more in this cluster)*

### `rc_mismatch_got2_want0` — 6 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_argument_parsing.TestBasicExecution.test_version_flag`
  > assert 2 == 0
- `eval.tests.test_help_version_and_errors.test_version_contains_fields_exit_0`
  > assert 2 == 0
  >  +  where 2 = RunResult(returncode=2, stdout=b'', stderr=b"usage: main.py [options] [files...]\nmain.py: error: argument -v/--version: ignored explicit argument 'ersion'\n").returncode
- `tests.test_gotests_externalized.test_ext_version_output_contains_expected_strings`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-version'], returncode=2, stdout=b'', stderr=b"usage: main.py [options] [files...]\nmain.py: error: argument -v/--version: ignored explic
- *(... 3 more in this cluster)*

### `boolean_false` — 5 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `eval.tests.test_generation_stdout_and_write_mode.test_generate_to_stdout_contains_generated_banner_and_test_code`
  > assert False
  >  +  where False = <built-in method startswith of str object at 0x558c1f59db60>('Generated TestAdd\n')
  >  +    where <built-in method startswith of str object at 0x558c1f59db60> = '// Generated tests for gotests.go\npackage main\n\nimport (\n\t"reflect"\n\t"testing"\n)\n\nfunc TestGenerateTests(t *testin
- `eval.tests.test_template_params_file.test_invalid_template_params_file_prints_error_to_stdout_exit_0`
  > assert False
  >  +  where False = <built-in method startswith of str object at 0x558c1f5ba110>('Failed to umarshal ')
  >  +    where <built-in method startswith of str object at 0x558c1f5ba110> = '// Generated tests for gotests.go\npackage main\n\nimport (\n\t"reflect"\n\t"testing"\n)\n\nfunc TestGenerateTests(t *testin
- `eval.tests.test_help_output.test_help_starts_with_usage_line_prefix`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7f7114f40030>('Usage of ')
  >  +    where <built-in method startswith of str object at 0x7f7114f40030> = ''.startswith
  >  +      where '' = CompletedProcess(args=['/workspace/executable', '--help'], returncode=0, stdout='usage: main.py [options] [files...]\n\nGenerate Go tests from source files\n\noptions:\n  -h, --help
- *(... 2 more in this cluster)*

### `returned_none` — 2 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_generation_stdout_and_write_mode.test_write_mode_creates_test_file_and_prints_only_banner`
  > AssertionError: assert None
  >  +  where None = <function fullmatch at 0x7fe275c43e20>('Generated TestAdd\\n?', 'Generated sample_test.go\n')
  >  +    where <function fullmatch at 0x7fe275c43e20> = re.fullmatch
  >  +    and   'Generated sample_test.go\n' = RunResult(returncode=0, stdout=b'Generated sample_test.go\n', stderr=b'').stdout_text
- `eval.tests.test_help_output.test_help_has_expected_tab_indentation_for_description_lines`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f7114eb2680>('^\\s+\\tgenerate test cases using AI', '', re.MULTILINE)
  >  +    where <function search at 0x7f7114eb2680> = re.search
  >  +    and   '' = CompletedProcess(args=['/workspace/executable', '--help'], returncode=0, stdout='usage: main.py [options] [files...]\n\nGenerate Go tests from source files\n\noptions:\n  -h, --help  
  >  +    and   re.MULTILINE = re.M

