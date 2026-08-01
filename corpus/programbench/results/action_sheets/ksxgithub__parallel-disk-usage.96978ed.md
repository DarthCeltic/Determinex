# Action Sheet — ksxgithub__parallel-disk-usage.96978ed

**Current:** 19.36%  (152/785)
**Pass / Fail / Skip:** 152 / 477 / 1
**Gap to 100%:** 80.64 percentage points (633 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_pdu_cli.test_version_format`
  - reason: test_version_format depends on test_help_exact

## Failure clusters

477 failed tests grouped into 16 buckets (sorted by count).

### `other_assertion` — 218 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_help_flag`
  > AssertionError: assert b'Summarize disk usage' in b'Usage:\nArguments:\n--version\n--json-input\n--json-output\n--bytes-format\nExamples:\nUsage:\n--help\nfile1.txt\n'
  >  +  where b'Usage:\nArguments:\n--version\n--json-input\n--json-output\n--bytes-format\nExamples:\nUsage:\n--help\nfile1.txt\n' = CompletedProcess(args=['./executable', '--help'], returncode=0, stdout
- `tests.test_basic_invocation.test_help_short_flag`
  > AssertionError: assert b'Summarize disk usage' in b'Usage:\n--help\nfile1.txt\n'
  >  +  where b'Usage:\n--help\nfile1.txt\n' = CompletedProcess(args=['./executable', '-h'], returncode=0, stdout=b'Usage:\n--help\nfile1.txt\n', stderr=b'').stdout
- `tests.test_basic_invocation.test_no_arguments_current_dir`
  > assert (b'\xe2\x94\x82' in b'{\n  "all_links": "",\n  "children": "",\n  "details": "",\n  "detected_links": "",\n  "exclusive_inodes": "",\n  "exclusive_links": "",\n  "exclusive_shared_size": "",\n 
  >  +  where b'{\n  "all_links": "",\n  "children": "",\n  "details": "",\n  "detected_links": "",\n  "exclusive_inodes": "",\n  "exclusive_links": "",\n  "exclusive_shared_size": "",\n  "ino": "",\n  "i
  >  +  and   b'{\n  "all_links": "",\n  "children": "",\n  "details": "",\n  "detected_links": "",\n  "exclusive_inodes": "",\n  "exclusive_links": "",\n  "exclusive_shared_size": "",\n  "ino": "",\n  "i
- *(... 215 more in this cluster)*

### `json_output_missing_or_bad` — 126 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `tests.test_output_modes.test_json_output_flag`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_output_modes.test_json_output_structure`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_output_modes.test_json_min_ratio_zero`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- *(... 123 more in this cluster)*

### `string_output_mismatch` — 45 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_pdu_cli.test_help_exact`
  > AssertionError: assert 'Usage:\nArgu...\nfile1.txt\n' == 'Summarize di...-usage.json\n'
  >   
  >   + Usage:
  >   - Summarize disk usage of the set of files, recursively for directories.
  >   - 
  >   - Copyright: Apache-2.0 © 2021 Hoàng Văn Khải <https://github.com/KSXGitHub/>
  >   - Sponsor: https://github.com/sponsors/KSXGitHub
  >   - ...
- `eval.tests.test_pdu_cli.test_invalid_flag_errors_and_exit_code`
  > AssertionError: assert 'error: unexp...nformation.\n' == ''
  >   
  >   + error: unexpected argument '--definitely-not-a-flag' found
  >   + Error: unexpected argument '--definitely-not-a-flag' found
  >   + unknown flag: unexpected argument '--definitely-not-a-flag' found
  >   + Unknown flag: unexpected argument '--definitely-not-a-flag' found
  >   + Usage: parallel-disk-usage [OPTIONS] [ARGS]...
  >   + USAGE: parallel-disk-usage [OPTIONS] [ARGS]......
- `tests.test_errors.test_invalid_quantity_value`
  > assert '' == "error: inval...try '--help'."
  >   
  >   - error: invalid value 'invalid' for '--quantity <QUANTITY>'
  >   -   [possible values: apparent-size, block-size, block-count]
  >   - 
  >   - For more information, try '--help'.
- *(... 42 more in this cluster)*

### `rc_unexpected_zero` — 31 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_edge_cases.test_min_ratio_greater_than_one`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '--min-ratio=1.5', '/tmp/tmpioxp0nhb'], returncode=0, stdout=b'file\nfile.txt\nfile.txt\n', stderr=b'').returncode
- `tests.test_performance_options.test_threads_invalid`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '--threads=invalid', '.'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_performance_options.test_threads_zero`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '--threads=0', '.'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 28 more in this cluster)*

### `returned_none` — 19 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_basic_invocation.test_version_flag`
  > AssertionError: assert None
  >  +  where None = <function match at 0x7f8dc5131120>(b'pdu \\d+\\.\\d+\\.\\d+', b'pdu\npdu\nUsage:\nArguments:\n--version\n--json-input\n--json-output\n--bytes-format\nExamples:\nUsage:\n')
  >  +    where <function match at 0x7f8dc5131120> = re.match
  >  +    and   b'pdu\npdu\nUsage:\nArguments:\n--version\n--json-input\n--json-output\n--bytes-format\nExamples:\nUsage:\n' = CompletedProcess(args=['./executable', '--version'], returncode=0, stdout=b'p
- `tests.test_basic_invocation.test_version_short_flag`
  > AssertionError: assert None
  >  +  where None = <function match at 0x7f8dc5131120>(b'pdu \\d+\\.\\d+\\.\\d+', b'pdu\nUsage:\nArguments:\n--version\n--json-input\n--json-output\n--bytes-format\nExamples:\nUsage:\n--help\n')
  >  +    where <function match at 0x7f8dc5131120> = re.match
  >  +    and   b'pdu\nUsage:\nArguments:\n--version\n--json-input\n--json-output\n--bytes-format\nExamples:\nUsage:\n--help\n' = CompletedProcess(args=['./executable', '-V'], returncode=0, stdout=b'pdu\n
- `tests.test_edge_cases.test_max_depth_one`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f8dc5133760>(b'\\d+', b'tmp\n')
  >  +    where <function search at 0x7f8dc5133760> = re.search
  >  +    and   b'tmp\n' = CompletedProcess(args=['./executable', '--max-depth=1', '/tmp/tmpw2fdu_66'], returncode=0, stdout=b'tmp\n', stderr=b'').stdout
- *(... 16 more in this cluster)*

### `rc_mismatch_got0_want2` — 14 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `eval.tests.test_argparse_validation.test_argument_errors[args0-2-expected_substrs0]`
  > assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--no-such-flag'], returncode=0, stdout=b'{\n  "all_links": "",\n  "children": "",\n  "details": "",\n  "detected_links": "",\n  "exclusiv
- `eval.tests.test_argparse_validation.test_argument_errors[args6-2-expected_substrs6]`
  > assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--json-output', '--max-depth=0'], returncode=0, stdout=b'{\n  "all_links": "",\n  "children": "",\n  "details": "",\n  "detected_links": 
- `eval.tests.test_argparse_validation.test_argument_errors[args7-2-expected_substrs7]`
  > assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--json-output', '--max-depth=-1'], returncode=0, stdout=b'{\n  "all_links": "",\n  "children": "",\n  "details": "",\n  "detected_links":
- *(... 11 more in this cluster)*

### `rc_mismatch_got4_want2` — 6 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_argparse_validation.test_argument_errors[args2-2-expected_substrs2]`
  > AssertionError: assert 4 == 2
  >  +  where 4 = CompletedProcess(args=['/workspace/executable', '--json-output', '--bytes-format', 'banana', '--max-depth=1', '.'], returncode=4, stdout=b'', stderr=b'').returncode
- `eval.tests.test_argparse_validation.test_argument_errors[args3-2-expected_substrs3]`
  > AssertionError: assert 4 == 2
  >  +  where 4 = CompletedProcess(args=['/workspace/executable', '--json-output', '--quantity=banana', '--max-depth=1', '.'], returncode=4, stdout=b'', stderr=b'').returncode
- `eval.tests.test_argparse_validation.test_argument_errors[args4-2-expected_substrs4]`
  > AssertionError: assert 4 == 2
  >  +  where 4 = CompletedProcess(args=['/workspace/executable', '--json-output', '--threads=banana', '--max-depth=1', '.'], returncode=4, stdout=b'', stderr=b'').returncode
- *(... 3 more in this cluster)*

### `boolean_false` — 5 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_progress_reporting.test_progress_with_deduplicate_hardlinks`
  > assert False
  >  +  where False = any(<generator object test_progress_with_deduplicate_hardlinks.<locals>.<genexpr> at 0x7f358351c900>)
- `tests.test_quantity.test_quantity_apparent_size`
  > assert False
  >  +  where False = any(<generator object test_quantity_apparent_size.<locals>.<genexpr> at 0x7f358355c9e0>)
- `eval.tests.test_help_and_version.test_version_format`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7fcb48ec63a0>('pdu ')
  >  +    where <built-in method startswith of str object at 0x7fcb48ec63a0> = 'pdu\npdu\nUsage:\nArguments:\n--version\n--json-input\n--json-output\n--bytes-format\nExamples:\nUsage:'.startswith
- *(... 2 more in this cluster)*

### `rc_mismatch_got0_want3` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_argparse_validation.test_json_input_requires_valid_json_on_stdin`
  > AssertionError: assert 0 == 3
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--json-input'], returncode=0, stdout=b'file1.txt\n', stderr=b'').returncode
- `tests.test_errors.test_invalid_json_input`
  > AssertionError: assert 0 == 3
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--json-input'], returncode=0, stdout='file1.txt\n', stderr='').returncode
- `tests.test_errors.test_empty_json_object`
  > AssertionError: assert 0 == 3
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--json-input'], returncode=0, stdout='file1.txt\n', stderr='').returncode

### `type_error` — 3 test(s)

**Quick patch ideas:**
- Specific TypeError; check arg types vs expected

**Sample failures:**

- `tests.test_json_modes.test_json_output_with_max_depth_2`
  > TypeError: string indices must be integers
- `tests.test_json_modes.test_json_output_with_min_ratio_filtering`
  > TypeError: string indices must be integers
- `tests.test_scale.test_combine_multiple_options`
  > TypeError: string indices must be integers

### `rc_mismatch_got0_want5` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_gap_fill.test_json_input_child_larger_than_parent_error`
  > AssertionError: assert 0 == 5
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--json-input'], returncode=0, stdout='file1.txt\n', stderr='').returncode
- `tests.test_gap_fill.test_json_input_nested_child_larger_than_parent_error`
  > AssertionError: assert 0 == 5
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--json-input'], returncode=0, stdout='file1.txt\n', stderr='').returncode

### `bytes_output_mismatch` — 1 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_sorting_and_errors.test_empty_json_input`
  > AssertionError: assert (0 != 0 or b'file1.txt\n' == b''
  >  +  where 0 = CompletedProcess(args=['./executable', '--json-input'], returncode=0, stdout=b'file1.txt\n', stderr=b'').returncode
  >   
  >   Full diff:
  >   - b''
  >   + (b'file1.txt\n'))

### `empty_list_or_string` — 1 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_flag_interactions.test_bytes_format_binary_vs_metric`
  > IndexError: list index out of range

### `rc_mismatch_got4_want0` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_json_modes.test_json_output_with_max_depth_1`
  > AssertionError: assert 4 == 0
  >  +  where 4 = CompletedProcess(args=['/workspace/executable', '/workspace/eval/test_resources/test_json_modes/test_tree1', '--json-output', '--max-depth=1'], returncode=4, stdout='', stderr='').return

### `uncategorized` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_size_edge_cases.test_mixed_quantities_same_directory`
  > StopIteration

### `rc_mismatch_got0_want1` — 1 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_unreachable_constructors.test_files_are_represented_as_empty_directories`
  > assert 0 == 1
  >  +  where 0 = len([])

