---
name: swebench-briannesbitt__carbon
description: SWE-bench repo behavioral spec for briannesbitt/carbon. Aggregated from 10 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# briannesbitt/carbon — SWE-bench Repo Spec

> **10 bug-fix instances** across 1 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-multilingual-test | 10 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `src/Carbon/CarbonInterval.php` | 5 |
| `src/Carbon/Traits/Rounding.php` | 1 |
| `src/Carbon/Traits/Comparison.php` | 1 |
| `composer.json` | 1 |
| `src/Carbon/FactoryImmutable.php` | 1 |
| `phpdoc.php` | 1 |
| `src/Carbon/Traits/Difference.php` | 1 |
| `src/Carbon/AbstractTranslator.php` | 1 |
| `src/Carbon/CarbonInterface.php` | 1 |
| `phpstan.neon` | 1 |
| `src/Carbon/CarbonPeriod.php` | 1 |
| `src/Carbon/Traits/Creator.php` | 1 |
| `src/Carbon/Traits/Date.php` | 1 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: Round > Floor year, Is > Is, Rounding > With cascade factors, Rounding > Ceil, Factory > Psr clock**

Sample FAIL_TO_PASS test names (first 10):
```
  Round > Floor year
  Is > Is
  Rounding > With cascade factors
  Rounding > Ceil
  Factory > Psr clock
  Total > Alteration after diff
  Construct > From serialization
  Create > Create from date strings with timezones
  Total > Absolute diff
  Construct > Make
```

## Section 4 — Problem-theme distribution

Top themes across 10 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| documentation | 6 | 60.0% |
| wrong_output | 3 | 30.0% |
| crash_or_traceback | 1 | 10.0% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `briannesbitt__carbon-2665`

**Files likely affected**: `src/Carbon/Traits/Rounding.php`
**FAIL_TO_PASS** (1 tests, first 3): `['Round > Floor year']`

**Problem statement (excerpt):**
> floorYear() is not working <!--
     🛑 DON'T REMOVE ME.
     This issue template apply to all
       - bug reports,
       - feature proposals,
       - and documentation requests
 
     Having all those informations will allow us to know exactly
     what you expect and answer you faster and precisely (answer
     that matches your Carbon version, PHP version and usage).
     
     Note: Comments

### Sample 2 — `briannesbitt__carbon-2752`

**Files likely affected**: `src/Carbon/Traits/Comparison.php`
**FAIL_TO_PASS** (1 tests, first 3): `['Is > Is']`

**Problem statement (excerpt):**
> Bug in method '->is()', date with month october return true in to ask if is january <!--
     🛑 DON'T REMOVE ME.
     This issue template applies to all
       - bug reports,
       - feature proposals,
       - and documentation requests
 
     Having all those informations will allow us to know exactly
     what you expect and answer you faster and precisely (answer
     that matches your Carbon

### Sample 3 — `briannesbitt__carbon-2762`

**Files likely affected**: `src/Carbon/CarbonInterval.php`
**FAIL_TO_PASS** (2 tests, first 3): `['Rounding > With cascade factors', 'Rounding > Ceil']`

**Problem statement (excerpt):**
> Round breaks custom cascade factors <!--
     🛑 DON'T REMOVE ME.
     This issue template apply to all
       - bug reports,
       - feature proposals,
       - and documentation requests
 
     Having all those informations will allow us to know exactly
     what you expect and answer you faster and precisely (answer
     that matches your Carbon version, PHP version and usage).
     
     Note:

### Sample 4 — `briannesbitt__carbon-2813`

**Files likely affected**: `composer.json`, `src/Carbon/FactoryImmutable.php`, `phpdoc.php`
**FAIL_TO_PASS** (1 tests, first 3): `['Factory > Psr clock']`

**Problem statement (excerpt):**
> ⭐ Implement 'Psr\Clock\ClockInterface' Allow to use 'Carbon\FactoryImmutable' where 'Psr\Clock\ClockInterface' is expected. 

### Sample 5 — `briannesbitt__carbon-2981`

**Files likely affected**: `src/Carbon/CarbonInterval.php`
**FAIL_TO_PASS** (1 tests, first 3): `['Total > Alteration after diff']`

**Problem statement (excerpt):**
> Incorrect totalSeconds after adding interval to CarbonInterval in v3 <!--
     🛑 DON'T REMOVE ME.
     This issue template applies to all
       - bug reports,
       - feature proposals,
       - and documentation requests
 
     Having all those information will allow us to know exactly
     what you expect and answer you faster and precisely (answer
     that matches your Carbon version, PHP ve

### Sample 6 — `briannesbitt__carbon-3005`

**Files likely affected**: `src/Carbon/CarbonInterval.php`, `src/Carbon/Traits/Difference.php`, `src/Carbon/AbstractTranslator.php`, `src/Carbon/CarbonInterface.php`, `phpstan.neon`
**FAIL_TO_PASS** (1 tests, first 3): `['Construct > From serialization']`

**Problem statement (excerpt):**
> Serialization of 'Closure' is not allowed <!--
     🛑 DON'T REMOVE ME.
     This issue template applies to all
       - bug reports,
       - feature proposals,
       - and documentation requests
 
     Having all those information will allow us to know exactly
     what you expect and answer you faster and precisely (answer
     that matches your Carbon version, PHP version and usage).
     
   

### Sample 7 — `briannesbitt__carbon-3041`

**Files likely affected**: `src/Carbon/CarbonPeriod.php`, `src/Carbon/Traits/Creator.php`
**FAIL_TO_PASS** (1 tests, first 3): `['Create > Create from date strings with timezones']`

**Problem statement (excerpt):**
> CarbonPeriod loses timezone when accessing days <!--
     🛑 Important notice to read.
 
     Before anything else, please search in previous issues (both open and close):
     https://github.com/briannesbitt/Carbon/issues?q=is%3Aissue
 
     ⚠️ Please don't create an issue about a problem already disccussed or addressed.
 
     ⚠️ Please check if the documentation (https://carbon.nesbot.com/docs/)

### Sample 8 — `briannesbitt__carbon-3073`

**Files likely affected**: `src/Carbon/CarbonInterval.php`
**FAIL_TO_PASS** (1 tests, first 3): `['Total > Absolute diff']`

**Problem statement (excerpt):**
> CarbonInterval 'lte' gives wrong result if the interval is absolute <!--
     🛑 Important notice to read.
 
     Before anything else, please search in previous issues (both open and close):
     https://github.com/briannesbitt/Carbon/issues?q=is%3Aissue
 
     ⚠️ Please don't create an issue about a problem already discussed or addressed.
 
     ⚠️ Please check if the documentation (https://carbo

## Section 6 — Builder guidance

When building a fix for an instance in briannesbitt/carbon:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. src/Carbon/CarbonInterval.php appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 10 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "briannesbitt/carbon"`).

First 20 instance_ids:

- `briannesbitt__carbon-2665` (dataset: `swe-bench-multilingual-test`)
- `briannesbitt__carbon-2752` (dataset: `swe-bench-multilingual-test`)
- `briannesbitt__carbon-2762` (dataset: `swe-bench-multilingual-test`)
- `briannesbitt__carbon-2813` (dataset: `swe-bench-multilingual-test`)
- `briannesbitt__carbon-2981` (dataset: `swe-bench-multilingual-test`)
- `briannesbitt__carbon-3005` (dataset: `swe-bench-multilingual-test`)
- `briannesbitt__carbon-3041` (dataset: `swe-bench-multilingual-test`)
- `briannesbitt__carbon-3073` (dataset: `swe-bench-multilingual-test`)
- `briannesbitt__carbon-3098` (dataset: `swe-bench-multilingual-test`)
- `briannesbitt__carbon-3103` (dataset: `swe-bench-multilingual-test`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
