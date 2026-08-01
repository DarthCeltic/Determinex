# Action Sheet — arq5x__bedtools2.dd57059

**Current:** 0.66%  (7/1060)
**Pass / Fail / Skip:** 7 / 342 / 1
**Gap to 100%:** 99.34 percentage points (1053 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_harvest_bam_bed_conversions.test_bigchroms_t03_getfasta_big_chromosome`
  - reason: Test requires BT_NO_BIG_FILES env var and creates large files (bigx.fasta) - conditional test in original suite

## Failure clusters

342 failed tests grouped into 7 buckets (sorted by count).

### `string_output_mismatch` — 223 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_annotate.test_annotate_single_file_fraction_coverage`
  > AssertionError: assert '' == 'chr1\t100\t2...-\t0.500000\n'
  >   
  >   - chr1	100	200	interval1	10	+	0.400000
  >   - chr1	300	500	interval2	20	-	0.400000
  >   - chr2	50	150	interval3	30	+	0.200000
  >   - chr2	400	600	interval4	40	-	0.500000
- `tests.test_annotate.test_annotate_multiple_files_fraction_coverage`
  > AssertionError: assert '' == 'chr1\t100\t2...0\t0.450000\n'
  >   
  >   - chr1	100	200	interval1	10	+	0.400000	0.200000
  >   - chr1	300	500	interval2	20	-	0.400000	0.500000
  >   - chr2	50	150	interval3	30	+	0.200000	0.200000
  >   - chr2	400	600	interval4	40	-	0.500000	0.450000
- `tests.test_annotate.test_annotate_with_names_header`
  > AssertionError: assert '' == '#\t\t\t\t\t\...0\t0.450000\n'
  >   
  >   - #						File1	File2
  >   - chr1	100	200	interval1	10	+	0.400000	0.200000
  >   - chr1	300	500	interval2	20	-	0.400000	0.500000
  >   - chr2	50	150	interval3	30	+	0.200000	0.200000
  >   - chr2	400	600	interval4	40	-	0.500000	0.450000
- *(... 220 more in this cluster)*

### `other_assertion` — 92 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_fasta_ops.test_maskfasta_error_missing_fasta`
  > AssertionError: assert 'could not be opened' in ''
- `tests.test_fasta_ops.test_nuc_error_missing_fasta`
  > AssertionError: assert 'could not be opened' in ''
- `tests.test_harvest_closest.test_closest_t01`
  > AssertionError: Output mismatch
  >   Expected:
  >   chr1	10	20	chr1	20	21	1
  >   Got:
  >   
  > assert '' == 'chr1\t10\t20...r1\t20\t21\t1'
  >   
  >   - chr1	10	20	chr1	20	21	1
- *(... 89 more in this cluster)*

### `missing_file` — 13 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_fasta_ops.test_maskfasta_basic_hard_mask`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_maskfasta_basic_hard_mask2/masked.fa'
- `tests.test_fasta_ops.test_maskfasta_soft_mask`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_maskfasta_soft_mask2/masked_soft.fa'
- `tests.test_fasta_ops.test_maskfasta_custom_mask_character`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_maskfasta_custom_mask_cha2/masked_custom.fa'
- *(... 10 more in this cluster)*

### `empty_list_or_string` — 5 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_harvest_fasta_groupby.test_getfasta_t02`
  > IndexError: list index out of range
- `tests.test_harvest_fasta_groupby.test_getfasta_t03`
  > IndexError: list index out of range
- `tests.test_harvest_fasta_groupby.test_getfasta_t04`
  > IndexError: list index out of range
- *(... 2 more in this cluster)*

### `rc_mismatch_got0_want1` — 4 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_annotate.test_annotate_error_missing_input_file`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'annotate', '-files', '/workspace/eval/test_resources/test_annotate/features1.bed'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_annotate.test_annotate_error_missing_files_parameter`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'annotate', '-i', '/workspace/eval/test_resources/test_annotate/intervals.bed'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_annotate.test_annotate_error_both_strand_flags`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'annotate', '-i', '/workspace/eval/test_resources/test_annotate/intervals.bed', '-files', '/workspace/eval/test_resources/test_annotate/fe
- *(... 1 more in this cluster)*

### `rc_unexpected_zero` — 4 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_harvest_general_coverage.TestGeneral.test_general_t01_negative_coordinates`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'merge', '-i', '-'], returncode=0, stdout='chr1\t1\t10\nchr1\t-1\t10', stderr='').returncode
- `tests.test_harvest_general_coverage.TestGeneral.test_general_t02_start_greater_than_end`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'merge', '-i', '-'], returncode=0, stdout='chr1\t1\t2\nchr1\t10\t5', stderr='').returncode
- `tests.test_harvest_general_coverage.TestGeneral.test_general_t03_non_integer_coordinates`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'merge', '-i', '-'], returncode=0, stdout='chr1\t.\t2', stderr='').returncode
- *(... 1 more in this cluster)*

### `subprocess_failed` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_harvest_bam_bed_conversions.test_bedtobam_t1_basic_conversion`
  > subprocess.CalledProcessError: Command '['/workspace/eval/tests/resources/htsutil', 'viewbamrecords', '/tmp/tmpki74c80x/output.bam']' returned non-zero exit status 1.

