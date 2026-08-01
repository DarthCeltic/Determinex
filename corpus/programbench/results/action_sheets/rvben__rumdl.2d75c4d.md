# Action Sheet — rvben__rumdl.2d75c4d

**Current:** 9.84%  (437/4443)
**Pass / Fail / Skip:** 437 / 761 / 30
**Gap to 100%:** 90.16 percentage points (4006 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_all_rules_comprehensive.test_all_output_formats`
  - reason: May crash worker in parallel execution
- `eval.tests.test_check_io.test_check_unreadable_file_is_error`
  - reason: Cannot make file unreadable in this environment (likely elevated privileges)
- `eval.tests.test_subcommand_dispatch.test_each_subcommand_has_help[NOTSET]`
  - reason: got empty parameter set for (subcmd)
- `tests.test_code_block_processor_gapfill.test_on_error_skip_continues_processing`
  - reason: gold-env-limitation: returncode -13 SIGPIPE when external tool scripts run
- `tests.test_code_block_processor_gapfill.test_multiple_tools_for_language_all_run`
  - reason: gold-env-limitation: returncode -13 SIGPIPE when external tool scripts run
- *(... 25 more skipped)*

## Failure clusters

761 failed tests grouped into 11 buckets (sorted by count).

### `other_assertion` — 383 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_help_flag`
  > AssertionError: assert b'Commands:' in b'rumdl 0.1.0 - bootstrap scaffold\n\nUsage: rumdl [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n'
  >  +  where b'rumdl 0.1.0 - bootstrap scaffold\n\nUsage: rumdl [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['/workspace/executabl
- `tests.test_basic_invocation.test_help_flag_short`
  > AssertionError: assert b'Commands:' in b'rumdl 0.1.0 - bootstrap scaffold\n\nUsage: rumdl [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n'
  >  +  where b'rumdl 0.1.0 - bootstrap scaffold\n\nUsage: rumdl [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['/workspace/executabl
- `tests.test_basic_invocation.test_version_subcommand`
  > AssertionError: assert b'rumdl' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', 'version'], returncode=0, stdout=b'', stderr=b'').stdout
- *(... 380 more in this cluster)*

### `rc_mismatch_got0_want1` — 107 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_additional_rules.test_md003_heading_style_atx`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', 'check', '/tmp/tmppygx84c9/test.md', '--enable', 'MD003', '--no-config'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_additional_rules.test_md004_ul_style_consistent`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', 'check', '/tmp/tmp0upq_5vt/test.md', '--enable', 'MD004', '--no-config'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_additional_rules.test_md031_fenced_code_blocks_surrounded_by_blanks`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', 'check', '/tmp/tmpttlh8o8u/test.md', '--enable', 'MD031', '--no-config'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 104 more in this cluster)*

### `string_output_mismatch` — 105 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_baseline_smoke.test_baseline_main_help_matches_fixture`
  > AssertionError: assert '\nUsage: rum...int version\n' == 'A fast Markd...int version\n'
  >   
  >   - A fast Markdown linter written in Rust (Ru(st) MarkDown Linter)
  >     
  >   + Usage: rumdl [OPTIONS] [ARGS]
  >   - Usage: executable [OPTIONS] <COMMAND>
  >   - 
  >   - Commands:...
- `eval.tests.test_help_baseline_smoke.test_baseline_check_help_matches_fixture`
  > AssertionError: assert '' == 'Lint Markdow... Print help\n'
  >   
  >   - Lint Markdown files and print warnings/errors
  >   - 
  >   - Usage: executable check [OPTIONS] [PATHS]...
  >   - 
  >   - Arguments:
  >   -   [PATHS]...  Files or directories to lint (use '-' for stdin)...
- `eval.tests.test_fmt_io.test_fmt_dash_reads_stdin_and_writes_formatted_to_stdout`
  > AssertionError: assert '' == '# H\n\ntext\n'
  >   
  >   - # H
  >   - 
  >   - text
- *(... 102 more in this cluster)*

### `rc_unexpected_zero` — 72 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_basic_invocation.test_invalid_subcommand`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'invalidcommand'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_check_command.test_check_single_file_with_issues`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'check', '/tmp/tmpreflzgp7/invalid.md'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_check_command.test_check_check_flag_needs_changes`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'check', '--check', '/tmp/tmprrkqwpxx/check_fail.md'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 69 more in this cluster)*

### `boolean_false` — 23 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_check_command.test_check_fix_flag`
  > AssertionError: assert False
  >  +  where False = <built-in method endswith of str object at 0x7f2c13611ac0>('\n')
  >  +    where <built-in method endswith of str object at 0x7f2c13611ac0> = '# Hello\nno newline'.endswith
- `tests.test_check_command.test_check_fix_short_flag`
  > AssertionError: assert False
  >  +  where False = <built-in method endswith of str object at 0x7f2c136121a0>('\n')
  >  +    where <built-in method endswith of str object at 0x7f2c136121a0> = '# Hello\nno newline'.endswith
- `tests.test_error_handling.test_fix_multiple_issues`
  > AssertionError: assert False
  >  +  where False = <built-in method endswith of str object at 0x7f2c12a7dc50>('\n')
  >  +    where <built-in method endswith of str object at 0x7f2c12a7dc50> = '# Test\n\n\n\nno newline'.endswith
- *(... 20 more in this cluster)*

### `json_output_missing_or_bad` — 20 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `tests.test_output_formats.test_output_format_json`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_output_formats.test_output_format_sarif`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_additional_features.test_rule_explain_in_json`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- *(... 17 more in this cluster)*

### `returned_none` — 19 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_check_subcommand.test_check_help_has_arguments_section`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7ff2a0e76680>('^Arguments:\\s*$', '', flags=re.MULTILINE)
  >  +    where <function search at 0x7ff2a0e76680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- `eval.tests.test_help_check_subcommand.test_check_help_has_options_section`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7ff2a0e76680>('^Options:\\s*$', '', flags=re.MULTILINE)
  >  +    where <function search at 0x7ff2a0e76680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- `eval.tests.test_help_check_subcommand.test_check_help_has_fail_on_possible_values`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7ff2a0e76680>('\\bany\\b', '')
  >  +    where <function search at 0x7ff2a0e76680> = re.search
- *(... 16 more in this cluster)*

### `rc_mismatch_got0_want2` — 14 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `eval.tests.test_args_parsing.test_unknown_or_missing_required_args[args2-2-unexpected argument]`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'check', '--badflag'], returncode=0, stdout='', stderr='').returncode
- `eval.tests.test_args_parsing.test_unknown_flag_tip_for_double_dash_passthrough`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'check', '--badflag'], returncode=0, stdout='', stderr='').returncode
- `eval.tests.test_args_parsing.test_missing_value_for_value_taking_flag[args0-a value is required for '--config <CONFIG>']`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'check', '--config'], returncode=0, stdout='', stderr='').returncode
- *(... 11 more in this cluster)*

### `rc_mismatch_got2_want0` — 13 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_basic_invocation.test_color_option_auto`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--color', 'auto', 'version'], returncode=2, stdout=b'', stderr=b"rumdl: unknown option: --color\nusage: rumdl [OPTIONS] [ARGS]\nTry 'rumd
- `tests.test_basic_invocation.test_color_option_always`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--color', 'always', 'version'], returncode=2, stdout=b'', stderr=b"rumdl: unknown option: --color\nusage: rumdl [OPTIONS] [ARGS]\nTry 'ru
- `tests.test_basic_invocation.test_color_option_never`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--color', 'never', 'version'], returncode=2, stdout=b'', stderr=b"rumdl: unknown option: --color\nusage: rumdl [OPTIONS] [ARGS]\nTry 'rum
- *(... 10 more in this cluster)*

### `missing_file` — 4 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_clean_cache.test_cache_version_isolation`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_cache_version_isolation2/.rumdl_cache'
- `tests.test_completions_schema.test_schema_generate_creates_valid_json_structure`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_schema_generate_creates_v2/rumdl.schema.json'
- `tests.test_completions_schema.test_schema_check_validates_json_semantically`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_schema_check_validates_js2/rumdl.schema.json'
- *(... 1 more in this cluster)*

### `bytes_output_mismatch` — 1 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `eval.tests.test_subcommand_dispatch.test_help_subcommand_routing`
  > AssertionError: assert b'rumdl 0.1.0...int version\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'rumdl 0.1.0 - bootstrap scaffold\n\nUsage: rumdl [OPTIONS] [ARGS]\n\nOptions'
  >   +  b':\n  -h, --help     Print help\n  -V, --version  Print version\n')

