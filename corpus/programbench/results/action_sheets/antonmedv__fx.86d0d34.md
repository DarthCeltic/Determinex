# Action Sheet — antonmedv__fx.86d0d34

**Current:** 16.39%  (492/3002)
**Pass / Fail / Skip:** 492 / 1066 / 0
**Gap to 100%:** 83.61 percentage points (2510 tests)

## Failure clusters

1066 failed tests grouped into 18 buckets (sorted by count).

### `other_assertion` — 485 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_additional_coverage.TestAdditionalCoverage.test_array_includes`
  > AssertionError: assert b'true' in b''
  >  +  where b'' = CompletedProcess(args=['./executable', 'x => x.includes(3)'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_additional_coverage.TestAdditionalCoverage.test_array_indexOf`
  > AssertionError: assert b'2' in b''
  >  +  where b'' = CompletedProcess(args=['./executable', 'x => x.indexOf(3)'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_additional_coverage.TestAdditionalCoverage.test_string_toLowerCase`
  > AssertionError: assert b'hello' in b''
  >  +  where b'' = CompletedProcess(args=['./executable', 'x => x.toLowerCase()'], returncode=0, stdout=b'', stderr=b'').stdout
- *(... 482 more in this cluster)*

### `string_output_mismatch` — 193 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_builtin_functions.test_toBase64_function`
  > AssertionError: assert '' == 'hello'
  >   
  >   - hello
- `eval.tests.test_argparse_validation.test_comp_accepts_known_shells[bash]`
  > AssertionError: assert 'fx: unknown ... information.' == ''
  >   
  >   + fx: unknown option: --comp=bash
  >   + usage: fx [OPTIONS] [ARGS]
  >   + Try 'fx --help' for more information.
- `eval.tests.test_argparse_validation.test_comp_accepts_known_shells[zsh]`
  > AssertionError: assert 'fx: unknown ... information.' == ''
  >   
  >   + fx: unknown option: --comp=zsh
  >   + usage: fx [OPTIONS] [ARGS]
  >   + Try 'fx --help' for more information.
- *(... 190 more in this cluster)*

### `rc_mismatch_got2_want0` — 168 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_additional_coverage.TestAdditionalCoverage.test_multiple_json_lines_slurp`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--slurp', 'x => x.length'], returncode=2, stdout=b'', stderr=b"fx: unknown option: --slurp\nusage: fx [OPTIONS] [ARGS]\nTry 'fx --help' for more i
- `tests.test_additional_coverage.TestAdditionalCoverage.test_yaml_list`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--yaml', 'x => x.length'], returncode=2, stdout=b'', stderr=b"fx: unknown option: --yaml\nusage: fx [OPTIONS] [ARGS]\nTry 'fx --help' for more inf
- `tests.test_additional_coverage.TestAdditionalCoverage.test_yaml_nested_structure`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--yaml', '.root.child.value'], returncode=2, stdout=b'', stderr=b"fx: unknown option: --yaml\nusage: fx [OPTIONS] [ARGS]\nTry 'fx --help' for more
- *(... 165 more in this cluster)*

### `json_output_missing_or_bad` — 100 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `tests.test_additional_coverage.TestAdditionalCoverage.test_object_entries`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_advanced_operations.TestAdvancedOperations.test_object_keys`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_advanced_operations.TestAdvancedOperations.test_object_values`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- *(... 97 more in this cluster)*

### `rc_unexpected_zero` — 37 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_error_handling.TestErrorHandling.test_invalid_json_unclosed_brace`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '.'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_error_handling.TestErrorHandling.test_invalid_json_single_quotes`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '.'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_error_handling.TestErrorHandling.test_invalid_javascript_syntax`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'x => x +'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 34 more in this cluster)*

### `rc_mismatch_got0_want1` — 37 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_builtin_functions.test_exit_function_one`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'exit(1)'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_coverage_improvements.test_invalid_json_input`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '.'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_coverage_improvements.test_unclosed_json_object`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '.'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 34 more in this cluster)*

### `rc_mismatch_got2_want1` — 17 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_coverage_improvements.test_yaml_and_toml_conflict`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--yaml', '--toml', '.'], returncode=2, stdout=b'', stderr=b"fx: unknown option: --yaml\nusage: fx [OPTIONS] [ARGS]\nTry 'fx --help' for m
- `tests.test_coverage_improvements.test_yaml_and_raw_conflict`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--yaml', '--raw', '.'], returncode=2, stdout=b'', stderr=b"fx: unknown option: --yaml\nusage: fx [OPTIONS] [ARGS]\nTry 'fx --help' for mo
- `tests.test_coverage_improvements.test_toml_and_raw_conflict`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--toml', '--raw', '.'], returncode=2, stdout=b'', stderr=b"fx: unknown option: --toml\nusage: fx [OPTIONS] [ARGS]\nTry 'fx --help' for mo
- *(... 14 more in this cluster)*

### `returned_none` — 7 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_basic_invocation.TestBasicInvocation.test_version_flag_v_uppercase`
  > AssertionError: assert None
  >  +  where None = <function match at 0x7f8fba48e170>(b'^\\d+\\.\\d+\\.\\d+\\s*$', b'fx 0.1.0\n')
  >  +    where <function match at 0x7f8fba48e170> = re.match
  >  +    and   b'fx 0.1.0\n' = CompletedProcess(args=['./executable', '-V'], returncode=0, stdout=b'fx 0.1.0\n', stderr=b'').stdout
- `tests.test_basic_invocation.TestBasicInvocation.test_version_flag_long`
  > AssertionError: assert None
  >  +  where None = <function match at 0x7f8fba48e170>(b'^\\d+\\.\\d+\\.\\d+\\s*$', b'fx 0.1.0\n')
  >  +    where <function match at 0x7f8fba48e170> = re.match
  >  +    and   b'fx 0.1.0\n' = CompletedProcess(args=['./executable', '--version'], returncode=0, stdout=b'fx 0.1.0\n', stderr=b'').stdout
- `tests.test_basic_invocation.test_version_flag_uppercase`
  > AssertionError: assert None
  >  +  where None = <function match at 0x7f873723d120>(b'^\\d+\\.\\d+\\.\\d+\\s*$', b'fx 0.1.0\n')
  >  +    where <function match at 0x7f873723d120> = re.match
  >  +    and   b'fx 0.1.0\n' = CompletedProcess(args=['/workspace/executable', '-V'], returncode=0, stdout=b'fx 0.1.0\n', stderr=b'').stdout
- *(... 4 more in this cluster)*

### `uncategorized` — 5 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_stdlib_functions.TestStdlibFunctions.test_sortKeys_function`
  > ValueError: substring not found
- `tests.test_additional_stdlib.test_sortBy_numeric`
  > ValueError: substring not found
- `tests.test_builtin_functions.test_sortKeys_function`
  > ValueError: substring not found
- *(... 2 more in this cluster)*

### `boolean_false` — 5 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_argument_parsing.TestVersionFlag.test_version_flag[-V]`
  > assert False
  >  +  where False = all(<generator object TestVersionFlag.test_version_flag.<locals>.<genexpr> at 0x7f8767bab530>)
- `tests.test_argument_parsing.TestVersionFlag.test_version_flag[--version]`
  > assert False
  >  +  where False = all(<generator object TestVersionFlag.test_version_flag.<locals>.<genexpr> at 0x7f8767ba9a10>)
- `tests.test_help_output.test_help_starts_with_newline`
  > assert False
  >  +  where False = <built-in method startswith of str object at 0x7fb2f93e2d30>('\n')
  >  +    where <built-in method startswith of str object at 0x7fb2f93e2d30> = 'fx 0.1.0 - command-line JSON viewer/processor\n\nUsage: fx [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, 
  >  +      where 'fx 0.1.0 - command-line JSON viewer/processor\n\nUsage: fx [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n\nExamples:\n  cat data.json | fx .
- *(... 2 more in this cluster)*

### `rc_mismatch_got0_want2` — 3 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_fx_cli_json_parser_strictness.test_ext_json_parse_invalid_escape_panics_in_non_strict_mode_currently`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '.'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_engine_internals.test_nested_map_operations`
  > assert 0 == 2
  >  +  where 0 = len([])
- `tests.test_engine_pretty_gaps.test_exit_code_custom_values`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'exit(2)'], returncode=0, stdout=b'', stderr=b'').returncode

### `bytes_output_mismatch` — 2 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `eval.tests.test_fx_cli.test_help_exact_snapshot`
  > assert b'fx 0.1.0 - ...fx \'.[0]\'\n' == b'\n  fx 39.2...@medv.io>\n\n'
  >   
  >   At index 0 diff: b'f' != b'\n'
  >   
  >   Full diff:
  >   + (b'fx 0.1.0 - command-line JSON viewer/processor\n\nUsage: fx [OPTIONS] [ARGS'
  >   +  b']\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print versi'
  >   +  b'on\n\nExamples:\n  cat data.json | fx .name\n  echo \'{"a":1}\' | fx .a\n  '...
- `eval.tests.test_fx_cli.test_version_exact`
  > AssertionError: assert b'fx 0.1.0\n' == b'39.2.0\n'
  >   
  >   At index 0 diff: b'f' != b'3'
  >   
  >   Full diff:
  >   - (b'39.2.0\n')
  >   + (b'fx 0.1.0\n')

### `subprocess_failed` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_fuzzy_utils_normalize.test_fuzzy_search_diacritics_comprehensive`
  > subprocess.CalledProcessError: Command '['/workspace/tui2cli', '-n', 'test_diacritics', 'start', '--', '/workspace/executable', '/workspace/eval/test_resources/test_fuzzy_utils_normalize/accented_keys
- `tests.test_jsonx_edge_cases.test_deeply_nested_structure_150_levels`
  > subprocess.CalledProcessError: Command '['/workspace/tui2cli', '-n', 'test_deep_nest_150', 'start', '--', '/workspace/executable', '/workspace/eval/test_resources/test_jsonx_edge_cases/deep_nest_150.j

### `rc_mismatch_got0_want42` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_builtin_functions.test_exit_function`
  > AssertionError: assert 0 == 42
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'exit(42)'], returncode=0, stdout=b'', stderr=b'').returncode

### `type_error` — 1 test(s)

**Quick patch ideas:**
- Specific TypeError; check arg types vs expected

**Sample failures:**

- `tests.test_coverage_targeted.test_vm_with_prelude`
  > TypeError: run() got an unexpected keyword argument 'args'

### `rc_mismatch_got1_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_input_formats.TestJSONInput.test_ndjson_without_slurp`
  > AssertionError: assert 1 == 3
  >  +  where 1 = len([''])

### `rc_mismatch_got0_want5` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_engine_pretty_gaps.test_exit_with_custom_code`
  > AssertionError: assert 0 == 5
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'exit(5)'], returncode=0, stdout=b'', stderr=b'').returncode

### `test_timeout` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_harvest.test_main_TestOutput`
  > subprocess.TimeoutExpired: Command '['go', 'test', '-v', '-run', '^TestOutput$', '.']' timed out after 30 seconds

