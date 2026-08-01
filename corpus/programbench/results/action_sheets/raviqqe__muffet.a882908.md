# Action Sheet — raviqqe__muffet.a882908

**Current:** 11.86%  (60/506)
**Pass / Fail / Skip:** 60 / 372 / 0
**Gap to 100%:** 88.14 percentage points (446 tests)

## Failure clusters

372 failed tests grouped into 10 buckets (sorted by count).

### `other_assertion` — 127 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic.test_help_flag`
  > AssertionError: assert b'Application Options:' in b'muffet 0.1.0 - bootstrap scaffold\n\nUsage: muffet [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n'
  >  +  where b'muffet 0.1.0 - bootstrap scaffold\n\nUsage: muffet [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['../executable', '-
- `tests.test_basic.test_help_flag_short`
  > AssertionError: assert b'Application Options:' in b'muffet 0.1.0 - bootstrap scaffold\n\nUsage: muffet [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n'
  >  +  where b'muffet 0.1.0 - bootstrap scaffold\n\nUsage: muffet [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['../executable', '-
- `tests.test_output_formats.test_verbose_and_junit_conflict`
  > assert (b'verbose' in b"muffet: unknown option: --junit\nusage: muffet [options] [args]\ntry 'muffet --help' for more information.\n" or b'not supported' in b"muffet: unknown option: --junit\nusage: m
  >  +  where b"muffet: unknown option: --junit\nusage: muffet [options] [args]\ntry 'muffet --help' for more information.\n" = <built-in method lower of bytes object at 0x7fe6018a92c0>()
  >  +    where <built-in method lower of bytes object at 0x7fe6018a92c0> = b"muffet: unknown option: --junit\nusage: muffet [OPTIONS] [ARGS]\nTry 'muffet --help' for more information.\n".lower
  >  +      where b"muffet: unknown option: --junit\nusage: muffet [OPTIONS] [ARGS]\nTry 'muffet --help' for more information.\n" = CompletedProcess(args=['../executable', '--junit', '--verbose', 'http://
  >  +  and   b"muffet: unknown option: --junit\nusage: muffet [options] [args]\ntry 'muffet --help' for more information.\n" = <built-in method lower of bytes object at 0x7fe6018a92c0>()
  >  +    where <built-in method lower of bytes object at 0x7fe6018a92c0> = b"muffet: unknown option: --junit\nusage: muffet [OPTIONS] [ARGS]\nTry 'muffet --help' for more information.\n".lower
  >  +      where b"muffet: unknown option: --junit\nusage: muffet [OPTIONS] [ARGS]\nTry 'muffet --help' for more information.\n" = CompletedProcess(args=['../executable', '--junit', '--verbose', 'http://
- *(... 124 more in this cluster)*

### `rc_mismatch_got2_want0` — 108 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_color.test_color_auto_default`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['../executable', '-v', 'http://localhost:8888/'], returncode=2, stdout=b'', stderr=b"muffet: unknown option: -v\nusage: muffet [OPTIONS] [ARGS]\nTry 'muffet --help
- `tests.test_color.test_color_always`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['../executable', '--color=always', '-v', 'http://localhost:8888/'], returncode=2, stdout=b'', stderr=b"muffet: unknown option: --color=always\nusage: muffet [OPTIO
- `tests.test_color.test_color_never`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['../executable', '--color=never', '-v', 'http://localhost:8888/'], returncode=2, stdout=b'', stderr=b"muffet: unknown option: --color=never\nusage: muffet [OPTIONS
- *(... 105 more in this cluster)*

### `rc_mismatch_got2_want1` — 104 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_no_arguments`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['./executable'], returncode=2, stdout=b'', stderr=b"usage: muffet [OPTIONS] [ARGS]\nTry 'muffet --help' for more information.\n").returncode
- `tests.test_basic_invocation.test_invalid_flag`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['./executable', '--unknown-flag-xyz123'], returncode=2, stdout=b'', stderr=b"muffet: unknown option: --unknown-flag-xyz123\nusage: muffet [OPTIONS] [ARGS]\nTry 'mu
- `tests.test_connection_options.test_max_connections_flag`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['./executable', '--max-connections=10', 'http://localhost:19999'], returncode=2, stdout=b'', stderr=b"muffet: unknown option: --max-connections=10\nusage: muffet [
- *(... 101 more in this cluster)*

### `rc_mismatch_got0_want1` — 13 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_basic_invocation.test_invalid_url_format`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', 'not-a-url'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_output_formats.test_text_format_default`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', 'http://localhost:19999'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_status_codes.test_accepted_status_codes_default`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', 'http://localhost:19999'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 10 more in this cluster)*

### `string_output_mismatch` — 6 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_output.test_baseline_help_output_matches_fixture`
  > AssertionError: assert 'muffet 0.1.0...int version\n' == 'Usage:\n  ex...how version\n'
  >   
  >   + muffet 0.1.0 - bootstrap scaffold
  >   - Usage:
  >   -   executable [options] <url>
  >     
  >   + Usage: muffet [OPTIONS] [ARGS]
  >   + ...
- `tests.test_filtering.test_one_page_only_prevents_recursive_crawling`
  > AssertionError: assert '' == 'http://127.0...46501/broken1'
  >   
  >   - http://127.0.0.1:46501/
  >   - 	404	http://127.0.0.1:46501/broken1
- `tests.test_sitemap_robots.test_sitemap_filters_links_not_in_sitemap`
  > AssertionError: assert '' == 'http://127.0...c/open.html\n'
  >   
  >   - http://127.0.0.1:19876/
  >   - 	404	http://127.0.0.1:19876/allowed/test.html
  >   - 	404	http://127.0.0.1:19876/blocked/test.html
  >   - 	404	http://127.0.0.1:19876/private/secret.html
  >   - 	404	http://127.0.0.1:19876/public/open.html
- *(... 3 more in this cluster)*

### `rc_unexpected_zero` — 4 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_basic.test_too_many_arguments`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['../executable', 'http://example.com', 'http://example.org'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_basic.test_invalid_url_format`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['../executable', 'not-a-url'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_edge_cases.test_non_html_root_page`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['../executable', 'http://localhost:8888/image.png'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 1 more in this cluster)*

### `json_output_missing_or_bad` — 4 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `tests.test_output_formats.test_json_format`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_output_formats.test_json_format_valid_structure`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_output_formats.test_deprecated_json_flag`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- *(... 1 more in this cluster)*

### `returned_none` — 3 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_basic.test_version_flag`
  > AssertionError: assert None
  >  +  where None = <function match at 0x7fe603631120>(b'^\\d+\\.\\d+\\.\\d+\\s*$', b'muffet 0.1.0\n')
  >  +    where <function match at 0x7fe603631120> = re.match
  >  +    and   b'muffet 0.1.0\n' = CompletedProcess(args=['../executable', '--version'], returncode=0, stdout=b'muffet 0.1.0\n', stderr=b'').stdout
- `tests.test_basic_invocation.test_version_flag`
  > AssertionError: assert None
  >  +  where None = <function match at 0x7fd7f0f92170>(b'\\d+\\.\\d+\\.\\d+', b'muffet 0.1.0')
  >  +    where <function match at 0x7fd7f0f92170> = re.match
  >  +    and   b'muffet 0.1.0' = <built-in method strip of bytes object at 0x7fd7f0490b70>()
  >  +      where <built-in method strip of bytes object at 0x7fd7f0490b70> = b'muffet 0.1.0\n'.strip
  >  +        where b'muffet 0.1.0\n' = CompletedProcess(args=['./executable', '--version'], returncode=0, stdout=b'muffet 0.1.0\n', stderr=b'').stdout
- `eval.tests.test_help_output.test_usage_line_mentions_options_and_url`
  > AssertionError: assert None is not None
  >  +  where None = <function search at 0x7facb05ce680>('^\\s*executable\\s+\\[options\\]\\s+<url>\\s*$', 'muffet 0.1.0 - bootstrap scaffold\n\nUsage: muffet [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help   
  >  +    where <function search at 0x7facb05ce680> = re.search
  >  +    and   re.MULTILINE = re.M

### `uncategorized` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_output_formats.test_junit_format`
  > xml.etree.ElementTree.ParseError: no element found: line 1, column 0
- `tests.test_output_formats.test_deprecated_junit_flag`
  > xml.etree.ElementTree.ParseError: no element found: line 1, column 0

### `bytes_output_mismatch` — 1 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_link_checking.test_one_page_only_flag`
  > assert (b'localhost:8888' in b'' or 2 == 0)
  >  +  where b'' = CompletedProcess(args=['../executable', '--one-page-only', 'http://localhost:8888/page1'], returncode=2, stdout=b'', stderr=b"muffet: unknown option: --one-page-only\nusage: muffet [OP
  >  +  and   2 = CompletedProcess(args=['../executable', '--one-page-only', 'http://localhost:8888/page1'], returncode=2, stdout=b'', stderr=b"muffet: unknown option: --one-page-only\nusage: muffet [OPTI

