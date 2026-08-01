# Action Sheet — ggreer__the_silver_searcher.a61f178

**Current:** 46.56%  (555/1192)
**Pass / Fail / Skip:** 555 / 636 / 1
**Gap to 100%:** 53.44 percentage points (637 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_harvest.test_big_file_handling`
  - reason: Big file test requires multi-GB file creation, impractical in CI

## Failure clusters

636 failed tests grouped into 23 buckets (sorted by count).

### `other_assertion` — 272 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_basic_invocation.TestBasicInvocation.test_help_flag`
  > AssertionError: assert b'Usage: ag' in b'the-silver-searcher 0.1.0\nSearch files for a pattern\n\nUsage: the-silver-searcher [OPTIONS] [ARGS]...\n\nOptions:\n  --ackmate\n  --actionscript\n  --ada\n  
  >  +  where b'the-silver-searcher 0.1.0\nSearch files for a pattern\n\nUsage: the-silver-searcher [OPTIONS] [ARGS]...\n\nOptions:\n  --ackmate\n  --actionscript\n  --ada\n  --ada...\n  --affinity\n  --a
- `eval.tests.test_basic_invocation.TestBasicInvocation.test_help_short_flag`
  > AssertionError: assert b'Usage: ag' in b'the-silver-searcher 0.1.0\nSearch files for a pattern\n\nUsage: the-silver-searcher [OPTIONS] [ARGS]...\n\nOptions:\n  --ackmate\n  --actionscript\n  --ada\n  
  >  +  where b'the-silver-searcher 0.1.0\nSearch files for a pattern\n\nUsage: the-silver-searcher [OPTIONS] [ARGS]...\n\nOptions:\n  --ackmate\n  --actionscript\n  --ada\n  --ada...\n  --affinity\n  --a
- `eval.tests.test_basic_invocation.TestBasicInvocation.test_version_flag`
  > AssertionError: assert b'ag version' in b'the-silver-searcher 0.1.0\n'
  >  +  where b'the-silver-searcher 0.1.0\n' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'the-silver-searcher 0.1.0\n', stderr=b'').stdout
- *(... 269 more in this cluster)*

### `rc_mismatch_got1_want0` — 124 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `eval.tests.test_debug_and_special.TestDebugAndSpecial.test_print_all_files`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '--print-all-files', 'hello', '/tmp/tmp2ivny1wj'], returncode=1, stdout=b'', stderr=b'').returncode
- `eval.tests.test_debug_and_special.TestDebugAndSpecial.test_color_codes_custom`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '--color-match', '1;31', '--color', 'hello', '/tmp/tmp3xd7v9l0'], returncode=1, stdout=b'', stderr=b"the-silver-searcher: cannot access 'h
- `eval.tests.test_file_types.TestFileTypes.test_all_text_files`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-t', 'hello', '/tmp/tmpfd_sgm3d'], returncode=1, stdout=b'', stderr=b'').returncode
- *(... 121 more in this cluster)*

### `string_output_mismatch` — 101 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_combinations.test_group_flag_enables_heading_and_break`
  > AssertionError: assert ['/workspace/...tch in file2'] == ['', '/worksp...n file2', ...]
  >   
  >   At index 0 diff: '/workspace/eval/test_resources/test_combinations/dir1/file1.txt:1:match one in file1' != ''
  >   Right contains 3 more items, first extra item: '2:another match in file2'
  >   
  >   Full diff:
  >     [
  >   -     '',...
- `tests.test_errors.test_regex_unclosed_bracket`
  > AssertionError: assert 'Error: error...at position 0' == 'ERR: Bad reg...un ag with -Q'
  >   
  >   + Error: error parsing regex '[unclosed': unterminated character set at position 0
  >   - ERR: Bad regex! pcre_compile() failed at position 9: missing terminating ] for character class
  >   - If you meant to search for a literal string, run ag with -Q
- `tests.test_errors.test_regex_unclosed_parenthesis`
  > AssertionError: assert 'Error: error...at position 0' == 'ERR: Bad reg...un ag with -Q'
  >   
  >   + Error: error parsing regex '(abc': missing ), unterminated subpattern at position 0
  >   - ERR: Bad regex! pcre_compile() failed at position 4: missing )
  >   - If you meant to search for a literal string, run ag with -Q
- *(... 98 more in this cluster)*

### `rc_mismatch_got2_want0` — 43 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `eval.tests.test_file_types.TestFileTypes.test_list_file_types`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--list-file-types'], returncode=2, stdout=b'', stderr=b"error: a value is required for '--list-file-types <VALUE>' but none was supplied\
- `eval.tests.test_basic.test_list_file_types`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--list-file-types'], returncode=2, stdout=b'', stderr=b"error: a value is required for '--list-file-types <VALUE>' but none was supplied\
- `eval.tests.test_file_filtering.test_filename_pattern`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-g', 'test'], returncode=2, stdout=b'', stderr=b"error: the following required arguments were not provided: <PATTERN>\n\nUsage: the-silve
- *(... 40 more in this cluster)*

### `rc_mismatch_got0_want1` — 26 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `eval.tests.test_debug_and_special.TestDebugAndSpecial.test_empty_stdin`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'test'], returncode=0, stdout=b'CONTRIBUTING.md:5:### Running the test suite\nCONTRIBUTING.md:7:If you contribute, you might want to run t
- `eval.tests.test_input_handling.TestInputHandling.test_binary_file_default_skip`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '.', '/tmp/tmp1h07pi8u'], returncode=0, stdout=b'/tmp/tmp1h07pi8u/binary.bin:1:\x00\x01\x02\xef\xbf\xbd\xef\xbf\xbd\n', stderr=b'').return
- `eval.tests.test_error_handling.test_invert_match_no_matches`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-v', 'match', 'allmatch.txt'], returncode=0, stdout=b'allmatch.txt:1:match\nallmatch.txt:2:match\nallmatch.txt:3:match\n', stderr=b'').re
- *(... 23 more in this cluster)*

### `bytes_output_mismatch` — 25 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_combinations.test_context_before_and_after_with_multiple_matches`
  > AssertionError: assert b'/workspace/...xt:2:line 2\n' == b'1:match on ...ine 10\n11-\n'
  >   
  >   At index 0 diff: b'/' != b'1'
  >   
  >   Full diff:
  >   + (b'/workspace/eval/test_resources/test_combinations/large_file.txt:2:line 2\n')
  >   - (b'1:match on line 1\n2-line 2\n3-line 3\n4-line 4\n5-line 5\n6:match on lin'
  >   -  b'e 6\n7-line 7\n8-line 8\n9:match on line 9\n10-line 10\n11-\n')
- `tests.test_combinations.test_column_with_vimgrep_redundancy`
  > AssertionError: assert b'/workspace/...match again\n' == b'/workspace/...match again\n'
  >   
  >   At index 65 diff: b'm' != b'1'
  >   
  >   Full diff:
  >   - (b'/workspace/eval/test_resources/test_combinations/multiline.txt:1:1:match her'
  >   ?                                                                     --
  >   + (b'/workspace/eval/test_resources/test_combinations/multiline.txt:1:match here '...
- `tests.test_compression.test_xz_with_context_lines`
  > AssertionError: assert b'/workspace/...0\x00\x04YZ\n' == b'9:Another l...stack.\n10-\n'
  >   
  >   At index 0 diff: b'/' != b'9'
  >   
  >   Full diff:
  >   - (b'9:Another line with needle in a haystack.\n10-\n')
  >   + (b'/workspace/eval/test_resources/test_compression/plain_file.txt.xz:10'
  >   +  b':\xef\xbf\xbd\x1b\xef\xbf\xbdyQU\xef\xbf\xbd\tk\x1b\xd6\xb3\xef'...
- *(... 22 more in this cluster)*

### `rc_mismatch_got2_want1` — 19 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_basic_invocation.TestBasicInvocation.test_no_arguments_shows_usage`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b"error: the following required arguments were not provided: <PATTERN>\n\nUsage: the-silver-searcher [OP
- `eval.tests.test_basic_invocation.TestBasicInvocation.test_missing_pattern_shows_usage`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b"error: the following required arguments were not provided: <PATTERN>\n\nUsage: the-silver-searcher [OP
- `tests.test_errors.test_duplicate_file_search_regex_flags`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-g', '*.txt', '-G', '*.c', 'test'], returncode=2, stdout=b'', stderr=b"Error: error parsing regex '*.c': nothing to repeat at position 0\
- *(... 16 more in this cluster)*

### `rc_mismatch_got3_want2` — 4 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_combinations.test_word_regexp_with_only_matching`
  > AssertionError: assert 3 == 2
  >  +  where 3 = len(['/workspace/eval/test_resources/test_combinations/words.txt:1:word wordy wordsmith', '/workspace/eval/test_resources/test_combinations/words.txt:2:the word is here', '/workspace/eva
- `tests.test_edge_cases.test_print0_with_list_files`
  > AssertionError: assert 3 == 2
  >  +  where 3 = len([b'/workspace/eval/test_resources/test_edge_cases/file1.txt:1:apple banana cherry\n/workspace/eval/test_resources/test_edge_cases/file2.txt:1:banana orange\n/workspace/eval/test_reso
- `tests.test_edge_cases.test_print0_short_form`
  > AssertionError: assert 3 == 2
  >  +  where 3 = len([b'/workspace/eval/test_resources/test_edge_cases/file1.txt:1:apple banana cherry\n/workspace/eval/test_resources/test_edge_cases/file2.txt:1:banana orange\n/workspace/eval/test_reso
- *(... 1 more in this cluster)*

### `boolean_false` — 4 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_options.test_vimgrep_format_output`
  > AssertionError: assert False
  >  +  where False = <built-in method endswith of str object at 0x7f0d80e505b0>('multi.txt:1:1:foo bar')
  >  +    where <built-in method endswith of str object at 0x7f0d80e505b0> = '/tmp/pytest-of-root/pytest-0/test_vimgrep_format_output5/multi.txt:1:foo bar'.endswith
- `tests.test_search.test_two_char_literal_hash_search`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7f0d80afd8f0>('1:')
  >  +    where <built-in method startswith of str object at 0x7f0d80afd8f0> = '/tmp/pytest-of-root/pytest-0/test_two_char_literal_hash_sea2/two_char.txt:1:ab is here'.startswith
- `tests.test_util.test_large_file_with_utf8`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x557b4c288ae0>('café café café')
  >  +    where <built-in method startswith of str object at 0x557b4c288ae0> = '/tmp/pytest-of-root/pytest-0/test_large_file_with_utf82/large_utf8.txt:1:café café café café café café café café café café c
- *(... 1 more in this cluster)*

### `returned_none` — 3 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_output_format.test_column_numbers`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f52082cb760>(b'1:\\d+:', b'col.txt:1:hello world\n')
  >  +    where <function search at 0x7f52082cb760> = re.search
  >  +    and   b'col.txt:1:hello world\n' = CompletedProcess(args=['/workspace/executable', '--column', 'world', 'col.txt'], returncode=0, stdout=b'col.txt:1:hello world\n', stderr=b'').stdout
- `eval.tests.test_output_format.test_vimgrep_format`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f52082cb760>(b'vim\\.txt:\\d+:\\d+:', b'vim.txt:1:match here\n')
  >  +    where <function search at 0x7f52082cb760> = re.search
  >  +    and   b'vim.txt:1:match here\n' = CompletedProcess(args=['/workspace/executable', '--vimgrep', 'match', 'vim.txt'], returncode=0, stdout=b'vim.txt:1:match here\n', stderr=b'').stdout
- `eval.tests.test_ag_behavior.test_numbers_and_no_numbers_format`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f1c0b47e680>('^1:foo$', 'src/a.txt:1:foo')
  >  +    where <function search at 0x7f1c0b47e680> = re.search

### `rc_mismatch_got0_want2` — 2 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_errors.test_invalid_width_value`
  > assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--width=abc', 'test'], returncode=0, stdout=b'run.sh:6:pip install pytest pytest-timeout pytest-xdist -q 2>/dev/null || true\nrun.sh:8:# 
- `eval.tests.test_argparse_validation.test_width_requires_integer_value_errors`
  > assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--width', 'nope', 'foo', '.'], returncode=0, stdout='eval/tests/__pycache__/test_argparse_validation.cpython-310-pytest-9.0.3.pyc:74:@py_

### `rc_mismatch_got1_want5` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_file_utils.test_max_matches_limit_literal_search`
  > AssertionError: assert 1 == 5
  >  +  where 1 = len(['/tmp/pytest-of-root/pytest-0/test_max_matches_limit_literal2/many.txt:5:line test 5'])
- `tests.test_options.test_stats_only_shows_stats_without_matches`
  > AssertionError: assert 1 == 5
  >  +  where 1 = len(['/workspace/eval/test_resources/test_options/sample.txt:1:foo bar baz'])

### `rc_mismatch_got82_want0` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_special_cases.test_silent_mode`
  > assert 82 == 0
  >  +  where 82 = len(b"the-silver-searcher: cannot access '/nonexistent/path': No such file or directory\n")
  >  +    where b"the-silver-searcher: cannot access '/nonexistent/path': No such file or directory\n" = CompletedProcess(args=['/workspace/executable', '--silent', 'nonexistent', '/nonexistent/path'], re

### `rc_mismatch_got2_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_combinations.test_vimgrep_format_shows_column_for_each_match`
  > AssertionError: assert 2 == 3
  >  +  where 2 = len(['/workspace/eval/test_resources/test_combinations/multiline.txt:1:match here match there', '/workspace/eval/test_resources/test_combinations/multiline.txt:3:match again'])

### `rc_mismatch_got5_want2` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_combinations.test_files_with_matches_lists_filenames_only`
  > AssertionError: assert 5 == 2
  >  +  where 5 = len(['/workspace/eval/test_resources/test_combinations/dir1/file1.txt:1:match one in file1', '/workspace/eval/test_resources/test_combinations/dir1/file1.txt:2:no match here', '/workspac

### `rc_mismatch_got3_want1` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_edge_cases.test_case_sensitive_flag_combination`
  > AssertionError: assert 3 == 1
  >  +  where 3 = len(['/workspace/eval/test_resources/test_edge_cases/case_test.txt:1:Match', '/workspace/eval/test_resources/test_edge_cases/case_test.txt:2:match', '/workspace/eval/test_resources/test_

### `rc_mismatch_got4_want1` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_edge_cases.test_literal_mode_escapes_regex`
  > AssertionError: assert 4 == 1
  >  +  where 4 = len(['/workspace/eval/test_resources/test_edge_cases/literal_test.txt:1:.*', '/workspace/eval/test_resources/test_edge_cases/literal_test.txt:2:abc', '/workspace/eval/test_resources/test

### `empty_list_or_string` — 1 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_edge_cases.test_only_matching_part_with_o_flag`
  > IndexError: list index out of range

### `rc_mismatch_got1_want2` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_options.test_invalid_width_option_dies_with_error`
  > assert 1 == 2
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-W', 'notanumber', 'foo', '/workspace/eval/test_resources/test_options/sample.txt'], returncode=1, stdout=b'', stderr=b"the-silver-search

### `test_timeout` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_util.test_named_pipe_skipped`
  > subprocess.TimeoutExpired: Command '['/workspace/executable', '--no-numbers', 'content']' timed out after 30 seconds

### `rc_mismatch_got2_want4` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_util.test_smart_case_mixed_case_pattern`
  > AssertionError: assert 2 == 4
  >  +  where 2 = len(['/tmp/pytest-of-root/pytest-0/test_smart_case_mixed_case_pat2/case_test.txt:2:test', '/tmp/pytest-of-root/pytest-0/test_smart_case_mixed_case_pat2/case_test.txt:4:testing'])

### `rc_unexpected_zero` — 1 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `eval.tests.test_subcommand_dispatch.TestInvalidOptions.test_invalid_short_option`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '-Z', 'pattern'], returncode=0, stdout=b'README.md:17:* It ignores file patterns from your `.gitignore` and `.hgignore`.\nREADME.md:18:* If there a

### `rc_mismatch_got6_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_additional_coverage.TestConsecutiveMatches.test_all_lines_match`
  > AssertionError: assert 6 == 3
  >  +  where 6 = <built-in method count of str object at 0x7f9668764730>('match')
  >  +    where <built-in method count of str object at 0x7f9668764730> = '/tmp/pytest-of-root/pytest-0/test_all_lines_match2/test.txt:1:match\n/tmp/pytest-of-root/pytest-0/test_all_lines_match2/test.txt:

