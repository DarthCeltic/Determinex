---
name: swebench-mwaskom__seaborn
description: SWE-bench repo behavioral spec for mwaskom/seaborn. Aggregated from 28 bug-fix instances across 3 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# mwaskom/seaborn — SWE-bench Repo Spec

> **28 bug-fix instances** across 3 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-full-test | 22 |
| swe-bench-lite-test | 4 |
| swe-bench-verified-test | 2 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `seaborn/_core/plot.py` | 8 |
| `seaborn/_core/scales.py` | 5 |
| `seaborn/axisgrid.py` | 4 |
| `seaborn/_oldcore.py` | 3 |
| `seaborn/utils.py` | 3 |
| `seaborn/relational.py` | 3 |
| `seaborn/regression.py` | 3 |
| `seaborn/_statistics.py` | 3 |
| `seaborn/_stats/regression.py` | 2 |
| `seaborn/matrix.py` | 2 |
| `seaborn/_compat.py` | 2 |
| `seaborn/categorical.py` | 1 |
| `seaborn/external/version.py` | 1 |
| `seaborn/rcmod.py` | 1 |
| `seaborn/_core.py` | 1 |
| `seaborn/distributions.py` | 1 |
| `seaborn/_core/subplots.py` | 1 |
| `seaborn/_marks/bar.py` | 1 |
| `seaborn/_core/rules.py` | 1 |

## Section 3 — Test framework signal

Detected: **pytest (file::TestClass::test_method or file::test_func)**

Sample FAIL_TO_PASS test names (first 10):
```
  tests/test_relational.py::TestScatterPlotter::test_hue_order
  tests/_stats/test_regression.py::TestPolyFit::test_missing_data
  tests/_core/test_scales.py::TestContinuous::test_interval_with_bools
  tests/test_axisgrid.py::TestPairGrid::test_pairplot_column_multiindex
  tests/_core/test_plot.py::TestScaling::test_nominal_x_axis_tweaks
  tests/_core/test_plot.py::TestScaling::test_nominal_y_axis_tweaks
  tests/_core/test_plot.py::TestLegend::test_legend_has_no_offset
  tests/test_relational.py::TestRelationalPlotter::test_legend_has_no_offset
  seaborn/tests/test_matrix.py::TestClustermap::test_categorical_colors_input
  seaborn/tests/test_utils.py::test_deprecate_ci
```

## Section 4 — Problem-theme distribution

Top themes across 28 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| other | 11 | 39.3% |
| import_module | 8 | 28.6% |
| crash_or_traceback | 5 | 17.9% |
| config_environment | 1 | 3.6% |
| regression | 1 | 3.6% |
| documentation | 1 | 3.6% |
| wrong_output | 1 | 3.6% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `mwaskom__seaborn-2848`

**Files likely affected**: `seaborn/_oldcore.py`
**FAIL_TO_PASS** (1 tests, first 3): `['tests/test_relational.py::TestScatterPlotter::test_hue_order']`

**Problem statement (excerpt):**
> pairplot fails with hue_order not containing all hue values in seaborn 0.11.1 In seaborn < 0.11, one could plot only a subset of the values in the hue column, by passing a hue_order list containing only the desired values. Points with hue values not in the list were simply not plotted. '''python iris = sns.load_dataset("iris")' # The hue column contains three different species; here we want to plo

### Sample 2 — `mwaskom__seaborn-3010`

**Files likely affected**: `seaborn/_stats/regression.py`
**FAIL_TO_PASS** (1 tests, first 3): `['tests/_stats/test_regression.py::TestPolyFit::test_missing_data']`

**Problem statement (excerpt):**
> PolyFit is not robust to missing data '''python
 so.Plot([1, 2, 3, None, 4], [1, 2, 3, 4, 5]).add(so.Line(), so.PolyFit())
 '''
 
 <details><summary>Traceback</summary>
 
 '''python-traceback
 ---------------------------------------------------------------------------
 LinAlgError                               Traceback (most recent call last)
 File ~/miniconda3/envs/seaborn-py39-latest/lib/python

### Sample 3 — `mwaskom__seaborn-3190`

**Files likely affected**: `seaborn/_core/scales.py`
**FAIL_TO_PASS** (1 tests, first 3): `['tests/_core/test_scales.py::TestContinuous::test_interval_with_bools']`

**Problem statement (excerpt):**
> Color mapping fails with boolean data '''python
 so.Plot(["a", "b"], [1, 2], color=[True, False]).add(so.Bar())
 '''
 '''python-traceback
 ---------------------------------------------------------------------------
 TypeError                                 Traceback (most recent call last)
 ...
 File ~/code/seaborn/seaborn/_core/plot.py:841, in Plot._plot(self, pyplot)
     838 plotter._compute_s

### Sample 4 — `mwaskom__seaborn-3407`

**Files likely affected**: `seaborn/axisgrid.py`
**FAIL_TO_PASS** (1 tests, first 3): `['tests/test_axisgrid.py::TestPairGrid::test_pairplot_column_multiindex']`

**Problem statement (excerpt):**
> pairplot raises KeyError with MultiIndex DataFrame When trying to pairplot a MultiIndex DataFrame, 'pairplot' raises a 'KeyError':
 
 MRE:
 
 '''python
 import numpy as np
 import pandas as pd
 import seaborn as sns
 
 
 data = {
     ("A", "1"): np.random.rand(100),
     ("A", "2"): np.random.rand(100),
     ("B", "1"): np.random.rand(100),
     ("B", "2"): np.random.rand(100),
 }
 df = pd.DataFr

### Sample 5 — `mwaskom__seaborn-3069`

**Files likely affected**: `seaborn/_core/plot.py`
**FAIL_TO_PASS** (2 tests, first 3): `['tests/_core/test_plot.py::TestScaling::test_nominal_x_axis_tweaks', 'tests/_core/test_plot.py::TestScaling::test_nominal_y_axis_tweaks']`

**Problem statement (excerpt):**
> Nominal scale should be drawn the same way as categorical scales Three distinctive things happen on the categorical axis in seaborn's categorical plots:
 
 1. The scale is drawn to +/- 0.5 from the first and last tick, rather than using the normal margin logic
 2. A grid is not shown, even when it otherwise would be with the active style
 3. If on the y axis, the axis is inverted
 
 It probably ma

### Sample 6 — `mwaskom__seaborn-3187`

**Files likely affected**: `seaborn/_core/scales.py`, `seaborn/utils.py`
**FAIL_TO_PASS** (2 tests, first 3): `['tests/_core/test_plot.py::TestLegend::test_legend_has_no_offset', 'tests/test_relational.py::TestRelationalPlotter::test_legend_has_no_offset']`

**Problem statement (excerpt):**
> Wrong legend values of large ranges As of 0.12.1, legends describing large numbers that were created using 'ScalarFormatter' with an offset are formatted without their multiplicative offset value. An example:
 '''python
 import seaborn as sns
 import seaborn.objects as so
 
 penguins = sns.load_dataset("Penguins")
 penguins["body_mass_mg"] = penguins["body_mass_g"]*1000
 (
     so.Plot(
         p

### Sample 7 — `mwaskom__seaborn-2389`

**Files likely affected**: `seaborn/matrix.py`
**FAIL_TO_PASS** (1 tests, first 3): `['seaborn/tests/test_matrix.py::TestClustermap::test_categorical_colors_input']`

**Problem statement (excerpt):**
> ValueError: fill value must be in categories In the  _preprocess_colors function, there is the code to replace na's with background color as the comment said, using 'colors = colors.fillna('white')', however, if the original colors do not contain the 'white' category, this line would raise the Pandas ValueError:fill value must be in categories in 'Pandas 0.25.3'. 

### Sample 8 — `mwaskom__seaborn-2457`

**Files likely affected**: `seaborn/relational.py`, `seaborn/utils.py`
**FAIL_TO_PASS** (1 tests, first 3): `['seaborn/tests/test_utils.py::test_deprecate_ci']`

**Problem statement (excerpt):**
> lineplot ignoring ci=None '''python
 sns.lineplot(x=[1, 1, 2, 2], y=[1, 2, 3, 4], ci=None)
 '''
 
 This should warn and then reformat the args to have 'errorbar=None' 

## Section 6 — Builder guidance

When building a fix for an instance in mwaskom/seaborn:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. seaborn/_core/plot.py appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 28 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "mwaskom/seaborn"`).

First 20 instance_ids:

- `mwaskom__seaborn-2848` (dataset: `swe-bench-lite-test`)
- `mwaskom__seaborn-3010` (dataset: `swe-bench-lite-test`)
- `mwaskom__seaborn-3190` (dataset: `swe-bench-lite-test`)
- `mwaskom__seaborn-3407` (dataset: `swe-bench-lite-test`)
- `mwaskom__seaborn-3069` (dataset: `swe-bench-verified-test`)
- `mwaskom__seaborn-3187` (dataset: `swe-bench-verified-test`)
- `mwaskom__seaborn-2389` (dataset: `swe-bench-full-test`)
- `mwaskom__seaborn-2457` (dataset: `swe-bench-full-test`)
- `mwaskom__seaborn-2576` (dataset: `swe-bench-full-test`)
- `mwaskom__seaborn-2766` (dataset: `swe-bench-full-test`)
- `mwaskom__seaborn-2813` (dataset: `swe-bench-full-test`)
- `mwaskom__seaborn-2846` (dataset: `swe-bench-full-test`)
- `mwaskom__seaborn-2848` (dataset: `swe-bench-full-test`)
- `mwaskom__seaborn-2853` (dataset: `swe-bench-full-test`)
- `mwaskom__seaborn-2946` (dataset: `swe-bench-full-test`)
- `mwaskom__seaborn-2979` (dataset: `swe-bench-full-test`)
- `mwaskom__seaborn-2996` (dataset: `swe-bench-full-test`)
- `mwaskom__seaborn-3010` (dataset: `swe-bench-full-test`)
- `mwaskom__seaborn-3069` (dataset: `swe-bench-full-test`)
- `mwaskom__seaborn-3180` (dataset: `swe-bench-full-test`)
- ... (8 more)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
