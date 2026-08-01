# Pattern 002 Collection Wall Evidence - 2026-06-11

Purpose: first-cycle root-cause record for the four named collection-wall probes. This is an evidence artifact, not an eval_index update.

## Inputs

| Tool | Raw report | Best raw counts |
|---|---|---|
| `skeema__skeema.6a76243` | `T:\determinex-programbench\hetzner_results\hetzner_full_200_20260606\results\skeema__skeema.6a76243.eval.json` | `1654 passed / 2632 total`, `43 failed`, `130 skipped`, `805 not_run` |
| `tree-sitter__tree-sitter.5e23cca` | `T:\determinex-staging\hetzner_returns\hetzner_full_200_20260606\results\tree-sitter__tree-sitter.5e23cca.eval.json` | `445 passed / 1608 total`, `241 failed/error`, `1 skipped`, `921 not_run` |
| `samtools__samtools.aa823b5` | `T:\determinex-programbench\determinex_pb_factory_samtools__samtools.aa823b5_v1\samtools__samtools.aa823b5\samtools__samtools.aa823b5.eval.json` | `145 passed / 1511 total`, `555 failed`, `0 skipped`, `811 not_run` |
| `ogham__dog.721440b` | `T:\determinex-programbench\determinex_pb_factory_ogham__dog.721440b_v1\ogham__dog.721440b\ogham__dog.721440b.eval.json` | `290 passed / 1813 total`, `702 failed`, `3 skipped`, `818 not_run` |

## Branch Evidence

| Tool | Dominant branch examples | Prefix shape |
|---|---|---|
| `skeema` | `a903bacb7595`: `250 passed`, `20 failed`, `130 skipped`, `347 not_run`; `41d65330ce2f`: `400 passed`, `296 not_run`; `34521d0dbd17`: `392 passed`, `8 failed`, `137 not_run` | `780 tests.* not_run`, `25 eval.tests.* not_run` |
| `tree-sitter` | `40cb72101fde`: `9 collection/module errors`, `879 not_run`; `c433554013b2`: `1 module error`, `20 not_run`; `646e0e3dbe15`: `17 failed`, `13 not_run` | `879 tests.* not_run`, `42 eval.tests.* not_run` |
| `samtools` | `a71ea420de7f`: `26 passed`, `324 failed`, `710 not_run`; `60fc4d786b87`: `119 passed`, `231 failed`, `101 not_run` | `811 tests.* not_run` |
| `dog` | `db7d53e19106`: `6 passed`, `341 failed`, `3 skipped`, `559 not_run`; `78e6b2a03639`: `237 passed`, `113 failed`, `259 not_run` | `559 tests.* not_run`, `259 eval.tests.* not_run` |

## Verdict

Pattern 002 generalizes partially: all four probes show large branch-level JUnit/result attrition, but not the same single root cause.

- `tree-sitter` has direct module collection errors on entire modules before individual test emission.
- `skeema`, `samtools`, and `dog` combine real behavioral failures with large not_run gaps.
- Prefix shape is mixed across tools: some gaps are mostly `tests.*`, some include both `tests.*` and `eval.tests.*`.
- This is not yet safe to solve by one blind conftest or filter edit. The fix home is still plugin/scaffold-level collection/JUnit emission, but it needs a branch-aware before/after probe.

## Before/After Status

No after-fix eval has been run in this cycle. Before counts are listed above. Required next probe:

1. Build a branch-level collector that records expected IDs from PB `tests.json`, collected pytest nodeids before Determinex injection, and emitted JUnit testcase IDs after injection.
2. Run it on at least two tools before changing behavior.
3. Only then apply a scaffold-level fix and rerun the same collector for after counts.

## Dispatch Recommendation

- Do not fan out Pattern 002 yet.
- Start with `tree-sitter` plus one non-import-error tool (`skeema` or `dog`) to separate module import/collection failure from JUnit namespace/duplication failure.
- Keep `samtools` in Lane P but expect substantial behavioral work after collection recovery because failures are already numerous.
