# Action Sheet — anordal__shellharden.6a6ffd4

**Current:** 76.32%  (986/1292)
**Pass / Fail / Skip:** 986 / 306 / 0
**Gap to 100%:** 23.68 percentage points (306 tests)

## Failure clusters

306 failed tests grouped into 10 buckets (sorted by count).

### `string_output_mismatch` — 115 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_cli.test_syntax_mode_produces_highlighted_output`
  > assert '\x1b[0;42mec...$foo"\x1b[m\n' == '\x1b[0;38;2;...m$foo\x1b[m\n'
  >   
  >   - #x1B[0;38;2;192;0;128mecho#x1B[m #x1B[0;38;2;63;127;207m$foo#x1B[m
  >   + #x1B[0;42mecho "$foo"#x1B[m
- `tests.test_cli.test_stdin_with_syntax_error`
  > assert 'shellharden:...ouble quote\n' == 'echo "$foo"\... malformed.\n'
  >   
  >   + shellharden: unclosed double quote
  >   - echo "$foo"
  >   - echo "unclosed
  >   - 
  >   - : Unexpected end of file
  >   - The file's end was reached without closing all sytactic scopes.
- `tests.test_cli.test_nonexistent_file_error`
  > AssertionError: assert 'shellharden:...r directory\n' == '/nonexistent...os error 2)\n'
  >   
  >   - /nonexistent/file.sh: No such file or directory (os error 2)
  >   ?                                                -------------
  >   + shellharden: /nonexistent/file.sh: No such file or directory
  >   ? +++++++++++++
- *(... 112 more in this cluster)*

### `other_assertion` — 90 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_contexts_no_quoting.test_case_pattern_no_quoting`
  > assert '$pattern)' in 'case value in\n    "$pattern")\n        echo match\n    ;;\nesac\n'
- `eval.tests.test_error_handling.test_unexpected_eof_single_quote`
  > AssertionError: assert b'Unexpected end of file' in b'shellharden: unclosed single quote\n'
  >  +  where b'shellharden: unclosed single quote\n' = CompletedProcess(args=['./executable', '--transform', ''], returncode=1, stdout=b'', stderr=b'shellharden: unclosed single quote\n').stderr
- `eval.tests.test_error_handling.test_unexpected_eof_heredoc`
  > AssertionError: assert b'Unexpected end of file' in b'shellharden: unclosed heredoc\n'
  >  +  where b'shellharden: unclosed heredoc\n' = CompletedProcess(args=['./executable', '--transform', ''], returncode=1, stdout=b'', stderr=b'shellharden: unclosed heredoc\n').stderr
- *(... 87 more in this cluster)*

### `rc_mismatch_got1_want0` — 44 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `eval.tests.test_contexts_no_quoting.test_arithmetic_no_quoting`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '--transform', ''], returncode=1, stdout=b'', stderr=b'shellharden: unclosed arithmetic\n').returncode
- `eval.tests.test_edge_cases.test_deeply_nested_substitutions`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '--transform', ''], returncode=1, stdout=b'', stderr=b'shellharden: unclosed command substitution\n').returncode
- `eval.tests.test_edge_cases.test_deeply_nested_quotes`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '--transform', ''], returncode=1, stdout=b'', stderr=b'shellharden: unclosed command substitution\n').returncode
- *(... 41 more in this cluster)*

### `rc_mismatch_got0_want1` — 24 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `eval.tests.test_error_handling.test_unexpected_eof_double_bracket`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', '--transform', ''], returncode=0, stdout=b'[[ $a ==]]', stderr=b'').returncode
- `tests.test_error_handling.test_unclosed_double_brackets`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--transform', ''], returncode=0, stdout=b'[[ $va]]', stderr=b'').returncode
- `tests.test_errors.test_unclosed_double_quote_exit_code`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/tmp/pytest-of-root/pytest-0/popen-gw1/test_unclosed_double_quote_exi2/test.sh'], returncode=0, stdout='echo "unterminated', stderr='').r
- *(... 21 more in this cluster)*

### `rc_mismatch_got2_want0` — 10 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `eval.tests.test_moduletests.test_moduletest_check_expected[quoting_unneeded.bash]`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--check', 'moduletests/expected/quoting_unneeded.bash'], returncode=2, stdout=b'', stderr=b'').returncode
- `eval.tests.test_moduletests.test_moduletest_check_expected[esac_1.bash]`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--check', 'moduletests/expected/esac_1.bash'], returncode=2, stdout=b'', stderr=b'').returncode
- `eval.tests.test_moduletests.test_moduletest_check_expected[esac_2.bash]`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--check', 'moduletests/expected/esac_2.bash'], returncode=2, stdout=b'', stderr=b'').returncode
- *(... 7 more in this cluster)*

### `bytes_output_mismatch` — 7 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `eval.tests.test_contexts_no_quoting.test_backtick_in_assignment_context`
  > AssertionError: assert b'a=$(uname -a)\n' == b'a=`uname -a`\n'
  >   
  >   At index 2 diff: b'$' != b'`'
  >   
  >   Full diff:
  >   - (b'a=`uname -a`\n')
  >   ?      ^        ^
  >   + (b'a=$(uname -a)\n')
- `eval.tests.test_quoting_transformations.test_pwd_backtick_with_text`
  > AssertionError: assert b'pwd=$PWDhazard\n' == b'pwd=`pwd`hazard\n'
  >   
  >   At index 4 diff: b'$' != b'`'
  >   
  >   Full diff:
  >   - (b'pwd=`pwd`hazard\n')
  >   ?        ^^^^^
  >   + (b'pwd=$PWDhazard\n')
- `eval.tests.test_quoting_transformations.test_special_variable_dash`
  > assert b'echo $-\n' == b'echo "$-"\n'
  >   
  >   At index 5 diff: b'$' != b'"'
  >   
  >   Full diff:
  >   - (b'echo "$-"\n')
  >   ?         -  -
  >   + (b'echo $-\n')
- *(... 4 more in this cluster)*

### `rc_mismatch_got0_want2` — 5 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_errors.test_check_mode_with_changes_needed`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--check', '/tmp/pytest-of-root/pytest-0/popen-gw2/test_check_mode_with_changes_n2/test.sh'], returncode=0, stdout='', stderr='').returnco
- `tests.test_errors.test_check_mode_exits_immediately_on_first_change`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--check', '/tmp/pytest-of-root/pytest-0/popen-gw2/test_check_mode_exits_immediat2/file1.sh', '/tmp/pytest-of-root/pytest-0/popen-gw2/test
- `tests.test_variables.test_check_mode_accepts_quoted_braced_variable`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--check', '/tmp/pytest-of-root/pytest-0/popen-gw4/test_check_mode_accepts_quoted2/test.sh'], returncode=0, stdout='', stderr='').returnco
- *(... 2 more in this cluster)*

### `uncategorized` — 5 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_shellharden_module_tests.TestModuleTests.test_transform_matches_expected[test.bash]`
  > Failed: Command failed: /workspace/executable --transform -- /workspace/moduletests/original/test.bash
  > stdout: 
  > stderr: shellharden: unclosed command substitution
- `eval.tests.test_shellharden_module_tests.TestModuleTests.test_transform_matches_expected[pwd.bash]`
  > Failed: Command failed: /workspace/executable --transform -- /workspace/moduletests/original/pwd.bash
  > stdout: 
  > stderr: shellharden: unclosed command substitution
- `eval.tests.test_shellharden_module_tests.TestModuleTests.test_transform_matches_expected[backtick.bash]`
  > Failed: Command failed: /workspace/executable --transform -- /workspace/moduletests/original/backtick.bash
  > stdout: 
  > stderr: shellharden: unclosed backtick
- *(... 2 more in this cluster)*

### `boolean_false` — 3 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_replace.test_replace_file_with_very_long_line`
  > assert False
  >  +  where False = <built-in method startswith of str object at 0x59126bf22500>('echo "${')
  >  +    where <built-in method startswith of str object at 0x59126bf22500> = 'echo "$xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
- `eval.tests.test_argparse_validation.test_unknown_option_errors[argv1]`
  > AssertionError: assert False
  >  +  where False = <built-in method endswith of str object at 0x753a5f96ac40>('No such option.\n')
  >  +    where <built-in method endswith of str object at 0x753a5f96ac40> = 'shellharden: -: No such option\n'.endswith
- `eval.tests.test_argparse_validation.test_unknown_option_errors[argv0]`
  > AssertionError: assert False
  >  +  where False = <built-in method endswith of str object at 0x7de62e8355f0>('No such option.\n')
  >  +    where <built-in method endswith of str object at 0x7de62e8355f0> = 'shellharden: --nope: No such option\n'.endswith

### `returned_none` — 3 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_syntax.test_ansi_codes_bold_format`
  > assert None is not None
  >  +  where None = <function search at 0x731c79ef4af0>('\\[0;1[;m]', '#!/bin/bash\nif true; then\n  echo "test"\nfi\n\nfor i in 1 2 3; do\n\x1b[0;42m  echo "$i"\x1b[m\ndone\n\nwhile true; do\n  break\nd
  >  +    where <function search at 0x731c79ef4af0> = re.search
  >  +    and   '#!/bin/bash\nif true; then\n  echo "test"\nfi\n\nfor i in 1 2 3; do\n\x1b[0;42m  echo "$i"\x1b[m\ndone\n\nwhile true; do\n  break\ndone\n\ncase $1 in\n  a) echo "a" ;;\n  b) echo "b" ;;\n
- `tests.test_syntax.test_ansi_codes_italic_format`
  > assert None is not None
  >  +  where None = <function search at 0x731c79ef4af0>('\\[0;1;3;', '#!/bin/bash\n# This is a comment\necho "test"  # inline comment\n# Another comment with special chars: $var "quotes"\n')
  >  +    where <function search at 0x731c79ef4af0> = re.search
  >  +    and   '#!/bin/bash\n# This is a comment\necho "test"  # inline comment\n# Another comment with special chars: $var "quotes"\n' = CompletedProcess(args=['/workspace/executable', '--syntax', '/wor
- `tests.test_syntax.test_ansi_codes_rgb_format_for_foreground`
  > assert None is not None
  >  +  where None = <function search at 0x708e957ccaf0>('\\[0;38;2;\\d+;\\d+;\\d+m', '#!/bin/bash\nname="world"\necho "Hello $name"\necho "Path: $PATH"\nresult=${var:-default}\n\x1b[0;42mecho "${array[0]
  >  +    where <function search at 0x708e957ccaf0> = re.search
  >  +    and   '#!/bin/bash\nname="world"\necho "Hello $name"\necho "Path: $PATH"\nresult=${var:-default}\n\x1b[0;42mecho "${array[0]}"\x1b[m\n' = CompletedProcess(args=['/workspace/executable', '--synta

