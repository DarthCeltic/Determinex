---
name: swebench-pallets__flask
description: SWE-bench repo behavioral spec for pallets/flask. Aggregated from 15 bug-fix instances across 3 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# pallets/flask — SWE-bench Repo Spec

> **15 bug-fix instances** across 3 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-full-test | 11 |
| swe-bench-lite-test | 3 |
| swe-bench-verified-test | 1 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `src/flask/blueprints.py` | 6 |
| `src/flask/cli.py` | 5 |
| `src/flask/app.py` | 3 |
| `src/flask/config.py` | 2 |
| `src/flask/helpers.py` | 2 |
| `src/flask/wrappers.py` | 1 |
| `src/flask/json/__init__.py` | 1 |
| `src/flask/__init__.py` | 1 |
| `src/flask/debughelpers.py` | 1 |

## Section 3 — Test framework signal

Detected: **pytest (file::TestClass::test_method or file::test_func)**

Sample FAIL_TO_PASS test names (first 10):
```
  tests/test_blueprints.py::test_dotted_name_not_allowed
  tests/test_blueprints.py::test_route_decorator_custom_endpoint_with_dots
  tests/test_config.py::test_config_from_file_toml
  tests/test_cli.py::TestRoutes::test_subdomain
  tests/test_cli.py::TestRoutes::test_host
  tests/test_blueprints.py::test_empty_name_not_allowed
  tests/test_blueprints.py::test_dotted_name_not_allowed
  tests/test_blueprints.py::test_route_decorator_custom_endpoint_with_dots
  tests/test_blueprints.py::test_unique_blueprint_names
  tests/test_blueprints.py::test_self_registration
```

## Section 4 — Problem-theme distribution

Top themes across 15 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| other | 5 | 33.3% |
| type_handling | 2 | 13.3% |
| edge_case | 2 | 13.3% |
| wrong_output | 2 | 13.3% |
| encoding_unicode | 1 | 6.7% |
| crash_or_traceback | 1 | 6.7% |
| json_serialization | 1 | 6.7% |
| documentation | 1 | 6.7% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `pallets__flask-4045`

**Files likely affected**: `src/flask/blueprints.py`
**FAIL_TO_PASS** (2 tests, first 3): `['tests/test_blueprints.py::test_dotted_name_not_allowed', 'tests/test_blueprints.py::test_route_decorator_custom_endpoint_with_dots']`

**Problem statement (excerpt):**
> Raise error when blueprint name contains a dot This is required since every dot is now significant since blueprints can be nested. An error was already added for endpoint names in 1.0, but should have been added for this as well. 

### Sample 2 — `pallets__flask-4992`

**Files likely affected**: `src/flask/config.py`
**FAIL_TO_PASS** (1 tests, first 3): `['tests/test_config.py::test_config_from_file_toml']`

**Problem statement (excerpt):**
> Add a file mode parameter to flask.Config.from_file() Python 3.11 introduced native TOML support with the 'tomllib' package. This could work nicely with the 'flask.Config.from_file()' method as an easy way to load TOML config files:
 
 '''python
 app.config.from_file("config.toml", tomllib.load)
 '''
 
 However, 'tomllib.load()' takes an object readable in binary mode, while 'flask.Config.from_fil

### Sample 3 — `pallets__flask-5063`

**Files likely affected**: `src/flask/cli.py`
**FAIL_TO_PASS** (2 tests, first 3): `['tests/test_cli.py::TestRoutes::test_subdomain', 'tests/test_cli.py::TestRoutes::test_host']`

**Problem statement (excerpt):**
> Flask routes to return domain/sub-domains information Currently when checking **flask routes** it provides all routes but **it is no way to see which routes are assigned to which subdomain**.
 
 **Default server name:**
 SERVER_NAME: 'test.local'
 
 **Domains (sub-domains):**
 test.test.local
 admin.test.local
 test.local
 
 **Adding blueprints:**
 app.register_blueprint(admin_blueprint,url_prefix

### Sample 4 — `pallets__flask-5014`

**Files likely affected**: `src/flask/blueprints.py`
**FAIL_TO_PASS** (1 tests, first 3): `['tests/test_blueprints.py::test_empty_name_not_allowed']`

**Problem statement (excerpt):**
> Require a non-empty name for Blueprints Things do not work correctly if a Blueprint is given an empty name (e.g. #4944).
 It would be helpful if a 'ValueError' was raised when trying to do that. 

### Sample 5 — `pallets__flask-4045`

**Files likely affected**: `src/flask/blueprints.py`
**FAIL_TO_PASS** (2 tests, first 3): `['tests/test_blueprints.py::test_dotted_name_not_allowed', 'tests/test_blueprints.py::test_route_decorator_custom_endpoint_with_dots']`

**Problem statement (excerpt):**
> Raise error when blueprint name contains a dot This is required since every dot is now significant since blueprints can be nested. An error was already added for endpoint names in 1.0, but should have been added for this as well. 

### Sample 6 — `pallets__flask-4074`

**Files likely affected**: `src/flask/helpers.py`, `src/flask/wrappers.py`, `src/flask/blueprints.py`, `src/flask/app.py`
**FAIL_TO_PASS** (2 tests, first 3): `['tests/test_blueprints.py::test_unique_blueprint_names', 'tests/test_blueprints.py::test_self_registration']`

**Problem statement (excerpt):**
> url_for can't distinguish a blueprint mounted two times Based on blueprint concept, I expected it to handle relative 'url_for' nicely:  ''' from flask import Blueprint, Flask, url_for  bp = Blueprint('foo', __name__)  @bp.route('/') def func():     return url_for('.func')  app = Flask(__name__) app.register_blueprint(bp, url_prefix='/foo') app.register_blueprint(bp, url_prefix='/bar')  client = ap

### Sample 7 — `pallets__flask-4160`

**Files likely affected**: `src/flask/json/__init__.py`
**FAIL_TO_PASS** (1 tests, first 3): `['tests/test_json.py::test_json_decimal']`

**Problem statement (excerpt):**
> handle Decimal in json encoder The 'simplejson' removal (#3555) decreased the flask encoding capabilities as the built-in 'json' doesn't cover cases like 'Decimal' types. The solution seems to be: overwrite the flask app encoder with 'JSONEnconder' from 'simplejson', but this incorporates a problem for users that relies on both 'Decimal' and 'datetimes' as 'simplejon' doesn't handle 'datetimes', w

### Sample 8 — `pallets__flask-4169`

**Files likely affected**: `src/flask/cli.py`
**FAIL_TO_PASS** (1 tests, first 3): `['tests/test_cli.py::test_lazy_load_error']`

**Problem statement (excerpt):**
> Exceptions are sometimes replaced with "TypeError: exceptions must derive from BaseException" '''python
 # a.py
 def create_app(): raise RuntimeError()
 '''
 '''
 $ FLASK_APP=a.py flask run --lazy-loading
 $ curl http://127.0.0.1:5000
 [...]
 Traceback (most recent call last):
   File "[...]/lib/python3.9/site-packages/flask/cli.py", line 356, in __call__
     self._flush_bg_loading_exception()
  

## Section 6 — Builder guidance

When building a fix for an instance in pallets/flask:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. src/flask/blueprints.py appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 15 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "pallets/flask"`).

First 20 instance_ids:

- `pallets__flask-4045` (dataset: `swe-bench-lite-test`)
- `pallets__flask-4992` (dataset: `swe-bench-lite-test`)
- `pallets__flask-5063` (dataset: `swe-bench-lite-test`)
- `pallets__flask-5014` (dataset: `swe-bench-verified-test`)
- `pallets__flask-4045` (dataset: `swe-bench-full-test`)
- `pallets__flask-4074` (dataset: `swe-bench-full-test`)
- `pallets__flask-4160` (dataset: `swe-bench-full-test`)
- `pallets__flask-4169` (dataset: `swe-bench-full-test`)
- `pallets__flask-4544` (dataset: `swe-bench-full-test`)
- `pallets__flask-4575` (dataset: `swe-bench-full-test`)
- `pallets__flask-4642` (dataset: `swe-bench-full-test`)
- `pallets__flask-4935` (dataset: `swe-bench-full-test`)
- `pallets__flask-4992` (dataset: `swe-bench-full-test`)
- `pallets__flask-5014` (dataset: `swe-bench-full-test`)
- `pallets__flask-5063` (dataset: `swe-bench-full-test`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
