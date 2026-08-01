# Action Sheet — incu6us__goimports-reviser.81bd549

**Current:** 4.95%  (37/747)
**Pass / Fail / Skip:** 37 / 557 / 3
**Gap to 100%:** 95.05 percentage points (710 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_formatting_behavior.test_output_write_modifies_file`
  - reason: test_output_write_modifies_file depends on test_output_stdout_does_not_modify_file
- `eval.tests.test_formatting_behavior.test_list_diff_and_set_exit_status`
  - reason: test_list_diff_and_set_exit_status depends on test_output_write_modifies_file
- `tests.test_externalized.test_ext_is_terminal_behavior`
  - reason: Internal tests for isTerminal() are not reliably externalizable via a non-interactive CLI.

## Failure clusters

557 failed tests grouped into 8 buckets (sorted by count).

### `other_assertion` — 270 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_additional_coverage.test_cgo_import_handling`
  > AssertionError: assert 2 in [0, 1]
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-output', 'stdout', '/tmp/tmpgio8pil2/test.go'], returncode=2, stdout=b'', stderr=b'goimports-reviser: error: unrecognized argument: -u\n
- `tests.test_additional_coverage.test_imports_with_trailing_comma`
  > AssertionError: assert 2 in [0, 1]
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-output', 'stdout', '/tmp/tmp99mlhubb/test.go'], returncode=2, stdout=b'', stderr=b'goimports-reviser: error: unrecognized argument: -u\n
- `tests.test_basic_invocation.test_help_flag`
  > AssertionError: assert b'Usage of' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', '--help'], returncode=0, stdout=b'goimports-reviser 0.1.0\n\nusage: goimports-reviser [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Pri
- *(... 267 more in this cluster)*

### `rc_mismatch_got2_want0` — 249 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_additional_coverage.test_project_name_auto_detection`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-output', 'stdout', '/tmp/tmpmjmwryaw/main.go'], returncode=2, stdout=b'', stderr=b'goimports-reviser: error: unrecognized argument: -u\n
- `tests.test_additional_coverage.test_multiple_files_same_package`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-output', 'stdout', '/tmp/tmpnu0tjvr2/file1.go', '/tmp/tmpnu0tjvr2/file2.go'], returncode=2, stdout=b'', stderr=b'goimports-reviser: erro
- `tests.test_additional_coverage.test_file_with_no_package_import_section`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-output', 'stdout', '/tmp/tmpeeta0gm3/test.go'], returncode=2, stdout=b'', stderr=b'goimports-reviser: error: unrecognized argument: -u\n
- *(... 246 more in this cluster)*

### `rc_mismatch_got2_want1` — 28 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_no_arguments_shows_help`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b'usage: goimports-reviser [OPTIONS] [ARGS]\n').returncode
- `tests.test_error_handling.test_malformed_go_file`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-output', 'stdout', '/tmp/tmpasi9hpx_/test.go'], returncode=2, stdout=b'', stderr=b'goimports-reviser: error: unrecognized argument: -u\n
- `tests.test_error_handling.test_missing_package_declaration`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-output', 'stdout', '/tmp/tmpdr9ra6ij/test.go'], returncode=2, stdout=b'', stderr=b'goimports-reviser: error: unrecognized argument: -u\n
- *(... 25 more in this cluster)*

### `rc_mismatch_got1_want0` — 3 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_error_conditions.test_directory_with_no_go_files`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '/tmp/tmprx5m38zs/emptydir'], returncode=1, stdout=b'', stderr=b'goimports-reviser: error: not a file: /tmp/tmprx5m38zs/emptydir\n').retur
- `tests.test_file_operations.test_directory_without_recursive_flag`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '/tmp/tmpjaga78ar/testdir'], returncode=1, stdout=b'', stderr=b'goimports-reviser: error: not a file: /tmp/tmpjaga78ar/testdir\n').returnc
- `tests.test_file_operations.test_dotdotdot_pattern_recursive`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', './...'], returncode=1, stdout=b'', stderr=b'goimports-reviser: error: no such file or directory: ./...\n').returncode

### `string_output_mismatch` — 3 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_baseline.test_help_stderr_matches_baseline_fixture_normalized`
  > AssertionError: assert 'goimports-re...  Show help\n' == ''
  >   
  >   + goimports-reviser 0.1.0
  >   + 
  >   + usage: goimports-reviser [OPTIONS] [ARGS]
  >   + 
  >   + Options:
  >   +   -h, --help     Print help...
- `eval.tests.test_cli_meta.test_help_snapshot`
  > AssertionError: assert 'goimports-re...  Show help\n' == 'Usage of /wo...sion string\n'
  >   
  >   + goimports-reviser 0.1.0
  >   + 
  >   + usage: goimports-reviser [OPTIONS] [ARGS]
  >   + 
  >   + Options:
  >   +   -h, --help     Print help...
- `tests.test_cli.test_help_flag_displays_usage`
  > AssertionError: assert 'goimports-re...  Show help\n' == 'Usage of ./e...sion string\n'
  >   
  >   + goimports-reviser 0.1.0
  >   + 
  >   + usage: goimports-reviser [OPTIONS] [ARGS]
  >   + 
  >   + Options:
  >   +   -h, --help     Print help...

### `rc_unexpected_zero` — 2 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `eval.tests.test_args_parsing.test_flags_after_positional_are_not_parsed_as_flags`
  > assert 2 != 2
- `tests.test_subcommands.TestNoSubcommandHelp.test_subcommand_help_not_valid`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'add', '--help'], returncode=0, stdout=b'goimports-reviser 0.1.0\n\nusage: goimports-reviser [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help   

### `returned_none` — 1 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_usage.test_help_documents_output_default`
  > assert None
  >  +  where None = <function search at 0x7f6814642680>('\\(default \\"file\\"\\)', 'goimports-reviser 0.1.0\n\nusage: goimports-reviser [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, -
  >  +    where <function search at 0x7f6814642680> = re.search

### `rc_mismatch_got0_want1` — 1 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_cli.test_missing_go_mod_shows_clear_error`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/tmp/tmpa2ef8e2l/test.go'], returncode=0, stdout='package main\nimport "fmt"\nfunc main() {}\n\n', stderr='').returncode

