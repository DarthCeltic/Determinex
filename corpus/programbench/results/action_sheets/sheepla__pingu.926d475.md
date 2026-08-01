# Action Sheet — sheepla__pingu.926d475

**Current:** 5.45%  (28/514)
**Pass / Fail / Skip:** 28 / 385 / 6
**Gap to 100%:** 94.55 percentage points (486 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_pingu.test_version_format`
  - reason: test_version_format depends on test_help_exact_usage_block
- `eval.tests.test_pingu.test_ping_count_2_produces_two_sequences`
  - reason: test_ping_count_2_produces_two_sequences depends on test_ping_count_1_localhost_core_structure
- `eval.tests.test_pingu.test_ping_long_count_flag_equivalent`
  - reason: test_ping_long_count_flag_equivalent depends on test_ping_count_1_localhost_core_structure
- `tests.test_art_rendering.test_renderASCIIArt_wraparound_at_40`
  - reason: Too slow (45 pings); core wraparound logic tested in wraparound_at_20
- `tests.test_art_rendering.test_renderASCIIArt_wraparound_high_index`
  - reason: Too slow (105 pings); core wraparound logic tested in wraparound_at_20
- *(... 1 more skipped)*

## Failure clusters

385 failed tests grouped into 11 buckets (sorted by count).

### `other_assertion` — 187 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_pingu.test_help_short_flag`
  > AssertionError: assert b'pingu [OPTIONS] HOST' in b'pingu 0.1.0 - bootstrap scaffold\n\nUsage: pingu [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n'
  >  +  where b'pingu 0.1.0 - bootstrap scaffold\n\nUsage: pingu [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['./executable', '-h']
- `tests.test_pingu.test_help_long_flag`
  > AssertionError: assert b'pingu [OPTIONS] HOST' in b'pingu 0.1.0 - bootstrap scaffold\n\nUsage: pingu [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n'
  >  +  where b'pingu 0.1.0 - bootstrap scaffold\n\nUsage: pingu [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['./executable', '--he
- `tests.test_pingu.test_version_short_flag`
  > AssertionError: assert b'pingu:' in b'pingu 0.1.0\n'
  >  +  where b'pingu 0.1.0\n' = CompletedProcess(args=['./executable', '-V'], returncode=0, stdout=b'pingu 0.1.0\n', stderr=b'').stdout
- *(... 184 more in this cluster)*

### `rc_mismatch_got2_want0` — 106 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_pingu.test_count_short_flag`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '-c', '2', 'localhost'], returncode=2, stdout=b'', stderr=b"pingu: unknown option: -c\nusage: pingu [OPTIONS] [ARGS]\nTry 'pingu --help' for more i
- `tests.test_pingu.test_count_long_flag`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--count', '3', 'localhost'], returncode=2, stdout=b'', stderr=b"pingu: unknown option: --count\nusage: pingu [OPTIONS] [ARGS]\nTry 'pingu --help' 
- `tests.test_pingu.test_count_single_packet`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '-c', '1', 'localhost'], returncode=2, stdout=b'', stderr=b"pingu: unknown option: -c\nusage: pingu [OPTIONS] [ARGS]\nTry 'pingu --help' for more i
- *(... 103 more in this cluster)*

### `rc_mismatch_got2_want1` — 39 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_pingu.test_no_arguments_error`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['./executable'], returncode=2, stdout=b'', stderr=b"usage: pingu [OPTIONS] [ARGS]\nTry 'pingu --help' for more information.\n").returncode
- `tests.test_pingu.test_count_invalid_value`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['./executable', '-c', 'abc', 'localhost'], returncode=2, stdout=b'', stderr=b"pingu: unknown option: -c\nusage: pingu [OPTIONS] [ARGS]\nTry 'pingu --help' for more
- `tests.test_pingu.test_no_arguments`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['./executable'], returncode=2, stdout=b'', stderr=b"usage: pingu [OPTIONS] [ARGS]\nTry 'pingu --help' for more information.\n").returncode
- *(... 36 more in this cluster)*

### `rc_mismatch_got0_want1` — 16 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_pingu.test_too_many_arguments_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', 'host1', 'host2'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_pingu.test_too_many_arguments`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', 'host1', 'host2'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_pingu.test_three_arguments_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', 'host1', 'host2', 'host3'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 13 more in this cluster)*

### `string_output_mismatch` — 16 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_cli.TestHelpOption.test_help_flag_long`
  > AssertionError: assert 'pingu 0.1.0 ...int version\n' == 'Usage:\n  pi...p message\n\n'
  >   
  >   + pingu 0.1.0 - bootstrap scaffold
  >   - Usage:
  >   -   pingu [OPTIONS] HOST
  >     
  >   - `ping` command but with pingu
  >   + Usage: pingu [OPTIONS] [ARGS]...
- `tests.test_cli.TestHelpOption.test_help_flag_short`
  > AssertionError: assert 'pingu 0.1.0 ...int version\n' == 'Usage:\n  pi...p message\n\n'
  >   
  >   + pingu 0.1.0 - bootstrap scaffold
  >   - Usage:
  >   -   pingu [OPTIONS] HOST
  >     
  >   - `ping` command but with pingu
  >   + Usage: pingu [OPTIONS] [ARGS]...
- `tests.test_errors.test_invalid_hostname_lookup_failure`
  > AssertionError: assert '' == '[ ERROR ] an...o such host\n'
  >   
  >   - [ ERROR ] an error occurred while initializing pinger: failed to init pinger lookup invalid-host-12345-nonexistent.example.com on 10.0.0.2:53: no such host
- *(... 13 more in this cluster)*

### `boolean_false` — 11 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_cli.TestVersionOption.test_version_flag_long`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7f3e52193cb0>('pingu: v')
  >  +    where <built-in method startswith of str object at 0x7f3e52193cb0> = 'pingu 0.1.0\n'.startswith
- `tests.test_cli.TestVersionOption.test_version_flag_short`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7f3e5217f830>('pingu: v')
  >  +    where <built-in method startswith of str object at 0x7f3e5217f830> = 'pingu 0.1.0\n'.startswith
- `eval.tests.test_pingu.test_help_exact_usage_block`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7f27e8c96430>('Usage:\n  pingu [OPTIONS] HOST\n\n`ping` command but with pingu\n\nApplication Options:\n  -c, --count=     Stop after <
  >  +    where <built-in method startswith of str object at 0x7f27e8c96430> = 'pingu 0.1.0 - bootstrap scaffold\n\nUsage: pingu [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version 
- *(... 8 more in this cluster)*

### `returned_none` — 6 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_pingu.test_ping_displays_ttl`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f56ede3e680>(b'ttl=\\d+', b'')
  >  +    where <function search at 0x7f56ede3e680> = re.search
  >  +    and   b'' = CompletedProcess(args=['./executable', 'localhost', '-c', '1'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_pingu.test_ping_displays_bytes`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f56ede3e680>(b'\\d+bytes from', b'')
  >  +    where <function search at 0x7f56ede3e680> = re.search
  >  +    and   b'' = CompletedProcess(args=['./executable', 'localhost', '-c', '1'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_pingu.test_ping_displays_time`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f56ede3e680>(b'time=[\\d.]+\\xc2\\xb5s', b'')
  >  +    where <function search at 0x7f56ede3e680> = re.search
  >  +    and   b'' = CompletedProcess(args=['./executable', 'localhost', '-c', '1'], returncode=0, stdout=b'', stderr=b'').stdout
- *(... 3 more in this cluster)*

### `rc_mismatch_got0_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_pingu.test_output_multiple_ascii_art_lines`
  > assert 0 == 3
  >  +  where 0 = len([])

### `bytes_output_mismatch` — 1 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_pingu.test_statistics_separator_line`
  > AssertionError: assert (b'\xe2\x94\x80' in b'' or b'---' in b'' or b'===' in b'')
  >  +  where b'' = CompletedProcess(args=['./executable', 'localhost', '-c', '1'], returncode=0, stdout=b'', stderr=b'').stdout
  >  +  and   b'' = CompletedProcess(args=['./executable', 'localhost', '-c', '1'], returncode=0, stdout=b'', stderr=b'').stdout
  >  +  and   b'' = CompletedProcess(args=['./executable', 'localhost', '-c', '1'], returncode=0, stdout=b'', stderr=b'').stdout

### `rc_mismatch_got0_want5` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_pingu.test_ascii_art_cycles_through_all_lines`
  > assert 0 == 5
  >  +  where 0 = len([])

### `rc_unexpected_zero` — 1 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_flags.test_too_many_arguments_error`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'host1', 'host2'], returncode=0, stdout='', stderr='').returncode

