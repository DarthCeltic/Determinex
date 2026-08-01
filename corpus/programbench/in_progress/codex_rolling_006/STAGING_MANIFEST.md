# CODEX-ROLLING-006 Staging Manifest

Timestamp: 2026-06-11T10:30:29-04:00

Scope: rolling queue executor batch. Codex repaired scaffold-level collection filters inside staged tool directories only. No lock verdict is proposed.

Claimed slugs:
- `epistates__treemd`
- `alexpovel__srgn`
- `tree-sitter__tree-sitter`
- `skeema__skeema`

Failure class:
- `scaffold-broken`: all four current `vbidir7` tarballs had generated pytest collection filters (`collect_ignore_glob` plus `items[:] = keep`) causing high `not_run` board-cache rows.

Known patterns checked:
- Pattern 002: bidir XML injection is present and preserved. This batch did not delete or regenerate `results.xml.orig`; no such path was present in the staged source trees.
- Pattern 004: compile scripts are LF-only before packing.

Edits:
- Removed stale collection filters from each tool's generated `compile.sh`.
- Removed `treemd`'s extra `test_keybindings/file_picker` collection skip.
- Preserved eval nodeid normalization and the `determinex_bidir` JUnit XML injection plugin.

Board-cache collection targets:
- `epistates__treemd`: before collected `1022/2019`; after target `2019/2019`; current board score `263/2019`.
- `alexpovel__srgn`: before collected `1513/2472`; after target `2472/2472`; current board score `437/2472`.
- `tree-sitter__tree-sitter`: before collected `687/1608`; after target `1608/1608`; current board score `445/1608`.
- `skeema__skeema`: before collected `1627/2475`; after target `2475/2475`; current board score `1036/2475`.

Hashes:
- `treemd/submission.tar.gz`: `889DB7DBA8D2B63D2B2E5582080179FA8A366998003417C9D0F2952325D4AF9D`
- `treemd/submission.original.tar.gz`: `2AE07A5FB211995FE796DEF5A63FB50F0660250685BA8CED13C23664AE320730`
- `treemd/source/compile.sh`: `31F8F03E3E516D4C0E854E8D4300E1E6EEF1D52655949CDF0FCA0DA16A6D964C`
- `srgn/submission.tar.gz`: `583A27CF91AEF7046BEDC45F0F1BA1FE96F06B4DDD9497D975E0AC077BBF207A`
- `srgn/submission.original.tar.gz`: `78D04F2A5009F963C6053DAE1A73FE56E53492D603385F594570BE23672293CA`
- `srgn/source/compile.sh`: `6CCA678BE119BD5DEDC28033E72906873A39D5F8CD7E92BACF9E43FF0FF8A531`
- `tree-sitter/submission.tar.gz`: `777F86FB3FC22AEFD5870E707C702A61FE28447DFB87E0E643D6CDB6F6F2DCF9`
- `tree-sitter/submission.original.tar.gz`: `B91D32ED43806FC468E3AA8AA120D4368769E44C9840D5BF10B1DDF9C167821E`
- `tree-sitter/source/compile.sh`: `61DE6F39BB2AD312FBE156BDCE6C22F9DA886EB08FA313DE4AF24C88E98C4157`
- `skeema/submission.tar.gz`: `3B540DAE2F25614BA4E45F4EF597F58D890266B2BACFA75DB4F793B57766258B`
- `skeema/submission.original.tar.gz`: `7DF60C52AF951D9BC67E51E39EAF60645E1659551F5B56C7821B14BC419D95E3`
- `skeema/source/compile.sh`: `45F67246F82E8411677A19FDC2EE542F9F4DA526C2E3D060445860B04D4E2F8F`

Verification:
- `bash -n` passed for all four `compile.sh` files.
- Focused cap/filter grep returned no matches.
- Tar sanity check confirmed root `./compile.sh` is present and no `target/` members matched.
- Disk before local eval: `C:/` free `79.24 GB`, `T:/` free `891.68 GB`; RAM available `12.62 GB`.

Local eval attempt:
- Attempted `epistates__treemd` only:
  `uv run programbench eval C:\Dev\Determinex\corpus\programbench\in_progress\codex_rolling_006\eval_input --filter 'epistates__treemd.*' --force --workers 1 --branch-workers 1 --docker-cpus 4 --output C:\Dev\Determinex\corpus\programbench\in_progress\codex_rolling_006\eval_output`
- The first sandboxed attempt failed before start because `uv` could not access the user cache.
- The escalated attempt ran for 45 minutes, spawned container `programbench-75c68eb9ac7a`, and produced no `eval_output`.
- After timeout, ProgramBench respawned `programbench-9379216cadd4`; Codex stopped the local eval process tree and both containers to leave local state clean.
- No local eval_report exists for this batch.
