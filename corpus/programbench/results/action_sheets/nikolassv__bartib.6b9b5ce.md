# Action Sheet — nikolassv__bartib.6b9b5ce

**Current:** 23.64%  (234/990)
**Pass / Fail / Skip:** 234 / 673 / 2
**Gap to 100%:** 76.36 percentage points (756 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_subcommands.TestSubcommandRecognition.test_subcommand_has_help[help]`
  - reason: help subcommand doesn't support --help
- `eval.tests.test_bartib_workflow.test_start_auto_stops_previous_activity`
  - reason: test_start_auto_stops_previous_activity depends on test_start_creates_file_and_writes_line

## Failure clusters

673 failed tests grouped into 14 buckets (sorted by count).

### `other_assertion` — 320 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_basic_invocation.test_no_arguments_shows_help`
  > assert (b'A simple timetracker' in b"error: the following required arguments were not provided: <PATTERN>\nError: the following required arguments were not provided: <PATTERN>\nunknown flag: the follo
  >  +  where b"error: the following required arguments were not provided: <PATTERN>\nError: the following required arguments were not provided: <PATTERN>\nunknown flag: the following required arguments w
  >  +  and   b"error: the following required arguments were not provided: <PATTERN>\nError: the following required arguments were not provided: <PATTERN>\nunknown flag: the following required arguments w
- `tests.test_basic_invocation.test_help_lists_all_subcommands`
  > AssertionError: Subcommand b'start' not in help output
  > assert b'start' in b'bartib\nA simple timetracker\nUSAGE:\nSUBCOMMANDS:\nbartib\nUSAGE:\nbartib 1.1.0\nbartib 1.1.0\nPlease specify a file\nBARTIB_FILE\n'
  >  +  where b'bartib\nA simple timetracker\nUSAGE:\nSUBCOMMANDS:\nbartib\nUSAGE:\nbartib 1.1.0\nbartib 1.1.0\nPlease specify a file\nBARTIB_FILE\n' = CompletedProcess(args=['../executable', '--help'], r
- `tests.test_change_continue.test_change_description`
  > AssertionError: assert 'NewTask' in ''
- *(... 317 more in this cluster)*

### `string_output_mismatch` — 155 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_main.test_dash_h_matches_dash_dash_help_exactly`
  > AssertionError: assert 'bartib\nUSAG...BARTIB_FILE\n' == 'bartib\nA si...BARTIB_FILE\n'
  >   
  >   - bartib
  >   - A simple timetracker
  >   - USAGE:
  >   - SUBCOMMANDS:
  >     bartib
  >     USAGE:...
- `eval.tests.test_help_main.test_help_precedence_over_other_flags_exact_match`
  > AssertionError: assert 'bartib 0.1.0...int version\n' == 'bartib\nA si...BARTIB_FILE\n'
  >   
  >   - bartib
  >   - A simple timetracker
  >   - USAGE:
  >   - SUBCOMMANDS:
  >   - bartib
  >   - USAGE:...
- `eval.tests.test_list_report_projects_last_search.test_projects_quotes_default_and_no_quotes_flag`
  > assert '' == '"Important Project"'
  >   
  >   - "Important Project"
- *(... 152 more in this cluster)*

### `rc_mismatch_got1_want0` — 74 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_cancel_change_continue.test_change_time`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-f', '/tmp/tmpkqxt_sbl.bartib', 'change', '-t', '08:00'], returncode=1, stdout=b"error: unexpected argument '-f' found\nError: unexpected
- `tests.test_cancel_change_continue.test_continue_with_custom_time`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-f', '/tmp/tmpko4vw02i.bartib', 'continue', '-t', '14:00'], returncode=1, stdout=b"error: unexpected argument '-f' found\nError: unexpect
- `tests.test_edge_cases.test_round_time_15_minutes`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-f', '/tmp/tmpy_cp5wbn.bartib', 'list', '--round', '15m'], returncode=1, stdout=b"error: unexpected argument '-f' found\nError: unexpecte
- *(... 71 more in this cluster)*

### `rc_unexpected_zero` — 34 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_basic_invocation.test_error_when_no_file_specified`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['../executable', 'start', '-p', 'Test', '-d', 'Test task'], returncode=0, stdout=b'Please specify a file\nBARTIB_FILE\n', stderr=b'').returncode
- `tests.test_basic_invocation.test_invalid_subcommand`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['../executable', 'invalid_command'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_start.test_start_missing_project`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['../executable', 'start', '-d', 'Task'], returncode=0, stdout=b'Started activity:\n', stderr=b'').returncode
- *(... 31 more in this cluster)*

### `missing_file` — 28 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_edge_cases.test_bartib_file_env_var`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_bartib_file_env_var2/activities.txt'
- `eval.tests.test_bartib_validation_and_edges.test_escaping_of_pipe_and_backslash_in_log_file`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_escaping_of_pipe_and_back2/activities.bartib'
- `eval.tests.test_bartib_validation_and_edges.test_unicode_project_and_description_roundtrip`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_unicode_project_and_descr2/activities.bartib'
- *(... 25 more in this cluster)*

### `returned_none` — 21 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_file_format.test_time_formats_in_file`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f5537d73760>('\\d{2}:\\d{2}', '')
  >  +    where <function search at 0x7f5537d73760> = re.search
- `eval.tests.test_help_main.test_help_contains_usage_section`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f9588e6e680>('^USAGE:\\n\\s+executable\\s+\\[OPTIONS\\]\\s+<SUBCOMMAND>\\s*$', 'bartib\nA simple timetracker\nUSAGE:\nSUBCOMMANDS:\nbartib\nUSAGE:\nbartib 1.1.0
  >  +    where <function search at 0x7f9588e6e680> = re.search
  >  +    and   re.MULTILINE = re.M
- `eval.tests.test_help_main.test_help_documents_file_option_and_env`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f9588e6e680>('^\\s*-f\\s+<FILE>\\s+', 'bartib\nA simple timetracker\nUSAGE:\nSUBCOMMANDS:\nbartib\nUSAGE:\nbartib 1.1.0\nbartib 1.1.0\nPlease specify a file\nBA
  >  +    where <function search at 0x7f9588e6e680> = re.search
  >  +    and   re.MULTILINE = re.M
- *(... 18 more in this cluster)*

### `rc_mismatch_got0_want1` — 16 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_change_continue.test_continue_when_nothing_exists_error`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['../executable', '-f', '/tmp/pytest-of-root/pytest-0/test_continue_when_nothing_exi2/bartib.log', 'continue'], returncode=0, stdout='', stderr='').returncode
- `tests.test_change_continue.test_continue_number_larger_than_available`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['../executable', '-f', '/tmp/pytest-of-root/pytest-0/test_continue_number_larger_th2/bartib.log', 'continue', '5'], returncode=0, stdout='', stderr='').returncode
- `tests.test_edge_cases.test_continue_with_no_previous_activities`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['../executable', '-f', '/tmp/pytest-of-root/pytest-0/test_continue_with_no_previous2/continue_empty.bartib', 'continue'], returncode=0, stdout='', stderr='').retur
- *(... 13 more in this cluster)*

### `boolean_false` — 13 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_start.test_start_creates_file_if_not_exists`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/pytest-of-root/pytest-0/test_start_creates_file_if_not2/new.bartib').exists
- `tests.test_edge_cases.test_file_path_with_spaces`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/tmp_z0apsc_/my bartib file.txt').exists
  >  +      where PosixPath('/tmp/tmp_z0apsc_/my bartib file.txt') = Path('/tmp/tmp_z0apsc_/my bartib file.txt')
- `tests.test_edge_cases.test_relative_file_path`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('bartib.txt').exists
  >  +      where PosixPath('bartib.txt') = Path('./bartib.txt')
- *(... 10 more in this cluster)*

### `rc_mismatch_got0_want2` — 4 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `eval.tests.test_externalized.test_ext_get_descriptions_and_projects_simple_last_lists_unique_pairs`
  > assert 0 == 2
  >  +  where 0 = len([])
- `eval.tests.test_externalized.test_ext_get_descriptions_and_projects_restarted_activity_ordering`
  > assert 0 == 2
  >  +  where 0 = len([])
- `tests.test_current_status.test_current_single_running_activity_table_format`
  > assert 0 == 2
  >  +  where 0 = len([])
- *(... 1 more in this cluster)*

### `empty_list_or_string` — 3 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_current_status.test_status_month_boundary_first_day`
  > IndexError: list index out of range
- `tests.test_current_status.test_status_aggregation_multiple_same_project`
  > IndexError: list index out of range
- `tests.test_search.test_search_large_file_performance`
  > IndexError: list index out of range

### `subprocess_failed` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_start_stop.test_multiple_stops_no_duplicate_end_times`
  > subprocess.CalledProcessError: Command '['../executable', '-f', '/tmp/pytest-of-root/pytest-0/test_multiple_stops_no_duplica2/bartib.log', 'stop', '-t', '10:00']' returned non-zero exit status 1.
- `tests.test_start_stop.test_start_stop_start_sequence`
  > subprocess.CalledProcessError: Command '['../executable', '-f', '/tmp/pytest-of-root/pytest-0/test_start_stop_start_sequence2/bartib.log', 'stop', '-t', '10:00']' returned non-zero exit status 1.

### `bytes_output_mismatch` — 1 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_change_continue.test_change_no_running_activity`
  > AssertionError: assert (b'continues a...nNewProject\n' == b''
  >   
  >   Full diff:
  >   - b''
  >   + (b'continues a previous activity\nNUMBER\n--description\n--project\nStarted act'
  >   +  b'ivity:\nTask\nProject\nStarted activity:\nNewTask\nNewProject\n') or b'no' in b'continues a previous activity\nnumber\n--description\n--project\nstarted activity:\ntask\nproject\nstarted activi
  >  +  where b'continues a previous activity\nnumber\n--description\n--project\nstarted activity:\ntask\nproject\nstarted activity:\nnewtask\nnewproject\n' = <built-in method lower of bytes object at 0x7
  >  +    where <built-in method lower of bytes object at 0x7f5536b91630> = b'continues a previous activity\nNUMBER\n--description\n--project\nStarted activity:\nTask\nProject\nStarted activity:\nNewTask\

### `uncategorized` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_current_status.test_current_preserves_file_order`
  > ValueError: substring not found

### `rc_mismatch_got1_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_start_stop.test_cancel_multiple_concurrent_activities`
  > AssertionError: assert 1 == 3
  >  +  where 1 = len([''])

