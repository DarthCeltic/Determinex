# Determinex — 3-Minute Demo Script

> **Status**: Draft for Ryan's review. Agents draft; Ryan records and publishes.
> Conform to docs/policy/SOVEREIGNTY_SURFACING_STANDARD.md.
> Every beat below names the on-screen artifact.

---

## Beat 1 — Spec to Build (0:00–0:30)

**Screen**: `specs/demo_spec.md` open in editor. Show a plain Markdown spec:
```
# Goal: A CLI tool that counts unique words in a file.
## Language: rust
## Constraints: No unsafe blocks. Returns word count to stdout.
```

**Narration** (verbatim or close):
> "This is all Determinex needs — a plain spec. No prompt engineering. No special syntax."

**Action**: Run `python scripts/determinex_hive.py new-session --spec specs/demo_spec.md --lang rust`

**Screen**: Terminal output showing session ID, DAG generation, Builder step executing.

**Key artifact on screen**: `sessions/<session_id>/wal.jsonl` — the write-ahead log.

**Narration**:
> "The Hive Mind generates a build plan — a DAG of steps — and hands each to the Builder.
> Every step goes into the write-ahead log. Nothing is lost."

---

## Beat 2 — Compiler Gate (0:30–1:10)

**Screen**: The builder generates code. Show a deliberate first-pass error:
- Display the code with a compile error
- Show the Compiler Oracle output: `rustc` error message, exact line, exact symbol

**Narration**:
> "The Compiler Oracle is the only judge. Not an LLM. Not a rubric. rustc.
> If it doesn't compile, the system retries — with the exact error injected back
> into the next prompt."

**Action**: Watch auto-retry. Second attempt produces passing code.

**Key artifact on screen**: `sessions/<session_id>/wal.jsonl` entry:
```json
{"attempt": 2, "compile_errors": ["error[E0308]: mismatched types..."], "status": "PASS"}
```

**Narration**:
> "That error-to-fix pair is now a training sample. Every failure teaches the next model."

---

## Beat 3 — Project Cloak (1:10–1:50)

**Screen**: Open `scripts/determinex_cloak/` directory. Show the cloak pipeline.

**Action**: Run a cloaked SWE-bench task (pre-recorded or live if fast enough).

**Screen split**:
- Left: Real source code with real identifier names (`separability_matrix`, `CompoundModel`)
- Right: Obfuscated prompt sent to cloud AI: `x_0070`, `x_0177`, `x_0187`

**Narration**:
> "Before any cloud AI call, every private identifier in your codebase maps to an opaque token.
> The AI sees x-0070. It never sees separability-matrix."

**Screen**: Cloak audit log — `logs/cloak_audit/cloak_audit_<run>.jsonl`:
```
VERDICT: CLEAN — 1,813,760 identifiers audited, 0 restoration failures, 0 privacy leaks
```

**Narration**:
> "The audit log captures every API request. 1.8 million identifiers. Zero leaks.
> The receipt exists. You can check it."

---

## Beat 4 — Provenance (1:50–2:20)

**Screen**: Open `logs/copyright_guard/attribution.jsonl`:
```json
{"slug": "entr", "source": "eradman/entr", "license": "MIT", "match_type": "corpus_ref"}
```

**Narration**:
> "Every training sample that enters the corpus carries its provenance.
> If Determinex's output resembles a registered reference, it logs it — automatically —
> before the sample ever reaches the training queue."

**Screen**: Show `corpus/references/` directory structure (academic/, open_source/, patents/).

**Narration**:
> "Attribution isn't an afterthought. It's wired into every build."

---

## Beat 5 — Benchmark and Honesty (2:20–3:00)

**Screen**: `corpus/programbench/eval_index.json` — filter to `official_full_suite_resolved: true` entries.
Show count in terminal.

**Screen**: `docs/audits/pb_measurement_audit_2026_06_06.md` — open to the headline.

**Narration**:
> "47 CLI tools fully resolved under ProgramBench's official metric — every test passing,
> zero tests missing. But this number used to be 77."

**Screen**: Show the audit doc's correction: 77 → 15 → 47.

**Narration**:
> "We found a measurement bug. Our metric excluded not_run tests. The official metric counts them.
> We ran the audit, published the discrepancy, corrected the count, and built a guard
> that makes the same mistake impossible going forward."

**Screen**: `scripts/pb_override_scan.py --guard` running — output: `0 violations`.

**Narration**:
> "One developer. Consumer GPU. Third-year student. Lincolnton, NC.
> The receipts are in the repo. The code is real. The math is checked."

**End card**: `docs/policy/SOVEREIGNTY_SURFACING_STANDARD.md` — "Your code never leaves in the clear. Nothing unverified ever gets in. Receipts for both."

---

## Production Notes

- Record in a single continuous session if possible — no cuts mid-demo
- Terminal: dark theme, 14pt monospace, full-width
- Determinex UI (Tauri app): if frontend is stable, use the Proof Center panel for Beat 4
- Beat 3 cloak visualization is the most valuable — spend extra time here if running long
- The self-correction story in Beat 5 is the strongest credibility moment — do not cut it
