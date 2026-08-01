---
name: swebench-pyvista__pyvista
description: SWE-bench repo behavioral spec for pyvista/pyvista. Aggregated from 17 bug-fix instances across 2 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# pyvista/pyvista — SWE-bench Repo Spec

> **17 bug-fix instances** across 2 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-full-dev | 16 |
| swe-bench-lite-dev | 1 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `pyvista/plotting/plotting.py` | 3 |
| `pyvista/core/grid.py` | 2 |
| `pyvista/core/filters/data_set.py` | 2 |
| `pyvista/core/filters/poly_data.py` | 2 |
| `pyvista/core/filters/rectilinear_grid.py` | 2 |
| `pyvista/core/composite.py` | 2 |
| `pyvista/plotting/widgets.py` | 2 |
| `pyvista/plotting/actor.py` | 2 |
| `pyvista/core/pointset.py` | 2 |
| `pyvista/utilities/geometric_objects.py` | 2 |
| `pyvista/core/utilities/geometric_objects.py` | 1 |
| `examples/01-filter/interpolate.py` | 1 |
| `examples/01-filter/resample.py` | 1 |
| `pyvista/core/datasetattributes.py` | 1 |
| `pyvista/utilities/misc.py` | 1 |
| `pyvista/plotting/composite_mapper.py` | 1 |
| `pyvista/plotting/_property.py` | 1 |
| `pyvista/themes.py` | 1 |
| `pyvista/plotting/renderer.py` | 1 |
| `pyvista/demos/logo.py` | 1 |
| `doc/source/conf.py` | 1 |
| `pyvista/core/errors.py` | 1 |
| `pyvista/core/filters.py` | 1 |
| `pyvista/utilities/utilities.py` | 1 |
| `pyvista/utilities/errors.py` | 1 |
| `examples/01-filter/decimate.py` | 1 |
| `pyvista/plotting/helpers.py` | 1 |
| `pyvista/plotting/qt_plotting.py` | 1 |
| `pyvista/utilities/__init__.py` | 1 |
| `pyvista/utilities/parametric_objects.py` | 1 |

## Section 3 — Test framework signal

Detected: **pytest (file::TestClass::test_method or file::test_func)**

Sample FAIL_TO_PASS test names (first 10):
```
  tests/test_grid.py::test_create_rectilinear_grid_from_specs
  tests/core/test_parametric_geometry.py::test_direction
  tests/filters/test_dataset_filters.py::test_sample
  tests/filters/test_dataset_filters.py::test_probe[None-True-True]
  tests/filters/test_dataset_filters.py::test_probe[None-True-False]
  tests/filters/test_dataset_filters.py::test_probe[None-False-True]
  tests/filters/test_dataset_filters.py::test_probe[None-False-False]
  tests/core/test_polydata_filters.py::test_identical_boolean
  tests/filters/test_rectilinear_grid.py::test_to_tetrahedral_pass_cell_ids
  tests/filters/test_rectilinear_grid.py::test_to_tetrahedral_pass_cell_data
```

## Section 4 — Problem-theme distribution

Top themes across 17 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| wrong_output | 11 | 64.7% |
| documentation | 2 | 11.8% |
| crash_or_traceback | 2 | 11.8% |
| import_module | 1 | 5.9% |
| other | 1 | 5.9% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `pyvista__pyvista-4315`

**Files likely affected**: `pyvista/core/grid.py`
**FAIL_TO_PASS** (1 tests, first 3): `['tests/test_grid.py::test_create_rectilinear_grid_from_specs']`

**Problem statement (excerpt):**
> Rectilinear grid does not allow Sequences as inputs ### Describe the bug, what's wrong, and what you expected.
 
 Rectilinear grid gives an error when 'Sequence's are passed in, but 'ndarray' are ok.
 
 ### Steps to reproduce the bug.
 
 This doesn't work
 '''python
 import pyvista as pv
 pv.RectilinearGrid([0, 1], [0, 1], [0, 1])
 '''
 
 This works
 '''py
 import pyvista as pv
 import numpy as np

### Sample 2 — `pyvista__pyvista-4853`

**Files likely affected**: `pyvista/core/utilities/geometric_objects.py`
**FAIL_TO_PASS** (1 tests, first 3): `['tests/core/test_parametric_geometry.py::test_direction']`

**Problem statement (excerpt):**
> Confusing behaviour of ParametricEllipsoid ### Describe the bug, what's wrong, and what you expected.
 
 When creating a ParametricEllispoid using a direction of [0, 1, 0], the ellipsoid is rotated along the y axis.  
 For example if setting the direction to [1e-5, 1, 0], which corresponds to approximately similar direction, the ellipsoid displays then the correct behaviour.
 
 ### Steps to reprod

### Sample 3 — `pyvista__pyvista-4648`

**Files likely affected**: `pyvista/core/filters/data_set.py`, `examples/01-filter/interpolate.py`, `examples/01-filter/resample.py`
**FAIL_TO_PASS** (9 tests, first 3): `['tests/filters/test_dataset_filters.py::test_sample', 'tests/filters/test_dataset_filters.py::test_probe[None-True-True]', 'tests/filters/test_dataset_filters.py::test_probe[None-True-False]']`

**Problem statement (excerpt):**
> Clean up and clarify sampling-like filters ### Describe what maintenance you would like added.  There was a discussion on slack on the use of sampling-like filters, i.e. 'sample', 'probe', and 'interpolate'.  One issue is that it is hard to figure out when to use which filter.  The other issue is that 'probe' has the opposite behavior of 'sample' and 'interpolate' in regards to order of operation 

### Sample 4 — `pyvista__pyvista-4808`

**Files likely affected**: `pyvista/core/filters/poly_data.py`
**FAIL_TO_PASS** (1 tests, first 3): `['tests/core/test_polydata_filters.py::test_identical_boolean']`

**Problem statement (excerpt):**
> Boolean Operation freezes/crashes  ### Describe the bug, what's wrong, and what you expected.  Apparently, if two polyData have the exact same shape, their boolean operation freezes/crashes the application!
   ### Steps to reproduce the bug.  '''python
 p1 = pv.Sphere().triangulate()
 p2 = pv.Sphere().triangulate()
 
 p1.boolean_intersection(p2)
 ''''''  ### System Information  '''shell ----------

### Sample 5 — `pyvista__pyvista-4311`

**Files likely affected**: `pyvista/core/datasetattributes.py`, `pyvista/core/filters/rectilinear_grid.py`
**FAIL_TO_PASS** (2 tests, first 3): `['tests/filters/test_rectilinear_grid.py::test_to_tetrahedral_pass_cell_ids', 'tests/filters/test_rectilinear_grid.py::test_to_tetrahedral_pass_cell_data']`

**Problem statement (excerpt):**
> Allow passing through cell data in 'to_tetrahedra' method in RectilinearGrid ### Describe the feature you would like to be added.  No cell data is passed through when converting to a tetrahedra.  The user can currently request to pass through the original cell id, but it requires one more step to regenerate the cell data on the tetrahedralized mesh.  ### Links to VTK Documentation, Examples, or Cl

### Sample 6 — `pyvista__pyvista-4414`

**Files likely affected**: `pyvista/core/filters/poly_data.py`
**FAIL_TO_PASS** (1 tests, first 3): `['tests/test_polydata.py::test_merge']`

**Problem statement (excerpt):**
> Adding ''CircularArc''s together does not provide a line ### Describe the bug, what's wrong, and what you expected.
 
 Don't know if it can be considered a bug or not but...
 
 If you define two consecutive ''pv.CircularArc'' and you plot them, weird things start to appear with the new PyVista 0.39 version. Run the following code snippet using ''pyvista==0.38.6'' and ''pyvista==0.39.0''
 
 ### Ste

### Sample 7 — `pyvista__pyvista-4417`

**Files likely affected**: `pyvista/core/composite.py`
**FAIL_TO_PASS** (1 tests, first 3): `['tests/test_composite.py::test_to_polydata']`

**Problem statement (excerpt):**
> ''Multiblock''.plot does not work when using ''PointSet'' ### Describe the bug, what's wrong, and what you expected.  It seems ''MultiBlock'' entities made of ''PointSet'' plot nothing when using ''plot'' method.  ### Steps to reproduce the bug.  '''python
 import pyvista as pv
 import numpy as np
 
 points_arr = np.array(
     [
         [0.0, 1.0, 0.0],
         [0.0, 0.0, 0.0],
         [1.0, 1

### Sample 8 — `pyvista__pyvista-4406`

**Files likely affected**: `pyvista/core/filters/rectilinear_grid.py`
**FAIL_TO_PASS** (2 tests, first 3): `['tests/filters/test_rectilinear_grid.py::test_to_tetrahedral_pass_cell_ids', 'tests/filters/test_rectilinear_grid.py::test_to_tetrahedral_pass_cell_data']`

**Problem statement (excerpt):**
> to_tetrahedra active scalars ### Describe the bug, what's wrong, and what you expected.  #4311 passes cell data through the 'to_tetrahedra' call. However, after these changes.  The active scalars information is lost.
 
 cc @akaszynski who implemented these changes in that PR.  ### Steps to reproduce the bug.  '''py
 import pyvista as pv
 import numpy as np
 mesh = pv.UniformGrid(dimensions=(10, 10

## Section 6 — Builder guidance

When building a fix for an instance in pyvista/pyvista:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. pyvista/plotting/plotting.py appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 17 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "pyvista/pyvista"`).

First 20 instance_ids:

- `pyvista__pyvista-4315` (dataset: `swe-bench-lite-dev`)
- `pyvista__pyvista-4853` (dataset: `swe-bench-full-dev`)
- `pyvista__pyvista-4648` (dataset: `swe-bench-full-dev`)
- `pyvista__pyvista-4808` (dataset: `swe-bench-full-dev`)
- `pyvista__pyvista-4311` (dataset: `swe-bench-full-dev`)
- `pyvista__pyvista-4414` (dataset: `swe-bench-full-dev`)
- `pyvista__pyvista-4417` (dataset: `swe-bench-full-dev`)
- `pyvista__pyvista-4406` (dataset: `swe-bench-full-dev`)
- `pyvista__pyvista-4226` (dataset: `swe-bench-full-dev`)
- `pyvista__pyvista-3750` (dataset: `swe-bench-full-dev`)
- `pyvista__pyvista-3747` (dataset: `swe-bench-full-dev`)
- `pyvista__pyvista-4329` (dataset: `swe-bench-full-dev`)
- `pyvista__pyvista-4225` (dataset: `swe-bench-full-dev`)
- `pyvista__pyvista-432` (dataset: `swe-bench-full-dev`)
- `pyvista__pyvista-3710` (dataset: `swe-bench-full-dev`)
- `pyvista__pyvista-3675` (dataset: `swe-bench-full-dev`)
- `pyvista__pyvista-4315` (dataset: `swe-bench-full-dev`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
