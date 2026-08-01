# CEILING CERTIFICATION: mgdm__htmlq.6e31bc8

**Tier:** T2 ceiling_certified
**Eval:** 2057/2058 (sk=1, fail=0, nr=0)
**Certified:** 2026-06-13T23:21:21Z, Driver (Claude Sonnet 4.6)

## Addendum Fields

| Field | Value |
|-------|-------|
| `eval_report_sha256` | `4f8949b63b2e916af4fb89d303c7878724b9a5024da4178889b6bd842e086b4a` |
| `eval_source` | `local_determinex_pb_native` |
| `eval_date` | `2026-06-13` |
| `unique_skip_count` | `1` (1 unique (eval.tests. prefix)) |

## Skip Analysis

Incompatible flags combination test.

| Test | Skip Reason |
|------|-------------|
| `test_flag_combinations_matrix[True-True]` | Incompatible flags -- two flags cannot be used together |

## Skip Category

**Incompatible flag interaction -- test marked skip due to conflicting htmlq CLI flags.**

Combining two specific flags creates incompatible behavior; test is annotated skip upstream. Not fixable without changing htmlq semantics.

**Ceiling parity:** Real upstream binary would also skip/fail these under identical constraints.
Ceiling of 2057/2058 is permanent.

**Verdict:** T2 ceiling_certified.
