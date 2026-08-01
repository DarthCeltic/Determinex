# Action Sheet — jrnxf__thokr.09375ef

**Current:** 19.94%  (130/652)
**Pass / Fail / Skip:** 130 / 261 / 0
**Gap to 100%:** 80.06 percentage points (522 tests)

## Failure clusters

261 failed tests grouped into 9 buckets (sorted by count).

### `other_assertion` — 145 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_additional_behaviors.test_help_output_structure`
  > AssertionError: assert 'USAGE:' in 'Usage: thokr [OPTIONS]\n       thokr [OPTIONS] <text>\n\nA typing test tool for the terminal.\n\nOPTIONS:\n  -h, --help                    Print help\n  -V, --versi
- `tests.test_additional_behaviors.test_help_with_invalid_flags_shows_help`
  > AssertionError: assert b'USAGE:' in b'Usage: thokr [OPTIONS]\n       thokr [OPTIONS] <text>\n\nA typing test tool for the terminal.\n\nOPTIONS:\n  -h, --help                    Print help\n  -V, --ver
  >  +  where b'Usage: thokr [OPTIONS]\n       thokr [OPTIONS] <text>\n\nA typing test tool for the terminal.\n\nOPTIONS:\n  -h, --help                    Print help\n  -V, --version                 Print
- `tests.test_additional_behaviors.test_stdin_error_includes_usage`
  > AssertionError: assert b'USAGE:' in b'stdin must be a tty\nUsage: thokr [OPTIONS]\n       thokr [OPTIONS] <text>\n\nA typing test tool for the terminal.\n\nOPTIONS:\n  -h, --help                    Pr
  >  +  where b'stdin must be a tty\nUsage: thokr [OPTIONS]\n       thokr [OPTIONS] <text>\n\nA typing test tool for the terminal.\n\nOPTIONS:\n  -h, --help                    Print help\n  -V, --version 
- *(... 142 more in this cluster)*

### `string_output_mismatch` — 65 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_baseline_smoke.test_help_matches_baseline_except_version`
  > AssertionError: assert 'Usage: thokr...st be a tty\n' == '\\1 <VERSION...efault: 15]\n'
  >   
  >   - \1 <VERSION>
  >   - sleek typing tui with visualized results and historical logging
  >   + Usage: thokr [OPTIONS]
  >   +        thokr [OPTIONS] <text>
  >     
  >   + A typing test tool for the terminal....
- `tests.test_cli_args.TestHelpAndVersion.test_help_short`
  > AssertionError: assert 'Usage: thokr...st be a tty\n' == 'thokr 0.4.1\...efault: 15]\n'
  >   
  >   - thokr 0.4.1
  >   - sleek typing tui with visualized results and historical logging
  >   + Usage: thokr [OPTIONS]
  >   +        thokr [OPTIONS] <text>
  >     
  >   + A typing test tool for the terminal....
- `tests.test_cli_args.TestHelpAndVersion.test_help_long`
  > AssertionError: assert 'Usage: thokr...st be a tty\n' == 'thokr 0.4.1\...efault: 15]\n'
  >   
  >   - thokr 0.4.1
  >   - sleek typing tui with visualized results and historical logging
  >   + Usage: thokr [OPTIONS]
  >   +        thokr [OPTIONS] <text>
  >     
  >   + A typing test tool for the terminal....
- *(... 62 more in this cluster)*

### `missing_file` — 16 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_logging.test_log_file_has_correct_format`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_log_file_has_correct_form2/thokr/log.csv'
- `tests.test_logging.test_log_file_appends_multiple_tests`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_log_file_appends_multiple2/thokr/log.csv'
- `tests.test_logging.test_log_file_header_written_once`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_log_file_header_written_o2/thokr/log.csv'
- *(... 13 more in this cluster)*

### `uncategorized` — 14 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_graphs.test_multiword_graph_rendering`
  > RuntimeError: Failed to send keys: can't find pane: test_multiword_graph
- `tests.test_graphs.test_single_character_edge_case`
  > RuntimeError: Failed to send keys: can't find pane: test_single_char
- `tests.test_graphs.test_perfect_accuracy_short_test`
  > RuntimeError: Failed to send keys: can't find pane: test_perfect_short
- *(... 11 more in this cluster)*

### `boolean_false` — 12 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_logging.test_log_file_created_after_completion`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/pytest-of-root/pytest-0/test_log_file_created_after_co2/thokr/log.csv').exists
- `tests.test_tui_interactive.test_tui_default_starts_and_exits`
  > assert False
  >  +  where False = isalive()
  >  +    where isalive = <pexpect.pty_spawn.spawn object at 0x7f18043c48e0>.isalive
- `tests.test_tui_interactive.test_tui_completes_test_and_shows_results`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/pytest-of-root/pytest-0/test_tui_completes_test_and_sh2/thokr/log.csv').exists
- *(... 9 more in this cluster)*

### `rc_mismatch_got2_want0` — 5 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_basic.TestTimeLimitOptions.test_time_limit_long_flag`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--number-of-secs', '60', '--help'], returncode=2, stdout=b'', stderr=b"error: unknown option '--number-of-secs'\nUsage: thokr [OPTIONS]\n       th
- `tests.test_edge_cases.TestFlagParsing.test_equals_syntax_word_count`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--number-of-words=10', '--help'], returncode=2, stdout=b'', stderr=b"error: unknown option '--number-of-words=10'\nUsage: thokr [OPTIONS]\n       
- `tests.test_edge_cases.TestFlagParsing.test_equals_syntax_language`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--supported-language=english1k', '--help'], returncode=2, stdout=b'', stderr=b"error: unknown option '--supported-language=english1k'\nUsage: thok
- *(... 2 more in this cluster)*

### `rc_unexpected_zero` — 2 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_subcommands.TestUnknownArguments.test_positional_argument_without_flag`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'sometext'], returncode=0, stdout=b'sometext\n', stderr=b'').returncode
- `tests.test_subcommands.TestUnknownArguments.test_multiple_unknown_args`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'arg1', 'arg2', 'arg3'], returncode=0, stdout=b'arg1 arg2 arg3\n', stderr=b'').returncode

### `rc_mismatch_got0_want2` — 1 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `eval.tests.test_args_parsing.test_unexpected_positional_argument_errors`
  > assert 0 == 2

### `returned_none` — 1 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_behavior.test_usage_line_mentions_executable`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7fe87ca8a680>('^\\s*executable\\s+\\[OPTIONS\\]\\s*$', 'Usage: thokr [OPTIONS]\n       thokr [OPTIONS] <text>\n\nA typing test tool for the terminal.\n\nOPTIONS:
  >  +    where <function search at 0x7fe87ca8a680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE

