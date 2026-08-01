# Action Sheet — y2z__monolith.8702e66

**Current:** 7.19%  (81/1126)
**Pass / Fail / Skip:** 81 / 526 / 0
**Gap to 100%:** 92.81 percentage points (1045 tests)

## Failure clusters

526 failed tests grouped into 15 buckets (sorted by count).

### `other_assertion` — 326 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_asset_removal.test_no_audio_flag`
  > assert b'Content' in b"style-src 'none'\ndefault-src 'unsafe-eval' 'unsafe-inline' data:;\nframe-src 'none'\n"
  >  +  where b"style-src 'none'\ndefault-src 'unsafe-eval' 'unsafe-inline' data:;\nframe-src 'none'\n" = CompletedProcess(args=['../executable', '-M', '-a', '-'], returncode=0, stdout=b"style-src 'none'\
- `tests.test_asset_removal.test_no_css_flag`
  > assert b'Content' in b"style-src 'none'\ndefault-src 'unsafe-eval' 'unsafe-inline' data:;\nframe-src 'none'\n"
  >  +  where b"style-src 'none'\ndefault-src 'unsafe-eval' 'unsafe-inline' data:;\nframe-src 'none'\n" = CompletedProcess(args=['../executable', '-M', '-c', '-'], returncode=0, stdout=b"style-src 'none'\
- `tests.test_asset_removal.test_no_images_flag`
  > assert b'Content' in b"style-src 'none'\ndefault-src 'unsafe-eval' 'unsafe-inline' data:;\nframe-src 'none'\n"
  >  +  where b"style-src 'none'\ndefault-src 'unsafe-eval' 'unsafe-inline' data:;\nframe-src 'none'\n" = CompletedProcess(args=['../executable', '-M', '-i', '-'], returncode=0, stdout=b"style-src 'none'\
- *(... 323 more in this cluster)*

### `string_output_mismatch` — 63 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_baseline_sanitized.test_help_matches_sanitized_baseline`
  > assert "monolith <VE...-src 'none'\n" == ' _____    __...int version\n'
  >   
  >   -  _____    _____________   __________     ___________________    ___
  >   - |     \  /             \ |          |   |                   |  |   |
  >   - |      \/       __      \|    __    |   |    ___     ___    |__|   |
  >   - |              |  |          |  |   |   |   |   |   |   |          |
  >   - |   |\    /|   |__|          |__|   |___|   |   |   |   |    __    |
  >   - |   | \__/ |          |\                    |   |   |   |   |  |   |...
- `eval.tests.test_monolith_cli.test_version_exact`
  > AssertionError: assert 'monolith 0.1.0\n' == 'monolith 2.11.0\n'
  >   
  >   - monolith 2.11.0
  >   ?          ^ -
  >   + monolith 0.1.0
  >   ?          ^
- `eval.tests.test_monolith_cli.test_help_snapshot`
  > assert "monolith 0.1...-src 'none'\n" == ' _____    __...int version\n'
  >   
  >   + monolith 0.1.0
  >   -  _____    _____________   __________     ___________________    ___
  >   - |     \  /             \ |          |   |                   |  |   |
  >   - |      \/       __      \|    __    |   |    ___     ___    |__|   |
  >   - |              |  |          |  |   |   |   |   |   |   |          |
  >   - |   |\    /|   |__|          |__|   |___|   |   |   |   |    __    |...
- *(... 60 more in this cluster)*

### `returned_none` — 42 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_behavior.test_help_has_arguments_section`
  > assert None
  >  +  where None = <function search at 0x7f20e3276680>('^Arguments:\\s*$', "monolith 0.1.0\n\nusage: monolith [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n 
  >  +    where <function search at 0x7f20e3276680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- `tests.test_assets.test_no_css_flag_removes_css_and_adds_csp`
  > assert None is not None
- `tests.test_assets.test_no_images_flag_replaces_with_empty_image`
  > assert None is not None
- *(... 39 more in this cluster)*

### `boolean_false` — 23 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_output_handling.test_output_to_file`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpog4ypc1o/output.html').exists
- `tests.test_output_handling.test_output_short_flag`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpzo3r5ygw/out.html').exists
- `tests.test_output_handling.test_output_long_flag`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpuo6kd49m/out.html').exists
- *(... 20 more in this cluster)*

### `rc_unexpected_zero` — 18 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_basic_invocation.test_exit_code_failure`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['../executable', 'https://this-domain-definitely-does-not-exist-12345.com'], returncode=0, stdout=b"style-src 'none'\ndefault-src 'unsafe-eval' 'unsafe-inline' dat
- `tests.test_input_handling.test_nonexistent_local_file`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['../executable', '/tmp/this-file-definitely-does-not-exist-xyz123.html'], returncode=0, stdout=b"style-src 'none'\ndefault-src 'unsafe-eval' 'unsafe-inline' data:;
- `tests.test_verbosity.test_error_message_in_verbose`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['../executable', 'https://this-domain-definitely-does-not-exist-xyz123.com'], returncode=0, stdout=b"style-src 'none'\ndefault-src 'unsafe-eval' 'unsafe-inline' da
- *(... 15 more in this cluster)*

### `rc_mismatch_got0_want1` — 17 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_basic_invocation.test_empty_target`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['../executable', ''], returncode=0, stdout=b"style-src 'none'\ndefault-src 'unsafe-eval' 'unsafe-inline' data:;\nframe-src 'none'\n", stderr=b'').returncode
- `tests.test_basic_invocation.test_unsupported_scheme_mailto`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['../executable', 'mailto:test@example.com'], returncode=0, stdout=b"style-src 'none'\ndefault-src 'unsafe-eval' 'unsafe-inline' data:;\nframe-src 'none'\n", stderr
- `tests.test_basic_invocation.test_unsupported_scheme_ftp`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['../executable', 'ftp://ftp.example.com/file.txt'], returncode=0, stdout=b"style-src 'none'\ndefault-src 'unsafe-eval' 'unsafe-inline' data:;\nframe-src 'none'\n",
- *(... 14 more in this cluster)*

### `rc_mismatch_got0_want2` — 15 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_cache_cli.test_cache_mixed_sizes`
  > assert 0 == 2
  >  +  where 0 = len([])
- `tests.test_cache_cli.test_cache_empty_file`
  > assert 0 == 2
  >  +  where 0 = len([])
- `tests.test_cache_cli.test_cache_with_different_resources`
  > assert 0 == 2
  >  +  where 0 = len([])
- *(... 12 more in this cluster)*

### `uncategorized` — 11 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_favicon.test_local_file_without_favicon_no_auto_fetch`
  > AttributeError: 'NoneType' object has no attribute 'text'
- `tests.test_favicon.test_html_with_explicit_favicon_no_auto_fetch`
  > AttributeError: 'NoneType' object has no attribute 'text'
- `tests.test_favicon.test_no_images_flag_prevents_favicon_auto_fetch`
  > AttributeError: 'NoneType' object has no attribute 'text'
- *(... 8 more in this cluster)*

### `rc_mismatch_got0_want3` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_css_edge.test_empty_url_variations_all_normalized`
  > assert 0 == 3
  >  +  where 0 = <built-in method count of str object at 0x7f8ee22d3750>('url()')
  >  +    where <built-in method count of str object at 0x7f8ee22d3750> = "style-src 'none'\ndefault-src 'unsafe-eval' 'unsafe-inline' data:;\nframe-src 'none'\n".count
- `tests.test_html_advanced.test_anchor_relative_href_resolved`
  > assert 0 == 3
  >  +  where 0 = len([])
- `tests.test_html_advanced.test_area_href_resolution`
  > assert 0 == 3
  >  +  where 0 = len([])

### `rc_mismatch_got2_want0` — 2 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_isolation_and_metadata.test_no_metadata_long_flag`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['../executable', '--no-metadata', '-'], returncode=2, stdout=b'', stderr=b'monolith: error: unrecognized argument: --no-metadata\n').returncode
- `tests.test_core_edge.test_no_metadata_with_custom_encoding`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--no-metadata', '-E', 'iso-8859-1', '/tmp/tmpgc2cepzq.html'], returncode=2, stdout=b'', stderr=b'monolith: error: unrecognized argument: 

### `rc_mismatch_got2_want1` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_argparse_validation.test_dash_dash_makes_next_token_positional_not_flag`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--', '-q'], returncode=2, stdout='', stderr='monolith: error: unrecognized argument: --\n').returncode
- `eval.tests.test_help_behavior.test_double_dash_makes_help_treated_as_target_and_errors`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--', '--help'], returncode=2, stdout='', stderr='monolith: error: unrecognized argument: --\n').returncode

### `rc_mismatch_got0_want101` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_operations.test_invalid_output_path_panics`
  > assert 0 == 101
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-M', '-o', '/nonexistent/directory/output.html', '/workspace/eval/test_resources/test_cli_operations/simple.html'], returncode=0, stdout=

### `rc_mismatch_got0_want10` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_css_edge.test_all_image_url_properties_replaced_with_no_images`
  > assert 0 == 10
  >  +  where 0 = <built-in method count of str object at 0x7f8ee22ffcf0>('data:image/png,%89PNG')
  >  +    where <built-in method count of str object at 0x7f8ee22ffcf0> = "style-src 'none'\ndefault-src 'unsafe-eval' 'unsafe-inline' data:;\nframe-src 'none'\n".count

### `rc_mismatch_got0_want8` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_css_edge.test_counter_style_image_props_replaced_with_no_images`
  > assert 0 == 8
  >  +  where 0 = <built-in method count of str object at 0x7f8ee27e60d0>('data:image/png,%89PNG')
  >  +    where <built-in method count of str object at 0x7f8ee27e60d0> = "style-src 'none'\ndefault-src 'unsafe-eval' 'unsafe-inline' data:;\nframe-src 'none'\n".count

### `rc_mismatch_got0_want100` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_encoding_edge_cases.test_deeply_nested_elements`
  > assert 0 == 100
  >  +  where 0 = <built-in method count of str object at 0x7f8ee2816ee0>('<div>')
  >  +    where <built-in method count of str object at 0x7f8ee2816ee0> = "style-src 'none'\ndefault-src 'unsafe-eval' 'unsafe-inline' data:;\nframe-src 'none'\n".count

