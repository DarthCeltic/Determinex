# Action Sheet — robertdavidgraham__masscan.b99d433

**Current:** 7.39%  (227/3073)
**Pass / Fail / Skip:** 227 / 991 / 0
**Gap to 100%:** 92.61 percentage points (2846 tests)

## Failure clusters

991 failed tests grouped into 11 buckets (sorted by count).

### `other_assertion` — 756 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_actual_output_generation.test_echo_all_output_formats`
  > AssertionError: assert ('xml' in '' or 'output' in '')
  >  +  where '' = <built-in method lower of str object at 0x7fcff93cc030>()
  >  +    where <built-in method lower of str object at 0x7fcff93cc030> = ''.lower
  >  +  and   '' = <built-in method lower of str object at 0x7fcff93cc030>()
  >  +    where <built-in method lower of str object at 0x7fcff93cc030> = ''.lower
- `tests.test_actual_output_generation.test_offline_with_packet_trace`
  > AssertionError: assert 'offline' in ''
  >  +  where '' = <built-in method lower of str object at 0x7fcff93cc030>()
  >  +    where <built-in method lower of str object at 0x7fcff93cc030> = ''.lower
- `tests.test_actual_output_generation.test_seed_affects_randomization`
  > AssertionError: assert '12345' in ''
- *(... 753 more in this cluster)*

### `rc_mismatch_got1_want0` — 125 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_actual_output_generation.test_multiple_output_formats`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '-p80', '127.0.0.1', '--output-format', 'xml', '--output-filename', '/tmp/tmpm3f4t2vo/scan.xml', '--offline', '--wait', '0', '--echo'], returncode=
- `tests.test_actual_output_generation.test_multiple_port_types`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '--ports', 'T:80,T:443,U:53,U:161', '--echo'], returncode=1, stdout=b"error: unexpected argument '--echo' found\nError: unexpected argument '--echo
- `tests.test_binary_and_advanced.test_mixed_tcp_udp_sctp_ports`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '127.0.0.1', '-p80,443,U:53,U:161', '--echo'], returncode=1, stdout=b"error: unexpected argument '-p80,443,U:53,U:161' found\nError: unexpected arg
- *(... 122 more in this cluster)*

### `string_output_mismatch` — 57 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_basic_cli.TestHelp.test_help_exact_output`
  > AssertionError: assert '' == 'usage: massc...34 --echo\n\n'
  >   
  >   - usage: masscan [options] [<IP|RANGE>... -pPORT[,PORT...]]
  >   - MASSCAN is a fast port scanner. The primary input parameters are the
  >   - IP addresses/ranges you want to scan, and the port numbers. An example
  >   - is the following, which scans the 10.x.x.x network for web servers:
  >   - 
  >   -     masscan 10.0.0.0/8 -p80...
- `tests.test_basic_cli.TestHelp.test_nmap_exact_output`
  > AssertionError: assert '' == 'Masscan (htt...MORE HELP\n\n'
  >   
  >   - Masscan (https://github.com/robertdavidgraham/masscan)
  >   - Usage: masscan [Options] -p{Target-Ports} {Target-IP-Ranges}
  >   - TARGET SPECIFICATION:
  >   -   Can pass only IPv4/IPv6 address, CIDR networks, or ranges (non-nmap style)
  >   -   Ex: 10.0.0.0/8, 192.168.0.1, 10.0.0.1-10.0.0.254
  >   -   -iL <inputfilename>: Input from list of hosts/networks...
- `eval.tests.test_masscan_cli.test_help_exact_output`
  > AssertionError: assert '' == 'usage: massc...34 --echo\n\n'
  >   
  >   - usage: masscan [options] [<IP|RANGE>... -pPORT[,PORT...]]
  >   - MASSCAN is a fast port scanner. The primary input parameters are the
  >   - IP addresses/ranges you want to scan, and the port numbers. An example
  >   - is the following, which scans the 10.x.x.x network for web servers:
  >   - 
  >   -     masscan 10.0.0.0/8 -p80...
- *(... 54 more in this cluster)*

### `returned_none` — 20 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_config_env_handling.test_default_config_without_args_has_rate_and_seed`
  > AssertionError: assert None is not None
  >  +  where None = _get_echo_value(b'', 'rate')
  >  +    where b'' = CompletedProcess(args=['/workspace/executable', '--echo'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_config_env_handling.test_config_file_sets_value_rate`
  > AssertionError: assert None == '12345'
  >  +  where None = _get_echo_value(b'', 'rate')
  >  +    where b'' = CompletedProcess(args=['/workspace/executable', '-c', '/tmp/tmpazqlh8zs/scan.conf', '--echo'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_config_env_handling.test_cli_overrides_config_file_for_same_option`
  > AssertionError: assert None == '2'
  >  +  where None = _get_echo_value(b'', 'rate')
  >  +    where b'' = CompletedProcess(args=['/workspace/executable', '-c', '/tmp/tmpqzmmkzne/scan.conf', '--rate', '2', '--echo'], returncode=0, stdout=b'', stderr=b'').stdout
- *(... 17 more in this cluster)*

### `rc_mismatch_got0_want1` — 19 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_basic.test_version_short_flag`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-V'], returncode=0, stdout=b'masscan 0.1.0\n', stderr=b'').returncode
- `tests.test_basic_cli.TestNoArguments.test_no_arguments`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable'], returncode=0, stdout='-- blackrock-1 --\n-- blackrock-2 --\n-- smack-1 --\n-- smack-1 -- \\nbits/second\n--adapter-ip\n--echo\n--max-rate
- `eval.tests.test_masscan_cli.test_missing_config_file_errors_include_cwd`
  > assert 0 == 1
- *(... 16 more in this cluster)*

### `rc_unexpected_zero` — 4 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_basic_invocation.test_no_arguments_shows_error`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable'], returncode=0, stdout=b'-- blackrock-1 --\n-- blackrock-2 --\n-- smack-1 --\n-- smack-1 -- \\nbits/second\n--adapter-ip\n--echo\n--max-rate\n--rota
- `tests.test_config_env_handling.test_unknown_config_option_in_file_is_fatal`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-c', '/tmp/tmp73u6ep9g/bad.conf', '--echo'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_config_files.TestIncludeFile.test_include_file_missing`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-p80', '-iL', '/nonexistent/ips.txt', '--echo'], returncode=0, stdout='', stderr='').returncode
- *(... 1 more in this cluster)*

### `bytes_output_mismatch` — 3 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_basic_invocation.test_regress_flag_runs_regression_test`
  > AssertionError: assert b'regression test:' in b'=== benchmarking (64-bits) ===\n-- blackrock-1 -- \n-- blackrock-2 -- \n'
  >  +  where b'=== benchmarking (64-bits) ===\n-- blackrock-1 -- \n-- blackrock-2 -- \n' = <built-in method lower of bytes object at 0x7fcff7587a60>()
  >  +    where <built-in method lower of bytes object at 0x7fcff7587a60> = b'=== benchmarking (64-bits) ===\n-- blackrock-1 -- \n-- blackrock-2 -- \n'.lower
- `tests.test_absolute_final_push.test_regress_10_times`
  > AssertionError: assert (b'success' in b'=== benchmarking (64-bits) ===\n-- blackrock-1 -- \n-- blackrock-2 -- \n' or b'regression' in b'=== benchmarking (64-bits) ===\n-- blackrock-1 -- \n-- blackrock
  >  +  where b'=== benchmarking (64-bits) ===\n-- blackrock-1 -- \n-- blackrock-2 -- \n' = <built-in method lower of bytes object at 0x7f015066f8a0>()
  >  +    where <built-in method lower of bytes object at 0x7f015066f8a0> = b'=== benchmarking (64-bits) ===\n-- blackrock-1 -- \n-- blackrock-2 -- \n'.lower
  >  +      where b'=== benchmarking (64-bits) ===\n-- blackrock-1 -- \n-- blackrock-2 -- \n' = CompletedProcess(args=['/workspace/executable', '--regress'], returncode=0, stdout=b'=== benchmarking (64-bi
  >  +  and   b'=== benchmarking (64-bits) ===\n-- blackrock-1 -- \n-- blackrock-2 -- \n' = <built-in method lower of bytes object at 0x7f015066f8a0>()
  >  +    where <built-in method lower of bytes object at 0x7f015066f8a0> = b'=== benchmarking (64-bits) ===\n-- blackrock-1 -- \n-- blackrock-2 -- \n'.lower
  >  +      where b'=== benchmarking (64-bits) ===\n-- blackrock-1 -- \n-- blackrock-2 -- \n' = CompletedProcess(args=['/workspace/executable', '--regress'], returncode=0, stdout=b'=== benchmarking (64-bi
- `tests.test_coverage_final_push.test_regress_mode`
  > AssertionError: assert (b'regress' in b'=== benchmarking (64-bits) ===\n-- blackrock-1 -- \n-- blackrock-2 -- \n' or b'test' in b'=== benchmarking (64-bits) ===\n-- blackrock-1 -- \n-- blackrock-2 -- 
  >  +  where b'=== benchmarking (64-bits) ===\n-- blackrock-1 -- \n-- blackrock-2 -- \n' = <built-in method lower of bytes object at 0x7f01504ccff0>()
  >  +    where <built-in method lower of bytes object at 0x7f01504ccff0> = b'=== benchmarking (64-bits) ===\n-- blackrock-1 -- \n-- blackrock-2 -- \n'.lower
  >  +  and   b'=== benchmarking (64-bits) ===\n-- blackrock-1 -- \n-- blackrock-2 -- \n' = <built-in method lower of bytes object at 0x7f01504ccff0>()
  >  +    where <built-in method lower of bytes object at 0x7f01504ccff0> = b'=== benchmarking (64-bits) ===\n-- blackrock-1 -- \n-- blackrock-2 -- \n'.lower
  >  +  and   b'=== benchmarking (64-bits) ===\n-- blackrock-1 -- \n-- blackrock-2 -- \n' = <built-in method lower of bytes object at 0x7f01504ccff0>()
  >  +    where <built-in method lower of bytes object at 0x7f01504ccff0> = b'=== benchmarking (64-bits) ===\n-- blackrock-1 -- \n-- blackrock-2 -- \n'.lower

### `uncategorized` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_binary_edge_cases.test_binary_large_banner`
  > struct.error: ubyte format requires 0 <= number <= 255
- `tests.test_crypto.test_benchmark_blackrock2_rounds_affect_performance`
  > AttributeError: 'NoneType' object has no attribute 'group'

### `boolean_false` — 2 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `eval.tests.test_masscan_cli.test_echo_includes_sections_and_default_ports_empty`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7ffa724b8030>('[-] FAIL: failed to load libpcap shared library')
  >  +    where <built-in method startswith of str object at 0x7ffa724b8030> = ''.startswith
- `tests.test_main.test_min_max_rate_parameters`
  > assert False

### `rc_mismatch_got0_want2` — 2 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_binary_format.test_readscan_duplicate_banners`
  > assert 0 == 2
  >  +  where 0 = len([])
- `tests.test_binary_format.test_readscan_duplicates_with_banners_different_data`
  > assert 0 == 2
  >  +  where 0 = len([])

### `empty_list_or_string` — 1 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_config.test_echo_mixed_protocols`
  > IndexError: list index out of range

