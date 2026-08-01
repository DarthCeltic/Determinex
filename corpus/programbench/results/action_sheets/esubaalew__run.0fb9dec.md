# Action Sheet — esubaalew__run.0fb9dec

**Current:** 4.27%  (67/1568)
**Pass / Fail / Skip:** 67 / 605 / 0
**Gap to 100%:** 95.73 percentage points (1501 tests)

## Failure clusters

605 failed tests grouped into 12 buckets (sorted by count).

### `other_assertion` — 231 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_bash_comprehensive.test_bash_simple_echo`
  > assert b'hello' in b'argc = 1\n'
  >  +  where b'argc = 1\n' = CompletedProcess(args=['./executable', '-l', 'bash', '-c', "echo 'hello'"], returncode=0, stdout=b'argc = 1\n', stderr=b'').stdout
- `tests.test_bash_comprehensive.test_bash_if_statement`
  > assert b'yes' in b'argc = 1\n'
  >  +  where b'argc = 1\n' = CompletedProcess(args=['./executable', '-l', 'bash', '-c', "if [ 5 -gt 3 ]; then echo 'yes'; fi"], returncode=0, stdout=b'argc = 1\n', stderr=b'').stdout
- `tests.test_bash_comprehensive.test_bash_function`
  > assert b'Hello, World' in b'argc = 1\n'
  >  +  where b'argc = 1\n' = CompletedProcess(args=['./executable', '-l', 'bash', '-c', 'greet() {\n    echo "Hello, $1"\n}\ngreet World'], returncode=0, stdout=b'argc = 1\n', stderr=b'').stdout
- *(... 228 more in this cluster)*

### `string_output_mismatch` — 222 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_argparse_validation.test_lang_accepts_equals_form_and_runs`
  > AssertionError: assert 'run 0.1.0\n-...\nyes\n--code' == 'eq'
  >   
  >   - eq
  >   + run 0.1.0
  >   + ----------------------------------------
  >   + Interactive TUI tool driven by tmux/libtmux/pexpect harness
  >   + 
  >   + Journals...
- `eval.tests.test_argparse_validation.test_code_accepts_equals_form_and_runs`
  > AssertionError: assert 'run 0.1.0\n-...\nyes\n--code' == 'eq2'
  >   
  >   - eq2
  >   + run 0.1.0
  >   + ----------------------------------------
  >   + Interactive TUI tool driven by tmux/libtmux/pexpect harness
  >   + 
  >   + Journals...
- `eval.tests.test_argparse_validation.test_short_lang_joined_value_form_runs`
  > AssertionError: assert 'run 0.1.0\n-...\nyes\n--code' == 'joined'
  >   
  >   - joined
  >   + run 0.1.0
  >   + ----------------------------------------
  >   + Interactive TUI tool driven by tmux/libtmux/pexpect harness
  >   + 
  >   + Journals...
- *(... 219 more in this cluster)*

### `uncategorized` — 75 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_bash_engine.test_repl_session_state_persistence`
  > pexpect.exceptions.EOF: End Of File (EOF). Exception style platform.
  > <pexpect.pty_spawn.spawn object at 0x7feecb07f1c0>
  > command: /workspace/executable
  > args: [b'/workspace/executable', b'--lang', b'bash']
  > buffer (last 100 chars): ''
  > before (last 100 chars): ''
  > after: <class 'pexpect.exceptions.EOF'>
  > match: None
- `tests.test_bash_engine.test_repl_session_error_recovery`
  > pexpect.exceptions.EOF: End Of File (EOF). Exception style platform.
  > <pexpect.pty_spawn.spawn object at 0x7feecabfc160>
  > command: /workspace/executable
  > args: [b'/workspace/executable', b'--lang', b'bash']
  > buffer (last 100 chars): ''
  > before (last 100 chars): ''
  > after: <class 'pexpect.exceptions.EOF'>
  > match: None
- `tests.test_bash_engine.test_repl_session_empty_input`
  > pexpect.exceptions.EOF: End Of File (EOF). Exception style platform.
  > <pexpect.pty_spawn.spawn object at 0x7feecaf497b0>
  > command: /workspace/executable
  > args: [b'/workspace/executable', b'--lang', b'bash']
  > buffer (last 100 chars): ''
  > before (last 100 chars): ''
  > after: <class 'pexpect.exceptions.EOF'>
  > match: None
- *(... 72 more in this cluster)*

### `rc_unexpected_zero` — 35 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_error_handling.test_invalid_language`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '-l', 'invalidlang', '-c', 'test'], returncode=0, stdout=b'short flags\n', stderr=b'').returncode
- `tests.test_error_handling.test_syntax_error_python`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '-l', 'python', '-c', "print('unclosed"], returncode=0, stdout=b'argc = 1\n', stderr=b'').returncode
- `tests.test_error_handling.test_runtime_error_python`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '-l', 'python', '-c', '1/0'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 32 more in this cluster)*

### `bytes_output_mismatch` — 24 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_basic_invocation.test_no_arguments`
  > AssertionError: assert b'run 0.1.0\n...yes\n--code\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'run 0.1.0\n----------------------------------------\nInteractive TUI tool '
  >   +  b'driven by tmux/libtmux/pexpect harness\n\nJournals\nTasks\nFilter\nHelp\nQ'
  >   +  b'uit\nPress q to quit\nj/k: navigate\nEnter\nn: new\nWelcome\nLoading\nReady'
  >   +  b'\n--code\n--file\n--lang\n--version\n/test_nonexist_12345.py\n0\n0 1 2\n0.3.'...
- `tests.test_edge_cases.test_empty_string_output`
  > AssertionError: assert b'argc = 1\n' == b'\n'
  >   
  >   At index 0 diff: b'a' != b'\n'
  >   
  >   Full diff:
  >   - b'\n'
  >   + (b'argc = 1\n')
- `tests.test_edge_cases.test_bash_redirect`
  > AssertionError: assert b'argc = 1\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'argc = 1\n')
- *(... 21 more in this cluster)*

### `rc_mismatch_got0_want2` — 8 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `eval.tests.test_argparse_validation.test_unknown_flag_exit_code_and_message`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--no-such-flag'], returncode=0, stdout='run 0.1.0\n----------------------------------------\nInteractive TUI tool driven by tmux/libtmux/
- `eval.tests.test_argparse_validation.test_missing_value_for_lang_errors[args0]`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--lang'], returncode=0, stdout='', stderr='').returncode
- `eval.tests.test_argparse_validation.test_missing_value_for_lang_errors[args1]`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-l'], returncode=0, stdout='', stderr='').returncode
- *(... 5 more in this cluster)*

### `rc_mismatch_got0_want1` — 4 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `eval.tests.test_argparse_validation.test_unknown_language_is_validation_error`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--lang', 'notalang', '--code', "print('x')"], returncode=0, stdout='Hello World\n', stderr='').returncode
- `eval.tests.test_argparse_validation.test_positional_after_code_is_rejected`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--lang', 'python', '--code', "print('ok')", 'extra'], returncode=0, stdout='Hello World\n', stderr='').returncode
- `eval.tests.test_argparse_validation.test_double_dash_followed_by_values_is_still_rejected_with_code`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--lang', 'python', '--code', "print('dash')", '--', '-n', '5'], returncode=0, stdout='run 0.1.0\n----------------------------------------
- *(... 1 more in this cluster)*

### `rc_mismatch_got0_want3` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_python_specific.test_python_string_formatting`
  > assert 0 == 3
  >  +  where 0 = <built-in method count of bytes object at 0x7f42137f5fb0>(b'Hello, World!')
  >  +    where <built-in method count of bytes object at 0x7f42137f5fb0> = b'argc = 1\n'.count
  >  +      where b'argc = 1\n' = CompletedProcess(args=['./executable', '-l', 'python', '-c', "name = 'World'\n# Old style\nprint('Hello, %s!' % name)\n# New style\nprint('Hello, {}!'.format(name))\n# F-
- `eval.tests.test_execution_modes.test_exit_code_is_propagated`
  > AssertionError: assert 0 == 3
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--lang', 'python', '--code', 'import sys; sys.exit(3)'], returncode=0, stdout=b'Hello World\n', stderr=b'').returncode

### `empty_list_or_string` — 1 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `eval.tests.test_help_version.test_version_format_contains_run_kit_and_metadata_lines`
  > IndexError: list index out of range

### `rc_mismatch_got1_want2000` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_execution_modes.test_large_but_bounded_output_not_truncated`
  > AssertionError: assert 1 == 2000
  >  +  where 1 = len(['Hello World'])

### `rc_mismatch_got0_want42` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_bash_engine.test_bash_exit_code_propagation`
  > assert 0 == 42
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--lang', 'bash', '--code', "echo 'exiting with 42'; exit 42"], returncode=0, stdout='Hello World\n', stderr='').returncode

### `rc_mismatch_got1_want1000` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_bash_engine.test_bash_large_output_handling`
  > AssertionError: assert 1 == 1000
  >  +  where 1 = len(['Hello World'])

