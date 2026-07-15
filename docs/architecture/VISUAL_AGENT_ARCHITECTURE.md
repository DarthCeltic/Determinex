# Visual Agent Architecture

**Date:** 2026-05-27  
**Status:** Implemented and active

---

## Overview

Determinex's visual agent system extends the Compiler Oracle model from code to actions. Every agent observes an environment, plans an action, passes it through the safety governor, executes it in a sandboxed context, and verifies the result via an oracle — then writes a signed trace record to the corpus on T:.

The system supports four environment types: browser, desktop (VM-only), mobile (emulator-only), and visual document. All agents share the same action/verdict/corpus contract defined in `base_agent.py`.

---

## Execution Pipeline (Invariant)

```
TaskSpec valid
→ observation captured (screenshot / DOM / accessibility tree / screen state)
→ action planned
→ safety_governor.evaluate_action() → ALLOW / REQUIRE_CONFIRMATION / BLOCK
→ sandbox requirement satisfied (VM/emulator/browser isolation)
→ action executed via controller
→ oracle verified
→ trace HMAC-signed
→ corpus written via CorpusManager
```

No action may be executed unless every step in this chain passes.

---

## Type Contract (`scripts/agents/base_agent.py`)

### Core Types

| Type | Role |
|---|---|
| `VisualTaskSpec` | Task description: env type, goal, constraints, benchmark source |
| `AgentObservation` | Captured environment state (screenshot, DOM, accessibility tree, OCR text) |
| `AgentAction` | Planned action with type, target, payload, rationale |
| `ActionResult` | Execution outcome: success, new observation, error |
| `OracleVerdict` | Verification result: passed, score, evidence, oracle type |
| `AgentTrace` | Full trace: spec → observations → actions → results → verdicts |
| `CorpusRecord` | Signed, versioned training record written to T: |

### Environment Types
`code · terminal · vision · browser · desktop · mobile · document · sql · security`

### Action Types
`READ_SCREEN · READ_DOM · READ_ACCESSIBILITY_TREE · CLICK · TYPE · PRESS_KEY · SCROLL · DRAG · TAP · SWIPE · OPEN_APP · SWITCH_WINDOW · RUN_COMMAND · EDIT_FILE · APPLY_PATCH · UPLOAD_FILE · DOWNLOAD_FILE · SUBMIT_FORM · SEND_MESSAGE · INSTALL_SOFTWARE · GRANT_PERMISSION · ENTER_CREDENTIAL · MAKE_PURCHASE · DELETE_DATA · DEPLOY_OR_PUBLISH`

### Oracle Types
`compiler · test · terminal · browser · visual · dom · accessibility · desktop · mobile · sql · security · policy · human_confirmation`

---

## Corpus Types (Seven)

| Corpus | T: Path | Content |
|---|---|---|
| `code_verdict` | `T:/determinex_corpus/code_verdict/` | Compiler-verified code patches |
| `terminal_trace` | `T:/determinex_corpus/terminal_trace/` | CLI task execution traces |
| `browser_trace` | `T:/determinex_corpus/browser_trace/` | Browser navigation/form/DOM traces |
| `desktop_trace` | `T:/determinex_corpus/desktop_trace/` | Desktop GUI interaction traces (VM) |
| `mobile_trace` | `T:/determinex_corpus/mobile_trace/` | Mobile app interaction traces (emulator) |
| `visual_repair` | `T:/determinex_corpus/visual_repair/` | Screenshot diff → patch pairs |
| `safety_refusal` | `T:/determinex_corpus/safety_refusal/` | Denied requests + blocked actions |

All writes via `CorpusManager`. No module writes directly to corpus JSONL except `corpus_manager.py`.

---

## Safety Layers

| Layer | File | Gate |
|---|---|---|
| L0 | `determinex_safety.py` | Categorical keyword scan on spec text |
| L1 | `determinex_safety.py` | Intent classifier (signal + amplifier) |
| L2 | `hive/safety_gate.py` | Egress secret filter + Cloak enforcement |
| L3 | `hive/compiler.py` | Builder output malicious-pattern scan |
| L4 | `determinex_safety.py` | Corpus HMAC sign/verify |
| L5 | `agents/safety_governor.py` | Action-level gate (pre-execution) |

L5 runs before every click, tap, type, submit, install, or deploy.

---

## Module Dependency Order

```
base_agent.py
    └── corpus_manager.py
        └── safety_governor.py
            └── vision/*
                └── browser/* / desktop/* / mobile/*
                    └── bench_adapters/*
                        └── tests/sentinelbench/*
```

Nothing should be imported above its layer in this chain.

---

## Sandbox Requirements

| Environment | Required Sandbox | Hard-block if absent |
|---|---|---|
| Browser | Playwright isolated profile | Yes |
| Desktop | VM (VirtualBox/QEMU/Hyper-V) | Yes |
| Mobile | Android emulator | Yes |
| Cloud vision API | Visual Cloak PII redaction | Yes |

---

## Benchmark Targets

| Benchmark | Adapter | Env |
|---|---|---|
| SWE-bench Multimodal (517 JS instances) | `swebench_multimodal_adapter.py` | browser |
| WebArena | `webarena_adapter.py` | browser |
| VisualWebArena | `webarena_adapter.py` | browser + vision |
| OSWorld-Verified | `osworld_adapter.py` | desktop |
| AndroidWorld | `androidworld_adapter.py` | mobile |

---

*Determinex Visual Agent Architecture · Lunarian Data Systems · 2026-05-27*
