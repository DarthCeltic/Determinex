# Action Sheet — quinn-rs__quinn.bb359cc

**Current:** 15.26%  (123/806)
**Pass / Fail / Skip:** 123 / 474 / 2
**Gap to 100%:** 84.74 percentage points (683 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_client.test_client_connection_refused`
  - reason: gold-env-limitation: pytest timeout (30s) conflicts with client timeout (30s), causing test to fail before client completes
- `eval.tests.test_client_json_and_network.test_client_json_to_stdout_option_is_present_in_help`
  - reason: test_client_json_to_stdout_option_is_present_in_help depends on test_client_json_flag_rejects_non_pathish_value

## Failure clusters

474 failed tests grouped into 14 buckets (sorted by count).

### `other_assertion` — 347 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_advanced_options.test_client_with_cubic_congestion`
  > AssertionError: assert (b'resolving' in b'' or b'connecting' in b'' or b'failed' in b'')
  >  +  where b'' = <built-in method lower of bytes object at 0x7e2ae68e4030>()
  >  +    where <built-in method lower of bytes object at 0x7e2ae68e4030> = b''.lower
  >  +  and   b'' = <built-in method lower of bytes object at 0x7e2ae68e4030>()
  >  +    where <built-in method lower of bytes object at 0x7e2ae68e4030> = b''.lower
  >  +  and   b'' = <built-in method lower of bytes object at 0x7e2ae68e4030>()
  >  +    where <built-in method lower of bytes object at 0x7e2ae68e4030> = b''.lower
- `tests.test_advanced_options.test_client_with_bbr_congestion`
  > AssertionError: assert (b'resolving' in b'' or b'connecting' in b'' or b'failed' in b'')
  >  +  where b'' = <built-in method lower of bytes object at 0x7e2ae68e4030>()
  >  +    where <built-in method lower of bytes object at 0x7e2ae68e4030> = b''.lower
  >  +  and   b'' = <built-in method lower of bytes object at 0x7e2ae68e4030>()
  >  +    where <built-in method lower of bytes object at 0x7e2ae68e4030> = b''.lower
  >  +  and   b'' = <built-in method lower of bytes object at 0x7e2ae68e4030>()
  >  +    where <built-in method lower of bytes object at 0x7e2ae68e4030> = b''.lower
- `tests.test_advanced_options.test_client_with_new_reno_congestion`
  > AssertionError: assert (b'resolving' in b'' or b'connecting' in b'' or b'failed' in b'')
  >  +  where b'' = <built-in method lower of bytes object at 0x7e2ae68e4030>()
  >  +    where <built-in method lower of bytes object at 0x7e2ae68e4030> = b''.lower
  >  +  and   b'' = <built-in method lower of bytes object at 0x7e2ae68e4030>()
  >  +    where <built-in method lower of bytes object at 0x7e2ae68e4030> = b''.lower
  >  +  and   b'' = <built-in method lower of bytes object at 0x7e2ae68e4030>()
  >  +    where <built-in method lower of bytes object at 0x7e2ae68e4030> = b''.lower
- *(... 344 more in this cluster)*

### `bytes_output_mismatch` — 42 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_argument_parsing.test_client_duration`
  > AssertionError: assert (b'resolving' in b'' or b'connecting' in b'' or 2 == 124)
  >  +  where b'' = <built-in method lower of bytes object at 0x7e2ae68e4030>()
  >  +    where <built-in method lower of bytes object at 0x7e2ae68e4030> = b''.lower
  >  +  and   b'' = <built-in method lower of bytes object at 0x7e2ae68e4030>()
  >  +    where <built-in method lower of bytes object at 0x7e2ae68e4030> = b''.lower
  >  +  and   2 = CompletedProcess(args=['./executable', 'client', 'invalid-host:9999', '--duration', '5'], returncode=2, stdout=b'', stderr=b'').returncode
- `tests.test_flags.test_help_long_flag`
  > AssertionError: assert b'' == b'Usage: exec... Print help\n'
  >   
  >   Full diff:
  >   + b''
  >   - (b'Usage: executable <COMMAND>\n\nCommands:\n  server  Run as a perf server\n  '
  >   -  b'client  Run as a perf client\n  help    Print this message or the help of'
  >   -  b' the given subcommand(s)\n\nOptions:\n  -h, --help  Print help\n')
- `tests.test_flags.test_help_short_flag`
  > AssertionError: assert b'Usage:\nser...r\n--listen\n' == b'Usage: exec... Print help\n'
  >   
  >   At index 6 diff: b'\n' != b' '
  >   
  >   Full diff:
  >   + (b'Usage:\nserver\nclient\nperf server\nUsage:\nserver\nclient\nRun as a perf\n'
  >   +  b'Run as a perf server\n--listen\n')
  >   - (b'Usage: executable <COMMAND>\n\nCommands:\n  server  Run as a perf server\n  '
- *(... 39 more in this cluster)*

### `string_output_mismatch` — 38 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_errors.test_invalid_subcommand`
  > assert '' == "error: unrec...y '--help'.\n"
  >   
  >   - error: unrecognized subcommand 'invalid_command'
  >   - 
  >   - Usage: executable <COMMAND>
  >   - 
  >   - For more information, try '--help'.
- `tests.test_errors.test_server_invalid_listen_address`
  > assert '' == "error: inval...y '--help'.\n"
  >   
  >   - error: invalid value 'not_an_address' for '--listen <LISTEN>': invalid socket address syntax
  >   - 
  >   - For more information, try '--help'.
- `tests.test_errors.test_server_invalid_port_number`
  > assert '' == "error: inval...y '--help'.\n"
  >   
  >   - error: invalid value '127.0.0.1:99999' for '--listen <LISTEN>': invalid socket address syntax
  >   - 
  >   - For more information, try '--help'.
- *(... 35 more in this cluster)*

### `rc_unexpected_zero` — 18 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_argument_parsing.test_server_invalid_congestion`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'server', '--congestion', 'invalid-algo'], returncode=0, stdout=b'localhost:4433\n[default:\n', stderr=b'').returncode
- `tests.test_basic_invocation.test_no_arguments_shows_usage`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_basic_invocation.test_invalid_command`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'invalid-command'], returncode=0, stdout=b'Usage:\nserver\nclient\nRun as a perf\nRun as a perf server\n--listen\n--key\n--cert\nAddress to listen 
- *(... 15 more in this cluster)*

### `rc_mismatch_got0_want2` — 10 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_basic.test_no_arguments_shows_usage`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['./executable'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_errors.test_no_subcommand`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_integration.test_multiple_unidirectional_streams`
  > AssertionError: assert 0 == 2
  >  +  where 0 = <built-in method count of str object at 0x79c2863fc030>('Overall stats:')
  >  +    where <built-in method count of str object at 0x79c2863fc030> = ''.count
  >  +  and   2 = <built-in method count of str object at 0x5808e2677900>('Overall stats:')
  >  +    where <built-in method count of str object at 0x5808e2677900> = 'TIMESTAMP  WARN perf: Unable to set desired send buffer size. Desired: 2097152, Actual: 425984\nTIMESTAMP  WARN perf: Unable to s
- *(... 7 more in this cluster)*

### `empty_list_or_string` — 7 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_stats.test_json_interval_structure`
  > IndexError: list index out of range
- `tests.test_stats.test_multiple_intervals`
  > IndexError: list index out of range
- `tests.test_stats.test_throughput_calculation_accuracy`
  > IndexError: list index out of range
- *(... 4 more in this cluster)*

### `boolean_false` — 4 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `eval.tests.test_env_config.test_keylog_writes_to_path_from_sslkeylogfile`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/pytest-of-root/pytest-0/test_keylog_writes_to_path_fro2/keys.log').exists
- `eval.tests.test_help_edge_cases.test_help_subcommand_prints_main_help`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7bafb17d4030>('Usage: executable <COMMAND>\n')
  >  +    where <built-in method startswith of str object at 0x7bafb17d4030> = ''.startswith
  >  +      where '' = CompletedProcess(args=['/workspace/executable', 'help'], returncode=0, stdout='', stderr='').stdout
- `eval.tests.test_help_main.test_help_trailing_newline`
  > AssertionError: assert False
  >  +  where False = <built-in method endswith of str object at 0x7bafb17d4030>('\n')
  >  +    where <built-in method endswith of str object at 0x7bafb17d4030> = ''.endswith
- *(... 1 more in this cluster)*

### `rc_mismatch_got2_want0` — 2 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_coverage_boost.test_client_with_various_interval_settings`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', 'client', '127.0.0.1:36979', '--interval', '1', '--duration', '3', '--download-size', '20k', '--upload-size', '20k'], returncode=2, stdout=b'', std
- `tests.test_integration.test_conn_stats_server_output`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'client', '--duration', '2', '127.0.0.1:33665'], returncode=2, stdout=b'', stderr=b'').returncode

### `returned_none` — 1 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_client.test_client_bidirectional_requests`
  > assert None is not None

### `json_output_missing_or_bad` — 1 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `tests.test_client.test_client_json_output_structure`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

### `rc_mismatch_got0_want1` — 1 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_integration.test_keylog_generation`
  > AssertionError: assert 0 == 1
  >  +  where 0 = <built-in method count of str object at 0x79c2863fc030>('Overall stats:')
  >  +    where <built-in method count of str object at 0x79c2863fc030> = ''.count
  >  +  and   1 = <built-in method count of str object at 0x5808e2757fc0>('Overall stats:')
  >  +    where <built-in method count of str object at 0x5808e2757fc0> = 'TIMESTAMP  WARN perf: Unable to set desired send buffer size. Desired: 2097152, Actual: 425984\nTIMESTAMP  WARN perf: Unable to s

### `uncategorized` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_server.test_server_keylog_flag`
  > Failed: Server exited with code 0. stdout: , stderr:

### `test_timeout` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_env_config.test_keylog_flag_requires_sslkeylogfile_to_be_nonempty`
  > Failed: DID NOT RAISE <class 'subprocess.TimeoutExpired'>

### `rc_mismatch_got1_want2` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_cli_validation.test_ext_unknown_subcommand`
  > assert 1 == 2
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'no_such_cmd'], returncode=1, stdout=b'', stderr=b"error: [Errno 2] No such file or directory: 'no_such_cmd'\n").returncode

