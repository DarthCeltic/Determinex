# Action Sheet — kyoh86__richgo.313114f

**Current:** 36.32%  (345/950)
**Pass / Fail / Skip:** 345 / 441 / 1
**Gap to 100%:** 63.68 percentage points (605 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_externalized_richgo.test_ext_config_load_invalid_file_read_is_nonfatal`
  - reason: chmod(000) did not cause a read error on this filesystem

## Failure clusters

441 failed tests grouped into 11 buckets (sorted by count).

### `other_assertion` — 220 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.TestBasicInvocation.test_version_command_shows_go_version`
  > AssertionError: assert (b'linux' in b'richgo version 0.1.0\n' or b'darwin' in b'richgo version 0.1.0\n')
- `tests.test_basic_invocation.TestBasicInvocation.test_env_command_passthrough`
  > AssertionError: assert 0 > 0
  >  +  where 0 = len(b'')
- `tests.test_basic_invocation.TestTestFilterMode.test_testfilter_basic_pass`
  > AssertionError: assert b'TestExample' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', 'testfilter'], returncode=0, stdout=b'', stderr=b'').stdout
- *(... 217 more in this cluster)*

### `string_output_mismatch` — 183 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_cli.test_version_command_exact_output`
  > AssertionError: assert 'richgo version 0.1.0\n' == 'go version g...linux/amd64\n'
  >   
  >   - go version go1.21.0 linux/amd64
  >   + richgo version 0.1.0
- `tests.test_cli.test_testfilter_mode_basic_pass`
  > AssertionError: assert '' == '--- FAIL: Te...e\t0.002s\n\n'
  >   
  >   - --- FAIL: TestSampleNG (0.00s)
  >   -     sample_ng_test.go:9: It's not OK... :(
  >   -     --- FAIL: TestSampleNG/SubtestNG (0.00s)
  >   -         sample_ng_test.go:13: It's also not OK... :(
  >   - FAIL
  >   - exit status 1
- `tests.test_cli.test_wrapper_mode_passing_test`
  > AssertionError: assert 'time:2017-01...XXXs\x1b[0m\n' == 'time:2017-01...e\t0.XXXs\n\n'
  >   
  >     time:2017-01-01T01:01:01+09:00
  >   - PASS
  >   + #x1B[90mPASS#x1B[0m
  >   - ok  	github.com/kyoh86/richgo/sample	0.XXXs
  >   + #x1B[32mok  	github.com/kyoh86/richgo/sample	0.XXXs#x1B[0m
  >   ? +++++    	                               	      ++++
- *(... 180 more in this cluster)*

### `bytes_output_mismatch` — 14 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `eval.tests.test_richgo_io.test_testfilter_echoes_stdin_and_appends_blank_line_and_writes_leading_newline_to_stderr`
  > AssertionError: assert b'' == b'PASS\n\n'
  >   
  >   Full diff:
  >   - (b'PASS\n\n')
  >   + b''
- `eval.tests.test_richgo_io.test_testfilter_empty_input_outputs_two_newlines_and_stderr_newline`
  > AssertionError: assert b'' == b'\n'
  >   
  >   Full diff:
  >   - b'\n'
  >   ?   --
  >   + b''
- `tests.test_core.test_version_pass_through`
  > AssertionError: assert b'richgo version 0.1.0\n' == b'go version ...linux/amd64\n'
  >   
  >   At index 0 diff: b'r' != b'g'
  >   
  >   Full diff:
  >   - (b'go version go1.21.0 linux/amd64\n')
  >   + (b'richgo version 0.1.0\n')
- *(... 11 more in this cluster)*

### `rc_mismatch_got2_want0` — 6 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `eval.tests.test_argparse_validation.test_no_args_prints_go_usage_and_exits_success`
  > assert 2 == 0
- `eval.tests.test_argparse_validation.test_testfilter_accepts_unknown_args_and_still_outputs_newline`
  > assert 2 == 0
- `tests.test_subcommand_dispatch.TestSubcommandRouting.test_help_command_routing`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', 'help'], returncode=2, stdout='', stderr='Go is a tool for managing Go source code.\n\nUsage:\n\n\tgo <command> [arguments]\n\nThe commands are:\n\
- *(... 3 more in this cluster)*

### `test_timeout` — 4 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_advanced_config.TestLineRemoval.test_removal_pattern`
  > subprocess.TimeoutExpired: Command '['/workspace/executable', 'test', '.', '-v']' timed out after 5.0 seconds
- `eval.tests.test_argparse_validation.test_test_subcommand_unknown_flag_is_treated_as_package_pattern_and_succeeds_here`
  > subprocess.TimeoutExpired: Command '['/workspace/executable', 'test', '--nonexistent-flag']' timed out after 4 seconds
- `eval.tests.test_argparse_validation.test_double_dash_is_passed_through_to_go_test_and_still_succeeds_here`
  > subprocess.TimeoutExpired: Command '['/workspace/executable', 'test', '--', '--nonexistent-flag']' timed out after 4 seconds
- *(... 1 more in this cluster)*

### `rc_unexpected_zero` — 4 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_edge_cases.test_no_go_mod_directory`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'test'], returncode=0, stdout=b'github.com/example/pkg\nPASS\npkg1\npkg2\n', stderr=b'').returncode
- `tests.test_test_mode.test_test_mode_failing_test`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'test', '-v'], returncode=0, stdout=b'Hex\nRgb\nColors\n', stderr=b'').returncode
- `tests.test_externalized_richgo.test_ext_editor_stream_error_case_via_invalid_removal_regex_panics`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'testfilter'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 1 more in this cluster)*

### `boolean_false` — 4 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_passthrough_commands.test_go_build_passthrough`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpjl58qahn/testmodule').exists
  >  +      where PosixPath('/tmp/tmpjl58qahn/testmodule') = Path('/tmp/tmpjl58qahn', 'testmodule')
- `tests.test_harvest.test_executable_passes_through_unknown_commands`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7f5f3cd616b0>('go version go1.')
  >  +    where <built-in method startswith of str object at 0x7f5f3cd616b0> = 'richgo version 0.1.0\n'.startswith
- `eval.tests.test_argparse_validation.test_go_subcommand_flags_pass_through_and_are_validated_by_go`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7f18bff58030>('{')
  >  +    where <built-in method startswith of str object at 0x7f18bff58030> = ''.startswith
  >  +      where '' = <built-in method strip of str object at 0x7f18bff58030>()
  >  +        where <built-in method strip of str object at 0x7f18bff58030> = ''.strip
- *(... 1 more in this cluster)*

### `returned_none` — 2 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_basic_invocation.test_version_command`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f29d7db3760>(b'go\\d+\\.\\d+', b'richgo version 0.1.0\n')
  >  +    where <function search at 0x7f29d7db3760> = re.search
  >  +    and   b'richgo version 0.1.0\n' = CompletedProcess(args=['/workspace/executable', 'version'], returncode=0, stdout=b'richgo version 0.1.0\n', stderr=b'').stdout
- `eval.tests.test_cli_basics.test_version_format`
  > AssertionError: assert None
  >  +  where None = <function fullmatch at 0x7fa0e6cbbe20>('go version go\\d+\\.\\d+(?:\\.\\d+)? [^\\s]+/[^\\s]+\\n', 'richgo version 0.1.0\n')
  >  +    where <function fullmatch at 0x7fa0e6cbbe20> = re.fullmatch
  >  +    and   'richgo version 0.1.0\n' = CompletedProcess(args=['/workspace/executable', 'version'], returncode=0, stdout='richgo version 0.1.0\n', stderr='').stdout

### `rc_mismatch_got0_want2` — 2 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `eval.tests.test_argparse_validation.test_unknown_top_level_flags_error_from_go[args2]`
  > assert 0 == 2
- `eval.tests.test_argparse_validation.test_go_subcommand_unknown_flag_errors_like_go`
  > assert 0 == 2

### `subprocess_failed` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli.test_help_command_shows_go_help`
  > subprocess.CalledProcessError: Command '['help']' returned non-zero exit status 2.

### `json_output_missing_or_bad` — 1 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `eval.tests.test_env_and_list.test_env_json_is_valid_and_has_keys`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

