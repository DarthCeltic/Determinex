# Action Sheet — yaa110__nomino.f892499

**Current:** 8.93%  (36/403)
**Pass / Fail / Skip:** 36 / 302 / 0
**Gap to 100%:** 91.07 percentage points (367 tests)

## Failure clusters

302 failed tests grouped into 12 buckets (sorted by count).

### `other_assertion` — 118 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_no_arguments_produces_error`
  > AssertionError: assert (b'error' in b'' or b'error' in b'usage: nomino [options] [args]\n')
  >  +  where b'' = <built-in method lower of bytes object at 0x7f6042544030>()
  >  +    where <built-in method lower of bytes object at 0x7f6042544030> = b''.lower
  >  +      where b'' = CompletedProcess(args=['./executable'], returncode=2, stdout=b'', stderr=b'usage: nomino [OPTIONS] [ARGS]\n').stdout
  >  +  and   b'usage: nomino [options] [args]\n' = <built-in method lower of bytes object at 0x7f604116b830>()
  >  +    where <built-in method lower of bytes object at 0x7f604116b830> = b'usage: nomino [OPTIONS] [ARGS]\n'.lower
  >  +      where b'usage: nomino [OPTIONS] [ARGS]\n' = CompletedProcess(args=['./executable'], returncode=2, stdout=b'', stderr=b'usage: nomino [OPTIONS] [ARGS]\n').stderr
- `tests.test_basic_invocation.test_help_flag_long`
  > AssertionError: assert b'Usage:' in b'nomino 0.1.0\n\nusage: nomino [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --verbose  Verbose\n  -q, --quiet  
  >  +  where b'nomino 0.1.0\n\nusage: nomino [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --verbose  Verbose\n  -q, --quiet    Quiet\n\n' = CompletedPr
- `tests.test_basic_invocation.test_help_flag_short`
  > AssertionError: assert b'Usage:' in b'nomino 0.1.0\n\nusage: nomino [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --verbose  Verbose\n  -q, --quiet  
  >  +  where b'nomino 0.1.0\n\nusage: nomino [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --verbose  Verbose\n  -q, --quiet    Quiet\n\n' = CompletedPr
- *(... 115 more in this cluster)*

### `string_output_mismatch` — 99 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_file_handling.test_overwrite_mode`
  > AssertionError: assert 'existing' == 'data1'
  >   
  >   - data1
  >   + existing
- `eval.tests.test_help_usage.test_help_title_line_present`
  > AssertionError: assert 'nomino 0.1.0' == 'Batch rename...or developers'
  >   
  >   - Batch rename utility for developers
  >   + nomino 0.1.0
- `eval.tests.test_help_usage.test_short_help_exact_fixture_match`
  > AssertionError: assert 'nomino 0.1.0...    Quiet\n\n' == 'Batch rename...nformation.\n'
  >   
  >   - Batch rename utility for developers
  >   + nomino 0.1.0
  >     
  >   + usage: nomino [OPTIONS] [ARGS]
  >   - Usage: executable [OPTIONS] [[SOURCE] OUTPUT]...
  >   - ...
- *(... 96 more in this cluster)*

### `missing_file` — 25 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `eval.tests.test_rename_regex.test_regex_subdir_depth_2`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_regex_subdir_depth_22/01'
- `eval.tests.test_rename_regex.test_regex_subdir_max_depth_2_with_depth_3`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_regex_subdir_max_depth_2_2/01'
- `tests.test_flags.test_map_output_json_structure`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_map_output_json_structure2/map.json'
- *(... 22 more in this cluster)*

### `rc_mismatch_got0_want1` — 16 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `eval.tests.test_argparse_validation.test_positional_source_only_is_not_enough`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'a'], returncode=0, stdout='', stderr='').returncode
- `eval.tests.test_argparse_validation.test_too_many_positionals_with_sort_is_rejected`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-t', '-s', 'asc', '{1}', 'extra'], returncode=0, stdout='', stderr='').returncode
- `eval.tests.test_argparse_validation.test_output_only_without_mode_is_rejected`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-t', '{1}'], returncode=0, stdout='', stderr='').returncode
- *(... 13 more in this cluster)*

### `boolean_false` — 15 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_edge_cases.test_binary_file_content`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmp42w3clu0/renamed.dat').exists
- `tests.test_file_handling.test_mkdir_flag`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpjt1f8t29/new/sub/dir/renamed.txt').exists
  >  +      where PosixPath('/tmp/tmpjt1f8t29/new/sub/dir/renamed.txt') = Path('/tmp/tmpjt1f8t29', 'new', 'sub', 'dir', 'renamed.txt')
  >  +        where '/tmp/tmpjt1f8t29' = path()
  >  +          where path = <test_file_handling.TempFiles object at 0x7f60406db5e0>.path
- `tests.test_file_handling.test_generate_map_file`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpfa0jexv2/output.json').exists
- *(... 12 more in this cluster)*

### `rc_unexpected_zero` — 11 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_edge_cases.test_invalid_directory`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '-d', '/nonexistent/directory/path', '-s', 'asc', '{}.txt'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_edge_cases.test_generate_to_invalid_path`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '-g', '/invalid/path/output.json', '-d', '/tmp/tmp5d06p_r5', '-s', 'asc', '{}'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_map_mode.test_map_missing_file`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '-m', 'nonexistent.json', '-d', '/tmp/tmpz1ksz1ug'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 8 more in this cluster)*

### `rc_mismatch_got2_want1` — 9 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_argparse_validation.test_empty_args_requires_mode`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout='', stderr='usage: nomino [OPTIONS] [ARGS]\n').returncode
- `eval.tests.test_cli_errors.test_no_args_prints_error_and_usage_hint`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b'usage: nomino [OPTIONS] [ARGS]\n').returncode
- `tests.test_errors.test_invalid_map_malformed_json`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['./executable', '--map', '/workspace/eval/test_resources/test_errors/invalid_map.json'], returncode=2, stdout='', stderr='nomino: error: unrecognized argument: --m
- *(... 6 more in this cluster)*

### `rc_mismatch_got2_want0` — 3 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_map_mode.test_map_from_file_alias`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--from-file', '/tmp/tmpf115ltk6/map.json', '-d', '/tmp/tmpf115ltk6'], returncode=2, stdout=b'', stderr=b'nomino: error: unrecognized argument: --f
- `tests.test_regex_mode.test_regex_dry_run_alias`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--dry-run', '-d', '/tmp/tmplx4evjm4', '-r', 'file(\\d+)', 'new{}'], returncode=2, stdout=b'', stderr=b'nomino: error: unrecognized argument: --dry
- `tests.test_errors.test_map_mode_uses_json_mappings`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--map', '/tmp/pytest-of-root/pytest-0/test_map_mode_uses_json_mappin2/map.json', '-d', '/tmp/pytest-of-root/pytest-0/test_map_mode_uses_json_mappi

### `bytes_output_mismatch` — 2 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `eval.tests.test_cli_golden.test_help_exact`
  > assert b'nomino 0.1....    Quiet\n\n' == b"Batch renam...nformation.\n"
  >   
  >   At index 0 diff: b'n' != b'B'
  >   
  >   Full diff:
  >   + (b'nomino 0.1.0\n\nusage: nomino [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help '
  >   +  b'    Print help\n  -V, --version  Print version\n  -v, --verbose  Verbose\n '
  >   +  b' -q, --quiet    Quiet\n\n')...
- `eval.tests.test_cli_golden.test_version_exact`
  > AssertionError: assert b'nomino 0.1.0\n' == b'nomino 1.6.4\n'
  >   
  >   At index 7 diff: b'0' != b'1'
  >   
  >   Full diff:
  >   - (b'nomino 1.6.4\n')
  >   ?             ^^^
  >   + (b'nomino 0.1.0\n')

### `rc_mismatch_got0_want4` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_errors.test_sort_asc_orders_files_naturally`
  > assert 0 == 4
  >  +  where 0 = len([])
- `tests.test_errors.test_sort_desc_orders_files_reverse_naturally`
  > assert 0 == 4
  >  +  where 0 = len([])

### `rc_mismatch_got0_want2` — 1 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `eval.tests.test_argparse_validation.test_missing_value_for_regex_errors`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-r'], returncode=0, stdout='', stderr='').returncode

### `returned_none` — 1 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_usage.test_help_contains_arguments_section`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7fed23202680>('^Arguments:\\s*$', 'nomino 0.1.0\n\nusage: nomino [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v,
  >  +    where <function search at 0x7fed23202680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE

