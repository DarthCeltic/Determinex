---
name: swebench-sphinx-doc__sphinx
description: SWE-bench repo behavioral spec for sphinx-doc/sphinx. Aggregated from 247 bug-fix instances across 3 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# sphinx-doc/sphinx — SWE-bench Repo Spec

> **247 bug-fix instances** across 3 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-full-test | 187 |
| swe-bench-verified-test | 44 |
| swe-bench-lite-test | 16 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `sphinx/ext/autodoc/__init__.py` | 43 |
| `sphinx/domains/python.py` | 38 |
| `sphinx/util/inspect.py` | 19 |
| `sphinx/builders/linkcheck.py` | 16 |
| `sphinx/ext/napoleon/docstring.py` | 14 |
| `sphinx/domains/cpp.py` | 13 |
| `sphinx/ext/autodoc/typehints.py` | 12 |
| `sphinx/util/typing.py` | 12 |
| `sphinx/domains/std.py` | 10 |
| `sphinx/writers/latex.py` | 9 |
| `sphinx/pycode/ast.py` | 9 |
| `sphinx/domains/c.py` | 9 |
| `sphinx/ext/autosummary/generate.py` | 6 |
| `sphinx/ext/autodoc/importer.py` | 6 |
| `sphinx/builders/html/transforms.py` | 6 |
| `sphinx/config.py` | 6 |
| `sphinx/util/cfamily.py` | 5 |
| `sphinx/ext/napoleon/__init__.py` | 5 |
| `sphinx/util/docfields.py` | 5 |
| `sphinx/writers/html.py` | 5 |
| `sphinx/ext/autodoc/preserve_defaults.py` | 5 |
| `sphinx/util/rst.py` | 4 |
| `sphinx/builders/manpage.py` | 4 |
| `sphinx/ext/viewcode.py` | 4 |
| `sphinx/directives/other.py` | 4 |
| `sphinx/ext/autodoc/mock.py` | 4 |
| `sphinx/application.py` | 4 |
| `sphinx/writers/html5.py` | 4 |
| `sphinx/util/i18n.py` | 4 |
| `sphinx/builders/html/__init__.py` | 4 |

## Section 3 — Test framework signal

Detected: **pytest (file::TestClass::test_method or file::test_func)**

Sample FAIL_TO_PASS test names (first 10):
```
  tests/test_ext_autodoc_automodule.py::test_automodule_inherited_members
  tests/test_ext_napoleon_docstring.py::test_napoleon_and_autodoc_typehints_description_all
  tests/test_ext_napoleon_docstring.py::test_napoleon_and_autodoc_typehints_description_documented_params
  tests/test_util_rst.py::test_prepend_prolog_with_roles_in_sections_with_newline
  tests/test_util_rst.py::test_prepend_prolog_with_roles_in_sections_without_newline
  tests/test_ext_autosummary.py::test_autosummary_generate_content_for_module
  tests/test_ext_autosummary.py::test_autosummary_generate_content_for_module_skipped
  tests/test_ext_napoleon_docstring.py::NumpyDocstringTest::test_underscore_in_attribute
  tests/test_environment_indexentries.py::test_create_single_index
  tests/test_build_manpage.py::test_man_make_section_directory
```

## Section 4 — Problem-theme distribution

Top themes across 247 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| documentation | 129 | 52.2% |
| wrong_output | 58 | 23.5% |
| other | 18 | 7.3% |
| regression | 16 | 6.5% |
| import_module | 6 | 2.4% |
| config_environment | 6 | 2.4% |
| edge_case | 4 | 1.6% |
| crash_or_traceback | 4 | 1.6% |
| performance | 3 | 1.2% |
| encoding_unicode | 2 | 0.8% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `sphinx-doc__sphinx-10325`

**Files likely affected**: `sphinx/ext/autodoc/__init__.py`
**FAIL_TO_PASS** (1 tests, first 3): `['tests/test_ext_autodoc_automodule.py::test_automodule_inherited_members']`

**Problem statement (excerpt):**
> inherited-members should support more than one class **Is your feature request related to a problem? Please describe.**
 I have two situations:
 - A class inherits from multiple other classes. I want to document members from some of the base classes but ignore some of the base classes
 - A module contains several class definitions that inherit from different classes that should all be ignored (e.g

### Sample 2 — `sphinx-doc__sphinx-10451`

**Files likely affected**: `sphinx/ext/autodoc/typehints.py`
**FAIL_TO_PASS** (2 tests, first 3): `['tests/test_ext_napoleon_docstring.py::test_napoleon_and_autodoc_typehints_description_all', 'tests/test_ext_napoleon_docstring.py::test_napoleon_and_autodoc_typehints_description_documented_params']`

**Problem statement (excerpt):**
> Fix duplicated *args and **kwargs with autodoc_typehints Fix duplicated *args and **kwargs with autodoc_typehints
 
 ### Bugfix
 - Bugfix
 
 ### Detail
 Consider this
 '''python
 class _ClassWithDocumentedInitAndStarArgs:
     """Class docstring."""
 
     def __init__(self, x: int, *args: int, **kwargs: int) -> None:
         """Init docstring.
 
         :param x: Some integer
         :param *a

### Sample 3 — `sphinx-doc__sphinx-11445`

**Files likely affected**: `sphinx/util/rst.py`
**FAIL_TO_PASS** (2 tests, first 3): `['tests/test_util_rst.py::test_prepend_prolog_with_roles_in_sections_with_newline', 'tests/test_util_rst.py::test_prepend_prolog_with_roles_in_sections_without_newline']`

**Problem statement (excerpt):**
> Using rst_prolog removes top level headings containing a domain directive ### Describe the bug
 
 If 'rst_prolog' is set, then any documents that contain a domain directive as the first heading (eg ':mod:') do not render the heading correctly or include the heading in the toctree.
 
 In the example below, if the heading of 'docs/mypackage.rst' were 'mypackage2' instead of ':mod:mypackage2' then th

### Sample 4 — `sphinx-doc__sphinx-7686`

**Files likely affected**: `sphinx/ext/autosummary/generate.py`
**FAIL_TO_PASS** (2 tests, first 3): `['tests/test_ext_autosummary.py::test_autosummary_generate_content_for_module', 'tests/test_ext_autosummary.py::test_autosummary_generate_content_for_module_skipped']`

**Problem statement (excerpt):**
> autosummary: The members variable for module template contains imported members **Describe the bug**
 autosummary: The members variable for module template contains imported members even if autosummary_imported_members is False.
 
 **To Reproduce**
 
 '''
 # _templates/autosummary/module.rst
 {{ fullname | escape | underline }}
 
 .. automodule:: {{ fullname }}
 
    .. autosummary::
    {% for it

### Sample 5 — `sphinx-doc__sphinx-7738`

**Files likely affected**: `sphinx/ext/napoleon/docstring.py`
**FAIL_TO_PASS** (1 tests, first 3): `['tests/test_ext_napoleon_docstring.py::NumpyDocstringTest::test_underscore_in_attribute']`

**Problem statement (excerpt):**
> overescaped trailing underscore on attribute with napoleon **Describe the bug**
 Attribute name 'hello_' shows up as 'hello\_' in the html (visible backslash) with napoleon.
 
 **To Reproduce**
 Steps to reproduce the behavior:
 
 empty '__init__.py'
 'a.py' contains
 '''python
 class A:
     """
     Attributes
     ----------
     hello_: int
         hi
     """
     pass
 '''
 run 'sphinx-quic

### Sample 6 — `sphinx-doc__sphinx-7975`

**Files likely affected**: `sphinx/environment/adapters/indexentries.py`
**FAIL_TO_PASS** (1 tests, first 3): `['tests/test_environment_indexentries.py::test_create_single_index']`

**Problem statement (excerpt):**
> Two sections called Symbols in index When using index entries with the following leading characters: _@_, _£_, and _←_ I get two sections called _Symbols_ in the HTML output, the first containing all _@_ entries before "normal" words and the second containing _£_ and _←_ entries after the "normal" words.  Both have the same anchor in HTML so the links at the top of the index page contain two _Symb

### Sample 7 — `sphinx-doc__sphinx-8273`

**Files likely affected**: `sphinx/builders/manpage.py`
**FAIL_TO_PASS** (1 tests, first 3): `['tests/test_build_manpage.py::test_man_make_section_directory']`

**Problem statement (excerpt):**
> Generate man page section directories **Current man page generation does not conform to 'MANPATH' search functionality**
 Currently, all generated man pages are placed in to a single-level directory: '<build-dir>/man'. Unfortunately, this cannot be used in combination with the unix 'MANPATH' environment variable. The 'man' program explicitly looks for man pages in section directories (such as 'man

### Sample 8 — `sphinx-doc__sphinx-8282`

**Files likely affected**: `sphinx/ext/autodoc/__init__.py`
**FAIL_TO_PASS** (1 tests, first 3): `['tests/test_ext_autodoc_configs.py::test_autodoc_typehints_none_for_overload']`

**Problem statement (excerpt):**
> autodoc_typehints does not effect to overloaded callables **Describe the bug**
 autodoc_typehints does not effect to overloaded callables.
 
 **To Reproduce**
 
 '''
 # in conf.py
 autodoc_typehints = 'none'
 '''
 '''
 # in index.rst
 .. automodule:: example
    :members:
    :undoc-members:
 '''
 '''
 # in example.py
 from typing import overload
 
 
 @overload
 def foo(x: int) -> int:
     ...
 

## Section 6 — Builder guidance

When building a fix for an instance in sphinx-doc/sphinx:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. sphinx/ext/autodoc/__init__.py appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 247 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "sphinx-doc/sphinx"`).

First 20 instance_ids:

- `sphinx-doc__sphinx-10325` (dataset: `swe-bench-lite-test`)
- `sphinx-doc__sphinx-10451` (dataset: `swe-bench-lite-test`)
- `sphinx-doc__sphinx-11445` (dataset: `swe-bench-lite-test`)
- `sphinx-doc__sphinx-7686` (dataset: `swe-bench-lite-test`)
- `sphinx-doc__sphinx-7738` (dataset: `swe-bench-lite-test`)
- `sphinx-doc__sphinx-7975` (dataset: `swe-bench-lite-test`)
- `sphinx-doc__sphinx-8273` (dataset: `swe-bench-lite-test`)
- `sphinx-doc__sphinx-8282` (dataset: `swe-bench-lite-test`)
- `sphinx-doc__sphinx-8435` (dataset: `swe-bench-lite-test`)
- `sphinx-doc__sphinx-8474` (dataset: `swe-bench-lite-test`)
- `sphinx-doc__sphinx-8506` (dataset: `swe-bench-lite-test`)
- `sphinx-doc__sphinx-8595` (dataset: `swe-bench-lite-test`)
- `sphinx-doc__sphinx-8627` (dataset: `swe-bench-lite-test`)
- `sphinx-doc__sphinx-8713` (dataset: `swe-bench-lite-test`)
- `sphinx-doc__sphinx-8721` (dataset: `swe-bench-lite-test`)
- `sphinx-doc__sphinx-8801` (dataset: `swe-bench-lite-test`)
- `sphinx-doc__sphinx-10323` (dataset: `swe-bench-verified-test`)
- `sphinx-doc__sphinx-10435` (dataset: `swe-bench-verified-test`)
- `sphinx-doc__sphinx-10449` (dataset: `swe-bench-verified-test`)
- `sphinx-doc__sphinx-10466` (dataset: `swe-bench-verified-test`)
- ... (227 more)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
