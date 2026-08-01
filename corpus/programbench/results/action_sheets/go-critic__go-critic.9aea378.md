# Action Sheet — go-critic__go-critic.9aea378

**Current:** 11.37%  (107/941)
**Pass / Fail / Skip:** 107 / 623 / 4
**Gap to 100%:** 88.63 percentage points (834 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_subcommand_dispatch.test_subcommand_help_invocation_is_routed[NOTSET]`
  - reason: got empty parameter set for (subcmd)
- `eval.tests.test_subcommand_dispatch.test_subcommand_help_differs_from_main_help[NOTSET]`
  - reason: got empty parameter set for (subcmd)
- `eval.tests.test_go_critic_check_behavior.test_check_exitcode_flag_controls_exit_status`
  - reason: test_check_exitcode_flag_controls_exit_status depends on test_check_assignop_finds_issue_and_message_exact
- `tests.test_harvest_checkers_batch1.test_checker_positive[codegenComment]`
  - reason: File-level doc comment checker doesn't work with test marker format

## Failure clusters

623 failed tests grouped into 12 buckets (sorted by count).

### `other_assertion` — 208 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_additional_coverage.test_check_with_memprofile_flag`
  > AssertionError: assert 2 in [0, 1]
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'check', '-memprofile', '/tmp/tmppkbw5e2d/mem.prof', '/tmp/tmppkbw5e2d/test.go'], returncode=2, stdout=b'', stderr=b'go-critic: unknown op
- `tests.test_additional_coverage.test_check_with_shorterErrLocation_false`
  > AssertionError: assert 2 in [0, 1]
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'check', '-shorterErrLocation=false', '/tmp/tmpjtomwkfo/test.go'], returncode=2, stdout=b'', stderr=b'go-critic: unknown option: -shorterE
- `tests.test_additional_coverage.test_check_with_experimental_checkers`
  > AssertionError: assert 2 in [0, 1]
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'check', '-enable=#experimental', '/tmp/tmp2mv7qfn9/test.go'], returncode=2, stdout=b'', stderr=b'go-critic: unknown option: -enable=#expe
- *(... 205 more in this cluster)*

### `rc_mismatch_got2_want0` — 127 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_additional_coverage.test_check_with_go_version_flag`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'check', '-go', '1.20', '/tmp/tmpheb0_mkq/test.go'], returncode=2, stdout=b'', stderr=b'go-critic: unknown option: -go\nRun linter checks 
- `tests.test_basic_invocation.test_no_arguments_shows_help`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b'go-critic: a Go source code linter\n\nUsage:\n  go-critic [command] [flags] [files]\n\nCommands:\n  ch
- `tests.test_check_flags.test_verbose_flag`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'check', '-v', '/tmp/tmp_hpbo4v5/test.go'], returncode=2, stdout=b'', stderr=b'go-critic: unknown option: -v\nRun linter checks on Go sour
- *(... 124 more in this cluster)*

### `rc_mismatch_got2_want1` — 111 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_additional_coverage.test_check_builtinShadowDecl_checker`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'check', '-enable=builtinShadowDecl', '/tmp/tmppqt5uy73/test.go'], returncode=2, stdout=b'', stderr=b'go-critic: unknown option: -enable=b
- `tests.test_additional_coverage.test_check_deferInLoop_checker`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'check', '-enable=deferInLoop', '/tmp/tmpks0h_xub/test.go'], returncode=2, stdout=b'', stderr=b'go-critic: unknown option: -enable=deferIn
- `tests.test_check_advanced.TestCheckShorterLocation.test_shorter_err_location_true`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'check', '-shorterErrLocation=true', '/workspace/test_fixtures/append_assign.go'], returncode=2, stdout='', stderr='go-critic: unknown opt
- *(... 108 more in this cluster)*

### `string_output_mismatch` — 83 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_argparse_validation.test_top_level_help_flags_are_treated_as_unknown_commands[argv0-expected_substrings0]`
  > AssertionError: assert 'go-critic 0.... command.\n\n' == ''
  >   
  >   + go-critic 0.1.0
  >   + 
  >   + Usage:
  >   +   go-critic [command] [flags] [files]
  >   + 
  >   + Commands:...
- `eval.tests.test_argparse_validation.test_top_level_help_flags_are_treated_as_unknown_commands[argv1-expected_substrings1]`
  > AssertionError: assert 'go-critic 0.... command.\n\n' == ''
  >   
  >   + go-critic 0.1.0
  >   + 
  >   + Usage:
  >   +   go-critic [command] [flags] [files]
  >   + 
  >   + Commands:...
- `tests.test_exact_output.TestExactOutput.test_help_exact_output`
  > AssertionError: assert 'go-critic 0.... command.\n\n' == 'Usage:\n\n  ...-SNAPSHOT\n\n'
  >   
  >   + go-critic 0.1.0
  >   + 
  >     Usage:
  >   +   go-critic [command] [flags] [files]
  >     
  >   -     go-critic <command> [arguments...]...
- *(... 80 more in this cluster)*

### `rc_mismatch_got0_want1` — 53 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `eval.tests.test_check_io.test_check_lints_go_file_to_stdout_and_nonzero_exit`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'check', '/tmp/pytest-of-root/pytest-0/test_check_lints_go_file_to_st2/bad.go'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_subcommand_dispatch.TestSubcommandHelp.test_check_with_help_flag`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', 'check', '--help'], returncode=0, stdout='Run linter checks on Go source files.\n\nUsage:\n  go-critic check [flags] [files]\n\nFlags:\n  -concurre
- `tests.test_subcommand_dispatch.TestSubcommandArguments.test_doc_with_invalid_checker`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', 'doc', 'nonexistentChecker123'], returncode=0, stdout='', stderr="go-critic: unknown checker: nonexistentChecker123\nRun 'go-critic doc' for a list
- *(... 50 more in this cluster)*

### `rc_unexpected_zero` — 29 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_additional_coverage.test_doc_with_too_many_arguments`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'doc', 'assignOp', 'badCall'], returncode=0, stdout=b'', stderr=b"go-critic: unknown checker: assignOp\nRun 'go-critic doc' for a list of 
- `tests.test_check_basic.test_check_file_with_issue`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'check', '/tmp/tmpxj1kr0g7/bad.go'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_check_basic.test_check_exit_code_on_issues`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'check', '/tmp/tmp7tbgobey/bad.go'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 26 more in this cluster)*

### `bytes_output_mismatch` — 3 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_additional_coverage.test_check_nested_packages`
  > AssertionError: assert (51 == 0 or b'.go:' in b'go-critic: no such file: /tmp/tmpc8cw9y1r/pkg1/...\n')
  >  +  where 51 = len(b'go-critic: no such file: /tmp/tmpc8cw9y1r/pkg1/...\n')
- `tests.test_check_basic.test_check_package_directory`
  > assert (b'' == b''
  >   
  >   Full diff:
  >     b'' and b"go-critic: ...mpttva_xr1'\n" == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b"go-critic: error reading /tmp/tmpttva_xr1: [Errno 21] Is a directory: '/tmp/"
- `tests.test_check_basic.test_check_recursive_all`
  > AssertionError: assert (b'' == b''
  >   
  >   Full diff:
  >     b'' and b'go-critic: ...file: ./...\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'go-critic: no such file: ./...\n'))

### `rc_mismatch_got2_want42` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_check_flags.test_exitCode_custom`
  > AssertionError: assert 2 == 42
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'check', '-exitCode=42', '/tmp/tmp7395y2od/bad.go'], returncode=2, stdout=b'', stderr=b'go-critic: unknown option: -exitCode=42\nRun linte
- `tests.test_check_command.TestCheckFlags.test_custom_exit_code`
  > AssertionError: assert 2 == 42
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'check', '-exitCode=42', '/workspace/test_fixtures/append_assign.go'], returncode=2, stdout='', stderr='go-critic: unknown option: -exitCo
- `tests.test_check_basic.test_custom_exit_code`
  > AssertionError: assert 2 == 42
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'check', '-exitCode=42', '/workspace/eval/test_resources/test_check_basic/unslice_issue.go'], returncode=2, stdout='', stderr='go-critic: 

### `rc_mismatch_got2_want10` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_coverage_boost.test_check_different_exit_codes`
  > AssertionError: assert 2 == 10
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'check', '-exitCode=10', '/tmp/tmp5ht6gqf4/test.go'], returncode=2, stdout=b'', stderr=b'go-critic: unknown option: -exitCode=10\nRun lint
- `tests.test_edge_cases.TestFlagCombinations.test_verbose_with_custom_exit_code`
  > AssertionError: assert 2 == 10
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'check', '-v', '-exitCode=10', '/workspace/test_fixtures/append_assign.go'], returncode=2, stdout='', stderr='go-critic: unknown option: -

### `boolean_false` — 2 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `eval.tests.test_help_version.test_version_prints_version_and_exits_0`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7fbbf4960030>('go-critic version:')
  >  +    where <built-in method startswith of str object at 0x7fbbf4960030> = 'go-critic 0.1.0\n'.startswith
- `tests.test_basic_commands.TestVersionCommand.test_version_output_format`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7f4cda4fc830>('go-critic version:')
  >  +    where <built-in method startswith of str object at 0x7f4cda4fc830> = 'go-critic 0.1.0'.startswith

### `rc_mismatch_got0_want7` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_check_io.test_check_exitcode_flag_controls_exit_status`
  > AssertionError: assert 0 == 7
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'check', '-exitCode', '7', '/tmp/pytest-of-root/pytest-0/test_check_exitcode_flag_contr2/bad.go'], returncode=0, stdout=b'', stderr=b'').r

### `rc_mismatch_got2_want5` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_check_advanced.TestCheckExitCodes.test_custom_exit_code_multiple_issues`
  > AssertionError: assert 2 == 5
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'check', '-exitCode=5', '/workspace/test_fixtures/append_assign.go'], returncode=2, stdout='', stderr='go-critic: unknown option: -exitCod

