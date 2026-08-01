---
name: swebench-rayon-rs__rayon
description: SWE-bench repo behavioral spec for rayon-rs/rayon. Aggregated from 2 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# rayon-rs/rayon — SWE-bench Repo Spec

> **2 bug-fix instances** across 1 dataset(s); language(s): rust.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| multi-swe-bench | 2 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `src/vec.rs` | 1 |
| `src/slice/mod.rs` | 1 |
| `src/slice/rchunks.rs` | 1 |
| `src/slice/chunks.rs` | 1 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: **

Sample FAIL_TO_PASS test names (first 10):
```
```

## Section 4 — Problem-theme distribution

Top themes across 2 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|

## Section 5 — Sample issues (no patches — those are the answer)

## Section 6 — Builder guidance

When building a fix for an instance in rayon-rs/rayon:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. src/vec.rs appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 2 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "rayon-rs/rayon"`).

First 20 instance_ids:

- `rayon-rs__rayon-986` (dataset: `multi-swe-bench`)
- `rayon-rs__rayon-863` (dataset: `multi-swe-bench`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
