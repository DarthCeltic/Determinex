---
name: swebench-pydata__xarray
description: SWE-bench repo behavioral spec for pydata/xarray. Aggregated from 137 bug-fix instances across 3 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# pydata/xarray — SWE-bench Repo Spec

> **137 bug-fix instances** across 3 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-full-test | 110 |
| swe-bench-verified-test | 22 |
| swe-bench-lite-test | 5 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `xarray/core/dataset.py` | 32 |
| `xarray/core/dataarray.py` | 28 |
| `xarray/core/variable.py` | 20 |
| `xarray/core/computation.py` | 14 |
| `xarray/core/formatting.py` | 11 |
| `xarray/core/groupby.py` | 11 |
| `xarray/core/indexing.py` | 10 |
| `xarray/core/concat.py` | 9 |
| `xarray/core/common.py` | 9 |
| `xarray/core/indexes.py` | 8 |
| `xarray/core/utils.py` | 8 |
| `xarray/core/duck_array_ops.py` | 8 |
| `xarray/core/rolling.py` | 7 |
| `xarray/core/merge.py` | 6 |
| `xarray/coding/times.py` | 6 |
| `xarray/core/combine.py` | 5 |
| `xarray/core/weighted.py` | 5 |
| `xarray/core/missing.py` | 5 |
| `xarray/core/nanops.py` | 4 |
| `xarray/coding/variables.py` | 4 |
| `xarray/backends/api.py` | 4 |
| `xarray/core/options.py` | 4 |
| `xarray/core/alignment.py` | 4 |
| `xarray/core/pycompat.py` | 4 |
| `xarray/core/dask_array_ops.py` | 3 |
| `xarray/__init__.py` | 3 |
| `xarray/core/coordinates.py` | 3 |
| `xarray/coding/cftime_offsets.py` | 3 |
| `xarray/backends/plugins.py` | 3 |
| `xarray/backends/zarr.py` | 3 |

## Section 3 — Test framework signal

Detected: **pytest (file::TestClass::test_method or file::test_func)**

Sample FAIL_TO_PASS test names (first 10):
```
  xarray/tests/test_combine.py::TestAutoCombineOldAPI::test_auto_combine_with_new_variables
  xarray/tests/test_concat.py::TestConcatDataset::test_concat_merge_variables_present_in_some_datasets
  xarray/tests/test_dataset.py::TestDataset::test_to_stacked_array_to_unstacked_dataset
  xarray/tests/test_formatting.py::test_inline_variable_array_repr_custom_repr
  xarray/tests/test_variable.py::TestVariable::test_as_variable
  xarray/tests/test_groupby.py::test_groupby_repr[obj0-x]
  xarray/tests/test_groupby.py::test_groupby_repr[obj0-y]
  xarray/tests/test_groupby.py::test_groupby_repr[obj0-z]
  xarray/tests/test_groupby.py::test_groupby_repr[obj0-month]
  xarray/tests/test_groupby.py::test_groupby_repr[obj1-x]
```

## Section 4 — Problem-theme distribution

Top themes across 137 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| other | 48 | 35.0% |
| import_module | 23 | 16.8% |
| wrong_output | 17 | 12.4% |
| regression | 12 | 8.8% |
| documentation | 11 | 8.0% |
| crash_or_traceback | 8 | 5.8% |
| edge_case | 7 | 5.1% |
| config_environment | 4 | 2.9% |
| encoding_unicode | 2 | 1.5% |
| type_handling | 2 | 1.5% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `pydata__xarray-3364`

**Files likely affected**: `xarray/core/concat.py`
**FAIL_TO_PASS** (2 tests, first 3): `['xarray/tests/test_combine.py::TestAutoCombineOldAPI::test_auto_combine_with_new_variables', 'xarray/tests/test_concat.py::TestConcatDataset::test_concat_merge_variables_present_in_some_datasets']`

**Problem statement (excerpt):**
> Ignore missing variables when concatenating datasets? Several users (@raj-kesavan, @richardotis, now myself) have wondered about how to concatenate xray Datasets with different variables.  With the current 'xray.concat', you need to awkwardly create dummy variables filled with 'NaN' in datasets that don't have them (or drop mismatched variables entirely). Neither of these are great options -- 'con

### Sample 2 — `pydata__xarray-4094`

**Files likely affected**: `xarray/core/dataarray.py`
**FAIL_TO_PASS** (1 tests, first 3): `['xarray/tests/test_dataset.py::TestDataset::test_to_stacked_array_to_unstacked_dataset']`

**Problem statement (excerpt):**
> to_unstacked_dataset broken for single-dim variables <!-- A short summary of the issue, if appropriate -->
 
 
 #### MCVE Code Sample
 
 '''python
 arr = xr.DataArray(
      np.arange(3),
      coords=[("x", [0, 1, 2])],
  )
 data = xr.Dataset({"a": arr, "b": arr})
 stacked = data.to_stacked_array('y', sample_dims=['x'])
 unstacked = stacked.to_unstacked_dataset('y')
 # MergeError: conflicting val

### Sample 3 — `pydata__xarray-4248`

**Files likely affected**: `xarray/core/formatting.py`
**FAIL_TO_PASS** (1 tests, first 3): `['xarray/tests/test_formatting.py::test_inline_variable_array_repr_custom_repr']`

**Problem statement (excerpt):**
> Feature request: show units in dataset overview Here's a hypothetical dataset:
 
 '''
 <xarray.Dataset>
 Dimensions:  (time: 3, x: 988, y: 822)
 Coordinates:
   * x         (x) float64 ...
   * y         (y) float64 ...
   * time      (time) datetime64[ns] ...
 Data variables:
     rainfall  (time, y, x) float32 ...
     max_temp  (time, y, x) float32 ...
 '''
 
 It would be really nice if the uni

### Sample 4 — `pydata__xarray-4493`

**Files likely affected**: `xarray/core/variable.py`
**FAIL_TO_PASS** (1 tests, first 3): `['xarray/tests/test_variable.py::TestVariable::test_as_variable']`

**Problem statement (excerpt):**
> DataSet.update causes chunked dask DataArray to evalute its values eagerly  **What happened**:
 Used 'DataSet.update' to update a chunked dask DataArray, but the DataArray is no longer chunked after the update.
 
 **What you expected to happen**:
 The chunked DataArray should still be chunked after the update
 
 **Minimal Complete Verifiable Example**:
 
 '''python
 foo = xr.DataArray(np.random.ra

### Sample 5 — `pydata__xarray-5131`

**Files likely affected**: `xarray/core/groupby.py`
**FAIL_TO_PASS** (10 tests, first 3): `['xarray/tests/test_groupby.py::test_groupby_repr[obj0-x]', 'xarray/tests/test_groupby.py::test_groupby_repr[obj0-y]', 'xarray/tests/test_groupby.py::test_groupby_repr[obj0-z]']`

**Problem statement (excerpt):**
> Trailing whitespace in DatasetGroupBy text representation When displaying a DatasetGroupBy in an interactive Python session, the first line of output contains a trailing whitespace. The first example in the documentation demonstrate this:
 
 '''pycon
 >>> import xarray as xr, numpy as np
 >>> ds = xr.Dataset(
 ...     {"foo": (("x", "y"), np.random.rand(4, 3))},
 ...     coords={"x": [10, 20, 30, 

### Sample 6 — `pydata__xarray-2905`

**Files likely affected**: `xarray/core/variable.py`
**FAIL_TO_PASS** (1 tests, first 3): `['xarray/tests/test_variable.py::TestAsCompatibleData::test_unsupported_type']`

**Problem statement (excerpt):**
> Variable.__setitem__ coercing types on objects with a values property #### Minimal example
 '''python
 import xarray as xr
 
 good_indexed, bad_indexed = xr.DataArray([None]), xr.DataArray([None])
 
 class HasValues(object):
     values = 5
     
 good_indexed.loc[{'dim_0': 0}] = set()
 bad_indexed.loc[{'dim_0': 0}] = HasValues()
 
 # correct
 # good_indexed.values => array([set()], dtype=object)

### Sample 7 — `pydata__xarray-3095`

**Files likely affected**: `xarray/core/variable.py`, `xarray/core/indexing.py`
**FAIL_TO_PASS** (1 tests, first 3): `['xarray/tests/test_variable.py::TestIndexVariable::test_copy[str-True]']`

**Problem statement (excerpt):**
> REGRESSION: copy(deep=True) casts unicode indices to object Dataset.copy(deep=True) and DataArray.copy (deep=True/False) accidentally cast IndexVariable's with dtype='<U*' to object. Same applies to copy.copy() and copy.deepcopy().
 
 This is a regression in xarray >= 0.12.2. xarray 0.12.1 and earlier are unaffected.
 
 '''
 
 In [1]: ds = xarray.Dataset(
    ...:     coords={'x': ['foo'], 'y': ('

### Sample 8 — `pydata__xarray-3151`

**Files likely affected**: `xarray/core/combine.py`
**FAIL_TO_PASS** (1 tests, first 3): `['xarray/tests/test_combine.py::TestCombineAuto::test_combine_leaving_bystander_dimensions']`

**Problem statement (excerpt):**
> xr.combine_by_coords raises ValueError if identical coordinates are non-monotonic #### MCVE Code Sample
 <!-- In order for the maintainers to efficiently understand and prioritize issues, we ask you post a "Minimal, Complete and Verifiable Example" (MCVE): http://matthewrocklin.com/blog/work/2018/02/28/minimal-bug-reports -->
 
 '''python
 import xarray as xr
 import numpy as np
 
 #yCoord = ['a',

## Section 6 — Builder guidance

When building a fix for an instance in pydata/xarray:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. xarray/core/dataset.py appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 137 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "pydata/xarray"`).

First 20 instance_ids:

- `pydata__xarray-3364` (dataset: `swe-bench-lite-test`)
- `pydata__xarray-4094` (dataset: `swe-bench-lite-test`)
- `pydata__xarray-4248` (dataset: `swe-bench-lite-test`)
- `pydata__xarray-4493` (dataset: `swe-bench-lite-test`)
- `pydata__xarray-5131` (dataset: `swe-bench-lite-test`)
- `pydata__xarray-2905` (dataset: `swe-bench-verified-test`)
- `pydata__xarray-3095` (dataset: `swe-bench-verified-test`)
- `pydata__xarray-3151` (dataset: `swe-bench-verified-test`)
- `pydata__xarray-3305` (dataset: `swe-bench-verified-test`)
- `pydata__xarray-3677` (dataset: `swe-bench-verified-test`)
- `pydata__xarray-3993` (dataset: `swe-bench-verified-test`)
- `pydata__xarray-4075` (dataset: `swe-bench-verified-test`)
- `pydata__xarray-4094` (dataset: `swe-bench-verified-test`)
- `pydata__xarray-4356` (dataset: `swe-bench-verified-test`)
- `pydata__xarray-4629` (dataset: `swe-bench-verified-test`)
- `pydata__xarray-4687` (dataset: `swe-bench-verified-test`)
- `pydata__xarray-4695` (dataset: `swe-bench-verified-test`)
- `pydata__xarray-4966` (dataset: `swe-bench-verified-test`)
- `pydata__xarray-6461` (dataset: `swe-bench-verified-test`)
- `pydata__xarray-6599` (dataset: `swe-bench-verified-test`)
- ... (117 more)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
