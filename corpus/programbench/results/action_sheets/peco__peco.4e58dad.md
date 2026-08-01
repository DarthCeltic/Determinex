# Action Sheet — peco__peco.4e58dad

**Current:** 5.22%  (89/1705)
**Pass / Fail / Skip:** 89 / 991 / 0
**Gap to 100%:** 94.78 percentage points (1616 tests)

## Failure clusters

991 failed tests grouped into 12 buckets (sorted by count).

### `rc_mismatch_got2_want0` — 460 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_basic.test_select_1_with_single_line`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--select-1'], returncode=2, stdout=b'', stderr=b"peco: unknown option: --select-1\nusage: peco [OPTIONS] [ARGS]\nTry 'peco --help' for more inform
- `tests.test_basic.test_read_from_stdin_single_line`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--select-1'], returncode=2, stdout=b'', stderr=b"peco: unknown option: --select-1\nusage: peco [OPTIONS] [ARGS]\nTry 'peco --help' for more inform
- `tests.test_basic.test_read_from_file_with_select_1`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--select-1', '/tmp/tmp4n0fn9aw/input.txt'], returncode=2, stdout=b'', stderr=b"peco: unknown option: --select-1\nusage: peco [OPTIONS] [ARGS]\nTry
- *(... 457 more in this cluster)*

### `other_assertion` — 320 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic.test_help_flag`
  > AssertionError: assert b'--query' in b'peco 0.1.0 - bootstrap scaffold\n\nUsage: peco [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n'
  >  +  where b'peco 0.1.0 - bootstrap scaffold\n\nUsage: peco [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['./executable', '--help
- `tests.test_basic.test_version_flag`
  > AssertionError: assert b'peco version' in b'peco 0.1.0\n'
  >  +  where b'peco 0.1.0\n' = CompletedProcess(args=['./executable', '--version'], returncode=0, stdout=b'peco 0.1.0\n', stderr=b'').stdout
- `tests.test_basic.test_invalid_layout`
  > assert (b'unknown layout' in b"peco: unknown option: --layout\nusage: peco [OPTIONS] [ARGS]\nTry 'peco --help' for more information.\n" or b'invalid' in b"peco: unknown option: --layout\nusage: peco [
  >  +  where b"peco: unknown option: --layout\nusage: peco [OPTIONS] [ARGS]\nTry 'peco --help' for more information.\n" = CompletedProcess(args=['./executable', '--layout', 'invalid-layout'], returncode=
  >  +  and   b"peco: unknown option: --layout\nusage: peco [options] [args]\ntry 'peco --help' for more information.\n" = <built-in method lower of bytes object at 0x7f21152a6940>()
  >  +    where <built-in method lower of bytes object at 0x7f21152a6940> = b"peco: unknown option: --layout\nusage: peco [OPTIONS] [ARGS]\nTry 'peco --help' for more information.\n".lower
  >  +      where b"peco: unknown option: --layout\nusage: peco [OPTIONS] [ARGS]\nTry 'peco --help' for more information.\n" = CompletedProcess(args=['./executable', '--layout', 'invalid-layout'], returnc
- *(... 317 more in this cluster)*

### `string_output_mismatch` — 117 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_buffer_gap.test_empty_buffer_display`
  > AssertionError: assert '\n\n\n\n\n\n...9:43:29 2026)' == 'QUERY>      ...ase [0 (1/1)]'
  >   
  >   - QUERY>                                                      IgnoreCase [0 (1/1)]
  >   + 
  >   + 
  >   + 
  >   + 
  >   + ...
- `tests.test_buffer_gap.test_single_line_buffer`
  > AssertionError: assert '\n\n\n\n\n\n...9:43:36 2026)' == 'QUERY>      ...\nsingle-line'
  >   
  >   - QUERY>                                                      IgnoreCase [1 (1/1)]
  >   - single-line
  >   + 
  >   + 
  >   + 
  >   + ...
- `tests.test_buffer_gap.test_single_line_pagedown_noop`
  > AssertionError: assert '\n\n\n\n\n\n...9:43:43 2026)' == 'QUERY>      ...\nsingle-line'
  >   
  >   - QUERY>                                                      IgnoreCase [1 (1/1)]
  >   - single-line
  >   + 
  >   + 
  >   + 
  >   + ...
- *(... 114 more in this cluster)*

### `rc_mismatch_got2_want1` — 58 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic.test_select_1_with_multiple_lines_fails_without_tty`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['./executable', '--select-1'], returncode=2, stdout=b'', stderr=b"peco: unknown option: --select-1\nusage: peco [OPTIONS] [ARGS]\nTry 'peco --help' for more inform
- `tests.test_basic.test_select_all_requires_tty`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['./executable', '--select-all'], returncode=2, stdout=b'', stderr=b"peco: unknown option: --select-all\nusage: peco [OPTIONS] [ARGS]\nTry 'peco --help' for more in
- `tests.test_basic.test_query_no_match_single_line`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['./executable', '--select-1', '--query', 'nomatch'], returncode=2, stdout=b'', stderr=b"peco: unknown option: --select-1\nusage: peco [OPTIONS] [ARGS]\nTry 'peco -
- *(... 55 more in this cluster)*

### `subprocess_failed` — 22 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_filtering_basic.test_initial_state_shows_all_lines`
  > subprocess.CalledProcessError: Command '['tmux', 'capture-pane', '-t', 'test_initial', '-p']' returned non-zero exit status 1.
- `tests.test_filtering_basic.test_single_term_case_insensitive_lowercase`
  > subprocess.CalledProcessError: Command '['tmux', 'send-keys', '-t', 'test_filter_app', '-l', '--', 'app']' returned non-zero exit status 1.
- `tests.test_filtering_basic.test_single_term_case_insensitive_uppercase`
  > subprocess.CalledProcessError: Command '['tmux', 'send-keys', '-t', 'test_filter_APP', '-l', '--', 'APP']' returned non-zero exit status 1.
- *(... 19 more in this cluster)*

### `uncategorized` — 4 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_coverage.test_signal_handling`
  > AttributeError: '_io.BufferedReader' object has no attribute 'lower'
- `tests.test_coverage.test_stdin_closed_early`
  > ValueError: flush of closed file
- `tests.test_errors.test_null_bytes_in_query`
  > ValueError: embedded null byte
- *(... 1 more in this cluster)*

### `returned_none` — 3 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_output.test_help_includes_short_flag_for_help`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f43fcd52680>('\\s-h,\\s+--help\\s+show this help message', 'peco 0.1.0 - bootstrap scaffold\n\nUsage: peco [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print 
  >  +    where <function search at 0x7f43fcd52680> = re.search
- `eval.tests.test_help_output.test_help_includes_short_flag_for_buffer_size`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f43fcd52680>('\\s-b,\\s+--buffer-size\\s+number of lines', 'peco 0.1.0 - bootstrap scaffold\n\nUsage: peco [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print 
  >  +    where <function search at 0x7f43fcd52680> = re.search
- `eval.tests.test_peco_behavior.test_version_format`
  > AssertionError: assert None
  >  +  where None = <function fullmatch at 0x7fdaa3f4fe20>('peco version v\\d+\\.\\d+\\.\\d+ \\(built with go\\d+\\.\\d+\\.\\d+\\)', 'peco 0.1.0')
  >  +    where <function fullmatch at 0x7fdaa3f4fe20> = re.fullmatch

### `rc_unexpected_zero` — 2 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_coverage.test_file_does_not_exist`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '/nonexistent/file.txt'], returncode=0, stdout=b'', stderr=b'').returncode
- `eval.tests.test_peco_behavior.test_layout_invalid_value_errors`
  > AssertionError: assert 0 != 0
  >  +  where 0 = TmuxRunResult(exit_code=0, stdout='', stderr='', screen='( TERM=xterm-256color /workspace/executable --layout definitely-not-valid < /workspace/eval/_tmp_input.bin > /workspace/\neval/_t

### `empty_list_or_string` — 2 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_final_gaps.test_query_with_spaces_and_filtering`
  > IndexError: list index out of range
- `tests.test_final_gaps.test_beginning_and_end_of_line`
  > IndexError: list index out of range

### `bytes_output_mismatch` — 1 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_basic.test_newline_at_end_preserved`
  > AssertionError: assert (b'' == b'test\n'
  >   
  >   Full diff:
  >   - (b'test\n')
  >   + b'' or b'' == b'test'
  >   
  >   Full diff:
  >   - b'test'

### `rc_mismatch_got0_want1` — 1 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `eval.tests.test_args_parsing_validation.test_too_many_positionals_is_ignored_but_first_used_for_file_open_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'file1', 'file2'], returncode=0, stdout='', stderr='').returncode

### `boolean_false` — 1 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `eval.tests.test_peco_behavior.test_help_includes_usage_and_options`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7fdaa3322130>('\nUsage: peco [options] [FILE]\n\nOptions:\n')
  >  +    where <built-in method startswith of str object at 0x7fdaa3322130> = 'peco 0.1.0 - bootstrap scaffold\n\nUsage: peco [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  P

