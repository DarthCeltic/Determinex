---
name: swebench-tokio-rs__tracing
description: SWE-bench repo behavioral spec for tokio-rs/tracing. Aggregated from 21 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# tokio-rs/tracing — SWE-bench Repo Spec

> **21 bug-fix instances** across 1 dataset(s); language(s): rust.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| multi-swe-bench | 21 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `tracing-attributes/src/lib.rs` | 6 |
| `tracing-attributes/src/expand.rs` | 4 |
| `tracing-subscriber/src/fmt/mod.rs` | 3 |
| `tracing-subscriber/src/reload.rs` | 3 |
| `tracing/src/dispatcher.rs` | 3 |
| `tracing/src/subscriber.rs` | 3 |
| `tracing-core/src/dispatcher.rs` | 3 |
| `tracing/src/macros.rs` | 2 |
| `tracing-subscriber/src/subscribe/mod.rs` | 2 |
| `tracing-core/src/dispatch.rs` | 2 |
| `tracing-subscriber/src/filter/env/mod.rs` | 2 |
| `tracing-opentelemetry/src/lib.rs` | 2 |
| `tracing-opentelemetry/src/span_ext.rs` | 2 |
| `tracing-subscriber/src/filter/layer_filters.rs` | 2 |
| `tracing-subscriber/src/lib.rs` | 2 |
| `tracing-subscriber/src/layer.rs` | 2 |
| `tracing-subscriber/src/registry/mod.rs` | 2 |
| `tracing-subscriber/src/registry/sharded.rs` | 2 |
| `tracing-subscriber/src/filter/mod.rs` | 2 |
| `tracing-subscriber/src/registry/extensions.rs` | 2 |
| `tracing-attributes/Cargo.toml` | 2 |
| `tracing/src/span.rs` | 2 |
| `tracing-subscriber/src/util.rs` | 2 |
| `tracing-core/src/lib.rs` | 2 |
| `tracing/benches/subscriber.rs` | 2 |
| `tracing/benches/global_subscriber.rs` | 2 |
| `tracing-core/src/callsite.rs` | 2 |
| `tracing-core/src/subscriber.rs` | 2 |
| `tracing-core/src/field.rs` | 2 |
| `tracing/src/lib.rs` | 2 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: **

Sample FAIL_TO_PASS test names (first 10):
```
```

## Section 4 — Problem-theme distribution

Top themes across 21 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|

## Section 5 — Sample issues (no patches — those are the answer)

## Section 6 — Builder guidance

When building a fix for an instance in tokio-rs/tracing:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. tracing-attributes/src/lib.rs appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 21 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "tokio-rs/tracing"`).

First 20 instance_ids:

- `tokio-rs__tracing-2897` (dataset: `multi-swe-bench`)
- `tokio-rs__tracing-2892` (dataset: `multi-swe-bench`)
- `tokio-rs__tracing-2883` (dataset: `multi-swe-bench`)
- `tokio-rs__tracing-2335` (dataset: `multi-swe-bench`)
- `tokio-rs__tracing-2090` (dataset: `multi-swe-bench`)
- `tokio-rs__tracing-2027` (dataset: `multi-swe-bench`)
- `tokio-rs__tracing-2008` (dataset: `multi-swe-bench`)
- `tokio-rs__tracing-2001` (dataset: `multi-swe-bench`)
- `tokio-rs__tracing-1983` (dataset: `multi-swe-bench`)
- `tokio-rs__tracing-1853` (dataset: `multi-swe-bench`)
- `tokio-rs__tracing-1619` (dataset: `multi-swe-bench`)
- `tokio-rs__tracing-1523` (dataset: `multi-swe-bench`)
- `tokio-rs__tracing-1297` (dataset: `multi-swe-bench`)
- `tokio-rs__tracing-1291` (dataset: `multi-swe-bench`)
- `tokio-rs__tracing-1252` (dataset: `multi-swe-bench`)
- `tokio-rs__tracing-1236` (dataset: `multi-swe-bench`)
- `tokio-rs__tracing-1233` (dataset: `multi-swe-bench`)
- `tokio-rs__tracing-1228` (dataset: `multi-swe-bench`)
- `tokio-rs__tracing-1045` (dataset: `multi-swe-bench`)
- `tokio-rs__tracing-1017` (dataset: `multi-swe-bench`)
- ... (1 more)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
