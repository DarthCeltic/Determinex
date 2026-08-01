# Action Sheet — osgeo__proj.75d455c

**Current:** 0.05%  (3/5793)
**Pass / Fail / Skip:** 3 / 590 / 107
**Gap to 100%:** 99.95 percentage points (5790 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_harvest.test_gie_case[4D-API_cs2cs-style:L51:4D-API_cs2cs-style_1]`
  - reason: proj command-line tool cannot handle this operation type
- `tests.test_harvest.test_gie_case[4D-API_cs2cs-style:L63:4D-API_cs2cs-style_2]`
  - reason: proj command-line tool cannot handle this operation type
- `tests.test_harvest.test_gie_case[4D-API_cs2cs-style:L66:4D-API_cs2cs-style_3]`
  - reason: proj command-line tool cannot handle this operation type
- `tests.test_harvest.test_gie_case[4D-API_cs2cs-style:L77:4D-API_cs2cs-style_4]`
  - reason: proj command-line tool cannot handle this operation type
- `tests.test_harvest.test_gie_case[4D-API_cs2cs-style:L82:4D-API_cs2cs-style_5]`
  - reason: proj command-line tool cannot handle this operation type
- *(... 102 more skipped)*

## Failure clusters

590 failed tests grouped into 9 buckets (sorted by count).

### `missing_file` — 350 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_proj.TestBasicInvocation.test_no_args_prints_usage`
  > FileNotFoundError: [Errno 2] No such file or directory: './build_cov/bin/proj'
- `tests.test_proj.TestBasicInvocation.test_no_args_version_in_stderr`
  > FileNotFoundError: [Errno 2] No such file or directory: './build_cov/bin/proj'
- `tests.test_proj.TestBasicInvocation.test_usage_format`
  > FileNotFoundError: [Errno 2] No such file or directory: './build_cov/bin/proj'
- *(... 347 more in this cluster)*

### `other_assertion` — 117 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic.test_proj_runs_with_help`
  > AssertionError: Expected usage message in output
  > assert 'usage:' in '#\n# another tag line\n# comment 1\n# comment 2\n# comment 3\n# final comment\n# this is a comment/tag line\n#final earth figure: ellipsoid\n#final earth figure: sphere\n#mercator\
  >  +  where '#\n# another tag line\n# comment 1\n# comment 2\n# comment 3\n# final comment\n# this is a comment/tag line\n#final earth figure: ellipsoid\n#final earth figure: sphere\n#mercator\n%comment
  >  +    where <built-in method lower of str object at 0x555f933b7ef0> = '#\n# Another tag line\n# Comment 1\n# Comment 2\n# Comment 3\n# Final comment\n# This is a comment/tag line\n#Final Earth figure:
- `tests.test_basic.test_simple_mercator_projection`
  > AssertionError: Expected 2 coordinates, got: some_label
  >   W
  >   N
  > assert 3 == 2
  >  +  where 3 = len(['some_label', 'W', 'N'])
- `tests.test_basic.test_mercator_projection_with_coordinates`
  > AssertionError: Expected 2 coordinates, got: some_label
  >   W
  >   N
  > assert 3 == 2
  >  +  where 3 = len(['some_label', 'W', 'N'])
- *(... 114 more in this cluster)*

### `string_output_mismatch` — 59 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_crs_input.test_epsg_projected_crs_forward`
  > AssertionError: assert '#\n# Another...roj.db\nConic' == '175775.36\t86923.19'
  >   
  >   - 175775.36	86923.19
  >   + #
  >   + # Another tag line
  >   + # Comment 1
  >   + # Comment 2
  >   + # Comment 3...
- `tests.test_crs_input.test_epsg_projected_crs_inverse`
  > assert 'W\nN\nd' == '0d5\'14.159"E\t0d47\'7.433"N'
  >   
  >   - 0d5'14.159"E	0d47'7.433"N
  >   + W
  >   + N
  >   + d
- `tests.test_crs_input.test_epsg_different_zone`
  > AssertionError: assert '#\n# Another...roj.db\nConic' == '-1158383.26\t79808.12'
  >   
  >   - -1158383.26	79808.12
  >   + #
  >   + # Another tag line
  >   + # Comment 1
  >   + # Comment 2
  >   + # Comment 3...
- *(... 56 more in this cluster)*

### `uncategorized` — 57 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_errors.test_scale_factor_application`
  > ValueError: could not convert string to float: 'some_label\nW\nN'
- `tests.test_errors.test_inverse_scale_factor_1_over_n`
  > ValueError: could not convert string to float: 'some_label\nW\nN'
- `tests.test_errors.test_stdin_explicit_dash`
  > ValueError: could not convert string to float: '708216.87\n# comment line\n708216.87\n% comment\n708216.87\n708216.87\n<\n>'
- *(... 54 more in this cluster)*

### `rc_mismatch_got1_want2` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_errors.test_reverse_output_order`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len(['some_label\nW\nN'])
- `tests.test_errors.test_combined_reversal_flags`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len(['0 51.5\n708216.87\n#\n<\n# a comment\n708216.87\n774548.26'])

### `rc_mismatch_got2_want0` — 2 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_errors.test_lowercase_width_precision_flag`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-I', '-w3', '+proj=merc'], returncode=2, stdout=b"error: unexpected argument '-I' found\nError: unexpected argument '-I' found\nunknown f
- `tests.test_errors.test_list_units`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-lu'], returncode=2, stdout=b"error: unexpected argument '-lu' found\nError: unexpected argument '-lu' found\nunknown flag: unexpected ar

### `rc_mismatch_got0_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_errors.test_errors_go_to_stderr_not_stdout`
  > AssertionError: assert 0 == 3
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '+proj=nonexistent'], returncode=0, stdout=b'#\n# Another tag line\n# Comment 1\n# Comment 2\n# Comment 3\n# Final comment\n# This is a co

### `rc_mismatch_got5_want1` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_errors.test_format_string_application`
  > AssertionError: assert 5 == 1
  >  +  where 5 = <built-in method count of str object at 0x7f1ad3f0c830>('.')
  >  +    where <built-in method count of str object at 0x7f1ad3f0c830> = '708216.872176\n5709696.983573\n708216.8722\n5709696.9836\nd\n0d00\n708216.87'.count

### `bytes_output_mismatch` — 1 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_file_input.test_trailing_whitespace_preserved`
  > AssertionError: assert b'some_label\nW\nN\n' == b'1113194.91\...8471.40\t\t\n'
  >   
  >   At index 0 diff: b's' != b'1'
  >   
  >   Full diff:
  >   - (b'1113194.91\t2258423.65   \n3339584.72\t4838471.40\t\t\n')
  >   + (b'some_label\nW\nN\n')

