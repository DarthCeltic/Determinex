# Action Sheet — ast-grep__ast-grep.dde0fe0

**Current:** 1.38%  (17/1232)
**Pass / Fail / Skip:** 17 / 333 / 0
**Gap to 100%:** 98.62 percentage points (1215 tests)

## Failure clusters

333 failed tests grouped into 11 buckets (sorted by count).

### `other_assertion` — 164 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_completions.test_invalid_shell_name_error`
  > AssertionError: should exit with code 2 for invalid argument, got 0
  > assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'completions', 'invalid-shell'], returncode=0, stdout='[]\n', stderr='').returncode
- `tests.test_completions.test_no_shell_argument_no_env_fails`
  > AssertionError: should exit with code 10 when shell cannot be inferred, got 0
  > assert 0 == 10
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'completions'], returncode=0, stdout='[\n  {\n    "text": "completions",\n    "file": "test_resources/test_completions/bash.golden",\n    
- `tests.test_config_validation.test_json_output_includes_fix_replacement_fields`
  > AssertionError: JSON output differs from golden
  > assert [] == [{'charCount'...Script', ...}]
  >   
  >   Right contains 2 more items, first extra item: {'charCount': {'leading': 0, 'trailing': 0}, 'file': '/tmp/json_fix_test.js', 'labels': [{'range': {'byteOffset': {'en...ne': 0}, 'start': {'column': 0
  >   
  >   Full diff:
  >   + []
  >   - [
- *(... 161 more in this cluster)*

### `string_output_mismatch` — 102 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_completions.test_bash_completions_exact_golden`
  > assert '[]\n' == '_executable(...cutable\nfi\n'
  >   
  >   + []
  >   - _executable() {
  >   -     local i cur prev opts cmd
  >   -     COMPREPLY=()
  >   -     if [[ "${BASH_VERSINFO[0]}" -ge 4 ]]; then
  >   -         cur="$2"...
- `tests.test_completions.test_zsh_completions_exact_golden`
  > AssertionError: assert '[]\n' == '#compdef exe...cutable\nfi\n'
  >   
  >   + []
  >   - #compdef executable
  >   - 
  >   - autoload -U is-at-least
  >   - 
  >   - _executable() {...
- `tests.test_completions.test_fish_completions_exact_golden`
  > assert '[]\n' == "# Print an o...ility rule'\n"
  >   
  >   + []
  >   - # Print an optspec for argparse to handle cmd's options that are independent of any subcommand.
  >   - function __fish_executable_global_optspecs
  >   - 	string join \n c/config= h/help V/version
  >   - end
  >   - ...
- *(... 99 more in this cluster)*

### `rc_unexpected_zero` — 27 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_config_validation.test_undefined_metavar_in_fix_section`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'scan', '--rule', '/tmp/pytest-of-root/pytest-0/test_undefined_metavar_in_fix_2/rule.yml', '/tmp/pytest-of-root/pytest-0/test_undefined_me
- `tests.test_config_validation.test_undefined_metavar_in_constraints_section`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'scan', '--rule', '/tmp/pytest-of-root/pytest-0/test_undefined_metavar_in_cons2/rule.yml', '/tmp/pytest-of-root/pytest-0/test_undefined_me
- `tests.test_config_validation.test_undefined_metavar_in_transform_section`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'scan', '--rule', '/tmp/pytest-of-root/pytest-0/test_undefined_metavar_in_tran2/rule.yml', '/tmp/pytest-of-root/pytest-0/test_undefined_me
- *(... 24 more in this cluster)*

### `boolean_false` — 16 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_debug_query.test_debug_query_sexp_var_decl`
  > assert False
  >  +  where False = <built-in method startswith of str object at 0x7f269c53ca80>('Debug Sexp:')
  >  +    where <built-in method startswith of str object at 0x7f269c53ca80> = "ast-grep: unknown option: --debug-query=sexp\nusage: ast-grep [OPTIONS] [ARGS]\nTry 'ast-grep --help' for more information."
- `tests.test_debug_query.test_debug_query_default_format`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7f269e4d8030>('Debug Pattern:')
  >  +    where <built-in method startswith of str object at 0x7f269e4d8030> = ''.startswith
- `tests.test_debug_query.test_debug_query_pattern_empty_body`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7f269e4d8030>('Debug Pattern:')
  >  +    where <built-in method startswith of str object at 0x7f269e4d8030> = ''.startswith
- *(... 13 more in this cluster)*

### `rc_mismatch_got0_want2` — 8 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_config_validation.test_fix_with_transform_applies_transformation`
  > assert 0 == 2
  >  +  where 0 = len([])
- `tests.test_config_validation.test_utils_define_metavars_available_in_fix`
  > assert 0 == 2
  >  +  where 0 = len([])
- `tests.test_custom_languages.test_custom_language_file_type_detection`
  > assert 0 == 2
  >  +  where 0 = len([])
- *(... 5 more in this cluster)*

### `rc_mismatch_got0_want1` — 7 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_config_validation.test_nested_transform_depends_on_another_transform`
  > assert 0 == 1
  >  +  where 0 = len([])
- `tests.test_injection.test_injection_without_content_capture_skips_region`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'run', '-c', '/workspace/eval/test_resources/test_injection/sgconfig_no_content.yml', '-p', '.btn', '-l', 'css', '/workspace/eval/test_res
- `tests.test_injection.test_dynamic_injection_without_lang_capture_skips`
  > assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'run', '-c', '/workspace/eval/test_resources/test_injection/sgconfig_dynamic_no_default.yml', '-p', '.test', '-l', 'css', '/workspace/eval
- *(... 4 more in this cluster)*

### `rc_mismatch_got0_want3` — 4 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_custom_languages.test_custom_language_multiple_extensions`
  > assert 0 == 3
  >  +  where 0 = len([])
- `tests.test_injection.test_scan_json_output_with_injection`
  > assert 0 == 3
  >  +  where 0 = len([])
- `tests.test_multiple_fixers.test_json_replacement_from_first_fixer_only`
  > assert 0 == 3
  >  +  where 0 = len([])
- *(... 1 more in this cluster)*

### `missing_file` — 2 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_new.test_new_project_sgconfig_structure`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_new_project_sgconfig_stru2/sgconfig.yml'
- `tests.test_new.test_new_project_creates_absolute_paths_in_config`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_new_project_creates_absol2/sgconfig.yml'

### `rc_mismatch_got0_want4` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_custom_languages.test_custom_language_metavar_char_configuration`
  > assert 0 == 4
  >  +  where 0 = len([])

### `rc_mismatch_got1_want2` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_multiple_fixers.test_multiple_fixers_json_stream_format`
  > AssertionError: assert 1 == 2
  >  +  where 1 = len(['[]'])

### `rc_mismatch_got0_want8` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_multiple_fixers.test_multiple_fixers_without_title_rejected`
  > AssertionError: assert 0 == 8
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'scan', '-r', '/workspace/eval/test_resources/test_multiple_fixers/rule_no_title.yml', '/workspace/eval/test_resources/test_multiple_fixer

