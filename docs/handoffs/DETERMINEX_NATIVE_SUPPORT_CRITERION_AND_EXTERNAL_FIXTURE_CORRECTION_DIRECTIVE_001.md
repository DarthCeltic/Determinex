# DETERMINEX — NATIVE-SUPPORT CRITERION + EXTERNAL-FIXTURE CORRECTION DIRECTIVE 001

**Author:** Claude (lead coordinator). **Date:** 2026-06-03. **Status:** correction directive for the next wave (Batch 006) + our-side config fixes.

## The problem this fixes
The engine is **complying with proof discipline but proving almost nothing real.** Lane B "Python CLI family" = 5 of Determinex's OWN scripts (claim_scanner, promotion_harness, acquisition_packets, toolchain_inventory, per_family_template), with shallow pillars (detector="script exists", verifier="runs + emits JSON"). It is honest (correctly NOT claimed as support, registry 13/0) but **self-referential** — Determinex proving itself against itself. After all waves, real external native-support = ~0. The fix is not more discipline; it is **pointing the discipline at real external targets.**

## 1. Native-support acceptance criterion (LOAD-BEARING — encode this in the harness)
"Determinex **natively supports** family X" is true ONLY when, for **≥ N real EXTERNAL projects** of family X (N≥3, not Determinex-owned):
1. **detector** — Determinex correctly identifies the project type from the real repo (not "a script exists").
2. **toolchain** — required toolchain admitted via governed acquisition packet (real version+hash+verify transcript).
3. **build** — the real project builds under Determinex's bounded execution.
4. **verifier (behavioral)** — the project's **own test suite passes** after Determinex operates on it (reuse the compiler-oracle / SWE-bench / ProgramBench eval harness — NOT a new "emits JSON" check).
5. **repair-loop** — Determinex repairs a **seeded defect** in the real project and **re-verifies green** (proves it can actually fix, not just observe).
6. **claim boundary** — no support/family/public claim beyond what passed; evidence + transcripts on disk, sha-recorded.
A row is `NATIVE_SUPPORT_PROVEN` only if 1–6 pass on real external projects. Anything less = `PROMOTION_CANDIDATE` or exact blocker. **Self-owned Determinex scripts are NOT valid fixtures.**

## 2. External-fixture mandate (you already own the corpus)
- **Use the real corpora that exist:** 56 ProgramBench locked tool dirs (`corpus/programbench/locked/<tool>/source/`) + SWE-bench repos (`T:/determinex-swebench`) + the 89 SWE-bench per-repo specs. These ARE real external projects across languages/families.
- **Hard rule:** every family proof's fixture must be a real external project from these corpora (or a curated real third-party repo). **A Determinex-owned script may never be a fixture.** Encode a guard that rejects fixtures whose path is under `scripts/`, `assurance/`, or other Determinex-owned trees.

## 3. Wire the verifiers you already built (do not write shallow new ones)
- Family verifier MUST call an existing real engine: `scripts/validators/*` (compiler oracle, 14 langs), the SWE-bench solve+repair loop (`scripts/determinex_swebench_agent.py`), or the ProgramBench eval harness. The verifier = "real project's tests pass after Determinex touches it" — never "Determinex's own script returns 0."

## 4. Raise the harness bar
- `promotion_harness_001.py` / `per_family_proof_template_001.py`: add a guard that a row's fixture + verifier evidence reference **external, non-Determinex** paths and a **behavioral test result** (project test suite), plus a **repair-loop result**. Self-surface or "script-exists/runs-JSON" evidence → `PROMOTION_REFUSED: SELF_SURFACE_OR_SHALLOW_FIXTURE`. Add tests for these refuse-cases.
- This makes tonight's 5 self-surface rows correctly drop from "eligible" to "refused (shallow)" — which is the honest state.

## 5. ProgramBench → native-support bridge (Lane C) is the highest-yield path
- 56 locked tools are *real external projects you've already reimplemented to 100% testable*. The bridge should: detect a real repo using tool X → build it → run its tests → repair a seeded bug → re-verify. A PB lock + that bridge = genuine native support of working with X-based projects. This converts up to ~56 (then 200) rows of *real* evidence — not self-surfaces.

## 6. Our-side config fixes (operator actions)
1. **Codex sandbox mode → workspace-write/full-access** (trusted local repo): clears the Docker-pipe escalation + the ACL-stamping wedge so build/test/Docker "just run."
2. **Disable the image/vision tool in the Codex (openai.chatgpt) extension** — the `gpt-image-2 does not exist` config error took Codex fully offline; it's not needed for repo work.
3. **Raise Codex's ChatGPT/OpenAI plan tier** (or have it batch into larger chunks) — the 429s forced a takeover.
4. **AGENTS.md additions:** "commit coherent chunks frequently; append-only to coord docs (never overwrite the other agent's section); push only after self-verify; every promotion fixture must be a real EXTERNAL project, never a Determinex-owned script."
5. **Admit toolchains** (node/cargo/go/python via packets) so external builds run.
6. **Fix stale prompt path:** claim scanner is `scripts/claim_scanner/day_one_public_claim_scanner.py` (not `scripts/status/...`).

## 7. Next wave (Batch 006) — "external-fixture native-support proof"
- Lane 1: write criterion §1 into the harness + add refuse-tests (self-surface/shallow → refused).
- Lane 2: pick ONE real external Python CLI project (from PB locked or a curated repo), run the full §1 chain (detect→toolchain→build→behavioral-verify→repair→re-verify). Measure real per-row cost (will be >> the 0.1–0.75s self-surface cost).
- Lane 3: PB→native-support bridge against 3–5 real PB-locked tools end-to-end.
- Lane 4: if ≥N external rows pass §1, attempt the FIRST real release-family promotion through the accounting path (registry 0→1 only if all family criteria pass).
- Gates unchanged: no fake green, no self-surface fixtures, registry change only on real proof, public NO_GO, PATENT_FILED false.

## The one-line correction
**No promotion fixture may be a Determinex-owned script. Every native-support proof runs against a real external project, verified by its own tests + a repair-loop, using the engines we already built.** That converts the machine from proving itself to proving it does your code.
