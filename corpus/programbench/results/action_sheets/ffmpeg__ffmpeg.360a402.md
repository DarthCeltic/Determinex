# Action Sheet — ffmpeg__ffmpeg.360a402

**Current:** 2.08%  (68/3266)
**Pass / Fail / Skip:** 68 / 596 / 0
**Gap to 100%:** 97.92 percentage points (3198 tests)

## Failure clusters

596 failed tests grouped into 14 buckets (sorted by count).

### `other_assertion` — 303 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_help_behavior.test_help_mentions_universal_media_converter`
  > AssertionError: assert 'Universal media converter' in 'ffmpeg 0.1.0 - bootstrap scaffold\n\nUsage: ffmpeg [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n'
- `eval.tests.test_help_behavior.test_help_has_usage_synopsis_line`
  > AssertionError: assert 'usage: ffmpeg [options]' in 'ffmpeg 0.1.0 - bootstrap scaffold\n\nUsage: ffmpeg [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n'
- `eval.tests.test_help_behavior.test_help_has_getting_help_section`
  > AssertionError: assert 'Getting help:' in 'ffmpeg 0.1.0 - bootstrap scaffold\n\nUsage: ffmpeg [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n'
- *(... 300 more in this cluster)*

### `rc_mismatch_got2_want0` — 135 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `eval.tests.test_config_env_ffreport.test_ffreport_env_creates_report_file_at_path`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-v', 'error', '-f', 'lavfi', '-i', 'anullsrc=r=8000:cl=mono', '-t', '0.01', '-f', 'null', '-'], returncode=2, stdout=b'', stderr=b"ffmpeg
- `eval.tests.test_config_env_ffreport.test_ffreport_env_unknown_key_is_nonfatal_and_still_writes_file`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-v', 'error', '-f', 'lavfi', '-i', 'anullsrc=r=8000:cl=mono', '-t', '0.01', '-f', 'null', '-'], returncode=2, stdout=b'', stderr=b"ffmpeg
- `eval.tests.test_config_env_ffreport.test_ffreport_invalid_level_prints_error_and_does_not_create_default_log`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-v', 'error', '-f', 'lavfi', '-i', 'anullsrc=r=8000:cl=mono', '-t', '0.01', '-f', 'null', '-'], returncode=2, stdout=b'', stderr=b"ffmpeg
- *(... 132 more in this cluster)*

### `boolean_false` — 42 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_filters.TestVideoFilters.test_scale_filter`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/pytest-of-root/pytest-0/test_scale_filter2/output.mp4').exists
- `tests.test_filters.TestVideoFilters.test_crop_filter`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/pytest-of-root/pytest-0/test_crop_filter2/output.mp4').exists
- `tests.test_filters.TestVideoFilters.test_hflip_filter`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/pytest-of-root/pytest-0/test_hflip_filter2/output.mp4').exists
- *(... 39 more in this cluster)*

### `rc_unexpected_zero` — 29 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `eval.tests.test_errors.test_nonexistent_input_file`
  > AssertionError: assert 0 != 0
  >  +  where 0 = RunResult(args=['/workspace/executable', '-hide_banner', '-y', '-i', '/tmp/pytest-of-root/pytest-0/test_nonexistent_input_file2/no_such_file.wav', '/tmp/pytest-of-root/pytest-0/test_none
- `tests.test_error_handling.TestMissingInput.test_missing_input_file_nonzero_exit`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/eval/tests/../../executable', '-i', '/nonexistent/file.mp4', '-f', 'null', '-'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_error_handling.TestMissingInput.test_missing_input_directory`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/eval/tests/../../executable', '-i', '/no/such/dir/video.mp4', '-f', 'null', '-'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 26 more in this cluster)*

### `missing_file` — 18 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_probe.TestFrameOperations.test_limit_frames`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/ffmpeg_test_p3decnf7/limited.rgb'
- `tests.test_synthetic_generation.TestAudioGeneration.test_generate_sine_wav`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/ffmpeg_test_fkzd7d3l/sine.wav'
- `tests.test_synthetic_generation.TestAudioGeneration.test_generate_silence_wav`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/ffmpeg_test_5svat6ck/silence.wav'
- *(... 15 more in this cluster)*

### `string_output_mismatch` — 13 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_behavior.test_help_baseline_exact_match_for_static_portion`
  > AssertionError: assert 'ffmpeg 0.1.0...int version\n' == 'Universal me...exit code 0\n'
  >   
  >   + ffmpeg 0.1.0 - bootstrap scaffold
  >   - Universal media converter
  >   - usage: ffmpeg [options] [[infile options] -i infile]... {[outfile options] outfile}...
  >     
  >   + Usage: ffmpeg [OPTIONS] [ARGS]
  >   - Getting help:...
- `tests.test_cmdutils.test_invalid_duration_parsing_error`
  > assert "ffmpeg: Inva...notanumber'\n" == 'ffmpeg versi...id argument\n'
  >   
  >   + ffmpeg: Invalid duration 'notanumber'
  >   - ffmpeg version git-YYYY-MM-DD-HASH Copyright (c) 2000-2026 the FFmpeg developers
  >   -   built with gcc 11 (Ubuntu 11.4.0-1ubuntu1~22.04.3)
  >   -   configuration: <BUILD_CONFIG>
  >   -   libavutil      60. 25.100 / 60. 25.100
  >   -   libavcodec     62. 23.103 / 62. 23.103...
- `tests.test_cmdutils_deep.test_error_file_not_found`
  > AssertionError: assert 'ffmpeg: /non...r directory\n' == 'ffmpeg versi...r directory\n'
  >   
  >   + ffmpeg: /nonexistent.mp4: No such file or directory
  >   - ffmpeg version git-YYYY-MM-DD-HASH Copyright (c) 2000-2026 the FFmpeg developers
  >   -   built with gcc 11 (Ubuntu 11.4.0-1ubuntu1~22.04.3)
  >   -   configuration: <BUILD_CONFIG>
  >   -   libavutil      60. 25.100 / 60. 25.100
  >   -   libavcodec     62. 23.103 / 62. 23.103...
- *(... 10 more in this cluster)*

### `rc_mismatch_got2_want8` — 12 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_argparse_validation.test_unknown_options_error_out[args0-8-expected_stderr_substrings0]`
  > assert 2 == 8
  >  +  where 2 = RunResult(returncode=2, stdout='', stderr="ffmpeg: unknown option: -foo\nusage: ffmpeg [OPTIONS] [ARGS]\nTry 'ffmpeg --help' for more information.\n").returncode
- `eval.tests.test_argparse_validation.test_unknown_options_error_out[args1-8-expected_stderr_substrings1]`
  > assert 2 == 8
  >  +  where 2 = RunResult(returncode=2, stdout='', stderr="ffmpeg: unknown option: --no-such-option\nusage: ffmpeg [OPTIONS] [ARGS]\nTry 'ffmpeg --help' for more information.\n").returncode
- `eval.tests.test_argparse_validation.test_unknown_options_error_out[args2-8-expected_stderr_substrings2]`
  > assert 2 == 8
  >  +  where 2 = RunResult(returncode=2, stdout='', stderr="ffmpeg: unknown option: -nostdin\nusage: ffmpeg [OPTIONS] [ARGS]\nTry 'ffmpeg --help' for more information.\n").returncode
- *(... 9 more in this cluster)*

### `returned_none` — 10 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_chapters_disposition.test_disposition_multiple_flags_on_stream`
  > assert None is not None
- `tests.test_decoder_deep.test_decoder_corrupt_frame_exit_on_error`
  > assert None is not None
- `tests.test_decoder_deep.test_decoder_wallclock_latency_timestamps_set`
  > assert None is not None
- *(... 7 more in this cluster)*

### `empty_list_or_string` — 9 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_audio_options.test_af_aresample_filter`
  > IndexError: list index out of range
- `tests.test_audio_options.test_ar_and_ac_combined`
  > IndexError: list index out of range
- `tests.test_audio_options.test_ba_and_ar_combined`
  > IndexError: list index out of range
- *(... 6 more in this cluster)*

### `rc_mismatch_got2_want1` — 7 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_argparse_validation.test_no_output_specified_usage_errors[args0-1-expected_stderr_substrings0]`
  > assert 2 == 1
  >  +  where 2 = RunResult(returncode=2, stdout='', stderr="usage: ffmpeg [OPTIONS] [ARGS]\nTry 'ffmpeg --help' for more information.\n").returncode
- `eval.tests.test_argparse_validation.test_no_output_specified_usage_errors[args1-1-expected_stderr_substrings1]`
  > assert 2 == 1
  >  +  where 2 = RunResult(returncode=2, stdout='', stderr="ffmpeg: unknown option: -nostdin\nusage: ffmpeg [OPTIONS] [ARGS]\nTry 'ffmpeg --help' for more information.\n").returncode
- `eval.tests.test_argparse_validation.test_short_and_long_loglevel_equivalent_for_parse_success`
  > assert 2 == 1
  >  +  where 2 = RunResult(returncode=2, stdout='', stderr="ffmpeg: unknown option: -v\nusage: ffmpeg [OPTIONS] [ARGS]\nTry 'ffmpeg --help' for more information.\n").returncode
- *(... 4 more in this cluster)*

### `rc_mismatch_got0_want2` — 7 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_codecs.test_stream_copy_codec`
  > assert 0 == 2
  >  +  where 0 = len([])
- `tests.test_codecs.test_video_codec_copy`
  > assert 0 == 2
  >  +  where 0 = len([])
- `tests.test_concat_segment.test_segment_reset_timestamps`
  > assert 0 == 2
  >  +  where 0 = len([])
- *(... 4 more in this cluster)*

### `rc_mismatch_got0_want1` — 6 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `eval.tests.test_argparse_validation.test_no_output_specified_usage_errors[args2-1-expected_stderr_substrings2]`
  > AssertionError: assert 0 == 1
  >  +  where 0 = RunResult(returncode=0, stdout='', stderr='').returncode
- `eval.tests.test_argparse_validation.test_no_output_specified_usage_errors[args3-1-expected_stderr_substrings3]`
  > AssertionError: assert 0 == 1
  >  +  where 0 = RunResult(returncode=0, stdout='', stderr='').returncode
- `tests.test_audio_options.test_ba_128k_bitrate`
  > assert 0 == 1
  >  +  where 0 = len([])
- *(... 3 more in this cluster)*

### `rc_mismatch_got2_want234` — 4 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cmdutils.test_missing_argument_error`
  > assert 2 == 234
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-c:v'], returncode=2, stdout='', stderr="ffmpeg: unknown option: -c:v\nusage: ffmpeg [OPTIONS] [ARGS]\nTry 'ffmpeg --help' for more infor
- `tests.test_cmdutils_gaps.test_loglevel_invalid_string`
  > assert 2 == 234
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-loglevel', 'overflow'], returncode=2, stdout='', stderr="ffmpeg: unknown option: -loglevel\nusage: ffmpeg [OPTIONS] [ARGS]\nTry 'ffmpeg 
- `tests.test_cmdutils_gaps.test_cpuflags_invalid_normalized`
  > assert 2 == 234
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-cpuflags', 'invalid_cpu_flag'], returncode=2, stdout='', stderr="ffmpeg: unknown option: -cpuflags\nusage: ffmpeg [OPTIONS] [ARGS]\nTry 
- *(... 1 more in this cluster)*

### `rc_mismatch_got2_want244` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cmdutils_gaps.test_max_alloc_small_value_error`
  > assert 2 == 244
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-max_alloc', '1', '-f', 'lavfi', '-i', 'testsrc=d=0.01', '-f', 'null', '-'], returncode=2, stdout='', stderr="ffmpeg: unknown option: -ma

