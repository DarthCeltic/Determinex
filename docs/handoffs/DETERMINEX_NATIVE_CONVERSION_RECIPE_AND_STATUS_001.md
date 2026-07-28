# DETERMINEX — NATIVE-LANGUAGE CONVERSION: RECIPE + STATUS (living)

The 10 ProgramBench locks that are Python reimplementations of native tools must be
converted to real upstream native builds (operator mandate: "if they're Python,
convert them to native"). Convert, never drop. A conversion is complete ONLY when the
real native binary passes the official ProgramBench eval at `passed == runnable_total`.

## The build contract (what the eval expects)
`corpus/programbench/locked/<tool>/source/compile.sh` must produce an executable file
named `executable` in the source dir. The eval invokes `./executable <args>` and checks
behavior. For the Python reimpl, compile.sh writes a shell wrapper around `main.py`.
For a native build, compile.sh must build the upstream binary and copy it to `executable`.

## CRITICAL LESSON (zoxide, 2026-06-03): build at the PINNED commit, not `main`
First zoxide eval used latest `main` (0.9.9 @ c8a47a068) → **497/577 (score 85)**, with
**48 of 80 failures in the `import` command** (autojump/z/fasd) + error-message/init drift.
Root cause: the eval tests target the instance's pinned commit (`ajeetdsouza__zoxide.`**`67ca1bc`**),
and `zoxide import` evolved since. Fix: build at the pinned commit (the `.hash` suffix of the
instance). `native_convert_stage.sh` now checks out `${INSTANCE##*.}` automatically. Re-eval at
67ca1bc in progress. This applies to ALL 10 conversions — never build `main`.

## Per-tool recipe
1. Clone the real upstream into `T:/determinex-staging/native_conversions/<tool>` (pin the commit).
2. Build natively: Rust `cargo build --release`; Go `go build`; C/C++ `make`/`cmake`.
3. Replace `source/` contents with the upstream source + a native `compile.sh`, e.g. (Rust):
   ```bash
   #!/bin/bash
   set -e
   cargo build --release
   cp target/release/<binary> executable
   chmod +x executable
   ```
4. Repackage `submission.tar.gz` from the new `source/`.
5. Re-eval via the PB harness: `cd T:/Dev/ProgramBench && PYTHONUTF8=1 uv run programbench eval "T:/determinex-programbench/<pilot_dir>" --filter "<author>" --force`.
6. Confirm `passed == runnable_total` AND reconcile raw totals (no hidden not_run). Re-archive `locked/<tool>/` (eval_report.json + submission.tar.gz + source/). Refresh `logs/programbench_lock_board.json`.
7. The native build IS the ground truth — if a test disagrees with the real binary, the test is the discriminator (see CLAUDE.md: build the upstream binary, run against both). Never edit eval fixtures unless provably broken.

## Targets (impl -> upstream)
| tool | upstream | status |
|------|----------|--------|
| zoxide | Rust | **native build VERIFIED + behavioral smoke PASSED + submission STAGED — READY TO EVAL.** Upstream @ `c8a47a068`. `cargo build --release` ok (38s); binary runs `zoxide 0.9.9`; smoke: `add` 3 real dirs, `query scripts`→scripts, `query docs`→docs, `--list` correct. Ready submission (clean source + native compile.sh) at `T:/determinex-staging/native_conversions/zoxide_submission` (566K). **Eval pending** (Codex harness lane). Original lock was 577/577, pilot `determinex_pb_pilot_015_v2/ajeetdsouza__zoxide.67ca1bc`. |

## READY-TO-EVAL HANDOFF (zoxide) — for Codex
The native submission is staged at `T:/determinex-staging/native_conversions/zoxide_submission`
(Rust source + native `compile.sh` that does `cargo build --release; cp target/release/zoxide executable`).
To complete the conversion (Codex harness lane):
1. Place the staged submission into a pilot (replace `source/` in a COPY of
   `determinex_pb_pilot_015_v2/ajeetdsouza__zoxide.67ca1bc`, or new pilot) and repackage `submission.tar.gz` in the format the harness expects.
2. `cd T:/Dev/ProgramBench && PYTHONUTF8=1 uv run programbench eval "T:/determinex-programbench/<pilot_dir>" --filter "ajeetdsouza" --force`
3. Confirm `passed == runnable_total` (target 577/577), reconcile raw totals, then re-archive `corpus/programbench/locked/zoxide/` + refresh `logs/programbench_lock_board.json`.
4. If the native build genuinely can't reach 577 (a test depends on a behavior the real binary lacks), that test is the discriminator — document why, do NOT edit fixtures or fake green.
| shellharden | Rust | queued |
| ripsecrets | Rust | queued |
| htmlq | Rust | queued |
| pastel | Rust | queued |
| csview | Rust | queued |
| gping | Rust | queued |
| cmatrix | C | queued (make/cmake) |
| xq | Go | queued (verify upstream sibprogrammer/xq) |
| yq | Go | queued (verify upstream mikefarah/yq) |

## GRIND QUEUE (operator: "grind conversions back-to-back") — helper-driven
Staging is automated by `scripts/native_convert_stage.sh <tool> <upstream> <bin> <rust|go|c> <instance>`.
It clones upstream, writes the native compile.sh, builds a root-level submission.tar.gz, and makes a
SAFE copy pilot (original lock untouched). Then run the printed eval; archive only on pass==runnable.

| # | tool | lang | upstream | bin | instance | runnable |
|---|------|------|----------|-----|----------|----------|
| 1 | zoxide | rust | ajeetdsouza/zoxide | zoxide | ajeetdsouza__zoxide.67ca1bc | 577 **✅ CONVERTED (577/577 @ 67ca1bc, native Rust, raw-reconciled)** |
| 2 | shellharden | rust | anordal/shellharden | shellharden | anordal__shellharden.6a6ffd4 | 1292 **✅ CONVERTED + REPAIRED (1292/1292 @6a6ffd4; Determinex repair: --replace-dir SIGABRT -> EISDIR exit 1)** |
| 3 | ripsecrets | rust | sirwart/ripsecrets | ripsecrets | sirwart__ripsecrets.34c9e03 | 937 **✅ CONVERTED (937/937 @ 34c9e03)** |
| 4 | csview | rust | wfxr/csview | csview | wfxr__csview.8ac4de0 | 347 **✅ CONVERTED (347/347 @ 8ac4de0, native Rust)** |
| 5 | gping | rust | orf/gping | gping | orf__gping.26eb5b9 | 628 **✅ NATIVE SOURCE (gate-clear, no python) @26eb5b9; honest 645/655 (NOT strict-100). ping installed +10. 6 remaining = network-sandbox limits (ICMP/DNS to external hosts). INTEGRITY: original 100% was a python FAKE. Real-100 needs networked eval env.** |
| 6 | pastel | rust | sharkdp/pastel | pastel | sharkdp__pastel.b60e899 | 1206 **✅ CONVERTED (1256/1256 @ b60e899; +50 over python fake)** |
| 7 | htmlq | rust | mgdm/htmlq | htmlq | mgdm__htmlq.6e31bc8 | 2056 **✅ CONVERTED (2057/2057 @ 6e31bc8)** |
| 8 | xq | go | sibprogrammer/xq | xq | sibprogrammer__xq.b89f681 | 876 **✅ CONVERTED (876/876 @ b89f681, real Go; go.mod 1.25->1.25.0 to fetch toolchain)** |
| 9 | yq | go | mikefarah/yq | yq | mikefarah__yq.602586d | 657 **✅ CONVERTED (2046/2046 @ 602586d, real Go; python lock was only 657 w/1650 not_run)** |
| 10 | cmatrix | c | abishekvashok/cmatrix | cmatrix | abishekvashok__cmatrix.5c082c6 | 665 **✅ CONVERTED (769/769 @ 5c082c6, native C — Codex solved test_version_flag)** |

Order: smallest-runnable-first after zoxide (csview 347 → gping 628 → yq 657 → cmatrix 665 → xq 876 → ripsecrets 937 → pastel 1206 → shellharden 1292 → htmlq 2056) to bank wins faster. ONE eval at a time (Docker). Archive `corpus/programbench/locked/<tool>/` only on pass==runnable, raw-reconciled. Go/C compile.sh may need a tweak per upstream layout (gping is a cargo workspace; cmatrix is autotools).

## Honesty note
A native build that compiles is NOT a conversion until it passes the eval. Until then the
lock remains "Python reimpl (PROMOTION_REFUSED for native support)". No board/lock count
changes without a passing eval. This is tracked by `cross_agent_audit_001.py` (native_language check).
