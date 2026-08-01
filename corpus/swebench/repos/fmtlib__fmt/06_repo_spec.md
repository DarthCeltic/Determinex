---
name: swebench-fmtlib__fmt
description: SWE-bench repo behavioral spec for fmtlib/fmt. Aggregated from 52 bug-fix instances across 2 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# fmtlib/fmt — SWE-bench Repo Spec

> **52 bug-fix instances** across 2 dataset(s); language(s): cpp, python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| multi-swe-bench | 41 |
| swe-bench-multilingual-test | 11 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `include/fmt/format.h` | 17 |
| `include/fmt/core.h` | 9 |
| `include/fmt/ranges.h` | 9 |
| `include/fmt/chrono.h` | 8 |
| `include/fmt/std.h` | 4 |
| `include/fmt/color.h` | 4 |
| `include/fmt/base.h` | 2 |
| `include/fmt/printf.h` | 1 |
| `include/fmt/format-inl.h` | 1 |
| `include/fmt/prepare.h` | 1 |
| `fmt/ostream.h` | 1 |

## Section 3 — Test framework signal

Detected: **pytest (dotted module path test_module.test_func)**

Sample FAIL_TO_PASS test names (first 10):
```
  PrintfTest.MinusFlag
  format_test.format_nan
  format_test.format_infinity
  format_test.format_double
  ranges_test.join_tuple
  ranges_test.format_vector
  format_test.zero_flag_and_align
  format_test.width
  locale_test.localized_double
  std_test.path
```

## Section 4 — Problem-theme distribution

Top themes across 52 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| other | 5 | 45.5% |
| wrong_output | 4 | 36.4% |
| edge_case | 1 | 9.1% |
| documentation | 1 | 9.1% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `fmtlib__fmt-1683`

**Files likely affected**: `include/fmt/printf.h`
**FAIL_TO_PASS** (1 tests, first 3): `['PrintfTest.MinusFlag']`

**Problem statement (excerpt):**
> fmt::sprintf ignores minus flag for char First of all thanks for the huge amount of work you put into the library (including shepherding it through standardization).
 
 Me and a friend of mine were at a loss to understand why fmt::sprintf ignores the minus flag when formatting a char from a look at the linked https://pubs.opengroup.org/onlinepubs/009695399/functions/fprintf.html (but it is certain

### Sample 2 — `fmtlib__fmt-2310`

**Files likely affected**: `include/fmt/format.h`, `include/fmt/core.h`
**FAIL_TO_PASS** (2 tests, first 3): `['format_test.format_nan', 'format_test.format_infinity']`

**Problem statement (excerpt):**
> Numeric zero fill is applied to inf/nan From the documentation (emphasis mine):
 > Preceding the width field by a zero ('0') character enables sign-aware zero-padding for numeric types. It forces the padding to be placed after the sign or base (if any) but before the digits. This is used for printing fields in the form '+000000120'. This option is only valid for numeric types and ***it has no effe

### Sample 3 — `fmtlib__fmt-2317`

**Files likely affected**: `include/fmt/format.h`
**FAIL_TO_PASS** (1 tests, first 3): `['format_test.format_double']`

**Problem statement (excerpt):**
> Hex float default alignment From the documentation (emphasis mine):
 <!--StartFragment-->
 Option | Meaning
 -- | --
 '&lt;' | Forces the field to be left-aligned within the available space (this is the default for most objects).
 '&gt;' | Forces the field to be right-aligned within the available space (***this is the default for numbers***).
 '^' | Forces the field to be centered within the avail

### Sample 4 — `fmtlib__fmt-2457`

**Files likely affected**: `include/fmt/ranges.h`
**FAIL_TO_PASS** (1 tests, first 3): `['ranges_test.join_tuple']`

**Problem statement (excerpt):**
> fmt::join tuple does not support format specifiers Using fmt 8.0.1:
 '''
 #include <tuple>
 #include <vector>
 #include <fmt/format.h>
 #include <fmt/ranges.h>
 
 int main() {
   std::vector<int> a = { 1, 2, 3 };
   fmt::print("{:02}\n", fmt::join(a, ", "));
 
   std::tuple<int,int,int> b = std::make_tuple(1, 2, 3);
   fmt::print("{:02}\n", fmt::join(b, ", "));
 }
 '''
 Results in:
 '''
 01, 02, 0

### Sample 5 — `fmtlib__fmt-3158`

**Files likely affected**: `include/fmt/ranges.h`
**FAIL_TO_PASS** (1 tests, first 3): `['ranges_test.format_vector']`

**Problem statement (excerpt):**
> Some ranges of char are misprinted or don't compile [First example](https://godbolt.org/z/4WeMdPdj7):
 
 '''cpp
 #include <ranges>
 #include <string>
 #include <fmt/ranges.h>
 
 int main() {
     std::string line = "a,b-c,d-e,f";
     fmt::print("{}\n", line | std::views::split(','));
 }
 '''
 
 With C++20, this prints the expected/desired:
 
 '''
 [['a'], ['b', '-', 'c'], ['d', '-', 'e'], ['f']]

### Sample 6 — `fmtlib__fmt-3248`

**Files likely affected**: `include/fmt/core.h`
**FAIL_TO_PASS** (2 tests, first 3): `['format_test.zero_flag_and_align', 'format_test.width']`

**Problem statement (excerpt):**
> Wrong formatting when both alignment and '0' for leading zeroes is given According to https://en.cppreference.com/w/cpp/utility/format/formatter: "If the 0 character and an align option both appear, the 0 character is ignored."
 
 '''
 fmt::print("{:<06}\n", -42); // expected: "-42   ", actual: "-42000"
 fmt::print("{:>06}\n", -42); // expected: "   -42", actual: "000-42"
 ''' 

### Sample 7 — `fmtlib__fmt-3272`

**Files likely affected**: `include/fmt/format.h`
**FAIL_TO_PASS** (1 tests, first 3): `['locale_test.localized_double']`

**Problem statement (excerpt):**
> Alignment of floating-point numbers is incorrect if the output is localized and the integer part is zero Consider the following code (https://godbolt.org/z/f7czaGcdG):
 '''
 #include <locale>
 #include <fmt/printf.h>
 
 int main(int argc, char* argv[]) {
     std::locale::global(std::locale("en_US.UTF-8"));
 
     fmt::print("     X = {:19.3Lf}\n", -119.921);
     fmt::print("     Y = {:19.3Lf}\n"

### Sample 8 — `fmtlib__fmt-3729`

**Files likely affected**: `include/fmt/std.h`
**FAIL_TO_PASS** (1 tests, first 3): `['std_test.path']`

**Problem statement (excerpt):**
> Support both generic and native format of std::filesystem::path Why
 -----
 Need a way to include the paths with only slashes rather than backslashes in the output in a cross-platform manner. This can be done by introducing  _'type'_ in format-spec for 'path'.
 
 How to use the proposed feature
 -------------
 On Windows,
 
 '''cpp
 std::filesystem::path filename = R"(C:\Users\zhihaoy\.cache)";
 p

## Section 6 — Builder guidance

When building a fix for an instance in fmtlib/fmt:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. include/fmt/format.h appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 52 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "fmtlib/fmt"`).

First 20 instance_ids:

- `fmtlib__fmt-1683` (dataset: `swe-bench-multilingual-test`)
- `fmtlib__fmt-2310` (dataset: `swe-bench-multilingual-test`)
- `fmtlib__fmt-2317` (dataset: `swe-bench-multilingual-test`)
- `fmtlib__fmt-2457` (dataset: `swe-bench-multilingual-test`)
- `fmtlib__fmt-3158` (dataset: `swe-bench-multilingual-test`)
- `fmtlib__fmt-3248` (dataset: `swe-bench-multilingual-test`)
- `fmtlib__fmt-3272` (dataset: `swe-bench-multilingual-test`)
- `fmtlib__fmt-3729` (dataset: `swe-bench-multilingual-test`)
- `fmtlib__fmt-3750` (dataset: `swe-bench-multilingual-test`)
- `fmtlib__fmt-3863` (dataset: `swe-bench-multilingual-test`)
- `fmtlib__fmt-3901` (dataset: `swe-bench-multilingual-test`)
- `fmtlib__fmt-4310` (dataset: `multi-swe-bench`)
- `fmtlib__fmt-4286` (dataset: `multi-swe-bench`)
- `fmtlib__fmt-4057` (dataset: `multi-swe-bench`)
- `fmtlib__fmt-4055` (dataset: `multi-swe-bench`)
- `fmtlib__fmt-3913` (dataset: `multi-swe-bench`)
- `fmtlib__fmt-3912` (dataset: `multi-swe-bench`)
- `fmtlib__fmt-3863` (dataset: `multi-swe-bench`)
- `fmtlib__fmt-3824` (dataset: `multi-swe-bench`)
- `fmtlib__fmt-3819` (dataset: `multi-swe-bench`)
- ... (32 more)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
