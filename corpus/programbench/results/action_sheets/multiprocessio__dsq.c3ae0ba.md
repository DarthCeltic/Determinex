# Action Sheet — multiprocessio__dsq.c3ae0ba

**Current:** 7.54%  (74/982)
**Pass / Fail / Skip:** 74 / 667 / 3
**Gap to 100%:** 92.46 percentage points (908 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_harvest.test_caching_first_import`
  - reason: taxi.csv not available for cache tests
- `tests.test_harvest.test_caching_from_pipe`
  - reason: taxi.csv not available for cache tests
- `tests.test_harvest.test_caching_reimport_on_change`
  - reason: taxi.csv not available for cache tests

## Failure clusters

667 failed tests grouped into 11 buckets (sorted by count).

### `rc_mismatch_got1_want0` — 264 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_advanced_features.test_excel_multiple_sheets`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', 'testdata/excel/multiple-sheets.xlsx'], returncode=1, stdout=b'', stderr=b'Traceback (most recent call last):\n  File "/workspace/main.py", line 28
- `tests.test_advanced_features.test_no_sqlite_writer_env`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', 'testdata/userdata.csv', 'SELECT COUNT(*) as total FROM {}'], returncode=1, stdout=b'', stderr=b'dsq: file not found: SELECT COUNT(*) as total FROM
- `tests.test_advanced_features.test_string_functions`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', 'testdata/userdata.csv', 'SELECT UPPER(State) as upper_state FROM {} LIMIT 3'], returncode=1, stdout=b'', stderr=b'dsq: file not found: SELECT UPPE
- *(... 261 more in this cluster)*

### `subprocess_failed` — 191 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_env_cache.test_dsq_convert_numbers_env_var_converts_numeric_strings`
  > subprocess.CalledProcessError: Command '['/workspace/executable', '/workspace/eval/test_resources/test_env_cache/numbers.csv', 'SELECT * FROM {}']' returned non-zero exit status 1.
- `tests.test_env_cache.test_dsq_convert_numbers_false_keeps_strings`
  > subprocess.CalledProcessError: Command '['/workspace/executable', '/workspace/eval/test_resources/test_env_cache/numbers.csv', 'SELECT * FROM {}']' returned non-zero exit status 1.
- `tests.test_env_cache.test_dsq_convert_numbers_default_no_conversion`
  > subprocess.CalledProcessError: Command '['/workspace/executable', '/workspace/eval/test_resources/test_env_cache/numbers.csv', 'SELECT * FROM {}']' returned non-zero exit status 1.
- *(... 188 more in this cluster)*

### `rc_mismatch_got2_want0` — 90 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_advanced_features.test_no_sqlite_writer_flag`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--no-sqlite-writer', 'testdata/userdata.csv', 'SELECT COUNT(*) as total FROM {}'], returncode=2, stdout=b'', stderr=b"dsq: unknown option: --no-sq
- `tests.test_basic_invocation.test_version_short_flag`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '-v'], returncode=2, stdout=b'', stderr=b"dsq: unknown option: -v\nusage: dsq [OPTIONS] [ARGS]\nTry 'dsq --help' for more information.\n").returnco
- `tests.test_basic_invocation.test_verbose_flag`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--verbose', 'testdata/userdata.csv', 'SELECT COUNT(*) as count FROM {}'], returncode=2, stdout=b'', stderr=b"dsq: unknown option: --verbose\nusage
- *(... 87 more in this cluster)*

### `other_assertion` — 70 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_no_arguments_shows_error`
  > assert (b'No input' in b"usage: dsq [OPTIONS] [ARGS]\nTry 'dsq --help' for more information.\n" or b'input' in b"usage: dsq [options] [args]\ntry 'dsq --help' for more information.\n")
  >  +  where b"usage: dsq [options] [args]\ntry 'dsq --help' for more information.\n" = <built-in method lower of bytes object at 0x7efdc415e1e0>()
  >  +    where <built-in method lower of bytes object at 0x7efdc415e1e0> = b"usage: dsq [OPTIONS] [ARGS]\nTry 'dsq --help' for more information.\n".lower
- `tests.test_basic_invocation.test_help_flag`
  > AssertionError: assert (b'SQL' in b'dsq 0.1.0 - bootstrap scaffold\n\nUsage: dsq [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n\n' or b'SQL' in b'')
  >  +  where b'dsq 0.1.0 - bootstrap scaffold\n\nUsage: dsq [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n\n' = CompletedProcess(args=['./executable', '--help
  >  +  and   b'' = CompletedProcess(args=['./executable', '--help'], returncode=0, stdout=b'dsq 0.1.0 - bootstrap scaffold\n\nUsage: dsq [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, -
- `tests.test_basic_invocation.test_help_short_flag`
  > AssertionError: assert (b'commandline' in b'dsq 0.1.0 - bootstrap scaffold\n\nUsage: dsq [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n\n' or b'SQL' in b'd
- *(... 67 more in this cluster)*

### `string_output_mismatch` — 38 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_usage.test_help_emitted_to_stderr_not_stdout`
  > AssertionError: assert 'dsq 0.1.0 - ...t version\n\n' == ''
  >   
  >   + dsq 0.1.0 - bootstrap scaffold
  >   + 
  >   + Usage: dsq [OPTIONS] [ARGS]
  >   + 
  >   + Options:
  >   +   -h, --help     Print help
- `eval.tests.test_help_usage.test_baseline_help_text_matches_fixture_exactly`
  > AssertionError: assert '' == 'dsq (Version...ocessio/dsq\n'
  >   
  >   - dsq (Version latest) - commandline SQL engine for data files
  >   - 
  >   - Usage:  dsq [file...] $query
  >   -         dsq $file [query]
  >   -         cat $file | dsq -s $filetype [query]
  >   -         dsq $file -f $queryfile...
- `tests.test_exact_output.TestExactOutput.test_help_output_exact`
  > AssertionError: assert '' == 'dsq (Version...ocessio/dsq\n'
  >   
  >   - dsq (Version latest) - commandline SQL engine for data files
  >   - 
  >   - Usage:  dsq [file...] $query
  >   -         dsq $file [query]
  >   -         cat $file | dsq -s $filetype [query]
  >   -         dsq $file -f $queryfile...
- *(... 35 more in this cluster)*

### `rc_mismatch_got2_want1` — 7 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_no_arguments_error`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['./executable'], returncode=2, stdout=b'', stderr=b"usage: dsq [OPTIONS] [ARGS]\nTry 'dsq --help' for more information.\n").returncode
- `tests.test_schema_and_files.test_query_file_missing_error`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['./executable', 'testdata/join/users.csv', '-f', 'nonexistent.sql'], returncode=2, stdout=b'', stderr=b"dsq: unknown option: -f\nusage: dsq [OPTIONS] [ARGS]\nTry '
- `tests.test_schema_and_files.test_query_file_empty_error`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['./executable', 'testdata/join/users.csv', '-f', '/tmp/tmp1ze9ksab/empty.sql'], returncode=2, stdout=b'', stderr=b"dsq: unknown option: -f\nusage: dsq [OPTIONS] [A
- *(... 4 more in this cluster)*

### `rc_mismatch_got0_want1` — 2 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_basic_invocation.test_unknown_file_type_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', '/tmp/tmp79q72n6d/test.unknown'], returncode=0, stdout=b'[]\n', stderr=b'').returncode
- `tests.test_error_handling.test_empty_query_string`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', 'testdata/join/users.csv', ''], returncode=0, stdout=b'[]\n', stderr=b'').returncode

### `boolean_false` — 2 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `eval.tests.test_help_usage.test_help_ends_with_single_newline`
  > AssertionError: assert False
  >  +  where False = <built-in method endswith of str object at 0x7f3c04a14030>('\n')
  >  +    where <built-in method endswith of str object at 0x7f3c04a14030> = ''.endswith
  >  +      where '' = CompletedProcess(args=['/workspace/executable', '--help'], returncode=0, stdout='dsq 0.1.0 - bootstrap scaffold\n\nUsage: dsq [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print he
- `eval.tests.test_dsq_behavior.test_help_text_starts_with_banner`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7f3e2f0d1ef0>('dsq (Version latest) - commandline SQL engine for data files\n')
  >  +    where <built-in method startswith of str object at 0x7f3e2f0d1ef0> = 'dsq 0.1.0 - bootstrap scaffold\n\nUsage: dsq [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Pri

### `bytes_output_mismatch` — 1 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `eval.tests.test_dsq_io.test_help_includes_usage_and_examples`
  > AssertionError: assert b'dsq 0.1.0 -...t version\n\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'dsq 0.1.0 - bootstrap scaffold\n\nUsage: dsq [OPTIONS] [ARGS]\n\nOptions'
  >   +  b':\n  -h, --help     Print help\n  -V, --version  Print version\n\n')

### `rc_unexpected_zero` — 1 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_subcommands.TestNotSubcommandBased.test_common_subcommand_names_not_recognized[help]`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'help'], returncode=0, stdout='dsq 0.1.0 - bootstrap scaffold\n\nUsage: dsq [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -

### `rc_mismatch_got3_want1` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_harvest.test_version_flag`
  > assert 3 == 1
  >  +  where 3 = len(['dsq: unknown option: -v', 'usage: dsq [OPTIONS] [ARGS]', "Try 'dsq --help' for more information."])

