# Action Sheet — chmln__handlr.90e78ba

**Current:** 12.37%  (138/1116)
**Pass / Fail / Skip:** 138 / 721 / 6
**Gap to 100%:** 87.63 percentage points (978 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_subcommand_dispatch.test_subcommand_recognized_via_help[NOTSET]`
  - reason: got empty parameter set for (subcmd)
- `eval.tests.test_subcommand_dispatch.test_subcommand_help_differs_from_main_help[NOTSET]`
  - reason: got empty parameter set for (subcmd)
- `eval.tests.test_add_list.test_list_contains_mapping`
  - reason: test_list_contains_mapping depends on test_add_keeps_default_first
- `eval.tests.test_add_list.test_list_all_shows_added_associations`
  - reason: test_list_all_shows_added_associations depends on test_add_keeps_default_first
- `eval.tests.test_set_get_unset.test_get_returns_handler`
  - reason: test_get_returns_handler depends on test_set_writes_mimeapps_list
- *(... 1 more skipped)*

## Failure clusters

721 failed tests grouped into 10 buckets (sorted by count).

### `rc_mismatch_got2_want0` — 333 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_add.test_add_handler`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', 'add', 'text/plain', 'test-app.desktop'], returncode=2, stdout=b'', stderr=b"usage: main.py [-h] {} ...\nmain.py: error: argument command: invalid 
- `tests.test_add.test_add_multiple_handlers`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', 'add', 'text/plain', 'test-app.desktop'], returncode=2, stdout=b'', stderr=b"usage: main.py [-h] {} ...\nmain.py: error: argument command: invalid 
- `tests.test_add.test_add_wildcard`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', 'add', 'text/*', 'test-app.desktop'], returncode=2, stdout=b'', stderr=b"usage: main.py [-h] {} ...\nmain.py: error: argument command: invalid choi
- *(... 330 more in this cluster)*

### `other_assertion` — 196 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_add.test_add_to_existing`
  > assert b'test-app.desktop' in b''
  >  +  where b'' = CompletedProcess(args=['./executable', 'get', 'text/plain'], returncode=2, stdout=b'', stderr=b"usage: main.py [-h] {} ...\nmain.py: error: argument command: invalid choice: 'get' (cho
  >  +    where CompletedProcess(args=['./executable', 'get', 'text/plain'], returncode=2, stdout=b'', stderr=b"usage: main.py [-h] {} ...\nmain.py: error: argument command: invalid choice: 'get' (choose 
- `tests.test_autocomplete.test_autocomplete_desktop_files`
  > assert 2 in [0, 1]
  >  +  where 2 = CompletedProcess(args=['./executable', 'autocomplete', '-d'], returncode=2, stdout=b'', stderr=b"usage: main.py [-h] {} ...\nmain.py: error: argument command: invalid choice: 'autocomple
- `tests.test_autocomplete.test_autocomplete_mimes`
  > assert 2 in [0, 1]
  >  +  where 2 = CompletedProcess(args=['./executable', 'autocomplete', '-m'], returncode=2, stdout=b'', stderr=b"usage: main.py [-h] {} ...\nmain.py: error: argument command: invalid choice: 'autocomple
- *(... 193 more in this cluster)*

### `subprocess_failed` — 119 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_add.test_first_handler_becomes_default`
  > subprocess.CalledProcessError: Command '['/workspace/executable', 'add', 'video/mp4', 'mpv.desktop']' returned non-zero exit status 2.
- `tests.test_add.test_add_to_existing_set_association`
  > subprocess.CalledProcessError: Command '['/workspace/executable', 'set', 'video/mp4', 'mpv.desktop']' returned non-zero exit status 2.
- `tests.test_add.test_add_three_handlers_ordering`
  > subprocess.CalledProcessError: Command '['/workspace/executable', 'add', 'text/plain', 'vim.desktop']' returned non-zero exit status 2.
- *(... 116 more in this cluster)*

### `string_output_mismatch` — 39 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_add.test_add_invalid_mime_type_fails`
  > AssertionError: assert 'usage: main....oose from )\n' == 'error: Inval... try --help\n'
  >   
  >   + usage: main.py [-h] {} ...
  >   + main.py: error: argument command: invalid choice: 'add' (choose from )
  >   - error: Invalid value for '<mime>': mime parse error: an invalid token was encountered, 2F at position 8
  >   - 
  >   - For more information try --help
- `tests.test_add.test_add_incomplete_mime_type_fails`
  > AssertionError: assert 'usage: main....oose from )\n' == 'error: Inval... try --help\n'
  >   
  >   + usage: main.py [-h] {} ...
  >   + main.py: error: argument command: invalid choice: 'add' (choose from )
  >   - error: Invalid value for '<mime>': bad mime: image/
  >   - 
  >   - For more information try --help
- `tests.test_add.test_add_no_arguments_fails`
  > AssertionError: assert 'usage: main....oose from )\n' == 'error: The f... try --help\n'
  >   
  >   + usage: main.py [-h] {} ...
  >   + main.py: error: argument command: invalid choice: 'add' (choose from )
  >   - error: The following required arguments were not provided:
  >   -     <mime>
  >   -     <handler>
  >   - ...
- *(... 36 more in this cluster)*

### `missing_file` — 15 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_config_advanced.test_config_enable_selector_false_by_default`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_config_enable_selector_fa2/config/handlr/handlr.toml'
- `tests.test_config_advanced.test_config_selector_default_rofi_command`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_config_selector_default_r2/config/handlr/handlr.toml'
- `tests.test_config_advanced.test_config_preserves_custom_selector_command`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_config_preserves_custom_s2/config/handlr/handlr.toml'
- *(... 12 more in this cluster)*

### `returned_none` — 8 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_main.test_help_usage_line_is_expected`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f4665a36680>('^\\s*executable\\s+<SUBCOMMAND>\\s*$', 'usage: main.py [-h] {} ...\n\nBatch rename files\n\npositional arguments:\n  {}\n\noptions:\n  -h, --help 
  >  +    where <function search at 0x7f4665a36680> = re.search
  >  +    and   'usage: main.py [-h] {} ...\n\nBatch rename files\n\npositional arguments:\n  {}\n\noptions:\n  -h, --help  show this help message and exit\n' = CompletedProcess(args=['/workspace/executab
  >  +    and   re.MULTILINE = re.MULTILINE
- `eval.tests.test_help_main.test_main_help_lists_subcommand[list]`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f4665a36680>('^\\s*list\\b', 'usage: main.py [-h] {} ...\n\nBatch rename files\n\npositional arguments:\n  {}\n\noptions:\n  -h, --help  show this help message 
  >  +    where <function search at 0x7f4665a36680> = re.search
  >  +    and   'usage: main.py [-h] {} ...\n\nBatch rename files\n\npositional arguments:\n  {}\n\noptions:\n  -h, --help  show this help message and exit\n' = CompletedProcess(args=['/workspace/executab
  >  +    and   re.MULTILINE = re.MULTILINE
- `eval.tests.test_help_main.test_main_help_lists_subcommand[open]`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f4665a36680>('^\\s*open\\b', 'usage: main.py [-h] {} ...\n\nBatch rename files\n\npositional arguments:\n  {}\n\noptions:\n  -h, --help  show this help message 
  >  +    where <function search at 0x7f4665a36680> = re.search
  >  +    and   'usage: main.py [-h] {} ...\n\nBatch rename files\n\npositional arguments:\n  {}\n\noptions:\n  -h, --help  show this help message and exit\n' = CompletedProcess(args=['/workspace/executab
  >  +    and   re.MULTILINE = re.MULTILINE
- *(... 5 more in this cluster)*

### `rc_mismatch_got2_want1` — 7 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_externalized_rs_like.test_ext_mime_types_from_path`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'open', '.'], returncode=2, stdout='', stderr="usage: main.py [-h] {} ...\nmain.py: error: argument command: invalid choice: 'open' (choos
- `tests.test_config_advanced.test_selector_with_no_matching_handlers_returns_not_found`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'get', 'application/x-nonexistent-type'], returncode=2, stdout='', stderr="usage: main.py [-h] {} ...\nmain.py: error: argument command: i
- `tests.test_errors.test_get_no_handler_configured`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'get', 'text/plain'], returncode=2, stdout='', stderr="usage: main.py [-h] {} ...\nmain.py: error: argument command: invalid choice: 'get'
- *(... 4 more in this cluster)*

### `uncategorized` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_set_get_unset.test_set_missing_arguments`
  > NameError: name 'output' is not defined
- `tests.test_set_get_unset.test_get_missing_arguments`
  > NameError: name 'output' is not defined

### `bytes_output_mismatch` — 1 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_comprehensive_coverage.test_autocomplete_desktop_files_flag`
  > assert (b'myapp.desktop' in b'' or 2 == 0)
  >  +  where b'' = CompletedProcess(args=['./executable', 'autocomplete', '-d'], returncode=2, stdout=b'', stderr=b"usage: main.py [-h] {} ...\nmain.py: error: argument command: invalid choice: 'autocomp
  >  +  and   2 = CompletedProcess(args=['./executable', 'autocomplete', '-d'], returncode=2, stdout=b'', stderr=b"usage: main.py [-h] {} ...\nmain.py: error: argument command: invalid choice: 'autocomple

### `rc_unexpected_zero` — 1 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_externalized_rs_like.test_ext_mime_types_from_ext_and_invalid_inputs`
  > assert 2 != 2
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'get', 'audio/mpeg'], returncode=2, stdout='', stderr="usage: main.py [-h] {} ...\nmain.py: error: argument command: invalid choice: 'get'

