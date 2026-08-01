# Action Sheet — samtools__samtools.aa823b5

**Current:** 9.6%  (145/1511)
**Pass / Fail / Skip:** 145 / 555 / 0
**Gap to 100%:** 90.40 percentage points (1366 tests)

## Failure clusters

555 failed tests grouped into 19 buckets (sorted by count).

### `other_assertion` — 226 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic.TestBasicInvocation.test_version_command`
  > AssertionError: assert b'htslib' in b'samtools 1.17\n'
  >  +  where b'samtools 1.17\n' = CompletedProcess(args=['/workspace/executable', 'version'], returncode=0, stdout=b'samtools 1.17\n', stderr=b'').stdout
- `tests.test_basic.TestBasicInvocation.test_version_contains_compilation_details`
  > AssertionError: assert b'Samtools compilation details' in b'samtools 1.17\n'
  >  +  where b'samtools 1.17\n' = CompletedProcess(args=['/workspace/executable', 'version'], returncode=0, stdout=b'samtools 1.17\n', stderr=b'').stdout
- `tests.test_basic.TestBasicInvocation.test_version_htslib_info`
  > AssertionError: assert (b'HTSlib compilation details' in b'samtools 1.17\n' or b'Using htslib' in b'samtools 1.17\n')
  >  +  where b'samtools 1.17\n' = CompletedProcess(args=['/workspace/executable', 'version'], returncode=0, stdout=b'samtools 1.17\n', stderr=b'').stdout
  >  +  and   b'samtools 1.17\n' = CompletedProcess(args=['/workspace/executable', 'version'], returncode=0, stdout=b'samtools 1.17\n', stderr=b'').stdout
- *(... 223 more in this cluster)*

### `string_output_mismatch` — 78 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_coverage_gap.TestViewWithMoreOptions.test_view_qname_file`
  > AssertionError: assert '@SQ' == '@HD'
  >   
  >   - @HD
  >   + @SQ
- `tests.test_coverage_gap.TestViewMoreCoverage.test_view_output_qname`
  > AssertionError: assert '@SQ' == '@HD'
  >   
  >   - @HD
  >   + @SQ
- `tests.test_editing.TestBedcovCommand.test_bedcov_output_format`
  > AssertionError: assert '1' == '6'
  >   
  >   - 6
  >   + 1
- *(... 75 more in this cluster)*

### `rc_mismatch_got1_want0` — 59 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_basic.TestFlagsCommand.test_flags_no_args_shows_usage`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'flags'], returncode=1, stdout=b'', stderr=b'usage: samtools flags <flag>\n').returncode
- `tests.test_basic.TestFlagsCommand.test_flags_text_to_numeric`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'flags', 'PAIRED'], returncode=1, stdout=b'', stderr=b'samtools: invalid flag: PAIRED\n').returncode
- `tests.test_basic.TestFlagsCommand.test_flags_multiple_flags`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'flags', 'PAIRED', 'UNMAP'], returncode=1, stdout=b'', stderr=b'samtools: invalid flag: PAIRED\n').returncode
- *(... 56 more in this cluster)*

### `boolean_false` — 55 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_coverage_gap.TestViewAdvanced.test_view_fast_compression`
  > AssertionError: assert False
  >  +  where False = is_bgzf(b'@HD\tVN:1.6\tSO:coordinate\n@SQ\tSN:ref\tLN:1000\n')
  >  +    where b'@HD\tVN:1.6\tSO:coordinate\n@SQ\tSN:ref\tLN:1000\n' = read_bytes()
  >  +      where read_bytes = PosixPath('/tmp/tmpqr57_y_y/fast.bam').read_bytes
- `tests.test_coverage_gap.TestViewAdvanced.test_view_save_counts`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmp2pplbxoa/counts.txt').exists
- `tests.test_coverage_gap.TestAddReplaceRGAdvanced.test_addreplacerg_overwrite_mode`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpih38ybah/out.bam').exists
- *(... 52 more in this cluster)*

### `rc_unexpected_zero` — 32 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_basic.TestErrorHandling.test_view_missing_file`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'view', '/nonexistent/file.bam'], returncode=0, stdout=b'@HD\tVN:1.6\tSO:coordinate\n@SQ\tSN:ref\tLN:1000\n', stderr=b'').returncode
- `tests.test_basic.TestErrorHandling.test_sort_missing_file`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'sort', '/nonexistent/file.bam'], returncode=0, stdout=b'@HD\tVN:1.6\tSO:coordinate\n@SQ\tSN:ref\tLN:1000\n', stderr=b'').returncode
- `tests.test_basic.TestErrorHandling.test_flagstat_missing_file`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'flagstat', '/nonexistent/file.bam'], returncode=0, stdout=b'0 + 0 mapped (0.00% : N/A)\n0 + 0 paired in sequencing\n0 + 0 read1\n0 + 0 re
- *(... 29 more in this cluster)*

### `bytes_output_mismatch` — 31 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_coverage_gap.TestSortAdvanced.test_sort_by_tag`
  > AssertionError: assert b'0' == b'12'
  >   
  >   At index 0 diff: b'0' != b'1'
  >   
  >   Full diff:
  >   - b'12'
  >   + b'0'
- `tests.test_coverage_gap.TestSortAdvanced.test_sort_minimiser`
  > AssertionError: assert b'0' == b'12'
  >   
  >   At index 0 diff: b'0' != b'1'
  >   
  >   Full diff:
  >   - b'12'
  >   + b'0'
- `tests.test_coverage_gap.TestViewAdvanced.test_view_cram_input`
  > AssertionError: assert b'>ref\n>ref2' == b'12'
  >   
  >   At index 0 diff: b'>' != b'1'
  >   
  >   Full diff:
  >   - b'12'
  >   + (b'>ref\n>ref2')
- *(... 28 more in this cluster)*

### `missing_file` — 18 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_editing.TestAddReplaceRGCommand.test_addreplacerg_output_is_bam`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpxz4rbyik/out.bam'
- `tests.test_editing.TestAddReplaceRGCommand.test_addreplacerg_sam_output`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmppseecuu2/out.sam'
- `tests.test_indexing.TestFaidxCommand.test_faidx_length_in_index`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/toy_fa0/toy.fa.fai'
- *(... 15 more in this cluster)*

### `empty_list_or_string` — 14 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_addrg_padding_qcheck_gaps.test_addreplacerg_complex_rg_fields`
  > IndexError: list index out of range
- `tests.test_addrg_padding_qcheck_gaps.test_addreplacerg_orphan_only_mode`
  > IndexError: list index out of range
- `tests.test_addrg_padding_qcheck_gaps.test_addreplacerg_escape_backslash`
  > IndexError: list index out of range
- *(... 11 more in this cluster)*

### `subprocess_failed` — 14 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_addrg_padding_qcheck_gaps.test_depad_sam_to_sam_comprehensive`
  > subprocess.CalledProcessError: Command '['/workspace/executable', 'depad', '-S', '-s', '-T', '/workspace/test/dat/depad.001.fa', '--no-PG', '/workspace/test/dat/depad.001p.sam']' returned non-zero exi
- `tests.test_addrg_padding_qcheck_gaps.test_depad_without_reference_warning`
  > subprocess.CalledProcessError: Command '['/workspace/executable', 'depad', '-S', '-s', '--no-PG', '/workspace/test/dat/depad.001p.sam']' returned non-zero exit status 1.
- `tests.test_addrg_padding_qcheck_gaps.test_depad_bam_output_compression_levels`
  > subprocess.CalledProcessError: Command '['/workspace/executable', 'depad', '-1', '-T', '/workspace/test/dat/depad.001.fa', '--no-PG', '-o', '/tmp/pytest-of-root/pytest-0/test_depad_bam_output_compress
- *(... 11 more in this cluster)*

### `rc_mismatch_got0_want2` — 8 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_fixmate.test_basic_mate_info_filling`
  > assert 0 == 2
  >  +  where 0 = len([])
- `tests.test_fixmate.test_mate_score_tag_addition`
  > assert 0 == 2
  >  +  where 0 = len([])
- `tests.test_fixmate.test_template_cigar_ct_tag`
  > assert 0 == 2
  >  +  where 0 = len([])
- *(... 5 more in this cluster)*

### `rc_mismatch_got0_want1` — 5 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_ampliconclip.test_missing_bed_file_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'ampliconclip', '-b', 'nonexistent.bed', '/workspace/eval/test_resources/test_ampliconclip/1_test_data.sam'], returncode=0, stdout=b'@HD\t
- `tests.test_ampliconclip.test_invalid_bed_format_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'ampliconclip', '-b', '/tmp/pytest-of-root/pytest-0/test_invalid_bed_format_error2/invalid.bed', '/workspace/eval/test_resources/test_ampl
- `tests.test_faidx_advanced.test_faidx_nonexistent_chromosome_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'faidx', '/workspace/eval/test_resources/test_faidx_advanced/test.fa', 'nonexistent_chr'], returncode=0, stdout=b'>ref\nACGT\n', stderr=b'
- *(... 2 more in this cluster)*

### `rc_mismatch_got2_want1` — 4 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic.TestBasicInvocation.test_no_args_shows_help`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b'usage: samtools <command> [options]\n\nCommands:\n  --help               display this help and exit\n 
- `tests.test_basic.TestBasicInvocation.test_no_args_shows_commands`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b'usage: samtools <command> [options]\n\nCommands:\n  --help               display this help and exit\n 
- `tests.test_cat_remaining.test_cat_cram_query_container_count`
  > AssertionError: assert 2 == 1
  >  +  where 2 = len(['@HD\tVN:1.6\tSO:coordinate', '@SQ\tSN:ref\tLN:1000'])
- *(... 1 more in this cluster)*

### `rc_mismatch_got2_want12` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_coverage_gap.TestViewAdvanced.test_view_add_flags`
  > AssertionError: assert 2 == 12
  >  +  where 2 = len(['@HD\tVN:1.6\tSO:coordinate', '@SQ\tSN:ref\tLN:1000'])
- `tests.test_coverage_gap.TestViewMoreCoverage.test_view_keep_tag`
  > AssertionError: assert 2 == 12
  >  +  where 2 = len(['@HD\tVN:1.6\tSO:coordinate', '@SQ\tSN:ref\tLN:1000'])

### `rc_mismatch_got1_want2` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_editing.TestBedcovCommand.test_bedcov_multiple_regions`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len(['ref\t1\t1000\t0'])
- `tests.test_indexing.TestDictCommand.test_dict_sq_entries`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len(['@SQ\tSN:ref\tLN:1000'])

### `rc_mismatch_got0_want4` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_color.test_colorspace_tags_round_trip_bam_to_sam`
  > assert 0 == 4
  >  +  where 0 = len([])
- `tests.test_color.test_colorspace_sam_to_bam_to_sam_roundtrip`
  > AssertionError: assert 0 == 4
  >  +  where 0 = len([])
  >  +  and   4 = len(['read1\t0\tchr1\t10\t60\t10M\t*\t0\t0\tACGTACGTAC\t##########\tCS:Z:T0123012301\tCQ:Z:IIIIIIIIII', 'read2\t16\tchr1\t30\t60\t10M\t*\t0\t0\tTGCATGCATG\t##########\tCS:Z:A3210321032\t

### `uncategorized` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_fastq_advanced.test_compression_level_setting`
  > gzip.BadGzipFile: Not a gzipped file (b'@r')
- `tests.test_fastq_import_gaps.test_fastq_compression_level`
  > gzip.BadGzipFile: Not a gzipped file (b'@r')

### `rc_mismatch_got2_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_coverage_gap.TestIdxstatsAndSamples.test_idxstats_from_stdin`
  > AssertionError: assert 2 == 3
  >  +  where 2 = len(['ref\t1000\t0\t0', '*\t0\t0\t0'])

### `rc_mismatch_got2_want6` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cat_advanced.test_cat_multiple_files_preserves_order`
  > AssertionError: assert 2 == 6
  >  +  where 2 = len(['@HD\tVN:1.6\tSO:coordinate', '@SQ\tSN:ref\tLN:1000'])

### `rc_mismatch_got2_want4` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_color.test_colorspace_tags_preserved_through_view`
  > AssertionError: assert 2 == 4
  >  +  where 2 = len(['@HD\tVN:1.6\tSO:coordinate', '@SQ\tSN:ref\tLN:1000'])

