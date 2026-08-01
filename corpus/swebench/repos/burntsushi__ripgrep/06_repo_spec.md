---
name: swebench-BurntSushi__ripgrep
description: SWE-bench repo behavioral spec for BurntSushi/ripgrep. Aggregated from 14 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# BurntSushi/ripgrep — SWE-bench Repo Spec

> **14 bug-fix instances** across 1 dataset(s); language(s): rust.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| multi-swe-bench | 14 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `crates/core/args.rs` | 4 |
| `complete/_rg` | 4 |
| `crates/printer/src/json.rs` | 3 |
| `crates/printer/src/util.rs` | 3 |
| `CHANGELOG.md` | 3 |
| `crates/printer/src/standard.rs` | 3 |
| `crates/core/app.rs` | 3 |
| `src/args.rs` | 3 |
| `crates/core/main.rs` | 2 |
| `.github/workflows/ci.yml` | 2 |
| `crates/cli/src/wtr.rs` | 2 |
| `Cargo.lock` | 2 |
| `crates/printer/src/summary.rs` | 2 |
| `crates/regex/src/word.rs` | 2 |
| `src/app.rs` | 2 |
| `src/printer.rs` | 2 |
| `crates/core/flags/parse.rs` | 1 |
| `crates/core/flags/doc/template.rg.1` | 1 |
| `ci/build-deb` | 1 |
| `ci/build-and-publish-m2` | 1 |
| `crates/core/flags/doc/template.long.help` | 1 |
| `RELEASE-CHECKLIST.md` | 1 |
| `crates/core/flags/complete/mod.rs` | 1 |
| `crates/core/logger.rs` | 1 |
| `crates/ignore/src/gitignore.rs` | 1 |
| `crates/core/subject.rs` | 1 |
| `.cargo/config.toml` | 1 |
| `crates/core/search.rs` | 1 |
| `crates/core/flags/doc/template.short.help` | 1 |
| `crates/core/flags/complete/bash.rs` | 1 |

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

When building a fix for an instance in BurntSushi/ripgrep:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. crates/core/args.rs appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 14 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "BurntSushi/ripgrep"`).

First 20 instance_ids:

- `BurntSushi__ripgrep-2626` (dataset: `multi-swe-bench`)
- `BurntSushi__ripgrep-2610` (dataset: `multi-swe-bench`)
- `BurntSushi__ripgrep-2576` (dataset: `multi-swe-bench`)
- `BurntSushi__ripgrep-2488` (dataset: `multi-swe-bench`)
- `BurntSushi__ripgrep-2295` (dataset: `multi-swe-bench`)
- `BurntSushi__ripgrep-2209` (dataset: `multi-swe-bench`)
- `BurntSushi__ripgrep-1980` (dataset: `multi-swe-bench`)
- `BurntSushi__ripgrep-1642` (dataset: `multi-swe-bench`)
- `BurntSushi__ripgrep-1367` (dataset: `multi-swe-bench`)
- `BurntSushi__ripgrep-1294` (dataset: `multi-swe-bench`)
- `BurntSushi__ripgrep-954` (dataset: `multi-swe-bench`)
- `BurntSushi__ripgrep-727` (dataset: `multi-swe-bench`)
- `BurntSushi__ripgrep-723` (dataset: `multi-swe-bench`)
- `BurntSushi__ripgrep-454` (dataset: `multi-swe-bench`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
