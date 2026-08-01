# Action Sheet — ogham__dog.721440b

**Current:** 11.91%  (216/1813)
**Pass / Fail / Skip:** 216 / 776 / 3
**Gap to 100%:** 88.09 percentage points (1597 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_harvest.test_features_001_the_missing_features_are_documented_in_the_version`
  - reason: Requires --no-default-features build
- `tests.test_harvest.test_features_002_the_tls_option_is_not_accepted_when_the_feature_is_disabled`
  - reason: Requires --no-default-features build
- `tests.test_harvest.test_features_003_the_https_option_is_not_accepted_when_the_feature_is_disabled`
  - reason: Requires --no-default-features build

## Failure clusters

776 failed tests grouped into 12 buckets (sorted by count).

### `other_assertion` — 450 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_additional_edge_cases.test_invalid_color_setting`
  > assert 2 in [0, 1]
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--color', 'invalid', 'example.com', '@8.8.8.8'], returncode=2, stdout=b'', stderr=b"dog: unknown option: --color\nusage: dog [OPTIONS] [A
- `tests.test_additional_edge_cases.test_colour_british_spelling`
  > assert 2 in [0, 1]
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--colour', 'never', 'example.com', '@8.8.8.8'], returncode=2, stdout=b'', stderr=b"dog: unknown option: --colour\nusage: dog [OPTIONS] [A
- `tests.test_additional_edge_cases.test_txid_with_hex_format`
  > assert 2 in [0, 1]
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--txid', '255', 'example.com', '@8.8.8.8'], returncode=2, stdout=b'', stderr=b"dog: unknown option: --txid\nusage: dog [OPTIONS] [ARGS]\n
- *(... 447 more in this cluster)*

### `rc_mismatch_got2_want0` — 155 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_basic_invocation.test_version_short_flag_shows_version`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-v'], returncode=2, stdout=b'', stderr=b"dog: unknown option: -v\nusage: dog [OPTIONS] [ARGS]\nTry 'dog --help' for more information.\n")
- `tests.test_edge_cases.test_multiple_edns_flags`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--edns=show', '-Z', 'bufsize=4096', 'dns.google', '@8.8.8.8'], returncode=2, stdout=b'', stderr=b"dog: unknown option: --edns=show\nusage
- `tests.test_edge_cases.test_txid_with_protocol_tweaks`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--txid=42', '-Z', 'aa', '-Z', 'ad', 'dns.google', '@8.8.8.8'], returncode=2, stdout=b'', stderr=b"dog: unknown option: --txid=42\nusage: 
- *(... 152 more in this cluster)*

### `json_output_missing_or_bad` — 57 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `eval.tests.test_queries_json.test_json_schema_minimal_keys`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `eval.tests.test_queries_json.test_query_type_positional_token_works[A]`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `eval.tests.test_queries_json.test_query_type_positional_token_works[AAAA]`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- *(... 54 more in this cluster)*

### `rc_mismatch_got2_want3` — 40 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_no_arguments_shows_help`
  > assert 2 == 3
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b"usage: dog [OPTIONS] [ARGS]\nTry 'dog --help' for more information.\n").returncode
- `tests.test_edge_cases.test_empty_type_argument`
  > assert 2 == 3
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--type', '', 'dns.google', '@8.8.8.8'], returncode=2, stdout=b'', stderr=b"dog: unknown option: --type\nusage: dog [OPTIONS] [ARGS]\nTry 
- `tests.test_error_handling.test_invalid_argument`
  > assert 2 == 3
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--wibble'], returncode=2, stdout=b'', stderr=b"dog: unknown option: --wibble\nusage: dog [OPTIONS] [ARGS]\nTry 'dog --help' for more info
- *(... 37 more in this cluster)*

### `string_output_mismatch` — 26 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_output.test_help_matches_baseline_exactly`
  > AssertionError: assert 'dog 0.1.0 - ...int version\n' == 'dog ● comman...information\n'
  >   
  >   - dog ● command-line DNS client
  >   + dog 0.1.0 - bootstrap scaffold
  >     
  >   + Usage: dog [OPTIONS] [ARGS]
  >   - Usage:
  >   -   dog [OPTIONS] [--] <arguments>...
- `eval.tests.test_subcommands.test_unknown_subcommand_is_treated_as_query_or_errors[version]`
  > AssertionError: assert '' == 'dog 0.1.0 - ...Print version'
  >   
  >   - dog 0.1.0 - bootstrap scaffold
  >   - 
  >   - Usage: dog [OPTIONS] [ARGS]
  >   - 
  >   - Options:
  >   -   -h, --help     Print help
- `eval.tests.test_subcommands.test_unknown_subcommand_is_treated_as_query_or_errors[query]`
  > AssertionError: assert '' == 'dog 0.1.0 - ...Print version'
  >   
  >   - dog 0.1.0 - bootstrap scaffold
  >   - 
  >   - Usage: dog [OPTIONS] [ARGS]
  >   - 
  >   - Options:
  >   -   -h, --help     Print help
- *(... 23 more in this cluster)*

### `rc_mismatch_got0_want3` — 22 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_error_handling.test_opt_query_not_allowed`
  > AssertionError: assert 0 == 3
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'OPT', 'dns.google'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_error_handling.test_opt_query_lowercase_not_allowed`
  > AssertionError: assert 0 == 3
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'opt', 'dns.google'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_error_handling.test_domain_name_too_long`
  > AssertionError: assert 0 == 3
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
- *(... 19 more in this cluster)*

### `rc_mismatch_got0_want1` — 12 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_error_formatting.test_wire_error_insufficient_data_truncated_answer`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'A', 'truncated.example.com', '@127.0.0.1:15357'], returncode=0, stdout='', stderr='').returncode
- `tests.test_error_formatting.test_wire_error_insufficient_data_partial_label`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'A', 'shortpacket.example.com', '@127.0.0.1:15357'], returncode=0, stdout='', stderr='').returncode
- `tests.test_errors.test_nonexistent_nameserver_lookup_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'example.com', '@nonexistent.invalid'], returncode=0, stdout='', stderr='').returncode
- *(... 9 more in this cluster)*

### `bytes_output_mismatch` — 6 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_timing_and_formatting.test_time_with_short_mode`
  > assert (b"dog: unknow...nformation.\n" == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b"dog: unknown option: --time\nusage: dog [OPTIONS] [ARGS]\nTry 'dog --help'"
  >   +  b' for more information.\n') or b'error' in b"dog: unknown option: --time\nusage: dog [options] [args]\ntry 'dog --help' for more information.\n")
  >  +  where b"dog: unknown option: --time\nusage: dog [options] [args]\ntry 'dog --help' for more information.\n" = <built-in method lower of bytes object at 0x7fcb23ec2130>()
  >  +    where <built-in method lower of bytes object at 0x7fcb23ec2130> = b"dog: unknown option: --time\nusage: dog [OPTIONS] [ARGS]\nTry 'dog --help' for more information.\n".lower
- `eval.tests.test_queries_json.test_query_type_flag_works[A]`
  > assert b"dog: unknow...nformation.\n" == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b"dog: unknown option: -t\nusage: dog [OPTIONS] [ARGS]\nTry 'dog --help' for"
  >   +  b' more information.\n')
- `eval.tests.test_queries_json.test_query_type_flag_works[AAAA]`
  > assert b"dog: unknow...nformation.\n" == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b"dog: unknown option: -t\nusage: dog [OPTIONS] [ARGS]\nTry 'dog --help' for"
  >   +  b' more information.\n')
- *(... 3 more in this cluster)*

### `rc_unexpected_zero` — 3 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_advanced_error_handling.test_very_long_domain_name`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
- `eval.tests.test_help_output.test_invalid_short_h_errors_and_mentions_unrecognized_option`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-h'], returncode=0, stdout='dog 0.1.0 - bootstrap scaffold\n\nUsage: dog [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V,
- `tests.test_final_gaps.test_color_output_requires_argument`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'example.com', 'A', '@8.8.8.8', '--color'], returncode=0, stdout=b'', stderr=b'').returncode

### `returned_none` — 2 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_basic_invocation.test_version_output_format`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7fcb29e86680>('v\\d+\\.\\d+', 'dog 0.1.0\n')
  >  +    where <function search at 0x7fcb29e86680> = re.search
- `eval.tests.test_help_version_errors.test_version_succeeds_and_contains_version_prefix`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f6cceed2680>('\\bv\\d+\\.\\d+\\.\\d+', 'dog 0.1.0\n')
  >  +    where <function search at 0x7f6cceed2680> = re.search

### `rc_mismatch_got2_want1` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_wire_unit_tests_externalized_as_cli_errors.test_ext_build_request_smoke_via_connection_refused`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-q', 'example.net', '-t', 'A', '-n', '127.0.0.1'], returncode=2, stdout=b'', stderr=b"dog: unknown option: -q\nusage: dog [OPTIONS] [ARGS
- `eval.tests.test_wire_unit_tests_externalized_as_cli_errors.test_ext_parse_nothing_smoke_via_connection_refused`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-q', 'example.net', '-t', 'A', '-n', '127.0.0.1'], returncode=2, stdout=b'', stderr=b"dog: unknown option: -q\nusage: dog [OPTIONS] [ARGS

### `rc_mismatch_got0_want2` — 1 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_error_formatting.test_short_format_no_results`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'A', 'nonexistent99999.invalid', '@8.8.8.8', '--short'], returncode=0, stdout='', stderr='').returncode

