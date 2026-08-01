# Action Sheet — elkowar__pipr.fae0b17

**Current:** 6.74%  (50/742)
**Pass / Fail / Skip:** 50 / 145 / 0
**Gap to 100%:** 93.26 percentage points (692 tests)

## Failure clusters

145 failed tests grouped into 9 buckets (sorted by count).

### `other_assertion` — 100 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_help_flag`
  > AssertionError: assert b'Usage:' in b'bubblewrap installation not found\n'
  >  +  where b'bubblewrap installation not found\n' = CompletedProcess(args=['./executable', '--help'], returncode=0, stdout=b'bubblewrap installation not found\n', stderr=b'').stdout
- `tests.test_basic_invocation.test_config_reference_flag`
  > AssertionError: assert b'# A commandline utility by' in b'bubblewrap installation not found\n'
  >  +  where b'bubblewrap installation not found\n' = CompletedProcess(args=['./executable', '--config-reference'], returncode=0, stdout=b'bubblewrap installation not found\n', stderr=b'').stdout
- `tests.test_basic_invocation.test_config_reference_has_comments`
  > AssertionError: assert b'finish_hook' in b'bubblewrap installation not found\n'
  >  +  where b'bubblewrap installation not found\n' = CompletedProcess(args=['./executable', '--config-reference'], returncode=0, stdout=b'bubblewrap installation not found\n', stderr=b'').stdout
- *(... 97 more in this cluster)*

### `rc_mismatch_got1_want0` — 11 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_file_operations.test_out_file_short_option`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '-o', '/tmp/tmpvyqy2xv2/output.txt', '--help'], returncode=1, stdout=b"error: unexpected argument '-o' found\nError: unexpected argument '-o' found
- `eval.tests.test_argparse_validation.test_options_accept_values_in_multiple_forms_without_error[args0]`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '--default=hi', '--config-reference'], returncode=1, stdout="error: unexpected argument '--config-reference' found\nError: unexpected argu
- `eval.tests.test_argparse_validation.test_options_accept_values_in_multiple_forms_without_error[args1]`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-d=hi', '--config-reference'], returncode=1, stdout="error: unexpected argument '-d=hi' found\nError: unexpected argument '-d=hi' found\n
- *(... 8 more in this cluster)*

### `subprocess_failed` — 10 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_tui_interaction.test_tui_with_enter_key`
  > subprocess.CalledProcessError: Command '['tmux', 'send-keys', '-t', 'pipr_test_enter', 'Enter']' returned non-zero exit status 1.
- `tests.test_tui_interaction.test_tui_text_input`
  > subprocess.CalledProcessError: Command '['tmux', 'send-keys', '-t', 'pipr_test_input', '-l', 'ls -la']' returned non-zero exit status 1.
- `tests.test_tui_interaction.test_tui_ctrl_a_ctrl_e`
  > subprocess.CalledProcessError: Command '['tmux', 'send-keys', '-t', 'pipr_test_nav', 'C-a']' returned non-zero exit status 1.
- *(... 7 more in this cluster)*

### `string_output_mismatch` — 8 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_argparse_validation.test_unknown_long_option_errors_and_exit_code_1`
  > AssertionError: assert 'pipr\n____\n...o-isolation\n' == ''
  >   
  >   + pipr
  >   + ____
  >   + bubblewrap installation not found
  >   + --no-isolation
- `eval.tests.test_argparse_validation.test_missing_required_value_for_option_exits_1_and_reports_which[args0-Argument to option 'default' missing]`
  > AssertionError: assert 'Usage:\n[snippets]\n' == ''
  >   
  >   + Usage:
  >   + [snippets]
- `eval.tests.test_argparse_validation.test_missing_required_value_for_option_exits_1_and_reports_which[args1-Argument to option 'd' missing]`
  > AssertionError: assert '--default\n-...ge:\nUsage:\n' == ''
  >   
  >   + --default
  >   + --default
  >   + text inserted into the textfield
  >   + Usage:
  >   + Usage:
- *(... 5 more in this cluster)*

### `missing_file` — 6 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_file_io_comprehensive.test_in_file_overrides_default`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpi9ugclt5/output.txt'
- `tests.test_file_io_comprehensive.test_raw_mode_preserves_newlines`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmp4fbcl2b4/output.txt'
- `tests.test_file_io_comprehensive.test_normal_mode_joins_lines`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmphef_xtdh/output.txt'
- *(... 3 more in this cluster)*

### `bytes_output_mismatch` — 3 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_basic_invocation.test_help_output_identical`
  > AssertionError: assert b'Usage:\nOpt...n[snippets]\n' == b'bubblewrap ...n not found\n'
  >   
  >   At index 0 diff: b'U' != b'b'
  >   
  >   Full diff:
  >   - (b'bubblewrap installation not found\n')
  >   + (b'Usage:\nOptions:\n--help\nfinish_hook\nparanoid_history_mode_default\naut'
  >   +  b'oeval_mode_default\nhistory_size\ncmd_timeout_millis\nhighlighting_enabled\n'
- `tests.test_cli_comprehensive.test_short_help_flag_equivalent`
  > AssertionError: assert b'Usage:\nOpt...n[snippets]\n' == b'bubblewrap ...n not found\n'
  >   
  >   At index 0 diff: b'U' != b'b'
  >   
  >   Full diff:
  >   - (b'bubblewrap installation not found\n')
  >   + (b'Usage:\nOptions:\n--help\nfinish_hook\nparanoid_history_mode_default\naut'
  >   +  b'oeval_mode_default\nhistory_size\ncmd_timeout_millis\nhighlighting_enabled\n'
- `eval.tests.test_cli_behavior.test_help_exact_match`
  > AssertionError: assert b'Usage:\nOpt...n[snippets]\n' == b'Usage: ./ex...s help menu\n'
  >   
  >   At index 6 diff: b'\n' != b' '
  >   
  >   Full diff:
  >   + (b'Usage:\nOptions:\n--help\nfinish_hook\nparanoid_history_mode_default\naut'
  >   +  b'oeval_mode_default\nhistory_size\ncmd_timeout_millis\nhighlighting_enabled\n'
  >   +  b'[snippets]\n')...

### `rc_unexpected_zero` — 3 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_edge_cases.test_in_file_nonexistent`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '--in-file', '/nonexistent/path/to/file.txt'], returncode=0, stdout=b'--default\n--default\ntext inserted into the textfield\nUsage:\nUsage:\n=\n[\
- `eval.tests.test_cli_behavior.test_unknown_option_errors`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--definitely-not-a-flag'], returncode=0, stdout=b'', stderr=b'').returncode
- `eval.tests.test_cli_behavior.test_without_tty_fails_gracefully[args0]`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--no-isolation'], returncode=0, stdout=b'Usage:\n--no-isolation\neval_environment\ncmd_timeout_millis\n', stderr=b'').returncode

### `boolean_false` — 3 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_file_io_comprehensive.test_in_file_reads_command`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpqbkzjetg/output.txt').exists
- `tests.test_file_io_comprehensive.test_in_and_out_file_together`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmp7j5e3iep/output.txt').exists
- `eval.tests.test_io_behavior.test_config_reference_prints_default_config_to_stdout_only`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of bytes object at 0x7f2162e8c2b0>(b'\n#')
  >  +    where <built-in method startswith of bytes object at 0x7f2162e8c2b0> = b'bubblewrap installation not found\n'.startswith
  >  +      where b'bubblewrap installation not found\n' = CompletedProcess(args=['/workspace/executable', '--config-reference'], returncode=0, stdout=b'bubblewrap installation not found\n', stderr=b'').s

### `rc_mismatch_got0_want1` — 1 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_edge_cases.test_double_dash_separator`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', '--', '--help'], returncode=0, stdout=b'', stderr=b'').returncode

