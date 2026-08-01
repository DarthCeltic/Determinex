# Action Sheet — stranger6667__jsonschema.d52e881

**Current:** 7.32%  (247/3373)
**Pass / Fail / Skip:** 247 / 665 / 0
**Gap to 100%:** 92.68 percentage points (3126 tests)

## Failure clusters

665 failed tests grouped into 16 buckets (sorted by count).

### `rc_mismatch_got0_want1` — 187 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_additional_coverage.test_items_false_no_additional`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', '/tmp/tmpznif4jr9/schema.json', '-i', '/tmp/tmpznif4jr9/invalid.json'], returncode=0, stdout=b'/workspace/eval/test_resources/test_additional_prope
- `tests.test_additional_coverage.test_min_contains_invalid`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', '/tmp/tmpft4ozo8g/schema.json', '-i', '/tmp/tmpft4ozo8g/invalid.json'], returncode=0, stdout=b'/workspace/eval/test_resources/test_additional_prope
- `tests.test_additional_coverage.test_max_contains_invalid`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', '/tmp/tmpam8uhrag/schema.json', '-i', '/tmp/tmpam8uhrag/invalid.json'], returncode=0, stdout=b'/workspace/eval/test_resources/test_additional_prope
- *(... 184 more in this cluster)*

### `rc_mismatch_got1_want0` — 183 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_draft_specification.test_draft_4_enforcement`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '/tmp/tmpxqabtncs/schema.json', '-i', '/tmp/tmpxqabtncs/instance.json', '--draft', '4'], returncode=1, stdout=b"/workspace/eval/test_resources/test
- `tests.test_draft_specification.test_draft_6_enforcement`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '/tmp/tmpe0d89ork/schema.json', '-i', '/tmp/tmpe0d89ork/instance.json', '--draft', '6'], returncode=1, stdout=b"/workspace/eval/test_resources/test
- `tests.test_draft_specification.test_draft_7_enforcement`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '/tmp/tmpmp_m6a9o/schema.json', '-i', '/tmp/tmpmp_m6a9o/instance.json', '--draft', '7'], returncode=1, stdout=b"/workspace/eval/test_resources/test
- *(... 180 more in this cluster)*

### `other_assertion` — 128 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_help_flag_displays_usage`
  > AssertionError: assert b'Usage: executable [OPTIONS] [SCHEMA]' in b''
  >  +  where b'' = CompletedProcess(args=['./executable', '--help'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_basic_invocation.test_help_short_flag`
  > AssertionError: assert b'Usage: executable [OPTIONS] [SCHEMA]' in b''
  >  +  where b'' = CompletedProcess(args=['./executable', '-h'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_basic_invocation.test_version_flag`
  > AssertionError: assert b'Version: ' in b''
  >  +  where b'' = CompletedProcess(args=['./executable', '--version'], returncode=0, stdout=b'', stderr=b'').stdout
- *(... 125 more in this cluster)*

### `string_output_mismatch` — 50 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_cli_io.test_text_output_valid_and_invalid_exit_codes_and_messages`
  > AssertionError: assert '/workspace/e...son - VALID\n' == '/tmp/pytest-...son - VALID\n'
  >   
  >   - /tmp/pytest-of-root/pytest-0/test_text_output_valid_and_inv2/valid.json - VALID
  >   + /workspace/eval/test_resources/test_additional_properties/instance_extra_numbers.json - VALID
- `tests.test_cli_io.test_errors_only_suppresses_valid_output`
  > AssertionError: assert 'error: unexp...nformation.\n' == ''
  >   
  >   + error: unexpected argument '--errors-only' found
  >   + Error: unexpected argument '--errors-only' found
  >   + unknown flag: unexpected argument '--errors-only' found
  >   + Unknown flag: unexpected argument '--errors-only' found
  >   + Usage: jsonschema [OPTIONS] [ARGS]...
  >   + USAGE: jsonschema [OPTIONS] [ARGS]......
- `tests.test_cli_io.test_output_flag_is_json_and_has_expected_keys`
  > AssertionError: assert '/workspace/e...ap_false.json' == '/tmp/pytest-...2/schema.json'
  >   
  >   - /tmp/pytest-of-root/pytest-0/test_output_flag_is_json_and_h2/schema.json
  >   + /workspace/eval/test_resources/test_additional_properties/schema_ap_false.json
- *(... 47 more in this cluster)*

### `rc_mismatch_got7_want0` — 31 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_schema_only_validates_metaschema`
  > AssertionError: assert 7 == 0
  >  +  where 7 = CompletedProcess(args=['./executable', '/tmp/tmpvzl1tfeh/schema.json'], returncode=7, stdout=b'', stderr=b'error: cannot connect to http://127.0.0.1:8080/: <urlopen error [Errno 111] Con
- `tests.test_draft_specification.test_draft_short_flag`
  > AssertionError: assert 7 == 0
  >  +  where 7 = CompletedProcess(args=['./executable', '/tmp/tmpbsio_1h4/schema.json', '-i', '/tmp/tmpbsio_1h4/instance.json', '-d', '7'], returncode=7, stdout=b'', stderr=b'error: cannot connect to htt
- `tests.test_http_options.test_insecure_flag`
  > AssertionError: assert 7 == 0
  >  +  where 7 = CompletedProcess(args=['./executable', '/tmp/tmp5rmp0chm/schema.json', '--insecure'], returncode=7, stdout=b'', stderr=b'error: cannot connect to http://127.0.0.1:8080/: <urlopen error [
- *(... 28 more in this cluster)*

### `rc_mismatch_got7_want1` — 21 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_instance_validation.test_multiple_instances_mixed_validity`
  > AssertionError: assert 7 == 1
  >  +  where 7 = CompletedProcess(args=['./executable', '/tmp/tmphfx6vjv2/schema.json', '-i', '/tmp/tmphfx6vjv2/valid.json', '-i', '/tmp/tmphfx6vjv2/invalid.json'], returncode=7, stdout=b'', stderr=b'err
- `tests.test_schema_validation.test_invalid_schema_type`
  > AssertionError: assert 7 == 1
  >  +  where 7 = CompletedProcess(args=['./executable', '/tmp/tmp0cbg3pvz/schema.json'], returncode=7, stdout=b'', stderr=b'error: cannot connect to http://127.0.0.1:8080/: <urlopen error [Errno 111] Con
- `tests.test_schema_validation.test_schema_with_syntax_error`
  > AssertionError: assert 7 == 1
  >  +  where 7 = CompletedProcess(args=['./executable', '/tmp/tmpgl_sgvl3/schema.json'], returncode=7, stdout=b'', stderr=b'error: cannot connect to http://127.0.0.1:8080/: <urlopen error [Errno 111] Con
- *(... 18 more in this cluster)*

### `rc_unexpected_zero` — 21 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_help_output.test_unknown_flag_errors_when_before_help`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--no-such-flag', '--help'], returncode=0, stdout="error: unexpected argument '--no-such-flag' found\nError: unexpected argument '--no-suc
- `tests.test_error_handling.TestErrorHandling.test_invalid_draft_value`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/tmp/pytest-of-root/pytest-0/test_invalid_draft_value2/schema.json', '--draft', 'invalid'], returncode=0, stdout='VALID\nVALID\n', stderr
- `tests.test_error_handling.TestErrorHandling.test_invalid_timeout_negative`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/tmp/pytest-of-root/pytest-0/test_invalid_timeout_negative2/schema.json', '--timeout', '-1'], returncode=0, stdout="error: unexpected arg
- *(... 18 more in this cluster)*

### `json_output_missing_or_bad` — 13 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `tests.test_http_options.test_http_options_with_structured_output`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_schema_validation.test_invalid_schema_flag_output`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_cli_args.test_no_instances_with_flag_output_invalid`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- *(... 10 more in this cluster)*

### `boolean_false` — 12 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_help_output.test_help_has_trailing_newline`
  > AssertionError: assert False
  >  +  where False = <built-in method endswith of str object at 0x7f81980b4030>('\n')
  >  +    where <built-in method endswith of str object at 0x7f81980b4030> = ''.endswith
  >  +      where '' = CompletedProcess(args=['/workspace/executable', '--help'], returncode=0, stdout='', stderr='').stdout
- `tests.test_help_output.test_help_takes_precedence_over_unknown_flag_when_first`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x55d79c36aaf0>('Usage: executable')
  >  +    where <built-in method startswith of str object at 0x55d79c36aaf0> = 'jsonschema 0.1.0\nNetwork client whose tests stand up a fixture server on a port\n\nUsage: jsonschema [OPTIONS] [ARGS]...\nU
  >  +      where 'jsonschema 0.1.0\nNetwork client whose tests stand up a fixture server on a port\n\nUsage: jsonschema [OPTIONS] [ARGS]...\nUSAGE: jsonschema [OPTIONS] [ARGS]...\nusage: jsonschema [OPTI
- `tests.test_cli_io.test_version_flag_output`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7ff03c660030>('Version: ')
  >  +    where <built-in method startswith of str object at 0x7ff03c660030> = ''.startswith
  >  +      where '' = <built-in method decode of bytes object at 0x7ff03c65c030>('utf-8')
  >  +        where <built-in method decode of bytes object at 0x7ff03c65c030> = b''.decode
  >  +          where b'' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'', stderr=b'').stdout
- *(... 9 more in this cluster)*

### `rc_mismatch_got0_want2` — 10 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_draft_specification.test_invalid_draft_value`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['./executable', '/tmp/tmpkthyv7kk/schema.json', '--draft', 'invalid'], returncode=0, stdout=b'VALID\nVALID\n', stderr=b'').returncode
- `tests.test_http_options.test_invalid_timeout_not_a_number`
  > assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['./executable', '/tmp/tmpwsj68e2t/schema.json', '--timeout', 'invalid'], returncode=0, stdout=b"error: unexpected argument '--timeout' found\nError: unexpected arg
- `tests.test_http_options.test_invalid_connect_timeout_negative`
  > assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['./executable', '/tmp/tmp04rddkrn/schema.json', '--connect-timeout=-5'], returncode=0, stdout=b"error: unexpected argument '--connect-timeout=-5' found\nError: une
- *(... 7 more in this cluster)*

### `rc_mismatch_got7_want2` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_no_arguments_shows_error`
  > AssertionError: assert 7 == 2
  >  +  where 7 = CompletedProcess(args=['./executable'], returncode=7, stdout=b'', stderr=b'error: cannot connect to http://127.0.0.1:8080/: <urlopen error [Errno 111] Connection refused>\n').returncode
- `tests.test_cli_args.test_missing_schema_error`
  > AssertionError: assert 7 == 2
  >  +  where 7 = CompletedProcess(args=['/workspace/executable'], returncode=7, stdout=b'', stderr=b'error: cannot connect to http://127.0.0.1:8080/: <urlopen error [Errno 111] Connection refused>\n').re
- `eval.tests.test_cli_behavior.test_no_args_errors_and_exit_2`
  > assert 7 == 2

### `bytes_output_mismatch` — 2 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_errors_only.test_errors_only_suppresses_valid_text`
  > assert b"error: unex...nformation.\n" == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b"error: unexpected argument '--errors-only' found\nError: unexpected argum"
  >   +  b"ent '--errors-only' found\nunknown flag: unexpected argument '--errors-on"
  >   +  b"ly' found\nUnknown flag: unexpected argument '--errors-only' found\nUsage:"
  >   +  b' jsonschema [OPTIONS] [ARGS]...\nUSAGE: jsonschema [OPTIONS] [ARGS]...\nus'
- `tests.test_errors_only.test_errors_only_schema_validation`
  > assert b"error: unex...nformation.\n" == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b"error: unexpected argument '--errors-only' found\nError: unexpected argum"
  >   +  b"ent '--errors-only' found\nunknown flag: unexpected argument '--errors-on"
  >   +  b"ly' found\nUnknown flag: unexpected argument '--errors-only' found\nUsage:"
  >   +  b' jsonschema [OPTIONS] [ARGS]...\nUSAGE: jsonschema [OPTIONS] [ARGS]...\nus'

### `empty_list_or_string` — 1 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_help_output.test_help_usage_synopsis_exact_first_line`
  > IndexError: list index out of range

### `returned_none` — 1 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_help_output.test_draft_option_possible_values`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f8197eaf760>('possible values:\\s*4,\\s*6,\\s*7,\\s*2019,\\s*2020', '')
  >  +    where <function search at 0x7f8197eaf760> = re.search
  >  +    and   '' = CompletedProcess(args=['/workspace/executable', '--help'], returncode=0, stdout='', stderr='').stdout

### `rc_mismatch_got1_want2` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_args.test_invalid_output_mode`
  > AssertionError: assert 1 == 2
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '/tmp/tmpn5rcep8t/schema.json', '--output', 'invalid'], returncode=1, stdout=b'', stderr=b'').returncode

### `missing_dict_key` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_contains.test_contains_hierarchical_invalid_no_matches`
  > KeyError: 'details'

