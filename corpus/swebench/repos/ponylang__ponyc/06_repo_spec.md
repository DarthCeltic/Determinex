---
name: swebench-ponylang__ponyc
description: SWE-bench repo behavioral spec for ponylang/ponyc. Aggregated from 82 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# ponylang/ponyc — SWE-bench Repo Spec

> **82 bug-fix instances** across 1 dataset(s); language(s): c.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| multi-swe-bench | 82 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `src/libponyc/expr/reference.c` | 11 |
| `src/libponyc/pass/sugar.c` | 9 |
| `src/libponyc/pass/refer.c` | 8 |
| `src/libponyc/codegen/gentype.c` | 7 |
| `src/libponyc/expr/call.c` | 7 |
| `src/libponyc/pass/syntax.c` | 7 |
| `src/libponyc/expr/match.c` | 6 |
| `src/libponyc/type/subtype.c` | 6 |
| `src/libponyc/codegen/genprim.c` | 6 |
| `src/libponyc/type/alias.c` | 6 |
| `src/libponyc/expr/operator.c` | 6 |
| `src/libponyc/pass/verify.c` | 6 |
| `src/libponyc/ast/lexer.c` | 6 |
| `src/libponyc/pass/expr.c` | 6 |
| `src/libponyc/pass/flatten.c` | 6 |
| `CHANGELOG.md` | 6 |
| `src/libponyc/codegen/gencall.c` | 6 |
| `src/libponyc/type/matchtype.c` | 5 |
| `src/libponyc/codegen/genreference.c` | 5 |
| `src/libponyc/codegen/genexe.c` | 5 |
| `src/libponyc/codegen/gendesc.c` | 5 |
| `src/libponyc/codegen/genfun.c` | 5 |
| `pony.g` | 5 |
| `src/libponyc/ast/parser.c` | 5 |
| `src/libponyc/reach/reach.c` | 5 |
| `src/libponyc/expr/lambda.c` | 5 |
| `src/libponyc/expr/postfix.c` | 5 |
| `src/libponyc/codegen/genmatch.c` | 4 |
| `src/libponyc/codegen/genident.c` | 4 |
| `src/libponyc/codegen/genserialise.c` | 4 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: **

Sample FAIL_TO_PASS test names (first 10):
```
```

## Section 4 — Problem-theme distribution

Top themes across 82 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|

## Section 5 — Sample issues (no patches — those are the answer)

## Section 6 — Builder guidance

When building a fix for an instance in ponylang/ponyc:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. src/libponyc/expr/reference.c appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 82 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "ponylang/ponyc"`).

First 20 instance_ids:

- `ponylang__ponyc-4595` (dataset: `multi-swe-bench`)
- `ponylang__ponyc-4593` (dataset: `multi-swe-bench`)
- `ponylang__ponyc-4588` (dataset: `multi-swe-bench`)
- `ponylang__ponyc-4583` (dataset: `multi-swe-bench`)
- `ponylang__ponyc-4506` (dataset: `multi-swe-bench`)
- `ponylang__ponyc-4505` (dataset: `multi-swe-bench`)
- `ponylang__ponyc-4458` (dataset: `multi-swe-bench`)
- `ponylang__ponyc-4299` (dataset: `multi-swe-bench`)
- `ponylang__ponyc-4294` (dataset: `multi-swe-bench`)
- `ponylang__ponyc-4288` (dataset: `multi-swe-bench`)
- `ponylang__ponyc-4263` (dataset: `multi-swe-bench`)
- `ponylang__ponyc-4182` (dataset: `multi-swe-bench`)
- `ponylang__ponyc-4132` (dataset: `multi-swe-bench`)
- `ponylang__ponyc-4087` (dataset: `multi-swe-bench`)
- `ponylang__ponyc-4067` (dataset: `multi-swe-bench`)
- `ponylang__ponyc-4061` (dataset: `multi-swe-bench`)
- `ponylang__ponyc-4057` (dataset: `multi-swe-bench`)
- `ponylang__ponyc-4034` (dataset: `multi-swe-bench`)
- `ponylang__ponyc-4024` (dataset: `multi-swe-bench`)
- `ponylang__ponyc-4017` (dataset: `multi-swe-bench`)
- ... (62 more)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
