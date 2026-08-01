# Action Sheet — simeg__eureka.df3796c

**Current:** 8.68%  (58/668)
**Pass / Fail / Skip:** 58 / 337 / 1
**Gap to 100%:** 91.32 percentage points (610 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_config_and_clear.test_clear_config_removes_file`
  - reason: test_clear_config_removes_file depends on test_first_time_setup_rejects_empty_and_relative_then_writes_config

## Failure clusters

337 failed tests grouped into 6 buckets (sorted by count).

### `rc_mismatch_got2_want0` — 181 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_config_management.test_clear_config_removes_config_file`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--clear-config'], returncode=2, stdout=b'', stderr=b'eureka: error: unrecognized argument: --clear-config\n').returncode
- `tests.test_config_management.test_clear_config_when_no_config_exists`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--clear-config'], returncode=2, stdout=b'', stderr=b'eureka: error: unrecognized argument: --clear-config\n').returncode
- `tests.test_edge_cases.test_view_and_clear_config_together`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--clear-config', '--view'], returncode=2, stdout=b'', stderr=b'eureka: error: unrecognized argument: --clear-config\n').returncode
- *(... 178 more in this cluster)*

### `other_assertion` — 133 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_help_flag`
  > AssertionError: assert b'Input and store your ideas without leaving the terminal' in b'eureka 0.1.0\n\nusage: eureka [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print v
  >  +  where b'eureka 0.1.0\n\nusage: eureka [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --verbose  Verbose\n  -q, --quiet    Quiet\n\n' = CompletedPr
- `tests.test_basic_invocation.test_help_flag_short`
  > AssertionError: assert b'Input and store your ideas without leaving the terminal' in b'eureka 0.1.0\n\nusage: eureka [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print v
  >  +  where b'eureka 0.1.0\n\nusage: eureka [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --verbose  Verbose\n  -q, --quiet    Quiet\n\n' = CompletedPr
- `tests.test_basic_invocation.test_help_mentions_pager_env`
  > AssertionError: assert b'$PAGER' in b'eureka 0.1.0\n\nusage: eureka [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --verbose  Verbose\n  -q, --quiet  
  >  +  where b'eureka 0.1.0\n\nusage: eureka [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --verbose  Verbose\n  -q, --quiet    Quiet\n\n' = CompletedPr
- *(... 130 more in this cluster)*

### `boolean_false` — 13 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_config_management.test_config_stored_in_xdg_config_home`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmp_r73m0ym/xdg/eureka/config.json').exists
- `tests.test_config_management.test_config_stored_in_home_when_xdg_unset`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmp7ej7sj0g/.config/eureka/config.json').exists
- `tests.test_config_management.test_first_time_setup_creates_config_directory`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpaaun3vkb/config/eureka').exists
- *(... 10 more in this cluster)*

### `missing_file` — 5 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_config_management.test_config_file_is_json_format`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpapa_hgmn/config/eureka/config.json'
- `tests.test_config_management.test_config_contains_repo_field`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpq6xfed93/config/eureka/config.json'
- `tests.test_setup_config.test_clear_config_removes_only_config_json_not_other_files`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_clear_config_removes_only2/eureka/other_data.txt'
- *(... 2 more in this cluster)*

### `string_output_mismatch` — 4 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_cli_help_version.test_help_exact_output`
  > AssertionError: assert 'eureka 0.1.0...    Quiet\n\n' == 'Input and st...int version\n'
  >   
  >   - Input and store your ideas without leaving the terminal
  >   + eureka 0.1.0
  >     
  >   - Usage: executable [OPTIONS]
  >   + usage: eureka [OPTIONS] [ARGS]
  >     ...
- `eval.tests.test_cli_help_version.test_version_exact_output`
  > AssertionError: assert 'eureka 0.1.0\n' == 'eureka 2.0.0\n'
  >   
  >   - eureka 2.0.0
  >   ?        ^ ^
  >   + eureka 0.1.0
  >   ?        ^ ^
- `tests.test_io_errors.test_version_flag_displays_version_info`
  > AssertionError: assert 'eureka 0.1.0' == 'eureka 2.0.0'
  >   
  >   - eureka 2.0.0
  >   ?        ^  --
  >   + eureka 0.1.0
  >   ?        ^^^
- *(... 1 more in this cluster)*

### `rc_mismatch_got0_want2` — 1 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_help_version.TestHelpVersion.test_invalid_short_flag`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-x'], returncode=0, stdout='', stderr='').returncode

