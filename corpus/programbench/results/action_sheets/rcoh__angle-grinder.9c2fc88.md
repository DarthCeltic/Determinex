# Action Sheet — rcoh__angle-grinder.9c2fc88

**Current:** 0.74%  (11/1480)
**Pass / Fail / Skip:** 11 / 689 / 0
**Gap to 100%:** 99.26 percentage points (1469 tests)

## Failure clusters

689 failed tests grouped into 10 buckets (sorted by count).

### `other_assertion` — 299 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_aliases.test_custom_alias_with_alias_dir_flag`
  > AssertionError: angle-grinder: unknown option: --alias-dir
  >   usage: angle-grinder [OPTIONS] [ARGS]
  >   Try 'angle-grinder --help' for more information.
  >   
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--alias-dir', '/workspace/eval/test_resources/test_aliases/custom_alias_dir', '* | keyvalue', '-f', '/workspace/eval/test_resources/test_
- `tests.test_aliases.test_malformed_alias_toml_syntax_error`
  > AssertionError: Should succeed despite invalid alias. stderr: angle-grinder: unknown option: --alias-dir
  >   usage: angle-grinder [OPTIONS] [ARGS]
  >   Try 'angle-grinder --help' for more information.
  >   
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--alias-dir', '/tmp/tmpqmf01v2i', '* | count', '-f', '/workspace/tmp_test_malformed.json'], returncode=2, stdout='', stderr="angle-grinde
- `tests.test_aliases.test_custom_alias_overrides_builtin_alias`
  > AssertionError: angle-grinder: unknown option: --alias-dir
  >   usage: angle-grinder [OPTIONS] [ARGS]
  >   Try 'angle-grinder --help' for more information.
  >   
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--alias-dir', '/tmp/tmp5688rrjn', '* | apache', '-f', '/workspace/tmp_custom_apache.txt'], returncode=2, stdout='', stderr="angle-grinder
- *(... 296 more in this cluster)*

### `string_output_mismatch` — 245 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_aggregation.test_count_basic`
  > AssertionError: assert '' == '_count\n--------------\n4\n'
  >   
  >   - _count
  >   - --------------
  >   - 4
- `tests.test_aggregation.test_count_by_field`
  > AssertionError: assert '' == 'level       ...ning      1\n'
  >   
  >   - level        _count
  >   - ---------------------------
  >   - info         2
  >   - error        1
  >   - warning      1
- `tests.test_aggregation.test_count_single_record`
  > AssertionError: assert '' == '_count\n--------------\n1\n'
  >   
  >   - _count
  >   - --------------
  >   - 1
- *(... 242 more in this cluster)*

### `rc_mismatch_got2_want0` — 54 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_aliases.test_malformed_alias_template_parse_error`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--alias-dir', '/tmp/tmp5j6lvnis', '* | count', '-f', '/workspace/tmp_test_badtemplate.json'], returncode=2, stdout='', stderr="angle-grin
- `tests.test_cli.test_invalid_alias_file_shows_warning`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--alias-dir', '/tmp/tmpipqomrxv', '*'], returncode=2, stdout='', stderr="angle-grinder: unknown option: --alias-dir\nusage: angle-grinder
- `tests.test_data_structures.test_datetime_subtraction_produces_duration`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-o', 'json', '* | json | fields start, end'], returncode=2, stdout='', stderr="angle-grinder: unknown option: -o\nusage: angle-grinder [O
- *(... 51 more in this cluster)*

### `rc_unexpected_zero` — 39 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_aliases.test_nonexistent_alias_error`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '* | nonexistentalias', '-f', '/workspace/eval/test_resources/test_aliases/apache_sample.log'], returncode=0, stdout='', stderr='').return
- `tests.test_cli.test_nonexistent_file_error`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '*', '-f', '/nonexistent/file.txt'], returncode=0, stdout='', stderr='').returncode
- `tests.test_cli.test_invalid_query_syntax_error`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'invalid | | syntax'], returncode=0, stdout='', stderr='').returncode
- *(... 36 more in this cluster)*

### `rc_mismatch_got0_want1` — 28 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_errors.test_where_missing_condition`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '* | where'], returncode=0, stdout='', stderr='').returncode
- `tests.test_errors.test_limit_zero`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '* | limit 0'], returncode=0, stdout='', stderr='').returncode
- `tests.test_errors.test_limit_fractional`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '* | limit 5.5'], returncode=0, stdout='', stderr='').returncode
- *(... 25 more in this cluster)*

### `json_output_missing_or_bad` — 20 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `tests.test_agrind.test_output_json_format`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_agrind.test_output_json_sorted_agg`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_agrind.test_json_output_float_values`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- *(... 17 more in this cluster)*

### `rc_mismatch_got1_want10000` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli.test_large_file_processing`
  > AssertionError: assert 1 == 10000
  >  +  where 1 = len([''])

### `rc_mismatch_got0_want2` — 1 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_agrind.test_limit_basic`
  > AssertionError: assert 0 == 2
  >  +  where 0 = <built-in method count of str object at 0x7f8071804030>('level')
  >  +    where <built-in method count of str object at 0x7f8071804030> = ''.count

### `rc_mismatch_got1_want10` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_agrind.test_default_limit_no_number`
  > AssertionError: assert 1 == 10
  >  +  where 1 = len([''])

### `bytes_output_mismatch` — 1 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_agrind.test_where_clause_comparison_all_ops`
  > AssertionError: Expected b'x=5' in output for * | json | where x == 5, got b''
  > assert b'x=5' in b''
  >  +  where b'' = CompletedProcess(args=['./executable', '* | json | where x == 5'], returncode=0, stdout=b'', stderr=b'').stdout

