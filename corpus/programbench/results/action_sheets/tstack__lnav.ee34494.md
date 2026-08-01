# Action Sheet — tstack__lnav.ee34494

**Current:** 0.4%  (4/1005)
**Pass / Fail / Skip:** 4 / 346 / 0
**Gap to 100%:** 99.60 percentage points (1001 tests)

## Failure clusters

346 failed tests grouped into 3 buckets (sorted by count).

### `other_assertion` — 258 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_all_ids_vtabs.test_all_opids_basic_access_log`
  > AssertionError: lnav: unknown option: -n
  >   usage: lnav [OPTIONS] [ARGS]
  >   Try 'lnav --help' for more information.
  >   
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-n', '-c', ';SELECT * FROM all_opids ORDER BY earliest', '/workspace/eval/test_resources/test_all_ids_vtabs/access.log'], returncode=2, s
- `tests.test_all_ids_vtabs.test_all_opids_java_with_explicit_opid`
  > AssertionError: lnav: unknown option: -n
  >   usage: lnav [OPTIONS] [ARGS]
  >   Try 'lnav --help' for more information.
  >   
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-n', '-c', ';SELECT * FROM all_opids', '/workspace/eval/test_resources/test_all_ids_vtabs/java_with_opid.log'], returncode=2, stdout='', 
- `tests.test_all_ids_vtabs.test_all_opids_stats_aggregation`
  > AssertionError: lnav: unknown option: -n
  >   usage: lnav [OPTIONS] [ARGS]
  >   Try 'lnav --help' for more information.
  >   
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-n', '-c', ';SELECT opid, errors, warnings, total FROM all_opids ORDER BY opid', '/workspace/eval/test_resources/test_all_ids_vtabs/java_
- *(... 255 more in this cluster)*

### `rc_mismatch_got2_want0` — 79 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_all_ids_vtabs.test_all_thread_ids_update_rejected`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-n', '-c', ';UPDATE all_thread_ids SET total = 99 WHERE thread_id = "worker-1"', '/workspace/eval/test_resources/test_all_ids_vtabs/java_
- `tests.test_basic_smoke.test_headless_stdin`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-n'], returncode=2, stdout='', stderr="lnav: unknown option: -n\nusage: lnav [OPTIONS] [ARGS]\nTry 'lnav --help' for more information.\n"
- `tests.test_breakpoints.test_breakpoint_invalid_format`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-n', '-c', ':breakpoint bad', '/workspace/eval/test_resources/test_breakpoints/logfile_glog.0'], returncode=2, stdout='', stderr="lnav: u
- *(... 76 more in this cluster)*

### `string_output_mismatch` — 9 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_breadcrumb_curses.test_breadcrumb_initial_focus`
  > AssertionError: assert '\n\n\n\n\n\n...02:15 2026)\n' == ' DATETIME UT...or messages\n'
  >   
  >   -  DATETIME UTC                Press ` to focus on the breadcrumb bar
  >   -  LOG ▼  :2024-01-15T10:00:02.456000 :rust_tracing_log :simple.log[4] :#x1F9F5 ⋯
  >   - LOG      (1 file)    xe                                                        x
  >   - PRETTY               xINFO ] (-         ) -                                    x
  >   - SCHEMA               x                                                         x
  >   - SPECTRO              xDEBUG] (-         ) -                                    x...
- `tests.test_breadcrumb_curses.test_breadcrumb_navigate_right`
  > AssertionError: assert '\n\n\n\n\n\n...02:33 2026)\n' == ' DATETIME UT...or messages\n'
  >   
  >   -  DATETIME UTC                Press ` to focus on the breadcrumb bar
  >   -  LOG ▼  :2024-01-15T10:00:02.456000 :rust_tracing_log :simple.log[4] :#x1F9F5 ⋯
  >   -  No messag(Enter an absolute or relative time)  x                              x
  >   - l2024-01-1+1 day                                x                              x
  >   - x  message+1h                                   x                              x
  >   - x2024-01-1+1m                                   x                              x...
- `tests.test_breadcrumb_curses.test_breadcrumb_navigate_left`
  > AssertionError: assert '\n\n\n\n\n\n...02:53 2026)\n' == ' DATETIME UT...or messages\n'
  >   
  >   -  DATETIME UTC                Press ` to focus on the breadcrumb bar
  >   -  LOG ▼  :2024-01-15T10:00:02.456000 :rust_tracing_log :simple.log[4] :#x1F9F5 ⋯
  >   - LOG      (1 file)    xe                                                        x
  >   - PRETTY               xINFO ] (-         ) -                                    x
  >   - SCHEMA               x                                                         x
  >   - SPECTRO              xDEBUG] (-         ) -                                    x...
- *(... 6 more in this cluster)*

