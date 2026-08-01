# Action Sheet — segmentio__chamber.5f93f5f

**Current:** 19.0%  (379/1995)
**Pass / Fail / Skip:** 379 / 600 / 0
**Gap to 100%:** 81.00 percentage points (1616 tests)

## Failure clusters

600 failed tests grouped into 20 buckets (sorted by count).

### `other_assertion` — 226 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_backend_attempts.TestSSMBackendAttempts.test_ssm_history_attempt`
  > AssertionError: assert b'' != b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', '--backend', 'ssm', 'history', 'testservice', 'testkey'], returncode=0, stdout=b'chamber\nchamber\nchamber\nchamber\n', stderr=b'').stde
- `tests.test_backend_extensive.TestSSMBackendExtensive.test_ssm_tag_write_attempt`
  > AssertionError: assert b'' != b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', '--backend', 'ssm', 'tag', 'write', 'testsvc', 'testkey', 'tag1=value1'], returncode=0, stdout=b'chamber\nchamber\nchamber\nchamber\n', 
- `tests.test_backend_extensive.TestSSMBackendExtensive.test_ssm_tag_read_attempt`
  > AssertionError: assert b'' != b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', '--backend', 'ssm', 'tag', 'read', 'testsvc', 'testkey'], returncode=0, stdout=b'chamber\nchamber\nchamber\nchamber\n', stderr=b'').stde
- *(... 223 more in this cluster)*

### `rc_unexpected_zero` — 120 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_backend_attempts.TestSSMBackendAttempts.test_ssm_write_attempt`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--backend', 'ssm', 'write', 'testservice', 'testkey', 'testvalue'], returncode=0, stdout=b'chamber\nchamber\nchamber\nchamber\n', stderr=
- `tests.test_backend_attempts.TestSSMBackendAttempts.test_ssm_read_attempt`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--backend', 'ssm', 'read', 'testservice', 'testkey'], returncode=0, stdout=b'chamber\nchamber\nchamber\nchamber\n', stderr=b'').returncod
- `tests.test_backend_attempts.TestSSMBackendAttempts.test_ssm_list_attempt`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--backend', 'ssm', 'list', 'testservice'], returncode=0, stdout=b'chamber\nchamber\nchamber\nchamber\n', stderr=b'').returncode
- *(... 117 more in this cluster)*

### `rc_mismatch_got0_want1` — 101 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `eval.tests.test_args.test_env_requires_exactly_one_positional[args0-1-accepts 1 arg]`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'env'], returncode=0, stdout='Print the secrets from the parameter store\nUsage:\nchamber env\n<service>\n--preserve-case\n--escape-string
- `eval.tests.test_args.test_env_requires_exactly_one_positional[args1-1-accepts 1 arg]`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'env', 'svc', 'extra'], returncode=0, stdout='Print the secrets from the parameter store\nUsage:\nchamber env\n<service>\n--preserve-case\
- `eval.tests.test_subcommand_dispatch.test_subcommand_specific_flag_rejected_globally`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--expand'], returncode=0, stdout=b"error: a value is required for '--expand <VALUE>' but none was supplied\nError: a value is required fo
- *(... 98 more in this cluster)*

### `string_output_mismatch` — 76 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_args.test_version_command_ignores_extra_positional_args`
  > AssertionError: assert 'chamber\ndev...es\n--verbose' == 'chamber dev'
  >   
  >   - chamber dev
  >   + chamber
  >   + dev
  >   + CLI for storing secrets
  >   + Usage:
  >   + write a secret...
- `eval.tests.test_args.test_retries_accepts_negative_and_zero[args0]`
  > AssertionError: assert 'chamber\ntest' == 'chamber dev'
  >   
  >   - chamber dev
  >   + chamber
  >   + test
- `eval.tests.test_args.test_retries_accepts_negative_and_zero[args1]`
  > AssertionError: assert 'error: unexp... information.' == 'chamber dev'
  >   
  >   - chamber dev
  >   + error: unexpected argument '-r' found
  >   + Error: unexpected argument '-r' found
  >   + unknown flag: unexpected argument '-r' found
  >   + Unknown flag: unexpected argument '-r' found
  >   + ...
- *(... 73 more in this cluster)*

### `json_output_missing_or_bad` — 21 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `tests.test_coverage_push.TestExportFormatVariations.test_export_json_format_valid_json`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_export_env.TestExportCommand.test_export_json_empty_service`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_export_env.TestExportCommand.test_export_multiple_services`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- *(... 18 more in this cluster)*

### `returned_none` — 12 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_main.test_help_usage_synopsis_mentions_chamber_command`
  > AssertionError: assert None is not None
  >  +  where None = <function search at 0x7f8e8d98e680>('^\\s*chamber \\[command\\]\\s*$', 'CLI for storing secrets\nUsage:\nAvailable Commands:\nwrite\nread\ndelete\nexec\nCLI for storing secrets\nUsage
  >  +    where <function search at 0x7f8e8d98e680> = re.search
  >  +    and   'CLI for storing secrets\nUsage:\nAvailable Commands:\nwrite\nread\ndelete\nexec\nCLI for storing secrets\nUsage:\nAvailable Commands:\n' = CompletedProcess(args=['/workspace/executable', 
  >  +    and   re.MULTILINE = re.M
- `eval.tests.test_help_main.test_main_help_documents_subcommand[completion]`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f8e8d98e680>('^\\s*completion\\s+', 'CLI for storing secrets\nUsage:\nAvailable Commands:\nwrite\nread\ndelete\nexec\nCLI for storing secrets\nUsage:\nAvailable
  >  +    where <function search at 0x7f8e8d98e680> = re.search
  >  +    and   'CLI for storing secrets\nUsage:\nAvailable Commands:\nwrite\nread\ndelete\nexec\nCLI for storing secrets\nUsage:\nAvailable Commands:\n' = CompletedProcess(args=['/workspace/executable', 
  >  +    and   re.MULTILINE = re.M
- `eval.tests.test_help_main.test_main_help_documents_subcommand[env]`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f8e8d98e680>('^\\s*env\\s+', 'CLI for storing secrets\nUsage:\nAvailable Commands:\nwrite\nread\ndelete\nexec\nCLI for storing secrets\nUsage:\nAvailable Comman
  >  +    where <function search at 0x7f8e8d98e680> = re.search
  >  +    and   'CLI for storing secrets\nUsage:\nAvailable Commands:\nwrite\nread\ndelete\nexec\nCLI for storing secrets\nUsage:\nAvailable Commands:\n' = CompletedProcess(args=['/workspace/executable', 
  >  +    and   re.MULTILINE = re.M
- *(... 9 more in this cluster)*

### `boolean_false` — 8 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_cmd_helper_functions.TestOutputFileVariations.test_export_to_output_file`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpba37kjal/output.json').exists
- `tests.test_cmd_helper_functions.TestOutputFileVariations.test_export_yaml_to_file`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmph8sm4rji/output.yaml').exists
- `tests.test_cmd_helper_functions.TestOutputFileVariations.test_export_csv_to_file`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpiqsmryw2/output.csv').exists
- *(... 5 more in this cluster)*

### `rc_mismatch_got7_want0` — 7 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.TestBasicInvocation.test_no_arguments_shows_help`
  > AssertionError: assert 7 == 0
  >  +  where 7 = CompletedProcess(args=['/workspace/executable'], returncode=7, stdout=b'', stderr=b'error: cannot connect to http://127.0.0.1:8080/: <urlopen error [Errno 111] Connection refused>\n').re
- `tests.test_basic_invocation_old.TestBasicInvocation.test_no_arguments_shows_help`
  > AssertionError: assert 7 == 0
  >  +  where 7 = CompletedProcess(args=['/workspace/executable'], returncode=7, stdout=b'', stderr=b'error: cannot connect to http://127.0.0.1:8080/: <urlopen error [Errno 111] Connection refused>\n').re
- `eval.tests.test_args.test_retries_accepts_negative_and_zero[args2]`
  > AssertionError: assert 7 == 0
  >  +  where 7 = CompletedProcess(args=['/workspace/executable', '--retries=10', 'version'], returncode=7, stdout='', stderr='error: cannot connect to http://127.0.0.1:8080/: <urlopen error [Errno 111] C
- *(... 4 more in this cluster)*

### `bytes_output_mismatch` — 7 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_cmd_helper_functions.TestEnvHelperFunctions.test_env_escape_strings_triggers_double_quote_escape`
  > AssertionError: assert b'Service\nService\ntest\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'Service\nService\ntest\n')
- `tests.test_coverage_improvements.TestEnvCommandAdvanced.test_env_with_null_backend_empty`
  > AssertionError: assert b'Service\nService\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'Service\nService\n')
- `tests.test_coverage_improvements.TestEnvCommandAdvanced.test_env_escape_strings_flag`
  > AssertionError: assert b',\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + b',\n'
- *(... 4 more in this cluster)*

### `uncategorized` — 7 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_coverage_push.TestExportFormatVariations.test_export_yaml_format_valid_yaml`
  > yaml.scanner.ScannerError: mapping values are not allowed here
  >   in "<unicode string>", line 2, column 6:
  >     Usage:
  >          ^
- `eval.tests.test_help_main.test_help_lists_available_commands_section`
  > ValueError: substring not found
- `tests.test_environ.TestEnvironLoadStrictWithBackend.test_load_strict_substitutes_sentinel_values_from_backend`
  > OSError: [Errno 98] Address already in use
- *(... 4 more in this cluster)*

### `missing_file` — 5 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_backend_gap_demonstration.test_write_tags_on_existing_secret_error_path`
  > FileNotFoundError: [Errno 2] No such file or directory: './executable'
- `tests.test_backend_gap_demonstration.test_kms_key_alias_without_prefix`
  > FileNotFoundError: [Errno 2] No such file or directory: './executable'
- `tests.test_backend_gap_proof_final.TestS3NotImplementedFeatures.test_s3_write_with_tags_error`
  > FileNotFoundError: [Errno 2] No such file or directory: './executable'
- *(... 2 more in this cluster)*

### `rc_mismatch_got7_want1` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_subcommand_dispatch.test_unknown_subcommand_errors_and_mentions_unknown`
  > AssertionError: assert 7 == 1
  >  +  where 7 = CompletedProcess(args=['/workspace/executable', 'does-not-exist'], returncode=7, stdout=b'', stderr=b'error: cannot connect to http://127.0.0.1:8080/: <urlopen error [Errno 111] Connecti
- `tests.test_detailed_output.TestErrorMessages.test_unknown_command_error_format`
  > assert 7 == 1

### `rc_mismatch_got0_want2` — 1 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_comprehensive.TestExitCodePropagation.test_exec_exit_2`
  > assert 0 == 2

### `rc_mismatch_got10_want1` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_detailed_output.TestExactOutputs.test_version_output_exact`
  > AssertionError: assert 10 == 1
  >  +  where 10 = len(['chamber', 'dev', 'CLI for storing secrets', 'Usage:', 'write a secret', 'Usage:', ...])

### `empty_list_or_string` — 1 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `eval.tests.test_chamber_cli.test_null_backend_list_header_for_service`
  > IndexError: list index out of range

### `rc_mismatch_got0_want42` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_exec.test_exec_propagates_exit_code_failure`
  > AssertionError: assert 0 == 42
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'exec', 'myservice', '--', '/bin/sh', '-c', 'exit 42'], returncode=0, stdout='ok\n', stderr='').returncode

### `rc_mismatch_got1_want0` — 1 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_exec.test_exec_strict_custom_value_ignores_default`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'exec', '--strict', '--strict-value', 'MYVALUE', 'myservice', '--', 'env'], returncode=1, stdout='error\n', stderr='').returncode

### `rc_mismatch_got1_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_exec.test_exec_complex_command_with_multiple_statements`
  > AssertionError: assert 1 == 3
  >  +  where 1 = len(['ok'])

### `rc_mismatch_got0_want5` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_exec.test_exec_command_with_exit_in_middle`
  > AssertionError: assert 0 == 5
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'exec', 'myservice', '--', '/bin/sh', '-c', 'echo before; exit 5; echo after'], returncode=0, stdout='ok\n', stderr='').returncode

### `rc_mismatch_got1_want1000` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_exec.test_exec_command_with_long_output`
  > AssertionError: assert 1 == 1000
  >  +  where 1 = len(['ok'])

