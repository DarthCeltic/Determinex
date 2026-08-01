# Action Sheet — hpjansson__chafa.dd4d4c1

**Current:** 14.46%  (406/2808)
**Pass / Fail / Skip:** 406 / 899 / 0
**Gap to 100%:** 85.54 percentage points (2402 tests)

## Failure clusters

899 failed tests grouped into 10 buckets (sorted by count).

### `other_assertion` — 575 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_additional_features.test_format_and_color_combination`
  > AssertionError: assert 0 > 0
  >  +  where 0 = len(b'')
  >  +    where b'' = CompletedProcess(args=['./executable', 'tests/data/good/pixel.png', '-f', 'symbols', '-c', 'none', '-s', '5x5'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_additional_features.test_preprocess_with_low_colors`
  > AssertionError: assert 0 > 0
  >  +  where 0 = len(b'')
  >  +    where b'' = CompletedProcess(args=['./executable', 'tests/data/good/taxic.jpg', '-p', 'on', '-c', '2', '-s', '10x10'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_additional_features.test_no_preprocess_with_high_colors`
  > AssertionError: assert 0 > 0
  >  +  where 0 = len(b'')
  >  +    where b'' = CompletedProcess(args=['./executable', 'tests/data/good/taxic.jpg', '-p', 'off', '-c', '256', '-s', '10x10'], returncode=0, stdout=b'', stderr=b'').stdout
- *(... 572 more in this cluster)*

### `string_output_mismatch` — 208 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_usage.test_short_help_matches_long_help_exactly`
  > AssertionError: assert 'Usage:\nChaf...and timing:\n' == ''
  >   
  >   + Usage:
  >   + Chafa
  >   + --help
  >   + --version
  >   + --format
  >   + Usage:...
- `tests.test_subcommand_dispatch.TestNoSubcommands.test_main_help_is_only_help`
  > AssertionError: assert '' == 'Usage:\nChaf...and timing:\n'
  >   
  >   - Usage:
  >   - Chafa
  >   - --help
  >   - --version
  >   - --format
  >   - Usage:...
- `eval.tests.test_rendering_symbols.test_symbols_output_exact_for_known_asset_20x10`
  > AssertionError: assert '' == '@~B$@@@@M5MM...__@$$R$$y$@\n'
  >   
  >   - @~B$@@@@M5MM$@B$@@~@
  >   - @ $$~`4RRRRRRF`~@@ @
  >   - @ Bgggge  ggr   ~@ @
  >   - @ BPP4PF .`4     9 @
  >   - @@$ mmggg'jgagsm g@$
  >   - @@R,MMPP4@@@@@g$w@@@
- *(... 205 more in this cluster)*

### `rc_mismatch_got0_want2` — 56 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `eval.tests.test_help_usage.test_unknown_option_exit_code_and_message`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--badflag'], returncode=0, stdout='chafa 0.1.0\n----------------------------------------\nInteractive TUI tool driven by tmux/libtmux/pex
- `eval.tests.test_help_usage.test_help_does_not_override_unknown_option_error`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--help', '--badflag'], returncode=0, stdout='chafa 0.1.0\nInteractive TUI tool driven by tmux/libtmux/pexpect harness\n\nUsage: chafa [OP
- `eval.tests.test_help_usage.test_double_dash_treats_help_as_filename_error`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--', '--help'], returncode=0, stdout='chafa 0.1.0\n----------------------------------------\nInteractive TUI tool driven by tmux/libtmux/
- *(... 53 more in this cluster)*

### `rc_unexpected_zero` — 46 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_basic_invocation.test_no_arguments`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable'], returncode=0, stdout=b'chafa 0.1.0\n----------------------------------------\nInteractive TUI tool driven by tmux/libtmux/pexpect harness\n\nJourn
- `tests.test_basic_invocation.test_invalid_option`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '--invalid-option-xyz'], returncode=0, stdout=b'chafa 0.1.0\n----------------------------------------\nInteractive TUI tool driven by tmux/libtmux/
- `tests.test_basic_invocation.test_invalid_file`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'nonexistent_file_xyz.png'], returncode=0, stdout=b'chafa 0.1.0\n----------------------------------------\nInteractive TUI tool driven by tmux/libt
- *(... 43 more in this cluster)*

### `boolean_false` — 4 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `eval.tests.test_help_usage.test_help_ends_with_newline`
  > AssertionError: assert False
  >  +  where False = <built-in method endswith of str object at 0x7f7990f34030>('\n')
  >  +    where <built-in method endswith of str object at 0x7f7990f34030> = ''.endswith
- `eval.tests.test_help_usage.test_usage_header_present`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7f7990f34030>('Usage:\n')
  >  +    where <built-in method startswith of str object at 0x7f7990f34030> = ''.startswith
- `eval.tests.test_io_behavior.test_version_to_stdout_exit_0`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of bytes object at 0x7fd8791d8030>(b'Chafa version ')
  >  +    where <built-in method startswith of bytes object at 0x7fd8791d8030> = b''.startswith
  >  +      where b'' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'', stderr=b'').stdout
- *(... 1 more in this cluster)*

### `bytes_output_mismatch` — 3 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `eval.tests.test_io_behavior.test_multiple_files_are_processed_in_order_with_blank_line_separator`
  > AssertionError: assert b'BB\n' == b'BB\n\nBB\n'
  >   
  >   Full diff:
  >   - (b'BB\n\nBB\n')
  >   + b'BB\n'
- `eval.tests.test_files_list_inputs.test_files_stdin_newline_separated`
  > AssertionError: assert b'chafa 0.1.0...d/pixel.png\n' == b'@\n'
  >   
  >   At index 0 diff: b'c' != b'@'
  >   
  >   Full diff:
  >   - b'@\n'
  >   + (b'chafa 0.1.0\n----------------------------------------\nInteractive TUI too'
  >   +  b'l driven by tmux/libtmux/pexpect harness\n\nJournals\nTasks\nFilter\nHelp'...
- `eval.tests.test_files_list_inputs.test_files0_stdin_nul_separated`
  > AssertionError: assert b'chafa 0.1.0...xel.png\x00\n' == b'@\n'
  >   
  >   At index 0 diff: b'c' != b'@'
  >   
  >   Full diff:
  >   - b'@\n'
  >   + (b'chafa 0.1.0\n----------------------------------------\nInteractive TUI too'
  >   +  b'l driven by tmux/libtmux/pexpect harness\n\nJournals\nTasks\nFilter\nHelp'...

### `rc_mismatch_got0_want1` — 3 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_basic_cli.TestExitCodes.test_mixed_valid_invalid_files`
  > assert 0 == 1
- `eval.tests.test_files_list_inputs.test_files_stdin_multiple_one_missing_exitcode_1`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--files=-', '--probe=off', '--animate=no', '-f', 'symbols', '-c', 'none', '-s', '10x5'], returncode=0, stdout=b'chafa 0.1.0\n------------
- `tests.test_chafa_externalized.test_ext_tool_retval_some_files_failed_exit_1`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--animate', 'no', '/workspace/tests/data/good/pixel.png', 'missing.foo'], returncode=0, stdout=b'', stderr=b'').returncode

### `empty_list_or_string` — 2 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_basic.test_version_contains_format_loaders`
  > IndexError: list index out of range
- `tests.test_subcommand_dispatch.TestSingleCommandBehavior.test_flag_positioning_typical_of_single_command`
  > IndexError: list index out of range

### `returned_none` — 1 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_usage.test_help_contains_symbols_classes_line`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f7990eaa680>('\\ball\\b', '')
  >  +    where <function search at 0x7f7990eaa680> = re.search

### `rc_mismatch_got2_want1` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_cli_basics.test_some_files_missing_exitcode_1_when_some_missing`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '/workspace/tests/data/good/pixel.png', 'missing.foo', '--animate=no'], returncode=2, stdout=b'', stderr=b'').returncode

