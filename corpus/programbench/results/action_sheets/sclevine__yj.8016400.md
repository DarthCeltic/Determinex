# Action Sheet — sclevine__yj.8016400

**Current:** 63.64%  (525/825)
**Pass / Fail / Skip:** 525 / 299 / 1
**Gap to 100%:** 36.36 percentage points (300 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_executable_behavior.test_invalid_flag_prints_help_to_stderr_and_error_line`
  - reason: test_invalid_flag_prints_help_to_stderr_and_error_line depends on test_help_exact_text

## Failure clusters

299 failed tests grouped into 10 buckets (sorted by count).

### `other_assertion` — 127 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_flags.test_invalid_flag_combination_k_without_yaml`
  > AssertionError: assert b'only valid for YAML output' in b'Error: -k flag is only valid when converting to YAML\nUsage: /workspace/executable.py [-][ytjcrneikhv]\n\nConvert between YAML, TOML, JSON, an
  >  +  where b'Error: -k flag is only valid when converting to YAML\nUsage: /workspace/executable.py [-][ytjcrneikhv]\n\nConvert between YAML, TOML, JSON, and HCL.\nPreserves map order.\n\n-x[x]  Convert
- `eval.tests.test_flags.test_invalid_flag_combination_i_without_json_or_toml`
  > AssertionError: assert b'only valid for JSON or TOML output' in b'Error: -i flag is only valid when converting to JSON or TOML\nUsage: /workspace/executable.py [-][ytjcrneikhv]\n\nConvert between YAML
  >  +  where b'Error: -i flag is only valid when converting to JSON or TOML\nUsage: /workspace/executable.py [-][ytjcrneikhv]\n\nConvert between YAML, TOML, JSON, and HCL.\nPreserves map order.\n\n-x[x] 
- `eval.tests.test_flags.test_invalid_flag_combination_e_without_json`
  > AssertionError: assert b'only valid for JSON output' in b'Error: -e flag is only valid when converting to JSON\nUsage: /workspace/executable.py [-][ytjcrneikhv]\n\nConvert between YAML, TOML, JSON, an
  >  +  where b'Error: -e flag is only valid when converting to JSON\nUsage: /workspace/executable.py [-][ytjcrneikhv]\n\nConvert between YAML, TOML, JSON, and HCL.\nPreserves map order.\n\n-x[x]  Convert
- *(... 124 more in this cluster)*

### `string_output_mismatch` — 65 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_errors.test_yaml_duplicate_keys_allowed`
  > assert '{"key":"value2"}\n' == '{"key":"valu...":"value2"}\n'
  >   
  >   - {"key":"value1","key":"value2"}
  >   + {"key":"value2"}
- `tests.test_errors.test_yaml_special_float_infinity`
  > AssertionError: assert inf == 'Infinity'
- `tests.test_errors.test_yaml_merge_keys`
  > assert '{"base":{"na..."value":2}}\n' == '{"base":{"na..."value":2}}\n'
  >   
  >   - {"base":{"name":"base","value":1},"extended":{"name":"base","value":1,"value":2}}
  >   ?                                                                     ----------
  >   + {"base":{"name":"base","value":1},"extended":{"name":"base","value":2}}
- *(... 62 more in this cluster)*

### `bytes_output_mismatch` — 61 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `eval.tests.test_testdata_cases.test_case1_json_to_yaml`
  > assert b'\'0\': 0\n\...:\n- a\n- b\n' == b'"0": 0\n"1.... - a\n  - b\n'
  >   
  >   At index 0 diff: b"'" != b'"'
  >   
  >   Full diff:
  >   - (b'"0": 0\n"1.0": 1.0\n"1.1": 1.1\n\'"key"\': \'"value"\'\n<: \'>\'\n\'{"<":">"'
  >   ?    ^ ^     ^   ^       ^   ^                                           --------
  >   + (b'\'0\': 0\n\'1.0\': 1.0\n\'1.1\': 1.1\n\'"key"\': \'"value"\'\n<: \'>\'\n\''...
- `eval.tests.test_testdata_cases.test_case1_json_to_yaml_with_n`
  > assert b'\'0\': 0\n\...:\n- a\n- b\n' == b'"0": 0\n"1.... - a\n  - b\n'
  >   
  >   At index 0 diff: b"'" != b'"'
  >   
  >   Full diff:
  >   - (b'"0": 0\n"1.0": 1.0\n"1.1": 1.1\n\'"key"\': \'"value"\'\n<: \'>\'\n\'{"<":">"'
  >   ?    ^ ^     ^   ^       ^   ^                                           --------
  >   + (b'\'0\': 0\n\'1.0\': 1.0\n\'1.1\': 1.1\n\'"key"\': \'"value"\'\n<: \'>\'\n\''...
- `eval.tests.test_testdata_cases.test_case1_json_to_hcl`
  > assert b'"0" = 0\n"1... ["a", "b"]\n' == b'"0" = 0\n\n... = ["a", "b"]'
  >   
  >   At index 8 diff: b'"' != b'\n'
  >   
  >   Full diff:
  >   - (b'"0" = 0\n\n"1.0" = 1\n\n"1.1" = 1.1\n\n"\\"key\\"" = "\\"value\\""\n\n"<" = '
  >   ?           --           ^^             --                               --
  >   + (b'"0" = 0\n"1.0" = 1.0\n"1.1" = 1.1\n"\\"key\\"" = "\\"value\\""\n"<" = ">'...
- *(... 58 more in this cluster)*

### `rc_mismatch_got1_want0` — 19 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `eval.tests.test_hcl_conversions.test_hcl_boolean`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '-cj'], returncode=1, stdout=b'', stderr=b'Error: HCL parse error: Line 1, column 0: unexpected BOOL; expected $end, IDENTIFIER, STRING, COMMENT, M
- `eval.tests.test_testdata_cases.test_case2_yaml_to_json_indent_n`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '-yjin'], returncode=1, stdout=b'', stderr=b'Error: YAML parse error: while constructing a mapping\n  in "<unicode string>", line 1, column 1:\n   
- `eval.tests.test_testdata_cases.test_case2_yaml_to_json_indent`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '-yji'], returncode=1, stdout=b'', stderr=b'Error: YAML parse error: while constructing a mapping\n  in "<unicode string>", line 1, column 1:\n    
- *(... 16 more in this cluster)*

### `missing_dict_key` — 13 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_hcl.test_heredoc_strings`
  > KeyError: 0
- `tests.test_hcl.test_nested_maps_in_attributes`
  > KeyError: 0
- `tests.test_hcl.test_deeply_nested_structures`
  > KeyError: 0
- *(... 10 more in this cluster)*

### `boolean_false` — 5 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_hcl.test_terraform_style_to_json`
  > AssertionError: assert False
  >  +  where False = isinstance({'aws_instance': {'web': {'ami': 'ami-123456', 'instance_type': 't2.micro', 'tags': {'Environment': 'production', 'Name': 'WebServer'}}}, 'aws_s3_bucket': {'data': {'acl':
- `tests.test_roundtrip.test_hcl_json_hcl_block_structure_preservation`
  > AssertionError: assert False
  >  +  where False = isinstance({'aws_instance': {'web': {'ami': 'ami-a1b2c3d4', 'instance_type': 't2.micro', 'tags': {'Name': 'HelloWorld'}}}}, list)
- `eval.tests.test_help_version_and_errors.test_invalid_flag_prints_help_then_error_to_stderr_exit_1`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x5779e85723b0>('Usage:')
  >  +    where <built-in method startswith of str object at 0x5779e85723b0> = 'Error: invalid flags specified: p\nUsage: /workspace/executable.py [-][ytjcrneikhv]\n\nConvert between YAML, TOML, JSON, and
- *(... 2 more in this cluster)*

### `rc_mismatch_got0_want1` — 4 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_errors.test_json_with_nan_literal`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-jy'], returncode=0, stdout=b'value: .nan\n', stderr=b'').returncode
- `tests.test_hcl.test_null_values_not_supported_in_hcl`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-cj'], returncode=0, stdout=b'{"config":{"value":"null"}}\n', stderr=b'').returncode
- `eval.tests.test_argparse_validation.test_double_dash_long_flags_are_invalid[args1]`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--help'], returncode=0, stdout=b'Usage: /workspace/executable.py [-][ytjcrneikhv]\n\nConvert between YAML, TOML, JSON, and HCL.\nPreserve
- *(... 1 more in this cluster)*

### `json_output_missing_or_bad` — 2 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `tests.test_hcl.test_empty_input_produces_empty_object`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_hcl.test_whitespace_only_input`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

### `rc_unexpected_zero` — 2 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `eval.tests.test_help_usage.test_double_dash_help_is_treated_as_invalid_flags_and_prints_help`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--help'], returncode=0, stdout='Usage: /workspace/executable.py [-][ytjcrneikhv]\n\nConvert between YAML, TOML, JSON, and HCL.\nPreserves
- `eval.tests.test_help_usage.test_help_with_extra_invalid_flags_prints_help_and_error_on_stderr`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-h', '-p'], returncode=0, stdout='Usage: /workspace/executable.py [-][ytjcrneikhv]\n\nConvert between YAML, TOML, JSON, and HCL.\nPreserv

### `test_timeout` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_gaps.test_yaml_excessive_alias_expansion`
  > subprocess.TimeoutExpired: Command '['/workspace/executable', '-yj']' timed out after 5 seconds

