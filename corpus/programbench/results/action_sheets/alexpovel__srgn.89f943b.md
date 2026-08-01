# Action Sheet — alexpovel__srgn.89f943b

**Current:** 15.21%  (376/2472)
**Pass / Fail / Skip:** 376 / 1137 / 0
**Gap to 100%:** 84.79 percentage points (2096 tests)

## Failure clusters

1137 failed tests grouped into 10 buckets (sorted by count).

### `rc_mismatch_got2_want0` — 430 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_actions.test_action_composition_replace_then_upper`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--upper', 'world', '--', 'there'], returncode=2, stdout=b'', stderr=b'File not found: there\n').returncode
- `tests.test_actions.test_action_composition_replace_then_lower`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--lower', 'WORLD', '--', 'THERE'], returncode=2, stdout=b'', stderr=b'File not found: THERE\n').returncode
- `tests.test_basic.test_no_args_with_stdin`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b"Usage: srgn [OPTIONS] [PATTERN] [FILES...]\nTry 'srgn --help' for more information.\n").returncode
- *(... 427 more in this cluster)*

### `other_assertion` — 324 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_actions.test_symbols_substitution`
  > AssertionError: assert b'\xe2\x89\xa0' in b'a EXCLAMATIONEQUALS b\n'
  >  +  where b'a EXCLAMATIONEQUALS b\n' = CompletedProcess(args=['/workspace/executable', '--symbols'], returncode=0, stdout=b'a EXCLAMATIONEQUALS b\n', stderr=b'').stdout
- `tests.test_actions.test_symbols_arrow`
  > AssertionError: assert b'\xe2\x86\x92' in b'a DASHGT b\n'
  >  +  where b'a DASHGT b\n' = CompletedProcess(args=['/workspace/executable', '--symbols'], returncode=0, stdout=b'a DASHGT b\n', stderr=b'').stdout
- `tests.test_actions.test_symbols_with_invert`
  > AssertionError: assert b'!=' in b'a \xe2\x89\xa0 b\n'
  >  +  where b'a \xe2\x89\xa0 b\n' = CompletedProcess(args=['/workspace/executable', '--symbols', '--invert'], returncode=0, stdout=b'a \xe2\x89\xa0 b\n', stderr=b'').stdout
- *(... 321 more in this cluster)*

### `string_output_mismatch` — 220 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_files.test_glob_action_without_replacement`
  > AssertionError: assert 'hello world' == 'hello WORLD'
  >   
  >   - hello WORLD
  >   + hello world
- `tests.test_case_transforms.test_uppercase_with_unicode`
  > AssertionError: assert 'CAFÉ\n' == 'CAFÉ'
  >   
  >   - CAFÉ
  >   + CAFÉ
  >   ?     +
- `tests.test_case_transforms.test_lowercase_with_unicode`
  > AssertionError: assert 'café\n' == 'café'
  >   
  >   - café
  >   + café
  >   ?     +
- *(... 217 more in this cluster)*

### `bytes_output_mismatch` — 50 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_actions.test_uppercase_action`
  > AssertionError: assert b'HELLO WORLD!\n' == b'Hello WORLD!'
  >   
  >   At index 1 diff: b'E' != b'e'
  >   
  >   Full diff:
  >   - (b'Hello WORLD!')
  >   + (b'HELLO WORLD!\n')
- `tests.test_actions.test_uppercase_all`
  > AssertionError: assert b'HELLO WORLD\n' == b'HELLO WORLD'
  >   
  >   Full diff:
  >   - (b'HELLO WORLD')
  >   + (b'HELLO WORLD\n')
  >   ?               ++
- `tests.test_actions.test_lowercase_action`
  > AssertionError: assert b'hello world!\n' == b'Hello world!'
  >   
  >   At index 0 diff: b'h' != b'H'
  >   
  >   Full diff:
  >   - (b'Hello world!')
  >   ?    ^
  >   + (b'hello world!\n')
- *(... 47 more in this cluster)*

### `rc_mismatch_got0_want2` — 45 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_argument_parsing.TestUnknownFlags.test_unknown_short_flag`
  > assert 0 == 2
- `tests.test_argument_parsing.TestUnknownFlags.test_misspelled_flag`
  > assert 0 == 2
- `tests.test_argument_parsing.TestShortAndLongFlagEquivalence.test_invert_flag[-i]`
  > assert 0 == 2
- *(... 42 more in this cluster)*

### `rc_unexpected_zero` — 33 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_basic.test_invalid_flag`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--invalid-flag-xyz'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_error_cases.test_conflicting_delete_with_other_action`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--delete', '--upper', 'test'], returncode=0, stdout=b'TEST\n', stderr=b'').returncode
- `tests.test_files.test_fail_any`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--fail-any', 'world'], returncode=0, stdout=b'Hello world\n', stderr=b'').returncode
- *(... 30 more in this cluster)*

### `rc_mismatch_got2_want1` — 13 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_argparse_validation.test_fail_no_files_requires_glob_context_to_trigger_failure`
  > AssertionError: assert 2 == 1
  >  +  where 2 = RunResult(rc=2, out='', err='').rc
- `tests.test_errors_and_edge_cases.test_glob_no_files_with_fail_flag`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--glob', '/nonexistent/*.txt', '--fail-no-files'], returncode=2, stdout='', stderr='').returncode
- `tests.test_errors_and_edge_cases.test_empty_python_scope_with_empty_file`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--python', 'def', '--stdin-detection', 'force-readable'], returncode=2, stdout='', stderr='File not found: force-readable\n').returncode
- *(... 10 more in this cluster)*

### `rc_mismatch_got0_want1` — 9 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_errors_and_edge_cases.test_invalid_regex_unclosed_bracket`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '[unclosed'], returncode=0, stdout='test\n', stderr='').returncode
- `tests.test_errors_and_edge_cases.test_invalid_regex_unclosed_group`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '(?P<'], returncode=0, stdout='test\n', stderr='').returncode
- `tests.test_errors_and_edge_cases.test_fail_any_and_fail_none_both_trigger`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--fail-any', '--fail-none', 'test'], returncode=0, stdout='test\n', stderr='').returncode
- *(... 6 more in this cluster)*

### `subprocess_failed` — 8 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_actions_basic.test_squeeze_with_replacement`
  > subprocess.CalledProcessError: Command '['/workspace/executable', '--squeeze', ' +', '--', '_']' returned non-zero exit status 2.
- `tests.test_actions_basic.test_squeeze_adjacent_patterns`
  > subprocess.CalledProcessError: Command '['/workspace/executable', '--squeeze', 'a+', '--', 'X']' returned non-zero exit status 2.
- `tests.test_actions_basic.test_squeeze_multiple_newlines`
  > subprocess.CalledProcessError: Command '['/workspace/executable', '--squeeze', '\\n+', '--', '\n']' returned non-zero exit status 2.
- *(... 5 more in this cluster)*

### `boolean_false` — 5 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_help_structure.TestHelpUsageLine.test_usage_mentions_options`
  > assert False
  >  +  where False = any(<generator object TestHelpUsageLine.test_usage_mentions_options.<locals>.<genexpr> at 0x7f29a060dee0>)
- `tests.test_help_structure.TestHelpUsageLine.test_usage_mentions_scope`
  > assert False
  >  +  where False = any(<generator object TestHelpUsageLine.test_usage_mentions_scope.<locals>.<genexpr> at 0x7f29a0600900>)
- `tests.test_help_structure.TestHelpUsageLine.test_usage_mentions_replacement`
  > assert False
  >  +  where False = any(<generator object TestHelpUsageLine.test_usage_mentions_replacement.<locals>.<genexpr> at 0x7f29a060edc0>)
- *(... 2 more in this cluster)*

