---
name: swebench-catchorg__Catch2
description: SWE-bench repo behavioral spec for catchorg/Catch2. Aggregated from 12 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# catchorg/Catch2 — SWE-bench Repo Spec

> **12 bug-fix instances** across 1 dataset(s); language(s): cpp.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| multi-swe-bench | 12 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `projects/SelfTest/Baselines/compact.sw.approved.txt` | 6 |
| `projects/SelfTest/Baselines/console.std.approved.txt` | 6 |
| `projects/SelfTest/Baselines/xml.sw.approved.txt` | 6 |
| `projects/SelfTest/Baselines/console.sw.approved.txt` | 6 |
| `projects/SelfTest/Baselines/junit.sw.approved.txt` | 6 |
| `src/catch2/internal/catch_run_context.cpp` | 2 |
| `include/catch.hpp` | 2 |
| `include/internal/catch_meta.hpp` | 2 |
| `include/internal/catch_commandline.cpp` | 2 |
| `include/internal/catch_compiler_capabilities.h` | 2 |
| `include/internal/catch_message.cpp` | 2 |
| `src/catch2/internal/catch_textflow.hpp` | 1 |
| `src/catch2/internal/catch_textflow.cpp` | 1 |
| `src/catch2/catch_all.hpp` | 1 |
| `src/CMakeLists.txt` | 1 |
| `include/internal/catch_approx.h` | 1 |
| `docs/deprecations.md` | 1 |
| `docs/other-macros.md` | 1 |
| `src/catch2/internal/catch_decomposer.hpp` | 1 |
| `include/internal/benchmark/catch_clock.hpp` | 1 |
| `include/internal/benchmark/detail/catch_measure.hpp` | 1 |
| `docs/configuration.md` | 1 |
| `include/internal/benchmark/catch_chronometer.hpp` | 1 |
| `include/internal/benchmark/detail/catch_repeat.hpp` | 1 |
| `include/internal/catch_stream.cpp` | 1 |
| `include/internal/catch_run_context.cpp` | 1 |
| `include/reporters/catch_reporter_xml.cpp` | 1 |
| `include/internal/catch_interfaces_reporter.h` | 1 |
| `include/reporters/catch_reporter_listening.cpp` | 1 |
| `include/internal/benchmark/catch_environment.hpp` | 1 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: **

Sample FAIL_TO_PASS test names (first 10):
```
```

## Section 4 — Problem-theme distribution

Top themes across 12 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|

## Section 5 — Sample issues (no patches — those are the answer)

## Section 6 — Builder guidance

When building a fix for an instance in catchorg/Catch2:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. projects/SelfTest/Baselines/compact.sw.approved.txt appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 12 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "catchorg/Catch2"`).

First 20 instance_ids:

- `catchorg__Catch2-2849` (dataset: `multi-swe-bench`)
- `catchorg__Catch2-2723` (dataset: `multi-swe-bench`)
- `catchorg__Catch2-2394` (dataset: `multi-swe-bench`)
- `catchorg__Catch2-2288` (dataset: `multi-swe-bench`)
- `catchorg__Catch2-2187` (dataset: `multi-swe-bench`)
- `catchorg__Catch2-2128` (dataset: `multi-swe-bench`)
- `catchorg__Catch2-1616` (dataset: `multi-swe-bench`)
- `catchorg__Catch2-1614` (dataset: `multi-swe-bench`)
- `catchorg__Catch2-1609` (dataset: `multi-swe-bench`)
- `catchorg__Catch2-1608` (dataset: `multi-swe-bench`)
- `catchorg__Catch2-1448` (dataset: `multi-swe-bench`)
- `catchorg__Catch2-1422` (dataset: `multi-swe-bench`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
