---
name: swebench-immutable-js__immutable-js
description: SWE-bench repo behavioral spec for immutable-js/immutable-js. Aggregated from 2 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# immutable-js/immutable-js — SWE-bench Repo Spec

> **2 bug-fix instances** across 1 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-multilingual-test | 2 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `CHANGELOG.md` | 1 |
| `src/CollectionImpl.js` | 1 |
| `src/Operations.js` | 1 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: OrderedSet > hashCode should return the same value if the values are the same, OrderedMap > hashCode should return the same value if the values are the same, sliced sequence works even on filtered sequence**

Sample FAIL_TO_PASS test names (first 10):
```
  OrderedSet > hashCode should return the same value if the values are the same
  OrderedMap > hashCode should return the same value if the values are the same
  sliced sequence works even on filtered sequence
```

## Section 4 — Problem-theme distribution

Top themes across 2 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| documentation | 1 | 50.0% |
| wrong_output | 1 | 50.0% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `immutable-js__immutable-js-2005`

**Files likely affected**: `CHANGELOG.md`, `src/CollectionImpl.js`
**FAIL_TO_PASS** (2 tests, first 3): `['OrderedSet > hashCode should return the same value if the values are the same', 'OrderedMap > hashCode should return the same value if the values are the same']`

**Problem statement (excerpt):**
> OrderedSet equality and hashCode bug <!--
 
 
                                 STOP AND READ THIS BEFORE POSTING YOUR ISSUE
 
 
                                                   ---  Have a general question?  ---
 
 First check out the Docs: https://immutable-js.github.io/immutable-js/docs/
 And check out the Wiki: https://github.com/immutable-js/immutable-js/wiki/
 Search existing issues: https:

### Sample 2 — `immutable-js__immutable-js-2006`

**Files likely affected**: `src/Operations.js`
**FAIL_TO_PASS** (1 tests, first 3): `['sliced sequence works even on filtered sequence']`

**Problem statement (excerpt):**
> filter followed by slice with negative begin not working ### What happened
 
 I would expect the following code
 
 'Immutable.Range(0, 10).filter($ => true).slice(-2).toArray()'
 
 to return
 
 '[8, 9]'
 
 but instead it returns
 
 '[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]'
 
 i.e. the slice operation is ignored.
 
 If you remove the filter operation, the slice works as expected.
 
 If you slice with a posi

## Section 6 — Builder guidance

When building a fix for an instance in immutable-js/immutable-js:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. CHANGELOG.md appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 2 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "immutable-js/immutable-js"`).

First 20 instance_ids:

- `immutable-js__immutable-js-2005` (dataset: `swe-bench-multilingual-test`)
- `immutable-js__immutable-js-2006` (dataset: `swe-bench-multilingual-test`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
