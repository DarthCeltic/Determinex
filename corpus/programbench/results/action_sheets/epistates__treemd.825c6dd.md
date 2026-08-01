# Action Sheet — epistates__treemd.825c6dd

**Current:** 13.03%  (263/2019)
**Pass / Fail / Skip:** 263 / 754 / 5
**Gap to 100%:** 86.97 percentage points (1756 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_cli_atline.test_at_line_basic`
  - reason: at-line subcommand not implemented in src/main.rs - defined but no handler exists
- `tests.test_cli_atline.test_at_line_first_line`
  - reason: at-line subcommand not implemented in src/main.rs
- `tests.test_cli_atline.test_at_line_beyond_eof`
  - reason: at-line subcommand not implemented in src/main.rs
- `eval.tests.test_subcommand_dispatch.test_subcommand_help_recognized[NOTSET]`
  - reason: got empty parameter set for (subcmd)
- `eval.tests.test_subcommand_dispatch.test_subcommand_help_differs_from_main_help[NOTSET]`
  - reason: got empty parameter set for (subcmd)

## Failure clusters

754 failed tests grouped into 18 buckets (sorted by count).

### `other_assertion` — 383 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_at_line_subcommand.test_at_line_help`
  > AssertionError: assert b'Show heading at specific line' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', 'at-line', '--help'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_basic_invocation.test_help_short`
  > AssertionError: assert b'markdown' in b''
  >  +  where b'' = <built-in method lower of bytes object at 0x7f2d339ac030>()
  >  +    where <built-in method lower of bytes object at 0x7f2d339ac030> = b''.lower
  >  +      where b'' = CompletedProcess(args=['/workspace/executable', '-h'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_basic_invocation.test_help_long`
  > AssertionError: assert (b'treemd' in b'' or b'markdown' in b'')
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', '--help'], returncode=0, stdout=b'', stderr=b'').stdout
  >  +  and   b'' = <built-in method lower of bytes object at 0x7f2d339ac030>()
  >  +    where <built-in method lower of bytes object at 0x7f2d339ac030> = b''.lower
  >  +      where b'' = CompletedProcess(args=['/workspace/executable', '--help'], returncode=0, stdout=b'', stderr=b'').stdout
- *(... 380 more in this cluster)*

### `string_output_mismatch` — 172 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_query_advanced.test_query_length_function`
  > AssertionError: assert 'Section 1' == '3'
  >   
  >   - 3
  >   + Section 1
- `tests.test_query_advanced.test_query_size_function`
  > AssertionError: assert 'Section 1' == '3'
  >   
  >   - 3
  >   + Section 1
- `tests.test_query_advanced.test_query_len_alias`
  > AssertionError: assert 'Section 1' == '3'
  >   
  >   - 3
  >   + Section 1
- *(... 169 more in this cluster)*

### `json_output_missing_or_bad` — 62 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `tests.test_cli_commands.test_cli_list_json_structure`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_cli_commands.test_cli_tree_json_structure`
  > json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 2 column 1 (char 2)
- `tests.test_list_mode.test_list_output_json`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- *(... 59 more in this cluster)*

### `rc_mismatch_got1_want0` — 45 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_list_mode.test_list_basic`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '--list', '/tmp/tmpxcmgk3os/sample.md'], returncode=1, stdout=b'', stderr=b'').returncode
- `tests.test_cli_atline.test_very_deep_nesting_beyond_h6`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '--list', '/tmp/pytest-of-root/pytest-0/test_very_deep_nesting_beyond_2/too_deep.md'], returncode=1, stdout='', stderr='').returncode
- `tests.test_cli_commands.test_list_empty_document`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '--list', '/workspace/eval/test_resources/test_cli_commands/empty.md'], returncode=1, stdout='# Test Heading\n## Subheading\n', stderr='').returnco
- *(... 42 more in this cluster)*

### `rc_unexpected_zero` — 36 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_at_line_subcommand.test_at_line_invalid_number`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'at-line', 'abc'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_basic_invocation.test_no_args_without_terminal`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable'], returncode=0, stdout=b'treemd 0.1.0\n----------------------------------------\nInteractive TUI tool driven by tmux/libtmux/pexpect harnes
- `tests.test_error_handling.test_empty_stdin_error`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-l', '-'], returncode=0, stdout=b'Test Heading\nSection 1\n', stderr=b'').returncode
- *(... 33 more in this cluster)*

### `rc_mismatch_got0_want2` — 15 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_argument_parsing.TestInvalidFlags.test_unknown_flag_long`
  > assert 0 == 2
- `tests.test_argument_parsing.TestInvalidFlags.test_unknown_flag_short`
  > assert 0 == 2
- `tests.test_argument_parsing.TestInvalidFlags.test_misspelled_flag`
  > assert 0 == 2
- *(... 12 more in this cluster)*

### `rc_mismatch_got0_want1` — 13 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_cli_atline.test_truly_empty_stdin_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', '--list', '-'], returncode=0, stdout='# First File\n', stderr='').returncode
- `tests.test_cli_commands_gap.test_truly_empty_stdin_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', '--list', '-'], returncode=0, stdout='# First File\n', stderr='').returncode
- `tests.test_cli_commands_gap.test_section_not_found_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', '--section', 'Nonexistent Section', '/workspace/eval/test_resources/test_cli_commands_gap/precedence.md'], returncode=0, stdout='Section 1\nSection
- *(... 10 more in this cluster)*

### `boolean_false` — 12 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_query_language.test_query_count_function`
  > AssertionError: assert False
  >  +  where False = <built-in method isdigit of str object at 0x7f2d31b2df70>()
  >  +    where <built-in method isdigit of str object at 0x7f2d31b2df70> = 'Section 1'.isdigit
- `tests.test_cli_setup_config.test_setup_completions_with_spaces_in_home`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/test with spaces_x9_20kcf/.bashrc').exists
- `tests.test_cli_setup_config.test_setup_completions_zsh_adds_to_zshrc`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/test_zsh_add_t23t1qj6/.zshrc').exists
- *(... 9 more in this cluster)*

### `bytes_output_mismatch` — 4 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_cli_commands_gap.test_filter_special_character_colon`
  > AssertionError: assert '## Second Le...econd Level B' == '## Test Section: With Colon'
  >   
  >   - ## Test Section: With Colon
  >   + ## Second Level A
  >   + ## Second Level B
- `tests.test_cli_commands_gap.test_filter_special_character_parenthesis`
  > AssertionError: assert '## Second Le...econd Level B' == '## Section (... Parentheses)'
  >   
  >   - ## Section (With Parentheses)
  >   + ## Second Level A
  >   + ## Second Level B
- `eval.tests.test_help_and_version.test_version_exact`
  > AssertionError: assert b'treemd\ntre...n Title\n#:\n' == b'treemd 0.5.7\n'
  >   
  >   At index 6 diff: b'\n' != b' '
  >   
  >   Full diff:
  >   - (b'treemd 0.5.7\n')
  >   + (b'treemd\ntreemd\nMain Title\nSection 1\nMain Title\nSection 1\nMain Title\n#'
  >   +  b':\n')
- *(... 1 more in this cluster)*

### `rc_mismatch_got1_want3` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_query_basic.test_heading_with_special_characters_in_text`
  > AssertionError: assert 1 == 3
  >  +  where 1 = len(['Section 1'])
- `tests.test_cli_query_basic.test_multiple_heading_levels_in_one_query`
  > AssertionError: assert 1 == 3
  >  +  where 1 = len(['Section 1'])
- `tests.test_cli_query_basic.test_slice_with_negative_start`
  > AssertionError: assert 1 == 3
  >  +  where 1 = len(['Section 1'])

### `rc_mismatch_got1_want2` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_argument_parsing.TestErrorExitCodes.test_invalid_argument_exit_code`
  > assert 1 == 2
- `tests.test_argument_parsing.TestMissingRequiredValues.test_filter_flag_without_value`
  > assert 1 == 2

### `rc_mismatch_got123_want0` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_commands_remaining.test_completion_nonexistent_directory_returns_empty`
  > AssertionError: assert 123 == 0
  >  +  where 123 = len(['treemd 0.1.0', 'Interactive TUI tool driven by tmux/libtmux/pexpect harness', 'Journals', 'Tasks', 'Filter', 'Help', ...])

### `rc_mismatch_got2_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_output.test_level_takes_precedence_over_filter`
  > AssertionError: assert 2 == 3
  >  +  where 2 = len(['## Second Level A', '## Second Level B'])

### `rc_mismatch_got1_want11` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_query_basic.test_all_headings_selector`
  > AssertionError: assert 1 == 11
  >  +  where 1 = len(['Section 1'])

### `rc_mismatch_got1_want6` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_query_basic.test_iterate_operator_empty_brackets`
  > AssertionError: assert 1 == 6
  >  +  where 1 = len(['Section 1'])

### `rc_mismatch_got1_want4` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_query_basic.test_slice_with_negative_end`
  > AssertionError: assert 1 == 4
  >  +  where 1 = len(['Section 1'])

### `missing_file` — 1 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_cli_setup_config.test_setup_completions_no_duplicate_on_rerun`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/test_no_dup_byxp2sd9/.bashrc'

### `empty_list_or_string` — 1 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `eval.tests.test_help_and_version.test_query_help_starts_with_banner`
  > IndexError: list index out of range

