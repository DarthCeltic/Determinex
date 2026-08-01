# Action Sheet — duckdb__duckdb.bdb65ec

**Current:** 0.28%  (17/5988)
**Pass / Fail / Skip:** 17 / 774 / 104
**Gap to 100%:** 99.72 percentage points (5971 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_harvest_copy.test_sql_copy_file[test/sql/copy/csv/14874.test]`
  - reason: Test file marked as skip
- `tests.test_harvest_copy.test_sql_copy_file[test/sql/copy/csv/afl/fuzz_20250226.test]`
  - reason: Skipped: Requires extension
- `tests.test_harvest_copy.test_sql_copy_file[test/sql/copy/csv/afl/test_afl_ignore_errors.test]`
  - reason: Skipped: Contains foreach/loop construct
- `tests.test_harvest_copy.test_sql_copy_file[test/sql/copy/csv/afl/test_afl_no_parameter.test]`
  - reason: Skipped: Contains foreach/loop construct
- `tests.test_harvest_copy.test_sql_copy_file[test/sql/copy/csv/afl/test_afl_null_padding.test]`
  - reason: Skipped: Contains foreach/loop construct
- *(... 99 more skipped)*

## Failure clusters

774 failed tests grouped into 20 buckets (sorted by count).

### `rc_mismatch_got2_want0` — 224 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_duckdb_cli.TestBasicInvocation.test_help_flag_help`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-help'], returncode=2, stdout=b'', stderr=b"duckdb: unknown option: -help\nusage: duckdb [OPTIONS] [ARGS]\nTry 'duckdb --help' for more i
- `tests.test_duckdb_cli.TestBasicInvocation.test_help_shows_all_modes`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-help'], returncode=2, stdout=b'', stderr=b"duckdb: unknown option: -help\nusage: duckdb [OPTIONS] [ARGS]\nTry 'duckdb --help' for more i
- `tests.test_duckdb_cli.TestBasicInvocation.test_version_flag`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-version'], returncode=2, stdout=b'', stderr=b"duckdb: unknown option: -version\nusage: duckdb [OPTIONS] [ARGS]\nTry 'duckdb --help' for 
- *(... 221 more in this cluster)*

### `uncategorized` — 179 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_harvest_copy.test_sql_copy_file[test/sql/copy/copy_blob.test]`
  > Failed: Test case 0 (statement error) succeeded but should have failed:
  > SQL: COPY (select 'foo') TO '{TEST_DIR}/test.blob' (FORMAT BLOB);
- `tests.test_harvest_copy.test_sql_copy_file[test/sql/copy/csv/14512.test]`
  > Failed: Test case 1 (query) result mismatch:
  > SQL: FROM read_csv('{DATA_DIR}/csv/14512.csv', strict_mode=TRUE);
  > Expected: ['onions', ',']
  > Got: []
  > Raw output:
  > FROM READ_CSV('/WORKSPACE/DATA/CSV/14512.CSV', STRICT_MODE=TRUE);
- `tests.test_harvest_copy.test_sql_copy_file[test/sql/copy/csv/17738.test]`
  > Failed: Test case 1 (query) result mismatch:
  > SQL: FROM read_csv('{DATA_DIR}/csv/17738_rn.csv',header=False,skip=3, delim = ';');
  > Expected: ['xyz', 'lorem ipsum', 'NULL', 'NULL', 'John,Doe,120 jefferson st.,Riverside, NJ, 08075', 'Jack,McGinnis,220 hobo Av.,Phila, PA,09119', '"John ""Da Man""",Repici,120 Jefferson St.,Riverside,
  > Got: []
  > Raw output:
  > FROM READ_CSV('/WORKSPACE/DATA/CSV/17738_RN.CSV',HEADER=FALSE,SKIP=3, DELIM = ';');
- *(... 176 more in this cluster)*

### `string_output_mismatch` — 98 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_cli_database.test_readonly_allows_select`
  > AssertionError: assert '' == 'id\n99'
  >   
  >   - id
  >   - 99
- `tests.test_cli_database.test_safe_mode_allows_normal_queries`
  > AssertionError: assert '' == 'id\n1\n2'
  >   
  >   - id
  >   - 1
  >   - 2
- `tests.test_cli_database.test_database_persistence_across_invocations`
  > AssertionError: assert '' == 'id,data\n1,f...n2,second run'
  >   
  >   - id,data
  >   - 1,first run
  >   - 2,second run
- *(... 95 more in this cluster)*

### `rc_mismatch_got2_want1` — 80 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_execution.test_c_error_handling`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-c', 'SELECT * FROM nonexistent_table'], returncode=2, stdout='', stderr="duckdb: unknown option: -c\nusage: duckdb [OPTIONS] [ARGS]\nTry
- `tests.test_cli_execution.test_f_nonexistent_file`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-f', '/nonexistent/file.sql'], returncode=2, stdout='', stderr="duckdb: unknown option: -f\nusage: duckdb [OPTIONS] [ARGS]\nTry 'duckdb -
- `tests.test_cli_execution.test_f_with_syntax_error_and_bail`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-bail', '-f', '/workspace/eval/test_resources/test_cli_execution/syntax_error.sql'], returncode=2, stdout='', stderr="duckdb: unknown opt
- *(... 77 more in this cluster)*

### `other_assertion` — 75 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_duckdb_cli.TestBasicInvocation.test_help_flag_h`
  > AssertionError: assert b'FILENAME' in b'duckdb 0.1.0 - bootstrap scaffold\n\nUsage: duckdb [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n'
  >  +  where b'duckdb 0.1.0 - bootstrap scaffold\n\nUsage: duckdb [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['/workspace/executa
- `tests.test_duckdb_cli.TestBasicInvocation.test_unrecognized_option`
  > assert (b'Unrecognized' in b"duckdb: unknown option: -xyz_nonexistent_option\nusage: duckdb [OPTIONS] [ARGS]\nTry 'duckdb --help' for more information.\n" or b'Unknown' in b"duckdb: unknown option: -x
  >  +  where b"duckdb: unknown option: -xyz_nonexistent_option\nusage: duckdb [OPTIONS] [ARGS]\nTry 'duckdb --help' for more information.\n" = CompletedProcess(args=['/workspace/executable', '-xyz_nonexi
  >  +  and   b"duckdb: unknown option: -xyz_nonexistent_option\nusage: duckdb [OPTIONS] [ARGS]\nTry 'duckdb --help' for more information.\n" = CompletedProcess(args=['/workspace/executable', '-xyz_nonexi
- `tests.test_duckdb_cli.TestBasicInvocation.test_help_shows_usage_format`
  > AssertionError: assert b'FILENAME' in b'duckdb 0.1.0 - bootstrap scaffold\n\nUsage: duckdb [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n'
  >  +  where b'duckdb 0.1.0 - bootstrap scaffold\n\nUsage: duckdb [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['/workspace/executa
- *(... 72 more in this cluster)*

### `rc_unexpected_zero` — 42 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_cli_database.test_readonly_prevents_insert`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/tmp/tmp0r8tbax_.duckdb', '-readonly', '-c', 'INSERT INTO readonly_test VALUES (100);'], returncode=0, stdout='\n', stderr='').returncode
- `tests.test_cli_database.test_readonly_prevents_update`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/tmp/tmpyqw20jhv.duckdb', '-readonly', '-c', 'UPDATE readonly_test SET id = 2;'], returncode=0, stdout='\n', stderr='').returncode
- `tests.test_cli_database.test_readonly_prevents_delete`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/tmp/tmpqjz1kmyz.duckdb', '-readonly', '-c', 'DELETE FROM readonly_test;'], returncode=0, stdout='\n', stderr='').returncode
- *(... 39 more in this cluster)*

### `json_output_missing_or_bad` — 19 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `tests.test_cli_dotcommands.test_mode_json`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_cli_formats.test_json_basic`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_cli_formats.test_json_all_nulls`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- *(... 16 more in this cluster)*

### `missing_file` — 10 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_cli_database.test_readonly_data_not_modified`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpor_aqu12.duckdb'
- `tests.test_cli_database.test_database_file_permissions_readonly_filesystem`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpz5h3b1ss/test.duckdb'
- `tests.test_cli_import_export.test_output_redirect_to_file_and_restore_stdout`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_output_redirect_to_file_a2/output.txt'
- *(... 7 more in this cluster)*

### `rc_mismatch_got0_want1` — 9 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_cli_dotcommands.test_timer_on`
  > AssertionError: assert 0 == 1
  >  +  where 0 = <built-in method count of str object at 0x7fc080756010>('Run Time (s):')
  >  +    where <built-in method count of str object at 0x7fc080756010> = '.TIMER ON\nSELECT COUNT(*) FROM EMPLOYEES;\n\n'.count
  >  +      where '.TIMER ON\nSELECT COUNT(*) FROM EMPLOYEES;\n\n' = CompletedProcess(args=['/workspace/executable', '/tmp/tmpgtz086g6.duckdb'], returncode=0, stdout='.TIMER ON\nSELECT COUNT(*) FROM EMPLO
- `tests.test_cli_dotcommands.test_bail_on_error`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/tmp/tmp9tt48vse.duckdb'], returncode=0, stdout=".BAIL ON\nSELECT * FROM NONEXISTENT_TABLE;\nSELECT 'THIS SHOULD NOT EXECUTE';\n\n", stde
- `tests.test_cli_dotcommands.test_timer_off`
  > AssertionError: assert 0 == 1
  >  +  where 0 = <built-in method count of str object at 0x7fc080c4efe0>('Run Time (s):')
  >  +    where <built-in method count of str object at 0x7fc080c4efe0> = '.TIMER ON\nSELECT * FROM TEST;\n.TIMER OFF\nSELECT * FROM TEST;\n\n'.count
  >  +      where '.TIMER ON\nSELECT * FROM TEST;\n.TIMER OFF\nSELECT * FROM TEST;\n\n' = CompletedProcess(args=['/workspace/executable', '/tmp/tmpkw7zgutr.duckdb'], returncode=0, stdout='.TIMER ON\nSELEC
- *(... 6 more in this cluster)*

### `rc_mismatch_got1_want2` — 9 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_formats.test_jsonlines_basic`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len([''])
- `tests.test_cli_formats.test_list_basic`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len([''])
- `tests.test_cli_formats.test_quote_basic`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len([''])
- *(... 6 more in this cluster)*

### `boolean_false` — 8 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_cli_database.test_create_new_database`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmp_tx_yboa.duckdb').exists
  >  +      where PosixPath('/tmp/tmp_tx_yboa.duckdb') = Path('/tmp/tmp_tx_yboa.duckdb')
- `tests.test_cli_database.test_database_file_with_spaces_in_path`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpnak9oigf/my database file.duckdb').exists
  >  +      where PosixPath('/tmp/tmpnak9oigf/my database file.duckdb') = Path('/tmp/tmpnak9oigf/my database file.duckdb')
- `tests.test_cli_database.test_empty_database_file_query`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmp1cm8qmgn.duckdb').exists
  >  +      where PosixPath('/tmp/tmp1cm8qmgn.duckdb') = Path('/tmp/tmp1cm8qmgn.duckdb')
- *(... 5 more in this cluster)*

### `rc_mismatch_got0_want2` — 5 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_cli_formats.test_html_empty_nullvalue`
  > assert 0 == 2
  >  +  where 0 = len([])
- `tests.test_cli_flags.test_html_output_escaping`
  > assert 0 == 2
  >  +  where 0 = len([])
- `tests.test_cli_flags.test_custom_nullvalue_in_csv`
  > assert 0 == 2
  >  +  where 0 = len([])
- *(... 2 more in this cluster)*

### `rc_mismatch_got0_want3` — 4 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_formats.test_html_basic`
  > assert 0 == 3
  >  +  where 0 = len([])
- `tests.test_cli_formats.test_html_multirow`
  > assert 0 == 3
  >  +  where 0 = len([])
- `tests.test_cli_formats.test_html_with_null`
  > assert 0 == 3
  >  +  where 0 = len([])
- *(... 1 more in this cluster)*

### `rc_mismatch_got1_want3` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_flags.test_line_format_key_value_pairs`
  > AssertionError: assert 1 == 3
  >  +  where 1 = len([''])
- `tests.test_cli_flags.test_column_format_aligned_output`
  > AssertionError: assert 1 == 3
  >  +  where 1 = len([''])
- `tests.test_cli_flags.test_markdown_with_null_values_and_alignment`
  > AssertionError: assert 1 == 3
  >  +  where 1 = len([''])

### `rc_mismatch_got2_want42` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_duckdb_cli.TestDotCommandDataOperations.test_dot_exit_with_custom_code`
  > assert 2 == 42
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--batch', '--no-init'], returncode=2, stdout=b'', stderr=b"duckdb: unknown option: --batch\nusage: duckdb [OPTIONS] [ARGS]\nTry 'duckdb -
- `tests.test_cli_dotcommands.test_exit_with_code`
  > assert 2 == 42
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout='', stderr="usage: duckdb [OPTIONS] [ARGS]\nTry 'duckdb --help' for more information.\n").returncode

### `bytes_output_mismatch` — 2 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_cli_database.test_open_existing_database`
  > AssertionError: assert '' == 'id,name\n1,Alice\n2,Bob'
  >   
  >   - id,name
  >   - 1,Alice
  >   - 2,Bob
- `tests.test_cli_database.test_memory_database_basic`
  > AssertionError: assert '' == 'id,name\n1,Alice\n2,Bob'
  >   
  >   - id,name
  >   - 1,Alice
  >   - 2,Bob

### `rc_mismatch_got1_want4` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_flags.test_markdown_table_format`
  > AssertionError: assert 1 == 4
  >  +  where 1 = len([''])
- `tests.test_cli_flags.test_ascii_format_simple_output`
  > AssertionError: assert 1 == 4
  >  +  where 1 = len([''])

### `rc_mismatch_got0_want4` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_formats.test_html_noheader`
  > assert 0 == 4
  >  +  where 0 = len([])

### `rc_mismatch_got1_want10` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_formats.test_jsonlines_multiple_rows`
  > AssertionError: assert 1 == 10
  >  +  where 1 = len([''])

### `rc_mismatch_got1_want5` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_flags.test_jsonlines_with_generated_series`
  > AssertionError: assert 1 == 5
  >  +  where 1 = len([''])

