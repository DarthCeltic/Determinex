# Action Sheet — drew-alleman__datasurgeon.d257cee

**Current:** 10.24%  (68/664)
**Pass / Fail / Skip:** 68 / 495 / 0
**Gap to 100%:** 89.76 percentage points (596 tests)

## Failure clusters

495 failed tests grouped into 11 buckets (sorted by count).

### `rc_mismatch_got2_want0` — 308 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_additional_coverage.test_extraction_without_flags_finds_content`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '-S'], returncode=2, stdout=b'', stderr=b"datasurgeon: error: failed to process '-S': [Errno 2] No such file or directory: '-S'\n").returncode
- `tests.test_additional_coverage.test_multiple_hashes_different_types`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '-H', '-S'], returncode=2, stdout=b'', stderr=b"datasurgeon: error: failed to process '-H': [Errno 2] No such file or directory: '-H'\n").returncod
- `tests.test_additional_coverage.test_credit_card_various_formats`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '-c', '-S'], returncode=2, stdout=b'', stderr=b"datasurgeon: error: failed to process '-c': [Errno 2] No such file or directory: '-c'\n").returncod
- *(... 305 more in this cluster)*

### `other_assertion` — 125 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_help_flag`
  > AssertionError: assert b'Usage: executable [OPTIONS]' in b'datasurgeon 0.1.0\n\nusage: datasurgeon [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --ve
  >  +  where b'datasurgeon 0.1.0\n\nusage: datasurgeon [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --verbose  Verbose\n  -q, --quiet    Quiet\n  -i, -
- `tests.test_basic_invocation.test_help_short_flag`
  > AssertionError: assert b'Usage: executable [OPTIONS]' in b'datasurgeon 0.1.0\n\nusage: datasurgeon [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --ve
  >  +  where b'datasurgeon 0.1.0\n\nusage: datasurgeon [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --verbose  Verbose\n  -q, --quiet    Quiet\n  -i, -
- `tests.test_basic_invocation.test_version_flag`
  > AssertionError: assert b'DataSurgeon' in b'datasurgeon 0.1.0\n'
  >  +  where b'datasurgeon 0.1.0\n' = CompletedProcess(args=['./executable', '--version'], returncode=0, stdout=b'datasurgeon 0.1.0\n', stderr=b'').stdout
- *(... 122 more in this cluster)*

### `rc_mismatch_got2_want1` — 17 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_argparse_validation.test_file_dash_is_treated_as_literal_path_not_stdin`
  > assert 2 == 1
- `eval.tests.test_env_config_plugins.test_home_env_var_controls_plugin_file_path_when_listing_empty`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--list'], returncode=2, stdout='', stderr='datasurgeon: error: unrecognized argument: --list\n').returncode
- `eval.tests.test_env_config_plugins.test_local_plugins_json_takes_precedence_over_home_location`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--list'], returncode=2, stdout='', stderr='datasurgeon: error: unrecognized argument: --list\n').returncode
- *(... 14 more in this cluster)*

### `uncategorized` — 17 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_plugins_basic.test_system_path_plugin_file_loads`
  > FileExistsError: [Errno 17] File exists: '/tmp/pytest-of-root/pytest-0/test_system_path_plugin_file_l2/home'
- `tests.test_plugins_basic.test_plugin_system_path_priority_over_local`
  > FileExistsError: [Errno 17] File exists: '/tmp/pytest-of-root/pytest-0/test_plugin_system_path_priori2/home'
- `tests.test_plugins_errors.test_malformed_json_syntax_error_with_exit`
  > FileExistsError: [Errno 17] File exists: '/tmp/pytest-of-root/pytest-0/test_malformed_json_syntax_err2/home'
- *(... 14 more in this cluster)*

### `string_output_mismatch` — 15 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_usage.test_baseline_help_output_matches_fixture_exactly`
  > AssertionError: assert 'datasurgeon ... header row\n' == 'Note: All ex...int version\n'
  >   
  >   - Note: All extraction features (e.g: -i) work on a specified file (-f) or an output stream.
  >   + datasurgeon 0.1.0
  >     
  >   - Usage: executable [OPTIONS]
  >   + usage: datasurgeon [OPTIONS] [ARGS]
  >     ...
- `tests.test_extraction_extended.test_dns_srv_records_from_file`
  > AssertionError: assert '/workspace/e...192.168.1.1\n' == 'srv_dns: _se...SRV 1 1 1 h\n'
  >   
  >   + /workspace/eval/test_resources/test_extraction_extended/dns_input.txt:ip:192.168.1.1
  >   - srv_dns: _service._tcp.example.com IN SRV 10 60 5060 sipserver.example.com
  >   - srv_dns: _http._tcp.web.example.org IN SRV 0 5 80 webserver.example.org
  >   - srv_dns: _ldap._tcp.dc IN SRV 0 100 389 ldap-server.domain.local
  >   - srv_dns: Multiple: _sip._tcp.voip.net IN SRV 10 60 5060 sip1.voip.net and _sip._udp.voip.net IN SRV 20 30 5060 sip2.voip.net
  >   - srv_dns: Short form: _s._t.d IN SRV 1 1 1 h
- `tests.test_plugins_management.test_list_plugins_empty`
  > AssertionError: assert '' == 'No plugins f.../plugins.json'
  >   
  >   - No plugins found. Plugin File: /tmp/pytest-of-root/pytest-0/test_list_plugins_empty2/.DataSurgeon/plugins.json
- *(... 12 more in this cluster)*

### `rc_mismatch_got0_want1` — 5 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `eval.tests.test_executable_behavior.test_missing_file_ignore_suppresses_message_but_exit_code_unchanged`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-f', '/no/such/file', '-e', '-S', '--ignore'], returncode=0, stdout='', stderr='').returncode
- `tests.test_gap_filling.test_ignore_flag_suppresses_file_errors`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-e', '-f', 'nonexistent.txt', '--ignore'], returncode=0, stdout='', stderr='').returncode
- `tests.test_plugins_basic.test_plugin_with_thorough_flag_gets_all_matches`
  > AssertionError: assert 0 == 1
  >  +  where 0 = <built-in method count of str object at 0x7f402f050030>('numbers:')
  >  +    where <built-in method count of str object at 0x7f402f050030> = ''.count
  >  +      where '' = CompletedProcess(args=['/workspace/executable', '--numbers', '-C', '-S', '-f', '/workspace/eval/test_resources/test_plugins_basic/sample_input.txt'], returncode=2, stdout='', stderr
- *(... 2 more in this cluster)*

### `rc_mismatch_got2_want101` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_timing_errors.test_invalid_filter_regex_causes_panic`
  > AssertionError: assert 2 == 101
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-e', '--filter', '[unclosed'], returncode=2, stdout='', stderr='datasurgeon: error: unrecognized argument: --filter\n').returncode
- `tests.test_timing_errors.test_invalid_drop_regex_causes_panic`
  > AssertionError: assert 2 == 101
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-e', '--drop', '(?P<invalid'], returncode=2, stdout='', stderr='datasurgeon: error: unrecognized argument: --drop\n').returncode
- `tests.test_timing_errors.test_ignore_does_not_prevent_regex_panic`
  > AssertionError: assert 2 == 101
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-e', '--ignore', '--filter', '[invalid'], returncode=2, stdout='', stderr='datasurgeon: error: unrecognized argument: --filter\n').return

### `empty_list_or_string` — 2 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_plugins_management.test_list_plugins_single_entry_formatting`
  > IndexError: list index out of range
- `tests.test_plugins_management.test_list_plugins_column_width_calculation`
  > IndexError: list index out of range

### `returned_none` — 1 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_usage.test_help_has_usage_line`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7ff18a392680>('^Usage: executable \\[OPTIONS\\]$', 'datasurgeon 0.1.0\n\nusage: datasurgeon [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --ve
  >  +    where <function search at 0x7ff18a392680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE

### `bytes_output_mismatch` — 1 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_plugins_management.test_remove_all_plugins_leaves_empty_array`
  > AssertionError: assert [{'arg_long_n...,3}\\b', ...}] == []
  >   
  >   Left contains 3 more items, first extra item: {'arg_long_name': 'numbers', 'content_type': 'numbers', 'help_message': 'Extracts numbers', 'regex': '(\\d+)', ...}
  >   
  >   Full diff:
  >   - []
  >   + [
  >   +     {...

### `rc_mismatch_got1_want2` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_timing_errors.test_ignore_flag_with_timing_shows_timing`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len([''])

