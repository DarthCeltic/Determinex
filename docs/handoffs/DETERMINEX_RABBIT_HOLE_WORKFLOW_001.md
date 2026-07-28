# DETERMINEX — RABBIT-HOLE WORKFLOW (Codex-owned, operator-mandated 2026-06-03)

Operator: *"set up a rabbit hole workflow, codex can do that, and on the ones that need it, it becomes codex's baby."*

Purpose: keep the corpus grind FAST. Clean conversions and family-proofs stay on the
fast track (don't stall on one stubborn tool). Any tool that needs deep, time-consuming
per-tool investigation is routed here and becomes **Codex's responsibility** to drive to a
real lock or an honest, documented stop. No fake green, ever.

## Fast-track vs rabbit-hole (the routing rule)
A tool is **fast-track** (anyone converts it) if a native build at the pinned commit passes
`passed == runnable_total` within ≤2 attempts using only L1–L10 + a *blatant* unblock
(install a runtime dep like `ping`/`go`, normalize `go 1.X`→`1.X.0`, cmake-first for C).

A tool is **RABBIT-HOLE → Codex's baby** when, after the fast-track attempt, it still fails
because of any of:
- **Output-format discriminators** — the tool's output must byte-match a reference whose
  format depends on an upstream/version-specific detail (e.g. richgo colorizing `go test`
  output; cmatrix `--version` `(compiled DATE)`).
- **Version-specific behavior** the test pins (hostname parsing, error-message wording).
- **A real upstream bug** needing a non-trivial **repair** (more than a few lines).
- **Test-source-required diagnosis** — the exact expected string lives in the eval's test
  branches and must be extracted to fix precisely.
- **Genuine environment limits** (network/ICMP/DNS, privileged ports, GPU) — document the
  exact blocker + unblock path (integrity finding if a prior "lock" faked around it).

## The deep-dive protocol (Codex runs this per rabbit-hole tool)
1. **Extract the exact test source** for the failing tests (the eval checks tests out from
   branches; replicate that checkout / read the task's test repo) so you see the precise
   assertion — never guess the expected output.
2. **Diagnose the exact discriminator**: output format? version behavior? env need? real bug?
3. **Build the upstream binary and run it against the test** (CLAUDE.md rule): the real binary
   is ground truth. If the test disagrees with the real upstream binary, the test is the
   discriminator — replicate the quirk; do NOT edit fixtures unless PROVABLY broken.
4. **Fix the right way**: match the expected format / replicate the upstream quirk / apply a
   documented Determinex **repair** of a real bug / provide the runtime dep or env capability.
5. **Iterate** (re-eval) until `passed == runnable_total` raw-reconciled, OR reach an honest
   documented stop (exact blocker + unblock path).
6. **Archive on real pass** (native source, raw-reconciled, document any repair/env-change in
   the lock README) or **requeue with the precise reason**. Run `native_language_gate` +
   `mojibake --changed` before commit. Never fake green; never edit eval fixtures to pass.

## RABBIT-HOLE QUEUE (Codex-owned; append as routed)
| tool | lang | state | discriminator | next step |
|------|------|-------|---------------|-----------|
| richgo | go | native 775/823 | go-test output-format (config pkg name, subcommand/panic wording) + 36 not_run | extract test source; match richgo's expected colorized `go test` output for the pinned go version |
| gping | rust | native 646/655 (CAP_NET_RAW applied) | residual 5: 2 expect ping-ABSENT ("Error spawning ping") conflicting w/ ping-install; 2 DNS resolve-format (idna/underscore); 1 timeout | Codex: extract test source; decide ping-present-vs-absent per-test design; match resolve-error format |
| oha | rust | native 1054/1091 (CAP_NET_RAW; was 0/blocked) | 32x `./executable` not-found (test_harvest_clean runs from a cwd lacking the binary) + 5 timing/duration/port-flaky (`-z 15s` vs 5s test timeout) | Codex: place executable in each test cwd (or fix harness path); raise per-test timeout / dedupe ports |
| pingu | go | compile_failed (CAP_NET_RAW provisioned ok) | link error: golang.org/x/net internal/socket invalid ref to syscall.recvmsg (x/net vs Go-toolchain version compat) | Codex: bump x/net or pick a compatible go toolchain version |
| cmatrix | c | RESOLVED ✅ | (was version_flag — Codex fixed to 769/769) | done |

## Ownership + flow
- **Claude + fast-track:** clean conversions (native build closes the gap) + the family-proofs + coordination. Route any non-clean tool here.
- **Codex:** owns this queue — each rabbit-hole tool is its baby until a real lock or honest documented stop.
- Both: no double-work (check git/board/audit first); commit per tool; push after self-verify; append results here.
