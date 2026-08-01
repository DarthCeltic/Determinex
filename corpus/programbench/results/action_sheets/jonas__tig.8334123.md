# Action Sheet — jonas__tig.8334123

**Current:** 18.61%  (440/2364)
**Pass / Fail / Skip:** 440 / 1179 / 8
**Gap to 100%:** 81.39 percentage points (1924 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_tmux_fixed.test_tmux_open_commit_disabled`
  - reason: Flaky test
- `tests.test_tmux_fixed.test_tmux_help_view_disabled`
  - reason: Flaky test
- `tests.test_subcommands.test_subcommand_help_routes_to_main_help[NOTSET]`
  - reason: got empty parameter set for (subcmd)
- `tests.test_subcommands.test_version_flag_routing_before_and_after_subcommand[NOTSET]`
  - reason: got empty parameter set for (subcmd)
- `eval.tests.test_tig_tui.test_navigation_down_selects_other_commit`
  - reason: test_navigation_down_selects_other_commit depends on initial
- *(... 3 more skipped)*

## Failure clusters

1179 failed tests grouped into 12 buckets (sorted by count).

### `other_assertion` — 628 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_advanced_features.test_git_diff_options_pass_through`
  > AssertionError: assert b'usage' in b''
  >  +  where b'' = <built-in method lower of bytes object at 0x7f5b597a0030>()
  >  +    where <built-in method lower of bytes object at 0x7f5b597a0030> = b''.lower
  >  +      where b'' = CompletedProcess(args=['/workspace/executable', 'show', '--color', '--help'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_argument_parsing.test_subcommand_with_multiple_flags`
  > AssertionError: assert b'tig' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', 'log', '--all', '--graph', '--version'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_argument_parsing.test_show_with_multiple_flags`
  > AssertionError: assert b'tig' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', 'show', '--stat', '--patch', '--version'], returncode=0, stdout=b'', stderr=b'').stdout
- *(... 625 more in this cluster)*

### `rc_mismatch_got2_want0` — 451 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_advanced_features.test_combination_of_multiple_flags`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-C', '/tmp/pytest-of-root/pytest-0/test_combination_of_multiple_f2/test_repo', '--all', '--reverse', '--help'], returncode=2, stdout=b'',
- `tests.test_advanced_features.test_git_log_options_pass_through`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--oneline', '--help'], returncode=2, stdout=b'', stderr=b"tig: unknown option: --oneline\nusage: tig [OPTIONS] [ARGS]\nTry 'tig --help' f
- `tests.test_advanced_features.test_date_formats`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--date=relative', '--help'], returncode=2, stdout=b'', stderr=b"tig: unknown option: --date=relative\nusage: tig [OPTIONS] [ARGS]\nTry 't
- *(... 448 more in this cluster)*

### `string_output_mismatch` — 38 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_blame_view.test_blame_initial_screen`
  > AssertionError: assert '\n\n\n\n\n\n...42:26 2026)\n' == '8fe4d07 Auth...9      100%\n'
  >   
  >   - 8fe4d07 Author One   2026-01-01 10:00 +0000   1│ #include <stdio.h>
  >   - faf4a5c Author Two   2026-01-02 10:00 +0000   2│ #include <stdlib.h>
  >   - faf4a5c Author Two   2026-01-02 10:00 +0000   3│
  >   - faf4a5c Author Two   2026-01-02 10:00 +0000   4│ int add(int a, int b) {
  >   - faf4a5c Author Two   2026-01-02 10:00 +0000   5│     return a + b;
  >   - faf4a5c Author Two   2026-01-02 10:00 +0000   6│ }...
- `tests.test_blame_view.test_blame_navigation`
  > AssertionError: assert '\n\n\n\n\n\n...42:38 2026)\n' == '8fe4d07 Auth...9      100%\n'
  >   
  >   - 8fe4d07 Author One   2026-01-01 10:00 +0000   1│ #include <stdio.h>
  >   - faf4a5c Author Two   2026-01-02 10:00 +0000   2│ #include <stdlib.h>
  >   - faf4a5c Author Two   2026-01-02 10:00 +0000   3│
  >   - faf4a5c Author Two   2026-01-02 10:00 +0000   4│ int add(int a, int b) {
  >   - faf4a5c Author Two   2026-01-02 10:00 +0000   5│     return a + b;
  >   - faf4a5c Author Two   2026-01-02 10:00 +0000   6│ }...
- `tests.test_blame_view.test_blame_enter_opens_diff`
  > AssertionError: assert '\n\n\n\n\n\n...42:51 2026)\n' == '8fe4d07 Auth...        93%\n'
  >   
  >   - 8fe4d07 Author One   2026-01-01 10:00 +0000   1│ #include <stdio.h>
  >   - faf4a5c Author Two   2026-01-02 10:00 +0000   2│ #include <stdlib.h>
  >   - faf4a5c Author Two   2026-01-02 10:00 +0000   3│
  >   - faf4a5c Author Two   2026-01-02 10:00 +0000   4│ int add(int a, int b) {
  >   - faf4a5c Author Two   2026-01-02 10:00 +0000   5│     return a + b;
  >   - faf4a5c Author Two   2026-01-02 10:00 +0000   6│ }...
- *(... 35 more in this cluster)*

### `rc_unexpected_zero` — 19 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_subcommands.test_blame_requires_file`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'blame'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_edge_cases.test_numeric_argument_alone`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '123'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_edge_cases.test_plus_without_number`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '+'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 16 more in this cluster)*

### `rc_mismatch_got2_want1` — 14 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_argv_and_options.test_empty_argument_list`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b"usage: tig [OPTIONS] [ARGS]\nTry 'tig --help' for more information.\n").returncode
- `tests.test_cli_args.test_change_directory_invalid`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-C', '/nonexistent/path/to/nowhere'], returncode=2, stdout='', stderr="tig: unknown option: -C\nusage: tig [OPTIONS] [ARGS]\nTry 'tig --h
- `tests.test_cli_args.test_multiple_c_flags_first_invalid`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-C', '/nonexistent', '-C', '/tmp/pytest-of-root/pytest-0/test_multiple_c_flags_first_in2/valid', '--version'], returncode=2, stdout='', s
- *(... 11 more in this cluster)*

### `rc_mismatch_got0_want1` — 9 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_cli_args.test_subcommand_status_no_tty`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'status'], returncode=0, stdout='', stderr='').returncode
- `tests.test_cli_args.test_subcommand_log_no_tty`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'log'], returncode=0, stdout='', stderr='').returncode
- `tests.test_cli_args.test_subcommand_show_no_tty`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'show'], returncode=0, stdout='', stderr='').returncode
- *(... 6 more in this cluster)*

### `boolean_false` — 8 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_basic_functionality.test_version_exact_format`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x711cd4c2c3b0>('tig version ')
  >  +    where <built-in method startswith of str object at 0x711cd4c2c3b0> = 'tig 0.1.0'.startswith
- `tests.test_env_and_config.test_tig_trace_enables_logging`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmp44nk72yj/trace.log').exists
- `tests.test_env_and_config.test_multiple_env_vars_together`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpaufl2xet/trace.log').exists
- *(... 5 more in this cluster)*

### `bytes_output_mismatch` — 6 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_coverage_io_parse.test_stdin_with_git_log_output`
  > assert (b'tty' in b"usage: tig [options] [args]\ntry 'tig --help' for more information.\n" or 2 == 0)
  >  +  where b"usage: tig [options] [args]\ntry 'tig --help' for more information.\n" = <built-in method lower of bytes object at 0x7f5b5751fbb0>()
  >  +    where <built-in method lower of bytes object at 0x7f5b5751fbb0> = b"usage: tig [OPTIONS] [ARGS]\nTry 'tig --help' for more information.\n".lower
  >  +      where b"usage: tig [OPTIONS] [ARGS]\nTry 'tig --help' for more information.\n" = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b"usage: tig [OPTIONS] [ARGS]
  >  +  and   2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b"usage: tig [OPTIONS] [ARGS]\nTry 'tig --help' for more information.\n").returncode
- `tests.test_coverage_io_parse.test_stdin_with_git_diff_output`
  > assert (b'tty' in b"usage: tig [options] [args]\ntry 'tig --help' for more information.\n" or 2 == 0)
  >  +  where b"usage: tig [options] [args]\ntry 'tig --help' for more information.\n" = <built-in method lower of bytes object at 0x7f5b5723a720>()
  >  +    where <built-in method lower of bytes object at 0x7f5b5723a720> = b"usage: tig [OPTIONS] [ARGS]\nTry 'tig --help' for more information.\n".lower
  >  +      where b"usage: tig [OPTIONS] [ARGS]\nTry 'tig --help' for more information.\n" = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b"usage: tig [OPTIONS] [ARGS]
  >  +  and   2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b"usage: tig [OPTIONS] [ARGS]\nTry 'tig --help' for more information.\n").returncode
- `tests.test_coverage_io_parse.test_stdin_with_git_show_output`
  > assert (b'tty' in b"usage: tig [options] [args]\ntry 'tig --help' for more information.\n" or 2 == 0)
  >  +  where b"usage: tig [options] [args]\ntry 'tig --help' for more information.\n" = <built-in method lower of bytes object at 0x7f5b57385760>()
  >  +    where <built-in method lower of bytes object at 0x7f5b57385760> = b"usage: tig [OPTIONS] [ARGS]\nTry 'tig --help' for more information.\n".lower
  >  +      where b"usage: tig [OPTIONS] [ARGS]\nTry 'tig --help' for more information.\n" = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b"usage: tig [OPTIONS] [ARGS]
  >  +  and   2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b"usage: tig [OPTIONS] [ARGS]\nTry 'tig --help' for more information.\n").returncode
- *(... 3 more in this cluster)*

### `type_error` — 2 test(s)

**Quick patch ideas:**
- Specific TypeError; check arg types vs expected

**Sample failures:**

- `tests.test_argument_parsing.test_version_multiple_times`
  > TypeError: 'in <string>' requires string as left operand, not bytes
- `tests.test_argv_and_options.test_version_output_format`
  > TypeError: 'in <string>' requires string as left operand, not bytes

### `returned_none` — 2 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_output_modes.test_version_output_contains_build_info`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f5b59716680>(b'tig version \\d+\\.\\d+', b'tig 0.1.0\n')
  >  +    where <function search at 0x7f5b59716680> = re.search
  >  +    and   b'tig 0.1.0\n' = <built-in method lower of bytes object at 0x7f5b56a76cd0>()
  >  +      where <built-in method lower of bytes object at 0x7f5b56a76cd0> = b'tig 0.1.0\n'.lower
  >  +        where b'tig 0.1.0\n' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'tig 0.1.0\n', stderr=b'').stdout
- `eval.tests.test_tig_external.test_ext_help_shows_usage`
  > AssertionError: assert None
  >  +  where None = <function search at 0x72646251e680>('or:\\s+tig\\s+show', 'tig 0.1.0 - bootstrap scaffold\n\nUsage: tig [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Pri
  >  +    where <function search at 0x72646251e680> = re.search

### `rc_mismatch_got1_want2` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_argument_parsing_improved.test_version_format_detailed`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len(['tig 0.1.0'])

### `rc_mismatch_got0_want2` — 1 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_subcommands.TestHelpConsistency.test_version_and_v_produce_same_output`
  > assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'tig 0.1.0\n', stderr=b'').returncode
  >  +  and   2 = CompletedProcess(args=['/workspace/executable', '-v'], returncode=2, stdout=b'', stderr=b"tig: unknown option: -v\nusage: tig [OPTIONS] [ARGS]\nTry 'tig --help' for more information.\n")

