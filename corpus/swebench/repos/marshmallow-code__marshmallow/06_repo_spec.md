---
name: swebench-marshmallow-code__marshmallow
description: SWE-bench repo behavioral spec for marshmallow-code/marshmallow. Aggregated from 11 bug-fix instances across 2 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# marshmallow-code/marshmallow — SWE-bench Repo Spec

> **11 bug-fix instances** across 2 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-full-dev | 9 |
| swe-bench-lite-dev | 2 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `src/marshmallow/fields.py` | 7 |
| `src/marshmallow/schema.py` | 3 |
| `src/marshmallow/validate.py` | 2 |
| `src/marshmallow/utils.py` | 1 |
| `src/marshmallow/base.py` | 1 |

## Section 3 — Test framework signal

Detected: **pytest (file::TestClass::test_method or file::test_func)**

Sample FAIL_TO_PASS test names (first 10):
```
  tests/test_fields.py::TestParentAndName::test_datetime_list_inner_format
  tests/test_marshalling.py::TestUnmarshaller::test_deserialize_wrong_nested_type_with_validates_method
  tests/test_serialization.py::test_nested_field_many_serializing_generator
  tests/test_utils.py::test_from_iso_datetime[timezone1-False]
  tests/test_fields.py::TestParentAndName::test_datetime_list_inner_format
  tests/test_marshalling.py::TestUnmarshaller::test_deserialize_wrong_nested_type_with_validates_method
  tests/test_validate.py::test_url_relative_only_valid[/foo/bar]
  tests/test_validate.py::test_url_relative_only_valid[/foo?bar]
  tests/test_validate.py::test_url_relative_only_valid[?bar]
  tests/test_validate.py::test_url_relative_only_valid[/foo?bar#baz]
```

## Section 4 — Problem-theme distribution

Top themes across 11 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| crash_or_traceback | 5 | 45.5% |
| import_module | 2 | 18.2% |
| other | 2 | 18.2% |
| regression | 1 | 9.1% |
| wrong_output | 1 | 9.1% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `marshmallow-code__marshmallow-1359`

**Files likely affected**: `src/marshmallow/fields.py`
**FAIL_TO_PASS** (1 tests, first 3): `['tests/test_fields.py::TestParentAndName::test_datetime_list_inner_format']`

**Problem statement (excerpt):**
> 3.0: DateTime fields cannot be used as inner field for List or Tuple fields Between releases 3.0.0rc8 and 3.0.0rc9, 'DateTime' fields have started throwing an error when being instantiated as inner fields of container fields like 'List' or 'Tuple'. The snippet below works in <=3.0.0rc8 and throws the error below in >=3.0.0rc9 (and, worryingly, 3.0.0):
 
 '''python
 from marshmallow import fields, 

### Sample 2 — `marshmallow-code__marshmallow-1343`

**Files likely affected**: `src/marshmallow/schema.py`
**FAIL_TO_PASS** (1 tests, first 3): `['tests/test_marshalling.py::TestUnmarshaller::test_deserialize_wrong_nested_type_with_validates_method']`

**Problem statement (excerpt):**
> [version 2.20.0] TypeError: 'NoneType' object is not subscriptable After update from version 2.19.5 to 2.20.0 I got error for code like:
 
 '''python
 from marshmallow import Schema, fields, validates
 
 
 class Bar(Schema):
     value = fields.String()
 
     @validates('value')  # <- issue here
     def validate_value(self, value):
         pass
 
 
 class Foo(Schema):
     bar = fields.Nested(B

### Sample 3 — `marshmallow-code__marshmallow-1164`

**Files likely affected**: `src/marshmallow/schema.py`, `src/marshmallow/fields.py`
**FAIL_TO_PASS** (1 tests, first 3): `['tests/test_serialization.py::test_nested_field_many_serializing_generator']`

**Problem statement (excerpt):**
> 2.x: Nested(many=True) eats first element from generator value when dumping As reproduced in Python 3.6.8:
 
 '''py
 from marshmallow import Schema, fields
 
 class O(Schema):
     i = fields.Int()
 
 class P(Schema):
     os = fields.Nested(O, many=True)
 
 def gen():
     yield {'i': 1}
     yield {'i': 0}
 
 p = P()
 p.dump({'os': gen()})
 # MarshalResult(data={'os': [{'i': 0}]}, errors={})
 ''

### Sample 4 — `marshmallow-code__marshmallow-1252`

**Files likely affected**: `src/marshmallow/utils.py`
**FAIL_TO_PASS** (1 tests, first 3): `['tests/test_utils.py::test_from_iso_datetime[timezone1-False]']`

**Problem statement (excerpt):**
> ISO8601 DateTimes ending with Z considered not valid in 2.19.4 Probably related to #1247 and #1234 - in marshmallow '2.19.4', with 'python-dateutil' _not_ installed, it seems that loading a datetime in ISO8601 that ends in 'Z' (UTC time) results in an error:
 
 '''python
 class Foo(Schema):
     date = DateTime(required=True)
 
 
 foo_schema = Foo(strict=True)
 
 a_date_with_z = '2019-06-17T00:57:

### Sample 5 — `marshmallow-code__marshmallow-1359`

**Files likely affected**: `src/marshmallow/fields.py`
**FAIL_TO_PASS** (1 tests, first 3): `['tests/test_fields.py::TestParentAndName::test_datetime_list_inner_format']`

**Problem statement (excerpt):**
> 3.0: DateTime fields cannot be used as inner field for List or Tuple fields Between releases 3.0.0rc8 and 3.0.0rc9, 'DateTime' fields have started throwing an error when being instantiated as inner fields of container fields like 'List' or 'Tuple'. The snippet below works in <=3.0.0rc8 and throws the error below in >=3.0.0rc9 (and, worryingly, 3.0.0):
 
 '''python
 from marshmallow import fields, 

### Sample 6 — `marshmallow-code__marshmallow-1343`

**Files likely affected**: `src/marshmallow/schema.py`
**FAIL_TO_PASS** (1 tests, first 3): `['tests/test_marshalling.py::TestUnmarshaller::test_deserialize_wrong_nested_type_with_validates_method']`

**Problem statement (excerpt):**
> [version 2.20.0] TypeError: 'NoneType' object is not subscriptable After update from version 2.19.5 to 2.20.0 I got error for code like:
 
 '''python
 from marshmallow import Schema, fields, validates
 
 
 class Bar(Schema):
     value = fields.String()
 
     @validates('value')  # <- issue here
     def validate_value(self, value):
         pass
 
 
 class Foo(Schema):
     bar = fields.Nested(B

### Sample 7 — `marshmallow-code__marshmallow-2123`

**Files likely affected**: `src/marshmallow/fields.py`, `src/marshmallow/validate.py`
**FAIL_TO_PASS** (23 tests, first 3): `['tests/test_validate.py::test_url_relative_only_valid[/foo/bar]', 'tests/test_validate.py::test_url_relative_only_valid[/foo?bar]', 'tests/test_validate.py::test_url_relative_only_valid[?bar]']`

**Problem statement (excerpt):**
> fields.URL should allow relative-only validation Relative URLs may be used to redirect the user within the site, such as to sign in, and allowing absolute URLs without extra validation opens up a possibility of nefarious redirects.
 
 Current 'fields.URL(relative = True)' allows relative URLs _in addition_ to absolute URLs, so one must set up extra validation to catch either all absolute URLs or j

### Sample 8 — `marshmallow-code__marshmallow-1229`

**Files likely affected**: `src/marshmallow/fields.py`
**FAIL_TO_PASS** (8 tests, first 3): `['tests/test_fields.py::TestListNested::test_list_nested_only_exclude_dump_only_load_only_propagated_to_nested[only]', 'tests/test_fields.py::TestListNested::test_list_nested_only_exclude_dump_only_load_only_propagated_to_nested[exclude]', 'tests/test_fields.py::TestListNested::test_list_nested_only_and_exclude_merged_with_nested[only-expected0]']`

**Problem statement (excerpt):**
> 'only' argument inconsistent between Nested(S, many=True) and List(Nested(S)) '''python
 from pprint import pprint
 
 from marshmallow import Schema
 from marshmallow.fields import Integer, List, Nested, String
 
 
 class Child(Schema):
     name = String()
     age = Integer()
 
 
 class Family(Schema):
     children = List(Nested(Child))
 
 
 class Family2(Schema):
     children = Nested(Child, 

## Section 6 — Builder guidance

When building a fix for an instance in marshmallow-code/marshmallow:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. src/marshmallow/fields.py appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 11 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "marshmallow-code/marshmallow"`).

First 20 instance_ids:

- `marshmallow-code__marshmallow-1359` (dataset: `swe-bench-lite-dev`)
- `marshmallow-code__marshmallow-1343` (dataset: `swe-bench-lite-dev`)
- `marshmallow-code__marshmallow-1164` (dataset: `swe-bench-full-dev`)
- `marshmallow-code__marshmallow-1252` (dataset: `swe-bench-full-dev`)
- `marshmallow-code__marshmallow-1359` (dataset: `swe-bench-full-dev`)
- `marshmallow-code__marshmallow-1343` (dataset: `swe-bench-full-dev`)
- `marshmallow-code__marshmallow-2123` (dataset: `swe-bench-full-dev`)
- `marshmallow-code__marshmallow-1229` (dataset: `swe-bench-full-dev`)
- `marshmallow-code__marshmallow-1810` (dataset: `swe-bench-full-dev`)
- `marshmallow-code__marshmallow-1702` (dataset: `swe-bench-full-dev`)
- `marshmallow-code__marshmallow-1524` (dataset: `swe-bench-full-dev`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
