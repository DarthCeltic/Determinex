# Action Sheet — sharkdp__pastel.b60e899

**Current:** 6.67%  (98/1470)
**Pass / Fail / Skip:** 98 / 1058 / 0
**Gap to 100%:** 93.33 percentage points (1372 tests)

## Failure clusters

1058 failed tests grouped into 27 buckets (sorted by count).

### `other_assertion` — 440 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_amount_commands.test_darken_basic`
  > AssertionError: assert b'hsl' in b''
  >  +  where b'' = CompletedProcess(args=['./executable', 'darken', '0.2', 'red'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_amount_commands.test_darken_negative`
  > AssertionError: assert b'hsl' in b''
  >  +  where b'' = CompletedProcess(args=['./executable', 'darken', '--', '-0.2', 'red'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_amount_commands.test_darken_edge_zero`
  > AssertionError: assert b'hsl' in b''
  >  +  where b'' = CompletedProcess(args=['./executable', 'darken', '0.0', 'red'], returncode=0, stdout=b'', stderr=b'').stdout
- *(... 437 more in this cluster)*

### `string_output_mismatch` — 295 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_advanced.test_gradient_default_count`
  > AssertionError: assert '' == 'hsl(0,100.0%...0.0%,50.0%)\n'
  >   
  >   - hsl(0,100.0%,50.0%)
  >   - hsl(349,100.0%,48.0%)
  >   - hsl(341,100.0%,46.1%)
  >   - hsl(333,100.0%,43.7%)
  >   - hsl(324,100.0%,41.0%)
  >   - hsl(314,100.0%,37.8%)...
- `tests.test_advanced.test_gradient_custom_count_3`
  > AssertionError: assert '' == 'hsl(0,100.0%...0.0%,50.0%)\n'
  >   
  >   - hsl(0,100.0%,50.0%)
  >   - hsl(320,100.0%,39.6%)
  >   - hsl(240,100.0%,50.0%)
- `tests.test_advanced.test_gradient_custom_count_5`
  > AssertionError: assert '' == 'hsl(0,100.0%...0.0%,50.0%)\n'
  >   
  >   - hsl(0,100.0%,50.0%)
  >   - hsl(339,100.0%,45.5%)
  >   - hsl(320,100.0%,39.6%)
  >   - hsl(287,100.0%,38.2%)
  >   - hsl(240,100.0%,50.0%)
- *(... 292 more in this cluster)*

### `rc_unexpected_zero` — 78 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_basic.test_invalid_command`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'invalid_command_xyz'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_color_command.test_color_invalid`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'color', 'not_a_color'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_color_input.test_invalid_color_format`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'color', 'not_a_color_xyz'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 75 more in this cluster)*

### `rc_mismatch_got0_want1` — 42 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_utility_commands.test_gray_multiple_values`
  > AssertionError: assert 0 == 1
  >  +  where 0 = <built-in method count of bytes object at 0x7d74f0224030>(b'\n')
  >  +    where <built-in method count of bytes object at 0x7d74f0224030> = b''.count
  >  +      where b'' = CompletedProcess(args=['/workspace/executable', 'gray', '0.5'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_advanced.test_sortby_single_color`
  > assert 0 == 1
  >  +  where 0 = len([])
- `tests.test_colorspace.test_gradient_error_on_count_one`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'gradient', '--colorspace=Lab', '--number=1', 'red', 'blue'], returncode=0, stdout='', stderr='').returncode
- *(... 39 more in this cluster)*

### `rc_mismatch_got2_want0` — 27 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_basic.test_color_mode_24bit`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--color-mode', '24bit', 'color', 'red'], returncode=2, stdout=b'', stderr=b"pastel: unknown option: --color-mode\nusage: pastel [OPTIONS] [ARGS]\n
- `tests.test_basic.test_color_mode_8bit`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '-m', '8bit', 'color', 'red'], returncode=2, stdout=b'', stderr=b"pastel: unknown option: -m\nusage: pastel [OPTIONS] [ARGS]\nTry 'pastel --help' f
- `tests.test_basic.test_color_mode_off`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '-m', 'off', 'color', 'red'], returncode=2, stdout=b'', stderr=b"pastel: unknown option: -m\nusage: pastel [OPTIONS] [ARGS]\nTry 'pastel --help' fo
- *(... 24 more in this cluster)*

### `rc_mismatch_got0_want2` — 25 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_amount_commands.test_lighten_multiple`
  > AssertionError: assert 0 == 2
  >  +  where 0 = <built-in method count of bytes object at 0x772971670030>(b'hsl')
  >  +    where <built-in method count of bytes object at 0x772971670030> = b''.count
  >  +      where b'' = CompletedProcess(args=['./executable', 'lighten', '0.3', 'red', 'blue'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_amount_commands.test_desaturate_multiple`
  > AssertionError: assert 0 == 2
  >  +  where 0 = <built-in method count of bytes object at 0x772971670030>(b'hsl')
  >  +    where <built-in method count of bytes object at 0x772971670030> = b''.count
  >  +      where b'' = CompletedProcess(args=['./executable', 'desaturate', '0.3', 'red', 'green'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_amount_commands.test_rotate_multiple`
  > AssertionError: assert 0 == 2
  >  +  where 0 = <built-in method count of bytes object at 0x772971670030>(b'hsl')
  >  +    where <built-in method count of bytes object at 0x772971670030> = b''.count
  >  +      where b'' = CompletedProcess(args=['./executable', 'rotate', '180', 'red', 'blue'], returncode=0, stdout=b'', stderr=b'').stdout
- *(... 22 more in this cluster)*

### `rc_mismatch_got0_want3` — 24 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_amount_commands.test_darken_multiple`
  > AssertionError: assert 0 == 3
  >  +  where 0 = <built-in method count of bytes object at 0x772971670030>(b'hsl')
  >  +    where <built-in method count of bytes object at 0x772971670030> = b''.count
  >  +      where b'' = CompletedProcess(args=['./executable', 'darken', '0.1', 'red', 'green', 'blue'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_colorblind.test_colorblind_multiple_colors`
  > AssertionError: assert 0 == 3
  >  +  where 0 = <built-in method count of bytes object at 0x772971670030>(b'hsl')
  >  +    where <built-in method count of bytes object at 0x772971670030> = b''.count
  >  +      where b'' = CompletedProcess(args=['./executable', 'colorblind', 'prot', 'red', 'green', 'blue'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_piping.test_pipe_distinct_to_colorblind`
  > AssertionError: assert 0 == 3
  >  +  where 0 = <built-in method count of bytes object at 0x772971670030>(b'hsl')
  >  +    where <built-in method count of bytes object at 0x772971670030> = b''.count
  >  +      where b'' = CompletedProcess(args=['./executable', 'colorblind', 'deuter'], returncode=0, stdout=b'', stderr=b'').stdout
- *(... 21 more in this cluster)*

### `rc_mismatch_got1_want3` — 22 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_ansi_formats.test_ansi_8bit_value_multiple_colors`
  > AssertionError: assert 1 == 3
  >  +  where 1 = len([''])
- `tests.test_ansi_formats.test_ansi_8bit_grayscale_colors`
  > AssertionError: assert 1 == 3
  >  +  where 1 = len([''])
- `tests.test_ansi_formats.test_ansi_8bit_cube_colors`
  > AssertionError: assert 1 == 3
  >  +  where 1 = len([''])
- *(... 19 more in this cluster)*

### `rc_mismatch_got0_want10` — 19 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_gradient.test_gradient_basic`
  > AssertionError: assert 0 == 10
  >  +  where 0 = <built-in method count of bytes object at 0x772971670030>(b'hsl')
  >  +    where <built-in method count of bytes object at 0x772971670030> = b''.count
  >  +      where b'' = CompletedProcess(args=['./executable', 'gradient', 'red', 'blue'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_gradient.test_gradient_three_stops`
  > AssertionError: assert 0 == 10
  >  +  where 0 = <built-in method count of bytes object at 0x772971670030>(b'hsl')
  >  +    where <built-in method count of bytes object at 0x772971670030> = b''.count
  >  +      where b'' = CompletedProcess(args=['./executable', 'gradient', 'red', 'green', 'blue'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_gradient.test_gradient_many_stops`
  > AssertionError: assert 0 == 10
  >  +  where 0 = <built-in method count of bytes object at 0x772971670030>(b'hsl')
  >  +    where <built-in method count of bytes object at 0x772971670030> = b''.count
  >  +      where b'' = CompletedProcess(args=['./executable', 'gradient', 'red', 'orange', 'yellow', 'green', 'blue'], returncode=0, stdout=b'', stderr=b'').stdout
- *(... 16 more in this cluster)*

### `boolean_false` — 17 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_color_input.test_gray_format`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of bytes object at 0x772971670030>(b'#')
  >  +    where <built-in method startswith of bytes object at 0x772971670030> = b''.startswith
  >  +      where b'' = CompletedProcess(args=['./executable', 'format', 'hex', 'gray(50)'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_ansi_formats.test_ansi_8bit_value_format`
  > AssertionError: assert False
  >  +  where False = <built-in method isdigit of str object at 0x7d74f0228030>()
  >  +    where <built-in method isdigit of str object at 0x7d74f0228030> = ''.isdigit
- `tests.test_color_input_formats.test_gray_format`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of bytes object at 0x7d74f0224030>(b'#')
  >  +    where <built-in method startswith of bytes object at 0x7d74f0224030> = b''.startswith
  >  +      where b'' = CompletedProcess(args=['/workspace/executable', 'format', 'hex', 'gray(0.5)'], returncode=0, stdout=b'', stderr=b'').stdout
- *(... 14 more in this cluster)*

### `rc_mismatch_got0_want5` — 17 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_gradient.test_gradient_custom_count`
  > AssertionError: assert 0 == 5
  >  +  where 0 = <built-in method count of bytes object at 0x772971670030>(b'hsl')
  >  +    where <built-in method count of bytes object at 0x772971670030> = b''.count
  >  +      where b'' = CompletedProcess(args=['./executable', 'gradient', '-n', '5', 'red', 'blue'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_piping.test_pipe_random_to_sort`
  > AssertionError: assert 0 == 5
  >  +  where 0 = <built-in method count of bytes object at 0x772971670030>(b'hsl')
  >  +    where <built-in method count of bytes object at 0x772971670030> = b''.count
  >  +      where b'' = CompletedProcess(args=['./executable', 'sort-by', 'hue'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_piping.test_pipe_gradient_to_format`
  > AssertionError: assert 0 == 5
  >  +  where 0 = <built-in method count of bytes object at 0x772971670030>(b'#')
  >  +    where <built-in method count of bytes object at 0x772971670030> = b''.count
  >  +      where b'' = CompletedProcess(args=['./executable', 'format', 'hex'], returncode=0, stdout=b'', stderr=b'').stdout
- *(... 14 more in this cluster)*

### `rc_mismatch_got0_want50` — 13 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_gradient.test_gradient_large_count`
  > AssertionError: assert 0 == 50
  >  +  where 0 = <built-in method count of bytes object at 0x772971670030>(b'hsl')
  >  +    where <built-in method count of bytes object at 0x772971670030> = b''.count
  >  +      where b'' = CompletedProcess(args=['./executable', 'gradient', '-n', '50', 'red', 'blue'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_edge_cases.test_distinct_with_large_count`
  > assert 0 == 50
  >  +  where 0 = len([])
- `tests.test_batch_performance.test_format_rgb_conversion_batch`
  > assert 0 == 50
  >  +  where 0 = len([])
- *(... 10 more in this cluster)*

### `bytes_output_mismatch` — 8 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_env_config.test_default_piped_output_is_uncolored`
  > AssertionError: assert b'' == b'test\n'
  >   
  >   Full diff:
  >   - (b'test\n')
  >   + b''
- `tests.test_env_config.test_pastel_color_mode_off_disables_color_even_when_tty`
  > AssertionError: assert b'' == b'test\n'
  >   
  >   Full diff:
  >   - (b'test\n')
  >   + b''
- `eval.tests.test_format_io.test_format_hex_reads_stdin_when_no_color_args`
  > AssertionError: assert b'' == b'#ff0000\n#00ff00\n'
  >   
  >   Full diff:
  >   - (b'#ff0000\n#00ff00\n')
  >   + b''
- *(... 5 more in this cluster)*

### `rc_mismatch_got1_want2` — 7 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_colorspace.test_gradient_minimum_size_two_colors`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len([''])
- `tests.test_manipulation.TestSaturateDesaturate.test_desaturate_multiple_colors`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len([''])
- `tests.test_manipulation.TestComplement.test_complement_multiple`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len([''])
- *(... 4 more in this cluster)*

### `rc_mismatch_got0_want20` — 5 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_random_distinct.test_distinct_large_count`
  > AssertionError: assert 0 == 20
  >  +  where 0 = <built-in method count of bytes object at 0x772971670030>(b'hsl')
  >  +    where <built-in method count of bytes object at 0x772971670030> = b''.count
  >  +      where b'' = CompletedProcess(args=['./executable', 'distinct', '20'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_sort.test_sortby_many_colors`
  > AssertionError: assert 0 == 20
  >  +  where 0 = <built-in method count of bytes object at 0x772971670030>(b'hsl')
  >  +    where <built-in method count of bytes object at 0x772971670030> = b''.count
  >  +      where b'' = CompletedProcess(args=['./executable', 'sort-by', 'hue'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_edge_cases.test_gradient_with_many_stops`
  > assert 0 == 20
  >  +  where 0 = len([])
- *(... 2 more in this cluster)*

### `rc_mismatch_got1_want5` — 5 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_distinct_command.test_distinct_colors_are_different`
  > AssertionError: assert 1 == 5
  >  +  where 1 = len([b''])
- `tests.test_error_handling.test_gradient_many_input_colors_10_colors`
  > AssertionError: assert 1 == 5
  >  +  where 1 = len([''])
- `tests.test_generation.TestRandom.test_random_custom_count`
  > AssertionError: assert 1 == 5
  >  +  where 1 = len([''])
- *(... 2 more in this cluster)*

### `rc_mismatch_got0_want100` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_edge_cases.test_very_long_input_line`
  > AssertionError: assert 0 == 100
  >  +  where 0 = <built-in method count of bytes object at 0x772971670030>(b'hsl')
  >  +    where <built-in method count of bytes object at 0x772971670030> = b''.count
  >  +      where b'' = CompletedProcess(args=['./executable', 'color', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red',
- `tests.test_random_distinct.test_random_large_count`
  > AssertionError: assert 0 == 100
  >  +  where 0 = <built-in method count of bytes object at 0x772971670030>(b'hsl')
  >  +    where <built-in method count of bytes object at 0x772971670030> = b''.count
  >  +      where b'' = CompletedProcess(args=['./executable', 'random', '-n', '100'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_edge_cases.test_random_with_large_number`
  > assert 0 == 100
  >  +  where 0 = len([])

### `rc_mismatch_got1_want10` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_generation.TestRandom.test_random_default`
  > AssertionError: assert 1 == 10
  >  +  where 1 = len([''])
- `tests.test_mix_gradient.TestGradient.test_gradient_default_count`
  > AssertionError: assert 1 == 10
  >  +  where 1 = len([''])

### `rc_mismatch_got0_want1000` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_edge_cases.test_very_large_count`
  > AssertionError: assert 0 == 1000
  >  +  where 0 = <built-in method count of bytes object at 0x772971670030>(b'hsl')
  >  +    where <built-in method count of bytes object at 0x772971670030> = b''.count
  >  +      where b'' = CompletedProcess(args=['./executable', 'random', '-n', '1000'], returncode=0, stdout=b'', stderr=b'').stdout

### `returned_none` — 1 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_format_command.test_format_ansi_8bit_value`
  > AssertionError: assert None
  >  +  where None = <function match at 0x7d74f0146170>(b'\\d+', b'')
  >  +    where <function match at 0x7d74f0146170> = re.match
  >  +    and   b'' = <built-in method strip of bytes object at 0x7d74f0224030>()
  >  +      where <built-in method strip of bytes object at 0x7d74f0224030> = b''.strip
  >  +        where b'' = CompletedProcess(args=['/workspace/executable', 'format', 'ansi-8bit-value', 'red'], returncode=0, stdout=b'', stderr=b'').stdout

### `rc_mismatch_got0_want4` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_advanced.test_sortby_already_sorted`
  > assert 0 == 4
  >  +  where 0 = len([])

### `rc_mismatch_got0_want6` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_advanced.test_sortby_luminance_verify_order`
  > assert 0 == 6
  >  +  where 0 = len([])

### `rc_mismatch_got1_want1000` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_error_handling.test_very_large_gradient_1000_colors`
  > AssertionError: assert 1 == 1000
  >  +  where 1 = len([''])

### `rc_mismatch_got1_want100` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_error_handling.test_very_large_stdin_input_100_colors`
  > AssertionError: assert 1 == 100
  >  +  where 1 = len([''])

### `rc_mismatch_got1_want50` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_error_handling.test_distinct_large_count_50_colors`
  > AssertionError: assert 1 == 50
  >  +  where 1 = len([''])

### `empty_list_or_string` — 1 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `eval.tests.test_subcommand_dispatch.test_subcommand_help_differs_from_main_help`
  > IndexError: list index out of range

### `rc_mismatch_got1_want20` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_generation.TestDistinct.test_distinct_large_count`
  > AssertionError: assert 1 == 20
  >  +  where 1 = len([''])

