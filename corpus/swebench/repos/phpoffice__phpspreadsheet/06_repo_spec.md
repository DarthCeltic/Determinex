---
name: swebench-phpoffice__phpspreadsheet
description: SWE-bench repo behavioral spec for phpoffice/phpspreadsheet. Aggregated from 10 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# phpoffice/phpspreadsheet — SWE-bench Repo Spec

> **10 bug-fix instances** across 1 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-multilingual-test | 10 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `CHANGELOG.md` | 7 |
| `src/PhpSpreadsheet/Writer/Xlsx/FunctionPrefix.php` | 2 |
| `src/PhpSpreadsheet/Worksheet/Worksheet.php` | 2 |
| `src/PhpSpreadsheet/Spreadsheet.php` | 2 |
| `src/PhpSpreadsheet/Style/Style.php` | 1 |
| `src/PhpSpreadsheet/Calculation/LookupRef/HLookup.php` | 1 |
| `src/PhpSpreadsheet/Calculation/LookupRef/VLookup.php` | 1 |
| `src/PhpSpreadsheet/Calculation/Calculation.php` | 1 |
| `src/PhpSpreadsheet/Calculation/Engine/Operands/StructuredReference.php` | 1 |
| `src/PhpSpreadsheet/Style/NumberFormat/BaseFormatter.php` | 1 |
| `src/PhpSpreadsheet/ReferenceHelper.php` | 1 |
| `src/PhpSpreadsheet/Calculation/MathTrig/Round.php` | 1 |
| `src/PhpSpreadsheet/Calculation/MathTrig/Trunc.php` | 1 |
| `src/PhpSpreadsheet/Reader/Ods/FormulaTranslator.php` | 1 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: Function Prefix > Function prefix with data set "DAYS/NETWORKDAYS 5", Style > Style cell address object, Style > Style cell range object, VLookup > V lookup array with data set "issue 3561", Issue3635 > New example**

Sample FAIL_TO_PASS test names (first 10):
```
  Function Prefix > Function prefix with data set "DAYS/NETWORKDAYS 5"
  Style > Style cell address object
  Style > Style cell range object
  VLookup > V lookup array with data set "issue 3561"
  Issue3635 > New example
  Issue3635 > Original example
  String Helper > Issue 3900
  Worksheet > Remove column with data set "Data includes nulls"
  Issue4112 > Issue 4112 with data set "problem case"
  Issue4112 > Issue 4112 with data set "positive number"
```

## Section 4 — Problem-theme distribution

Top themes across 10 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| wrong_output | 7 | 70.0% |
| crash_or_traceback | 3 | 30.0% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `phpoffice__phpspreadsheet-3463`

**Files likely affected**: `CHANGELOG.md`, `src/PhpSpreadsheet/Writer/Xlsx/FunctionPrefix.php`
**FAIL_TO_PASS** (1 tests, first 3): `['Function Prefix > Function prefix with data set "DAYS/NETWORKDAYS 5"']`

**Problem statement (excerpt):**
> NETWORKDAYS function erroneously being converted to NETWORK_xlfn.DAYS by phpspreadsheet This is:
 
 '''
 - [*] a bug report
 - [ ] a feature request
 - [ ] **not** a usage question (ask them on https://stackoverflow.com/questions/tagged/phpspreadsheet or https://gitter.im/PHPOffice/PhpSpreadsheet)
 '''
 
 ### What is the expected behavior?
 The Excel function "NETWORKDAYS" outputs correctly in the

### Sample 2 — `phpoffice__phpspreadsheet-3469`

**Files likely affected**: `CHANGELOG.md`, `src/PhpSpreadsheet/Style/Style.php`
**FAIL_TO_PASS** (2 tests, first 3): `['Style > Style cell address object', 'Style > Style cell range object']`

**Problem statement (excerpt):**
> Getting a style for a CellAddress instance fails if the worksheet is set in the CellAddress instance There appears to be a bug when applying a number format to a 'Style' instance when 'Style' was created with a 'CellAddress' instance that has got a 'Worksheet' instance defined.
 
 ### What is the expected behaviour?
 
 'Style' instance to be retrieved for further use.
 
 ### What is the current be

### Sample 3 — `phpoffice__phpspreadsheet-3570`

**Files likely affected**: `src/PhpSpreadsheet/Calculation/LookupRef/HLookup.php`, `src/PhpSpreadsheet/Calculation/LookupRef/VLookup.php`
**FAIL_TO_PASS** (1 tests, first 3): `['VLookup > V lookup array with data set "issue 3561"']`

**Problem statement (excerpt):**
> Debug: The index_number parameter of the VLOOKUP function This is:
 
 '''
 - [*] a bug report
 - [ ] a feature request
 - [ ] **not** a usage question (ask them on https://stackoverflow.com/questions/tagged/phpspreadsheet or https://gitter.im/PHPOffice/PhpSpreadsheet)
 '''
 The cell's function is set to VLOOKUP(A7,Sheet2!$A$1:$AG$50,{12,13,12},FALSE)
 
 
 ### What is the expected behavior?
 Return

### Sample 4 — `phpoffice__phpspreadsheet-3659`

**Files likely affected**: `src/PhpSpreadsheet/Worksheet/Worksheet.php`, `src/PhpSpreadsheet/Calculation/Calculation.php`, `src/PhpSpreadsheet/Spreadsheet.php`, `src/PhpSpreadsheet/Calculation/Engine/Operands/StructuredReference.php`
**FAIL_TO_PASS** (2 tests, first 3): `['Issue3635 > New example', 'Issue3635 > Original example']`

**Problem statement (excerpt):**
> Object of class PhpOffice\PhpSpreadsheet\Calculation\Engine\Operands\StructuredReference could not be converted to string when accessing a cell object's getCalculatedValue() This is:
 
 '''
 - [x] a bug report
 - [ ] a feature request
 - [ ] **not** a usage question (ask them on https://stackoverflow.com/questions/tagged/phpspreadsheet or https://gitter.im/PHPOffice/PhpSpreadsheet)
 '''
 
 ### Wha

### Sample 5 — `phpoffice__phpspreadsheet-3903`

**Files likely affected**: `src/PhpSpreadsheet/Style/NumberFormat/BaseFormatter.php`
**FAIL_TO_PASS** (1 tests, first 3): `['String Helper > Issue 3900']`

**Problem statement (excerpt):**
> When writing CSV file thousand separator and decimal separator are not respected This is:
 
 - [x] a bug report
 - [ ] a feature request
 - [ ] **not** a usage question (ask them on https://stackoverflow.com/questions/tagged/phpspreadsheet or https://gitter.im/PHPOffice/PhpSpreadsheet)
 
 ### What is the expected behavior?
 
 
 CSV to have numbers set as is defined in decimal separator and thousan

### Sample 6 — `phpoffice__phpspreadsheet-3940`

**Files likely affected**: `CHANGELOG.md`, `src/PhpSpreadsheet/ReferenceHelper.php`
**FAIL_TO_PASS** (1 tests, first 3): `['Worksheet > Remove column with data set "Data includes nulls"']`

**Problem statement (excerpt):**
> [Bug] Removing column when next column value is null shifts cell value from deleted column into the next column This is:
 
 '''
 - [x] a bug report
 - [ ] a feature request
 - [ ] **not** a usage question (ask them on https://stackoverflow.com/questions/tagged/phpspreadsheet or https://gitter.im/PHPOffice/PhpSpreadsheet)
 '''
 
 ### What is the expected behavior?
 
 Removing the column when the ne

### Sample 7 — `phpoffice__phpspreadsheet-4114`

**Files likely affected**: `src/PhpSpreadsheet/Worksheet/Worksheet.php`, `CHANGELOG.md`, `src/PhpSpreadsheet/Spreadsheet.php`
**FAIL_TO_PASS** (2 tests, first 3): `['Issue4112 > Issue 4112 with data set "problem case"', 'Issue4112 > Issue 4112 with data set "positive number"']`

**Problem statement (excerpt):**
> Your requested sheet index: -1 is out of bounds. The actual number of sheets is 1 This is:
 
 '''
 - [ ] a bug report
 '''
 
 ### What is the expected behavior?
 
 not throwing an Exception ? 
 
 ### What is the current behavior?
 
 [Exception]
 HTTP 500 Internal Server Error
 Your requested sheet index: -1 is out of bounds. The actual number of sheets is 1.
 
 ### What are the steps to reproduce?

### Sample 8 — `phpoffice__phpspreadsheet-4186`

**Files likely affected**: `CHANGELOG.md`, `src/PhpSpreadsheet/Writer/Xlsx/FunctionPrefix.php`
**FAIL_TO_PASS** (1 tests, first 3): `['Function Prefix > Function prefix with data set "SUMIFS reclassified as Legacy"']`

**Problem statement (excerpt):**
> Unnecessary _xlfn prefix for SUMIFS This is:
 
 - a bug report
 
 ### What is the expected behavior?
 Save 'SUMIFS' function to XLSX without '_xlfn' prefix.
 
 ### What is the current behavior?
 PhpSpreadsheet adds a '_xlfn' prefix to 'SUMIFS', which breaks LO Calc compatibility.
 
 ### What are the steps to reproduce?
 I think 'SUMIFS' function was mistakenly categorized as released in Excel 2019

## Section 6 — Builder guidance

When building a fix for an instance in phpoffice/phpspreadsheet:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. CHANGELOG.md appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 10 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "phpoffice/phpspreadsheet"`).

First 20 instance_ids:

- `phpoffice__phpspreadsheet-3463` (dataset: `swe-bench-multilingual-test`)
- `phpoffice__phpspreadsheet-3469` (dataset: `swe-bench-multilingual-test`)
- `phpoffice__phpspreadsheet-3570` (dataset: `swe-bench-multilingual-test`)
- `phpoffice__phpspreadsheet-3659` (dataset: `swe-bench-multilingual-test`)
- `phpoffice__phpspreadsheet-3903` (dataset: `swe-bench-multilingual-test`)
- `phpoffice__phpspreadsheet-3940` (dataset: `swe-bench-multilingual-test`)
- `phpoffice__phpspreadsheet-4114` (dataset: `swe-bench-multilingual-test`)
- `phpoffice__phpspreadsheet-4186` (dataset: `swe-bench-multilingual-test`)
- `phpoffice__phpspreadsheet-4214` (dataset: `swe-bench-multilingual-test`)
- `phpoffice__phpspreadsheet-4313` (dataset: `swe-bench-multilingual-test`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
