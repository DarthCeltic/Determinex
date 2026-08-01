---
name: swebench-pytest-dev__pytest
description: SWE-bench repo behavioral spec for pytest-dev/pytest. Aggregated from 155 bug-fix instances across 3 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# pytest-dev/pytest — SWE-bench Repo Spec

> **155 bug-fix instances** across 3 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-full-test | 119 |
| swe-bench-verified-test | 19 |
| swe-bench-lite-test | 17 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `src/_pytest/python.py` | 16 |
| `src/_pytest/logging.py` | 13 |
| `src/_pytest/pathlib.py` | 12 |
| `src/_pytest/unittest.py` | 11 |
| `src/_pytest/config/__init__.py` | 11 |
| `src/_pytest/assertion/rewrite.py` | 8 |
| `src/_pytest/skipping.py` | 8 |
| `src/_pytest/main.py` | 7 |
| `src/_pytest/nodes.py` | 7 |
| `src/_pytest/deprecated.py` | 7 |
| `src/_pytest/_code/code.py` | 6 |
| `src/_pytest/mark/structures.py` | 6 |
| `src/_pytest/capture.py` | 6 |
| `src/_pytest/python_api.py` | 6 |
| `src/_pytest/junitxml.py` | 5 |
| `src/_pytest/tmpdir.py` | 5 |
| `src/_pytest/mark/expression.py` | 5 |
| `src/_pytest/fixtures.py` | 5 |
| `src/_pytest/pytester.py` | 5 |
| `src/_pytest/stepwise.py` | 4 |
| `src/_pytest/compat.py` | 3 |
| `src/_pytest/reports.py` | 3 |
| `src/_pytest/pastebin.py` | 3 |
| `src/_pytest/warning_types.py` | 3 |
| `src/_pytest/terminal.py` | 3 |
| `src/_pytest/doctest.py` | 3 |
| `src/_pytest/hookspec.py` | 3 |
| `src/_pytest/pytester_assertions.py` | 3 |
| `src/_pytest/assertion/util.py` | 2 |
| `src/_pytest/_io/saferepr.py` | 2 |

## Section 3 — Test framework signal

Detected: **pytest (file::TestClass::test_method or file::test_func)**

Sample FAIL_TO_PASS test names (first 10):
```
  testing/test_assertrewrite.py::TestIssue11140::test_constant_not_picked_as_module_docstring
  testing/test_pathlib.py::TestImportPath::test_remembers_previous_imports
  testing/acceptance_test.py::test_doctest_and_normal_imports_with_importlib
  testing/test_assertrewrite.py::TestAssertionRewrite::test_unroll_expression
  testing/python/fixtures.py::TestShowFixtures::test_show_fixtures
  testing/python/fixtures.py::TestShowFixtures::test_show_fixtures_verbose
  testing/logging/test_reporting.py::test_log_cli_enabled_disabled[True]
  testing/logging/test_reporting.py::test_log_cli_default_level
  testing/logging/test_reporting.py::test_sections_single_new_line_after_test_outcome
  testing/code/test_excinfo.py::test_excinfo_repr_str
```

## Section 4 — Problem-theme distribution

Top themes across 155 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| other | 39 | 25.2% |
| crash_or_traceback | 21 | 13.5% |
| wrong_output | 18 | 11.6% |
| import_module | 17 | 11.0% |
| documentation | 15 | 9.7% |
| config_environment | 14 | 9.0% |
| test_failure | 14 | 9.0% |
| regression | 9 | 5.8% |
| encoding_unicode | 5 | 3.2% |
| edge_case | 2 | 1.3% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `pytest-dev__pytest-11143`

**Files likely affected**: `src/_pytest/assertion/rewrite.py`
**FAIL_TO_PASS** (1 tests, first 3): `['testing/test_assertrewrite.py::TestIssue11140::test_constant_not_picked_as_module_docstring']`

**Problem statement (excerpt):**
> Rewrite fails when first expression of file is a number and mistaken as docstring  <!--
 Thanks for submitting an issue!
 
 Quick check-list while reporting bugs:
 -->
 
 - [x] a detailed description of the bug or problem you are having
 - [x] output of 'pip list' from the virtual environment you are using
 - [x] pytest and operating system versions
 - [x] minimal example if possible
 '''
 Install

### Sample 2 — `pytest-dev__pytest-11148`

**Files likely affected**: `src/_pytest/pathlib.py`
**FAIL_TO_PASS** (2 tests, first 3): `['testing/test_pathlib.py::TestImportPath::test_remembers_previous_imports', 'testing/acceptance_test.py::test_doctest_and_normal_imports_with_importlib']`

**Problem statement (excerpt):**
> Module imported twice under import-mode=importlib In pmxbot/pmxbot@7f189ad, I'm attempting to switch pmxbot off of pkg_resources style namespace packaging to PEP 420 namespace packages. To do so, I've needed to switch to 'importlib' for the 'import-mode' and re-organize the tests to avoid import errors on the tests.
 
 Yet even after working around these issues, the tests are failing when the effe

### Sample 3 — `pytest-dev__pytest-5103`

**Files likely affected**: `src/_pytest/assertion/rewrite.py`
**FAIL_TO_PASS** (1 tests, first 3): `['testing/test_assertrewrite.py::TestAssertionRewrite::test_unroll_expression']`

**Problem statement (excerpt):**
> Unroll the iterable for all/any calls to get better reports Sometime I need to assert some predicate on all of an iterable, and for that the builtin functions 'all'/'any' are great - but the failure messages aren't useful at all!
 For example - the same test written in three ways:
 
 - A generator expression
 '''sh                                                                                    

### Sample 4 — `pytest-dev__pytest-5221`

**Files likely affected**: `src/_pytest/python.py`
**FAIL_TO_PASS** (2 tests, first 3): `['testing/python/fixtures.py::TestShowFixtures::test_show_fixtures', 'testing/python/fixtures.py::TestShowFixtures::test_show_fixtures_verbose']`

**Problem statement (excerpt):**
> Display fixture scope with 'pytest --fixtures' It would be useful to show fixture scopes with 'pytest --fixtures'; currently the only way to learn the scope of a fixture is look at the docs (when that is documented) or at the source code. 

### Sample 5 — `pytest-dev__pytest-5227`

**Files likely affected**: `src/_pytest/logging.py`
**FAIL_TO_PASS** (3 tests, first 3): `['testing/logging/test_reporting.py::test_log_cli_enabled_disabled[True]', 'testing/logging/test_reporting.py::test_log_cli_default_level', 'testing/logging/test_reporting.py::test_sections_single_new_line_after_test_outcome']`

**Problem statement (excerpt):**
> Improve default logging format Currently it is:
 
 > DEFAULT_LOG_FORMAT = "%(filename)-25s %(lineno)4d %(levelname)-8s %(message)s"
 
 I think 'name' (module name) would be very useful here, instead of just the base filename.
 
 (It might also be good to have the relative path there (maybe at the end), but it is usually still very long (but e.g. '$VIRTUAL_ENV' could be substituted therein))
 
 Cur

### Sample 6 — `pytest-dev__pytest-5413`

**Files likely affected**: `src/_pytest/_code/code.py`
**FAIL_TO_PASS** (1 tests, first 3): `['testing/code/test_excinfo.py::test_excinfo_repr_str']`

**Problem statement (excerpt):**
> str() on the pytest.raises context variable doesn't behave same as normal exception catch Pytest 4.6.2, macOS 10.14.5
 
 '''Python
 try:
     raise LookupError(
         f"A\n"
         f"B\n"
         f"C"
     )
 except LookupError as e:
     print(str(e))
 '''
 prints
 
 > A
 > B
 > C
 
 But
 
 '''Python
 with pytest.raises(LookupError) as e:
     raise LookupError(
         f"A\n"
         f"B

### Sample 7 — `pytest-dev__pytest-5495`

**Files likely affected**: `src/_pytest/assertion/util.py`
**FAIL_TO_PASS** (2 tests, first 3): `['testing/test_assertion.py::TestAssert_reprcompare::test_bytes_diff_normal', 'testing/test_assertion.py::TestAssert_reprcompare::test_bytes_diff_verbose']`

**Problem statement (excerpt):**
> Confusing assertion rewriting message with byte strings The comparison with assertion rewriting for byte strings is confusing: 
 '''
     def test_b():
 >       assert b"" == b"42"
 E       AssertionError: assert b'' == b'42'
 E         Right contains more items, first extra item: 52
 E         Full diff:
 E         - b''
 E         + b'42'
 E         ?   ++
 '''
 
 52 is the ASCII ordinal of "4" 

### Sample 8 — `pytest-dev__pytest-5692`

**Files likely affected**: `src/_pytest/junitxml.py`
**FAIL_TO_PASS** (2 tests, first 3): `['testing/test_junitxml.py::TestPython::test_hostname_in_xml', 'testing/test_junitxml.py::TestPython::test_timestamp_in_xml']`

**Problem statement (excerpt):**
> Hostname and timestamp properties in generated JUnit XML reports Pytest enables generating JUnit XML reports of the tests.
 
 However, there are some properties missing, specifically 'hostname' and 'timestamp' from the 'testsuite' XML element. Is there an option to include them?
 
 Example of a pytest XML report:
 '''xml
 <?xml version="1.0" encoding="utf-8"?>
 <testsuite errors="0" failures="2" n

## Section 6 — Builder guidance

When building a fix for an instance in pytest-dev/pytest:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. src/_pytest/python.py appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 155 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "pytest-dev/pytest"`).

First 20 instance_ids:

- `pytest-dev__pytest-11143` (dataset: `swe-bench-lite-test`)
- `pytest-dev__pytest-11148` (dataset: `swe-bench-lite-test`)
- `pytest-dev__pytest-5103` (dataset: `swe-bench-lite-test`)
- `pytest-dev__pytest-5221` (dataset: `swe-bench-lite-test`)
- `pytest-dev__pytest-5227` (dataset: `swe-bench-lite-test`)
- `pytest-dev__pytest-5413` (dataset: `swe-bench-lite-test`)
- `pytest-dev__pytest-5495` (dataset: `swe-bench-lite-test`)
- `pytest-dev__pytest-5692` (dataset: `swe-bench-lite-test`)
- `pytest-dev__pytest-6116` (dataset: `swe-bench-lite-test`)
- `pytest-dev__pytest-7168` (dataset: `swe-bench-lite-test`)
- `pytest-dev__pytest-7220` (dataset: `swe-bench-lite-test`)
- `pytest-dev__pytest-7373` (dataset: `swe-bench-lite-test`)
- `pytest-dev__pytest-7432` (dataset: `swe-bench-lite-test`)
- `pytest-dev__pytest-7490` (dataset: `swe-bench-lite-test`)
- `pytest-dev__pytest-8365` (dataset: `swe-bench-lite-test`)
- `pytest-dev__pytest-8906` (dataset: `swe-bench-lite-test`)
- `pytest-dev__pytest-9359` (dataset: `swe-bench-lite-test`)
- `pytest-dev__pytest-10051` (dataset: `swe-bench-verified-test`)
- `pytest-dev__pytest-10081` (dataset: `swe-bench-verified-test`)
- `pytest-dev__pytest-10356` (dataset: `swe-bench-verified-test`)
- ... (135 more)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
