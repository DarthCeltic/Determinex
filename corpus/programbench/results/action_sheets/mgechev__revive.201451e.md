# Action Sheet — mgechev__revive.201451e

**Current:** 5.23%  (49/937)
**Pass / Fail / Skip:** 49 / 548 / 0
**Gap to 100%:** 94.77 percentage points (888 tests)

## Failure clusters

548 failed tests grouped into 14 buckets (sorted by count).

### `rc_mismatch_got2_want0` — 289 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_basic_invocation.test_version_flag`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-version'], returncode=2, stdout=b'', stderr=b"revive: unknown option: -version\nusage: revive [OPTIONS] [ARGS]\nTry 'revive --help' for 
- `tests.test_basic_invocation.test_no_args_with_no_go_files`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b"usage: revive [OPTIONS] [ARGS]\nTry 'revive --help' for more information.\n").returncode
- `tests.test_basic_invocation.test_version_output_format`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-version'], returncode=2, stdout=b'', stderr=b"revive: unknown option: -version\nusage: revive [OPTIONS] [ARGS]\nTry 'revive --help' for 
- *(... 286 more in this cluster)*

### `other_assertion` — 175 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_additional_rules.test_add_constant_rule`
  > assert 2 in [0, 1]
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-config', '/tmp/tmp0dkmmfp9/config.toml', '/tmp/tmp0dkmmfp9/test.go'], returncode=2, stdout=b'', stderr=b"revive: unknown option: -config
- `tests.test_additional_rules.test_cognitive_complexity_rule`
  > assert 2 in [0, 1]
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-config', '/tmp/tmpxe5jk9u2/config.toml', '/tmp/tmpxe5jk9u2/complex.go'], returncode=2, stdout=b'', stderr=b"revive: unknown option: -con
- `tests.test_additional_rules.test_banned_characters_rule`
  > assert 2 in [0, 1]
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-config', '/tmp/tmpaoy7zmsq/config.toml', '/tmp/tmpaoy7zmsq/test.go'], returncode=2, stdout=b'', stderr=b"revive: unknown option: -config
- *(... 172 more in this cluster)*

### `rc_mismatch_got2_want1` — 47 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_flags.test_set_exit_status_with_issues`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-set_exit_status', '/tmp/tmp9ykopzrs/test.go'], returncode=2, stdout=b'', stderr=b"revive: unknown option: -set_exit_status\nusage: reviv
- `tests.test_flags.test_config_and_set_exit_status`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-config', '/tmp/tmpuiwxm7s9/config.toml', '-set_exit_status', '/tmp/tmpuiwxm7s9/test.go'], returncode=2, stdout=b'', stderr=b"revive: unk
- `eval.tests.test_revive_io.test_formatter_json_outputs_valid_json_array_and_exit_one`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-formatter', 'json', '/tmp/pytest-of-root/pytest-0/test_formatter_json_outputs_va2/p/bad.go'], returncode=2, stdout=b'', stderr=b"revive:
- *(... 44 more in this cluster)*

### `rc_mismatch_got1_want0` — 20 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_environment.test_empty_directory`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '/tmp/tmpl_az06bd'], returncode=1, stdout=b'Linting results here...\n', stderr=b'').returncode
- `tests.test_cli.test_exit_status_without_issues`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '/tmp/tmpc2swai1g.go'], returncode=1, stdout=b'Linting results here...\n', stderr=b'').returncode
- `tests.test_cli.test_non_go_file_error`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '/tmp/tmpplosazyx/notgo.txt'], returncode=1, stdout=b'Linting results here...\n', stderr=b'').returncode
- *(... 17 more in this cluster)*

### `string_output_mismatch` — 5 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_configuration.test_config_enable_specific_rules`
  > assert ('exported' in '' or 'package' in '' or 2 == 0)
  >  +  where '' = <built-in method lower of str object at 0x7fc256064030>()
  >  +    where <built-in method lower of str object at 0x7fc256064030> = ''.lower
  >  +  and   '' = <built-in method lower of str object at 0x7fc256064030>()
  >  +    where <built-in method lower of str object at 0x7fc256064030> = ''.lower
  >  +  and   2 = CompletedProcess(args=['/workspace/executable', '-config', '/tmp/tmpasiaym2r/specific.toml', '/tmp/tmpasiaym2r/test.go'], returncode=2, stdout=b'', stderr=b"revive: unknown option: -conf
- `tests.test_input_handling.test_directory_pattern`
  > AssertionError: assert ('test.go' in 'Linting results here...\n' or 1 == 0)
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', './...'], returncode=1, stdout=b'Linting results here...\n', stderr=b'').returncode
- `tests.test_rules.test_cyclomatic_complexity_rule`
  > assert ('cyclomatic' in '' or 'complexity' in '' or 2 == 0)
  >  +  where '' = <built-in method lower of str object at 0x7fc256064030>()
  >  +    where <built-in method lower of str object at 0x7fc256064030> = ''.lower
  >  +  and   '' = <built-in method lower of str object at 0x7fc256064030>()
  >  +    where <built-in method lower of str object at 0x7fc256064030> = ''.lower
  >  +  and   2 = CompletedProcess(args=['/workspace/executable', '-config', '/tmp/tmp5p79vpth/config.toml', '/tmp/tmp5p79vpth/complex.go'], returncode=2, stdout=b'', stderr=b"revive: unknown option: -con
- *(... 2 more in this cluster)*

### `json_output_missing_or_bad` — 3 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `tests.test_cli.test_complex_go_file_json_output`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_cli.test_severity_levels_in_output`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_file_processing.test_empty_directory_handling`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

### `boolean_false` — 2 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_environment.test_concurrent_execution`
  > assert False
  >  +  where False = all(<generator object test_concurrent_execution.<locals>.<genexpr> at 0x7fc2540ee030>)
- `eval.tests.test_revive_io.test_lint_single_file_emits_issue_on_stdout_and_exit_one`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7f9ff9ec3370>(('/tmp/pytest-of-root/pytest-0/test_lint_single_file_emits_is2/p/bad.go' + ':1:1: '))
  >  +    where <built-in method startswith of str object at 0x7f9ff9ec3370> = 'Linting results here...\n'.startswith
  >  +    and   '/tmp/pytest-of-root/pytest-0/test_lint_single_file_emits_is2/p/bad.go' = str(PosixPath('/tmp/pytest-of-root/pytest-0/test_lint_single_file_emits_is2/p/bad.go'))

### `returned_none` — 1 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_behavior.test_help_documents_default_config_value`
  > assert None
  >  +  where None = <function search at 0x7f4663ece680>('\\(default \\"revive\\.toml\\"\\)', '')
  >  +    where <function search at 0x7f4663ece680> = re.search
  >  +    and   '' = ExecResult(returncode=0, stdout='revive 0.1.0\n\nUsage: revive [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n', stderr='').stderr

### `rc_mismatch_got1_want5` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli.test_xdg_config_home_discovery`
  > AssertionError: assert 1 == 5
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '/tmp/tmphraj9005.go'], returncode=1, stdout=b'Linting results here...\n', stderr=b'').returncode

### `rc_mismatch_got1_want7` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli.test_home_config_discovery`
  > AssertionError: assert 1 == 7
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '/tmp/tmpyll3std4.go'], returncode=1, stdout=b'Linting results here...\n', stderr=b'').returncode

### `rc_mismatch_got2_want9` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli.test_config_flag_overrides_discovery`
  > assert 2 == 9
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-config', '/tmp/tmpmh1zft73/explicit.toml', '/tmp/tmp0fxwebej.go'], returncode=2, stdout=b'', stderr=b"revive: unknown option: -config\nu

### `rc_mismatch_got2_want5` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_config.test_error_exit_code_without_set_exit_status`
  > assert 2 == 5
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-config', '/workspace/eval/test_resources/test_config/exit_codes.toml', '/workspace/eval/test_resources/test_config/sample.go'], returnco

### `rc_mismatch_got2_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_config.test_warning_exit_code_without_set_exit_status`
  > assert 2 == 3
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-config', '/workspace/eval/test_resources/test_config/warning_code.toml', '/workspace/eval/test_resources/test_config/sample.go'], return

### `uncategorized` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_file_processing.test_nonexistent_file_handling`
  > Failed: Output is not valid JSON when processing nonexistent file

