# CODEX-ROLLING-008 Staging Manifest

Claim time: 2026-06-11T12:04:02-04:00

Claimed slugs:
- ammarabouzor__tui-journal
- tinycc__tinycc
- arq5x__bedtools2
- ip7z__7zip

Skipped queue slug:
- ducaale__xh: `docs/campaign/parked.json` contains parked concrete instance `ducaale__xh.4a6e44f`; not reattempted without new evidence.

Protocol role: Codex executor. This package is a staging proposal only; driver verifies, dispatches, certifies, archives, and updates canonical state.

## Recon

All four claimed rows are `board_cache_only` in `corpus/programbench/eval_index.json`.

| Tool | Board-cache score | not_run | collected before | target denominator |
|---|---:|---:|---:|---:|
| ammarabouzor__tui-journal | 518/2265 | 772 | 1493 | 2265 |
| tinycc__tinycc | 1148/2341 | 742 | 1599 | 2341 |
| arq5x__bedtools2 | 7/1060 | 710 | 350 | 1060 |
| ip7z__7zip | 151/1234 | 708 | 526 | 1234 |

Failure class: scaffold-broken. Current vbidir7 tarballs had `collect_ignore_glob` and keyword filtering in `pytest_collection_modifyitems`, suppressing large parts of the test surface.

Applicable patterns:
- Pattern 004: compile.sh must remain LF-only before packing.
- Prior handback change request: tools are part of the mixed-prefix bidir class, so this batch does not attempt a per-tool shared harness fix.

No `results.xml.orig` files existed in extracted sources. The `determinex_bidir` XML injection plugin was preserved.

## Source Tarballs

Original sources:
- tui-journal: `T:\determinex-programbench\determinex_pb_tui-journal_vbidir7\ammarabouzor__tui-journal.2b4540d\submission.tar.gz`
- tinycc: `T:\determinex-programbench\determinex_pb_tinycc_vbidir7\tinycc__tinycc.9b8765d\submission.tar.gz`
- bedtools2: `T:\determinex-programbench\determinex_pb_bedtools2_vbidir7\arq5x__bedtools2.dd57059\submission.tar.gz`
- 7zip: `T:\determinex-programbench\determinex_pb_7zip_vbidir7\ip7z__7zip.839151e\submission.tar.gz`

## Edits

For each `source/compile.sh`:
- Removed `collect_ignore_glob`.
- Removed keyword-based item filtering and `items[:] = keep`.
- Preserved timeout configuration.
- Preserved `eval/` nodeid normalization.
- Preserved `determinex_bidir` plugin install and XML injection.

## Validation

- Git Bash syntax check passed for all four compile scripts: `C:\Program Files\Git\bin\bash.exe -n`.
- Focused cap/filter grep returned no matches for `collect_ignore`, `items[:] = keep`, `del items`, `test_tui`, `test_tmux`, `test_pty`, `test_interactive`, `test_pexpect`, or `test_curses`.
- LF-only compile.sh confirmed:
  - tui-journal: LF, 5286 bytes
  - tinycc: LF, 4818 bytes
  - bedtools2: LF, 4918 bytes
  - 7zip: LF, 5596 bytes
- Tar sanity: each `submission.tar.gz` contains root `./compile.sh` and no `target/` members.
- Free space before staging/dispatch decision: C:/ 78.87 GB free, T:/ 891.68 GB free.

## Hashes

| Tool | File | SHA256 |
|---|---|---|
| tui-journal | submission.tar.gz | 21AB4A6EC0012B179D0B258E6B1C818A415EE2770AF638DB0EF393BCA37A9111 |
| tui-journal | submission.original.tar.gz | 0C0C7A45A5A9170891B80902415CEFC11EFE2B3132FEC1B12A716977FDACE71A |
| tui-journal | source/compile.sh | 1C2907A947D693AD00B68CD8D8B04D193BF904D43DB1C6C6214D0E2D3B649298 |
| tinycc | submission.tar.gz | A91474AF5AEBC0CE0A551C2CE825DBDE143C188C5677396E78CCF8222DE75342 |
| tinycc | submission.original.tar.gz | 3BF7D770702F4D3955CF2694963A4531DBBDFE448D8FD008FC876AC24421CCEC |
| tinycc | source/compile.sh | D71E30220E14BEE9266C0BD6A72F1632FA6E8C099D82E41BB8E1A31B2CDD2907 |
| bedtools2 | submission.tar.gz | A3E31D7DAA679DFC25045AC4EF673E211575C4E2048CC53EEC4171A86FCCAA5A |
| bedtools2 | submission.original.tar.gz | 66DEE11D6827D1F45320941C1F326968758E8691D98B479F0127CA5AC1868EAC |
| bedtools2 | source/compile.sh | 89A4ED1953532A9E9314F53B6225F9D816542FF7ABEAA9A8F37BAD200B200EB8 |
| 7zip | submission.tar.gz | FDBC553B9795DD685090F99640EF97D32ED1571A5AC1BFEF7E3CBE42EF0D2685 |
| 7zip | submission.original.tar.gz | 8964F06CB5435256EF79D07AC7DF4CA6ED014880BABEFE6CAA79416116276A30 |
| 7zip | source/compile.sh | 5BE705F5057700F4DB719E75B805F5BDEEAFBF8E6D4D00CE7AB9C8EFCF3103DC |

## Eval Status

No local ProgramBench evals were launched for this batch. The artifacts are staged for driver/Hetzner dispatch and post-filter failure classification from completed eval reports.
