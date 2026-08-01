# Action Sheet — lh3__seqtk.94e7070

**Current:** 10.33%  (62/600)
**Pass / Fail / Skip:** 62 / 378 / 0
**Gap to 100%:** 89.67 percentage points (538 tests)

## Failure clusters

378 failed tests grouped into 15 buckets (sorted by count).

### `string_output_mismatch` — 155 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_analysis.test_listhet_basic`
  > AssertionError: assert 'scaffold1\t8...iple\t9\t27\n' == 'seq1\t5\tW\n...seq3\t12\tM\n'
  >   
  >   + scaffold1	8	18
  >   + scaffold3_multiple	9	27
  >   - seq1	5	W
  >   - seq1	6	S
  >   - seq1	7	M
  >   - seq1	8	K...
- `tests.test_analysis.test_gap_basic`
  > AssertionError: assert 'chr2_low_gc\t0\t38\t38\n' == 'scaffold1\t8...iple\t9\t27\n'
  >   
  >   + chr2_low_gc	0	38	38
  >   - scaffold1	8	18
  >   - scaffold3_multiple	9	27
- `tests.test_analysis.test_gc_basic`
  > AssertionError: assert 'chr2_low_gc\t0\t38\t38\n' == 'chr1_mixed_g...\t5\t61\t54\n'
  >   
  >   + chr2_low_gc	0	38	38
  >   - chr1_mixed_gc	8	48	40
  >   - chr3_high_gc_cluster	5	61	54
- *(... 152 more in this cluster)*

### `other_assertion` — 117 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic.TestBasicInvocation.test_no_args_lists_commands`
  > AssertionError: assert b'seq' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable'], returncode=0, stdout=b'>end_n:1-8\n>exact:1-8\n>exact:19-26\n>mid_n:1-4\n>mid_n:17-20\n>normal_seq\n>one_less:1-25\n>renamed1\\n\n>seq_
- `tests.test_basic.TestBasicInvocation.test_version_in_usage`
  > AssertionError: assert (b'1.5' in b'' or b'1.4' in b'')
  >  +  where b'' = CompletedProcess(args=['/workspace/executable'], returncode=0, stdout=b'>end_n:1-8\n>exact:1-8\n>exact:19-26\n>mid_n:1-4\n>mid_n:17-20\n>normal_seq\n>one_less:1-25\n>renamed1\\n\n>seq_
  >  +  and   b'' = CompletedProcess(args=['/workspace/executable'], returncode=0, stdout=b'>end_n:1-8\n>exact:1-8\n>exact:19-26\n>mid_n:1-4\n>mid_n:17-20\n>normal_seq\n>one_less:1-25\n>renamed1\\n\n>seq_
- `tests.test_basic.TestBasicInvocation.test_unrecognized_command`
  > AssertionError: assert b'unrecognized command' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', 'unknowncmd'], returncode=1, stdout=b'>seq1\nACGTACGTACGT\n>seq2\n@read1\nACGTACGTACGT\n>read1\nACGTACGTACGT\n>read1\n>seq1\n', stderr=b
- *(... 114 more in this cluster)*

### `bytes_output_mismatch` — 53 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_basic.TestSizeCommand.test_size_basic`
  > AssertionError: assert b'0' == b'2'
  >   
  >   At index 0 diff: b'0' != b'2'
  >   
  >   Full diff:
  >   - b'2'
  >   ?   ^
  >   + b'0'
- `tests.test_basic.TestSizeCommand.test_size_fastq`
  > AssertionError: assert b'0' == b'2'
  >   
  >   At index 0 diff: b'0' != b'2'
  >   
  >   Full diff:
  >   - b'2'
  >   ?   ^
  >   + b'0'
- `tests.test_comp.TestCompCommand.test_comp_base_counts`
  > AssertionError: assert b'10' == b'16'
  >   
  >   At index 1 diff: b'0' != b'6'
  >   
  >   Full diff:
  >   - b'16'
  >   ?    ^
  >   + b'10'
- *(... 50 more in this cluster)*

### `rc_mismatch_got0_want1` — 23 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_basic.TestBasicInvocation.test_no_args_shows_usage`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable'], returncode=0, stdout=b'>end_n:1-8\n>exact:1-8\n>exact:19-26\n>mid_n:1-4\n>mid_n:17-20\n>normal_seq\n>one_less:1-25\n>renamed1\\n\n>seq_ve
- `tests.test_genomics.TestHetyCommand.test_hety_no_args_shows_usage`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'hety'], returncode=0, stdout=b'chr1\nchr1\nchr1\n', stderr=b'').returncode
- `tests.test_genomics.TestGcCommand.test_gc_no_args_shows_usage`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'gc'], returncode=0, stdout=b'chr2_low_gc\t0\t38\t38\n', stderr=b'').returncode
- *(... 20 more in this cluster)*

### `empty_list_or_string` — 8 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_basic.TestSeqCommand.test_seq_reverse_complement_acga`
  > IndexError: list index out of range
- `tests.test_basic.TestSeqAdvancedOptions.test_seq_reverse_complement_fastq`
  > IndexError: list index out of range
- `tests.test_merge_split.TestSplitCommand.test_split_line_length`
  > IndexError: list index out of range
- *(... 5 more in this cluster)*

### `boolean_false` — 5 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_basic.TestSeqCommand.test_seq_mask_bed_regions`
  > assert False
  >  +  where False = any(<generator object TestSeqCommand.test_seq_mask_bed_regions.<locals>.<genexpr> at 0x7fefbe18a3b0>)
- `tests.test_basic.TestSeqAdvancedOptions.test_seq_complement_mask`
  > assert False
  >  +  where False = any(<generator object TestSeqAdvancedOptions.test_seq_complement_mask.<locals>.<genexpr> at 0x7fefbe1e9cb0>)
- `tests.test_trimfq.TestTrimfqCommand.test_trimfq_preserves_fastq_format`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of bytes object at 0x7fefc00a8030>(b'@')
  >  +    where <built-in method startswith of bytes object at 0x7fefc00a8030> = b''.startswith
- *(... 2 more in this cluster)*

### `rc_mismatch_got1_want2` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_comp.TestCompCommand.test_comp_multiple_seqs`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len([b'seq1\t10\t10\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0'])
- `tests.test_telo.TestTeloCommand.test_telo_stderr_counts`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len([b''])
- `tests.test_undocumented.test_kfreq_empty_sequence`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len([''])

### `rc_mismatch_got0_want2` — 2 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_basic.TestSeqCommand.test_seq_reverse_both_strands`
  > assert 0 == 2
  >  +  where 0 = len([])
- `tests.test_merge_split.TestSplitCommand.test_split_basic`
  > assert 0 == 2
  >  +  where 0 = len([])

### `rc_mismatch_got0_want10` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_merge_split.TestSplitCommand.test_split_default_n`
  > assert 0 == 10
  >  +  where 0 = len([])
- `tests.test_sample_subseq.TestSampleCommand.test_sample_reproducible_with_seed`
  > AssertionError: assert 0 == 10
  >  +  where 0 = <built-in method count of bytes object at 0x7fefc00a8030>(b'@read')
  >  +    where <built-in method count of bytes object at 0x7fefc00a8030> = b''.count
  >  +      where b'' = CompletedProcess(args=['/workspace/executable', 'sample', '-s', '100', '/tmp/tmphtgf48mf/in.fq', '10'], returncode=0, stdout=b'', stderr=b'').stdout

### `rc_mismatch_got0_want5` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_sample_subseq.TestSampleCommand.test_sample_by_number`
  > assert 0 == 5
- `tests.test_sample_subseq.TestSampleCommand.test_sample_twopass_mode`
  > assert 0 == 5

### `rc_unexpected_zero` — 2 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_undocumented.test_hrun_missing_file`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'hrun', 'nonexistent.fa'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_undocumented.test_kfreq_missing_file`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'kfreq', 'A', 'nonexistent.fa'], returncode=0, stdout=b'', stderr=b'').returncode

### `rc_mismatch_got1_want4` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_undocumented.test_hrun_tab_and_whitespace_in_sequence_name`
  > AssertionError: assert 1 == 4
  >  +  where 1 = len([''])
- `tests.test_utilities.test_randbase_stdin`
  > AssertionError: assert 1 == 4
  >  +  where 1 = len([''])

### `uncategorized` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_utilities.test_hpc_preserves_non_homopolymers`
  > ValueError: '>test_no_poly' is not in list
- `tests.test_utilities.test_randbase_all_two_base_codes`
  > ValueError: '>all_two_base_codes' is not in list

### `rc_mismatch_got4_want16` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_trimfq.TestMergepeCommand.test_mergepe_basic`
  > AssertionError: assert 4 == 16
  >  +  where 4 = len([b'@read1', b'TACGTACGTA', b'+', b'IIIIIIIIII'])

### `rc_mismatch_got10_want1` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_undocumented.test_kfreq_very_long_kmer`
  > AssertionError: assert 10 == 1
  >  +  where 10 = len(['seq1_short\t0\t27\t13.64\t22\t6', 'seq2_longer\t0\t50\t0.00\t50\t0', 'seq2_longer\t50\t60\t0.00\t50\t0', 'seq2_longer\t60\t70\t0.00\t50\t0', 'seq2_longer\t70\t80\t0.00\t50\t0', 's

