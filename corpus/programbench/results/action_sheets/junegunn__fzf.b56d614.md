# Action Sheet — junegunn__fzf.b56d614

**Current:** 26.66%  (702/2633)
**Pass / Fail / Skip:** 702 / 510 / 0
**Gap to 100%:** 73.34 percentage points (1931 tests)

## Failure clusters

510 failed tests grouped into 19 buckets (sorted by count).

### `other_assertion` — 161 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_algorithms.test_scoring_camelcase`
  > AssertionError: assert 1 >= 2
  >  +  where 1 = len(['testcheck'])
- `tests.test_basic.test_version_output`
  > AssertionError: Version should contain version number
  > assert None
  >  +  where None = <function match at 0x7fe789df1120>(b'\\d+\\.\\d+', b'fzf 0.1.0\n')
  >  +    where <function match at 0x7fe789df1120> = re.match
  >  +    and   b'fzf 0.1.0\n' = CompletedProcess(args=['./executable', '--version'], returncode=0, stdout=b'fzf 0.1.0\n', stderr=b'').stdout
- `tests.test_basic.test_help_output`
  > AssertionError: assert b'fzf is an interactive filter program' in b'fzf 0.1.0 - bootstrap scaffold\n\nUsage: fzf [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print versi
  >  +  where b'fzf 0.1.0 - bootstrap scaffold\n\nUsage: fzf [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n\n' = CompletedProcess(args=['./executable', '--help
- *(... 158 more in this cluster)*

### `rc_mismatch_got2_want0` — 117 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_advanced.test_bash_integration_script`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--bash'], returncode=2, stdout=b'', stderr=b"fzf: unknown option: --bash\nusage: fzf [OPTIONS] [ARGS]\nTry 'fzf --help' for more information.\n").
- `tests.test_advanced.test_zsh_integration_script`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--zsh'], returncode=2, stdout=b'', stderr=b"fzf: unknown option: --zsh\nusage: fzf [OPTIONS] [ARGS]\nTry 'fzf --help' for more information.\n").re
- `tests.test_advanced.test_fish_integration_script`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--fish'], returncode=2, stdout=b'', stderr=b"fzf: unknown option: --fish\nusage: fzf [OPTIONS] [ARGS]\nTry 'fzf --help' for more information.\n").
- *(... 114 more in this cluster)*

### `string_output_mismatch` — 87 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_comprehensive.test_print_query_only`
  > AssertionError: assert '' == 'xyz'
  >   
  >   - xyz
- `tests.test_coverage_boost.test_print_query_no_match`
  > AssertionError: assert '' == 'nomatch'
  >   
  >   - nomatch
- `tests.test_coverage_boost.test_tac_with_no_sort`
  > AssertionError: assert 'test1' == 'test3'
  >   
  >   - test3
  >   ?     ^
  >   + test1
  >   ?     ^
- *(... 84 more in this cluster)*

### `rc_mismatch_got1_want0` — 70 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_algorithms.test_prefix_match_variations`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '-f', '^t'], returncode=1, stdout=b'', stderr=b'').returncode
- `tests.test_algorithms.test_suffix_match_variations`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '-f', 'st$'], returncode=1, stdout=b'', stderr=b'').returncode
- `tests.test_algorithms.test_inverse_match_multiple`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '-f', '!test !foo'], returncode=1, stdout=b'', stderr=b'').returncode
- *(... 67 more in this cluster)*

### `rc_mismatch_got0_want2` — 15 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_advanced_options.test_tail_zero`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['./executable', '-f', 'test', '--tail=0'], returncode=0, stdout=b'test\n', stderr=b'').returncode
- `tests.test_edge_cases_advanced.test_invalid_scheme`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['./executable', '-f', 'test', '--scheme=invalid_scheme_xyz'], returncode=0, stdout=b'test', stderr=b'').returncode
- `tests.test_edge_cases_advanced.test_invalid_tiebreak_criterion`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['./executable', '-f', 'test', '--tiebreak=invalid_xyz'], returncode=0, stdout=b'test', stderr=b'').returncode
- *(... 12 more in this cluster)*

### `bytes_output_mismatch` — 13 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `eval.tests.test_fzf_filter_io.test_read0_and_print0_roundtrip_delimiters`
  > AssertionError: assert b'foo\x00bar\x00baz\x00' == b'bar\x00baz\x00'
  >   
  >   At index 0 diff: b'f' != b'b'
  >   
  >   Full diff:
  >   - (b'bar\x00baz\x00')
  >   + (b'foo\x00bar\x00baz\x00')
  >   ?    +++++++
- `eval.tests.test_fzf_cli.test_version_exact`
  > AssertionError: assert b'fzf 0.1.0\n' == b'0.68.0 (5676da4a)\n'
  >   
  >   At index 0 diff: b'f' != b'0'
  >   
  >   Full diff:
  >   - (b'0.68.0 (5676da4a)\n')
  >   + (b'fzf 0.1.0\n')
- `eval.tests.test_fzf_cli.test_unknown_option_exit_2_and_message_on_stderr`
  > assert b"fzf: unknow...nformation.\n" == b'unknown option: --unknown\n'
  >   
  >   At index 0 diff: b'f' != b'u'
  >   
  >   Full diff:
  >   - (b'unknown option: --unknown\n')
  >   + (b"fzf: unknown option: --unknown\nusage: fzf [OPTIONS] [ARGS]\nTry 'fzf --he"
  >   +  b"lp' for more information.\n")
- *(... 10 more in this cluster)*

### `rc_mismatch_got2_want1` — 10 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_fzf_filter_io.test_filter_no_matches_exit_code_1_and_no_output`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--filter=zz'], returncode=2, stdout=b'', stderr=b"fzf: unknown option: --filter=zz\nusage: fzf [OPTIONS] [ARGS]\nTry 'fzf --help' for mor
- `eval.tests.test_fzf_filter_io.test_print0_outputs_nul_delimited_and_preserves_exit_code_on_no_match`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--filter=zz', '--print0'], returncode=2, stdout=b'', stderr=b"fzf: unknown option: --filter=zz\nusage: fzf [OPTIONS] [ARGS]\nTry 'fzf --h
- `eval.tests.test_fzf_externalized.test_ext_algo_exact_match_enabled_requires_contiguous_substring`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-i', '--exact', '--filter', 'oBZ'], returncode=2, stdout=b'', stderr=b"fzf: unknown option: -i\nusage: fzf [OPTIONS] [ARGS]\nTry 'fzf --h
- *(... 7 more in this cluster)*

### `missing_file` — 10 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_history.test_history_empty_query_not_recorded`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_history_empty_query_not_r2/history_empty.txt'
- `tests.test_history.test_history_allows_duplicate_queries`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_history_allows_duplicate_2/history_dedup.txt'
- `tests.test_history.test_history_file_format_one_line_per_entry`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_history_file_format_one_l2/history_format.txt'
- *(... 7 more in this cluster)*

### `rc_unexpected_zero` — 7 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `eval.tests.test_help_error_precedence.test_unknown_option_errors_and_no_help_when_help_first`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--help', '--definitely-not-a-real-option'], returncode=0, stdout='fzf 0.1.0 - bootstrap scaffold\n\nUsage: fzf [OPTIONS] [ARGS]\n\nOption
- `tests.test_subcommand_dispatch.TestUnknownOptions.test_unknown_subcommand_style_arg`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'add'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_subcommand_dispatch.TestUnknownOptions.test_another_unknown_subcommand`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'remove'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 4 more in this cluster)*

### `boolean_false` — 4 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_history.test_history_file_created_when_nonexistent`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/pytest-of-root/pytest-0/test_history_file_created_when2/new_history.txt').exists
- `tests.test_history.test_history_file_empty_on_first_filter_use`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/pytest-of-root/pytest-0/test_history_file_empty_on_fir2/filter_history.txt').exists
- `tests.test_history.test_history_writes_search_query_on_selection`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/pytest-of-root/pytest-0/test_history_writes_search_que2/history.txt').exists
- *(... 1 more in this cluster)*

### `rc_mismatch_got1_want4` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_algorithms.test_fuzzy_match_spacing`
  > AssertionError: assert 1 == 4
  >  +  where 1 = len(['ab'])
- `tests.test_algorithms.test_case_variations_smart`
  > AssertionError: assert 1 == 4
  >  +  where 1 = len(['test'])
- `tests.test_fzf.TestFilterModeBasicSearch.test_exact_match_flag`
  > AssertionError: assert 1 == 4
  >  +  where 1 = len([''])

### `rc_mismatch_got0_want1` — 3 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_fzf.TestFilterModeBasicSearch.test_case_sensitive`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '+i', '-f', 'apple'], returncode=0, stdout='', stderr='').returncode
- `eval.tests.test_fzf_cli.test_nth_limits_search_scope_so_leading_spaces_are_excluded`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-f', 'apple', '-n', '2..'], returncode=0, stdout=b'  apple\n', stderr=b'').returncode
- `eval.tests.test_fzf_externalized.test_ext_algo_fuzzy_match_case_sensitive_non_match_exits_1`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '+i', '--filter', 'oBZ'], returncode=0, stdout=b'', stderr=b'').returncode

### `returned_none` — 2 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_basic_invocation.test_version_output`
  > AssertionError: assert None
  >  +  where None = <function match at 0x7fc37954d120>(b'\\d+\\.\\d+', b'fzf 0.1.0\n')
  >  +    where <function match at 0x7fc37954d120> = re.match
  >  +    and   b'fzf 0.1.0\n' = CompletedProcess(args=['./executable', '--version'], returncode=0, stdout=b'fzf 0.1.0\n', stderr=b'').stdout
- `tests.test_error_handling.test_version_with_other_flags`
  > AssertionError: assert None
  >  +  where None = <function match at 0x7fc37954d120>(b'\\d+\\.\\d+', b'fzf 0.1.0\n')
  >  +    where <function match at 0x7fc37954d120> = re.match
  >  +    and   b'fzf 0.1.0\n' = CompletedProcess(args=['./executable', '--version', '--filter=test'], returncode=0, stdout=b'fzf 0.1.0\n', stderr=b'').stdout

### `rc_mismatch_got1_want2` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_error_handling.test_missing_delimiter_value`
  > AssertionError: assert 1 == 2
  >  +  where 1 = CompletedProcess(args=['./executable', '-f', 'test', '-d'], returncode=1, stdout=b'', stderr=b'').returncode
- `tests.test_error_handling.test_missing_filter_query`
  > AssertionError: assert 1 == 2
  >  +  where 1 = CompletedProcess(args=['./executable', '-f'], returncode=1, stdout=b'', stderr=b'').returncode

### `rc_mismatch_got3_want2` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_core.test_ansi_with_nth_preserves_colors`
  > AssertionError: assert 3 == 2
  >  +  where 3 = len(['\x1b[31m1\x1b[0m apple red', '\x1b[32m2\x1b[0m banana yellow', '\x1b[33m3\x1b[0m cherry red'])
- `tests.test_io.test_ansi_color_with_multiple_codes`
  > AssertionError: assert 3 == 2
  >  +  where 3 = len(['\x1b[1;31mbold red apple\x1b[0m', '\x1b[38;5;196m256-color red\x1b[0m', 'banana'])

### `rc_mismatch_got1_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic.test_case_insensitive`
  > AssertionError: assert 1 == 3
  >  +  where 1 = len(['FOO'])

### `rc_mismatch_got100_want10` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic.test_tail_limit`
  > AssertionError: assert 100 == 10
  >  +  where 100 = len(['line0', 'line1', 'line2', 'line3', 'line4', 'line5', ...])

### `rc_mismatch_got2_want4` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_harvest.TestFilter.test_exact`
  > AssertionError: assert 2 == 4
  >  +  where 2 = len(['13', '113'])
  >  +    where ['13', '113'] = <built-in method split of str object at 0x7fd4a6d22ff0>('\n')
  >  +      where <built-in method split of str object at 0x7fd4a6d22ff0> = '13\n113'.split
  >  +        where '13\n113' = <built-in method strip of str object at 0x7fd4a6d223b0>()
  >  +          where <built-in method strip of str object at 0x7fd4a6d223b0> = '13\n113\n'.strip
  >  +            where '13\n113\n' = <built-in method decode of bytes object at 0x7fd4a6cb1140>()
  >  +              where <built-in method decode of bytes object at 0x7fd4a6cb1140> = b'13\n113\n'.decode

### `rc_mismatch_got1_want6` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_harvest.TestFilter.test_escaped_meta_characters`
  > assert 1 == 6
  >  +  where 1 = len(['foo bar'])
  >  +    where ['foo bar'] = <built-in method split of str object at 0x7fd4a699ac30>('\n')
  >  +      where <built-in method split of str object at 0x7fd4a699ac30> = 'foo bar'.split
  >  +        where 'foo bar' = <built-in method strip of str object at 0x7fd4a69984f0>()
  >  +          where <built-in method strip of str object at 0x7fd4a69984f0> = 'foo bar\n'.strip
  >  +            where 'foo bar\n' = <built-in method decode of bytes object at 0x7fd4a69535d0>()
  >  +              where <built-in method decode of bytes object at 0x7fd4a69535d0> = b'foo bar\n'.decode

