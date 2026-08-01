---
name: swebench-simdjson__simdjson
description: SWE-bench repo behavioral spec for simdjson/simdjson. Aggregated from 20 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# simdjson/simdjson — SWE-bench Repo Spec

> **20 bug-fix instances** across 1 dataset(s); language(s): cpp.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| multi-swe-bench | 20 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `include/simdjson/inline/document.h` | 6 |
| `include/simdjson/document.h` | 6 |
| `include/simdjson/generic/ondemand/document.h` | 5 |
| `include/simdjson/generic/ondemand/document-inl.h` | 5 |
| `doc/basics.md` | 5 |
| `include/simdjson/error.h` | 4 |
| `benchmark/parse_stream.cpp` | 4 |
| `benchmark/benchmarker.h` | 4 |
| `benchmark/distinctuseridcompetition.cpp` | 4 |
| `include/simdjson/generic/ondemand/value-inl.h` | 3 |
| `include/simdjson/generic/ondemand/object.h` | 3 |
| `include/simdjson/generic/ondemand/value.h` | 3 |
| `include/simdjson/dom/element.h` | 3 |
| `singleheader/simdjson.h` | 3 |
| `include/simdjson/inline/document_stream.h` | 3 |
| `tools/jsonpointer.cpp` | 3 |
| `include/simdjson/inline/document_iterator.h` | 3 |
| `tools/json2json.cpp` | 3 |
| `benchmark/bench_dom_api.cpp` | 3 |
| `tools/jsonstats.cpp` | 3 |
| `benchmark/statisticalmodel.cpp` | 3 |
| `benchmark/parseandstatcompetition.cpp` | 3 |
| `amalgamation.sh` | 3 |
| `include/CMakeLists.txt` | 3 |
| `src/CMakeLists.txt` | 3 |
| `Makefile` | 3 |
| `include/simdjson/generic/ondemand/json_iterator-inl.h` | 2 |
| `include/simdjson/generic/ondemand/json_iterator.h` | 2 |
| `include/simdjson/generic/numberparsing.h` | 2 |
| `include/simdjson/generic/ondemand/array-inl.h` | 2 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: **

Sample FAIL_TO_PASS test names (first 10):
```
```

## Section 4 — Problem-theme distribution

Top themes across 20 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|

## Section 5 — Sample issues (no patches — those are the answer)

## Section 6 — Builder guidance

When building a fix for an instance in simdjson/simdjson:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. include/simdjson/inline/document.h appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 20 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "simdjson/simdjson"`).

First 20 instance_ids:

- `simdjson__simdjson-2178` (dataset: `multi-swe-bench`)
- `simdjson__simdjson-2150` (dataset: `multi-swe-bench`)
- `simdjson__simdjson-2026` (dataset: `multi-swe-bench`)
- `simdjson__simdjson-2016` (dataset: `multi-swe-bench`)
- `simdjson__simdjson-1899` (dataset: `multi-swe-bench`)
- `simdjson__simdjson-1896` (dataset: `multi-swe-bench`)
- `simdjson__simdjson-1712` (dataset: `multi-swe-bench`)
- `simdjson__simdjson-1695` (dataset: `multi-swe-bench`)
- `simdjson__simdjson-1667` (dataset: `multi-swe-bench`)
- `simdjson__simdjson-1624` (dataset: `multi-swe-bench`)
- `simdjson__simdjson-1615` (dataset: `multi-swe-bench`)
- `simdjson__simdjson-958` (dataset: `multi-swe-bench`)
- `simdjson__simdjson-954` (dataset: `multi-swe-bench`)
- `simdjson__simdjson-949` (dataset: `multi-swe-bench`)
- `simdjson__simdjson-644` (dataset: `multi-swe-bench`)
- `simdjson__simdjson-559` (dataset: `multi-swe-bench`)
- `simdjson__simdjson-545` (dataset: `multi-swe-bench`)
- `simdjson__simdjson-543` (dataset: `multi-swe-bench`)
- `simdjson__simdjson-524` (dataset: `multi-swe-bench`)
- `simdjson__simdjson-485` (dataset: `multi-swe-bench`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
