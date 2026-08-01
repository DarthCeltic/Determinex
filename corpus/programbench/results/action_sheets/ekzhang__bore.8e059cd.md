# Action Sheet — ekzhang__bore.8e059cd

**Current:** 9.97%  (63/632)
**Pass / Fail / Skip:** 63 / 296 / 0
**Gap to 100%:** 90.03 percentage points (569 tests)

## Failure clusters

296 failed tests grouped into 11 buckets (sorted by count).

### `other_assertion` — 122 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_help_subcommands.test_local_help_documents_required_args_and_key_flags`
  > assert '--local-host' in "error: the following required arguments were not provided:\n  --to <TO>\n  <LOCAL_PORT>\n\nUsage: executable local --to <TO> <LOCAL_PORT>\n\nFor more information, try '--help
- `eval.tests.test_cli_io.test_subcommand_help_local_contains_env_hints_and_defaults`
  > assert '[env: BORE_LOCAL_PORT' in "error: the following required arguments were not provided:\n  --to <TO>\n  <LOCAL_PORT>\n\nUsage: executable local --to <TO> <LOCAL_PORT>\n\nFor more information, tr
- `eval.tests.test_cli_io.test_local_missing_required_to_flag_is_usage_error_exit_2`
  > AssertionError: assert '--to' in ''
- *(... 119 more in this cluster)*

### `string_output_mismatch` — 78 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_args_parsing.test_local_missing_required_args[args0-needles0]`
  > assert "error: inval...y '--help'.\n" == ''
  >   
  >   + error: invalid value '99999' for '--port <PORT>': 99999 is not in 0..=65535
  >   + 
  >   + For more information, try '--help'.
- `eval.tests.test_args_parsing.test_local_missing_required_args[args1-needles1]`
  > assert "error: inval...y '--help'.\n" == ''
  >   
  >   + error: invalid value '99999' for '--port <PORT>': 99999 is not in 0..=65535
  >   + 
  >   + For more information, try '--help'.
- `eval.tests.test_args_parsing.test_local_missing_option_values[args1-needles1]`
  > assert "error: inval...y '--help'.\n" == ''
  >   
  >   + error: invalid value '99999' for '--port <PORT>': 99999 is not in 0..=65535
  >   + 
  >   + For more information, try '--help'.
- *(... 75 more in this cluster)*

### `uncategorized` — 52 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_harvest.test_very_long_frame`
  > ConnectionRefusedError: [Errno 111] Connection refused
- `tests.test_protocol.test_oversized_frame_rejected`
  > ConnectionRefusedError: [Errno 111] Connection refused
- `tests.test_protocol.test_malformed_json_closes_connection`
  > ConnectionRefusedError: [Errno 111] Connection refused
- *(... 49 more in this cluster)*

### `returned_none` — 12 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_subcommands.test_local_help_has_usage_and_arguments_section`
  > assert None
  >  +  where None = <function search at 0x7f043c52e680>('^Arguments:\\s*$', "error: the following required arguments were not provided:\n  --to <TO>\n  <LOCAL_PORT>\n\nUsage: executable local --to <TO> <
  >  +    where <function search at 0x7f043c52e680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- `tests.test_all.test_proxy_and_auth_and_range`
  > assert None is not None
- `tests.test_client_gaps.test_client_connection_proxies_data_bidirectionally`
  > assert None is not None
  >  +  where None = <test_client_gaps.ClientProcess object at 0x7f43c7731b40>.assigned_port
- *(... 9 more in this cluster)*

### `rc_unexpected_zero` — 11 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `eval.tests.test_subcommand_dispatch.test_help_subcommand_requires_target_or_no_extra_args`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'help', '--help'], returncode=0, stdout='A modern, simple TCP tunnel in Rust that exposes local ports to a remote server, bypassing standa
- `eval.tests.test_subcommand_dispatch.test_server_rejects_unknown_flag`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'server', '--unknown'], returncode=0, stdout='Runs the remote proxy server\n\nUsage: executable server [OPTIONS]\n\nOptions:\n      --min-
- `tests.test_auth.test_auth_multiple_clients_different_secrets`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'local', '12345', '--to', '127.0.0.1', '--secret', 'wrong1'], returncode=0, stdout='', stderr='').returncode
- *(... 8 more in this cluster)*

### `rc_mismatch_got0_want2` — 10 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `eval.tests.test_args_parsing.test_root_level_errors[args2-needles2]`
  > assert 0 == 2
- `eval.tests.test_args_parsing.test_local_missing_required_args[args2-needles2]`
  > assert 0 == 2
- `eval.tests.test_args_parsing.test_local_missing_option_values[args2-needles2]`
  > assert 0 == 2
- *(... 7 more in this cluster)*

### `rc_mismatch_got0_want1` — 4 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `eval.tests.test_args_parsing.test_local_accepts_common_flag_syntax[args0]`
  > assert 0 == 1
- `eval.tests.test_args_parsing.test_local_accepts_common_flag_syntax[args1]`
  > assert 0 == 1
- `eval.tests.test_args_parsing.test_local_accepts_common_flag_syntax[args2]`
  > assert 0 == 1
- *(... 1 more in this cluster)*

### `rc_mismatch_got7_want2` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_args_parsing.test_root_level_errors[args0-needles0]`
  > assert 7 == 2
- `eval.tests.test_args_parsing.test_root_level_errors[args1-needles1]`
  > assert 7 == 2
- `tests.test_cli_basics.test_no_command_error`
  > AssertionError: assert 7 == 2
  >  +  where 7 = CompletedProcess(args=['./executable'], returncode=7, stdout='', stderr='error: cannot connect to http://127.0.0.1:10050/: <urlopen error [Errno 111] Connection refused>\n').returncode

### `rc_mismatch_got2_want1` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_cli_io.test_local_uses_bore_server_env_when_to_not_provided_and_connection_refused_exit_1`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'local', '8000'], returncode=2, stdout=b'', stderr=b'').returncode
- `tests.test_cli_basics.test_env_bore_server_used_when_no_to_flag`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['./executable', 'local', '8080'], returncode=2, stdout="error: invalid value '99999' for '--port <PORT>': 99999 is not in 0..=65535\n\nFor more information, try '-

### `bytes_output_mismatch` — 1 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_01_basic_invocation.TestBasicInvocation.test_help_short_flag`
  > AssertionError: assert b'Usage:\nlocal\nserver\n' == b'A modern, s...int version\n'
  >   
  >   At index 0 diff: b'U' != b'A'
  >   
  >   Full diff:
  >   + (b'Usage:\nlocal\nserver\n')
  >   - (b'A modern, simple TCP tunnel in Rust that exposes local ports to a remote ser'
  >   -  b'ver, bypassing standard NAT connection firewalls.\n\nUsage: executable <CO'...

### `rc_mismatch_got1_want2` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_args_parsing.test_local_missing_option_values[args0-needles0]`
  > assert 1 == 2

