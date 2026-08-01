# Action Sheet — hatoo__oha.8dc6349

**Current:** 4.71%  (56/1188)
**Pass / Fail / Skip:** 56 / 778 / 4
**Gap to 100%:** 95.29 percentage points (1132 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_client_easy_wins.test_format_host_port_ipv6_basic`
  - reason: IPv6 not available on this system
- `tests.test_harvest.TestGoogle.test_google`
  - reason: External test, skip for CI/CD
- `tests.test_harvest_clean.TestGoogleLive.test_google`
  - reason: Live external test - enable manually if needed
- `tests.test_output.test_json_schema_validation`
  - reason: jsonschema not installed

## Failure clusters

778 failed tests grouped into 10 buckets (sorted by count).

### `rc_mismatch_got2_want0` — 369 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_advanced.test_request_count_suffix_m`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--dump-urls', '3', '--rand-regex-url', 'http://127.0.0.1/test'], returncode=2, stdout=b'', stderr=b"oha: unknown option: --dump-urls\nusa
- `tests.test_advanced.test_proxy_header_option`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--no-tui', '-n', '2', '--proxy-header', 'X-Proxy: value', '--output-format', 'json', 'http://127.0.0.1:34443'], returncode=2, stdout=b'',
- `tests.test_advanced.test_csv_output_structure`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--no-tui', '-n', '10', '--output-format', 'csv', 'http://127.0.0.1:54543'], returncode=2, stdout=b'', stderr=b"oha: unknown option: --no-
- *(... 366 more in this cluster)*

### `other_assertion` — 183 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic.test_help_long`
  > AssertionError: assert b'Ohayou' in b'oha 0.1.0 - bootstrap scaffold\n\nUsage: oha [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n'
  >  +  where b'oha 0.1.0 - bootstrap scaffold\n\nUsage: oha [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['/workspace/executable', 
- `tests.test_basic.test_help_short`
  > AssertionError: assert b'Ohayou' in b'oha 0.1.0 - bootstrap scaffold\n\nUsage: oha [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n'
  >  +  where b'oha 0.1.0 - bootstrap scaffold\n\nUsage: oha [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['/workspace/executable', 
- `tests.test_basic.test_no_args_shows_help`
  > assert b'Usage:' in b"usage: oha [OPTIONS] [ARGS]\nTry 'oha --help' for more information.\n"
- *(... 180 more in this cluster)*

### `subprocess_failed` — 97 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_advanced_features.TestAdvancedFeatures.test_redirect_default`
  > subprocess.CalledProcessError: Command '['/workspace/executable', '-n', '1', '--no-tui', 'http://127.0.0.1:55215/redirect']' returned non-zero exit status 2.
- `tests.test_advanced_features.TestAdvancedFeatures.test_disable_keepalive`
  > subprocess.CalledProcessError: Command '['/workspace/executable', '-n', '5', '--disable-keepalive', '--no-tui', 'http://127.0.0.1:51727/']' returned non-zero exit status 2.
- `tests.test_advanced_features.TestAdvancedFeatures.test_disable_compression`
  > subprocess.CalledProcessError: Command '['/workspace/executable', '-n', '5', '--disable-compression', '--no-tui', 'http://127.0.0.1:38859/']' returned non-zero exit status 2.
- *(... 94 more in this cluster)*

### `uncategorized` — 58 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_client_easy_wins.test_format_host_port_ipv6_with_connect_to`
  > OSError: [Errno 98] Address already in use
- `tests.test_client_easy_wins.test_proxy_https_connect_basic`
  > OSError: [Errno 98] Address already in use
- `tests.test_client_easy_wins.test_timeout_path_triggered`
  > OSError: [Errno 98] Address already in use
- *(... 55 more in this cluster)*

### `missing_file` — 32 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_harvest_clean.TestBasicRequests.test_enable_compression_default`
  > FileNotFoundError: [Errno 2] No such file or directory: './executable'
- `tests.test_harvest_clean.TestBasicRequests.test_setting_custom_header`
  > FileNotFoundError: [Errno 2] No such file or directory: './executable'
- `tests.test_harvest_clean.TestBasicRequests.test_setting_accept_header`
  > FileNotFoundError: [Errno 2] No such file or directory: './executable'
- *(... 29 more in this cluster)*

### `rc_mismatch_got2_want1` — 19 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_args_validation.test_argument_errors_exit_codes_and_messages[args4-1-exp_stderr_substrs4]`
  > assert 2 == 1
- `eval.tests.test_errors_and_edge_cases.test_dns_failure_is_exit_1`
  > assert 2 == 1
  >  +  where 2 = ExecResult(returncode=2, stdout='', stderr="oha: unknown option: --no-tui\nusage: oha [OPTIONS] [ARGS]\nTry 'oha --help' for more information.\n").returncode
- `tests.test_client_final.test_dns_no_record`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--no-tui', '-n', '1', 'http://this-domain-definitely-does-not-exist-12345.invalid/'], returncode=2, stdout=b'', stderr=b"oha: unknown opt
- *(... 16 more in this cluster)*

### `json_output_missing_or_bad` — 11 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `tests.test_advanced.test_request_timeout`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_errors.test_invalid_url_scheme`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_errors.test_unreachable_host`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- *(... 8 more in this cluster)*

### `rc_unexpected_zero` — 5 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_subcommand_dispatch.TestNoSubcommandStructure.test_no_help_subcommand`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'help'], returncode=0, stdout='oha 0.1.0 - bootstrap scaffold\n\nUsage: oha [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -
- `tests.test_subcommand_dispatch.TestNoSubcommandStructure.test_no_version_subcommand`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'version'], returncode=0, stdout="b'Simulated tool output'\n", stderr='').returncode
- `tests.test_subcommand_dispatch.TestNoSubcommandStructure.test_unknown_command_treated_as_url`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'nonexistent_command'], returncode=0, stdout="b'Simulated tool output'\n", stderr='').returncode
- *(... 2 more in this cluster)*

### `string_output_mismatch` — 3 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_baseline.test_help_matches_baseline_fixture_exactly`
  > AssertionError: assert 'oha 0.1.0 - ...int version\n' == 'Ohayou(おはよう)...int version\n'
  >   
  >   - Ohayou(おはよう), HTTP load generator, inspired by rakyll/hey with tui animation.
  >   + oha 0.1.0 - bootstrap scaffold
  >     
  >   + Usage: oha [OPTIONS] [ARGS]
  >   - Usage: executable [OPTIONS] <URL>
  >   - ...
- `eval.tests.test_help_version.test_version_exact`
  > AssertionError: assert 'oha 0.1.0\n' == 'oha 1.12.1\n'
  >   
  >   - oha 1.12.1
  >   + oha 0.1.0
- `eval.tests.test_help_version.test_help_golden_exact`
  > AssertionError: assert 'oha 0.1.0 - ...int version\n' == 'Ohayou(おはよう)...int version\n'
  >   
  >   - Ohayou(おはよう), HTTP load generator, inspired by rakyll/hey with tui animation.
  >   + oha 0.1.0 - bootstrap scaffold
  >     
  >   + Usage: oha [OPTIONS] [ARGS]
  >   - Usage: executable [OPTIONS] <URL>
  >   - ...

### `returned_none` — 1 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_output.test_help_usage_mentions_url_argument`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f8e1b982680>('Usage:\\s+executable\\s+\\[OPTIONS\\]\\s+<URL>', 'oha 0.1.0 - bootstrap scaffold\n\nUsage: oha [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Prin
  >  +    where <function search at 0x7f8e1b982680> = re.search

