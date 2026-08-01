# Action Sheet — orf__gping.26eb5b9

**Current:** 42.04%  (309/735)
**Pass / Fail / Skip:** 309 / 319 / 4
**Gap to 100%:** 57.96 percentage points (426 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_harvest_pinger.TestIntegration.test_integration_any`
  - reason: Requires network access to ping tomforb.es
- `tests.test_harvest_pinger.TestIntegration.test_integration_ipv4`
  - reason: Requires network access to ping tomforb.es with IPv4
- `tests.test_harvest_pinger.TestIntegration.test_integration_ipv6`
  - reason: Requires network access to ping tomforb.es with IPv6 (may not be available on CI)
- `tests.test_harvest_pinger.TestParser.test_parser_windows`
  - reason: Windows ping parser only available on Windows platform - executable uses compile-time platform detection

## Failure clusters

319 failed tests grouped into 8 buckets (sorted by count).

### `other_assertion` — 218 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_help_flag`
  > AssertionError: assert b'Ping, but with a graph' in b'gping 0.1.0 - bootstrap scaffold\n\nUsage: gping [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n'
  >  +  where b'gping 0.1.0 - bootstrap scaffold\n\nUsage: gping [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['./executable', '--he
- `tests.test_basic_invocation.test_help_short_flag`
  > AssertionError: assert b'Ping, but with a graph' in b'gping 0.1.0 - bootstrap scaffold\n\nUsage: gping [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n'
  >  +  where b'gping 0.1.0 - bootstrap scaffold\n\nUsage: gping [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['./executable', '-h']
- `tests.test_basic_invocation.test_version_flag`
  > AssertionError: assert b'commit_hash:' in b'gping 0.1.0\n'
  >  +  where b'gping 0.1.0\n' = CompletedProcess(args=['./executable', '--version'], returncode=0, stdout=b'gping 0.1.0\n', stderr=b'').stdout
- *(... 215 more in this cluster)*

### `string_output_mismatch` — 58 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_exact_baseline.test_help_output_matches_baseline_exactly`
  > AssertionError: assert 'gping 0.1.0 ...int version\n' == 'Ping, but wi...int version\n'
  >   
  >   - Ping, but with a graph.
  >   + gping 0.1.0 - bootstrap scaffold
  >     
  >   + Usage: gping [OPTIONS] [ARGS]
  >   - Usage: executable [OPTIONS] [HOSTS_OR_COMMANDS]...
  >   - ...
- `tests.test_gping.test_help_exact_output`
  > AssertionError: assert 'gping 0.1.0 ...int version\n' == 'Ping, but wi...int version\n'
  >   
  >   - Ping, but with a graph.
  >   + gping 0.1.0 - bootstrap scaffold
  >     
  >   + Usage: gping [OPTIONS] [ARGS]
  >   - Usage: executable [OPTIONS] [HOSTS_OR_COMMANDS]...
  >   - ...
- `eval.tests.test_cli_golden.test_help_exact_matches_golden`
  > AssertionError: assert 'gping 0.1.0 ...int version\n' == 'Ping, but wi...int version\n'
  >   
  >   - Ping, but with a graph.
  >   + gping 0.1.0 - bootstrap scaffold
  >     
  >   + Usage: gping [OPTIONS] [ARGS]
  >   - Usage: executable [OPTIONS] [HOSTS_OR_COMMANDS]...
  >   - ...
- *(... 55 more in this cluster)*

### `rc_unexpected_zero` — 31 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_error_paths.test_invalid_hostname_resolution_error`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'this-hostname-definitely-does-not-exist-xyz12345.invalid'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_error_paths.test_empty_hostname_error`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', ''], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_error_paths.test_multiple_errors_in_batch`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'invalid-host-1.invalid', 'invalid-host-2.invalid'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 28 more in this cluster)*

### `rc_mismatch_got2_want1` — 7 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_no_args_shows_error`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['./executable'], returncode=2, stdout=b'', stderr=b"usage: gping [OPTIONS] [ARGS]\nTry 'gping --help' for more information.\n").returncode
- `tests.test_command_mode.test_cmd_mode_requires_argument`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['./executable', '--cmd'], returncode=2, stdout=b'', stderr=b"gping: unknown option: --cmd\nusage: gping [OPTIONS] [ARGS]\nTry 'gping --help' for more information.\
- `tests.test_cli_batch2.test_color_valid_names_case_insensitive`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--color', 'RED', 'localhost'], returncode=2, stdout='', stderr="gping: unknown option: --color\nusage: gping [OPTIONS] [ARGS]\nTry 'gping
- *(... 4 more in this cluster)*

### `returned_none` — 2 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_usage.test_help_usage_has_options_and_hosts`
  > AssertionError: assert None is not None
  >  +  where None = <function search at 0x7f2b1fa02680>('^Usage: executable\\s+\\[OPTIONS\\]\\s+\\[HOSTS_OR_COMMANDS\\]\\.\\.\\.$', 'gping 0.1.0 - bootstrap scaffold\n\nUsage: gping [OPTIONS] [ARGS]\n\nO
  >  +    where <function search at 0x7f2b1fa02680> = re.search
  >  +    and   re.MULTILINE = re.M
- `eval.tests.test_help_usage.test_help_has_arguments_section`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f2b1fa02680>('^Arguments:\\s*$', 'gping 0.1.0 - bootstrap scaffold\n\nUsage: gping [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  P
  >  +    where <function search at 0x7f2b1fa02680> = re.search
  >  +    and   re.MULTILINE = re.M

### `boolean_false` — 1 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `eval.tests.test_help_usage.test_help_precedence_with_invalid_flag_still_shows_help_and_exits_zero`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7f2b1e7495f0>('Ping, but with a graph.\n\nUsage: executable')
  >  +    where <built-in method startswith of str object at 0x7f2b1e7495f0> = 'gping 0.1.0 - bootstrap scaffold\n\nUsage: gping [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version 
  >  +      where 'gping 0.1.0 - bootstrap scaffold\n\nUsage: gping [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['/workspace/execut

### `rc_mismatch_got0_want1` — 1 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_cli_batch2.test_multiple_hosts_accepted`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'localhost', 'google.com', 'example.com'], returncode=0, stdout='', stderr='').returncode

### `rc_mismatch_got2_want101` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cmd_mode.test_empty_command_string_panics`
  > assert 2 == 101
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--cmd', ''], returncode=2, stdout='', stderr="gping: unknown option: --cmd\nusage: gping [OPTIONS] [ARGS]\nTry 'gping --help' for more in

