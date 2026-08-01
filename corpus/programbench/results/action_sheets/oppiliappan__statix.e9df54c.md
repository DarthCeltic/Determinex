# Action Sheet — oppiliappan__statix.e9df54c

**Current:** 24.16%  (267/1105)
**Pass / Fail / Skip:** 267 / 680 / 4
**Gap to 100%:** 75.84 percentage points (838 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_fix.test_fix_ignore_pattern_single_glob`
  - reason: Ignore patterns appear not to function correctly with fix command
- `tests.test_fix.test_fix_ignore_pattern_multiple_globs`
  - reason: Ignore patterns appear not to function correctly with fix command
- `tests.test_fix.test_fix_config_disable_lint`
  - reason: Config file lint disabling appears not to work in current implementation
- `tests.test_fix.test_fix_config_disable_preserves_other_fixes`
  - reason: Config file lint disabling appears not to work in current implementation

## Failure clusters

680 failed tests grouped into 8 buckets (sorted by count).

### `other_assertion` — 316 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_help_output`
  > AssertionError: assert b'USAGE:' in b'statix 0.1.0 - bootstrap scaffold\n\nUsage: statix [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n'
  >  +  where b'statix 0.1.0 - bootstrap scaffold\n\nUsage: statix [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['./executable', '--
- `tests.test_basic_invocation.test_help_short_flag`
  > AssertionError: assert b'USAGE:' in b'statix 0.1.0 - bootstrap scaffold\n\nUsage: statix [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n'
  >  +  where b'statix 0.1.0 - bootstrap scaffold\n\nUsage: statix [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['./executable', '-h
- `tests.test_basic_invocation.test_no_args`
  > assert (b'USAGE:' in b"usage: statix [OPTIONS] [ARGS]\nTry 'statix --help' for more information.\n" or b'required' in b"usage: statix [options] [args]\ntry 'statix --help' for more information.\n")
  >  +  where b"usage: statix [OPTIONS] [ARGS]\nTry 'statix --help' for more information.\n" = CompletedProcess(args=['./executable'], returncode=2, stdout=b'', stderr=b"usage: statix [OPTIONS] [ARGS]\nTr
  >  +  and   b"usage: statix [options] [args]\ntry 'statix --help' for more information.\n" = <built-in method lower of bytes object at 0x7049d0bd5370>()
  >  +    where <built-in method lower of bytes object at 0x7049d0bd5370> = b"usage: statix [OPTIONS] [ARGS]\nTry 'statix --help' for more information.\n".lower
  >  +      where b"usage: statix [OPTIONS] [ARGS]\nTry 'statix --help' for more information.\n" = CompletedProcess(args=['./executable'], returncode=2, stdout=b'', stderr=b"usage: statix [OPTIONS] [ARGS]
- *(... 313 more in this cluster)*

### `string_output_mismatch` — 194 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_fix_subcommand.test_fix_in_place`
  > AssertionError: assert 'if x then' in 'if x == true then 0 else 1\n'
- `tests.test_fix_subcommand.test_fix_in_place`
  > AssertionError: assert 'if x then 0 else 1' in 'if x == true then 0 else 1'
- `tests.test_fix_subcommand.test_fix_directory_recursive`
  > AssertionError: assert '== true' not in 'if x == true then 0 else 1'
  >   
  >   '== true' is contained here:
  >     if x == true then 0 else 1
  >   ?      +++++++
- *(... 191 more in this cluster)*

### `rc_mismatch_got0_want1` — 115 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_additional_lints.test_output_format_differences`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', 'check', '/tmp/tmppkqzvc8n/test.nix', '--format', 'stderr'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_check_subcommand.test_check_bool_comparison_lint`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', 'check', '/tmp/tmp0b14wyag/test.nix'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_check_subcommand.test_check_empty_let_in`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', 'check', '/tmp/tmpoyy_ziqw/test.nix'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 112 more in this cluster)*

### `rc_mismatch_got0_want2` — 26 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_config.test_config_parse_invalid_position_format`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['./executable', 'single', '/workspace/eval/test_resources/test_config/single_test.nix', '--position', 'invalid'], returncode=0, stdout='', stderr='').returncode
- `tests.test_errors.test_unknown_flag`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['./executable', 'check', '--unknown-flag'], returncode=0, stdout='', stderr='').returncode
- `tests.test_errors.test_invalid_position_format_single_fix`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['./executable', 'single', '-p', 'invalid', 'dummy.nix'], returncode=0, stdout='', stderr='').returncode
- *(... 23 more in this cluster)*

### `rc_unexpected_zero` — 21 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_basic_invocation.test_invalid_subcommand`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'invalid_subcommand'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_dump_subcommand.test_dump_no_extra_args`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'dump', 'extra'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_explain_subcommand.test_explain_no_args`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'explain'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 18 more in this cluster)*

### `rc_mismatch_got0_want101` — 5 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_errors.test_empty_file`
  > AssertionError: assert 0 == 101
  >  +  where 0 = CompletedProcess(args=['./executable', 'check', '/tmp/tmppwytxy3a/empty.nix'], returncode=0, stdout='', stderr='').returncode
- `tests.test_errors.test_streaming_mode_empty_stdin`
  > AssertionError: assert 0 == 101
  >  +  where 0 = CompletedProcess(args=['./executable', 'check', '-s'], returncode=0, stdout='', stderr='').returncode
- `tests.test_errors.test_streaming_mode_binary_data_non_utf8`
  > AssertionError: assert 0 == 101
  >  +  where 0 = CompletedProcess(args=['./executable', 'check', '-s'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 2 more in this cluster)*

### `returned_none` — 2 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_main.test_help_lists_expected_subcommands`
  > AssertionError: assert None
  >  +  where None = <function search at 0x72649171a680>('^\\s*check\\b', 'statix 0.1.0 - bootstrap scaffold\n\nUsage: statix [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Pr
  >  +    where <function search at 0x72649171a680> = re.search
  >  +    and   re.MULTILINE = re.M
- `eval.tests.test_help_main.test_version_line_present_but_not_asserted_exact`
  > AssertionError: assert None
  >  +  where None = <function match at 0x7264916c6170>('^statix\\s+\\d+\\.\\d+\\.\\d+\\s*$', 'statix 0.1.0 - bootstrap scaffold')
  >  +    where <function match at 0x7264916c6170> = re.match

### `boolean_false` — 1 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_errors.test_very_long_file_path`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x77bb90890030>('config error: path error: file not found:')
  >  +    where <built-in method startswith of str object at 0x77bb90890030> = ''.startswith

