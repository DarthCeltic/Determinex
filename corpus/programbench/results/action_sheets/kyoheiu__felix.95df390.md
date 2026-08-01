# Action Sheet — kyoheiu__felix.95df390

**Current:** 12.3%  (113/919)
**Pass / Fail / Skip:** 113 / 578 / 0
**Gap to 100%:** 87.70 percentage points (806 tests)

## Failure clusters

578 failed tests grouped into 8 buckets (sorted by count).

### `other_assertion` — 315 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_cli_coverage.TestLogFlag.test_log_flag_with_invalid_path`
  > AssertionError: assert b'Invalid path' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', '-l', '/nonexistent/path/that/does/not/exist'], returncode=0, stdout=b'', stderr=b'').stderr
- `tests.test_cli_coverage.TestConfigFileHandling.test_with_valid_config_file`
  > AssertionError: assert ('cannot detect terminal size' in '  .config/\n' or 0 > 0)
  >  +  where '  .config/\n' = <built-in method lower of str object at 0x711e49db5f30>()
  >  +    where <built-in method lower of str object at 0x711e49db5f30> = '  .config/\n'.lower
  >  +  and   0 = len(b'')
  >  +    where b'' = CompletedProcess(args=['/workspace/executable', '/tmp/tmpm6pp0j_a'], returncode=0, stdout=b'  .config/\n', stderr=b'').stderr
- `tests.test_cli_coverage.TestConfigFileHandling.test_with_config_yml_extension`
  > AssertionError: assert (b'Cannot detect terminal size' in b'' or 0 > 0)
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', '/tmp/tmp76mvpxj4'], returncode=0, stdout=b'  .config/\n', stderr=b'').stderr
  >  +  and   0 = len(b'')
  >  +    where b'' = CompletedProcess(args=['/workspace/executable', '/tmp/tmp76mvpxj4'], returncode=0, stdout=b'  .config/\n', stderr=b'').stderr
- *(... 312 more in this cluster)*

### `rc_mismatch_got2_want0` — 134 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_cli_coverage.TestLogFlag.test_log_flag_short`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-l', '/tmp/tmpri41o0kj'], returncode=2, stdout=b'', stderr=b'Error: Cannot write to log file: /tmp/tmpri41o0kj\n').returncode
- `tests.test_cli_coverage.TestLogFlag.test_log_flag_long`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--log', '/tmp/tmpb369dtfh'], returncode=2, stdout=b'', stderr=b'Error: Cannot write to log file: /tmp/tmpb369dtfh\n').returncode
- `tests.test_cli_coverage.TestLogFlag.test_log_flag_with_relative_path`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-l', 'tmp040pg5p5'], returncode=2, stdout=b'', stderr=b'Error: Cannot write to log file: tmp040pg5p5\n').returncode
- *(... 131 more in this cluster)*

### `string_output_mismatch` — 86 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_cli.test_help_flag_long`
  > AssertionError: assert 'felix 0.1.0\...ected files\n' == '# felix v2.1...oheiu/felix\n'
  >   
  >   - # felix v2.16.1
  >   - A simple TUI file manager with vim-like keymapping.
  >   + felix 0.1.0
  >   + A simple file manager
  >     
  >   + Usage: felix [OPTIONS] [PATH]...
- `tests.test_cli.test_help_flag_short`
  > AssertionError: assert 'felix 0.1.0\...ected files\n' == '# felix v2.1...oheiu/felix\n'
  >   
  >   - # felix v2.16.1
  >   - A simple TUI file manager with vim-like keymapping.
  >   + felix 0.1.0
  >   + A simple file manager
  >     
  >   + Usage: felix [OPTIONS] [PATH]...
- `tests.test_cli.test_file_instead_of_directory_error`
  > AssertionError: assert '' == 'Path should ...shows help.\n'
  >   
  >   - Path should be directory.
  >   - `fx -h` shows help.
- *(... 83 more in this cluster)*

### `boolean_false` — 18 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_preview.test_archive_extraction_preserves_file_permissions`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/felix_test_ke3v7u4p/extract_test/test_perms.tar_1').exists
- `tests.test_preview.test_extract_nested_directories_preserves_structure`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/felix_test__f7oj9y6/nested.tar_1').exists
- `tests.test_preview.test_large_archive_with_many_files`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/felix_test_qtt_r7uz/many_files.tar_1/source').exists
- *(... 15 more in this cluster)*

### `returned_none` — 11 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_felix.TestCommandLineInterface.test_help_contains_version_number`
  > AssertionError: assert None
  >  +  where None = <function search at 0x711e4bd4b760>(b'v\\d+\\.\\d+\\.\\d+', b'felix 0.1.0\nA simple file manager\n\nUsage: felix [OPTIONS] [PATH]\n\nArguments:\n  [PATH]  Directory to open\n\nOptions
  >  +    where <function search at 0x711e4bd4b760> = re.search
  >  +    and   b'felix 0.1.0\nA simple file manager\n\nUsage: felix [OPTIONS] [PATH]\n\nArguments:\n  [PATH]  Directory to open\n\nOptions:\n  -h, --help           Print help\n  -V, --version        Prin
- `tests.test_op_utils.test_delete_operation_logged`
  > assert None is not None
- `tests.test_op_utils.test_put_operation_logged`
  > assert None is not None
- *(... 8 more in this cluster)*

### `rc_mismatch_got1_want0` — 10 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_cli.test_very_long_path_error`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '/nonexistent/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
- `tests.test_errors.test_very_long_path`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
- `tests.test_layout_calculations.test_minimum_terminal_size_4x4_accepted`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['tmux', 'capture-pane', '-t', 'test_4x4', '-p'], returncode=1, stdout='', stderr="can't find pane: test_4x4\n").returncode
- *(... 7 more in this cluster)*

### `uncategorized` — 3 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_args.test_log_requires_tty_but_parses[--log]`
  > Failed: Expected args to be accepted, but got rc=2
  > STDOUT:
  > 
  > STDERR:
  > Error: --log requires a value
- `eval.tests.test_args.test_log_requires_tty_but_parses[-l]`
  > Failed: Expected args to be accepted, but got rc=2
  > STDOUT:
  > 
  > STDERR:
  > Error: --log requires a value
- `eval.tests.test_args.test_default_invocation_parses_and_attempts_tui`
  > Failed: Expected args to be accepted, but got rc=2
  > STDOUT:
  > 
  > STDERR:
  > usage: felix [OPTIONS] [ARGS]
  > Try 'felix --help' for more information.

### `bytes_output_mismatch` — 1 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_felix.TestFlagCombinations.test_log_short_with_valid_path`
  > AssertionError: assert (b'terminal' in b'error: cannot write to log file: /tmp/tmpxrezhxie\n' or 2 == 0)
  >  +  where b'error: cannot write to log file: /tmp/tmpxrezhxie\n' = <built-in method lower of bytes object at 0x711e49c5b1b0>()
  >  +    where <built-in method lower of bytes object at 0x711e49c5b1b0> = b'Error: Cannot write to log file: /tmp/tmpxrezhxie\n'.lower
  >  +      where b'Error: Cannot write to log file: /tmp/tmpxrezhxie\n' = CompletedProcess(args=['/workspace/executable', '-l', '/tmp/tmpxrezhxie'], returncode=2, stdout=b'', stderr=b'Error: Cannot write
  >  +  and   2 = CompletedProcess(args=['/workspace/executable', '-l', '/tmp/tmpxrezhxie'], returncode=2, stdout=b'', stderr=b'Error: Cannot write to log file: /tmp/tmpxrezhxie\n').returncode

