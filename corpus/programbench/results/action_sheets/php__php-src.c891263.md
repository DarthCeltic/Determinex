# Action Sheet — php__php-src.c891263

**Current:** 0.18%  (27/15054)
**Pass / Fail / Skip:** 27 / 879 / 2
**Gap to 100%:** 99.82 percentage points (15027 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_cli_webserver.test_malformed_request_line`
  - reason: Requires raw socket testing
- `tests.test_cli_webserver.test_options_method_allowed`
  - reason: OPTIONS request failed: curl failed with exit code 7

## Failure clusters

879 failed tests grouped into 16 buckets (sorted by count).

### `rc_mismatch_got2_want0` — 546 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_additional_features.TestRepeatFlag.test_repeat_execution`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--repeat', '3', '/tmp/tmpd5tcwv93/test.php'], returncode=2, stdout=b'', stderr=b"php-src: unknown option: --repeat\nusage: php-src [OPTIO
- `tests.test_additional_features.TestRepeatFlag.test_repeat_with_r`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--repeat', '2', '-r', "echo 'Y';"], returncode=2, stdout=b'', stderr=b"php-src: unknown option: --repeat\nusage: php-src [OPTIONS] [ARGS]
- `tests.test_additional_features.TestRepeatFlag.test_repeat_one`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--repeat', '1', '-r', "echo 'once';"], returncode=2, stdout=b'', stderr=b"php-src: unknown option: --repeat\nusage: php-src [OPTIONS] [AR
- *(... 543 more in this cluster)*

### `string_output_mismatch` — 81 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_attributes.test_basic_class_attribute`
  > AssertionError: assert '' == 'Name: MyAttr...Value: test\n'
  >   
  >   - Name: MyAttribute
  >   - Value: test
- `tests.test_attributes.test_multiple_repeatable_attributes`
  > AssertionError: assert '' == 'Count: 3\nTa...v2\nTag: v3\n'
  >   
  >   - Count: 3
  >   - Tag: v1
  >   - Tag: v2
  >   - Tag: v3
- `tests.test_attributes.test_method_attribute`
  > AssertionError: assert '' == 'Method: getU...sers [POST]\n'
  >   
  >   - Method: getUsers - /users [GET]
  >   - Method: createUser - /users [POST]
- *(... 78 more in this cluster)*

### `uncategorized` — 53 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_webserver.test_server_starts_and_serves_static_html`
  > RuntimeError: curl failed with exit code 7
- `tests.test_cli_webserver.test_server_executes_php_files`
  > RuntimeError: curl failed with exit code 7
- `tests.test_cli_webserver.test_get_parameters_parsing`
  > RuntimeError: curl failed with exit code 7
- *(... 50 more in this cluster)*

### `other_assertion` — 52 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_additional_features.TestFileOperations.test_file_reading_in_script`
  > AssertionError: assert b'test data' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', '/tmp/tmpyz6q9d1u/read.php'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_additional_features.TestFileOperations.test_file_writing_in_script`
  > AssertionError: assert b'done' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', '/tmp/tmp6enz2g_4/write.php'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_additional_features.TestFileOperations.test_file_existence_check`
  > AssertionError: assert b'yes' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', '/tmp/tmpohr4z4gf/check.php'], returncode=0, stdout=b'', stderr=b'').stdout
- *(... 49 more in this cluster)*

### `json_output_missing_or_bad` — 39 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `tests.test_file_uploads.test_basic_single_file_upload`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_file_uploads.test_file_upload_with_post_data`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_file_uploads.test_multiple_file_uploads`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- *(... 36 more in this cluster)*

### `rc_mismatch_got2_want255` — 28 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_flags.test_lint_invalid_file`
  > assert 2 == 255
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-l', '/workspace/eval/test_resources/test_cli_flags/invalid.php'], returncode=2, stdout=b'', stderr=b"php-src: unknown option: -l\nusage:
- `tests.test_cli_flags.test_syntax_error_in_code`
  > assert 2 == 255
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-r', 'syntax error here'], returncode=2, stdout=b'', stderr=b"php-src: unknown option: -r\nusage: php-src [OPTIONS] [ARGS]\nTry 'php-src 
- `tests.test_cli_flags.test_runtime_error_undefined_function`
  > assert 2 == 255
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-r', 'undefined_function();'], returncode=2, stdout=b'', stderr=b"php-src: unknown option: -r\nusage: php-src [OPTIONS] [ARGS]\nTry 'php-
- *(... 25 more in this cluster)*

### `returned_none` — 20 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_output.test_help_documents_short_flag_with_description[-c-Look for php.ini file]`
  > AssertionError: assert None is not None
  >  +  where None = <function search at 0x783a302ee680>('^\\s*\\-c\\b.*Look\\ for\\ php\\.ini\\ file', 'php-src 0.1.0 - bootstrap scaffold\n\nUsage: php-src [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help    
  >  +    where <function search at 0x783a302ee680> = re.search
  >  +    and   re.MULTILINE = re.M
- `eval.tests.test_help_output.test_help_documents_short_flag_with_description[-n-No configuration (ini) files]`
  > AssertionError: assert None is not None
  >  +  where None = <function search at 0x783a302ee680>('^\\s*\\-n\\b.*No\\ configuration\\ \\(ini\\)\\ files', 'php-src 0.1.0 - bootstrap scaffold\n\nUsage: php-src [OPTIONS] [ARGS]\n\nOptions:\n  -h, -
  >  +    where <function search at 0x783a302ee680> = re.search
  >  +    and   re.MULTILINE = re.M
- `eval.tests.test_help_output.test_help_documents_short_flag_with_description[-d-Define INI entry]`
  > AssertionError: assert None is not None
  >  +  where None = <function search at 0x783a302ee680>('^\\s*\\-d\\b.*Define\\ INI\\ entry', 'php-src 0.1.0 - bootstrap scaffold\n\nUsage: php-src [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print he
  >  +    where <function search at 0x783a302ee680> = re.search
  >  +    and   re.MULTILINE = re.M
- *(... 17 more in this cluster)*

### `boolean_false` — 14 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_builtin_server.TestBuiltInServer.test_server_serves_static_file`
  > AssertionError: assert False
  >  +  where False = wait_for_server('127.0.0.1', 32851)
- `tests.test_builtin_server.TestBuiltInServer.test_server_404_error`
  > AssertionError: assert False
  >  +  where False = wait_for_server('127.0.0.1', 42209)
- `tests.test_builtin_server.TestBuiltInServer.test_server_with_router_script`
  > AssertionError: assert False
  >  +  where False = wait_for_server('127.0.0.1', 36709)
- *(... 11 more in this cluster)*

### `rc_unexpected_zero` — 14 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_attributes.test_invalid_target_runtime_error`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/workspace/eval/test_resources/test_attributes/invalid_target_runtime.php'], returncode=0, stdout='', stderr='').returncode
- `tests.test_attributes.test_non_repeatable_attribute_error`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/workspace/eval/test_resources/test_attributes/non_repeatable_runtime.php'], returncode=0, stdout='', stderr='').returncode
- `tests.test_attributes.test_allow_dynamic_properties_on_trait_error`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/workspace/eval/test_resources/test_attributes/allow_dynamic_on_trait_error.php'], returncode=0, stdout='', stderr='').returncode
- *(... 11 more in this cluster)*

### `rc_mismatch_got2_want1` — 10 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_flags.test_missing_file_error`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-f', '/nonexistent/file.php'], returncode=2, stdout=b'', stderr=b"php-src: unknown option: -f\nusage: php-src [OPTIONS] [ARGS]\nTry 'php-
- `tests.test_cli_flags.test_reflection_nonexistent_function`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--rf', 'nonexistent_function'], returncode=2, stdout=b'', stderr=b"php-src: unknown option: --rf\nusage: php-src [OPTIONS] [ARGS]\nTry 'p
- `tests.test_cli_flags.test_reflection_nonexistent_class`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--rc', 'NonExistentClass'], returncode=2, stdout=b'', stderr=b"php-src: unknown option: --rc\nusage: php-src [OPTIONS] [ARGS]\nTry 'php-s
- *(... 7 more in this cluster)*

### `rc_mismatch_got7_want0` — 9 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_webserver.test_concurrent_requests_handled`
  > assert 7 == 0
  >  +  where 7 = CompletedProcess(args=['bash', '-c', '\nset -e\n/workspace/executable -S localhost:9018 -t /workspace/eval/test_resources/test_cli_webserver >/dev/null 2>&1 &\nSERVER_PID=$!\nsleep 0.6\n
- `tests.test_cli_webserver.test_large_post_body_not_truncated`
  > assert 7 == 0
  >  +  where 7 = CompletedProcess(args=['bash', '-c', '\nset -e\n/workspace/executable -S localhost:9211 -t /workspace/eval/test_resources/test_cli_webserver/advanced >/dev/null 2>&1 &\nSERVER_PID=$!\nsl
- `tests.test_cli_webserver.test_http_1_0_protocol_version`
  > AssertionError: assert 7 == 0
  >  +  where 7 = CompletedProcess(args=['bash', '-c', '\nset -e\n/workspace/executable -S localhost:9212 -t /workspace/eval/test_resources/test_cli_webserver/advanced >/dev/null 2>&1 &\nSERVER_PID=$!\nsl
- *(... 6 more in this cluster)*

### `rc_mismatch_got0_want255` — 5 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_errors.test_parse_error_missing_semicolon`
  > AssertionError: assert 0 == 255
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/tmp/tmp0x0nemfb.php'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_errors.test_parse_error_unclosed_brace`
  > AssertionError: assert 0 == 255
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/tmp/tmp0betipc2.php'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_errors.test_parse_error_unexpected_token`
  > AssertionError: assert 0 == 255
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/tmp/tmpwhn_73hz.php'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 2 more in this cluster)*

### `rc_mismatch_got2_want42` — 4 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_flags.test_exit_code_propagation`
  > assert 2 == 42
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-r', 'exit(42);'], returncode=2, stdout=b'', stderr=b"php-src: unknown option: -r\nusage: php-src [OPTIONS] [ARGS]\nTry 'php-src --help' 
- `tests.test_errors.test_exit_with_numeric_code`
  > assert 2 == 42
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-r', 'exit(42);'], returncode=2, stdout=b'', stderr=b"php-src: unknown option: -r\nusage: php-src [OPTIONS] [ARGS]\nTry 'php-src --help' 
- `tests.test_error_handling.TestErrorHandling.test_exit_with_code`
  > assert 2 == 42
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-r', 'exit(42);'], returncode=2, stdout='', stderr="php-src: unknown option: -r\nusage: php-src [OPTIONS] [ARGS]\nTry 'php-src --help' fo
- *(... 1 more in this cluster)*

### `bytes_output_mismatch` — 2 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `eval.tests.test_cli_io.test_file_argument_executes_script_file`
  > AssertionError: assert b'' == b'hello file\n'
  >   
  >   Full diff:
  >   - (b'hello file\n')
  >   + b''
- `eval.tests.test_cli_io.test_separate_stdout_stderr_streams`
  > AssertionError: assert b'' == b'OUT\n'
  >   
  >   Full diff:
  >   - b'OUT\n'
  >   + b''

### `rc_mismatch_got2_want123` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_errors.test_die_with_numeric_code`
  > assert 2 == 123
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-r', 'die(123);'], returncode=2, stdout=b'', stderr=b"php-src: unknown option: -r\nusage: php-src [OPTIONS] [ARGS]\nTry 'php-src --help' 

### `rc_mismatch_got0_want1` — 1 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_file_operations.TestIncludeRequire.test_include_once`
  > AssertionError: assert 0 == 1
  >  +  where 0 = <built-in method count of str object at 0x7f48867e4030>('X')
  >  +    where <built-in method count of str object at 0x7f48867e4030> = ''.count
  >  +      where '' = CompletedProcess(args=['/workspace/executable', '/tmp/pytest-of-root/pytest-0/test_include_once2/main.php'], returncode=0, stdout='', stderr='').stdout

