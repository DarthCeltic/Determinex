# Action Sheet — ecumene__rust-sloth.051c559

**Current:** 4.5%  (26/578)
**Pass / Fail / Skip:** 26 / 397 / 4
**Gap to 100%:** 95.50 percentage points (552 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_subcommand_dispatch.test_subcommand_has_help_route[NOTSET]`
  - reason: got empty parameter set for (subcmd)
- `eval.tests.test_image_rendering.test_image_contains_ansi_csi_sequences`
  - reason: test_image_contains_ansi_csi_sequences depends on image_snapshot_small_exact
- `eval.tests.test_image_rendering.test_image_newline_count_for_h10`
  - reason: test_image_newline_count_for_h10 depends on image_snapshot_small_exact
- `eval.tests.test_image_rendering.test_rotation_flags_change_output`
  - reason: test_rotation_flags_change_output depends on image_snapshot_small_exact

## Failure clusters

397 failed tests grouped into 9 buckets (sorted by count).

### `other_assertion` — 225 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_help_flag`
  > AssertionError: assert b'USAGE:' in b'rust-sloth 0.1.0\n\nusage: rust-sloth [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n'
  >  +  where b'rust-sloth 0.1.0\n\nusage: rust-sloth [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['./executable', '--help'], retur
- `tests.test_basic_invocation.test_help_flag_short`
  > AssertionError: assert b'USAGE:' in b'rust-sloth 0.1.0\n\nusage: rust-sloth [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n'
  >  +  where b'rust-sloth 0.1.0\n\nusage: rust-sloth [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['./executable', '-h'], returncod
- `tests.test_basic_invocation.test_version_flag`
  > AssertionError: assert b'Sloth' in b'rust-sloth 0.1.0\n'
  >  +  where b'rust-sloth 0.1.0\n' = CompletedProcess(args=['./executable', '--version'], returncode=0, stdout=b'rust-sloth 0.1.0\n', stderr=b'').stdout
- *(... 222 more in this cluster)*

### `rc_mismatch_got2_want0` — 156 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_basic_invocation.test_help_subcommand`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', 'help'], returncode=2, stdout=b'', stderr=b'usage: rust-sloth [OPTIONS] [ARGS]\n').returncode
- `tests.test_basic_invocation.test_image_help`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', 'image', '--help'], returncode=2, stdout=b'', stderr=b'usage: rust-sloth [OPTIONS] [ARGS]\n').returncode
- `tests.test_color_modes.test_no_color_flag_main`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', 'models/cube.obj', '-b', 'image', '-w', '10', '-h', '10'], returncode=2, stdout=b'', stderr=b'usage: rust-sloth [OPTIONS] [ARGS]\n').returncode
- *(... 153 more in this cluster)*

### `string_output_mismatch` — 6 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_version.test_version_exact_string`
  > AssertionError: assert 'rust-sloth 0.1.0\n' == 'Sloth 0.1\n'
  >   
  >   - Sloth 0.1
  >   + rust-sloth 0.1.0
- `eval.tests.test_help_main.test_main_help_baseline_match_ignoring_version_header_only`
  > AssertionError: assert 'rust-sloth 0...int version\n' == 'Mitchell Hyn...nes of text\n'
  >   
  >   + rust-sloth 0.1.0
  >   - Mitchell Hynes. <mshynes@mun.ca>
  >   - A toy for rendering 3D objects in the command line
  >     
  >   + usage: rust-sloth [OPTIONS] [ARGS]
  >   - USAGE:...
- `tests.test_image_basic.test_missing_width_flag_error`
  > AssertionError: assert 'usage: rust-...ONS] [ARGS]\n' == 'error: The f... try --help\n'
  >   
  >   + usage: rust-sloth [OPTIONS] [ARGS]
  >   - error: The following required arguments were not provided:
  >   -     -w <width>
  >   - 
  >   - USAGE:
  >   -     executable image [FLAGS] [OPTIONS] -w <width>
- *(... 3 more in this cluster)*

### `boolean_false` — 2 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `eval.tests.test_argparse_validation.test_image_width_missing_value_flag_only`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7fb2c84cbc30>('error:')
  >  +    where <built-in method startswith of str object at 0x7fb2c84cbc30> = 'usage: rust-sloth [OPTIONS] [ARGS]\n'.startswith
  >  +      where 'usage: rust-sloth [OPTIONS] [ARGS]\n' = RunResult(rc=2, out='', err='usage: rust-sloth [OPTIONS] [ARGS]\n').err
- `eval.tests.test_help_image.test_image_help_trailing_newline_present`
  > AssertionError: assert False
  >  +  where False = <built-in method endswith of str object at 0x7fc5f71b4030>('\n')
  >  +    where <built-in method endswith of str object at 0x7fc5f71b4030> = ''.endswith

### `rc_mismatch_got2_want101` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_errors.test_nonexistent_input_panics_with_rc_101_and_message`
  > AssertionError: assert 2 == 101
  >  +  where 2 = RunResult(returncode=2, stdout=b'', stderr=b'usage: rust-sloth [OPTIONS] [ARGS]\n').returncode
- `eval.tests.test_errors.test_nonexistent_input_panics_with_101`
  > AssertionError: assert 2 == 101
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'not_a_file.obj', 'image', '-w', '10', '-h', '5'], returncode=2, stdout=b'', stderr=b'usage: rust-sloth [OPTIONS] [ARGS]\n').returncode

### `empty_list_or_string` — 2 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `eval.tests.test_help_main.test_main_help_lists_subcommands[help]`
  > IndexError: list index out of range
- `eval.tests.test_help_main.test_main_help_lists_subcommands[image]`
  > IndexError: list index out of range

### `bytes_output_mismatch` — 2 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `eval.tests.test_help_and_version.test_help_exact`
  > assert b'rust-sloth ...int version\n' == b"Sloth 0.1\n...nes of text\n"
  >   
  >   At index 0 diff: b'r' != b'S'
  >   
  >   Full diff:
  >   + (b'rust-sloth 0.1.0\n\nusage: rust-sloth [OPTIONS] [ARGS]\n\nOptions:\n  -h,'
  >   +  b' --help     Print help\n  -V, --version  Print version\n')
  >   - (b'Sloth 0.1\nMitchell Hynes. <mshynes@mun.ca>\nA toy for rendering 3D object'...
- `eval.tests.test_help_and_version.test_version`
  > AssertionError: assert b'rust-sloth 0.1.0' == b'Sloth 0.1'
  >   
  >   At index 0 diff: b'r' != b'S'
  >   
  >   Full diff:
  >   - (b'Sloth 0.1')
  >   + (b'rust-sloth 0.1.0')

### `returned_none` — 1 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_image.test_image_help_usage_mentions_width_required_flag`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7fc5f7126680>('-w\\s+<width>', '')
  >  +    where <function search at 0x7fc5f7126680> = re.search

### `uncategorized` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_help_main.test_main_help_has_expected_sections_in_order`
  > ValueError: substring not found

