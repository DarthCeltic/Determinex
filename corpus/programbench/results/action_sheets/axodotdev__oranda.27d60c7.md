# Action Sheet — axodotdev__oranda.27d60c7

**Current:** 20.51%  (271/1321)
**Pass / Fail / Skip:** 271 / 700 / 4
**Gap to 100%:** 79.49 percentage points (1050 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_artifact_inference.test_multiple_archive_format_detection_and_labeling`
  - reason: artifacts.json not created, possibly due to API limits
- `tests.test_artifact_inference.test_installer_preference_ordering`
  - reason: artifacts.json not created, possibly due to API limits
- `tests.test_harvest.test_gal_workspace`
  - reason: gal_workspace requires workspace state from other tests - complex orchestration test
- `tests.test_release_data.test_release_page_date_formatting`
  - reason: GitHub API rate limit - release page not generated

## Failure clusters

700 failed tests grouped into 18 buckets (sorted by count).

### `other_assertion` — 467 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_advanced_config.test_build_with_path_prefix`
  > AssertionError: assert b'SUCCESS' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', 'build'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_advanced_config.test_build_with_static_dir`
  > AssertionError: assert b'SUCCESS' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', 'build'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_advanced_config.test_build_with_logo_and_favicon`
  > AssertionError: assert b'SUCCESS' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', 'build'], returncode=0, stdout=b'', stderr=b'').stdout
- *(... 464 more in this cluster)*

### `rc_unexpected_zero` — 40 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_basic_invocation.test_invalid_command`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'nonexistent-command'], returncode=0, stdout=b'Commands:\nBuild an oranda site\n--json-only\n', stderr=b'').returncode
- `tests.test_build_command.test_build_with_invalid_json_config`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'build'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_error_cases.test_serve_requires_public_dir`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'serve'], returncode=0, stdout=b'Start a file server\n', stderr=b'').returncode
- *(... 37 more in this cluster)*

### `boolean_false` — 37 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_hidden_commands.test_config_schema_with_output_file`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmprpi61_ia/schema.json').exists
- `eval.tests.test_help_main.test_help_ends_with_newline`
  > AssertionError: assert False
  >  +  where False = <built-in method endswith of str object at 0x7f266f010030>('\n')
  >  +    where <built-in method endswith of str object at 0x7f266f010030> = ''.endswith
  >  +      where '' = CompletedProcess(args=['/workspace/executable', '--help'], returncode=0, stdout='', stderr='').stdout
- `eval.tests.test_externalized.test_ext_it_adds_oranda_css_with_pinned_version`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = (PosixPath('/tmp/oranda_ext_rjjvxdjk/public') / 'oranda-v0.1.0.css').exists
- *(... 34 more in this cluster)*

### `missing_file` — 33 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_build.test_build_multiple_files_in_static_dir`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmp2px5a5ye/public/static/file1.txt'
- `tests.test_build.test_build_idempotent_workspace`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpriseubhi/public/proj/index.html'
- `tests.test_funding.test_funding_all_platform_types`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpxxadb4iw/public/funding/index.html'
- *(... 30 more in this cluster)*

### `returned_none` — 23 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_basic_invocation.test_version_flag`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f4be5a43760>(b'\\d+\\.\\d+\\.\\d+', b'oranda\noranda\n')
  >  +    where <function search at 0x7f4be5a43760> = re.search
  >  +    and   b'oranda\noranda\n' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'oranda\noranda\n', stderr=b'').stdout
- `tests.test_basic_invocation.test_version_flag_short`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f4be5a43760>(b'\\d+\\.\\d+\\.\\d+', b'oranda\n')
  >  +    where <function search at 0x7f4be5a43760> = re.search
  >  +    and   b'oranda\n' = CompletedProcess(args=['/workspace/executable', '-V'], returncode=0, stdout=b'oranda\n', stderr=b'').stdout
- `tests.test_oranda_comprehensive.test_version_flag`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7fe130bda680>(b'\\d+\\.\\d+\\.\\d+', b'oranda\noranda\n')
  >  +    where <function search at 0x7fe130bda680> = re.search
  >  +    and   b'oranda\noranda\n' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'oranda\noranda\n', stderr=b'').stdout
- *(... 20 more in this cluster)*

### `rc_mismatch_got0_want1` — 18 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_config.test_marketing_analytics_fathom_special_chars_in_site_id`
  > assert 0 == 1
  >  +  where 0 = len([])
- `tests.test_config.test_marketing_analytics_umami_uuid_website_id`
  > assert 0 == 1
  >  +  where 0 = len([])
- `tests.test_config.test_marketing_analytics_plausible_default_script_url`
  > assert 0 == 1
  >  +  where 0 = len([])
- *(... 15 more in this cluster)*

### `rc_mismatch_got2_want0` — 17 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_artifacts.test_build_json_only_creates_artifacts_json`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'build', '--json-only'], returncode=2, stdout=b'', stderr=b'').returncode
- `eval.tests.test_args_parsing.test_verbose_short_and_long_are_equivalent_accept_once`
  > AssertionError: assert 2 == 0
  >  +  where 2 = RunResult(rc=2, out='', err='').rc
- `eval.tests.test_cli_io.test_build_supports_json_only_flag_and_still_creates_public_dir`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'build', '--json-only'], returncode=2, stdout=b'', stderr=b'').returncode
- *(... 14 more in this cluster)*

### `string_output_mismatch` — 15 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_alias_and_precedence.test_help_command_matches_help_flag`
  > AssertionError: assert '' == 'Commands:\nB...--json-only\n'
  >   
  >   - Commands:
  >   - Build an oranda site
  >   - --json-only
- `eval.tests.test_help_baselines.test_help_exact_output_matches_fixture[argv0-main_help.txt]`
  > AssertionError: assert '' == '#x1F381 generate b...JSON output\n'
  >   
  >   - #x1F381 generate beautiful landing pages for your projects
  >   - 
  >   - Usage: executable [OPTIONS] <COMMAND>
  >   - 
  >   - Commands:
  >   -   build     Build an oranda site...
- `eval.tests.test_help_baselines.test_help_exact_output_matches_fixture[argv1-build_help.txt]`
  > AssertionError: assert 'Build an ora...AL OPTIONS:\n' == 'Build an ora...JSON output\n'
  >   
  >     Build an oranda site
  >   - 
  >   - Usage: executable build [OPTIONS]
  >   - 
  >   - Options:
  >   -       --json-only...
- *(... 12 more in this cluster)*

### `uncategorized` — 13 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_build.test_build_with_cargo_toml_extracts_metadata`
  > AttributeError: 'NoneType' object has no attribute 'text'
- `tests.test_build.test_build_with_package_json_extracts_metadata`
  > AttributeError: 'NoneType' object has no attribute 'text'
- `tests.test_build.test_build_with_oranda_json_overrides_config`
  > AttributeError: 'NoneType' object has no attribute 'text'
- *(... 10 more in this cluster)*

### `rc_mismatch_got0_want255` — 9 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_cli_io.test_build_with_invalid_oranda_json_errors_to_stderr_exit_255`
  > AssertionError: assert 0 == 255
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'build'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_build.test_build_workspace_empty_members_list`
  > AssertionError: assert 0 == 255
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'build'], returncode=0, stdout='', stderr='').returncode
- `tests.test_build.test_build_workspace_member_with_missing_path`
  > AssertionError: assert 0 == 255
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'build'], returncode=0, stdout='', stderr='').returncode
- *(... 6 more in this cluster)*

### `rc_mismatch_got1_want2` — 7 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_args_parsing.test_invalid_enum_value_rejected[args1]`
  > assert 1 == 2
  >  +  where 1 = RunResult(rc=1, out='', err="error: [Errno 2] No such file or directory: 'build'\n").rc
- `eval.tests.test_args_parsing.test_output_format_cannot_be_repeated`
  > assert 1 == 2
  >  +  where 1 = RunResult(rc=1, out='', err="error: [Errno 2] No such file or directory: 'build'\n").rc
- `tests.test_subcommand_dispatch.TestUnknownSubcommand.test_various_unknown_subcommands[xyz]`
  > assert 1 == 2
  >  +  where 1 = CompletedProcess(args=['./executable', 'xyz'], returncode=1, stdout=b'', stderr=b"error: [Errno 2] No such file or directory: 'xyz'\n").returncode
- *(... 4 more in this cluster)*

### `json_output_missing_or_bad` — 6 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `tests.test_hidden_commands.test_config_schema_outputs_valid_json`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_hidden_commands.test_config_schema_has_expected_top_level_structure`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_hidden_commands.test_config_schema_definitions_section_exists`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- *(... 3 more in this cluster)*

### `rc_mismatch_got0_want2` — 5 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_basic_invocation.test_no_args_shows_help`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_oranda_comprehensive.test_no_arguments_shows_help`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_argument_parsing.TestBasicCommands.test_no_arguments_shows_usage`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['./executable'], returncode=0, stdout='', stderr='').returncode
- *(... 2 more in this cluster)*

### `rc_mismatch_got0_want4` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_syntax_highlight.test_python_syntax_highlighting`
  > assert 0 == 4
  >  +  where 0 = len([])
- `tests.test_syntax_highlight.test_javascript_syntax_highlighting`
  > assert 0 == 4
  >  +  where 0 = len([])
- `tests.test_syntax_highlight.test_bash_syntax_highlighting`
  > assert 0 == 4
  >  +  where 0 = len([])

### `bytes_output_mismatch` — 2 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_build_command.test_build_json_only_flag`
  > AssertionError: assert (2 == 0 or b'json' in b'' or b'artifact' in b'')
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'build', '--json-only'], returncode=2, stdout=b'', stderr=b'').returncode
  >  +  and   b'' = <built-in method lower of bytes object at 0x7f4be5c44030>()
  >  +    where <built-in method lower of bytes object at 0x7f4be5c44030> = b''.lower
  >  +      where b'' = CompletedProcess(args=['/workspace/executable', 'build', '--json-only'], returncode=2, stdout=b'', stderr=b'').stdout
  >  +  and   b'' = <built-in method lower of bytes object at 0x7f4be5c44030>()
  >  +    where <built-in method lower of bytes object at 0x7f4be5c44030> = b''.lower
  >  +      where b'' = CompletedProcess(args=['/workspace/executable', 'build', '--json-only'], returncode=2, stdout=b'', stderr=b'').stdout
- `tests.test_oranda_comprehensive.test_build_json_only`
  > AssertionError: assert (b'json' in b'' or b'artifact' in b'' or 2 == 0)
  >  +  where b'' = <built-in method lower of bytes object at 0x7fe130c64030>()
  >  +    where <built-in method lower of bytes object at 0x7fe130c64030> = b''.lower
  >  +      where b'' = CompletedProcess(args=['/workspace/executable', 'build', '--json-only'], returncode=2, stdout=b'', stderr=b'').stdout
  >  +  and   b'' = <built-in method lower of bytes object at 0x7fe130c64030>()
  >  +    where <built-in method lower of bytes object at 0x7fe130c64030> = b''.lower
  >  +      where b'' = CompletedProcess(args=['/workspace/executable', 'build', '--json-only'], returncode=2, stdout=b'', stderr=b'').stdout
  >  +  and   2 = CompletedProcess(args=['/workspace/executable', 'build', '--json-only'], returncode=2, stdout=b'', stderr=b'').returncode

### `test_timeout` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_serve.test_serve_default_port`
  > Failed: Server did not start on port 7979 within timeout
- `tests.test_serve.test_serve_custom_port`
  > Failed: Server did not start on port 8081 within timeout

### `rc_mismatch_got2_want255` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_cli.test_generate_ci_requires_tty_and_panics_in_non_tty`
  > AssertionError: assert 2 == 255
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'generate', 'ci', '--ci', 'github', '-o', '/tmp/pytest-of-root/pytest-0/test_generate_ci_requires_tty_2/ci.yml'], returncode=2, stdout='',
- `tests.test_edge_cases.test_generate_ci_without_tty_fails_clearly`
  > AssertionError: assert 2 == 255
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'generate', 'ci'], returncode=2, stdout='', stderr='').returncode

### `empty_list_or_string` — 1 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `eval.tests.test_help_main.test_help_starts_with_tagline`
  > IndexError: list index out of range

