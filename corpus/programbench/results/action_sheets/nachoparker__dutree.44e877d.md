# Action Sheet — nachoparker__dutree.44e877d

**Current:** 45.25%  (433/957)
**Pass / Fail / Skip:** 433 / 484 / 10
**Gap to 100%:** 54.75 percentage points (524 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_dutree_executable.test_depth_variants[args1-None]`
  - reason: test_depth_variants[args1-None] depends on test_ascii_full_tree_matches_golden_exact
- `eval.tests.test_dutree_executable.test_no_hidden_excludes_hidden_entries`
  - reason: test_no_hidden_excludes_hidden_entries depends on test_ascii_full_tree_matches_golden_exact
- `eval.tests.test_dutree_executable.test_exclude_removes_matching_entries`
  - reason: test_exclude_removes_matching_entries depends on test_ascii_full_tree_matches_golden_exact
- `eval.tests.test_dutree_executable.test_depth_variants[args0-golden_ascii_d1.txt]`
  - reason: test_depth_variants[args0-golden_ascii_d1.txt] depends on test_ascii_full_tree_matches_golden_exact
- `eval.tests.test_dutree_executable.test_files_only_excludes_directories`
  - reason: test_files_only_excludes_directories depends on test_ascii_full_tree_matches_golden_exact
- *(... 5 more skipped)*

## Failure clusters

484 failed tests grouped into 10 buckets (sorted by count).

### `string_output_mismatch` — 344 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_colors.test_ls_colors_not_set`
  > AssertionError: assert '[ testdir 0 ...        0 B\n' == '[ testdir 17...        0 B\n'
  >   
  >   - [ testdir 175 B ]
  >   ?           ^^^
  >   + [ testdir 0 B ]
  >   ?           ^
  >   + |- executable.sh                        [                              ]    0%           0 B
  >   + |- file.mp3                             [                              ]    0%           0 B...
- `tests.test_colors.test_ls_colors_unicode_in_values`
  > AssertionError: assert '[ testdir 0 ...        0 B\n' == '[ testdir 17...        0 B\n'
  >   
  >   - [ testdir 175 B ]
  >   ?           ^^^
  >   + [ testdir 0 B ]
  >   ?           ^
  >   + |- executable.sh                        [                              ]    0%           0 B
  >   + |- file.mp3                             [                              ]    0%           0 B...
- `tests.test_core.test_depth_limit_deep`
  > AssertionError: assert '[ dir1 0 B ]...        0 B\n' == '[ dir1 2.94 ...      256 B\n'
  >   
  >   - [ dir1 2.94 KiB ]
  >   - ├─ test3                  │ ################################│  54%      1.61 KiB
  >   - │  ├─ test2               │ ################################│  82%      1.33 KiB
  >   - │  │  ├─ test2            │ ################################│  40%         544 B
  >   - │  │  │  ├─ file1         │ ################################│  47%         256 B
  >   - │  │  │  └─ file2         │ ################################│  47%         256 B...
- *(... 341 more in this cluster)*

### `other_assertion` — 102 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_aggregation.test_aggregation_bytes`
  > AssertionError: assert 13 > 50
  >  +  where 13 = len(b'[ test 0 B ]\n')
  >  +    where b'[ test 0 B ]\n' = CompletedProcess(args=['/workspace/executable', '-a', '100B', '/workspace/test'], returncode=0, stdout=b'[ test 0 B ]\n', stderr=b'').stdout
- `tests.test_coverage_boost.test_very_large_files_tib_range`
  > AssertionError: assert (b'MiB' in b'[ tmpykhl5dlc 0 B ]\n\xe2\x94\x9c\xe2\x94\x80 file0.dat                            \xe2\x94\x82                              \xe2\x94\x82    0%           0 B\n\xe2\
  >  +  where b'[ tmpykhl5dlc 0 B ]\n\xe2\x94\x9c\xe2\x94\x80 file0.dat                            \xe2\x94\x82                              \xe2\x94\x82    0%           0 B\n\xe2\x94\x9c\xe2\x94\x80 file
  >  +  and   b'[ tmpykhl5dlc 0 B ]\n\xe2\x94\x9c\xe2\x94\x80 file0.dat                            \xe2\x94\x82                              \xe2\x94\x82    0%           0 B\n\xe2\x94\x9c\xe2\x94\x80 file
  >  +  and   b'[ tmpykhl5dlc 0 B ]\n\xe2\x94\x9c\xe2\x94\x80 file0.dat                            \xe2\x94\x82                              \xe2\x94\x82    0%           0 B\n\xe2\x94\x9c\xe2\x94\x80 file
- `tests.test_aggregation.test_aggregation_various_sizes`
  > AssertionError: assert (b'large.txt' in b'[ tmp1tg85g4q 0 B ]\n' or b'<aggregated>' in b'[ tmp1tg85g4q 0 B ]\n')
  >  +  where b'[ tmp1tg85g4q 0 B ]\n' = CompletedProcess(args=['/workspace/executable', '-a', '100K', '/tmp/tmp1tg85g4q'], returncode=0, stdout=b'[ tmp1tg85g4q 0 B ]\n', stderr=b'').stdout
  >  +  and   b'[ tmp1tg85g4q 0 B ]\n' = CompletedProcess(args=['/workspace/executable', '-a', '100K', '/tmp/tmp1tg85g4q'], returncode=0, stdout=b'[ tmp1tg85g4q 0 B ]\n', stderr=b'').stdout
- *(... 99 more in this cluster)*

### `bytes_output_mismatch` — 17 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_edge_cases.test_aggregation_large_threshold_all_aggregated`
  > AssertionError: assert '[ test 0 B ]' == '[ test 16.53...    12.53 KiB'
  >   
  >   + [ test 0 B ]
  >   - [ test 16.53 KiB ]
  >   - └─ <aggregated>           │ ████████████████████████████████│  75%     12.53 KiB
- `tests.test_edge_cases.test_files_only_flag`
  > AssertionError: assert '[ dir1 0 B ]...          0 B' == '[ dir1 570 B...        256 B'
  >   
  >   - [ dir1 570 B ]
  >   ?        --
  >   + [ dir1 0 B ]
  >   - ├─ file1                  │ ████████████████████████████████│  44%         256 B
  >   - └─ file2                  │ ████████████████████████████████│  44%         256 B
  >   + ├─ file1                                │                              │    0%           0 B
- `tests.test_edge_cases.test_combined_ascii_no_hidden`
  > AssertionError: assert '[ test 0 B ]...          0 B' == '[ test 16.53...        256 B'
  >   
  >   - [ test 16.53 KiB ]
  >   - ├─ file_sparse            │ ################################│  48%      8.00 KiB
  >   - ├─ dir1                   │                      ###########│  17%      2.94 KiB
  >   - │  ├─ test3               │                      ###########│  54%      1.61 KiB
  >   - │  │  ├─ test2            │                      ###########│  82%      1.33 KiB
  >   - │  │  │  ├─ test2         │                      ###########│  40%         544 B...
- *(... 14 more in this cluster)*

### `rc_mismatch_got1_want0` — 7 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_core.test_invalid_depth_defaults_to_one`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '/workspace/test', '-d', 'notanumber', '--ascii'], returncode=1, stdout='[ test 0 B ]\n|- .file_hidden                         [          
- `tests.test_formatting.test_empty_directory_formatting`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-A', '/workspace/eval/test_resources/test_formatting/empty_dir'], returncode=1, stdout='', stderr="dutree: '/workspace/eval/test_resource
- `tests.test_formatting.test_directory_only_tree`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-A', '/workspace/eval/test_resources/test_formatting/only_dirs'], returncode=1, stdout='', stderr="dutree: '/workspace/eval/test_resource
- *(... 4 more in this cluster)*

### `subprocess_failed` — 4 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_depth.test_depth_invalid_non_numeric_defaults_to_one`
  > subprocess.CalledProcessError: Command '['/workspace/executable', '-A', '-dabc', '/workspace/test/dir1']' returned non-zero exit status 1.
- `tests.test_depth.test_depth_negative_value_defaults_to_one`
  > subprocess.CalledProcessError: Command '['/workspace/executable', '-A', '-d-5', '/workspace/test/dir1']' returned non-zero exit status 1.
- `tests.test_sizes.test_aggr_default_1m`
  > subprocess.CalledProcessError: Command '['/workspace/executable', '-A', '-a', '--', '/workspace/test']' returned non-zero exit status 1.
- *(... 1 more in this cluster)*

### `rc_mismatch_got0_want1` — 4 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_depth.test_both_depth_flags_given_errors`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-A', '-d1', '--depth=2', '/workspace/test/dir1'], returncode=0, stdout='[ dir1 0 B ]\n|- file1                                [          
- `tests.test_errors.test_duplicate_depth_flag_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-d1', '-d2', '/workspace/test'], returncode=0, stdout='[ test 0 B ]\n├─ .file_hidden                         │                           
- `tests.test_errors.test_multiple_aggregation_flags_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-a1K', '-a2M', '/workspace/test'], returncode=0, stdout='[ test 0 B ]\n', stderr='').returncode
- *(... 1 more in this cluster)*

### `rc_unexpected_zero` — 3 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_colors.test_ls_colors_malformed_no_equals`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-A', '/workspace/eval/test_resources/test_colors/testdir'], returncode=0, stdout='[ testdir 0 B ]\n|- executable.sh                      
- `eval.tests.test_env_config.test_malformed_ls_colors_can_crash_original_binary_documented_behavior`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '.'], returncode=0, stdout=b'[ workspace 0 B ]\n\xe2\x94\x9c\xe2\x94\x80 .git                                 \xe2\x94\x82                
- `eval.tests.test_help_behavior.test_help_takes_precedence_over_unknown_option`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--help', '--nope'], returncode=0, stdout='Usage: /workspace/main.py [options] <path> [<path>..]\n\nOptions:\n    -d, --depth [DEPTH] show

### `rc_mismatch_got3_want4` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_core.test_default_current_directory`
  > AssertionError: assert 3 == 4
  >  +  where 3 = len(['[ test_default_mujlpwqt 0 B ]', '|- file1.txt                            [                              ]    0%           0 B', '`- subdir                               [          

### `uncategorized` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_core.test_size_sorting_descending`
  > StopIteration

### `boolean_false` — 1 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_errors.test_invalid_flag_error_message`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x73df39508030>('Usage:')
  >  +    where <built-in method startswith of str object at 0x73df39508030> = ''.startswith
  >  +      where '' = CompletedProcess(args=['/workspace/executable', '--invalid-flag'], returncode=1, stdout='', stderr='Unrecognized option: --invalid-flag\n').stdout

