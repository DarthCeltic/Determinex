# Action Sheet — hush-shell__hush.560c33a

**Current:** 2.6%  (42/1615)
**Pass / Fail / Skip:** 42 / 897 / 0
**Gap to 100%:** 97.40 percentage points (1573 tests)

## Failure clusters

897 failed tests grouped into 14 buckets (sorted by count).

### `rc_mismatch_got2_want0` — 525 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_advanced_features.test_command_with_arguments_interpolation`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable'], returncode=2, stdout=b'', stderr=b'usage: hush [OPTIONS] [ARGS]\n').returncode
- `tests.test_advanced_features.test_command_with_escape_sequences`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable'], returncode=2, stdout=b'', stderr=b'usage: hush [OPTIONS] [ARGS]\n').returncode
- `tests.test_advanced_features.test_nested_function_calls`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable'], returncode=2, stdout=b'', stderr=b'usage: hush [OPTIONS] [ARGS]\n').returncode
- *(... 522 more in this cluster)*

### `other_assertion` — 153 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_help_flag`
  > AssertionError: assert b'Hush' in b'hush 0.1.0\n\nusage: hush [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --verbose  Verbose\n  -q, --quiet    Quie
  >  +  where b'hush 0.1.0\n\nusage: hush [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --verbose  Verbose\n  -q, --quiet    Quiet\n' = CompletedProcess(
- `tests.test_basic_invocation.test_help_short_flag`
  > AssertionError: assert b'Hush' in b'hush 0.1.0\n\nusage: hush [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --verbose  Verbose\n  -q, --quiet    Quie
  >  +  where b'hush 0.1.0\n\nusage: hush [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --verbose  Verbose\n  -q, --quiet    Quiet\n' = CompletedProcess(
- `tests.test_basic_invocation.test_version_flag`
  > AssertionError: assert b'Hush' in b'hush 0.1.0\n'
  >  +  where b'hush 0.1.0\n' = CompletedProcess(args=['./executable', '--version'], returncode=0, stdout=b'hush 0.1.0\n', stderr=b'').stdout
- *(... 150 more in this cluster)*

### `rc_mismatch_got126_want0` — 103 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_error_formatting.test_command_with_redirect`
  > AssertionError: assert 126 == 0
  >  +  where 126 = CompletedProcess(args=['./executable', '/tmp/tmpki9mx4r8/test.hsh'], returncode=126, stdout=b'', stderr=b'hush: error: /tmp/tmpki9mx4r8/test.hsh: Permission denied\n').returncode
- `tests.test_file_input.test_script_file_execution`
  > AssertionError: assert 126 == 0
  >  +  where 126 = CompletedProcess(args=['./executable', '/tmp/tmpccmpwe1u/test.hsh'], returncode=126, stdout=b'', stderr=b'hush: error: /tmp/tmpccmpwe1u/test.hsh: Permission denied\n').returncode
- `tests.test_file_input.test_script_with_multiple_lines`
  > AssertionError: assert 126 == 0
  >  +  where 126 = CompletedProcess(args=['./executable', '/tmp/tmp2wlbbd_9/multi.hsh'], returncode=126, stdout=b'', stderr=b'hush: error: /tmp/tmp2wlbbd_9/multi.hsh: Permission denied\n').returncode
- *(... 100 more in this cluster)*

### `string_output_mismatch` — 42 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_ast_formatting.test_try_operator_ast`
  > assert '' == '------------...-----------\n'
  >   
  >   - --------------------------------------------------
  >   - AST for <stdin>
  >   - let test = function()
  >   - 	let result = (std.int("not a number") ?)
  >   - 	std.println(result)
  >   - end
- `tests.test_ast_formatting.test_command_block_types_ast`
  > assert '' == '------------...-----------\n'
  >   
  >   - --------------------------------------------------
  >   - AST for <stdin>
  >   - let sync = {
  >   - 	"echo" "hello";
  >   - 	"echo" "world"
  >   - }...
- `tests.test_ast_formatting.test_commands_with_pipes_and_redirections_ast`
  > assert '' == '------------...-----------\n'
  >   
  >   - --------------------------------------------------
  >   - AST for <stdin>
  >   - let output = ${
  >   - 	"echo" "test" | "cat"
  >   - }
  >   - let redir = ${...
- *(... 39 more in this cluster)*

### `rc_mismatch_got2_want127` — 36 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_edge_cases.test_accessing_missing_table_field`
  > AssertionError: assert 2 == 127
  >  +  where 2 = CompletedProcess(args=['./executable'], returncode=2, stdout=b'', stderr=b'usage: hush [OPTIONS] [ARGS]\n').returncode
- `tests.test_error_conditions.test_type_error_int_float_mix`
  > AssertionError: assert 2 == 127
  >  +  where 2 = CompletedProcess(args=['./executable'], returncode=2, stdout=b'', stderr=b'usage: hush [OPTIONS] [ARGS]\n').returncode
- `tests.test_error_conditions.test_type_error_string_number`
  > AssertionError: assert 2 == 127
  >  +  where 2 = CompletedProcess(args=['./executable'], returncode=2, stdout=b'', stderr=b'usage: hush [OPTIONS] [ARGS]\n').returncode
- *(... 33 more in this cluster)*

### `rc_mismatch_got127_want0` — 7 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_stdin_dash_argument`
  > AssertionError: assert 127 == 0
  >  +  where 127 = CompletedProcess(args=['./executable', '-'], returncode=127, stdout=b'', stderr=b'hush: error: -: command not found\n').returncode
- `tests.test_file_input.test_nonexistent_file_as_argument`
  > AssertionError: assert 127 == 0
  >  +  where 127 = CompletedProcess(args=['./executable', '/nonexistent/script.hsh'], returncode=127, stdout=b'', stderr=b'hush: error: /nonexistent/script.hsh: command not found\n').returncode
- `tests.test_cli.test_dash_stdin_explicit`
  > AssertionError: assert 127 == 0
  >  +  where 127 = CompletedProcess(args=['/workspace/executable', '-'], returncode=127, stdout='', stderr='hush: error: -: command not found\n').returncode
- *(... 4 more in this cluster)*

### `rc_mismatch_got2_want1` — 7 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_invalid_flag`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['./executable', '--invalid-flag-xyz'], returncode=2, stdout=b'', stderr=b'usage: hush [OPTIONS] [ARGS]\n').returncode
- `tests.test_cli.test_unknown_flag_rejected`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--unknown-flag'], returncode=2, stdout='', stderr='usage: hush [OPTIONS] [ARGS]\n').returncode
- `tests.test_cli.test_multiple_identical_flags`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--lex', '--lex'], returncode=2, stdout='', stderr='usage: hush [OPTIONS] [ARGS]\n').returncode
- *(... 4 more in this cluster)*

### `rc_mismatch_got126_want127` — 6 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_commands.test_nested_array_interpolation_error`
  > AssertionError: assert 126 == 127
  >  +  where 126 = CompletedProcess(args=['/workspace/executable', '/workspace/eval/test_resources/test_commands/nested_array.hsh'], returncode=126, stdout='', stderr='hush: error: /workspace/eval/test_r
- `tests.test_control_flow.test_non_boolean_condition_panics`
  > AssertionError: assert 126 == 127
  >  +  where 126 = CompletedProcess(args=['/workspace/executable', '/workspace/eval/test_resources/test_control_flow/non_bool_condition.hsh'], returncode=126, stdout='', stderr='hush: error: /workspace/e
- `tests.test_control_flow.test_iter_on_non_iterable_type_panics`
  > AssertionError: assert 126 == 127
  >  +  where 126 = CompletedProcess(args=['/workspace/executable', '/workspace/eval/test_resources/test_control_flow/iter_non_iterable.hsh'], returncode=126, stdout='', stderr='hush: error: /workspace/ev
- *(... 3 more in this cluster)*

### `rc_mismatch_got126_want2` — 5 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_file_input.test_script_with_syntax_error`
  > AssertionError: assert 126 == 2
  >  +  where 126 = CompletedProcess(args=['./executable', '/tmp/tmp65_pqsf6/syntax_error.hsh'], returncode=126, stdout=b'', stderr=b'hush: error: /tmp/tmp65_pqsf6/syntax_error.hsh: Permission denied\n').
- `tests.test_cli.test_file_with_syntax_error_exit_2`
  > AssertionError: assert 126 == 2
  >  +  where 126 = CompletedProcess(args=['/workspace/executable', '/workspace/eval/test_resources/test_cli/syntax_error.hsh'], returncode=126, stdout='', stderr='hush: error: /workspace/eval/test_resour
- `tests.test_cli.test_multiple_semantic_errors_all_reported`
  > AssertionError: assert 126 == 2
  >  +  where 126 = CompletedProcess(args=['/workspace/executable', '/workspace/eval/test_resources/test_cli/multiline_error.hsh'], returncode=126, stdout='', stderr='hush: error: /workspace/eval/test_res
- *(... 2 more in this cluster)*

### `rc_mismatch_got0_want2` — 5 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_flags.test_check_flag_static_error`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['./executable', '--check'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_cli.test_check_mode_syntax_error_exit_2`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--check'], returncode=0, stdout='', stderr='').returncode
- `tests.test_cli.test_check_mode_semantic_error_exit_2`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--check'], returncode=0, stdout='', stderr='').returncode
- *(... 2 more in this cluster)*

### `bytes_output_mismatch` — 4 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_errors.test_multichar_literal`
  > assert 'usage: hush ...ONS] [ARGS]\n' == "Error: <stdi...pected 'b'.\n"
  >   
  >   - Error: <stdin> (line 1, column 10) - unexpected 'b'.
  >   + usage: hush [OPTIONS] [ARGS]
- `eval.tests.test_executable_behavior.test_help_exact_output`
  > AssertionError: assert b'hush 0.1.0\...et    Quiet\n' == b'Hush 0.1.4\...r arguments\n'
  >   
  >   At index 0 diff: b'h' != b'H'
  >   
  >   Full diff:
  >   + (b'hush 0.1.0\n\nusage: hush [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     '
  >   +  b'Print help\n  -V, --version  Print version\n  -v, --verbose  Verbose\n  -q,'
  >   +  b' --quiet    Quiet\n')...
- `eval.tests.test_executable_behavior.test_version_exact_output`
  > AssertionError: assert b'hush 0.1.0\n' == b'Hush 0.1.4\n'
  >   
  >   At index 0 diff: b'h' != b'H'
  >   
  >   Full diff:
  >   - (b'Hush 0.1.4\n')
  >   ?    ^        ^
  >   + (b'hush 0.1.0\n')
- *(... 1 more in this cluster)*

### `rc_unexpected_zero` — 2 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_error_formatting.test_check_flag_invalid_syntax`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '--check'], returncode=0, stdout=b'', stderr=b'').returncode
- `eval.tests.test_hush_externalized.test_ext_semantic_test_negative_dir`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--check', '/workspace/src/semantic/tests/data/negative/async-builtin-1.hsh'], returncode=0, stdout=b'', stderr=b'').returncode

### `returned_none` — 1 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_usage.test_usage_line_format`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f2f8466a680>('^USAGE:\\n\\s+executable \\[FLAGS\\] \\[arguments\\]\\.\\.\\.\\s*$', 'hush 0.1.0\n\nusage: hush [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Pri
  >  +    where <function search at 0x7f2f8466a680> = re.search
  >  +    and   re.MULTILINE = re.M

### `boolean_false` — 1 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_subcommand_dispatch.TestUnknownCommandHandling.test_unknown_flag_produces_error`
  > assert False
  >  +  where False = any(<generator object TestUnknownCommandHandling.test_unknown_flag_produces_error.<locals>.<genexpr> at 0x7f391ee19690>)

