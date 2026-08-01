# Action Sheet — johnkerl__miller.8d85b46

**Current:** 0.82%  (130/15786)
**Pass / Fail / Skip:** 130 / 1618 / 2
**Gap to 100%:** 99.18 percentage points (15656 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `tests.test_subcommand_dispatch.TestUnknownVerb.test_various_invalid_verbs[]`
  - reason: Empty string handling varies
- `tests.test_subcommand_dispatch.TestUnknownVerb.test_various_invalid_verbs[  ]`
  - reason: Empty string handling varies

## Failure clusters

1618 failed tests grouped into 13 buckets (sorted by count).

### `other_assertion` — 734 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_absolute_final.test_a1`
  > assert 0 > 0
  >  +  where 0 = len(b'')
  >  +    where b'' = CompletedProcess(args=['/workspace/executable', '--csv', 'cat'], returncode=2, stdout=b'', stderr=b"miller: unknown option: --csv\nusage: miller [OPTIONS] [ARGS]\nTry 'miller --help'
- `tests.test_absolute_final.test_a2`
  > assert 0 > 0
  >  +  where 0 = len(b'')
  >  +    where b'' = CompletedProcess(args=['/workspace/executable', '--csv', 'head', '-n', '2'], returncode=2, stdout=b'', stderr=b"miller: unknown option: --csv\nusage: miller [OPTIONS] [ARGS]\nTry 'mi
- `tests.test_absolute_final.test_a3`
  > assert 0 > 0
  >  +  where 0 = len(b'')
  >  +    where b'' = CompletedProcess(args=['/workspace/executable', '--csv', 'tail', '-n', '2'], returncode=2, stdout=b'', stderr=b"miller: unknown option: --csv\nusage: miller [OPTIONS] [ARGS]\nTry 'mi
- *(... 731 more in this cluster)*

### `rc_mismatch_got2_want0` — 422 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `tests.test_absolute_final.test_a11`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--csv', 'sort', '-n', 'x'], returncode=2, stdout=b'', stderr=b"miller: unknown option: --csv\nusage: miller [OPTIONS] [ARGS]\nTry 'miller
- `tests.test_absolute_final.test_a12`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--csv', 'sort', '-nr', 'x'], returncode=2, stdout=b'', stderr=b"miller: unknown option: --csv\nusage: miller [OPTIONS] [ARGS]\nTry 'mille
- `tests.test_absolute_final.test_a19`
  > assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--csv', 'tac'], returncode=2, stdout=b'', stderr=b"miller: unknown option: --csv\nusage: miller [OPTIONS] [ARGS]\nTry 'miller --help' for
- *(... 419 more in this cluster)*

### `missing_file` — 283 test(s)

**Quick patch ideas:**
- Scaffold not creating expected output file; check write logic

**Sample failures:**

- `tests.test_all_verbs_systematic.test_split_verb`
  > FileNotFoundError: [Errno 2] No such file or directory: './executable'
- `tests.test_all_verbs_systematic.test_stats1_with_group`
  > FileNotFoundError: [Errno 2] No such file or directory: './executable'
- `tests.test_all_verbs_systematic.test_stats2_verb`
  > FileNotFoundError: [Errno 2] No such file or directory: './executable'
- *(... 280 more in this cluster)*

### `string_output_mismatch` — 139 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_config_mlrrc.test_home_mlrrc_is_loaded_by_default`
  > AssertionError: assert '' == 'a=1,b=2'
  >   
  >   - a=1,b=2
- `tests.test_config_mlrrc.test_home_and_cwd_mlrrc_are_stacked`
  > AssertionError: assert '' == 'a b\n1 2'
  >   
  >   - a b
  >   - 1 2
- `eval.tests.test_help_main.test_help_command_matches_double_dash_help`
  > AssertionError: assert '' == 'miller 0.1.0...int version\n'
  >   
  >   - miller 0.1.0 - bootstrap scaffold
  >   - 
  >   - Usage: miller [OPTIONS] [ARGS]
  >   - 
  >   - Options:
  >   -   -h, --help     Print help
- *(... 136 more in this cluster)*

### `rc_unexpected_zero` — 10 test(s)

**Quick patch ideas:**
- Tool returns success on invalid input; add validation

**Sample failures:**

- `tests.test_basic_invocation.test_invalid_verb_shows_error`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'nonexistent_verb'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_config_mlrrc.test_malformed_mlrrc_line_exits_nonzero_with_parse_error`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'cat'], returncode=0, stdout='', stderr='').returncode
- `tests.test_config_mlrrc.test_disallowed_prepipe_in_mlrrc_is_rejected`
  > AssertionError: assert 0 != 0
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'cat'], returncode=0, stdout='', stderr='').returncode
- *(... 7 more in this cluster)*

### `rc_mismatch_got2_want1` — 7 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_argparse_validation.test_no_verb_supplied_errors[args0-1-stderr_substrings0]`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable'], returncode=2, stdout=b'', stderr=b"usage: miller [OPTIONS] [ARGS]\nTry 'miller --help' for more information.\n").returncode
- `eval.tests.test_argparse_validation.test_no_verb_supplied_errors[args1-1-stderr_substrings1]`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--csv'], returncode=2, stdout=b'', stderr=b"miller: unknown option: --csv\nusage: miller [OPTIONS] [ARGS]\nTry 'miller --help' for more i
- `eval.tests.test_argparse_validation.test_no_verb_supplied_errors[args2-1-stderr_substrings2]`
  > assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '--norc'], returncode=2, stdout=b'', stderr=b"miller: unknown option: --norc\nusage: miller [OPTIONS] [ARGS]\nTry 'miller --help' for more
- *(... 4 more in this cluster)*

### `rc_mismatch_got0_want1` — 7 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_auxents.test_hex_nonexistent_file`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'hex', 'nonexistent.txt'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_auxents.test_unhex_nonexistent_file`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'unhex', 'nonexistent.txt'], returncode=0, stdout=b'', stderr=b'').returncode
- `tests.test_auxents.test_lecat_invalid_option`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', 'lecat', '--invalid-flag'], returncode=0, stdout=b'', stderr=b'').returncode
- *(... 4 more in this cluster)*

### `empty_list_or_string` — 4 test(s)

**Quick patch ideas:**
- Defensive: check list/string emptiness before indexing

**Sample failures:**

- `tests.test_config_mlrrc.test_default_without_mlrrc_is_headerless_kv_pairs`
  > IndexError: list index out of range
- `tests.test_config_mlrrc.test_env_mlrrc_overrides_home_and_cwd`
  > IndexError: list index out of range
- `tests.test_config_mlrrc.test_env_mlrrc___none___disables_all_rc_files`
  > IndexError: list index out of range
- *(... 1 more in this cluster)*

### `boolean_false` — 4 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `eval.tests.test_help_main.test_help_has_usage_line`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7fe9b35324f0>('Usage: ')
  >  +    where <built-in method startswith of str object at 0x7fe9b35324f0> = 'miller 0.1.0 - bootstrap scaffold'.startswith
- `eval.tests.test_mlr_io.test_help_to_stdout_exit0`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of bytes object at 0x7f0d44b58710>(b'Usage: mlr')
  >  +    where <built-in method startswith of bytes object at 0x7f0d44b58710> = b'miller 0.1.0 - bootstrap scaffold\n\nUsage: miller [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --ver
  >  +      where b'miller 0.1.0 - bootstrap scaffold\n\nUsage: miller [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  Print version\n' = RunResult(returncode=0, stdout=b'mille
  >  +    and   b'Usage: mlr' = b('Usage: mlr')
- `eval.tests.test_mlr_io.test_version_to_stdout_exit0`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of bytes object at 0x7f0d44db3de0>(b'mlr ')
  >  +    where <built-in method startswith of bytes object at 0x7f0d44db3de0> = b'miller 0.1.0\n'.startswith
  >  +      where b'miller 0.1.0\n' = RunResult(returncode=0, stdout=b'miller 0.1.0\n', stderr=b'').stdout
  >  +    and   b'mlr ' = b('mlr ')
- *(... 1 more in this cluster)*

### `bytes_output_mismatch` — 4 test(s)

**Quick patch ideas:**
- Likely ANSI color, terminal escape sequences, or binary framing
- Match exact byte sequence from golden

**Sample failures:**

- `tests.test_auxents.test_unhex_basic`
  > AssertionError: assert b'' == b'Hello'
  >   
  >   Full diff:
  >   - (b'Hello')
  >   + b''
- `tests.test_auxents.test_unhex_tab_separated_values`
  > AssertionError: assert b'' == b'ABC'
  >   
  >   Full diff:
  >   - b'ABC'
  >   + b''
- `tests.test_auxents.test_unhex_mixed_case_hex_digits`
  > AssertionError: assert b'' == b'JKL'
  >   
  >   Full diff:
  >   - b'JKL'
  >   + b''
- *(... 1 more in this cluster)*

### `returned_none` — 2 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `tests.test_basic_invocation.test_version_output`
  > AssertionError: assert None
  >  +  where None = <function match at 0x7f78cdd9d120>(b'mlr \\d+\\.\\d+\\.\\d+', b'miller 0.1.0\n')
  >  +    where <function match at 0x7f78cdd9d120> = re.match
  >  +    and   b'miller 0.1.0\n' = CompletedProcess(args=['/workspace/executable', '--version'], returncode=0, stdout=b'miller 0.1.0\n', stderr=b'').stdout
- `eval.tests.test_help_main.test_help_usage_references_mlr_program_name`
  > AssertionError: assert None is not None
  >  +  where None = <function search at 0x7fe9b5a62680>('^Usage: mlr\\b', 'miller 0.1.0 - bootstrap scaffold\n\nUsage: miller [OPTIONS] [ARGS]\n\nOptions:\n  -h, --help     Print help\n  -V, --version  P
  >  +    where <function search at 0x7fe9b5a62680> = re.search
  >  +    and   re.MULTILINE = re.M

### `rc_mismatch_got0_want3` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_absolute_final.test_a22`
  > assert 0 == 3
  >  +  where 0 = <built-in method count of bytes object at 0x7f78cdf9c030>(b'1')
  >  +    where <built-in method count of bytes object at 0x7f78cdf9c030> = b''.count
  >  +      where b'' = CompletedProcess(args=['/workspace/executable', '--csv', 'repeat', '-n', '3'], returncode=2, stdout=b'', stderr=b"miller: unknown option: --csv\nusage: miller [OPTIONS] [ARGS]\nTry

### `rc_mismatch_got0_want256` — 1 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `tests.test_auxents.test_unhex_large_file`
  > AssertionError: assert 0 == 256
  >  +  where 0 = len(b'')
  >  +    where b'' = CompletedProcess(args=['/workspace/executable', 'unhex', '/workspace/eval/test_resources/test_auxents/all_bytes_hex.txt'], returncode=0, stdout=b'', stderr=b'').stdout

