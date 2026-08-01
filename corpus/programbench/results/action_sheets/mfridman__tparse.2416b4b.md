# Action Sheet — mfridman__tparse.2416b4b

**Current:** 37.25%  (244/655)
**Pass / Fail / Skip:** 244 / 312 / 0
**Gap to 100%:** 62.75 percentage points (411 tests)

## Failure clusters

312 failed tests grouped into 9 buckets (sorted by count).

### `other_assertion` — 140 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_additional_coverage.test_compare_flag_experimental`
  > AssertionError: assert 2 in [0, 1]
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-file', '/tmp/tmpvwljpsc2/test2.jsonl', '-compare', '/tmp/tmpvwljpsc2/test1.jsonl'], returncode=2, stdout=b'', stderr=b'flag provided but
- `tests.test_additional_coverage.test_sort_by_elapsed_descending`
  > assert 727 < 667
- `tests.test_additional_coverage.test_coverage_with_multiple_packages`
  > AssertionError: assert (b'60' in b'\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\
  >  +  where b'\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94
  >  +  and   b'\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94
- *(... 137 more in this cluster)*

### `rc_mismatch_got2_want0` — 56 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_additional_coverage.test_markdown_table_output`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-file', '/tmp/tmp_n0aof1c/test.jsonl', '-format', 'markdown', '-pass'], returncode=2, stdout=b'', stderr=b'flag provided but not defined:
- `tests.test_additional_coverage.test_plain_format_output`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-file', '/tmp/tmpz0yts7m5/test.jsonl', '-format', 'plain', '-pass'], returncode=2, stdout=b'', stderr=b'flag provided but not defined: -f
- `tests.test_follow_mode.test_include_timestamp_flag`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-file', '/tmp/tmp7yr4w2qq/test.jsonl', '-follow', '-include-timestamp'], returncode=2, stdout=b'', stderr=b'flag provided but not defined
- *(... 53 more in this cluster)*

### `string_output_mismatch` — 56 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_argparse_validation.test_no_args_requires_pipe_or_file`
  > AssertionError: assert 'error: no pa... add -json?\n' == ''
  >   
  >   + error: no parsable events; did you forget to add -json?
- `eval.tests.test_argparse_validation.test_enum_flags_invalid_choice_prints_error_and_exit_0_when_pipe_present[args0-invalid option:"bad". The -sort flag must be one of: name, elapsed or cover]`
  > AssertionError: assert '┌───────────... 0  SKIP: 0\n' == ''
  >   
  >   + ┌──────────────────────────────┬────────┬──────────┐
  >   + │ Package                      │ Status │ Elapsed  │
  >   + ├──────────────────────────────┼────────┼──────────┤
  >   + │ example.com/p                │ ?      │   0.00s │
  >   + └──────────────────────────────┴────────┴──────────┘
  >   + ...
- `eval.tests.test_tparse_cli.test_help_text_exact`
  > AssertionError: assert 'Usage: tpars...lt: name)\n\n' == 'Usage:\n    ...ir display.\n'
  >   
  >   + Usage: tparse [OPTIONS]
  >   + 
  >   +   Parses go test -json output into a formatted table.
  >   - Usage:
  >   -     go test ./... -json | tparse [options...]
  >   -     go test [packages...] -json | tparse [options...]...
- *(... 53 more in this cluster)*

### `rc_mismatch_got0_want1` — 27 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_failed_tests.test_failed_tests_always_displayed`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-file', '/workspace/tests/testdata/failed/test_02.jsonl'], returncode=0, stdout=b'\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x9
- `tests.test_failed_tests.test_failed_test_names`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-file', '/workspace/tests/testdata/failed/test_02.jsonl'], returncode=0, stdout=b'\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x9
- `tests.test_failed_tests.test_failed_test_output`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-file', '/workspace/tests/testdata/failed/test_02.jsonl'], returncode=0, stdout=b'\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x9
- *(... 24 more in this cluster)*

### `rc_mismatch_got2_want1` — 21 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_edge_cases.test_format_plain_with_failed_tests`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-format', 'plain', '-file', '/workspace/tests/testdata/failed/test_02.jsonl'], returncode=2, stdout=b'', stderr=b'flag provided but not d
- `eval.tests.test_argparse_validation.test_file_nonexistent_is_runtime_error_exit_1[args0]`
  > assert 2 == 1
- `eval.tests.test_argparse_validation.test_slow_accepts_int_values[args1]`
  > assert 2 == 1
- *(... 18 more in this cluster)*

### `boolean_false` — 7 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_follow_mode.test_follow_output_writes_to_file`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmppec8sw3_/output.txt').exists
- `tests.test_follow_mode.test_follow_output_takes_precedence`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmp6r008xno/output.txt').exists
- `tests.test_follow_mode.test_follow_output_to_file`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/pytest-of-root/pytest-0/test_follow_output_to_file2/follow_output.txt').exists
- *(... 4 more in this cluster)*

### `rc_mismatch_got1_want2` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_argparse_validation.test_flag_value_missing_for_file_is_parse_error_exit_2`
  > assert 1 == 2
- `eval.tests.test_argparse_validation.test_slow_requires_int_parse_error_exit_2[args0]`
  > assert 1 == 2
- `eval.tests.test_argparse_validation.test_follow_output_missing_value_is_parse_error_or_runtime_error[args0]`
  > assert 1 == 2

### `bytes_output_mismatch` — 1 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `eval.tests.test_errors_and_exit_codes.test_missing_file_exits_1_and_prints_error_to_stderr_only`
  > AssertionError: assert b'open does_n...r directory\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'open does_not_exist: no such file or directory\n')

### `missing_file` — 1 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `eval.tests.test_tparse_flags.test_follow_output_precedence_over_follow`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_follow_output_precedence_2/raw.out'

