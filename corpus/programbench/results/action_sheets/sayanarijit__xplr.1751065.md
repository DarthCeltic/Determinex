# Action Sheet — sayanarijit__xplr.1751065

**Current:** 31.03%  (270/870)
**Pass / Fail / Skip:** 270 / 463 / 0
**Gap to 100%:** 68.97 percentage points (600 tests)

## Failure clusters

463 failed tests grouped into 10 buckets (sorted by count).

### `other_assertion` — 235 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_help_long`
  > AssertionError: assert b'USAGE:' in b'xplr 0.1.0 - bootstrap scaffold\n\nUsage: xplr [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n'
  >  +  where b'xplr 0.1.0 - bootstrap scaffold\n\nUsage: xplr [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['./executable', '--help
- `tests.test_basic_invocation.test_help_short`
  > AssertionError: assert b'USAGE:' in b'xplr 0.1.0 - bootstrap scaffold\n\nUsage: xplr [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n'
  >  +  where b'xplr 0.1.0 - bootstrap scaffold\n\nUsage: xplr [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['./executable', '-h'], 
- `tests.test_basic_invocation.test_help_contains_all_flags`
  > AssertionError: Flag b'--read-only' not in help output
  > assert b'--read-only' in b'xplr 0.1.0 - bootstrap scaffold\n\nUsage: xplr [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n'
  >  +  where b'xplr 0.1.0 - bootstrap scaffold\n\nUsage: xplr [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['./executable', '--help
- *(... 232 more in this cluster)*

### `rc_mismatch_got2_want0` — 128 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_config_handling.test_config_with_valid_file`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '-c', '/tmp/tmp62lk5qvl.lua', '--version'], returncode=2, stdout=b'', stderr=b"xplr: unknown option: -c\nusage: xplr [OPTIONS] [ARGS]\nTry 'xplr --
- `tests.test_config_handling.test_extra_config_multiple`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '-C', '/tmp/tmpw8z2ndw2/extra1.lua', '/tmp/tmpw8z2ndw2/extra2.lua', '--version'], returncode=2, stdout=b'', stderr=b"xplr: unknown option: -C\nusag
- `tests.test_config_handling.test_extra_config_stops_at_next_flag`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '-C', '/tmp/tmpkrcgrbpa.lua', '--version'], returncode=2, stdout=b'', stderr=b"xplr: unknown option: -C\nusage: xplr [OPTIONS] [ARGS]\nTry 'xplr --
- *(... 125 more in this cluster)*

### `rc_mismatch_got2_want1` — 30 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_flags.test_print_msg_in_without_arguments_error`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['./executable', '-M'], returncode=2, stdout='', stderr="xplr: unknown option: -M\nusage: xplr [OPTIONS] [ARGS]\nTry 'xplr --help' for more information.\n").returnc
- `tests.test_cli_flags.test_print_msg_in_long_flag_without_arguments_error`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['./executable', '--print-msg-in'], returncode=2, stdout='', stderr="xplr: unknown option: --print-msg-in\nusage: xplr [OPTIONS] [ARGS]\nTry 'xplr --help' for more 
- `tests.test_cli_flags.test_print_msg_in_invalid_message_variant`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['./executable', '-M', '{Foo: Bar}'], returncode=2, stdout='', stderr="xplr: unknown option: -M\nusage: xplr [OPTIONS] [ARGS]\nTry 'xplr --help' for more informatio
- *(... 27 more in this cluster)*

### `missing_dict_key` — 23 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_file_ops_advanced.test_symlink_chain_resolution`
  > KeyError: 'directory_buffer'
- `tests.test_file_ops_advanced.test_broken_symlink_chain_detection`
  > KeyError: 'directory_buffer'
- `tests.test_file_ops_advanced.test_circular_symlink_detected_as_broken`
  > KeyError: 'directory_buffer'
- *(... 20 more in this cluster)*

### `string_output_mismatch` — 19 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_version_help.TestVersion.test_version_long_flag`
  > AssertionError: assert 'xplr 0.1.0\n' == 'xplr 1.1.0\n'
  >   
  >   - xplr 1.1.0
  >   ?      ^
  >   + xplr 0.1.0
  >   ?      ^
- `tests.test_version_help.TestVersion.test_version_short_flag`
  > AssertionError: assert 'xplr 0.1.0\n' == 'xplr 1.1.0\n'
  >   
  >   - xplr 1.1.0
  >   ?      ^
  >   + xplr 0.1.0
  >   ?      ^
- `tests.test_version_help.TestHelp.test_help_long_flag`
  > AssertionError: assert 'xplr 0.1.0 -...int version\n' == 'xplr 1.1.0\n... explicitly\n'
  >   
  >   + xplr 0.1.0 - bootstrap scaffold
  >   - xplr 1.1.0
  >   - Arijit Basu <hi@arijitbasu.in>
  >   - A hackable, minimal, fast TUI file explorer
  >     
  >   + Usage: xplr [OPTIONS] [ARGS]...
- *(... 16 more in this cluster)*

### `rc_unexpected_zero` — 13 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_basic_invocation.test_version_with_invalid_arg`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '--version', '--invalid'], returncode=0, stdout=b'xplr 0.1.0\n', stderr=b'').returncode
- `tests.test_edge_cases.test_stdin_with_empty_lines`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '-', '-M', 'Quit'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_error_conditions.test_nonexistent_path`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '/nonexistent/path/that/does/not/exist'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 10 more in this cluster)*

### `boolean_false` — 7 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_runner.test_call_silently_creates_file`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpia6feu2s/created.txt').exists
- `tests.test_runner.test_bash_exec_silently_creates_file`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpqzvu_daj/bash_silent.txt').exists
- `tests.test_runner.test_bash_exec_silently0_creates_file`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpnkjmseh7/bash_silent0.txt').exists
- *(... 4 more in this cluster)*

### `subprocess_failed` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_config_env.test_default_config_location_is_xdg_config_home`
  > subprocess.CalledProcessError: Command '['tmux', 'capture-pane', '-t', 'xplr_xdg', '-p']' returned non-zero exit status 1.
- `eval.tests.test_config_env.test_extra_config_extends_base_config_and_can_override_it`
  > subprocess.CalledProcessError: Command '['tmux', 'capture-pane', '-t', 'xplr_extra_config', '-p']' returned non-zero exit status 1.
- `eval.tests.test_config_env.test_malformed_config_triggers_debug_error_screen_by_default`
  > subprocess.CalledProcessError: Command '['tmux', 'capture-pane', '-t', 'xplr_bad_config', '-p']' returned non-zero exit status 1.

### `returned_none` — 3 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_output.test_help_documents_dash_dash_end_of_options`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f016ff1e680>('^\\s*--\\s+Denotes the end of command-line flags and options\\s*$', 'xplr 0.1.0 - bootstrap scaffold\n\nUsage: xplr [OPTIONS] [ARGS]\n\nOptions:\n
  >  +    where <function search at 0x7f016ff1e680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- `eval.tests.test_help_output.test_help_documents_stdin_dash_flag`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f016ff1e680>('^\\s*-\\s+Reads new-line \\(\\\\n\\) separated paths from stdin\\s*$', 'xplr 0.1.0 - bootstrap scaffold\n\nUsage: xplr [OPTIONS] [ARGS]\n\nOptions
  >  +    where <function search at 0x7f016ff1e680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- `eval.tests.test_help_output.test_help_documents_args_path_and_selection`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f016ff1e680>('^\\s*<PATH>\\s+Path to focus on, or enter if directory, \\(default is `\\.`\\)\\s*$', 'xplr 0.1.0 - bootstrap scaffold\n\nUsage: xplr [OPTIONS] [A
  >  +    where <function search at 0x7f016ff1e680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE

### `rc_mismatch_got0_want1` — 2 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_cli_flags.test_nonexistent_path_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', '/nonexistent/path/to/nowhere'], returncode=0, stdout='', stderr='').returncode
- `tests.test_cli_flags.test_empty_string_path_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', ''], returncode=0, stdout='', stderr='').returncode

