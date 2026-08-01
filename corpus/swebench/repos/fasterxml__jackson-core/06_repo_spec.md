---
name: swebench-fasterxml__jackson-core
description: SWE-bench repo behavioral spec for fasterxml/jackson-core. Aggregated from 18 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# fasterxml/jackson-core — SWE-bench Repo Spec

> **18 bug-fix instances** across 1 dataset(s); language(s): java.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| multi-swe-bench | 18 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `release-notes/VERSION-2.x` | 9 |
| `src/main/java/com/fasterxml/jackson/core/JsonFactory.java` | 3 |
| `src/main/java/com/fasterxml/jackson/core/json/ReaderBasedJsonParser.java` | 3 |
| `src/main/java/com/fasterxml/jackson/core/json/UTF8DataInputJsonParser.java` | 3 |
| `src/main/java/com/fasterxml/jackson/core/util/RecyclerPool.java` | 2 |
| `src/main/java/com/fasterxml/jackson/core/JsonPointer.java` | 2 |
| `src/main/java/com/fasterxml/jackson/core/Version.java` | 2 |
| `src/main/java/com/fasterxml/jackson/core/io/NumberInput.java` | 1 |
| `src/main/java/com/fasterxml/jackson/core/util/JsonParserDelegate.java` | 1 |
| `src/main/java/com/fasterxml/jackson/core/JsonParser.java` | 1 |
| `release-notes/CREDITS-2.x` | 1 |
| `src/main/java/com/fasterxml/jackson/core/json/async/NonBlockingJsonParserBase.java` | 1 |
| `src/main/java/com/fasterxml/jackson/core/json/UTF8StreamJsonParser.java` | 1 |
| `src/main/java/com/fasterxml/jackson/core/filter/FilteringGeneratorDelegate.java` | 1 |
| `src/main/java/com/fasterxml/jackson/core/filter/TokenFilter.java` | 1 |
| `src/main/java/com/fasterxml/jackson/core/filter/FilteringParserDelegate.java` | 1 |
| `src/main/java/com/fasterxml/jackson/core/filter/TokenFilterContext.java` | 1 |
| `src/main/java/com/fasterxml/jackson/core/JsonGenerator.java` | 1 |
| `src/main/java/com/fasterxml/jackson/core/util/TextBuffer.java` | 1 |
| `src/main/java/com/fasterxml/jackson/core/base/ParserBase.java` | 1 |
| `src/main/java/com/fasterxml/jackson/core/StreamReadConstraints.java` | 1 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: **

Sample FAIL_TO_PASS test names (first 10):
```
```

## Section 4 — Problem-theme distribution

Top themes across 18 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|

## Section 5 — Sample issues (no patches — those are the answer)

## Section 6 — Builder guidance

When building a fix for an instance in fasterxml/jackson-core:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. release-notes/VERSION-2.x appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 18 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "fasterxml/jackson-core"`).

First 20 instance_ids:

- `fasterxml__jackson-core-1309` (dataset: `multi-swe-bench`)
- `fasterxml__jackson-core-1263` (dataset: `multi-swe-bench`)
- `fasterxml__jackson-core-1208` (dataset: `multi-swe-bench`)
- `fasterxml__jackson-core-1204` (dataset: `multi-swe-bench`)
- `fasterxml__jackson-core-1182` (dataset: `multi-swe-bench`)
- `fasterxml__jackson-core-1172` (dataset: `multi-swe-bench`)
- `fasterxml__jackson-core-1142` (dataset: `multi-swe-bench`)
- `fasterxml__jackson-core-1053` (dataset: `multi-swe-bench`)
- `fasterxml__jackson-core-1016` (dataset: `multi-swe-bench`)
- `fasterxml__jackson-core-964` (dataset: `multi-swe-bench`)
- `fasterxml__jackson-core-922` (dataset: `multi-swe-bench`)
- `fasterxml__jackson-core-891` (dataset: `multi-swe-bench`)
- `fasterxml__jackson-core-729` (dataset: `multi-swe-bench`)
- `fasterxml__jackson-core-566` (dataset: `multi-swe-bench`)
- `fasterxml__jackson-core-370` (dataset: `multi-swe-bench`)
- `fasterxml__jackson-core-183` (dataset: `multi-swe-bench`)
- `fasterxml__jackson-core-174` (dataset: `multi-swe-bench`)
- `fasterxml__jackson-core-980` (dataset: `multi-swe-bench`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
