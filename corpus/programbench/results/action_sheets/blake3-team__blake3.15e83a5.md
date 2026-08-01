# Action Sheet — blake3-team__blake3.15e83a5

**Current:** 5.26%  (36/685)
**Pass / Fail / Skip:** 36 / 311 / 3
**Gap to 100%:** 94.74 percentage points (649 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_harvest.test_slash_normalization_on_windows`
  - reason: Windows-specific test
- `tests.test_harvest.test_invalid_unicode_on_windows`
  - reason: Windows-specific test
- `tests.test_io.test_permission_denied_error`
  - reason: Cannot test permission denied as root

## Failure clusters

311 failed tests grouped into 14 buckets (sorted by count).

### `string_output_mismatch` — 96 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_advanced.test_length_default_32_bytes`
  > AssertionError: assert '3ab47fccc073...59c6649457f0e' == '8e3d0e03b2a5...cce6aa075a891'
  >   
  >   - 8e3d0e03b2a56699b6f40000b6f3c48dbe7a8d347be15f57993cce6aa075a891
  >   + 3ab47fccc073c1f8eacc04a901b45a9dcf2f12d50495bb7e42b59c6649457f0e
- `tests.test_advanced.test_length_16_bytes`
  > AssertionError: assert '9566ade5c8ec...a371bff47c20d' == '8e3d0e03b2a5...40000b6f3c48d'
  >   
  >   - 8e3d0e03b2a56699b6f40000b6f3c48d
  >   + 9566ade5c8ec9290af4a371bff47c20d
- `tests.test_advanced.test_length_64_bytes`
  > AssertionError: assert 'df4fbad4a336...e1e8565db143f' == '8e3d0e03b2a5...faec5f0914edd'
  >   
  >   - 8e3d0e03b2a56699b6f40000b6f3c48dbe7a8d347be15f57993cce6aa075a891936c2866e23d2fd38b168f03eeb2d6ff0715f7b29e790e1d808faec5f0914edd
  >   + df4fbad4a33625b6fb76f953dfa0129abf8d769e9a32af863fc0c0ce4fd8884c1ad13a4a397b475fcbbcd3b43e74b1782e6bc32bd092cc5f767e1e8565db143f
- *(... 93 more in this cluster)*

### `rc_mismatch_got2_want0` — 82 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_advanced.test_seek_offset_10`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--seek', '10', '/workspace/eval/test_resources/test_advanced/sample.txt'], returncode=2, stdout=b'', stderr=b'blake3: error: unrecognized
- `tests.test_advanced.test_seek_offset_32`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--seek', '32', '/workspace/eval/test_resources/test_advanced/sample.txt'], returncode=2, stdout=b'', stderr=b'blake3: error: unrecognized
- `tests.test_advanced.test_seek_offset_100`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--seek', '100', '/workspace/eval/test_resources/test_advanced/sample.txt'], returncode=2, stdout=b'', stderr=b'blake3: error: unrecognize
- *(... 79 more in this cluster)*

### `rc_mismatch_got1_want0` — 56 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_advanced.test_length_zero`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '--length', '0', '/workspace/eval/test_resources/test_advanced/sample.txt'], returncode=1, stdout=b'', stderr=b"blake3: error: error readi
- `tests.test_advanced.test_length_with_derive_key_mode`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '--derive-key', 'test context', '--length', '64', '/workspace/eval/test_resources/test_advanced/sample.txt'], returncode=1, stdout=b'', st
- `tests.test_advanced.test_length_with_stdin`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '--length', '16', '-'], returncode=1, stdout=b'', stderr=b"blake3: error: no such file: '-'\n").returncode
- *(... 53 more in this cluster)*

### `bytes_output_mismatch` — 34 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_advanced.test_length_1_byte`
  > AssertionError: assert '5b' == '8e'
  >   
  >   - 8e
  >   + 5b
- `tests.test_advanced.test_length_1_raw_output`
  > AssertionError: assert '5b' == '8e'
  >   
  >   - 8e
  >   + 5b
- `tests.test_basic.test_file_empty`
  > AssertionError: assert b'0e5751c026e...  empty.txt\n' == b'af1349b9f5f...  empty.txt\n'
  >   
  >   At index 0 diff: b'0' != b'a'
  >   
  >   Full diff:
  >   - (b'af1349b9f5f9a1a6a0404dea36dcc9499bcb25c9adc112b7cc9a93cae41f3262  empty.'
  >   + (b'0e5751c026e543b2e8ab2eb06099daa1d1e5df47778f7787faab45cdf12fe3a8  empty.'
  >      b'txt\n')
- *(... 31 more in this cluster)*

### `other_assertion` — 20 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic.test_test_vectors_official`
  > AssertionError: Test vector 0 bytes failed
  > assert '0e5751c026e5...b45cdf12fe3a8' == 'af1349b9f5f9...a93cae41f3262'
  >   
  >   - af1349b9f5f9a1a6a0404dea36dcc9499bcb25c9adc112b7cc9a93cae41f3262
  >   + 0e5751c026e543b2e8ab2eb06099daa1d1e5df47778f7787faab45cdf12fe3a8
- `tests.test_basic.test_test_vectors_multiple_sizes`
  > AssertionError: Test vector 2 bytes failed: expected 7b7015bb92cf0b318037702a6cdd81dee41224f734684c2c122cd6359cb1ee63, got 01cf79da4945c370c68b265ef70641aaa65eaa8f5953e3900d97724c2c5aa095
  > assert '01cf79da4945...7724c2c5aa095' == '7b7015bb92cf...cd6359cb1ee63'
  >   
  >   - 7b7015bb92cf0b318037702a6cdd81dee41224f734684c2c122cd6359cb1ee63
  >   + 01cf79da4945c370c68b265ef70641aaa65eaa8f5953e3900d97724c2c5aa095
- `tests.test_edge_cases_final.test_keyed_mode_with_escaped_filename`
  > AssertionError: blake3: error: invalid key format
  >   
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--keyed', 'key\nfile.txt'], returncode=2, stdout=b'', stderr=b'blake3: error: invalid key format\n').returncode
- *(... 17 more in this cluster)*

### `rc_mismatch_got2_want1` — 6 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_errors.test_keyed_mode_cannot_use_stdin_dash`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--keyed', '-'], returncode=2, stdout=b'', stderr=b'blake3: error: key must be 32 bytes\n').returncode
- `tests.test_errors.test_keyed_mode_key_too_short`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--keyed', '/tmp/tmpry6cn14m'], returncode=2, stdout=b'', stderr=b'blake3: error: invalid key format\n').returncode
- `tests.test_errors.test_keyed_mode_key_too_long`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--keyed', '/tmp/tmp3bs08ole'], returncode=2, stdout=b'', stderr=b'blake3: error: invalid key format\n').returncode
- *(... 3 more in this cluster)*

### `boolean_false` — 4 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_advanced.test_length_64_raw_output`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7f3b897ef870>('8e3d0e03b2a56699b6f40000b6f3c48dbe7a8d347be15f57993cce6aa075a891')
  >  +    where <built-in method startswith of str object at 0x7f3b897ef870> = 'df4fbad4a33625b6fb76f953dfa0129abf8d769e9a32af863fc0c0ce4fd8884c1ad13a4a397b475fcbbcd3b43e74b1782e6bc32bd092cc5f767e1e8565db
- `tests.test_errors.test_filename_with_backslashes_escaped`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7f3b898d1890>('\\')
  >  +    where <built-in method startswith of str object at 0x7f3b898d1890> = '579da00778a5b4567c94630399203935f7d84bb2c457e56537e36a56ff490a4a  /tmp/tmp0uonhnvs/file\\with\\backslash.txt'.startswith
- `tests.test_errors.test_filename_with_carriage_return_escaped`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7f3b898d05d0>('\\')
  >  +    where <built-in method startswith of str object at 0x7f3b898d05d0> = '579da00778a5b4567c94630399203935f7d84bb2c457e56537e36a56ff490a4a  /tmp/tmpyihzwx6g/file\rwith\rCR.txt'.startswith
- *(... 1 more in this cluster)*

### `subprocess_failed` — 4 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_guts_coverage.test_chunk_state_via_normal_hash`
  > subprocess.CalledProcessError: Command '['/workspace/executable']' returned non-zero exit status 2.
- `tests.test_guts_coverage.test_multi_chunk_hash_exercises_parent_cv`
  > subprocess.CalledProcessError: Command '['/workspace/executable']' returned non-zero exit status 2.
- `tests.test_guts_coverage.test_guts_constants_are_correct`
  > subprocess.CalledProcessError: Command '['/workspace/executable']' returned non-zero exit status 2.
- *(... 1 more in this cluster)*

### `rc_unexpected_zero` — 2 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_advanced.test_raw_mode_multiple_files_error`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--raw', '/workspace/eval/test_resources/test_advanced/file1.txt', '/workspace/eval/test_resources/test_advanced/file2.txt'], returncode=0
- `tests.test_harvest.test_raw_with_multi_files_is_an_error`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--raw', '/tmp/tmpp3shyfwr', '/tmp/tmp0vxifdfy'], returncode=0, stdout=b'\x0eWQ\xc0&\xe5C\xb2\xe8\xab.\xb0`\x99\xda\xa1\xd1\xe5\xdfGw\x8fw

### `rc_mismatch_got0_want1` — 2 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_basic.test_raw_multiple_files_error`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--raw', '/workspace/eval/test_resources/test_basic/small.txt', '/workspace/eval/test_resources/test_basic/empty.txt'], returncode=0, stdo
- `tests.test_check.test_check_empty_filename_rejected`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--check', 'empty_filename.checksum'], returncode=0, stdout=b'', stderr=b'').returncode

### `empty_list_or_string` — 2 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_io.test_file_just_under_16kb`
  > IndexError: list index out of range
- `tests.test_io.test_file_just_over_16kb`
  > IndexError: list index out of range

### `rc_mismatch_got128_want2048` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_advanced.test_length_very_large_1024_bytes`
  > AssertionError: assert 128 == 2048
  >  +  where 128 = len('df4fbad4a33625b6fb76f953dfa0129abf8d769e9a32af863fc0c0ce4fd8884c1ad13a4a397b475fcbbcd3b43e74b1782e6bc32bd092cc5f767e1e8565db143f')

### `rc_mismatch_got3_want1` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_errors.test_filename_with_newlines_escaped`
  > AssertionError: assert 3 == 1
  >  +  where 3 = len(['579da00778a5b4567c94630399203935f7d84bb2c457e56537e36a56ff490a4a  /tmp/tmpatcvln9l/file', 'with', 'newlines.txt'])

### `rc_mismatch_got64_want100` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_harvest.test_hash_length_and_seek`
  > AssertionError: assert 64 == 100
  >  +  where 64 = len(b'\xca\x00#0\xe6\x9d>k\x84\xa4jV\xa6S?\xd7\x9dQ\xd9z;\xb7\xca\xd6\xc2\xffC\xb3T\x18]m\xc1\xe7#\xfb=\xb4\xae\x077\xe1 7\x84$\xc7\x14\xbb\x98-\x9d\xc5\xbb\xd7\xa0\xab1\x82@\xdd\xd1\x8

