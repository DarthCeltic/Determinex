# Action Sheet — yassinebridi__serpl.c48a9d7

**Current:** 17.22%  (88/511)
**Pass / Fail / Skip:** 88 / 254 / 0
**Gap to 100%:** 82.78 percentage points (423 tests)

## Failure clusters

254 failed tests grouped into 12 buckets (sorted by count).

### `other_assertion` — 89 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_advanced_scenarios.test_rapid_invocations`
  > AssertionError: assert b'0.3.4' in b'serpl 0.1.0\n'
  >  +  where b'serpl 0.1.0\n' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'serpl 0.1.0\n', stderr=b'').stdout
- `tests.test_advanced_scenarios.test_various_path_formats`
  > assert b'serpl error' in b"serpl: error: unrecognized argument: --project-root\nunexpected argument '-x' found\n"
  >  +  where b"serpl: error: unrecognized argument: --project-root\nunexpected argument '-x' found\n" = CompletedProcess(args=['/workspace/executable', '--project-root', '/tmp/tmpfffot1bn/test'], returnc
- `tests.test_advanced_scenarios.test_help_and_version_alternating`
  > AssertionError: assert b'Usage:' in b'serpl 0.1.0\n\nusage: serpl [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --verbose  Verbose\n  -q, --quiet    
  >  +  where b'serpl 0.1.0\n\nusage: serpl [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --verbose  Verbose\n  -q, --quiet    Quiet\n\n' = CompletedProc
- *(... 86 more in this cluster)*

### `string_output_mismatch` — 55 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_cli.test_help_flag_long`
  > AssertionError: assert 'serpl 0.1.0\...    Quiet\n\n' == 'A simple ter...int version\n'
  >   
  >   - A simple terminal UI for search and replace, ala VS Code
  >   + serpl 0.1.0
  >     
  >   - Usage: executable [OPTIONS]
  >   + usage: serpl [OPTIONS] [ARGS]
  >     ...
- `tests.test_cli.test_help_flag_short`
  > AssertionError: assert 'serpl 0.1.0\...    Quiet\n\n' == 'A simple ter...int version\n'
  >   
  >   - A simple terminal UI for search and replace, ala VS Code
  >   + serpl 0.1.0
  >     
  >   - Usage: executable [OPTIONS]
  >   + usage: serpl [OPTIONS] [ARGS]
  >     ...
- `tests.test_cli.test_version_flag_long`
  > AssertionError: assert 'serpl 0.1.0\n' == 'serpl 0.3.4-...onfig/serpl\n'
  >   
  >   + serpl 0.1.0
  >   - serpl 0.3.4- (<BUILD_DATE>)
  >   - 
  >   - Authors: Yassine Bridi <ybridi@gmail.com>
  >   - 
  >   - Config directory: /root/.config/serpl
- *(... 52 more in this cluster)*

### `rc_mismatch_got1_want5` — 53 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_config.test_minimal_valid_json_config`
  > AssertionError: assert 1 == 5
  >  +  where 1 = len(['serpl 0.1.0'])
- `tests.test_config.test_empty_json_config_uses_defaults`
  > AssertionError: assert 1 == 5
  >  +  where 1 = len(['serpl 0.1.0'])
- `tests.test_config.test_invalid_json_silently_uses_defaults`
  > AssertionError: assert 1 == 5
  >  +  where 1 = len(['serpl 0.1.0'])
- *(... 50 more in this cluster)*

### `missing_file` — 25 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_config_color_edge_cases.TestColorParsingEdgeCases.test_bright_color_parsing`
  > FileNotFoundError: [Errno 2] No such file or directory: './executable'
- `tests.test_config_color_edge_cases.TestColorParsingEdgeCases.test_regular_color_index`
  > FileNotFoundError: [Errno 2] No such file or directory: './executable'
- `tests.test_config_color_edge_cases.TestColorParsingEdgeCases.test_gray_color_parsing`
  > FileNotFoundError: [Errno 2] No such file or directory: './executable'
- *(... 22 more in this cluster)*

### `rc_mismatch_got2_want1` — 17 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli.test_project_root_with_relative_path`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--project-root', 'project'], returncode=2, stdout='', stderr="serpl: error: unrecognized argument: --project-root\nunexpected argument '-
- `tests.test_cli.test_project_root_with_absolute_path`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--project-root', '/tmp/pytest-of-root/pytest-0/test_project_root_with_absolut2/absolute_test'], returncode=2, stdout='', stderr="serpl: e
- `tests.test_cli.test_project_root_with_spaces_in_path`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--project-root', '/tmp/pytest-of-root/pytest-0/test_project_root_with_spaces_2/path with spaces'], returncode=2, stdout='', stderr="serpl
- *(... 14 more in this cluster)*

### `rc_mismatch_got2_want0` — 4 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_cli_edge_cases.test_mixed_flags`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--project-root', '/tmp/tmpy3dc3z58/test'], returncode=2, stdout=b'', stderr=b"serpl: error: unrecognized argument: --project-root\nunexpe
- `eval.tests.test_argparse_validation.test_project_root_accepts_value_forms_and_does_not_block_version[args0]`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--project-root', '/tmp', '--version'], returncode=2, stdout='', stderr="serpl: error: unrecognized argument: --project-root\nunexpected a
- `eval.tests.test_argparse_validation.test_project_root_accepts_value_forms_and_does_not_block_version[args2]`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--project-root=/tmp', '--version'], returncode=2, stdout='', stderr="serpl: error: unrecognized argument: --project-root=/tmp\nunexpected
- *(... 1 more in this cluster)*

### `rc_mismatch_got0_want2` — 3 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `eval.tests.test_argparse_validation.test_invalid_args_exit_2_and_stderr_messages[args2-expected_substrings2]`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-p'], returncode=0, stdout='', stderr='').returncode
- `tests.test_cli.test_short_and_long_project_root_together`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-p', '/tmp/pytest-of-root/pytest-0/test_short_and_long_project_ro2/dir1', '--project-root', '/tmp/pytest-of-root/pytest-0/test_short_and_
- `tests.test_cli.test_case_sensitive_flags`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-v'], returncode=0, stdout='', stderr='').returncode

### `boolean_false` — 2 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_advanced_scenarios.test_concurrent_config_access`
  > assert False
  >  +  where False = all(<generator object test_concurrent_config_access.<locals>.<genexpr> at 0x7f9829abd2a0>)
- `tests.test_basic_invocation.test_version_output_format`
  > assert False

### `rc_mismatch_got0_want1` — 2 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_environment.test_consistent_config_dir_reporting`
  > assert 0 == 1
  >  +  where 0 = len(set())
  >  +    where set() = set([])
- `tests.test_cli.test_project_root_short_flag`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-p', '/tmp/pytest-of-root/pytest-0/test_project_root_short_flag2/short_test'], returncode=0, stdout='', stderr='').returncode

### `bytes_output_mismatch` — 2 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `eval.tests.test_cli_golden.test_help_matches_golden`
  > AssertionError: assert b'serpl 0.1.0...    Quiet\n\n' == b'A simple te...int version\n'
  >   
  >   At index 0 diff: b's' != b'A'
  >   
  >   Full diff:
  >   + (b'serpl 0.1.0\n\nusage: serpl [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help   '
  >   +  b'  Print help\n  -V, --version  Print version\n  -v, --verbose  Verbose\n  -'
  >   +  b'q, --quiet    Quiet\n\n')...
- `eval.tests.test_cli_golden.test_version_matches_golden`
  > AssertionError: assert b'serpl 0.1.0\n' == b'serpl 0.3.4...onfig/serpl\n'
  >   
  >   At index 8 diff: b'1' != b'3'
  >   
  >   Full diff:
  >   + (b'serpl 0.1.0\n')
  >   - (b'serpl 0.3.4- (2026-03-09)\n\nAuthors: Yassine Bridi <ybridi@gmail.com>\n\nCo'
  >   -  b'nfig directory: /root/.config/serpl\n')

### `rc_unexpected_zero` — 1 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_error_handling.test_invalid_short_flag`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-x'], returncode=0, stdout=b'', stderr=b'').returncode

### `rc_mismatch_got1_want0` — 1 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `eval.tests.test_externalized_config_unit_tests.test_ext_parse_style_invalid_does_not_crash_app`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['bash', '-lc', "set -euo pipefail\ntmux kill-session -t exttest_89_83d_px1k 2>/dev/null || true\ntmux new-session -d -s exttest_89_83d_px1k -x 120 -y 40 '/workspac

