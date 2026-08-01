# Action Sheet — lfos__calcurse.49180d5

**Current:** 7.26%  (108/1488)
**Pass / Fail / Skip:** 108 / 775 / 0
**Gap to 100%:** 92.74 percentage points (1380 tests)

## Failure clusters

775 failed tests grouped into 11 buckets (sorted by count).

### `rc_mismatch_got2_want0` — 507 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_basic_invocation.test_read_only_flag_with_query`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '-D', '/tmp/pytest-of-root/pytest-0/test_read_only_flag_with_query2/data', '--read-only', '-Q'], returncode=2, stdout=b'', stderr=b'calcurse: error
- `tests.test_comprehensive_coverage.test_pcal_export_basic`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '-D', '/tmp/pytest-of-root/pytest-0/test_pcal_export_basic2/data', '-x', 'pcal'], returncode=2, stdout=b'', stderr=b'calcurse: error: unrecognized 
- `tests.test_comprehensive_coverage.test_pcal_export_with_events`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '-D', '/tmp/pytest-of-root/pytest-0/test_pcal_export_with_events2/data', '-x', 'pcal'], returncode=2, stdout=b'', stderr=b'calcurse: error: unrecog
- *(... 504 more in this cluster)*

### `other_assertion` — 123 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_help_long`
  > AssertionError: assert b'-Q, --query' in b'calcurse 4.8.1 -- a text-based calendar and scheduling application\n\nUsage: calcurse [OPTION]... [FILE]...\n\nOptions:\n  -a, --appointment    show appointm
  >  +  where b'calcurse 4.8.1 -- a text-based calendar and scheduling application\n\nUsage: calcurse [OPTION]... [FILE]...\n\nOptions:\n  -a, --appointment    show appointments\n  -c, --calendar       sh
- `tests.test_basic_invocation.test_version_short`
  > AssertionError: assert b'text-based organizer' in b'calcurse 4.8.1\n'
  >  +  where b'calcurse 4.8.1\n' = CompletedProcess(args=['./executable', '-v'], returncode=0, stdout=b'calcurse 4.8.1\n', stderr=b'').stdout
- `tests.test_basic_invocation.test_version_long`
  > AssertionError: assert b'Copyright' in b'calcurse 4.8.1\n'
  >  +  where b'calcurse 4.8.1\n' = CompletedProcess(args=['./executable', '--version'], returncode=0, stdout=b'calcurse 4.8.1\n', stderr=b'').stdout
- *(... 120 more in this cluster)*

### `uncategorized` — 97 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_data_operations.TestDataOperations.test_purge_operation_readonly`
  > Failed: Command failed with exit code 2: calcurse: error: unrecognized argument: -D
- `tests.test_data_operations.TestDataOperations.test_purge_operation_write`
  > Failed: Command failed with exit code 2: calcurse: error: unrecognized argument: -D
- `tests.test_data_operations.TestDataOperations.test_grep_operation_basic`
  > Failed: Command failed with exit code 2: calcurse: error: unrecognized argument: -D
- *(... 94 more in this cluster)*

### `string_output_mismatch` — 21 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_output.test_baseline_help_output_exact_match`
  > AssertionError: assert 'calcurse 4.8...lcurse.org>\n' == 'Usage:\ncalc...curse.org>.\n'
  >   
  >   + calcurse 4.8.1 -- a text-based calendar and scheduling application
  >   - Usage:
  >   - calcurse [-D <directory>] [-C <directory>] [-c <calendar file>]
  >   - calcurse -Q [--from <date>] [--to <date>] [--days <number>]
  >   - calcurse -a | -d <date> | -d <number> | -n | -r[<number>] | -s[<date>] | -t[<number>]
  >   - calcurse -h | -v | --status | -G | -P | -g | -i <file> | -x[<format>] | --daemon...
- `tests.test_calcurse.test_appointment_output[appointment-002-extra_args0]`
  > AssertionError: assert '' == '02/23/13:\n ...Appointment\n'
  >   
  >   - 02/23/13:
  >   -  - 10:00 -> 12:00
  >   - 	Appointment
- `tests.test_calcurse.test_appointment_output[appointment-003-extra_args1]`
  > AssertionError: assert '' == '02/23/13:\n ...Appointment\n'
  >   
  >   - 02/23/13:
  >   -  - 10:00 -> ..:..
  >   - 	Appointment
- *(... 18 more in this cluster)*

### `rc_unexpected_zero` — 16 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_comprehensive_coverage.test_invalid_calendar_file`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '-c', '/nonexistent/file', '-Q'], returncode=0, stdout=b'May 2026\n      May 2026\nMo Tu We Th Fr Sa Su\n             1  2  3\n 4  5  6  7  8  9 10
- `tests.test_comprehensive_coverage.test_invalid_import_file`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '-i', '/nonexistent/file.ics'], returncode=0, stdout=b'Importing from /nonexistent/file.ics\n', stderr=b'').returncode
- `tests.test_comprehensive_coverage.test_invalid_export_format`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '-x', 'invalid_format'], returncode=0, stdout=b'BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:-//calcurse//NONSGML v4.8.1//EN\nBEGIN:VTIMEZONE\nTZID:/freeas
- *(... 13 more in this cluster)*

### `boolean_false` — 4 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `eval.tests.test_help_output.test_help_has_usage_header`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x558e27fb4300>('Usage:\n')
  >  +    where <built-in method startswith of str object at 0x558e27fb4300> = 'calcurse 4.8.1 -- a text-based calendar and scheduling application\n\nUsage: calcurse [OPTION]... [FILE]...\n\nOptions:\n  -
  >  +      where 'calcurse 4.8.1 -- a text-based calendar and scheduling application\n\nUsage: calcurse [OPTION]... [FILE]...\n\nOptions:\n  -a, --appointment    show appointments\n  -c, --calendar      
- `eval.tests.test_help_output.test_help_precedes_after_double_dash_separator`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x558e2808f090>('Usage:\n')
  >  +    where <built-in method startswith of str object at 0x558e2808f090> = 'calcurse 4.8.1 -- a text-based calendar and scheduling application\n\nUsage: calcurse [OPTION]... [FILE]...\n\nOptions:\n  -
  >  +      where 'calcurse 4.8.1 -- a text-based calendar and scheduling application\n\nUsage: calcurse [OPTION]... [FILE]...\n\nOptions:\n  -a, --appointment    show appointments\n  -c, --calendar      
- `tests.test_calcurse.test_io_001`
  > AssertionError: assert False
  >  +  where False = <function isfile at 0x7f8a2d9a5fc0>('/tmp/tmpcu2shcw6/apts')
  >  +    where <function isfile at 0x7f8a2d9a5fc0> = <module 'posixpath' from '/usr/lib/python3.10/posixpath.py'>.isfile
  >  +      where <module 'posixpath' from '/usr/lib/python3.10/posixpath.py'> = os.path
  >  +    and   '/tmp/tmpcu2shcw6/apts' = <function join at 0x7f8a2d9a67a0>('/tmp/tmpcu2shcw6', 'apts')
  >  +      where <function join at 0x7f8a2d9a67a0> = <module 'posixpath' from '/usr/lib/python3.10/posixpath.py'>.join
  >  +        where <module 'posixpath' from '/usr/lib/python3.10/posixpath.py'> = os.path
- *(... 1 more in this cluster)*

### `rc_mismatch_got0_want1` — 2 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `eval.tests.test_help_output.test_help_with_unrecognized_option_prints_error_first_then_usage`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--help', '--badflag'], returncode=0, stdout='calcurse 4.8.1 -- a text-based calendar and scheduling application\n\nUsage: calcurse [OPTIO
- `eval.tests.test_import.test_import_missing_file_errors_to_stderr_and_exit_1`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-i', '/no/such/file'], returncode=0, stdout=b'Importing from /no/such/file\n', stderr=b'').returncode

### `bytes_output_mismatch` — 2 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `eval.tests.test_cli_golden.test_help_exact_stdout`
  > assert b'calcurse 4....lcurse.org>\n' == b"Usage:\ncal...curse.org>.\n"
  >   
  >   At index 0 diff: b'c' != b'U'
  >   
  >   Full diff:
  >   + (b'calcurse 4.8.1 -- a text-based calendar and scheduling application\n\nUsag'
  >   +  b'e: calcurse [OPTION]... [FILE]...\n\nOptions:\n  -a, --appointment    show '
  >   +  b'appointments\n  -c, --calendar       show calendar\n  -d, --day           '...
- `eval.tests.test_cli_golden.test_version_exact_stdout`
  > AssertionError: assert b'calcurse 4.8.1\n' == b'calcurse 4....conditions.\n'
  >   
  >   At index 13 diff: b'1' != b'2'
  >   
  >   Full diff:
  >   + (b'calcurse 4.8.1\n')
  >   - (b'calcurse 4.8.2 -- text-based organizer\n\nCopyright (c) 2004-2023 calcurse'
  >   -  b' Development Team.\nThis is free software; see the source for copying con'

### `rc_mismatch_got2_want1` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_help_output.test_unrecognized_option_shows_error_and_usage_hint`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--badflag'], returncode=2, stdout='', stderr='calcurse: error: unrecognized argument: --badflag\n').returncode

### `returned_none` — 1 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_output.test_help_has_expected_indentation_for_sections`
  > AssertionError: assert None is not None
  >  +  where None = <function search at 0x7f688fece680>('^  -Q, --query\\s+Print items', 'calcurse 4.8.1 -- a text-based calendar and scheduling application\n\nUsage: calcurse [OPTION]... [FILE]...\n\nOp
  >  +    where <function search at 0x7f688fece680> = re.search
  >  +    and   re.MULTILINE = re.M

### `missing_file` — 1 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_calcurse.test_ical_011_export_import_roundtrip`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpui7v6jo4/apts'

