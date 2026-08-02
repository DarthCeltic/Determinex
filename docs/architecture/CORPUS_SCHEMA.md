# Corpus Schema

**Date:** 2026-05-27
**Schema Version:** `determinex-agent-trace-v1`

---

## Overview

Every training record written to T: must conform to this schema. The `CorpusManager` enforces it on every write. No module writes directly to corpus JSONL files except `scripts/corpus/corpus_manager.py`.

---

## Base Record (all corpus types)

```json
{
  "schema_version": "determinex-agent-trace-v1",
  "corpus_type": "<code_verdict|terminal_trace|browser_trace|desktop_trace|mobile_trace|visual_repair|safety_refusal>",
  "timestamp": "2026-05-27T14:32:00Z",
  "source_benchmark": "<programbench|swebench|webarena|osworld|androidworld|hive|sentinelbench|manual>",
  "task_id": "<stable identifier for the task instance>",
  "input_hash": "<SHA-256 of canonical input>",
  "output_hash": "<SHA-256 of canonical output>",
  "_sig": "<BLAKE2b-256 HMAC hex over sorted-key canonical JSON>"
}
```

All fields except `_sig` are included in the HMAC computation (sorted keys, ASCII-safe JSON).

---

## Per-Type Extensions

### `code_verdict`

```json
{
  "lang": "rust",
  "spec_text": "...",
  "patch": "...",
  "compile_result": "pass|fail",
  "compile_errors": [],
  "test_result": "pass|fail",
  "test_errors": [],
  "attempt": 1,
  "model_builder": "determinex-engineer-v11-dsl"
}
```

### `terminal_trace`

```json
{
  "task_spec": {},
  "commands": [{"cmd": "ls -la", "stdout": "...", "rc": 0}],
  "oracle_verdict": {"passed": true, "score": 1.0, "oracle_type": "terminal"},
  "duration_ms": 340
}
```

### `browser_trace`

```json
{
  "task_spec": {},
  "observations": [{"type": "screenshot", "url": "...", "dom_hash": "..."}],
  "actions": [{"type": "CLICK", "selector": "#submit", "safety_decision": "ALLOW"}],
  "oracle_verdict": {"passed": true, "score": 1.0, "oracle_type": "browser"},
  "replay_available": true
}
```

### `desktop_trace`

```json
{
  "task_spec": {},
  "vm_id": "determinex-vm-001",
  "observations": [{"screenshot_hash": "...", "window_title": "...", "accessibility_tree_hash": "..."}],
  "actions": [{"type": "CLICK", "x": 120, "y": 340, "safety_decision": "ALLOW"}],
  "oracle_verdict": {"passed": true, "score": 1.0, "oracle_type": "desktop"}
}
```

### `mobile_trace`

```json
{
  "task_spec": {},
  "emulator_id": "emulator-5554",
  "observations": [{"screenshot_hash": "...", "activity": "com.app.MainActivity"}],
  "actions": [{"type": "TAP", "x": 200, "y": 400, "safety_decision": "ALLOW"}],
  "oracle_verdict": {"passed": true, "score": 1.0, "oracle_type": "mobile"}
}
```

### `visual_repair`

```json
{
  "task_spec": {},
  "before_screenshot_hash": "...",
  "after_screenshot_hash": "...",
  "diff_regions": [{"x": 10, "y": 20, "w": 100, "h": 50, "diff_score": 0.87}],
  "repair_patch": "...",
  "oracle_verdict": {"passed": true, "score": 1.0, "oracle_type": "visual"}
}
```

### `safety_refusal`

```json
{
  "trigger": "spec|action|output|api_egress",
  "layer": "L0|L1|L2|L3|L4|L5",
  "category": "<harm category name>",
  "violating_text_excerpt": "<first 200 chars of matching content>",
  "safety_mode": "strict|warn|audit",
  "action_type": "<action type if L5>",
  "blocked": true
}
```

---

## File Layout on T:

```
T:/determinex_corpus/
  code_verdict/
    YYYY-MM-DD.jsonl
  terminal_trace/
    YYYY-MM-DD.jsonl
  browser_trace/
    YYYY-MM-DD.jsonl
  desktop_trace/
    YYYY-MM-DD.jsonl
  mobile_trace/
    YYYY-MM-DD.jsonl
  visual_repair/
    YYYY-MM-DD.jsonl
  safety_refusal/
    YYYY-MM-DD.jsonl
  audit/
    YYYY-MM-DD_audit.log
  rejected/
    YYYY-MM-DD_rejected.jsonl
```

## Rejected Records

Records that fail HMAC verification are written to `rejected/` with an `_rejection_reason` field appended. They are never used for training.

## Versioning

`schema_version` must be bumped whenever the base record or any per-type extension adds/removes a mandatory field. Old records remain valid under their schema version.

---

*Determinex Corpus Schema · Ryan Gurganious · 2026-05-27*
