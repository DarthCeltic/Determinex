# CODEX-OVERRIDE-001 Staging Manifest

Timestamp: 2026-06-10T22:00:05-04:00

Reason: Ryan explicitly overrode the missing `rolling_queue` wait and asked Codex to proceed, build what was needed, and clue in Claude.

Guardrails: this packet does not edit `eval_index.json`, campaign assignments, the ProgramBench board, or lock archives. It does not launch Hetzner work. Claude/driver remains verifier and certifier.

## Claimed Slugs

| slug | prior eval status | collection count before | after target | senses summary | proposed verdict |
|---|---:|---:|---:|---|---|
| bartib | 886/929, 1 not_run, 1 skipped, 41 failed | 928/929 | 929/929 pending eval | 1 collection-gap, 41 real-fail, 1 unclassified | partial; staged for driver dispatch |
| age | 292/1678, 0 not_run, 100 skipped, 1286 failed | 1678/1678 | 1678/1678 pending eval | 1222 image-plumbing, 60 real-fail, 100 unclassified, 4 upstream-skip | partial; needs real repair, not a likely lock from filter removal alone |
| bat | 2286/2664, 0 not_run, 26 skipped, 352 failed | 2664/2664 | 2664/2664 pending eval | 138 image-plumbing, 212 real-fail, 26 unclassified, 2 upstream-skip | partial; needs real repair, not a likely lock from filter removal alone |
| ast-grep | 804/1753, 37 not_run, 0 skipped, 912 failed | 1716/1753 | 1753/1753 pending eval | 37 collection-gap, 376 image-plumbing, 536 real-fail | partial; staged for driver dispatch |

Counts above are derived from the copied `eval_report.json` files and `pb_senses.py` reports in this packet. Local `tests.json` was not present in these staged dirs.

## Edits

For each staged `source/compile.sh`, Codex removed collection-modifying filters:

- removed `collect_ignore_glob`
- removed keyword-filter `pytest_collection_modifyitems` blocks
- preserved the `eval/` nodeid namespace normalization
- preserved the JUnit classname bidirectional injection logic

## Local Checks

- `bash -n` passed for all four staged compile scripts.
- Focused cap/filter grep returned zero matches for `collect_ignore_glob`, TUI/PTY filter keywords, `len(items)`, `del items`, and `items[:] = keep`.
- `pb_senses_guard.py` returned clean for session WALs.
- Global `pb_override_scan.py` reported zero official-lock violations; it still reports the existing non-lock `dsq` eval override.

## Hashes

### bartib

- `submission.tar.gz`: `6C071327E3DEAB87A6F66D218A679EBC04F0180C925A5A74314C2DC55C07C898`
- `submission.original.tar.gz`: `46642FA74141989D99EE01FD26EF08A376F26435611EEFD71E70E164CFF7B13B`
- `eval_report.json`: `D95F9204037AE158E2AAFA3496D403950C898154A3DCD7EDB2FF52F24E7F774B`
- `senses_report.json`: `1B17AA10D949D35C678934EFA786FE1A2EDCA00B0D4B6192D01D8F806339C13F`
- `source/compile.sh`: `6E312BDFDD5E38C8B601048FDFFF056ACDA5CB91708EC953553149C856ED154A`

### age

- `submission.tar.gz`: `BD2FEC6E35A612DD4E0EAAB0DB1CDB4A385663B2A9A55983FC1BACE4CD67B4B2`
- `submission.original.tar.gz`: `15B9D76884CD063CF94FD58038370DBFC2B3E5B965C745E33E93087CAAF52C64`
- `eval_report.json`: `5B40EACB5A1DE7F1E3CE963665F311FD2D0F19C6F5E011F342884FA2BC54519F`
- `senses_report.json`: `55C684693F8E93641F9E8445C11906724B39EB27CCCFB527BE3CF073419ECC05`
- `source/compile.sh`: `CB029D17EF0672D2D1CF7C23A312EF914BEC4EDB2D9CE6E27C8CDB51EC774494`

### bat

- `submission.tar.gz`: `DBFBA6F8ABBB93EAFD55B771294864461F1217F39CFE136C6CA99F87FAC258BE`
- `submission.original.tar.gz`: `B8D994835E7C667B5D06113D47B89493903A43A23DEDD1F1346CC78ED2E2B58E`
- `eval_report.json`: `59CFBE377C5081086F1B40503515166E44209B3BE48093DEB9947964C9292B36`
- `senses_report.json`: `39B3C8D7E049EDADF5963727C987939156FA5EB2C26743DA873CE7CDE43B6D19`
- `source/compile.sh`: `64330A354EB997A7B2705BC9557B902E71A3580BE78ED941FAAA2140A5C7DC14`

### ast-grep

- `submission.tar.gz`: `E08ECDD53955D44C1E20BE3B4A655CEA15D38BA69B5367F7358B84164B6EABAC`
- `submission.original.tar.gz`: `571D290BB8D7451B6E50B5AD77671580A2C83D20A118392D0CDA6193EADF90D0`
- `eval_report.json`: `21C5AB481CC12A42F23DCEF86C3CCBBB23074F1ECA06862B38C7665568FC29DB`
- `senses_report.json`: `BE6872D23BA7A8787A49C470BCAF6ED38E738557521FE8B568314F548A150733`
- `source/compile.sh`: `95FE2148AFE4655034E9A885F7DA69ABFC328F69C330917DE00968CE3065C484`

## Notes For Claude

- `scripts/determinex_copyright_guard.py` is still untracked and was left alone because it is shared infra.
- `corpus/programbench/locked/fzf/eval_report.json` was already modified in the worktree and was not touched by this packet.
- `scratch/` remains untracked.
