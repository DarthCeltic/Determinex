# Action Sheet — ivanceras__svgbob.6d00ad9

**Current:** 0.72%  (4/554)
**Pass / Fail / Skip:** 4 / 427 / 0
**Gap to 100%:** 99.28 percentage points (550 tests)

## Failure clusters

427 failed tests grouped into 9 buckets (sorted by count).

### `subprocess_failed` — 162 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_circle_shapes.test_circle_scale_factor`
  > subprocess.CalledProcessError: Command '['/workspace/executable', '--scale', '2.0']' returned non-zero exit status 2.
- `tests.test_circle_shapes.test_circle_scale_factor_half`
  > subprocess.CalledProcessError: Command '['/workspace/executable', '--scale', '0.5']' returned non-zero exit status 2.
- `tests.test_circle_shapes.test_circle_scale_factor_3x`
  > subprocess.CalledProcessError: Command '['/workspace/executable', '--scale', '3.0', '/workspace/eval/test_resources/test_circle_shapes/scale_test.bob']' returned non-zero exit status 2.
- *(... 159 more in this cluster)*

### `rc_mismatch_got2_want0` — 75 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_svgbob.test_stdin_input_produces_svg`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable'], returncode=2, stdout=b'', stderr=b"usage: svgbob [OPTIONS] [ARGS]\nTry 'svgbob --help' for more information.\n").returncode
- `tests.test_svgbob.test_inline_string_flag`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '-s', '+--+'], returncode=2, stdout=b'', stderr=b"svgbob: unknown option: -s\nusage: svgbob [OPTIONS] [ARGS]\nTry 'svgbob --help' for more informat
- `tests.test_svgbob.test_inline_string_with_newline_escape`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '-s', '+--+\\n|  |\\n+--+'], returncode=2, stdout=b'', stderr=b"svgbob: unknown option: -s\nusage: svgbob [OPTIONS] [ARGS]\nTry 'svgbob --help' for
- *(... 72 more in this cluster)*

### `other_assertion` — 65 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_svgbob.test_help_flag_long`
  > AssertionError: assert b'USAGE' in b'svgbob 0.1.0 - bootstrap scaffold\n\nUsage: svgbob [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n'
  >  +  where b'svgbob 0.1.0 - bootstrap scaffold\n\nUsage: svgbob [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['./executable', '--
- `tests.test_svgbob.test_help_flag_short`
  > AssertionError: assert b'USAGE' in b'svgbob 0.1.0 - bootstrap scaffold\n\nUsage: svgbob [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n'
  >  +  where b'svgbob 0.1.0 - bootstrap scaffold\n\nUsage: svgbob [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['./executable', '-h
- `tests.test_svgbob.test_help_mentions_subcommands`
  > AssertionError: assert b'build' in b'svgbob 0.1.0 - bootstrap scaffold\n\nUsage: svgbob [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n'
  >  +  where b'svgbob 0.1.0 - bootstrap scaffold\n\nUsage: svgbob [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['./executable', '--
- *(... 62 more in this cluster)*

### `rc_mismatch_got0_want1` — 54 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_svgbob.test_nonexistent_file_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', '/tmp/does_not_exist_12345.bob'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_svgbob.test_build_error_nonexistent_input_dir`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', 'build', '-i', '/nonexistent_parent_abc123/subdir'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_svgbob.test_build_no_input_uses_default_pattern`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', 'build'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 51 more in this cluster)*

### `string_output_mismatch` — 24 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_build_subcommand.test_build_help_flag`
  > AssertionError: assert '' == 'executable-b...f svg files\n'
  >   
  >   - executable-build 0.0.1
  >   - Batch convert files to svg.
  >   - 
  >   - USAGE:
  >   -     executable build [OPTIONS]
  >   - ...
- `tests.test_build_subcommand.test_build_version_flag`
  > AssertionError: assert '' == 'executable-build 0.0.1\n'
  >   
  >   - executable-build 0.0.1
- `tests.test_cli_flags.test_help_flag`
  > AssertionError: assert 'svgbob 0.1.0...int version\n' == 'svgbob 0.7.6...bcommand(s)\n'
  >   
  >   + svgbob 0.1.0 - bootstrap scaffold
  >   - svgbob 0.7.6
  >   - SvgBobRus is an ascii to svg converter
  >     
  >   + Usage: svgbob [OPTIONS] [ARGS]
  >   - USAGE:...
- *(... 21 more in this cluster)*

### `uncategorized` — 20 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_flags.test_file_input_mode`
  > xml.etree.ElementTree.ParseError: no element found: line 1, column 0
- `tests.test_core_conversion.test_nested_boxes`
  > xml.etree.ElementTree.ParseError: no element found: line 1, column 0
- `tests.test_core_conversion.test_connecting_lines_between_boxes`
  > xml.etree.ElementTree.ParseError: no element found: line 1, column 0
- *(... 17 more in this cluster)*

### `returned_none` — 13 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_complex_diagrams.test_large_architecture_diagram_with_legend`
  > assert None is not None
- `tests.test_complex_diagrams.test_legend_with_multiple_css_classes_per_shape`
  > assert None is not None
- `tests.test_complex_diagrams.test_legend_edge_cases_whitespace_newlines`
  > assert None is not None
- *(... 10 more in this cluster)*

### `boolean_false` — 8 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_svgbob.test_build_converts_bob_files`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = (PosixPath('/tmp/tmpqlpx4xqf/output') / 'test.svg').exists
- `tests.test_svgbob.test_build_creates_output_dir`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpkd265mte/new_output_dir').exists
- `tests.test_svgbob.test_build_default_output_same_dir`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = (PosixPath('/tmp/tmpp9_afe2x/input') / 'myfile.svg').exists
- *(... 5 more in this cluster)*

### `rc_mismatch_got2_want1` — 6 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_svgbob.test_invalid_font_size_error`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['./executable', '--font-size', 'notanumber'], returncode=2, stdout=b'', stderr=b"svgbob: unknown option: --font-size\nusage: svgbob [OPTIONS] [ARGS]\nTry 'svgbob -
- `tests.test_svgbob.test_invalid_stroke_width_error`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['./executable', '--stroke-width', 'abc'], returncode=2, stdout=b'', stderr=b"svgbob: unknown option: --stroke-width\nusage: svgbob [OPTIONS] [ARGS]\nTry 'svgbob --
- `tests.test_svgbob.test_invalid_scale_error`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['./executable', '--scale', 'notafloat'], returncode=2, stdout=b'', stderr=b"svgbob: unknown option: --scale\nusage: svgbob [OPTIONS] [ARGS]\nTry 'svgbob --help' fo
- *(... 3 more in this cluster)*

