# Action Sheet — wfxr__csview.8ac4de0

**Current:** 21.26%  (74/348)
**Pass / Fail / Skip:** 74 / 273 / 1
**Gap to 100%:** 78.74 percentage points (274 tests)

## Skipped tests

PB counts skipped as non-passing for Resolved metric. Triage these first if no real failures.

- `eval.tests.test_csview_io.test_unreadable_file_permission_denied_exit_1`
  - reason: running as root; cannot reliably make file unreadable

## Failure clusters

273 failed tests grouped into 8 buckets (sorted by count).

### `other_assertion` — 120 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_csview.test_style_none`
  > AssertionError: assert b'\xe2\x94\x80' not in b'\xe2\x95\xad\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\xac\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\xae\n\xe2\x94\x82 A \xe2\x94\x82 B \xe2\x94\x82
  >  +  where b'\xe2\x94\x80' = <built-in method encode of str object at 0x7d7c5f4e8d00>('utf-8')
  >  +    where <built-in method encode of str object at 0x7d7c5f4e8d00> = '─'.encode
  >  +  and   b'\xe2\x95\xad\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\xac\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\xae\n\xe2\x94\x82 A \xe2\x94\x82 B \xe2\x94\x82\n\xe2\x94\x9c\xe2\x94\x80\xe2\x94\x
- `eval.tests.test_csview.test_style_reinforced`
  > AssertionError: assert b'\xe2\x94\x8f' in b'\xe2\x95\xad\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\xac\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\xae\n\xe2\x94\x82 A \xe2\x94\x82 B \xe2\x94\x82\n\x
  >  +  where b'\xe2\x94\x8f' = <built-in method encode of str object at 0x7d7c5f4eb230>('utf-8')
  >  +    where <built-in method encode of str object at 0x7d7c5f4eb230> = '┏'.encode
  >  +  and   b'\xe2\x95\xad\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\xac\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\xae\n\xe2\x94\x82 A \xe2\x94\x82 B \xe2\x94\x82\n\xe2\x94\x9c\xe2\x94\x80\xe2\x94\x
- `eval.tests.test_csview.test_style_grid`
  > AssertionError: assert b'\xe2\x94\x8c' in b'+---+---+\n| A | B |\n+---+---+\n| 1 | 2 |\n+---+---+\n| 3 | 4 |\n+---+---+\n'
  >  +  where b'\xe2\x94\x8c' = <built-in method encode of str object at 0x7d7c5fb33230>('utf-8')
  >  +    where <built-in method encode of str object at 0x7d7c5fb33230> = '┌'.encode
  >  +  and   b'+---+---+\n| A | B |\n+---+---+\n| 1 | 2 |\n+---+---+\n| 3 | 4 |\n+---+---+\n' = CompletedProcess(args=['./executable', '-s', 'grid'], returncode=0, stdout=b'+---+---+\n| A | B |\n+---+---
- *(... 117 more in this cluster)*

### `rc_mismatch_got2_want0` — 79 test(s)

**Quick patch ideas:**
- Tool exits with usage error on valid args; check argv parsing
- Missing required flag detection too aggressive

**Sample failures:**

- `eval.tests.test_csview.test_no_args_no_stdin`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable'], returncode=2, stdout=b'', stderr=b'usage: executable [-H] [-n] [-t] [-d DELIMITER] [-s STYLE] [-l SNIFF_LIMIT] [-h] [-V] [FILE]\nerror: a FILE arg
- `eval.tests.test_csview.test_no_args_with_stdin`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable'], returncode=2, stdout=b'', stderr=b'usage: executable [-H] [-n] [-t] [-d DELIMITER] [-s STYLE] [-l SNIFF_LIMIT] [-h] [-V] [FILE]\nerror: a FILE arg
- `eval.tests.test_csview.test_empty_csv_stdin`
  > AssertionError: assert 2 == 0
  >  +  where 2 = CompletedProcess(args=['./executable'], returncode=2, stdout=b'', stderr=b'usage: executable [-H] [-n] [-t] [-d DELIMITER] [-s STYLE] [-l SNIFF_LIMIT] [-h] [-V] [FILE]\nerror: a FILE arg
- *(... 76 more in this cluster)*

### `string_output_mismatch` — 60 test(s)

**Quick patch ideas:**
- Compare actual vs golden output for one failing test, identify format diff
- Common: trailing newline, ANSI color codes, locale formatting

**Sample failures:**

- `tests.test_edge_cases.test_ascii_only_baseline`
  > AssertionError: assert '╭─────────┬─...──────────╯\n' == '┌─────────┬─...──────────┘\n'
  >   
  >   - ┌─────────┬─────┬───────────┐
  >   ? ^                           ^
  >   + ╭─────────┬─────┬───────────╮
  >   ? ^                           ^
  >   - │  name   │ age │   city    │
  >   ?  -               --...
- `tests.test_edge_cases.test_latin_extended_characters`
  > AssertionError: assert '╭──────────┬...──────────╯\n' == '┌──────────┬...──────────┘\n'
  >   
  >   - ┌──────────┬─────────────┬─────────────────────┐
  >   ? ^                                              ^
  >   + ╭──────────┬─────────────┬─────────────────────╮
  >   ? ^                                              ^
  >   - │   name   │   country   │     description     │
  >   ?  --         --            ----...
- `tests.test_edge_cases.test_cjk_character_rendering`
  > AssertionError: assert '╭──────────┬...┴─────────╯\n' == '┌──────────┬...┴─────────┘\n'
  >   
  >   - ┌──────────┬──────┬─────────┐
  >   ? ^                           ^
  >   + ╭──────────┬──────┬─────────╮
  >   ? ^                           ^
  >   - │   name   │ city │ country │
  >   ?  --...
- *(... 57 more in this cluster)*

### `rc_mismatch_got1_want2` — 7 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_argparse.test_delimiter_rejects_empty_string[args0]`
  > assert 1 == 2
- `eval.tests.test_argparse.test_delimiter_rejects_empty_string[args1]`
  > assert 1 == 2
- `eval.tests.test_argparse.test_delimiter_rejects_empty_string[args2]`
  > assert 1 == 2
- *(... 4 more in this cluster)*

### `rc_mismatch_got0_want1` — 2 test(s)

**Quick patch ideas:**
- Check argv: if invalid input → `sys.exit(1)`
- Wrap main body in try/except → exit(1) on parse error

**Sample failures:**

- `tests.test_input.test_unequal_row_lengths_too_few_fields`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/workspace/eval/test_resources/test_input/unequal_lengths.csv'], returncode=0, stdout=b'\xe2\x95\xad\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\
- `tests.test_input.test_unequal_row_lengths_too_many_fields`
  > AssertionError: assert 0 == 1
  >  +  where 0 = CompletedProcess(args=['/workspace/executable', '/workspace/eval/test_resources/test_input/unequal_extra.csv'], returncode=0, stdout=b'\xe2\x95\xad\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe

### `rc_mismatch_got2_want1` — 2 test(s)

**Quick patch ideas:**
- Inspect samples manually

**Sample failures:**

- `eval.tests.test_argparse.test_double_dash_treats_dash_prefixed_value_as_positional`
  > assert 2 == 1
- `eval.tests.test_csview_io.test_nonexistent_file_errors_to_stderr_exit_1`
  > AssertionError: assert 2 == 1
  >  +  where 2 = CompletedProcess(args=['/workspace/executable', '-P', 'does_not_exist.csv'], returncode=2, stdout=b'', stderr=b'usage: executable [-H] [-n] [-t] [-d DELIMITER] [-s STYLE] [-l SNIFF_LIMIT

### `rc_mismatch_got0_want2` — 2 test(s)

**Quick patch ideas:**
- No args → print usage to stderr + `sys.exit(2)` (POSIX usage convention)
- Unknown flag → `sys.exit(2)`

**Sample failures:**

- `eval.tests.test_argparse.test_choice_flag_style_rejects_invalid_value_and_lists_possible_values`
  > assert 0 == 2
- `eval.tests.test_argparse.test_mutually_exclusive_tsv_and_delimiter`
  > assert 0 == 2

### `boolean_false` — 1 test(s)

**Quick patch ideas:**
- Generic boolean check; inspect specific test to find what's expected False

**Sample failures:**

- `eval.tests.test_rendering_and_options.test_missing_file_exit_1_and_message`
  > AssertionError: assert False
  >  +  where False = <built-in method startswith of str object at 0x7d08f578b630>('csview: ')
  >  +    where <built-in method startswith of str object at 0x7d08f578b630> = 'error: file not found: /no/such/file\n'.startswith
  >  +      where 'error: file not found: /no/such/file\n' = CompletedProcess(args=['/workspace/executable', '/no/such/file'], returncode=1, stdout='', stderr='error: file not found: /no/such/file\n').std

