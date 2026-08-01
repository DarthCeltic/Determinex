# Action Sheet — typst__typst.88356d0

**Current:** 0.79%  (16/2027)
**Pass / Fail / Skip:** 16 / 724 / 3
**Gap to 100%:** 99.21 percentage points (2011 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_subcommand_dispatch.test_subcommand_help_recognized[NOTSET]`
  - reason: got empty parameter set for (subcmd)
- `eval.tests.test_subcommand_dispatch.test_subcommand_alias_routes_to_same_help[NOTSET]`
  - reason: got empty parameter set for (cmd, alias)
- `eval.tests.test_eval_behavior.test_eval_pretty_json_exact_formatting`
  - reason: test_eval_pretty_json_exact_formatting depends on test_eval_json_object_default

## Failure clusters

724 failed tests grouped into 12 buckets (sorted by count).

### `other_assertion` — 231 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_additional_coverage.test_eval_sys_version`
  > AssertionError: assert ('0.14.2' in '' or 'version' in '')
  >  +  where '' = <built-in method lower of str object at 0x7f2652620030>()
  >  +    where <built-in method lower of str object at 0x7f2652620030> = ''.lower
- `tests.test_additional_coverage.test_eval_boolean_operations`
  > AssertionError: assert 'false' in ''
  >  +  where '' = <built-in method lower of str object at 0x7f2652620030>()
  >  +    where <built-in method lower of str object at 0x7f2652620030> = ''.lower
- `tests.test_additional_coverage.test_eval_comparison_operations`
  > AssertionError: assert 'true' in ''
  >  +  where '' = <built-in method lower of str object at 0x7f2652620030>()
  >  +    where <built-in method lower of str object at 0x7f2652620030> = ''.lower
- *(... 228 more in this cluster)*

### `boolean_false` — 211 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_additional_coverage.test_compile_with_timings`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpn_99p3tp/output.pdf').exists
- `tests.test_advanced_compile.test_compile_html_format_with_feature`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmp7mjeunib/output.html').exists
- `tests.test_advanced_compile.test_compile_multipage_svg_template_simple`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpch00r084/page-1.svg').exists
- *(... 208 more in this cluster)*

### `string_output_mismatch` — 88 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_baseline.test_baseline_main_help_exact_match`
  > AssertionError: assert 'typst 0.1.0 ...int version\n' == 'Typst 0.14.2....typst.app/\n'
  >   
  >   - Typst 0.14.2 (c064a23d)
  >   + typst 0.1.0 - bootstrap scaffold
  >     
  >   + Usage: typst [OPTIONS] [ARGS]
  >   - Usage: executable [OPTIONS] <COMMAND>
  >   - ...
- `eval.tests.test_help_baseline.test_baseline_compile_help_exact_match`
  > assert 'typst 0.1.0 ...int version\n' == "Compiles an ... with '-h')\n"
  >   
  >   - Compiles an input file into a supported output format
  >   + typst 0.1.0 - bootstrap scaffold
  >     
  >   + Usage: typst [OPTIONS] [ARGS]
  >   - Usage: executable compile [OPTIONS] <INPUT> [OUTPUT]
  >   - ...
- `eval.tests.test_cli_help_and_version.test_version_exact`
  > AssertionError: assert 'typst 0.1.0\n' == 'typst 0.14.2 (c064a23d)\n'
  >   
  >   - typst 0.14.2 (c064a23d)
  >   + typst 0.1.0
- *(... 85 more in this cluster)*

### `rc_unexpected_zero` — 87 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_advanced_compile.test_compile_diagnostic_format_human`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'compile', '/tmp/tmpw3p3isqz/test.typ', '/tmp/tmpw3p3isqz/output.pdf', '--diagnostic-format', 'human'], returncode=0, stdout=b'', stderr=b'').retur
- `tests.test_basic_invocation.test_invalid_command`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'invalid-command'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_compile.test_compile_diagnostic_format_short`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'compile', '/tmp/tmpokk1xthe/test.typ', '/tmp/tmpokk1xthe/output.pdf', '--diagnostic-format', 'short'], returncode=0, stdout=b'', stderr=b'').retur
- *(... 84 more in this cluster)*

### `missing_file` — 49 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_additional_coverage.test_compile_all_pdf_versions`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpq48estvc/output_1.4.pdf'
- `tests.test_additional_coverage.test_compile_multipage_range_combinations`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmphvfm1oov/output_1.pdf'
- `tests.test_additional_coverage.test_compile_jobs_variations`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmplgi0jbam/output_j1.pdf'
- *(... 46 more in this cluster)*

### `json_output_missing_or_bad` — 16 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `tests.test_eval.test_eval_simple_expression`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_eval.test_eval_string_expression`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_eval.test_eval_array_expression`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- *(... 13 more in this cluster)*

### `rc_mismatch_got2_want0` — 13 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_basic_invocation.test_no_arguments`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable'], returncode=2, stdout=b'', stderr=b"usage: typst [OPTIONS] [ARGS]\nTry 'typst --help' for more information.\n").returncode
- `tests.test_basic_invocation.test_color_auto`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--color', 'auto', '--help'], returncode=2, stdout=b'', stderr=b"typst: unknown option: --color\nusage: typst [OPTIONS] [ARGS]\nTry 'typst --help' 
- `tests.test_basic_invocation.test_color_always`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--color', 'always', '--help'], returncode=2, stdout=b'', stderr=b"typst: unknown option: --color\nusage: typst [OPTIONS] [ARGS]\nTry 'typst --help
- *(... 10 more in this cluster)*

### `rc_mismatch_got0_want1` — 10 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `eval.tests.test_compile_io.test_compile_nonexistent_input_errors_to_stderr_and_exit_1`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'compile', 'does_not_exist.typ', '/tmp/pytest-of-root/pytest-0/test_compile_nonexistent_input2/out.pdf'], returncode=0, stdout=b'', stderr
- `tests.test_environment_flags.test_typst_root_env_absolute_imports`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CommandResult(returncode=0, stdout='', stderr='').returncode
- `tests.test_environment_flags.test_invalid_root_directory_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CommandResult(returncode=0, stdout='', stderr='').returncode
- *(... 7 more in this cluster)*

### `bytes_output_mismatch` — 7 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `eval.tests.test_compile_io.test_compile_can_write_pdf_to_stdout_when_output_is_dash`
  > AssertionError: assert b'' == b'%PDF-'
  >   
  >   Full diff:
  >   - (b'%PDF-')
  >   + b''
- `eval.tests.test_eval_io.test_eval_simple_expression_prints_number_and_newline`
  > AssertionError: assert b'' == b'3\n'
  >   
  >   Full diff:
  >   - b'3\n'
  >   + b''
- `eval.tests.test_eval_io.test_eval_pretty_option_keeps_trailing_newline_for_scalars`
  > AssertionError: assert b'' == b'3\n'
  >   
  >   Full diff:
  >   - b'3\n'
  >   + b''
- *(... 4 more in this cluster)*

### `rc_mismatch_got0_want2` — 5 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `eval.tests.test_help_subcommands.test_invalid_subcommand_error_mentions_try_help_and_usage`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'nosuchsubcommand', '--help'], returncode=0, stdout='', stderr='').returncode
- `tests.test_environment_flags.test_empty_font_paths_env`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CommandResult(returncode=0, stdout='', stderr='').returncode
- `tests.test_environment_flags.test_invalid_source_date_epoch_format`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CommandResult(returncode=0, stdout='', stderr='').returncode
- *(... 2 more in this cluster)*

### `returned_none` — 4 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_basic_invocation.test_version_short`
  > AssertionError: assert None
  >  +  where None = <function match at 0x7f2652419120>(b'typst \\d+\\.\\d+\\.\\d+ \\([a-f0-9]+\\)', b'typst 0.1.0\n')
  >  +    where <function match at 0x7f2652419120> = re.match
  >  +    and   b'typst 0.1.0\n' = CompletedProcess(args=['./executable', '-V'], returncode=0, stdout=b'typst 0.1.0\n', stderr=b'').stdout
- `tests.test_basic_invocation.test_version_long`
  > AssertionError: assert None
  >  +  where None = <function match at 0x7f2652419120>(b'typst \\d+\\.\\d+\\.\\d+ \\([a-f0-9]+\\)', b'typst 0.1.0\n')
  >  +    where <function match at 0x7f2652419120> = re.match
  >  +    and   b'typst 0.1.0\n' = CompletedProcess(args=['./executable', '--version'], returncode=0, stdout=b'typst 0.1.0\n', stderr=b'').stdout
- `eval.tests.test_help_main.test_main_help_lists_known_subcommands`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f2fcd7a6680>('^\\s*compile\\b', 'typst 0.1.0 - bootstrap scaffold\n\nUsage: typst [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Pr
  >  +    where <function search at 0x7f2fcd7a6680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- *(... 1 more in this cluster)*

### `rc_mismatch_got2_want1` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_environment_flags.test_color_always_forces_ansi_codes`
  > assert 2 == 1
  >  +  where 2 = CommandResult(returncode=2, stdout='', stderr="typst: unknown option: --color=always\nusage: typst [OPTIONS] [ARGS]\nTry 'typst --help' for more information.\n").returncode
- `tests.test_environment_flags.test_color_never_strips_ansi_codes`
  > assert 2 == 1
  >  +  where 2 = CommandResult(returncode=2, stdout='', stderr="typst: unknown option: --color=never\nusage: typst [OPTIONS] [ARGS]\nTry 'typst --help' for more information.\n").returncode
- `tests.test_environment_flags.test_color_auto_default_behavior`
  > assert 2 == 1
  >  +  where 2 = CommandResult(returncode=2, stdout='', stderr="typst: unknown option: --color=auto\nusage: typst [OPTIONS] [ARGS]\nTry 'typst --help' for more information.\n").returncode

