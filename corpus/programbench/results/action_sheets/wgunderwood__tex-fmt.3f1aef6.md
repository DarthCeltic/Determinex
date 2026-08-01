# Action Sheet — wgunderwood__tex-fmt.3f1aef6

**Current:** 5.6%  (33/589)
**Pass / Fail / Skip:** 33 / 461 / 1
**Gap to 100%:** 94.40 percentage points (556 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_files_modes.test_check_formatted_exits_0`
  - reason: test_check_formatted_exits_0 depends on test_check_unformatted_exits_1

## Failure clusters

461 failed tests grouped into 11 buckets (sorted by count).

### `rc_mismatch_got2_want0` — 244 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_advanced_formatting.test_verbatim_environment`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--print', '/tmp/tmpori3btmu/test.tex'], returncode=2, stdout=b'', stderr=b'tex-fmt: error: unrecognized argument: --print\n').returncode
- `tests.test_advanced_formatting.test_verb_command`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--print', '/tmp/tmp7qiinyk4/test.tex'], returncode=2, stdout=b'', stderr=b'tex-fmt: error: unrecognized argument: --print\n').returncode
- `tests.test_advanced_formatting.test_figure_environment`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--print', '/tmp/tmp1nf78q51/test.tex'], returncode=2, stdout=b'', stderr=b'tex-fmt: error: unrecognized argument: --print\n').returncode
- *(... 241 more in this cluster)*

### `other_assertion` — 118 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_help_flag`
  > AssertionError: assert b'Usage:' in b'tex-fmt 0.1.0\n\nusage: tex-fmt [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --verbose  Verbose\n  -q, --quiet
  >  +  where b'tex-fmt 0.1.0\n\nusage: tex-fmt [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --verbose  Verbose\n  -q, --quiet    Quiet\n\n' = Completed
- `tests.test_basic_invocation.test_help_short_flag`
  > AssertionError: assert b'Usage:' in b'tex-fmt 0.1.0\n\nusage: tex-fmt [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --verbose  Verbose\n  -q, --quiet
  >  +  where b'tex-fmt 0.1.0\n\nusage: tex-fmt [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --verbose  Verbose\n  -q, --quiet    Quiet\n\n' = Completed
- `tests.test_file_operations.test_format_single_file_in_place`
  > AssertionError: assert '  \\item First item' in '\\documentclass{article}\n\\begin{document}\n\\begin{itemize}\n\\item First item\n\\item Second item\n\\end{itemize}\n\\end{document}'
- *(... 115 more in this cluster)*

### `string_output_mismatch` — 28 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_baseline.test_help_matches_baseline_except_version`
  > AssertionError: assert 'tex-fmt <VER...    Quiet\n\n' == 'tex-fmt <VER...int version\n'
  >   
  >     tex-fmt <VERSION>
  >   + usage: tex-fmt [OPTIONS] [ARGS]
  >   - LaTeX formatter written in Rust
  >   - 
  >   - Usage: executable [OPTIONS] [files]...
  >   - ...
- `eval.tests.test_io_behavior.test_default_overwrites_file_in_place_and_is_silent`
  > AssertionError: assert '\\begin{item...nd{itemize}\n' == '\\begin{item...nd{itemize}\n'
  >   
  >     \begin{itemize}
  >   -   \item a
  >   ? --
  >   + \item a
  >     \end{itemize}
- `eval.tests.test_cli_outputs.test_help_exact`
  > AssertionError: assert 'tex-fmt 0.1....    Quiet\n\n' == 'tex-fmt 0.5....int version\n'
  >   
  >   - tex-fmt 0.5.6
  >   ?           ^ ^
  >   + tex-fmt 0.1.0
  >   ?           ^ ^
  >     
  >   + usage: tex-fmt [OPTIONS] [ARGS]...
- *(... 25 more in this cluster)*

### `rc_mismatch_got2_want1` — 24 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_args_parsing.test_double_dash_treats_following_tokens_as_positional_not_flags`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--', '--nonexistent-flag', '--args'], returncode=2, stdout='', stderr='tex-fmt: error: unrecognized argument: --\n').returncode
- `eval.tests.test_args_parsing.test_no_files_no_recursive_no_stdin_is_validation_error_rc1`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--check', '--print'], returncode=2, stdout='', stderr='tex-fmt: error: unrecognized argument: --check\n').returncode
- `eval.tests.test_io_behavior.test_check_exit_codes_and_stderr_message_when_incorrect`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--check', '/tmp/io-tests-56wt2ca2/a.tex'], returncode=2, stdout='', stderr='tex-fmt: error: unrecognized argument: --check\n').returncode
- *(... 21 more in this cluster)*

### `bytes_output_mismatch` — 21 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `eval.tests.test_externalized_from_internal_rs_tests.test_ext_brackets`
  > AssertionError: assert b'' == b'\\documentc...d{document}\n'
  >   
  >   Full diff:
  >   + b''
  >   - (b'\\documentclass{article}\n\n\\begin{document}\n\nMatching brackets on a li'
  >   -  b'ne do nothing (like this).\n\nMatching brackets on two lines also do nothi'
  >   -  b'ng (like this\nlonger example).\n\nMatching brackets on three lines get an '
  >   -  b'indent (like this\n  much much longer example\nright here on these lines).'...
- `eval.tests.test_externalized_from_internal_rs_tests.test_ext_comments`
  > AssertionError: assert b'' == b'\\documentc...d{document}\n'
  >   
  >   Full diff:
  >   + b''
  >   - (b'\\documentclass{article}\n\n\\begin{document}\n\n% Comments should be inde'
  >   -  b'nted along with other text\n(these parentheses\n  make the middle line her'
  >   -  b'e\n  % and this comment aligns with the text\nindented as usual)\n\n% Commen'
  >   -  b'ts do not directly affect indenting,\n% so they can contain arbitrary bra'...
- `eval.tests.test_externalized_from_internal_rs_tests.test_ext_cv`
  > assert b'' == b"% !TeX prog...d{document}\n"
  >   
  >   Full diff:
  >   + b''
  >   - (b'% !TeX program = lualatex\n\n\\documentclass{wgu-cv}\n\n\\yourname{William'
  >   -  b' G Underwood}\n\\youraddress{\n  ORFE Department,\n  Sherrerd Hall,\n  Ch'
  >   -  b'arlton Street,\n  Princeton,\n  NJ 08544,\n  USA\n}\n\\youremail{wgu2@prin'
  >   -  b'ceton.edu}\n\\yourwebsite{wgunderwood.github.io}\n\n\\begin{document}\n\n\\m'...
- *(... 18 more in this cluster)*

### `rc_unexpected_zero` — 8 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_error_handling.test_nonexistent_file`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '/tmp/nonexistent_file_xyz123.tex'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_error_handling.test_multiple_nonexistent_files`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '/tmp/fake1.tex', '/tmp/fake2.tex'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_file_operations.test_check_mode_short_flag`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '-c', '/tmp/tmpnv7bamjf/test.tex'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 5 more in this cluster)*

### `missing_dict_key` — 8 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_args_parsing.test_combined_short_flags_supported_v_and_p`
  > KeyError: 'print'
- `eval.tests.test_args_parsing.test_option_value_forms_space_and_equals_work[form2]`
  > KeyError: 'wraplen'
- `eval.tests.test_args_parsing.test_option_value_forms_space_and_equals_work[form3]`
  > KeyError: 'wraplen'
- *(... 5 more in this cluster)*

### `rc_mismatch_got0_want1` — 6 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `eval.tests.test_io_behavior.test_nonexistent_file_is_error_on_stderr_exit1`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'no_such_file_hopefully.tex'], returncode=0, stdout='', stderr='').returncode
- `tests.test_cli.test_nonexistent_file_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/tmp/nonexistent_file_12345.tex'], returncode=0, stdout='', stderr='').returncode
- `tests.test_file_ops.test_nonexistent_file_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/nonexistent/path/file.tex'], returncode=0, stdout='', stderr='').returncode
- *(... 3 more in this cluster)*

### `returned_none` — 2 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_behavior.test_help_has_usage_section`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f9be011e680>('^Usage:\\s', 'tex-fmt 0.1.0\n\nusage: tex-fmt [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --v
  >  +    where <function search at 0x7f9be011e680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- `eval.tests.test_help_behavior.test_help_has_arguments_and_options_sections`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f9be011e680>('^Arguments:\\s*$', 'tex-fmt 0.1.0\n\nusage: tex-fmt [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -
  >  +    where <function search at 0x7f9be011e680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE

### `uncategorized` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_formatting.test_nowrap_short_flag`
  > ValueError: max() arg is an empty sequence

### `boolean_false` — 1 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_file_ops.test_file_ending_without_newline`
  > AssertionError: assert False
  >  +  where False = <built-in method endswith of str object at 0x7f607c6d1f70>('\n')
  >  +    where <built-in method endswith of str object at 0x7f607c6d1f70> = '\\item test'.endswith

