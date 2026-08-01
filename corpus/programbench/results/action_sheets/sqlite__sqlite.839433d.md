# Action Sheet — sqlite__sqlite.839433d

**Current:** 0.95%  (135/14138)
**Pass / Fail / Skip:** 135 / 491 / 0
**Gap to 100%:** 99.05 percentage points (14003 tests)

## Failure clusters

491 failed tests grouped into 14 buckets (sorted by count).

### `other_assertion` — 441 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_sqlite3.test_help_output`
  > AssertionError: assert b'Usage:' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', '--help'], returncode=0, stdout=b'sqlite 0.1.0\n\nusage: sqlite [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --versi
- `tests.test_sqlite3.test_help_short`
  > AssertionError: assert b'Usage:' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', '-help'], returncode=0, stdout=b'', stderr=b'').stderr
- `tests.test_sqlite3.test_version_flag`
  > AssertionError: assert b'3.54' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', '-version'], returncode=0, stdout=b'', stderr=b'').stdout
- *(... 438 more in this cluster)*

### `rc_mismatch_got0_want1` — 11 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_sqlite3.test_unknown_option_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-invalid_option_xyz'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_sqlite3.test_exit_code_sql_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', ':memory:'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_sqlite3.test_ifexists_nonexistent`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-ifexists', '/tmp/tmpkzwhmik8/nonexistent.db', 'SELECT 1;'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 8 more in this cluster)*

### `rc_mismatch_got2_want0` — 9 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_sqlite3.test_version_dot_command`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b'usage: sqlite [OPTIONS] [ARGS]\n').returncode
- `tests.test_sqlite3.test_no_args_default_memory`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b'usage: sqlite [OPTIONS] [ARGS]\n').returncode
- `tests.test_sqlite3.test_double_dash_stops_option_parsing`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--', ':memory:'], returncode=2, stdout=b'', stderr=b'sqlite: error: unrecognized argument: --\n').returncode
- *(... 6 more in this cluster)*

### `boolean_false` — 6 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_sqlite3.test_create_database_file`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmp5eto7njh/test.db').exists
  >  +      where PosixPath('/tmp/tmp5eto7njh/test.db') = Path('/tmp/tmp5eto7njh/test.db')
- `tests.test_sqlite3.test_backup_dot_command`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmp0jnqxrl2/backup.db').exists
  >  +      where PosixPath('/tmp/tmp0jnqxrl2/backup.db') = Path('/tmp/tmp0jnqxrl2/backup.db')
- `tests.test_sqlite3.test_save_dot_command`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmplr0nj_1_/saved.db').exists
  >  +      where PosixPath('/tmp/tmplr0nj_1_/saved.db') = Path('/tmp/tmplr0nj_1_/saved.db')
- *(... 3 more in this cluster)*

### `returned_none` — 4 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_sqlite3.test_sqlite_version_func`
  > AssertionError: assert None
  >  +  where None = <function match at 0x7fd64cce2170>(b'\\d+\\.\\d+\\.\\d+', b'')
  >  +    where <function match at 0x7fd64cce2170> = re.match
- `tests.test_sqlite3.test_dot_sha3sum`
  > AssertionError: assert None
  >  +  where None = <function match at 0x7fd64cce2170>(b'[0-9a-f]+', b'')
  >  +    where <function match at 0x7fd64cce2170> = re.match
- `tests.test_sqlite3.test_sha3sum_multiple_tables`
  > AssertionError: assert None
  >  +  where None = <function match at 0x7fd64cce2170>(b'[0-9a-f]+', b'')
  >  +    where <function match at 0x7fd64cce2170> = re.match
- *(... 1 more in this cluster)*

### `empty_list_or_string` — 4 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_sqlite3.test_order_by`
  > IndexError: list index out of range
- `tests.test_sqlite3.test_decimal_cmp`
  > IndexError: list index out of range
- `tests.test_sqlite3.test_decimal_collation`
  > IndexError: list index out of range
- *(... 1 more in this cluster)*

### `json_output_missing_or_bad` — 3 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `tests.test_sqlite3.test_mode_json`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_sqlite3.test_dot_mode_json`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_sqlite3.test_json_functions`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

### `string_output_mismatch` — 3 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_sqlite3.test_header_csv`
  > AssertionError: assert '' == 'col1,col2'
  >   
  >   - col1,col2
- `tests.test_sqlite3.test_noheader`
  > AssertionError: assert '' == '1,hello'
  >   
  >   - 1,hello
- `tests.test_sqlite3.test_dot_headers_on`
  > AssertionError: assert '' == 'x'
  >   
  >   - x

### `rc_mismatch_got0_want64` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_sqlite3.test_sha3_agg_function`
  > AssertionError: assert 0 == 64
  >  +  where 0 = len(b'')
  >  +    where b'' = <built-in method strip of bytes object at 0x7fd64cdc0030>()
  >  +      where <built-in method strip of bytes object at 0x7fd64cdc0030> = b''.strip
  >  +        where b'' = CompletedProcess(args=['/workspace/executable', ':memory:'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_sqlite3.test_sha3_query_function`
  > assert 0 == 64
  >  +  where 0 = len(b'')
  >  +    where b'' = <built-in method strip of bytes object at 0x7fd64cdc0030>()
  >  +      where <built-in method strip of bytes object at 0x7fd64cdc0030> = b''.strip
  >  +        where b'' = CompletedProcess(args=['/workspace/executable', ':memory:', "SELECT hex(sha3_query('SELECT 1'));"], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_sqlite3.test_sha3_blob_input`
  > assert 0 == 64
  >  +  where 0 = len(b'')
  >  +    where b'' = <built-in method strip of bytes object at 0x7fd64cdc0030>()
  >  +      where <built-in method strip of bytes object at 0x7fd64cdc0030> = b''.strip
  >  +        where b'' = CompletedProcess(args=['/workspace/executable', ':memory:', "SELECT hex(sha3(x'deadbeef'));"], returncode=0, stdout=b'', stderr=b'').stdout

### `bytes_output_mismatch` — 3 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_sqlite3.test_generate_series_step`
  > AssertionError: assert [] == [b'10', b'8',...', b'4', b'2']
  >   
  >   Right contains 5 more items, first extra item: b'10'
  >   
  >   Full diff:
  >   + []
  >   - [
  >   -     b'10',...
- `tests.test_sqlite3.test_generate_series_with_step`
  > AssertionError: assert [] == [b'0', b'2', ..., b'8', b'10']
  >   
  >   Right contains 6 more items, first extra item: b'0'
  >   
  >   Full diff:
  >   + []
  >   - [
  >   -     b'0',...
- `tests.test_sqlite3.test_generate_series_descending`
  > AssertionError: assert [] == [b'5', b'4', b'3', b'2', b'1']
  >   
  >   Right contains 5 more items, first extra item: b'5'
  >   
  >   Full diff:
  >   + []
  >   - [
  >   -     b'5',...

### `test_timeout` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_sqlite3.test_typeof_function`
  > subprocess.TimeoutExpired: Command '['/workspace/executable', ':memory:', "SELECT typeof(1), typeof(1.5), typeof('hello'), typeof(NULL), typeof(x'deadbeef');"]' timed out after 5.0 seconds

### `missing_file` — 1 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_sqlite3.test_dot_output`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpey_1mdsh/out.txt'

### `rc_mismatch_got2_want5` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_sqlite3.test_dot_exit_nonzero`
  > AssertionError: assert 2 == 5
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b'usage: sqlite [OPTIONS] [ARGS]\n').returncode

### `rc_mismatch_got0_want128` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_sqlite3.test_sha3sum_with_size`
  > AssertionError: assert 0 == 128
  >  +  where 0 = len(b'')
  >  +    where b'' = <built-in method strip of bytes object at 0x7fd64cdc0030>()
  >  +      where <built-in method strip of bytes object at 0x7fd64cdc0030> = b''.strip
  >  +        where b'' = CompletedProcess(args=['/workspace/executable', '/tmp/tmpf76e70yv/test.db'], returncode=0, stdout=b'', stderr=b'').stdout

