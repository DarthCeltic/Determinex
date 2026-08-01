# Action Sheet — tomarrell__wrapcheck.c058da1

**Current:** 27.18%  (184/677)
**Pass / Fail / Skip:** 184 / 480 / 5
**Gap to 100%:** 72.82 percentage points (493 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_argparse.test_boolean_flag_accepts_equals_form[flag_form1]`
  - reason: Unsupported form for this executable
- `eval.tests.test_wrapcheck_behavior.test_context_flag_c_changes_output[-1-/workspace/wrapcheck/testdata/catch_fmt_sscanf/main.go:14:10: error returned from external package is unwrapped: sig: func fmt.Scanf(format string, a ...any) (n int, err error)\n]`
  - reason: test_context_flag_c_changes_output[-1-/workspace/wrapcheck/testdata/catch_fmt_sscanf/main.go:14:10: error returned from external package is unwrapped: sig: func fmt.Scanf(format string, a ...any) (n i
- `eval.tests.test_wrapcheck_behavior.test_context_flag_c_changes_output[0-/workspace/wrapcheck/testdata/catch_fmt_sscanf/main.go:14:10: error returned from external package is unwrapped: sig: func fmt.Scanf(format string, a ...any) (n int, err error)\n14\t\t\treturn err // want `error returned from external package is unwrapped`\n]`
  - reason: test_context_flag_c_changes_output[0-/workspace/wrapcheck/testdata/catch_fmt_sscanf/main.go:14:10: error returned from external package is unwrapped: sig: func fmt.Scanf(format string, a ...any) (n in
- `eval.tests.test_wrapcheck_behavior.test_context_flag_c_changes_output[1-/workspace/wrapcheck/testdata/catch_fmt_sscanf/main.go:14:10: error returned from external package is unwrapped: sig: func fmt.Scanf(format string, a ...any) (n int, err error)\n13\t\tif err != nil {\n14\t\t\treturn err // want `error returned from external package is unwrapped`\n15\t\t}\n]`
  - reason: test_context_flag_c_changes_output[1-/workspace/wrapcheck/testdata/catch_fmt_sscanf/main.go:14:10: error returned from external package is unwrapped: sig: func fmt.Scanf(format string, a ...any) (n in
- `tests.test_harvest.test_config_ignoreSigRegexps_fail`
  - reason: Test marked for analysistest_skip - tests analyzer initialization

## Failure clusters

480 failed tests grouped into 13 buckets (sorted by count).

### `other_assertion` — 189 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_wrapcheck.test_help_flag`
  > AssertionError: assert b'wrapcheck: Checks that errors returned from external packages are wrapped' in b''
  >  +  where b'' = CompletedProcess(args=['./executable', '--help'], returncode=0, stdout=b'wrapcheck 0.1.0\n\nusage: wrapcheck [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version 
- `tests.test_wrapcheck.test_version_flag_full`
  > AssertionError: assert b'version' in b''
  >  +  where b'' = CompletedProcess(args=['./executable', '-V=full'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_analysis.test_defer_goroutine_error_handling`
  > AssertionError: assert 'defer_goroutine.go:22:10' in ''
- *(... 186 more in this cluster)*

### `rc_mismatch_got0_want3` — 150 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_wrapcheck.test_analyze_package_with_issues`
  > AssertionError: assert 0 == 3
  >  +  where 0 = CompletedProcess(args=['./executable', './wrapcheck/testdata/simple_no_wrap'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_wrapcheck.test_analyze_with_test_files_default`
  > AssertionError: assert 0 == 3
  >  +  where 0 = CompletedProcess(args=['./executable', '/workspace/tmp/tmpsh10wk8k'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_wrapcheck.test_detect_unwrapped_json_error`
  > AssertionError: assert 0 == 3
  >  +  where 0 = CompletedProcess(args=['./executable', '/workspace/tmp/tmpxu62req9'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 147 more in this cluster)*

### `string_output_mismatch` — 36 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_cli.test_json_output_format_structure`
  > assert '' == '{\n\t"testda...\t]\n\t}\n}\n'
  >   
  >   - {
  >   - 	"testdata/simple_no_wrap": {
  >   - 		"wrapcheck": [
  >   - 			{
  >   - 				"posn": "testdata/simple_no_wrap/main.go:14:10",
  >   - 				"message": "error returned from external package is unwrapped: sig: func encoding/json.Marshal(v any) ([]byte, error)"...
- `tests.test_cli.test_zero_context_multiple_issues`
  > assert '' == '{\n\t"testda...\t]\n\t}\n}\n'
  >   
  >   - {
  >   - 	"testdata/simple_no_wrap": {
  >   - 		"wrapcheck": [
  >   - 			{
  >   - 				"posn": "testdata/simple_no_wrap/main.go:14:10",
  >   - 				"message": "error returned from external package is unwrapped: sig: func encoding/json.Marshal(v any) ([]byte, error)"...
- `tests.test_edge_cases.test_empty_package_no_functions`
  > AssertionError: assert '' == 'warning: GOC... data emitted'
  >   
  >   - warning: GOCOVERDIR not set, no coverage data emitted
- *(... 33 more in this cluster)*

### `json_output_missing_or_bad` — 34 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `tests.test_wrapcheck.test_flags_json_output`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_wrapcheck.test_json_output_format`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_wrapcheck.test_json_output_no_issues`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- *(... 31 more in this cluster)*

### `rc_mismatch_got0_want1` — 26 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_wrapcheck.test_version_flag_invalid`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', '-V=true'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_cli.test_version_flag_short_unsupported`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-V=short'], returncode=0, stdout='', stderr='').returncode
- `tests.test_cli.test_version_flag_bare_unsupported`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-V'], returncode=0, stdout='wrapcheck 0.1.0\n', stderr='').returncode
- *(... 23 more in this cluster)*

### `rc_unexpected_zero` — 24 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_wrapcheck.test_analyze_nonexistent_package`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', './nonexistent/package'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_wrapcheck.test_config_ignore_sig_regexps_fail`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', './wrapcheck/testdata/config_ignoreSigRegexps_fail'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_wrapcheck.test_config_invalid_yaml`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '/workspace/tmp/tmpq7kt0vc2'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 21 more in this cluster)*

### `boolean_false` — 7 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_wrapcheck.test_cpuprofile_flag`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/workspace/tmp/tmp58g5iw0z/cpu.prof').exists
- `tests.test_wrapcheck.test_memprofile_flag`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/workspace/tmp/tmp3poe0_qb/mem.prof').exists
- `tests.test_wrapcheck.test_trace_flag`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/workspace/tmp/tmp3s7nyy8x/trace.out').exists
- *(... 4 more in this cluster)*

### `rc_mismatch_got0_want2` — 6 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_cli.test_invalid_context_value_non_numeric`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-c', 'abc', '.'], returncode=0, stdout='', stderr='').returncode
- `eval.tests.test_argparse.test_flag_parse_errors_show_message_and_usage[args1-2-flag needs an argument]`
  > assert 0 == 2
- `eval.tests.test_argparse.test_flag_parse_errors_show_message_and_usage[args2-2-invalid value "abc" for flag -c]`
  > assert 0 == 2
- *(... 3 more in this cluster)*

### `rc_mismatch_got3_want1` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli.test_no_package_path_requires_explicit_package`
  > AssertionError: assert 3 == 1
  >  +  where 3 = CompletedProcess(args=['/workspace/executable'], returncode=3, stdout='', stderr='usage: wrapcheck [OPTIONS] [ARGS]\n').returncode
- `tests.test_cli_flags.test_no_package_argument`
  > AssertionError: assert 3 == 1
  >  +  where 3 = CompletedProcess(args=['/workspace/executable'], returncode=3, stdout='', stderr='usage: wrapcheck [OPTIONS] [ARGS]\n').returncode
- `eval.tests.test_argparse.test_no_args_errors_with_usage`
  > assert 3 == 1

### `returned_none` — 2 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_usage.test_test_flag_shows_default_true`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f061c3f2680>('\\-test\\s*\\n\\s+.*\\(default true\\)', 'wrapcheck 0.1.0\n\nusage: wrapcheck [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --v
  >  +    where <function search at 0x7f061c3f2680> = re.search
- `eval.tests.test_help_usage.test_context_flag_shows_default_minus_one`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f061c3f2680>('\\-c int\\s*\\n\\s+.*\\(default -1\\)', 'wrapcheck 0.1.0\n\nusage: wrapcheck [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --ve
  >  +    where <function search at 0x7f061c3f2680> = re.search

### `missing_file` — 1 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_wrapcheck.test_analyze_current_directory`
  > FileNotFoundError: [Errno 2] No such file or directory: './executable'

### `rc_mismatch_got2_want0` — 1 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `eval.tests.test_argparse.test_double_dash_separator_treats_following_as_positional`
  > assert 2 == 0

### `rc_mismatch_got0_want10` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_edge_cases.test_many_files_in_package`
  > AssertionError: assert 0 == 10
  >  +  where 0 = <built-in method count of str object at 0x7f8fd2aec030>('error returned from external package is unwrapped')
  >  +    where <built-in method count of str object at 0x7f8fd2aec030> = ''.count

