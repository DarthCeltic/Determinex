# Action Sheet — svenstaro__miniserve.8449e8b

**Current:** 8.53%  (50/586)
**Pass / Fail / Skip:** 50 / 389 / 1
**Gap to 100%:** 91.47 percentage points (536 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_http_basic.test_hidden_file_not_listed_by_default`
  - reason: test_hidden_file_not_listed_by_default depends on test_directory_listing_contains_files

## Failure clusters

389 failed tests grouped into 6 buckets (sorted by count).

### `uncategorized` — 298 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_additional_coverage.test_multiple_interfaces`
  > RuntimeError: Server failed to start: miniserve: unknown option: -i
  > usage: miniserve [OPTIONS] [ARGS]
  > Try 'miniserve --help' for more information.
- `tests.test_additional_coverage.test_temp_directory_option`
  > RuntimeError: Server failed to start: miniserve: unknown option: -u
  > usage: miniserve [OPTIONS] [ARGS]
  > Try 'miniserve --help' for more information.
- `tests.test_additional_coverage.test_file_external_url`
  > RuntimeError: Server failed to start: miniserve: unknown option: --file-external-url
  > usage: miniserve [OPTIONS] [ARGS]
  > Try 'miniserve --help' for more information.
- *(... 295 more in this cluster)*

### `other_assertion` — 60 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_authentication.test_auth_invalid_format`
  > assert (b'error' in b"miniserve: unknown option: --auth\nusage: miniserve [options] [args]\ntry 'miniserve --help' for more information.\n" or b'invalid' in b"miniserve: unknown option: --auth\nusage:
- `tests.test_authentication.test_auth_file_nonexistent`
  > assert (b'error' in b"miniserve: unknown option: --auth-file\nusage: miniserve [options] [args]\ntry 'miniserve --help' for more information.\n" or b'not found' in b"miniserve: unknown option: --auth-
- `tests.test_basic_invocation.test_help_shows`
  > AssertionError: assert (b'--port' in b'miniserve 0.1.0 - bootstrap scaffold\n\nUsage: miniserve [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' or b'port' 
  >  +  where b'miniserve 0.1.0 - bootstrap scaffold\n\nUsage: miniserve [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['./executable
  >  +  and   b'miniserve 0.1.0 - bootstrap scaffold\n\nusage: miniserve [options] [args]\n\noptions:\n  -h, --help     print help\n  -v, --version  print version\n' = <built-in method lower of bytes obje
  >  +    where <built-in method lower of bytes object at 0x7ff177235d10> = b'miniserve 0.1.0 - bootstrap scaffold\n\nUsage: miniserve [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --ve
  >  +      where b'miniserve 0.1.0 - bootstrap scaffold\n\nUsage: miniserve [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['./execut
- *(... 57 more in this cluster)*

### `rc_mismatch_got2_want0` — 22 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_basic_invocation.test_print_completions_bash`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--print-completions', 'bash'], returncode=2, stdout=b'', stderr=b"miniserve: unknown option: --print-completions\nusage: miniserve [OPTIONS] [ARGS
- `tests.test_basic_invocation.test_print_completions_zsh`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--print-completions', 'zsh'], returncode=2, stdout=b'', stderr=b"miniserve: unknown option: --print-completions\nusage: miniserve [OPTIONS] [ARGS]
- `tests.test_basic_invocation.test_print_completions_fish`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--print-completions', 'fish'], returncode=2, stdout=b'', stderr=b"miniserve: unknown option: --print-completions\nusage: miniserve [OPTIONS] [ARGS
- *(... 19 more in this cluster)*

### `rc_unexpected_zero` — 6 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `eval.tests.test_env_and_errors.test_nonexistent_path_is_error_and_nonzero_exit_code`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/definitely/does/not/exist'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_basic_invocation.test_serve_nonexistent_path`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '/nonexistent/path/that/does/not/exist'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_interface_binding.TestInterfaceBinding.test_bind_to_invalid_interface_fails`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/tmp/tmp826e1287', '-p', '48581', '-i', '12.34.56.78'], returncode=0, stdout='', stderr='').returncode
- *(... 3 more in this cluster)*

### `string_output_mismatch` — 2 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_output.test_dash_dash_help_exact_match_fixture`
  > AssertionError: assert 'miniserve 0....int version\n' == 'For when you...int version\n'
  >   
  >   - For when you really just want to serve some files over HTTP right now!
  >   + miniserve 0.1.0 - bootstrap scaffold
  >     
  >   + Usage: miniserve [OPTIONS] [ARGS]
  >   - Usage: executable [OPTIONS] [PATH]
  >   - ...
- `eval.tests.test_help_output.test_short_h_exact_match_fixture`
  > AssertionError: assert 'miniserve 0....int version\n' == 'For when you...int version\n'
  >   
  >   - For when you really just want to serve some files over HTTP right now!
  >   + miniserve 0.1.0 - bootstrap scaffold
  >     
  >   + Usage: miniserve [OPTIONS] [ARGS]
  >   - Usage: executable [OPTIONS] [PATH]
  >   - ...

### `boolean_false` — 1 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `eval.tests.test_env_config.test_cli_port_overrides_env_port`
  > AssertionError: assert False
  >  +  where False = wait_listening('127.0.0.1', 51117, timeout=2.0)

