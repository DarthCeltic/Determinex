# Action Sheet — trasta298__keifu.3331426

**Current:** 20.72%  (86/415)
**Pass / Fail / Skip:** 86 / 188 / 4
**Gap to 100%:** 79.28 percentage points (329 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_tui.test_help_overlay_opens_and_closes`
  - reason: test_help_overlay_opens_and_closes depends on test_tui_initial_screen_has_panes_and_footer
- `eval.tests.test_tui.test_move_selection_changes_commit_detail`
  - reason: test_move_selection_changes_commit_detail depends on test_tui_initial_screen_has_panes_and_footer
- `eval.tests.test_tui.test_search_mode_can_be_entered_and_cancelled`
  - reason: test_search_mode_can_be_entered_and_cancelled depends on test_tui_initial_screen_has_panes_and_footer
- `eval.tests.test_tui.test_unbound_key_does_not_crash_or_exit`
  - reason: test_unbound_key_does_not_crash_or_exit depends on test_tui_initial_screen_has_panes_and_footer

## Failure clusters

188 failed tests grouped into 10 buckets (sorted by count).

### `other_assertion` — 108 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic.test_help_shows_all_flags`
  > AssertionError: assert '-V, --version' in 'TUI tool to visualize Git commit graphs\nUsage:\nOptions:\n--help\n--version\nTUI tool to visualize Git commit graphs\nUsage:\nOptions:\n-h, --help\nkeifu\n'
- `tests.test_basic.test_help_contains_description`
  > AssertionError: assert b'genealogy' in b'TUI tool to visualize Git commit graphs\nUsage:\nOptions:\n--help\n--version\nTUI tool to visualize Git commit graphs\nUsage:\nOptions:\n-h, --help\nkeifu\n'
  >  +  where b'TUI tool to visualize Git commit graphs\nUsage:\nOptions:\n--help\n--version\nTUI tool to visualize Git commit graphs\nUsage:\nOptions:\n-h, --help\nkeifu\n' = CompletedProcess(args=['/wor
- `tests.test_basic.test_version_contains_only_version`
  > AssertionError: assert 4 <= 1
  >  +  where 4 = <built-in method count of bytes object at 0x7f4f743d89e0>(b'\n')
  >  +    where <built-in method count of bytes object at 0x7f4f743d89e0> = b'keifu\nkeifu\n-h, --help\n-V, --version\n'.count
  >  +      where b'keifu\nkeifu\n-h, --help\n-V, --version\n' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'keifu\nkeifu\n-h, --help\n-V, --version\n', stderr=b''
- *(... 105 more in this cluster)*

### `rc_unexpected_zero` — 37 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_basic.test_invalid_flag`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--invalid-flag-xyz'], returncode=0, stdout=b'-h, --help\n-V, --version\ngenealogy\ncommit\ngraph\n', stderr=b'').returncode
- `tests.test_basic.test_no_arguments_requires_git_repo`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable'], returncode=0, stdout=b'keifu 0.1.0\n----------------------------------------\nInteractive TUI tool driven by tmux/libtmux/pexpect harness
- `tests.test_edge_cases.test_executable_in_current_repo`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable'], returncode=0, stdout=b'keifu 0.1.0\n----------------------------------------\nInteractive TUI tool driven by tmux/libtmux/pexpect harness
- *(... 34 more in this cluster)*

### `string_output_mismatch` — 16 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_cli.test_help_flag`
  > AssertionError: assert 'TUI tool to ...--help\nkeifu' == 'A TUI tool t...Print version'
  >   
  >   - A TUI tool to visualize Git commit graphs with branch genealogy
  >   ? --                                       ----------------------
  >   + TUI tool to visualize Git commit graphs
  >   + Usage:
  >   - 
  >   - Usage: executable...
- `tests.test_cli.test_version_flag`
  > AssertionError: assert 'keifu\nkeifu...-V, --version' == 'keifu 0.2.3'
  >   
  >   - keifu 0.2.3
  >   + keifu
  >   + keifu
  >   + -h, --help
  >   + -V, --version
- `tests.test_repository.test_help_flag_complete_output`
  > AssertionError: assert 'TUI tool to ...help\nkeifu\n' == 'A TUI tool t...int version\n'
  >   
  >   - A TUI tool to visualize Git commit graphs with branch genealogy
  >   ? --                                       ----------------------
  >   + TUI tool to visualize Git commit graphs
  >   + Usage:
  >   - 
  >   - Usage: executable...
- *(... 13 more in this cluster)*

### `returned_none` — 8 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_basic.test_version_flag`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f4f760be680>(b'keifu\\s+\\d+\\.\\d+\\.\\d+', b'keifu\nkeifu\n-h, --help\n-V, --version\n')
  >  +    where <function search at 0x7f4f760be680> = re.search
  >  +    and   b'keifu\nkeifu\n-h, --help\n-V, --version\n' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'keifu\nkeifu\n-h, --help\n-V, --version\n', stderr=b'').
- `tests.test_basic.test_version_short_flag`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f4f760be680>(b'keifu\\s+\\d+\\.\\d+\\.\\d+', b'keifu\n-h, --help\n-V, --version\n')
  >  +    where <function search at 0x7f4f760be680> = re.search
  >  +    and   b'keifu\n-h, --help\n-V, --version\n' = CompletedProcess(args=['/workspace/executable', '-V'], returncode=0, stdout=b'keifu\n-h, --help\n-V, --version\n', stderr=b'').stdout
- `tests.test_basic.test_help_and_version_are_different`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f4f760be680>(b'\\d+\\.\\d+\\.\\d+', b'keifu\nkeifu\n-h, --help\n-V, --version\n')
  >  +    where <function search at 0x7f4f760be680> = re.search
  >  +    and   b'keifu\nkeifu\n-h, --help\n-V, --version\n' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'keifu\nkeifu\n-h, --help\n-V, --version\n', stderr=b'').
- *(... 5 more in this cluster)*

### `boolean_false` — 8 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_cli.TestCLIArguments.test_version_long`
  > assert False
  >  +  where False = any(<generator object TestCLIArguments.test_version_long.<locals>.<genexpr> at 0x7fef2d5c2c00>)
- `tests.test_tui.TestNavigation.test_navigation_down`
  > AssertionError: assert False
  >  +  where False = wait_for('Commit', timeout=3)
  >  +    where wait_for = <test_tui.TmuxTestHarness object at 0x7fef2e087eb0>.wait_for
- `tests.test_tui.TestNavigation.test_navigation_up`
  > AssertionError: assert False
  >  +  where False = wait_for('Commit', timeout=3)
  >  +    where wait_for = <test_tui.TmuxTestHarness object at 0x7fef2e5d7f40>.wait_for
- *(... 5 more in this cluster)*

### `test_timeout` — 5 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_graph_edge_cases.test_extremely_narrow_terminal_branch_truncation`
  > subprocess.TimeoutExpired: Command '['/workspace/tui2cli', '-n', 'test_narrow_branch', 'stop']' timed out after 5 seconds
- `tests.test_graph_edge_cases.test_narrow_terminal_right_side_truncation`
  > subprocess.TimeoutExpired: Command '['/workspace/tui2cli', '-n', 'test_narrow_metadata', 'stop']' timed out after 5 seconds
- `tests.test_graph_edge_cases.test_medium_terminal_author_only`
  > subprocess.TimeoutExpired: Command '['/workspace/tui2cli', '-n', 'test_medium_author', 'stop']' timed out after 5 seconds
- *(... 2 more in this cluster)*

### `rc_mismatch_got0_want1` — 2 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_cli.test_non_git_directory_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable'], returncode=0, stdout='keifu 0.1.0\n----------------------------------------\nInteractive TUI tool driven by tmux/libtmux/pexpect harness\
- `tests.test_repository.test_non_git_directory_clear_error_message`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable'], returncode=0, stdout='keifu 0.1.0\n----------------------------------------\nInteractive TUI tool driven by tmux/libtmux/pexpect harness\

### `rc_mismatch_got0_want2` — 2 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_repository.test_invalid_flag_error_message_and_exit_code`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--invalid-flag'], returncode=0, stdout='', stderr='').returncode
- `tests.test_cli.TestCLIArguments.test_unknown_short_flag`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-x'], returncode=0, stdout='', stderr='').returncode

### `rc_mismatch_got4_want1` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic.test_version_format`
  > AssertionError: assert 4 == 1
  >  +  where 4 = len(['keifu', 'keifu', '-h, --help', '-V, --version'])

### `rc_mismatch_got1_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_edge_cases.test_version_includes_semantic_version`
  > AssertionError: assert 1 == 3
  >  +  where 1 = len(['keifu'])

