# Action Sheet — jarun__nnn.cb2c535

**Current:** 26.31%  (377/1433)
**Pass / Fail / Skip:** 377 / 644 / 5
**Gap to 100%:** 73.69 percentage points (1056 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_basic_navigation.test_parent_directory_navigation`
  - reason: test_parent_directory_navigation depends on test_enter_directory
- `tests.test_display_modes.test_hide_hidden_files_again`
  - reason: test_hide_hidden_files_again depends on test_show_hidden_files
- `tests.test_sorting.test_sort_by_size`
  - reason: test_sort_by_size depends on test_sort_menu_opens
- `tests.test_sorting.test_sort_by_time`
  - reason: test_sort_by_time depends on test_sort_menu_opens
- `tests.test_sorting.test_sort_by_extension`
  - reason: test_sort_by_extension depends on test_sort_menu_opens

## Failure clusters

644 failed tests grouped into 10 buckets (sorted by count).

### `other_assertion` — 485 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_01_basic.test_help_short_flag`
  > AssertionError: assert b'usage: nnn [OPTIONS] [PATH]' in b'nnn 0.1.0 - bootstrap scaffold\n\nUsage: nnn [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n'
  >  +  where b'nnn 0.1.0 - bootstrap scaffold\n\nUsage: nnn [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['/workspace/executable', 
- `tests.test_01_basic.test_invalid_short_option`
  > assert (b'invalid' in b"nnn: unknown option: -z\nusage: nnn [options] [args]\ntry 'nnn --help' for more information.\n" or b'usage:' in b'')
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', '-Z'], returncode=2, stdout=b'', stderr=b"nnn: unknown option: -Z\nusage: nnn [OPTIONS] [ARGS]\nTry 'nnn --help' for more information.\n
- `tests.test_01_basic.test_help_contains_all_flags`
  > AssertionError: Flag -a not in help
  > assert '-a' in 'nnn 0.1.0 - bootstrap scaffold\n\nUsage: nnn [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n'
- *(... 482 more in this cluster)*

### `rc_mismatch_got2_want0` — 76 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_01_basic.test_help_as_flag_cluster_shows_help`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-help'], returncode=2, stdout=b'', stderr=b"nnn: unknown option: -help\nusage: nnn [OPTIONS] [ARGS]\nTry 'nnn --help' for more informatio
- `tests.test_01_basic.test_key_collision_check`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-K'], returncode=2, stdout=b'', stderr=b"nnn: unknown option: -K\nusage: nnn [OPTIONS] [ARGS]\nTry 'nnn --help' for more information.\n")
- `tests.test_02_fifo_flag.test_fifo_flag_value_0`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-F', '0', '-V'], returncode=2, stdout=b'', stderr=b"nnn: unknown option: -F\nusage: nnn [OPTIONS] [ARGS]\nTry 'nnn --help' for more infor
- *(... 73 more in this cluster)*

### `returned_none` — 23 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_basic.test_version_flag`
  > AssertionError: assert None
  >  +  where None = <function match at 0x7f088c636170>(b'\\d+\\.\\d+', b'nnn 0.1.0')
  >  +    where <function match at 0x7f088c636170> = re.match
  >  +    and   b'nnn 0.1.0' = <built-in method strip of bytes object at 0x7f088b4738d0>()
  >  +      where <built-in method strip of bytes object at 0x7f088b4738d0> = b'nnn 0.1.0\n'.strip
  >  +        where b'nnn 0.1.0\n' = CompletedProcess(args=['./executable', '-V'], returncode=0, stdout=b'nnn 0.1.0\n', stderr=b'').stdout
- `tests.test_basic.test_version_flag_ignores_other_arguments`
  > AssertionError: assert None
  >  +  where None = <function match at 0x7f088c636170>(b'\\d+\\.\\d+', b'nnn 0.1.0')
  >  +    where <function match at 0x7f088c636170> = re.match
  >  +    and   b'nnn 0.1.0' = <built-in method strip of bytes object at 0x7f0889fe9620>()
  >  +      where <built-in method strip of bytes object at 0x7f0889fe9620> = b'nnn 0.1.0\n'.strip
  >  +        where b'nnn 0.1.0\n' = CompletedProcess(args=['./executable', '-V', '/tmp', '-H'], returncode=0, stdout=b'nnn 0.1.0\n', stderr=b'').stdout
- `tests.test_version_output.test_version_flag_V`
  > AssertionError: assert None
  >  +  where None = <function match at 0x7f088c636170>(b'^\\d+\\.\\d+', b'nnn 0.1.0\n')
  >  +    where <function match at 0x7f088c636170> = re.match
  >  +    and   b'nnn 0.1.0\n' = CompletedProcess(args=['./executable', '-V'], returncode=0, stdout=b'nnn 0.1.0\n', stderr=b'').stdout
- *(... 20 more in this cluster)*

### `string_output_mismatch` — 23 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_argparse_validation.test_F_accepts_attached_value_with_equals_and_without`
  > AssertionError: assert 'nnn: unknown...nformation.\n' == 'nnn: unknown...nformation.\n'
  >   
  >   - nnn: unknown option: -F1
  >   + nnn: unknown option: -F=1
  >   ?                        +
  >     usage: nnn [OPTIONS] [ARGS]
  >     Try 'nnn --help' for more information.
- `eval.tests.test_argparse_validation.test_T_accepts_value_in_separate_arg_attached_or_equals`
  > AssertionError: assert 'nnn: unknown...nformation.\n' == 'nnn: unknown...nformation.\n'
  >   
  >   - nnn: unknown option: -Tz
  >   ?                        -
  >   + nnn: unknown option: -T
  >     usage: nnn [OPTIONS] [ARGS]
  >     Try 'nnn --help' for more information.
- `eval.tests.test_argparse_validation.test_combined_short_flags_with_value_tz_equivalent_to_t_space_z`
  > AssertionError: assert 'nnn: unknown...nformation.\n' == 'nnn: unknown...nformation.\n'
  >   
  >   - nnn: unknown option: -t
  >   + nnn: unknown option: -tz
  >   ?                        +
  >     usage: nnn [OPTIONS] [ARGS]
  >     Try 'nnn --help' for more information.
- *(... 20 more in this cluster)*

### `rc_unexpected_zero` — 9 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_01_basic.test_double_dash_help_invalid`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--help'], returncode=0, stdout=b'nnn 0.1.0 - bootstrap scaffold\n\nUsage: nnn [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n
- `tests.test_basic.test_long_flag_format`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '--help'], returncode=0, stdout=b'nnn 0.1.0 - bootstrap scaffold\n\nUsage: nnn [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --v
- `tests.test_invalid_options.test_double_dash_help`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '--help'], returncode=0, stdout=b'nnn 0.1.0 - bootstrap scaffold\n\nUsage: nnn [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --v
- *(... 6 more in this cluster)*

### `uncategorized` — 8 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_flag_combinations.test_multiple_boolean_flags`
  > NameError: name 'output' is not defined
- `tests.test_flag_combinations.test_flags_with_values`
  > NameError: name 'output' is not defined
- `tests.test_flag_combinations.test_detail_and_hidden`
  > NameError: name 'output' is not defined
- *(... 5 more in this cluster)*

### `rc_mismatch_got2_want1` — 7 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_flag_combinations.test_regex_and_fuzzy_conflict`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['./executable', '-gz'], returncode=2, stdout=b'', stderr=b"nnn: unknown option: -gz\nusage: nnn [OPTIONS] [ARGS]\nTry 'nnn --help' for more information.\n").return
- `tests.test_flag_combinations.test_fuzzy_and_regex_conflict`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['./executable', '-zg'], returncode=2, stdout=b'', stderr=b"nnn: unknown option: -zg\nusage: nnn [OPTIONS] [ARGS]\nTry 'nnn --help' for more information.\n").return
- `tests.test_terminal_required.test_with_flags_still_fails`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['./executable', '-d', '/tmp/tmps8kuimcf'], returncode=2, stdout=b'', stderr=b"nnn: unknown option: -d\nusage: nnn [OPTIONS] [ARGS]\nTry 'nnn --help' for more infor
- *(... 4 more in this cluster)*

### `bytes_output_mismatch` — 5 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_01_basic.test_version_output`
  > AssertionError: assert b'nnn 0.1.0' == b'5.2'
  >   
  >   At index 0 diff: b'n' != b'5'
  >   
  >   Full diff:
  >   - b'5.2'
  >   + (b'nnn 0.1.0')
- `tests.test_14_additional_env_vars.test_nnn_fcolors_short`
  > AssertionError: assert b'nnn 0.1.0' == b'5.2'
  >   
  >   At index 0 diff: b'n' != b'5'
  >   
  >   Full diff:
  >   - b'5.2'
  >   + (b'nnn 0.1.0')
- `tests.test_14_additional_env_vars.test_nnnlvl_nested`
  > AssertionError: assert b'nnn 0.1.0' == b'5.2'
  >   
  >   At index 0 diff: b'n' != b'5'
  >   
  >   Full diff:
  >   - b'5.2'
  >   + (b'nnn 0.1.0')
- *(... 2 more in this cluster)*

### `rc_mismatch_got0_want1` — 5 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_terminal_required.test_exits_with_error_no_terminal`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', '/tmp/tmpmak04pnz'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_terminal_required.test_empty_directory_shows_entries`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', '/tmp/tmphztnwxod'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_terminal_required.test_non_empty_directory_behavior`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', '/tmp/tmpa871teie'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 2 more in this cluster)*

### `boolean_false` — 3 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `eval.tests.test_help_output.test_help_precedence_over_invalid_flag_combo`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7fdc0670d5f0>('usage:')
  >  +    where <built-in method startswith of str object at 0x7fdc0670d5f0> = 'nnn 0.1.0 - bootstrap scaffold\n\nUsage: nnn [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Pri
  >  +      where 'nnn 0.1.0 - bootstrap scaffold\n\nUsage: nnn [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['/workspace/executable
- `tests.test_batch_ops.test_copy_as_multiple_files`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = (PosixPath('/tmp/nnn_batch_9h0dz0dh/testdir') / 'file1.txt_copy').exists
- `tests.test_batch_ops.test_batch_rename_unicode_filenames`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = (PosixPath('/tmp/nnn_batch_2l6dwj3g/testdir') / 'café.txt_renamed').exists

