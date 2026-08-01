# Action Sheet — dundee__gdu.ede21d2

**Current:** 7.98%  (131/1641)
**Pass / Fail / Skip:** 131 / 787 / 20
**Gap to 100%:** 92.02 percentage points (1510 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_comprehensive.test_directory_contents_displayed`
  - reason: test_directory_contents_displayed depends on test_tui_launches_successfully
- `tests.test_comprehensive.test_vim_style_navigation_j_k`
  - reason: test_vim_style_navigation_j_k depends on test_tui_launches_successfully
- `tests.test_comprehensive.test_arrow_key_navigation`
  - reason: test_arrow_key_navigation depends on test_tui_launches_successfully
- `tests.test_comprehensive.test_enter_and_exit_directory`
  - reason: test_enter_and_exit_directory depends on test_directory_contents_displayed
- `tests.test_comprehensive.test_navigate_using_left_arrow`
  - reason: test_navigate_using_left_arrow depends on test_directory_contents_displayed
- *(... 15 more skipped)*

## Failure clusters

787 failed tests grouped into 13 buckets (sorted by count).

### `other_assertion` — 469 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_additional_coverage.test_multiple_cores_variations`
  > AssertionError: assert b'file1.txt' in b''
  >  +  where b'' = CompletedProcess(args=['./executable', '-n', '-p', '-m', '1', '/tmp/tmp42i1jloj'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_additional_coverage.test_sorting_by_name`
  > AssertionError: assert b'zebra.txt' in b''
  >  +  where b'' = CompletedProcess(args=['./executable', '-n', '-p', '/tmp/tmp5ddp0wvx'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_additional_coverage.test_time_filter_combinations`
  > AssertionError: assert b'new.txt' in b''
  >  +  where b'' = CompletedProcess(args=['./executable', '-n', '-p', '--max-age', '7d', '/tmp/tmpserhwe59'], returncode=0, stdout=b'', stderr=b'').stdout
- *(... 466 more in this cluster)*

### `string_output_mismatch` — 103 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_cli_advanced.test_sequential_scanning_produces_same_results_as_parallel`
  > AssertionError: assert '' == '    8.0 KiB ...B file1.txt\n'
  >   
  >   -     8.0 KiB /subdir
  >   -     4.0 KiB file2.txt
  >   -     4.0 KiB file1.txt
- `tests.test_cli_advanced.test_max_cores_limits_parallelism`
  > AssertionError: assert '' == '    8.0 KiB ...B file1.txt\n'
  >   
  >   -     8.0 KiB /subdir
  >   -     4.0 KiB file2.txt
  >   -     4.0 KiB file1.txt
- `tests.test_cli_advanced.test_scan_current_directory_no_args`
  > AssertionError: assert '' == '    8.0 KiB ...B file1.txt\n'
  >   
  >   -     8.0 KiB /subdir
  >   -     4.0 KiB file2.txt
  >   -     4.0 KiB file1.txt
- *(... 100 more in this cluster)*

### `boolean_false` — 62 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_additional_coverage.test_json_export_with_various_options`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmp2yhmote4/out.json').exists
- `tests.test_additional_coverage.test_database_with_filtering`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpuj64zahk/test.sqlite').exists
- `tests.test_additional_coverage.test_write_config`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpzdwqfoun/test.yaml').exists
- *(... 59 more in this cluster)*

### `rc_unexpected_zero` — 50 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_config_and_sorting.test_invalid_directory_path`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '-n', '-p', '/this/path/does/not/exist/anywhere'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_coverage_boost.test_invalid_max_age_format`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '-n', '-p', '--max-age', 'invalid', '/tmp/tmptpub3dsb'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_coverage_boost.test_invalid_min_age_format`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '-n', '-p', '--min-age', 'badformat', '/tmp/tmp4ps5mh0a'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 47 more in this cluster)*

### `json_output_missing_or_bad` — 37 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `tests.test_cli_archives.test_archive_browsing_disabled_by_default`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_cli_archives.test_archive_browsing_simple_zip_structure`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_cli_archives.test_archive_browsing_jar_file_recognition`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- *(... 34 more in this cluster)*

### `missing_file` — 33 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_cli_advanced.test_config_file_with_invalid_yaml_reports_error`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmp0zakweb0/yaml_error.log'
- `tests.test_cli_advanced.test_max_cores_with_log_file_confirms_setting`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpd7pu0065/cores.log'
- `tests.test_cli_analyze_gaps.test_json_output_contains_structured_metadata`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpsjf0nmwe/test.json'
- *(... 30 more in this cluster)*

### `rc_mismatch_got0_want1` — 20 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_cli_advanced.test_combined_flags_sequential_maxcores_summarize`
  > assert 0 == 1
  >  +  where 0 = len([])
- `tests.test_cli_basic.test_combined_summarize_and_si`
  > assert 0 == 1
  >  +  where 0 = len([])
- `tests.test_cli_errors.test_nonexistent_directory`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', '/nonexistent/path/to/directory'], returncode=0, stdout='', stderr='').returncode
- *(... 17 more in this cluster)*

### `uncategorized` — 6 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_config_comprehensive.test_config_reverse_sort`
  > ValueError: substring not found
- `tests.test_cli_final_gaps.test_stdout_reverse_sort_mode`
  > StopIteration
- `tests.test_cli_fs_gaps.test_apparent_size_sort_descending`
  > StopIteration
- *(... 3 more in this cluster)*

### `returned_none` — 3 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_output.test_help_has_usage_section`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f33c68b6680>('^Usage:\\s*$', '', flags=re.MULTILINE)
  >  +    where <function search at 0x7f33c68b6680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- `eval.tests.test_help_output.test_help_has_flags_section_header`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f33c68b6680>('^Flags:\\s*$', '', flags=re.MULTILINE)
  >  +    where <function search at 0x7f33c68b6680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- `eval.tests.test_externalized_stdout_and_filters.test_ext_format_size_raw_no_prefix_prints_integer_bytes`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f55e406e680>('\\b\\d+\\b', '')
  >  +    where <function search at 0x7f55e406e680> = re.search
  >  +    and   '' = CompletedProcess(args=['/workspace/executable', '--non-interactive', '--no-prefix', '/tmp/gdu-e2e-ngz801g7/d'], returncode=0, stdout='', stderr='').stdout

### `rc_mismatch_got1_want5` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_database.test_sqlite_with_depth_limit`
  > AssertionError: assert 1 == 5
  >  +  where 1 = len([''])

### `rc_mismatch_got1_want100` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_database.test_sqlite_many_files_performance`
  > AssertionError: assert 1 == 100
  >  +  where 1 = len([''])

### `empty_list_or_string` — 1 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_cli_gaps.test_gitannex_mixed_regular_and_annexed_files`
  > IndexError: list index out of range

### `rc_mismatch_got0_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_cli_help_version_errors.test_version_output_structure`
  > assert 0 == 3
  >  +  where 0 = len([])

