# Action Sheet — ismaelgv__rnr.fc0733b

**Current:** 12.97%  (103/794)
**Pass / Fail / Skip:** 103 / 631 / 2
**Gap to 100%:** 87.03 percentage points (691 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_subcommand_dispatch.test_subcommand_help_recognized[NOTSET]`
  - reason: got empty parameter set for (subcmd)
- `tests.test_subcommand_dispatch.test_subcommand_help_differs_from_main_help[NOTSET]`
  - reason: got empty parameter set for (subcmd)

## Failure clusters

631 failed tests grouped into 10 buckets (sorted by count).

### `rc_mismatch_got2_want0` — 399 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_error_handling.test_empty_input_no_files`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'regex', '-f', '-r', 'pattern', 'replacement', '/tmp/tmpsqdojohu/empty'], returncode=2, stdout=b'', stderr=b'Error: Missing required argum
- `tests.test_error_handling.test_special_chars_in_filename`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'regex', '-f', 'file', 'renamed', '/tmp/tmp08grofpq/file with spaces.txt'], returncode=2, stdout=b'', stderr=b'Error: Missing required arg
- `tests.test_error_handling.test_file_with_no_extension`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'regex', '-f', 'file', 'renamed', '/tmp/tmpwn7erzop/file'], returncode=2, stdout=b'', stderr=b'Error: Missing required argument: REPLACEME
- *(... 396 more in this cluster)*

### `other_assertion` — 88 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_no_arguments`
  > AssertionError: assert (b'COMMAND' in b'' or b'COMMAND' in b'Error: Missing required argument: EXPRESSION\nUsage: rnr [OPTIONS] <EXPRESSION> <REPLACEMENT> <PATH(S)>...\n')
  >  +  where b'' = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b'Error: Missing required argument: EXPRESSION\nUsage: rnr [OPTIONS] <EXPRESSION> <REPLACEMENT> <PATH(
  >  +  and   b'Error: Missing required argument: EXPRESSION\nUsage: rnr [OPTIONS] <EXPRESSION> <REPLACEMENT> <PATH(S)>...\n' = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', s
- `tests.test_basic_invocation.test_help_flag`
  > assert b'RnR is a command-line tool' in b"rnr 0.1.0\nRename files and directories using a regular expression\n\nUsage:\n  rnr [OPTIONS] <EXPRESSION> <REPLACEMENT> <PATH(S)>...\n\nCommands:\n  --help, 
  >  +  where b"rnr 0.1.0\nRename files and directories using a regular expression\n\nUsage:\n  rnr [OPTIONS] <EXPRESSION> <REPLACEMENT> <PATH(S)>...\n\nCommands:\n  --help, -h          Show this help mes
- `tests.test_basic_invocation.test_version_flag`
  > AssertionError: assert b'0.5.1' in b'rnr 0.1.0\n'
  >  +  where b'rnr 0.1.0\n' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'rnr 0.1.0\n', stderr=b'').stdout
- *(... 85 more in this cluster)*

### `rc_mismatch_got1_want0` — 85 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_regex_basic.test_simple_rename_dry_run`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'regex', 'file', 'renamed', '/tmp/tmpantaz8df/file-01.txt', '/tmp/tmpantaz8df/file-02.txt'], returncode=1, stdout=b'', stderr=b'Traceback 
- `tests.test_regex.test_regex_dry_run_default`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'regex', 'test', 'renamed', '/tmp/tmpo_uos05n/test-01.txt'], returncode=1, stdout=b'', stderr=b'Traceback (most recent call last):\n  File
- `eval.tests.test_regex_basic.test_regex_dry_run_default_outputs_banner_and_no_fs_change`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'regex', 'foo', 'bar', 'foo.txt'], returncode=1, stdout=b'', stderr=b'Traceback (most recent call last):\n  File "/workspace/main.py", lin
- *(... 82 more in this cluster)*

### `string_output_mismatch` — 23 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_argparse_validation.test_flag_with_value_supports_space_and_equals_forms`
  > AssertionError: assert 'Error: Missi...PATH(S)>...\n' == ''
  >   
  >   + Error: Missing required argument: REPLACEMENT
  >   + Usage: rnr [OPTIONS] <EXPRESSION> <REPLACEMENT> <PATH(S)>...
- `eval.tests.test_argparse_validation.test_flag_after_positionals_is_accepted`
  > assert 'Traceback (m...bscriptable\n' == ''
  >   
  >   + Traceback (most recent call last):
  >   +   File "/workspace/main.py", line 640, in <module>
  >   +     main()
  >   +   File "/workspace/main.py", line 602, in main
  >   +     args.recursive or args['-recursive'], 
  >   + TypeError: 'Namespace' object is not subscriptable
- `eval.tests.test_baseline_snapshots.test_baseline_main_help_exact_match`
  > assert "rnr 0.1.0\nR...md' ./docs/\n" == 'RnR is a com...int version\n'
  >   
  >   - RnR is a command-line tool to rename multiple files and directories that
  >   - supports regular expressions
  >   + rnr 0.1.0
  >   + Rename files and directories using a regular expression
  >     
  >   - ...
- *(... 20 more in this cluster)*

### `rc_mismatch_got2_want1` — 20 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_dumpfile_gaps.test_empty_json_file`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'from-file', '-f', 'empty.json'], returncode=2, stdout='', stderr='Error: Missing required argument: REPLACEMENT\nUsage: rnr [OPTIONS] <EX
- `tests.test_dumpfile_gaps.test_json_missing_date_field`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'from-file', '-f', 'missing_date.json'], returncode=2, stdout='', stderr='Error: Missing required argument: REPLACEMENT\nUsage: rnr [OPTIO
- `tests.test_dumpfile_gaps.test_json_missing_operations_field`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'from-file', '-f', 'missing_operations.json'], returncode=2, stdout='', stderr='Error: Missing required argument: REPLACEMENT\nUsage: rnr 
- *(... 17 more in this cluster)*

### `empty_list_or_string` — 6 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_from_file.test_from_file_backup`
  > IndexError: list index out of range
- `tests.test_from_file.test_from_file_silent`
  > IndexError: list index out of range
- `tests.test_from_file.test_from_file_color_options`
  > IndexError: list index out of range
- *(... 3 more in this cluster)*

### `missing_file` — 5 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_from_file.TestFromFile.test_from_file_dry_run`
  > FileNotFoundError: No dump file found with prefix 'rnr-'
- `tests.test_from_file.TestFromFile.test_from_file_silent`
  > FileNotFoundError: No dump file found with prefix 'rnr-'
- `tests.test_from_file.TestFromFile.test_from_file_backup`
  > FileNotFoundError: No dump file found with prefix 'rnr-'
- *(... 2 more in this cluster)*

### `returned_none` — 2 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_main_help.test_main_help_has_commands_section_and_known_subcommands_listed`
  > assert None
  >  +  where None = <function search at 0x7ff40247e680>('^\\s*regex\\b', "rnr 0.1.0\nRename files and directories using a regular expression\n\nUsage:\n  rnr [OPTIONS] <EXPRESSION> <REPLACEMENT> <PATH(S)
  >  +    where <function search at 0x7ff40247e680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- `eval.tests.test_subcommand_help.test_invalid_subcommand_error_message_and_exit_code`
  > assert None
  >  +  where None = <function search at 0x7ff40247e680>("error: unrecognized subcommand 'bogus'", 'Error: Missing required argument: REPLACEMENT\nUsage: rnr [OPTIONS] <EXPRESSION> <REPLACEMENT> <PATH(S)>
  >  +    where <function search at 0x7ff40247e680> = re.search
  >  +    and   'Error: Missing required argument: REPLACEMENT\nUsage: rnr [OPTIONS] <EXPRESSION> <REPLACEMENT> <PATH(S)>...\n' = RunResult(returncode=2, stdout='', stderr='Error: Missing required argumen

### `rc_unexpected_zero` — 2 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_subcommand_dispatch.test_help_subcommand_does_not_accept_help_flag`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'help', '--help'], returncode=0, stdout="rnr 0.1.0\nRename files and directories using a regular expression\n\nUsage:\n  rnr [OPTIONS] <EX
- `tests.test_subcommand_dispatch.test_subcommand_specific_flag_rejected_globally_before_subcommand`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--color', 'never', 'regex', '--help'], returncode=0, stdout="rnr 0.1.0\nRename files and directories using a regular expression\n\nUsage:

### `rc_mismatch_got0_want1` — 1 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_from_file.TestFromFile.test_undo_then_apply_original`
  > assert 0 == 1
  >  +  where 0 = len([])

