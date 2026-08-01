# Action Sheet — agourlay__zip-password-finder.704700d

**Current:** 19.88%  (224/1127)
**Pass / Fail / Skip:** 224 / 567 / 1
**Gap to 100%:** 80.12 percentage points (903 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_zip_password_finder.TestDictionaryAttack.test_dictionary_password_not_found`
  - reason: File 4 takes too long to process - encrypted differently

## Failure clusters

567 failed tests grouped into 12 buckets (sorted by count).

### `other_assertion` — 269 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_help_flag`
  > AssertionError: assert b'Usage:' in b'Find the password of protected ZIP files\n--inputFile\n--workers\n--passwordDictionary\n--charset\n--help\n--version\nzip-password-finder\n0.10.3\n'
  >  +  where b'Find the password of protected ZIP files\n--inputFile\n--workers\n--passwordDictionary\n--charset\n--help\n--version\nzip-password-finder\n0.10.3\n' = CompletedProcess(args=['./executable'
- `tests.test_basic_invocation.test_help_short_flag`
  > AssertionError: assert b'Find the password of protected ZIP files' in b'zip-password-finder\nzip-password-finder\n'
  >  +  where b'zip-password-finder\nzip-password-finder\n' = CompletedProcess(args=['./executable', '-h'], returncode=0, stdout=b'zip-password-finder\nzip-password-finder\n', stderr=b'').stdout
- `tests.test_basic_invocation.test_help_contains_all_options`
  > AssertionError: Option b'--charsetFile' not in help
  > assert b'--charsetFile' in b'Find the password of protected ZIP files\n--inputFile\n--workers\n--passwordDictionary\n--charset\n--help\n--version\nzip-password-finder\n0.10.3\n'
  >  +  where b'Find the password of protected ZIP files\n--inputFile\n--workers\n--passwordDictionary\n--charset\n--help\n--version\nzip-password-finder\n0.10.3\n' = CompletedProcess(args=['./executable'
- *(... 266 more in this cluster)*

### `rc_mismatch_got1_want0` — 123 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_dictionary_mode.test_dictionary_empty`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '-i', 'test-files/2.test.txt.zip', '-p', '/tmp/tmpz9u2gobc/empty_dict.txt', '-w', '1'], returncode=1, stdout=b'Password found:ab\nPassword found:ab
- `tests.test_edge_cases.test_very_small_dictionary_no_match`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '-i', 'test-files/2.test.txt.zip', '-p', '/tmp/tmp3_mk2_7_/nopass.txt', '-w', '1'], returncode=1, stdout=b'Password found:ab\nPassword found:abc\nP
- `tests.test_fast_integration.test_empty_dictionary`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '-i', 'test-files/2.test.txt.zip', '-p', '/tmp/tmpankyfv5p/empty.txt'], returncode=1, stdout=b'', stderr=b'').returncode
- *(... 120 more in this cluster)*

### `string_output_mismatch` — 60 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_help_baseline.TestHelpBaseline.test_help_exact_output`
  > AssertionError: assert 'Find the pas...der\n0.10.3\n' == 'Find the pas...int version\n'
  >   
  >     Find the password of protected ZIP files
  >   + --inputFile
  >   + --workers
  >   + --passwordDictionary
  >   + --charset
  >   + --help...
- `tests.test_help_baseline.TestHelpBaseline.test_short_help_exact_output`
  > AssertionError: assert 'zip-password...word-finder\n' == 'Find the pas...int version\n'
  >   
  >   + zip-password-finder
  >   + zip-password-finder
  >   - Find the password of protected ZIP files
  >   - 
  >   - Usage: executable [OPTIONS] --inputFile <inputFile>
  >   - ...
- `tests.test_help_baseline.TestHelpBaseline.test_missing_required_arg_exact_output`
  > assert '' == "error: the f...y '--help'.\n"
  >   
  >   - error: the following required arguments were not provided:
  >   -   --inputFile <inputFile>
  >   - 
  >   - Usage: executable --inputFile <inputFile>
  >   - 
  >   - For more information, try '--help'.
- *(... 57 more in this cluster)*

### `rc_mismatch_got0_want1` — 32 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_basic.test_input_file_short_flag`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', '-i', 'nonexistent.zip'], returncode=0, stdout=b'inputFile\ndoes not exist\ndoes not exist\nworkers\npositive\n', stderr=b'').returncode
- `tests.test_error_handling.test_input_file_does_not_exist`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', '-i', 'nonexistent.zip'], returncode=0, stdout=b'inputFile\ndoes not exist\ndoes not exist\nworkers\npositive\n', stderr=b'').returncode
- `tests.test_error_handling.test_min_password_length_zero_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', '-i', 'test-files/2.test.txt.zip', '--minPasswordLen', '0'], returncode=0, stdout=b'PK\x03\x043\x03\x01\x00c\x00Z_$T\x00\x00\x00\x00 \x00\x00\x00\x
- *(... 29 more in this cluster)*

### `rc_mismatch_got0_want2` — 31 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_basic_invocation.test_no_arguments`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['./executable'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_input_file_handling.test_missing_input_file_argument`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['./executable'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_basic.test_no_arguments_error`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['./executable'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 28 more in this cluster)*

### `rc_unexpected_zero` — 18 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_argument_parsing.TestRequiredArguments.test_no_arguments`
  > assert 0 != 0
- `tests.test_argument_parsing.TestRequiredArguments.test_missing_input_file`
  > assert 0 != 0
- `tests.test_argument_parsing.TestPasswordLengthArguments.test_min_password_len_negative`
  > assert 0 != 0
- *(... 15 more in this cluster)*

### `rc_mismatch_got1_want2` — 13 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_argument_parsing.TestWorkersArgument.test_workers_non_integer`
  > assert 1 == 2
- `tests.test_argument_parsing.TestWorkersArgument.test_workers_float`
  > assert 1 == 2
- `tests.test_argument_parsing.TestUnknownArguments.test_positional_argument`
  > assert 1 == 2
- *(... 10 more in this cluster)*

### `returned_none` — 12 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_basic_invocation.test_version_short_flag`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7feb1548b760>(b'\\d+\\.\\d+\\.\\d+', b'zip-password-finder\n')
  >  +    where <function search at 0x7feb1548b760> = re.search
  >  +    and   b'zip-password-finder\n' = CompletedProcess(args=['./executable', '-V'], returncode=0, stdout=b'zip-password-finder\n', stderr=b'').stdout
- `tests.test_output_format.test_output_time_elapsed`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7feb1548b760>(b'\\d+\\w+', b'Time elapsed:\nPassword\nTime elapsed:\nPassword\nTime elapsed:\nPassword\nTime elapsed:\nPassword\nTime elapsed:\nPassword\n')
  >  +    where <function search at 0x7feb1548b760> = re.search
  >  +    and   b'Time elapsed:\nPassword\nTime elapsed:\nPassword\nTime elapsed:\nPassword\nTime elapsed:\nPassword\nTime elapsed:\nPassword\n' = CompletedProcess(args=['./executable', '-i', 'test-files/
- `tests.test_basic.test_version_short_flag`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7fdc8f32b760>(b'\\d+\\.\\d+\\.\\d+', b'zip-password-finder\n')
  >  +    where <function search at 0x7fdc8f32b760> = re.search
  >  +    and   b'zip-password-finder\n' = CompletedProcess(args=['./executable', '-V'], returncode=0, stdout=b'zip-password-finder\n', stderr=b'').stdout
- *(... 9 more in this cluster)*

### `bytes_output_mismatch` — 5 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_harvest.test_verify_command_version`
  > AssertionError: assert 'zip-password...word found:ab' == 'zip-password-finder 0.10.3'
  >   
  >   - zip-password-finder 0.10.3
  >   ?                    ^^^^^^^
  >   + zip-password-finder
  >   ?                    ^
  >   + 0.10.3
  >   + Password found:ab
- `tests.test_zip_files.test_starting_password_with_dictionary`
  > assert "error: [Errn...rectory: 'ab'" == 'CLI argument...tionary file"'
  >   
  >   - CLI argument error - "'startingPassword' cannot be used with a dictionary file"
  >   + error: [Errno 2] No such file or directory: 'ab'
- `eval.tests.test_bruteforce_charset.test_unknown_charset_is_cli_error_exit_1_and_message_on_stderr`
  > AssertionError: assert b'Password fo...d not found\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'Password found:ab\nPassword found:abc\nPassword not found\n')
- *(... 2 more in this cluster)*

### `rc_mismatch_got2_want1` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_input_file_handling.test_invalid_file_not_zip`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['./executable', '-i', '/tmp/tmpoizce4fl/not_a_zip.txt', '--minPasswordLen', '1', '--maxPasswordLen', '1', '-c', 'd', '-w', '1'], returncode=2, stdout=b'Time elapse
- `tests.test_input_file_handling.test_empty_file_as_zip`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['./executable', '-i', '/tmp/tmpgyeayzxb/empty.zip', '--minPasswordLen', '1', '--maxPasswordLen', '1', '-c', 'd', '-w', '1'], returncode=2, stdout=b'Time elapsed:\n

### `rc_mismatch_got4_want2` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli.test_version_long_flag`
  > AssertionError: assert 4 == 2
  >  +  where 4 = len(['zip-password-finder', '0.10.3', 'Password', 'found:ab'])

### `boolean_false` — 1 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `eval.tests.test_executable_behavior.test_version_output_format`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7efcaa75acd0>('zip-password-finder ')
  >  +    where <built-in method startswith of str object at 0x7efcaa75acd0> = 'zip-password-finder\n0.10.3\nPassword found:ab\n'.startswith

