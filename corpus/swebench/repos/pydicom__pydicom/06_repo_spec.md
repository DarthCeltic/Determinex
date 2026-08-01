---
name: swebench-pydicom__pydicom
description: SWE-bench repo behavioral spec for pydicom/pydicom. Aggregated from 61 bug-fix instances across 2 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# pydicom/pydicom — SWE-bench Repo Spec

> **61 bug-fix instances** across 2 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-full-dev | 56 |
| swe-bench-lite-dev | 5 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `pydicom/dataset.py` | 12 |
| `pydicom/dataelem.py` | 12 |
| `pydicom/valuerep.py` | 12 |
| `pydicom/filewriter.py` | 11 |
| `pydicom/pixel_data_handlers/util.py` | 6 |
| `pydicom/jsonrep.py` | 5 |
| `pydicom/filereader.py` | 5 |
| `pydicom/config.py` | 4 |
| `pydicom/values.py` | 4 |
| `pydicom/charset.py` | 4 |
| `pydicom/fileset.py` | 3 |
| `pydicom/sequence.py` | 2 |
| `pydicom/encaps.py` | 2 |
| `pydicom/pixel_data_handlers/numpy_handler.py` | 2 |
| `pydicom/filebase.py` | 2 |
| `pydicom/_version.py` | 1 |
| `setup.py` | 1 |
| `pydicom/data/data_manager.py` | 1 |
| `pydicom/dicomdir.py` | 1 |
| `pydicom/fileutil.py` | 1 |
| `pydicom/pixel_data_handlers/rle_handler.py` | 1 |
| `pydicom/multival.py` | 1 |
| `pydicom/util/codify.py` | 1 |
| `pydicom/cli/main.py` | 1 |
| `pydicom/datadict.py` | 1 |
| `pydicom/uid.py` | 1 |
| `pydicom/pixel_data_handlers/__init__.py` | 1 |
| `pydicom/encoders/base.py` | 1 |

## Section 3 — Test framework signal

Detected: **pytest (file::TestClass::test_method or file::test_func)**

Sample FAIL_TO_PASS test names (first 10):
```
  pydicom/tests/test_json.py::TestDataSetToJson::test_suppress_invalid_tags_with_failed_dataelement
  pydicom/tests/test_valuerep.py::test_assigning_bytes[OD-bytes-vm017-vmN17-DoubleFloatPixelData]
  pydicom/tests/test_valuerep.py::test_assigning_bytes[OL-bytes-vm019-vmN19-TrackPointIndexList]
  pydicom/tests/test_valuerep.py::test_assigning_bytes[OV-bytes-vm020-vmN20-SelectorOVValue]
  pydicom/tests/test_config.py::TestDebug::test_default
  pydicom/tests/test_config.py::TestDebug::test_debug_on_handler_null
  pydicom/tests/test_config.py::TestDebug::test_debug_off_handler_null
  pydicom/tests/test_config.py::TestDebug::test_debug_on_handler_stream
  pydicom/tests/test_config.py::TestDebug::test_debug_off_handler_stream
  pydicom/tests/test_valuerep.py::TestPersonName::test_next
```

## Section 4 — Problem-theme distribution

Top themes across 61 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| crash_or_traceback | 19 | 31.1% |
| wrong_output | 11 | 18.0% |
| other | 11 | 18.0% |
| type_handling | 5 | 8.2% |
| encoding_unicode | 4 | 6.6% |
| config_environment | 3 | 4.9% |
| import_module | 2 | 3.3% |
| edge_case | 2 | 3.3% |
| documentation | 2 | 3.3% |
| regression | 1 | 1.6% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `pydicom__pydicom-1694`

**Files likely affected**: `pydicom/dataset.py`
**FAIL_TO_PASS** (1 tests, first 3): `['pydicom/tests/test_json.py::TestDataSetToJson::test_suppress_invalid_tags_with_failed_dataelement']`

**Problem statement (excerpt):**
> Dataset.to_json_dict can still generate exceptions when suppress_invalid_tags=True **Describe the bug**
 I'm using 'Dataset.to_json_dict(suppress_invalid_tags=True)' and can live with losing invalid tags.  Unfortunately, I can still trigger an exception with something like  '2.0' in an 'IS' field.
 
 **Expected behavior**
 to_json_dict shouldn't throw an error about an invalid tag when 'suppress_i

### Sample 2 — `pydicom__pydicom-1413`

**Files likely affected**: `pydicom/dataelem.py`
**FAIL_TO_PASS** (3 tests, first 3): `['pydicom/tests/test_valuerep.py::test_assigning_bytes[OD-bytes-vm017-vmN17-DoubleFloatPixelData]', 'pydicom/tests/test_valuerep.py::test_assigning_bytes[OL-bytes-vm019-vmN19-TrackPointIndexList]', 'pydicom/tests/test_valuerep.py::test_assigning_bytes[OV-bytes-vm020-vmN20-SelectorOVValue]']`

**Problem statement (excerpt):**
> Error : a bytes-like object is required, not 'MultiValue' Hello,
 
 I am getting following error while updating the tag LongTrianglePointIndexList (0066,0040),
 **TypeError: a bytes-like object is required, not 'MultiValue'**
 
 I noticed that the error  gets produced only when the VR is given as "OL" , works fine with "OB", "OF" etc.
 
 sample code (assume 'lineSeq' is the dicom dataset sequence)

### Sample 3 — `pydicom__pydicom-901`

**Files likely affected**: `pydicom/config.py`
**FAIL_TO_PASS** (5 tests, first 3): `['pydicom/tests/test_config.py::TestDebug::test_default', 'pydicom/tests/test_config.py::TestDebug::test_debug_on_handler_null', 'pydicom/tests/test_config.py::TestDebug::test_debug_off_handler_null']`

**Problem statement (excerpt):**
> pydicom should not define handler, formatter and log level. The 'config' module (imported when pydicom is imported) defines a handler and set the log level for the pydicom logger. This should not be the case IMO. It should be the responsibility of the client code of pydicom to configure the logging module to its convenience. Otherwise one end up having multiple logs record as soon as pydicom is im

### Sample 4 — `pydicom__pydicom-1139`

**Files likely affected**: `pydicom/valuerep.py`
**FAIL_TO_PASS** (3 tests, first 3): `['pydicom/tests/test_valuerep.py::TestPersonName::test_next', 'pydicom/tests/test_valuerep.py::TestPersonName::test_iterator', 'pydicom/tests/test_valuerep.py::TestPersonName::test_contains']`

**Problem statement (excerpt):**
> Make PersonName3 iterable '''python
 from pydicom import Dataset
 
 ds = Dataset()
 ds.PatientName = 'SomeName'
 
 'S' in ds.PatientName
 '''
 '''
 Traceback (most recent call last):
   File "<stdin>", line 1, in <module>
 TypeError: argument of type 'PersonName3' is not iterable
 '''
 
 I'm not really sure if this is intentional or if PN elements should support 'str' methods. And yes I know I can

### Sample 5 — `pydicom__pydicom-1256`

**Files likely affected**: `pydicom/jsonrep.py`
**FAIL_TO_PASS** (1 tests, first 3): `['pydicom/tests/test_json.py::TestBinary::test_bulk_data_reader_is_called_within_SQ']`

**Problem statement (excerpt):**
> from_json does not correctly convert BulkDataURI's in SQ data elements **Describe the bug**
 When a DICOM object contains large data elements in SQ elements and is converted to JSON, those elements are correctly turned into BulkDataURI's. However, when the JSON is converted back to DICOM using from_json, the BulkDataURI's in SQ data elements are not converted back and warnings are thrown.
 
 **Exp

### Sample 6 — `pydicom__pydicom-996`

**Files likely affected**: `pydicom/dataset.py`, `pydicom/filewriter.py`, `pydicom/sequence.py`
**FAIL_TO_PASS** (1 tests, first 3): `['pydicom/tests/test_filewriter.py::TestCorrectAmbiguousVR::test_ambiguous_element_in_sequence_implicit_using_index']`

**Problem statement (excerpt):**
> Memory leaks when accessing sequence tags with Dataset.__getattr__. **Describe the bug**
 Accessing sequences via 'Dataset.__getattr__' seems to leak memory. The bug occurred for me when I was processing many DICOMs and manipulating some tags contained in sequences and each leaked a bit of memory, ultimately crashing the process.
 
 **Expected behavior**
 Memory should not leak. It works correctly

### Sample 7 — `pydicom__pydicom-1241`

**Files likely affected**: `pydicom/encaps.py`
**FAIL_TO_PASS** (72 tests, first 3): `['pydicom/tests/test_encaps.py::TestGetFrameOffsets::test_bad_tag', 'pydicom/tests/test_encaps.py::TestGetFrameOffsets::test_bad_length_multiple', 'pydicom/tests/test_encaps.py::TestGetFrameOffsets::test_zero_length']`

**Problem statement (excerpt):**
> Add support for Extended Offset Table to encaps module [CP1818](http://webcache.googleusercontent.com/search?q=cache:xeWXtrAs9G4J:ftp://medical.nema.org/medical/dicom/final/cp1818_ft_whenoffsettabletoosmall.pdf) added the use of an Extended Offset Table for encapsulated pixel data when the Basic Offset Table isn't suitable. 

### Sample 8 — `pydicom__pydicom-866`

**Files likely affected**: `pydicom/pixel_data_handlers/numpy_handler.py`
**FAIL_TO_PASS** (2 tests, first 3): `['pydicom/tests/test_numpy_pixel_data.py::TestNumpy_GetPixelData::test_bad_length_raises', 'pydicom/tests/test_numpy_pixel_data.py::TestNumpy_GetPixelData::test_missing_padding_warns']`

**Problem statement (excerpt):**
> Handle odd-sized dicoms with warning <!-- Instructions For Filing a Bug: https://github.com/pydicom/pydicom/blob/master/CONTRIBUTING.md#filing-bugs -->
 
 #### Description
 <!-- Example: Attribute Error thrown when printing (0x0010, 0x0020) patient Id> 0-->
 
 We have some uncompressed dicoms with an odd number of pixel bytes (saved by older versions of pydicom actually). 
 
 When we re-open with 

## Section 6 — Builder guidance

When building a fix for an instance in pydicom/pydicom:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. pydicom/dataset.py appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 61 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "pydicom/pydicom"`).

First 20 instance_ids:

- `pydicom__pydicom-1694` (dataset: `swe-bench-lite-dev`)
- `pydicom__pydicom-1413` (dataset: `swe-bench-lite-dev`)
- `pydicom__pydicom-901` (dataset: `swe-bench-lite-dev`)
- `pydicom__pydicom-1139` (dataset: `swe-bench-lite-dev`)
- `pydicom__pydicom-1256` (dataset: `swe-bench-lite-dev`)
- `pydicom__pydicom-996` (dataset: `swe-bench-full-dev`)
- `pydicom__pydicom-1241` (dataset: `swe-bench-full-dev`)
- `pydicom__pydicom-866` (dataset: `swe-bench-full-dev`)
- `pydicom__pydicom-1050` (dataset: `swe-bench-full-dev`)
- `pydicom__pydicom-944` (dataset: `swe-bench-full-dev`)
- `pydicom__pydicom-1255` (dataset: `swe-bench-full-dev`)
- `pydicom__pydicom-1017` (dataset: `swe-bench-full-dev`)
- `pydicom__pydicom-1048` (dataset: `swe-bench-full-dev`)
- `pydicom__pydicom-1608` (dataset: `swe-bench-full-dev`)
- `pydicom__pydicom-839` (dataset: `swe-bench-full-dev`)
- `pydicom__pydicom-995` (dataset: `swe-bench-full-dev`)
- `pydicom__pydicom-1416` (dataset: `swe-bench-full-dev`)
- `pydicom__pydicom-1000` (dataset: `swe-bench-full-dev`)
- `pydicom__pydicom-1069` (dataset: `swe-bench-full-dev`)
- `pydicom__pydicom-1439` (dataset: `swe-bench-full-dev`)
- ... (41 more)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
