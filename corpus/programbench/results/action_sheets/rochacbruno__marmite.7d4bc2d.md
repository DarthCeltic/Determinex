# Action Sheet — rochacbruno__marmite.7d4bc2d

**Current:** 6.28%  (87/1385)
**Pass / Fail / Skip:** 87 / 731 / 3
**Gap to 100%:** 93.72 percentage points (1298 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_configuration.test_default_author_config`
  - reason: Author template has known bug
- `tests.test_content_types.test_multiple_authors`
  - reason: Author template has known bug
- `tests.test_shortcodes.test_shortcode_authors`
  - reason: Author template has known bug

## Failure clusters

731 failed tests grouped into 11 buckets (sorted by count).

### `boolean_false` — 235 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_additional_features.test_series_functionality`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpre_1sacs/output/series.html').exists
- `tests.test_additional_features.test_robots_txt_generation`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpeh49xdtf/output/robots.txt').exists
- `tests.test_additional_features.test_404_page_generation`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpw02zcpmf/output/404.html').exists
- *(... 232 more in this cluster)*

### `other_assertion` — 208 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_additional_features.test_rss_feeds_for_tags`
  > assert 0 > 0
  >  +  where 0 = len([])
- `tests.test_additional_features.test_archive_by_year`
  > assert 0 > 0
  >  +  where 0 = len([])
- `tests.test_additional_features.test_multiple_tags_per_post`
  > assert 0 >= 3
  >  +  where 0 = len([])
- *(... 205 more in this cluster)*

### `missing_file` — 204 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_additional_features.test_multiple_posts_ordering`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpdjlgcyi0/output/index.html'
- `tests.test_additional_features.test_language_configuration`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpnk0nunz2/output/index.html'
- `tests.test_config_and_cli_options.test_site_name_cli_override`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpn5yyf76b/output/index.html'
- *(... 201 more in this cluster)*

### `rc_mismatch_got2_want0` — 45 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_config_handling.test_custom_config_path_via_flag`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--config', 'custom.yaml', '/tmp/pytest-of-root/pytest-0/test_custom_config_path_via_fl2/input'], returncode=2, stdout='', stderr="marmite: unknown
- `tests.test_config_handling.test_missing_custom_config_file_is_not_an_error`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--config', 'does_not_exist.yaml', '/tmp/pytest-of-root/pytest-0/test_missing_custom_config_fil2/input'], returncode=2, stdout='', stderr="marmite:
- `tests.test_config_handling.test_cli_overrides_config_file`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--name', 'FromCLI', '/tmp/pytest-of-root/pytest-0/test_cli_overrides_config_file2/input'], returncode=2, stdout='', stderr="marmite: unknown optio
- *(... 42 more in this cluster)*

### `rc_mismatch_got0_want1` — 14 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `eval.tests.test_marmite_io.test_missing_input_folder_is_error_exit_1_and_stderr_only`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/no/such/path'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_config_edge_cases.test_theme_folder_does_not_exist`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', '/tmp/marmite_test_h6b8z8v6/input'], returncode=0, stdout='', stderr='').returncode
- `tests.test_error_handling.test_missing_input_directory`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['./executable', '/nonexistent/directory/that/does/not/exist'], returncode=0, stdout='', stderr='').returncode
- *(... 11 more in this cluster)*

### `rc_unexpected_zero` — 9 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_basic_invocation.test_nonexistent_input_folder`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/nonexistent/path/to/folder'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_basic_invocation.test_file_as_input_folder`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/tmp/tmpu5n8l0do/not_a_folder.txt'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_new_content.test_new_command_without_site_dir`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/tmp/tmpxnrbdzud/nonexistent', '--new', 'Test Post'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 6 more in this cluster)*

### `subprocess_failed` — 8 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_advanced.TestInitCommands.test_init_templates`
  > subprocess.CalledProcessError: Command '['/workspace/executable', '--init-templates', '/tmp/pytest-of-root/pytest-0/test_init_templates2/input']' returned non-zero exit status 2.
- `tests.test_advanced.TestShortcodes.test_shortcodes_list`
  > subprocess.CalledProcessError: Command '['/workspace/executable', '--shortcodes', '/tmp/pytest-of-root/pytest-0/test_shortcodes_list2/input']' returned non-zero exit status 2.
- `tests.test_advanced.TestForceRebuild.test_force_rebuild`
  > subprocess.CalledProcessError: Command '['/workspace/executable', '--force', '/tmp/pytest-of-root/pytest-0/test_force_rebuild2/input', '/tmp/pytest-of-root/pytest-0/test_force_rebuild2/output']' retur
- *(... 5 more in this cluster)*

### `rc_mismatch_got2_want1` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_operations.test_init_site_fails_on_non_empty_directory`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['./executable', '--init-site', '/tmp/marmite_test_0ap3b5hf'], returncode=2, stdout='', stderr="marmite: unknown option: --init-site\nusage: marmite [OPTIONS] [ARGS
- `tests.test_cli_operations.test_new_without_input_folder_fails`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['./executable', '--new', 'Test Post', '/nonexistent/path'], returncode=2, stdout='', stderr="marmite: unknown option: --new\nusage: marmite [OPTIONS] [ARGS]\nTry '
- `tests.test_cli_operations.test_init_templates_in_nonexistent_directory_fails`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['./executable', '--init-templates', '/nonexistent/path'], returncode=2, stdout='', stderr="marmite: unknown option: --init-templates\nusage: marmite [OPTIONS] [ARG

### `uncategorized` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_additional_features.test_custom_css_js_files`
  > FileExistsError: [Errno 17] File exists: '/tmp/tmpmqu84bhf'
- `tests.test_markdown_features.test_shortcodes_listing`
  > FileExistsError: [Errno 17] File exists: '/tmp/tmpa7j57oab'

### `string_output_mismatch` — 2 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_marmite_executable.test_help_exact`
  > AssertionError: assert 'marmite 0.1....int version\n' == 'Marmite is t...int version\n'
  >   
  >   - Marmite is the easiest static site generator.
  >   + marmite 0.1.0 - bootstrap scaffold
  >     
  >   + Usage: marmite [OPTIONS] [ARGS]
  >   - Usage: executable [OPTIONS] <INPUT_FOLDER> [OUTPUT_FOLDER]
  >   - ...
- `eval.tests.test_marmite_executable.test_version_exact`
  > AssertionError: assert 'marmite 0.1.0\n' == 'marmite 0.2.7\n'
  >   
  >   - marmite 0.2.7
  >   ?           ^ ^
  >   + marmite 0.1.0
  >   ?           ^ ^

### `rc_mismatch_got0_want50` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_edge_cases.TestLargeContent.test_many_files`
  > assert 0 == 50
  >  +  where 0 = len([])

