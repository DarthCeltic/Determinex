# CODEX-ROLLING-001 Staging Manifest

Timestamp: 2026-06-10T22:17:06-04:00

Source: rolling queue in `docs/campaign/campaign_assignments.json`.

Guardrails: this packet does not edit `eval_index.json`, campaign assignments, the ProgramBench board, or lock archives. It does not launch Hetzner work. Claude/driver remains verifier and certifier.

## Claimed Slugs

| slug | eval_index status | board-cache score | board-cache not_run | action | proposed verdict |
|---|---|---:|---:|---|---|
| jhspetersson__fselect | board_cache_only | 60/3480 | 2780 | removed collection filters from current vbidir7 submission | partial; staged for driver dispatch |
| parcel-bundler__lightningcss | board_cache_only | 510/3666 | 2768 | removed collection filters from current vbidir7 submission | partial; staged for driver dispatch |
| luajit__luajit | board_cache_only | 205/3674 | 2552 | removed collection filters from current vbidir7 submission | partial; staged for driver dispatch |
| stranger6667__jsonschema | board_cache_only | 247/3373 | 2461 | removed collection filters from current vbidir7 submission | partial; staged for driver dispatch |

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

## Hashes

### jhspetersson__fselect

- `submission.tar.gz`: `384112F208C59B9BCA26D0009349443BD43091E858F26B840ED2A77D415F2CA1`
- `submission.original.tar.gz`: `8EF545C2BF45CCDDE24154E9009A16E97F212DA08EB3EC50ADA3017DC1BA116E`
- `source/compile.sh`: `29AFE58FB9F40CCF8C5F88B2810A159E70850284E24E5320721EE37E65E42E1C`

### parcel-bundler__lightningcss

- `submission.tar.gz`: `1B36B401CC29138A76B928877E5C6D34B07999020A9FCF619183D6AD0A027476`
- `submission.original.tar.gz`: `405456BA93D22080DB5C386F6E1DF53F9736BDBD811B8B03B70A427DCB8C2FEB`
- `source/compile.sh`: `6D20D900FF023819D41D0CE40EA03B743D4B802AF24D2F9693E69A3D45B3131F`

### luajit__luajit

- `submission.tar.gz`: `7D5669773011EA29597F9874C5BEBD965D2DD9CACF23BA16A4469C88C10D104B`
- `submission.original.tar.gz`: `7E2F45A449114A1B8455AB269EE215D60CB0A982CAEF410124C5A2FDD10FA830`
- `source/compile.sh`: `76A316C3586960AB205E32A3DA8C51766BF5481F26BADE673315138DCB6263A3`

### stranger6667__jsonschema

- `submission.tar.gz`: `DCAFD5B5DDC7BD88FE54A86F67CFDEEB5372FFA1620D10EB9092DE95BBCB01AC`
- `submission.original.tar.gz`: `0E42357EB3993EB9704C77279595777967775D965F085AF5EB40FE5D157275BB`
- `source/compile.sh`: `7E3CC4F9AD1CC8F1825B64C79BAB3FABACA0EFAE80547D922298A55FFB4C52AD`

## Notes For Claude

- These are proposals only. Dispatch is driver-owned.
- `pb_senses.py` is blocked until a real `eval_report.json` exists.
- The current dirty worktree also has unrelated `scripts/determinex_programbench_agent.py`, `corpus/references/`, `scratch/`, and `scripts/determinex_copyright_guard.py` state that this packet does not touch.
