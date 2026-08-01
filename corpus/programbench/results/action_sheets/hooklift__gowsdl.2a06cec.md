# Action Sheet — hooklift__gowsdl.2a06cec

**Current:** 12.95%  (76/587)
**Pass / Fail / Skip:** 76 / 343 / 0
**Gap to 100%:** 87.05 percentage points (511 tests)

## Failure clusters

343 failed tests grouped into 8 buckets (sorted by count).

### `missing_file` — 118 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_basic.TestCodeGeneration.test_generates_valid_go_code`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmppwc_0afv/testpkg/myservice.go'
- `tests.test_basic.TestCodeGeneration.test_generates_types_from_wsdl`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmp95euasss/testpkg/myservice.go'
- `tests.test_basic.TestCodeGeneration.test_generates_soap_operations`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpggeqdlfb/testpkg/myservice.go'
- *(... 115 more in this cluster)*

### `other_assertion` — 103 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic.TestBasicInvocation.test_no_arguments_shows_usage`
  > AssertionError: assert b'[options] myservice.wsdl' in b'Usage: gowsdl [OPTIONS] INPUT-FILE\n\n  -d, -dir       string  Output directory\n  -i, -ignore-tls       Ignore TLS errors\n  -make-public  bool
  >  +  where b'Usage: gowsdl [OPTIONS] INPUT-FILE\n\n  -d, -dir       string  Output directory\n  -i, -ignore-tls       Ignore TLS errors\n  -make-public  bool    Make all types public\n  -o, -output    
- `tests.test_basic.TestBasicInvocation.test_help_flag`
  > AssertionError: assert b'[options] myservice.wsdl' in b'Usage: gowsdl [OPTIONS] INPUT-FILE\n\n  -d, -dir       string  Output directory\n  -i, -ignore-tls       Ignore TLS errors\n  -make-public  bool
  >  +  where b'Usage: gowsdl [OPTIONS] INPUT-FILE\n\n  -d, -dir       string  Output directory\n  -i, -ignore-tls       Ignore TLS errors\n  -make-public  bool    Make all types public\n  -o, -output    
- `tests.test_basic.TestBasicInvocation.test_version_flag`
  > AssertionError: assert (b'v0.5.0' in b'gowsdl v0.10.0\n' or b'0.5' in b'gowsdl v0.10.0\n')
  >  +  where b'gowsdl v0.10.0\n' = CompletedProcess(args=['/workspace/executable', '-v'], returncode=0, stdout=b'gowsdl v0.10.0\n', stderr=b'').stdout
  >  +  and   b'gowsdl v0.10.0\n' = CompletedProcess(args=['/workspace/executable', '-v'], returncode=0, stdout=b'gowsdl v0.10.0\n', stderr=b'').stdout
- *(... 100 more in this cluster)*

### `boolean_false` — 71 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_basic.TestOutputGeneration.test_default_output_location`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpbelj138m/myservice').exists
- `tests.test_basic.TestOutputGeneration.test_custom_output_file`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmp2ijwxswz/mypkg').exists
- `tests.test_basic.TestOutputGeneration.test_custom_package_name`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpsd1ndcg2/custompackage').exists
- *(... 68 more in this cluster)*

### `string_output_mismatch` — 19 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_output.test_help_is_printed_to_stderr_by_default`
  > AssertionError: assert 'Usage: gowsd...how this help' == ''
  >   
  >   + Usage: gowsdl [OPTIONS] INPUT-FILE
  >   + 
  >   +   -d, -dir       string  Output directory
  >   +   -i, -ignore-tls       Ignore TLS errors
  >   +   -make-public  bool    Make all types public
  >   +   -o, -output    string  Output filename...
- `eval.tests.test_help_output.test_help_output_matches_baseline_exactly`
  > AssertionError: assert 'Usage: gowsd...this help\n\n' == 'Usage: /work...sdl version\n'
  >   
  >   + Usage: gowsdl [OPTIONS] INPUT-FILE
  >   + 
  >   +   -d, -dir       string  Output directory
  >   +   -i, -ignore-tls       Ignore TLS errors
  >   +   -make-public  bool    Make all types public
  >   +   -o, -output    string  Output filename...
- `eval.tests.test_gowsdl_cli.test_help_h_exact_except_usage_path`
  > assert 'Usage: gowsd...this help\n\n' == 'Usage: ./exe...sdl version\n'
  >   
  >   - Usage: ./executable [options] myservice.wsdl
  >   -   -d string
  >   -     	Directory under which package directory will be created (default "./")
  >   -   -i	Skips TLS Verification
  >   -   -make-public
  >   -     	Make the generated types public/exported (default true)...
- *(... 16 more in this cluster)*

### `rc_mismatch_got0_want1` — 16 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `eval.tests.test_argparse_validation.test_positional_first_then_flag_treated_as_filename_and_causes_open_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = RunResult(rc=0, out='gowsdl v0.10.0\n', err='').rc
- `tests.test_gowsdl.TestErrorHandling.test_nonexistent_output_directory`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-d', '/tmp/tmpyk60h3vd/nonexistent', '/workspace/fixtures/test.wsdl'], returncode=0, stdout='Reading file /workspace/fixtures/test.wsdl..
- `tests.test_cli.test_invalid_xml_eof_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/workspace/eval/test_resources/test_cli/invalid.wsdl'], returncode=0, stdout='Reading file /workspace/eval/test_resources/test_cli/invali
- *(... 13 more in this cluster)*

### `rc_unexpected_zero` — 12 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_basic.TestInputHandling.test_malformed_xml`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/tmp/tmpcddmjgk9/bad.wsdl'], returncode=0, stdout=b'Reading file /tmp/tmpcddmjgk9/bad.wsdl...\nGenerating code from /tmp/tmpcddmjgk9/bad.
- `tests.test_basic.TestOutputGeneration.test_output_same_as_input_error`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-o', 'test.wsdl', 'test.wsdl'], returncode=0, stdout=b'Reading file test.wsdl...\nGenerating code from test.wsdl...\nDone.\n', stderr=b''
- `tests.test_error_handling.test_output_file_same_as_input`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-o', 'fixtures/test.wsdl', 'fixtures/test.wsdl'], returncode=0, stdout=b'Reading file fixtures/test.wsdl...\nGenerating code from fixture
- *(... 9 more in this cluster)*

### `bytes_output_mismatch` — 3 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_basic_invocation.test_no_arguments_stdout_empty`
  > AssertionError: assert b'Usage: gows...this help\n\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'Usage: gowsdl [OPTIONS] INPUT-FILE\n\n  -d, -dir       string  Output dire'
  >   +  b'ctory\n  -i, -ignore-tls       Ignore TLS errors\n  -make-public  bool    '
  >   +  b'Make all types public\n  -o, -output    string  Output filename\n  -p, -pa'
  >   +  b'ckage   string  Package name\n  -v, -version          Print version info\n'
- `tests.test_basic_invocation.test_help_to_stderr`
  > AssertionError: assert b'Usage: gows...this help\n\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'Usage: gowsdl [OPTIONS] INPUT-FILE\n\n  -d, -dir       string  Output dire'
  >   +  b'ctory\n  -i, -ignore-tls       Ignore TLS errors\n  -make-public  bool    '
  >   +  b'Make all types public\n  -o, -output    string  Output filename\n  -p, -pa'
  >   +  b'ckage   string  Package name\n  -v, -version          Print version info\n'
- `eval.tests.test_error_cases.test_no_arguments_prints_usage_to_stderr_and_exit_zero`
  > AssertionError: assert b'Usage: gows...this help\n\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'Usage: gowsdl [OPTIONS] INPUT-FILE\n\n  -d, -dir       string  Output dire'
  >   +  b'ctory\n  -i, -ignore-tls       Ignore TLS errors\n  -make-public  bool    '
  >   +  b'Make all types public\n  -o, -output    string  Output filename\n  -p, -pa'
  >   +  b'ckage   string  Package name\n  -v, -version          Print version info\n'

### `rc_mismatch_got2_want1` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_error_handling.test_treat_last_arg_as_wsdl`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-p', 'testpkg'], returncode=2, stdout=b'', stderr=b'Usage: gowsdl [OPTIONS] INPUT-FILE\n\n  -d, -dir       string  Output directory\n  -i

