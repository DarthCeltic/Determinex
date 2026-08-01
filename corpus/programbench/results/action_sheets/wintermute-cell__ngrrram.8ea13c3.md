# Action Sheet — wintermute-cell__ngrrram.8ea13c3

**Current:** 7.54%  (30/398)
**Pass / Fail / Skip:** 30 / 247 / 0
**Gap to 100%:** 92.46 percentage points (368 tests)

## Failure clusters

247 failed tests grouped into 10 buckets (sorted by count).

### `other_assertion` — 152 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_help_flag`
  > AssertionError: assert b'Usage: executable [OPTIONS]' in b'ngrrram 0.1.0\n\nusage: ngrrram [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --verbose  V
  >  +  where b'ngrrram 0.1.0\n\nusage: ngrrram [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --verbose  Verbose\n  -q, --quiet    Quiet\n\n' = Completed
- `tests.test_basic_invocation.test_help_short_flag`
  > AssertionError: assert b'Usage: executable [OPTIONS]' in b'ngrrram 0.1.0\n\nusage: ngrrram [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --verbose  V
  >  +  where b'ngrrram 0.1.0\n\nusage: ngrrram [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --verbose  Verbose\n  -q, --quiet    Quiet\n\n' = Completed
- `tests.test_basic_invocation.test_invalid_flag`
  > AssertionError: assert b'--help' in b'ngrrram: error: unrecognized argument: --invalid-flag\n'
  >  +  where b'ngrrram: error: unrecognized argument: --invalid-flag\n' = CompletedProcess(args=['./executable', '--invalid-flag'], returncode=2, stdout=b'', stderr=b'ngrrram: error: unrecognized argumen
- *(... 149 more in this cluster)*

### `rc_mismatch_got2_want0` — 37 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_display_options.test_show_ortho_flag`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--show-ortho', '--help'], returncode=2, stdout=b'', stderr=b'ngrrram: error: unrecognized argument: --show-ortho\n').returncode
- `tests.test_display_options.test_nokb_flag`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--nokb', '--help'], returncode=2, stdout=b'', stderr=b'ngrrram: error: unrecognized argument: --nokb\n').returncode
- `tests.test_display_options.test_cat_flag`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--cat', '--help'], returncode=2, stdout=b'', stderr=b'ngrrram: error: unrecognized argument: --cat\n').returncode
- *(... 34 more in this cluster)*

### `string_output_mismatch` — 20 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_usage.test_full_help_matches_fixture_exactly`
  > AssertionError: assert 'ngrrram 0.1....    Quiet\n\n' == 'Usage: execu... Print help\n'
  >   
  >   - Usage: executable [OPTIONS]
  >   + ngrrram 0.1.0
  >   + 
  >   + usage: ngrrram [OPTIONS] [ARGS]
  >     
  >     Options:...
- `tests.test_cli.test_help_long_flag`
  > AssertionError: assert 'ngrrram 0.1....    Quiet\n\n' == 'Usage: execu... Print help\n'
  >   
  >   - Usage: executable [OPTIONS]
  >   + ngrrram 0.1.0
  >   + 
  >   + usage: ngrrram [OPTIONS] [ARGS]
  >     
  >     Options:...
- `tests.test_cli.test_help_short_flag`
  > AssertionError: assert 'ngrrram 0.1....    Quiet\n\n' == 'Usage: execu... Print help\n'
  >   
  >   - Usage: executable [OPTIONS]
  >   + ngrrram 0.1.0
  >   + 
  >   + usage: ngrrram [OPTIONS] [ARGS]
  >     
  >     Options:...
- *(... 17 more in this cluster)*

### `rc_mismatch_got0_want1` — 12 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_ngram_selection.test_n_flag_invalid_value`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', '-n', '5'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_ngram_selection.test_n_flag_file_nonexistent`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', '-n', '/nonexistent/file.txt'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_numeric_arguments.test_top_flag_zero`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', '-t', '0'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 9 more in this cluster)*

### `rc_mismatch_got2_want1` — 9 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_cli_layouts.test_emu_requires_both_in_and_out[unknown]`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--emu-in', 'unknown'], returncode=2, stdout=b'', stderr=b'ngrrram: error: unrecognized argument: --emu-in\n').returncode
- `eval.tests.test_cli_layouts.test_emu_requires_both_in_and_out[QWERTY]`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--emu-in', 'QWERTY'], returncode=2, stdout=b'', stderr=b'ngrrram: error: unrecognized argument: --emu-in\n').returncode
- `eval.tests.test_cli_layouts.test_emu_requires_both_in_and_out[colemak-dh]`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--emu-in', 'colemak-dh'], returncode=2, stdout=b'', stderr=b'ngrrram: error: unrecognized argument: --emu-in\n').returncode
- *(... 6 more in this cluster)*

### `rc_mismatch_got1_want0` — 7 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `eval.tests.test_argparse_validation.test_valid_invocations_start_tui[args0]`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['tmux', 'capture-pane', '-t', 'pytest_89_9356982', '-p'], returncode=1, stdout='', stderr='no server running on /tmp/tmux-0/default\n').returncode
- `eval.tests.test_argparse_validation.test_valid_invocations_start_tui[args1]`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['tmux', 'capture-pane', '-t', 'pytest_89_8605467', '-p'], returncode=1, stdout='', stderr='no server running on /tmp/tmux-0/default\n').returncode
- `eval.tests.test_argparse_validation.test_valid_invocations_start_tui[args2]`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['tmux', 'capture-pane', '-t', 'pytest_89_9367802', '-p'], returncode=1, stdout='', stderr='no server running on /tmp/tmux-0/default\n').returncode
- *(... 4 more in this cluster)*

### `rc_unexpected_zero` — 4 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_numeric_arguments.test_top_flag_negative`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '-t', '-5'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_numeric_arguments.test_top_flag_non_numeric`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '-t', 'abc'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_numeric_arguments.test_acc_flag_negative`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '-a', '-1'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 1 more in this cluster)*

### `boolean_false` — 3 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `eval.tests.test_help_usage.test_help_starts_with_usage_line`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7f3bd286e6b0>('Usage: executable [OPTIONS]\n')
  >  +    where <built-in method startswith of str object at 0x7f3bd286e6b0> = 'ngrrram 0.1.0\n\nusage: ngrrram [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n 
- `eval.tests.test_help_usage.test_help_takes_precedence_over_other_valid_flags`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7f3bd286e4f0>('Usage: executable')
  >  +    where <built-in method startswith of str object at 0x7f3bd286e4f0> = 'ngrrram 0.1.0\n\nusage: ngrrram [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n 
  >  +      where 'ngrrram 0.1.0\n\nusage: ngrrram [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --verbose  Verbose\n  -q, --quiet    Quiet\n\n' = Comple
- `eval.tests.test_help_usage.test_help_takes_precedence_over_invalid_flags`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7f3bd32ea790>('Usage: executable')
  >  +    where <built-in method startswith of str object at 0x7f3bd32ea790> = 'ngrrram 0.1.0\n\nusage: ngrrram [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n 
  >  +      where 'ngrrram 0.1.0\n\nusage: ngrrram [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --verbose  Verbose\n  -q, --quiet    Quiet\n\n' = Comple

### `rc_mismatch_got0_want2` — 2 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `eval.tests.test_cli_help_and_errors.test_unknown_flag_errors[--version]`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'ngrrram 0.1.0\n', stderr=b'').returncode
- `eval.tests.test_cli_help_and_errors.test_unknown_flag_errors[-Z]`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-Z'], returncode=0, stdout=b'', stderr=b'').returncode

### `bytes_output_mismatch` — 1 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `eval.tests.test_cli_help_and_errors.test_help_exact`
  > assert b'ngrrram 0.1...    Quiet\n\n' == b"Usage: exec... Print help\n"
  >   
  >   At index 0 diff: b'n' != b'U'
  >   
  >   Full diff:
  >   + (b'ngrrram 0.1.0\n\nusage: ngrrram [OPTIONS] [ARGS]\n\nOptions:\n  -h, --hel'
  >   +  b'p     Print help\n  -V, --version  Print version\n  -v, --verbose  Verbose'
  >   +  b'\n  -q, --quiet    Quiet\n\n')...

