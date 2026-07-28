# Determinex — Social Pack (10 posts)

> **Status**: Draft for Ryan's review. Agents draft; Ryan posts.
> Every post: one claim + one receipt + one screenshot spec.
> Conform to docs/policy/SOVEREIGNTY_SURFACING_STANDARD.md.
> Do not post without Ryan's review and approval.

---

## Post 1 — The One-Liner

**Platform**: X/Twitter + LinkedIn
**Copy**:
> Your code never leaves in the clear. Nothing unverified ever gets in. Receipts for both.
>
> That's Determinex — a local-first AI coding system I built from scratch.
> Solo dev. Consumer GPU. Third-year student. Lincolnton, NC.
>
> 47 CLI tools fully resolved under ProgramBench's official benchmark.
> The compiler is the only judge.

**Receipt**: `corpus/programbench/eval_index.json` — 47 entries with `official_full_suite_resolved: true`
**Screenshot spec**: `eval_index.json` filtered view in terminal, count visible. OR `docs/campaign/DUAL_AGENT_BOARD.md` Strict Locks section.

---

## Post 2 — The Self-Correction Story

**Platform**: X thread (3 posts) or LinkedIn long-form
**Copy**:
> We used to say 77 locks. Then we found the bug.

> Our metric excluded "not_run" tests from the denominator. The official ProgramBench
> metric counts them. 77 → 15 after correction. (It's 47 now after real fixes.)

> We published the audit doc, corrected every claim, and built a guard that makes
> the same mistake impossible in CI. The audit doc is committed to the repo.

> This is what "honest count only" means in practice.
> [Link to docs/audits/pb_measurement_audit_2026_06_06.md in repo]

**Receipt**: `docs/audits/pb_measurement_audit_2026_06_06.md`
**Screenshot spec**: The audit doc open in editor, showing the "77 → 15" headline clearly. Then `pb_override_scan.py --guard` terminal output: "0 violations."

---

## Post 3 — Project Cloak

**Platform**: X/Twitter + LinkedIn
**Copy**:
> When Determinex calls a cloud AI for code help, the AI sees this:
>   x_0070, x_0177, x_0187, x_0914
>
> Not this:
>   separability_matrix, CompoundModel, DeterminexConfig, _session_cache
>
> 1,813,760 identifiers audited. Zero leaks. The audit log is in the repo.

**Receipt**: `logs/cloak_audit/` — run with `DETERMINEX_CLOAK_AUDIT=1`, `verify_cloak.py` PASSED verdict
**Screenshot spec**: Side-by-side split: real source code (left) vs obfuscated prompt to cloud AI (right). Cloak audit verdict "CLEAN" at bottom.

---

## Post 4 — Compiler Oracle

**Platform**: X/Twitter
**Copy**:
> The training reward signal in most AI coding systems: another LLM saying "looks good."
>
> Determinex's training reward signal: rustc.
>
> Every training sample has passed a real compiler. Every failure — with the exact error
> and the fix that resolved it — is a labeled training pair.
>
> No LLM judges. No rubrics. Compiler or nothing.

**Receipt**: `corpus/programbench/locked/*/eval_report.json` — any locked tool's report showing passed==total
**Screenshot spec**: Terminal showing `cargo check` or `rustc` output, PASS status, then the WAL entry with the (error → fix) pair.

---

## Post 5 — Provenance in the Product

**Platform**: LinkedIn
**Copy**:
> Every AI system produces outputs. Most can't tell you where those outputs came from.
>
> Determinex can.
>
> The Attribution Tagger writes a log entry every time a generated output resembles
> a registered reference source — before it enters the training queue.
>
> attribution.jsonl: tool, source repo, SPDX license, match type.
> It's not an afterthought. It's wired into every build.

**Receipt**: `logs/copyright_guard/attribution.jsonl`
**Screenshot spec**: `attribution.jsonl` open showing several entries with license tags. The `corpus/references/` directory structure visible below it.

---

## Post 6 — The Origin Record

**Platform**: X/Twitter
**Copy**:
> April 9, 2026, 10pm: first commit.
> April 12, 2026, 11am: working multi-agent coding system.
>
> 73 hours. One developer. One GTX 1660 Ti. Lincolnton, NC.
>
> The git history is the receipt.
> [docs/papers/ARCHITECTURE.md — April 9-12 timeline]

**Receipt**: `docs/papers/ARCHITECTURE.md` (origin record section), git log
**Screenshot spec**: `git log --oneline` showing the April 9 initial commit through April 12 prototype commit. OR the ARCHITECTURE.md timeline section.

---

## Post 7 — ProgramBench Performance

**Platform**: LinkedIn long-form
**Copy**:
> ProgramBench: reimplementing 200 CLI tools that actually exist.
> Every public AI model tested: 0–0.5% of tools fully resolved.
>
> Determinex: 47 tools fully resolved under the official metric.
> (passed==total, zero not_run tests, zero overrides suppressing collection)
>
> "Fully resolved" means every test in every branch of every test suite passes —
> including tests most models never reach.
>
> Tool count. Not a percentage claim. Not "state of the art." 47 out of 200.
> The eval_index is public. The receipts are in the repo.

**Receipt**: `corpus/programbench/eval_index.json`, `pb_override_scan.py --guard` output
**Screenshot spec**: eval_index filtered to locked tools (terminal command + output), count visible. `just doc-guard` green.

---

## Post 8 — The Dual-Agent Architecture

**Platform**: X/Twitter
**Copy**:
> Determinex uses two AI agents working in parallel:
> - Claude (Driver): verifies every result, routes bounces, controls the benchmark ledger
> - Codex (Executor): builds, fixes, submits
>
> Neither agent can certify its own work.
> The Compiler Oracle is the only judge.
>
> If it doesn't compile, it doesn't count.

**Receipt**: `docs/campaign/PROTOCOL.md` (Section 1-2 on roles)
**Screenshot spec**: DUAL_AGENT_BOARD.md rendered view showing the strict lock count and active batch status.

---

## Post 9 — Consumer Hardware

**Platform**: X/Twitter + LinkedIn
**Copy**:
> Determinex's local AI models:
> - C1 Engineer (1.5B params, Qwen2.5-Coder) — builder
> - C3 Observer (3B, Qwen2.5) — monitor
> - C7 Sentinel (7B, Mistral) — architect
>
> All three run on a GTX 1660 Ti. 6GB VRAM.
> Fine-tuned on compiler-verified examples. Pre-DSL baseline: 83%. Post-DSL: 86%.
>
> No cloud compute required for the core loop.
> Cloud AI is optional — and when used, Project Cloak handles the privacy.

**Receipt**: `logs/eval_results/eval_determinex-engineer-v10-dsl_*.json`, `logs/eval_results/eval_determinex-observer-v5-dsl_*.json`
**Screenshot spec**: Terminal showing eval results for each model. GTX 1660 Ti visible in `nvidia-smi` output.

---

## Post 10 — Bidirectional Sovereignty

**Platform**: LinkedIn (flagship post)
**Copy**:
> "Bidirectional IP sovereignty" — what does that mean, concretely?
>
> OUT: Project Cloak. Before Determinex touches any cloud AI, every private identifier in your
> codebase is mapped to an opaque token. The AI sees x_0070, never separability_matrix.
> 1,813,760 identifiers audited. Zero leaks. Receipt: the cloak audit log.
>
> IN: Compiler Oracle + Provenance Tagger. Every training sample passes a real compiler before
> it enters the corpus. Every output with a reference match is logged to attribution.jsonl
> before training. Receipt: eval_report.json (passed==total) + attribution.jsonl.
>
> Both properties are auditable. Both receipts exist. Neither claim requires you to trust us.

**Receipt**: `logs/cloak_audit/` + `corpus/programbench/locked/*/eval_report.json` + `logs/copyright_guard/attribution.jsonl`
**Screenshot spec**: Three-panel: Cloak audit PASSED verdict (top-left), an eval_report.json passed==total (top-right), attribution.jsonl entries (bottom). Caption: "Receipts for both."

---

## Posting Notes

- Ryan reviews all copy before posting
- Numbers are rechecked against eval_index at post time (count may change)
- Screenshots must be taken fresh — not recycled from old sessions with stale numbers
- Post 2 (self-correction) should go early — it establishes credibility before performance claims
- Post 7 (ProgramBench) should include the scope qualifier in a thread reply
- Never post autonomously — Ryan presses publish
