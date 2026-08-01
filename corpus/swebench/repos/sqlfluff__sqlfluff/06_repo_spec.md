---
name: swebench-sqlfluff__sqlfluff
description: SWE-bench repo behavioral spec for sqlfluff/sqlfluff. Aggregated from 55 bug-fix instances across 2 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# sqlfluff/sqlfluff — SWE-bench Repo Spec

> **55 bug-fix instances** across 2 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-full-dev | 50 |
| swe-bench-lite-dev | 5 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `src/sqlfluff/cli/commands.py` | 14 |
| `src/sqlfluff/core/linter/linter.py` | 11 |
| `src/sqlfluff/core/templaters/slicers/tracer.py` | 7 |
| `src/sqlfluff/core/linter/linted_file.py` | 5 |
| `src/sqlfluff/cli/formatters.py` | 5 |
| `src/sqlfluff/core/rules/base.py` | 4 |
| `src/sqlfluff/core/parser/segments/base.py` | 3 |
| `src/sqlfluff/core/errors.py` | 3 |
| `src/sqlfluff/rules/L031.py` | 2 |
| `src/sqlfluff/rules/L060.py` | 2 |
| `src/sqlfluff/rules/L039.py` | 2 |
| `src/sqlfluff/core/parser/helpers.py` | 2 |
| `src/sqlfluff/core/linter/linted_dir.py` | 2 |
| `src/sqlfluff/core/parser/lexer.py` | 2 |
| `src/sqlfluff/core/linter/common.py` | 2 |
| `src/sqlfluff/dialects/dialect_ansi.py` | 2 |
| `src/sqlfluff/core/templaters/base.py` | 2 |
| `src/sqlfluff/core/linter/linting_result.py` | 2 |
| `src/sqlfluff/rules/L027.py` | 2 |
| `src/sqlfluff/rules/layout/LT12.py` | 2 |
| `src/sqlfluff/core/templaters/jinja.py` | 2 |
| `src/sqlfluff/core/rules/std/L036.py` | 2 |
| `src/sqlfluff/core/config.py` | 2 |
| `src/sqlfluff/core/linter.py` | 2 |
| `src/sqlfluff/rules/L009.py` | 1 |
| `src/sqlfluff/dialects/dialect_bigquery.py` | 1 |
| `src/sqlfluff/rules/L026.py` | 1 |
| `src/sqlfluff/core/rules/reference.py` | 1 |
| `src/sqlfluff/rules/L025.py` | 1 |
| `src/sqlfluff/core/rules/analysis/select.py` | 1 |

## Section 3 — Test framework signal

Detected: **pytest (file::TestClass::test_method or file::test_func)**

Sample FAIL_TO_PASS test names (first 10):
```
  test/cli/commands_test.py::test__cli__command_directed
  test/rules/std_L060_test.py::test__rules__std_L060_raised
  test/rules/std_L003_L036_L039_combo_test.py::test__rules__std_L003_L036_L039
  test/dialects/ansi_test.py::test__dialect__ansi_multiple_semicolons[select
  test/core/linter_test.py::test_safe_create_replace_file[utf8_create]
  test/core/linter_test.py::test_safe_create_replace_file[utf8_update]
  test/core/linter_test.py::test_safe_create_replace_file[utf8_special_char]
  test/cli/commands_test.py::test__cli__fix_multiple_errors_quiet_force
  test/cli/commands_test.py::test__cli__fix_multiple_errors_quiet_no_force
  test/api/simple_test.py::test__api__lint_string
```

## Section 4 — Problem-theme distribution

Top themes across 55 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| wrong_output | 20 | 36.4% |
| other | 17 | 30.9% |
| crash_or_traceback | 7 | 12.7% |
| config_environment | 5 | 9.1% |
| documentation | 3 | 5.5% |
| test_failure | 1 | 1.8% |
| regression | 1 | 1.8% |
| encoding_unicode | 1 | 1.8% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `sqlfluff__sqlfluff-1625`

**Files likely affected**: `src/sqlfluff/rules/L031.py`
**FAIL_TO_PASS** (1 tests, first 3): `['test/cli/commands_test.py::test__cli__command_directed']`

**Problem statement (excerpt):**
> TSQL - L031 incorrectly triggers "Avoid using aliases in join condition" when no join present ## Expected Behaviour
 
 Both of these queries should pass, the only difference is the addition of a table alias 'a':
 
 1/ no alias
 
 '''
 SELECT [hello]
 FROM
     mytable
 '''
 
 2/ same query with alias
 
 '''
 SELECT a.[hello]
 FROM
     mytable AS a
 '''
 
 ## Observed Behaviour
 
 1/ passes
 2/ fa

### Sample 2 — `sqlfluff__sqlfluff-2419`

**Files likely affected**: `src/sqlfluff/rules/L060.py`
**FAIL_TO_PASS** (1 tests, first 3): `['test/rules/std_L060_test.py::test__rules__std_L060_raised']`

**Problem statement (excerpt):**
> Rule L060 could give a specific error message At the moment rule L060 flags something like this:
 
 '''
 L:  21 | P:   9 | L060 | Use 'COALESCE' instead of 'IFNULL' or 'NVL'.
 '''
 
 Since we likely know the wrong word, it might be nice to actually flag that instead of both 'IFNULL' and 'NVL' - like most of the other rules do.
 
 That is it should flag this:
 
 '''
 L:  21 | P:   9 | L060 | Use 'C

### Sample 3 — `sqlfluff__sqlfluff-1733`

**Files likely affected**: `src/sqlfluff/rules/L039.py`
**FAIL_TO_PASS** (1 tests, first 3): `['test/rules/std_L003_L036_L039_combo_test.py::test__rules__std_L003_L036_L039']`

**Problem statement (excerpt):**
> Extra space when first field moved to new line in a WITH statement Note, the query below uses a 'WITH' statement. If I just try to fix the SQL within the CTE, this works fine.
 
 Given the following SQL:
 
 '''sql
 WITH example AS (
     SELECT my_id,
         other_thing,
         one_more
     FROM
         my_table
 )
 
 SELECT *
 FROM example
 '''
 
 ## Expected Behaviour
 
 after running 'sql

### Sample 4 — `sqlfluff__sqlfluff-1517`

**Files likely affected**: `src/sqlfluff/core/parser/helpers.py`
**FAIL_TO_PASS** (1 tests, first 3): `['test/dialects/ansi_test.py::test__dialect__ansi_multiple_semicolons[select']`

**Problem statement (excerpt):**
> "Dropped elements in sequence matching" when doubled semicolon ## Expected Behaviour
 Frankly, I'm not sure whether it (doubled ';') should be just ignored or rather some specific rule should be triggered.
 ## Observed Behaviour
 '''console
 (.venv) ?master ~/prod/_inne/sqlfluff> echo "select id from tbl;;" | sqlfluff lint -
 Traceback (most recent call last):
   File "/home/adam/prod/_inne/sqlflu

### Sample 5 — `sqlfluff__sqlfluff-1763`

**Files likely affected**: `src/sqlfluff/core/linter/linted_file.py`
**FAIL_TO_PASS** (3 tests, first 3): `['test/core/linter_test.py::test_safe_create_replace_file[utf8_create]', 'test/core/linter_test.py::test_safe_create_replace_file[utf8_update]', 'test/core/linter_test.py::test_safe_create_replace_file[utf8_special_char]']`

**Problem statement (excerpt):**
> dbt postgres fix command errors with UnicodeEncodeError and also wipes the .sql file _If this is a parsing or linting issue, please include a minimal SQL example which reproduces the issue, along with the 'sqlfluff parse' output, 'sqlfluff lint' output and 'sqlfluff fix' output when relevant._
 
 ## Expected Behaviour
 Violation failure notice at a minimum, without wiping the file. Would like a wa

### Sample 6 — `sqlfluff__sqlfluff-4764`

**Files likely affected**: `src/sqlfluff/core/linter/linted_dir.py`, `src/sqlfluff/cli/formatters.py`, `src/sqlfluff/cli/commands.py`
**FAIL_TO_PASS** (2 tests, first 3): `['test/cli/commands_test.py::test__cli__fix_multiple_errors_quiet_force', 'test/cli/commands_test.py::test__cli__fix_multiple_errors_quiet_no_force']`

**Problem statement (excerpt):**
> Enable quiet mode/no-verbose in CLI for use in pre-commit hook There seems to be only an option to increase the level of verbosity when using SQLFluff [CLI](https://docs.sqlfluff.com/en/stable/cli.html), not to limit it further.
 
 It would be great to have an option to further limit the amount of prints when running 'sqlfluff fix', especially in combination with deployment using a pre-commit hook

### Sample 7 — `sqlfluff__sqlfluff-2862`

**Files likely affected**: `src/sqlfluff/core/linter/linted_file.py`, `src/sqlfluff/core/parser/segments/base.py`, `src/sqlfluff/core/templaters/slicers/tracer.py`, `src/sqlfluff/core/rules/base.py`, `src/sqlfluff/core/parser/lexer.py`
**FAIL_TO_PASS** (3 tests, first 3): `['test/api/simple_test.py::test__api__lint_string', 'test/core/templaters/jinja_test.py::test__templater_jinja_slice_file[{%', 'test/core/templaters/jinja_test.py::test__templater_jinja_slice_file[{%-']`

**Problem statement (excerpt):**
> fix keep adding new line on wrong place  ### Search before asking  - [X] I searched the [issues](https://github.com/sqlfluff/sqlfluff/issues) and found no similar issues.   ### What Happened  To replicate this issue you can create a file eg. test.template.sql 
 
 '''
 {% if true %}
 SELECT 1 + 1
 {%- endif %}
 '''
 
 then run:
 '''
 sqlfluff fix test.template.sql  
 '''
 
 This will give you:
 '''

### Sample 8 — `sqlfluff__sqlfluff-2336`

**Files likely affected**: `src/sqlfluff/dialects/dialect_bigquery.py`, `src/sqlfluff/rules/L026.py`, `src/sqlfluff/dialects/dialect_ansi.py`, `src/sqlfluff/core/rules/reference.py`, `src/sqlfluff/rules/L025.py`
**FAIL_TO_PASS** (14 tests, first 3): `['test/core/rules/reference_test.py::test_object_ref_matches_table[possible_references0-targets0-True]', 'test/core/rules/reference_test.py::test_object_ref_matches_table[possible_references1-targets1-True]', 'test/core/rules/reference_test.py::test_object_ref_matches_table[possible_references2-targets2-False]']`

**Problem statement (excerpt):**
> L026: Rule incorrectly flag column does not exist in 'FROM' clause in an UPDATE statement. ## Expected Behaviour
 
 L026 should not fail when a subquery in an UPDATE statement references a column from the UPDATE target.
 
 ## Observed Behaviour
 
 L026 failed due to reference was not found in the FROM clause with the following error printed (When using 'sample.sql' content below)
 
 '''
 L:   7 | 

## Section 6 — Builder guidance

When building a fix for an instance in sqlfluff/sqlfluff:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. src/sqlfluff/cli/commands.py appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 55 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "sqlfluff/sqlfluff"`).

First 20 instance_ids:

- `sqlfluff__sqlfluff-1625` (dataset: `swe-bench-lite-dev`)
- `sqlfluff__sqlfluff-2419` (dataset: `swe-bench-lite-dev`)
- `sqlfluff__sqlfluff-1733` (dataset: `swe-bench-lite-dev`)
- `sqlfluff__sqlfluff-1517` (dataset: `swe-bench-lite-dev`)
- `sqlfluff__sqlfluff-1763` (dataset: `swe-bench-lite-dev`)
- `sqlfluff__sqlfluff-4764` (dataset: `swe-bench-full-dev`)
- `sqlfluff__sqlfluff-2862` (dataset: `swe-bench-full-dev`)
- `sqlfluff__sqlfluff-2336` (dataset: `swe-bench-full-dev`)
- `sqlfluff__sqlfluff-5074` (dataset: `swe-bench-full-dev`)
- `sqlfluff__sqlfluff-3436` (dataset: `swe-bench-full-dev`)
- `sqlfluff__sqlfluff-2849` (dataset: `swe-bench-full-dev`)
- `sqlfluff__sqlfluff-884` (dataset: `swe-bench-full-dev`)
- `sqlfluff__sqlfluff-4151` (dataset: `swe-bench-full-dev`)
- `sqlfluff__sqlfluff-3354` (dataset: `swe-bench-full-dev`)
- `sqlfluff__sqlfluff-3700` (dataset: `swe-bench-full-dev`)
- `sqlfluff__sqlfluff-3608` (dataset: `swe-bench-full-dev`)
- `sqlfluff__sqlfluff-3435` (dataset: `swe-bench-full-dev`)
- `sqlfluff__sqlfluff-3904` (dataset: `swe-bench-full-dev`)
- `sqlfluff__sqlfluff-4753` (dataset: `swe-bench-full-dev`)
- `sqlfluff__sqlfluff-4778` (dataset: `swe-bench-full-dev`)
- ... (35 more)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
