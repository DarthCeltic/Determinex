# Action Sheet — rs__jplot.2a54bcc

**Current:** 30.13%  (292/969)
**Pass / Fail / Skip:** 292 / 410 / 0
**Gap to 100%:** 69.87 percentage points (677 tests)

## Failure clusters

410 failed tests grouped into 10 buckets (sorted by count).

### `other_assertion` — 240 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_help_flag_long`
  > AssertionError: assert b'Usage: jplot [OPTIONS] FIELD_SPEC' in b''
  >  +  where b'' = CompletedProcess(args=['./executable', '--help'], returncode=0, stdout=b'Usage: jplot\n', stderr=b'').stderr
- `tests.test_basic_invocation.test_help_flag_short`
  > AssertionError: assert b'Usage: jplot [OPTIONS] FIELD_SPEC' in b''
  >  +  where b'' = CompletedProcess(args=['./executable', '-h'], returncode=0, stdout=b'iTerm2, Kitty, or DRCS Sixel graphics required\n', stderr=b'').stderr
- `tests.test_basic_invocation.test_help_describes_counter_option`
  > AssertionError: assert b'counter: Computes the difference with the last value' in b''
  >  +  where b'' = CompletedProcess(args=['./executable', '--help'], returncode=0, stdout=b'Usage: jplot\n', stderr=b'').stderr
- *(... 237 more in this cluster)*

### `rc_mismatch_got0_want1` — 89 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_basic_invocation.test_no_args_shows_graphics_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable'], returncode=0, stdout=b'jplot 0.1.0\n----------------------------------------\nInteractive TUI tool driven by tmux/libtmux/pexpect harness\n\nJourn
- `tests.test_comprehensive_edge_cases.test_deeply_nested_20_levels`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', 'level1.level2.level3.level4.level5.level6.level7.level8.level9.level10.level11.level12.level13.level14.level15.level16.level17.level18.level19.lev
- `tests.test_error_handling.test_missing_field_args`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable'], returncode=0, stdout=b'jplot 0.1.0\n----------------------------------------\nInteractive TUI tool driven by tmux/libtmux/pexpect harness\n\nJourn
- *(... 86 more in this cluster)*

### `string_output_mismatch` — 26 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_dashboard.test_single_field_spec_basic`
  > AssertionError: assert '' == 'jplot:  Cann... for device\n'
  >   
  >   - jplot:  Cannot get window size:  inappropriate ioctl for device
- `tests.test_dashboard.test_plus_separator_combines_fields_in_single_graph`
  > AssertionError: assert 'invalid field option\n' == 'jplot:  Cann... for device\n'
  >   
  >   - jplot:  Cannot get window size:  inappropriate ioctl for device
  >   + invalid field option
- `tests.test_dashboard.test_url_flag_with_multi_graph_dashboard`
  > AssertionError: assert 'error\nerror\nerror\n' == 'jplot:  Data...ng of value\n'
  >   
  >   - jplot:  Data source error:  input error: invalid character '<' looking for beginning of value
  >   + error
  >   + error
  >   + error
- *(... 23 more in this cluster)*

### `rc_unexpected_zero` — 23 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_basic_invocation.test_invalid_flag`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '--invalid-flag'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_flag_parsing.test_invalid_interval_format`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '--interval', 'invalid', 'field'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_flag_parsing.test_invalid_steps_format`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '--steps', 'notanumber', 'field'], returncode=0, stdout=b'graphics required\n', stderr=b'').returncode
- *(... 20 more in this cluster)*

### `test_timeout` — 9 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_http_source.test_nested_field_access`
  > Failed: DID NOT RAISE <class 'subprocess.TimeoutExpired'>
- `tests.test_http_source.test_deeply_nested_field`
  > Failed: DID NOT RAISE <class 'subprocess.TimeoutExpired'>
- `tests.test_http_source.test_counter_field_option`
  > Failed: DID NOT RAISE <class 'subprocess.TimeoutExpired'>
- *(... 6 more in this cluster)*

### `rc_mismatch_got2_want1` — 8 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_dashboard.test_steps_flag_applies_to_all_graphs`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-steps', '100', 'field1', 'field2'], returncode=2, stdout='Usage: jplot\nFIELD_SPEC\n', stderr='').returncode
- `tests.test_dashboard.test_rows_flag_affects_per_graph_height_calculation`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-rows', '50', 'field1', 'field2'], returncode=2, stdout='Usage: jplot\nFIELD_SPEC\n', stderr='').returncode
- `tests.test_terminal_common.test_rows_flag_without_graphics`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-rows', '10', 'value'], returncode=2, stdout='Usage: jplot\nFIELD_SPEC\n', stderr='').returncode
- *(... 5 more in this cluster)*

### `uncategorized` — 6 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_gap_fill_term.test_ticker_iteration_counter_increments`
  > Failed: PTY error during ticker test: [Errno 5] Input/output error
- `tests.test_graph_edge_cases.test_graph_with_marker_field`
  > OSError: [Errno 98] Address already in use
- `tests.test_graphics_protocols.test_kitty_protocol_basic_image_transmission`
  > OSError: [Errno 98] Address already in use
- *(... 3 more in this cluster)*

### `bytes_output_mismatch` — 5 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `eval.tests.test_help_baseline_exact.test_help_matches_baseline_fixture_exact_bytes_combined_streams`
  > AssertionError: assert b'Usage: jplot\n' == b'\x1b[cUsage...sub-field).\n'
  >   
  >   At index 0 diff: b'U' != b'\x1b'
  >   
  >   Full diff:
  >   + (b'Usage: jplot\n')
  >   - (b'\x1b[cUsage: jplot [OPTIONS] FIELD_SPEC [FIELD_SPEC...]:\n\nOPTIONS:\n  -i'
  >   -  b'nterval duration\n    \tWhen url is provided, defines the interval between'...
- `eval.tests.test_help_output.test_dash_h_matches_double_dash_help_exact_bytes_combined_streams`
  > AssertionError: assert b'Usage: jplot\n' == b'iTerm2, Kit...cs required\n'
  >   
  >   At index 0 diff: b'U' != b'i'
  >   
  >   Full diff:
  >   - (b'iTerm2, Kitty, or DRCS Sixel graphics required\n')
  >   + (b'Usage: jplot\n')
- `eval.tests.test_jplot_io.test_help_goes_to_stderr_and_exit0`
  > AssertionError: assert b'iTerm2, Kit...cs required\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'iTerm2, Kitty, or DRCS Sixel graphics required\n')
- *(... 2 more in this cluster)*

### `boolean_false` — 2 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `eval.tests.test_jplot_io.test_missing_graphics_support_error_on_stdout_exit1`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of bytes object at 0x7fdbfcbbc030>(b'jplot:  ')
  >  +    where <built-in method startswith of bytes object at 0x7fdbfcbbc030> = b''.startswith
- `eval.tests.test_jplot_io.test_term_screen_does_not_change_failure_mode_under_non_graphics_terminal`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of bytes object at 0x7fdbfcbbc030>(b'jplot:  ')
  >  +    where <built-in method startswith of bytes object at 0x7fdbfcbbc030> = b''.startswith

### `rc_mismatch_got0_want2` — 2 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_cli.TestInvalidFlags.test_invalid_flag`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--invalid-flag'], returncode=0, stdout='', stderr='').returncode
- `tests.test_flags.TestIntervalFlag.test_interval_invalid_duration`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--interval', 'invalid', 'field'], returncode=0, stdout='', stderr='').returncode

