---
name: swebench-laravel__framework
description: SWE-bench repo behavioral spec for laravel/framework. Aggregated from 13 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# laravel/framework — SWE-bench Repo Spec

> **13 bug-fix instances** across 1 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-multilingual-test | 13 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `src/Illuminate/Validation/Concerns/FormatsMessages.php` | 2 |
| `src/Illuminate/Routing/UrlGenerator.php` | 1 |
| `src/Illuminate/Cache/ArrayStore.php` | 1 |
| `src/Illuminate/Database/Eloquent/Model.php` | 1 |
| `src/Illuminate/View/Compilers/BladeCompiler.php` | 1 |
| `src/Illuminate/Database/Eloquent/Relations/Concerns/SupportsInverseRelations.php` | 1 |
| `src/Illuminate/Support/Str.php` | 1 |
| `src/Illuminate/Container/Container.php` | 1 |
| `src/Illuminate/Support/Js.php` | 1 |
| `src/Illuminate/Support/functions.php` | 1 |
| `src/Illuminate/Database/Schema/Blueprint.php` | 1 |
| `src/Illuminate/Database/DatabaseManager.php` | 1 |
| `src/Illuminate/Support/Once.php` | 1 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: Routing Url Generator > When previous is equal to current, Cache Array Store > Cache ttl, Database Eloquent Model > Clone model makes a fresh copy of the model when model has uuid, Database Eloquent Model > Clone model makes a fresh copy of the model when model has ulid, Blade Verbatim > Newlines are inserted correctly after echo**

Sample FAIL_TO_PASS test names (first 10):
```
  Routing Url Generator > When previous is equal to current
  Cache Array Store > Cache ttl
  Database Eloquent Model > Clone model makes a fresh copy of the model when model has uuid
  Database Eloquent Model > Clone model makes a fresh copy of the model when model has ulid
  Blade Verbatim > Newlines are inserted correctly after echo
  Validation Validator > Translated attributes can be missing
  Validation Validator > Custom validation is appended to messages
  Database Eloquent Inverse Relation > Only hydrates inverse relation on models
  Support Str > Trim
  Support Str > Ltrim
```

## Section 4 — Problem-theme distribution

Top themes across 13 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| other | 7 | 53.8% |
| crash_or_traceback | 2 | 15.4% |
| wrong_output | 1 | 7.7% |
| regression | 1 | 7.7% |
| edge_case | 1 | 7.7% |
| documentation | 1 | 7.7% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `laravel__framework-46234`

**Files likely affected**: `src/Illuminate/Routing/UrlGenerator.php`
**FAIL_TO_PASS** (1 tests, first 3): `['Routing Url Generator > When previous is equal to current']`

**Problem statement (excerpt):**
> URL::previous() does not use fallback when the previous url matches the current <!-- DO NOT THROW THIS AWAY -->
 <!-- Fill out the FULL versions with patch versions -->
 
 - Laravel Version: 9.52.0
 - PHP Version: 8.2.2
 - Database Driver & Version: n/a
 
 ### Description:
 
 When calling 'URL::previous(route('home'))' and the referrer matches the current route I'd expect the fallback to be used.

### Sample 2 — `laravel__framework-48573`

**Files likely affected**: `src/Illuminate/Cache/ArrayStore.php`
**FAIL_TO_PASS** (1 tests, first 3): `['Cache Array Store > Cache ttl']`

**Problem statement (excerpt):**
> ArrayCache TTL is less than the specified expire ### Laravel Version  10.25.0  ### PHP Version  8.1.2  ### Database Driver & Version  _No response_  ### Description  Hello. Since yesterday, tests in my project have started to fail:
 https://github.com/bavix/laravel-wallet/actions/runs/6321648269/job/17165996865
 https://github.com/bavix/laravel-wallet/actions/runs/6321648269/job/17187888910
 
 The

### Sample 3 — `laravel__framework-48636`

**Files likely affected**: `src/Illuminate/Database/Eloquent/Model.php`
**FAIL_TO_PASS** (2 tests, first 3): `['Database Eloquent Model > Clone model makes a fresh copy of the model when model has uuid', 'Database Eloquent Model > Clone model makes a fresh copy of the model when model has ulid']`

**Problem statement (excerpt):**
> [10.x] 'Model::replicate()' doesn't take into account unique IDs ### Laravel Version
 
 10.21.0
 
 ### PHP Version
 
 8.1.21
 
 ### Database Driver & Version
 
 N/A
 
 ### Description
 
 When replicating a model, some columns are purposefully omitted from the replica so that the original record will not be overwritten in the database.
 By default replication excludes the model's primary key but no

### Sample 4 — `laravel__framework-51195`

**Files likely affected**: `src/Illuminate/View/Compilers/BladeCompiler.php`
**FAIL_TO_PASS** (1 tests, first 3): `['Blade Verbatim > Newlines are inserted correctly after echo']`

**Problem statement (excerpt):**
> Unexpected newline behavior in blade template with echo followed by verbatim ### Laravel Version  v11.4.0  ### PHP Version  8.3.6  ### Database Driver & Version  _No response_  ### Description  In a Blade template, when a echo expression is followed by a verbatim directive, zero or two newlines are echoed. It does not seem possible to echo one newline.  ### Steps To Reproduce  Input 1, with no new

### Sample 5 — `laravel__framework-51890`

**Files likely affected**: `src/Illuminate/Validation/Concerns/FormatsMessages.php`
**FAIL_TO_PASS** (1 tests, first 3): `['Validation Validator > Translated attributes can be missing']`

**Problem statement (excerpt):**
> Validator Error message not being created correctly ### Laravel Version  11.11.0  ### PHP Version  8.2  ### Database Driver & Version  n/a  ### Description  The validator is not generating error messages correctly.
 
 Might be related to this MR - https://github.com/laravel/framework/pull/51805 - will investigate further tonight if time.  ### Steps To Reproduce  In version 11.10.0: 
 '''
 > Valida

### Sample 6 — `laravel__framework-52451`

**Files likely affected**: `src/Illuminate/Validation/Concerns/FormatsMessages.php`
**FAIL_TO_PASS** (1 tests, first 3): `['Validation Validator > Custom validation is appended to messages']`

**Problem statement (excerpt):**
> Custom validation rules break generated error MessageBag when custom messages are defined ### Laravel Version
 
 11.20.0
 
 ### PHP Version
 
 8.3.6
 
 ### Database Driver & Version
 
 _No response_
 
 ### Description
 
 When using custom-defined error messages, adding custom validation rules (be it through closures or classes) to a validator ruleset will cause the '->passes()' method to generate 

### Sample 7 — `laravel__framework-52680`

**Files likely affected**: `src/Illuminate/Database/Eloquent/Relations/Concerns/SupportsInverseRelations.php`
**FAIL_TO_PASS** (1 tests, first 3): `['Database Eloquent Inverse Relation > Only hydrates inverse relation on models']`

**Problem statement (excerpt):**
> Issue with new chaperone feature when utilizing "pluck" ### Laravel Version
 
 11.22
 
 ### PHP Version
 
 8.3
 
 ### Database Driver & Version
 
 _No response_
 
 ### Description
 This relates to the new feature #51582 
 There seems to be an issue when utilizing pluck on a model relationship. An error occurs on this line in
 
 '''php
 protected function applyInverseRelationToCollection($models, ?

### Sample 8 — `laravel__framework-52684`

**Files likely affected**: `src/Illuminate/Support/Str.php`
**FAIL_TO_PASS** (3 tests, first 3): `['Support Str > Trim', 'Support Str > Ltrim', 'Support Str > Rtrim']`

**Problem statement (excerpt):**
> Str::trim changed Behavior  ### Laravel Version
 
 11.22.0
 
 ### PHP Version
 
 8.3.10
 
 ### Database Driver & Version
 
 _No response_
 
 ### Description
 
 Previously, on Laravel 10, the 'str()->trim()->toString()' worked differently.
 
 ### Steps To Reproduce
 
 '''php
 
 $value = " " . chr(0) . " ";
 
 dd(
     "version: " . app()->version(),
 
     "using str::trim: " .
         str($value)

## Section 6 — Builder guidance

When building a fix for an instance in laravel/framework:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. src/Illuminate/Validation/Concerns/FormatsMessages.php appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 13 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "laravel/framework"`).

First 20 instance_ids:

- `laravel__framework-46234` (dataset: `swe-bench-multilingual-test`)
- `laravel__framework-48573` (dataset: `swe-bench-multilingual-test`)
- `laravel__framework-48636` (dataset: `swe-bench-multilingual-test`)
- `laravel__framework-51195` (dataset: `swe-bench-multilingual-test`)
- `laravel__framework-51890` (dataset: `swe-bench-multilingual-test`)
- `laravel__framework-52451` (dataset: `swe-bench-multilingual-test`)
- `laravel__framework-52680` (dataset: `swe-bench-multilingual-test`)
- `laravel__framework-52684` (dataset: `swe-bench-multilingual-test`)
- `laravel__framework-52866` (dataset: `swe-bench-multilingual-test`)
- `laravel__framework-53206` (dataset: `swe-bench-multilingual-test`)
- `laravel__framework-53696` (dataset: `swe-bench-multilingual-test`)
- `laravel__framework-53914` (dataset: `swe-bench-multilingual-test`)
- `laravel__framework-53949` (dataset: `swe-bench-multilingual-test`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
