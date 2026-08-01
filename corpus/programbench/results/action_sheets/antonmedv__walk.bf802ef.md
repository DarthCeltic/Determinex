# Action Sheet — antonmedv__walk.bf802ef

**Current:** 21.82%  (187/857)
**Pass / Fail / Skip:** 187 / 349 / 1
**Gap to 100%:** 78.18 percentage points (670 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_edge_cases.TestPermissions.test_unreadable_directory`
  - reason: Test requires non-root user

## Failure clusters

349 failed tests grouped into 15 buckets (sorted by count).

### `other_assertion` — 197 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_help_output_contains_all_keybindings`
  > AssertionError: Keybinding b'arrows, hjkl' not found in help
  > assert b'arrows, hjkl' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', '--help'], returncode=0, stdout=b'walk 0.1.0 - bootstrap scaffold\n\nUsage: walk [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print he
- `tests.test_basic_invocation.test_help_output_contains_all_flags`
  > AssertionError: Flag b'--icons' not found in help
  > assert b'--icons' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', '--help'], returncode=0, stdout=b'walk 0.1.0 - bootstrap scaffold\n\nUsage: walk [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print he
- `tests.test_basic_invocation.test_help_output_format`
  > AssertionError: assert 'Move cursor' in ''
- *(... 194 more in this cluster)*

### `rc_mismatch_got0_want1` — 52 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_basic_invocation.test_help_flag`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--help'], returncode=0, stdout=b'walk 0.1.0 - bootstrap scaffold\n\nUsage: walk [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help
- `tests.test_basic_invocation.test_h_flag`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-h'], returncode=0, stdout=b'walk 0.1.0 - bootstrap scaffold\n\nUsage: walk [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  
- `tests.test_error_paths.test_help_flag_first_argument`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--help', 'somepath', '--icons'], returncode=0, stdout=b'walk 0.1.0 - bootstrap scaffold\n\nUsage: walk [OPTIONS] [ARGS]\n\nOptions:\n  -h
- *(... 49 more in this cluster)*

### `string_output_mismatch` — 40 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_argument_parsing.TestVersionFlag.test_version_flags_equivalent`
  > AssertionError: assert 'walk 0.1.0\n' == ''
  >   
  >   + walk 0.1.0
- `tests.test_cli_config.test_icons_flag_enables_icons`
  > AssertionError: assert 'usage: walk ...16:57 2026)\n' == '/workspace/e...115 subdir/\n'
  >   
  >   - /workspace/eval/test_resources/test_cli_config/test_dir
  >   -  .hidden_dir/
  >   -  .hidden_file
  >   -  another_file.md
  >   -  regular_file.txt
  >   -  subdir/...
- `tests.test_cli_config.test_dir_only_flag_shows_only_directories`
  > AssertionError: assert 'walk: unknow...nformation.\n' == '/workspace/e...r/\nsubdir/\n'
  >   
  >   - /workspace/eval/test_resources/test_cli_config/test_dir
  >   - .hidden_dir/
  >   - subdir/
  >   + walk: unknown option: --dir-only
  >   + usage: walk [OPTIONS] [ARGS]
  >   + Try 'walk --help' for more information.
- *(... 37 more in this cluster)*

### `boolean_false` — 17 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_edge_cases.TestOutputFormat.test_version_output_format`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7fc6d92637b0>('v')
  >  +    where <built-in method startswith of str object at 0x7fc6d92637b0> = 'walk 0.1.0'.startswith
- `eval.tests.test_args.test_version_exits_zero_and_prints_version_line[--version]`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7f69846988f0>('v')
  >  +    where <built-in method startswith of str object at 0x7f69846988f0> = 'walk 0.1.0'.startswith
  >  +      where 'walk 0.1.0' = <built-in method strip of str object at 0x7f6984699670>()
  >  +        where <built-in method strip of str object at 0x7f6984699670> = 'walk 0.1.0\n'.strip
  >  +          where 'walk 0.1.0\n' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout='walk 0.1.0\n', stderr='').stdout
- `eval.tests.test_config_env.test_version_prints_and_exits_zero_even_with_other_env_set`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of bytes object at 0x7fa3844d1a70>(b'v')
  >  +    where <built-in method startswith of bytes object at 0x7fa3844d1a70> = b'walk 0.1.0'.startswith
  >  +      where b'walk 0.1.0' = <built-in method strip of bytes object at 0x7fa3844d1f20>()
  >  +        where <built-in method strip of bytes object at 0x7fa3844d1f20> = b'walk 0.1.0\n'.strip
  >  +          where b'walk 0.1.0\n' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'walk 0.1.0\n', stderr=b'').stdout
- *(... 14 more in this cluster)*

### `rc_mismatch_got2_want1` — 10 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_flags.test_multiple_flags_with_help`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--icons', '--dir-only', '--help'], returncode=2, stdout=b'', stderr=b"walk: unknown option: --icons\nusage: walk [OPTIONS] [ARGS]\nTry 'w
- `tests.test_flags.test_help_flag_precedence`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--preview', '--fuzzy', '--icons', '--help'], returncode=2, stdout=b'', stderr=b"walk: unknown option: --preview\nusage: walk [OPTIONS] [A
- `tests.test_basic_invocation.TestFlags.test_icons_flag`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--icons', '--help'], returncode=2, stdout=b'', stderr=b"walk: unknown option: --icons\nusage: walk [OPTIONS] [ARGS]\nTry 'walk --help' fo
- *(... 7 more in this cluster)*

### `rc_mismatch_got2_want0` — 9 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_basic_invocation.test_v_flag`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-v'], returncode=2, stdout=b'', stderr=b"walk: unknown option: -v\nusage: walk [OPTIONS] [ARGS]\nTry 'walk --help' for more information.\
- `tests.test_flags.test_flags_order_independence_with_version`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--icons', '--version'], returncode=2, stdout=b'', stderr=b"walk: unknown option: --icons\nusage: walk [OPTIONS] [ARGS]\nTry 'walk --help'
- `tests.test_basic_invocation.TestHelpAndVersion.test_version_flag_short`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-v'], returncode=2, stdout=b'', stderr=b"walk: unknown option: -v\nusage: walk [OPTIONS] [ARGS]\nTry 'walk --help' for more information.\
- *(... 6 more in this cluster)*

### `rc_unexpected_zero` — 7 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_environment_variables.test_invalid_walk_status_bar_causes_error`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'walk 0.1.0\n', stderr=b'').returncode
- `tests.test_path_arguments.test_nonexistent_path_handling`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/tmp/tmp86pm73ls/does_not_exist'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_status_bar_expressions.test_status_bar_empty_expression_causes_error`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'walk 0.1.0\n', stderr=b'').returncode
- *(... 4 more in this cluster)*

### `empty_list_or_string` — 5 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_help_output.TestExactHelpOutput.test_help_exact_structure`
  > IndexError: list index out of range
- `tests.test_help_output.TestHelpSpecificLines.test_version_line_format`
  > IndexError: list index out of range
- `tests.test_help_output.TestHelpSpecificLines.test_usage_line_format`
  > IndexError: list index out of range
- *(... 2 more in this cluster)*

### `returned_none` — 4 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_basic_invocation.test_version_format`
  > AssertionError: assert None
  >  +  where None = <function match at 0x7f8281702170>(b'v\\d+\\.\\d+\\.\\d+', b'walk 0.1.0')
  >  +    where <function match at 0x7f8281702170> = re.match
  >  +    and   b'walk 0.1.0' = <built-in method strip of bytes object at 0x7f8280aceee0>()
  >  +      where <built-in method strip of bytes object at 0x7f8280aceee0> = b'walk 0.1.0\n'.strip
  >  +        where b'walk 0.1.0\n' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'walk 0.1.0\n', stderr=b'').stdout
- `eval.tests.test_help_usage.test_help_has_walk_header_and_usage_line`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f0108f4a680>('^\\s*walk v', '', flags=re.MULTILINE)
  >  +    where <function search at 0x7f0108f4a680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- `eval.tests.test_help_usage.test_help_has_flags_section_header`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f0108f4a680>('^\\s*Flags:\\s*$', '', flags=re.MULTILINE)
  >  +    where <function search at 0x7f0108f4a680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- *(... 1 more in this cluster)*

### `bytes_output_mismatch` — 2 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_basic_invocation.test_version_flag`
  > AssertionError: assert b'walk 0.1.0' == b'v1.13.0'
  >   
  >   At index 0 diff: b'w' != b'v'
  >   
  >   Full diff:
  >   - (b'v1.13.0')
  >   + (b'walk 0.1.0')
- `tests.test_flags.test_version_flag_precedence`
  > AssertionError: assert b'walk 0.1.0' == b'v1.13.0'
  >   
  >   At index 0 diff: b'w' != b'v'
  >   
  >   Full diff:
  >   - (b'v1.13.0')
  >   + (b'walk 0.1.0')

### `rc_mismatch_got0_want2` — 2 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `eval.tests.test_args.test_extra_positional_args_are_ignored_for_start_path_selection`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'a', 'b'], returncode=0, stdout='', stderr='').returncode
- `tests.test_cli_config.test_walk_status_bar_invalid_expression_panics`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/workspace/eval/test_resources/test_cli_config/test_dir'], returncode=0, stdout='', stderr='').returncode

### `test_timeout` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_go_functions.TestGoUnitTests.test_run_go_tests`
  > subprocess.TimeoutExpired: Command '['go', 'test', '-v']' timed out after 10 seconds

### `rc_mismatch_got1_want0` — 1 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_cli_config.test_walk_status_bar_env_combined_expression`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/tui2cli', '-n', 'test_status_combined', 'start', '--', '/workspace/executable', '/workspace/eval/test_resources/test_cli_config/test_dir'], returncode=

### `rc_mismatch_got1_want27` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_help_output.TestExactHelpOutput.test_help_line_count`
  > AssertionError: assert 1 == 27
  >  +  where 1 = len([''])

### `rc_mismatch_got0_want6` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_help_output.TestHelpAlignment.test_flags_aligned`
  > assert 0 == 6
  >  +  where 0 = len([])

