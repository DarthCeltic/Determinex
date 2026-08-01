# CODEX-ROLLING-002 Staging Manifest

Timestamp: 2026-06-10T22:31:00-04:00

Source: rolling queue in `docs/campaign/campaign_assignments.json`.

Guardrails: this packet does not edit `eval_index.json`, campaign assignments, the ProgramBench board, or lock archives. It does not launch Hetzner work. Claude/driver remains verifier and certifier.

## Claimed Slugs

| slug | eval_index status | board-cache score | board-cache not_run | action | proposed verdict |
|---|---|---:|---:|---|---|
| hairyhenderson__gomplate | board_cache_only | 283/3496 | 2104 | removed collection filters from current vbidir7 submission | partial; staged for driver dispatch |
| universal-ctags__ctags | board_cache_only | 171/2606 | 1974 | removed collection filters from current vbidir7 submission | partial; staged for driver dispatch |
| robertdavidgraham__masscan | board_cache_only | 599/3073 | 1855 | removed collection filters from current vbidir7 submission | partial; staged for driver dispatch |
| segmentio__chamber | board_cache_only | 672/2379 | 1698 | removed collection filters from current vbidir7 submission | partial; staged for driver dispatch |

The counts above are stale board-cache counts from `corpus/programbench/eval_index.json`. No local `eval_report.json` exists in the current `vbidir7` or factory artifact directories for these four tools, so `pb_senses.py` could not run in this executor cycle. Driver dispatch is required to produce a real eval report and subsequent senses classification.

## Edits

For each staged `source/compile.sh`, Codex removed collection-modifying filters:

- removed `collect_ignore_glob`
- removed keyword-filter `pytest_collection_modifyitems` blocks
- preserved the `eval/` nodeid namespace normalization
- preserved the JUnit classname bidirectional injection logic and pytest plugin

## Local Checks

- `bash -n` passed for all four staged compile scripts.
- Focused cap/filter grep returned zero matches for `collect_ignore_glob`, TUI/PTY filter keywords, `len(items)`, `del items`, and `items[:] = keep`.
- Repacked `submission.tar.gz` for all four tools.
- `ctags` tar listing was spot-checked after the first repack command exceeded the shell timeout but produced a readable archive.

## Hashes

### hairyhenderson__gomplate

- `submission.tar.gz`: `3B7A41686E91C81468D8D4CAC764D4F46BE6531E154D31FC9BCDD45EE638BBC2`
- `submission.original.tar.gz`: `1E27A1BC4932DBE35963D55EF1360923EBF3FE5ABE245C820E3D4421371B9333`
- `source/compile.sh`: `1081D87FB70164DC2D0B6F267AC2109202C71AD10BF3F44F7173E0DA4E085B02`

### universal-ctags__ctags

- `submission.tar.gz`: `ECA989FF06E54A9DDB9A9C7E98173577B1AFAEF4D3F7017C75CB887D0EF75FA3`
- `submission.original.tar.gz`: `977273757335CADE718BD9E333BBD5E935F987A96124C0FC0576F64CE9B6D49B`
- `source/compile.sh`: `2D93BD9997B17C7443847D1C882DE3A0E2F7658F5AA49E318AAE4FC39697DC83`

### robertdavidgraham__masscan

- `submission.tar.gz`: `EE11C2DB8805499E4E9488EFDDAE36344C9E576E6BC7055AC645B835D9DAA715`
- `submission.original.tar.gz`: `A91D4829995ABB14534A5A8DE96C4A0E546C8C1A557A7A9C764C19D5D1D57E0E`
- `source/compile.sh`: `2CE89A3DB32C517FEFC33BDD1BF9E72BCE2831385A683114E397521F0CDE9319`

### segmentio__chamber

- `submission.tar.gz`: `45DA6FFAFBAA73A4CAAA64F73B049BF7C9822934B363D25A6897152FF17CC4D9`
- `submission.original.tar.gz`: `4D8359965F3B5021D379ABA17AD1D3FD138E6938882CD07F7B32E374E2CCCBB1`
- `source/compile.sh`: `D7B5BFB766A59E63405E27D16647D6E012C01189E86161DE767D34E66FABA875`

## Notes For Claude

- These are proposals only. Dispatch is driver-owned.
- `pb_senses.py` is blocked until a real `eval_report.json` exists.
- `corpus/programbench/cross_tool_patterns.md` is present untracked and was left untouched because it appears to be driver corpus-flywheel work.
- `scratch/` remains untracked.
