---
name: swebench-pylint-dev__pylint
description: SWE-bench repo behavioral spec for pylint-dev/pylint. Aggregated from 73 bug-fix instances across 3 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# pylint-dev/pylint — SWE-bench Repo Spec

> **73 bug-fix instances** across 3 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-full-test | 57 |
| swe-bench-verified-test | 10 |
| swe-bench-lite-test | 6 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `pylint/lint/pylinter.py` | 13 |
| `pylint/lint/expand_modules.py` | 9 |
| `pylint/config/argument.py` | 8 |
| `pylint/checkers/similar.py` | 8 |
| `pylint/lint/run.py` | 6 |
| `pylint/lint/base_options.py` | 5 |
| `pylint/config/config_initialization.py` | 4 |
| `pylint/checkers/misc.py` | 3 |
| `pylint/reporters/text.py` | 3 |
| `pylint/pyreverse/utils.py` | 3 |
| `pylint/checkers/variables.py` | 3 |
| `pylint/constants.py` | 3 |
| `pylint/config/utils.py` | 3 |
| `pylint/__init__.py` | 3 |
| `pylint/utils/utils.py` | 3 |
| `pylint/lint/parallel.py` | 3 |
| `pylint/checkers/imports.py` | 3 |
| `pylint/pyreverse/writer.py` | 2 |
| `pylint/pyreverse/diagrams.py` | 2 |
| `pylint/pyreverse/inspector.py` | 2 |
| `setup.cfg` | 2 |
| `pylint/config/__init__.py` | 2 |
| `pylint/config/arguments_manager.py` | 2 |
| `pylint/utils/__init__.py` | 2 |
| `pylint/reporters/__init__.py` | 2 |
| `pylint/extensions/_check_docs_utils.py` | 2 |
| `pylint/config/option.py` | 2 |
| `pylint/pyreverse/main.py` | 2 |
| `pylint/checkers/base_checker.py` | 2 |
| `pylint/interfaces.py` | 2 |

## Section 3 — Test framework signal

Detected: **pytest (file::TestClass::test_method or file::test_func)**

Sample FAIL_TO_PASS test names (first 10):
```
  tests/checkers/unittest_misc.py::TestFixme::test_non_alphanumeric_codetag
  tests/config/test_config.py::test_unknown_option_name
  tests/config/test_config.py::test_unknown_short_option_name
  tests/test_self.py::TestRunTC::test_ignore_path_recursive_current_dir
  tests/lint/unittest_lint.py::test_identically_named_nested_module
  tests/config/test_config.py::test_regex_error
  tests/config/test_config.py::test_csv_regex_error
  tests/reporters/unittest_reporting.py::test_template_option_with_header
  tests/unittest_pyreverse_writer.py::test_dot_files[packages_No_Name.dot]
  tests/unittest_pyreverse_writer.py::test_dot_files[classes_No_Name.dot]
```

## Section 4 — Problem-theme distribution

Top themes across 73 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| wrong_output | 14 | 19.2% |
| crash_or_traceback | 13 | 17.8% |
| config_environment | 13 | 17.8% |
| documentation | 12 | 16.4% |
| other | 8 | 11.0% |
| edge_case | 6 | 8.2% |
| import_module | 3 | 4.1% |
| regression | 2 | 2.7% |
| type_handling | 1 | 1.4% |
| regex | 1 | 1.4% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `pylint-dev__pylint-5859`

**Files likely affected**: `pylint/checkers/misc.py`
**FAIL_TO_PASS** (1 tests, first 3): `['tests/checkers/unittest_misc.py::TestFixme::test_non_alphanumeric_codetag']`

**Problem statement (excerpt):**
> "--notes" option ignores note tags that are entirely punctuation ### Bug description  If a note tag specified with the '--notes' option is entirely punctuation, pylint won't report a fixme warning (W0511).
 
 '''python
 # YES: yes
 # ???: no
 '''
 
 'pylint test.py --notes="YES,???"' will return a fixme warning (W0511) for the first line, but not the second.  ### Configuration  '''ini Default ''' 

### Sample 2 — `pylint-dev__pylint-6506`

**Files likely affected**: `pylint/config/config_initialization.py`
**FAIL_TO_PASS** (2 tests, first 3): `['tests/config/test_config.py::test_unknown_option_name', 'tests/config/test_config.py::test_unknown_short_option_name']`

**Problem statement (excerpt):**
> Traceback printed for unrecognized option ### Bug description  A traceback is printed when an unrecognized option is passed to pylint.  ### Configuration  _No response_  ### Command used  '''shell pylint -Q '''   ### Pylint output  '''shell ************* Module Command line
 Command line:1:0: E0015: Unrecognized option found: Q (unrecognized-option)
 Traceback (most recent call last):
   File "/Us

### Sample 3 — `pylint-dev__pylint-7080`

**Files likely affected**: `pylint/lint/expand_modules.py`
**FAIL_TO_PASS** (1 tests, first 3): `['tests/test_self.py::TestRunTC::test_ignore_path_recursive_current_dir']`

**Problem statement (excerpt):**
> '--recursive=y' ignores 'ignore-paths' ### Bug description
 
 When running recursively, it seems 'ignore-paths' in my settings in pyproject.toml is completely ignored
 
 ### Configuration
 
 '''ini
 [tool.pylint.MASTER]
 ignore-paths = [
   # Auto generated
   "^src/gen/.*$",
 ]
 '''
 
 
 ### Command used
 
 '''shell
 pylint --recursive=y src/
 '''
 
 
 ### Pylint output
 
 '''shell
 *************

### Sample 4 — `pylint-dev__pylint-7114`

**Files likely affected**: `pylint/lint/expand_modules.py`
**FAIL_TO_PASS** (1 tests, first 3): `['tests/lint/unittest_lint.py::test_identically_named_nested_module']`

**Problem statement (excerpt):**
> Linting fails if module contains module of the same name ### Steps to reproduce
 
 Given multiple files:
 '''
 .
 '-- a/
     |-- a.py
     '-- b.py
 '''
 Which are all empty, running 'pylint a' fails:
 
 '''
 $ pylint a
 ************* Module a
 a/__init__.py:1:0: F0010: error while code parsing: Unable to load file a/__init__.py:
 [Errno 2] No such file or directory: 'a/__init__.py' (parse-error)

### Sample 5 — `pylint-dev__pylint-7228`

**Files likely affected**: `pylint/config/argument.py`
**FAIL_TO_PASS** (2 tests, first 3): `['tests/config/test_config.py::test_regex_error', 'tests/config/test_config.py::test_csv_regex_error']`

**Problem statement (excerpt):**
> rxg include '\p{Han}' will throw error ### Bug description
 
 config rxg in pylintrc with \p{Han} will throw err
 
 ### Configuration
 .pylintrc:
 
 '''ini
 function-rgx=[\p{Han}a-z_][\p{Han}a-z0-9_]{2,30}$
 '''
 
 ### Command used
 
 '''shell
 pylint
 '''
 
 
 ### Pylint output
 
 '''shell
 (venvtest) tsung-hande-MacBook-Pro:robot_is_comming tsung-han$ pylint
 Traceback (most recent call last):
 

### Sample 6 — `pylint-dev__pylint-7993`

**Files likely affected**: `pylint/reporters/text.py`
**FAIL_TO_PASS** (1 tests, first 3): `['tests/reporters/unittest_reporting.py::test_template_option_with_header']`

**Problem statement (excerpt):**
> Using custom braces in message template does not work ### Bug description  Have any list of errors:
 
 On pylint 1.7 w/ python3.6 - I am able to use this as my message template
 '''
 $ pylint test.py --msg-template='{{ "Category": "{category}" }}'
 No config file found, using default configuration
 ************* Module [redacted].test
 { "Category": "convention" }
 { "Category": "error" }
 { "Cate

### Sample 7 — `pylint-dev__pylint-4551`

**Files likely affected**: `pylint/pyreverse/writer.py`, `pylint/pyreverse/utils.py`, `pylint/pyreverse/diagrams.py`, `pylint/pyreverse/inspector.py`
**FAIL_TO_PASS** (10 tests, first 3): `['tests/unittest_pyreverse_writer.py::test_dot_files[packages_No_Name.dot]', 'tests/unittest_pyreverse_writer.py::test_dot_files[classes_No_Name.dot]', 'tests/unittest_pyreverse_writer.py::test_get_visibility[names0-special]']`

**Problem statement (excerpt):**
> Use Python type hints for UML generation It seems that pyreverse does not read python type hints (as defined by [PEP 484](https://www.python.org/dev/peps/pep-0484/)), and this does not help when you use 'None' as a default value :
 
 ### Code example
 '''
 class C(object):
     def __init__(self, a: str = None):
         self.a = a
 '''
 
 ### Current behavior
 
 Output of pyreverse :
 
 ![classes

### Sample 8 — `pylint-dev__pylint-4604`

**Files likely affected**: `pylint/checkers/variables.py`, `pylint/constants.py`
**FAIL_TO_PASS** (21 tests, first 3): `['tests/checkers/unittest_variables.py::TestVariablesChecker::test_bitbucket_issue_78', 'tests/checkers/unittest_variables.py::TestVariablesChecker::test_no_name_in_module_skipped', 'tests/checkers/unittest_variables.py::TestVariablesChecker::test_all_elements_without_parent']`

**Problem statement (excerpt):**
> unused-import false positive for a module used in a type comment ### Steps to reproduce
 
 '''python
 """Docstring."""
 
 import abc
 from abc import ABC
 
 X = ...  # type: abc.ABC
 Y = ...  # type: ABC
 '''
 
 ### Current behavior
 
 '''
 ************* Module a
 /tmp/a.py:3:0: W0611: Unused import abc (unused-import)
 
 -----------------------------------
 Your code has been rated at 7.50/10
 ''

## Section 6 — Builder guidance

When building a fix for an instance in pylint-dev/pylint:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. pylint/lint/pylinter.py appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 73 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "pylint-dev/pylint"`).

First 20 instance_ids:

- `pylint-dev__pylint-5859` (dataset: `swe-bench-lite-test`)
- `pylint-dev__pylint-6506` (dataset: `swe-bench-lite-test`)
- `pylint-dev__pylint-7080` (dataset: `swe-bench-lite-test`)
- `pylint-dev__pylint-7114` (dataset: `swe-bench-lite-test`)
- `pylint-dev__pylint-7228` (dataset: `swe-bench-lite-test`)
- `pylint-dev__pylint-7993` (dataset: `swe-bench-lite-test`)
- `pylint-dev__pylint-4551` (dataset: `swe-bench-verified-test`)
- `pylint-dev__pylint-4604` (dataset: `swe-bench-verified-test`)
- `pylint-dev__pylint-4661` (dataset: `swe-bench-verified-test`)
- `pylint-dev__pylint-4970` (dataset: `swe-bench-verified-test`)
- `pylint-dev__pylint-6386` (dataset: `swe-bench-verified-test`)
- `pylint-dev__pylint-6528` (dataset: `swe-bench-verified-test`)
- `pylint-dev__pylint-6903` (dataset: `swe-bench-verified-test`)
- `pylint-dev__pylint-7080` (dataset: `swe-bench-verified-test`)
- `pylint-dev__pylint-7277` (dataset: `swe-bench-verified-test`)
- `pylint-dev__pylint-8898` (dataset: `swe-bench-verified-test`)
- `pylint-dev__pylint-4175` (dataset: `swe-bench-full-test`)
- `pylint-dev__pylint-4330` (dataset: `swe-bench-full-test`)
- `pylint-dev__pylint-4339` (dataset: `swe-bench-full-test`)
- `pylint-dev__pylint-4398` (dataset: `swe-bench-full-test`)
- ... (53 more)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
