# Action Sheet — kaushiksrini__parqeye.8072121

**Current:** 14.49%  (101/697)
**Pass / Fail / Skip:** 101 / 279 / 1
**Gap to 100%:** 85.51 percentage points (596 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_error_handling.test_path_component_too_long`
  - reason: OS doesn't support 300-char filenames

## Failure clusters

279 failed tests grouped into 6 buckets (sorted by count).

### `rc_unexpected_zero` — 98 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_bad_parquet_files.test_arrow_gh_41317`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'parquet-testing/bad_data/ARROW-GH-41317.parquet'], returncode=0, stdout=b'parqeye 0.1.0\n----------------------------------------\nInteractive TUI
- `tests.test_bad_parquet_files.test_arrow_gh_41321`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'parquet-testing/bad_data/ARROW-GH-41321.parquet'], returncode=0, stdout=b'parqeye 0.1.0\n----------------------------------------\nInteractive TUI
- `tests.test_bad_parquet_files.test_arrow_gh_43605`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'parquet-testing/bad_data/ARROW-GH-43605.parquet'], returncode=0, stdout=b'parqeye 0.1.0\n----------------------------------------\nInteractive TUI
- *(... 95 more in this cluster)*

### `string_output_mismatch` — 96 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_usage.test_h_and_help_outputs_match_exactly`
  > AssertionError: assert 'parqeye\nUsa...qeye\n0.0.2\n' == 'Command line...ye\nparqeye\n'
  >   
  >   - Command line tool to visualize parquet files
  >   + parqeye
  >     Usage:
  >   - <PATH>
  >     parqeye
  >   - parqeye
- `eval.tests.test_help_usage.test_help_baseline_snapshot_exact_match`
  > AssertionError: assert 'parqeye\nUsa...qeye\n0.0.2\n' == 'Command line...int version\n'
  >   
  >   + parqeye
  >   + Usage:
  >   + parqeye
  >   + 0.0.2
  >   - Command line tool to visualize parquet files
  >   - ...
- `eval.tests.test_cli_behavior.test_help_exact_output_matches_snapshot`
  > AssertionError: assert 'parqeye\nUsa...qeye\n0.0.2\n' == 'Command line...int version\n'
  >   
  >   + parqeye
  >   + Usage:
  >   + parqeye
  >   + 0.0.2
  >   - Command line tool to visualize parquet files
  >   - ...
- *(... 93 more in this cluster)*

### `other_assertion` — 64 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_help_flag`
  > AssertionError: assert b'Command line tool to visualize parquet files' in b'parqeye\nUsage:\nparqeye\n0.0.2\n'
  >  +  where b'parqeye\nUsage:\nparqeye\n0.0.2\n' = CompletedProcess(args=['./executable', '--help'], returncode=0, stdout=b'parqeye\nUsage:\nparqeye\n0.0.2\n', stderr=b'').stdout
- `tests.test_basic_invocation.test_invalid_flag`
  > AssertionError: assert (b'unexpected argument' in b'' or b'unrecognized' in b'')
  >  +  where b'' = CompletedProcess(args=['./executable', '--invalid-flag'], returncode=2, stdout=b'', stderr=b'').stderr
  >  +  and   b'' = <built-in method lower of bytes object at 0x7f48d1d10030>()
  >  +    where <built-in method lower of bytes object at 0x7f48d1d10030> = b''.lower
  >  +      where b'' = CompletedProcess(args=['./executable', '--invalid-flag'], returncode=2, stdout=b'', stderr=b'').stderr
- `tests.test_basic_invocation.test_multiple_paths`
  > AssertionError: assert (b'unexpected argument' in b'' or b'trailing arguments' in b'')
  >  +  where b'' = CompletedProcess(args=['./executable', 'file1.parquet', 'file2.parquet'], returncode=2, stdout=b'', stderr=b'').stderr
  >  +  and   b'' = <built-in method lower of bytes object at 0x7f48d1d10030>()
  >  +    where <built-in method lower of bytes object at 0x7f48d1d10030> = b''.lower
  >  +      where b'' = CompletedProcess(args=['./executable', 'file1.parquet', 'file2.parquet'], returncode=2, stdout=b'', stderr=b'').stderr
- *(... 61 more in this cluster)*

### `rc_mismatch_got0_want2` — 12 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_basic_invocation.test_no_arguments`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['./executable'], returncode=0, stdout=b'parqeye 0.1.0\n----------------------------------------\nInteractive TUI tool driven by tmux/libtmux/pexpect harness\n\nJou
- `eval.tests.test_args.test_no_args_errors_missing_required_path`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable'], returncode=0, stdout='parqeye 0.1.0\n----------------------------------------\nInteractive TUI tool driven by tmux/libtmux/pexpect harnes
- `eval.tests.test_args.test_too_many_positionals_errors_on_unexpected_argument`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'a', 'b'], returncode=0, stdout='', stderr='').returncode
- *(... 9 more in this cluster)*

### `boolean_false` — 5 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_additional_coverage.test_very_wide_terminal`
  > assert False
  >  +  where False = any(<generator object test_very_wide_terminal.<locals>.<genexpr> at 0x7f8d67ca6650>)
- `eval.tests.test_args.test_version_flag_exits_success_and_ignores_missing_path[-V]`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7fe60450a770>('parqeye ')
  >  +    where <built-in method startswith of str object at 0x7fe60450a770> = 'parqeye'.startswith
  >  +      where 'parqeye' = <built-in method strip of str object at 0x7fe60450b630>()
  >  +        where <built-in method strip of str object at 0x7fe60450b630> = ('parqeye\n').strip
  >  +          where 'parqeye\n' = CompletedProcess(args=['/workspace/executable', '-V'], returncode=0, stdout='parqeye\n', stderr='').stdout
- `eval.tests.test_args.test_version_flag_exits_success_and_ignores_missing_path[--version]`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7fe6046214f0>('parqeye ')
  >  +    where <built-in method startswith of str object at 0x7fe6046214f0> = 'parqeye\n0.0.2'.startswith
  >  +      where 'parqeye\n0.0.2' = <built-in method strip of str object at 0x7fe6046a8a70>()
  >  +        where <built-in method strip of str object at 0x7fe6046a8a70> = ('parqeye\n0.0.2\n').strip
  >  +          where 'parqeye\n0.0.2\n' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout='parqeye\n0.0.2\n', stderr='').stdout
- *(... 2 more in this cluster)*

### `returned_none` — 4 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_basic_invocation.test_version_short_flag`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f48d1c8a680>(b'\\d+\\.\\d+\\.\\d+', b'parqeye\n')
  >  +    where <function search at 0x7f48d1c8a680> = re.search
  >  +    and   b'parqeye\n' = CompletedProcess(args=['./executable', '-V'], returncode=0, stdout=b'parqeye\n', stderr=b'').stdout
- `tests.test_basic.test_version_short`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f8d69aca680>(b'\\d+\\.\\d+\\.\\d+', b'parqeye\n')
  >  +    where <function search at 0x7f8d69aca680> = re.search
  >  +    and   b'parqeye\n' = CompletedProcess(args=['./executable', '-V'], returncode=0, stdout=b'parqeye\n', stderr=b'').stdout
- `eval.tests.test_help_usage.test_help_includes_help_flag_description`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7fd0e808a680>('-h, --help\\s+Print help', 'parqeye\nUsage:\nparqeye\n0.0.2\n')
  >  +    where <function search at 0x7fd0e808a680> = re.search
- *(... 1 more in this cluster)*

