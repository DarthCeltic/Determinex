---
name: swebench-pvlib__pvlib-python
description: SWE-bench repo behavioral spec for pvlib/pvlib-python. Aggregated from 68 bug-fix instances across 2 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# pvlib/pvlib-python — SWE-bench Repo Spec

> **68 bug-fix instances** across 2 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-full-dev | 63 |
| swe-bench-lite-dev | 5 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `pvlib/pvsystem.py` | 19 |
| `pvlib/modelchain.py` | 14 |
| `pvlib/tracking.py` | 11 |
| `pvlib/irradiance.py` | 7 |
| `pvlib/tools.py` | 6 |
| `pvlib/singlediode.py` | 5 |
| `pvlib/iam.py` | 4 |
| `pvlib/iotools/pvgis.py` | 4 |
| `pvlib/temperature.py` | 3 |
| `pvlib/ivtools/sdm.py` | 3 |
| `pvlib/iotools/__init__.py` | 3 |
| `pvlib/iotools/crn.py` | 3 |
| `pvlib/bifacial/infinite_sheds.py` | 3 |
| `pvlib/clearsky.py` | 3 |
| `pvlib/soiling.py` | 2 |
| `pvlib/scaling.py` | 2 |
| `setup.py` | 2 |
| `pvlib/shading.py` | 2 |
| `pvlib/iotools/tmy.py` | 2 |
| `pvlib/iotools/sodapro.py` | 2 |
| `pvlib/bifacial/utils.py` | 2 |
| `pvlib/location.py` | 2 |
| `pvlib/forecast.py` | 1 |
| `pvlib/solarposition.py` | 1 |
| `pvlib/spectrum/spectrl2.py` | 1 |
| `pvlib/ivtools/utility.py` | 1 |
| `pvlib/ivtools/sde.py` | 1 |
| `pvlib/ivtools/__init__.py` | 1 |
| `docs/examples/soiling/plot_greensboro_kimber_soiling.py` | 1 |
| `docs/examples/irradiance-transposition/plot_seasonal_tilt.py` | 1 |

## Section 3 — Test framework signal

Detected: **pytest (file::TestClass::test_method or file::test_func)**

Sample FAIL_TO_PASS test names (first 10):
```
  pvlib/tests/test_iam.py::test_physical_n1_L0
  pvlib/tests/test_temperature.py::test_fuentes_timezone[Etc/GMT+5]
  pvlib/tests/test_tools.py::test__golden_sect_DataFrame_vector
  pvlib/tests/test_pvsystem.py::test_PVSystem_single_array
  pvlib/tests/test_irradiance.py::test_reindl
  pvlib/tests/test_modelchain.py::test_run_model_tracker_list
  pvlib/tests/test_soiling.py::test_hsu_no_cleaning
  pvlib/tests/test_soiling.py::test_hsu
  pvlib/tests/test_soiling.py::test_hsu_defaults
  pvlib/tests/test_soiling.py::test_hsu_variable_time_intervals
```

## Section 4 — Problem-theme distribution

Top themes across 68 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| other | 27 | 39.7% |
| wrong_output | 11 | 16.2% |
| documentation | 9 | 13.2% |
| edge_case | 6 | 8.8% |
| import_module | 5 | 7.4% |
| crash_or_traceback | 4 | 5.9% |
| regression | 2 | 2.9% |
| performance | 2 | 2.9% |
| config_environment | 1 | 1.5% |
| api_change | 1 | 1.5% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `pvlib__pvlib-python-1707`

**Files likely affected**: `pvlib/iam.py`
**FAIL_TO_PASS** (1 tests, first 3): `['pvlib/tests/test_iam.py::test_physical_n1_L0']`

**Problem statement (excerpt):**
> regression: iam.physical returns nan for aoi > 90° when n = 1 **Describe the bug**
 For pvlib==0.9.5, when n = 1 (no reflection) and aoi > 90°, we get nan as result.
 
 **To Reproduce**
 '''python
 import pvlib
 pvlib.iam.physical(aoi=100, n=1)
 '''
 returns 'nan'.
 
 **Expected behavior**
 The result should be '0', as it was for pvlib <= 0.9.4.
 
 
 **Versions:**
  - ''pvlib.__version__'': '0.9.5

### Sample 2 — `pvlib__pvlib-python-1072`

**Files likely affected**: `pvlib/temperature.py`
**FAIL_TO_PASS** (1 tests, first 3): `['pvlib/tests/test_temperature.py::test_fuentes_timezone[Etc/GMT+5]']`

**Problem statement (excerpt):**
> temperature.fuentes errors when given tz-aware inputs on pandas>=1.0.0 **Describe the bug**
 When the weather timeseries inputs to 'temperature.fuentes' have tz-aware index, an internal call to 'np.diff(index)' returns an array of 'Timedelta' objects instead of an array of nanosecond ints, throwing an error immediately after.  The error only happens when using pandas>=1.0.0; using 0.25.3 runs succ

### Sample 3 — `pvlib__pvlib-python-1606`

**Files likely affected**: `pvlib/tools.py`
**FAIL_TO_PASS** (1 tests, first 3): `['pvlib/tests/test_tools.py::test__golden_sect_DataFrame_vector']`

**Problem statement (excerpt):**
> golden-section search fails when upper and lower bounds are equal **Describe the bug**
 I was using pvlib for sometime now and until now I was always passing a big dataframe containing readings of a long period. Because of some changes in our software architecture, I need to pass the weather readings as a single reading (a dataframe with only one row) and I noticed that for readings that GHI-DHI a

### Sample 4 — `pvlib__pvlib-python-1854`

**Files likely affected**: `pvlib/pvsystem.py`
**FAIL_TO_PASS** (1 tests, first 3): `['pvlib/tests/test_pvsystem.py::test_PVSystem_single_array']`

**Problem statement (excerpt):**
> PVSystem with single Array generates an error **Is your feature request related to a problem? Please describe.**
 
 When a PVSystem has a single Array, you can't assign just the Array instance when constructing the PVSystem.
 
 '''
 mount = pvlib.pvsystem.FixedMount(surface_tilt=35, surface_azimuth=180)
 array = pvlib.pvsystem.Array(mount=mount)
 pv = pvlib.pvsystem.PVSystem(arrays=array)
 
 -----

### Sample 5 — `pvlib__pvlib-python-1154`

**Files likely affected**: `pvlib/irradiance.py`
**FAIL_TO_PASS** (1 tests, first 3): `['pvlib/tests/test_irradiance.py::test_reindl']`

**Problem statement (excerpt):**
> pvlib.irradiance.reindl() model generates NaNs when GHI = 0 **Describe the bug**
 The reindl function should give zero sky diffuse when GHI is zero. Instead it generates NaN or Inf values due to "term3" having a quotient that divides by GHI.  
 
 **Expected behavior**
 The reindl function should result in zero sky diffuse when GHI is zero.
 
  pvlib.irradiance.reindl() model generates NaNs when GH

### Sample 6 — `pvlib__pvlib-python-1160`

**Files likely affected**: `pvlib/tracking.py`
**FAIL_TO_PASS** (1 tests, first 3): `['pvlib/tests/test_modelchain.py::test_run_model_tracker_list']`

**Problem statement (excerpt):**
> ValueError: SingleAxisTracker, Array, and running the model on a tuple/list of weather **Describe the bug**
 I know a refactoring of the Array with single axis tracking is in the works #1146. In the meantime, a 'ValueError' is raised when trying to run a SingleAxisTracker defined with an array and supplying (ghi, dni, dhi) weather as a tuple/list. I would expect calling 'run_model([weather])' woul

### Sample 7 — `pvlib__pvlib-python-1738`

**Files likely affected**: `pvlib/soiling.py`
**FAIL_TO_PASS** (4 tests, first 3): `['pvlib/tests/test_soiling.py::test_hsu_no_cleaning', 'pvlib/tests/test_soiling.py::test_hsu', 'pvlib/tests/test_soiling.py::test_hsu_defaults']`

**Problem statement (excerpt):**
> 'pvlib.soiling.hsu' takes 'tilt' instead of 'surface_tilt' 'pvlib.soiling.hsu' takes a 'tilt' parameter representing the same thing we normally call 'surface_tilt':
 
 https://github.com/pvlib/pvlib-python/blob/7a2ec9b4765124463bf0ddd0a49dcfedc4cbcad7/pvlib/soiling.py#L13-L14
 
 https://github.com/pvlib/pvlib-python/blob/7a2ec9b4765124463bf0ddd0a49dcfedc4cbcad7/pvlib/soiling.py#L33-L34
 
 I don't 

### Sample 8 — `pvlib__pvlib-python-1782`

**Files likely affected**: `pvlib/singlediode.py`
**FAIL_TO_PASS** (1 tests, first 3): `['pvlib/tests/test_singlediode.py::test_singlediode_lambert_negative_voc']`

**Problem statement (excerpt):**
> _golden_sect_DataFrame changes in 0.9.4 **Describe the bug**
 
 '0.9.4' introduced the following changes in the '_golden_sect_DataFrame': We are checking 'upper' and 'lower' parameters and raise an error if 'lower > upper'.
 
 https://github.com/pvlib/pvlib-python/blob/81598e4fa8a9bd8fadaa7544136579c44885b3d1/pvlib/tools.py#L344-L345
 
 '_golden_sect_DataFrame' is used by '_lambertw':
 
 https://g

## Section 6 — Builder guidance

When building a fix for an instance in pvlib/pvlib-python:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. pvlib/pvsystem.py appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 68 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "pvlib/pvlib-python"`).

First 20 instance_ids:

- `pvlib__pvlib-python-1707` (dataset: `swe-bench-lite-dev`)
- `pvlib__pvlib-python-1072` (dataset: `swe-bench-lite-dev`)
- `pvlib__pvlib-python-1606` (dataset: `swe-bench-lite-dev`)
- `pvlib__pvlib-python-1854` (dataset: `swe-bench-lite-dev`)
- `pvlib__pvlib-python-1154` (dataset: `swe-bench-lite-dev`)
- `pvlib__pvlib-python-1160` (dataset: `swe-bench-full-dev`)
- `pvlib__pvlib-python-1738` (dataset: `swe-bench-full-dev`)
- `pvlib__pvlib-python-1782` (dataset: `swe-bench-full-dev`)
- `pvlib__pvlib-python-1719` (dataset: `swe-bench-full-dev`)
- `pvlib__pvlib-python-1426` (dataset: `swe-bench-full-dev`)
- `pvlib__pvlib-python-807` (dataset: `swe-bench-full-dev`)
- `pvlib__pvlib-python-1138` (dataset: `swe-bench-full-dev`)
- `pvlib__pvlib-python-1213` (dataset: `swe-bench-full-dev`)
- `pvlib__pvlib-python-1707` (dataset: `swe-bench-full-dev`)
- `pvlib__pvlib-python-1395` (dataset: `swe-bench-full-dev`)
- `pvlib__pvlib-python-1216` (dataset: `swe-bench-full-dev`)
- `pvlib__pvlib-python-1191` (dataset: `swe-bench-full-dev`)
- `pvlib__pvlib-python-823` (dataset: `swe-bench-full-dev`)
- `pvlib__pvlib-python-1368` (dataset: `swe-bench-full-dev`)
- `pvlib__pvlib-python-1448` (dataset: `swe-bench-full-dev`)
- ... (48 more)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
