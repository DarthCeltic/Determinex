# Action Sheet — cordx56__rustowl.655bc5c

**Current:** 23.18%  (162/699)
**Pass / Fail / Skip:** 162 / 336 / 7
**Gap to 100%:** 76.82 percentage points (537 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_argparse_validation.test_combined_short_flags_rejected[NOTSET]`
  - reason: got empty parameter set for (argv)
- `eval.tests.test_subcommand_dispatch.test_each_subcommand_help_is_recognized[NOTSET]`
  - reason: got empty parameter set for (subcmd)
- `tests.test_check_success.test_check_simple_project`
  - reason: Known bug: check command fails due to cargo metadata parsing issue in Analyzer::new
- `tests.test_check_success.test_check_with_borrowing`
  - reason: Known bug: check command fails due to cargo metadata parsing issue in Analyzer::new
- `tests.test_check_success.test_check_generates_cache`
  - reason: Known bug: check command fails due to cargo metadata parsing issue in Analyzer::new
- *(... 2 more skipped)*

## Failure clusters

336 failed tests grouped into 12 buckets (sorted by count).

### `other_assertion` — 137 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_argparse_validation.test_parse_errors_common[argv0-expected_bits0]`
  > AssertionError: expected stderr for parse/validation error
  > assert ''
  >  +  where '' = RunResult(rc=2, out='Check availability\n\nUsage: executable check [OPTIONS] [path]\n\nArguments:\n  [path]  The path of a file or directory to check availability\n\nOptions:\n      --a
- `eval.tests.test_argparse_validation.test_parse_errors_common[argv1-expected_bits1]`
  > AssertionError: expected stderr for parse/validation error
  > assert ''
  >  +  where '' = RunResult(rc=0, out='', err='').err
- `eval.tests.test_argparse_validation.test_parse_errors_common[argv2-expected_bits2]`
  > AssertionError: expected stderr for parse/validation error
  > assert ''
  >  +  where '' = RunResult(rc=0, out='', err='').err
- *(... 134 more in this cluster)*

### `string_output_mismatch` — 88 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_main.test_dash_h_matches_double_dash_help`
  > AssertionError: assert '' == 'Usage: execu...t directory\n'
  >   
  >   - Usage: executable [OPTIONS] [COMMAND]
  >   - Remove artifacts from the target directory
- `eval.tests.test_subcommand_dispatch.test_help_lists_expected_subcommands`
  > AssertionError: assert [] == ['check', 'cl...ions', 'help']
  >   
  >   Right contains 5 more items, first extra item: 'check'
  >   
  >   Full diff:
  >   + []
  >   - [
  >   -     'check',...
- `tests.test_check.test_check_help_output`
  > AssertionError: assert '' == 'Check availa... Print help\n'
  >   
  >   - Check availability
  >   - 
  >   - Usage: executable check [OPTIONS] [path]
  >   - 
  >   - Arguments:
  >   -   [path]  The path of a file or directory to check availability...
- *(... 85 more in this cluster)*

### `sigpipe_unhandled` — 67 test(s)

**Quick patch ideas:**
- Top of main.py: `import signal; signal.signal(signal.SIGPIPE, signal.SIG_DFL)`

**Sample failures:**

- `tests.test_lsp_analyze.test_single_file_analysis_without_cargo_project`
  > BrokenPipeError: [Errno 32] Broken pipe
- `tests.test_lsp_analyze.test_workspace_path_returns_none_without_metadata`
  > BrokenPipeError: [Errno 32] Broken pipe
- `tests.test_lsp_analyze.test_target_path_method_returns_correct_path`
  > BrokenPipeError: [Errno 32] Broken pipe
- *(... 64 more in this cluster)*

### `rc_mismatch_got0_want2` — 13 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_subcommand_dispatch.TestSubcommandExitCodes.test_missing_required_arg_exit_nonzero`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['./executable', 'completions'], returncode=0, stdout='', stderr='').returncode
- `tests.test_subcommand_dispatch.TestSubcommandExitCodes.test_invalid_argument_exit_nonzero`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['./executable', 'completions', 'invalid_shell'], returncode=0, stdout='[path]\nInstall the toolchain\nUninstall the toolchain\ninstall\n--all-targets\n', stderr=''
- `tests.test_clean_errors.test_invalid_command_error`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'invalid_command'], returncode=0, stdout='RustOwl\nv\nUsage:\nCommands:\n', stderr='').returncode
- *(... 10 more in this cluster)*

### `rc_unexpected_zero` — 10 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_subcommand_dispatch.TestSubcommandRecognition.test_help_subcommand_rejects_help_flag`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'help', '--help'], returncode=0, stdout='--all-targets\n--all-features\nRemove artifacts\ninstall\nuninstall\n--path\n--skip-rustowl-toolchain\n', 
- `tests.test_subcommand_dispatch.TestSubcommandRecognition.test_toolchain_help_rejects_help_flag`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'toolchain', 'help', '--help'], returncode=0, stdout='--all-targets\n--all-features\nRemove artifacts\ninstall\nuninstall\n--path\n--skip-rustowl-t
- `tests.test_subcommand_dispatch.TestUnknownSubcommand.test_unknown_main_subcommand_suggests_help`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'invalid_command'], returncode=0, stdout='RustOwl\nv\nUsage:\nCommands:\n', stderr='').returncode
- *(... 7 more in this cluster)*

### `returned_none` — 6 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_main.test_help_lists_known_commands[check]`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f91c6906680>('^\\s+check\\b', '', flags=re.MULTILINE)
  >  +    where <function search at 0x7f91c6906680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- `eval.tests.test_help_main.test_help_lists_known_commands[clean]`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f91c6906680>('^\\s+clean\\b', '', flags=re.MULTILINE)
  >  +    where <function search at 0x7f91c6906680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- `eval.tests.test_help_main.test_help_lists_known_commands[toolchain]`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f91c6906680>('^\\s+toolchain\\b', '', flags=re.MULTILINE)
  >  +    where <function search at 0x7f91c6906680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- *(... 3 more in this cluster)*

### `boolean_false` — 4 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `eval.tests.test_completions.test_completions_bash_deterministic_and_stderr_empty`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of bytes object at 0x7f29100c4030>(b'_rustowl()')
  >  +    where <built-in method startswith of bytes object at 0x7f29100c4030> = b''.startswith
  >  +      where b'' = CompletedProcess(args=['/workspace/executable', 'completions', 'bash'], returncode=0, stdout=b'', stderr=b'').stdout
- `eval.tests.test_help_main.test_help_has_usage_line`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7f91c6994030>('Usage: executable ')
  >  +    where <built-in method startswith of str object at 0x7f91c6994030> = ''.startswith
- `eval.tests.test_help_main.test_help_ends_with_newline`
  > AssertionError: assert False
  >  +  where False = <built-in method endswith of str object at 0x7f91c6994030>('\n')
  >  +    where <built-in method endswith of str object at 0x7f91c6994030> = ''.endswith
- *(... 1 more in this cluster)*

### `bytes_output_mismatch` — 4 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `eval.tests.test_cli_help_and_version.test_top_level_help_exact`
  > AssertionError: assert b'' == b'Usage: exec... Print help\n'
  >   
  >   Full diff:
  >   + b''
  >   - (b'Usage: executable [OPTIONS] [COMMAND]\n\nCommands:\n  check        Check av'
  >   -  b'ailability\n  clean        Remove artifacts from the target directory\n  t'
  >   -  b'oolchain    Install or uninstall the toolchain\n  completions  Generate s'
  >   -  b'hell completions\n  help         Print this message or the help of the gi'...
- `eval.tests.test_cli_help_and_version.test_subcommand_help_exact_check`
  > AssertionError: assert b'' == b'Check avail... Print help\n'
  >   
  >   Full diff:
  >   + b''
  >   - (b'Check availability\n\nUsage: executable check [OPTIONS] [path]\n\nArguments:'
  >   -  b'\n  [path]  The path of a file or directory to check availability\n\nOption'
  >   -  b's:\n      --all-targets   Run the check for all targets instead of curren'
  >   -  b't only\n      --all-features  Run the check for all features instead of t'
- `eval.tests.test_cli_help_and_version.test_subcommand_help_exact_clean`
  > AssertionError: assert b'' == b'Remove arti... Print help\n'
  >   
  >   Full diff:
  >   + b''
  >   - (b'Remove artifacts from the target directory\n\nUsage: executable clean\n\nOpt'
  >   -  b'ions:\n  -h, --help  Print help\n')
- *(... 1 more in this cluster)*

### `rc_mismatch_got0_want1` — 2 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_check.test_check_combined_flags_without_path_fails`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'check', '--all-targets', '--all-features', '/tmp/pytest-of-root/pytest-0/test_check_combined_flags_with2/empty'], returncode=0, stdout='#
- `tests.test_flag_interactions.test_check_flags_and_path_all_positions_produce_same_result`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'check', '--all-targets', '--all-features', '/tmp/test_proj'], returncode=0, stdout='#compdef rustowl\\n\n--all-features\n--all-targets\n-
  >  +  and   1 = CompletedProcess(args=['/workspace/executable', 'check', '/tmp/test_proj', '--all-targets', '--all-features'], returncode=1, stdout='', stderr='').returncode

### `rc_mismatch_got1_want2` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_check.test_check_with_empty_string_path`
  > AssertionError: assert 1 == 2
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'check', ''], returncode=1, stdout='', stderr='').returncode
- `tests.test_flag_interactions.test_check_empty_path_rejected`
  > AssertionError: assert 1 == 2
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'check', ''], returncode=1, stdout='', stderr='').returncode

### `test_timeout` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_lsp_backend.test_did_open_duplicate_file`
  > TimeoutError: No response received for initialize within 15.0s
- `tests.test_lsp_backend.test_initialize_rooturi_already_in_workspace_folders`
  > TimeoutError: No response received for initialize within 15.0s

### `rc_mismatch_got1_want0` — 1 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `eval.tests.test_subcommand_dispatch.test_check_specific_flags_accepted_with_check`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'check', '--all-targets', '--help'], returncode=1, stdout='', stderr='').returncode

