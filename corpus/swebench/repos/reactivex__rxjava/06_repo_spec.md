---
name: swebench-reactivex__rxjava
description: SWE-bench repo behavioral spec for reactivex/rxjava. Aggregated from 1 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# reactivex/rxjava — SWE-bench Repo Spec

> **1 bug-fix instances** across 1 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-multilingual-test | 1 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `src/main/java/io/reactivex/rxjava3/internal/operators/observable/ObservableSwitchMap.java` | 1 |

## Section 3 — Test framework signal

Detected: **Java/JUnit (TestClass.testMethod)**

Sample FAIL_TO_PASS test names (first 10):
```
  io.reactivex.rxjava3.internal.operators.observable.ObservableSwitchTest > innerOnSubscribeOuterCancelRace
```

## Section 4 — Problem-theme distribution

Top themes across 1 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| crash_or_traceback | 1 | 100.0% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `reactivex__rxjava-7597`

**Files likely affected**: `src/main/java/io/reactivex/rxjava3/internal/operators/observable/ObservableSwitchMap.java`
**FAIL_TO_PASS** (1 tests, first 3): `['io.reactivex.rxjava3.internal.operators.observable.ObservableSwitchTest > innerOnSubscribeOuterCancelRace']`

**Problem statement (excerpt):**
>  3.x: SwitchMapInnerObserver.queue.offer NullPointerException RxJava 3.1.0
 
 I'm getting this NPE:
 '''
 java.lang.NullPointerException: Attempt to invoke interface method 'boolean SimpleQueue.offer(java.lang.Object)' on a null object reference
 	at io.reactivex.rxjava3.internal.operators.observable.ObservableSwitchMap$SwitchMapInnerObserver.onNext(ObservableSwitchMap.java)
 	at io.reactivex.rxja

## Section 6 — Builder guidance

When building a fix for an instance in reactivex/rxjava:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. src/main/java/io/reactivex/rxjava3/internal/operators/observable/ObservableSwitchMap.java appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 1 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "reactivex/rxjava"`).

First 20 instance_ids:

- `reactivex__rxjava-7597` (dataset: `swe-bench-multilingual-test`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
