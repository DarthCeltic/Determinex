# Action Sheet — jhspetersson__fselect.c3559ca

**Current:** 1.72%  (60/3480)
**Pass / Fail / Skip:** 60 / 600 / 40
**Gap to 100%:** 98.28 percentage points (3420 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_acl_cap_coverage.TestACLFunctionality.test_acl_with_group_entry`
  - reason: setfacl not available
- `tests.test_acl_cap_coverage.TestACLFunctionality.test_acl_with_user_and_group_entries`
  - reason: setfacl not available
- `tests.test_acl_cap_coverage.TestACLFunctionality.test_has_acl_true`
  - reason: setfacl not available
- `tests.test_acl_cap_coverage.TestACLFunctionality.test_acl_entry_function_user`
  - reason: setfacl not available
- `tests.test_acl_cap_coverage.TestACLFunctionality.test_acl_entry_function_group`
  - reason: setfacl not available
- *(... 35 more skipped)*

## Failure clusters

600 failed tests grouped into 17 buckets (sorted by count).

### `other_assertion` — 260 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_acl_cap_coverage.TestACLFunctionality.test_has_acl_false`
  > AssertionError: assert 'no_acl.txt' in ''
- `tests.test_acl_cap_coverage.TestCapabilitiesFields.test_has_capabilities_on_regular_file`
  > AssertionError: assert 'no_caps.txt' in ''
- `tests.test_acl_coverage.TestACLFieldsWithRealACL.test_has_acl_false_no_acl`
  > AssertionError: assert 'no_acl.txt' in ''
- *(... 257 more in this cluster)*

### `string_output_mismatch` — 240 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_additional_queries.TestSelectKeyword.test_select_keyword`
  > AssertionError: assert '' == 'test.txt'
  >   
  >   - test.txt
- `tests.test_additional_queries.TestConcatWsInQuery.test_concat_ws_separator`
  > AssertionError: assert 'test.txt|txt' == 'test.txt'
  >   
  >   - test.txt
  >   + test.txt|txt
  >   ?         ++++
- `tests.test_additional_queries.TestFilenameFields.test_filename_without_extension`
  > AssertionError: assert '' == 'test'
  >   
  >   - test
- *(... 237 more in this cluster)*

### `rc_mismatch_got2_want0` — 35 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_basic.TestNoArgs.test_no_args_shows_usage`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b'fselect 0.8.0\nUsage: fselect [OPTIONS] [ARGS]\n\nFor more information try --help\n').returncode
- `tests.test_basic.TestNoArgs.test_no_args_includes_hint`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b'fselect 0.8.0\nUsage: fselect [OPTIONS] [ARGS]\n\nFor more information try --help\n').returncode
- `tests.test_basic.TestVersion.test_version_short`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-v'], returncode=2, stdout=b'', stderr=b'fselect: unknown option: -v\nfselect 0.8.0\nUsage: fselect [OPTIONS] [ARGS]\n\nFor more informat
- *(... 32 more in this cluster)*

### `rc_mismatch_got0_want1` — 17 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_columns.TestSizeColumns.test_size_column`
  > assert 0 == 1
  >  +  where 0 = len([])
- `tests.test_columns.TestPermissionColumns.test_uid_gid_columns`
  > assert 0 == 1
  >  +  where 0 = len([])
- `tests.test_columns.TestPermissionColumns.test_user_group_columns`
  > assert 0 == 1
  >  +  where 0 = len([])
- *(... 14 more in this cluster)*

### `rc_mismatch_got1_want2` — 8 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_additional_queries.TestTabsOutput.test_tabs_output`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len([''])
- `tests.test_advanced_columns.TestSha3Hash.test_sha3_hash`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len(['hello.txt'])
- `tests.test_columns.TestFileNameColumns.test_dir_column`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len(['nested.txt '])
- *(... 5 more in this cluster)*

### `uncategorized` — 8 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_advanced_columns.TestStddevVarianceFunctions.test_stddev_pop`
  > ValueError: could not convert string to float: ''
- `tests.test_advanced_columns.TestStddevVarianceFunctions.test_stddev_alias`
  > ValueError: could not convert string to float: ''
- `tests.test_advanced_columns.TestStddevVarianceFunctions.test_std_alias`
  > ValueError: could not convert string to float: ''
- *(... 5 more in this cluster)*

### `boolean_false` — 5 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_acl_functions.TestAclFormatting.test_acl_permissions_format`
  > assert False
  >  +  where False = any(<generator object TestAclFormatting.test_acl_permissions_format.<locals>.<genexpr> at 0x7f9a7d7d5bd0>)
- `tests.test_additional_queries.TestAbsPath.test_abspath_field`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7f9a7ff7c030>('/')
  >  +    where <built-in method startswith of str object at 0x7f9a7ff7c030> = ''.startswith
- `tests.test_additional_queries.TestAbsPath.test_absdir_field`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7f9a7ff7c030>('/')
  >  +    where <built-in method startswith of str object at 0x7f9a7ff7c030> = ''.startswith
- *(... 2 more in this cluster)*

### `rc_mismatch_got0_want2` — 5 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_additional_queries.TestLinesOutput.test_lines_output`
  > assert 0 == 2
  >  +  where 0 = len([])
- `tests.test_advanced_columns.TestLsStyleWildcard.test_star_wildcard_columns`
  > assert 0 == 2
  >  +  where 0 = len([])
- `tests.test_config_advanced.TestConfigErrorPaths.test_lexer_unterminated_string`
  > assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'name', 'from', '/tmp', 'depth', '1', 'where', "name = 'unterminated"], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 2 more in this cluster)*

### `returned_none` — 4 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_columns.TestTimestampColumns.test_modified_column`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f9a7fd7b760>('\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2}', '')
  >  +    where <function search at 0x7f9a7fd7b760> = <module 're' from '/usr/lib/python3.10/re.py'>.search
- `tests.test_columns.TestTimestampColumns.test_created_column`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f9a7fd7b760>('\\d{4}-\\d{2}-\\d{2}', '')
  >  +    where <function search at 0x7f9a7fd7b760> = <module 're' from '/usr/lib/python3.10/re.py'>.search
- `tests.test_columns.TestTimestampColumns.test_accessed_column`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f9a7fd7b760>('\\d{4}-\\d{2}-\\d{2}', '')
  >  +    where <function search at 0x7f9a7fd7b760> = <module 're' from '/usr/lib/python3.10/re.py'>.search
- *(... 1 more in this cluster)*

### `empty_list_or_string` — 4 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_aggregation_ordering.test_order_by_size_asc`
  > IndexError: list index out of range
- `tests.test_aggregation_ordering.test_order_by_size_desc`
  > IndexError: list index out of range
- `tests.test_aggregation_ordering.test_order_by_expression_arithmetic`
  > IndexError: list index out of range
- *(... 1 more in this cluster)*

### `json_output_missing_or_bad` — 3 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `tests.test_additional_queries.TestJsonOutput.test_json_output_valid`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_additional_queries.TestJsonOutput.test_json_output_multiple_files`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_additional_queries.TestJsonOutput.test_json_output_structure`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

### `rc_unexpected_zero` — 3 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_coverage_boost.TestParserErrorPaths.test_unparseable_query_gives_error`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '!!!invalid!!!'], returncode=0, stdout=b'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\
- `tests.test_coverage_boost.TestParserErrorPaths.test_unknown_output_format_error`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'name', 'from', '/tmp/pytest-of-root/pytest-0/test_unknown_output_format_err2', 'into', 'unknownformat'], returncode=0, stdout=b'', stderr
- `tests.test_coverage_boost.TestParserErrorPaths.test_order_by_index_out_of_range`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'name', 'from', '/tmp/pytest-of-root/pytest-0/test_order_by_index_out_of_ran2', 'order', 'by', '99'], returncode=0, stdout=b'', stderr=b''

### `bytes_output_mismatch` — 2 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_config_advanced.TestCommandLineFlags.test_no_error_flag_suppresses_errors`
  > AssertionError: assert b'fselect: un... try --help\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'fselect: unknown option: --no-error\nfselect 0.8.0\nUsage: fselect [OPTION'
  >   +  b'S] [ARGS]\n\nFor more information try --help\n')
- `tests.test_config_advanced.TestCommandLineFlags.test_no_error_with_inaccessible_dir`
  > AssertionError: assert b'fselect: un... try --help\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'fselect: unknown option: --no-error\nfselect 0.8.0\nUsage: fselect [OPTION'
  >   +  b'S] [ARGS]\n\nFor more information try --help\n')

### `rc_mismatch_got2_want1` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_datetime.test_date_comparison_greater_than`
  > AssertionError: assert 2 == 1
  >  +  where 2 = len(['new_file.txt', 'old_file.txt'])
- `tests.test_datetime.test_date_comparison_less_than`
  > AssertionError: assert 2 == 1
  >  +  where 2 = len(['new_file.txt', 'old_file.txt'])

### `rc_mismatch_got0_want3` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_errors.test_order_by_ascending`
  > assert 0 == 3
  >  +  where 0 = len([])
- `tests.test_errors.test_order_by_descending`
  > assert 0 == 3
  >  +  where 0 = len([])

### `rc_mismatch_got0_want7` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_aggregation_ordering.test_group_by_single_column_count`
  > AssertionError: assert 0 == 7
  >  +  where 0 = <built-in method get of dict object at 0x7f7417547500>('txt', 0)
  >  +    where <built-in method get of dict object at 0x7f7417547500> = {}.get

### `rc_mismatch_got1_want4` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_expr_deeper_gaps.test_multiple_datetime_fields_in_select`
  > AssertionError: assert 1 == 4
  >  +  where 1 = len([''])

