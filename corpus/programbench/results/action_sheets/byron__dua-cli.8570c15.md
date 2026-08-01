# Action Sheet — byron__dua-cli.8570c15

**Current:** 22.16%  (308/1390)
**Pass / Fail / Skip:** 308 / 618 / 5
**Gap to 100%:** 77.84 percentage points (1082 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_error_cases.test_aggregate_with_permission_denied`
  - reason: Running as root, can't test permission errors
- `tests.test_error_cases.test_mixed_readable_unreadable_files`
  - reason: Running as root, can't test permission errors
- `tests.test_input_handling.test_no_permission_handling`
  - reason: Running as root, can't test permission errors
- `tests.test_aggregate_advanced.test_permission_denied_error_handling`
  - reason: Cannot test permission denied when running as root
- `tests.test_subcommand_dispatch.test_each_subcommand_accepts_help[NOTSET]`
  - reason: got empty parameter set for (subcmd)

## Failure clusters

618 failed tests grouped into 14 buckets (sorted by count).

### `other_assertion` — 321 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_additional_coverage.test_threads_with_various_values`
  > AssertionError: assert b'total' in b' 16.0KiB /tmp/tmpkmi93vl7\n'
  >  +  where b' 16.0KiB /tmp/tmpkmi93vl7\n' = CompletedProcess(args=['/workspace/executable', '-t', '1', '/tmp/tmpkmi93vl7'], returncode=0, stdout=b' 16.0KiB /tmp/tmpkmi93vl7\n', stderr=b'').stdout
- `tests.test_additional_coverage.test_apparent_size_vs_disk_usage`
  > AssertionError: assert b'total' in b' 16.0KiB /tmp/tmp5juga6fh\n'
  >  +  where b' 16.0KiB /tmp/tmp5juga6fh\n' = CompletedProcess(args=['/workspace/executable', '/tmp/tmp5juga6fh'], returncode=0, stdout=b' 16.0KiB /tmp/tmp5juga6fh\n', stderr=b'').stdout
- `tests.test_additional_coverage.test_multiple_inputs_with_stats`
  > assert 0 > 0
  >  +  where 0 = len(b'')
  >  +    where b'' = CompletedProcess(args=['/workspace/executable', 'aggregate', '--stats', '/tmp/tmp1vjfqne_/file1.txt', '/tmp/tmp1vjfqne_/file2.txt'], returncode=0, stdout=b"  4.0KiB /tmp/tmp1vjfqne_/
- *(... 318 more in this cluster)*

### `rc_mismatch_got2_want0` — 160 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_additional_coverage.test_count_hard_links_behavior`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-l', '/tmp/tmp7gfi71bo'], returncode=2, stdout=b'', stderr=b"dua-cli: unknown option: -l\nusage: dua-cli [OPTIONS] [ARGS]\nTry 'dua-cli -
- `tests.test_additional_coverage.test_stay_on_filesystem_behavior`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-x', '/tmp/tmp2itrz412'], returncode=2, stdout=b'', stderr=b"dua-cli: unknown option: -x\nusage: dua-cli [OPTIONS] [ARGS]\nTry 'dua-cli -
- `tests.test_additional_coverage.test_ignore_dirs_behavior`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-i', '/tmp/tmp48775pac/ignored', '/tmp/tmp48775pac'], returncode=2, stdout=b'', stderr=b"dua-cli: unknown option: -i\nusage: dua-cli [OPT
- *(... 157 more in this cluster)*

### `rc_mismatch_got1_want0` — 71 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_additional_coverage.test_completions_all_shells`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'completions', 'bash'], returncode=1, stdout=b"Error: Path 'completions' does not exist\nError: Path 'bash' does not exist\n", stderr=b'')
- `tests.test_additional_coverage.test_aggregate_with_current_directory_implicit`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'aggregate'], returncode=1, stdout=b"Error: Path 'aggregate' does not exist\n", stderr=b'').returncode
- `tests.test_completions_command.test_completions_bash`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'completions', 'bash'], returncode=1, stdout=b"Error: Path 'completions' does not exist\nError: Path 'bash' does not exist\n", stderr=b'')
- *(... 68 more in this cluster)*

### `rc_unexpected_zero` — 18 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_aggregate_command.test_aggregate_mixed_valid_invalid_paths`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'aggregate', '/tmp/tmp0t8jm_8z', '/nonexistent/path/xyz'], returncode=0, stdout=b" 16.0KiB /tmp/tmp0t8jm_8z\nError: Path 'aggregate' does 
- `tests.test_basic_invocation.test_help_for_nonexistent_subcommand`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'help', 'nonexistent'], returncode=0, stdout=b'dua-cli 0.1.0\nAnalyze disk usage of files and directories\n\nUSAGE:\n    dua-cli [FLAGS] [
- `tests.test_error_cases.test_invalid_threads_negative`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--threads', '-1', '.'], returncode=0, stdout=b'  2.4MiB .\n', stderr=b'').returncode
- *(... 15 more in this cluster)*

### `string_output_mismatch` — 16 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_aggregate.test_aggregate_multiple_paths_default_sorted`
  > AssertionError: assert '100.0KiB /tm...s_2/large.bin' == '0   B /tmp/p...paths_2/empty'
  >   
  >   - 0   B /tmp/pytest-of-root/pytest-0/test_aggregate_multiple_paths_2/empty
  >   ?  ^^^                                                                ^^^^
  >   + 100.0KiB /tmp/pytest-of-root/pytest-0/test_aggregate_multiple_paths_2/large.bin
  >   ? + ^^^^^                                                               ++++ ^^^^
- `tests.test_aggregate.test_aggregate_empty_directory_shows_zero_bytes`
  > AssertionError: assert '4.0KiB /tmp/...ry2/with_file' == '0   B /tmp/p...ectory2/empty'
  >   
  >   - 0   B /tmp/pytest-of-root/pytest-0/test_aggregate_empty_directory2/empty
  >   ?  ^^^                                                                ----
  >   + 4.0KiB /tmp/pytest-of-root/pytest-0/test_aggregate_empty_directory2/with_file
  >   ? ++ ^^                                                               ++++++++
- `tests.test_aggregate.test_aggregate_multiple_nonexistent_paths_plural_errors`
  > assert "Error: Path ...oes not exist" == '0   B /nonex... <1 IO Error>'
  >   
  >   - 0   B /nonexistent1  <1 IO Error>
  >   + Error: Path 'aggregate' does not exist
- *(... 13 more in this cluster)*

### `rc_mismatch_got0_want1` — 8 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_aggregate.test_aggregate_mixed_valid_and_invalid_paths`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'aggregate', '/tmp/pytest-of-root/pytest-0/test_aggregate_mixed_valid_and2/valid.txt', '/totally/nonexistent'], returncode=0, stdout="  4.
- `tests.test_aggregate_advanced.test_multiple_roots_all_valid`
  > assert 0 == 1
  >  +  where 0 = len([])
- `tests.test_edge_cases.test_broken_symlink_explicit_path`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'aggregate', '/tmp/pytest-of-root/pytest-0/test_broken_symlink_explicit_p2/broken_link_test/broken_link.txt'], returncode=0, stdout="     
- *(... 5 more in this cluster)*

### `boolean_false` — 6 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_interactive_tmux.test_interactive_displays_sizes`
  > assert False
  >  +  where False = any(<generator object test_interactive_displays_sizes.<locals>.<genexpr> at 0x7f8817cbbd10>)
- `tests.test_output_variations.test_output_formats_comprehensive`
  > assert False
  >  +  where False = any(<generator object test_output_formats_comprehensive.<locals>.<genexpr> at 0x7f8816328f90>)
- `tests.test_aggregate.test_aggregate_stats_format_structure`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7fcb37504030>('Statistics {')
  >  +    where <built-in method startswith of str object at 0x7fcb37504030> = ''.startswith
- *(... 3 more in this cluster)*

### `returned_none` — 4 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_basic_invocation.test_version_output`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f696e1de680>(b'dua\\s+\\d+\\.\\d+\\.\\d+', b'dua-cli 0.1.0\n')
  >  +    where <function search at 0x7f696e1de680> = re.search
  >  +    and   b'dua-cli 0.1.0\n' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'dua-cli 0.1.0\n', stderr=b'').stdout
- `tests.test_basic_invocation.test_version_flag`
  > AssertionError: assert None
  >  +  where None = <function match at 0x7f8819a31120>(b'dua \\d+\\.\\d+\\.\\d+', b'dua-cli 0.1.0\n')
  >  +    where <function match at 0x7f8819a31120> = re.match
  >  +    and   b'dua-cli 0.1.0\n' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'dua-cli 0.1.0\n', stderr=b'').stdout
- `tests.test_basic_invocation.test_version_short_flag`
  > AssertionError: assert None
  >  +  where None = <function match at 0x7f8819a31120>(b'dua \\d+\\.\\d+\\.\\d+', b'dua-cli 0.1.0\n')
  >  +    where <function match at 0x7f8819a31120> = re.match
  >  +    and   b'dua-cli 0.1.0\n' = CompletedProcess(args=['/workspace/executable', '-V'], returncode=0, stdout=b'dua-cli 0.1.0\n', stderr=b'').stdout
- *(... 1 more in this cluster)*

### `rc_mismatch_got2_want1` — 4 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_aggregate_advanced.test_symlink_handling`
  > assert 2 == 1
  >  +  where 2 = len(['  4.0KiB /tmp/pytest-of-root/pytest-0/test_symlink_handling2/link.txt', "Error: Path 'aggregate' does not exist"])
- `tests.test_global_flags.test_log_file_invalid_path_fails`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--log-file', '/nonexistent/dir/test.log', 'aggregate', '/tmp/pytest-of-root/pytest-0/test_log_file_invalid_path_fai2/test.txt'], returnco
- `tests.test_global_flags.test_log_file_with_nonexistent_path`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--log-file', '/tmp/pytest-of-root/pytest-0/test_log_file_with_nonexistent2/nonexistent.log', 'aggregate', '/nonexistent_test_path'], retu
- *(... 1 more in this cluster)*

### `rc_mismatch_got1_want2` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_argparse_validation.test_completions_requires_shell_and_validates[args0-must_contain0]`
  > assert 1 == 2
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'completions'], returncode=1, stdout="Error: Path 'completions' does not exist\n", stderr='').returncode
- `eval.tests.test_argparse_validation.test_completions_requires_shell_and_validates[args1-must_contain1]`
  > assert 1 == 2
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'completions', 'bash', 'extra'], returncode=1, stdout="Error: Path 'completions' does not exist\nError: Path 'bash' does not exist\nError:
- `eval.tests.test_argparse_validation.test_completions_requires_shell_and_validates[args2-must_contain2]`
  > assert 1 == 2
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'completions', 'nope'], returncode=1, stdout="Error: Path 'completions' does not exist\nError: Path 'nope' does not exist\n", stderr='').r

### `bytes_output_mismatch` — 3 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_externalized_stateless_journey.test_ext_multiple_input_paths_with_total`
  > AssertionError: assert ['.', '.', 'd...dir/sub', 'a'] == ['dir/sub', '... '.', 'total']
  >   
  >   At index 0 diff: '.' != 'dir/sub'
  >   
  >   Full diff:
  >     [
  >   -     'dir/sub',
  >   +     '.',...
- `tests.test_externalized_stateless_journey.test_ext_multiple_input_paths_with_stats`
  > AssertionError: assert ['.', '.', 'd... 'total', ...] == ['dir/sub', '... 'total', ...]
  >   
  >   At index 0 diff: '.' != 'dir/sub'
  >   Left contains one more item: 'exist'
  >   
  >   Full diff:
  >     [
  >   -     'dir/sub',...
- `tests.test_externalized_stateless_journey.test_ext_multiple_input_paths_without_subcommand`
  > AssertionError: assert ['.', '.', 'd...r', 'dir/sub'] == ['dir/sub', '... '.', 'total']
  >   
  >   At index 0 diff: '.' != 'dir/sub'
  >   Right contains one more item: 'total'
  >   
  >   Full diff:
  >     [
  >   -     'dir/sub',...

### `rc_mismatch_got0_want2` — 2 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `eval.tests.test_argparse_default_and_precedence.test_repeated_flag_is_rejected_for_format`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--format', 'bytes', '--format', 'metric', '--threads', '1', 'eval/tmp_argparse6'], returncode=0, stdout='  4.0KiB eval/tmp_argparse6\n', 
- `eval.tests.test_argparse_validation.test_format_validation[args1-must_contain1]`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--format', 'nope'], returncode=0, stdout='  2.2MiB .\n', stderr='').returncode

### `rc_mismatch_got2_want4` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_aggregate.test_aggregate_bytes_format_alignment`
  > assert 2 == 4
  >  +  where 2 = len(['98.6KiB /tmp/pytest-of-root/pytest-0/test_aggregate_bytes_format_al2', "Error: Path 'aggregate' does not exist"])

### `uncategorized` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_help_main.test_help_usage_mentions_flags_options_subcommand_input`
  > StopIteration

