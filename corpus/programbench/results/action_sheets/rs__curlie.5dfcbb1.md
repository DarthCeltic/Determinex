# Action Sheet — rs__curlie.5dfcbb1

**Current:** 9.03%  (102/1130)
**Pass / Fail / Skip:** 102 / 639 / 0
**Gap to 100%:** 90.97 percentage points (1028 tests)

## Failure clusters

639 failed tests grouped into 11 buckets (sorted by count).

### `rc_mismatch_got2_want0` — 481 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_basic.test_help_no_args`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable'], returncode=2, stdout=b'', stderr=b"usage: curlie [OPTIONS] <url>\nTry 'curlie --help' for more information.\n").returncode
- `tests.test_curl_passthrough.test_curl_header_flag_short`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--curl', '-H', 'X-Test: Value', 'http://example.com'], returncode=2, stdout=b'', stderr=b'curlie: unknown option: --curl\n').returncode
- `tests.test_curl_passthrough.test_curl_header_flag_long`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--curl', '--header', 'X-Test: Value', 'http://example.com'], returncode=2, stdout=b'', stderr=b'curlie: unknown option: --curl\n').returncode
- *(... 478 more in this cluster)*

### `other_assertion` — 118 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic.test_version_flag`
  > AssertionError: assert b'libcurl' in b'curlie 0.1.0\n'
  >  +  where b'curlie 0.1.0\n' = CompletedProcess(args=['./executable', '--version'], returncode=0, stdout=b'curlie 0.1.0\n', stderr=b'').stdout
- `tests.test_basic.test_help_flag`
  > assert b'[METHOD] URL' in b"curlie 0.1.0\n\nUsage:\n  curlie [options] <method> <url>\n  curlie [options] <url>\n\nOptions:\n  -X, --request <method>  Specify request method\n  -H, --header <header>  
  >  +  where b"curlie 0.1.0\n\nUsage:\n  curlie [options] <method> <url>\n  curlie [options] <url>\n\nOptions:\n  -X, --request <method>  Specify request method\n  -H, --header <header>   Pass custom hea
- `tests.test_basic.test_help_long_flag`
  > assert b'[METHOD] URL' in b"curlie 0.1.0\n\nUsage:\n  curlie [options] <method> <url>\n  curlie [options] <url>\n\nOptions:\n  -X, --request <method>  Specify request method\n  -H, --header <header>  
  >  +  where b"curlie 0.1.0\n\nUsage:\n  curlie [options] <method> <url>\n  curlie [options] <url>\n\nOptions:\n  -X, --request <method>  Specify request method\n  -H, --header <header>   Pass custom hea
- *(... 115 more in this cluster)*

### `string_output_mismatch` — 17 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_argparse_validation.test_combined_short_flags_equivalent_for_output[args_a0-args_b0]`
  > AssertionError: assert (2, '', 'curl...option: -I\n') == (2, '', 'curl...ption: -Is\n')
  >   
  >   At index 2 diff: 'curlie: unknown option: -I\n' != 'curlie: unknown option: -Is\n'
  >   
  >   Full diff:
  >     (
  >         2,
  >         '',...
- `eval.tests.test_argparse_validation.test_combined_short_flags_equivalent_for_output[args_a1-args_b1]`
  > AssertionError: assert (2, '', 'curl...option: -I\n') == (2, '', 'curl...ption: -Is\n')
  >   
  >   At index 2 diff: 'curlie: unknown option: -I\n' != 'curlie: unknown option: -Is\n'
  >   
  >   Full diff:
  >     (
  >         2,
  >         '',...
- `eval.tests.test_help_main.test_baseline_full_help_matches_fixture`
  > AssertionError: assert 'curlie 0.1.0...example.com\n' == 'Usage: ./exe...put of curl\n'
  >   
  >   + curlie 0.1.0
  >   - Usage: ./executable [options...] [METHOD] URL [REQUEST_ITEM [REQUEST_ITEM ...]]
  >   - Invalid category provided, here is a list of all categories:
  >     
  >   -  auth        Different types of authentication methods
  >   -  connection  Low level networking operations...
- *(... 14 more in this cluster)*

### `rc_mismatch_got6_want0` — 6 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic.test_version_command`
  > AssertionError: assert 6 == 0
  >  +  where 6 = CompletedProcess(args=['./executable', 'version'], returncode=6, stdout=b'', stderr=b'  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current\n                   
- `tests.test_basic.test_version_command`
  > AssertionError: assert 6 == 0
  >  +  where 6 = CompletedProcess(args=['./executable', 'version'], returncode=6, stdout=b'', stderr=b'  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current\n                   
- `tests.test_basic.TestVersion.test_version_command`
  > AssertionError: assert 6 == 0
  >  +  where 6 = CompletedProcess(args=['./executable', 'version'], returncode=6, stdout='', stderr='  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current\n                     
- *(... 3 more in this cluster)*

### `boolean_false` — 6 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `eval.tests.test_help_categories.test_help_http_has_header_and_description`
  > assert False
  >  +  where False = <built-in method startswith of str object at 0x5632b1a8d3e0>('Usage:')
  >  +    where <built-in method startswith of str object at 0x5632b1a8d3e0> = "curlie 0.1.0\n\nUsage:\n  curlie [options] <method> <url>\n  curlie [options] <url>\n\nOptions:\n  -X, --request <method>  S
- `eval.tests.test_help_main.test_help_has_usage_line`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7fd5addc4df0>('Usage:')
  >  +    where <built-in method startswith of str object at 0x7fd5addc4df0> = 'curlie 0.1.0'.startswith
- `eval.tests.test_help_main.test_help_with_other_args_help_takes_precedence`
  > assert False
  >  +  where False = <built-in method startswith of str object at 0x5632b1ab36f0>('Usage:')
  >  +    where <built-in method startswith of str object at 0x5632b1ab36f0> = "curlie 0.1.0\n\nUsage:\n  curlie [options] <method> <url>\n  curlie [options] <url>\n\nOptions:\n  -X, --request <method>  S
  >  +      where "curlie 0.1.0\n\nUsage:\n  curlie [options] <method> <url>\n  curlie [options] <url>\n\nOptions:\n  -X, --request <method>  Specify request method\n  -H, --header <header>   Pass custom 
- *(... 3 more in this cluster)*

### `returned_none` — 5 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_main.test_help_lists_expected_categories`
  > assert None
  >  +  where None = <function search at 0x7fd5aef96680>('^\\s*auth\\b', "curlie 0.1.0\n\nUsage:\n  curlie [options] <method> <url>\n  curlie [options] <url>\n\nOptions:\n  -X, --request <method>  Specify
  >  +    where <function search at 0x7fd5aef96680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- `eval.tests.test_http_behavior.test_post_json_items_string_and_typed_int`
  > AssertionError: assert None == {'age': 30, 'name': 'alice'}
- `eval.tests.test_http_behavior.test_post_unicode_json_value_preserved`
  > AssertionError: assert None == {'hello': '世界'}
- *(... 2 more in this cluster)*

### `bytes_output_mismatch` — 2 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_formatting_json.test_no_pretty_flag_no_formatting`
  > assert b'  % Total  ...","value":42}' == b'http://127....","value":42}'
  >   
  >   At index 0 diff: b' ' != b'h'
  >   
  >   Full diff:
  >   - (b'http://127.0.0.1:8765/simple\n{"name":"test","value":42}')
  >   + (b'  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Curr'
  >   +  b'ent\n                                 Dload  Upload   Total   Spent    Le'...
- `eval.tests.test_http_behavior.test_querystring_item_double_equals_encodes_value_with_equals`
  > AssertionError: assert {} == {'q': 'a=b'}
  >   
  >   Right contains 1 more item:
  >   {'q': 'a=b'}
  >   
  >   Full diff:
  >   + {}
  >   - {

### `rc_mismatch_got1_want0` — 1 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_error_paths.test_curl_exec_format_error`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'http://example.com'], returncode=1, stdout='', stderr="curlie: error: [Errno 8] Exec format error: '/tmp/fake_curl_hk5jvufa/curl'\n").ret

### `rc_mismatch_got2_want28` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_error_paths.test_curl_timeout_error`
  > AssertionError: assert 2 == 28
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--max-time', '10', 'http://slow-server.com'], returncode=2, stdout='', stderr='curlie: unknown option: --max-time\n').returncode

### `rc_mismatch_got2_want22` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_error_paths.test_curl_http_error_404`
  > AssertionError: assert 2 == 22
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--fail', 'http://example.com/notfound'], returncode=2, stdout='', stderr='curlie: unknown option: --fail\n').returncode

### `rc_mismatch_got2_want47` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_error_paths.test_curl_too_many_redirects`
  > AssertionError: assert 2 == 47
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-L', 'http://redirect-loop.example.com'], returncode=2, stdout='', stderr='curlie: unknown option: -L\n').returncode

