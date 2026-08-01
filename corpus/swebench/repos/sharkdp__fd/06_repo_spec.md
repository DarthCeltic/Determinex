---
name: swebench-sharkdp__fd
description: SWE-bench repo behavioral spec for sharkdp/fd. Aggregated from 14 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# sharkdp/fd — SWE-bench Repo Spec

> **14 bug-fix instances** across 1 dataset(s); language(s): rust.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| multi-swe-bench | 14 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `src/main.rs` | 11 |
| `CHANGELOG.md` | 9 |
| `src/app.rs` | 8 |
| `src/walk.rs` | 8 |
| `doc/fd.1` | 6 |
| `src/options.rs` | 4 |
| `src/cli.rs` | 2 |
| `src/output.rs` | 2 |
| `src/exec/job.rs` | 2 |
| `contrib/completion/_fd` | 2 |
| `src/internal/opts.rs` | 2 |
| `src/dir_entry.rs` | 1 |
| `src/config.rs` | 1 |
| `src/exit_codes.rs` | 1 |
| `src/exec/input.rs` | 1 |
| `src/filesystem.rs` | 1 |
| `src/exec/mod.rs` | 1 |
| `src/fshelper/mod.rs` | 1 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: **

Sample FAIL_TO_PASS test names (first 10):
```
```

## Section 4 — Problem-theme distribution

Top themes across 14 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|

## Section 5 — Sample issues (no patches — those are the answer)

## Section 6 — Builder guidance

When building a fix for an instance in sharkdp/fd:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. src/main.rs appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 14 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "sharkdp/fd"`).

First 20 instance_ids:

- `sharkdp__fd-1394` (dataset: `multi-swe-bench`)
- `sharkdp__fd-1162` (dataset: `multi-swe-bench`)
- `sharkdp__fd-1121` (dataset: `multi-swe-bench`)
- `sharkdp__fd-1079` (dataset: `multi-swe-bench`)
- `sharkdp__fd-986` (dataset: `multi-swe-bench`)
- `sharkdp__fd-866` (dataset: `multi-swe-bench`)
- `sharkdp__fd-813` (dataset: `multi-swe-bench`)
- `sharkdp__fd-658` (dataset: `multi-swe-bench`)
- `sharkdp__fd-590` (dataset: `multi-swe-bench`)
- `sharkdp__fd-569` (dataset: `multi-swe-bench`)
- `sharkdp__fd-558` (dataset: `multi-swe-bench`)
- `sharkdp__fd-555` (dataset: `multi-swe-bench`)
- `sharkdp__fd-546` (dataset: `multi-swe-bench`)
- `sharkdp__fd-497` (dataset: `multi-swe-bench`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
