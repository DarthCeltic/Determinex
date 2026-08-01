# Action Sheet — wfxr__code-minimap.0ddeea5

**Current:** 24.71%  (105/425)
**Pass / Fail / Skip:** 105 / 262 / 1
**Gap to 100%:** 75.29 percentage points (320 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_subcommands.test_subcommand_recognized_via_help_flag[NOTSET]`
  - reason: got empty parameter set for (subcmd)

## Failure clusters

262 failed tests grouped into 16 buckets (sorted by count).

### `string_output_mismatch` — 100 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_args_parsing.test_invalid_args_errors[args0-2-err_substrings0]`
  > assert "error: unexp...y '--help'.\n" == ''
  >   
  >   + error: unexpected argument '--nonexistent-flag' found
  >   + 
  >   + Usage: code-minimap [OPTIONS] [FILE] [COMMAND]
  >   + 
  >   + For more information, try '--help'.
- `eval.tests.test_args_parsing.test_invalid_args_errors[args1-2-err_substrings1]`
  > assert "error: unexp...y '--help'.\n" == ''
  >   
  >   + error: unexpected argument '--horizontal-scale' found
  >   + 
  >   + Usage: code-minimap [OPTIONS] [FILE] [COMMAND]
  >   + 
  >   + For more information, try '--help'.
- `eval.tests.test_args_parsing.test_invalid_args_errors[args2-2-err_substrings2]`
  > assert "error: unexp...y '--help'.\n" == ''
  >   
  >   + error: unexpected argument '--vertical-scale' found
  >   + 
  >   + Usage: code-minimap [OPTIONS] [FILE] [COMMAND]
  >   + 
  >   + For more information, try '--help'.
- *(... 97 more in this cluster)*

### `rc_mismatch_got1_want0` — 46 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_completion.test_completion_bash`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', 'completion', 'bash'], returncode=1, stdout=b'', stderr=b'error: No such file or directory: completion\n').returncode
- `tests.test_completion.test_completion_zsh`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', 'completion', 'zsh'], returncode=1, stdout=b'', stderr=b'error: No such file or directory: completion\n').returncode
- `tests.test_completion.test_completion_fish`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', 'completion', 'fish'], returncode=1, stdout=b'', stderr=b'error: No such file or directory: completion\n').returncode
- *(... 43 more in this cluster)*

### `rc_mismatch_got2_want0` — 40 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_edge_cases.test_encoding_with_bom`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '/tmp/tmpris51n0a/bom.txt', '--encoding', 'utf8-lossy'], returncode=2, stdout=b"error: unexpected argument '--encoding' found\n\nUsage: code-minima
- `tests.test_encoding.test_encoding_utf8_lossy_explicit`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '/tmp/tmp1rx7pzz3/test.txt', '--encoding', 'utf8-lossy'], returncode=2, stdout=b"error: unexpected argument '--encoding' found\n\nUsage: code-minim
- `tests.test_encoding.test_encoding_utf8_explicit`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '/tmp/tmpa95g8slz/test.txt', '--encoding', 'utf8'], returncode=2, stdout=b"error: unexpected argument '--encoding' found\n\nUsage: code-minimap [OP
- *(... 37 more in this cluster)*

### `other_assertion` — 33 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_help_flag`
  > AssertionError: assert b'code minimap' in b'code-minimap 0.6.8\nVisualize content for minimap\n\nUsage: code-minimap [OPTIONS] [FILE] [COMMAND]\n\nCommands:\n  completion  Generate shell completion\n\
  >  +  where b'code-minimap 0.6.8\nVisualize content for minimap\n\nUsage: code-minimap [OPTIONS] [FILE] [COMMAND]\n\nCommands:\n  completion  Generate shell completion\n\nArguments:\n  [FILE]  Input fil
- `tests.test_basic_invocation.test_help_short_flag`
  > AssertionError: assert b'code minimap' in b'code-minimap 0.6.8\nVisualize content for minimap\n\nUsage: code-minimap [OPTIONS] [FILE] [COMMAND]\n\nCommands:\n  completion  Generate shell completion\n\
  >  +  where b'code-minimap 0.6.8\nVisualize content for minimap\n\nUsage: code-minimap [OPTIONS] [FILE] [COMMAND]\n\nCommands:\n  completion  Generate shell completion\n\nArguments:\n  [FILE]  Input fil
- `tests.test_basic_invocation.test_stdin_single_empty_line`
  > AssertionError: assert b'\xe2\xa0\x80' in b''
  >  +  where b'' = CompletedProcess(args=['./executable'], returncode=0, stdout=b'', stderr=b'').stdout
- *(... 30 more in this cluster)*

### `rc_mismatch_got1_want2` — 11 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_args_parsing.test_invalid_args_errors[args6-2-err_substrings6]`
  > assert 1 == 2
- `eval.tests.test_args_parsing.test_invalid_args_errors[args7-2-err_substrings7]`
  > assert 1 == 2
- `eval.tests.test_args_parsing.test_invalid_args_errors[args8-2-err_substrings8]`
  > assert 1 == 2
- *(... 8 more in this cluster)*

### `rc_mismatch_got0_want2` — 8 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_error_handling.test_negative_scale_as_flag_error`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['./executable', '/tmp/tmp4dv5m40x/test.txt', '-H', '-1.0'], returncode=0, stdout=b'\xe2\xa1\x87\n', stderr=b'').returncode
- `eval.tests.test_args_parsing.test_invalid_args_errors[args3-2-err_substrings3]`
  > assert 0 == 2
- `eval.tests.test_args_parsing.test_negative_number_as_separate_token_is_not_accepted_as_option_value[args0-expected_substrings0]`
  > assert 0 == 2
- *(... 5 more in this cluster)*

### `rc_mismatch_got2_want1` — 6 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_encoding.test_encoding_utf8_with_invalid_bytes`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['./executable', '/tmp/tmphn76vvm6/invalid.txt', '--encoding', 'utf8'], returncode=2, stdout=b"error: unexpected argument '--encoding' found\n\nUsage: code-minimap 
- `eval.tests.test_args_parsing.test_single_dash_is_treated_as_file_and_fails_with_os_error`
  > assert 2 == 1
- `eval.tests.test_args_parsing.test_double_dash_makes_following_token_positional_and_fails_opening_that_filename`
  > assert 2 == 1
- *(... 3 more in this cluster)*

### `rc_unexpected_zero` — 4 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_error_handling.test_invalid_horizontal_scale`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '/tmp/tmpuh56f2vw/test.txt', '-H', 'invalid'], returncode=0, stdout=b'\xe2\xa3\xbf\xe2\xa3\xbf\n', stderr=b'').returncode
- `tests.test_error_handling.test_invalid_vertical_scale`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '/tmp/tmprtn7rcc0/test.txt', '-V', 'not-a-number'], returncode=0, stdout=b'code-minimap 0.6.8\n', stderr=b'').returncode
- `tests.test_error_handling.test_invalid_padding`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '/tmp/tmpt0q275s3/test.txt', '--padding', 'abc'], returncode=0, stdout=b'\xe2\xa3\xbf\xe2\xa3\xbf\n', stderr=b'').returncode
- *(... 1 more in this cluster)*

### `bytes_output_mismatch` — 4 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `eval.tests.test_cli_behavior.test_core_minimap_output_matches_golden[args1-golden_one_h2.bin]`
  > AssertionError: assert b'code-minimap 0.6.8\n' == b'\xe2\xa0\x89\n'
  >   
  >   At index 0 diff: b'c' != b'\xe2'
  >   
  >   Full diff:
  >   - b'\xe2\xa0\x89\n'
  >   + (b'code-minimap 0.6.8\n')
- `eval.tests.test_cli_behavior.test_core_minimap_output_matches_golden[args2-golden_one_pad2.bin]`
  > AssertionError: assert b'  \xe2\xa0\x81\n' == b'\xe2\xa0\x81 \n'
  >   
  >   At index 0 diff: b' ' != b'\xe2'
  >   
  >   Full diff:
  >   - (b'\xe2\xa0\x81 \n')
  >   ?                -
  >   + (b'  \xe2\xa0\x81\n')
- `eval.tests.test_cli_behavior.test_core_minimap_output_matches_golden[args3-golden_one_v05.bin]`
  > AssertionError: assert b'code-minimap 0.6.8\n' == b'\xe2\xa0\x81\n'
  >   
  >   At index 0 diff: b'c' != b'\xe2'
  >   
  >   Full diff:
  >   - b'\xe2\xa0\x81\n'
  >   + (b'code-minimap 0.6.8\n')
- *(... 1 more in this cluster)*

### `boolean_false` — 3 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_errors.test_whitespace_only_stdin`
  > assert False
  >  +  where False = any(<generator object test_whitespace_only_stdin.<locals>.<genexpr> at 0x7fedf325dee0>)
- `tests.test_errors.test_very_long_single_line`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7fedf4156550>('⠛⠛⠛⠛⠛⠉⠉')
  >  +    where <built-in method startswith of str object at 0x7fedf4156550> = '⠛⠛⠋⠛⠛⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉'.startswith
- `tests.test_scaling.test_horizontal_scale_0_0_produces_empty`
  > assert False
  >  +  where False = all(<generator object test_horizontal_scale_0_0_produces_empty.<locals>.<genexpr> at 0x7fedf3559f50>)

### `returned_none` — 2 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_main.test_help_lists_commands_completion_and_help`
  > AssertionError: assert None is not None
  >  +  where None = <function search at 0x7f28f35fe680>('^\\s*completion\\s*$', 'code-minimap 0.6.8\nVisualize content for minimap\n\nUsage: code-minimap [OPTIONS] [FILE] [COMMAND]\n\nCommands:\n  comple
  >  +    where <function search at 0x7f28f35fe680> = re.search
  >  +    and   re.MULTILINE = re.M
- `eval.tests.test_help_subcommands.test_completion_help_has_help_option_only`
  > AssertionError: assert None is not None
  >  +  where None = <function search at 0x7f28f35fe680>('^\\s*-h, --help\\s*$', 'code-minimap 0.6.8\nVisualize content for minimap\n\nUsage: code-minimap [OPTIONS] [FILE] [COMMAND]\n\nCommands:\n  comple
  >  +    where <function search at 0x7f28f35fe680> = re.search
  >  +    and   re.MULTILINE = re.M

### `rc_mismatch_got11_want10` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_padding.test_padding_value_10`
  > AssertionError: assert 11 == 10
  >  +  where 11 = len('          ⣿')

### `rc_mismatch_got21_want20` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_padding.test_padding_value_20`
  > AssertionError: assert 21 == 20
  >  +  where 21 = len('                    ⡇')

### `rc_mismatch_got51_want50` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_padding.test_padding_larger_than_content`
  > AssertionError: assert 51 == 50
  >  +  where 51 = len('                                                  ⡇')

### `rc_mismatch_got17_want15` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_padding.test_padding_with_scaling`
  > AssertionError: assert 17 == 15
  >  +  where 17 = len('               ⣿⠃')

### `rc_mismatch_got4_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_core_minimap.test_horizontal_scale_fractional`
  > AssertionError: assert 4 == 3
  >  +  where 4 = len('⠃⠃⠃⠃')

