# Action Sheet — sigoden__argc.04a08f1

**Current:** 6.3%  (69/1095)
**Pass / Fail / Skip:** 69 / 597 / 34
**Gap to 100%:** 93.70 percentage points (1026 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_harvest.test_compgen_arg_terminated`
  - reason: Compgen tests require library-level testing, not CLI
- `tests.test_harvest.test_compgen_assign_option_value`
  - reason: Compgen tests require library-level testing, not CLI
- `tests.test_harvest.test_compgen_auto_alias_subcommand`
  - reason: Compgen tests require library-level testing, not CLI
- `tests.test_harvest.test_compgen_bash_shell`
  - reason: Compgen tests require library-level testing, not CLI
- `tests.test_harvest.test_compgen_break_chars_bash`
  - reason: Compgen tests require library-level testing, not CLI
- *(... 29 more skipped)*

## Failure clusters

597 failed tests grouped into 7 buckets (sorted by count).

### `rc_mismatch_got2_want0` — 303 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_build.test_build_to_stdout_simple`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--argc-build', '/workspace/eval/test_resources/test_build/simple.sh'], returncode=2, stdout='', stderr="argc: unknown option: --argc-buil
- `tests.test_build.test_build_to_stdout_subcommands`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--argc-build', '/workspace/eval/test_resources/test_build/subcommands.sh'], returncode=2, stdout='', stderr="argc: unknown option: --argc
- `tests.test_build.test_build_to_file_creates_executable`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--argc-build', '/workspace/eval/test_resources/test_build/simple.sh', '/tmp/tmp2_ufvopj/built_script.sh'], returncode=2, stdout='', stder
- *(... 300 more in this cluster)*

### `other_assertion` — 246 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_build.test_built_script_syntactic_validity`
  > AssertionError: simple.sh build failed: argc: unknown option: --argc-build
  >   usage: argc [OPTIONS] [ARGS]
  >   Try 'argc --help' for more information.
  >   
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--argc-build', '/workspace/eval/test_resources/test_build/simple.sh'], returncode=2, stdout='', stderr="argc: unknown option: --argc-buil
- `tests.test_completions.test_bash_completions_structure`
  > AssertionError: argc: unknown option: --argc-completions
  >   usage: argc [OPTIONS] [ARGS]
  >   Try 'argc --help' for more information.
  >   
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--argc-completions', 'bash', '/workspace/eval/test_resources/test_completions/simple.sh'], returncode=2, stdout='', stderr="argc: unknown
- `tests.test_completions.test_zsh_completions_structure`
  > AssertionError: argc: unknown option: --argc-completions
  >   usage: argc [OPTIONS] [ARGS]
  >   Try 'argc --help' for more information.
  >   
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--argc-completions', 'zsh', '/workspace/eval/test_resources/test_completions/simple.sh'], returncode=2, stdout='', stderr="argc: unknown 
- *(... 243 more in this cluster)*

### `string_output_mismatch` — 28 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_build.test_build_error_invalid_script`
  > AssertionError: assert 'argc: unknow...nformation.\n' == 'syntax error at line 3\n'
  >   
  >   - syntax error at line 3
  >   + argc: unknown option: --argc-build
  >   + usage: argc [OPTIONS] [ARGS]
  >   + Try 'argc --help' for more information.
- `tests.test_build.test_build_nonexistent_file`
  > AssertionError: assert 'argc: unknow...nformation.\n' == 'Failed to lo...os error 2)\n'
  >   
  >   + argc: unknown option: --argc-build
  >   + usage: argc [OPTIONS] [ARGS]
  >   + Try 'argc --help' for more information.
  >   - Failed to load script at '/nonexistent/file.sh'
  >   - 
  >   - Caused by:
- `tests.test_create_run.test_argc_run_syntax_error_in_script`
  > assert 'argc: unknow...nformation.\n' == 'syntax_error...end of file\n'
  >   
  >   - syntax_error.sh: line 9: unexpected EOF while looking for matching `"'
  >   - syntax_error.sh: line 10: syntax error: unexpected end of file
  >   + argc: unknown option: --argc-run
  >   + usage: argc [OPTIONS] [ARGS]
  >   + Try 'argc --help' for more information.
- *(... 25 more in this cluster)*

### `rc_mismatch_got2_want1` — 17 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_completions.test_completions_invalid_shell`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--argc-completions', 'invalid', '/workspace/examples/demo.sh'], returncode=2, stdout='', stderr="argc: unknown option: --argc-completions
- `tests.test_create_run.test_argc_create_file_already_exists`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--argc-create'], returncode=2, stdout='', stderr="argc: unknown option: --argc-create\nusage: argc [OPTIONS] [ARGS]\nTry 'argc --help' fo
- `tests.test_create_run.test_argc_run_no_script_provided`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--argc-run'], returncode=2, stdout='', stderr="argc: unknown option: --argc-run\nusage: argc [OPTIONS] [ARGS]\nTry 'argc --help' for more
- *(... 14 more in this cluster)*

### `rc_mismatch_got2_want127` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_create_run.test_argc_run_script_not_found`
  > assert 2 == 127
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--argc-run', '/tmp/nonexistent.sh'], returncode=2, stdout='', stderr="argc: unknown option: --argc-run\nusage: argc [OPTIONS] [ARGS]\nTry

### `bytes_output_mismatch` — 1 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_harvest.test_env_missing`
  > AssertionError: assert 'argc: unknow... information.' == 'error: the f...d:\n  TEST_EB'
  >   
  >   - error: the following required environments were not provided:
  >   -   TEST_EB
  >   + argc: unknown option: --argc-eval
  >   + usage: argc [OPTIONS] [ARGS]
  >   + Try 'argc --help' for more information.

### `rc_mismatch_got0_want1` — 1 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_cli.test_unknown_command_with_no_argcfile`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'unknown-command'], returncode=0, stdout='', stderr='').returncode

