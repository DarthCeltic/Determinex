# Action Sheet — cmatsuoka__figlet.202a0a8

**Current:** 14.92%  (197/1320)
**Pass / Fail / Skip:** 197 / 711 / 0
**Gap to 100%:** 85.08 percentage points (1123 tests)

## Failure clusters

711 failed tests grouped into 14 buckets (sorted by count).

### `other_assertion` — 313 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_additional_coverage.TestAdvancedOptions.test_very_long_text_line`
  > AssertionError: assert 0 > 100
  >  +  where 0 = len(b'')
  >  +    where b'' = CompletedProcess(args=['./executable', '-d', 'fonts', '-w', '40'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_additional_coverage.TestAdvancedOptions.test_paragraph_mode_with_wrapping`
  > AssertionError: assert 0 > 50
  >  +  where 0 = len(b'')
  >  +    where b'' = CompletedProcess(args=['./executable', '-d', 'fonts', '-p', '-w', '30'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_additional_coverage.TestAdvancedOptions.test_combined_options_kpc`
  > AssertionError: assert 0 > 20
  >  +  where 0 = len(b'')
  >  +    where b'' = CompletedProcess(args=['./executable', '-d', 'fonts', '-k', '-p', '-c', '-f', 'small', 'Test'], returncode=0, stdout=b'', stderr=b'').stdout
- *(... 310 more in this cluster)*

### `bytes_output_mismatch` — 189 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_basic_invocation.test_info_version_integer`
  > AssertionError: assert b'1' == b'20205'
  >   
  >   At index 0 diff: b'1' != b'2'
  >   
  >   Full diff:
  >   - (b'20205')
  >   + b'1'
- `tests.test_basic_invocation.test_info_output_width`
  > AssertionError: assert b'4' == b'80'
  >   
  >   At index 0 diff: b'4' != b'8'
  >   
  >   Full diff:
  >   - b'80'
  >   + b'4'
- `tests.test_basic_invocation.test_info_output_width_custom`
  > AssertionError: assert b'4' == b'120'
  >   
  >   At index 0 diff: b'4' != b'1'
  >   
  >   Full diff:
  >   - b'120'
  >   + b'4'
- *(... 186 more in this cluster)*

### `string_output_mismatch` — 103 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_argument_parsing.TestBooleanFlags.test_boolean_flag_accepted[-x]`
  > AssertionError: assert (1 == 0 or 'Unable to open font file' in 'figlet: illegal option -- x\n')
- `eval.tests.test_subcommand_dispatch.test_unknown_info_code_is_graceful_empty_output_success`
  > AssertionError: assert '999' == ''
  >   
  >   + 999
- `eval.tests.test_executable_figlet_behavior.test_invalid_option_prints_usage_and_exits_1`
  > AssertionError: assert '/workspace/e...[ message ]\n' == 'figlet: inva...option -- Z\n'
  >   
  >   - figlet: invalid option -- Z
  >   + /workspace/executable: invalid option -- 'Z'
  >   + Usage: executable [ -cklnoprstvxDELNRSWX ] [ -d fontdirectory ]
  >   +               [ -f fontfile ] [ -m smushmode ] [ -w outputwidth ]
  >   +               [ -C controlfile ] [ -I infocode ] [ message ]
- *(... 100 more in this cluster)*

### `rc_mismatch_got1_want0` — 47 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_basic_invocation.TestBasicInvocation.test_info_version_copyright`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '-d', 'fonts', '-I0'], returncode=1, stdout=b'', stderr=b'figlet: invalid option -- I\n').returncode
- `tests.test_basic_invocation.TestBasicInvocation.test_info_version_integer`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '-d', 'fonts', '-I1'], returncode=1, stdout=b'', stderr=b'figlet: invalid option -- I\n').returncode
- `tests.test_basic_invocation.TestBasicInvocation.test_info_font_directory`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '-d', 'fonts', '-I2'], returncode=1, stdout=b'', stderr=b'figlet: invalid option -- I\n').returncode
- *(... 44 more in this cluster)*

### `rc_unexpected_zero` — 31 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_basic_invocation.TestInvalidOptions.test_double_dash_help`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '-d', 'fonts', '--help'], returncode=0, stdout=b'Usage: executable [ -cklnoprstvxDELNRSWX ] [ -d control_directory ] [ -f font_file ] [ -m smush_mo
- `tests.test_compressed_fonts.TestZipEdgeCases.test_empty_zip`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '-d', '/tmp/tmpv2be696s', '-f', 'empty', 'X'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_fonts.TestFontSelection.test_nonexistent_font`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '-d', 'fonts', '-f', 'nonexistent', 'X'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 28 more in this cluster)*

### `rc_mismatch_got0_want1` — 18 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `eval.tests.test_io_behavior.test_invalid_option_prints_usage_to_stderr_and_exit_1`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-h'], returncode=0, stdout=b'Usage: executable [ -cklnoprstvxDELNRSWX ] [ -d control_directory ] [ -f font_file ] [ -m smush_mode ] [ -w 
- `eval.tests.test_io_behavior.test_missing_font_file_errors_and_exit_1_and_goes_to_stderr`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-d', '/workspace/fonts', '-f', 'doesnotexist.flf', 'Hi'], returncode=0, stdout=b'', stderr=b'').returncode
- `eval.tests.test_executable_figlet_behavior.test_without_font_dir_fails_to_open_default_font`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'Hello'], returncode=0, stdout='#    #  ######  #       #         ##  \n#    #  #       #       #        #  # \n#    #  #       #       # 
- *(... 15 more in this cluster)*

### `rc_mismatch_got0_want6` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_errors.test_newline_only_input`
  > AssertionError: assert 0 == 6
  >  +  where 0 = <built-in method count of str object at 0x7f8a79664030>('\n')
  >  +    where <built-in method count of str object at 0x7f8a79664030> = ''.count
- `tests.test_errors.test_spaces_only_input`
  > AssertionError: assert 0 == 6
  >  +  where 0 = <built-in method count of str object at 0x7f8a79664030>('\n')
  >  +    where <built-in method count of str object at 0x7f8a79664030> = ''.count

### `rc_mismatch_got4_want100` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_info.test_info_code_flag_order_w_after_t`
  > AssertionError: assert 4 == 100
  >  +  where 4 = int('4')
- `tests.test_info.test_info_code_flag_order_t_after_w`
  > AssertionError: assert 4 == 100
  >  +  where 4 = int('4')

### `boolean_false` — 1 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `eval.tests.test_help_usage.test_help_usage_line_starts_with_usage_executable`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7f7dc0510030>('Usage: executable')
  >  +    where <built-in method startswith of str object at 0x7f7dc0510030> = ''.startswith

### `uncategorized` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_help_usage.test_help_usage_is_multiline_and_indented`
  > StopIteration

### `rc_mismatch_got0_want18` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_errors.test_multiple_newlines_input`
  > AssertionError: assert 0 == 18
  >  +  where 0 = <built-in method count of str object at 0x7f8a79664030>('\n')
  >  +    where <built-in method count of str object at 0x7f8a79664030> = ''.count

### `rc_mismatch_got2_want0` — 1 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_harvest.test_003_long_text_rendering`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b'Usage: executable [ -cklnoprstvxDELNRSWX ] [ -d control_directory ] [ -f font_file ] [ -m smush_mode ]

### `rc_mismatch_got4_want80` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_info.test_info_code_4_ignores_invalid_width`
  > AssertionError: assert 4 == 80
  >  +  where 4 = int('4')

### `rc_mismatch_got0_want2` — 1 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_info.test_info_code_1_is_numeric_version`
  > assert 0 == 2

