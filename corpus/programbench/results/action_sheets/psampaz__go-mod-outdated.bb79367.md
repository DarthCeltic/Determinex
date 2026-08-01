# Action Sheet — psampaz__go-mod-outdated.bb79367

**Current:** 12.28%  (42/342)
**Pass / Fail / Skip:** 42 / 295 / 5
**Gap to 100%:** 87.72 percentage points (300 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_executable_behavior.test_markdown_style_output_exact`
  - reason: test_markdown_style_output_exact depends on test_default_table_output_exact
- `eval.tests.test_executable_behavior.test_unknown_style_falls_back_to_default`
  - reason: test_unknown_style_falls_back_to_default depends on test_default_table_output_exact
- `eval.tests.test_executable_behavior.test_filters_exact_output[args0-default_table_update_only.txt]`
  - reason: test_filters_exact_output[args0-default_table_update_only.txt] depends on test_default_table_output_exact
- `eval.tests.test_executable_behavior.test_filters_exact_output[args1-default_table_direct_only.txt]`
  - reason: test_filters_exact_output[args1-default_table_direct_only.txt] depends on test_default_table_output_exact
- `eval.tests.test_executable_behavior.test_filters_exact_output[args2-default_table_direct_only.txt]`
  - reason: test_filters_exact_output[args2-default_table_direct_only.txt] depends on test_default_table_output_exact

## Failure clusters

295 failed tests grouped into 13 buckets (sorted by count).

### `rc_mismatch_got2_want0` — 140 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_basic_invocation.test_no_input`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b'usage: go-mod-outdated [OPTIONS] [ARGS]\n').returncode
- `tests.test_basic_invocation.test_empty_json_object`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b'usage: go-mod-outdated [OPTIONS] [ARGS]\n').returncode
- `tests.test_basic_invocation.test_main_module_excluded`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b'usage: go-mod-outdated [OPTIONS] [ARGS]\n').returncode
- *(... 137 more in this cluster)*

### `subprocess_failed` — 52 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_core.test_no_flags_shows_all_non_main_modules`
  > subprocess.CalledProcessError: Command '['/workspace/executable']' returned non-zero exit status 2.
- `tests.test_core.test_only_indirect_modules_no_flags`
  > subprocess.CalledProcessError: Command '['/workspace/executable']' returned non-zero exit status 2.
- `tests.test_core.test_all_modules_up_to_date_no_flags`
  > subprocess.CalledProcessError: Command '['/workspace/executable']' returned non-zero exit status 2.
- *(... 49 more in this cluster)*

### `other_assertion` — 48 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_help_flag`
  > AssertionError: assert b'Usage of' in b'go-mod-outdated 0.1.0\n\nusage: go-mod-outdated [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --verbose  Verb
- `tests.test_basic_invocation.test_invalid_flag`
  > AssertionError: assert b'flag provided but not defined' in b'go-mod-outdated: error: unrecognized argument: --invalid-flag\n'
  >  +  where b'go-mod-outdated: error: unrecognized argument: --invalid-flag\n' = CompletedProcess(args=['/workspace/executable', '--invalid-flag'], returncode=2, stdout=b'', stderr=b'go-mod-outdated: er
- `tests.test_complex_scenarios.test_real_world_with_update_filter`
  > AssertionError: assert b'github.com/BurntSushi/toml' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', '-update'], returncode=0, stdout=b'', stderr=b'').stdout
- *(... 45 more in this cluster)*

### `string_output_mismatch` — 19 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_usage.test_help_is_printed_to_stderr_not_stdout`
  > AssertionError: assert 'go-mod-outda...    Quiet\n\n' == ''
  >   
  >   + go-mod-outdated 0.1.0
  >   + 
  >   + usage: go-mod-outdated [OPTIONS] [ARGS]
  >   + 
  >   + Options:
  >   +   -h, --help     Print help...
- `eval.tests.test_help_usage.test_help_output_matches_baseline_exactly_except_invocation_path`
  > AssertionError: assert '' == 'Usage of <pr...ith updates\n'
  >   
  >   - Usage of <prog>:
  >   -   -ci
  >   -     	Non-zero exit code when at least one outdated dependency was found
  >   -   -direct
  >   -     	List only direct modules
  >   -   -style string...
- `tests.test_core.test_update_flag_shows_only_modules_with_updates`
  > AssertionError: assert '' == '+-----------...----------+\n'
  >   
  >   - +-------------------------------------+---------+-------------+--------+------------------+
  >   - |               MODULE                | VERSION | NEW VERSION | DIRECT | VALID TIMESTAMPS |
  >   - +-------------------------------------+---------+-------------+--------+------------------+
  >   - | github.com/example/direct-updated   | v1.0.0  | v1.1.0      | true   | true             |
  >   - | github.com/example/indirect-updated | v0.5.0  | v0.6.0      | false  | true             |
  >   - +-------------------------------------+---------+-------------+--------+------------------+
- *(... 16 more in this cluster)*

### `rc_mismatch_got0_want1` — 16 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_complex_scenarios.test_ci_mode_realistic`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-ci'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_edge_cases.test_all_flags_combined`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-update', '-direct', '-ci', '-style', 'markdown'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_flags.test_ci_flag_with_outdated`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-ci'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 13 more in this cluster)*

### `rc_mismatch_got0_want2` — 6 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `eval.tests.test_argparse_validation.test_boolean_flags_reject_invalid_values[args0-bogus--ci]`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-ci=bogus'], returncode=0, stdout='', stderr='').returncode
- `eval.tests.test_argparse_validation.test_boolean_flags_reject_invalid_values[args2-bogus--direct]`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-direct=bogus'], returncode=0, stdout='', stderr='').returncode
- `eval.tests.test_argparse_validation.test_boolean_flags_reject_invalid_values[args4-bogus--update]`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-update=bogus'], returncode=0, stdout='', stderr='').returncode
- *(... 3 more in this cluster)*

### `returned_none` — 5 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_usage.test_help_has_usage_header`
  > AssertionError: assert None is not None
  >  +  where None = <function search at 0x7f5e2e3b6680>('\\AUsage of .*executable:\\n', '')
  >  +    where <function search at 0x7f5e2e3b6680> = re.search
- `eval.tests.test_help_usage.test_help_documents_flags[\\s+-ci\\n]`
  > AssertionError: assert None is not None
  >  +  where None = <function search at 0x7f5e2e3b6680>('\\s+-ci\\n', '')
  >  +    where <function search at 0x7f5e2e3b6680> = re.search
- `eval.tests.test_help_usage.test_help_documents_flags[\\s+-direct\\n]`
  > AssertionError: assert None is not None
  >  +  where None = <function search at 0x7f5e2e3b6680>('\\s+-direct\\n', '')
  >  +    where <function search at 0x7f5e2e3b6680> = re.search
- *(... 2 more in this cluster)*

### `bytes_output_mismatch` — 4 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `eval.tests.test_io_behavior.test_help_prints_usage_to_stderr_and_exit_0`
  > AssertionError: assert b'go-mod-outd...    Quiet\n\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'go-mod-outdated 0.1.0\n\nusage: go-mod-outdated [OPTIONS] [ARGS]\n\nOptions:'
  >   +  b'\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --verb'
  >   +  b'ose  Verbose\n  -q, --quiet    Quiet\n\n')
- `eval.tests.test_externalized.test_ext_run_outputs_default_table_default_style`
  > AssertionError: assert b'' == b'+----------...----------+\n'
  >   
  >   Full diff:
  >   + b''
  >   - (b'+-------------------------------+------------------------------------+------'
  >   -  b'-------+--------+------------------+\n|            MODULE             |  '
  >   -  b'            VERSION               | NEW VERSION | DIRECT | VALID TIMESTAMPS '
  >   -  b'|\n+-------------------------------+------------------------------------+'...
- `eval.tests.test_externalized.test_ext_run_outputs_default_table_nonexistent_style_falls_back`
  > AssertionError: assert b'' == b'+----------...----------+\n'
  >   
  >   Full diff:
  >   + b''
  >   - (b'+-------------------------------+------------------------------------+------'
  >   -  b'-------+--------+------------------+\n|            MODULE             |  '
  >   -  b'            VERSION               | NEW VERSION | DIRECT | VALID TIMESTAMPS '
  >   -  b'|\n+-------------------------------+------------------------------------+'...
- *(... 1 more in this cluster)*

### `boolean_false` — 1 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `eval.tests.test_help_usage.test_help_ends_with_newline`
  > AssertionError: assert False
  >  +  where False = <built-in method endswith of str object at 0x7f5e2e440030>('\n')
  >  +    where <built-in method endswith of str object at 0x7f5e2e440030> = ''.endswith

### `empty_list_or_string` — 1 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `eval.tests.test_io_behavior.test_markdown_style_has_pipe_separated_header_and_no_plus_borders`
  > IndexError: list index out of range

### `rc_mismatch_got0_want17` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_core.test_large_dataset_with_update_filter`
  > assert 0 == 17
  >  +  where 0 = len([])

### `rc_mismatch_got0_want25` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_core.test_large_dataset_with_direct_filter`
  > assert 0 == 25
  >  +  where 0 = len([])

### `rc_mismatch_got2_want1` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_errors.test_ci_flag_exits_nonzero_when_outdated_found`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--ci'], returncode=2, stdout='', stderr='go-mod-outdated: error: unrecognized argument: --ci\n').returncode

