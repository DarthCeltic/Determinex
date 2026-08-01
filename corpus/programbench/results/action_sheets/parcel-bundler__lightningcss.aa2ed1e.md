# Action Sheet — parcel-bundler__lightningcss.aa2ed1e

**Current:** 0.87%  (32/3666)
**Pass / Fail / Skip:** 32 / 862 / 4
**Gap to 100%:** 99.13 percentage points (3634 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_cli_basic.test_version_exact_golden`
  - reason: test_version_exact_golden depends on test_help_exact_golden
- `eval.tests.test_css_modules_and_bundle.test_css_modules_output_file_and_default_exports_json`
  - reason: test_css_modules_output_file_and_default_exports_json depends on test_css_modules_stdout_json_when_no_output_file
- `eval.tests.test_minify_and_files.test_output_file_writes_and_stdout_empty`
  - reason: test_output_file_writes_and_stdout_empty depends on test_minify_from_stdin_basic
- `eval.tests.test_minify_and_files.test_sourcemap_creates_valid_json`
  - reason: test_sourcemap_creates_valid_json depends on test_output_file_writes_and_stdout_empty

## Failure clusters

862 failed tests grouped into 9 buckets (sorted by count).

### `rc_mismatch_got2_want0` — 405 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_advanced_features.test_counter_style`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b'usage: lightningcss [OPTIONS] [ARGS]\n').returncode
- `tests.test_advanced_features.test_font_face`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b'usage: lightningcss [OPTIONS] [ARGS]\n').returncode
- `tests.test_advanced_features.test_font_feature_values`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b'usage: lightningcss [OPTIONS] [ARGS]\n').returncode
- *(... 402 more in this cluster)*

### `other_assertion` — 248 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_advanced_features.test_nested_css`
  > AssertionError: assert b'parent' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', '-t', 'chrome 80'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_advanced_features.test_dir_lang_selectors`
  > AssertionError: assert (b'lang' in b'' or b'dir' in b'' or b'direction' in b'')
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', '-t', 'chrome 80'], returncode=0, stdout=b'', stderr=b'').stdout
  >  +  and   b'' = CompletedProcess(args=['/workspace/executable', '-t', 'chrome 80'], returncode=0, stdout=b'', stderr=b'').stdout
  >  +  and   b'' = CompletedProcess(args=['/workspace/executable', '-t', 'chrome 80'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_basic.test_help_flag`
  > AssertionError: assert b'USAGE:' in b'lightningcss 0.1.0\n\nusage: lightningcss [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --verbose  Verbose\n  -
  >  +  where b'lightningcss 0.1.0\n\nusage: lightningcss [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n  -v, --verbose  Verbose\n  -q, --quiet    Quiet\n\n' =
- *(... 245 more in this cluster)*

### `string_output_mismatch` — 167 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_advanced_css.test_pseudo_classes_and_elements`
  > AssertionError: assert '' == 'a:hover {\n ... #00f;\n}\n\n'
  >   
  >   - a:hover {
  >   -   color: red;
  >   - }
  >   - 
  >   - li:nth-child(odd) {
  >   -   background: gray;...
- `tests.test_advanced_css.test_attribute_selectors_all_operators`
  > assert '' == '[data-type] ...green;\n}\n\n'
  >   
  >   - [data-type] {
  >   -   color: #00f;
  >   - }
  >   - 
  >   - [data-type="primary"] {
  >   -   font-weight: bold;...
- `tests.test_advanced_css.test_complex_selector_combinators`
  > AssertionError: assert '' == 'div > p {\n ... #00f;\n}\n\n'
  >   
  >   - div > p {
  >   -   margin-top: 10px;
  >   - }
  >   - 
  >   - h1 + p {
  >   -   font-size: 18px;...
- *(... 164 more in this cluster)*

### `missing_file` — 15 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_cli_combinations.test_minify_with_sourcemap`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpg45m4rar/out.css'
- `tests.test_cli_combinations.test_targets_with_sourcemap`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpyok77e6c/output.css'
- `tests.test_cli_combinations.test_css_modules_with_minify`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmp6jbkn604/output.css'
- *(... 12 more in this cluster)*

### `boolean_false` — 15 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_cli_combinations.test_all_flags_combined`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmp3ce4w3dw/output.css').exists
- `tests.test_cli_combinations.test_multiple_files_with_all_options`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = (PosixPath('/tmp/tmpkufyrmaw/out') / 'file1.css').exists
- `tests.test_css_modules.test_css_modules_basic`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmp6l30el28/output.json').exists
- *(... 12 more in this cluster)*

### `rc_unexpected_zero` — 7 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_bundling.test_bundle_missing_import`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/tmp/tmp96f94j4i/main.css', '--bundle'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_atrules_edge.test_import_after_style_rule_error`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '/workspace/eval/test_resources/test_atrules_edge/import_after_rule.css'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_atrules_edge.test_namespace_after_style_rule_error`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', '/workspace/eval/test_resources/test_atrules_edge/namespace_after_rule.css'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 4 more in this cluster)*

### `bytes_output_mismatch` — 2 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `eval.tests.test_minify_and_files.test_input_file_argument_pretty_printed`
  > AssertionError: assert b'' == b'a {\n  color: red;\n}\n\n'
  >   
  >   Full diff:
  >   - (b'a {\n  color: red;\n}\n\n')
  >   + b''
- `tests.test_lightningcss.test_exact_version_output`
  > AssertionError: assert b'lightningcss 0.1.0\n' == b'lightningcs....0-alpha.70\n'
  >   
  >   At index 13 diff: b'0' != b'1'
  >   
  >   Full diff:
  >   - (b'lightningcss 1.0.0-alpha.70\n')
  >   ?                   -----------
  >   + (b'lightningcss 0.1.0\n')

### `json_output_missing_or_bad` — 2 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `tests.test_cli_externalized.test_ext_css_modules_stdout_outputs_json_with_code_and_exports`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_cli_externalized.test_ext_css_modules_pattern_affects_generated_class_names`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

### `returned_none` — 1 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_content.test_help_usage_mentions_executable_name`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f9c74fb2680>('^\\s*executable\\b', 'lightningcss 0.1.0\n\nusage: lightningcss [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print 
  >  +    where <function search at 0x7f9c74fb2680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE

