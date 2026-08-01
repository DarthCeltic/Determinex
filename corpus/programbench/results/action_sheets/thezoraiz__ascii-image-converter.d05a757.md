# Action Sheet — thezoraiz__ascii-image-converter.d05a757

**Current:** 6.19%  (30/485)
**Pass / Fail / Skip:** 30 / 440 / 1
**Gap to 100%:** 93.81 percentage points (455 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_conversion_basic.test_negative_flag_changes_output_deterministically`
  - reason: test_negative_flag_changes_output_deterministically depends on test_convert_dimensions_2x1_stdout_exact

## Failure clusters

440 failed tests grouped into 13 buckets (sorted by count).

### `other_assertion` — 163 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_args_validation.test_custom_validation_errors_without_needing_real_file[args1-requires 2 dimensions, got 1]`
  > AssertionError: Expected to find 'requires 2 dimensions, got 1' in output. Output was:
  >   
  >   Error: can't decode
  >   
  > assert 'requires 2 dimensions, got 1' in "\nError: can't decode\n"
- `eval.tests.test_config_env_none.test_help_mentions_flags_only_not_config_files_or_env_vars`
  > assert 'configuration' in "ascii-image-converter 0.1.0\n\nusage: ascii-image-converter [options] [args]\n\noptions:\n  -h, --help     print help\n  -v, --version  print version\n  -v, --verbose  verbo
- `eval.tests.test_help_usage.test_help_contains_intro_sentence`
  > assert 'converts images into ascii art' in "ascii-image-converter 0.1.0\n\nusage: ascii-image-converter [options] [args]\n\noptions:\n  -h, --help     print help\n  -v, --version  print version\n  -v,
  >  +  where "ascii-image-converter 0.1.0\n\nusage: ascii-image-converter [options] [args]\n\noptions:\n  -h, --help     print help\n  -v, --version  print version\n  -v, --verbose  verbose\n  -q, --quie
  >  +    where <built-in method lower of str object at 0x7f45a22e3cc0> = "ascii-image-converter 0.1.0\n\nusage: ascii-image-converter [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --ve
- *(... 160 more in this cluster)*

### `string_output_mismatch` — 150 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_usage.test_help_baseline_exact_match_fixture`
  > assert "ascii-image-...an't decode\n" == 'This tool co...e-converter\n'
  >   
  >   + ascii-image-converter 0.1.0
  >   - This tool converts images into ascii art and prints them on the terminal.
  >   - Further configuration can be managed with flags.
  >     
  >   + usage: ascii-image-converter [OPTIONS] [ARGS]
  >   - Usage:...
- `eval.tests.test_conversion_basic.test_convert_dimensions_2x1_stdout_exact`
  > assert "Error: can't decode\n" == ' @\n'
  >   
  >   -  @
  >   + Error: can't decode
- `eval.tests.test_help_and_formats.test_help_exact_output_matches_snapshot`
  > assert "ascii-image-...an't decode\n" == 'This tool co...e-converter\n'
  >   
  >   + ascii-image-converter 0.1.0
  >   - This tool converts images into ascii art and prints them on the terminal.
  >   - Further configuration can be managed with flags.
  >     
  >   + usage: ascii-image-converter [OPTIONS] [ARGS]
  >   - Usage:...
- *(... 147 more in this cluster)*

### `boolean_false` — 52 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `eval.tests.test_errors_and_streams.test_nonexistent_file_prints_error_to_stdout_and_exit_0`
  > assert False
  >  +  where False = <built-in method startswith of str object at 0x7fad1a712510>('Error: unable to open file: open does_not_exist.png:')
  >  +    where <built-in method startswith of str object at 0x7fad1a712510> = "Error: can't decode\n".startswith
- `eval.tests.test_help_version.test_version_flag_outputs_version_and_exits_0`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of bytes object at 0x7fad1ad12330>(b'v')
  >  +    where <built-in method startswith of bytes object at 0x7fad1ad12330> = b'ascii-image-converter 0.1.0\n'.startswith
  >  +      where b'ascii-image-converter 0.1.0\n' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'ascii-image-converter 0.1.0\n', stderr=b'').stdout
- `eval.tests.test_save_txt.test_save_txt_creates_file_and_only_save_suppresses_ascii_art`
  > assert False
  >  +  where False = <built-in method startswith of str object at 0x7fad1a789ac0>('Saved ')
  >  +    where <built-in method startswith of str object at 0x7fad1a789ac0> = "Error: can't decode\n".startswith
- *(... 49 more in this cluster)*

### `rc_mismatch_got2_want0` — 40 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `eval.tests.test_args_validation.test_custom_validation_errors_without_needing_real_file[args0-requires 2 dimensions, got 1]`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--dimensions', '60', 'dummy.png'], returncode=2, stdout='', stderr="ascii-image-converter: error: unrecognized argument: --dimensions\nEr
- `eval.tests.test_args_validation.test_custom_validation_errors_without_needing_real_file[args2---save-bg requires 4 values for RGBA, got 3]`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--save-bg', '1,2,3', 'dummy.png'], returncode=2, stdout='', stderr="ascii-image-converter: error: unrecognized argument: --save-bg\nError
- `eval.tests.test_args_validation.test_custom_validation_errors_without_needing_real_file[args3---font-color requires 3 values for RGB, got 2]`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--font-color', '1,2', 'dummy.png'], returncode=2, stdout='', stderr="ascii-image-converter: error: unrecognized argument: --font-color\nE
- *(... 37 more in this cluster)*

### `rc_mismatch_got2_want1` — 11 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_args_validation.test_unknown_flag_errors_nonzero[--unknown]`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--unknown'], returncode=2, stdout='', stderr="ascii-image-converter: error: unrecognized argument: --unknown\nError: both --width and --h
- `eval.tests.test_args_validation.test_unknown_flag_errors_nonzero[--nonexistent-flag]`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--nonexistent-flag'], returncode=2, stdout='', stderr="ascii-image-converter: error: unrecognized argument: --nonexistent-flag\nError: bo
- `eval.tests.test_args_validation.test_unknown_flag_errors_nonzero[--does-not-exist]`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--does-not-exist'], returncode=2, stdout='', stderr="ascii-image-converter: error: unrecognized argument: --does-not-exist\nError: both -
- *(... 8 more in this cluster)*

### `rc_mismatch_got0_want1` — 8 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `eval.tests.test_args_validation.test_missing_value_for_value_flags[args4-needs an argument]`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-m'], returncode=0, stdout="Error: can't decode\n", stderr='').returncode
- `eval.tests.test_args_validation.test_invalid_int_type_errors[args1-invalid argument "notanint"]`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-W', 'notanint'], returncode=0, stdout="Error: can't decode\n", stderr='').returncode
- `eval.tests.test_args_validation.test_invalid_int_type_errors[args3-invalid argument "notanint"]`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-H', 'notanint'], returncode=0, stdout="Error: can't decode\n", stderr='').returncode
- *(... 5 more in this cluster)*

### `rc_mismatch_got1_want0` — 6 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `eval.tests.test_args_validation.test_no_args_requires_input`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable'], returncode=1, stdout='', stderr='usage: ascii-image-converter [OPTIONS] [ARGS]\n').returncode
- `eval.tests.test_errors_and_streams.test_no_input_prints_error_to_stdout_and_exit_0`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable'], returncode=1, stdout=b'', stderr=b'usage: ascii-image-converter [OPTIONS] [ARGS]\n').returncode
- `eval.tests.test_errors.test_no_args_errors_and_mentions_help_flag`
  > AssertionError: assert 1 == 0
  >  +  where 1 = ExecResult(returncode=1, stdout='', stderr='usage: ascii-image-converter [OPTIONS] [ARGS]\n').returncode
- *(... 3 more in this cluster)*

### `rc_mismatch_got0_want2` — 3 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_config_and_utils.test_width_zero_panics`
  > assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/workspace/eval/test_resources/test_basic_conversion/black_10x10.png', '-W', '0'], returncode=0, stdout="Error: can't decode\n", stderr='
- `tests.test_config_and_utils.test_height_zero_panics`
  > assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/workspace/eval/test_resources/test_basic_conversion/black_10x10.png', '-H', '0'], returncode=0, stdout="Error: can't decode\n", stderr='
- `tests.test_errors.test_multiple_images_first_succeeds_second_fails`
  > assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/workspace/eval/test_resources/test_basic_conversion/black_10x10.png', '/tmp/pytest-of-root/pytest-0/test_multiple_images_first_suc2/none

### `returned_none` — 2 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_usage.test_usage_line_mentions_program_name`
  > assert None
  >  +  where None = <function search at 0x7f45a2c1e680>('(?m)^\\s*ascii-image-converter\\s+\\[image paths/urls or piped stdin\\]\\s+\\[flags\\]\\s*$', "ascii-image-converter 0.1.0\n\nusage: ascii-image-c
  >  +    where <function search at 0x7f45a2c1e680> = re.search
- `eval.tests.test_help_usage.test_help_has_flags_section`
  > assert None
  >  +  where None = <function search at 0x7f45a2c1e680>('(?m)^Flags:\\s*$', "ascii-image-converter 0.1.0\n\nusage: ascii-image-converter [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, -
  >  +    where <function search at 0x7f45a2c1e680> = re.search

### `missing_file` — 2 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_output_saving.test_save_txt_content_matches_terminal_output`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpcj4uwn3f/simple_red-ascii-art.txt'
- `tests.test_output_saving.test_save_txt_preserves_ascii_structure`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpb1z3s24s/simple_red-ascii-art.txt'

### `rc_unexpected_zero` — 1 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `eval.tests.test_help_usage.test_help_unknown_flag_error_has_expected_streams_and_usage`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--help', '--bogus'], returncode=0, stdout="ascii-image-converter 0.1.0\n\nusage: ascii-image-converter [OPTIONS] [ARGS]\n\nOptions:\n  -h

### `rc_mismatch_got1_want4` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_basic_ascii_output.test_small_solid_image_ascii_dimensions_and_newlines`
  > assert 1 == 4
  >  +  where 1 = len(["Error: can't decode"])

### `test_timeout` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_gif.test_gif_without_only_save_requires_timeout`
  > Failed: DID NOT RAISE <class 'subprocess.TimeoutExpired'>

