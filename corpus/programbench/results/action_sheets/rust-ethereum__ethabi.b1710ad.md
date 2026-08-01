# Action Sheet — rust-ethereum__ethabi.b1710ad

**Current:** 18.08%  (226/1250)
**Pass / Fail / Skip:** 226 / 744 / 0
**Gap to 100%:** 81.92 percentage points (1024 tests)

## Failure clusters

744 failed tests grouped into 21 buckets (sorted by count).

### `string_output_mismatch` — 242 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_abi_edge_cases.test_abi_mixed_with_fallback_receive`
  > AssertionError: assert 'a9059cbb\n11...1111111111111' == 'a9059cbb0000...00000000003e8'
  >   
  >   - a9059cbb000000000000000000000000111111111111111111111111111111111111111100000000000000000000000000000000000000000000000000000000000003e8
  >   + a9059cbb
  >   + 1111111111111111111111111111111111111111
  >   + USAGE
  >   + uint256
  >   + 64...
- `tests.test_abi_edge_cases.test_abi_with_all_operation_types`
  > AssertionError: assert '45557578\n00...1111111111111' == '70a082310000...435e7ef1beaed'
  >   
  >   - 70a082310000000000000000000000005aaeb6053f3e94c9b9a09f33669435e7ef1beaed
  >   + 45557578
  >   + 0000000000000000000000001111111111111111111111111111111111111111
- `tests.test_abi_edge_cases.test_abi_with_overloaded_errors`
  > AssertionError: assert '45557578\n00...1111111111111' == '1a6952300000...1111111111111'
  >   
  >   + 45557578
  >   - 1a6952300000000000000000000000001111111111111111111111111111111111111111
  >   ? --------
  >   + 0000000000000000000000001111111111111111111111111111111111111111
- *(... 239 more in this cluster)*

### `other_assertion` — 232 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_data_types.test_decode_address_array`
  > AssertionError: assert b'address[]' in b'uint8\nff\nuint16\nffff\nint8\n80\nff\n12345678\n68656c6c6f20776f726c64\n1111111111111111111111111111111111111111\n'
  >  +  where b'uint8\nff\nuint16\nffff\nint8\n80\nff\n12345678\n68656c6c6f20776f726c64\n1111111111111111111111111111111111111111\n' = CompletedProcess(args=['/workspace/executable', 'decode', 'params', '
- `tests.test_decode_params.test_decode_string`
  > AssertionError: assert b'string' in b'uint8\nff\nuint16\nffff\nint8\n80\nff\n12345678\n68656c6c6f20776f726c64\n1111111111111111111111111111111111111111\n'
  >  +  where b'uint8\nff\nuint16\nffff\nint8\n80\nff\n12345678\n68656c6c6f20776f726c64\n1111111111111111111111111111111111111111\n' = CompletedProcess(args=['/workspace/executable', 'decode', 'params', '
- `tests.test_decode_params.test_decode_bool_array`
  > AssertionError: assert b'bool[]' in b'uint8\nff\nuint16\nffff\nint8\n80\nff\n12345678\n68656c6c6f20776f726c64\n1111111111111111111111111111111111111111\n'
  >  +  where b'uint8\nff\nuint16\nffff\nint8\n80\nff\n12345678\n68656c6c6f20776f726c64\n1111111111111111111111111111111111111111\n' = CompletedProcess(args=['/workspace/executable', 'decode', 'params', '
- *(... 229 more in this cluster)*

### `rc_unexpected_zero` — 201 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_basic_invocation.test_invalid_subcommand`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'invalid-command'], returncode=0, stdout=b'ethabi-cli\nUSAGE:\n', stderr=b'').returncode
- `tests.test_decode_function.test_decode_function_nonexistent`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'decode', 'function', 'res/foo.abi', 'nonexistent', '0000000000000000000000000000000000000000000000000000000000000001'], returncode=0, std
- `tests.test_decode_log.test_decode_log_nonexistent_event`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'decode', 'log', 'res/event.abi', 'Nope(bool,address)', '-l', '0000000000000000000000000000000000000000000000000000000000000000', '0000000
- *(... 198 more in this cluster)*

### `bytes_output_mismatch` — 16 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_basic_invocation.test_version_flag_short`
  > AssertionError: assert b'ethabi-cli\...cli\nUSAGE:\n' == b'ethabi-cli\...cli\nUSAGE:\n'
  >   
  >   At index 29 diff: b'U' != b'1'
  >   
  >   Full diff:
  >   - (b'ethabi-cli\n18.0.0\nethabi-cli\n18.0.0\nethabi-cli\nUSAGE:\n')
  >   ?    --------------------
  >   + (b'ethabi-cli\n18.0.0\nethabi-cli\nUSAGE:\n')
- `tests.test_encode_function.test_encode_function_by_name`
  > AssertionError: assert b'more than o...0000000000001' == b'45557578000...0000000000001'
  >   
  >   At index 0 diff: b'm' != b'4'
  >   
  >   Full diff:
  >   - (b'455575780000000000000000000000000000000000000000000000000000000000000001')
  >   + (b'more than one function\nd473a8ed\n0000000000000000000000000000000000000000'
  >   +  b'000000000000000000000020\n31\n45557578\n00000000000000000000000000000000000'
- `tests.test_encode_function.test_encode_function_by_signature`
  > AssertionError: assert b'more than o...001\n45557578' == b'45557578000...0000000000001'
  >   
  >   At index 0 diff: b'm' != b'4'
  >   
  >   Full diff:
  >   - (b'455575780000000000000000000000000000000000000000000000000000000000000001')
  >   + (b'more than one function\nd473a8ed\n0000000000000000000000000000000000000000'
  >   +  b'000000000000000000000020\n31\n45557578\n00000000000000000000000000000000000'
- *(... 13 more in this cluster)*

### `rc_mismatch_got0_want1` — 13 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_basic_invocation.test_no_arguments_shows_help`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable'], returncode=0, stdout=b'(\n(string,bool,string)\n--lenient\n-1\n0000000000000000000000000000000000000000000000000000000000000000\n00000000
- `tests.test_basic_invocation.test_no_arguments_shows_help`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable'], returncode=0, stdout=b'(\n(string,bool,string)\n--lenient\n-1\n0000000000000000000000000000000000000000000000000000000000000000\n00000000000000000
- `eval.tests.test_argparse_validation.test_missing_required_positionals_reports_each_required_arg[argv0-required_markers0]`
  > assert 0 == 1
- *(... 10 more in this cluster)*

### `returned_none` — 10 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_basic_invocation.test_version_flag_long`
  > AssertionError: assert None
  >  +  where None = <function match at 0x7f90a5036170>(b'ethabi-cli \\d+\\.\\d+\\.\\d+', b'ethabi-cli\n18.0.0\nethabi-cli\n18.0.0\nethabi-cli\nUSAGE:\n')
  >  +    where <function match at 0x7f90a5036170> = re.match
  >  +    and   b'ethabi-cli\n18.0.0\nethabi-cli\n18.0.0\nethabi-cli\nUSAGE:\n' = CompletedProcess(args=['./executable', '--version'], returncode=0, stdout=b'ethabi-cli\n18.0.0\nethabi-cli\n18.0.0\nethabi
- `tests.test_basic_invocation.test_version_flag_short`
  > AssertionError: assert None
  >  +  where None = <function match at 0x7f90a5036170>(b'ethabi-cli \\d+\\.\\d+\\.\\d+', b'ethabi-cli\n18.0.0\nethabi-cli\nUSAGE:\n')
  >  +    where <function match at 0x7f90a5036170> = re.match
  >  +    and   b'ethabi-cli\n18.0.0\nethabi-cli\nUSAGE:\n' = CompletedProcess(args=['./executable', '-V'], returncode=0, stdout=b'ethabi-cli\n18.0.0\nethabi-cli\nUSAGE:\n', stderr=b'').stdout
- `eval.tests.test_help_main.test_help_usage_line_mentions_subcommand`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7fcc8bec2680>('^\\s*executable\\s+<SUBCOMMAND>\\s*$', 'ethabi-cli\nUSAGE:\nFLAGS:\n-h, --help\n-V, --version\nSUBCOMMANDS:\nencode\ndecode\nethabi-cli\nUSAGE:\n'
  >  +    where <function search at 0x7fcc8bec2680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- *(... 7 more in this cluster)*

### `rc_mismatch_got362_want64` — 6 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_more_coverage.test_encode_int16_lenient`
  > AssertionError: assert 362 == 64
  >  +  where 362 = len(b'00000000000000000000000000000000000000000000000000000000000000ff\n000000000000000000000000000000000000000000000000000000000000ffff\n0000000000000000000000000000000000000000000000
  >  +    where b'00000000000000000000000000000000000000000000000000000000000000ff\n000000000000000000000000000000000000000000000000000000000000ffff\n000000000000000000000000000000000000000000000000000000
  >  +      where <built-in method strip of bytes object at 0x7f90a2f94350> = b'00000000000000000000000000000000000000000000000000000000000000ff\n0000000000000000000000000000000000000000000000000000000000
  >  +        where b'00000000000000000000000000000000000000000000000000000000000000ff\n000000000000000000000000000000000000000000000000000000000000ffff\n00000000000000000000000000000000000000000000000000
- `tests.test_more_coverage.test_encode_int64_lenient`
  > AssertionError: assert 362 == 64
  >  +  where 362 = len(b'00000000000000000000000000000000000000000000000000000000000000ff\n000000000000000000000000000000000000000000000000000000000000ffff\n0000000000000000000000000000000000000000000000
  >  +    where b'00000000000000000000000000000000000000000000000000000000000000ff\n000000000000000000000000000000000000000000000000000000000000ffff\n000000000000000000000000000000000000000000000000000000
  >  +      where <built-in method strip of bytes object at 0x7f90a2f901c0> = b'00000000000000000000000000000000000000000000000000000000000000ff\n0000000000000000000000000000000000000000000000000000000000
  >  +        where b'00000000000000000000000000000000000000000000000000000000000000ff\n000000000000000000000000000000000000000000000000000000000000ffff\n00000000000000000000000000000000000000000000000000
- `tests.test_more_coverage.test_encode_uint128_lenient`
  > AssertionError: assert 362 == 64
  >  +  where 362 = len(b'00000000000000000000000000000000000000000000000000000000000000ff\n000000000000000000000000000000000000000000000000000000000000ffff\n0000000000000000000000000000000000000000000000
  >  +    where b'00000000000000000000000000000000000000000000000000000000000000ff\n000000000000000000000000000000000000000000000000000000000000ffff\n000000000000000000000000000000000000000000000000000000
  >  +      where <built-in method strip of bytes object at 0x7f90a2f904e0> = b'00000000000000000000000000000000000000000000000000000000000000ff\n0000000000000000000000000000000000000000000000000000000000
  >  +        where b'00000000000000000000000000000000000000000000000000000000000000ff\n000000000000000000000000000000000000000000000000000000000000ffff\n00000000000000000000000000000000000000000000000000
- *(... 3 more in this cluster)*

### `rc_mismatch_got1_want0` — 4 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_decode_params.test_decode_params_multiple_bools`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', 'decode', 'params', '-t', 'bool', '-t', 'bool', '00000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000
- `tests.test_decode_params.TestMultipleParamsDecode.test_decode_two_bools`
  > assert 1 == 0
- `tests.test_roundtrip.TestRoundtripMultipleParams.test_roundtrip_two_bools`
  > assert 1 == 0
- *(... 1 more in this cluster)*

### `rc_mismatch_got207_want8` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_special_cases.test_encode_with_no_params`
  > AssertionError: assert 207 == 8
  >  +  where 207 = len(b'a9059cbb\n1111111111111111111111111111111111111111\nUSAGE\nuint256\n64\ndd62ed3e\n1111111111111111111111111111111111111111\n2222222222222222222222222222222222222222\n095ea7b3\n11
  >  +    where b'a9059cbb\n1111111111111111111111111111111111111111\nUSAGE\nuint256\n64\ndd62ed3e\n1111111111111111111111111111111111111111\n2222222222222222222222222222222222222222\n095ea7b3\n1111111111
  >  +      where <built-in method strip of bytes object at 0x7f196d6b9830> = b'a9059cbb\n1111111111111111111111111111111111111111\nUSAGE\nuint256\n64\ndd62ed3e\n1111111111111111111111111111111111111111\n
  >  +        where b'a9059cbb\n1111111111111111111111111111111111111111\nUSAGE\nuint256\n64\ndd62ed3e\n1111111111111111111111111111111111111111\n2222222222222222222222222222222222222222\n095ea7b3\n111111
- `tests.test_encode_function.test_encode_function_no_params`
  > AssertionError: assert 207 == 8
  >  +  where 207 = len(b'a9059cbb\n1111111111111111111111111111111111111111\nUSAGE\nuint256\n64\ndd62ed3e\n1111111111111111111111111111111111111111\n2222222222222222222222222222222222222222\n095ea7b3\n11
- `tests.test_encode_function.test_encode_function_no_params`
  > AssertionError: assert 207 == 8
  >  +  where 207 = len('a9059cbb\n1111111111111111111111111111111111111111\nUSAGE\nuint256\n64\ndd62ed3e\n1111111111111111111111111111111111111111\n2222222222222222222222222222222222222222\n095ea7b3\n111

### `boolean_false` — 3 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `eval.tests.test_help_and_version.test_version_flag_exits_0_and_prints_version`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7fb884bad840>('ethabi-cli ')
  >  +    where <built-in method startswith of str object at 0x7fb884bad840> = 'ethabi-cli\n18.0.0\nethabi-cli\n18.0.0\nethabi-cli\nUSAGE:'.startswith
- `eval.tests.test_subcommand_dispatch.test_nested_subcommands_listed[decode-expected_nested0]`
  > AssertionError: assert False
  >  +  where False = <built-in method issubset of set object at 0x7f4ce34e3840>(set())
  >  +    where <built-in method issubset of set object at 0x7f4ce34e3840> = {'function', 'help', 'log', 'params'}.issubset
- `eval.tests.test_subcommand_dispatch.test_nested_subcommands_listed[encode-expected_nested1]`
  > AssertionError: assert False
  >  +  where False = <built-in method issubset of set object at 0x7f4ce34e3ca0>(set())
  >  +    where <built-in method issubset of set object at 0x7f4ce34e3ca0> = {'function', 'help', 'params'}.issubset

### `rc_mismatch_got60_want64` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_additional_types.TestAddressVariations.test_encode_address_lowercase`
  > AssertionError: assert 60 == 64
  >  +  where 60 = len('ff\n12345678\n1234567890abcdef\nuint8\nff\nuint16\nffff\nint8\n80\nff')
- `tests.test_additional_types.TestAddressVariations.test_encode_address_uppercase`
  > AssertionError: assert 60 == 64
  >  +  where 60 = len('ff\n12345678\n1234567890abcdef\nuint8\nff\nuint16\nffff\nint8\n80\nff')
- `tests.test_additional_types.TestAddressVariations.test_encode_address_mixed_case`
  > AssertionError: assert 60 == 64
  >  +  where 60 = len('ff\n12345678\n1234567890abcdef\nuint8\nff\nuint16\nffff\nint8\n80\nff')

### `rc_mismatch_got60_want192` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_additional_types.TestFixedArrays.test_encode_fixed_bool_array`
  > AssertionError: assert 60 == 192
  >  +  where 60 = len('ff\n12345678\n1234567890abcdef\nuint8\nff\nuint16\nffff\nint8\n80\nff')
- `tests.test_encode_params.TestBasicTypes.test_encode_string_simple`
  > AssertionError: assert 60 == 192
  >  +  where 60 = len('ff\n12345678\n1234567890abcdef\nuint8\nff\nuint16\nffff\nint8\n80\nff')

### `rc_mismatch_got6_want1` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_version_flag_long`
  > AssertionError: assert 6 == 1
  >  +  where 6 = len([b'ethabi-cli', b'18.0.0', b'ethabi-cli', b'18.0.0', b'ethabi-cli', b'USAGE:'])

### `rc_mismatch_got21_want64` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_additional_coverage.test_encode_int32_value`
  > AssertionError: assert 21 == 64
  >  +  where 21 = len(b'int32\n12345678\nbytes8')

### `rc_mismatch_got0_want64` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_edge_cases.test_encode_negative_int128`
  > AssertionError: assert 0 == 64
  >  +  where 0 = len(b'')

### `rc_mismatch_got148_want64` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_encode_params.test_encode_params_bool_true`
  > AssertionError: assert 148 == 64
  >  +  where 148 = len(b'0000000000000000000000000000000000000000000000000000000000000001\n0000000000000000000000000000000000000000000000000000000000000060\n6761766f66796f726b')

### `rc_mismatch_got107_want8` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_real_abi_files.test_validators_abi`
  > AssertionError: assert 107 == 8
  >  +  where 107 = len(b'a\ntrue\nb\n4444444444444444444444444444444444444444\na\ntrue\nb\n4444444444444444444444444444444444444444\na\nfalse')

### `rc_mismatch_got10_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_decode_params.test_decode_multiple_params`
  > AssertionError: assert 10 == 3
  >  +  where 10 = len(['bool', 'true', 'string', 'gavofyork', 'false', 'address', ...])

### `rc_mismatch_got1_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_decode_params.test_decode_multiple_params_complex`
  > AssertionError: assert 1 == 3
  >  +  where 1 = len([''])

### `rc_mismatch_got2_want1` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_argparse_validation.test_unknown_top_level_flag_errors_and_prints_usage`
  > assert 2 == 1

### `rc_mismatch_got0_want128` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_encode_params.TestMultipleParams.test_encode_two_bools`
  > AssertionError: assert 0 == 128
  >  +  where 0 = len('')

