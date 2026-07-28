# DETERMINEX — PATH TO FULL PB + FAMILY LOCKS (audit, living)

Operator: *"once these clear, audit what else can be done, and the tools + path to full family/PB locks."*
This is the forward-audit. A DEEP per-tool audit auto-runs once the current Ring-1 grind +
first family-proof clear (trigger in the loop); this doc holds the map + is updated each pass.

## PB locks: 56 / 200 (28%). Path on the 144 non-locked
By current best_score (board, 2026-06-03):

| bucket | count | nature | path |
|--------|-------|--------|------|
| ≥99% | 2 | near-lock (doxygen 249/250, fasttext 349/352) | fast-track / 1-3 test fixes (Codex a-m has these) |
| 90-99% | 2 | a few fixes | fast-track / rabbit-hole |
| 50-90% | 24 | partial impls | native build + targeted work |
| 10-50% | 92 | weak impls / python stubs | **highest-yield: native build often jumps these (yq 657→2046 pattern)** if a real upstream exists |
| <10% | 24 | barely started | real per-tool engineering; some are hard-native (compilers) |

**Highest-yield lever:** the 116 low-score tools (10-50% + <10%) — many are python reimpls/stubs;
a native upstream build can jump them to ~100% the way yq/xq/pastel did. Triage each: python-reimpl
with real native upstream → fast-track; complex-native (compilers/interpreters) → rabbit-hole.

## The honest ceiling (tools that need an env grant, not laziness)
~7 non-locked tools are network/privileged and **cannot fully lock in a no-network/no-privilege
sandbox** — they need a deliberately networked/privileged eval env, or they're honest env-gates:
`ekzhang__bore`, `hatoo__oha`, `mkj__dropbear`, `robertdavidgraham__masscan`, `nuta__nsh`,
`sheepla__pingu`, `johanneskaufmann__html-to-markdown` (+ gping, already documented). Path: stand up
an ICMP/DNS/network-capable eval container (CAP_NET_RAW + outbound) for these, or document the exact
env-gate (per gping's integrity-finding pattern). **This is the realistic ceiling: ~full PB locks are
achievable only with a networked eval env for this cluster.**

Genuinely hard-native (multi-session, real compilers/interpreters): `tinycc`, `tree-sitter`,
`ninja`, `svd2rust` — rabbit-hole, deep work, not quick.

## Realistic PB ceiling estimate
- Fast/medium (native build + targeted work + rabbit-hole): the ~133 non-network, non-hard-compiler tools → lockable.
- Network/env cluster (~7): lockable only with a networked eval env grant.
- Hard-native compilers (~4): lockable with sustained deep work.
- So **~190+/200 is realistically achievable** given (a) the grind, (b) a networked eval env for the cluster, (c) deep work on the compilers. A small honest tail may remain env/license-gated and documented.

## Path to FAMILY locks
Family-proof needs ≥3 real external fixtures per family — **we already have Rust 37 / Go 15 / C 6 native-locked tools.**
- **Now runnable:** Rust family-proof (then Go, then C) — detect→toolchain→build→their tests→repair→re-verify on ≥3 real native projects → registry families 0→1→2→3.
- **Beyond PB (Ring 2):** the known-world 383 rows span non-PB families (frameworks, DBs, security, docs, infra). Each needs its own family-proof template + real external fixtures (curated repos / SWE-bench corpora). The PB native locks seed the language families; non-PB families need their own fixture sourcing.
- **Full family locks** = every family in the known-world release-supported via its family-proof. Sequence: Rust → Go → C (PB-seeded) → then the non-PB families by fixture availability.

## DEEP AUDIT (queued — auto-run when current grind + first family-proof clear)
When Ring-1 fast-track is largely drained and the first family-proof lands, run a per-tool audit:
1. Classify all remaining non-locked tools: fast-track | rabbit-hole | network-env | hard-native | license/other.
2. For each: upstream lang, instance, exact blocker, the path, est. effort.
3. Family map: which families are lock-ready (≥3 fixtures) vs need fixtures.
4. Produce the ranked execution order + the env grants needed (networked eval, etc.).
5. Update the master plan scorecard with the realistic ceiling per layer.

## NETWORKED EVAL ENV — GRANTED + APPLIED (2026-06-03)
Operator granted the networked eval env (the one infra grant for the ~7 network/privileged tools).
**Applied:** `T:/Dev/ProgramBench/src/programbench/constants.py` `DOCKER_RUN_ARGS` now includes
`--cap-add=NET_RAW` (env-overridable via `PROGRAMBENCH_DOCKER_RUN_ARGS`). This grants eval containers
raw ICMP sockets so network tools can actually ping/render — capability-only, no test-logic change,
non-network tools unaffected (no existing lock changes). Default bridge network already provides
outbound + DNS. NOTE: this is an external change to the PB harness (not in Determinex git) — recorded here.
Validating on gping first; then the cluster (oha/pingu/bore/dropbear/masscan/nsh) becomes lock-eligible.
Revert: set `PROGRAMBENCH_DOCKER_RUN_ARGS=""` or restore the empty list.
