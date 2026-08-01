# CODEX-ROLLING-003 Staging Manifest

Timestamp: 2026-06-10T22:36:51-04:00

Source: bounce-priority rolling queue in `docs/campaign/campaign_assignments.json`.

Guardrails: this packet does not edit `eval_index.json`, campaign assignments,
the ProgramBench board, or lock archives. It does not launch Hetzner work.
Claude/driver remains verifier and certifier.

## Claimed Slugs

| slug | bounce class | source report | current report count | action | proposed verdict |
|---|---|---|---:|---|---|
| fzf | behavioral + PTY/man-page residuals | `corpus/programbench/locked/fzf/eval_report.json` | 2072/2164, 89 failed, 3 skipped | removed stale collection filters; added locale/TERM defaults and best-effort `man-db`/`groff` install | partial; staged for driver dispatch |
| ov | collection | `corpus/programbench/locked/ov/eval_report.json` | 1243/2137, 894 not_run | removed stale collection filters; preserved bidir JUnit injection | partial; staged for driver dispatch |
| fasttext | harness-class | `corpus/programbench/locked/fasttext/eval_report.json` | 353/665, 312 not_run | removed stale collection filters only; prefix inversion filed as change request | partial; staged for driver dispatch after driver decision |
| bartib | behavioral | `corpus/programbench/in_progress/codex_override_001/bartib/eval_report.json` | 886/929, 41 failed, 1 skipped, 1 not_run | added env-driven frozen-date helper and pytest env default `BARTIB_TEST_DATE=2026-04-12` | partial; staged for driver dispatch |

Counts above are parsed from the current eval reports and are not Section 5 lock
verdicts. A new official eval is required for every proposed retry.

## Senses Reports

Fresh `pb_senses.py` reports were generated into this packet:

- `fzf/senses_report.json`: 2164 total, 2072 passed, 83 real-fail, 6 pty-gap, 3 unclassified.
- `ov/senses_report.json`: 2137 total, 1243 passed, 894 collection-gap.
- `fasttext/senses_report.json`: 665 total, 353 passed, 312 collection-gap. Driver bounce class remains harness-class due bidir prefix inversion.
- `bartib/senses_report.json`: 929 total, 886 passed, 41 real-fail, 1 collection-gap, 1 unclassified.

## Local Checks

- `bash -n` passed for all four staged compile scripts.
- `cargo build --release` passed for `bartib/source`.
- Bartib smoke with `BARTIB_TEST_DATE=2026-04-12` printed `Started activity: "Task A" (ProjectA) at 2026-04-12 10:00`.
- Focused cap/filter grep returned zero matches for `collect_ignore_glob`, TUI/PTY filter keywords, `len(items)`, `del items`, and `items[:] = keep`.
- Repacked `submission.tar.gz` for all four tools.
- Tar sanity check confirmed every archive contains `compile.sh` and has zero `target/` members.

## Hashes

### fzf

- `eval_report.json`: `969B7A8E4819472BA14A77D93E0262551178E8A7A269D608A5148C0C927E403C`
- `senses_report.json`: `3523E88487FD36A5EAD505D536A375C9409ADA4B2233228ADD31502FFA746A05`
- `submission.tar.gz`: `3A186E81729ECC19AA5D036A51AD9F11A8245E141899DFACE888089C81E24524`
- `submission.original.tar.gz`: `8CEBB2A355B9199C51F05B614BDCCAA737B4F0374A6DFE632C2B9004B9B35CB4`
- `source/compile.sh`: `7FDA9940B4165FC13B70954C0F8D18FE6A83741F249CCA9C5E8B0D3F3BE84764`

### ov

- `eval_report.json`: `58BB2CAF142775F296D4032274D9CC96C9764537C54246960329F2991A00E084`
- `senses_report.json`: `2037FA2CF31AF1865238E3DF9795E1D27FD90007086D7D0DCAF8C418EB0C25E7`
- `submission.tar.gz`: `74C66C458A81F8A876715064E2661F88DA138935FCD0A138ADEF3DF345DFD37F`
- `submission.original.tar.gz`: `3033C3E3774A002B64717D94C4D5BB9F6B689EA164738131FD6C4037B3518384`
- `source/compile.sh`: `9F13D7063A0EFBD134EBA8B0802C13B20B6865C1AA054984A54BEB0E51A017E0`

### fasttext

- `eval_report.json`: `4FEE45F887E9F552D09789E28E73F2B57876D1414A86AF5B0A54E69287443AA7`
- `senses_report.json`: `8F2EC59D96650011F664538106368B7AEF8B0BF56C906FF033059DF10F78D3A9`
- `submission.tar.gz`: `344308BC75C84A1697DFB4139491511E9BB29B5D13E828715C5471DF1E86374C`
- `submission.original.tar.gz`: `E6F21159928CC68F1196900287156F40A4A2CC01CE2913F1FCA74D1B7EB7BC8F`
- `source/compile.sh`: `CA8E7F7ED715EE699CC70CD1C261F1712489D69E9B65DC8E6C157B42482A95EC`

### bartib

- `eval_report.json`: `D95F9204037AE158E2AAFA3496D403950C898154A3DCD7EDB2FF52F24E7F774B`
- `senses_report.json`: `C44A8BAD0A9D9EFC24B5D7636B50E5CA8678329471F272D50FA4D1DB08BD6B08`
- `submission.tar.gz`: `82D9358203D3200104B92919EDFC9BEFE5BDFF69BD8889CFC18D0FF1C9B290C7`
- `submission.original.tar.gz`: `46642FA74141989D99EE01FD26EF08A376F26435611EEFD71E70E164CFF7B13B`
- `source/compile.sh`: `B4C5E867E6B3195FF6CB18E26CC5F1E47E3FAA7C010C4D8B618813A3A23D6F7C`

## Change Requests

### Harness-Class: JUnit Prefix Inversion

Fasttext bounced because `tests.json` expected `tests.*` while generated JUnit
contained `eval.tests.*`. This signature is broader than fasttext; the rolling
queue contains many mixed-prefix tools, including fzf, ov, bartib, fselect,
jsonschema, gomplate, ctags, masscan, chamber, lz4, cppcheck, chafa, fx, walk,
solar, typst, zstd, treemd, srgn, tree-sitter, skeema, dog, stgit, melody,
tui-journal, tinycc, xh, 7zip, zk, gdu, atlas, dust, hwatch, oranda, monolith,
pingu, sox, ffmpeg, miller, php-src, sqlite, duckdb, and proj. Driver should
approve or reject a shared bidir-prefix strategy before Codex applies a per-tool
prefix fix.

### Sovereignty Surfacing Standard

The new surfacing request asks Codex to wire attribution visibility into product
UI/templates and generated-output helpers. This touches shared UI, templates,
and executor output behavior, so Codex is filing a change request instead of
editing it directly under Protocol Section 6.

Proposed implementation after driver approval:

- Wire `format_reference_block(style="code_comment")` into generated-output
  paths only when provenance tags exist.
- Add a read-only Proof Operator Center "Provenance" view backed by
  `attribution.jsonl` and `logs/copyright_guard/audit.jsonl`.
- Generate README badges from `eval_index.json` and the reference registry at
  doc build time: strict count, reference-parity count, and provenance-audited
  corpus source count.
- Expand `corpus/references/` ReferenceSource entries for locked native upstream
  tools, then run `pb_provenance_calibrate.py` and report per-tier hit rates and
  stoplist candidates.

Suggested driver-gated smoke set before merge: 3-5 existing locked ProgramBench
tools plus claim scanner and provenance calibration.
