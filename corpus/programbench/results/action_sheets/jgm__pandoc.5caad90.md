# Action Sheet — jgm__pandoc.5caad90

**Current:** 0.02%  (1/5482)
**Pass / Fail / Skip:** 1 / 603 / 0
**Gap to 100%:** 99.98 percentage points (5481 tests)

## Failure clusters

603 failed tests grouped into 4 buckets (sorted by count).

### `rc_mismatch_got2_want0` — 399 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_pandoc.test_version_short_flag`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-v'], returncode=2, stdout=b'', stderr=b"pandoc: unknown option: -v\nusage: pandoc [OPTIONS] [ARGS]\nTry 'pandoc --help' for more informa
- `tests.test_pandoc.test_no_args_reads_stdin`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b"usage: pandoc [OPTIONS] [ARGS]\nTry 'pandoc --help' for more information.\n").returncode
- `tests.test_pandoc.test_list_input_formats`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--list-input-formats'], returncode=2, stdout=b'', stderr=b"pandoc: unknown option: --list-input-formats\nusage: pandoc [OPTIONS] [ARGS]\n
- *(... 396 more in this cluster)*

### `other_assertion` — 201 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_pandoc.test_version_output`
  > AssertionError: assert b'3.' in b'pandoc 2.19.2\n'
  >  +  where b'pandoc 2.19.2\n' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'pandoc 2.19.2\n', stderr=b'').stdout
- `tests.test_pandoc.test_help_output`
  > AssertionError: assert b'--from' in b'pandoc 2.19.2 - a universal document converter\n\nUsage: pandoc [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n'
  >  +  where b'pandoc 2.19.2 - a universal document converter\n\nUsage: pandoc [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['/work
- `tests.test_pandoc.test_help_short_flag`
  > AssertionError: assert b'--from' in b'pandoc 2.19.2 - a universal document converter\n\nUsage: pandoc [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n'
  >  +  where b'pandoc 2.19.2 - a universal document converter\n\nUsage: pandoc [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['/work
- *(... 198 more in this cluster)*

### `string_output_mismatch` — 2 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_abbreviations.test_nonexistent_abbreviations_file`
  > AssertionError: assert 'pandoc: unkn... information.' == 'executable: ...or directory)'
  >   
  >   - executable: /nonexistent/file.txt: withBinaryFile: does not exist (No such file or directory)
  >   + pandoc: unknown option: --abbreviations=/nonexistent/file.txt
  >   + usage: pandoc [OPTIONS] [ARGS]
  >   + Try 'pandoc --help' for more information.
- `tests.test_advanced_citations.test_malformed_bibtex_error_handling`
  > assert 'pandoc: unkn...nformation.\n' == 'Error at "ma...Jane},\n  ^\n'
  >   
  >   + pandoc: unknown option: --from=bibtex
  >   + usage: pandoc [OPTIONS] [ARGS]
  >   + Try 'pandoc --help' for more information.
  >   - Error at "malformed.bib" (line 9, column 3):
  >   - unexpected 'a'
  >   -   author = {Jones, Jane},

### `bytes_output_mismatch` — 1 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_pandoc.test_biblatex_writer`
  > assert (2 == 0 or b'error' in b"pandoc: unknown option: -f\nusage: pandoc [options] [args]\ntry 'pandoc --help' for more information.\n")
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-f', 'markdown', '-t', 'biblatex', '--bibliography=/dev/null'], returncode=2, stdout=b'', stderr=b"pandoc: unknown option: -f\nusage: pan
  >  +  and   b"pandoc: unknown option: -f\nusage: pandoc [options] [args]\ntry 'pandoc --help' for more information.\n" = <built-in method lower of bytes object at 0x7f90d7606790>()
  >  +    where <built-in method lower of bytes object at 0x7f90d7606790> = b"pandoc: unknown option: -f\nusage: pandoc [OPTIONS] [ARGS]\nTry 'pandoc --help' for more information.\n".lower
  >  +      where b"pandoc: unknown option: -f\nusage: pandoc [OPTIONS] [ARGS]\nTry 'pandoc --help' for more information.\n" = CompletedProcess(args=['/workspace/executable', '-f', 'markdown', '-t', 'bibl

