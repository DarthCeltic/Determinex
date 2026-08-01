# Action Sheet — dandavison__delta.acd758f

**Current:** 14.99%  (183/1221)
**Pass / Fail / Skip:** 183 / 468 / 0
**Gap to 100%:** 85.01 percentage points (1038 tests)

## Failure clusters

468 failed tests grouped into 10 buckets (sorted by count).

### `rc_mismatch_got2_want0` — 176 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_argument_parsing.TestBooleanFlags.test_boolean_flags_no_value[--show-syntax-themes]`
  > assert 2 == 0
- `tests.test_argument_parsing.TestBooleanFlags.test_boolean_flags_no_value[--diff-highlight]`
  > assert 2 == 0
- `tests.test_argument_parsing.TestBooleanFlags.test_boolean_flags_no_value[--parse-ansi]`
  > assert 2 == 0
- *(... 173 more in this cluster)*

### `other_assertion` — 159 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_argument_parsing.TestUnknownFlags.test_unknown_long_flag`
  > assert ('unexpected argument' in "delta: unknown option: --nonexistent-flag\nusage: delta [options] [args]\ntry 'delta --help' for more information.\n" or 'error' in "delta: unknown option: --nonexist
  >  +  where "delta: unknown option: --nonexistent-flag\nusage: delta [options] [args]\ntry 'delta --help' for more information.\n" = <built-in method lower of str object at 0x7f4d0e9f75d0>()
  >  +    where <built-in method lower of str object at 0x7f4d0e9f75d0> = "delta: unknown option: --nonexistent-flag\nusage: delta [OPTIONS] [ARGS]\nTry 'delta --help' for more information.\n".lower
  >  +      where "delta: unknown option: --nonexistent-flag\nusage: delta [OPTIONS] [ARGS]\nTry 'delta --help' for more information.\n" = strip_ansi("delta: unknown option: --nonexistent-flag\nusage: del
  >  +  and   "delta: unknown option: --nonexistent-flag\nusage: delta [options] [args]\ntry 'delta --help' for more information.\n" = <built-in method lower of str object at 0x7f4d0e9f75d0>()
  >  +    where <built-in method lower of str object at 0x7f4d0e9f75d0> = "delta: unknown option: --nonexistent-flag\nusage: delta [OPTIONS] [ARGS]\nTry 'delta --help' for more information.\n".lower
  >  +      where "delta: unknown option: --nonexistent-flag\nusage: delta [OPTIONS] [ARGS]\nTry 'delta --help' for more information.\n" = strip_ansi("delta: unknown option: --nonexistent-flag\nusage: del
- `tests.test_argument_parsing.TestFlagsWithIntegerValues.test_integer_flags_missing_value[--max-line-distance]`
  > assert ('value is required' in "delta: unknown option: --max-line-distance\nusage: delta [options] [args]\ntry 'delta --help' for more information.\n" or 'error' in "delta: unknown option: --max-line-
  >  +  where "delta: unknown option: --max-line-distance\nusage: delta [options] [args]\ntry 'delta --help' for more information.\n" = <built-in method lower of str object at 0x7f4d0ea7dc60>()
  >  +    where <built-in method lower of str object at 0x7f4d0ea7dc60> = "delta: unknown option: --max-line-distance\nusage: delta [OPTIONS] [ARGS]\nTry 'delta --help' for more information.\n".lower
  >  +  and   "delta: unknown option: --max-line-distance\nusage: delta [options] [args]\ntry 'delta --help' for more information.\n" = <built-in method lower of str object at 0x7f4d0ea7dc60>()
  >  +    where <built-in method lower of str object at 0x7f4d0ea7dc60> = "delta: unknown option: --max-line-distance\nusage: delta [OPTIONS] [ARGS]\nTry 'delta --help' for more information.\n".lower
- `tests.test_argument_parsing.TestFlagsWithEnumValues.test_enum_flags_invalid_values[--true-color-true]`
  > assert ('invalid value' in "delta: unknown option: --true-color\nusage: delta [options] [args]\ntry 'delta --help' for more information.\n" or 'possible values' in "delta: unknown option: --true-color
  >  +  where "delta: unknown option: --true-color\nusage: delta [options] [args]\ntry 'delta --help' for more information.\n" = <built-in method lower of str object at 0x7f4d0f51f910>()
  >  +    where <built-in method lower of str object at 0x7f4d0f51f910> = "delta: unknown option: --true-color\nusage: delta [OPTIONS] [ARGS]\nTry 'delta --help' for more information.\n".lower
  >  +  and   "delta: unknown option: --true-color\nusage: delta [options] [args]\ntry 'delta --help' for more information.\n" = <built-in method lower of str object at 0x7f4d0f51f910>()
  >  +    where <built-in method lower of str object at 0x7f4d0f51f910> = "delta: unknown option: --true-color\nusage: delta [OPTIONS] [ARGS]\nTry 'delta --help' for more information.\n".lower
- *(... 156 more in this cluster)*

### `bytes_output_mismatch` — 62 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `eval.tests.test_help_version.test_version_exact`
  > AssertionError: assert b'delta 0.1.0\n' == b'delta 0.18.2\n'
  >   
  >   At index 9 diff: b'.' != b'8'
  >   
  >   Full diff:
  >   - (b'delta 0.18.2\n')
  >   ?             - ^
  >   + (b'delta 0.1.0\n')
- `tests.test_bat_output_gaps.test_paging_never_mode`
  > AssertionError: assert b'diff --git ...ed\n line 3\n' == b'\n\x1b[34mf...ne 3\x1b[0m\n'
  >   
  >   At index 0 diff: b'd' != b'\n'
  >   
  >   Full diff:
  >   + (b'diff --git a/file.txt b/file.txt\nindex 1234567..abcdefg 100644\n--- a/fil'
  >   +  b'e.txt\n+++ b/file.txt\n@@ -1,3 +1,3 @@\n line 1\n-line 2\n+line 2 modifie'
  >   +  b'd\n line 3\n')...
- `tests.test_bat_output_gaps.test_paging_always_with_pager_env_var`
  > AssertionError: assert b'diff --git ...ed\n line 3\n' == b'\n\x1b[34mf...ne 3\x1b[0m\n'
  >   
  >   At index 0 diff: b'd' != b'\n'
  >   
  >   Full diff:
  >   + (b'diff --git a/file.txt b/file.txt\nindex 1234567..abcdefg 100644\n--- a/fil'
  >   +  b'e.txt\n+++ b/file.txt\n@@ -1,3 +1,3 @@\n line 1\n-line 2\n+line 2 modifie'
  >   +  b'd\n line 3\n')...
- *(... 59 more in this cluster)*

### `string_output_mismatch` — 32 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_output.test_help_long_baseline_smoke`
  > AssertionError: assert 'delta 0.1.0\...ailing CR\n\n' == 'A viewer for...e delta -h.\n'
  >   
  >   - A viewer for git and diff output
  >   + delta 0.1.0
  >     
  >   - Usage: delta [OPTIONS] [MINUS_FILE] [PLUS_FILE]
  >   + A syntax-highlighting pager for git, diff, and grep output
  >     ...
- `tests.test_diff_stat.test_diff_stat_followed_by_patch`
  > AssertionError: assert 'commit dc9ae...n+even more\n' == 'commit dc9ae...\neven more\n'
  >   
  >     commit dc9ae812538aceb8ec41874d6b68150a7f1b3624
  >     Author: Test User <test@test.com>
  >     Date:   Fri Apr 10 12:14:18 2026 +0000
  >     
  >         Update long path file
  >     ---...
- `tests.test_diff_stat.test_relative_paths_from_src_subdir`
  > AssertionError: assert ' lib/core/ut...sertions(+)\n' == ' ../lib/core...sertions(+)\n'
  >   
  >   -  ../lib/core/util.rs                             | 1 +
  >   -  handlers/module.rs                              | 1 +
  >   +  lib/core/util.rs       | 1 +
  >   +  src/handlers/module.rs | 1 +
  >      2 files changed, 2 insertions(+)
- *(... 29 more in this cluster)*

### `rc_mismatch_got0_want2` — 22 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_argument_parsing.TestUnknownFlags.test_unknown_short_flag`
  > assert 0 == 2
- `tests.test_argument_parsing.TestMutuallyExclusiveFlags.test_dark_and_light_conflict`
  > assert 0 == 2
- `tests.test_argument_parsing.TestMutuallyExclusiveFlags.test_light_and_dark_conflict`
  > assert 0 == 2
- *(... 19 more in this cluster)*

### `rc_mismatch_got2_want1` — 12 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_file_inputs.test_two_file_args_are_treated_as_minus_plus_file_and_exit_1`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--paging=never', '--color-only', '/tmp/pytest-of-root/pytest-0/test_two_file_args_are_treated2/1.txt', '/tmp/pytest-of-root/pytest-0/test
- `tests.test_diff_and_syntect.test_diff_with_ansi_color_styles`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--no-gitconfig', '--minus-style=red', '--plus-style=green', '/workspace/eval/test_resources/test_diff_and_syntect/file1.txt', '/workspace
- `tests.test_diff_and_syntect.test_diff_with_rgb_color_styles`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--no-gitconfig', '--minus-style=#ff0000', '--plus-style=#00ff00', '/workspace/eval/test_resources/test_diff_and_syntect/file1.txt', '/wor
- *(... 9 more in this cluster)*

### `boolean_false` — 2 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_externalized_delta.test_ext_navigate_creates_less_history_file_when_pager_is_less`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = ((PosixPath('/tmp/tmpab8larvk/xdg') / 'delta') / 'lesshst').exists
- `eval.tests.test_color_only_diff.test_color_only_unified_diff_exact_bytes`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of bytes object at 0x7fa54b528030>(b'--- a/file.txt\n+++ b/file.txt\n@@ -1 +1 @@\n')
  >  +    where <built-in method startswith of bytes object at 0x7fa54b528030> = b''.startswith
  >  +      where b'' = CompletedProcess(args=['/workspace/executable', '--color-only'], returncode=0, stdout=b'', stderr=b'').stdout

### `rc_unexpected_zero` — 1 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_subcommand_dispatch.TestUnknownSubcommands.test_invalid_option_value`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '--tabs', 'invalid_number'], returncode=0, stdout=b'', stderr=b'').returncode

### `returned_none` — 1 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_output.test_help_long_has_arguments_section`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7fae04d26680>('^Arguments:\\s*$', 'delta 0.1.0\n\nA syntax-highlighting pager for git, diff, and grep output\n\nUsage: delta [OPTIONS] [ARGS]\n\nOptions:\n  -h, 
  >  +    where <function search at 0x7fae04d26680> = re.search
  >  +    and   'delta 0.1.0\n\nA syntax-highlighting pager for git, diff, and grep output\n\nUsage: delta [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  --no
  >  +    and   re.MULTILINE = re.MULTILINE

### `rc_mismatch_got0_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_grep.test_git_grep_multiple_matches_same_line`
  > AssertionError: assert 0 == 3
  >  +  where 0 = <built-in method count of str object at 0x7ff45843de90>('48;5;28')
  >  +    where <built-in method count of str object at 0x7ff45843de90> = 'multiline_match.rs\x1b[36m:\x1b[m2\x1b[36m:\x1b[m    \x1b[1;31mreturn\x1b[m \x1b[1;31mreturn\x1b[m \x1b[1;31mreturn\x1b[m;\n'.cou

