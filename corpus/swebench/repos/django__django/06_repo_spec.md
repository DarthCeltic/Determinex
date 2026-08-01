---
name: swebench-django__django
description: SWE-bench repo behavioral spec for django/django. Aggregated from 1195 bug-fix instances across 3 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# django/django — SWE-bench Repo Spec

> **1195 bug-fix instances** across 3 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-full-test | 850 |
| swe-bench-verified-test | 231 |
| swe-bench-lite-test | 114 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `django/db/models/sql/query.py` | 72 |
| `django/db/models/expressions.py` | 54 |
| `django/db/models/fields/__init__.py` | 49 |
| `django/db/models/base.py` | 47 |
| `django/db/models/query.py` | 47 |
| `django/db/models/sql/compiler.py` | 45 |
| `django/forms/models.py` | 28 |
| `django/contrib/admin/options.py` | 27 |
| `django/db/migrations/autodetector.py` | 26 |
| `django/db/models/fields/related.py` | 23 |
| `django/db/migrations/operations/models.py` | 21 |
| `django/urls/resolvers.py` | 20 |
| `django/utils/autoreload.py` | 19 |
| `django/db/backends/base/schema.py` | 18 |
| `django/db/models/query_utils.py` | 18 |
| `django/views/debug.py` | 17 |
| `django/template/defaultfilters.py` | 17 |
| `django/db/models/lookups.py` | 16 |
| `django/db/migrations/serializer.py` | 16 |
| `django/forms/formsets.py` | 16 |
| `django/http/response.py` | 15 |
| `django/db/backends/sqlite3/schema.py` | 15 |
| `django/db/models/deletion.py` | 14 |
| `django/core/validators.py` | 14 |
| `django/core/management/base.py` | 14 |
| `django/contrib/admin/checks.py` | 14 |
| `django/forms/widgets.py` | 13 |
| `django/core/management/__init__.py` | 13 |
| `django/contrib/auth/forms.py` | 13 |
| `django/db/models/fields/related_descriptors.py` | 13 |

## Section 3 — Test framework signal

Detected: **pytest (dotted module path test_module.test_func)**

Sample FAIL_TO_PASS test names (first 10):
```
  test_override_file_upload_permissions (test_utils.tests.OverrideSettingsTests)
  test_callable_path (model_fields.test_filepathfield.FilePathFieldTests)
  test_order_by_multiline_sql (expressions.tests.BasicExpressionsTests)
  test_order_of_operations (expressions.tests.BasicExpressionsTests)
  test_combine_media (forms_tests.tests.test_media.FormsMediaTestCase)
  test_construction (forms_tests.tests.test_media.FormsMediaTestCase)
  test_form_media (forms_tests.tests.test_media.FormsMediaTestCase)
  test_media_deduplication (forms_tests.tests.test_media.FormsMediaTestCase)
  test_media_inheritance (forms_tests.tests.test_media.FormsMediaTestCase)
  test_sqlmigrate_for_non_transactional_databases (migrations.test_commands.MigrateTests)
```

## Section 4 — Problem-theme distribution

Top themes across 1195 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| other | 455 | 38.1% |
| crash_or_traceback | 214 | 17.9% |
| wrong_output | 128 | 10.7% |
| documentation | 87 | 7.3% |
| config_environment | 69 | 5.8% |
| import_module | 56 | 4.7% |
| regression | 48 | 4.0% |
| edge_case | 42 | 3.5% |
| json_serialization | 21 | 1.8% |
| performance | 17 | 1.4% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `django__django-10914`

**Files likely affected**: `django/conf/global_settings.py`
**FAIL_TO_PASS** (1 tests, first 3): `['test_override_file_upload_permissions (test_utils.tests.OverrideSettingsTests)']`

**Problem statement (excerpt):**
> Set default FILE_UPLOAD_PERMISSION to 0o644. Description 	 Hello, As far as I can see, the ​File Uploads documentation page does not mention any permission issues. What I would like to see is a warning that in absence of explicitly configured FILE_UPLOAD_PERMISSIONS, the permissions for a file uploaded to FileSystemStorage might not be consistent depending on whether a MemoryUploadedFile or a Temp

### Sample 2 — `django__django-10924`

**Files likely affected**: `django/db/models/fields/__init__.py`
**FAIL_TO_PASS** (1 tests, first 3): `['test_callable_path (model_fields.test_filepathfield.FilePathFieldTests)']`

**Problem statement (excerpt):**
> Allow FilePathField path to accept a callable. Description 	 I have a special case where I want to create a model containing the path to some local files on the server/dev machine. Seeing as the place where these files are stored is different on different machines I have the following: import os from django.conf import settings from django.db import models class LocalFiles(models.Model): 	name = m

### Sample 3 — `django__django-11001`

**Files likely affected**: `django/db/models/sql/compiler.py`
**FAIL_TO_PASS** (2 tests, first 3): `['test_order_by_multiline_sql (expressions.tests.BasicExpressionsTests)', 'test_order_of_operations (expressions.tests.BasicExpressionsTests)']`

**Problem statement (excerpt):**
> Incorrect removal of order_by clause created as multiline RawSQL Description 	 Hi. The SQLCompiler is ripping off one of my "order by" clause, because he "thinks" the clause was already "seen" (in SQLCompiler.get_order_by()). I'm using expressions written as multiline RawSQLs, which are similar but not the same.  The bug is located in SQLCompiler.get_order_by(), somewhere around line computing par

### Sample 4 — `django__django-11019`

**Files likely affected**: `django/forms/widgets.py`
**FAIL_TO_PASS** (16 tests, first 3): `['test_combine_media (forms_tests.tests.test_media.FormsMediaTestCase)', 'test_construction (forms_tests.tests.test_media.FormsMediaTestCase)', 'test_form_media (forms_tests.tests.test_media.FormsMediaTestCase)']`

**Problem statement (excerpt):**
> Merging 3 or more media objects can throw unnecessary MediaOrderConflictWarnings Description 	 Consider the following form definition, where text-editor-extras.js depends on text-editor.js but all other JS files are independent: from django import forms class ColorPicker(forms.Widget): 	class Media: 		js = ['color-picker.js'] class SimpleTextWidget(forms.Widget): 	class Media: 		js = ['text-editor

### Sample 5 — `django__django-11039`

**Files likely affected**: `django/core/management/commands/sqlmigrate.py`
**FAIL_TO_PASS** (1 tests, first 3): `['test_sqlmigrate_for_non_transactional_databases (migrations.test_commands.MigrateTests)']`

**Problem statement (excerpt):**
> sqlmigrate wraps it's outpout in BEGIN/COMMIT even if the database doesn't support transactional DDL Description 	  		(last modified by Simon Charette) 	  The migration executor only adds the outer BEGIN/COMMIT ​if the migration is atomic and ​the schema editor can rollback DDL but the current sqlmigrate logic only takes migration.atomic into consideration. The issue can be addressed by Changing s

### Sample 6 — `django__django-11049`

**Files likely affected**: `django/db/models/fields/__init__.py`
**FAIL_TO_PASS** (1 tests, first 3): `['test_invalid_string (model_fields.test_durationfield.TestValidation)']`

**Problem statement (excerpt):**
> Correct expected format in invalid DurationField error message Description 	 If you enter a duration "14:00" into a duration field, it translates to "00:14:00" which is 14 minutes. The current error message for invalid DurationField says that this should be the format of durations: "[DD] [HH:[MM:]]ss[.uuuuuu]". But according to the actual behaviour, it should be: "[DD] [[HH:]MM:]ss[.uuuuuu]", beca

### Sample 7 — `django__django-11099`

**Files likely affected**: `django/contrib/auth/validators.py`
**FAIL_TO_PASS** (3 tests, first 3): `['test_ascii_validator (auth_tests.test_validators.UsernameValidatorsTests)', 'test_unicode_validator (auth_tests.test_validators.UsernameValidatorsTests)', 'test_help_text (auth_tests.test_validators.UserAttributeSimilarityValidatorTest)']`

**Problem statement (excerpt):**
> UsernameValidator allows trailing newline in usernames Description 	 ASCIIUsernameValidator and UnicodeUsernameValidator use the regex  r'^[\w.@+-]+$' The intent is to only allow alphanumeric characters as well as ., @, +, and -. However, a little known quirk of Python regexes is that $ will also match a trailing newline. Therefore, the user name validators will accept usernames which end with a n

### Sample 8 — `django__django-11133`

**Files likely affected**: `django/http/response.py`
**FAIL_TO_PASS** (1 tests, first 3): `['test_memoryview_content (httpwrappers.tests.HttpResponseTests)']`

**Problem statement (excerpt):**
> HttpResponse doesn't handle memoryview objects Description 	 I am trying to write a BinaryField retrieved from the database into a HttpResponse. When the database is Sqlite this works correctly, but Postgresql returns the contents of the field as a memoryview object and it seems like current Django doesn't like this combination: from django.http import HttpResponse																	  # String conte

## Section 6 — Builder guidance

When building a fix for an instance in django/django:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. django/db/models/sql/query.py appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 1195 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "django/django"`).

First 20 instance_ids:

- `django__django-10914` (dataset: `swe-bench-lite-test`)
- `django__django-10924` (dataset: `swe-bench-lite-test`)
- `django__django-11001` (dataset: `swe-bench-lite-test`)
- `django__django-11019` (dataset: `swe-bench-lite-test`)
- `django__django-11039` (dataset: `swe-bench-lite-test`)
- `django__django-11049` (dataset: `swe-bench-lite-test`)
- `django__django-11099` (dataset: `swe-bench-lite-test`)
- `django__django-11133` (dataset: `swe-bench-lite-test`)
- `django__django-11179` (dataset: `swe-bench-lite-test`)
- `django__django-11283` (dataset: `swe-bench-lite-test`)
- `django__django-11422` (dataset: `swe-bench-lite-test`)
- `django__django-11564` (dataset: `swe-bench-lite-test`)
- `django__django-11583` (dataset: `swe-bench-lite-test`)
- `django__django-11620` (dataset: `swe-bench-lite-test`)
- `django__django-11630` (dataset: `swe-bench-lite-test`)
- `django__django-11742` (dataset: `swe-bench-lite-test`)
- `django__django-11797` (dataset: `swe-bench-lite-test`)
- `django__django-11815` (dataset: `swe-bench-lite-test`)
- `django__django-11848` (dataset: `swe-bench-lite-test`)
- `django__django-11905` (dataset: `swe-bench-lite-test`)
- ... (1175 more)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*

---

## Section 8 — Anchor-grade hand-curated reference (top-1 by instance count, 1,195 instances)

### Repo overview
Django is the canonical Python web framework. SWE-bench's largest single-repo target. Bug fixes
span the ORM (`django/db/`), template system (`django/template/`), forms (`django/forms/`),
admin (`django/contrib/admin/`), middleware (`django/middleware/`), and migrations.

### High-leverage bug zones (mined from 1,195 patches)

| Subsystem | Touch count | Common bug pattern |
|-----------|------------|--------------------|
| `django/db/models/sql/query.py` | 72 | QuerySet compilation; JOIN ordering; subquery flattening |
| `django/db/models/expressions.py` | 54 | F() / Q() / Subquery composition; OrderBy semantics |
| `django/db/models/fields/__init__.py` | 49 | Field validation; default values; null vs blank |
| `django/db/models/aggregates.py` | ~30 | Annotate/aggregate distinct, filter args |
| `django/forms/fields.py` | ~25 | Field clean() / to_python() type coercion |
| `django/template/base.py` | ~25 | Template tag parsing; variable resolution |
| `django/contrib/admin/options.py` | ~25 | Admin queryset filtering; permissions |

### Test framework
**Django test runner** (`django/test/runner.py`) — extends pytest's discovery but uses Django's
own TestCase. Tests live under `tests/<app>/tests.py`. FAIL_TO_PASS names look like:
`tests.queries.tests.QueryTests.test_join_with_aggregate`.

### Builder rules specific to Django

1. **Migrations**: never edit migration files. Bug fixes touch model code; users regenerate migrations.
2. **`Meta` ordering**: changes to `class Meta: ordering = ...` cascade — verify with `qs.query.get_compiler(...).as_sql()`.
3. **Backwards compat**: Django has tight backwards-compat policy. Patches must not change public API signatures.
4. **`__hash__` / `__eq__`** on model classes: don't add unless explicitly needed; many subtle bugs come from this.
5. **`F()` / `Q()` / `Value()` / `Subquery()`** composition: most expression bugs live in `expressions.py`'s `_combine`, `as_sql`, `resolve_expression`.
6. **TestCase isolation**: tests use transaction rollback, NOT truncate. Don't introduce TestCase code that assumes truncation.
7. **`select_related` / `prefetch_related`**: bugs often involve nested traversal — debug with `qs.query.alias_map`.

### Where 90→100% lives (per-test-cluster)

- `test_*ordering*` → `OrderBy.copy()`, `Query.set_group_by()` — preserve copy semantics
- `test_*subquery*` → `Subquery.as_sql()` — alias generation must not collide
- `test_*aggregate*` → `Aggregate.resolve_expression()` — output_field inference
- `test_*join*` → `Query.join()` — `promote=True` for left-outer correctness
- `test_*migration*` → `MigrationLoader` — graph traversal idempotency

### Estimated lock cost per instance
~5-15 min builder time on Sonnet 4.6 + spec; ~15-45 min on local Qwen 14b.
