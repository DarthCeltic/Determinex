---
name: swebench-alibaba__fastjson2
description: SWE-bench repo behavioral spec for alibaba/fastjson2. Aggregated from 6 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# alibaba/fastjson2 — SWE-bench Repo Spec

> **6 bug-fix instances** across 1 dataset(s); language(s): java.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| multi-swe-bench | 6 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `core/src/main/java/com/alibaba/fastjson2/JSON.java` | 2 |
| `core/src/main/java/com/alibaba/fastjson2/reader/ObjectReaderImplList.java` | 2 |
| `core/src/main/java/com/alibaba/fastjson2/util/TypeUtils.java` | 1 |
| `core/src/main/java/com/alibaba/fastjson2/writer/ObjectWriterBaseModule.java` | 1 |
| `core/src/main/java/com/alibaba/fastjson2/filter/ContextAutoTypeBeforeHandler.java` | 1 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: **

Sample FAIL_TO_PASS test names (first 10):
```
```

## Section 4 — Problem-theme distribution

Top themes across 6 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|

## Section 5 — Sample issues (no patches — those are the answer)

## Section 6 — Builder guidance

When building a fix for an instance in alibaba/fastjson2:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. core/src/main/java/com/alibaba/fastjson2/JSON.java appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 6 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "alibaba/fastjson2"`).

First 20 instance_ids:

- `alibaba__fastjson2-2775` (dataset: `multi-swe-bench`)
- `alibaba__fastjson2-2559` (dataset: `multi-swe-bench`)
- `alibaba__fastjson2-2285` (dataset: `multi-swe-bench`)
- `alibaba__fastjson2-2097` (dataset: `multi-swe-bench`)
- `alibaba__fastjson2-1245` (dataset: `multi-swe-bench`)
- `alibaba__fastjson2-82` (dataset: `multi-swe-bench`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
