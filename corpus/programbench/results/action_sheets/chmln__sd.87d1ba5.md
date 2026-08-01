# Action Sheet — chmln__sd.87d1ba5

**Current:** 3.87%  (48/1241)
**Pass / Fail / Skip:** 48 / 816 / 5
**Gap to 100%:** 96.13 percentage points (1193 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_cli.test_correctly_fails_on_unreadable_file`
  - reason: root bypasses file permission restrictions
- `tests.test_cli.test_reports_errors_on_atomic_file_swap_creation_failure`
  - reason: root bypasses file permission restrictions
- `tests.test_harvest.test_ambiguous_replace_ensure_styling`
  - reason: Original test is ignored - TODO: wait for proper colorization
- `tests.test_harvest.test_correctly_fails_on_unreadable_file`
  - reason: Test requires non-root user for permission checks
- `tests.test_harvest.test_reports_errors_on_atomic_file_swap_creation_failure`
  - reason: Test requires non-root user for permission checks

## Failure clusters

816 failed tests grouped into 7 buckets (sorted by count).

### `rc_mismatch_got1_want0` — 444 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_additional_coverage.test_stdin_with_preview_flag_position`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', 'test', 'TEST', '-p'], returncode=1, stdout=b'', stderr=b'Traceback (most recent call last):\n  File "/workspace/main.py", line 48, in <module>\n  
- `tests.test_additional_coverage.test_empty_file_multiple`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', 'test', 'replace', '/tmp/tmp_bi67z9w/empty1.txt', '/tmp/tmp_bi67z9w/empty2.txt'], returncode=1, stdout=b'', stderr=b'Traceback (most recent call la
- `tests.test_additional_coverage.test_capture_group_not_in_pattern`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', 'test', '$1'], returncode=1, stdout=b'', stderr=b'Traceback (most recent call last):\n  File "/workspace/main.py", line 48, in <module>\n    sys.ex
- *(... 441 more in this cluster)*

### `rc_mismatch_got2_want0` — 236 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_additional_coverage.test_preview_stdin_no_separator`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '-p', 'test', 'TEST'], returncode=2, stdout=b'', stderr=b"sd: unknown option: -p\nusage: sd [OPTIONS] [ARGS]\nTry 'sd --help' for more information.
- `tests.test_additional_coverage.test_flag_combinations_all`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '-f', 'ims', 'test.*end', 'X'], returncode=2, stdout=b'', stderr=b"sd: unknown option: -f\nusage: sd [OPTIONS] [ARGS]\nTry 'sd --help' for more inf
- `tests.test_additional_coverage.test_fixed_strings_with_flags`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '-F', '-f', 'i', 'TEST', 'replaced'], returncode=2, stdout=b'', stderr=b"sd: unknown option: -F\nusage: sd [OPTIONS] [ARGS]\nTry 'sd --help' for mo
- *(... 233 more in this cluster)*

### `other_assertion` — 105 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic.test_no_arguments`
  > assert b'required arguments were not provided' in b"usage: sd [OPTIONS] [ARGS]\nTry 'sd --help' for more information.\n"
  >  +  where b"usage: sd [OPTIONS] [ARGS]\nTry 'sd --help' for more information.\n" = CompletedProcess(args=['./executable'], returncode=2, stdout=b'', stderr=b"usage: sd [OPTIONS] [ARGS]\nTry 'sd --help
- `tests.test_basic.test_help_flag`
  > AssertionError: assert b'sd v' in b'sd 0.1.0 - bootstrap scaffold\n\nUsage: sd [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n'
  >  +  where b'sd 0.1.0 - bootstrap scaffold\n\nUsage: sd [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['./executable', '--help'], 
- `tests.test_basic.test_help_short_flag`
  > AssertionError: assert b'sd v' in b'sd 0.1.0 - bootstrap scaffold\n\nUsage: sd [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n'
  >  +  where b'sd 0.1.0 - bootstrap scaffold\n\nUsage: sd [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['./executable', '-h'], retu
- *(... 102 more in this cluster)*

### `string_output_mismatch` — 16 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_additional_coverage.test_file_with_replacement_error_continues`
  > AssertionError: assert 'hello world' == 'goodbye world'
  >   
  >   - goodbye world
  >   + hello world
- `eval.tests.test_sd_behavior.test_version_exact`
  > AssertionError: assert 'sd 0.1.0\n' == 'sd 1.0.0\n'
  >   
  >   - sd 1.0.0
  >   ?       --
  >   + sd 0.1.0
  >   ?    ++
- `tests.test_errors.test_nonexistent_file`
  > assert 'Traceback (m...tr, not bytes' == 'error: inval...tent/file.txt'
  >   
  >   - error: invalid path: /nonexistent/file.txt
  >   + Traceback (most recent call last):
  >   +   File "/workspace/main.py", line 48, in <module>
  >   +     sys.exit(main())
  >   +   File "/workspace/main.py", line 41, in main
  >   +     output_data = input_data.replace(b'sd v', b'')
- *(... 13 more in this cluster)*

### `rc_mismatch_got1_want2` — 12 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic.test_missing_replace_argument`
  > assert 1 == 2
  >  +  where 1 = CompletedProcess(args=['./executable', 'pattern'], returncode=1, stdout=b'', stderr=b'Traceback (most recent call last):\n  File "/workspace/main.py", line 48, in <module>\n    sys.exit(
- `tests.test_argument_parsing.TestRequiredArguments.test_only_find_argument`
  > assert 1 == 2
- `eval.tests.test_argparse_validation.test_missing_required_positionals[args1-substrings1]`
  > assert 1 == 2
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'foo'], returncode=1, stdout='', stderr='Traceback (most recent call last):\n  File "/workspace/main.py", line 48, in <module>\n    sys.ex
- *(... 9 more in this cluster)*

### `bytes_output_mismatch` — 2 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_subcommand_dispatch.TestNoSubcommandSpecificHelp.test_help_is_consistent_regardless_of_first_arg`
  > AssertionError: assert b'sd 0.1.0 - ...int version\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'sd 0.1.0 - bootstrap scaffold\n\nUsage: sd [OPTIONS] [ARGS]\n\nOptions:\n'
  >   +  b'  -h, --help     Print help\n  -V, --version  Print version\n')
- `tests.test_io_modes.test_invalid_path_error`
  > assert b'Traceback (..., not bytes\n' == b'error: inva...th/file.txt\n'
  >   
  >   At index 0 diff: b'T' != b'e'
  >   
  >   Full diff:
  >   - (b'error: invalid path: /nonexistent/path/file.txt\n')
  >   + (b'Traceback (most recent call last):\n  File "/workspace/main.py", line 48,'
  >   +  b' in <module>\n    sys.exit(main())\n  File "/workspace/main.py", line 41, '

### `uncategorized` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_io_modes.test_symlink_target_is_modified`
  > FileExistsError: [Errno 17] File exists: '/tmp/tmpem6gyopk' -> '/tmp/link_to_file.txt'

