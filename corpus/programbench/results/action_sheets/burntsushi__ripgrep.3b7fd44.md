# Action Sheet — burntsushi__ripgrep.3b7fd44

**Current:** 99.96%  (2537/2538)
**Pass / Fail / Skip:** 2537 / 1 / 0
**Gap to 100%:** 0.04 percentage points (1 tests)

## Failure clusters

1 failed tests grouped into 1 buckets (sorted by count).

### `returned_none` — 1 test(s)

**Quick patch ideas:**
- Function returning None unexpectedly; check return statements

**Sample failures:**

- `eval.tests.test_rg_behavior.test_line_number_default_and_no_filename_behavior`
  > AssertionError: assert None
  >  +  where None = <function search at 0x708254156680>('a\\.txt:\\d+:', '/tmp/pytest-of-root/pytest-0/test_line_number_default_and_n2/a.txt:foo.bar\n/tmp/pytest-of-root/pytest-0/test_line_number_default
  >  +    where <function search at 0x708254156680> = re.search
  >  +    and   '/tmp/pytest-of-root/pytest-0/test_line_number_default_and_n2/a.txt:foo.bar\n/tmp/pytest-of-root/pytest-0/test_line_number_default_and_n2/a.txt:foo bar\n/tmp/pytest-of-root/pytest-0/test_l

