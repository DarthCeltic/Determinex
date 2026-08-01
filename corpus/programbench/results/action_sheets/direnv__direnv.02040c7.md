# Action Sheet — direnv__direnv.02040c7

**Current:** 12.62%  (127/1006)
**Pass / Fail / Skip:** 127 / 497 / 3
**Gap to 100%:** 87.38 percentage points (879 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_subcommand_dispatch.test_subcommand_is_recognized_via_help_subcommand[NOTSET]`
  - reason: got empty parameter set for (subcmd)
- `eval.tests.test_subcommand_dispatch.test_subcommand_help_is_not_identical_to_main_help[NOTSET]`
  - reason: got empty parameter set for (subcmd)
- `tests.test_harvest.test_ruby_layout_scenario`
  - reason: Ruby not available

## Failure clusters

497 failed tests grouped into 16 buckets (sorted by count).

### `other_assertion` — 211 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic.test_help_flag`
  > AssertionError: assert b'direnv v' in b'direnv 2.32.2\nusage: direnv [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --verbose  Verbose\n  -q, --quiet 
  >  +  where b'direnv 2.32.2\nusage: direnv [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --verbose  Verbose\n  -q, --quiet    Quiet\n\n' = CompletedPro
- `tests.test_basic.test_help_command`
  > AssertionError: assert b'direnv v' in b'direnv 2.32.2\nusage: direnv [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --verbose  Verbose\n  -q, --quiet 
  >  +  where b'direnv 2.32.2\nusage: direnv [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --verbose  Verbose\n  -q, --quiet    Quiet\n\n' = CompletedPro
- `tests.test_exec.test_exec_with_dotenv_in_envrc`
  > AssertionError: assert b'env_success' in b'\n'
  >  +  where b'\n' = CompletedProcess(args=['/workspace/executable', 'exec', '/tmp/tmpi4j99nkm', 'sh', '-c', 'echo $ENV_TEST'], returncode=0, stdout=b'\n', stderr=b'').stdout
- *(... 208 more in this cluster)*

### `rc_mismatch_got2_want0` — 126 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_allow.test_allow_current_directory_envrc`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'status'], returncode=2, stdout=b'', stderr=b'direnv: error: unrecognized command: status\n').returncode
- `tests.test_allow.test_allow_alias_permit`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'permit', '/tmp/tmpd3gp6hjd/.envrc'], returncode=2, stdout=b'', stderr=b'direnv: error: unrecognized command: permit\n').returncode
- `tests.test_allow.test_allow_alias_grant`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'grant', '/tmp/tmp0ux5cm4t/.envrc'], returncode=2, stdout=b'', stderr=b'direnv: error: unrecognized command: grant\n').returncode
- *(... 123 more in this cluster)*

### `rc_mismatch_got0_want1` — 37 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_basic.test_version_with_at_least_fail`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'version', '999.0.0'], returncode=0, stdout=b'direnv 2.32.2\n', stderr=b'').returncode
- `eval.tests.test_argparse_validation.test_version_argument_changes_exit_code`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'version', '3.0.0'], returncode=0, stdout='direnv 2.32.2\n', stderr='').returncode
- `eval.tests.test_export_behavior.test_export_json_blocked_envrc_sets_direnv_vars_and_exit1`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'export', 'json'], returncode=0, stdout=b"export export FOO='bar'\n", stderr=b'').returncode
- *(... 34 more in this cluster)*

### `string_output_mismatch` — 34 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_usage.test_dash_h_is_not_help_and_goes_to_stderr_with_color_codes`
  > AssertionError: assert 'direnv 2.32....    Quiet\n\n' == ''
  >   
  >   + direnv 2.32.2
  >   + usage: direnv [OPTIONS] [ARGS]
  >   + 
  >   + Options:
  >   +   -h, --help     Print help
  >   +   -V, --version  Print version...
- `eval.tests.test_cli_basics.test_version_exact_output`
  > AssertionError: assert 'direnv 2.32.2\n' == '2.37.1\n'
  >   
  >   - 2.37.1
  >   + direnv 2.32.2
- `eval.tests.test_status_hook_exec.test_exec_runs_command_with_env_applied`
  > assert "export export FOO='bar'\n" == 'bar'
  >   
  >   - bar
  >   + export export FOO='bar'
- *(... 31 more in this cluster)*

### `rc_mismatch_got1_want0` — 27 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_allow.test_allow_with_envrc_and_dotenv`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'export', 'bash'], returncode=1, stdout=b'\n', stderr=b'').returncode
- `tests.test_dotenv.test_basic_dotenv_loading`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'export', 'bash'], returncode=1, stdout=b'\n', stderr=b'').returncode
- `tests.test_dotenv.test_dotenv_with_comments`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'export', 'bash'], returncode=1, stdout=b'\n', stderr=b'').returncode
- *(... 24 more in this cluster)*

### `rc_mismatch_got2_want1` — 20 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic.test_invalid_command`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'nonexistent_command_xyz'], returncode=2, stdout=b'', stderr=b'direnv: error: unrecognized command: nonexistent_command_xyz\n').returncode
- `eval.tests.test_subcommand_dispatch.test_aliases_are_routed_to_same_command_behavior_for_allow`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'permit', '/workspace/__this_file_should_not_exist__.envrc'], returncode=2, stdout='', stderr='direnv: error: unrecognized command: permit
  >  +  and   1 = CompletedProcess(args=['/workspace/executable', 'allow', '/workspace/__this_file_should_not_exist__.envrc'], returncode=1, stdout='', stderr='direnv: error: file not found: /workspace/__
- `tests.test_dump_check_required.test_dump_unknown_shell_error`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'dump', 'unknown_shell_xyz'], returncode=2, stdout='', stderr='direnv: error: unrecognized command: dump\n').returncode
- *(... 17 more in this cluster)*

### `json_output_missing_or_bad` — 10 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `tests.test_externalized.test_ext_TestEnvDiff_roundtrip_via_export_json_includes_direnv_diff`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_externalized.test_ext_TestIgnoredEnv_via_export_json_omits_ignored_keys`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_externalized.test_ext_TestUpdate_and_roundtrip_via_export_json_has_watches`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- *(... 7 more in this cluster)*

### `returned_none` — 8 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_basic.test_version_command`
  > AssertionError: assert None
  >  +  where None = <function match at 0x7f775ee4e170>(b'^\\d+\\.\\d+\\.\\d+\\s*$', b'direnv 2.32.2\n')
  >  +    where <function match at 0x7f775ee4e170> = re.match
  >  +    and   b'direnv 2.32.2\n' = CompletedProcess(args=['/workspace/executable', 'version'], returncode=0, stdout=b'direnv 2.32.2\n', stderr=b'').stdout
- `eval.tests.test_help_and_version.test_version_prints_semver_like`
  > AssertionError: assert None
  >  +  where None = <function fullmatch at 0x7f7a8f857e20>('\\d+\\.\\d+\\.\\d+', 'direnv 2.32.2')
  >  +    where <function fullmatch at 0x7f7a8f857e20> = re.fullmatch
- `tests.test_externalized.test_ext_TestVersionDotTxt_semver_valid`
  > AssertionError: assert None
  >  +  where None = <function fullmatch at 0x7f97a9d1fe20>('\\d+\\.\\d+\\.\\d+', 'direnv 2.32.2')
  >  +    where <function fullmatch at 0x7f97a9d1fe20> = re.fullmatch
- *(... 5 more in this cluster)*

### `boolean_false` — 8 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_externalized.test_ext_TestEnvDiffEmptyValue_export_bash_includes_empty_assignment`
  > assert False
  >  +  where False = _bash_export_line_present(b"export export FOO=''\n", 'FOO')
  >  +    where b"export export FOO=''\n" = CompletedProcess(args=['/workspace/executable', 'export', 'bash'], returncode=0, stdout=b"export export FOO=''\n", stderr=b'').stdout
- `eval.tests.test_cli_basics.test_help_contains_expected_sections`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7f6e54593d70>('direnv v')
  >  +    where <built-in method startswith of str object at 0x7f6e54593d70> = 'direnv 2.32.2\nusage: direnv [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v
  >  +      where 'direnv 2.32.2\nusage: direnv [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --verbose  Verbose\n  -q, --quiet    Quiet\n\n' = Completed
- `tests.test_dump_check_required.test_deny_removes_allowed_required_files`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/pytest-of-root/pytest-0/test_deny_removes_allowed_requ2/data/direnv/allowed-required').exists
- *(... 5 more in this cluster)*

### `rc_unexpected_zero` — 6 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `eval.tests.test_argparse_validation.test_missing_required_args_errors[argv3-missing COMMAND argument]`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'exec', '/tmp'], returncode=0, stdout='', stderr='').returncode
- `tests.test_subcommand_dispatch.TestExecSubcommand.test_exec_with_directory_no_command`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'exec', '.'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_externalized.test_ext_TestWriter_via_fetchurl_integrity_error`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'fetchurl', 'https://example.com', 'sha256-AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA='], returncode=0, stdout=b'fetched: https://example
- *(... 3 more in this cluster)*

### `rc_mismatch_got127_want0` — 4 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_exec.test_exec_path_modification`
  > assert 127 == 0
  >  +  where 127 = CompletedProcess(args=['/workspace/executable', 'exec', '/tmp/tmp1kzcwm25', 'test_script.sh'], returncode=127, stdout=b"export export PATH='/tmp/tmp1kzcwm25/bin:$PATH'\n", stderr=b'dir
- `tests.test_exec.test_exec_path_modification`
  > assert 127 == 0
  >  +  where 127 = CompletedProcess(args=['/workspace/executable', 'exec', '/tmp/pytest-of-root/pytest-0/test_exec_path_modification2/project', 'mycommand'], returncode=127, stdout="export export PATH='$
- `tests.test_misc_gaps.test_exec_command_found_in_path`
  > assert 127 == 0
  >  +  where 127 = CompletedProcess(args=['/workspace/executable', 'exec', '/tmp/pytest-of-root/pytest-0/test_exec_command_found_in_pat2/project', 'my_cmd'], returncode=127, stdout="export export PATH='/
- *(... 1 more in this cluster)*

### `rc_mismatch_got127_want1` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_exec.test_exec_nonexistent_directory`
  > AssertionError: assert 127 == 1
  >  +  where 127 = CompletedProcess(args=['/workspace/executable', 'exec', '/tmp/nonexistent_xyz_123', 'echo', 'test'], returncode=127, stdout='', stderr='direnv: error: command not found: /tmp/nonexiste
- `tests.test_exec.test_exec_command_not_found`
  > assert 127 == 1
  >  +  where 127 = CompletedProcess(args=['/workspace/executable', 'exec', '/tmp/pytest-of-root/pytest-0/test_exec_command_not_found5/project', 'nonexistent_command_xyz_123'], returncode=127, stdout="exp

### `rc_mismatch_got1_want2` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_subcommand_dispatch.test_aliases_are_routed_to_same_command_behavior_for_block`
  > AssertionError: assert 1 == 2
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'deny', '/workspace/__this_file_should_not_exist__.envrc'], returncode=1, stdout='', stderr='direnv: error: file not found: /workspace/__t
  >  +  and   2 = CompletedProcess(args=['/workspace/executable', 'block', '/workspace/__this_file_should_not_exist__.envrc'], returncode=2, stdout='', stderr='direnv: error: unrecognized command: block\n

### `rc_mismatch_got0_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_allow_deny.test_allow_multiple_different_envrc_files`
  > assert 0 == 3
  >  +  where 0 = len([])

### `rc_mismatch_got4_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_exec.test_exec_with_newlines_in_command_output`
  > assert 4 == 3
  >  +  where 4 = len(["export export TEST='val'", 'line1', 'line2', 'line3'])

### `bytes_output_mismatch` — 1 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_exec.test_exec_with_shell_metacharacters_in_args`
  > AssertionError: assert 'export expor...r baz&qux a;b' == 'foo|bar baz&qux a;b'
  >   
  >   + export export TEST='val'
  >     foo|bar baz&qux a;b

