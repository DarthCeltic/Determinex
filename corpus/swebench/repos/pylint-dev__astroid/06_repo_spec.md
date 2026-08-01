---
name: swebench-pylint-dev__astroid
description: SWE-bench repo behavioral spec for pylint-dev/astroid. Aggregated from 36 bug-fix instances across 2 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# pylint-dev/astroid — SWE-bench Repo Spec

> **36 bug-fix instances** across 2 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-full-dev | 31 |
| swe-bench-lite-dev | 5 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `astroid/nodes/node_classes.py` | 7 |
| `astroid/brain/brain_builtin_inference.py` | 6 |
| `astroid/raw_building.py` | 5 |
| `astroid/modutils.py` | 4 |
| `astroid/brain/brain_typing.py` | 4 |
| `astroid/nodes/scoped_nodes/scoped_nodes.py` | 4 |
| `astroid/nodes/as_string.py` | 3 |
| `astroid/bases.py` | 3 |
| `astroid/protocols.py` | 3 |
| `astroid/inference.py` | 3 |
| `astroid/rebuilder.py` | 3 |
| `astroid/scoped_nodes.py` | 3 |
| `astroid/brain/brain_namedtuple_enum.py` | 2 |
| `astroid/arguments.py` | 2 |
| `astroid/builder.py` | 2 |
| `astroid/helpers.py` | 2 |
| `astroid/nodes/node_ng.py` | 2 |
| `astroid/const.py` | 2 |
| `astroid/manager.py` | 2 |
| `astroid/nodes/__init__.py` | 2 |
| `astroid/brain/brain_dataclasses.py` | 1 |
| `astroid/util.py` | 1 |
| `astroid/brain/brain_functools.py` | 1 |
| `astroid/typing.py` | 1 |
| `astroid/constraint.py` | 1 |
| `astroid/interpreter/objectmodel.py` | 1 |
| `astroid/inference_tip.py` | 1 |
| `astroid/mixins.py` | 1 |
| `astroid/objects.py` | 1 |
| `astroid/decorators.py` | 1 |

## Section 3 — Test framework signal

Detected: **pytest (file::TestClass::test_method or file::test_func)**

Sample FAIL_TO_PASS test names (first 10):
```
  tests/unittest_raw_building.py::test_build_module_getattr_catch_output
  tests/unittest_modutils.py::ModPathFromFileTest::test_load_packages_without_init
  tests/unittest_python3.py::Python3TC::test_unpacking_in_dict_getitem_uninferable
  tests/unittest_python3.py::Python3TC::test_unpacking_in_dict_getitem_with_ref
  tests/unittest_brain_builtin.py::TestStringNodes::test_string_format_uninferable[\n
  tests/unittest_nodes.py::AsStringTest::test_as_string_unknown
  tests/unittest_protocols.py::ProtocolTests::test_assign_stmts_starred_fails
  tests/unittest_protocols.py::ProtocolTests::test_assigned_stmts_annassignments
  tests/unittest_protocols.py::ProtocolTests::test_assigned_stmts_assignments
  tests/unittest_protocols.py::ProtocolTests::test_assigned_stmts_nested_for_dict
```

## Section 4 — Problem-theme distribution

Top themes across 36 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| wrong_output | 7 | 19.4% |
| import_module | 6 | 16.7% |
| other | 6 | 16.7% |
| crash_or_traceback | 6 | 16.7% |
| regression | 5 | 13.9% |
| edge_case | 3 | 8.3% |
| documentation | 3 | 8.3% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `pylint-dev__astroid-1978`

**Files likely affected**: `astroid/raw_building.py`
**FAIL_TO_PASS** (1 tests, first 3): `['tests/unittest_raw_building.py::test_build_module_getattr_catch_output']`

**Problem statement (excerpt):**
> Deprecation warnings from numpy ### Steps to reproduce
 
 1. Run pylint over the following test case:
 
 '''
 """Test case"""
 
 import numpy as np
 value = np.random.seed(1234)
 '''
 
 ### Current behavior
 '''
 /home/bje/source/nemo/myenv/lib/python3.10/site-packages/astroid/raw_building.py:470: FutureWarning: In the future 'np.long' will be defined as the corresponding NumPy scalar.  (This may 

### Sample 2 — `pylint-dev__astroid-1333`

**Files likely affected**: `astroid/modutils.py`
**FAIL_TO_PASS** (1 tests, first 3): `['tests/unittest_modutils.py::ModPathFromFileTest::test_load_packages_without_init']`

**Problem statement (excerpt):**
> astroid 2.9.1 breaks pylint with missing __init__.py: F0010: error while code parsing: Unable to load file __init__.py ### Steps to reproduce
 > Steps provided are for Windows 11, but initial problem found in Ubuntu 20.04
 
 > Update 2022-01-04: Corrected repro steps and added more environment details
 
 1. Set up simple repo with following structure (all files can be empty):
 '''
 root_dir/
 |--s

### Sample 3 — `pylint-dev__astroid-1196`

**Files likely affected**: `astroid/nodes/node_classes.py`
**FAIL_TO_PASS** (2 tests, first 3): `['tests/unittest_python3.py::Python3TC::test_unpacking_in_dict_getitem_uninferable', 'tests/unittest_python3.py::Python3TC::test_unpacking_in_dict_getitem_with_ref']`

**Problem statement (excerpt):**
> getitem does not infer the actual unpacked value When trying to call 'Dict.getitem()' on a context where we have a dict unpacking of anything beside a real dict, astroid currently raises an 'AttributeError: 'getitem'', which has 2 problems:
 
 - The object might be a reference against something constant, this pattern is usually seen when we have different sets of dicts that extend each other, and 

### Sample 4 — `pylint-dev__astroid-1866`

**Files likely affected**: `astroid/brain/brain_builtin_inference.py`
**FAIL_TO_PASS** (1 tests, first 3): `['tests/unittest_brain_builtin.py::TestStringNodes::test_string_format_uninferable[\\n']`

**Problem statement (excerpt):**
> "TypeError: unsupported format string passed to NoneType.__format__" while running type inference in version 2.12.x ### Steps to reproduce
 
 I have no concise reproducer. Exception happens every time I run pylint on some internal code, with astroid 2.12.10 and 2.12.12 (debian bookworm). It does _not_ happen with earlier versions of astroid (not with version 2.9). The pylinted code itself is "vali

### Sample 5 — `pylint-dev__astroid-1268`

**Files likely affected**: `astroid/nodes/as_string.py`
**FAIL_TO_PASS** (1 tests, first 3): `['tests/unittest_nodes.py::AsStringTest::test_as_string_unknown']`

**Problem statement (excerpt):**
> 'AsStringVisitor' object has no attribute 'visit_unknown' '''python
 >>> import astroid
 >>> astroid.nodes.Unknown().as_string()
 Traceback (most recent call last):
   File "<stdin>", line 1, in <module>
   File "/Users/tusharsadhwani/code/marvin-python/venv/lib/python3.9/site-packages/astroid/nodes/node_ng.py", line 609, in as_string
     return AsStringVisitor()(self)
   File "/Users/tusharsadhw

### Sample 6 — `pylint-dev__astroid-1741`

**Files likely affected**: `astroid/nodes/node_classes.py`, `astroid/bases.py`, `astroid/brain/brain_dataclasses.py`, `astroid/util.py`, `astroid/brain/brain_namedtuple_enum.py`
**FAIL_TO_PASS** (14 tests, first 3): `['tests/unittest_protocols.py::ProtocolTests::test_assign_stmts_starred_fails', 'tests/unittest_protocols.py::ProtocolTests::test_assigned_stmts_annassignments', 'tests/unittest_protocols.py::ProtocolTests::test_assigned_stmts_assignments']`

**Problem statement (excerpt):**
> Consider creating a ''UninferableType'' or ''_Uninferable'' class I opened https://github.com/microsoft/pyright/issues/3641 as I wondered why 'pyright' didn't recognise how we type 'Uninferable'. Normally they are a little bit more up to date than 'mypy' so I wondered if this was intentional.
 
 Turns out it is. According to them, the way we currently handle the typing of 'Uninferable' is incorrec

### Sample 7 — `pylint-dev__astroid-1616`

**Files likely affected**: `astroid/brain/brain_builtin_inference.py`
**FAIL_TO_PASS** (1 tests, first 3): `['tests/unittest_brain_builtin.py::TestStringNodes::test_string_format[empty-indexes-on-variable]']`

**Problem statement (excerpt):**
> Infer calls to str.format() on names Future enhancement could infer this value instead of giving an empty string:
 
 '''python
 from astroid import extract_node
 call = extract_node("""
 x = 'python is {}'
 x.format('helpful sometimes')
 """)
 call.inferred()[0].value  # gives ""
 '''
 
 _Originally posted by @jacobtylerwalls in https://github.com/PyCQA/astroid/pull/1602#discussion_r893423433_ 

### Sample 8 — `pylint-dev__astroid-1978`

**Files likely affected**: `astroid/raw_building.py`
**FAIL_TO_PASS** (1 tests, first 3): `['tests/unittest_raw_building.py::test_build_module_getattr_catch_output']`

**Problem statement (excerpt):**
> Deprecation warnings from numpy ### Steps to reproduce
 
 1. Run pylint over the following test case:
 
 '''
 """Test case"""
 
 import numpy as np
 value = np.random.seed(1234)
 '''
 
 ### Current behavior
 '''
 /home/bje/source/nemo/myenv/lib/python3.10/site-packages/astroid/raw_building.py:470: FutureWarning: In the future 'np.long' will be defined as the corresponding NumPy scalar.  (This may 

## Section 6 — Builder guidance

When building a fix for an instance in pylint-dev/astroid:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. astroid/nodes/node_classes.py appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 36 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "pylint-dev/astroid"`).

First 20 instance_ids:

- `pylint-dev__astroid-1978` (dataset: `swe-bench-lite-dev`)
- `pylint-dev__astroid-1333` (dataset: `swe-bench-lite-dev`)
- `pylint-dev__astroid-1196` (dataset: `swe-bench-lite-dev`)
- `pylint-dev__astroid-1866` (dataset: `swe-bench-lite-dev`)
- `pylint-dev__astroid-1268` (dataset: `swe-bench-lite-dev`)
- `pylint-dev__astroid-1741` (dataset: `swe-bench-full-dev`)
- `pylint-dev__astroid-1616` (dataset: `swe-bench-full-dev`)
- `pylint-dev__astroid-1978` (dataset: `swe-bench-full-dev`)
- `pylint-dev__astroid-934` (dataset: `swe-bench-full-dev`)
- `pylint-dev__astroid-1962` (dataset: `swe-bench-full-dev`)
- `pylint-dev__astroid-2240` (dataset: `swe-bench-full-dev`)
- `pylint-dev__astroid-941` (dataset: `swe-bench-full-dev`)
- `pylint-dev__astroid-1417` (dataset: `swe-bench-full-dev`)
- `pylint-dev__astroid-1364` (dataset: `swe-bench-full-dev`)
- `pylint-dev__astroid-2023` (dataset: `swe-bench-full-dev`)
- `pylint-dev__astroid-1719` (dataset: `swe-bench-full-dev`)
- `pylint-dev__astroid-1614` (dataset: `swe-bench-full-dev`)
- `pylint-dev__astroid-984` (dataset: `swe-bench-full-dev`)
- `pylint-dev__astroid-1164` (dataset: `swe-bench-full-dev`)
- `pylint-dev__astroid-1030` (dataset: `swe-bench-full-dev`)
- ... (16 more)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
