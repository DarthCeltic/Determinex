# Action Sheet — rust-lang__mdbook.37273ba

**Current:** 15.68%  (213/1358)
**Pass / Fail / Skip:** 213 / 813 / 6
**Gap to 100%:** 84.32 percentage points (1145 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_harvest.test_failing_preprocessor`
  - reason: Requires cargo example preprocessor
- `tests.test_harvest.test_renderer_with_arguments`
  - reason: Requires custom renderer program
- `tests.test_harvest.test_backends_receive_render_context_via_stdin`
  - reason: Requires custom renderer program
- `tests.test_harvest.test_legacy_relative_command_path`
  - reason: Requires custom renderer program
- `tests.test_harvest.test_example_supports_whatever`
  - reason: API-level test
- *(... 1 more skipped)*

## Failure clusters

813 failed tests grouped into 8 buckets (sorted by count).

### `other_assertion` — 281 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_advanced_features.test_build_with_configuration_options`
  > AssertionError: assert b'HTML' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', 'build'], returncode=0, stdout=b'', stderr=b'').stderr
- `tests.test_advanced_features.test_build_with_custom_theme_colors`
  > AssertionError: assert b'HTML' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', 'build'], returncode=0, stdout=b'', stderr=b'').stderr
- `tests.test_advanced_features.test_build_with_multilevel_summary`
  > AssertionError: assert b'HTML' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', 'build'], returncode=0, stdout=b'', stderr=b'').stderr
- *(... 278 more in this cluster)*

### `missing_file` — 225 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_book_loading.test_book_with_src_dir_config`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmplmvotwvr/custom_src_book/book/ch.html'
- `tests.test_book_loading.test_book_with_build_dir_config`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpzlhcikca/custom_build_book/output/ch.html'
- `tests.test_book_loading.test_book_with_preprocessor_config`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpzj7mes2_/preprocessor_book/book/ch.html'
- *(... 222 more in this cluster)*

### `boolean_false` — 199 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_advanced_features.test_build_output_structure`
  > AssertionError: assert False
  >  +  where False = is_dir()
  >  +    where is_dir = (PosixPath('/tmp/tmp1v39v0ps/book') / 'css').is_dir
- `tests.test_clean_command.test_clean_basic`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpuwvl_894/book').exists
- `tests.test_clean_command.test_clean_custom_directory`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmppc_qt530/book').exists
- *(... 196 more in this cluster)*

### `rc_unexpected_zero` — 61 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_basic_invocation.test_invalid_command`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'invalid_command_xyz'], returncode=0, stdout=b'boilerplate\n--force\n--title\n--theme\n--ignore\nBuilds a book\n--dest-dir\n--open\nRust c
- `tests.test_build_command.test_build_missing_book_toml`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'build'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_build_command.test_build_invalid_book_toml`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'build'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 58 more in this cluster)*

### `string_output_mismatch` — 24 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_baselines_serial.test_help_main_exact_baseline_match`
  > AssertionError: assert 'Creates a bo...atch\nserve\n' == 'Creates a bo...lang/mdBook\n'
  >   
  >     Creates a book from markdown files
  >   - 
  >     Usage: executable [COMMAND]
  >   - 
  >     Commands:
  >   + init...
- `eval.tests.test_help_baselines_serial.test_init_help_exact_baseline_match`
  > AssertionError: assert 'Creates the ...e\n--ignore\n' == 'Creates the ...int version\n'
  >   
  >     Creates the boilerplate structure and files for a new book
  >   + Usage: executable init
  >   + --theme
  >   + --force
  >   + --title
  >   + --ignore...
- `eval.tests.test_help_main.test_dash_h_matches_dash_dash_help_exact`
  > AssertionError: assert 'Creates a bo...kdown files\n' == 'Creates a bo...atch\nserve\n'
  >   
  >     Creates a book from markdown files
  >   - Usage: executable [COMMAND]
  >   - Commands:
  >   - init
  >   - build
  >   - test...
- *(... 21 more in this cluster)*

### `returned_none` — 10 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_main.test_help_has_commands_section_with_known_commands`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7ffb59902680>('^\\s*help\\b', 'Creates a book from markdown files\nUsage: executable [COMMAND]\nCommands:\ninit\nbuild\ntest\nclean\ncompletions\nwatch\nserve\n'
  >  +    where <function search at 0x7ffb59902680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- `eval.tests.test_help_subcommands.test_subcommand_help_has_usage_and_key_flags[init-^Usage: executable init \\[OPTIONS\\] \\[dir\\]$-must_contain0]`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7ffb59902680>('^Usage: executable init \\[OPTIONS\\] \\[dir\\]$', 'Creates the boilerplate structure and files for a new book\nUsage: executable init\n--theme\n-
  >  +    where <function search at 0x7ffb59902680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- `eval.tests.test_help_subcommands.test_subcommand_help_has_usage_and_key_flags[build-^Usage: executable build \\[OPTIONS\\] \\[dir\\]$-must_contain1]`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7ffb59902680>('^Usage: executable build \\[OPTIONS\\] \\[dir\\]$', 'Builds a book from its markdown files\nUsage: executable build\n--dest-dir\n--open\n', re.MUL
  >  +    where <function search at 0x7ffb59902680> = re.search
  >  +    and   re.MULTILINE = re.MULTILINE
- *(... 7 more in this cluster)*

### `rc_mismatch_got0_want2` — 7 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_basic_invocation.test_no_arguments_shows_help`
  > assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable'], returncode=0, stdout=b'{\n  "Alice": "",\n  "Author": "",\n  "Author1": "",\n  "Chapter": "",\n  "GIT_CONFIG_NOSYSTEM": "",\n  "GOCOVERDI
- `tests.test_basic.test_no_args_shows_help`
  > assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable'], returncode=0, stdout=b'{\n  "Alice": "",\n  "Author": "",\n  "Author1": "",\n  "Chapter": "",\n  "GIT_CONFIG_NOSYSTEM": "",\n  "GOCOVERDI
- `eval.tests.test_args_parsing.test_unknown_subcommand_errors`
  > assert 0 == 2
  >  +  where 0 = RunResult(returncode=0, stdout='{\n  "Alice": "",\n  "Author": "",\n  "Author1": "",\n  "Chapter": "",\n  "GIT_CONFIG_NOSYSTEM": "",\n  "GOCOVERDIR": "",\n  "LLVM_PROFILE_FILE": "",\n  "
- *(... 4 more in this cluster)*

### `rc_mismatch_got0_want101` — 6 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_build_clean.test_build_nonexistent_dir_errors_with_101`
  > AssertionError: assert 0 == 101
  >  +  where 0 = RunResult(args=['/workspace/executable', 'build', '/tmp/pytest-of-root/pytest-0/test_build_nonexistent_dir_err2/does_not_exist'], returncode=0, stdout='Builds a book from its markdown fi
- `tests.test_errors.test_conflicting_config_options`
  > AssertionError: assert 0 == 101
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'build'], returncode=0, stdout='', stderr='').returncode
- `tests.test_errors.test_duplicate_chapter_files`
  > AssertionError: assert 0 == 101
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'build'], returncode=0, stdout='', stderr='').returncode
- *(... 3 more in this cluster)*

