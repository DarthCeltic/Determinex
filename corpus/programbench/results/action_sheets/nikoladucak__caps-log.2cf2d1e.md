# Action Sheet — nikoladucak__caps-log.2cf2d1e

**Current:** 46.57%  (530/1138)
**Pass / Fail / Skip:** 530 / 563 / 21
**Gap to 100%:** 53.43 percentage points (608 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_calendar_interaction.test_navigate_calendar_dates`
  - reason: test_navigate_calendar_dates depends on test_switch_focus_to_calendar
- `tests.test_calendar_interaction.test_calendar_navigation_with_arrows`
  - reason: test_calendar_navigation_with_arrows depends on test_switch_focus_to_calendar
- `tests.test_calendar_interaction.test_minus_key_previous_year`
  - reason: test_minus_key_previous_year depends on test_plus_key_next_year
- `tests.test_calendar_interaction.test_selecting_date_shows_preview`
  - reason: test_selecting_date_shows_preview depends on test_switch_focus_to_calendar
- `tests.test_scratchpad.test_scratchpad_view_has_content`
  - reason: test_scratchpad_view_has_content depends on test_switch_to_scratchpad_with_s
- *(... 16 more skipped)*

## Failure clusters

563 failed tests grouped into 10 buckets (sorted by count).

### `other_assertion` — 410 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_additional_coverage.test_decrypt_validates_password`
  > AssertionError: assert b'Applying crypto' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', '--config', '/tmp/tmp85pmbc9p/config.ini', '--log-dir-path', '/tmp/tmp85pmbc9p/logs', '--decrypt', '--password', 'correctpass'], returnc
- `tests.test_additional_coverage.test_encryption_multiple_year_dirs`
  > AssertionError: assert b'Log for 2024-01-1' not in b'Log for 2024-01-1'
  >  +  where b'Log for 2024-01-1' = <built-in method encode of str object at 0x7f921d81b140>()
  >  +    where <built-in method encode of str object at 0x7f921d81b140> = 'Log for 2024-01-1'.encode
- `tests.test_additional_coverage.test_decrypt_multiple_year_dirs`
  > AssertionError: assert b'Applying crypto' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', '--config', '/tmp/tmp8ru1vqh6/config.ini', '--log-dir-path', '/tmp/tmp8ru1vqh6/logs', '--decrypt', '--password', 'pass'], returncode=0, 
- *(... 407 more in this cluster)*

### `string_output_mismatch` — 61 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_output.test_help_starts_with_program_banner`
  > assert '--help' == "Captain's Lo...urnalig tool."
  >   
  >   - Captain's Log (caps-log)! A CLI journalig tool.
  >   + --help
- `eval.tests.test_help_output.test_short_help_h_equals_long_help_output`
  > AssertionError: assert '--help\n--co...ying crypto\n' == 'Allowed opti...\n--decrypt\n'
  >   
  >   - Allowed options:
  >     --help
  >     --config
  >     --log-dir-path
  >     --log-name-format
  >     --sunday-start...
- `eval.tests.test_help_output.test_help_baseline_normalized_matches_fixture`
  > assert '--help\n--co...ying crypto\n' == "Captain's Lo...--password)\n"
  >   
  >   + --help
  >   + --config
  >   + --log-dir-path
  >   + --log-name-format
  >   + --sunday-start
  >   + --first-line-section...
- *(... 58 more in this cluster)*

### `rc_unexpected_zero` — 45 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_more_error_paths.test_decrypt_without_password`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--config', '/tmp/tmpgmvyqfrm/config.ini', '--log-dir-path', '/tmp/tmpgmvyqfrm/logs', '--decrypt'], returncode=0, stdout=b'', stderr=b'').
- `tests.test_more_error_paths.test_decrypt_non_encrypted`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--config', '/tmp/tmpbysy3sny/config.ini', '--log-dir-path', '/tmp/tmpbysy3sny/logs', '--decrypt', '--password', 'pass'], returncode=0, st
- `eval.tests.test_argparse_validation.test_missing_value_for_value_taking_options[args1-required argument for option '--config' is missing]`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--config'], returncode=0, stdout='Applying crypto\n', stderr='').returncode
- *(... 42 more in this cluster)*

### `rc_mismatch_got1_want0` — 15 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_more_error_paths.test_log_dir_path_not_exist`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '--config', '/tmp/tmpoxbrjzve/config.ini', '--log-dir-path', '/tmp/tmpoxbrjzve/nonexistent_logs'], returncode=1, stdout=b"error: unexpecte
- `tests.test_more_error_paths.test_config_with_password_in_file`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '--config', '/tmp/tmpqk0i5wal/config.ini', '--encrypt'], returncode=1, stdout=b'', stderr=b'').returncode
- `eval.tests.test_argparse_validation.test_option_value_formats_work_for_encrypt[<lambda>1]`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '--config=/tmp/pytest-of-root/pytest-0/test_option_value_formats_work3/caps/config.ini', '--log-dir-path=/tmp/pytest-of-root/pytest-0/test
- *(... 12 more in this cluster)*

### `rc_mismatch_got0_want1` — 14 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_basic_invocation.test_no_args_requires_config_file`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable'], returncode=0, stdout=b'caps-log 0.1.0\n----------------------------------------\nInteractive TUI tool driven by tmux/libtmux/pexpect harn
- `tests.test_edge_cases.test_empty_password`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--config', '/tmp/tmpmahlzfsu/config.ini', '--log-dir-path', '/tmp/tmpmahlzfsu/logs', '--encrypt', '--password', ''], returncode=0, stdout
- `tests.test_encryption.test_decrypt_requires_password`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--config', '/tmp/tmpzg4aomo6/config.ini', '--log-dir-path', '/tmp/tmpzg4aomo6/logs', '--decrypt'], returncode=0, stdout=b'', stderr=b'').
- *(... 11 more in this cluster)*

### `boolean_false` — 13 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_additional_coverage.test_encryption_marker_file_content`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpk7wmq8iu/logs/.cle').exists
- `tests.test_comprehensive_behavior.test_encryption_creates_marker_with_hash`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpfigt4jxo/logs/.cle').exists
- `tests.test_comprehensive_behavior.test_decryption_removes_marker`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpusg72n_c/logs/.cle').exists
- *(... 10 more in this cluster)*

### `uncategorized` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_coverage_boost_logs.test_decrypt_restores_original_content`
  > UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb2 in position 0: invalid start byte
- `tests.test_coverage_boost_logs.test_encrypt_multiple_files_same_operation`
  > UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf5 in position 2: invalid start byte

### `test_timeout` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_coverage_boost_logs.test_missing_password_for_encrypted_repo`
  > subprocess.TimeoutExpired: Command '['/workspace/executable_coverage', '--config', '/tmp/tmpow5kk9ch/config.ini', '--log-dir-path', '/tmp/tmpow5kk9ch/logs']' timed out after 2 seconds

### `bytes_output_mismatch` — 1 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `eval.tests.test_encrypt_decrypt_io.test_decrypt_with_wrong_password_still_exit0_but_corrupts_plaintext`
  > AssertionError: assert b'' == b'Applying crypto...\n'
  >   
  >   Full diff:
  >   - (b'Applying crypto...\n')
  >   + b''

### `returned_none` — 1 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_externalized.test_ext_config_file_invalid_theme_exits_nonzero_and_mentions_ansi256`
  > assert None
  >  +  where None = <function search at 0x7f59ddebe680>('ansi256\\(999\\)|ansi256', "error: unexpected argument '--log-dir-path' found\nError: unexpected argument '--log-dir-path' found\nunknown flag: un
  >  +    where <function search at 0x7f59ddebe680> = re.search
  >  +    and   "error: unexpected argument '--log-dir-path' found\nError: unexpected argument '--log-dir-path' found\nunknown flag: unexpected argument '--log-dir-path' found\nUnknown flag: unexpected ar
  >  +    and   re.IGNORECASE = re.IGNORECASE

