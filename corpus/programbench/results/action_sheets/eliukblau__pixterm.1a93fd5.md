# Action Sheet — eliukblau__pixterm.1a93fd5

**Current:** 12.52%  (66/527)
**Pass / Fail / Skip:** 66 / 392 / 0
**Gap to 100%:** 87.48 percentage points (461 tests)

## Failure clusters

392 failed tests grouped into 11 buckets (sorted by count).

### `other_assertion` — 229 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_help_contains_all_flags`
  > AssertionError: assert b'-credits' in b'USAGE:\nexecutable [options] image/url\nSupported image formats: JPEG, PNG, GIF, BMP, TIFF, WebP\nSupported URL protocols: HTTP, HTTPS\nUSAGE:\nOPTIONS:\nprints
  >  +  where b'USAGE:\nexecutable [options] image/url\nSupported image formats: JPEG, PNG, GIF, BMP, TIFF, WebP\nSupported URL protocols: HTTP, HTTPS\nUSAGE:\nOPTIONS:\nprints this message :D LOL\n1.3.2\
- `tests.test_basic_invocation.test_help_contains_dithering_modes`
  > AssertionError: assert b'0 - no dithering' in b'USAGE:\nexecutable [options] image/url\nSupported image formats: JPEG, PNG, GIF, BMP, TIFF, WebP\nSupported URL protocols: HTTP, HTTPS\nUSAGE:\nOPTIONS:
  >  +  where b'USAGE:\nexecutable [options] image/url\nSupported image formats: JPEG, PNG, GIF, BMP, TIFF, WebP\nSupported URL protocols: HTTP, HTTPS\nUSAGE:\nOPTIONS:\nprints this message :D LOL\n1.3.2\
- `tests.test_basic_invocation.test_help_contains_scale_methods`
  > AssertionError: assert b'0 - resize' in b'USAGE:\nexecutable [options] image/url\nSupported image formats: JPEG, PNG, GIF, BMP, TIFF, WebP\nSupported URL protocols: HTTP, HTTPS\nUSAGE:\nOPTIONS:\nprin
  >  +  where b'USAGE:\nexecutable [options] image/url\nSupported image formats: JPEG, PNG, GIF, BMP, TIFF, WebP\nSupported URL protocols: HTTP, HTTPS\nUSAGE:\nOPTIONS:\nprints this message :D LOL\n1.3.2\
- *(... 226 more in this cluster)*

### `rc_mismatch_got1_want0` — 53 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_edge_cases.test_very_small_image`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '/tmp/tmpc_wjh1h7/tiny.bmp', '-tc', '10', '-tr', '5'], returncode=1, stdout=b"   ___  _____  ____\n  / _ \\/  _/ |/_/ /____ ______ _      Made with
- `tests.test_edge_cases.test_all_black_image`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '/tmp/tmp4sr2d5wb/black.bmp', '-tc', '10', '-tr', '5'], returncode=1, stdout=b"   ___  _____  ____\n  / _ \\/  _/ |/_/ /____ ______ _      Made wit
- `tests.test_edge_cases.test_all_white_image`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', '/tmp/tmphgk9_09y/white.bmp', '-tc', '10', '-tr', '5'], returncode=1, stdout=b"   ___  _____  ____\n  / _ \\/  _/ |/_/ /____ ______ _      Made wit
- *(... 50 more in this cluster)*

### `string_output_mismatch` — 28 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_output.test_help_variants_match_exactly`
  > AssertionError: assert 'USAGE:\nexec...ORS:\n@disq\n' == ''
  >   
  >   + USAGE:
  >   + executable [options] image/url
  >   + Supported image formats: JPEG, PNG, GIF, BMP, TIFF, WebP
  >   + Supported URL protocols: HTTP, HTTPS
  >   + USAGE:
  >   + OPTIONS:...
- `tests.test_ansimage_api.test_corrupt_png_file_error`
  > AssertionError: assert '   ___  ____...nown format\n' == '   ___  ____...xpected EOF\n'
  >   
  >        ___  _____  ____
  >       / _ \/  _/ |/_/ /____ ______ _      Made with love by Eliuk Blau
  >      / ___// /_>  </ __/ -_) __/  ' \ https://github.com/eliukblau/pixterm
  >     /_/  /___/_/|_|\__/\__/_/ /_/_/_/                1.3.2
  >     
  >   - [PIXTERM ERROR] TIMESTAMP unexpected EOF
- `tests.test_dithering.test_dithering_respects_terminal_size_rows`
  > AssertionError: assert '\x1b[48;2;0;...60m░\x1b[0m\n' == '\x1b[48;2;0;...93m▓\x1b[0m\n'
  >   
  >   - #x1B[48;2;0;0;0m#x1B[38;2;61;61;61m░#x1B[48;2;0;0;0m#x1B[38;2;193;193;193m▓#x1B[0m
  >   ?                      ^  ^  ^                      ^^^ ^^^ ^^^ ^
  >   + #x1B[48;2;0;0;0m#x1B[38;2;60;60;60m░#x1B[48;2;0;0;0m#x1B[38;2;60;60;60m░#x1B[0m
  >   ?                      ^  ^  ^                      ^^ ^^ ^^ ^
  >   - #x1B[48;2;0;0;0m#x1B[38;2;61;61;61m░#x1B[48;2;0;0;0m#x1B[38;2;193;193;193m▓#x1B[0m
  >   ?                      ^  ^  ^                      ^^^ ^^^ ^^^ ^...
- *(... 25 more in this cluster)*

### `rc_mismatch_got2_want0` — 27 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_flag_combinations.test_multiple_flags_order_independence`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '/tmp/tmp9jv7q527/test.bmp', '-d', '1', '-tc', '10', '-tr', '5'], returncode=2, stdout=b"   ___  _____  ____\n  / _ \\/  _/ |/_/ /____ ______ _    
- `tests.test_nobg_flag.test_output_differs_with_and_without_nobg`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '/tmp/tmp9wa3n5m9/test.bmp', '-d', '1', '-tc', '10', '-tr', '5'], returncode=2, stdout=b"   ___  _____  ____\n  / _ \\/  _/ |/_/ /____ ______ _    
- `tests.test_output_format.test_output_contains_unicode_block`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '/tmp/tmpea_34afz/test.bmp', '-d', '0', '-tc', '10', '-tr', '5'], returncode=2, stdout=b"   ___  _____  ____\n  / _ \\/  _/ |/_/ /____ ______ _    
- *(... 24 more in this cluster)*

### `rc_mismatch_got0_want2` — 16 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_basic_invocation.test_no_arguments_shows_help`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['./executable'], returncode=0, stdout=b'#\n-credits\n-d\n-go\n-m\n-nobg\n-s\n-tc\n-tr\n-version\n/ _ \\\\/  _/ |/_/ /____ ______ _\n/_/  /___/_/|_|\\\\__/\\\\__/_/
- `eval.tests.test_argparse_validation.test_argparse_errors_show_usage_and_exit_2[args0]`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable'], returncode=0, stdout='#\n-credits\n-d\n-go\n-m\n-nobg\n-s\n-tc\n-tr\n-version\n/ _ \\\\/  _/ |/_/ /____ ______ _\n/_/  /___/_/|_|\\\\__/\
- `eval.tests.test_argparse_validation.test_argparse_errors_show_usage_and_exit_2[args1]`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-unknown'], returncode=0, stdout='#\n-credits\n-d\n-go\n-m\n-nobg\n-s\n-tc\n-tr\n-version\n/ _ \\\\/  _/ |/_/ /____ ______ _\n/_/  /___/_
- *(... 13 more in this cluster)*

### `rc_mismatch_got0_want1` — 13 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_input_handling.test_invalid_file_format`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', '/tmp/tmpj02nlk85/invalid.txt'], returncode=0, stdout=b'not an image#\n-credits\n-d\n-go\n-m\n-nobg\n-s\n-tc\n-tr\n-version\n/ _ \\\\/  _/ |/_/ /__
- `tests.test_input_handling.test_empty_file`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', '/tmp/tmpk9fm4xi3/empty.png'], returncode=0, stdout=b'#\n-credits\n-d\n-go\n-m\n-nobg\n-s\n-tc\n-tr\n-version\n/ _ \\\\/  _/ |/_/ /____ ______ _\n/
- `tests.test_input_handling.test_corrupted_image`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', '/tmp/tmpine33p39/corrupted.png'], returncode=0, stdout=b'\xef\xbf\xbdPNG\n\x1a\nGARBAGE#\n-credits\n-d\n-go\n-m\n-nobg\n-s\n-tc\n-tr\n-version\n/ 
- *(... 10 more in this cluster)*

### `bytes_output_mismatch` — 10 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_basic_invocation.test_version_flag`
  > AssertionError: assert b'1.3.2\nCONT...:\ngithub.com' == b'1.3.2'
  >   
  >   Full diff:
  >   - (b'1.3.2')
  >   + (b'1.3.2\nCONTRIBUTORS:\n@disq\n@timob\n@HongjiangHuang\n@brutestack\n@diamon'
  >   +  b'dburned\ntransparency support\nCONTRIBUTORS:\ngithub.com')
- `eval.tests.test_pixterm_cli.test_version_exact`
  > AssertionError: assert b'1.3.2\nCONT...ngithub.com\n' == b'1.3.2\n'
  >   
  >   Full diff:
  >   - (b'1.3.2\n')
  >   + (b'1.3.2\nCONTRIBUTORS:\n@disq\n@timob\n@HongjiangHuang\n@brutestack\n@diamon'
  >   +  b'dburned\ntransparency support\nCONTRIBUTORS:\ngithub.com\n')
- `tests.test_scaling.test_scale_method_with_dithering_mode1`
  > AssertionError: assert b'' == b'\x1b[48;2;0...\x88\x1b[0m\n'
  >   
  >   Full diff:
  >   + b''
  >   - (b'\x1b[48;2;0;0;0m\x1b[38;2;255;0;0m\xe2\x96\x88\x1b[48;2;0;0;0m\x1b[38;2;2'
  >   -  b'55;0;0m\xe2\x96\x88\x1b[48;2;0;0;0m\x1b[38;2;255;0;0m\xe2\x96\x88\x1b[48;2;'
  >   -  b'0;0;0m\x1b[38;2;255;0;0m\xe2\x96\x88\x1b[48;2;0;0;0m\x1b[38;2;255;0;0m'
  >   -  b'\xe2\x96\x88\x1b[48;2;0;0;0m\x1b[38;2;255;0;0m\xe2\x96\x88\x1b[48;2;0;0'...
- *(... 7 more in this cluster)*

### `rc_unexpected_zero` — 7 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `eval.tests.test_help_output.test_separator_double_dash_disables_flag_parsing_for_help_like_arg`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--', '-help'], returncode=0, stdout='#\n-credits\n-d\n-go\n-m\n-nobg\n-s\n-tc\n-tr\n-version\n/ _ \\\\/  _/ |/_/ /____ ______ _\n/_/  /__
- `eval.tests.test_pixterm_cli.test_invalid_terminal_size_is_rejected[args0]`
  > assert 0 != 0
- `eval.tests.test_pixterm_cli.test_invalid_terminal_size_is_rejected[args1]`
  > assert 0 != 0
- *(... 4 more in this cluster)*

### `rc_mismatch_got2_want1` — 4 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_argparse_validation.test_valid_argparse_proceeds_to_runtime_and_fails_opening_file[args2]`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-d', '0', 'foo'], returncode=2, stdout='\x1b[48;2;0;0;0m\x1b[38;2;200;0;0m▓\x1b[48;2;0;0;0m\x1b[38;2;200;0;0m▓\x1b[48;2;0;0;0m\x1b[38;2;0
- `eval.tests.test_argparse_validation.test_valid_argparse_proceeds_to_runtime_and_fails_opening_file[args4]`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-s', '0', 'foo'], returncode=2, stdout='USAGE:\nUSAGE:\nUSAGE:\n', stderr='').returncode
- `eval.tests.test_argparse_validation.test_valid_argparse_proceeds_to_runtime_and_fails_opening_file[args7]`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-m', '000000', 'foo'], returncode=2, stdout='', stderr='').returncode
- *(... 1 more in this cluster)*

### `returned_none` — 3 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_argparse_validation.test_version_flag_prints_only_version_line_and_exit_0`
  > AssertionError: assert None
  >  +  where None = <function fullmatch at 0x7fef95a93e20>('\\d+\\.\\d+\\.\\d+\\n', '1.3.2\nCONTRIBUTORS:\n@disq\n@timob\n@HongjiangHuang\n@brutestack\n@diamondburned\ntransparency support\nCONTRIBUTORS:
  >  +    where <function fullmatch at 0x7fef95a93e20> = re.fullmatch
  >  +    and   '1.3.2\nCONTRIBUTORS:\n@disq\n@timob\n@HongjiangHuang\n@brutestack\n@diamondburned\ntransparency support\nCONTRIBUTORS:\ngithub.com\n' = CompletedProcess(args=['/workspace/executable', '-v
- `eval.tests.test_help_output.test_help_contains_ascii_art_header_lines`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7fdf5e65e680>('^\\s+___', 'USAGE:\nexecutable [options] image/url\nSupported image formats: JPEG, PNG, GIF, BMP, TIFF, WebP\nSupported URL protocols: HTTP, HTTPS
  >  +    where <function search at 0x7fdf5e65e680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- `eval.tests.test_pixterm_cli.test_credits_contains_header_and_a_contributor`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7fbd169fe680>('>\\s+@\\w+\\s+-\\s+https://github.com/', 'CONTRIBUTORS:\ngithub.com\n-credits\n-d mode\n-go\n-m color\n-nobg\n-s method\n-tc columns\n-tr rows\n')
  >  +    where <function search at 0x7fbd169fe680> = re.search

### `rc_mismatch_got1_want2` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_ansimage_api.test_one_terminal_column_rejected`
  > assert 1 == 2
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-tc', '1', '-tr', '10', '/workspace/eval/test_resources/test_rendering_basic/all_black_30x30.png'], returncode=1, stdout=b"   ___  _____ 
- `tests.test_ansimage_api.test_one_terminal_row_rejected`
  > assert 1 == 2
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-tc', '10', '-tr', '1', '/workspace/eval/test_resources/test_rendering_basic/all_black_30x30.png'], returncode=1, stdout=b"   ___  _____ 

