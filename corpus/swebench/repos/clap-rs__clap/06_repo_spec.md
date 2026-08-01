---
name: swebench-clap-rs__clap
description: SWE-bench repo behavioral spec for clap-rs/clap. Aggregated from 132 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# clap-rs/clap — SWE-bench Repo Spec

> **132 bug-fix instances** across 1 dataset(s); language(s): rust.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| multi-swe-bench | 132 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `src/parse/parser.rs` | 25 |
| `src/parse/validator.rs` | 21 |
| `src/build/app/mod.rs` | 20 |
| `src/builder/command.rs` | 19 |
| `src/build/arg/mod.rs` | 19 |
| `src/output/help.rs` | 17 |
| `clap_derive/src/derives/args.rs` | 14 |
| `CHANGELOG.md` | 13 |
| `src/output/usage.rs` | 13 |
| `src/parse/errors.rs` | 13 |
| `src/builder/arg.rs` | 12 |
| `clap_derive/src/derives/subcommand.rs` | 11 |
| `src/builder/debug_asserts.rs` | 10 |
| `clap_derive/src/attrs.rs` | 9 |
| `src/parse/arg_matcher.rs` | 9 |
| `clap_builder/src/parser/parser.rs` | 8 |
| `src/parser/parser.rs` | 8 |
| `src/parser/matches/arg_matches.rs` | 6 |
| `src/parser/validator.rs` | 6 |
| `src/lib.rs` | 6 |
| `src/macros.rs` | 6 |
| `src/parse/matches/matched_arg.rs` | 6 |
| `clap_builder/src/output/help_template.rs` | 5 |
| `examples/git.md` | 5 |
| `Cargo.toml` | 5 |
| `clap_bench/benches/05_ripgrep.rs` | 5 |
| `src/util/mod.rs` | 5 |
| `clap_complete_fig/src/fig.rs` | 4 |
| `examples/git-derive.md` | 4 |
| `examples/git.rs` | 4 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: **

Sample FAIL_TO_PASS test names (first 10):
```
```

## Section 4 — Problem-theme distribution

Top themes across 132 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|

## Section 5 — Sample issues (no patches — those are the answer)

## Section 6 — Builder guidance

When building a fix for an instance in clap-rs/clap:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. src/parse/parser.rs appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 132 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "clap-rs/clap"`).

First 20 instance_ids:

- `clap-rs__clap-5873` (dataset: `multi-swe-bench`)
- `clap-rs__clap-5527` (dataset: `multi-swe-bench`)
- `clap-rs__clap-5520` (dataset: `multi-swe-bench`)
- `clap-rs__clap-5489` (dataset: `multi-swe-bench`)
- `clap-rs__clap-5298` (dataset: `multi-swe-bench`)
- `clap-rs__clap-5228` (dataset: `multi-swe-bench`)
- `clap-rs__clap-5227` (dataset: `multi-swe-bench`)
- `clap-rs__clap-5206` (dataset: `multi-swe-bench`)
- `clap-rs__clap-5084` (dataset: `multi-swe-bench`)
- `clap-rs__clap-5080` (dataset: `multi-swe-bench`)
- `clap-rs__clap-5075` (dataset: `multi-swe-bench`)
- `clap-rs__clap-5025` (dataset: `multi-swe-bench`)
- `clap-rs__clap-5015` (dataset: `multi-swe-bench`)
- `clap-rs__clap-4909` (dataset: `multi-swe-bench`)
- `clap-rs__clap-4902` (dataset: `multi-swe-bench`)
- `clap-rs__clap-4667` (dataset: `multi-swe-bench`)
- `clap-rs__clap-4635` (dataset: `multi-swe-bench`)
- `clap-rs__clap-4601` (dataset: `multi-swe-bench`)
- `clap-rs__clap-4573` (dataset: `multi-swe-bench`)
- `clap-rs__clap-4523` (dataset: `multi-swe-bench`)
- ... (112 more)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
