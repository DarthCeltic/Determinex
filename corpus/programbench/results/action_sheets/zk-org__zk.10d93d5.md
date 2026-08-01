# Action Sheet — zk-org__zk.10d93d5

**Current:** 2.03%  (27/1331)
**Pass / Fail / Skip:** 27 / 411 / 15
**Gap to 100%:** 97.97 percentage points (1304 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_subcommand_dispatch.test_each_subcommand_help_succeeds[NOTSET]`
  - reason: got empty parameter set for (subcmd)
- `eval.tests.test_subcommand_dispatch.test_subcommand_help_differs_from_main_help[NOTSET]`
  - reason: got empty parameter set for (subcmd)
- `tests.test_database_errors.test_fts5_required_for_initialization`
  - reason: gold-env-limitation: Gold executable lacks FTS5, but FTS5 is REQUIRED per infra.md for actual binary under test
- `tests.test_database_errors.test_database_schema_version_correct`
  - reason: gold-env-limitation: Requires init which needs FTS5
- `tests.test_harvest.test_tesh_scenario[cmd-edit_scenario_1]`
  - reason: Requires TTY (/dev/tty) for editor interaction
- *(... 10 more skipped)*

## Failure clusters

411 failed tests grouped into 12 buckets (sorted by count).

### `other_assertion` — 269 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_help_flag`
  > AssertionError: assert b'Usage: zk <command>' in b'zk 0.1.0 - bootstrap scaffold\n\nUsage: zk [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n'
  >  +  where b'zk 0.1.0 - bootstrap scaffold\n\nUsage: zk [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['/workspace/executable', '-
- `tests.test_edit_command.test_edit_help`
  > AssertionError: assert b'Usage: zk edit' in b'zk 0.1.0 - bootstrap scaffold\n\nUsage: zk [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n'
  >  +  where b'zk 0.1.0 - bootstrap scaffold\n\nUsage: zk [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['/workspace/executable', 'e
- `tests.test_error_handling.test_new_without_notebook`
  > assert (b'notebook' in b"zk: unknown option: --print-path\nusage: zk [options] [args]\ntry 'zk --help' for more information.\n" or b'error' in b"zk: unknown option: --print-path\nusage: zk [options] [
  >  +  where b"zk: unknown option: --print-path\nusage: zk [options] [args]\ntry 'zk --help' for more information.\n" = <built-in method lower of bytes object at 0x7f3efc8f3ab0>()
  >  +    where <built-in method lower of bytes object at 0x7f3efc8f3ab0> = b"zk: unknown option: --print-path\nusage: zk [OPTIONS] [ARGS]\nTry 'zk --help' for more information.\n".lower
  >  +      where b"zk: unknown option: --print-path\nusage: zk [OPTIONS] [ARGS]\nTry 'zk --help' for more information.\n" = CompletedProcess(args=['/workspace/executable', 'new', '--title', 'Test', '--pr
  >  +  and   b"zk: unknown option: --print-path\nusage: zk [options] [args]\ntry 'zk --help' for more information.\n" = <built-in method lower of bytes object at 0x7f3efc8f3ab0>()
  >  +    where <built-in method lower of bytes object at 0x7f3efc8f3ab0> = b"zk: unknown option: --print-path\nusage: zk [OPTIONS] [ARGS]\nTry 'zk --help' for more information.\n".lower
  >  +      where b"zk: unknown option: --print-path\nusage: zk [OPTIONS] [ARGS]\nTry 'zk --help' for more information.\n" = CompletedProcess(args=['/workspace/executable', 'new', '--title', 'Test', '--pr
- *(... 266 more in this cluster)*

### `subprocess_failed` — 59 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_core_coverage.test_template_parse_error_unclosed_expression`
  > subprocess.CalledProcessError: Command '['/workspace/executable', 'init', '--no-input', '/tmp/pytest-of-root/pytest-0/test_template_parse_error_uncl2/test_notebook']' returned non-zero exit status 2.
- `tests.test_core_coverage.test_template_not_found_error`
  > subprocess.CalledProcessError: Command '['/workspace/executable', 'init', '--no-input', '/tmp/pytest-of-root/pytest-0/test_template_not_found_error2/test_notebook']' returned non-zero exit status 2.
- `tests.test_core_coverage.test_template_unclosed_block_helper`
  > subprocess.CalledProcessError: Command '['/workspace/executable', 'init', '--no-input', '/tmp/pytest-of-root/pytest-0/test_template_unclosed_block_h2/test_notebook']' returned non-zero exit status 2.
- *(... 56 more in this cluster)*

### `rc_mismatch_got2_want0` — 31 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_basic_invocation.test_no_args_shows_help`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b"usage: zk [OPTIONS] [ARGS]\nTry 'zk --help' for more information.\n").returncode
- `tests.test_error_handling.test_missing_required_format_for_graph`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'init', '--no-input', '/tmp/tmpnn0wroe5'], returncode=2, stdout=b'', stderr=b"zk: unknown option: --no-input\nusage: zk [OPTIONS] [ARGS]\n
- `tests.test_global_flags.test_notebook_dir_flag`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'init', '--no-input', '/tmp/tmpqz_c081s/notebook'], returncode=2, stdout=b'', stderr=b"zk: unknown option: --no-input\nusage: zk [OPTIONS]
- *(... 28 more in this cluster)*

### `string_output_mismatch` — 13 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_main.test_help_usage_line`
  > AssertionError: assert 'zk 0.1.0 - b...trap scaffold' == 'Usage: zk <command>'
  >   
  >   - Usage: zk <command>
  >   + zk 0.1.0 - bootstrap scaffold
- `eval.tests.test_help_subcommands.test_subcommand_help_usage_line[init-Usage: zk init [<directory>]]`
  > AssertionError: assert 'zk 0.1.0 - b...trap scaffold' == 'Usage: zk init [<directory>]'
  >   
  >   - Usage: zk init [<directory>]
  >   + zk 0.1.0 - bootstrap scaffold
- `eval.tests.test_help_subcommands.test_subcommand_help_usage_line[index-Usage: zk index]`
  > AssertionError: assert 'zk 0.1.0 - b...trap scaffold' == 'Usage: zk index'
  >   
  >   - Usage: zk index
  >   + zk 0.1.0 - bootstrap scaffold
- *(... 10 more in this cluster)*

### `rc_unexpected_zero` — 10 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_basic_invocation.test_invalid_command`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'invalid-command'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_error_handling.test_command_without_notebook`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'list'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_error_handling.test_invalid_date_format`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'list', '--created-after', 'invalid-date'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 7 more in this cluster)*

### `rc_mismatch_got2_want1` — 8 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_argparse_validation.test_flag_ordering_and_equal_syntax_are_accepted[argv0]`
  > assert 2 == 1
  >  +  where 2 = RunResult(code=2, out='', err="zk: unknown option: --notebook-dir\nusage: zk [OPTIONS] [ARGS]\nTry 'zk --help' for more information.\n").code
- `eval.tests.test_argparse_validation.test_flag_ordering_and_equal_syntax_are_accepted[argv1]`
  > assert 2 == 1
  >  +  where 2 = RunResult(code=2, out='', err="zk: unknown option: --notebook-dir\nusage: zk [OPTIONS] [ARGS]\nTry 'zk --help' for more information.\n").code
- `eval.tests.test_argparse_validation.test_flag_ordering_and_equal_syntax_are_accepted[argv2]`
  > assert 2 == 1
  >  +  where 2 = RunResult(code=2, out='', err="zk: unknown option: --notebook-dir=/tmp\nusage: zk [OPTIONS] [ARGS]\nTry 'zk --help' for more information.\n").code
- *(... 5 more in this cluster)*

### `boolean_false` — 8 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `eval.tests.test_subcommand_help.test_subcommand_help_exact[init-init_help.txt-Usage: zk init [<directory>]]`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7f9a12c9a1e0>(('Usage: zk init [<directory>]' + '\n'))
  >  +    where <built-in method startswith of str object at 0x7f9a12c9a1e0> = 'zk 0.1.0 - bootstrap scaffold\n\nUsage: zk [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print
  >  +      where 'zk 0.1.0 - bootstrap scaffold\n\nUsage: zk [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = RunResult(returncode=0, stdout='zk 0.1.0 - boot
- `eval.tests.test_subcommand_help.test_subcommand_help_exact[index-index_help.txt-Usage: zk index]`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7f9a12c9b680>(('Usage: zk index' + '\n'))
  >  +    where <built-in method startswith of str object at 0x7f9a12c9b680> = 'zk 0.1.0 - bootstrap scaffold\n\nUsage: zk [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print
  >  +      where 'zk 0.1.0 - bootstrap scaffold\n\nUsage: zk [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = RunResult(returncode=0, stdout='zk 0.1.0 - boot
- `eval.tests.test_subcommand_help.test_subcommand_help_exact[new-new_help.txt-Usage: zk new [<directory>]]`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7f9a12ca8920>(('Usage: zk new [<directory>]' + '\n'))
  >  +    where <built-in method startswith of str object at 0x7f9a12ca8920> = 'zk 0.1.0 - bootstrap scaffold\n\nUsage: zk [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print
  >  +      where 'zk 0.1.0 - bootstrap scaffold\n\nUsage: zk [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = RunResult(returncode=0, stdout='zk 0.1.0 - boot
- *(... 5 more in this cluster)*

### `rc_mismatch_got0_want1` — 7 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `eval.tests.test_argparse_validation.test_double_dash_stops_flag_parsing_unknown_flag_after_is_positional`
  > AssertionError: assert 0 == 1
  >  +  where 0 = RunResult(code=0, out='', err='').code
- `eval.tests.test_argparse_validation.test_graph_accepts_multiple_positionals_after_required_flags`
  > AssertionError: assert 0 == 1
  >  +  where 0 = RunResult(code=0, out='', err='').code
- `eval.tests.test_help_main.test_double_dash_separator_makes_help_be_treated_as_argument_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--', '--help'], returncode=0, stdout='', stderr='').returncode
- *(... 4 more in this cluster)*

### `returned_none` — 3 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_main.test_help_has_group_headings[NOTEBOOK]`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f38b94b6680>('^\\s*NOTEBOOK\\s*$', 'zk 0.1.0 - bootstrap scaffold\n\nUsage: zk [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print
  >  +    where <function search at 0x7f38b94b6680> = re.search
  >  +    and   re.MULTILINE = re.M
- `eval.tests.test_help_main.test_help_has_group_headings[NOTES]`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f38b94b6680>('^\\s*NOTES\\s*$', 'zk 0.1.0 - bootstrap scaffold\n\nUsage: zk [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print ve
  >  +    where <function search at 0x7f38b94b6680> = re.search
  >  +    and   re.MULTILINE = re.M
- `eval.tests.test_init_io_and_exit_codes.test_init_on_existing_notebook_exits_0_and_prints_error_on_stderr`
  > assert None
  >  +  where None = <function search at 0x7fc7d56ea680>('init: a notebook already exists', "zk: unknown option: --no-input\nusage: zk [OPTIONS] [ARGS]\nTry 'zk --help' for more information.\n")
  >  +    where <function search at 0x7fc7d56ea680> = re.search

### `rc_mismatch_got14_want5` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_edit.test_edit_sort_parameter`
  > AssertionError: assert 14 == 5
  >  +  where 14 = len(['zk:', 'unknown', 'option:', '--no-input', 'usage:', 'zk', ...])

### `rc_mismatch_got14_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_edit.test_edit_with_working_dir_flag`
  > AssertionError: assert 14 == 3
  >  +  where 14 = len(['zk:', 'unknown', 'option:', '-W', 'usage:', 'zk', ...])

### `rc_mismatch_got14_want2` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_edit.test_edit_with_notebook_dir_flag`
  > AssertionError: assert 14 == 2
  >  +  where 14 = len(['zk:', 'unknown', 'option:', '--notebook-dir', 'usage:', 'zk', ...])

