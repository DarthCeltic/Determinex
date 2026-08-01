# CODEX-ROLLING-004 Staging Manifest

Timestamp: 2026-06-10T23:03:20-04:00

Source: rolling queue in `docs/campaign/campaign_assignments.json`.

Guardrails: this packet does not edit `eval_index.json`, campaign assignments,
the ProgramBench board, or lock archives. It does not launch Hetzner work.
Claude/driver remains verifier and certifier.

## Claimed Slugs

| slug | eval_index status | board-cache score | board-cache not_run | board-cache collected | action | proposed verdict |
|---|---|---:|---:|---:|---|---|
| lz4__lz4 | board_cache_only | 109/1869 | 1599 | 270/1869 | removed collection filters from current vbidir7 submission | partial; staged for driver dispatch |
| danmar__cppcheck | board_cache_only | 285/2544 | 1527 | 1017/2544 | removed collection filters from current vbidir7 submission | partial; staged for driver dispatch |
| hpjansson__chafa | board_cache_only | 601/2808 | 1503 | 1305/2808 | removed collection filters from current vbidir7 submission | partial; staged for driver dispatch |
| antonmedv__fx | board_cache_only | 601/3002 | 1444 | 1558/3002 | removed collection filters from current vbidir7 submission | partial; staged for driver dispatch |

The counts above are stale board-cache counts from
`corpus/programbench/eval_index.json`. No local `eval_report.json` exists in the
current `vbidir7` or factory artifact directories for these four tools, so
`pb_senses.py` could not run in this executor cycle. Driver dispatch is required
to produce a real eval report and subsequent senses classification.

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
- Tar sanity check confirmed every archive contains `compile.sh` and has zero `target/` members.

## Hashes

### lz4__lz4

- `submission.tar.gz`: `0E5EA87A7004F23B8B0C03BBDCDC495A57E7BEF4A953814F19DD7AFB9F79DFCA`
- `submission.original.tar.gz`: `3F1A0A184E4E02889CAE8EAB7DEC500FB4BC6CAF289D7EBE7A962182C1EAEDDA`
- `source/compile.sh`: `109E033D8F84339DB20B84B2826B7E47791811CDC2EE1DF5DA23D3A3F6325889`

### danmar__cppcheck

- `submission.tar.gz`: `1CCAD2097E9BDC10606BA61318111D9A4B6AE5899C215B8E273D57B04BFB9C0A`
- `submission.original.tar.gz`: `9A807ADC3E0F8BC078CFE3643498A2ED6878451E5F36B13DBF178D79D6823E96`
- `source/compile.sh`: `D7E88743997E36E15628153A99136D28E6E6E0D40E55B512A09CB9C0B190F3CF`

### hpjansson__chafa

- `submission.tar.gz`: `B73172EE409FB6CEDE70AC740812EBD3A8E1EBEAB8F931724AE68DB1131CAEAD`
- `submission.original.tar.gz`: `CF295806E4ED1E695124EB70FC8C86B782088D9B83A730C34FD269C9DB418722`
- `source/compile.sh`: `E887F85BD3B7E2309ADF25F42F2DB1E2F86AC26A61EBC6DF7D6B988CFE193375`

### antonmedv__fx

- `submission.tar.gz`: `A99E2E0D943618B9A950731840D708473B8977C0EB91364ABDE7CA8846A9C5FC`
- `submission.original.tar.gz`: `6E1E037C06FE6B5819F8038BF4C65EB79C6778BBF0134C5EC59194EB60F3936C`
- `source/compile.sh`: `833DD2D42A2CFA0E9D89330266DFC450C1BF1FE35C59131E014B71A6A3EC01B5`

## Notes For Claude

- These are proposals only. Dispatch is driver-owned.
- `pb_senses.py` is blocked until real `eval_report.json` files exist.
- `corpus/programbench/cross_tool_patterns.md` remains modified by driver/shared work and was left untouched.
- `scratch/` remains untracked.
