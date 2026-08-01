# Action Sheet — canop__broot.d6c798e

**Current:** 27.22%  (236/867)
**Pass / Fail / Skip:** 236 / 434 / 0
**Gap to 100%:** 72.78 percentage points (631 tests)

## Failure clusters

434 failed tests grouped into 12 buckets (sorted by count).

### `other_assertion` — 258 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_advanced_verbs.test_parent_navigation_from_root`
  > AssertionError: assert '/test_advanced_verbs' in '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPane is dead (status 0, Sun May 17 05:47:12 2026)\n'
- `tests.test_advanced_verbs.test_custom_verb_parent_pattern`
  > assert '/tree_structure/dir2' in "usage: broot [OPTIONS] [ARGS]\nTry 'broot --help' for more information.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPane is dead (status 2, Sun May 17 05:47:29 2026)\n
- `tests.test_advanced_verbs.test_focus_nonexistent_path`
  > AssertionError: assert '/tree_structure' in '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPane is dead (status 0, Sun May 17 05:48:15 2026)\n'
- *(... 255 more in this cluster)*

### `string_output_mismatch` — 66 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_advanced_verbs.test_focus_enter_on_directory`
  > AssertionError: assert '\n\n\n\n\n\n...45:22 2026)\n' == '/workspace/e...  h:n  gi:y\n'
  >   
  >   - /workspace/eval/test_resources/test_advanced_verbs/tree_structure
  >   -  ├──dir1
  >   -  │  └──file2.txt
  >   -  ├──dir2
  >   -  │  └──subdir
  >   -  │     └──file3.txt...
- `tests.test_advanced_verbs.test_focus_relative_path_argument`
  > AssertionError: assert '\n\n\n\n\n\n...45:38 2026)\n' == '/workspace/e...  h:n  gi:y\n'
  >   
  >   - /workspace/eval/test_resources/test_advanced_verbs/tree_structure/dir2
  >   -  └──subdir
  >   -     └──file3.txt
  >     
  >     
  >     ...
- `tests.test_advanced_verbs.test_focus_absolute_path_argument`
  > AssertionError: assert '\n' == '/workspace/e...  h:n  gi:y\n'
  >   
  >   Strings contain only whitespace, escaping them using repr()
  >   - '/workspace/eval/test_resources/test_advanced_verbs/tree_structure/dir3\n └──deep\n    └──nested\n       └──file4.txt\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n Hit esc to go back, enter to go up, ? fo
  >   + '\n'
- *(... 63 more in this cluster)*

### `rc_mismatch_got2_want0` — 64 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_config.test_write_default_conf_idempotent`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--write-default-conf', '/tmp/pytest-of-root/pytest-0/test_write_default_conf_idempo2/config'], returncode=2, stdout='', stderr="broot: un
- `tests.test_config.test_skin_files_have_color_definitions`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--write-default-conf', '/tmp/pytest-of-root/pytest-0/test_skin_files_have_color_def2/config'], returncode=2, stdout='', stderr="broot: un
- `tests.test_config.test_write_default_conf_permissions`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--write-default-conf', '/tmp/pytest-of-root/pytest-0/test_write_default_conf_permis2/config'], returncode=2, stdout='', stderr="broot: un
- *(... 61 more in this cluster)*

### `returned_none` — 30 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_execution_builder.test_file_placeholder_with_spaces`
  > assert None is not None
- `tests.test_execution_builder.test_directory_placeholder`
  > assert None is not None
- `tests.test_execution_builder.test_parent_placeholder`
  > assert None is not None
- *(... 27 more in this cluster)*

### `missing_file` — 5 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_advanced_verbs.test_verb_pattern_expansion_file_name`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_verb_pattern_expansion_fi2/pattern_output.txt'
- `tests.test_advanced_verbs.test_verb_pattern_file_stem_and_extension`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_verb_pattern_file_stem_an2/stem_ext_output.txt'
- `tests.test_advanced_verbs.test_verb_pattern_multiple_substitutions`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_verb_pattern_multiple_sub2/multi_pattern_output.txt'
- *(... 2 more in this cluster)*

### `boolean_false` — 3 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_advanced_verbs.test_select_nonexistent_path`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7bddeb9897b0>('/workspace/eval/test_resources/test_advanced_verbs/tree_structure\n')
  >  +    where <built-in method startswith of str object at 0x7bddeb9897b0> = '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPane is dead (status 0, Sun May 17 05:48:00 2026)\n'.startswith
- `tests.test_shell_install.test_set_install_state_refused_then_installed_file_transitions`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/pytest-of-root/pytest-0/test_set_install_state_refused5/home/.config/broot/launcher/refused').exists
- `tests.test_verbs_commands.test_verb_output_write_single_line`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/pytest-of-root/pytest-0/test_verb_output_write_single_2/verb_output.txt').exists

### `test_timeout` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_pattern_unit.test_fuzzy_pattern_rust_unit_tests`
  > subprocess.TimeoutExpired: Command '['cargo', 'test', '--lib', 'fuzzy_pattern', '--', '--test-threads=1']' timed out after 60 seconds
- `tests.test_pattern_unit.test_tok_pattern_rust_unit_tests`
  > subprocess.TimeoutExpired: Command '['cargo', 'test', '--lib', 'tok_pattern', '--', '--test-threads=1']' timed out after 60 seconds

### `rc_mismatch_got0_want2` — 2 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_argument_parsing.TestShortFlagEquivalents.test_short_long_flag_equivalence[-h---hidden]`
  > assert 0 == 2
- `eval.tests.test_arg_parsing_validation.test_too_many_positionals_error_exit_2`
  > AssertionError: assert 0 == 2
  >  +  where 0 = RunResult(code=0, out='', err='').code

### `rc_mismatch_got0_want1` — 1 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_advanced_verbs.test_select_followed_by_focus`
  > assert 0 == 1
  >  +  where 0 = len([])

### `rc_mismatch_got2_want1` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_display_flags.test_invalid_height_zero`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--height', '0', '/tmp'], returncode=2, stdout='', stderr="broot: unknown option: --height\nusage: broot [OPTIONS] [ARGS]\nTry 'broot --he

### `rc_unexpected_zero` — 1 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `eval.tests.test_help_usage.test_help_with_invalid_flag_returns_error_and_usage`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--help', '--definitely-not-a-real-flag'], returncode=0, stdout='broot 0.1.0 - bootstrap scaffold\n\nUsage: broot [OPTIONS] [ARGS]\n\nOpti

### `bytes_output_mismatch` — 1 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `eval.tests.test_cli.test_help_exact_matches_frozen_file`
  > assert b'broot 0.1.0...int version\n' == b"           ...8\x1b[39m\n\n"
  >   
  >   At index 0 diff: b'b' != b' '
  >   
  >   Full diff:
  >   + (b'broot 0.1.0 - bootstrap scaffold\n\nUsage: broot [OPTIONS] [ARGS]\n\nOptions'
  >   +  b':\n  -h, --help     Print help\n  -V, --version  Print version\n')
  >   - (b'                   \x1b[1m\x1b[4mbroot\x1b[0m\x1b[1m\x1b[4m \x1b[0m\x1b[1'...

