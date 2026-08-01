# Action Sheet — boyter__scc.515f91c

**Current:** 0.21%  (1/474)
**Pass / Fail / Skip:** 1 / 348 / 1
**Gap to 100%:** 99.79 percentage points (473 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_harvest.test_denylist_gitignore`
  - reason: examples/denylist directory does not exist

## Failure clusters

348 failed tests grouped into 3 buckets (sorted by count).

### `rc_mismatch_got1_want0` — 319 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_analysis.test_complexity_default_enabled`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '/workspace/examples/complexity'], returncode=1, stdout='', stderr='  File "/workspace/main.py", line 223\n    \'complexity_pattern\': r\'
- `tests.test_analysis.test_complexity_disabled_with_no_complexity_flag`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '--no-complexity', '/workspace/examples/complexity'], returncode=1, stdout='', stderr='  File "/workspace/main.py", line 223\n    \'comple
- `tests.test_analysis.test_complexity_disabled_with_short_flag`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-c', '/workspace/examples/complexity'], returncode=1, stdout='', stderr='  File "/workspace/main.py", line 223\n    \'complexity_pattern\
- *(... 316 more in this cluster)*

### `other_assertion` — 25 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_formats.test_json2_locomo_estimates_present`
  > AssertionError:   File "/workspace/main.py", line 223
  >       'complexity_pattern': r'\b(IF|ELSE|END-IF|PERFORM|UNTIL|VARYING|AFTER|FROM|BY|TIMES|THRU|THROUGH|EXIT|PERFORM|CYCLE|GOBACK|STOP|RUN|CALL|USING|BY|REFERENCE|VALUE|CONTENT|LENGTH|ADDRESS|DISPLAY|A
  >                             ^
  >   SyntaxError: unterminated string literal (detected at line 223)
  >   
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '--format', 'json2', '--locomo', '/workspace/examples/language'], returncode=1, stdout='', stderr='  File "/workspace/main.py", line 223\n
- `tests.test_formats.test_sql_locomo_metadata_table_inserted`
  > AssertionError:   File "/workspace/main.py", line 223
  >       'complexity_pattern': r'\b(IF|ELSE|END-IF|PERFORM|UNTIL|VARYING|AFTER|FROM|BY|TIMES|THRU|THROUGH|EXIT|PERFORM|CYCLE|GOBACK|STOP|RUN|CALL|USING|BY|REFERENCE|VALUE|CONTENT|LENGTH|ADDRESS|DISPLAY|A
  >                             ^
  >   SyntaxError: unterminated string literal (detected at line 223)
  >   
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '--format', 'sql', '--locomo', '/workspace/examples/language'], returncode=1, stdout='', stderr='  File "/workspace/main.py", line 223\n  
- `tests.test_formats.test_tabular_no_hborder_removes_horizontal_lines`
  > AssertionError:   File "/workspace/main.py", line 223
  >       'complexity_pattern': r'\b(IF|ELSE|END-IF|PERFORM|UNTIL|VARYING|AFTER|FROM|BY|TIMES|THRU|THROUGH|EXIT|PERFORM|CYCLE|GOBACK|STOP|RUN|CALL|USING|BY|REFERENCE|VALUE|CONTENT|LENGTH|ADDRESS|DISPLAY|A
  >                             ^
  >   SyntaxError: unterminated string literal (detected at line 223)
  >   
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '--no-hborder', '/workspace/examples/language'], returncode=1, stdout='', stderr='  File "/workspace/main.py", line 223\n    \'complexity_
- *(... 22 more in this cluster)*

### `string_output_mismatch` — 4 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_errors.test_nonexistent_directory_fails`
  > AssertionError: assert '' == 'file or dire... /nonexistent'
  >   
  >   - file or directory could not be read: /nonexistent
- `tests.test_errors.test_nonexistent_flags_file_fails`
  > AssertionError: assert '' == 'Error readin... or directory'
  >   
  >   - Error reading flags from a file: open /nonexistent/flags.txt: no such file or directory
- `tests.test_errors.test_invalid_flag_exclude_shows_usage`
  > assert '  File "/wor...t line 223)\n' == 'Error: unkno...mplexity)\n\n'
  >   
  >   +   File "/workspace/main.py", line 223
  >   +     'complexity_pattern': r'\b(IF|ELSE|END-IF|PERFORM|UNTIL|VARYING|AFTER|FROM|BY|TIMES|THRU|THROUGH|EXIT|PERFORM|CYCLE|GOBACK|STOP|RUN|CALL|USING|BY|REFERENCE|VALUE|CONTENT|LENGTH|ADDRESS|DISPLAY
  >   
  >   ...Full output truncated (80 lines hidden), use '-vv' to show
- *(... 1 more in this cluster)*

