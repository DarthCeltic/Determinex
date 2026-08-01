---
name: swebench-iamkun__dayjs
description: SWE-bench repo behavioral spec for iamkun/dayjs. Aggregated from 56 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# iamkun/dayjs — SWE-bench Repo Spec

> **56 bug-fix instances** across 1 dataset(s); language(s): js.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| multi-swe-bench | 56 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `src/index.js` | 14 |
| `src/plugin/duration/index.js` | 10 |
| `src/plugin/customParseFormat/index.js` | 6 |
| `src/constant.js` | 5 |
| `src/plugin/utc/index.js` | 5 |
| `src/plugin/localeData/index.js` | 4 |
| `src/plugin/timezone/index.js` | 3 |
| `src/locale/ar-ly.js` | 2 |
| `src/locale/es.js` | 2 |
| `types/plugin/duration.d.ts` | 2 |
| `types/plugin/timezone.d.ts` | 2 |
| `.gitignore` | 2 |
| `types/plugin/utc.d.ts` | 2 |
| `src/plugin/quarterOfYear/index.js` | 2 |
| `docs/en/API-reference.md` | 2 |
| `src/plugin/objectSupport/index.js` | 1 |
| `src/locale/mr.js` | 1 |
| `src/locale/sl.js` | 1 |
| `src/locale/ar-tn.js` | 1 |
| `src/locale/ar-iq.js` | 1 |
| `src/locale/ar-dz.js` | 1 |
| `src/locale/ar-ma.js` | 1 |
| `src/locale/ar-kw.js` | 1 |
| `src/locale/ar-sa.js` | 1 |
| `src/locale/ku.js` | 1 |
| `src/locale/bg.js` | 1 |
| `src/locale/es-do.js` | 1 |
| `src/locale/es-us.js` | 1 |
| `src/locale/es-pr.js` | 1 |
| `src/plugin/weekYear/index.js` | 1 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: **

Sample FAIL_TO_PASS test names (first 10):
```
```

## Section 4 — Problem-theme distribution

Top themes across 56 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|

## Section 5 — Sample issues (no patches — those are the answer)

## Section 6 — Builder guidance

When building a fix for an instance in iamkun/dayjs:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. src/index.js appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 56 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "iamkun/dayjs"`).

First 20 instance_ids:

- `iamkun__dayjs-2532` (dataset: `multi-swe-bench`)
- `iamkun__dayjs-2420` (dataset: `multi-swe-bench`)
- `iamkun__dayjs-2399` (dataset: `multi-swe-bench`)
- `iamkun__dayjs-2377` (dataset: `multi-swe-bench`)
- `iamkun__dayjs-2369` (dataset: `multi-swe-bench`)
- `iamkun__dayjs-2367` (dataset: `multi-swe-bench`)
- `iamkun__dayjs-2231` (dataset: `multi-swe-bench`)
- `iamkun__dayjs-2175` (dataset: `multi-swe-bench`)
- `iamkun__dayjs-1964` (dataset: `multi-swe-bench`)
- `iamkun__dayjs-1954` (dataset: `multi-swe-bench`)
- `iamkun__dayjs-1953` (dataset: `multi-swe-bench`)
- `iamkun__dayjs-1725` (dataset: `multi-swe-bench`)
- `iamkun__dayjs-1611` (dataset: `multi-swe-bench`)
- `iamkun__dayjs-1567` (dataset: `multi-swe-bench`)
- `iamkun__dayjs-1502` (dataset: `multi-swe-bench`)
- `iamkun__dayjs-1470` (dataset: `multi-swe-bench`)
- `iamkun__dayjs-1414` (dataset: `multi-swe-bench`)
- `iamkun__dayjs-1321` (dataset: `multi-swe-bench`)
- `iamkun__dayjs-1319` (dataset: `multi-swe-bench`)
- `iamkun__dayjs-1307` (dataset: `multi-swe-bench`)
- ... (36 more)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
