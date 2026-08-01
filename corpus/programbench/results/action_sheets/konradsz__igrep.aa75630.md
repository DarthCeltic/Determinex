# Action Sheet — konradsz__igrep.aa75630

**Current:** 50.0%  (352/704)
**Pass / Fail / Skip:** 352 / 351 / 1
**Gap to 100%:** 50.00 percentage points (352 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_tui_interaction.test_tui_navigation_changes_selected_line`
  - reason: test_tui_navigation_changes_selected_line depends on test_tui_quit_key_exits

## Failure clusters

351 failed tests grouped into 11 buckets (sorted by count).

### `other_assertion` — 181 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_basic.test_no_arguments`
  > AssertionError: assert b'required arguments were not provided' in b'usage: igrep [OPTIONS] [PATTERN] [PATH...]\n'
  >  +  where b'usage: igrep [OPTIONS] [PATTERN] [PATH...]\n' = CompletedProcess(args=['./executable'], returncode=2, stdout=b'', stderr=b'usage: igrep [OPTIONS] [PATTERN] [PATH...]\n').stderr
- `eval.tests.test_basic.test_help_flag`
  > AssertionError: assert b'Usage:' in b'Interactive Grep 0.1.0\nusage: igrep [OPTIONS] [PATTERN] [PATH...]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --verbose  Verb
  >  +  where b'Interactive Grep 0.1.0\nusage: igrep [OPTIONS] [PATTERN] [PATH...]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --verbose  Verbose\n  -q, --quiet    Quie
- `eval.tests.test_basic.test_help_short_flag`
  > AssertionError: assert b'Usage:' in b'Interactive Grep 0.1.0\nusage: igrep [OPTIONS] [PATTERN] [PATH...]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --verbose  Verb
  >  +  where b'Interactive Grep 0.1.0\nusage: igrep [OPTIONS] [PATTERN] [PATH...]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --verbose  Verbose\n  -q, --quiet    Quie
- *(... 178 more in this cluster)*

### `string_output_mismatch` — 72 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_cli.TestBasicCLI.test_help_flag`
  > AssertionError: assert 'Interactive ... ignore all\n' == 'Interactive ...int version\n'
  >   
  >   - Interactive Grep
  >   + Interactive Grep 0.1.0
  >   ?                 ++++++
  >   + usage: igrep [OPTIONS] [PATTERN] [PATH...]
  >   - 
  >   - Usage: executable [OPTIONS] --type-list <PATTERN> [PATHS]......
- `tests.test_cli.TestBasicCLI.test_help_short_flag`
  > AssertionError: assert 'Interactive ... ignore all\n' == 'Interactive ...int version\n'
  >   
  >   - Interactive Grep
  >   + Interactive Grep 0.1.0
  >   ?                 ++++++
  >   + usage: igrep [OPTIONS] [PATTERN] [PATH...]
  >   - 
  >   - Usage: executable [OPTIONS] --type-list <PATTERN> [PATHS]......
- `tests.test_cli.TestBasicCLI.test_version_flag`
  > AssertionError: assert 'igrep 0.1.0\n' == 'igrep 1.3.0\n'
  >   
  >   - igrep 1.3.0
  >   ?        --
  >   + igrep 0.1.0
  >   ?       ++
- *(... 69 more in this cluster)*

### `rc_mismatch_got2_want0` — 33 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `eval.tests.test_editor.test_custom_command_valid`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--custom-command', 'vim +{line_number} {file_name}', '--type-list'], returncode=2, stdout=b'', stderr=b'igrep: error: unrecognized argument: --cus
- `eval.tests.test_editor.test_custom_command_accepted_with_type_list`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--custom-command', 'vim +{line_number}', '--type-list'], returncode=2, stdout=b'', stderr=b'igrep: error: unrecognized argument: --custom-command\
- `eval.tests.test_editor.test_theme_dark`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--theme', 'dark', '--type-list'], returncode=2, stdout=b'', stderr=b'igrep: error: unrecognized argument: --theme\n').returncode
- *(... 30 more in this cluster)*

### `subprocess_failed` — 28 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_keymap_popup.test_keymap_popup_scroll_up_after_scroll_down`
  > subprocess.CalledProcessError: Command '['tmux', 'send-keys', '-t', 'test_keymap_up', 'q']' returned non-zero exit status 1.
- `tests.test_keymap_popup.test_keymap_popup_scroll_left`
  > subprocess.CalledProcessError: Command '['tmux', 'send-keys', '-t', 'test_keymap_left', 'q']' returned non-zero exit status 1.
- `tests.test_keymap_popup.test_keymap_popup_scroll_right`
  > subprocess.CalledProcessError: Command '['tmux', 'send-keys', '-t', 'test_keymap_right', 'q']' returned non-zero exit status 1.
- *(... 25 more in this cluster)*

### `rc_mismatch_got2_want1` — 12 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli.test_custom_command_missing_tokens`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--custom-command', 'invalid', 'pattern'], returncode=2, stdout='', stderr='igrep: error: unrecognized argument: --custom-command\n').retu
- `tests.test_cli.test_custom_command_missing_line_number_token`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--custom-command', 'editor {file_name}', 'pattern'], returncode=2, stdout='', stderr='igrep: error: unrecognized argument: --custom-comma
- `tests.test_cli.test_custom_command_missing_file_name_token`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--custom-command', 'editor {line_number}', 'pattern'], returncode=2, stdout='', stderr='igrep: error: unrecognized argument: --custom-com
- *(... 9 more in this cluster)*

### `rc_unexpected_zero` — 10 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `eval.tests.test_argparse_validation.test_unknown_flag_error_and_tip`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--type-list', '--unknown'], returncode=0, stdout='rust: *.rs\npython: *.py\njavascript: *.js\ntypescript: *.ts\nhtml: *.html\ncss: *.css\
- `eval.tests.test_argparse_validation.test_enum_invalid_value_errors_and_lists_possible`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--type-list', '--editor', 'notaneditor'], returncode=0, stdout='rust: *.rs\npython: *.py\njavascript: *.js\ntypescript: *.ts\nhtml: *.htm
- `eval.tests.test_argparse_validation.test_other_choice_flags_reject_invalid[--theme-bad-possible values: light, dark]`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--type-list', '--theme', 'bad'], returncode=0, stdout='rust: *.rs\npython: *.py\njavascript: *.js\ntypescript: *.ts\nhtml: *.html\ncss: *
- *(... 7 more in this cluster)*

### `rc_mismatch_got0_want1` — 7 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_cli.test_invalid_glob_pattern_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-g', '[invalid', 'pattern'], returncode=0, stdout='', stderr='').returncode
- `tests.test_cli.test_invalid_type_name_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-t', 'invalidtype', 'pattern'], returncode=0, stdout='', stderr='').returncode
- `tests.test_cli.test_invalid_type_not_name_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-T', 'invalidtype', 'pattern'], returncode=0, stdout='rust: *.rs\npython: *.py\njavascript: *.js\ntypescript: *.ts\nhtml: *.html\ncss: *.
- *(... 4 more in this cluster)*

### `boolean_false` — 4 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_interactive.TestBasicInteractive.test_tui_launches_and_shows_matches`
  > AssertionError: assert False
  >  +  where False = wait_for_any(['match1.txt', 'match2.txt'], timeout=2.0)
  >  +    where wait_for_any = <test_interactive.TmuxTestHarness object at 0x7f420007e500>.wait_for_any
- `eval.tests.test_interactive_combined.test_interactive_flags`
  > AssertionError: assert False
  >  +  where False = wait_for('file1.txt')
  >  +    where wait_for = <conftest.TmuxTestHarness object at 0x7f244ecef490>.wait_for
- `eval.tests.test_interactive_combined.test_interactive_features`
  > AssertionError: assert False
  >  +  where False = wait_for('banana')
  >  +    where wait_for = <conftest.TmuxTestHarness object at 0x7f244ecd5930>.wait_for
- *(... 1 more in this cluster)*

### `empty_list_or_string` — 2 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_tui_interactions.test_navigation_at_last_match_stays_at_boundary`
  > IndexError: list index out of range
- `tests.test_tui_interactions.test_shift_g_jumps_to_last_match`
  > IndexError: list index out of range

### `returned_none` — 1 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_tui_interaction.test_tui_quit_key_exits`
  > AssertionError: assert None is not None
  >  +  where None = wait_for_any(['FINISHED', 'Found', 'No matches', 'Error'], timeout=3.0)
  >  +    where wait_for_any = <test_tui_interaction.TmuxHarness object at 0x7f814fc20550>.wait_for_any

### `rc_mismatch_got0_want2` — 1 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_cli.test_pattern_with_type_list_mutually_exclusive`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'pattern', '--type-list'], returncode=0, stdout='', stderr='').returncode

