# Action Sheet — paradigmxyz__solar.5190d0e

**Current:** 10.58%  (285/2693)
**Pass / Fail / Skip:** 285 / 970 / 2
**Gap to 100%:** 89.42 percentage points (2408 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_cli_io.test_unreadable_file_is_error_exit1`
  - reason: permission tests require non-root
- `eval.tests.test_solar_cli.test_out_dir_writes_combined_json_same_as_stdout`
  - reason: test_out_dir_writes_combined_json_same_as_stdout depends on test_compile_files_with_imports_produces_two_contract_entries

## Failure clusters

970 failed tests grouped into 10 buckets (sorted by count).

### `other_assertion` — 350 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_help_short`
  > AssertionError: assert b'Usage: executable [OPTIONS] [INPUT]...' in b'solar 0.1.0 - bootstrap scaffold\n\nUsage: solar [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print
  >  +  where b'solar 0.1.0 - bootstrap scaffold\n\nUsage: solar [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['./executable', '-h']
- `tests.test_basic_invocation.test_help_long`
  > AssertionError: assert b'Usage: executable [OPTIONS] [INPUT]...' in b'solar 0.1.0 - bootstrap scaffold\n\nUsage: solar [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print
  >  +  where b'solar 0.1.0 - bootstrap scaffold\n\nUsage: solar [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['./executable', '--he
- `tests.test_basic_invocation.test_version`
  > AssertionError: assert b'solar Version:' in b'solar 0.1.0\n'
  >  +  where b'solar 0.1.0\n' = CompletedProcess(args=['./executable', '--version'], returncode=0, stdout=b'solar 0.1.0\n', stderr=b'').stdout
- *(... 347 more in this cluster)*

### `rc_unexpected_zero` — 294 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_compilation_options.test_invalid_evm_version`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'testdata/Counter.sol', '--evm-version', 'invalid123'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_coverage_gaps.test_yul_file_without_parse_yul_flag`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '/tmp/tmptirooffl/test.yul'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_coverage_gaps.test_error_format_json_with_syntax_error`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '/tmp/tmpijv0r52p/bad.sol', '--error-format', 'json'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 291 more in this cluster)*

### `rc_mismatch_got2_want0` — 98 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_basic_invocation.test_zhelp`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '-Zhelp'], returncode=2, stdout=b'', stderr=b"solar: unknown option: -Zhelp\nusage: solar [OPTIONS] [ARGS]\nTry 'solar --help' for more information
- `tests.test_input_handling.test_base_path`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--base-path', 'testdata', 'Counter.sol', '--emit', 'abi'], returncode=2, stdout=b'', stderr=b"solar: unknown option: --base-path\nusage: solar [OP
- `tests.test_basic_invocation.test_z_help`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-Zhelp'], returncode=2, stdout=b'', stderr=b"solar: unknown option: -Zhelp\nusage: solar [OPTIONS] [ARGS]\nTry 'solar --help' for more in
- *(... 95 more in this cluster)*

### `json_output_missing_or_bad` — 94 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `tests.test_additional_scenarios.test_nested_structs`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_additional_scenarios.test_multiple_inheritance`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_additional_scenarios.test_indexed_event_parameters`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- *(... 91 more in this cluster)*

### `string_output_mismatch` — 64 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_help_baseline.test_help_long_matches_fixture_exactly`
  > AssertionError: assert 'solar 0.1.0 ...int version\n' == 'Blazingly fa...le warnings\n'
  >   
  >   - Blazingly fast Solidity compiler
  >   + solar 0.1.0 - bootstrap scaffold
  >     
  >   + Usage: solar [OPTIONS] [ARGS]
  >   - Usage: executable [OPTIONS] [INPUT]...
  >   - ...
- `eval.tests.test_solar_cli.test_help_full_matches_golden`
  > AssertionError: assert 'solar 0.1.0 ...int version\n' == 'Blazingly fa...le warnings\n'
  >   
  >   - Blazingly fast Solidity compiler
  >   + solar 0.1.0 - bootstrap scaffold
  >     
  >   + Usage: solar [OPTIONS] [ARGS]
  >   - Usage: executable [OPTIONS] [INPUT]...
  >   - ...
- `eval.tests.test_solar_cli.test_help_short_matches_golden`
  > AssertionError: assert 'solar 0.1.0 ...int version\n' == 'Blazingly fa...le warnings\n'
  >   
  >   - Blazingly fast Solidity compiler
  >   + solar 0.1.0 - bootstrap scaffold
  >     
  >   + Usage: solar [OPTIONS] [ARGS]
  >   - Usage: executable [OPTIONS] [INPUT]...
  >   - ...
- *(... 61 more in this cluster)*

### `rc_mismatch_got0_want1` — 58 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_compilation_stages.test_stop_after_parsing_with_syntax_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-', '--stop-after', 'parsing'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_edge_cases.test_unicode_in_strings`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_error_handling.test_syntax_error_human`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 55 more in this cluster)*

### `bytes_output_mismatch` — 6 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_comprehensive_coverage.TestParseYul.test_parse_yul_with_yul_file`
  > assert (2 == 0 or b'error' in b"solar: unknown option: -zparse-yul\nusage: solar [options] [args]\ntry 'solar --help' for more information.\n")
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-Zparse-yul', '-'], returncode=2, stdout=b'', stderr=b"solar: unknown option: -Zparse-yul\nusage: solar [OPTIONS] [ARGS]\nTry 'solar --he
  >  +  and   b"solar: unknown option: -zparse-yul\nusage: solar [options] [args]\ntry 'solar --help' for more information.\n" = <built-in method lower of bytes object at 0x7f2c6ddac300>()
  >  +    where <built-in method lower of bytes object at 0x7f2c6ddac300> = b"solar: unknown option: -Zparse-yul\nusage: solar [OPTIONS] [ARGS]\nTry 'solar --help' for more information.\n".lower
  >  +      where b"solar: unknown option: -Zparse-yul\nusage: solar [OPTIONS] [ARGS]\nTry 'solar --help' for more information.\n" = CompletedProcess(args=['/workspace/executable', '-Zparse-yul', '-'], re
- `tests.test_comprehensive_coverage.TestTypeCheckingPaths.test_typeck_function_calls`
  > assert (2 == 0 or b'error' in b"solar: unknown option: -ztypeck\nusage: solar [options] [args]\ntry 'solar --help' for more information.\n")
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-Ztypeck', '-'], returncode=2, stdout=b'', stderr=b"solar: unknown option: -Ztypeck\nusage: solar [OPTIONS] [ARGS]\nTry 'solar --help' fo
  >  +  and   b"solar: unknown option: -ztypeck\nusage: solar [options] [args]\ntry 'solar --help' for more information.\n" = <built-in method lower of bytes object at 0x7f2c6ddaeca0>()
  >  +    where <built-in method lower of bytes object at 0x7f2c6ddaeca0> = b"solar: unknown option: -Ztypeck\nusage: solar [OPTIONS] [ARGS]\nTry 'solar --help' for more information.\n".lower
  >  +      where b"solar: unknown option: -Ztypeck\nusage: solar [OPTIONS] [ARGS]\nTry 'solar --help' for more information.\n" = CompletedProcess(args=['/workspace/executable', '-Ztypeck', '-'], returnco
- `tests.test_comprehensive_coverage.TestTypeCheckingPaths.test_typeck_type_conversions`
  > assert (2 == 0 or b'error' in b"solar: unknown option: -ztypeck\nusage: solar [options] [args]\ntry 'solar --help' for more information.\n")
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-Ztypeck', '-'], returncode=2, stdout=b'', stderr=b"solar: unknown option: -Ztypeck\nusage: solar [OPTIONS] [ARGS]\nTry 'solar --help' fo
  >  +  and   b"solar: unknown option: -ztypeck\nusage: solar [options] [args]\ntry 'solar --help' for more information.\n" = <built-in method lower of bytes object at 0x7f2c6ddaf900>()
  >  +    where <built-in method lower of bytes object at 0x7f2c6ddaf900> = b"solar: unknown option: -Ztypeck\nusage: solar [OPTIONS] [ARGS]\nTry 'solar --help' for more information.\n".lower
  >  +      where b"solar: unknown option: -Ztypeck\nusage: solar [OPTIONS] [ARGS]\nTry 'solar --help' for more information.\n" = CompletedProcess(args=['/workspace/executable', '-Ztypeck', '-'], returnco
- *(... 3 more in this cluster)*

### `boolean_false` — 3 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_comprehensive_coverage.TestDiagnosticWidth.test_diagnostic_width_zero`
  > assert False
- `eval.tests.test_cli_io.test_stdin_dash_emit_abi_json_single_line`
  > AssertionError: assert False
  >  +  where False = <built-in method endswith of bytes object at 0x7fcbd7914030>(b'}')
  >  +    where <built-in method endswith of bytes object at 0x7fcbd7914030> = b''.endswith
  >  +      where b'' = CompletedProcess(args=['/workspace/executable', '-', '--emit', 'abi'], returncode=0, stdout=b'', stderr=b'').stdout
- `eval.tests.test_solar_cli.test_pretty_json_is_multiline_and_valid_json`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7f1fa6e40030>('{\n')
  >  +    where <built-in method startswith of str object at 0x7f1fa6e40030> = ''.startswith

### `rc_mismatch_got2_want1` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_ast_gaps.test_error_json_format`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--error-format', 'json', '/workspace/eval/test_resources/test_ast_gaps/error_syntax.sol'], returncode=2, stdout='', stderr="solar: unknow
- `tests.test_ast_gaps.test_error_short_format`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--error-format-human', 'short', '/workspace/eval/test_resources/test_ast_gaps/error_syntax.sol'], returncode=2, stdout='', stderr="solar:

### `returned_none` — 1 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_help_output.test_help_has_arguments_and_options_sections`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f6cbb4f2680>('^Arguments:\\s*$', 'solar 0.1.0 - bootstrap scaffold\n\nUsage: solar [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  P
  >  +    where <function search at 0x7f6cbb4f2680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE

