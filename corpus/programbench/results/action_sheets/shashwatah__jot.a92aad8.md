# Action Sheet — shashwatah__jot.a92aad8

**Current:** 7.46%  (78/1045)
**Pass / Fail / Skip:** 78 / 735 / 0
**Gap to 100%:** 92.54 percentage points (967 tests)

## Failure clusters

735 failed tests grouped into 8 buckets (sorted by count).

### `string_output_mismatch` — 226 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_argparse.test_subcommand_aliases_have_same_validation_errors[op-open]`
  > AssertionError: assert '+-------+---...---+--------+' == 'editor\nchanged\nexist'
  >   
  >   - editor
  >   - changed
  >   - exist
  >   + +-------+--------+
  >   + | Input | Output |
  >   + +-------+--------+
- `eval.tests.test_argparse.test_subcommand_aliases_have_same_validation_errors[cd-chdir]`
  > AssertionError: assert 'testfolder' == ''
  >   
  >   + testfolder
- `eval.tests.test_argparse.test_subcommand_aliases_have_same_validation_errors[ls-list]`
  > AssertionError: assert 'testnote\non...oved\nrenamed' == 'testfolder'
  >   
  >   - testfolder
  >   + testnote
  >   + onlynote
  >   + removed
  >   + removed
  >   + renamed
- *(... 223 more in this cluster)*

### `other_assertion` — 216 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_argparse.test_unknown_flag_or_subcommand_errors[args0-Found argument 'nonexistent' which wasn't expected]`
  > assert "Found argument 'nonexistent' which wasn't expected" in '+-------+--------+\n| Input | Output |\n+-------+--------+\n+-------+--------+\n'
- `eval.tests.test_argparse.test_unknown_flag_or_subcommand_errors[args1-Found argument '--nonexistent-flag' which wasn't expected]`
  > assert "Found argument '--nonexistent-flag' which wasn't expected" in "error: unexpected argument '--nonexistent-flag' found\nError: unexpected argument '--nonexistent-flag' found\nunknown flag: unexp
- `eval.tests.test_argparse.test_missing_required_positional_args[args0-needles0]`
  > AssertionError: assert 'required arguments were not provided' in ''
- *(... 213 more in this cluster)*

### `missing_file` — 211 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_basic_invocation.test_no_arguments_shows_help`
  > FileNotFoundError: [Errno 2] No such file or directory: './executable'
- `tests.test_basic_invocation.test_help_command`
  > FileNotFoundError: [Errno 2] No such file or directory: './executable'
- `tests.test_basic_invocation.test_help_flag_dash_h`
  > FileNotFoundError: [Errno 2] No such file or directory: './executable'
- *(... 208 more in this cluster)*

### `boolean_false` — 62 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_config_handling.test_config_path_respects_xdg_config_home`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/jt-home-uwqg24oq/.config/jot/config').exists
  >  +      where PosixPath('/tmp/jt-home-uwqg24oq/.config/jot/config') = config_path()
  >  +        where config_path = <test_config_handling.TempHome object at 0x7f7e6c0b33d0>.config_path
- `eval.tests.test_jot_io.test_first_run_creates_default_config_and_vaults_data`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/pytest-of-root/pytest-0/test_first_run_creates_default2/xdg_config/jot/config').exists
- `eval.tests.test_jot_io.test_list_output_contains_tree_and_ansi_highlight_for_notes`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7f9b05bc7570>('myvault\n')
  >  +    where <built-in method startswith of str object at 0x7f9b05bc7570> = 'testfolder\n'.startswith
  >  +      where 'testfolder\n' = RunResult(returncode=0, stdout='testfolder\n', stderr='').stdout
- *(... 59 more in this cluster)*

### `rc_mismatch_got0_want2` — 10 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_help.test_no_args_shows_help`
  > assert 0 == 2
- `tests.test_error_handling.test_missing_note_name_argument`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['./executable', 'note'], returncode=0, stdout='testnote\n', stderr='').returncode
- `tests.test_error_handling.test_missing_folder_name_argument`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['./executable', 'folder'], returncode=0, stdout='', stderr='').returncode
- *(... 7 more in this cluster)*

### `rc_unexpected_zero` — 8 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_config_handling.test_invalid_bool_value_panics_and_exits_nonzero`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'config', 'conflict', 'notabool'], returncode=0, stdout=b'nvim\ntrue\nupdated\nupdated\nnvim\n', stderr=b'').returncode
- `tests.test_config_handling.test_malformed_config_file_panics_on_load`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'config', 'editor'], returncode=0, stdout=b'nvim\ntrue\nupdated\nupdated\nnvim\n', stderr=b'').returncode
- `eval.tests.test_help_edge_cases.test_unknown_subcommand_has_nonzero_exit_and_error_message`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'this-subcommand-does-not-exist'], returncode=0, stdout='+-------+--------+\n| Input | Output |\n+-------+--------+\n+-------+--------+\n'
- *(... 5 more in this cluster)*

### `rc_mismatch_got120_want0` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_jot_io.test_list_to_closed_pipe_does_not_panic`
  > AssertionError: assert 120 == 0
  >  +  where 120 = <Popen: returncode: 120 args: ['/workspace/executable', 'list']>.returncode

### `rc_mismatch_got0_want101` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_state_persistence.test_config_boolean_parsing_case_insensitive`
  > AssertionError: assert 0 == 101
  >  +  where 0 = CompletedProcess(args=['./executable', 'config', 'conflict', 'True'], returncode=0, stdout='nvim\ntrue\nupdated\nupdated\nnvim\n', stderr='').returncode

