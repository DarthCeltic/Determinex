---
name: swebench-astropy__astropy
description: SWE-bench repo behavioral spec for astropy/astropy. Aggregated from 123 bug-fix instances across 3 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# astropy/astropy — SWE-bench Repo Spec

> **123 bug-fix instances** across 3 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-full-test | 95 |
| swe-bench-verified-test | 22 |
| swe-bench-lite-test | 6 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `astropy/units/quantity.py` | 8 |
| `astropy/wcs/wcs.py` | 6 |
| `astropy/io/fits/card.py` | 6 |
| `astropy/time/core.py` | 5 |
| `astropy/time/formats.py` | 5 |
| `astropy/coordinates/angles.py` | 5 |
| `astropy/table/table.py` | 4 |
| `astropy/modeling/separable.py` | 3 |
| `astropy/io/ascii/rst.py` | 3 |
| `astropy/io/ascii/qdp.py` | 3 |
| `astropy/nddata/mixins/ndarithmetic.py` | 3 |
| `astropy/io/fits/fitsrec.py` | 3 |
| `astropy/coordinates/sky_coordinate.py` | 3 |
| `astropy/io/fits/connect.py` | 3 |
| `astropy/io/fits/diff.py` | 3 |
| `astropy/units/core.py` | 3 |
| `astropy/units/quantity_helper/function_helpers.py` | 3 |
| `astropy/timeseries/core.py` | 2 |
| `astropy/coordinates/builtin_frames/itrs_observed_transforms.py` | 2 |
| `astropy/coordinates/builtin_frames/itrs.py` | 2 |
| `astropy/coordinates/builtin_frames/__init__.py` | 2 |
| `astropy/coordinates/builtin_frames/intermediate_rotation_transforms.py` | 2 |
| `astropy/io/ascii/html.py` | 2 |
| `astropy/wcs/wcsapi/wrappers/sliced_wcs.py` | 2 |
| `astropy/units/format/cds.py` | 2 |
| `astropy/units/format/cds_parsetab.py` | 2 |
| `astropy/utils/misc.py` | 2 |
| `astropy/units/decorators.py` | 2 |
| `astropy/utils/introspection.py` | 2 |
| `astropy/io/fits/header.py` | 2 |

## Section 3 — Test framework signal

Detected: **pytest (file::TestClass::test_method or file::test_func)**

Sample FAIL_TO_PASS test names (first 10):
```
  astropy/modeling/tests/test_separable.py::test_separable[compound_model6-result6]
  astropy/modeling/tests/test_separable.py::test_separable[compound_model9-result9]
  astropy/io/ascii/tests/test_rst.py::test_rst_with_header_rows
  astropy/io/ascii/tests/test_qdp.py::test_roundtrip[True]
  astropy/nddata/mixins/tests/test_ndarithmetic.py::test_nddata_bitmask_arithmetic
  astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_ascii_table_data
  astropy/io/fits/tests/test_table.py::TestTableFunctions::test_ascii_table
  astropy/wcs/tests/test_wcs.py::test_zero_size_input
  astropy/modeling/tests/test_separable.py::test_separable[compound_model6-result6]
  astropy/modeling/tests/test_separable.py::test_separable[compound_model9-result9]
```

## Section 4 — Problem-theme distribution

Top themes across 123 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| other | 41 | 33.3% |
| crash_or_traceback | 22 | 17.9% |
| wrong_output | 21 | 17.1% |
| import_module | 15 | 12.2% |
| documentation | 10 | 8.1% |
| encoding_unicode | 8 | 6.5% |
| config_environment | 2 | 1.6% |
| type_handling | 2 | 1.6% |
| test_failure | 1 | 0.8% |
| regression | 1 | 0.8% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `astropy__astropy-12907`

**Files likely affected**: `astropy/modeling/separable.py`
**FAIL_TO_PASS** (2 tests, first 3): `['astropy/modeling/tests/test_separable.py::test_separable[compound_model6-result6]', 'astropy/modeling/tests/test_separable.py::test_separable[compound_model9-result9]']`

**Problem statement (excerpt):**
> Modeling's 'separability_matrix' does not compute separability correctly for nested CompoundModels Consider the following model:
 
 '''python
 from astropy.modeling import models as m
 from astropy.modeling.separable import separability_matrix
 
 cm = m.Linear1D(10) & m.Linear1D(5)
 '''
 
 It's separability matrix as you might expect is a diagonal:
 
 '''python
 >>> separability_matrix(cm)
 array(

### Sample 2 — `astropy__astropy-14182`

**Files likely affected**: `astropy/io/ascii/rst.py`
**FAIL_TO_PASS** (1 tests, first 3): `['astropy/io/ascii/tests/test_rst.py::test_rst_with_header_rows']`

**Problem statement (excerpt):**
> Please support header rows in RestructuredText output ### Description
 
 It would be great if the following would work:
 
 '''Python
 >>> from astropy.table import QTable
 >>> import astropy.units as u
 >>> import sys
 >>> tbl = QTable({'wave': [350,950]*u.nm, 'response': [0.7, 1.2]*u.count})
 >>> tbl.write(sys.stdout,  format="ascii.rst")
 ===== ========
  wave response
 ===== ========
 350.0    

### Sample 3 — `astropy__astropy-14365`

**Files likely affected**: `astropy/io/ascii/qdp.py`
**FAIL_TO_PASS** (1 tests, first 3): `['astropy/io/ascii/tests/test_qdp.py::test_roundtrip[True]']`

**Problem statement (excerpt):**
> ascii.qdp Table format assumes QDP commands are upper case ### Description  ascii.qdp assumes that commands in a QDP file are upper case, for example, for errors they must be "READ SERR 1 2" whereas QDP itself is not case sensitive and case use "read serr 1 2". 
 
 As many QDP files are created by hand, the expectation that all commands be all-caps should be removed.  ### Expected behavior  The fo

### Sample 4 — `astropy__astropy-14995`

**Files likely affected**: `astropy/nddata/mixins/ndarithmetic.py`
**FAIL_TO_PASS** (1 tests, first 3): `['astropy/nddata/mixins/tests/test_ndarithmetic.py::test_nddata_bitmask_arithmetic']`

**Problem statement (excerpt):**
> In v5.3, NDDataRef mask propagation fails when one of the operand does not have a mask ### Description  This applies to v5.3. 
 
 It looks like when one of the operand does not have a mask, the mask propagation when doing arithmetic, in particular with 'handle_mask=np.bitwise_or' fails.  This is not a problem in v5.2.
 
 I don't know enough about how all that works, but it seems from the error tha

### Sample 5 — `astropy__astropy-6938`

**Files likely affected**: `astropy/io/fits/fitsrec.py`
**FAIL_TO_PASS** (2 tests, first 3): `['astropy/io/fits/tests/test_checksum.py::TestChecksumFunctions::test_ascii_table_data', 'astropy/io/fits/tests/test_table.py::TestTableFunctions::test_ascii_table']`

**Problem statement (excerpt):**
> Possible bug in io.fits related to D exponents I came across the following code in ''fitsrec.py'':
 
 '''python
         # Replace exponent separator in floating point numbers
         if 'D' in format:
             output_field.replace(encode_ascii('E'), encode_ascii('D'))
 '''
 
 I think this may be incorrect because as far as I can tell ''replace'' is not an in-place operation for ''chararray''

### Sample 6 — `astropy__astropy-7746`

**Files likely affected**: `astropy/wcs/wcs.py`
**FAIL_TO_PASS** (1 tests, first 3): `['astropy/wcs/tests/test_wcs.py::test_zero_size_input']`

**Problem statement (excerpt):**
> Issue when passing empty lists/arrays to WCS transformations The following should not fail but instead should return empty lists/arrays:
 
 '''
 In [1]: from astropy.wcs import WCS
 
 In [2]: wcs = WCS('2MASS_h.fits')
 
 In [3]: wcs.wcs_pix2world([], [], 0)
 ---------------------------------------------------------------------------
 InconsistentAxisTypesError                Traceback (most recent

### Sample 7 — `astropy__astropy-12907`

**Files likely affected**: `astropy/modeling/separable.py`
**FAIL_TO_PASS** (2 tests, first 3): `['astropy/modeling/tests/test_separable.py::test_separable[compound_model6-result6]', 'astropy/modeling/tests/test_separable.py::test_separable[compound_model9-result9]']`

**Problem statement (excerpt):**
> Modeling's 'separability_matrix' does not compute separability correctly for nested CompoundModels Consider the following model:
 
 '''python
 from astropy.modeling import models as m
 from astropy.modeling.separable import separability_matrix
 
 cm = m.Linear1D(10) & m.Linear1D(5)
 '''
 
 It's separability matrix as you might expect is a diagonal:
 
 '''python
 >>> separability_matrix(cm)
 array(

### Sample 8 — `astropy__astropy-13033`

**Files likely affected**: `astropy/timeseries/core.py`
**FAIL_TO_PASS** (1 tests, first 3): `['astropy/timeseries/tests/test_sampled.py::test_required_columns']`

**Problem statement (excerpt):**
> TimeSeries: misleading exception when required column check fails. <!-- This comments are hidden when you submit the issue,
 so you do not need to remove them! -->
 
 <!-- Please be sure to check out our contributing guidelines,
 https://github.com/astropy/astropy/blob/main/CONTRIBUTING.md .
 Please be sure to check out our code of conduct,
 https://github.com/astropy/astropy/blob/main/CODE_OF_CON

## Section 6 — Builder guidance

When building a fix for an instance in astropy/astropy:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. astropy/units/quantity.py appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 123 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "astropy/astropy"`).

First 20 instance_ids:

- `astropy__astropy-12907` (dataset: `swe-bench-lite-test`)
- `astropy__astropy-14182` (dataset: `swe-bench-lite-test`)
- `astropy__astropy-14365` (dataset: `swe-bench-lite-test`)
- `astropy__astropy-14995` (dataset: `swe-bench-lite-test`)
- `astropy__astropy-6938` (dataset: `swe-bench-lite-test`)
- `astropy__astropy-7746` (dataset: `swe-bench-lite-test`)
- `astropy__astropy-12907` (dataset: `swe-bench-verified-test`)
- `astropy__astropy-13033` (dataset: `swe-bench-verified-test`)
- `astropy__astropy-13236` (dataset: `swe-bench-verified-test`)
- `astropy__astropy-13398` (dataset: `swe-bench-verified-test`)
- `astropy__astropy-13453` (dataset: `swe-bench-verified-test`)
- `astropy__astropy-13579` (dataset: `swe-bench-verified-test`)
- `astropy__astropy-13977` (dataset: `swe-bench-verified-test`)
- `astropy__astropy-14096` (dataset: `swe-bench-verified-test`)
- `astropy__astropy-14182` (dataset: `swe-bench-verified-test`)
- `astropy__astropy-14309` (dataset: `swe-bench-verified-test`)
- `astropy__astropy-14365` (dataset: `swe-bench-verified-test`)
- `astropy__astropy-14369` (dataset: `swe-bench-verified-test`)
- `astropy__astropy-14508` (dataset: `swe-bench-verified-test`)
- `astropy__astropy-14539` (dataset: `swe-bench-verified-test`)
- ... (103 more)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
