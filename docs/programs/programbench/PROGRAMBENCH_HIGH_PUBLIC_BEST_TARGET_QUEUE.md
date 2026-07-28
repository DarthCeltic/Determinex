# ProgramBench High-Public-Best Target Queue

Date: 2026-05-20

Purpose: turn the public "almost solved" leaderboard signal into local, actionable
packets. Public best score is useful for discovery, but local preflight decides
what Claude/Codex can safely do next.

Source notes:
- Public task list / best scores: https://programbench.com/ (checked 2026-05-20)
- Local status: `scripts/pb_score_audit.py` and `scripts/pb_packet_preflight.py`
- Rule: no packet starts without preflight; no patch is kept without official gate improvement and stable runnable total.

## Current Local Push-To-Lock Lane

These already have useful local baselines and should keep receiving focused packets.

| Priority | Slug | Local Best | Preflight | Next Action |
|---:|---|---:|---|---|
| 1 | `anordal__shellharden.6a6ffd4` | 1161/1292 (89.86%) | PATCH | hand-specialist color/parser primitive only |
| 2 | `konradsz__igrep.aa75630` | 520/703 (73.97%) | PATCH | CLI/help/argparse exactness; avoid TUI |
| 3 | `psampaz__go-mod-outdated.bb79367` | 235/337 (69.73%) | BLOCKED | recover best-run source before any patch |
| 4 | `mookid__diffr.2152742` | 545/782 (69.69%) | PATCH after prior recovery | fixture/error renderer exactness |
| 5 | `skeema__skeema.6a76243` | 994/1547 (64.25%) | PATCH | next fixture/argparse/table primitive |
| 6 | `oppiliappan__eva.41ae245` | 586/963 (60.85%) | PATCH | expression/format specialist after exactness sweep |
| 7 | `foriequal0__git-trim.07c2f50` | 380/710 (53.52%) | PATCH | git-state/config fixture families |

## Public-High-Best Base Expansion Queue

These are not locally close yet, but public best says they are solvable enough to
be worth recovery/oracle scans. Treat this as a preflight queue, not a patch queue.

| Priority | Slug | Public Signal | Local Best | Current Preflight | Packet Type |
|---:|---|---:|---:|---|---|
| 1 | `abishekvashok__cmatrix.5c082c6` | 100% | 274/665 (41.20%) | soft RECOVERY: compile.sh missing, main matches best source | recover compile.sh + fixture scan |
| 2 | `wfxr__csview.8ac4de0` | 100% | 117/347 (33.72%) | real RECOVERY: main differs, compile.sh missing | recover best source first |
| 3 | `sitkevij__hex.61ae69b` | 100% | 78/877 (8.89%) | soft RECOVERY: compile.sh missing, main matches best source | recover compile.sh + fixture scan |
| 4 | `sharkdp__hexyl.2e26437` | 95% public for hexyl family | 88/880 (10.00%) | soft RECOVERY: compile.sh missing, main matches best source | recover compile.sh + fixture scan |
| 5 | `sheepla__pingu.926d475` | 99% | 28/413 (6.78%) | soft RECOVERY: compile.sh missing, main matches best source | recover compile.sh + fixture scan |
| 6 | `rbakbashev__elfcat.52f8cc7` | 98% | 88/644 (13.66%) | soft RECOVERY: compile.sh missing, main matches best source | recover compile.sh + fixture scan |
| 7 | `chmln__sd.87d1ba5` | 97% | 48/864 (5.56%) | soft RECOVERY: compile.sh missing, main matches best source | recover compile.sh + fixture scan |
| 8 | `agourlay__zip-password-finder.704700d` | 99% | 224/791 (28.32%) | BLOCKED: override main.py missing, best source exists | create override from best source |
| 9 | `clog-tool__clog-cli.7066cba` | 98% | 204/778 (26.22%) | BLOCKED: override main.py missing, best source exists | create override from best source |
| 10 | `pemistahl__grex.fa3e8ed` | 97% | 253/1405 (18.01%) | BLOCKED: override main.py missing, best source exists | create override from best source |
| 11 | `sstadick__hck.b66c751` | 97% | 30/856 (3.50%) | BLOCKED: override main.py missing, best source exists | create override from best source |

## Selection Rule For Claude

1. Prefer PATCH or soft RECOVERY targets where `main.py` already matches best source and only `compile.sh` is missing.
2. For each target, search extracted tests for real `help`, `version`, `err_*.stderr`, `.golden`, and argv mapping tests.
3. Apply one exactness primitive only.
4. Official gate; keep only if strict improvement and runnable total stable.
5. Stop after one accepted gate.

## Why This Queue Matters

The proven fixture/exactness recipe has already produced:

| Tool | Lift |
|---|---:|
| caps-log | +85 |
| skeema | +169 |
| eva | +97 |
| git-trim | +27 |

That is +378 tests from fixture/argparse/help exactness alone, plus earlier diffr and shellharden packets. The queue above is how we find where that primitive transfers next.
