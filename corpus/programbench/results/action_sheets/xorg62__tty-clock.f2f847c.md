# Action Sheet — xorg62__tty-clock.f2f847c

**Current:** 6.43%  (22/342)
**Pass / Fail / Skip:** 22 / 193 / 1
**Gap to 100%:** 93.57 percentage points (320 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_cli_behavior.test_double_dash_help_is_invalid_option_and_prints_usage_to_stdout`
  - reason: test_double_dash_help_is_invalid_option_and_prints_usage_to_stdout depends on test_help_exact_text

## Failure clusters

193 failed tests grouped into 9 buckets (sorted by count).

### `other_assertion` — 74 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic.test_help_flag_short`
  > AssertionError: assert b'usage : tty-clock' in b'tty-clock 0.1.0\n\nusage: tty-clock [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --verbose  Verbose
  >  +  where b'tty-clock 0.1.0\n\nusage: tty-clock [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --verbose  Verbose\n  -q, --quiet    Quiet\n\n' = Compl
- `tests.test_basic.test_invalid_long_option_shows_help`
  > AssertionError: assert b'invalid option' in b''
  >  +  where b'' = CompletedProcess(args=['./executable', '--help'], returncode=0, stdout=b'tty-clock 0.1.0\n\nusage: tty-clock [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version 
- `tests.test_basic.test_version_flag`
  > AssertionError: assert b'TTY-Clock' in b''
  >  +  where b'' = CompletedProcess(args=['./executable', '-v'], returncode=0, stdout=b'', stderr=b'').stdout
- *(... 71 more in this cluster)*

### `rc_mismatch_got0_want1` — 44 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `eval.tests.test_argparse_validation.test_positional_argument_is_treated_as_terminal_name[args0]`
  > assert 0 == 1
- `eval.tests.test_argparse_validation.test_positional_argument_is_treated_as_terminal_name[args1]`
  > assert 0 == 1
- `eval.tests.test_help_usage.test_help_precedence_with_other_flags_shows_usage`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-h', '-v'], returncode=0, stdout='tty-clock 0.1.0\n\nusage: tty-clock [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --
- *(... 41 more in this cluster)*

### `string_output_mismatch` — 25 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_argparse_validation.test_combined_short_flags_equivalent_for_boolean_flags[args0]`
  > AssertionError: assert '' == 'TTY-Clock 2 © devel version'
  >   
  >   - TTY-Clock 2 © devel version
- `eval.tests.test_argparse_validation.test_combined_short_flags_equivalent_for_boolean_flags[args1]`
  > AssertionError: assert '' == 'TTY-Clock 2 © devel version'
  >   
  >   - TTY-Clock 2 © devel version
- `eval.tests.test_argparse_validation.test_combined_short_flags_equivalent_for_boolean_flags[args2]`
  > AssertionError: assert '' == 'TTY-Clock 2 © devel version'
  >   
  >   - TTY-Clock 2 © devel version
- *(... 22 more in this cluster)*

### `rc_mismatch_got2_want0` — 18 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_basic.test_info_flag`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '-i'], returncode=2, stdout=b'', stderr=b"tty-clock: error: a value is required for '-i <VALUE>'\n").returncode
- `tests.test_basic.test_info_flag_exits_immediately`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '-i'], returncode=2, stdout=b'', stderr=b"tty-clock: error: a value is required for '-i <VALUE>'\n").returncode
- `eval.tests.test_argparse_validation.test_missing_required_value_for_option[args1-d]`
  > assert 2 == 0
- *(... 15 more in this cluster)*

### `rc_mismatch_got0_want124` — 18 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_option_validation.test_color_option_negative_ignored`
  > AssertionError: assert 0 == 124
  >  +  where 0 = CompletedProcess(args=['./executable', '-C', '-1'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_option_validation.test_color_option_too_high_ignored`
  > AssertionError: assert 0 == 124
  >  +  where 0 = CompletedProcess(args=['./executable', '-C', '8'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_option_validation.test_color_option_too_high_9_ignored`
  > AssertionError: assert 0 == 124
  >  +  where 0 = CompletedProcess(args=['./executable', '-C', '9'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 15 more in this cluster)*

### `boolean_false` — 6 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `eval.tests.test_help_usage.test_help_has_expected_indentation`
  > assert False
  >  +  where False = all(<generator object test_help_has_expected_indentation.<locals>.<genexpr> at 0x7fa6ebcd7df0>)
- `eval.tests.test_help_usage.test_long_help_is_invalid_option_message_then_usage`
  > assert False
  >  +  where False = any(<generator object test_long_help_is_invalid_option_message_then_usage.<locals>.<genexpr> at 0x7fa6ebe0a500>)
- `eval.tests.test_help_usage.test_help_option_ordering_first_few_lines`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7fa6ed040030>('-s')
  >  +    where <built-in method startswith of str object at 0x7fa6ed040030> = ''.startswith
  >  +      where '' = <built-in method lstrip of str object at 0x7fa6ed040030>()
  >  +        where <built-in method lstrip of str object at 0x7fa6ed040030> = ''.lstrip
- *(... 3 more in this cluster)*

### `rc_unexpected_zero` — 5 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_tty_errors.test_tty_option_nonexistent_device`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '-T', '/dev/nonexistent_tty_12345'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_tty_errors.test_tty_option_no_permission`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '-T', '/tmp/tmped9ncahn'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_tty_errors.test_tty_option_regular_file`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '-T', '/tmp/tmp05pvbekk'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 2 more in this cluster)*

### `rc_mismatch_got2_want1` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_argparse_validation.test_double_dash_stops_option_parsing_and_treats_following_as_positional`
  > assert 2 == 1
- `eval.tests.test_help_usage.test_double_dash_separator_does_not_trigger_help`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--', '-h'], returncode=2, stdout='', stderr='tty-clock: error: unrecognized argument: --\n').returncode

### `returned_none` — 1 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_usage.test_C_flag_shows_bracketed_range`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7fa6ecfb2680>('\\-C\\s+\\[0\\-7\\]', 'tty-clock 0.1.0\n\nusage: tty-clock [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print versi
  >  +    where <function search at 0x7fa6ecfb2680> = re.search

