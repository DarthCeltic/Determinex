# Action Sheet — sharkdp__fd.40d8eb3

**Current:** 21.24%  (387/1822)
**Pass / Fail / Skip:** 387 / 831 / 10
**Gap to 100%:** 78.76 percentage points (1435 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_help_behavior.test_help_color_always_emits_ansi`
  - reason: Help output is not expected to be colorized in this non-TTY test harness
- `eval.tests.test_fd_behavior.test_hidden_flag_includes_hidden`
  - reason: test_hidden_flag_includes_hidden depends on test_no_args_lists_all_non_hidden_non_ignored
- `eval.tests.test_fd_behavior.test_no_ignore_flag_includes_gitignored`
  - reason: test_no_ignore_flag_includes_gitignored depends on test_no_args_lists_all_non_hidden_non_ignored
- `eval.tests.test_fd_behavior.test_unrestricted_includes_hidden_and_ignored`
  - reason: test_unrestricted_includes_hidden_and_ignored depends on test_hidden_flag_includes_hidden
- `tests.test_harvest.test_hidden_file_attribute`
  - reason: Windows-specific test
- *(... 5 more skipped)*

## Failure clusters

831 failed tests grouped into 17 buckets (sorted by count).

### `other_assertion` — 373 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_depth_control.test_max_depth_one`
  > AssertionError: assert b'file2.txt' not in b'tmpq8247c20/file.txt\ntmpq8247c20/sub\nsub/deep\nsub/file2.txt\n'
  >  +  where b'tmpq8247c20/file.txt\ntmpq8247c20/sub\nsub/deep\nsub/file2.txt\n' = CompletedProcess(args=['/workspace/executable', '--max-depth', '1'], returncode=0, stdout=b'tmpq8247c20/file.txt\ntmpq82
- `tests.test_depth_control.test_max_depth_two`
  > AssertionError: assert b'file3.txt' not in b'tmptwvx8tf9/file.txt\ntmptwvx8tf9/sub\nsub/deep\ndeep/file3.txt\nsub/file2.txt\n'
  >  +  where b'tmptwvx8tf9/file.txt\ntmptwvx8tf9/sub\nsub/deep\ndeep/file3.txt\nsub/file2.txt\n' = CompletedProcess(args=['/workspace/executable', '--max-depth', '2'], returncode=0, stdout=b'tmptwvx8tf9/
- `tests.test_error_handling.test_permission_denied`
  > AssertionError: assert (2 == 0 or 2 == 1)
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b'usage: fd [OPTIONS] [PATTERN] [PATH]\n').returncode
  >  +  and   2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b'usage: fd [OPTIONS] [PATTERN] [PATH]\n').returncode
- *(... 370 more in this cluster)*

### `rc_mismatch_got2_want0` — 318 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_basic_invocation.test_no_arguments_lists_files`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b'usage: fd [OPTIONS] [PATTERN] [PATH]\n').returncode
- `tests.test_basic_invocation.test_empty_directory`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b'usage: fd [OPTIONS] [PATTERN] [PATH]\n').returncode
- `tests.test_completions.test_gen_completions_bash`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--gen-completions', 'bash'], returncode=2, stdout=b'', stderr=b'fd: unknown option: --gen-completions\nusage: fd [OPTIONS] [PATTERN] [PAT
- *(... 315 more in this cluster)*

### `string_output_mismatch` — 74 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_exact_outputs.test_exact_help_long_matches_fixture_bytes`
  > AssertionError: assert 'fd 8.7.0\n\n...int version\n' == 'A program to...p/fd/issues\n'
  >   
  >   - A program to find entries in your filesystem
  >   + fd 8.7.0
  >     
  >   - Usage: executable [OPTIONS] [pattern] [path]...
  >   + A simple, fast and user-friendly alternative to 'find'.
  >   + ...
- `eval.tests.test_help_exact_outputs.test_exact_help_short_matches_fixture_bytes`
  > AssertionError: assert 'fd 8.7.0\n\n...int version\n' == 'A program to...int version\n'
  >   
  >   - A program to find entries in your filesystem
  >   + fd 8.7.0
  >     
  >   - Usage: executable [OPTIONS] [pattern] [path]...
  >   + A simple, fast and user-friendly alternative to 'find'.
  >   + ...
- `eval.tests.test_fd_behavior.test_regex_anchors_match_whole_filename`
  > AssertionError: assert {'test_regex_...e2/alpha.txt'} == {'Alpha.TXT', 'alpha.txt'}
  >   
  >   Extra items in the left set:
  >   'test_regex_anchors_match_whole2/Alpha.TXT'
  >   'test_regex_anchors_match_whole2/alpha.txt'
  >   Extra items in the right set:
  >   'alpha.txt'
  >   'Alpha.TXT'...
- *(... 71 more in this cluster)*

### `rc_unexpected_zero` — 12 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_error_handling.test_invalid_type_value`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--type', 'invalid'], returncode=0, stdout=b'workspace/CHANGELOG.md\nworkspace/CONTRIBUTING.md\nworkspace/Cargo.lock\nworkspace/Cargo.toml
- `tests.test_error_handling.test_invalid_color_value`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--color', 'invalid'], returncode=0, stdout=b'workspace/CHANGELOG.md\nworkspace/CONTRIBUTING.md\nworkspace/Cargo.lock\nworkspace/Cargo.tom
- `tests.test_error_handling.test_missing_exec_command`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--exec'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 9 more in this cluster)*

### `rc_mismatch_got1_want0` — 9 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_basic_invocation.test_multiple_path_arguments`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'txt', '/tmp/tmpbh_7qnc6/dir1', '/tmp/tmpbh_7qnc6/dir2'], returncode=1, stdout=b'', stderr=b'fd: error: unexpected argument: /tmp/tmpbh_7q
- `tests.test_path_specification.test_multiple_path_arguments`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'file', '/tmp/tmpimslf6nh/dir1', '/tmp/tmpimslf6nh/dir2'], returncode=1, stdout=b'', stderr=b'fd: error: unexpected argument: /tmp/tmpimsl
- `eval.tests.test_argparse_validation.test_dash_dash_separator_allows_pattern_starting_with_dash`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '--', '-1', '-1', '.'], returncode=1, stdout='', stderr='fd: error: unexpected argument: .\n').returncode
- *(... 6 more in this cluster)*

### `rc_mismatch_got3_want1` — 9 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_edge_cases.test_case_sensitive_smart_case_uppercase_pattern`
  > AssertionError: assert 3 == 1
  >  +  where 3 = len(['test_case_sensitive_smart_case2/TEST.txt', 'test_case_sensitive_smart_case2/Test.txt', 'test_case_sensitive_smart_case2/test.txt'])
- `tests.test_exec.test_exec_batch_basic`
  > AssertionError: assert 3 == 1
  >  +  where 3 = len(['test_exec_batch_basic2/file1.txt', 'test_exec_batch_basic2/file2.txt', 'test_exec_batch_basic2/file3.txt'])
- `tests.test_exec.test_exec_batch_basename_placeholder`
  > AssertionError: assert 3 == 1
  >  +  where 3 = len(['{/}', 'test_exec_batch_basename_place2/file1.txt', 'test_exec_batch_basename_place2/file2.txt'])
- *(... 6 more in this cluster)*

### `rc_mismatch_got1_want2` — 7 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_extensions.test_extension_case_insensitive`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len(['tmpbxwxnyul/file.txt'])
- `eval.tests.test_argparse_validation.test_missing_value_for_value_taking_options[args0-a value is required for '--max-depth <depth>']`
  > AssertionError: assert 1 == 2
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '--max-depth'], returncode=1, stdout='', stderr='fd: error: --max-depth requires a value\n').returncode
- `eval.tests.test_argparse_validation.test_nonzero_integer_validation_threads_rejects_zero`
  > AssertionError: assert 1 == 2
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-j', '0', '-1', '.'], returncode=1, stdout='', stderr='fd: error: --threads must be positive\n').returncode
- *(... 4 more in this cluster)*

### `rc_mismatch_got4_want2` — 6 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_exec.test_exec_explicit_placeholder`
  > AssertionError: assert 4 == 2
  >  +  where 4 = len(['test_exec_explicit_placeholder2/file1.txt', 'test_exec_explicit_placeholder2/file1.txt', 'test_exec_explicit_placeholder2/file2.txt', 'test_exec_explicit_placeholder2/file2.txt'])
- `tests.test_exec.test_exec_basename_placeholder`
  > AssertionError: assert 4 == 2
  >  +  where 4 = len(['subdir/file2.txt', 'test_exec_basename_placeholder2/file1.txt', '{/}', '{/}'])
- `tests.test_exec.test_exec_parent_placeholder`
  > AssertionError: assert 4 == 2
  >  +  where 4 = len(['subdir/file2.txt', 'test_exec_parent_placeholder2/file1.txt', '{//}', '{//}'])
- *(... 3 more in this cluster)*

### `rc_mismatch_got2_want1` — 5 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_result_limiting.test_quiet_mode_no_match`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--quiet', 'nomatch'], returncode=2, stdout=b'', stderr=b'fd: unknown option: --quiet\nusage: fd [OPTIONS] [PATTERN] [PATH]\n').returncode
- `tests.test_edge_cases.test_quiet_with_no_match`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--quiet', 'nonexistent'], returncode=2, stdout=b'', stderr=b'fd: unknown option: --quiet\nusage: fd [OPTIONS] [PATTERN] [PATH]\n').return
- `tests.test_output_format.test_quiet_mode_no_match`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--quiet', 'nonexistent'], returncode=2, stdout=b'', stderr=b'fd: unknown option: --quiet\nusage: fd [OPTIONS] [PATTERN] [PATH]\n').return
- *(... 2 more in this cluster)*

### `rc_mismatch_got0_want1` — 5 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_edge_cases.test_invalid_glob_pattern`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--glob', '[invalid'], returncode=0, stdout='', stderr='').returncode
- `tests.test_edge_cases.test_invalid_time_syntax`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--changed-within', 'invalid'], returncode=0, stdout='', stderr='').returncode
- `tests.test_exec.test_exec_command_failure_exit_code`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'txt', '-x', 'false'], returncode=0, stdout='test_exec_command_failure_exit2/file1.txt\n', stderr='').returncode
- *(... 2 more in this cluster)*

### `rc_mismatch_got0_want2` — 4 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `eval.tests.test_argparse_validation.test_missing_value_for_value_taking_options[args5-a value is required for '--exec <cmd>...']`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-x'], returncode=0, stdout='workspace/CHANGELOG.md\nworkspace/CONTRIBUTING.md\nworkspace/Cargo.lock\nworkspace/Cargo.toml\nworkspace/Cros
- `eval.tests.test_argparse_validation.test_choice_options_reject_invalid_values[args2]`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--type', 'fd', '-1', '.'], returncode=0, stdout='workspace/CHANGELOG.md\n', stderr='').returncode
- `eval.tests.test_argparse_validation.test_owner_value_validation_rejects_unknown_user`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--owner', 'abc:', '-1', '.'], returncode=0, stdout='', stderr='').returncode
- *(... 1 more in this cluster)*

### `boolean_false` — 2 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_command_execution.test_exec_basename_placeholder`
  > assert False
  >  +  where False = any(<generator object test_exec_basename_placeholder.<locals>.<genexpr> at 0x7f763c4f9930>)
- `tests.test_exec.test_exec_absolute_vs_relative_paths`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7fcec0277d50>('./')
  >  +    where <built-in method startswith of str object at 0x7fcec0277d50> = 'test_exec_absolute_vs_relative2/file.txt'.startswith

### `bytes_output_mismatch` — 2 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_coverage_improvements.test_show_errors_permission_denied`
  > AssertionError: assert (b'Permission denied' in b'fd: unknown option: --show-errors\nusage: fd [OPTIONS] [PATTERN] [PATH]\n' or 2 == 0)
  >  +  where b'fd: unknown option: --show-errors\nusage: fd [OPTIONS] [PATTERN] [PATH]\n' = CompletedProcess(args=['/workspace/executable', '--show-errors'], returncode=2, stdout=b'', stderr=b'fd: unknow
  >  +  and   2 = CompletedProcess(args=['/workspace/executable', '--show-errors'], returncode=2, stdout=b'', stderr=b'fd: unknown option: --show-errors\nusage: fd [OPTIONS] [PATTERN] [PATH]\n').returncod
- `tests.test_edge_cases.test_exec_with_failing_command`
  > AssertionError: assert (0 != 0 or (0 == 0 and b'tmpn3sp2d9g/file.txt\n' == b''
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--exec', 'false'], returncode=0, stdout=b'tmpn3sp2d9g/file.txt\n', stderr=b'').returncode
  >  +  and   0 = CompletedProcess(args=['/workspace/executable', '--exec', 'false'], returncode=0, stdout=b'tmpn3sp2d9g/file.txt\n', stderr=b'').returncode
  >   
  >   Full diff:
  >   - b''
  >   + (b'tmpn3sp2d9g/file.txt\n')))

### `rc_mismatch_got1_want3` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_edge_cases.test_case_insensitive_flag_overrides_smart_case`
  > AssertionError: assert 1 == 3
  >  +  where 1 = len(['test_case_insensitive_flag_ove2/TEST.txt'])
- `tests.test_exec.test_exec_sequential_threads_1`
  > AssertionError: assert 1 == 3
  >  +  where 1 = len([''])

### `returned_none` — 1 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_behavior.test_help_long_usage_indentation_and_colon_format`
  > assert None
  >  +  where None = <function search at 0x7f2afd1c2680>('^Usage: executable', "fd 8.7.0\n\nA simple, fast and user-friendly alternative to 'find'.\n\nUsage: fd [OPTIONS] [PATTERN] [PATH]\n\nArguments:\n 
  >  +    where <function search at 0x7f2afd1c2680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE

### `rc_mismatch_got8_want4` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_harvest.test_exec`
  > AssertionError: assert 8 == 4
  >  +  where 8 = len(['test_exec2/a.foo', 'one/b.foo', 'two/C.Foo2', 'two/c.foo', 'test_exec2/a.foo', 'one/b.foo', ...])

### `missing_file` — 1 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_harvest.test_invalid_cwd`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_invalid_cwd2/deleted'

