# Action Sheet — unhappychoice__gittype.34b72d0

**Current:** 10.39%  (86/828)
**Pass / Fail / Skip:** 86 / 360 / 3
**Gap to 100%:** 89.61 percentage points (742 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_cache.test_cache_stats_very_large_file`
  - reason: Too slow for CI - takes 2+ minutes
- `tests.test_subcommand_dispatch.test_subcommand_help_recognized[NOTSET]`
  - reason: got empty parameter set for (subcmd)
- `tests.test_subcommand_dispatch.test_subcommand_help_differs_from_main_help[NOTSET]`
  - reason: got empty parameter set for (subcmd)

## Failure clusters

360 failed tests grouped into 12 buckets (sorted by count).

### `other_assertion` — 178 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cache.test_cache_stats_then_list_consistency`
  > AssertionError: assert 'Cached repositories: 0' in 'No cached challenges found.\n'
  >  +  where 'No cached challenges found.\n' = CompletedProcess(args=['/workspace/executable', 'cache', 'stats'], returncode=0, stdout='No cached challenges found.\n', stderr='').stdout
- `tests.test_cache.test_cache_clear_then_stats`
  > AssertionError: assert 'Cached repositories: 0' in 'No cached challenges found.\n'
  >  +  where 'No cached challenges found.\n' = CompletedProcess(args=['/workspace/executable', 'cache', 'stats'], returncode=0, stdout='No cached challenges found.\n', stderr='').stdout
- `tests.test_cache.test_cache_stats_output_format_bytes`
  > AssertionError: Expected at least 2 lines, got 1
  > assert 1 >= 2
  >  +  where 1 = len(['No cached challenges found.'])
- *(... 175 more in this cluster)*

### `string_output_mismatch` — 126 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_cache.test_cache_stats_empty`
  > AssertionError: assert 'No cached ch...nges found.\n' == 'Challenge Ca...ze: 0 bytes\n'
  >   
  >   + No cached challenges found.
  >   - Challenge Cache Statistics:
  >   -   Cached repositories: 0
  >   -   Total size: 0 bytes
- `tests.test_cache.test_cache_subcommand_required`
  > AssertionError: assert '' == 'Manage chall... Print help\n'
  >   
  >   - Manage challenge cache
  >   - 
  >   - Usage: executable cache <COMMAND>
  >   - 
  >   - Commands:
  >   -   stats  Show cache statistics...
- `tests.test_cache.test_cache_help_flag`
  > AssertionError: assert '' == 'Manage chall... Print help\n'
  >   
  >   - Manage challenge cache
  >   - 
  >   - Usage: executable cache <COMMAND>
  >   - 
  >   - Commands:
  >   -   stats  Show cache statistics...
- *(... 123 more in this cluster)*

### `rc_mismatch_got0_want1` — 13 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_languages.test_javascript_language_metadata`
  > assert 0 == 1
  >  +  where 0 = len([])
- `tests.test_languages.test_csharp_language_metadata`
  > assert 0 == 1
  >  +  where 0 = len([])
- `tests.test_languages.test_cpp_language_metadata`
  > assert 0 == 1
  >  +  where 0 = len([])
- *(... 10 more in this cluster)*

### `rc_unexpected_zero` — 11 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_global_args.test_version_with_subcommand_ignored`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'cache', '--version'], returncode=0, stdout='', stderr='').returncode
- `tests.test_global_args.test_unknown_subcommand`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'unknown-command'], returncode=0, stdout='gittype 0.1.0\n----------------------------------------\nInteractive TUI tool driven by tmux/lib
- `tests.test_languages.test_invalid_language_provides_complete_supported_list`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'trending', 'notareallanguage'], returncode=0, stdout='', stderr='').returncode
- *(... 8 more in this cluster)*

### `returned_none` — 9 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_main.test_main_help_lists_subcommands[history]`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7fe433d32680>('^\\s*history\\b', '', flags=re.MULTILINE)
  >  +    where <function search at 0x7fe433d32680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- `eval.tests.test_help_main.test_main_help_lists_subcommands[stats]`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7fe433d32680>('^\\s*stats\\b', '', flags=re.MULTILINE)
  >  +    where <function search at 0x7fe433d32680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- `eval.tests.test_help_main.test_main_help_lists_subcommands[export]`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7fe433d32680>('^\\s*export\\b', '', flags=re.MULTILINE)
  >  +    where <function search at 0x7fe433d32680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- *(... 6 more in this cluster)*

### `uncategorized` — 8 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_database_daos.test_database_repositories_table_schema`
  > sqlite3.OperationalError: unable to open database file
- `tests.test_database_daos.test_database_sessions_table_schema`
  > sqlite3.OperationalError: unable to open database file
- `tests.test_database_daos.test_database_stage_results_table_schema`
  > sqlite3.OperationalError: unable to open database file
- *(... 5 more in this cluster)*

### `rc_mismatch_got1_want2` — 6 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_history_stats.test_history_with_many_repeated_flags`
  > AssertionError: assert 1 == 2
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'history', '--invalid', '--invalid', '--invalid', '--invalid', '--invalid', '--invalid', '--invalid', '--invalid', '--invalid', '--invalid
- `tests.test_history_stats.test_stats_with_many_repeated_flags`
  > AssertionError: assert 1 == 2
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'stats', '--invalid', '--invalid', '--invalid', '--invalid', '--invalid', '--invalid', '--invalid', '--invalid', '--invalid', '--invalid',
- `tests.test_history_stats.test_history_with_extremely_long_argument`
  > AssertionError: assert 1 == 2
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'history', '--xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
- *(... 3 more in this cluster)*

### `boolean_false` — 4 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_cache_repo_integration.test_cache_and_repo_under_same_gittype_root`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/pytest-of-root/pytest-0/test_cache_and_repo_under_same2/home/.gittype').exists
- `tests.test_cli_errors.test_version_flag`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7fd2d6678030>('gittype ')
  >  +    where <built-in method startswith of str object at 0x7fd2d6678030> = ''.startswith
  >  +      where '' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout='', stderr='').stdout
- `eval.tests.test_help_main.test_help_has_trailing_newline`
  > AssertionError: assert False
  >  +  where False = <built-in method endswith of str object at 0x7fe433dc0030>('\n')
  >  +    where <built-in method endswith of str object at 0x7fe433dc0030> = ''.endswith
  >  +      where '' = CompletedProcess(args=['/workspace/executable', '--help'], returncode=0, stdout='', stderr='').stdout
- *(... 1 more in this cluster)*

### `rc_mismatch_got2_want1` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_errors.test_export_output_very_long_path`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'export', '--output', '/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
- `tests.test_export.test_export_path_with_newlines`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'export', '--output', 'file\nname.json'], returncode=2, stdout='', stderr='').returncode

### `rc_mismatch_got1_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_export.test_export_error_message_structure`
  > AssertionError: assert 1 == 3
  >  +  where 1 = len([''])

### `rc_mismatch_got1_want4` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_export.test_export_with_both_flags_error_message_structure`
  > AssertionError: assert 1 == 4
  >  +  where 1 = len([''])

### `empty_list_or_string` — 1 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_languages.test_rust_language_metadata`
  > IndexError: list index out of range

