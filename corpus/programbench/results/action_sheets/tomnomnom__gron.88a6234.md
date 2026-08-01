# Action Sheet — tomnomnom__gron.88a6234

**Current:** 0.86%  (2/233)
**Pass / Fail / Skip:** 2 / 231 / 0
**Gap to 100%:** 99.14 percentage points (231 tests)

## Failure clusters

231 failed tests grouped into 5 buckets (sorted by count).

### `other_assertion` — 107 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_gaps.test_json_format_basic`
  > AssertionError: Expected exit code 0, got 2: gron: unknown option: --json
  >   usage: gron [OPTIONS] [ARGS]
  >   Try 'gron --help' for more information.
  >   
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--json'], returncode=2, stdout='', stderr="gron: unknown option: --json\nusage: gron [OPTIONS] [ARGS]\nTry 'gron --help' for more informa
- `tests.test_gaps.test_stream_json_format`
  > AssertionError: Expected exit code 0, got 2: gron: unknown option: --stream
  >   usage: gron [OPTIONS] [ARGS]
  >   Try 'gron --help' for more information.
  >   
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--stream', '--json'], returncode=2, stdout='', stderr="gron: unknown option: --stream\nusage: gron [OPTIONS] [ARGS]\nTry 'gron --help' fo
- `tests.test_gaps.test_stream_basic_multiline`
  > AssertionError: Expected exit code 0, got 2: gron: unknown option: --stream
  >   usage: gron [OPTIONS] [ARGS]
  >   Try 'gron --help' for more information.
  >   
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--stream', '-m'], returncode=2, stdout='', stderr="gron: unknown option: --stream\nusage: gron [OPTIONS] [ARGS]\nTry 'gron --help' for mo
- *(... 104 more in this cluster)*

### `rc_mismatch_got2_want0` — 100 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_gaps.test_stream_with_monochrome_flag`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--stream', '-m'], returncode=2, stdout='', stderr="gron: unknown option: --stream\nusage: gron [OPTIONS] [ARGS]\nTry 'gron --help' for mo
- `tests.test_gaps.test_large_nested_json_format`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--json'], returncode=2, stdout='', stderr="gron: unknown option: --json\nusage: gron [OPTIONS] [ARGS]\nTry 'gron --help' for more informa
- `tests.test_gaps.test_values_extraction_with_escaped_strings`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--values'], returncode=2, stdout='', stderr="gron: unknown option: --values\nusage: gron [OPTIONS] [ARGS]\nTry 'gron --help' for more inf
- *(... 97 more in this cluster)*

### `rc_mismatch_got2_want5` — 11 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_harvest.test_ungron_invalid_type_mismatch`
  > assert 2 == 5
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--ungron', '-m', '/workspace/testdata/invalid-type-mismatch.gron'], returncode=2, stdout='', stderr="gron: unknown option: --ungron\nusag
- `tests.test_harvest.test_ungron_invalid_value`
  > assert 2 == 5
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--ungron', '-m', '/workspace/testdata/invalid-value.gron'], returncode=2, stdout='', stderr="gron: unknown option: --ungron\nusage: gron 
- `tests.test_integration.test_ungron_negative_array_index_error`
  > assert 2 == 5
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-u', '-m'], returncode=2, stdout='', stderr="gron: unknown option: -u\nusage: gron [OPTIONS] [ARGS]\nTry 'gron --help' for more informati
- *(... 8 more in this cluster)*

### `string_output_mismatch` — 7 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_gaps.test_colorize_json_output_ungron`
  > assert 'gron: unknow...nformation.\n' == '\x1b[35m{\x1...35m}\x1b[0m\n'
  >   
  >   - #x1B[35m{#x1B[0m#x1B[34;1m"#x1B[0;22m#x1B[34;1ma#x1B[0;22m#x1B[34;1m"#x1B[0;22m#x1B[1m:#x1B[22m#x1B[31m1#x1B[0m#x1B[1m,#x1B[22m#x1B[34;1m"#x1B[0;22m#x1B[34;1mb#x1B[0;22m#x1B[34;1m"#x1B[0;22m#x1B[1
  >   + gron: unknown option: --ungron
  >   + usage: gron [OPTIONS] [ARGS]
  >   + Try 'gron --help' for more information.
- `tests.test_gaps.test_colorize_gron_output`
  > assert '' == '\x1b[34;1mjs...st"\x1b[0m;\n'
  >   
  >   - #x1B[34;1mjson#x1B[0;22m = #x1B[35m{}#x1B[0m;
  >   - #x1B[34;1mjson#x1B[0;22m.#x1B[34;1ma#x1B[0;22m = #x1B[31m1#x1B[0m;
  >   - #x1B[34;1mjson#x1B[0;22m.#x1B[34;1mb#x1B[0;22m = #x1B[33m"test"#x1B[0m;
- `tests.test_gron_core.test_version_flag`
  > AssertionError: assert 'gron 0.1.0\n' == 'gron version dev\n'
  >   
  >   - gron version dev
  >   + gron 0.1.0
- *(... 4 more in this cluster)*

### `rc_mismatch_got2_want3` — 6 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_integration.test_stream_mode_with_mixed_valid_invalid_json`
  > assert 2 == 3
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-s', '-m', '/workspace/eval/test_resources/test_integration/stream_input.jsonl'], returncode=2, stdout='', stderr="gron: unknown option: 
- `tests.test_output_modes.test_json_mode_invalid_json_error`
  > assert 2 == 3
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-j', '-m'], returncode=2, stdout='', stderr="gron: unknown option: -j\nusage: gron [OPTIONS] [ARGS]\nTry 'gron --help' for more informati
- `tests.test_stream.test_stream_empty_line_fails`
  > assert 2 == 3
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-s', '-m'], returncode=2, stdout='', stderr="gron: unknown option: -s\nusage: gron [OPTIONS] [ARGS]\nTry 'gron --help' for more informati
- *(... 3 more in this cluster)*

