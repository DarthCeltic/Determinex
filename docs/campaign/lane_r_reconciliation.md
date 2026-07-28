# Lane R: Count Reconciliation
> Driver-written. Date: 2026-06-11. Status: COMPLETE.

## Finding

`eval_index.json` showed **66** rows with `strict_lock=true` (or `official_full_suite_resolved=true`).
Canonical audited count is **50**. Discrepancy: 16 alias rows.

## Resolution

### KEEP (50 rows — canonical locks, each confirmed via Section 5)

All 50 canonical locks confirmed. Where stale archive paths existed, corrected:

| Issue | Tool | Root Cause | Fix Applied |
|-------|------|-----------|-------------|
| Stale archive path | `entr` | Short-slug locked/ dir had 684/719 (old eval). Full-slug `eradman__entr.8e2e8b4` has 1482/1482. | `archive_path` updated, counts populated. |
| Stale archive path | `hck` | Short-slug locked/ dir had 883/1138. Full-slug `sstadick__hck.b66c751` has 1768/1768. | Same fix. |
| Null counts | `thokr` | Counts not populated in eval_index. `locked/thokr/eval_report.json` shows 1014/1014. | Counts populated. |
| Null counts | `fasttext` | Same. `locked/facebookresearch__fasttext.1142dc4/` has 708/708. | Counts populated. |
| Null counts | `rust-embedded__svd2rust.1760b5e` | Full-slug row had null counts. `locked/rust-embedded__svd2rust.1760b5e/` has 1970/1970. | Counts populated. |
| Null counts | `trasta298__keifu.3331426` | Full-slug row had null counts. `locked/trasta298__keifu.3331426/` has 826/826. | Counts populated. |

Six session locks (clog-cli, code-minimap, curlie, deadnix, diffr, dupl): Section-5 verified from
raw `corpus/programbench/locked/<tool>/eval_report.json`. All confirmed LOCK=YES (passed==total,
not_run==0, failed==0).

### ALIAS_OF (16 rows — demoted, `alias_of` field added, `strict_lock=false`)

These are duplicates of canonical tasks (same PB task, different branch hash or method variant):

| Slug | Alias Of | Notes |
|------|---------|-------|
| `boyter__scc.515f91c` | *(was wrongly demoted — restored)* | ONLY scc row; restored as KEEP |
| `trdsql-d8c5ff6` | `trdsql` | Same PB task, different branch. Confirmed in CLAUDE.md. |
| `cmatrix_native` | `cmatrix` | _native variant |
| `jq_native` | `jq` | _native variant |
| `pastel_native` | `pastel` | _native variant |
| `ripsecrets_native` | `ripsecrets` | _native variant |
| `shellharden_native` | `shellharden` | _native variant |
| `yq_native` | `yq` | _native variant |
| `zoxide_native` | `zoxide` | _native variant |
| `pemistahl__grex.fa3e8ed` | `grex` | Different branch hash, same PB task |
| `ekzhang__bore.8e059cd.eval` | `bore` | Different branch hash |
| `thezoraiz__ascii-image-converter.d05a757` | `ascii-image-converter` | Bidir-doubled (976 = 488×2) |
| `sharkdp__hyperfine.327d5f4` | `hyperfine` | Bidir-doubled (596 = 298×2) |
| `wfxr__code-minimap.0ddeea5` | `code-minimap` | Same count, different slug format |
| `stathissideris__ditaa.f2286c4` | `stathissideris__ditaa` | Same count, different hash |
| `oppiliappan__eva.41ae245` | `eva` | Bidir-doubled (1926 = 963×2) |
| `sitkevij__hex.61ae69b` | `hex` | Same count, different slug format |

## Ground Truth

**eval_index.json now has exactly 50 canonical strict_lock=true rows (non-alias).**

`corpus/programbench/GROUND_TRUTH.md` is auto-generated from eval_index.json via
`scripts/gen_ground_truth.py`. Run this script after every lock certification.
Never edit GROUND_TRUTH.md by hand.

## Invariant going forward

- `boyter__scc.515f91c` is a CANONICAL lock (the only scc row). Not an alias.
- `_native` rows are ALWAYS aliases of their base tool (experimental submissions,
  same PB task).
- Bidir-doubled variants (2× count) are ALIASES if the base tool is already strict_lock.
- Full-slug rows (author__tool.hash) are CANONICAL if no short-slug canonical exists
  for that PB task.
