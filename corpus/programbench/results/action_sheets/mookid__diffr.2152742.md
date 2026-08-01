# Action Sheet — mookid__diffr.2152742

**Current:** 13.53%  (151/1116)
**Pass / Fail / Skip:** 151 / 631 / 0
**Gap to 100%:** 86.47 percentage points (965 tests)

## Failure clusters

631 failed tests grouped into 9 buckets (sorted by count).

### `rc_mismatch_got2_want0` — 391 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_basic.test_no_args_no_stdin`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable'], returncode=2, stdout=b'diffr 0.1.0\nA diff tool with color support\n\nUSAGE:\n    diffr [OPTIONS] [<file1> <file2>]\n\nOPTIONS:\n    -h, --help   
- `tests.test_debug_hidden.test_all_flags_combined`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--debug', '--line-numbers', 'compact', '--colors', 'added:bold', '--large-diff-threshold', '500'], returncode=2, stdout=b'', stderr=b"error: [Errn
- `tests.test_diff_processing.test_simple_diff`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable'], returncode=2, stdout=b'diffr 0.1.0\nA diff tool with color support\n\nUSAGE:\n    diffr [OPTIONS] [<file1> <file2>]\n\nOPTIONS:\n    -h, --help   
- *(... 388 more in this cluster)*

### `other_assertion` — 115 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic.test_version_short`
  > AssertionError: assert b'diffr' in b''
  >  +  where b'' = CompletedProcess(args=['./executable', '-V'], returncode=0, stdout=b'0.1.0\n', stderr=b'').stderr
- `tests.test_basic.test_version_long`
  > AssertionError: assert b'diffr' in b''
  >  +  where b'' = CompletedProcess(args=['./executable', '--version'], returncode=0, stdout=b'0.1.0\n', stderr=b'').stderr
- `tests.test_basic.test_help_short`
  > AssertionError: assert b'Nathan Moreau' in b'diffr 0.1.0\nA diff tool with color support\n\nUSAGE:\n    diffr [OPTIONS] [<file1> <file2>]\n\nOPTIONS:\n    -h, --help       Print help information\n    
  >  +  where b'diffr 0.1.0\nA diff tool with color support\n\nUSAGE:\n    diffr [OPTIONS] [<file1> <file2>]\n\nOPTIONS:\n    -h, --help       Print help information\n    -V, --version    Print version in
- *(... 112 more in this cluster)*

### `bytes_output_mismatch` — 54 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_cli_args.test_colors_added_foreground_blue`
  > AssertionError: assert b'--- a/test....erse\n- foo\n' == b'\x1b[0m--- ... foo\x1b[0m\n'
  >   
  >   At index 0 diff: b'-' != b'\x1b'
  >   
  >   Full diff:
  >   + (b'--- a/test.txt\n+++ b/test.txt\n@@ -1,7 +0,0 @@\n---- a/test.txt\n-+++ b/tes'
  >   +  b't.txt\n-@@ -1,3 +1,3 @@\n- hello\n--world\n-+universe\n- foo\n')
  >   - (b'\x1b[0m--- a/test.txt\x1b[0m\n\x1b[0m+++ b/test.txt\x1b[0m\n\x1b[0m@@ -1,'...
- `tests.test_cli_args.test_colors_added_background_yellow`
  > AssertionError: assert b'--- a/test....erse\n- foo\n' == b'\x1b[0m--- ... foo\x1b[0m\n'
  >   
  >   At index 0 diff: b'-' != b'\x1b'
  >   
  >   Full diff:
  >   + (b'--- a/test.txt\n+++ b/test.txt\n@@ -1,7 +0,0 @@\n---- a/test.txt\n-+++ b/tes'
  >   +  b't.txt\n-@@ -1,3 +1,3 @@\n- hello\n--world\n-+universe\n- foo\n')
  >   - (b'\x1b[0m--- a/test.txt\x1b[0m\n\x1b[0m+++ b/test.txt\x1b[0m\n\x1b[0m@@ -1,'...
- `tests.test_cli_args.test_colors_added_bold`
  > AssertionError: assert b'--- a/test....erse\n- foo\n' == b'\x1b[0m--- ... foo\x1b[0m\n'
  >   
  >   At index 0 diff: b'-' != b'\x1b'
  >   
  >   Full diff:
  >   + (b'--- a/test.txt\n+++ b/test.txt\n@@ -1,7 +0,0 @@\n---- a/test.txt\n-+++ b/tes'
  >   +  b't.txt\n-@@ -1,3 +1,3 @@\n- hello\n--world\n-+universe\n- foo\n')
  >   - (b'\x1b[0m--- a/test.txt\x1b[0m\n\x1b[0m+++ b/test.txt\x1b[0m\n\x1b[0m@@ -1,'...
- *(... 51 more in this cluster)*

### `rc_unexpected_zero` — 36 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_colors.test_colors_invalid_face_name`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '--colors', 'notafacename'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_colors.test_colors_ansi_256_invalid`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '--colors', 'added:foreground:256'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_colors.test_colors_rgb_invalid`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '--colors', 'added:foreground:256,0,0'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 33 more in this cluster)*

### `rc_mismatch_got0_want255` — 22 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_args.test_invalid_face_name`
  > AssertionError: assert 0 == 255
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--colors', 'invalid-face:foreground:red'], returncode=0, stdout=b'--- a/test.txt\n+++ b/test.txt\n@@ -1 +0,0 @@\n-test\n', stderr=b'').re
- `tests.test_cli_args.test_invalid_attribute_name`
  > AssertionError: assert 0 == 255
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--colors', 'added:invalid-attr:red'], returncode=0, stdout=b'--- a/test.txt\n+++ b/test.txt\n@@ -1 +0,0 @@\n-test\n', stderr=b'').returnc
- `tests.test_cli_args.test_invalid_color_value`
  > AssertionError: assert 0 == 255
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--colors', 'added:foreground:invalid-color'], returncode=0, stdout=b'--- a/test.txt\n+++ b/test.txt\n@@ -1 +0,0 @@\n-test\n', stderr=b'')
- *(... 19 more in this cluster)*

### `string_output_mismatch` — 5 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_harvest.test_cli_threshold`
  > assert 'error: --lar...uires a value' == "option requi...ff-threshold'"
  >   
  >   - option requires an argument: '--large-diff-threshold'
  >   + error: --large-diff-threshold requires a value
- `eval.tests.test_help_output.test_baseline_full_help_output_matches_fixture`
  > AssertionError: assert 'diffr 0.1.0\...large diffs\n' == 'diffr 0.1.5\...information\n'
  >   
  >   - diffr 0.1.5
  >   ?           ^
  >   + diffr 0.1.0
  >   ?           ^
  >   + A diff tool with color support
  >   - Nathan Moreau <nathan.moreau@m4x.org>...
- `eval.tests.test_external_cli.test_ext_threshold_missing_arg`
  > assert 'error: --lar...uires a value' == "option requi...ff-threshold'"
  >   
  >   - option requires an argument: '--large-diff-threshold'
  >   + error: --large-diff-threshold requires a value
- *(... 2 more in this cluster)*

### `boolean_false` — 5 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_harvest.test_cli_bad_argument`
  > assert False
  >  +  where False = <built-in method startswith of str object at 0x7f13314e32f0>("bad argument: '--invalid-option'")
  >  +    where <built-in method startswith of str object at 0x7f13314e32f0> = "error: unexpected argument '--invalid-option' found".startswith
- `eval.tests.test_diffr_io.test_line_numbers_flag_adds_numbers_to_changed_lines`
  > assert False
  >  +  where False = any(<generator object test_line_numbers_flag_adds_numbers_to_changed_lines.<locals>.<genexpr> at 0x7f3439e1c350>)
- `eval.tests.test_external_app_and_lib.test_ext_parse_line_number_with_escapes_via_line_numbers_flag`
  > assert False
  >  +  where False = any(<generator object test_ext_parse_line_number_with_escapes_via_line_numbers_flag.<locals>.<genexpr> at 0x7f6364d4d0e0>)
- *(... 2 more in this cluster)*

### `rc_mismatch_got2_want255` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_args.test_invalid_line_number_style`
  > assert 2 == 255
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--line-numbers', 'invalid-style'], returncode=2, stdout=b'', stderr=b"error: [Errno 2] No such file or directory: 'invalid-style'\n").ret
- `tests.test_cli_args.test_invalid_large_diff_threshold_non_numeric`
  > AssertionError: assert 2 == 255
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--large-diff-threshold', 'abc'], returncode=2, stdout=b'', stderr=b'error: invalid threshold value\n').returncode

### `rc_mismatch_got0_want2` — 1 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `eval.tests.test_diffr_io.test_file_argument_is_rejected_as_bad_argument_exit_zero`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/tmp/pytest-of-root/pytest-0/test_file_argument_is_rejected2/in.diff'], returncode=0, stdout=b'--- a/test.txt\n+++ b/test.txt\n@@ -0,0 +1

