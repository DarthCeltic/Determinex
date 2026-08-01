# Action Sheet — altdesktop__i3-style.f93821b

**Current:** 19.77%  (190/961)
**Pass / Fail / Skip:** 190 / 560 / 0
**Gap to 100%:** 80.23 percentage points (771 tests)

## Failure clusters

560 failed tests grouped into 14 buckets (sorted by count).

### `other_assertion` — 303 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_i3_style.test_list_all_flag_short`
  > AssertionError: assert b'Available themes:' in b'archlinux: Theme by Valentin Weber inspired by voronianski\nsolarized: Tomorrow Night 80s theme by jmfurlott\n'
  >  +  where b'archlinux: Theme by Valentin Weber inspired by voronianski\nsolarized: Tomorrow Night 80s theme by jmfurlott\n' = CompletedProcess(args=['./executable', '-l'], returncode=0, stdout=b'archl
- `tests.test_i3_style.test_list_all_flag_long`
  > AssertionError: assert b'Available themes:' in b'archlinux: Theme by Valentin Weber inspired by voronianski\nsolarized: Tomorrow Night 80s theme by jmfurlott\n'
  >  +  where b'archlinux: Theme by Valentin Weber inspired by voronianski\nsolarized: Tomorrow Night 80s theme by jmfurlott\n' = CompletedProcess(args=['./executable', '--list-all'], returncode=0, stdout
- `tests.test_i3_style.test_list_all_shows_all_builtin_themes`
  > AssertionError: assert b'deep-purple' in b'archlinux: Theme by Valentin Weber inspired by voronianski\nsolarized: Tomorrow Night 80s theme by jmfurlott\n'
  >  +  where b'deep-purple' = <built-in method encode of str object at 0x7f2a354398b0>()
  >  +    where <built-in method encode of str object at 0x7f2a354398b0> = 'deep-purple'.encode
  >  +  and   b'archlinux: Theme by Valentin Weber inspired by voronianski\nsolarized: Tomorrow Night 80s theme by jmfurlott\n' = CompletedProcess(args=['./executable', '--list-all'], returncode=0, stdout
- *(... 300 more in this cluster)*

### `rc_mismatch_got1_want0` — 114 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_i3_style.test_custom_theme_from_file`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', './test-resources/test-theme.yaml', '-c', './test-resources/minimal-config', '-o', '/tmp/tmp32iaf9yu/output'], returncode=1, stdout=b'', stderr=b'C
- `tests.test_i3_style.test_custom_config_with_c_flag`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', './test-resources/test-theme.yaml', '-c', './test-resources/minimal-config', '-o', '/tmp/tmpni67wr_k/output'], returncode=1, stdout=b'', stderr=b'C
- `tests.test_i3_style.test_custom_config_with_config_flag`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', './test-resources/test-theme.yaml', '--config', './test-resources/minimal-config', '-o', '/tmp/tmpsf3mvb1v/output'], returncode=1, stdout=b'', stde
- *(... 111 more in this cluster)*

### `rc_mismatch_got2_want1` — 65 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_i3_style.test_no_arguments_shows_help`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['./executable'], returncode=2, stdout=b'', stderr=b'USAGE:\n    i3-style [FLAGS] [OPTIONS] [<theme>]\n\nFor more information try --help\n').returncode
- `tests.test_i3_style.test_no_theme_with_flags_error`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['./executable', '-c', 'somefile'], returncode=2, stdout=b'', stderr=b'error: No theme specified\n').returncode
- `tests.test_basic_invocation.test_no_arguments_shows_usage`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b'USAGE:\n    i3-style [FLAGS] [OPTIONS] [<theme>]\n\nFor more information try --help\n').returncode
- *(... 62 more in this cluster)*

### `string_output_mismatch` — 27 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_theme_application.TestApplyBuiltinTheme.test_apply_solarized_to_minimal_config`
  > AssertionError: assert '#\n# Tomorro...und #002b36\n' == '# test templ...6e3 #dc322f\n'
  >   
  >   + #
  >   + # Tomorrow Night 80s theme by jmfurlott
  >   + #
  >   - # test templating with a minimal config
  >   - font pango:Fira Mono 8
  >   - ...
- `tests.test_auxiliary.test_list_all_exact_output`
  > AssertionError: assert 'archlinux: T...y jmfurlott\n' == '\nAvailable ...3 into MATE\n'
  >   
  >   + archlinux: Theme by Valentin Weber inspired by voronianski
  >   + solarized: Tomorrow Night 80s theme by jmfurlott
  >   - 
  >   - Available themes:
  >   - 
  >   -   slate              - Slate theme by Jody Ribton <jody@ribton.me>...
- `tests.test_auxiliary.test_to_theme_exact_output`
  > assert '{\n  "backgr...m theme"\n}\n' == '---\nmeta:\n...umvioletred\n'
  >   
  >   + {
  >   +   "background": "#002b36",
  >   - ---
  >   - meta:
  >   -   description: AUTOMATICALLY GENERATED THEME
  >   - colors:...
- *(... 24 more in this cluster)*

### `rc_mismatch_got0_want1` — 16 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_error_handling.test_to_theme_invalid_config`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--to-theme', '/tmp/tmp9_njd2xr/config'], returncode=0, stdout=b'{\n  "background": "#000000",\n  "bar_colors": {},\n  "border": "#000000"
- `tests.test_argument_parsing.TestOutputFlag.test_output_flag_with_space_separator`
  > assert 0 == 1
- `tests.test_argument_parsing.TestOutputFlag.test_output_short_flag_with_space`
  > assert 0 == 1
- *(... 13 more in this cluster)*

### `rc_mismatch_got2_want0` — 12 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_i3_style.test_to_theme_with_config_flag`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--to-theme', '', '-c', './test-resources/minimal-config'], returncode=2, stdout=b'', stderr=b'error: No theme specified\n').returncode
- `tests.test_config_to_theme.test_to_theme_with_config_flag`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-t', '', '-c', '/tmp/tmpv9fg2qqf/config'], returncode=2, stdout=b'', stderr=b'error: No theme specified\n').returncode
- `tests.test_argument_parsing.TestCombinedShortFlags.test_version_and_list_combined`
  > assert 2 == 0
- *(... 9 more in this cluster)*

### `rc_unexpected_zero` — 9 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_env_and_config.TestHomeEnvironment.test_home_unset_behavior`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'solarized'], returncode=0, stdout=b'#\n# Tomorrow Night 80s theme by jmfurlott\n#\n\nbar {\n    colors {\n        background #002b36\n        stat
- `tests.test_env_and_config.TestConfigFileFlag.test_config_flag_nonexistent_file`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'solarized', '-c', '/nonexistent/config/file', '-o', '/tmp/output.txt'], returncode=0, stdout=b'#\n# Tomorrow Night 80s theme by jmfurlott\n#\n\nba
- `tests.test_basic_functionality.TestExitCodes.test_theme_without_config_when_no_default`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'solarized'], returncode=0, stdout=b'#\n# Tomorrow Night 80s theme by jmfurlott\n#\n\nbar {\n    colors {\n        background #002b36\n   
- *(... 6 more in this cluster)*

### `rc_mismatch_got1_want101` — 4 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_edge.test_unicode_config_path_panics`
  > AssertionError: assert 1 == 101
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-c', 'café', 'slate'], returncode=1, stdout='', stderr='Could not find theme: slate\n').returncode
- `tests.test_cli_edge.test_empty_string_config_path_panics`
  > AssertionError: assert 1 == 101
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-c', '', 'slate'], returncode=1, stdout='', stderr='Could not find theme: slate\n').returncode
- `tests.test_cli_edge.test_whitespace_only_config_path_panics`
  > AssertionError: assert 1 == 101
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-c', '   ', 'slate'], returncode=1, stdout='', stderr='Could not find theme: slate\n').returncode
- *(... 1 more in this cluster)*

### `missing_dict_key` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_theme_application.test_to_theme_flag`
  > KeyError: 'background'
- `tests.test_theme_parsing.test_extract_theme_preserves_all_color_groups`
  > KeyError: 'window_colors'
- `tests.test_theme_parsing.test_extract_theme_from_config_with_4_param_client`
  > KeyError: 'window_colors'

### `bytes_output_mismatch` — 2 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_i3_style.test_version_flag_short`
  > AssertionError: assert b'i3-style 0.1.0' == b'i3-style 1.0'
  >   
  >   At index 9 diff: b'0' != b'1'
  >   
  >   Full diff:
  >   - (b'i3-style 1.0')
  >   + (b'i3-style 0.1.0')
  >   ?             ++
- `eval.tests.test_cli_basics.test_help_exact`
  > AssertionError: assert b'i3-style 0....y jmfurlott\n' == b'i3-style 1....heme to use\n'
  >   
  >   At index 9 diff: b'0' != b'1'
  >   
  >   Full diff:
  >   - (b'i3-style 1.0\nMake your i3 config a bit more stylish\n\nUSAGE:\n    executab'
  >   ?                                                                        ^^^^^ ^^
  >   + (b'i3-style 0.1.0\nMake your i3 config a bit more stylish\n\nUSAGE:\n    i3-sty'...

### `boolean_false` — 2 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_i3_style.test_reload_flag_creates_output_first`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpzs8_890i/output').exists
  >  +      where PosixPath('/tmp/tmpzs8_890i/output') = Path('/tmp/tmpzs8_890i/output')
- `eval.tests.test_to_theme.test_to_theme_prints_yaml_to_stdout`
  > assert False
  >  +  where False = <built-in method startswith of bytes object at 0x7f08177bb560>(b'---\n')
  >  +    where <built-in method startswith of bytes object at 0x7f08177bb560> = b'{\n  "background": "#002b36",\n  "bar_colors": {},\n  "border": "#000000",\n  "colors": {\n    "client.focused": "#859900
  >  +      where b'{\n  "background": "#002b36",\n  "bar_colors": {},\n  "border": "#000000",\n  "colors": {\n    "client.focused": "#859900 #859900 #fdf6e3",\n    "client.focused_inactive": "#073642 #07

### `rc_mismatch_got1_want2` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_complex_configs.test_config_with_multiple_bars`
  > AssertionError: assert 1 == 2
  >  +  where 1 = <built-in method count of str object at 0x55996d306d80>('colors {')
  >  +    where <built-in method count of str object at 0x55996d306d80> = '#\n# Tomorrow Night 80s theme by jmfurlott\n#\n\nbar {\n    colors {\n        background #002b36\n        statusline #ffffff\n   

### `rc_mismatch_got0_want19` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_auxiliary.test_list_all_includes_descriptions`
  > assert 0 == 19
  >  +  where 0 = len([])

### `empty_list_or_string` — 1 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_auxiliary.test_list_all_slate_first`
  > IndexError: list index out of range

