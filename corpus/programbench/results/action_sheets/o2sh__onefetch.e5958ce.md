# Action Sheet — o2sh__onefetch.e5958ce

**Current:** 4.3%  (57/1325)
**Pass / Fail / Skip:** 57 / 621 / 2
**Gap to 100%:** 95.70 percentage points (1268 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_onefetch_cli.test_version_prints_semver`
  - reason: test_version_prints_semver depends on test_help_contains_sections
- `tests.test_executable_externalized.test_ext_repo_with_pre_epoch_dates_runs_successfully_skip_known_fixture_breakage`
  - reason: Original fixture make_pre_epoch_repo.sh relies on GNU patch format; fails in this environment

## Failure clusters

621 failed tests grouped into 9 buckets (sorted by count).

### `rc_mismatch_got2_want0` — 358 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_ascii.test_ascii_input_custom_string`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '/tmp/tmp65435u5t/test_repo', '--ascii-input', 'CUSTOM\nASCII\nART'], returncode=2, stdout=b'', stderr=b"onefetch: unknown option: --ascii
- `tests.test_ascii.test_ascii_colors_single`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '/tmp/tmpfx220b9v/test_repo', '--ascii-colors', '5'], returncode=2, stdout=b'', stderr=b"onefetch: unknown option: --ascii-colors\nusage: 
- `tests.test_ascii.test_ascii_colors_multiple`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '/tmp/tmp_e2n__bt/test_repo', '--ascii-colors', '1', '2', '3'], returncode=2, stdout=b'', stderr=b"onefetch: unknown option: --ascii-color
- *(... 355 more in this cluster)*

### `other_assertion` — 227 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic.test_help_flag`
  > AssertionError: assert b'Command-line Git information tool' in b'onefetch 0.1.0 - bootstrap scaffold\n\nUsage: onefetch [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Prin
  >  +  where b'onefetch 0.1.0 - bootstrap scaffold\n\nUsage: onefetch [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['/workspace/exe
- `tests.test_basic.test_help_short_flag`
  > AssertionError: assert b'Command-line Git information tool' in b'onefetch 0.1.0 - bootstrap scaffold\n\nUsage: onefetch [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Prin
  >  +  where b'onefetch 0.1.0 - bootstrap scaffold\n\nUsage: onefetch [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['/workspace/exe
- `tests.test_basic.test_invalid_flag`
  > assert (b'error:' in b"onefetch: unknown option: --invalid-flag-xyz\nusage: onefetch [options] [args]\ntry 'onefetch --help' for more information.\n" or b'unrecognized' in b"onefetch: unknown option: 
  >  +  where b"onefetch: unknown option: --invalid-flag-xyz\nusage: onefetch [options] [args]\ntry 'onefetch --help' for more information.\n" = <built-in method lower of bytes object at 0x7fba08824670>()
  >  +    where <built-in method lower of bytes object at 0x7fba08824670> = b"onefetch: unknown option: --invalid-flag-xyz\nusage: onefetch [OPTIONS] [ARGS]\nTry 'onefetch --help' for more information.\n"
  >  +      where b"onefetch: unknown option: --invalid-flag-xyz\nusage: onefetch [OPTIONS] [ARGS]\nTry 'onefetch --help' for more information.\n" = CompletedProcess(args=['/workspace/executable', '--inva
  >  +  and   b"onefetch: unknown option: --invalid-flag-xyz\nusage: onefetch [options] [args]\ntry 'onefetch --help' for more information.\n" = <built-in method lower of bytes object at 0x7fba08824670>()
  >  +    where <built-in method lower of bytes object at 0x7fba08824670> = b"onefetch: unknown option: --invalid-flag-xyz\nusage: onefetch [OPTIONS] [ARGS]\nTry 'onefetch --help' for more information.\n"
  >  +      where b"onefetch: unknown option: --invalid-flag-xyz\nusage: onefetch [OPTIONS] [ARGS]\nTry 'onefetch --help' for more information.\n" = CompletedProcess(args=['/workspace/executable', '--inva
- *(... 224 more in this cluster)*

### `string_output_mismatch` — 22 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_cli_flags.test_version_flag_exact_format`
  > AssertionError: assert 'onefetch 0.1.0\n' == 'onefetch 2.25.0\n'
  >   
  >   - onefetch 2.25.0
  >   ?          ^ ^^
  >   + onefetch 0.1.0
  >   ?          ^ ^
- `tests.test_cli_gaps.test_invalid_regex_no_bots`
  > assert 'onefetch: un...nformation.\n' == "error: inval...y '--help'.\n"
  >   
  >   + onefetch: unknown option: --no-bots=[invalid
  >   + usage: onefetch [OPTIONS] [ARGS]
  >   + Try 'onefetch --help' for more information.
  >   - error: invalid value '[invalid' for '--no-bots[=<REGEX>]': regex parse error:
  >   -     [invalid
  >   -     ^...
- `tests.test_cli_gaps.test_generate_invalid_shell`
  > assert 'onefetch: un...nformation.\n' == "error: inval...y '--help'.\n"
  >   
  >   + onefetch: unknown option: --generate
  >   + usage: onefetch [OPTIONS] [ARGS]
  >   + Try 'onefetch --help' for more information.
  >   - error: invalid value 'invalid' for '--generate <SHELL>'
  >   -   [possible values: bash, elvish, fish, powershell, zsh]
  >   - 
- *(... 19 more in this cluster)*

### `rc_unexpected_zero` — 9 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_basic.test_nonexistent_directory`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/path/that/does/not/exist/xyz123'], returncode=0, stdout=b'', stderr=b"error: '/path/that/does/not/exist/xyz123' is not a git repository\
- `tests.test_edge_cases.test_non_git_directory`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/tmp/tmpij37jj57/non_git'], returncode=0, stdout=b'', stderr=b"error: '/tmp/tmpij37jj57/non_git' is not a git repository\n").returncode
- `tests.test_edge_cases.test_bare_repository`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/tmp/tmpfhtbm4oe/bare_repo'], returncode=0, stdout=b"    _ __   ___  _ __   ___ _ __\n   | '_ \\ / _ \\| '_ \\ / _ \\ '__|\n   | | | | (_
- *(... 6 more in this cluster)*

### `returned_none` — 1 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_output.test_help_has_arguments_section`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7fdfd312a680>('^Arguments:\\s*$', 'onefetch 0.1.0 - bootstrap scaffold\n\nUsage: onefetch [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --vers
  >  +    where <function search at 0x7fdfd312a680> = re.search
  >  +    and   'onefetch 0.1.0 - bootstrap scaffold\n\nUsage: onefetch [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['/workspace/ex
  >  +    and   re.MULTILINE = re.MULTILINE

### `bytes_output_mismatch` — 1 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `eval.tests.test_help_output.test_help_matches_saved_baseline`
  > AssertionError: assert b'onefetch 0....int version\n' == b'Command-lin...ge managers\n'
  >   
  >   At index 0 diff: b'o' != b'C'
  >   
  >   Full diff:
  >   + (b'onefetch 0.1.0 - bootstrap scaffold\n\nUsage: onefetch [OPTIONS] [ARGS]\n\nO'
  >   +  b'ptions:\n  -h, --help     Print help\n  -V, --version  Print version\n')
  >   - (b'Command-line Git information tool\n\nUsage: executable [OPTIONS] [INPUT]\n\n'...

### `empty_list_or_string` — 1 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `eval.tests.test_onefetch_repo_outputs.test_no_title_removes_title_line`
  > IndexError: list index out of range

### `uncategorized` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_onefetch_repo_outputs.test_include_hidden_counts_hidden_file`
  > AttributeError: 'NoneType' object has no attribute 'group'

### `rc_mismatch_got2_want1` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_authors.test_zero_commits_should_not_happen_but_handled`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--output', 'json'], returncode=2, stdout='', stderr="onefetch: unknown option: --output\nusage: onefetch [OPTIONS] [ARGS]\nTry 'onefetch 

