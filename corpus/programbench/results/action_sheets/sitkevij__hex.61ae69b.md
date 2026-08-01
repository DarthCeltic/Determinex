# Action Sheet — sitkevij__hex.61ae69b

**Current:** 6.26%  (78/1247)
**Pass / Fail / Skip:** 78 / 799 / 0
**Gap to 100%:** 93.74 percentage points (1169 tests)

## Failure clusters

799 failed tests grouped into 13 buckets (sorted by count).

### `rc_mismatch_got2_want0` — 443 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_advanced_error_handling.test_empty_stdin_with_flags`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '-fx', '-c4'], returncode=2, stdout=b'', stderr=b'hex: error: unrecognized argument: -x\n').returncode
- `tests.test_advanced_error_handling.test_combined_short_flags`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '-fx', '-c4', '/tmp/tmpoc30tlna/test.txt'], returncode=2, stdout=b'', stderr=b'hex: error: unrecognized argument: -x\n').returncode
- `tests.test_advanced_error_handling.test_array_format_with_empty_file`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '-ar', '/tmp/tmp8pg0eok4/empty.txt'], returncode=2, stdout=b'', stderr=b'hex: error: unrecognized argument: -a\n').returncode
- *(... 440 more in this cluster)*

### `other_assertion` — 217 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_advanced_error_handling.test_zero_len_value`
  > AssertionError: assert b'bytes:' in b'\n'
  >  +  where b'\n' = CompletedProcess(args=['./executable', '-l', '0', '/tmp/tmpp4vglyc1/test.txt'], returncode=0, stdout=b'\n', stderr=b'').stdout
- `tests.test_advanced_error_handling.test_file_with_spaces_in_name`
  > AssertionError: assert b'0x41 0x42 0x43' in b'00000000: 41 42 43                                         ABC\n'
  >  +  where b'00000000: 41 42 43                                         ABC\n' = CompletedProcess(args=['./executable', '/tmp/tmpgz0bswrx/test file.txt'], returncode=0, stdout=b'00000000: 41 42 43     
- `tests.test_advanced_error_handling.test_symlink_to_file`
  > AssertionError: assert b'0x41 0x42 0x43' in b'00000000: 41 42 43                                         ABC\n'
  >  +  where b'00000000: 41 42 43                                         ABC\n' = CompletedProcess(args=['./executable', '/tmp/tmpu5vma84l/link.txt'], returncode=0, stdout=b'00000000: 41 42 43          
- *(... 214 more in this cluster)*

### `bytes_output_mismatch` — 45 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_color.test_no_color_env_var_disables_color`
  > AssertionError: assert b'00000000: 0...   ... AZ..\n' == b'0x000000: 0...   bytes: 8\n'
  >   
  >   At index 1 diff: b'0' != b'x'
  >   
  >   Full diff:
  >   - (b'0x000000: 0x00 0x01 0x0a 0x20 0x41 0x5a 0x7f 0xff           ... AZ..\n   '
  >   ?     ^        --   --   --   --   --   --   --   --                       ---
  >   + (b'00000000: 00 01 0a 20 41 5a 7f ff                          ... AZ..\n')
- `tests.test_color.test_color_flag_invalid_value`
  > assert b'hex: error:...rgument: -t\n' == b"error: inva...y '--help'.\n"
  >   
  >   At index 0 diff: b'h' != b'e'
  >   
  >   Full diff:
  >   + (b'hex: error: unrecognized argument: -t\n')
  >   - (b"error: invalid value '2' for '--color <color>'\n  [possible values: 0, 1]"
  >   -  b"\n\nFor more information, try '--help'.\n")
- `tests.test_color.test_color_flag_missing_value`
  > assert b'hex: error:...rgument: -t\n' == b"error: inva...y '--help'.\n"
  >   
  >   At index 0 diff: b'h' != b'e'
  >   
  >   Full diff:
  >   + (b'hex: error: unrecognized argument: -t\n')
  >   - (b"error: invalid value '/workspace/eval/test_resources/test_color/test_bytes.b"
  >   -  b"in' for '--color <color>'\n  [possible values: 0, 1]\n\nFor more informatio"
- *(... 42 more in this cluster)*

### `string_output_mismatch` — 36 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_exact_output.test_help_output_exact`
  > AssertionError: assert 'hex 0.1.0\nu...rray output\n' == 'Futuristic t...int version\n'
  >   
  >   + hex 0.1.0
  >   + usage: hex [OPTIONS] [ARGS]
  >   - Futuristic take on hexdump, made in Rust.
  >   - 
  >   - 
  >   - Usage: executable [OPTIONS] [INPUTFILE]...
- `tests.test_exact_output.test_version_output_exact`
  > AssertionError: assert 'hex 0.1.0\n' == 'hx 0.7.0\n'
  >   
  >   - hx 0.7.0
  >   ?      ^
  >   + hex 0.1.0
  >   ?  +    ^
- `tests.test_exact_output.test_tiny_file_output_exact`
  > AssertionError: assert '00000000: 0a...          .\n' == '0x000000: 0x...   bytes: 3\n'
  >   
  >   - 0x000000: 0x69 0x6c 0x0a                                    il.
  >   ?  ^        ------------                                      ^^
  >   + 00000000: 0a                                               .
  >   ?  ^                                              ^^^^^^^^^^^
  >   -    bytes: 3
- *(... 33 more in this cluster)*

### `rc_unexpected_zero` — 21 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_error_handling.test_invalid_format_value`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '-f', 'z'], returncode=0, stdout=b'00000000: 74 65 73 74                                      test\n', stderr=b'').returncode
- `tests.test_errors.test_unknown_format`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '-f', 'z'], returncode=0, stdout=b'00000000: 74 65 73 74                                      test\n', stderr=b'').returncode
- `tests.test_errors.test_invalid_format_option`
  > assert 0 != 0
- *(... 18 more in this cluster)*

### `rc_mismatch_got2_want1` — 20 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_argparse_validation.test_dash_dash_makes_following_token_positional_and_can_error_as_extra_arg`
  > AssertionError: assert 2 == 1
  >  +  where 2 = RunResult(code=2, out='', err='hex: error: unrecognized argument: --\n').code
- `eval.tests.test_argparse_validation.test_integer_options_reject_non_integers[args0-extra0]`
  > assert 2 == 1
  >  +  where 2 = RunResult(code=2, out='', err="hex: error: invalid value 'notint' for '--cols <columns>'\n").code
- `eval.tests.test_argparse_validation.test_integer_options_reject_non_integers[args1-extra1]`
  > assert 2 == 1
  >  +  where 2 = RunResult(code=2, out='', err="hex: error: invalid value 'notint' for '--cols <columns>'\n").code
- *(... 17 more in this cluster)*

### `returned_none` — 7 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_output_structure.test_address_format`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7fe478226680>(b'0x[0-9a-fA-F]{6}:', b'00000000: 41 42 43                                         ABC\n')
  >  +    where <function search at 0x7fe478226680> = re.search
  >  +    and   b'00000000: 41 42 43                                         ABC\n' = CompletedProcess(args=['./executable', '/tmp/tmpa2gn_rwx/test.txt'], returncode=0, stdout=b'00000000: 41 42 43        
- `tests.test_output_structure.test_byte_count_footer`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7fe478226680>(b'bytes:\\s*5', b'00000000: 41 42 43 44 45                                   ABCDE\n')
  >  +    where <function search at 0x7fe478226680> = re.search
  >  +    and   b'00000000: 41 42 43 44 45                                   ABCDE\n' = CompletedProcess(args=['./executable', '/tmp/tmpvf5rwuct/test.txt'], returncode=0, stdout=b'00000000: 41 42 43 44 45
- `eval.tests.test_help_usage.test_help_usage_line_regex`
  > assert None is not None
- *(... 4 more in this cluster)*

### `rc_mismatch_got0_want2` — 5 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `eval.tests.test_argparse_validation.test_missing_value_for_value_options[args8-a value is required for '--array <array_format>']`
  > AssertionError: assert 0 == 2
  >  +  where 0 = RunResult(code=0, out='[]\n', err='').code
- `eval.tests.test_argparse_validation.test_bool_like_choices_reject_other_values[args1]`
  > AssertionError: assert 0 == 2
  >  +  where 0 = RunResult(code=0, out='\n', err='').code
- `eval.tests.test_argparse_validation.test_enum_choices_reject_invalid[args0]`
  > AssertionError: assert 0 == 2
  >  +  where 0 = RunResult(code=0, out='\n', err='').code
- *(... 2 more in this cluster)*

### `rc_mismatch_got0_want4` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_hx_io.test_cols_changes_row_width`
  > AssertionError: assert 0 == 4
  >  +  where 0 = len([])
  >  +    where [] = <function findall at 0x7fcfc5dca170>(b'0x[0-9a-fA-F]{2}', b' 61 62 63 64  abcd')
  >  +      where <function findall at 0x7fcfc5dca170> = re.findall

### `rc_mismatch_got1_want0` — 1 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_core.test_column_zero_defaults_to_one`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-c', '0'], returncode=1, stdout=b'', stderr=b'Traceback (most recent call last):\n  File "/workspace/main.py", line 329, in <module>\n   

### `rc_mismatch_got1_want2` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_display.test_column_width_larger_than_file`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len([b'00000000: 00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f 10 11 12 13 14 15 16 17 18 19 1a 1b 1c 1d 1e 1f                                                                          

### `boolean_false` — 1 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_errors.test_broken_pipe_handling_exit_zero`
  > assert False
  >  +  where False = <built-in method startswith of bytes object at 0x7f5cc9614030>(b'0x000000:')
  >  +    where <built-in method startswith of bytes object at 0x7f5cc9614030> = b''.startswith
  >  +      where b'' = CompletedProcess(args=['sh', '-c', "echo '0123456789abcdef0123456789abcdef' | ./executable | head -n 1"], returncode=0, stdout=b'', stderr=b'usage: hex [OPTIONS] [ARGS]\n').stdout

### `rc_mismatch_got0_want1` — 1 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_errors.test_len_overflow_value`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-l', '99999999999999999999'], returncode=0, stdout=b'00000000: 74 65 73 74                                      test\n', stderr=b'').retu

