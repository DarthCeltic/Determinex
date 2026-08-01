# Action Sheet — chirlu__sox.42b3557

**Current:** 0.41%  (6/1469)
**Pass / Fail / Skip:** 6 / 570 / 0
**Gap to 100%:** 99.59 percentage points (1463 tests)

## Failure clusters

570 failed tests grouped into 11 buckets (sorted by count).

### `rc_mismatch_got2_want0` — 212 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_audio_formats.test_stereo_wav_format`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-n', '-r', '44100', '-c', '2', '-b', '16', '/tmp/pytest-of-root/pytest-0/test_stereo_wav_format2/stereo.wav', 'synth', '0.5', 'sine', '44
- `tests.test_audio_formats.test_type_flag_explicit`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-t', 'wav', '/tmp/pytest-of-root/pytest-0/fmts0/source.wav', '-t', 'au', '/tmp/pytest-of-root/pytest-0/test_type_flag_explicit2/explicit_
- `tests.test_error_handling.test_guard_prevents_clipping`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-G', '/tmp/pytest-of-root/pytest-0/test_guard_prevents_clipping2/src.wav', '/tmp/pytest-of-root/pytest-0/test_guard_prevents_clipping2/gu
- *(... 209 more in this cluster)*

### `other_assertion` — 185 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_audio_formats.test_wav_pcm_16bit`
  > assert b'16' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', '--info', '-b', '/tmp/pytest-of-root/pytest-0/test_wav_pcm_16bit2/pcm16.wav'], returncode=2, stdout=b'', stderr=b"sox: unknown option: -
- `tests.test_audio_formats.test_wav_pcm_8bit`
  > assert b'8' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', '--info', '-b', '/tmp/pytest-of-root/pytest-0/test_wav_pcm_8bit2/pcm8.wav'], returncode=2, stdout=b'', stderr=b"sox: unknown option: --i
- `tests.test_audio_formats.test_au_ulaw`
  > assert (b'u-law' in b'' or b'mu-law' in b'')
  >  +  where b'' = <built-in method lower of bytes object at 0x7fcfcdac8030>()
  >  +    where <built-in method lower of bytes object at 0x7fcfcdac8030> = b''.lower
  >  +      where b'' = CompletedProcess(args=['/workspace/executable', '--info', '-e', '/tmp/pytest-of-root/pytest-0/test_au_ulaw2/ulaw.au'], returncode=2, stdout=b'', stderr=b"sox: unknown option: --inf
  >  +  and   b'' = <built-in method lower of bytes object at 0x7fcfcdac8030>()
  >  +    where <built-in method lower of bytes object at 0x7fcfcdac8030> = b''.lower
  >  +      where b'' = CompletedProcess(args=['/workspace/executable', '--info', '-e', '/tmp/pytest-of-root/pytest-0/test_au_ulaw2/ulaw.au'], returncode=2, stdout=b'', stderr=b"sox: unknown option: --inf
- *(... 182 more in this cluster)*

### `boolean_false` — 66 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_audio_formats.test_wav_format`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/pytest-of-root/pytest-0/test_wav_format2/output.wav').exists
- `tests.test_audio_formats.test_au_format`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/pytest-of-root/pytest-0/test_au_format2/output.au').exists
- `tests.test_audio_formats.test_aiff_format`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/pytest-of-root/pytest-0/test_aiff_format2/output.aiff').exists
- *(... 63 more in this cluster)*

### `string_output_mismatch` — 36 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_cli_options.test_type_option_unknown`
  > assert b"sox: unknow...nformation.\n" == b"/workspace/...e `unknown'\n"
  >   
  >   At index 0 diff: b's' != b'/'
  >   
  >   Full diff:
  >   - (b"/workspace/executable FAIL formats: no handler for given file type `unknown'"
  >   -  b'\n')
  >   + (b"sox: unknown option: -t\nusage: sox [OPTIONS] [ARGS]\nTry 'sox --help' for"
- `tests.test_effects_advanced_comp.test_mcompand_2band_compression`
  > AssertionError: assert '' == 'Samples read...        1.444'
  >   
  >   - Samples read:              8000
  >   - Length (seconds):      1.000000
  >   - Scaled by:         2147483647.0
  >   - Maximum amplitude:     0.692628
  >   - Minimum amplitude:    -0.675942
  >   - Midline amplitude:     0.008343...
- `tests.test_effects_advanced_comp.test_stats_default_output`
  > AssertionError: assert '' == 'DC offset   ...s       0.050'
  >   
  >   - DC offset   0.000003
  >   - Min level  -0.705000
  >   - Max level   0.705000
  >   - Pk lev dB      -3.04
  >   - RMS lev dB     -6.05
  >   - RMS Pk dB      -6.03...
- *(... 33 more in this cluster)*

### `rc_unexpected_zero` — 35 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_basic_invocation.test_nonexistent_file_error`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/tmp/nonexistent_file_xyz.wav', '/tmp/out.wav'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_error_handling.test_nonexistent_input_file`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/tmp/does_not_exist_abc123.wav', '/tmp/out.wav'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_error_handling.test_invalid_effect_name`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/tmp/pytest-of-root/pytest-0/test_invalid_effect_name2/src.wav', '/tmp/pytest-of-root/pytest-0/test_invalid_effect_name2/out.wav', 'nonex
- *(... 32 more in this cluster)*

### `returned_none` — 10 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_basic_invocation.test_version_format`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7fcfcda42680>(b'SoX v\\d+\\.\\d+', b'sox 0.1.0\n')
  >  +    where <function search at 0x7fcfcda42680> = re.search
  >  +    and   b'sox 0.1.0\n' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'sox 0.1.0\n', stderr=b'').stdout
- `tests.test_effects.test_gain_norm`
  > assert None is not None
- `tests.test_effects.test_vol_half`
  > assert None is not None
- *(... 7 more in this cluster)*

### `uncategorized` — 8 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_effects.test_trim_shortens_duration`
  > ValueError: could not convert string to float: b''
- `tests.test_effects.test_trim_with_offset`
  > ValueError: could not convert string to float: b''
- `tests.test_effects.test_pad_adds_silence`
  > ValueError: could not convert string to float: b''
- *(... 5 more in this cluster)*

### `missing_file` — 7 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_audio_formats.test_raw_format_unsigned8`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_raw_format_unsigned82/output_u8.raw'
- `tests.test_audio_formats.test_raw_format_float32`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_raw_format_float322/output_f32.raw'
- `tests.test_audio_formats.test_dat_header_contents`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_dat_header_contents2/output.dat'
- *(... 4 more in this cluster)*

### `bytes_output_mismatch` — 6 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_stdin_stdout.test_stdout_pipe_output`
  > AssertionError: assert b'' == b'RIFF'
  >   
  >   Full diff:
  >   - b'RIFF'
  >   + b''
- `tests.test_cli_options.test_version_output`
  > AssertionError: assert b'sox 0.1.0\n' == b'/workspace/...SoX v14.4.2\n'
  >   
  >   At index 0 diff: b's' != b'/'
  >   
  >   Full diff:
  >   - (b'/workspace/executable:      SoX v14.4.2\n')
  >   + (b'sox 0.1.0\n')
- `tests.test_cli_options.test_help_output_complete`
  > AssertionError: assert b'sox 0.1.0 -...int version\n' == b'/workspace/...help-effect\n'
  >   
  >   At index 0 diff: b's' != b'/'
  >   
  >   Full diff:
  >   + (b'sox 0.1.0 - bootstrap scaffold\n\nUsage: sox [OPTIONS] [ARGS]\n\nOptions'
  >   +  b':\n  -h, --help     Print help\n  -V, --version  Print version\n')
  >   - (b'/workspace/executable:      SoX v14.4.2\n\nUsage summary: [gopts] [[fopts]'...
- *(... 3 more in this cluster)*

### `rc_mismatch_got2_want1` — 4 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_options.test_help_effect_specific`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--help-effect', 'gain'], returncode=2, stdout=b'', stderr=b"sox: unknown option: --help-effect\nusage: sox [OPTIONS] [ARGS]\nTry 'sox --h
- `tests.test_cli_options.test_help_format_specific`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--help-format', 'wav'], returncode=2, stdout=b'', stderr=b"sox: unknown option: --help-format\nusage: sox [OPTIONS] [ARGS]\nTry 'sox --he
- `tests.test_cli_options.test_help_effect_all`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--help-effect', 'all'], returncode=2, stdout=b'', stderr=b"sox: unknown option: --help-effect\nusage: sox [OPTIONS] [ARGS]\nTry 'sox --he
- *(... 1 more in this cluster)*

### `rc_mismatch_got0_want1600` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_stdin_stdout.test_stdout_raw_output`
  > AssertionError: assert 0 == 1600
  >  +  where 0 = len(b'')
  >  +    where b'' = CompletedProcess(args=['/workspace/executable', '/tmp/pytest-of-root/pytest-0/test_stdout_raw_output2/source.wav', '-t', 'raw', '-e', 'signed-integer', '-b', '16', '-r', '8000', '-c'

