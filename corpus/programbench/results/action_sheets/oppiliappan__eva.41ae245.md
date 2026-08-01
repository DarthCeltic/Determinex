# Action Sheet — oppiliappan__eva.41ae245

**Current:** 37.33%  (489/1310)
**Pass / Fail / Skip:** 489 / 474 / 0
**Gap to 100%:** 62.67 percentage points (821 tests)

## Failure clusters

474 failed tests grouped into 11 buckets (sorted by count).

### `rc_mismatch_got1_want0` — 187 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_angle_units.test_angle_unit_long_form`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '--angle_unit', 'radian', 'sin(pi/2)'], returncode=1, stdout=b'error: unknown flag --angle_unit\n', stderr=b'error: unknown flag --angle_u
- `tests.test_angle_units.test_angle_conversion_deg`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'deg(pi)'], returncode=1, stdout=b"Error: name 'deg' is not defined\n", stderr=b"Error: name 'deg' is not defined\n").returncode
- `tests.test_angle_units.test_angle_conversion_rad`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'rad(180)'], returncode=1, stdout=b"Error: name 'rad' is not defined\n", stderr=b"Error: name 'rad' is not defined\n").returncode
- *(... 184 more in this cluster)*

### `other_assertion` — 134 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_angle_units.test_inverse_trig_returns_radians`
  > AssertionError: assert b'1.570' in b'90.0000000000\n'
  >  +  where b'90.0000000000\n' = CompletedProcess(args=['/workspace/executable', '-a', 'degree', 'asin(1)'], returncode=0, stdout=b'90.0000000000\n', stderr=b'').stdout
- `tests.test_basic_invocation.test_help_flag`
  > AssertionError: assert b'Usage:' in b'eva 0.3.1\nA calculator REPL, similar to bc(1), with syntax highlighting.\n\nUSAGE:\n    eva [OPTIONS] [INPUT]\n\nOPTIONS:\n    -f, --fix <FIX>           number o
  >  +  where b'eva 0.3.1\nA calculator REPL, similar to bc(1), with syntax highlighting.\n\nUSAGE:\n    eva [OPTIONS] [INPUT]\n\nOPTIONS:\n    -f, --fix <FIX>           number of digits after the decimal
- `tests.test_basic_invocation.test_help_short_flag`
  > AssertionError: assert b'Usage:' in b'eva 0.3.1\nA calculator REPL, similar to bc(1), with syntax highlighting.\n\nUSAGE:\n    eva [OPTIONS] [INPUT]\n\nOPTIONS:\n    -f, --fix <FIX>           number o
  >  +  where b'eva 0.3.1\nA calculator REPL, similar to bc(1), with syntax highlighting.\n\nUSAGE:\n    eva [OPTIONS] [INPUT]\n\nOPTIONS:\n    -f, --fix <FIX>           number of digits after the decimal
- *(... 131 more in this cluster)*

### `string_output_mismatch` — 82 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_eva_behavior.test_base_changes_output_radix_hex`
  > AssertionError: assert '255.0000000000\n' == ' ,   ,   , FF.0\n'
  >   
  >   -  ,   ,   , FF.0
  >   + 255.0000000000
- `eval.tests.test_eva_behavior.test_repl_previous_answer_var_underscore`
  > AssertionError: assert 'eva 0.3.1' == 'No previous history.'
  >   
  >   - No previous history.
  >   + eva 0.3.1
- `tests.test_command_mode.test_factorial_negative_error`
  > AssertionError: assert 'Error: inval...g>, line 1)\n' == 'Domain Error... of bounds!\n'
  >   
  >   - Domain Error: Out of bounds!
  >   + Error: invalid syntax (<string>, line 1)
- *(... 79 more in this cluster)*

### `rc_mismatch_got0_want2` — 27 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_error_handling.test_invalid_fix_too_high`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-f', '65', '1.5'], returncode=0, stdout=b'1.50000000000000000000000000000000000000000000000000000000000000000\n', stderr=b'').returncode
- `tests.test_error_handling.test_invalid_fix_zero`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-f', '0', '1.5'], returncode=0, stdout=b'2\n', stderr=b'').returncode
- `tests.test_error_handling.test_invalid_angle_unit`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-a', 'invalid', 'sin(30)'], returncode=0, stdout=b'-0.9880316241\n', stderr=b'').returncode
- *(... 24 more in this cluster)*

### `rc_mismatch_got1_want2` — 22 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_error_handling.test_invalid_base_too_high`
  > AssertionError: assert 1 == 2
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-b', '37', '10'], returncode=1, stdout=b'error: unknown flag -b\n', stderr=b'error: unknown flag -b\n').returncode
- `tests.test_error_handling.test_invalid_base_zero`
  > AssertionError: assert 1 == 2
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-b', '0', '10'], returncode=1, stdout=b'error: unknown flag -b\n', stderr=b'error: unknown flag -b\n').returncode
- `tests.test_cli_edge_cases.test_invalid_base_too_low`
  > AssertionError: assert 1 == 2
  >  +  where 1 = CompletedProcess(args=['./executable', '-b', '0', '10'], returncode=1, stdout=b'error: unknown flag -b\n', stderr=b'error: unknown flag -b\n').returncode
- *(... 19 more in this cluster)*

### `bytes_output_mismatch` — 7 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_basic_invocation.test_no_arguments_repl_mode`
  > assert (b'No previous history' in b"eva 0.3.1\nType an expression. 'help' for help, 'quit' to exit.\n>>> \n" or b"eva 0.3.1\n...exit.\n>>> \n" == b''
  >  +  where b"eva 0.3.1\nType an expression. 'help' for help, 'quit' to exit.\n>>> \n" = CompletedProcess(args=['/workspace/executable'], returncode=0, stdout=b"eva 0.3.1\nType an expression. 'help' for
  >   
  >   Full diff:
  >   - b''
  >   + (b"eva 0.3.1\nType an expression. 'help' for help, 'quit' to exit.\n>>> \n"))
- `eval.tests.test_command_mode.test_base_16_formats_output_with_grouping_and_decimal_dot_zero`
  > AssertionError: assert b'255.0000000000\n' == b' ,   ,   , FF.0\n'
  >   
  >   At index 0 diff: b'2' != b' '
  >   
  >   Full diff:
  >   - (b' ,   ,   , FF.0\n')
  >   + (b'255.0000000000\n')
- `eval.tests.test_errors_and_streams.test_domain_error_goes_to_stderr_and_exit_1`
  > AssertionError: assert b'Error: math domain error\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'Error: math domain error\n')
- *(... 4 more in this cluster)*

### `rc_unexpected_zero` — 6 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_formatting.test_fix_zero_invalid`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--fix', '0', '1/3'], returncode=0, stdout='0\n', stderr='').returncode
- `tests.test_formatting.test_fix_65_exceeds_maximum`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--fix', '65', '1/3'], returncode=0, stdout='0.33333333333333331482961625624739099293947219848632812500000000000\n', stderr='').returncode
- `tests.test_formatting.test_fix_non_numeric_invalid`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--fix', 'abc', '1/3'], returncode=0, stdout='0.3333333333\n', stderr='').returncode
- *(... 3 more in this cluster)*

### `returned_none` — 3 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_usage.test_help_has_arguments_section`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7ff07eff2680>('^Arguments:\\s*$', 'eva 0.3.1\nA calculator REPL, similar to bc(1), with syntax highlighting.\n\nUSAGE:\n    eva [OPTIONS] [INPUT]\n\nOPTIONS:\n  
  >  +    where <function search at 0x7ff07eff2680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- `eval.tests.test_help_usage.test_help_documents_input_argument`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7ff07eff2680>('^\\s*\\[INPUT\\]\\s+Optional expression string to run eva in command mode\\s*$', 'eva 0.3.1\nA calculator REPL, similar to bc(1), with syntax high
  >  +    where <function search at 0x7ff07eff2680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- `eval.tests.test_help_usage.test_help_has_options_section`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7ff07eff2680>('^Options:\\s*$', 'eva 0.3.1\nA calculator REPL, similar to bc(1), with syntax highlighting.\n\nUSAGE:\n    eva [OPTIONS] [INPUT]\n\nOPTIONS:\n    
  >  +    where <function search at 0x7ff07eff2680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE

### `rc_mismatch_got0_want1` — 3 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_constants.TestConstants.test_constants_case_sensitive`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'PI'], returncode=0, stdout='3.1415926536\n', stderr='').returncode
- `tests.test_errors.test_syntax_error_multiple_invalid_chars`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '1#2$3'], returncode=0, stdout='1.0000000000\n', stderr='').returncode
- `tests.test_parser_edge_cases.test_function_too_few_arguments`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'log(5)'], returncode=0, stdout='1.6094379124\n', stderr='').returncode

### `boolean_false` — 2 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `eval.tests.test_help_usage.test_help_indentation_for_options_lines`
  > assert False
  >  +  where False = all(<generator object test_help_indentation_for_options_lines.<locals>.<genexpr> at 0x7ff07dd24a50>)
- `tests.test_formatting.test_thousand_separator_million`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7f7408953fa0>('1,000,000')
  >  +    where <built-in method startswith of str object at 0x7f7408953fa0> = '1000000.0000000000'.startswith

### `rc_mismatch_got3_want2` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_final_gaps.test_empty_after_calculation_reuses_previous_answer`
  > assert 3 == 2
  >  +  where 3 = len(['eva 0.3.1', "Type an expression. 'help' for help, 'quit' to exit.", '>>>'])

