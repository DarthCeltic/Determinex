# Action Sheet — mkj__dropbear.75f699b

**Current:** 23.24%  (234/1007)
**Pass / Fail / Skip:** 234 / 331 / 6
**Gap to 100%:** 76.76 percentage points (773 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_environment_motd.test_ssh_tty_set_for_pty_session`
  - reason: PTY allocation requires interactive terminal
- `tests.test_harvest.test_signal`
  - reason: Not yet implemented in dropbear
- `tests.test_harvest.test_reexec`
  - reason: Requires permission to read /proc/PID/maps - needs special container capabilities
- `tests.test_harvest.test_pubkeyinfo`
  - reason: Requires specific keyfile and authorized_keys setup (DBTEST_IN_ACTION)
- `tests.test_harvest.test_pubkeyinfo_special`
  - reason: Requires specific keyfile and authorized_keys setup (DBTEST_IN_ACTION)
- *(... 1 more skipped)*

## Failure clusters

331 failed tests grouped into 8 buckets (sorted by count).

### `other_assertion` — 235 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_dropbear_cli.test_help_with_invalid_option`
  > assert (b'Invalid option' in b'  File "/workspace/main.py", line 61\n    ORACLE_MEMOS = [{\'argv\': [\'-r\'], \'rc\': 1, \'golden_files\': [\'missing_hostkeys.golden\', \'unreadable_hostkey.golden\']}
  >  +  where b'  File "/workspace/main.py", line 61\n    ORACLE_MEMOS = [{\'argv\': [\'-r\'], \'rc\': 1, \'golden_files\': [\'missing_hostkeys.golden\', \'unreadable_hostkey.golden\']}, {\'argv\': [\'-V\
  >  +  and   b'  File "/workspace/main.py", line 61\n    ORACLE_MEMOS = [{\'argv\': [\'-r\'], \'rc\': 1, \'golden_files\': [\'missing_hostkeys.golden\', \'unreadable_hostkey.golden\']}, {\'argv\': [\'-V\
- `tests.test_dropbear_cli.test_no_hostkeys_error`
  > assert (b'No hostkeys available' in b'  File "/workspace/main.py", line 61\n    ORACLE_MEMOS = [{\'argv\': [\'-r\'], \'rc\': 1, \'golden_files\': [\'missing_hostkeys.golden\', \'unreadable_hostkey.gol
  >  +  where b'  File "/workspace/main.py", line 61\n    ORACLE_MEMOS = [{\'argv\': [\'-r\'], \'rc\': 1, \'golden_files\': [\'missing_hostkeys.golden\', \'unreadable_hostkey.golden\']}, {\'argv\': [\'-V\
  >  +  and   b'  File "/workspace/main.py", line 61\n    ORACLE_MEMOS = [{\'argv\': [\'-r\'], \'rc\': 1, \'golden_files\': [\'missing_hostkeys.golden\', \'unreadable_hostkey.golden\']}, {\'argv\': [\'-V\
- `tests.test_01_basic_invocation.test_invalid_option_shows_usage`
  > assert (b'Usage:' in b'  File "/workspace/main.py", line 61\n    ORACLE_MEMOS = [{\'argv\': [\'-r\'], \'rc\': 1, \'golden_files\': [\'missing_hostkeys.golden\', \'unreadable_hostkey.golden\']}, {\'arg
  >  +  where b'  File "/workspace/main.py", line 61\n    ORACLE_MEMOS = [{\'argv\': [\'-r\'], \'rc\': 1, \'golden_files\': [\'missing_hostkeys.golden\', \'unreadable_hostkey.golden\']}, {\'argv\': [\'-V\
  >  +  and   b'  File "/workspace/main.py", line 61\n    ORACLE_MEMOS = [{\'argv\': [\'-r\'], \'rc\': 1, \'golden_files\': [\'missing_hostkeys.golden\', \'unreadable_hostkey.golden\']}, {\'argv\': [\'-V\
  >  +  and   b'  File "/workspace/main.py", line 61\n    ORACLE_MEMOS = [{\'argv\': [\'-r\'], \'rc\': 1, \'golden_files\': [\'missing_hostkeys.golden\', \'unreadable_hostkey.golden\']}, {\'argv\': [\'-V\
- *(... 232 more in this cluster)*

### `uncategorized` — 45 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_07_comprehensive_final.test_all_boolean_flags_individually`
  > NameError: name 'output' is not defined
- `tests.test_07_comprehensive_final.test_all_value_flags_with_defaults`
  > NameError: name 'output' is not defined
- `tests.test_07_comprehensive_final.test_option_combinations_exhaustive`
  > NameError: name 'output' is not defined
- *(... 42 more in this cluster)*

### `rc_mismatch_got1_want0` — 21 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_dropbear_cli.test_version_flag`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-V'], returncode=1, stdout=b'', stderr=b'  File "/workspace/main.py", line 61\n    ORACLE_MEMOS = [{\'argv\': [\'-r\'], \'rc\': 1, \'gold
- `tests.test_01_basic_invocation.test_version_flag`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-V'], returncode=1, stdout=b'', stderr=b'  File "/workspace/main.py", line 61\n    ORACLE_MEMOS = [{\'argv\': [\'-r\'], \'rc\': 1, \'gold
- `tests.test_06_coverage_targeted.test_exit_code_on_success`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-V'], returncode=1, stdout=b'', stderr=b'  File "/workspace/main.py", line 61\n    ORACLE_MEMOS = [{\'argv\': [\'-r\'], \'rc\': 1, \'gold
- *(... 18 more in this cluster)*

### `string_output_mismatch` — 20 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_help_baseline.test_help_matches_baseline_fixture_minus_version_and_path`
  > assert '  File "/wor...hesis \'[\'\n' == 'Dropbear ser...    Version\n'
  >   
  >   +   File "/workspace/main.py", line 61
  >   +     ORACLE_MEMOS = [{'argv': ['-r'], 'rc': 1, 'golden_files': ['missing_hostkeys.golden', 'unreadable_hostkey.golden']}, {'argv': ['-V'], 'rc': 0, 'golden_files': ['help_output.golden', 'version_o
  >   +                                                                                                                                                                                                     
  >   
  >   ...Full output truncated (42 lines hidden), use '-vv' to show
- `tests.test_cli_basic.TestVersionAndHelp.test_version_output_exact`
  > assert '  File "/wor...hesis \'[\'\n' == 'Dropbear v2025.89\n'
  >   
  >   - Dropbear v2025.89
  >   +   File "/workspace/main.py", line 61
  >   +     ORACLE_MEMOS = [{'argv': ['-r'], 'rc': 1, 'golden_files': ['missing_hostkeys.golden', 'unreadable_hostkey.golden']}, {'argv': ['-V'], 'rc': 0, 'golden_files': ['help_output.golden', 'version_o
  >   +                                                                                                                                                                                                     
  >   
  >   ...Full output truncated (2 lines hidden), use '-vv' to show
- `tests.test_cli_basics.test_long_help_is_invalid_option_matches_golden`
  > assert '  File "/wor...hesis \'[\'\n' == 'Invalid opti...    Version\n'
  >   
  >   +   File "/workspace/main.py", line 61
  >   +     ORACLE_MEMOS = [{'argv': ['-r'], 'rc': 1, 'golden_files': ['missing_hostkeys.golden', 'unreadable_hostkey.golden']}, {'argv': ['-V'], 'rc': 0, 'golden_files': ['help_output.golden', 'version_o
  >   +                                                                                                                                                                                                     
  >   
  >   ...Full output truncated (43 lines hidden), use '-vv' to show
- *(... 17 more in this cluster)*

### `rc_mismatch_got255_want0` — 6 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_ecdsa_gap.test_ecdsa_nistp256_pubkey_auth_signature_verification`
  > AssertionError: assert 255 == 0
  >  +  where 255 = CompletedProcess(args=['ssh', '-o', 'StrictHostKeyChecking=no', '-o', 'UserKnownHostsFile=/dev/null', '-o', 'BatchMode=yes', '-o', 'ConnectTimeout=2', '-i', '/root/keys_k68ui85f/client
- `tests.test_ecdsa_gap.test_ecdsa_nistp384_pubkey_auth_signature_verification`
  > AssertionError: assert 255 == 0
  >  +  where 255 = CompletedProcess(args=['ssh', '-o', 'StrictHostKeyChecking=no', '-o', 'UserKnownHostsFile=/dev/null', '-o', 'BatchMode=yes', '-o', 'ConnectTimeout=2', '-i', '/root/keys_jn6zlibp/client
- `tests.test_ecdsa_gap.test_ecdsa_nistp521_pubkey_auth_signature_verification`
  > AssertionError: assert 255 == 0
  >  +  where 255 = CompletedProcess(args=['ssh', '-o', 'StrictHostKeyChecking=no', '-o', 'UserKnownHostsFile=/dev/null', '-o', 'BatchMode=yes', '-o', 'ConnectTimeout=2', '-i', '/root/keys_igc_ud8i/client
- *(... 3 more in this cluster)*

### `returned_none` — 2 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_07_comprehensive_final.test_version_is_correct_format`
  > assert None
  >  +  where None = <function search at 0x7f9ad6e3b760>(b'Dropbear\\s+v?\\d{4}\\.\\d+', b'  File "/workspace/main.py", line 61\n    ORACLE_MEMOS = [{\'argv\': [\'-r\'], \'rc\': 1, \'golden_files\': [\'mi
  >  +    where <function search at 0x7f9ad6e3b760> = re.search
- `tests.test_help_exit_and_streams.test_help_has_usage_line`
  > assert None
  >  +  where None = <function search at 0x7f64ec712680>('^Usage:\\s+\\S*executable\\s+\\[options\\]\\s*$', '  File "/workspace/main.py", line 61\n    ORACLE_MEMOS = [{\'argv\': [\'-r\'], \'rc\': 1, \'gol
  >  +    where <function search at 0x7f64ec712680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE

### `missing_file` — 1 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_dropbear_cli.test_multiple_hostkey_files`
  > FileNotFoundError: [Errno 2] No such file or directory: '/workspace/dropbearkey'

### `boolean_false` — 1 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_cli_basics.test_unknown_short_option_is_invalid_option`
  > assert False
  >  +  where False = <built-in method startswith of str object at 0x563f695887d0>('Invalid option -Z\n')
  >  +    where <built-in method startswith of str object at 0x563f695887d0> = '  File "/workspace/main.py", line 61\n    ORACLE_MEMOS = [{\'argv\': [\'-r\'], \'rc\': 1, \'golden_files\': [\'missing_hostk

