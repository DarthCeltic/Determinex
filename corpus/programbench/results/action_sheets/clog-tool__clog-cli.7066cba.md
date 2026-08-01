# Action Sheet — clog-tool__clog-cli.7066cba

**Current:** 19.75%  (204/1033)
**Pass / Fail / Skip:** 204 / 574 / 0
**Gap to 100%:** 80.25 percentage points (829 tests)

## Failure clusters

574 failed tests grouped into 13 buckets (sorted by count).

### `other_assertion` — 227 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_clog.test_version_flag`
  > AssertionError: assert b'clog' in b'usage\n'
  >  +  where b'usage\n' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'usage\n', stderr=b'').stdout
- `tests.test_clog.test_version_short_flag`
  > AssertionError: assert b'clog' in b''
  >  +  where b'' = CompletedProcess(args=['/workspace/executable', '-V'], returncode=0, stdout=b'', stderr=b'').stdout
- `tests.test_clog.test_help_flag`
  > AssertionError: assert b'conventional changelog' in b'usage\n'
  >  +  where b'usage\n' = CompletedProcess(args=['/workspace/executable', '--help'], returncode=0, stdout=b'usage\n', stderr=b'').stdout
- *(... 224 more in this cluster)*

### `boolean_false` — 86 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `tests.test_clog.test_output_to_file`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/pytest-of-root/pytest-0/test_output_to_file2/test_repo/CHANGELOG.md').exists
- `tests.test_clog.test_infile_appends_content`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/pytest-of-root/pytest-0/test_infile_appends_content2/test_repo/new_changelog.md').exists
- `tests.test_clog.test_json_format`
  > AssertionError: assert False
  >  +  where False = exists()
  >  +    where exists = PosixPath('/tmp/pytest-of-root/pytest-0/test_json_format2/test_repo/output.json').exists
- *(... 83 more in this cluster)*

### `rc_unexpected_zero` — 61 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_clog.test_changelog_conflicts_with_outfile`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--changelog', '/tmp/pytest-of-root/pytest-0/test_changelog_conflicts_with_2/test_repo/CHANGELOG.md', '--outfile', '/tmp/pytest-of-root/py
- `tests.test_clog.test_changelog_conflicts_with_infile`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--changelog', '/tmp/pytest-of-root/pytest-0/test_changelog_conflicts_with_5/test_repo/CHANGELOG.md', '--infile', '/tmp/pytest-of-root/pyt
- `tests.test_clog.test_from_conflicts_with_from_latest_tag`
  > assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '--from', 'abc123', '--from-latest-tag'], returncode=0, stdout=b"error: the argument '--from <COMMIT>' cannot be used with '--from-latest-
- *(... 58 more in this cluster)*

### `rc_mismatch_got0_want2` — 61 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `tests.test_argument_parsing.TestUnknownFlags.test_unknown_long_flag`
  > assert 0 == 2
- `tests.test_argument_parsing.TestUnknownFlags.test_unknown_short_flag`
  > assert 0 == 2
- `tests.test_argument_parsing.TestUnknownFlags.test_misspelled_flag`
  > assert 0 == 2
- *(... 58 more in this cluster)*

### `string_output_mismatch` — 60 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_config_errors.test_invalid_toml_syntax_missing_bracket`
  > AssertionError: assert '' == 'error: Faile...guration file'
  >   
  >   - error: Failed to parse TOML configuration file
- `tests.test_config_errors.test_malformed_toml_unclosed_string`
  > AssertionError: assert '' == 'error: Faile...guration file'
  >   
  >   - error: Failed to parse TOML configuration file
- `tests.test_config_errors.test_empty_toml_file`
  > AssertionError: assert '' == 'error: Faile...guration file'
  >   
  >   - error: Failed to parse TOML configuration file
- *(... 57 more in this cluster)*

### `rc_mismatch_got0_want1` — 31 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_argument_parsing.TestShortFlagEquivalents.test_short_long_equivalence[-M---major-None]`
  > assert 0 == 1
- `tests.test_argument_parsing.TestShortFlagEquivalents.test_short_long_equivalence[-m---minor-None]`
  > assert 0 == 1
- `tests.test_argument_parsing.TestShortFlagEquivalents.test_short_long_equivalence[-c---config-.clog.toml]`
  > assert 0 == 1
- *(... 28 more in this cluster)*

### `returned_none` — 18 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_help_output.test_help_documents_short_flag[-r]`
  > AssertionError: assert None is not None
  >  +  where None = <function search at 0x7f688605e680>('(^|\\s)\\-r(\\s|,)', 'usage\n')
  >  +    where <function search at 0x7f688605e680> = re.search
- `eval.tests.test_help_output.test_help_documents_short_flag[-f]`
  > AssertionError: assert None is not None
  >  +  where None = <function search at 0x7f688605e680>('(^|\\s)\\-f(\\s|,)', 'usage\n')
  >  +    where <function search at 0x7f688605e680> = re.search
- `eval.tests.test_help_output.test_help_documents_short_flag[-T]`
  > AssertionError: assert None is not None
  >  +  where None = <function search at 0x7f688605e680>('(^|\\s)\\-T(\\s|,)', 'usage\n')
  >  +    where <function search at 0x7f688605e680> = re.search
- *(... 15 more in this cluster)*

### `rc_mismatch_got1_want0` — 14 test(s)

**Quick patch ideas:**
- Tool is over-erroring on valid input; relax error condition
- Specifically check what input triggers rc=1 in golden

**Sample failures:**

- `tests.test_clog.test_runs_without_git_if_config_present`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable'], returncode=1, stdout=b'', stderr=b"Error: could not find repository at '.'; class=Repository (6); code=NotFound (-3)\n").returncode
- `tests.test_clog.test_output_short_flag`
  > AssertionError: assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '-o', '/tmp/pytest-of-root/pytest-0/test_output_short_flag2/test_repo/CHANGELOG2.md'], returncode=1, stdout=b'', stderr=b'').returncode
- `tests.test_clog.test_work_tree_flag`
  > assert 1 == 0
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '--work-tree', '/tmp/pytest-of-root/pytest-0/test_work_tree_flag2/test_repo', '--config', '/tmp/pytest-of-root/pytest-0/test_work_tree_fla
- *(... 11 more in this cluster)*

### `missing_file` — 11 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_file_io.test_infile_and_outfile_combination`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_infile_and_outfile_combin2/new_changelog.md'
- `tests.test_file_io.test_empty_infile_preserves_structure`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_empty_infile_preserves_st2/out.md'
- `tests.test_file_io.test_multiple_changelog_append_operations`
  > FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pytest-of-root/pytest-0/test_multiple_changelog_append2/CHANGELOG.md'
- *(... 8 more in this cluster)*

### `json_output_missing_or_bad` — 2 test(s)

**Quick patch ideas:**
- Add `--format json` flag; emit `json.dumps()` of result dict

**Sample failures:**

- `tests.test_git_ops.test_from_latest_tag_json_format`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
- `tests.test_git_ops.test_json_format_structure`
  > json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

### `bytes_output_mismatch` — 1 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_simple_coverage_boost.test_major_version_attempt`
  > AssertionError: assert (1 == 0 or b'SemVer' in b'' or b'version' in b'')
  >  +  where 1 = CompletedProcess(args=['/workspace/executable', '--major'], returncode=1, stdout=b'', stderr=b'').returncode
  >  +  and   b'' = CompletedProcess(args=['/workspace/executable', '--major'], returncode=1, stdout=b'', stderr=b'').stderr
  >  +  and   b'' = <built-in method lower of bytes object at 0x7f9b5069c030>()
  >  +    where <built-in method lower of bytes object at 0x7f9b5069c030> = b''.lower
  >  +      where b'' = CompletedProcess(args=['/workspace/executable', '--major'], returncode=1, stdout=b'', stderr=b'').stderr

### `rc_mismatch_got1_want2` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_argument_parsing.TestFilePathFlags.test_path_flags_missing_value[--config]`
  > assert 1 == 2

### `uncategorized` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_file_io.test_outfile_prepends_to_existing_file`
  > ValueError: substring not found

