# Action Sheet — guumaster__hostctl.d6d9699

**Current:** 23.82%  (407/1709)
**Pass / Fail / Skip:** 407 / 755 / 0
**Gap to 100%:** 76.18 percentage points (1302 tests)

## Failure clusters

755 failed tests grouped into 14 buckets (sorted by count).

### `other_assertion` — 324 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_add_commands.test_add_missing_from_flag`
  > AssertionError: assert (b'error' in b'' or b'no such file' in b'')
  >  +  where b'' = <built-in method lower of bytes object at 0x7f11271e8030>()
  >  +    where <built-in method lower of bytes object at 0x7f11271e8030> = b''.lower
  >  +      where b'' = CompletedProcess(args=['./executable', 'add', 'test-profile', '--host-file', '/tmp/tmpn1tacgqy.hosts'], returncode=1, stdout=b'', stderr=b'error: missing arguments\n').stdout
  >  +  and   b'' = <built-in method lower of bytes object at 0x7f11271e8030>()
  >  +    where <built-in method lower of bytes object at 0x7f11271e8030> = b''.lower
  >  +      where b'' = CompletedProcess(args=['./executable', 'add', 'test-profile', '--host-file', '/tmp/tmpn1tacgqy.hosts'], returncode=1, stdout=b'', stderr=b'error: missing arguments\n').stdout
- `tests.test_backup_restore.test_backup_creates_file`
  > assert 0 > 0
  >  +  where 0 = len([])
- `tests.test_backup_restore.test_backup_filename_format`
  > assert 0 > 0
  >  +  where 0 = len([])
- *(... 321 more in this cluster)*

### `rc_mismatch_got1_want0` — 187 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_add_commands.test_add_from_file`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', 'add', 'test-profile', '--from', '/tmp/tmpy6xz87fw/profile.txt', '--host-file', '/tmp/tmpdewho5q9.hosts'], returncode=1, stdout=b'', stderr=b'error
- `tests.test_basic_invocation.test_help_command`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', 'help'], returncode=1, stdout=b'', stderr=b"error: unknown command 'help'\n").returncode
- `tests.test_completion.test_completion_help`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['./executable', 'completion', '--help'], returncode=1, stdout=b'', stderr=b"error: unknown command 'completion'\n").returncode
- *(... 184 more in this cluster)*

### `subprocess_failed` — 72 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_add_replace.test_add_new_profile_from_file`
  > subprocess.CalledProcessError: Command '['/workspace/executable', 'add', 'newprofile', '--from', '/workspace/eval/test_resources/test_add_replace/simple_hosts.txt', '--host-file', '/tmp/tmpkllvrudh.ho
- `tests.test_add_replace.test_add_to_existing_profile`
  > subprocess.CalledProcessError: Command '['/workspace/executable', 'add', 'existing', '--from', '/workspace/eval/test_resources/test_add_replace/simple_hosts.txt', '--host-file', '/tmp/tmp2h4lq79r.host
- `tests.test_add_replace.test_replace_existing_profile`
  > subprocess.CalledProcessError: Command '['/workspace/executable', 'replace', 'existing', '--from', '/workspace/eval/test_resources/test_add_replace/simple_hosts.txt', '--host-file', '/tmp/tmp94xsiyht.
- *(... 69 more in this cluster)*

### `string_output_mismatch` — 66 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_argparse_validation.test_global_out_flag_accepts_value_variants[out_args0]`
  > AssertionError: assert 'PROFILE     ...           on' == 'null'
  >   
  >   - null
  >   + PROFILE              STATUS    
  >   + ------------------------------
  >   + default              on
- `eval.tests.test_argparse_validation.test_global_out_flag_accepts_value_variants[out_args1]`
  > AssertionError: assert 'PROFILE     ...           on' == 'null'
  >   
  >   - null
  >   + PROFILE              STATUS    
  >   + ------------------------------
  >   + default              on
- `eval.tests.test_argparse_validation.test_global_out_flag_accepts_value_variants[out_args2]`
  > AssertionError: assert 'PROFILE     ...           on' == 'null'
  >   
  >   - null
  >   + PROFILE              STATUS    
  >   + ------------------------------
  >   + default              on
- *(... 63 more in this cluster)*

### `json_output_missing_or_bad` — 45 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `tests.test_output_formats.test_list_json_structure`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_output_formats.test_status_json_structure`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_additional_coverage.test_status_with_json_format`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- *(... 42 more in this cluster)*

### `returned_none` — 20 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_main.test_usage_line_mentions_hostctl_and_command_placeholder`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f9d2501a680>('^\\s*hostctl \\[command\\]\\s*$', 'hostctl is a CLI tool to manage your hosts file\n\nUsage:\n  hostctl [command] [flags]\n\nAvailable Commands:\n
  >  +    where <function search at 0x7f9d2501a680> = re.search
  >  +    and   'hostctl is a CLI tool to manage your hosts file\n\nUsage:\n  hostctl [command] [flags]\n\nAvailable Commands:\n  add         Add domains to a profile\n  backup      Backup hosts file\n  d
  >  +    and   re.MULTILINE = re.MULTILINE
- `eval.tests.test_help_main.test_help_lists_expected_commands[add-Add content]`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f9d2501a680>('^\\s*add\\s+.*Add\\ content.*$', 'hostctl is a CLI tool to manage your hosts file\n\nUsage:\n  hostctl [command] [flags]\n\nAvailable Commands:\n 
  >  +    where <function search at 0x7f9d2501a680> = re.search
  >  +    and   'hostctl is a CLI tool to manage your hosts file\n\nUsage:\n  hostctl [command] [flags]\n\nAvailable Commands:\n  add         Add domains to a profile\n  backup      Backup hosts file\n  d
  >  +    and   re.MULTILINE = re.MULTILINE
- `eval.tests.test_help_main.test_help_lists_expected_commands[backup-backup]`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f9d2501a680>('^\\s*backup\\s+.*backup.*$', 'hostctl is a CLI tool to manage your hosts file\n\nUsage:\n  hostctl [command] [flags]\n\nAvailable Commands:\n  add
  >  +    where <function search at 0x7f9d2501a680> = re.search
  >  +    and   'hostctl is a CLI tool to manage your hosts file\n\nUsage:\n  hostctl [command] [flags]\n\nAvailable Commands:\n  add         Add domains to a profile\n  backup      Backup hosts file\n  d
  >  +    and   re.MULTILINE = re.MULTILINE
- *(... 17 more in this cluster)*

### `rc_mismatch_got0_want1` — 10 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `eval.tests.test_help_and_errors.test_missing_hosts_file_is_error_exit1_and_message_on_stdout`
  > AssertionError: assert 0 == 1
  >  +  where 0 = RunResult(returncode=0, stdout='PROFILE              STATUS    \n------------------------------\ndefault              off       \n', stderr='').returncode
- `tests.test_final_gaps.test_malformed_hosts_file_parse_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'list', '-o', 'json', '--host-file', '/tmp/nonexistent_hosts_file_12345.txt'], returncode=0, stdout=b'PROFILE              IP             
- `tests.test_final_gaps.test_add_domains_to_default_profile_rejected`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'add', 'domains', 'default', 'test.loc', '--ip', '10.0.0.1', '--host-file', '/tmp/tmpqc0r2xe6.hosts'], returncode=0, stdout=b'', stderr=b'
- *(... 7 more in this cluster)*

### `missing_file` — 10 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_backup_restore.test_backup_contains_complete_hosts_content`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpn7rhhqeh/tmphf0tavki.hosts.20260517'
- `tests.test_backup_restore.test_backup_preserves_multiple_profiles`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpid42iwph/multi_profile.txt.20260517'
- `tests.test_backup_restore.test_backup_with_unicode_content`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpe0d9ybiy/unicode.txt.20260517'
- *(... 7 more in this cluster)*

### `rc_unexpected_zero` — 9 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_error_handling.test_invalid_flag`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'list', '--not-a-real-flag'], returncode=0, stdout=b'PROFILE              IP                   HOST                           STATUS    \n---------
- `tests.test_add_operations.test_add_missing_file_error`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'add', 'failprofile', '-f', '/nonexistent/file.txt', '--host-file', '/tmp/tmp5q_2eoxr/hosts_empty'], returncode=0, stdout=b'', stderr=b'').returnco
- `tests.test_final_push.test_add_with_invalid_file_path`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'add', 'badfile', '-f', '/tmp/this/path/does/not/exist.txt', '--host-file', '/tmp/tmpjte3_v1u/hosts_empty'], returncode=0, stdout=b'', stderr=b'').
- *(... 6 more in this cluster)*

### `rc_mismatch_got2_want0` — 4 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_basic_invocation.test_no_arguments_shows_help`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable'], returncode=2, stdout=b'', stderr=b'Usage: hostctl [command] [flags]\n').returncode
- `tests.test_basic_invocation.test_no_arguments_shows_help`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable'], returncode=2, stdout=b'', stderr=b'Usage: hostctl [command] [flags]\n').returncode
- `eval.tests.test_help_formatting.test_no_color_flag_does_not_introduce_ansi_sequences`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--no-color', '--help'], returncode=2, stdout='', stderr='Usage: hostctl [command] [flags]\n').returncode
- *(... 1 more in this cluster)*

### `boolean_false` — 4 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `eval.tests.test_help_formatting.test_help_output_starts_with_blank_line`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x556fa1027cd0>('\n')
  >  +    where <built-in method startswith of str object at 0x556fa1027cd0> = 'hostctl is a CLI tool to manage your hosts file\n\nUsage:\n  hostctl [command] [flags]\n\nAvailable Commands:\n  add        
  >  +      where 'hostctl is a CLI tool to manage your hosts file\n\nUsage:\n  hostctl [command] [flags]\n\nAvailable Commands:\n  add         Add domains to a profile\n  backup      Backup hosts file\n 
- `tests.test_backup_restore.test_restore_from_backup_replaces_content`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpchnwvi2i/original.txt.20260517').exists
- `tests.test_backup_restore.test_backup_empty_hosts_file`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmpduabp8q7/empty.txt.20260517').exists
- *(... 1 more in this cluster)*

### `empty_list_or_string` — 2 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_backup_restore.TestRestoreCommand.test_restore_overwrites_all_content`
  > IndexError: list index out of range
- `tests.test_backup_restore.TestBackupRestoreWorkflow.test_backup_modify_restore_workflow`
  > IndexError: list index out of range

### `bytes_output_mismatch` — 1 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_backup_restore.test_backup_with_quiet_flag`
  > AssertionError: assert (b'Backup crea...0517_215238\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'Backup created: /tmp/tmpn95cnn85.hosts.20260517_215238\n') or 55 < 50)
  >  +  where 55 = len(b'Backup created: /tmp/tmpn95cnn85.hosts.20260517_215238\n')
  >  +    where b'Backup created: /tmp/tmpn95cnn85.hosts.20260517_215238\n' = CompletedProcess(args=['./executable', 'backup', '--host-file', '/tmp/tmpn95cnn85.hosts', '--path', '/tmp/tmphggtcjpn', '--qui

### `type_error` — 1 test(s)

**Quick patch ideas:**
- Specific TypeError; check arg types vs expected

**Sample failures:**

- `eval.tests.test_remove_replace_backup_restore.test_backup_and_restore_roundtrip`
  > TypeError: argument of type 'NoneType' is not iterable

