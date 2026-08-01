---
name: swebench-nlohmann__json
description: SWE-bench repo behavioral spec for nlohmann/json. Aggregated from 56 bug-fix instances across 2 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# nlohmann/json — SWE-bench Repo Spec

> **56 bug-fix instances** across 2 dataset(s); language(s): cpp, python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| multi-swe-bench | 55 |
| swe-bench-multilingual-test | 1 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `single_include/nlohmann/json.hpp` | 49 |
| `include/nlohmann/json.hpp` | 25 |
| `include/nlohmann/detail/meta/type_traits.hpp` | 10 |
| `include/nlohmann/detail/input/binary_reader.hpp` | 10 |
| `include/nlohmann/detail/conversions/from_json.hpp` | 9 |
| `include/nlohmann/detail/json_pointer.hpp` | 7 |
| `include/nlohmann/detail/macro_scope.hpp` | 7 |
| `include/nlohmann/detail/output/serializer.hpp` | 7 |
| `include/nlohmann/detail/iterators/iter_impl.hpp` | 6 |
| `README.md` | 6 |
| `src/json.hpp` | 6 |
| `docs/mkdocs/mkdocs.yml` | 5 |
| `include/nlohmann/ordered_map.hpp` | 5 |
| `include/nlohmann/detail/conversions/to_json.hpp` | 4 |
| `include/nlohmann/detail/output/binary_writer.hpp` | 4 |
| `include/nlohmann/detail/iterators/iteration_proxy.hpp` | 3 |
| `include/nlohmann/json_fwd.hpp` | 3 |
| `docs/mkdocs/docs/api/json_pointer/index.md` | 3 |
| `CMakeLists.txt` | 3 |
| `docs/mkdocs/docs/api/macros/index.md` | 3 |
| `docs/mkdocs/docs/api/basic_json/index.md` | 3 |
| `include/nlohmann/detail/macro_unscope.hpp` | 3 |
| `include/nlohmann/detail/iterators/primitive_iterator.hpp` | 3 |
| `include/nlohmann/detail/input/lexer.hpp` | 3 |
| `include/nlohmann/detail/exceptions.hpp` | 3 |
| `include/nlohmann/detail/input/json_sax.hpp` | 3 |
| `Makefile` | 3 |
| `include/nlohmann/detail/input/parser.hpp` | 3 |
| `cmake/ci.cmake` | 2 |
| `include/nlohmann/detail/meta/identity_tag.hpp` | 2 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: basic usage > conversion to json via free-functions**

Sample FAIL_TO_PASS test names (first 10):
```
  basic usage > conversion to json via free-functions
```

## Section 4 — Problem-theme distribution

Top themes across 56 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| json_serialization | 1 | 100.0% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `nlohmann__json-4237`

**Files likely affected**: `single_include/nlohmann/json.hpp`, `include/nlohmann/detail/conversions/to_json.hpp`
**FAIL_TO_PASS** (1 tests, first 3): `['basic usage > conversion to json via free-functions']`

**Problem statement (excerpt):**
> 'to_json' is erroneously converting enums with underlying unsigned types to signed numbers ### Description
 
 In modern C++, enum types can have a user-specified integral underlying type. This type can be signed or unsigned. We use this in Microsoft's TTD in a number of places, where we need stronger-typed integral-like types.
 
 We've been trying this JSON serializer, and encountered this issue i

## Section 6 — Builder guidance

When building a fix for an instance in nlohmann/json:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. single_include/nlohmann/json.hpp appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 56 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "nlohmann/json"`).

First 20 instance_ids:

- `nlohmann__json-4237` (dataset: `swe-bench-multilingual-test`)
- `nlohmann__json-4537` (dataset: `multi-swe-bench`)
- `nlohmann__json-4536` (dataset: `multi-swe-bench`)
- `nlohmann__json-4525` (dataset: `multi-swe-bench`)
- `nlohmann__json-4512` (dataset: `multi-swe-bench`)
- `nlohmann__json-3664` (dataset: `multi-swe-bench`)
- `nlohmann__json-3663` (dataset: `multi-swe-bench`)
- `nlohmann__json-3605` (dataset: `multi-swe-bench`)
- `nlohmann__json-3601` (dataset: `multi-swe-bench`)
- `nlohmann__json-3590` (dataset: `multi-swe-bench`)
- `nlohmann__json-3564` (dataset: `multi-swe-bench`)
- `nlohmann__json-3543` (dataset: `multi-swe-bench`)
- `nlohmann__json-3523` (dataset: `multi-swe-bench`)
- `nlohmann__json-3514` (dataset: `multi-swe-bench`)
- `nlohmann__json-3463` (dataset: `multi-swe-bench`)
- `nlohmann__json-3446` (dataset: `multi-swe-bench`)
- `nlohmann__json-3415` (dataset: `multi-swe-bench`)
- `nlohmann__json-3332` (dataset: `multi-swe-bench`)
- `nlohmann__json-3109` (dataset: `multi-swe-bench`)
- `nlohmann__json-3073` (dataset: `multi-swe-bench`)
- ... (36 more)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
