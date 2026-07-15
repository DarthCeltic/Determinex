# Determinex System Coherence Map (2026-06-14)

> One picture of the whole system: every capability, its ONE canonical module, how
> it's exposed (CLI + IDE command + frontend), what's wired end-to-end vs partial,
> and the duplication that must be reconciled. The rule everywhere: **one
> implementation, thin wrappers, no duplication.**

## The spine (single source of truth, bottom-up)

```
GROUND TRUTH        determinex_oracle (pluggable per-language) + determinex_test_validator (no slop)
   │
AMPLIFIER CORE      determinex_verified_search        (any model -> correct; the math)
   ├── brownfield   determinex_amplified_solve  ──► hive/amplifier_bridge (DETERMINEX_AMPLIFY in executor)
   │                  (oracle = compiler/tests on EXISTING code)
   └── greenfield   determinex_build_from_idea
                      (oracle = determinex_synthesize on a NEW idea)
GOVERNOR            determinex_adjudicator (no cop-out) + governance/ (no overclaim)
EXPLAIN/FIX         determinex_explainer · determinex_remediation · determinex_ingest
ORCHESTRATION       determinex_autofix (report) · scripts/hive (build loop) · agents (swe/pb)
```

Greenfield and brownfield are **not two engines** — they are two *oracle sources*
feeding the one amplifier. The hive bridge and the IDE commands are thin wrappers.

## The transport chain (frontend ⇄ engine), verified

```
Next.js panel  --invoke()-->  Rust #[tauri::command]  -->  scripts/ide/tauri_backend_bridge.py
   -->  IDEBackendCommandSurface.call()  -->  canonical engine module
```

`/api/core` + `/api/event` HTTP endpoints also exist. The bridge has its own
allowlist (`_TAURI_COMMANDS`) + name-map + status-map, so **a command is only
reachable from the UI when it is wired at every link**.

## Capability → exposure matrix

| Capability | Canonical module | CLI | IDE command (surface→bridge) | Frontend panel | End-to-end? |
|---|---|---|---|---|---|
| Greenfield build | `determinex_build_from_idea` | ✅ | `synthesize_oracle_preview`/`build_from_idea_opt_in` → `preview_idea_oracle`/`build_idea` | Idea Lab | ⚠️ to bridge ✅; Rust+React page **pending** |
| Brownfield repair | `determinex_amplified_solve` + adjudicator | ✅ (`autofix`) | `diagnose_*`/`generate_patch_plan` (OLD path) | Repo Clinic | ⚠️ **old path wired, new engine NOT** |
| Amplified build-loop | `hive/amplifier_bridge` (DETERMINEX_AMPLIFY) | ✅ (env flag) | — | — | ⚠️ engine-only, no IDE trigger |
| Ceiling adjudication | `determinex_adjudicator` | ✅ (`classify`) | — | — | ❌ not surfaced |
| Test slop check | `determinex_test_validator` | ✅ | — | — | ❌ not surfaced |
| Governance / no-overclaim | `governance/` | ✅ (guard) | (view-models) | Proof Center | ⚠️ Proof Center uses OLD view-models, not `governance/` |
| Compiler-oracle evals | `agents` + hive | ✅ | — | (Benchmark UI) | ⚠️ partial |
| Cloak | `determinex_cloak` | ✅ | — | — | ❌ engine-internal, not surfaced |
| Rosetta | `rosetta/` | ✅ | — | — | ❌ engine-internal, not surfaced |

## What is genuinely wired end-to-end

- **Greenfield** to the Python bridge (preview returns a sound oracle; build blocks
  without opt-in). Proven live (1.9 GB model → verified `rle`).
- The **amplifier** in the hive executor (`DETERMINEX_AMPLIFY=1`), proven live.
- The **governance** guard in pre-commit + meta-bench (33 cases).
- 64 ProgramBench locks (the golden proof the loop works).

## Duplication / incoherence — RECONCILED 2026-06-14

1. ✅ **Two repair paths converged.** `determinex_repair.py` is now THE brownfield
   engine (ingest → oracle → adjudicate → validate → explain → amplified fix),
   the dual of `determinex_build_from_idea`. Wired as the `repair_diagnose` IDE
   command (surface + bridge). Delegates; reimplements nothing.
2. ✅ **Proof Center → governance/.** `get_governance_status` reads the live
   `governance/` authority anchors (all_closed=True, 18 anchors, 0 violations)
   as the source of truth, not the archived apparatus.
3. ✅ **Adjudicator/Validator surfaced.** `repair_diagnose` returns blame
   (CODE/ENVIRONMENT/TEST) + the adjudicator moves + proven-slop count.
4. ⏳ **Amplifier UI trigger.** `repair_diagnose` exposes diagnosis + the engine
   carries the opt-in amplified fix; a dedicated `amplified_build` panel trigger
   is the remaining thin add.

Go/Rust oracles are now real compile-oracles (not stubs); TS already was.

5. ✅ **Universal provider registry + extension protocol** (`determinex_providers.py`,
   `determinex_extensions.py`). Every model -- Claude, Codex/GPT, Gemini, DeepSeek,
   local Ollama, and any addon -- exposes the amplifier's one `generate` contract
   and feeds the router's multi-provider escalation ladder. Proven live (a Gemini
   call returned 'WORKS'; 4 providers ready). Addons (providers/oracles/commands)
   register via a plugin's `register(api)` -- the VS Code-style host pattern.
   Correctness stays oracle-bounded: an addon provider is just another `generate()`
   the oracle still judges.

## "Heir to VS Code" -- the honest path

The **brain** (oracle-bounded correctness + any-model + build/repair + extensions)
is the moat and it is built. The **editor shell** is the remaining product piece.
Smartest path is NOT to rebuild Monaco/LSP/terminal -- it is to ship this engine
where developers already are:
- as a **VS Code extension** (VS Code is the editor; Determinex is the brain), AND
- the **standalone Tauri shell** (Idea Lab / Repo Clinic / Proof Center),
both calling the SAME backend already wired through the command surface + bridge.
Plus an **agent-tool registry** to host Codex CLI / Claude Code / Gemini CLI as
*sub-agents* (not just models). These are product/frontend builds, not invention.

## The gap list — what to tackle next (honest, prioritized)

**A. Coherence (close the duplication above)**
   - A1 Converge the repair path: `diagnose_*` → new adjudicator/amplified engine.
   - A2 Rewire Proof Center → `governance/` + meta-bench truth.
   - A3 Add an `amplified_build` IDE command (delegate to the hive bridge).

**B. Frontend last-mile (per-panel)**
   - B1 Idea Lab: Rust `#[tauri::command]` for `preview_idea_oracle`/`build_idea`
        + the React page that calls them and renders the verified program.
   - B2 Repo Clinic: render adjudicator verdict + explainer blame + remediation.

**C. Capability depth**
   - C1 Richer model-assisted test synthesis for example-free vague ideas
        (today they degrade to a symbol-exists smoke test).
   - C2 Live-wire the TS/JVM oracles (the user's own stacks: SwingSwap, Hook).
   - C3 Field-prove `DETERMINEX_AMPLIFY` on a real ProgramBench tool end-to-end.

**D. Loose ends**
   - D1 The 4 pre-existing `test_audit_counts_invariants_preserved` failures.
   - D2 Rosetta L2 finish; re-eval C1/C3/C7 (v11/v6/v5); clean SWE-bench rerun
        (all *polish* now — the Amplifier makes model strength a knob, not a wall).
   - D3 Surface or explicitly scope Cloak / Rosetta in the product (or document
        them as engine-internal by design).

## The one-line state

The **engine and the spine are coherent and proven**; the **wiring is partial** —
greenfield reaches the bridge, the amplifier runs in the hive, governance guards
the repo. The work that remains is **convergence (kill the two repair paths),
frontend last-mile (Rust command + React pages), and capability depth (vague-idea
synthesis, TS/JVM oracles)** — integration and depth, not new invention.
