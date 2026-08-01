# Action Sheet — tree-sitter__tree-sitter.5e23cca

**Current:** 19.07%  (308/1615)
**Pass / Fail / Skip:** 308 / 375 / 2
**Gap to 100%:** 80.93 percentage points (1307 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_subcommand_dispatch.test_subcommand_help_recognized[NOTSET]`
  - reason: got empty parameter set for (subcmd)
- `eval.tests.test_config_and_errors.test_init_config_second_run_requires_removing_existing_config`
  - reason: test_init_config_second_run_requires_removing_existing_config depends on test_init_config_creates_file

## Failure clusters

375 failed tests grouped into 7 buckets (sorted by count).

### `other_assertion` — 231 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_advanced_features.test_parse_output_formats`
  > AssertionError: assert (b'<' in b'' or 0 > 0)
  >  +  where 0 = len(b'')
- `tests.test_advanced_features.test_parse_json_summary_detailed`
  > AssertionError: assert 0 > 0
  >  +  where 0 = len(b'')
- `tests.test_advanced_features.test_parse_stat_detailed`
  > AssertionError: assert 0 > 0
  >  +  where 0 = len(b'')
- *(... 228 more in this cluster)*

### `rc_unexpected_zero` — 75 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_basic_invocation.test_invalid_command`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'invalid-command'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_build.test_build_missing_parser`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'build'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_coverage_boosters.test_parse_with_lib_path`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'parse', '/tmp/tmp0ddukyh6/test.txt', '--lib-path', '/tmp/nonexistent.so', '--lang-name', 'test'], returncode=0, stdout=b'', stderr=b'').r
- *(... 72 more in this cluster)*

### `string_output_mismatch` — 35 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_advanced_features.test_version_all_bump_types`
  > AssertionError: assert '1.0.0' == '1.0.1'
  >   
  >   - 1.0.1
  >   ?     ^
  >   + 1.0.0
  >   ?     ^
- `tests.test_edge_cases.test_version_with_zero_version`
  > AssertionError: assert '0.0.0' == '0.0.1'
  >   
  >   - 0.0.1
  >   ?     ^
  >   + 0.0.0
  >   ?     ^
- `tests.test_version.test_version_bump_patch`
  > AssertionError: assert '1.2.3' == '1.2.4'
  >   
  >   - 1.2.4
  >   ?     ^
  >   + 1.2.3
  >   ?     ^
- *(... 32 more in this cluster)*

### `boolean_false` — 26 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_advanced_features.test_generate_with_complex_grammar`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = ((PosixPath('/tmp/tmpqijil0a_/complex') / 'src') / 'parser.c').exists
- `tests.test_advanced_features.test_generate_disable_optimizations_detailed`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = ((PosixPath('/tmp/tmp_qo0s9d8/no_opt') / 'src') / 'parser.c').exists
- `tests.test_edge_cases.test_generate_with_minimal_grammar`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = ((PosixPath('/tmp/tmpqaoqaw9v/minimal') / 'src') / 'grammar.json').exists
- *(... 23 more in this cluster)*

### `missing_file` — 3 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_init_config.test_init_config_structure`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmp_17v8l58/.config/tree-sitter/config.json'
- `tests.test_init_config.test_init_config_valid_json`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpaoqq0q_y/.config/tree-sitter/config.json'
- `tests.test_init_config.test_init_config_structure`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpinioljsz/.config/tree-sitter/config.json'

### `returned_none` — 3 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_help_main.test_main_usage_synopsis_is_command_dispatch`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f7c1366a680>('^Usage: executable <COMMAND>\\s*$', 'tree-sitter 0.1.0 - bootstrap scaffold\n\nUsage: tree-sitter [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     P
  >  +    where <function search at 0x7f7c1366a680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- `tests.test_help_main.test_main_help_lists_expected_commands`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f7c1366a680>('^\\s*init\\-config\\b', 'tree-sitter 0.1.0 - bootstrap scaffold\n\nUsage: tree-sitter [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n 
  >  +    where <function search at 0x7f7c1366a680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- `tests.test_help_subcommands.test_init_help_usage_line`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f7c1366a680>('^Usage: executable init \\[OPTIONS\\]\\s*$', '', flags=re.MULTILINE)
  >  +    where <function search at 0x7f7c1366a680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE

### `rc_mismatch_got0_want1` — 2 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_cli_io.test_parse_nonexistent_path_errors_to_stderr_exit1`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'parse', '/no/such/file'], returncode=0, stdout=b'', stderr=b'').returncode
- `eval.tests.test_config_and_errors.test_parse_unknown_extension_error_message`
  > assert 0 == 1

