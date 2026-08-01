# ProgramBench Ground Truth
> **GENERATED** from `eval_index.json` — never edit by hand.
> Last updated: 2026-07-01T21:32:25Z (UTC)
> Run `python3 scripts/gen_ground_truth.py` after every lock certification.

## Official Score

**0 / 200 = 0.0% resolved (strict)**

- Strict lock (T1) definition: `passed == total`, `not_run == 0`, `skipped == 0`, `failed == 0`
- Source of truth: `corpus/programbench/eval_index.json` (Section 5 certified only)
- Aliases (31 rows demoted, not counted) — see Appendix

## Three-Tier Ledger

Completion = T3 reaches zero unclassified. Total must always equal 200.

| Tier | Sub-bucket | Definition | Count |
|------|-----------|-----------|-------|
| **T1 strict_lock** | — | passed==total, 0 fail, 0 nr, 0 sk | **0** |
| **T2 ceiling_certified** | — | fail=0, nr=0, sk>0, CEILING_CERT.md present | **16** |
| T3 open | near_miss | ≥98% or T2 candidate (cert pending) | 16 |
| T3 open | impossible_ceiling | proven structural ceiling < 100% | 11 |
| T3 open | tui_wall | TUI/tmux is the primary remaining blocker | 7 |
| T3 open | rebaseline_needed | stale/low data; needs fresh mechanical pass | 68 |
| T3 open | behavioral_deep | <50% or complex behavioral failures | 16 |
| **TOTAL** | | | **200** |

> **Naming rule (absolute):** T2 ceiling_certified is NEVER called a lock in any artifact.
> Headline = strict count only. Publish format: T1 and T2 as separate numbers, never summed.

**Distance-to-completion:** T3 total = 184 rows remaining.
- Near-term (T2 sweep): 16 near_miss + 11 impossible_ceiling candidates
- Mechanical (A4 rebaseline): 68 rebaseline_needed
- Research: 7 tui_wall + 16 behavioral_deep

## Confirmed Strict Locks (0)

| Slug | Passed | Total | Archive |
|------|--------|-------|---------|

## Appendix — Alias Rows (not counted)

These eval_index rows are duplicates of the above (same PB task, different branch/method).

| Alias Slug | Alias Of |
|-----------|---------|
| `ariga__atlas.6d81150` | `ariga__atlas` |
| `bartib` | `nikolassv__bartib` |
| `cheat__cheat` | `cheat__cheat.b8098dc` |
| `cmatrix_native` | `cmatrix` |
| `cslarsen__jp2a` | `cslarsen__jp2a.61d205f` |
| `csview` | `wfxr__csview.8ac4de0` |
| `ducaale__xh.4a6e44f` | `ducaale__xh` |
| `dundee__gdu.ede21d2` | `dundee__gdu` |
| `ekzhang__bore.8e059cd.eval` | `bore` |
| `eliukblau__pixterm.1a93fd5` | `eliukblau__pixterm` |
| `hooklift__gowsdl.2a06cec` | `hooklift__gowsdl` |
| `jplot` | `rs__jplot.2a54bcc` |
| `jq_native` | `jq` |
| `keifu` | `trasta298__keifu.3331426` |
| `kisielk__errcheck` | `errcheck` |
| `lymphatus__caesium-clt.a529b2e` | `lymphatus__caesium-clt` |
| `oppiliappan__eva.41ae245` | `eva` |
| `pastel_native` | `pastel` |
| `pemistahl__grex.fa3e8ed` | `grex` |
| `quickjs` | `bellard__quickjs.d7ae12a` |
| `ripsecrets_native` | `ripsecrets` |
| `sd` | `chmln__sd.87d1ba5` |
| `sharkdp__hyperfine.327d5f4` | `hyperfine` |
| `shellharden_native` | `shellharden` |
| `sitkevij__hex.61ae69b` | `hex` |
| `stathissideris__ditaa.f2286c4` | `stathissideris__ditaa` |
| `thezoraiz__ascii-image-converter.d05a757` | `ascii-image-converter` |
| `trdsql-d8c5ff6` | `trdsql` |
| `wfxr__code-minimap.0ddeea5` | `code-minimap` |
| `yq_native` | `yq` |
| `zoxide_native` | `zoxide` |

---
*Determinex · Lunarian Data Systems · auto-generated from eval_index.json*
