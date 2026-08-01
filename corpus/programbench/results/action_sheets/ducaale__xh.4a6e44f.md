# Action Sheet — ducaale__xh.4a6e44f

**Current:** 5.51%  (78/1415)
**Pass / Fail / Skip:** 78 / 623 / 3
**Gap to 100%:** 94.49 percentage points (1337 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_10_offline_request_construction.test_json_literal_types_keycoloneq`
  - reason: test_json_literal_types_keycoloneq depends on test_json_body_keyeqvalue_default_json_and_post
- `eval.tests.test_10_offline_request_construction.test_unicode_in_json_body_is_preserved`
  - reason: test_unicode_in_json_body_is_preserved depends on test_json_body_keyeqvalue_default_json_and_post
- `eval.tests.test_20_stdin_and_errors.test_mixing_is_allowed_if_ignore_stdin`
  - reason: test_mixing_is_allowed_if_ignore_stdin depends on test_mixing_stdin_body_and_request_items_errors

## Failure clusters

623 failed tests grouped into 11 buckets (sorted by count).

### `rc_mismatch_got2_want0` — 400 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_authentication.test_basic_auth`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--offline', '-A', 'basic', '-a', 'user:password', 'http://example.com'], returncode=2, stdout=b'', stderr=b"xh: unknown option: --offline\nusage: 
- `tests.test_authentication.test_bearer_auth`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--offline', '-A', 'bearer', '-a', 'mytoken123', 'http://example.com'], returncode=2, stdout=b'', stderr=b"xh: unknown option: --offline\nusage: xh
- `tests.test_authentication.test_digest_auth`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--offline', '-A', 'digest', '-a', 'user:password', 'http://example.com'], returncode=2, stdout=b'', stderr=b"xh: unknown option: --offline\nusage:
- *(... 397 more in this cluster)*

### `other_assertion` — 167 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_version_output`
  > AssertionError: assert (b'tls' in b'xh 0.1.0\n' or b'rustls' in b'xh 0.1.0\n')
  >  +  where b'xh 0.1.0\n' = <built-in method lower of bytes object at 0x7f23e22e20d0>()
  >  +    where <built-in method lower of bytes object at 0x7f23e22e20d0> = b'xh 0.1.0\n'.lower
  >  +      where b'xh 0.1.0\n' = CompletedProcess(args=['./executable', '--version'], returncode=0, stdout=b'xh 0.1.0\n', stderr=b'').stdout
  >  +  and   b'xh 0.1.0\n' = CompletedProcess(args=['./executable', '--version'], returncode=0, stdout=b'xh 0.1.0\n', stderr=b'').stdout
- `tests.test_basic_invocation.test_help_output`
  > AssertionError: assert b'Arguments:' in b'xh 0.1.0\n\nUsage: xh [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n\nSubcommands:\n  GET, POST, PUT, DELETE, PAT
  >  +  where b'xh 0.1.0\n\nUsage: xh [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n\nSubcommands:\n  GET, POST, PUT, DELETE, PATCH, HEAD, OPTIONS  HTTP method
- `tests.test_basic_invocation.test_help_command`
  > AssertionError: assert 255 > 2000
  >  +  where 255 = len(b'xh 0.1.0\n\nUsage: xh [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n\nSubcommands:\n  GET, POST, PUT, DELETE, PATCH, HEAD, OPTIONS  H
  >  +    where b'xh 0.1.0\n\nUsage: xh [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n\nSubcommands:\n  GET, POST, PUT, DELETE, PATCH, HEAD, OPTIONS  HTTP meth
- *(... 164 more in this cluster)*

### `string_output_mismatch` — 20 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_00_cli_basics.test_version_exact_match`
  > AssertionError: assert 'xh 0.1.0\n' == 'xh 0.25.3\n-...tls +rustls\n'
  >   
  >   + xh 0.1.0
  >   - xh 0.25.3
  >   - -native-tls +rustls
- `tests.test_cli_gaps.test_help_command_shows_full_usage`
  > AssertionError: assert 'xh 0.1.0\n\n...name=John\n\n' == 'xh is a frie...N argument.\n'
  >   
  >   - xh is a friendly and fast tool for sending HTTP requests.
  >   + xh 0.1.0
  >     
  >   + Usage: xh [OPTIONS] [ARGS]
  >   - It reimplements as much as possible of HTTPie's excellent design, with a focus on improved
  >   - performance....
- `tests.test_cli_gaps.test_format_option_xml_format_unsupported`
  > assert 'xh: unknown ...nformation.\n' == "error: inval...y '--help'.\n"
  >   
  >   - error: invalid value 'xml.format:true' for '--format-options <FORMAT_OPTIONS>': Unsupported option 'xml.format'
  >   - 
  >   - For more information, try '--help'.
  >   + xh: unknown option: --format-options=xml.format:true
  >   + usage: xh [OPTIONS] [ARGS]
  >   + Try 'xh --help' for more information.
- *(... 17 more in this cluster)*

### `json_output_missing_or_bad` — 12 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `tests.test_decoder.test_x_gzip_legacy_encoding_support`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_decoder.test_large_gzip_compressed_response`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_decoder.test_multiple_content_encoding_headers_first_wins`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- *(... 9 more in this cluster)*

### `rc_mismatch_got0_want1` — 8 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_decoder.test_malformed_gzip_data_produces_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', 'http://127.0.0.1:58861/malformed-gzip'], returncode=0, stdout='this is not valid gzip data at all, just garbage bytes\n', stderr='').returncode
- `tests.test_decoder.test_truncated_gzip_data_produces_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', 'http://127.0.0.1:58861/truncated-gzip'], returncode=0, stdout='\x1f�\x08\x00\x13.\nj\x02��V�M-.NLOU�RP\n��,V(��/�IQHJU()\n', stderr='').returncode
- `tests.test_decoder.test_wrong_compression_algorithm_produces_error`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', 'http://127.0.0.1:58861/wrong-algorithm-gzip'], returncode=0, stdout='x��V�M-.NLOU�RP\n/��KWH�I�/�,��U�QPJIM�I,JM\x01I�We\x16��\x12�KJ\x13s@")�i9�%
- *(... 5 more in this cluster)*

### `boolean_false` — 6 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `eval.tests.test_00_cli_basics.test_help_has_expected_sections_and_options`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7fa08b420d40>('xh is a friendly and fast tool')
  >  +    where <built-in method startswith of str object at 0x7fa08b420d40> = 'xh 0.1.0\n\nUsage: xh [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n\nSubcomman
- `tests.test_download.test_download_multiple_file_collisions`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpgy7z0b5v/file.txt-2').exists
- `tests.test_download.test_download_binary_content_exact_bytes`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpt55deqv6/binary.bin').exists
- *(... 3 more in this cluster)*

### `bytes_output_mismatch` — 5 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_ssl_tls.test_ssl_version_tls1`
  > assert (2 == 0 or b'rustls' in b"xh: unknown option: --offline\nusage: xh [OPTIONS] [ARGS]\nTry 'xh --help' for more information.\n")
  >  +  where 2 = CompletedProcess(args=['./executable', '--offline', '-I', '--ssl', 'tls1', 'https://example.com'], returncode=2, stdout=b'', stderr=b"xh: unknown option: --offline\nusage: xh [OPTIONS] [
  >  +  and   b"xh: unknown option: --offline\nusage: xh [OPTIONS] [ARGS]\nTry 'xh --help' for more information.\n" = CompletedProcess(args=['./executable', '--offline', '-I', '--ssl', 'tls1', 'https://ex
- `tests.test_ssl_tls.test_ssl_version_tls1_1`
  > assert (2 == 0 or b'rustls' in b"xh: unknown option: --offline\nusage: xh [OPTIONS] [ARGS]\nTry 'xh --help' for more information.\n")
  >  +  where 2 = CompletedProcess(args=['./executable', '--offline', '-I', '--ssl', 'tls1.1', 'https://example.com'], returncode=2, stdout=b'', stderr=b"xh: unknown option: --offline\nusage: xh [OPTIONS]
  >  +  and   b"xh: unknown option: --offline\nusage: xh [OPTIONS] [ARGS]\nTry 'xh --help' for more information.\n" = CompletedProcess(args=['./executable', '--offline', '-I', '--ssl', 'tls1.1', 'https://
- `tests.test_ssl_tls.test_cert_option`
  > assert (2 == 0 or b'cert' in b"xh: unknown option: --offline\nusage: xh [options] [args]\ntry 'xh --help' for more information.\n")
  >  +  where 2 = CompletedProcess(args=['./executable', '--offline', '-I', '--cert', '/tmp/tmp8wp8s7qm/cert.pem', 'https://example.com'], returncode=2, stdout=b'', stderr=b"xh: unknown option: --offline\
  >  +  and   b"xh: unknown option: --offline\nusage: xh [options] [args]\ntry 'xh --help' for more information.\n" = <built-in method lower of bytes object at 0x7f23e105c630>()
  >  +    where <built-in method lower of bytes object at 0x7f23e105c630> = b"xh: unknown option: --offline\nusage: xh [OPTIONS] [ARGS]\nTry 'xh --help' for more information.\n".lower
  >  +      where b"xh: unknown option: --offline\nusage: xh [OPTIONS] [ARGS]\nTry 'xh --help' for more information.\n" = CompletedProcess(args=['./executable', '--offline', '-I', '--cert', '/tmp/tmp8wp8s
- *(... 2 more in this cluster)*

### `returned_none` — 2 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_usage.test_help_has_usage_section`
  > AssertionError: assert None is not None
  >  +  where None = <function search at 0x7f6faf3ca680>('^Usage:\\s+executable\\b', 'xh 0.1.0\n\nUsage: xh [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n\nSub
  >  +    where <function search at 0x7f6faf3ca680> = re.search
  >  +    and   re.MULTILINE = re.M
- `eval.tests.test_help_usage.test_help_has_arguments_and_options_sections`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f6faf3ca680>('^Arguments:\\s*$', 'xh 0.1.0\n\nUsage: xh [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n\nSubcommands
  >  +    where <function search at 0x7f6faf3ca680> = re.search
  >  +    and   re.MULTILINE = re.M

### `rc_mismatch_got1_want0` — 1 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_externalized_internal_suite.test_ext_multiple_headers_with_same_key`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'http://127.0.0.1:45315', 'hello:world', 'hello:people'], returncode=1, stdout=b'', stderr=b'Traceback (most recent call last):\n  File "/

### `rc_mismatch_got0_want4` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_externalized_internal_suite.test_ext_check_status_404_exits_4`
  > AssertionError: assert 0 == 4
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'http://127.0.0.1:41687'], returncode=0, stdout=b'', stderr=b'').returncode

### `rc_unexpected_zero` — 1 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `eval.tests.test_help_usage.test_dash_h_is_headers_shortcut_not_help`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-h'], returncode=0, stdout='xh 0.1.0\n\nUsage: xh [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print versi

