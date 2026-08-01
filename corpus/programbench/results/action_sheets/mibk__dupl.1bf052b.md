# Action Sheet — mibk__dupl.1bf052b

**Current:** 16.37%  (83/507)
**Pass / Fail / Skip:** 83 / 367 / 0
**Gap to 100%:** 83.63 percentage points (424 tests)

## Failure clusters

367 failed tests grouped into 9 buckets (sorted by count).

### `other_assertion` — 227 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_dupl.test_single_file_path`
  > AssertionError: assert b'Found total' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', 'main.go'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_dupl.test_directory_path`
  > AssertionError: assert b'Found total' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', 'printer/'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_dupl.test_multiple_paths`
  > AssertionError: assert b'Found total' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', 'main.go', 'printer/'], returncode=0, stdout=b'', stderr=b'').stdout
- *(... 224 more in this cluster)*

### `string_output_mismatch` — 65 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `eval.tests.test_help_usage.test_help_output_goes_to_stderr_and_not_stdout`
  > AssertionError: assert 'dupl 0.1.0\n...    Quiet\n\n' == ''
  >   
  >   + dupl 0.1.0
  >   + 
  >   + usage: dupl [OPTIONS] [ARGS]
  >   + 
  >   + Options:
  >   +   -h, --help     Print help...
- `eval.tests.test_help_usage.test_baseline_help_text_matches_fixture_exactly`
  > AssertionError: assert '' == 'Usage: dupl ...e as above.\n'
  >   
  >   - Usage: dupl [flags] [paths]
  >   - 
  >   - Paths:
  >   -   If the given path is a file, dupl will use it regardless of
  >   -   the file extension. If it is a directory, it will recursively
  >   -   search for *.go files in that directory....
- `eval.tests.test_core_outputs.test_text_output_single_group_and_summary`
  > AssertionError: assert '' == 'found 2 clon...one groups.\n'
  >   
  >   - found 2 clones:
  >   -   a.go:1,9
  >   -   b.go:1,9
  >   - 
  >   - Found total 1 clone groups.
- *(... 62 more in this cluster)*

### `rc_mismatch_got0_want2` — 26 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_dupl.test_help_flag`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--help'], returncode=0, stdout=b'dupl 0.1.0\n\nusage: dupl [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Pr
- `tests.test_dupl.test_h_flag`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-h'], returncode=0, stdout=b'dupl 0.1.0\n\nusage: dupl [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print 
- `tests.test_dupl.test_invalid_threshold_value`
  > AssertionError: assert 0 == 2
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-t', 'abc'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 23 more in this cluster)*

### `rc_mismatch_got2_want0` — 18 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_dupl.test_no_args_default_behavior`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b'usage: dupl [OPTIONS] [ARGS]\n').returncode
- `tests.test_dupl.test_vendor_flag`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b'usage: dupl [OPTIONS] [ARGS]\n').returncode
- `tests.test_dupl.test_empty_directory`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b'usage: dupl [OPTIONS] [ARGS]\n').returncode
- *(... 15 more in this cluster)*

### `rc_mismatch_got0_want1` — 11 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_dupl.test_conflicting_html_plumbing_flags`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-html', '-plumbing', 'syntax/'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_dupl.test_nonexistent_file`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'nonexistent_file_xyz.go'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_dupl.test_nonexistent_directory`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'nonexistent_dir_xyz/'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 8 more in this cluster)*

### `rc_unexpected_zero` — 11 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_dupl.test_nonexistent_path`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/nonexistent/path/to/file.go'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_dupl.test_html_and_plumbing_conflict`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '-html', '-plumbing', '/tmp/tmpk2unide1/test.go'], returncode=0, stdout=b'', stderr=b'').returncode
- `eval.tests.test_args.test_flag_after_positional_is_rejected_as_unknown_flag`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', './syntax', '-t', '15'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 8 more in this cluster)*

### `boolean_false` — 5 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `eval.tests.test_help_usage.test_help_has_trailing_newline`
  > AssertionError: assert False
  >  +  where False = <built-in method endswith of str object at 0x7f3f83a14030>('\n')
  >  +    where <built-in method endswith of str object at 0x7f3f83a14030> = ''.endswith
  >  +      where '' = CompletedProcess(args=['/workspace/executable', '--help'], returncode=0, stdout='dupl 0.1.0\n\nusage: dupl [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version
- `eval.tests.test_dupl_io.test_no_clones_prints_summary_and_exit_0`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7f42833f4030>('Found total 0 clone groups.')
  >  +    where <built-in method startswith of str object at 0x7f42833f4030> = ''.startswith
  >  +      where '' = <built-in method lstrip of str object at 0x7f42833f4030>()
  >  +        where <built-in method lstrip of str object at 0x7f42833f4030> = ''.lstrip
  >  +          where '' = <built-in method decode of bytes object at 0x7f42833f0030>('utf-8', errors='replace')
  >  +            where <built-in method decode of bytes object at 0x7f42833f0030> = b''.decode
  >  +              where b'' = CompletedProcess(args=['/workspace/executable', '-t', '10', '/tmp/pytest-of-root/pytest-0/test_no_clones_prints_summary_2/b.go'], returncode=0, stdout=b'', stderr=b'').stdo
- `eval.tests.test_dupl_io.test_html_output_starts_with_doctype_and_contains_code`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7f42833f4030>('<!DOCTYPE html>\n')
  >  +    where <built-in method startswith of str object at 0x7f42833f4030> = ''.startswith
- *(... 2 more in this cluster)*

### `returned_none` — 3 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_dupl.test_summary_line_format`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f39b3a72680>('Found total \\d+ clone groups?\\.', '')
  >  +    where <function search at 0x7f39b3a72680> = re.search
- `eval.tests.test_help_usage.test_help_documents_threshold_default_value`
  > AssertionError: assert None
  >  +  where None = <function search at 0x7f3f83986680>('default\\s+15', '')
  >  +    where <function search at 0x7f3f83986680> = re.search
- `tests.test_output_formats.test_threshold_html_combination`
  > assert None is not None
  >  +  where None = <test_output_formats.DuplHTMLParser object at 0x7f02aa293880>.doctype

### `empty_list_or_string` — 1 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `eval.tests.test_help_usage.test_help_usage_line_present_and_exact`
  > IndexError: list index out of range

