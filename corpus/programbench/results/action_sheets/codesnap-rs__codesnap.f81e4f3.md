# Action Sheet — codesnap-rs__codesnap.f81e4f3

**Current:** 27.43%  (302/1101)
**Pass / Fail / Skip:** 302 / 547 / 4
**Gap to 100%:** 72.57 percentage points (799 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_highlight_ranges.test_highlight_with_breadcrumbs`
  - reason: gold-env-limitation: Font rendering produces environment-specific SVG output. Worker produces 979KB (6219b23e...), gold produces 996KB (499c44e1...). See binary_notes.md for details.
- `tests.test_input_sources.test_with_breadcrumbs_exact_golden`
  - reason: pytest hangs showing diff of 700KB+ golden files
- `tests.test_input_sources.test_combined_flags_exact_golden`
  - reason: pytest hangs showing diff of 700KB+ golden files
- `tests.test_output_formats.test_large_code_file_processes_without_crash`
  - reason: Binary is too slow with large inputs (>30s timeout), performance issue not format issue

## Failure clusters

547 failed tests grouped into 12 buckets (sorted by count).

### `other_assertion` — 285 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_additional_coverage.test_language_with_file_path`
  > AssertionError: assert 364 > 1000
  >  +  where 364 = os.stat_result(st_mode=33188, st_ino=2942977, st_dev=51, st_nlink=1, st_uid=0, st_gid=0, st_size=364, st_atime=1779049790, st_mtime=1779049790, st_ctime=1779049790).st_size
  >  +    where os.stat_result(st_mode=33188, st_ino=2942977, st_dev=51, st_nlink=1, st_uid=0, st_gid=0, st_size=364, st_atime=1779049790, st_mtime=1779049790, st_ctime=1779049790) = stat()
  >  +      where stat = PosixPath('/tmp/tmp19mzoamt/output.png').stat
- `tests.test_additional_coverage.test_all_window_options_combined`
  > AssertionError: assert 485 > 1000
  >  +  where 485 = os.stat_result(st_mode=33188, st_ino=2944423, st_dev=51, st_nlink=1, st_uid=0, st_gid=0, st_size=485, st_atime=1779049799, st_mtime=1779049799, st_ctime=1779049799).st_size
  >  +    where os.stat_result(st_mode=33188, st_ino=2944423, st_dev=51, st_nlink=1, st_uid=0, st_gid=0, st_size=485, st_atime=1779049799, st_mtime=1779049799, st_ctime=1779049799) = stat()
  >  +      where stat = PosixPath('/tmp/tmp8hprzez8/output.png').stat
- `tests.test_additional_coverage.test_all_code_options_combined`
  > AssertionError: assert 624 > 1000
  >  +  where 624 = os.stat_result(st_mode=33188, st_ino=2944910, st_dev=51, st_nlink=1, st_uid=0, st_gid=0, st_size=624, st_atime=1779049801, st_mtime=1779049801, st_ctime=1779049801).st_size
  >  +    where os.stat_result(st_mode=33188, st_ino=2944910, st_dev=51, st_nlink=1, st_uid=0, st_gid=0, st_size=624, st_atime=1779049801, st_mtime=1779049801, st_ctime=1779049801) = stat()
  >  +      where stat = PosixPath('/tmp/tmpuih4_ljl/output.png').stat
- *(... 282 more in this cluster)*

### `bytes_output_mismatch` — 122 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_additional_coverage.test_range_with_line_numbers`
  > AssertionError: assert b'<svg' == b'\x89PNG'
  >   
  >   At index 0 diff: b'<' != b'\x89'
  >   
  >   Full diff:
  >   - b'\x89PNG'
  >   + b'<svg'
- `tests.test_additional_coverage.test_add_delete_lines_with_colors`
  > AssertionError: assert b'<svg' == b'\x89PNG'
  >   
  >   At index 0 diff: b'<' != b'\x89'
  >   
  >   Full diff:
  >   - b'\x89PNG'
  >   + b'<svg'
- `tests.test_additional_coverage.test_scale_factor_one`
  > AssertionError: assert b'<svg' == b'\x89PNG'
  >   
  >   At index 0 diff: b'<' != b'\x89'
  >   
  >   Full diff:
  >   - b'\x89PNG'
  >   + b'<svg'
- *(... 119 more in this cluster)*

### `boolean_false` — 46 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_additional_coverage.test_from_code_empty_default_value`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpu3b0ns8y/output.png').exists
- `tests.test_additional_coverage.test_highlight_lines_single_line_json`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpzl4fow9e/output.png').exists
- `tests.test_additional_coverage.test_relative_highlight_with_range`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpmngl3733/output.png').exists
- *(... 43 more in this cluster)*

### `rc_unexpected_zero` — 20 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_edge_cases.test_negative_scale_factor`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '-c', 'code', '-o', '/tmp/tmppjw4e5f1/output.png', '--scale-factor', '-1'], returncode=0, stdout=b'Output written to /tmp/tmppjw4e5f1/output.png\n'
- `tests.test_edge_cases.test_malformed_json_highlight_lines`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '-c', 'code', '-o', '/tmp/tmpdwgupbvb/output.png', '--raw-highlight-lines', 'not-json'], returncode=0, stdout=b'', stderr=b"usage: codesnap [OPTION
- `tests.test_output_destinations.test_output_unsupported_format`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '-c', 'test', '-o', '/tmp/output.unknown'], returncode=0, stdout=b'Output written to /tmp/output.unknown\n', stderr=b'').returncode
- *(... 17 more in this cluster)*

### `string_output_mismatch` — 20 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_baseline.test_full_help_matches_fixture_exactly_modulo_dynamic_tokens`
  > AssertionError: assert 'usage: codes...number flag\n' == 'CLI tools fo...int version\n'
  >   
  >   - CLI tools for generating beautiful code snapshots
  >   + usage: codesnap [OPTIONS]
  >     
  >   - Usage: codesnap [OPTIONS] --output <OUTPUT>
  >   + Render code snippets as beautiful images
  >     ...
- `eval.tests.test_help_behavior.test_help_starts_with_description_line`
  > AssertionError: assert 'usage: codesnap [OPTIONS]' == 'CLI tools fo...ode snapshots'
  >   
  >   - CLI tools for generating beautiful code snapshots
  >   + usage: codesnap [OPTIONS]
- `eval.tests.test_codesnap_cli.test_version_exact`
  > AssertionError: assert '0.1.0\n' == 'codesnap-cli 0.13.1\n'
  >   
  >   - codesnap-cli 0.13.1
  >   + 0.1.0
- *(... 17 more in this cluster)*

### `rc_mismatch_got0_want2` — 14 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `eval.tests.test_argparse_validation.test_output_missing_value_errors[--output]`
  > assert 0 == 2
- `eval.tests.test_argparse_validation.test_output_missing_value_errors[-o]`
  > assert 0 == 2
- `eval.tests.test_argparse_validation.test_extra_positional_argument_is_rejected`
  > assert 0 == 2
- *(... 11 more in this cluster)*

### `rc_mismatch_got2_want0` — 11 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_additional_coverage.test_execute_with_multiple_args`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '-e', 'echo', 'test', '-o', '/tmp/tmps0ax2tj2/output.png'], returncode=2, stdout=b'', stderr=b'error: no code snippet provided\n').returncode
- `tests.test_input_sources.test_execute_command`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '-e', 'echo', 'hello world', '-o', '/tmp/tmpfim53y7q/output.png'], returncode=2, stdout=b'', stderr=b'error: no code snippet provided\n').returncod
- `tests.test_input_sources.test_execute_with_skip`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '-e', 'echo', 'test', '--skip', '-o', '/tmp/tmp5toc199a/output.png'], returncode=2, stdout=b'', stderr=b'error: no code snippet provided\n').return
- *(... 8 more in this cluster)*

### `rc_mismatch_got1_want0` — 11 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_additional_coverage.test_highlight_and_annotations_combined`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '-c', 'line 1\nline 2\nline 3\nline 4\nline 5\nline 6\nline 7\nline 8\nline 9', '-o', '/tmp/tmpc0plbw97/output.png', '--highlight-range', '2:4', '-
- `tests.test_comprehensive_coverage.test_combined_annotations`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '-c', 'line 1\nline 2\nline 3\nline 4\nline 5\nline 6\nline 7\nline 8\nline 9\nline 10\nline 11\nline 12\nline 13\nline 14\nline 15\nline 16\nline 
- `tests.test_highlighting_and_annotations.test_highlight_range`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '-c', 'line 1\nline 2\nline 3\nline 4\nline 5\nline 6\nline 7\nline 8\nline 9\nline 10', '-o', '/tmp/tmp1lxa9_re/output.png', '--highlight-range', 
- *(... 8 more in this cluster)*

### `missing_file` — 7 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_configuration.test_second_run_uses_existing_config`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_second_run_uses_existing_2/home/.config/codesnap/config.json'
- `tests.test_highlight_ranges.test_raw_highlight_lines_multiple_colors`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_raw_highlight_lines_multi2/test.svg'
- `tests.test_highlight_ranges.test_relative_highlight_range`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_relative_highlight_range2/test.svg'
- *(... 4 more in this cluster)*

### `returned_none` — 5 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_basic_invocation.test_version_flag`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7fb46bce7760>(b'codesnap[^\\n]*\\d+\\.\\d+', b'0.1.0\n', re.IGNORECASE)
  >  +    where <function search at 0x7fb46bce7760> = re.search
  >  +    and   b'0.1.0\n' = CompletedProcess(args=['./executable', '--version'], returncode=0, stdout=b'0.1.0\n', stderr=b'').stdout
  >  +    and   re.IGNORECASE = re.IGNORECASE
- `tests.test_basic_invocation.test_version_short_flag`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7fb46bce7760>(b'codesnap[^\\n]*\\d+\\.\\d+', b'0.1.0\n', re.IGNORECASE)
  >  +    where <function search at 0x7fb46bce7760> = re.search
  >  +    and   b'0.1.0\n' = CompletedProcess(args=['./executable', '-V'], returncode=0, stdout=b'0.1.0\n', stderr=b'').stdout
  >  +    and   re.IGNORECASE = re.IGNORECASE
- `eval.tests.test_help_behavior.test_help_has_help_and_version_flags`
  > assert None
  >  +  where None = <function search at 0x7f84d3442680>('\\n\\s*-h,\\s*--help\\b', "usage: codesnap [OPTIONS]\n\nRender code snippets as beautiful images\n\noptions:\n  --help, -h            Show this he
  >  +    where <function search at 0x7f84d3442680> = re.search
- *(... 2 more in this cluster)*

### `rc_mismatch_got0_want1` — 3 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_line_modifications.test_delete_line_beyond_file_length`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--from-file', '/workspace/eval/test_resources/test_line_modifications/simple_10_lines.txt', '--delete-line', '15', '--output', '/tmp/pyte
- `tests.test_line_modifications.test_delete_line_zero`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--from-file', '/workspace/eval/test_resources/test_line_modifications/simple_10_lines.txt', '--delete-line', '0', '--output', '/tmp/pytes
- `tests.test_line_modifications.test_delete_line_empty_string`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--from-file', '/workspace/eval/test_resources/test_line_modifications/simple_10_lines.txt', '--delete-line', '', '--output', '/tmp/pytest

### `rc_mismatch_got0_want101` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_line_modifications.test_invalid_delete_color_format_invalid_string`
  > AssertionError: assert 0 == 101
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--from-file', '/workspace/eval/test_resources/test_line_modifications/simple_10_lines.txt', '--delete-line', '3', '--delete-line-color', 
- `tests.test_line_modifications.test_invalid_delete_color_format_no_hash`
  > AssertionError: assert 0 == 101
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--from-file', '/workspace/eval/test_resources/test_line_modifications/simple_10_lines.txt', '--delete-line', '3', '--delete-line-color', 
- `tests.test_line_modifications.test_invalid_add_color_format_short_hex`
  > AssertionError: assert 0 == 101
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--from-file', '/workspace/eval/test_resources/test_line_modifications/simple_10_lines.txt', '--add-line', '3', '--add-line-color', '#f00'

