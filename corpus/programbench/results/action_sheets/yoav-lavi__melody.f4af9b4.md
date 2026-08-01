# Action Sheet — yoav-lavi__melody.f4af9b4

**Current:** 8.15%  (131/1607)
**Pass / Fail / Skip:** 131 / 669 / 0
**Gap to 100%:** 91.85 percentage points (1476 tests)

## Failure clusters

669 failed tests grouped into 13 buckets (sorted by count).

### `string_output_mismatch` — 248 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_output.test_short_help_matches_long_help`
  > AssertionError: assert '(?:na){16}(?: batman){2}\n' == ''
  >   
  >   + (?:na){16}(?: batman){2}
- `eval.tests.test_help_output.test_help_takes_precedence_over_unknown_flag`
  > AssertionError: assert 'melody 0.1.0...int version\n' == ''
  >   
  >   + melody 0.1.0
  >   + Interactive TUI tool driven by tmux/libtmux/pexpect harness
  >   + 
  >   + Usage: melody [OPTIONS] [ARGS]...
  >   + USAGE: melody [OPTIONS] [ARGS]...
  >   + usage: melody [OPTIONS] [ARGS]......
- `eval.tests.test_help_output.test_help_no_color_flag_does_not_change_help`
  > AssertionError: assert 'melody 0.1.0...int version\n' == ''
  >   
  >   + melody 0.1.0
  >   + Interactive TUI tool driven by tmux/libtmux/pexpect harness
  >   + 
  >   + Usage: melody [OPTIONS] [ARGS]...
  >   + USAGE: melody [OPTIONS] [ARGS]...
  >   + usage: melody [OPTIONS] [ARGS]......
- *(... 245 more in this cluster)*

### `other_assertion` — 238 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_additional_symbols.test_symbol_return`
  > AssertionError: assert b'\\r' in b'melody 0.1.0\n----------------------------------------\nInteractive TUI tool driven by tmux/libtmux/pexpect harness\n\nJournals\nTasks\nFilter\nHelp\nQuit\nPress q t
  >  +  where b'melody 0.1.0\n----------------------------------------\nInteractive TUI tool driven by tmux/libtmux/pexpect harness\n\nJournals\nTasks\nFilter\nHelp\nQuit\nPress q to quit\nj/k: navigate\n
- `tests.test_additional_symbols.test_symbol_feed`
  > AssertionError: assert b'\\f' in b'melody 0.1.0\n----------------------------------------\nInteractive TUI tool driven by tmux/libtmux/pexpect harness\n\nJournals\nTasks\nFilter\nHelp\nQuit\nPress q t
  >  +  where b'melody 0.1.0\n----------------------------------------\nInteractive TUI tool driven by tmux/libtmux/pexpect harness\n\nJournals\nTasks\nFilter\nHelp\nQuit\nPress q to quit\nj/k: navigate\n
- `tests.test_additional_symbols.test_symbol_null`
  > AssertionError: assert b'\\0' in b'melody 0.1.0\n----------------------------------------\nInteractive TUI tool driven by tmux/libtmux/pexpect harness\n\nJournals\nTasks\nFilter\nHelp\nQuit\nPress q t
  >  +  where b'melody 0.1.0\n----------------------------------------\nInteractive TUI tool driven by tmux/libtmux/pexpect harness\n\nJournals\nTasks\nFilter\nHelp\nQuit\nPress q to quit\nj/k: navigate\n
- *(... 235 more in this cluster)*

### `rc_unexpected_zero` — 67 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_cli_combinations.test_repl_short`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '-r'], returncode=0, stdout=b'melody\n', stderr=b'').returncode
- `tests.test_cli_combinations.test_repl_long`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '--repl'], returncode=0, stdout=b'melody\n', stderr=b'').returncode
- `tests.test_compiler_errors.test_unrecognized_symbol_namespace`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable'], returncode=0, stdout=b'melody 0.1.0\n----------------------------------------\nInteractive TUI tool driven by tmux/libtmux/pexpect harness\n\nJour
- *(... 64 more in this cluster)*

### `bytes_output_mismatch` — 61 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_basic_invocation.test_empty_stdin`
  > AssertionError: assert b'melody 0.1....ompdef melody' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'melody 0.1.0\n----------------------------------------\nInteractive TUI to'
  >   +  b'ol driven by tmux/libtmux/pexpect harness\n\nJournals\nTasks\nFilter\nHel'
  >   +  b'p\nQuit\nPress q to quit\nj/k: navigate\nEnter\nn: new\nWelcome\nLoading\nRe'
  >   +  b'ady\n#compdef melody\n(?:a|b)\n(?:foo|bar|baz)\n(?<=\n(?<group>\n(?=\n*'...
- `tests.test_compiler_errors.test_empty_source`
  > AssertionError: assert (b'melody 0.1....pdef melody\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'melody 0.1.0\n----------------------------------------\nInteractive TUI to'
  >   +  b'ol driven by tmux/libtmux/pexpect harness\n\nJournals\nTasks\nFilter\nHel'
  >   +  b'p\nQuit\nPress q to quit\nj/k: navigate\nEnter\nn: new\nWelcome\nLoading\nRe'
  >   +  b'ady\n#compdef melody\n(?:a|b)\n(?:foo|bar|baz)\n(?<=\n(?<group>\n(?=\n*'...
- `tests.test_compiler_errors.test_only_comments`
  > AssertionError: assert (b'melody 0.1.... comment */\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'melody 0.1.0\n----------------------------------------\nInteractive TUI to'
  >   +  b'ol driven by tmux/libtmux/pexpect harness\n\nJournals\nTasks\nFilter\nHel'
  >   +  b'p\nQuit\nPress q to quit\nj/k: navigate\nEnter\nn: new\nWelcome\nLoading\nRe'
  >   +  b'ady\n#compdef melody\n(?:a|b)\n(?:foo|bar|baz)\n(?<=\n(?<group>\n(?=\n*'...
- *(... 58 more in this cluster)*

### `rc_mismatch_got0_want65` — 21 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_edge_cases.test_file_not_found_error`
  > AssertionError: assert 0 == 65
  >  +  where 0 = CompletedProcess(args=['./executable', '/nonexistent/file.mdy'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_cli_edge_cases.test_directory_as_input_file_error`
  > AssertionError: assert 0 == 65
  >  +  where 0 = CompletedProcess(args=['./executable', '/tmp'], returncode=0, stdout=b'melody 0.1.0\n----------------------------------------\nInteractive TUI tool driven by tmux/libtmux/pexpect harness
- `tests.test_cli_edge_cases.test_invalid_utf8_in_input_file`
  > AssertionError: assert 0 == 65
  >  +  where 0 = CompletedProcess(args=['./executable', '/tmp/pytest-of-root/pytest-0/test_invalid_utf8_in_input_fil2/invalid.mdy'], returncode=0, stdout=b'melody 0.1.0\n---------------------------------
- *(... 18 more in this cluster)*

### `rc_mismatch_got65_want0` — 11 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_cli_behavior.test_compile_from_file_exact`
  > AssertionError: assert 65 == 0
  >  +  where 65 = CompletedProcess(args=['/workspace/executable', '/workspace/eval/fixtures/hashtag.mel'], returncode=65, stdout=b'', stderr=b'').returncode
- `tests.test_acceptance.test_log_parser_with_timestamp_and_level`
  > AssertionError: assert 65 == 0
  >  +  where 65 = CompletedProcess(args=['./executable', '/workspace/eval/test_resources/test_acceptance/log_parser.mdy'], returncode=65, stdout=b'', stderr=b'').returncode
- `tests.test_acceptance.test_complex_captures_named_groups`
  > AssertionError: assert 65 == 0
  >  +  where 65 = CompletedProcess(args=['./executable', '/workspace/eval/test_resources/test_acceptance/complex_captures.mdy'], returncode=65, stdout=b'', stderr=b'').returncode
- *(... 8 more in this cluster)*

### `boolean_false` — 9 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_comprehensive_coverage.test_output_file_writing`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpwsht21n5/output.txt').exists
  >  +      where PosixPath('/tmp/tmpwsht21n5/output.txt') = Path('/tmp/tmpwsht21n5/output.txt')
- `tests.test_comprehensive_patterns.test_multiple_outputs_to_files`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpvco6e4fg/out1.txt').exists
- `tests.test_env_config_handling.test_clicolor_force_enables_color_even_when_not_tty`
  > assert False
  >  +  where False = has_ansi(b'melody 0.1.0\n----------------------------------------\nInteractive TUI tool driven by tmux/libtmux/pexpect harness\n\nJournals\nTasks\nFilter\nHelp\nQuit\nPress q to quit
  >  +    where b'melody 0.1.0\n----------------------------------------\nInteractive TUI tool driven by tmux/libtmux/pexpect harness\n\nJournals\nTasks\nFilter\nHelp\nQuit\nPress q to quit\nj/k: navigate
- *(... 6 more in this cluster)*

### `rc_mismatch_got0_want64` — 4 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_args.test_repl_rejects_piped_io_even_with_double_dash[args0]`
  > AssertionError: assert 0 == 64
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--repl'], returncode=0, stdout=b'melody\n', stderr=b'').returncode
- `eval.tests.test_args.test_repl_rejects_piped_io_even_with_double_dash[args1]`
  > assert 0 == 64
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--repl', '--'], returncode=0, stdout=b"error: unexpected argument '--repl' found\nError: unexpected argument '--repl' found\nunknown flag
- `eval.tests.test_args.test_repl_rejects_piped_io_even_with_double_dash[args2]`
  > assert 0 == 64
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--repl', '--', '-'], returncode=0, stdout=b"error: unexpected argument '--repl' found\nError: unexpected argument '--repl' found\nunknown
- *(... 1 more in this cluster)*

### `missing_file` — 3 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `eval.tests.test_compile_io.test_compile_output_to_file_flag_creates_file_and_suppresses_stdout`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_compile_output_to_file_fl2/out.regex'
- `eval.tests.test_cli_behavior.test_output_file_writes_regex`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_output_file_writes_regex2/out.regex'
- `tests.test_externalized.test_ext_cli_file_test`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpnsre9z3f/output.txt'

### `rc_mismatch_got0_want74` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_edge_cases.test_write_file_to_nonexistent_directory`
  > AssertionError: assert 0 == 74
  >  +  where 0 = CompletedProcess(args=['./executable', '-o', '/nonexistent/dir/output.txt'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_cli_edge_cases.test_write_to_read_only_location`
  > AssertionError: assert 0 == 74
  >  +  where 0 = CompletedProcess(args=['./executable', '-o', '/proc/version'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_errors.test_output_to_nonexistent_directory`
  > AssertionError: assert 0 == 74
  >  +  where 0 = CompletedProcess(args=['./executable', '/tmp/pytest-of-root/pytest-0/test_output_to_nonexistent_dir2/test.mdy', '-o', '/nonexistent/dir/out.txt'], returncode=0, stdout=b'', stderr=b'').r

### `rc_mismatch_got0_want66` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_edge_cases.test_stdin_without_pipe_error`
  > AssertionError: assert 0 == 66
  >  +  where 0 = CompletedProcess(args=['script', '-q', '-e', '-c', './executable', '/dev/null'], returncode=0, stdout=b'melody 0.1.0\r\n----------------------------------------\r\nInteractive TUI tool d
- `tests.test_cli_edge_cases.test_explicit_stdin_marker_without_pipe`
  > AssertionError: assert 0 == 66
  >  +  where 0 = CompletedProcess(args=['script', '-q', '-e', '-c', './executable -', '/dev/null'], returncode=0, stdout=b'', stderr=b'').returncode

### `returned_none` — 1 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_output.test_help_contains_completions_placeholder`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f6b11bfe680>('--generate-completions\\s+<completions>', '')
  >  +    where <function search at 0x7f6b11bfe680> = re.search

### `rc_mismatch_got0_want2` — 1 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_cli_edge_cases.test_multiple_input_files_rejected`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['./executable', '/tmp/test1.mdy', '/tmp/test2.mdy'], returncode=0, stdout=b'melody 0.1.0\n----------------------------------------\nInteractive TUI tool driven by 

