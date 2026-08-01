# Action Sheet — zevv__duc.a58fa4e

**Current:** 21.39%  (219/1024)
**Pass / Fail / Skip:** 219 / 446 / 9
**Gap to 100%:** 78.61 percentage points (805 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_index_and_queries.test_info_reads_db`
  - reason: test_info_reads_db depends on test_index_creates_db
- `eval.tests.test_index_and_queries.test_ls_bytes_lists_expected_entries`
  - reason: test_ls_bytes_lists_expected_entries depends on test_index_creates_db
- `eval.tests.test_index_and_queries.test_ls_name_sort_changes_order`
  - reason: test_ls_name_sort_changes_order depends on test_index_creates_db
- `eval.tests.test_index_and_queries.test_ls_dirs_only_excludes_files`
  - reason: test_ls_dirs_only_excludes_files depends on test_index_creates_db
- `eval.tests.test_index_and_queries.test_ls_directory_lists_self_not_contents`
  - reason: test_ls_directory_lists_self_not_contents depends on test_index_creates_db
- *(... 4 more skipped)*

## Failure clusters

446 failed tests grouped into 12 buckets (sorted by count).

### `other_assertion` — 234 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_absolutely_50.TestFinal.test_histogram_all_databases`
  > AssertionError: assert b'/tmp/testdir' in b'Cannot store more than\nCannot use more than\n'
  >  +  where b'Cannot store more than\nCannot use more than\n' = CompletedProcess(args=['/workspace/executable', 'histogram', '--database=/tmp/test.db'], returncode=0, stdout=b'Cannot store more than\nCa
- `tests.test_absolutely_50.TestFinal.test_info_all_databases`
  > AssertionError: assert b'/tmp/testdir' in b'Path\nPath\nPath\n4096\nPath\nPath\n13\nPath\nusage: duc\nAvailable subcommands\n'
  >  +  where b'Path\nPath\nPath\n4096\nPath\nPath\n13\nPath\nusage: duc\nAvailable subcommands\n' = CompletedProcess(args=['/workspace/executable', 'info', '--database=/tmp/test.db'], returncode=0, stdou
- `tests.test_additional_coverage.test_help_all_detailed`
  > AssertionError: assert b'duc gui' in b'duc help\nduc index\nduc info\nduc ls\nduc histogram\nduc topn\nduc xml\nduc json\nduc graph\nduc cgi\n'
  >  +  where b'duc help\nduc index\nduc info\nduc ls\nduc histogram\nduc topn\nduc xml\nduc json\nduc graph\nduc cgi\n' = CompletedProcess(args=['/workspace/executable', 'help', '--all'], returncode=0, s
- *(... 231 more in this cluster)*

### `rc_unexpected_zero` — 52 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_additional_coverage.test_graph_output_path_variations`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'graph', '-o', '/tmp/pytest-of-root/pytest-0/test_graph_output_path_variati2/out.png', '-d', '/tmp/nonexist.db'], returncode=0, stdout=b'<
- `tests.test_additional_coverage.test_ls_multiple_options_combined`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'ls', '-b', '-a', '-F', '-c', '-g', '-R', '-n', '-l', '3', '-d', '/tmp/nonexist.db'], returncode=0, stdout=b'not found\nnot found\nnot fou
- `tests.test_additional_coverage.test_graph_all_options_combined`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'graph', '-a', '--count', '--gradient', '--palette', 'rainbow', '--fuzz', '0.5', '--dpi', '120', '--ring-gap', '2', '-l', '5', '-s', '800'
- *(... 49 more in this cluster)*

### `missing_file` — 47 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_coverage_improvement.TestCmdIndexCoverage.test_index_with_force_flag`
  > FileNotFoundError: [Errno 2] No such file or directory: './executable'
- `tests.test_coverage_improvement.TestCmdIndexCoverage.test_index_with_progress_flag`
  > FileNotFoundError: [Errno 2] No such file or directory: './executable'
- `tests.test_coverage_improvement.TestCmdIndexCoverage.test_index_with_bytes_flag`
  > FileNotFoundError: [Errno 2] No such file or directory: './executable'
- *(... 44 more in this cluster)*

### `string_output_mismatch` — 39 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_main.test_short_help_matches_long_help_exactly`
  > AssertionError: assert 'Available su...nusage: duc\n' == 'usage: duc <...ubcommands:\n'
  >   
  >   - usage: duc <cmd> [options] [args]
  >   - Available subcommands:
  >   ?                      -
  >   + Available subcommands
  >   - index
  >   - ls...
- `eval.tests.test_help_subcommands.test_help_subcommand_index_matches_index_dash_help_exactly`
  > AssertionError: assert 'duc index\nP...nusage: duc\n' == '--force\nfor...-fs-include\n'
  >   
  >   + duc index
  >   + PATH
  >   + usage: duc
  >   + Available subcommands:
  >   + usage: duc
  >   + usage: duc...
- `eval.tests.test_help_and_version.test_root_help_dashdash_help_equals_help`
  > AssertionError: assert 'usage: duc <...ubcommands:\n' == 'Available su...n--username\n'
  >   
  >   + usage: duc <cmd> [options] [args]
  >   - Available subcommands
  >   + Available subcommands:
  >   ?                      +
  >     index
  >   - info...
- *(... 36 more in this cluster)*

### `returned_none` — 20 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_main.test_main_help_lists_expected_subcommand[help]`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f352b6a6680>('^\\s*help\\s+:\\s+', 'usage: duc <cmd> [options] [args]\nAvailable subcommands:\nindex\nls\nusage: duc <cmd> [options] [args]\nAvailable subcomman
  >  +    where <function search at 0x7f352b6a6680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- `eval.tests.test_help_main.test_main_help_lists_expected_subcommand[histogram]`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f352b6a6680>('^\\s*histogram\\s+:\\s+', 'usage: duc <cmd> [options] [args]\nAvailable subcommands:\nindex\nls\nusage: duc <cmd> [options] [args]\nAvailable subc
  >  +    where <function search at 0x7f352b6a6680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- `eval.tests.test_help_main.test_main_help_lists_expected_subcommand[index]`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f352b6a6680>('^\\s*index\\s+:\\s+', 'usage: duc <cmd> [options] [args]\nAvailable subcommands:\nindex\nls\nusage: duc <cmd> [options] [args]\nAvailable subcomma
  >  +    where <function search at 0x7f352b6a6680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- *(... 17 more in this cluster)*

### `uncategorized` — 18 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_ls.test_apparent_vs_actual_size_difference`
  > ValueError: invalid literal for int() with base 10: '/tmp/testdir'
- `tests.test_output.test_xml_basic_output`
  > xml.etree.ElementTree.ParseError: syntax error: line 1, column 0
- `tests.test_output.test_xml_exclude_files`
  > xml.etree.ElementTree.ParseError: not well-formed (invalid token): line 1, column 1
- *(... 15 more in this cluster)*

### `json_output_missing_or_bad` — 17 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `tests.test_output.test_json_basic_output`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_output.test_json_min_size_filtering`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_output.test_json_apparent_size`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- *(... 14 more in this cluster)*

### `boolean_false` — 9 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_config_env.test_env_duc_database_overrides_default_location`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/duc-home-cjrbprb9/my.db').exists
- `tests.test_config_env.test_cli_database_flag_overrides_env_duc_database`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/duc-home-3s6ri02e/cli.db').exists
- `eval.tests.test_help_main.test_flag_ordering_help_then_version_prefers_version`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x555f7b9a4f20>('duc version:')
  >  +    where <built-in method startswith of str object at 0x555f7b9a4f20> = 'duc 0.1.0\nInteractive TUI tool driven by tmux/libtmux/pexpect harness\n\nUsage: duc [OPTIONS] [ARGS]...\nUSAGE: duc [OPTION
- *(... 6 more in this cluster)*

### `rc_mismatch_got0_want1` — 5 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `eval.tests.test_errors_and_exit_codes.test_missing_database_file_is_error_on_stderr_exit_1`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'ls', '-d', '/tmp/pytest-of-root/pytest-0/test_missing_database_file_is_2/missing.db', '.'], returncode=0, stdout=b'error\n', stderr=b'').
- `eval.tests.test_duc_externalized_from_testsh.test_ext_testsh_backend_type_mismatch_db_rejected`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'info', '-d', 'testing/dbs/lmdb.db'], returncode=0, stdout=b'error\n', stderr=b'').returncode
- `tests.test_cgi.test_cgi_requires_gateway_interface`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'cgi'], returncode=0, stdout='<\n', stderr='').returncode
- *(... 2 more in this cluster)*

### `empty_list_or_string` — 3 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_info_histogram_topn.test_info_bytes_flag`
  > IndexError: list index out of range
- `tests.test_info_histogram_topn.test_info_apparent_vs_actual_size`
  > IndexError: list index out of range
- `tests.test_info_histogram_topn.test_info_with_combined_flags`
  > IndexError: list index out of range

### `bytes_output_mismatch` — 1 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `eval.tests.test_errors_and_exit_codes.test_unknown_top_level_option_shows_help_exit_0_and_no_stderr`
  > assert b"error: unex...nformation.\n" == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b"error: unexpected argument '--definitely-not-a-real-option' found\nError:"
  >   +  b" unexpected argument '--definitely-not-a-real-option' found\nunknown flag"
  >   +  b": unexpected argument '--definitely-not-a-real-option' found\nUnknown fla"
  >   +  b"g: unexpected argument '--definitely-not-a-real-option' found\n\nUsage: du"...

### `rc_mismatch_got10_want2` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_info_histogram_topn.test_info_apparent_vs_actual_with_sparse_file`
  > AssertionError: assert 10 == 2
  >  +  where 10 = len(['Path', 'Path', '4096', 'Path', 'Path', '13', ...])

