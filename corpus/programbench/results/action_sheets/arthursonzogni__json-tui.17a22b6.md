# Action Sheet — arthursonzogni__json-tui.17a22b6

**Current:** 29.97%  (362/1208)
**Pass / Fail / Skip:** 362 / 457 / 0
**Gap to 100%:** 70.03 percentage points (846 tests)

## Failure clusters

457 failed tests grouped into 12 buckets (sorted by count).

### `other_assertion` — 151 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_argument_parsing.test_double_dash_separator`
  > AssertionError: assert 1 in [0, 124]
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '--', '/tmp/tmpb_ofa7l0/test.json'], returncode=1, stdout=b'', stderr=b'Invalid arguments\n').returncode
- `tests.test_argument_parsing.test_version_with_file_ignores_file`
  > AssertionError: assert b'1.4.1' in b'json-tui 0.1.0\n'
  >  +  where b'json-tui 0.1.0\n' = CompletedProcess(args=['/workspace/executable', '--version', '/tmp/tmpv82sof2o/test.json'], returncode=0, stdout=b'json-tui 0.1.0\n', stderr=b'').stdout
- `tests.test_argument_parsing.test_flag_precedence_help_version`
  > AssertionError: assert b'OPTIONS:' in b'json-tui 0.1.0\n'
  >  +  where b'json-tui 0.1.0\n' = CompletedProcess(args=['/workspace/executable', '--help', '--version'], returncode=0, stdout=b'json-tui 0.1.0\n', stderr=b'').stdout
- *(... 148 more in this cluster)*

### `string_output_mismatch` — 128 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_argument_parsing.TestVersionFlag.test_version_long_flag`
  > AssertionError: assert 'json-tui 0.1.0' == '1.4.1'
  >   
  >   - 1.4.1
  >   + json-tui 0.1.0
- `tests.test_argument_parsing.TestVersionFlag.test_version_short_flag`
  > AssertionError: assert 'json-tui 0.1.0' == '1.4.1'
  >   
  >   - 1.4.1
  >   + json-tui 0.1.0
- `tests.test_argument_parsing.TestFlagCombinations.test_version_then_keybinding`
  > AssertionError: assert 'json-tui 0.1.0' == '1.4.1'
  >   
  >   - 1.4.1
  >   + json-tui 0.1.0
- *(... 125 more in this cluster)*

### `rc_mismatch_got1_want0` — 51 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_argument_parsing.test_keybinding_with_file_ignores_file`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '--keybinding', '/tmp/tmp4lni9b_y/test.json'], returncode=1, stdout=b'', stderr=b'Could not open file --keybinding\n').returncode
- `tests.test_basic_invocation.test_keybinding_flag`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '--keybinding'], returncode=1, stdout=b'', stderr=b'Could not open file --keybinding\n').returncode
- `tests.test_basic_invocation.test_keybinding_short_k_flag`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-k'], returncode=1, stdout=b'', stderr=b'Reading from stdin...\n').returncode
- *(... 48 more in this cluster)*

### `rc_mismatch_got0_want124` — 34 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_json_tui.test_read_simple_json_from_file`
  > assert 0 == 124
  >  +  where 0 = CompletedProcess(args=['./executable', '/tmp/tmpovx0ifpa/test.json'], returncode=0, stdout=b'{\n  "name": "test",\n  "value": 123\n}\n', stderr=b'').returncode
- `tests.test_json_tui.test_read_array_from_file`
  > assert 0 == 124
  >  +  where 0 = CompletedProcess(args=['./executable', '/tmp/tmpda02ux91/array.json'], returncode=0, stdout=b'[\n  1,\n  2,\n  3,\n  "four",\n  true,\n  null\n]\n', stderr=b'').returncode
- `tests.test_json_tui.test_read_nested_json_from_file`
  > assert 0 == 124
  >  +  where 0 = CompletedProcess(args=['./executable', '/tmp/tmpli52ig15/nested.json'], returncode=0, stdout=b'{\n  "user": {\n    "name": "Alice",\n    "age": 30,\n    "address": {\n      "city": "NYC"
- *(... 31 more in this cluster)*

### `uncategorized` — 33 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_json_edge_cases.test_deeply_nested_objects_10_levels`
  > Failed: Binary exited instead of starting TUI. stdout: {
  >   "level": {
  >     "level": {
  >       "level": {
  >         "level": {
  >           "level": {
  >             "level": {
  >               "level": {
- `tests.test_json_edge_cases.test_deeply_nested_objects_50_levels`
  > Failed: Binary exited instead of starting TUI. stdout: {
  >   "level": {
  >     "level": {
  >       "level": {
  >         "level": {
  >           "level": {
  >             "level": {
  >               "level": {
- `tests.test_json_edge_cases.test_deeply_nested_objects_100_levels`
  > Failed: Binary exited instead of starting TUI. stdout: {
  >   "level": {
  >     "level": {
  >       "level": {
  >         "level": {
  >           "level": {
  >             "level": {
  >               "level": {
- *(... 30 more in this cluster)*

### `test_timeout` — 24 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_args_parsing.test_dash_dash_can_be_last_arg_and_then_stdin_is_used[args0]`
  > Failed: DID NOT RAISE <class 'subprocess.TimeoutExpired'>
- `eval.tests.test_args_parsing.test_dash_dash_can_be_last_arg_and_then_stdin_is_used[args1]`
  > Failed: DID NOT RAISE <class 'subprocess.TimeoutExpired'>
- `tests.test_json_tui.test_stdin_valid_json_starts_tui[{}]`
  > Failed: DID NOT RAISE <class 'subprocess.TimeoutExpired'>
- *(... 21 more in this cluster)*

### `rc_mismatch_got0_want1` — 19 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_additional_coverage.test_argument_after_double_dash`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', '--', '--version'], returncode=0, stdout=b'json-tui 0.1.0\n', stderr=b'').returncode
- `tests.test_args_and_errors.test_double_dash_with_flag_like_filename`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', '--', '--help'], returncode=0, stdout=b'json-tui 0.1.0\nA JSON terminal UI\n\nOPTIONS:\n  -h, --help              Display this help menu\n  -v, --v
- `tests.test_comprehensive_json.test_json_error_nan`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable'], returncode=0, stdout=b'NaN\n', stderr=b'').returncode
- *(... 16 more in this cluster)*

### `returned_none` — 5 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_basic_invocation.test_version_flag`
  > AssertionError: assert None
  >  +  where None = <function match at 0x7ff4540b2170>(b'^\\d+\\.\\d+\\.\\d+\\s*$', b'json-tui 0.1.0\n')
  >  +    where <function match at 0x7ff4540b2170> = re.match
  >  +    and   b'json-tui 0.1.0\n' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'json-tui 0.1.0\n', stderr=b'').stdout
- `tests.test_json_tui.test_version_short_flag`
  > AssertionError: assert None
  >  +  where None = <function match at 0x7f860396e170>(b'^\\d+\\.\\d+\\.\\d+\\s*$', b'json-tui 0.1.0\n')
  >  +    where <function match at 0x7f860396e170> = re.match
  >  +    and   b'json-tui 0.1.0\n' = CompletedProcess(args=['./executable', '-v'], returncode=0, stdout=b'json-tui 0.1.0\n', stderr=b'').stdout
- `tests.test_json_tui.test_version_long_flag`
  > assert None is not None
- *(... 2 more in this cluster)*

### `boolean_false` — 5 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_additional_coverage.test_version_output_format`
  > assert False
  >  +  where False = all(<generator object test_version_output_format.<locals>.<genexpr> at 0x7f86016f4660>)
- `tests.test_help_output.TestKeybindingFormatting.test_keybinding_ends_with_newline`
  > AssertionError: assert False
  >  +  where False = <built-in method endswith of str object at 0x7fcb221ac030>('\n')
  >  +    where <built-in method endswith of str object at 0x7fcb221ac030> = ''.endswith
  >  +      where '' = CompletedProcess(args=['./executable', '-k'], returncode=1, stdout='', stderr='Reading from stdin...\n').stdout
- `tests.test_json_tui.test_version_flag`
  > assert False
  >  +  where False = all(<generator object test_version_flag.<locals>.<genexpr> at 0x7f6e300e6e30>)
- *(... 2 more in this cluster)*

### `subprocess_failed` — 4 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_expander_external.test_ext_expander_basic_root_minmax_level0_to1_observable_by_first_expand`
  > subprocess.CalledProcessError: Command '['tmux', 'send-keys', '-t', 'jt_83_1779047020470', '-']' returned non-zero exit status 1.
- `eval.tests.test_expander_external.test_ext_expander_expand_idempotent_after_full_expansion`
  > subprocess.CalledProcessError: Command '['tmux', 'send-keys', '-t', 'jt_83_1779047023411', '+']' returned non-zero exit status 1.
- `eval.tests.test_expander_external.test_ext_expander_collapse_root_to_placeholders_observable_by_minus`
  > subprocess.CalledProcessError: Command '['tmux', 'send-keys', '-t', 'jt_83_1779047027406', '+']' returned non-zero exit status 1.
- *(... 1 more in this cluster)*

### `rc_unexpected_zero` — 2 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_argument_parsing.test_flag_case_sensitivity`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--HELP'], returncode=0, stdout=b'json-tui 0.1.0\nA JSON terminal UI\n\nOPTIONS:\n  -h, --help              Display this help menu\n  -v, 
- `tests.test_help_output.TestDoubleHyphenSeparator.test_double_hyphen_treats_help_as_filename`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '--', '--help'], returncode=0, stdout='json-tui 0.1.0\nA JSON terminal UI\n\nOPTIONS:\n  -h, --help              Display this help menu\n  -v, --ve

### `rc_mismatch_got1_want124` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_json_tui.test_fullscreen_long_flag`
  > AssertionError: assert 1 == 124
  >  +  where 1 = CompletedProcess(args=['./executable', '--fullscreen', '/tmp/tmp9p999m7o/test.json'], returncode=1, stdout=b'', stderr=b'Could not open file --fullscreen\n').returncode

