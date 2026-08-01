# Action Sheet — naggie__dstask.ff57396

**Current:** 8.49%  (141/1661)
**Pass / Fail / Skip:** 141 / 906 / 5
**Gap to 100%:** 91.51 percentage points (1520 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_display_tty.test_next_tty_task_with_notes_display`
  - reason: Note command opens editor in TTY mode - requires editor mocking
- `eval.tests.test_dstask_behavior.test_modify_applies_tags_project_priority`
  - reason: test_modify_applies_tags_project_priority depends on test_add_task_creates_pending_and_appears_in_show_open
- `eval.tests.test_dstask_behavior.test_start_moves_to_active`
  - reason: test_start_moves_to_active depends on test_modify_applies_tags_project_priority
- `eval.tests.test_dstask_behavior.test_stop_moves_to_paused`
  - reason: test_stop_moves_to_paused depends on test_start_moves_to_active
- `eval.tests.test_dstask_behavior.test_done_moves_to_resolved`
  - reason: test_done_moves_to_resolved depends on test_stop_moves_to_paused

## Failure clusters

906 failed tests grouped into 21 buckets (sorted by count).

### `other_assertion` — 279 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_additional_commands.test_completions_command`
  > AssertionError: assert 2 in [0, 1]
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '_completions'], returncode=2, stdout=b'', stderr=b'Unknown command: _completions\n').returncode
- `tests.test_additional_commands.test_add_task_with_slash_for_notes`
  > assert 0 >= 1
  >  +  where 0 = len([])
- `tests.test_additional_commands.test_log_with_slash_separator`
  > assert 0 >= 1
  >  +  where 0 = len([])
- *(... 276 more in this cluster)*

### `rc_mismatch_got2_want0` — 258 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_additional_commands.test_show_next_alias`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'show-next'], returncode=2, stdout=b'', stderr=b'Unknown command: show-next\n').returncode
- `tests.test_additional_commands.test_context_with_multiple_tags`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'context', '+work', '+urgent'], returncode=2, stdout=b'', stderr=b'Unknown command: context\n').returncode
- `tests.test_additional_commands.test_show_tags_with_counts`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'show-tags'], returncode=2, stdout=b'', stderr=b'Unknown command: show-tags\n').returncode
- *(... 255 more in this cluster)*

### `json_output_missing_or_bad` — 101 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `tests.test_additional_coverage.test_add_task_with_due_date`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_additional_coverage.test_show_open_with_filter`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_additional_coverage.test_show_resolved_with_weeks`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- *(... 98 more in this cluster)*

### `rc_mismatch_got0_want1` — 73 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_task_creation.test_add_basic_task`
  > assert 0 == 1
  >  +  where 0 = len([])
- `tests.test_task_creation.test_add_task_with_tag`
  > assert 0 == 1
  >  +  where 0 = len([])
- `tests.test_task_creation.test_add_task_with_project`
  > assert 0 == 1
  >  +  where 0 = len([])
- *(... 70 more in this cluster)*

### `subprocess_failed` — 36 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_completions_misc.TestEdgeCases.test_concurrent_operations`
  > subprocess.CalledProcessError: Command '['/workspace/executable', 'start', '1']' returned non-zero exit status 2.
- `tests.test_context.TestContextCommand.test_context_set_none`
  > subprocess.CalledProcessError: Command '['/workspace/executable', 'context', '+work']' returned non-zero exit status 2.
- `tests.test_context.TestContextCommand.test_context_affects_next`
  > subprocess.CalledProcessError: Command '['/workspace/executable', 'context', '+work']' returned non-zero exit status 2.
- *(... 33 more in this cluster)*

### `uncategorized` — 29 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_commands_gaps.test_show_resolved_includes_resolved_tasks`
  > RuntimeError: Failed to parse JSON output: Expecting value: line 1 column 1 (char 0)
  > stdout:
- `tests.test_commands_gaps.test_show_active_filters_correctly`
  > RuntimeError: dstask command failed: show-active
  > stdout: 
  > stderr: Unknown command: show-active
- `tests.test_commands_gaps.test_show_paused_filters_correctly`
  > RuntimeError: dstask command failed: show-paused
  > stdout: 
  > stderr: Unknown command: show-paused
- *(... 26 more in this cluster)*

### `empty_list_or_string` — 26 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_priority_system.test_default_priority`
  > IndexError: list index out of range
- `tests.test_comprehensive_coverage.test_priority_sorting_verification`
  > IndexError: list index out of range
- `tests.test_context.test_context_bypass_with_double_dash_on_add`
  > IndexError: list index out of range
- *(... 23 more in this cluster)*

### `rc_mismatch_got0_want2` — 18 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_task_creation.test_add_task_bypass_context`
  > assert 0 == 2
  >  +  where 0 = len([])
- `tests.test_view_commands.test_show_templates_command`
  > assert 0 == 2
  >  +  where 0 = len([])
- `tests.test_viewing_filtering.test_filter_by_tag`
  > assert 0 == 2
  >  +  where 0 = len([])
- *(... 15 more in this cluster)*

### `rc_mismatch_got2_want1` — 15 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_edge_cases.test_operating_on_nonexistent_task`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '99999', 'start'], returncode=2, stdout=b'', stderr=b'Unknown command: 99999\n').returncode
- `tests.test_notes.test_note_on_nonexistent_task`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '99999', 'note', 'Note for missing task'], returncode=2, stdout=b'', stderr=b'Unknown command: 99999\n').returncode
- `tests.test_task_modification.test_modify_invalid_task_id`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '99999', 'modify', '+newtag'], returncode=2, stdout=b'', stderr=b'Unknown command: 99999\n').returncode
- *(... 12 more in this cluster)*

### `boolean_false` — 14 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_priority_system.test_priority_in_filtering`
  > assert False
  >  +  where False = any(<generator object test_priority_in_filtering.<locals>.<genexpr> at 0x7f72bfac7a00>)
- `tests.test_context.test_context_env_var_overrides`
  > assert False
  >  +  where False = any(<generator object test_context_env_var_overrides.<locals>.<genexpr> at 0x7fc1fb9b6500>)
- `tests.test_edge_cases.test_filter_with_text_search`
  > assert False
  >  +  where False = any(<generator object test_filter_with_text_search.<locals>.<genexpr> at 0x7fc1fb890820>)
- *(... 11 more in this cluster)*

### `rc_unexpected_zero` — 14 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_open_and_errors.test_done_already_resolved_task`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '1', 'done'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_subcommand_dispatch.TestSubcommandRequiredArgs.test_add_without_description_fails`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['./executable', 'add'], returncode=0, stdout=b'{"id": 1, "summary": "new task", "status": "active", "priority": "P2", "tags": [], "project": "", "created": "2026-0
- `tests.test_commands_errors.test_add_with_nonexistent_template_id`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'add', 'template:9999'], returncode=0, stdout='{"id": 1, "summary": "template:9999", "status": "active", "priority": "P2", "tags": [], "pr
- *(... 11 more in this cluster)*

### `rc_mismatch_got1_want0` — 12 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_task_modification.test_command_and_id_position_flexibility`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'done', '1'], returncode=1, stdout=b'', stderr=b'Error: task 1 not found\n').returncode
- `tests.test_commands_gaps.test_done_with_note_text`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'done', '1', 'completed successfully with extra notes'], returncode=1, stdout='', stderr='Error: task 1 not found\n').returncode
- `tests.test_commands_gaps.test_modify_multiple_tasks_with_ids`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', 'modify', '1', '2', '+shared'], returncode=1, stdout='', stderr='Error: task 1 not found\n').returncode
- *(... 9 more in this cluster)*

### `string_output_mismatch` — 10 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_main.test_help_output_is_bracketed_empty_list`
  > AssertionError: assert 'dstask - tas...Output JSON\n' == '[]'
  >   
  >   - []
  >   + dstask - task management tool
  >   + 
  >   + Usage:
  >   +   dstask [command] [options]
  >   + ...
- `eval.tests.test_help_main.test_help_precedence_over_invalid_flag`
  > AssertionError: assert 'dstask - tas...Output JSON\n' == '[]'
  >   
  >   - []
  >   + dstask - task management tool
  >   + 
  >   + Usage:
  >   +   dstask [command] [options]
  >   + ...
- `eval.tests.test_usage_and_command_help.test_command_help_is_printed_to_stderr`
  > AssertionError: assert 'dstask - tas...Output JSON\n' == ''
  >   
  >   + dstask - task management tool
  >   + 
  >   + Usage:
  >   +   dstask [command] [options]
  >   + 
  >   + Commands:...
- *(... 7 more in this cluster)*

### `rc_mismatch_got0_want3` — 6 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_view_commands.test_next_command_default`
  > assert 0 == 3
  >  +  where 0 = len([])
- `tests.test_view_commands.test_show_open_command`
  > assert 0 == 3
  >  +  where 0 = len([])
- `tests.test_display_rendering.test_next_command_with_tty_simulation`
  > assert 0 == 3
  >  +  where 0 = len([])
- *(... 3 more in this cluster)*

### `rc_mismatch_got0_want4` — 4 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_task_creation.test_add_task_with_priority`
  > assert 0 == 4
  >  +  where 0 = len([])
- `tests.test_advanced_features.test_priority_sorting`
  > assert 0 == 4
  >  +  where 0 = len([])
- `tests.test_display_rendering.test_mixed_priority_tasks_display`
  > assert 0 == 4
  >  +  where 0 = len([])
- *(... 1 more in this cluster)*

### `type_error` — 4 test(s)

**Quick patch ideas:**
- Specific TypeError; check arg types vs expected

**Sample failures:**

- `tests.test_filtering.TestIdBasedOperations.test_id_before_command`
  > TypeError: object of type 'NoneType' has no len()
- `tests.test_task_creation.TestLogCommand.test_log_simple_task`
  > TypeError: object of type 'NoneType' has no len()
- `tests.test_task_creation.TestLogCommand.test_log_task_with_tags_and_project`
  > TypeError: object of type 'NoneType' has no len()
- *(... 1 more in this cluster)*

### `bytes_output_mismatch` — 3 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_error_handling.test_undo_with_no_commits`
  > AssertionError: assert (2 == 0 or b'error' in b'unknown command: undo\n' or b'nothing' in b'unknown command: undo\n' or b'failed' in b'unknown command: undo\n' or b'fatal' in b'unknown command: undo\n
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'undo', '10'], returncode=2, stdout=b'', stderr=b'Unknown command: undo\n').returncode
  >  +  and   b'unknown command: undo\n' = <built-in method lower of bytes object at 0x7fc1fb8ccef0>()
  >  +    where <built-in method lower of bytes object at 0x7fc1fb8ccef0> = b'Unknown command: undo\n'.lower
  >  +      where b'Unknown command: undo\n' = CompletedProcess(args=['/workspace/executable', 'undo', '10'], returncode=2, stdout=b'', stderr=b'Unknown command: undo\n').stderr
  >  +  and   b'unknown command: undo\n' = <built-in method lower of bytes object at 0x7fc1fb8ccef0>()
  >  +    where <built-in method lower of bytes object at 0x7fc1fb8ccef0> = b'Unknown command: undo\n'.lower
  >  +      where b'Unknown command: undo\n' = CompletedProcess(args=['/workspace/executable', 'undo', '10'], returncode=2, stdout=b'', stderr=b'Unknown command: undo\n').stderr
- `tests.test_git_operations.test_sync_command_exists`
  > AssertionError: assert (b'sync' not in b'unknown command: sync\n' or 2 == 0 or b'remote' in b'unknown command: sync\n')
  >  +  where b'unknown command: sync\n' = <built-in method lower of bytes object at 0x7fc1fb94d4b0>()
  >  +    where <built-in method lower of bytes object at 0x7fc1fb94d4b0> = b'Unknown command: sync\n'.lower
  >  +      where b'Unknown command: sync\n' = CompletedProcess(args=['/workspace/executable', 'sync'], returncode=2, stdout=b'', stderr=b'Unknown command: sync\n').stderr
  >  +  and   2 = CompletedProcess(args=['/workspace/executable', 'sync'], returncode=2, stdout=b'', stderr=b'Unknown command: sync\n').returncode
  >  +  and   b'unknown command: sync\n' = <built-in method lower of bytes object at 0x7fc1fb94d4b0>()
  >  +    where <built-in method lower of bytes object at 0x7fc1fb94d4b0> = b'Unknown command: sync\n'.lower
  >  +      where b'Unknown command: sync\n' = CompletedProcess(args=['/workspace/executable', 'sync'], returncode=2, stdout=b'', stderr=b'Unknown command: sync\n').stderr
- `tests.test_open_and_errors.test_sync_command`
  > AssertionError: assert (2 == 0 or b'remote' in b'unknown command: sync\n')
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', 'sync'], returncode=2, stdout=b'', stderr=b'Unknown command: sync\n').returncode
  >  +  and   b'unknown command: sync\n' = <built-in method lower of bytes object at 0x7fc1fb8474f0>()
  >  +    where <built-in method lower of bytes object at 0x7fc1fb8474f0> = b'Unknown command: sync\n'.lower
  >  +      where b'Unknown command: sync\n' = CompletedProcess(args=['/workspace/executable', 'sync'], returncode=2, stdout=b'', stderr=b'Unknown command: sync\n').stderr

### `rc_mismatch_got1_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_io_behavior.test_version_prints_three_lines_and_exit_0`
  > AssertionError: assert 1 == 3
  >  +  where 1 = len(['dstask version 0.1.0'])

### `rc_mismatch_got0_want20` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_display_git_gaps.test_table_truncation_with_many_tasks`
  > assert 0 == 20
  >  +  where 0 = len([])

### `missing_file` — 1 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_final_80pct_push.test_unmarshal_task_invalid_filename_format`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_unmarshal_task_invalid_fi2/dstask_repo/pending/not-a-uuid.yml'

### `returned_none` — 1 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_dstask_behavior.test_add_task_creates_pending_and_appears_in_show_open`
  > assert None
  >  +  where None = <function search at 0x7fb20fd16680>('Added\\s+1:\\s+Hello world', ('{"id": 1, "summary": "Hello world", "status": "active", "priority": "P2", "tags": [], "project": "", "created": "20
  >  +    where <function search at 0x7fb20fd16680> = re.search
  >  +    and   '{"id": 1, "summary": "Hello world", "status": "active", "priority": "P2", "tags": [], "project": "", "created": "2026-05-18 00:00:53", "modified": "2026-05-18 00:00:53"}\n' = CompletedPro
  >  +    and   '' = CompletedProcess(args=['/workspace/executable', 'add', 'Hello world'], returncode=0, stdout='{"id": 1, "summary": "Hello world", "status": "active", "priority": "P2", "tags": [], "pro

