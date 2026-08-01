# Action Sheet — abishekvashok__cmatrix.5c082c6

**Current:** 29.09%  (274/942)
**Pass / Fail / Skip:** 274 / 391 / 0
**Gap to 100%:** 70.91 percentage points (668 tests)

## Failure clusters

391 failed tests grouped into 8 buckets (sorted by count).

### `rc_mismatch_got2_want0` — 216 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_cmatrix.TestColorOptions.test_color_green`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '-C', 'green', '-h'], returncode=2, stdout=b'', stderr=b'cmatrix: unknown option: -h\nusage: cmatrix [-abBcC:fF:hLlmoM:nprRsStTu:Vxy?] [-C color] [
- `tests.test_cmatrix.TestColorOptions.test_color_red`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '-C', 'red', '-h'], returncode=2, stdout=b'', stderr=b'cmatrix: unknown option: -h\nusage: cmatrix [-abBcC:fF:hLlmoM:nprRsStTu:Vxy?] [-C color] [-F
- `tests.test_cmatrix.TestColorOptions.test_color_blue`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '-C', 'blue', '-h'], returncode=2, stdout=b'', stderr=b'cmatrix: unknown option: -h\nusage: cmatrix [-abBcC:fF:hLlmoM:nprRsStTu:Vxy?] [-C color] [-
- *(... 213 more in this cluster)*

### `other_assertion` — 100 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cmatrix.TestBasicInvocation.test_version_flag_short`
  > AssertionError: assert b'CMatrix version' in b'cmatrix 0.1.0\n'
  >  +  where b'cmatrix 0.1.0\n' = CompletedProcess(args=['./executable', '-V'], returncode=0, stdout=b'cmatrix 0.1.0\n', stderr=b'').stdout
- `tests.test_cmatrix.TestBasicInvocation.test_version_flag_long_shows_help`
  > AssertionError: assert b'Usage: cmatrix' in b'cmatrix 0.1.0\n'
  >  +  where b'cmatrix 0.1.0\n' = CompletedProcess(args=['./executable', '--version'], returncode=0, stdout=b'cmatrix 0.1.0\n', stderr=b'').stdout
- `tests.test_cmatrix.TestHelpContent.test_help_contains_all_flags`
  > assert b'-k' in b"CMatrix version 0.1.0\nCopyright (c) 1999-2024 Chris Allegretta and others\nUsage: cmatrix [OPTIONS]\n\nOptions:\n  -a            Asynchronous scroll\n  -b            Bold characters
- *(... 97 more in this cluster)*

### `test_timeout` — 59 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cmatrix.TestColorOptions.test_color_invalid_shows_error_message`
  > subprocess.TimeoutExpired: Command '['./executable', '-C', 'purple']' timed out after 5.0 seconds
- `tests.test_cmatrix.TestErrorHandling.test_color_missing_argument_shows_help`
  > subprocess.TimeoutExpired: Command '['./executable', '-C']' timed out after 5.0 seconds
- `tests.test_cmatrix.TestErrorHandling.test_update_missing_argument_shows_help`
  > subprocess.TimeoutExpired: Command '['./executable', '-u']' timed out after 5.0 seconds
- *(... 56 more in this cluster)*

### `string_output_mismatch` — 8 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_help_output.TestExactHelpOutput.test_help_exact_match`
  > AssertionError: assert 'CMatrix vers...lp and exit\n' == ' Usage: cmat... tty to use\n'
  >   
  >   -  Usage: cmatrix -[abBcfhlsmVxk] [-u delay] [-C color] [-t tty] [-M message]
  >   + CMatrix version 0.1.0
  >   + Copyright (c) 1999-2024 Chris Allegretta and others
  >   + Usage: cmatrix [OPTIONS]
  >   + 
  >   + Options:...
- `tests.test_help_output.TestExactHelpOutput.test_short_help_exact_match`
  > AssertionError: assert 'CMatrix vers...lp and exit\n' == ' Usage: cmat... tty to use\n'
  >   
  >   -  Usage: cmatrix -[abBcfhlsmVxk] [-u delay] [-C color] [-t tty] [-M message]
  >   + CMatrix version 0.1.0
  >   + Copyright (c) 1999-2024 Chris Allegretta and others
  >   + Usage: cmatrix [OPTIONS]
  >   + 
  >   + Options:...
- `eval.tests.test_help_output.test_help_usage_line_exact`
  > AssertionError: assert 'CMatrix version 0.1.0' == ' Usage: cmat... [-M message]'
  >   
  >   -  Usage: cmatrix -[abBcfhlsmVxk] [-u delay] [-C color] [-t tty] [-M message]
  >   + CMatrix version 0.1.0
- *(... 5 more in this cluster)*

### `boolean_false` — 4 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_help_output.TestExactHelpOutput.test_help_starts_with_space`
  > assert False
  >  +  where False = <built-in method startswith of str object at 0x5584722dd650>(' ')
  >  +    where <built-in method startswith of str object at 0x5584722dd650> = "CMatrix version 0.1.0\nCopyright (c) 1999-2024 Chris Allegretta and others\nUsage: cmatrix [OPTIONS]\n\nOptions:\n  -a      
  >  +      where "CMatrix version 0.1.0\nCopyright (c) 1999-2024 Chris Allegretta and others\nUsage: cmatrix [OPTIONS]\n\nOptions:\n  -a            Asynchronous scroll\n  -b            Bold characters on
- `tests.test_cmatrix.TestBooleanFlags.test_boolean_flags_accepted[-ab]`
  > AssertionError: assert False
  >  +  where False = tmux_session_exists('test_flags_ab_1779045937707876')
- `tests.test_cmatrix.TestCombinedArguments.test_all_arguments_combined`
  > AssertionError: assert False
  >  +  where False = tmux_session_exists('test_combo_all_1779045957149698')
- *(... 1 more in this cluster)*

### `rc_mismatch_got31_want21` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_help_output.TestExactHelpOutput.test_help_line_count`
  > assert 31 == 21
- `eval.tests.test_help_output.test_help_contains_expected_number_of_lines`
  > assert 31 == 21
  >  +  where 31 = len(['CMatrix version 0.1.0', 'Copyright (c) 1999-2024 Chris Allegretta and others', 'Usage: cmatrix [OPTIONS]', '', 'Options:', '  -a            Asynchronous scroll', ...])
  >  +    where ['CMatrix version 0.1.0', 'Copyright (c) 1999-2024 Chris Allegretta and others', 'Usage: cmatrix [OPTIONS]', '', 'Options:', '  -a            Asynchronous scroll', ...] = <built-in method 
  >  +      where <built-in method splitlines of str object at 0x55ba525a9070> = "CMatrix version 0.1.0\nCopyright (c) 1999-2024 Chris Allegretta and others\nUsage: cmatrix [OPTIONS]\n\nOptions:\n  -a    

### `returned_none` — 1 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_basic_invocation.test_version_format`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f4b5bd8a680>(b'version\\s+\\d+\\.\\d+', b'cmatrix 0.1.0\n', re.IGNORECASE)
  >  +    where <function search at 0x7f4b5bd8a680> = re.search
  >  +    and   b'cmatrix 0.1.0\n' = CompletedProcess(args=['../executable', '-V'], returncode=0, stdout=b'cmatrix 0.1.0\n', stderr=b'').stdout
  >  +    and   re.IGNORECASE = re.IGNORECASE

### `bytes_output_mismatch` — 1 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `eval.tests.test_cmatrix_cli.test_help_exact_golden`
  > assert b"CMatrix ver...lp and exit\n" == b' Usage: cma... tty to use\n'
  >   
  >   At index 0 diff: b'C' != b' '
  >   
  >   Full diff:
  >   - (b' Usage: cmatrix -[abBcfhlsmVxk] [-u delay] [-C color] [-t tty] [-M messa'
  >   -  b'ge]\n -a: Asynchronous scroll\n -b: Bold characters on\n -B: All bold chara'
  >   -  b'cters (overrides -b)\n -c: Use Japanese characters as seen in the origina'...

