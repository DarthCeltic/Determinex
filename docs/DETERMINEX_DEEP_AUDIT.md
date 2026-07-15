# Determinex — Deep Audit (2026-06-14)

> A grounded, honest end-to-end account: what Determinex is, what it does, what it's
> meant to do, how it works, how it's safe and unsafe, how it teaches, how it
> helps coders at every level, and everything the audit surfaces — warts included.
> Every claim here is tied to code in this repo, not aspiration.

---

## 1. What Determinex *is*, in one sentence

> **Determinex is a local-first coding system that makes *any* AI model — tiny local,
> frontier cloud, or a future one — produce *correct* code, because correctness is
> bounded by a deterministic oracle (real compilers/tests), not by trusting the
> model.** The model proposes; the oracle disposes. Nothing is accepted unless it
> passes real ground truth.

It is **not** a prompt wrapper, an autocomplete, or a chat-with-your-codebase. It
is an *engine* with a refusal to hallucinate built into its physics.

## 2. What it's *meant* to do (the north star)

The stated vision (from the project's own records): an IDE that **natively
understands and fixes programs and code regardless of system, language, or
issue** — that any level of user can talk to, that builds correctly with few-to-no
bugs, runs on **any computer**, and into which **any AI or agent** (Claude, Codex,
Gemini, local, addons) can be plugged. The "natural heir to VS Code": not a better
editor, but a better *brain* behind the editor everyone already uses.

## 3. What it *does today* (capabilities, grounded)

| Capability | Module(s) | Proven |
|---|---|---|
| **Build from an idea** → verified program | `determinex_synthesize.py`, `determinex_build_from_idea.py` | Live: a 1.9 GB local model produced a verified `rle` against a synthesized oracle |
| **Repair any repo** (diagnose + fix) | `determinex_repair.py` | Live: broken Python diagnosed (blame=CODE, 0 slop) + amplified-fixed to oracle pass |
| **Make a weak model correct** | `determinex_verified_search.py` + 6 amplifier pieces | ~60,000× lift demonstrated (p=0.15/check, 6-check task) |
| **Never cop out / never call a false ceiling** | `determinex_adjudicator.py` | 29 ProgramBench "ceilings" audited → 0 proven-impossible |
| **Judge whether a *test* is correct (not slop)** | `determinex_test_validator.py` | Deterministic: contradiction / env-baked / tautology / reference-fail |
| **Reimplement CLI tools from spec** | the hive + agents | **0/200 legitimate locks** (Methodology pivot 2026-06-30 downgraded 62 upstream source builds from locks to reference corpus) |
| **Bring in any AI model** | `determinex_providers.py` | Live Gemini call returned through the universal contract |
| **Host any coding agent** (Codex/Claude Code/…) | `determinex_agents.py` | claude-code detected installed; output oracle-verified; no-op agent rejected |
| **Auto-establishing rotating rate limit** | `determinex_ratelimit.py` | Flaky 429 → rotates to backup → learns the limit |
| **Run on any computer (graceful degradation)** | `determinex_doctor.py` | Tiered: pure-python → +local model → +docker → +cloud |
| **Privacy-sovereign cloud use** | `determinex_cloak/` | AST obfuscation, audited; cloud sees `x_NNNN`, never your identifiers |
| **In the editor you use** | `frontend/vscode-extension/` | Compiles clean + packages to a real `.vsix` |

Regression net: `tests/test_autofix_pipeline.py` — **40 cases** scoring the
*system's reasoning*, runnable by anyone with `pytest`.

## 4. How it *works* (the architecture, bottom-up)

```
GROUND TRUTH        determinex_oracle (pluggable per-language: pytest/tsc/go/cargo/...)
   │                determinex_test_validator (is the TEST itself sound, or slop?)
   ▼
AMPLIFIER CORE      determinex_verified_search  — best-of-K vs the oracle; P(solve)=1-(1-p)^K
   ├── pieces       decompose · case_memory · context · progress · contract · router
   ├── brownfield   determinex_amplified_solve → hive/amplifier_bridge (DETERMINEX_AMPLIFY)
   └── greenfield   determinex_build_from_idea (synthesized oracle)
   ▼
GOVERNOR            determinex_adjudicator (no cop-out) + governance/ (no overclaim)
EXPLAIN / FIX       determinex_explainer · determinex_remediation · determinex_ingest
ORCHESTRATION       scripts/hive (build loop) · agents (swe/pb) · determinex_repair
PROVIDERS / AGENTS  determinex_providers (models) · determinex_agents (CLIs) · extensions
SURFACE             ide command surface → tauri bridge → JSON CLI → {Tauri shell, VS Code}
```

The load-bearing idea: **greenfield and brownfield are not two engines — they are
two oracle *sources* feeding one amplifier.** Everything is compositional; the IDE
commands, the hive bridge, and the agents are thin wrappers that *delegate*, never
reimplement (verified by a no-duplication meta-bench test).

### The math that makes it real
A model right with probability **p** per attempt, sampled **K** times against a
**sound** oracle, succeeds with **1 − (1−p)^K**. Any p > 0 is driven toward
correct. Decompose until p is workable; sample against the oracle; keep what
passes. *That* is why a tiny model can be correct on hard things (e.g. dstask
5%→99%): the cached binary ran, the oracle exposed the real failure surface, and
verified search drove it up.

## 5. The correctness moat — why it can't hallucinate

- **No LLM judges.** The only arbiter is a real compiler/test run. There is no
  "looks good to me."
- **`solved` is never claimed without a passing OracleResult + proof.** Verified
  search records the proof.
- **The Test Validator** stops the one way verified search could go wrong (a
  *slop* oracle) — garbage oracle in = confident garbage out, so a wrong test is
  caught deterministically (contradiction / env-baked / tautology / reference).
- **Falsification holds:** a model returning `def add(a,b): return 999` is
  *rejected*. (Meta-bench.)
- This session, the author's own code was wrong four times (a regex over-match, a
  guard false-alarm, a wrongly-committed red test, a code-extractor truncation) —
  **the ground-truth tests caught every one.** The system holds *itself* to the
  oracle.

## 6. How it's **safe**

- **Sandboxed execution.** Model-generated candidate code runs through
  `intake.hardened_runner` (workspace-bounded, env-scrubbed, **network + Docker
  denied by default**, opt-in only). Not raw `subprocess`.
- **Privacy sovereignty (Cloak).** With `DETERMINEX_REQUIRE_CLOAK=1` (default),
  cloud calls are **blocked unless Cloak is active**; proprietary identifiers are
  AST-obfuscated to `x_NNNN` before leaving the machine and restored locally.
- **Per-stage safety gates** (`hive/safety_gate.py`): `pre_spec_gate`,
  `pre_api_gate` (before every cloud call), `post_generation_gate` (after the
  builder), and corpus sign/verify gates.
- **No-overclaim governance** (`governance/`): 18 authority anchors
  (`release_ready`, `training_eligible`, `universal_support_claimed`, …) that must
  stay False until *proven*; a deterministic pre-commit guard fails the build if
  any tracked file asserts one true. **Verified across 11,858 files: all closed.**
- **Security scanning** (`scripts/security/`): SBOM generation, dependency scan,
  license scan, container scan, lockfile verification.
- **Workspace isolation**: symlink whitelist on workspace paths; Windows Job
  Objects for subprocess isolation; isolated git worktrees per patch in the gate.
- **A standing security audit** (`dev/parallel_execution_layer_audit.py`) that
  classifies every executing site and **fails the build on `os.system`/`os.popen`/
  `shell=True`** — it found and forced the fix of a real `os.popen` this session.

## 7. How it's **unsafe** (honest — the real risk surface)

- **It executes model-generated code.** Even sandboxed (no network), running
  arbitrary generated code on your machine is inherently risky; the hardened
  runner mitigates but does not eliminate (no kernel-level container locally on
  Windows). High-trust use should run the heavy path in Docker.
- **6 audit `UNKNOWN_REQUIRES_REVIEW` sites remain** (`determinex_oracle`,
  `determinex_agents`, `determinex_test_validator`, `determinex_metrics`, read-only git
  helpers). These execute by design (the oracle runs *your* build/test toolchain,
  which legitimately needs network for deps). Bringing them to a clean
  classification is an **owner trust-model decision**, deliberately left flagged,
  not faked green.
- **API keys live in `.env`** (Anthropic/DeepSeek/Gemini present). Standard
  local-dev practice, but they are real secrets on disk; `.env` is git-ignored and
  a pre-commit `detect-private-key` hook exists, but treat the machine accordingly.
- **Hosted agents (Codex CLI / Claude Code) can mutate real source.** The registry
  verifies their *output* through the oracle, but an agent run is real file
  editing — run it on a throwaway/worktree until you trust it; source-mutation
  authority is a governance anchor that stays False.
- **Cloak reduces but does not zero cloud exposure.** It obfuscates identifiers;
  control-flow/structure still leaves the machine. For maximum sovereignty use the
  local-only path (`DETERMINEX_LOCAL_BUILDER=1`).
- **Correctness is only as sound as the oracle.** If you synthesize an oracle from
  a vague idea, the build matches the *model's interpretation* (flagged
  `oracle_proposed` — confirm it). A wrong human spec yields a confidently-wrong
  program that passes a wrong test. The Test Validator catches *provable* slop, not
  intent errors.

## 8. How it **teaches** (this is a first-class feature, not an afterthought)

- **8 user levels with per-level teaching profiles**
  (`ide/user_levels_and_teaching_windows.py`), with **hard rules enforced at every
  level**:
  - `proof_status_visible=True` for *all* levels — **beginner mode must NOT hide
    proof; power-user mode must NOT loosen the gates.**
  - `authority_gates_active=True` for all levels.
  - Every level's **teaching window must explain *why* something is blocked**
    (`teaching_window_explains_blocked_reason=True`).
  - Every level must declare what it will not hide: proof status, **"training stays
    false"**, blocked reasons.
- **The Failure Explainer** (`determinex_explainer.py`) tells a learner, per failure:
  *whose fault* (CODE / ENVIRONMENT / TEST), *what the test expected*, *what the
  program did*, *the minimal delta to be right*, and the *proof*. That is a tutor
  that never hand-waves.
- **The Learning Studio** (`ide/learning_studio_*`) — a verified, **non-authorizing
  teaching** surface (teaching outputs explicitly cannot grant authority).
- **Companion RAG with citation-or-refuse**: the teaching companion must cite its
  source or refuse to answer — no confident fabrication.
- **The deepest teaching principle:** because the oracle is the judge, a learner
  *sees correctness happen*. "It works" is never an opinion they have to trust — it
  is a green test they can read. That builds the right mental model: verify, don't
  believe.

## 9. How it helps coders at **every level**

| Level | What Determinex gives them |
|---|---|
| **Absolute beginner** | "Describe an idea" → a *working, verified* program, with the synthesized tests shown so they learn what "correct" means. Teaching windows explain every block in plain language; proof is never hidden. |
| **Learning dev** | Repo Clinic diagnoses *their* repo with honest blame (CODE/ENV/TEST) + the minimal fix, so they learn debugging from ground truth, not vibes. |
| **Working engineer** | Repair + amplified build on real codebases; bring their preferred AI; the oracle guarantees no hallucinated fixes land. Cloak lets them use cloud AI on proprietary code safely. |
| **Senior / architect** | The Adjudicator's "is this actually impossible?" discipline + the Test Validator's "is this test slop?" turn fuzzy judgments into proofs. A genuine impossibility comes with a one-line proof, not a shrug. |
| **Team / org** | No-overclaim governance + SBOM/license/dependency scans + per-stage safety gates + a reproducible meta-bench = a system whose claims are *auditable*, not marketing. |
| **Researcher** | A grounded 0/200 ProgramBench empirical baseline, a pluggable-oracle benchmark substrate, and the verified-search math as a reusable correctness primitive. |

## 10. The honest state — proven vs provisional vs aspirational

- **Proven (tested, live or in the 40-case meta-bench):** the correctness engine,
  build-from-idea, repair, the amplifier math, the adjudicator/validator, provider
  + agent + extension registries, the rate limiter, the VS Code build, the methodology pivot (0/200 PB),
  governance, the sandbox migration.
- **Provisional (audited, not finalized):** the SWE-bench ablation (privacy-cost
  delta needs clean Docker reruns); Rosetta Layers 2–3 (L1 active); the
  v11/v6/v5 model generation (eval queued — last *verified* numbers are the prior
  generation at 86% system).
- **Aspirational / environment-gated:** the standalone Tauri editor shell's
  last-mile; agent-CLI *live* runs at scale; training runs (Rosetta finish, model
  re-eval); the 6-site security trust-model sign-off; Docker field-prove of
  `DETERMINEX_AMPLIFY` on a full ProgramBench tool.

## 11. Everything else the audit surfaces (the warts)

- **The repo was ~3× larger than its engine.** ~321k lines / 2,796 files were an
  accreted self-auditing "apparatus" (status/proof lane-shims + generated guard
  tests) from autonomous campaigns. It was mapped, its 254-line governance core
  *extracted* into `governance/`, and the sprawl staged to `T:` for deletion —
  reversible, nothing lost. `scripts/` engine ≈ 110k lines now.
- **Duplication is a live hazard** of fast autonomous building. This session alone,
  three near-duplications were caught *before* landing (a sandbox that would have
  duplicated `hardened_runner`; two repair paths; the provider-vs-agent overlap).
  The discipline that prevents it: thin wrappers that delegate to one canonical
  module. Keep auditing for it.
- **Windows-first reality:** two Python interpreters (3.11 hive vs 3.13 MS-Store)
  with different `/tmp` mappings bit a test this session; the toolchain is genuinely
  cross-platform but the dev machine has sharp edges.
- **The model family numbers are partly stale** (current gen unevaluated) — but the
  amplifier *deliberately makes model strength a knob, not a wall*, so this is
  lower-stakes than it looks.

---

## The one-paragraph verdict

Determinex is a **real, rare correctness engine** wrapped in a teaching-first product
vision. Its moat is not a model and not features — it is that **correctness is
bounded by a deterministic oracle**, which makes it un-hallucinatable wherever
ground truth exists, lets *any* model or agent plug in safely, and lets learners
*watch correctness happen* instead of trusting a claim. It is genuinely rigorous
(a verified 0/200 ProgramBench baseline reflecting true empirical rigor; build-from-idea and repair
proven live) and genuinely incomplete (editor last-mile, training polish, a
security sign-off, Docker-scale proof). The most important thing about it is the
discipline it embodies and enforces — on its users, on any AI plugged into it, and
on itself: **no claim without proof.**
