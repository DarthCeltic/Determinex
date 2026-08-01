---
name: swebench-matplotlib__matplotlib
description: SWE-bench repo behavioral spec for matplotlib/matplotlib. Aggregated from 241 bug-fix instances across 3 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# matplotlib/matplotlib — SWE-bench Repo Spec

> **241 bug-fix instances** across 3 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-full-test | 184 |
| swe-bench-verified-test | 34 |
| swe-bench-lite-test | 23 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `lib/matplotlib/axes/_axes.py` | 28 |
| `lib/matplotlib/figure.py` | 26 |
| `lib/matplotlib/axes/_base.py` | 18 |
| `lib/matplotlib/widgets.py` | 14 |
| `lib/matplotlib/axis.py` | 14 |
| `lib/matplotlib/colors.py` | 12 |
| `lib/matplotlib/legend.py` | 11 |
| `lib/matplotlib/contour.py` | 11 |
| `lib/matplotlib/offsetbox.py` | 10 |
| `lib/matplotlib/colorbar.py` | 10 |
| `lib/matplotlib/pyplot.py` | 10 |
| `lib/mpl_toolkits/mplot3d/axes3d.py` | 9 |
| `lib/matplotlib/collections.py` | 9 |
| `lib/matplotlib/__init__.py` | 8 |
| `lib/matplotlib/text.py` | 7 |
| `lib/mpl_toolkits/mplot3d/art3d.py` | 6 |
| `lib/matplotlib/dates.py` | 6 |
| `lib/matplotlib/backends/backend_ps.py` | 5 |
| `lib/matplotlib/image.py` | 5 |
| `lib/matplotlib/cm.py` | 5 |
| `lib/matplotlib/artist.py` | 4 |
| `lib/matplotlib/cbook.py` | 4 |
| `lib/matplotlib/ticker.py` | 4 |
| `lib/matplotlib/patches.py` | 4 |
| `lib/matplotlib/style/core.py` | 3 |
| `lib/matplotlib/tri/_tricontour.py` | 3 |
| `lib/matplotlib/backends/backend_agg.py` | 3 |
| `lib/matplotlib/animation.py` | 3 |
| `lib/matplotlib/backends/backend_pgf.py` | 3 |
| `lib/matplotlib/cbook/__init__.py` | 3 |

## Section 3 — Test framework signal

Detected: **pytest (file::TestClass::test_method or file::test_func)**

Sample FAIL_TO_PASS test names (first 10):
```
  lib/matplotlib/tests/test_matplotlib.py::test_parse_to_version_info[3.5.0-version_tuple0]
  lib/matplotlib/tests/test_matplotlib.py::test_parse_to_version_info[3.5.0rc2-version_tuple1]
  lib/matplotlib/tests/test_matplotlib.py::test_parse_to_version_info[3.5.0.dev820+g6768ef8c4c-version_tuple2]
  lib/matplotlib/tests/test_matplotlib.py::test_parse_to_version_info[3.5.0.post820+g6768ef8c4c-version_tuple3]
  lib/matplotlib/tests/test_widgets.py::test_range_slider[horizontal]
  lib/matplotlib/tests/test_widgets.py::test_range_slider[vertical]
  lib/matplotlib/tests/test_artist.py::test_format_cursor_data_BoundaryNorm
  lib/matplotlib/tests/test_rcparams.py::test_no_backend_reset_rccontext
  lib/mpl_toolkits/tests/test_mplot3d.py::test_invisible_axes[png]
  lib/matplotlib/tests/test_figure.py::test_unpickle_with_device_pixel_ratio
```

## Section 4 — Problem-theme distribution

Top themes across 241 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| import_module | 62 | 25.7% |
| other | 53 | 22.0% |
| wrong_output | 27 | 11.2% |
| crash_or_traceback | 26 | 10.8% |
| config_environment | 21 | 8.7% |
| edge_case | 15 | 6.2% |
| documentation | 11 | 4.6% |
| regression | 9 | 3.7% |
| concurrency | 6 | 2.5% |
| type_handling | 5 | 2.1% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `matplotlib__matplotlib-18869`

**Files likely affected**: `lib/matplotlib/__init__.py`
**FAIL_TO_PASS** (4 tests, first 3): `['lib/matplotlib/tests/test_matplotlib.py::test_parse_to_version_info[3.5.0-version_tuple0]', 'lib/matplotlib/tests/test_matplotlib.py::test_parse_to_version_info[3.5.0rc2-version_tuple1]', 'lib/matplotlib/tests/test_matplotlib.py::test_parse_to_version_info[3.5.0.dev820+g6768ef8c4c-version_tuple2]']`

**Problem statement (excerpt):**
> Add easily comparable version info to toplevel <!--
 Welcome! Thanks for thinking of a way to improve Matplotlib.
 
 
 Before creating a new feature request please search the issues for relevant feature requests.
 -->
 
 ### Problem
 
 Currently matplotlib only exposes '__version__'.  For quick version checks, exposing either a 'version_info' tuple (which can be compared with other tuples) or a 'L

### Sample 2 — `matplotlib__matplotlib-22711`

**Files likely affected**: `lib/matplotlib/widgets.py`
**FAIL_TO_PASS** (2 tests, first 3): `['lib/matplotlib/tests/test_widgets.py::test_range_slider[horizontal]', 'lib/matplotlib/tests/test_widgets.py::test_range_slider[vertical]']`

**Problem statement (excerpt):**
> [Bug]: cannot give init value for RangeSlider widget ### Bug summary
 
 I think 'xy[4] = .25, val[0]' should be commented in /matplotlib/widgets. py", line 915, in set_val
 as it prevents to initialized value for RangeSlider
 
 ### Code for reproduction
 
 '''python
 import numpy as np
 import matplotlib.pyplot as plt
 from matplotlib.widgets import RangeSlider
 
 # generate a fake image
 np.rando

### Sample 3 — `matplotlib__matplotlib-22835`

**Files likely affected**: `lib/matplotlib/artist.py`
**FAIL_TO_PASS** (1 tests, first 3): `['lib/matplotlib/tests/test_artist.py::test_format_cursor_data_BoundaryNorm']`

**Problem statement (excerpt):**
> [Bug]: scalar mappable format_cursor_data crashes on BoundarNorm ### Bug summary
 
 In 3.5.0 if you do:
 
 '''python
 import matplotlib.pyplot as plt
 import numpy as np
 import matplotlib as mpl
 
 fig, ax = plt.subplots()
 norm = mpl.colors.BoundaryNorm(np.linspace(-4, 4, 5), 256)
 X = np.random.randn(10, 10)
 pc = ax.imshow(X, cmap='RdBu_r', norm=norm)
 '''
 
 and mouse over the image, it crash

### Sample 4 — `matplotlib__matplotlib-23299`

**Files likely affected**: `lib/matplotlib/__init__.py`
**FAIL_TO_PASS** (1 tests, first 3): `['lib/matplotlib/tests/test_rcparams.py::test_no_backend_reset_rccontext']`

**Problem statement (excerpt):**
> [Bug]: get_backend() clears figures from Gcf.figs if they were created under rc_context ### Bug summary
 
 calling 'matplotlib.get_backend()' removes all figures from 'Gcf' if the *first* figure in 'Gcf.figs' was created in an 'rc_context'.
 
 ### Code for reproduction
 
 '''python
 import matplotlib.pyplot as plt
 from matplotlib import get_backend, rc_context
 
 # fig1 = plt.figure()  # <- UNCOM

### Sample 5 — `matplotlib__matplotlib-23314`

**Files likely affected**: `lib/mpl_toolkits/mplot3d/axes3d.py`
**FAIL_TO_PASS** (1 tests, first 3): `['lib/mpl_toolkits/tests/test_mplot3d.py::test_invisible_axes[png]']`

**Problem statement (excerpt):**
> [Bug]: set_visible() not working for 3d projection  ### Bug summary
 
 in the subplot projection="3d" the set_visible function doesn't work even if the value is set to False
 
 ### Code for reproduction
 
 '''python
 import matplotlib.pyplot as plt
 from matplotlib.gridspec import GridSpec
 
 fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw={'projection': '3d'})
 ax1.scatter(1,1,1)
 ax2.scatter(1,1

### Sample 6 — `matplotlib__matplotlib-23476`

**Files likely affected**: `lib/matplotlib/figure.py`
**FAIL_TO_PASS** (1 tests, first 3): `['lib/matplotlib/tests/test_figure.py::test_unpickle_with_device_pixel_ratio']`

**Problem statement (excerpt):**
> [Bug]: DPI of a figure is doubled after unpickling on M1 Mac ### Bug summary
 
 When a figure is unpickled, it's dpi is doubled. This behaviour happens every time and if done in a loop it can cause an 'OverflowError'.
 
 ### Code for reproduction
 
 '''python
 import numpy as np
 import matplotlib
 import matplotlib.pyplot as plt
 import pickle
 import platform
 
 print(matplotlib.get_backend())
 

### Sample 7 — `matplotlib__matplotlib-23562`

**Files likely affected**: `lib/mpl_toolkits/mplot3d/art3d.py`
**FAIL_TO_PASS** (2 tests, first 3): `['lib/mpl_toolkits/tests/test_mplot3d.py::test_Poly3DCollection_get_facecolor', 'lib/mpl_toolkits/tests/test_mplot3d.py::test_Poly3DCollection_get_edgecolor']`

**Problem statement (excerpt):**
> 'Poly3DCollection' object has no attribute '_facecolors2d' The following minimal example demonstrates the issue:  ''' import numpy as np import matplotlib.tri as mtri import matplotlib.pyplot as plt from mpl_toolkits.mplot3d import Axes3D  y,x = np.ogrid[1:10:100j, 1:10:100j] z2 = np.cos(x)**3 - np.sin(y)**2 fig = plt.figure() ax = fig.add_subplot(111, projection='3d') r = ax.plot_surface(x,y,z2, 

### Sample 8 — `matplotlib__matplotlib-23563`

**Files likely affected**: `lib/mpl_toolkits/mplot3d/art3d.py`
**FAIL_TO_PASS** (1 tests, first 3): `['lib/mpl_toolkits/tests/test_mplot3d.py::test_draw_single_lines_from_Nx1']`

**Problem statement (excerpt):**
> [Bug]: 'Line3D' object has no attribute '_verts3d' ### Bug summary  I use matplotlib 3D to visualize some lines in 3D. When I first run the following code, the code can run right. But, if I give 'x_s_0[n]' a numpy array, it will report the error 'input operand has more dimensions than allowed by the axis remapping'. The point is when next I give  'x_s_0[n]' and other variables an int number, the A

## Section 6 — Builder guidance

When building a fix for an instance in matplotlib/matplotlib:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. lib/matplotlib/axes/_axes.py appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 241 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "matplotlib/matplotlib"`).

First 20 instance_ids:

- `matplotlib__matplotlib-18869` (dataset: `swe-bench-lite-test`)
- `matplotlib__matplotlib-22711` (dataset: `swe-bench-lite-test`)
- `matplotlib__matplotlib-22835` (dataset: `swe-bench-lite-test`)
- `matplotlib__matplotlib-23299` (dataset: `swe-bench-lite-test`)
- `matplotlib__matplotlib-23314` (dataset: `swe-bench-lite-test`)
- `matplotlib__matplotlib-23476` (dataset: `swe-bench-lite-test`)
- `matplotlib__matplotlib-23562` (dataset: `swe-bench-lite-test`)
- `matplotlib__matplotlib-23563` (dataset: `swe-bench-lite-test`)
- `matplotlib__matplotlib-23913` (dataset: `swe-bench-lite-test`)
- `matplotlib__matplotlib-23964` (dataset: `swe-bench-lite-test`)
- `matplotlib__matplotlib-23987` (dataset: `swe-bench-lite-test`)
- `matplotlib__matplotlib-24149` (dataset: `swe-bench-lite-test`)
- `matplotlib__matplotlib-24265` (dataset: `swe-bench-lite-test`)
- `matplotlib__matplotlib-24334` (dataset: `swe-bench-lite-test`)
- `matplotlib__matplotlib-24970` (dataset: `swe-bench-lite-test`)
- `matplotlib__matplotlib-25079` (dataset: `swe-bench-lite-test`)
- `matplotlib__matplotlib-25311` (dataset: `swe-bench-lite-test`)
- `matplotlib__matplotlib-25332` (dataset: `swe-bench-lite-test`)
- `matplotlib__matplotlib-25433` (dataset: `swe-bench-lite-test`)
- `matplotlib__matplotlib-25442` (dataset: `swe-bench-lite-test`)
- ... (221 more)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
