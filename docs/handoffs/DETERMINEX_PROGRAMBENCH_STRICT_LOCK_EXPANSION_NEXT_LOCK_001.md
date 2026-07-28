# DETERMINEX_PROGRAMBENCH_STRICT_LOCK_EXPANSION_NEXT_LOCK_001

## Status

No ProgramBench evals were run in this batch. This is strict-lock prep only.

Canonical board source: `logs/programbench_lock_board.json`.

## Current Board Truth

- Board rows: `200`.
- Strict archived locks: `55`.
- Score-100 not archived: `1` (`trasta298__keifu.3331426`).
- Factory-accepted non-locked rows on current board query: `71`.
- Aggregate runnable score: `52.74%` (`84,957 / 161,099`).

## Next Strict-Lock Targets

| Priority | Tool | Board State | Prep Action | Boundary |
|---:|---|---|---|---|
| 1 | `trasta298__keifu.3331426` | `274/274`, score `100.0`, `next_action=lock-now` | Archive `eval_report.json`, `submission.tar.gz`, and `source/` under `corpus/programbench/locked/keifu/`, then refresh board. | Do not call it strict until archive and board refresh both exist. |
| 2 | `doxygen__doxygen.966d98e` | `249/250`, score `99.6`, `next_action=lock-now` | Reconcile with the existing Doxygen operator/security-policy blocker before any archive action. | Do not bypass policy admission because the score is near-lock. |
| 3 | `facebookresearch__fasttext.1142dc4` | `349/352`, score `99.15`, gap `3` | Read `gate_result.json` and patch only the newly failing native-source cases. | Re-eval required before archive. |
| 4 | `kyoh86__richgo.313114f` | `775/786`, score `98.60`, gap `11` | Split config-loading, argument parsing, and go-not-found panic failures before patching. | Re-eval required before archive. |
| 5 | `jqlang__jq.b33a763` | `1394/1521`, score `91.65`, gap `127` | Use `corpus/programbench/anchors/01_jq/` plus current `gate_result.json`; prioritize high-frequency parser/output regressions. | High-impact anchor, not a fast strict lock. |

## Exact Commands To Run Later

Do not run these until the operator authorizes ProgramBench eval work:

```powershell
cd T:\Dev\ProgramBench
PYTHONUTF8=1 uv run programbench eval "T:\determinex-staging\pb_keifu_detail_fixed_date_v5" --filter "trasta298__keifu" --force
```

For lock archival, preserve the strict definition: official eval has `passed == runnable_total`, archive contains `eval_report.json`, `submission.tar.gz`, and `source/`, and `logs/programbench_lock_board.json` refreshes with `locked_archive=true`.

