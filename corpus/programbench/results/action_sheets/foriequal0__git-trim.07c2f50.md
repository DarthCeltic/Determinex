# Action Sheet — foriequal0__git-trim.07c2f50

**Current:** 38.18%  (294/770)
**Pass / Fail / Skip:** 294 / 410 / 0
**Gap to 100%:** 61.82 percentage points (476 tests)

## Failure clusters

410 failed tests grouped into 7 buckets (sorted by count).

### `rc_mismatch_got1_want0` — 134 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_delete_ranges.test_delete_merged_with_remote`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '--delete', 'merged:origin', '--bases', 'master', '--dry-run', '--no-update'], returncode=1, stdout=b'', stderr=b"Error: invalid delete ra
- `tests.test_delete_ranges.test_delete_merged_remote`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '--delete', 'merged-remote:origin', '--bases', 'master', '--dry-run', '--no-update'], returncode=1, stdout=b'', stderr=b"Error: invalid de
- `tests.test_delete_ranges.test_delete_diverged`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '--delete', 'diverged:origin', '--bases', 'master', '--dry-run', '--no-update'], returncode=1, stdout=b'', stderr=b"Error: invalid delete 
- *(... 131 more in this cluster)*

### `other_assertion` — 128 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_bases_configuration.test_bases_empty_uses_default`
  > AssertionError: assert ('Branches' in 'No branches to delete.\n' or 'master' in 'No branches to delete.\n' or '[base]' in 'No branches to delete.\n')
- `tests.test_bases_configuration.test_bases_with_nonexistent_branch_succeeds`
  > AssertionError: assert ('Branches' in 'No branches to delete.\n' or 'remain' in 'No branches to delete.\n')
- `tests.test_basic_invocation.test_help_flag`
  > assert b'Automatically trims your tracking branches' in b'git-trim 0.4.4\nDelete merged and stray git branches\n\nUsage: executable [OPTIONS]\n\nOptions:\n  -h, --help            Print help\n  -V, --v
  >  +  where b'git-trim 0.4.4\nDelete merged and stray git branches\n\nUsage: executable [OPTIONS]\n\nOptions:\n  -h, --help            Print help\n  -V, --version         Print version\n  -n, --dry-run 
- *(... 125 more in this cluster)*

### `string_output_mismatch` — 125 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_output.test_baseline_help_long_matches_fixture`
  > AssertionError: assert 'git-trim 0.4...se branches\n' == 'Automaticall...int version\n'
  >   
  >   - Automatically trims your tracking branches whose upstream branches are merged or stray.
  >   - `git-trim` is a missing companion to the `git fetch --prune` and a proper, safer, faster alternative to your `<bash oneliner HERE>`.
  >   + git-trim 0.4.4
  >   + Delete merged and stray git branches
  >     
  >     Usage: executable [OPTIONS]...
- `eval.tests.test_help_output.test_baseline_help_short_matches_fixture`
  > AssertionError: assert 'git-trim 0.4...se branches\n' == 'Automaticall...int version\n'
  >   
  >   - Automatically trims your tracking branches whose upstream branches are merged or stray.
  >   + git-trim 0.4.4
  >   + Delete merged and stray git branches
  >     
  >     Usage: executable [OPTIONS]
  >     ...
- `eval.tests.test_help_output.test_help_contains_opening_description_line`
  > AssertionError: assert 'git-trim 0.4.4' == 'Automaticall...ged or stray.'
  >   
  >   - Automatically trims your tracking branches whose upstream branches are merged or stray.
  >   + git-trim 0.4.4
- *(... 122 more in this cluster)*

### `rc_unexpected_zero` — 19 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_delete_ranges.test_delete_invalid_format`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--delete', 'merged', '--bases', 'master', '--dry-run', '--no-update'], returncode=0, stdout=b'No branches to delete.\n', stderr=b'').retu
- `tests.test_conflicting_flags.test_conflicting_update_flags`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--update', '--no-update', '--bases', 'master', '--dry-run'], returncode=0, stdout=b'No branches to delete.\n', stderr=b'').returncode
- `tests.test_conflicting_flags.test_conflicting_confirm_flags`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--confirm', '--no-confirm', '--bases', 'master', '--dry-run'], returncode=0, stdout=b'No branches to delete.\n', stderr=b'').returncode
- *(... 16 more in this cluster)*

### `boolean_false` — 2 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_subcommand_dispatch.TestErrorHandling.test_unknown_flag_error`
  > assert False
  >  +  where False = any(<generator object TestErrorHandling.test_unknown_flag_error.<locals>.<genexpr> at 0x7ff9a63be110>)
- `tests.test_error_no_bases.test_error_message_final_line`
  > AssertionError: assert False
  >  +  where False = <built-in method endswith of str object at 0x7f1c20162130>('Error: No base branch is found!')
  >  +    where <built-in method endswith of str object at 0x7f1c20162130> = 'Error: No base branch is found!\nTry any following commands to set valid bases:\n  `git config trim.bases develop,master` for 
  >  +      where 'Error: No base branch is found!\nTry any following commands to set valid bases:\n  `git config trim.bases develop,master` for a repository.\n  `git config --global trim.bases develop,ma
  >  +        where <built-in method strip of str object at 0x7f1c20161bb0> = 'Error: No base branch is found!\nTry any following commands to set valid bases:\n  `git config trim.bases develop,master` for

### `rc_mismatch_got0_want2` — 1 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `eval.tests.test_help_output.test_dashdash_then_help_is_error_and_points_to_help`
  > assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--', '--help'], returncode=0, stdout='git-trim 0.4.4\nDelete merged and stray git branches\n\nUsage: executable [OPTIONS]\n\nOptions:\n  

### `returned_none` — 1 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_output.test_help_format_indentation_for_options`
  > assert None
  >  +  where None = <function search at 0x7fc43e6f2680>('^ {10}Comma separated multiple names of branches\\.', 'git-trim 0.4.4\nDelete merged and stray git branches\n\nUsage: executable [OPTIONS]\n\nOpti
  >  +    where <function search at 0x7fc43e6f2680> = re.search
  >  +    and   'git-trim 0.4.4\nDelete merged and stray git branches\n\nUsage: executable [OPTIONS]\n\nOptions:\n  -h, --help            Print help\n  -V, --version         Print version\n  -n, --dry-run
  >  +    and   re.MULTILINE = re.M

