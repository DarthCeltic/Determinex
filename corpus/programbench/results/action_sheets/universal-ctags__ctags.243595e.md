# Action Sheet — universal-ctags__ctags.243595e

**Current:** 2.11%  (55/2606)
**Pass / Fail / Skip:** 55 / 550 / 27
**Gap to 100%:** 97.89 percentage points (2551 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_harvest_tmain1.test_tmain[broken-json-output.d]`
  - reason: feature "json" is not available in /workspace/executable
- `tests.test_harvest_tmain1.test_tmain[broken-version.d]`
  - reason: feature "debug" is not available in /workspace/executable
- `tests.test_harvest_tmain1.test_tmain[case-insensitive-pattern.d]`
  - reason: feature "case-insensitive-filenames" is not available in /workspace/executable
- `tests.test_harvest_tmain1.test_tmain[client-vista-vim-fields-expectation.d]`
  - reason: feature "json" is not available in /workspace/executable
- `tests.test_harvest_tmain1.test_tmain[fixed-field-handling-in-json-format.d]`
  - reason: feature "json" is not available in /workspace/executable
- *(... 22 more skipped)*

## Failure clusters

550 failed tests grouped into 5 buckets (sorted by count).

### `rc_mismatch_got2_want0` — 329 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_coverage.test_ada_parsing`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--quiet', '--options=NONE', '-o', '-', '/tmp/tmpruy3l0nm/test.ads'], returncode=2, stdout=b'', stderr=b"ctags: unknown option: --quiet\nusage: cta
- `tests.test_coverage.test_julia_parsing`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--quiet', '--options=NONE', '-o', '-', '/tmp/tmpdl3ors4u/test.jl'], returncode=2, stdout=b'', stderr=b"ctags: unknown option: --quiet\nusage: ctag
- `tests.test_coverage.test_r_parsing`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable', '--quiet', '--options=NONE', '-o', '-', '/tmp/tmps8bu55mg/test.R'], returncode=2, stdout=b'', stderr=b"ctags: unknown option: --quiet\nusage: ctags
- *(... 326 more in this cluster)*

### `other_assertion` — 145 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_ctags.test_version_output`
  > AssertionError: assert b'Universal Ctags' in b'ctags 0.1.0\n'
  >  +  where b'ctags 0.1.0\n' = CompletedProcess(args=['./executable', '--version'], returncode=0, stdout=b'ctags 0.1.0\n', stderr=b'').stdout
- `tests.test_ctags.test_version_output_format`
  > AssertionError: assert b'Compiled:' in b'ctags 0.1.0\n'
  >  +  where b'ctags 0.1.0\n' = CompletedProcess(args=['./executable', '--version'], returncode=0, stdout=b'ctags 0.1.0\n', stderr=b'').stdout
- `tests.test_ctags.test_help_output`
  > AssertionError: assert b'[options]' in b'ctags 0.1.0 - bootstrap scaffold\n\nUsage: ctags [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n'
  >  +  where b'ctags 0.1.0 - bootstrap scaffold\n\nUsage: ctags [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = CompletedProcess(args=['./executable', '--he
- *(... 142 more in this cluster)*

### `uncategorized` — 55 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_harvest_tmain3.test_tmain[nameless-long-option.d]`
  > Failed: nameless-long-option.d: stderr mismatch, exit mismatch
- `tests.test_harvest_tmain3.test_tmain[nested-mio.d]`
  > Failed: nested-mio.d: stdout mismatch, exit mismatch
- `tests.test_harvest_tmain3.test_tmain[nested-subparsers-multilines.d]`
  > Failed: nested-subparsers-multilines.d: stdout mismatch
- *(... 52 more in this cluster)*

### `rc_mismatch_got2_want1` — 20 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_ctags.test_no_args_exit_code`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['./executable'], returncode=2, stdout=b'', stderr=b"usage: ctags [OPTIONS] [ARGS]\nTry 'ctags --help' for more information.\n").returncode
- `tests.test_ctags.test_invalid_option`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['./executable', '--totally-invalid-option-xyz'], returncode=2, stdout=b'', stderr=b"ctags: unknown option: --totally-invalid-option-xyz\nusage: ctags [OPTIONS] [AR
- `tests.test_errors_edge.test_unknown_long_option`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--invalid-option'], returncode=2, stdout='', stderr="ctags: unknown option: --invalid-option\nusage: ctags [OPTIONS] [ARGS]\nTry 'ctags -
- *(... 17 more in this cluster)*

### `rc_mismatch_got0_want1` — 1 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_errors_edge.test_dash_as_option_not_stdin`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-'], returncode=0, stdout='', stderr='').returncode

