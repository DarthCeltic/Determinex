# Action Sheet — stacked-git__stgit.430027d

**Current:** 20.63%  (491/2380)
**Pass / Fail / Skip:** 491 / 1058 / 21
**Gap to 100%:** 79.37 percentage points (1889 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_subcommand_dispatch.test_each_subcommand_recognized_via_help_or_special_case[NOTSET]`
  - reason: got empty parameter set for (subcmd)
- `eval.tests.test_subcommand_dispatch.test_each_alias_dispatches_to_git[NOTSET]`
  - reason: got empty parameter set for (alias)
- `tests.test_harvest.test_shell_test_suite[t0002-status.sh]`
  - reason: Status command issues with certain git states
- `tests.test_harvest.test_shell_test_suite[t0009-log.sh]`
  - reason: Log command filtering/display issues
- `tests.test_harvest.test_shell_test_suite[t1205-push-subdir.sh]`
  - reason: Push/pop from subdir when removing current dir fails
- *(... 16 more skipped)*

## Failure clusters

1058 failed tests grouped into 21 buckets (sorted by count).

### `other_assertion` — 594 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_additional_commands.test_series_count_option`
  > AssertionError: assert (b'1' in b'' or b'2' in b'')
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', 'series', '--count'], returncode=0, stdout=b'', stderr=b'').stdout
  >  +  and   b'' = CompletedProcess(args=['/workspace/executable', 'series', '--count'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_additional_commands.test_series_no_prefix`
  > AssertionError: assert b'p1' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', 'series', '--noprefix'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_additional_commands.test_series_short_option`
  > AssertionError: assert b'p1' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', 'series', '--short'], returncode=0, stdout=b'', stderr=b'').stdout
- *(... 591 more in this cluster)*

### `rc_unexpected_zero` — 171 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_administration.test_completion_invalid_shell`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'completion', 'invalid-shell'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_basic_invocation.test_invalid_subcommand`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'nonexistent-command'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_coverage_boost.test_top_on_empty_stack_errors`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'top'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 168 more in this cluster)*

### `string_output_mismatch` — 166 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_baselines.test_baseline_main_help_long_exact`
  > assert 'stgit 0.1.0 ...int version\n' == "Maintain a s... with '-h')\n"
  >   
  >   - Maintain a stack of patches on top of a Git branch.
  >   + stgit 0.1.0 - bootstrap scaffold
  >     
  >   + Usage: stgit [OPTIONS] [ARGS]
  >   - Usage: stg [OPTIONS] <command> [...]
  >   -        stg [OPTIONS] <-h|--help>...
- `eval.tests.test_help_baselines.test_baseline_main_help_short_exact`
  > assert 'stgit 0.1.0 ...int version\n' == "Maintain a s...h '--help')\n"
  >   
  >   - Maintain a stack of patches on top of a Git branch.
  >   + stgit 0.1.0 - bootstrap scaffold
  >     
  >   + Usage: stgit [OPTIONS] [ARGS]
  >   - Usage: stg [OPTIONS] <command> [...]
  >   -        stg [OPTIONS] <-h|--help>...
- `eval.tests.test_help_baselines.test_baseline_subcommand_diff_help_exact`
  > assert '' == "Show the dif... with '-h')\n"
  >   
  >   - Show the diff (default) or diffstat between the current working copy or a tree-ish
  >   - object and another tree-ish object (defaulting to HEAD). File names can also be given to
  >   - restrict the diff output. The tree-ish object has the format accepted by the 'stg id'
  >   - command.
  >   - 
  >   - Usage: stg diff [OPTIONS] [path]......
- *(... 163 more in this cluster)*

### `rc_mismatch_got0_want2` — 21 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_basic.TestGitRepositoryRequirement.test_series_without_git_repo`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'series'], returncode=0, stdout='', stderr='').returncode
- `tests.test_basic.TestExitCodes.test_system_error_exit_code`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'series'], returncode=0, stdout='', stderr='').returncode
- `tests.test_stack_navigation.TestTop.test_top_with_no_patches`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'top'], returncode=0, stdout='', stderr='').returncode
- *(... 18 more in this cluster)*

### `rc_mismatch_got2_want0` — 20 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_basic_invocation.test_color_option_auto`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--color', 'auto', '--help'], returncode=2, stdout=b'', stderr=b"stgit: unknown option: --color\nusage: stgit [OPTIONS] [ARGS]\nTry 'stgit
- `tests.test_basic_invocation.test_color_option_always`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--color', 'always', '--help'], returncode=2, stdout=b'', stderr=b"stgit: unknown option: --color\nusage: stgit [OPTIONS] [ARGS]\nTry 'stg
- `tests.test_basic_invocation.test_color_option_never`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--color', 'never', '--help'], returncode=2, stdout=b'', stderr=b"stgit: unknown option: --color\nusage: stgit [OPTIONS] [ARGS]\nTry 'stgi
- *(... 17 more in this cluster)*

### `boolean_false` — 18 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_comprehensive_commands.test_squash_save_template`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/pytest-of-root/pytest-0/test_squash_save_template2/template.txt').exists
- `tests.test_coverage_simple.test_export_command_basic`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/pytest-of-root/pytest-0/test_export_command_basic2/test_repo/exported').exists
- `tests.test_import_export_advanced.test_export_to_directory`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('exported').exists
- *(... 15 more in this cluster)*

### `uncategorized` — 12 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_coverage_boost.test_sink_moves_patch_down`
  > ValueError: substring not found
- `tests.test_comprehensive_options.test_series_reverse`
  > ValueError: substring not found
- `tests.test_config_aliases.test_float_with_series`
  > ValueError: substring not found
- *(... 9 more in this cluster)*

### `returned_none` — 12 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_main.test_help_lists_selected_commands[diff-Show a diff]`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7fc87f5b6680>('^\\s{2}diff\\s{2,}.*Show\\ a\\ diff', 'stgit 0.1.0 - bootstrap scaffold\n\nUsage: stgit [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\
  >  +    where <function search at 0x7fc87f5b6680> = re.search
  >  +    and   'stgit 0.1.0 - bootstrap scaffold\n\nUsage: stgit [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['/workspace/executab
  >  +    and   re.MULTILINE = re.MULTILINE
- `eval.tests.test_help_main.test_help_lists_selected_commands[files-Show files modified]`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7fc87f5b6680>('^\\s{2}files\\s{2,}.*Show\\ files\\ modified', 'stgit 0.1.0 - bootstrap scaffold\n\nUsage: stgit [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Pr
  >  +    where <function search at 0x7fc87f5b6680> = re.search
  >  +    and   'stgit 0.1.0 - bootstrap scaffold\n\nUsage: stgit [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['/workspace/executab
  >  +    and   re.MULTILINE = re.MULTILINE
- `eval.tests.test_help_main.test_help_lists_selected_commands[id-Print git hash]`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7fc87f5b6680>('^\\s{2}id\\s{2,}.*Print\\ git\\ hash', 'stgit 0.1.0 - bootstrap scaffold\n\nUsage: stgit [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help
  >  +    where <function search at 0x7fc87f5b6680> = re.search
  >  +    and   'stgit 0.1.0 - bootstrap scaffold\n\nUsage: stgit [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['/workspace/executab
  >  +    and   re.MULTILINE = re.MULTILINE
- *(... 9 more in this cluster)*

### `empty_list_or_string` — 11 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_config_env.test_global_gitconfig_stgit_alias_is_respected`
  > IndexError: list index out of range
- `tests.test_advanced_stack.test_float_series_from_file`
  > IndexError: list index out of range
- `tests.test_completion_shstream.test_bash_completion_multiline_raw_insertion`
  > IndexError: list index out of range
- *(... 8 more in this cluster)*

### `rc_mismatch_got0_want1` — 10 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_basic.TestInvalidCommands.test_invalid_subcommand`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'nonexistent-command'], returncode=0, stdout='', stderr='').returncode
- `tests.test_basic.TestExitCodes.test_user_error_exit_code`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'invalid-command'], returncode=0, stdout='', stderr='').returncode
- `tests.test_edit_rename_spill_sync.test_rename_invalid_name`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'rename', 'invalid..name'], returncode=0, stdout='', stderr='').returncode
- *(... 7 more in this cluster)*

### `missing_file` — 6 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_deep_coverage.test_sync_operation`
  > FileNotFoundError: [Errno 2] No such file or directory: '.git/patches/master/series'
- `tests.test_import_export.test_export_multifile_patch`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_export_multifile_patch2/export_multi/multifile'
- `tests.test_import_export.test_export_with_template`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_export_with_template2/export_tmpl/tpatch'
- *(... 3 more in this cluster)*

### `rc_mismatch_got1_want2` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_edit_rename_spill_sync.test_spill_empty_patch`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len([''])
- `tests.test_edit_rename_spill_sync.test_edit_authname_and_authemail_separately`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len([''])
- `tests.test_edit_rename_spill_sync.test_spill_multiple_pathspecs`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len([''])

### `rc_mismatch_got0_want3` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_hide_unhide_clean_patches.test_hide_unhide_patch_range`
  > assert 0 == 3
- `tests.test_t0008_series.test_applied_series`
  > assert 0 == 3
  >  +  where 0 = len([])
- `tests.test_t3100_reset.test_pop_and_series`
  > assert 0 == 3
  >  +  where 0 = len([])

### `subprocess_failed` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_edge_cases.test_repair_after_git_operations`
  > subprocess.CalledProcessError: Command '['git', 'reset', '--hard', 'HEAD~1']' returned non-zero exit status 128.
- `tests.test_t2702_refresh_rm.test_refresh_after_rm`
  > subprocess.CalledProcessError: Command '['git', 'rm', 'removeme.txt']' returned non-zero exit status 1.

### `bytes_output_mismatch` — 2 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_config_env.test_local_gitconfig_alias_overrides_global_alias`
  > AssertionError: assert b'' == b'master'
  >   
  >   Full diff:
  >   - (b'master')
  >   + b''
- `eval.tests.test_help_and_version.test_version_and_subcommand_version_match`
  > AssertionError: assert b'stgit 0.1.0\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'stgit 0.1.0\n')

### `rc_mismatch_got2_want1` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic.TestNoArguments.test_no_arguments_returns_error_code`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout='', stderr="usage: stgit [OPTIONS] [ARGS]\nTry 'stgit --help' for more information.\n").returncode
- `tests.test_basic.TestInvalidCommands.test_invalid_flag`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--invalid-flag'], returncode=2, stdout='', stderr="stgit: unknown option: --invalid-flag\nusage: stgit [OPTIONS] [ARGS]\nTry 'stgit --hel

### `rc_mismatch_got0_want40` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_comprehensive_options.test_id_with_branch_patch`
  > AssertionError: assert 0 == 40
  >  +  where 0 = len(b'')
  >  +    where b'' = <built-in method strip of bytes object at 0x7f873ab44030>()
  >  +      where <built-in method strip of bytes object at 0x7f873ab44030> = b''.strip
  >  +        where b'' = CompletedProcess(args=['/workspace/executable', 'id', 'other:p2'], returncode=0, stdout=b'', stderr=b'').stdout

### `type_error` — 1 test(s)

**Quick patch ideas:**
- Specific TypeError; check arg types vs expected

**Sample failures:**

- `tests.test_error_paths.test_init_no_git_repo`
  > TypeError: run() got an unexpected keyword argument 'args'

### `rc_mismatch_got1_want20` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_edge_cases.TestMultipleOperations.test_create_many_patches`
  > AssertionError: assert 1 == 20
  >  +  where 1 = len([''])

### `rc_mismatch_got1_want50` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_diff_wrapper.test_diff_files_large_number_of_files`
  > AssertionError: assert 1 == 50
  >  +  where 1 = len([''])

### `rc_mismatch_got0_want4` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_t0008_series.test_default_series`
  > assert 0 == 4
  >  +  where 0 = len([])

