# Documentation Audit — 2026-05-26

> Audit of all 34 markdown files under `docs/`, classifying each by purpose, age, and overlap. Identifies stale numbers, redundant docs that should be consolidated, and the canonical set going forward.

---

## Headline findings

- **34 docs total**, ~720 KB combined. **The WHITE_PAPER abstract is stale on the lead Determinex claim**: it says 35 ProgramBench locks at 46.97 % aggregate; reality is **53 locks at 52.59 %**.
- **9 ProgramBench planning/audit docs overlap heavily** and were written across 8 different days in May. They should collapse to **3 canonical surfaces** (status, strategy, history).
- **4 handoff docs** are session-specific and ~80 % stale; archive them under `docs/_handoffs/` or delete.
- **4 companion docs** (skill load files) are well-structured and should stay separate.
- **Foundation docs** (ARCHITECTURE, WHITE_PAPER, PROJECT_CLOAK, LICENSING) are canonical — keep as-is, update specific stale numbers.

---

## 1. WHITE_PAPER.md — needed updates

`docs/WHITE_PAPER.md` (2,087 lines, 170 KB, last updated 2026-05-25)

### 1.1 Stale numbers — update before next publication round

| Line | What it says | What it should say |
|---:|---|---|
| 18 (Abstract) | "Determinex has **35 strictly verified locks** archived... as of 2026-05-25, with corpus aggregate runnable score at **46.97 % (72,878 / 155,169)**" | "**53 strictly verified locks** archived... as of 2026-05-26, with corpus aggregate runnable score at **52.59 % (84,728 / 161,099)**" |
| 18 (Abstract) | "64 additional tools are at `gated:accept` status... and 112 are in `gated:reject`" | "72 at `gated:accept`, 110 at `gated:reject`" |
| 18 (Abstract) | mentions `ripgrep` / `shellharden` / `monolith` as the only-named locks | Add 5-26 marquee locks: `chroma`, `xz`, `flamelens`, `ascii-image-converter`, `muffet`, `ov` |
| 1118 | "**Determinex's confirmed position (as of May 13, 2026):** Four ProgramBench tasks are verified locks" | OK to keep as a dated historical snapshot — but add a forward pointer to the 5-26 board status doc |
| 1133 | "**The path to 35-40 locks:**" | "**The path to 75-100 locks (Phase 2):**" — 35-40 is met |

### 1.2 Structural status — good

The white paper section structure is sound:
- Abstract → Problem → Principle → Architecture → Hardening → Tech deep-dive → Self-improvement loop → Training data → Results → A better benchmark → Generalization → Moat → Enterprise → Phase 3 → Open questions → Acks → References

The 17 sections flow logically. Don't restructure. Just update numbers.

### 1.3 Add to white paper (new content for this rev)

- The **eight reusable patterns** that produced the 5-26 lock surge (slug-hash audit, install AS `executable`, `exec -a`, stderr/stdout `sed`, hardware env pinning, counter-state trick, source flag-parser fixes). These are publishable contributions to the "captured-fixture reproducibility" sub-problem and belong in Section 8 (A Better Benchmark) — they generalize beyond ProgramBench.
- The **`programbench-compiled:determinex-cached` image-cache stickiness** finding — Go `ldflags -X` injections silently fail under cache reuse. Belongs in Section 7 (Results) as a documented infrastructure limitation.

---

## 2. ProgramBench docs — consolidation map

There are **18 docs** with "programbench" in the name (case-insensitive). They serve different purposes but have heavy overlap. Recommended consolidation:

### Tier 1 — Canonical surfaces (KEEP, 3 files)

| Doc | Role |
|---|---|
| `PROGRAMBENCH.md` | Top-level strategy, lock list, current status block (updated 5-26). The entrypoint. |
| `PROGRAMBENCH_BOARD_STATUS_2026-05-26.md` | Latest dated board snapshot. Each new snapshot supersedes the previous; keep last ~3 for trend data, archive older. |
| `PROGRAMBENCH_FACTORY_ARCHITECTURE.md` | Design doc for the eval factory infrastructure (Hetzner shards, gate logic, two-ledger model). Architecture reference, not status. |

### Tier 2 — Historical snapshots (KEEP, but ARCHIVE older versions)

| Doc | Date | Action |
|---|---|---|
| `PROGRAMBENCH_BOARD_STATUS_2026-05-26.md` | 5-26 | Keep (current) |
| `PROGRAMBENCH_BOARD_STATUS_2026-05-25.md` | 5-25 | Keep (1-day delta reference) |
| `PROGRAMBENCH_BOARD_STATUS_2026-05-22.md` | 5-22 | **Move to `docs/_archive/`** |
| `RECENT_WORK_2026_05.md` | 5-18 | **Move to `docs/_archive/`** — superseded by board-status timeline |

### Tier 3 — Plans/maps that need to be MERGED into PROGRAMBENCH.md or DELETED

| Doc | Date | Recommendation | Why |
|---|---|---|---|
| `PROGRAMBENCH_200_LOCK_PLAN.md` | 5-18 | **DELETE** | Original 35-lock plan; goal met; superseded by FACTORY_ROADMAP |
| `PROGRAMBENCH_200_FACTORY_ROADMAP.md` | 5-25 | **MERGE into PROGRAMBENCH.md** (Phase 2 section) | Roadmap for next jump; should be a section of the canonical strategy doc |
| `PROGRAMBENCH_200_COMPLETION_MAP.md` | 5-24 | **DELETE** | Auto-generated tool list; recreate on demand from `pb_score_audit.py` |
| `PROGRAMBENCH_HIGH_PUBLIC_BEST_TARGET_QUEUE.md` | 5-19 | **DELETE** | Captured 1-day target queue, superseded by board status |
| `PROGRAMBENCH_PAUSED_TOOL_LOCK_GAP_REPORT.md` | 5-21 | **DELETE** | One-off gap report; near-lock targets now live in board status |
| `programbench_floor_raise_roadmap.md` | 5-21 | **DELETE** | Floor-raise plan executed; results in board status |
| `PROGRAMBENCH_LANGUAGE_AUDIT.md` | 5-24 | **MERGE** language sections into `PROGRAMBENCH_FACTORY_ARCHITECTURE.md` | Native-source routing rules belong with factory design |

### Tier 4 — Quick audits / handoffs that are now redundant

| Doc | Date | Recommendation |
|---|---|---|
| `PROGRAMBENCH_AUDIT.md` | 5-26 | **DELETE** — superseded by 5-26 board status (this is the older "quick" version) |
| `PROGRAMBENCH_FULL_AUDIT.md` | 5-24 | **DELETE** — superseded |
| `PROGRAMBENCH_TWO_LEDGER_INTEGRITY.md` | 5-23 | **MERGE** into `PROGRAMBENCH_FACTORY_ARCHITECTURE.md` (Rule A vs Rule B section) |
| `CLAUDE_PROGRAMBENCH_HANDOFF.md` | 5-13 | **Move to `docs/_handoffs/`** — historical |
| `PROGRAMBENCH_EXTERNAL_MODEL_HANDOFF.md` | 5-19 | **Move to `docs/_handoffs/`** |
| `programbench_session_handoff_20260523.md` | 5-23 | **Move to `docs/_handoffs/`** |

### Net result

**Before:** 18 ProgramBench docs.
**After:** 5 ProgramBench docs (PROGRAMBENCH.md, BOARD_STATUS x2, FACTORY_ARCHITECTURE, plus an `_archive/` and `_handoffs/` containing older history).

---

## 3. Architecture / foundation docs — KEEP

These are canonical references. Recommend keeping each separate; they cover distinct surfaces.

| Doc | Size | Status |
|---|---:|---|
| `ARCHITECTURE.md` | 79 KB | Living document, last 5-19. **Action:** update with the 5-26 ProgramBench numbers and the 8-pattern catalog. |
| `WHITE_PAPER.md` | 170 KB | Lead deliverable. **Action:** see §1 above. |
| `PROJECT_CLOAK.md` | 26 KB | Cloak spec + validation log. **Action:** verify SWE-bench cited numbers are current. |
| `LICENSING.md` | 2 KB | Tiny, clear, current. **Action:** none. |

---

## 4. Companion docs (skill-load files) — KEEP separate

These are designed to be loaded individually based on user-query routing. They have YAML frontmatter (`name:`, `description:`, `depends:`) for that purpose. **Do not merge — they're working as designed.**

| Doc | Skill | Status |
|---|---|---|
| `COMPANION_VIBE_CODING.md` | vibe-coding | OK |
| `COMPANION_CLOAK_SAFETY.md` | cloak-safety | OK |
| `COMPANION_FLOW_AI.md` | flow-ai | OK |
| `COMPANION_MOA_MOE.md` | moa-moe | OK |

---

## 5. Audits / plans / playbooks — mixed; needs grooming

| Doc | Date | Recommendation | Why |
|---|---|---|---|
| `AUDIT_IDE_TECH_DEBT.md` | 5-06 → 5-18 | **Re-run the audit** and produce a 5-26 version. Then archive the old one. 3 weeks old, the codebase has changed a lot. |
| `capability_audit.md` | 5-18 | **Update or archive.** "May 2026" framing is fine, but the ProgramBench numbers cited will be stale. |
| `BENCHMARK_EXPANSION.md` | 5-18 | **Keep.** Forward-looking plan, references multiple benchmarks. Update PB numbers and SWE-bench status. |
| `WINDOWS_EVAL_PLAYBOOK.md` | 5-18 | **Keep.** Operational runbook for a specific eval lane. Not stale. |
| `MODERN_OPS_STACK.md` | 5-16 | **Keep.** Infrastructure runbook for the wave-3 modernization. |
| `WORLD_KILLER_PLAN.md` | 5-18 | **Update or split.** The "12-hour sprint plan" framing is stale; the SWE-bench + ProgramBench numbers are stale. Consider splitting into `SWEBENCH_PLAN.md` + `PROGRAMBENCH.md` (which already exists). |
| `HANDOFF_PROMPT_ANTIGRAVITY.md` | 5-06 | **Move to `docs/_handoffs/`.** Specifically a RunPod retrain handoff with `<POD_IP>` placeholders. Historical. |

---

## 6. Net consolidation plan

### Before
```
docs/
├── ARCHITECTURE.md
├── AUDIT_IDE_TECH_DEBT.md
├── BENCHMARK_EXPANSION.md
├── CLAUDE_PROGRAMBENCH_HANDOFF.md
├── COMPANION_CLOAK_SAFETY.md
├── COMPANION_FLOW_AI.md
├── COMPANION_MOA_MOE.md
├── COMPANION_VIBE_CODING.md
├── DOCS_AUDIT_2026-05-26.md          ← this file
├── HANDOFF_PROMPT_ANTIGRAVITY.md
├── LICENSING.md
├── MODERN_OPS_STACK.md
├── PROGRAMBENCH.md
├── PROGRAMBENCH_200_COMPLETION_MAP.md
├── PROGRAMBENCH_200_FACTORY_ROADMAP.md
├── PROGRAMBENCH_200_LOCK_PLAN.md
├── PROGRAMBENCH_AUDIT.md
├── PROGRAMBENCH_BOARD_STATUS_2026-05-22.md
├── PROGRAMBENCH_BOARD_STATUS_2026-05-25.md
├── PROGRAMBENCH_BOARD_STATUS_2026-05-26.md
├── PROGRAMBENCH_EXTERNAL_MODEL_HANDOFF.md
├── PROGRAMBENCH_FACTORY_ARCHITECTURE.md
├── PROGRAMBENCH_FULL_AUDIT.md
├── PROGRAMBENCH_HIGH_PUBLIC_BEST_TARGET_QUEUE.md
├── PROGRAMBENCH_LANGUAGE_AUDIT.md
├── PROGRAMBENCH_PAUSED_TOOL_LOCK_GAP_REPORT.md
├── PROGRAMBENCH_TWO_LEDGER_INTEGRITY.md
├── PROJECT_CLOAK.md
├── RECENT_WORK_2026_05.md
├── WHITE_PAPER.md
├── WINDOWS_EVAL_PLAYBOOK.md
├── WORLD_KILLER_PLAN.md
├── capability_audit.md
├── programbench_floor_raise_roadmap.md
└── programbench_session_handoff_20260523.md
```
34 files.

### After (proposed)
```
docs/
├── ARCHITECTURE.md                              (foundation, updated)
├── AUDIT_IDE_TECH_DEBT.md                       (re-audit; replace contents)
├── BENCHMARK_EXPANSION.md                       (forward plan, refresh numbers)
├── COMPANION_CLOAK_SAFETY.md
├── COMPANION_FLOW_AI.md
├── COMPANION_MOA_MOE.md
├── COMPANION_VIBE_CODING.md
├── DOCS_AUDIT_2026-05-26.md                     (this file)
├── LICENSING.md
├── MODERN_OPS_STACK.md
├── PROGRAMBENCH.md                              ← merge factory_roadmap §Phase 2 here
├── PROGRAMBENCH_BOARD_STATUS_2026-05-26.md      ← canonical current
├── PROGRAMBENCH_FACTORY_ARCHITECTURE.md         ← merge two_ledger_integrity + language_audit
├── PROJECT_CLOAK.md                             (foundation, validate)
├── WHITE_PAPER.md                               (lead; update abstract + add patterns section)
├── WINDOWS_EVAL_PLAYBOOK.md
├── capability_audit.md                          (refresh numbers)
├── _archive/
│   ├── PROGRAMBENCH_200_COMPLETION_MAP.md
│   ├── PROGRAMBENCH_200_FACTORY_ROADMAP.md      (after extracting Phase 2 into PROGRAMBENCH.md)
│   ├── PROGRAMBENCH_200_LOCK_PLAN.md
│   ├── PROGRAMBENCH_AUDIT.md
│   ├── PROGRAMBENCH_BOARD_STATUS_2026-05-22.md
│   ├── PROGRAMBENCH_BOARD_STATUS_2026-05-25.md
│   ├── PROGRAMBENCH_FULL_AUDIT.md
│   ├── PROGRAMBENCH_HIGH_PUBLIC_BEST_TARGET_QUEUE.md
│   ├── PROGRAMBENCH_LANGUAGE_AUDIT.md           (after merge into FACTORY_ARCHITECTURE)
│   ├── PROGRAMBENCH_PAUSED_TOOL_LOCK_GAP_REPORT.md
│   ├── PROGRAMBENCH_TWO_LEDGER_INTEGRITY.md     (after merge)
│   ├── RECENT_WORK_2026_05.md
│   ├── WORLD_KILLER_PLAN.md                     (if split into PB + SWE done)
│   └── programbench_floor_raise_roadmap.md
└── _handoffs/
    ├── CLAUDE_PROGRAMBENCH_HANDOFF.md
    ├── HANDOFF_PROMPT_ANTIGRAVITY.md
    ├── PROGRAMBENCH_EXTERNAL_MODEL_HANDOFF.md
    └── programbench_session_handoff_20260523.md
```
**17 top-level docs (down from 34)**, plus `_archive/` and `_handoffs/` for history.

---

## 7. Recommended action sequence (low → high effort)

### Quick wins (≤ 1 hour total)

1. **`mkdir docs/_archive docs/_handoffs`**, move the 18 archive/handoff files. Pure file moves, no content changes.
2. **Delete `PROGRAMBENCH_200_LOCK_PLAN.md`, `PROGRAMBENCH_200_COMPLETION_MAP.md`, `PROGRAMBENCH_HIGH_PUBLIC_BEST_TARGET_QUEUE.md`, `programbench_floor_raise_roadmap.md`, `PROGRAMBENCH_AUDIT.md`, `PROGRAMBENCH_FULL_AUDIT.md`.** All superseded; nothing in them isn't captured in `PROGRAMBENCH_BOARD_STATUS_2026-05-26.md`.

### Medium effort (~2-3 hours)

3. **Merge `PROGRAMBENCH_TWO_LEDGER_INTEGRITY.md` + `PROGRAMBENCH_LANGUAGE_AUDIT.md` into `PROGRAMBENCH_FACTORY_ARCHITECTURE.md`.** Both are sub-topics of factory architecture.
4. **Extract Phase 2 roadmap from `PROGRAMBENCH_200_FACTORY_ROADMAP.md` into `PROGRAMBENCH.md`** as a `## Phase 2` section. Archive the source.

### High effort (~1 day)

5. **Update WHITE_PAPER.md abstract + Section 7 (Results) + Section 8 (A Better Benchmark)** with 5-26 numbers and the 8-pattern catalog. This is the most visible change and the one that matters for any external review.
6. **Re-audit `AUDIT_IDE_TECH_DEBT.md` and `capability_audit.md`** — both are 3 weeks old, codebase has substantially changed.

---

## 8. What's missing from docs/ that should exist

Tracked gaps based on what was learned this week:

| Topic | Why missing matters | Recommended new file |
|---|---|---|
| **Reusable fixture-compat patterns catalog** | The 8 patterns (slug-hash, argv[0] rename, etc.) are scattered through the 5-26 board status doc and `corpus/programbench/locked/<tool>/lessons.md.stub` stubs. They deserve a single catalog. | `docs/PROGRAMBENCH_LOCK_PATTERNS.md` |
| **`programbench-compiled` image cache invalidation** | Blocking ~3 known tools (pingu, goimports-reviser, possibly more). Mechanism not documented. | Section in `PROGRAMBENCH_FACTORY_ARCHITECTURE.md` |
| **Hetzner shard pool runbook** | 27 shards drained this week, but the pool-watch / pull / gate / apply flow lives only in `scripts/pb_hetzner_pool.py` and ad-hoc commit messages. | Section in `MODERN_OPS_STACK.md` |
| **Path to 100 locks (Phase 2 roadmap)** | The 53 → 100 plan is implicit in the board status doc but should be a stand-alone planning section. | New `## Phase 2` section in `PROGRAMBENCH.md` |

---

## Summary recommendations

1. **Update WHITE_PAPER.md abstract + Section 8 numbers** — most visible stale claim in the entire docs/ tree.
2. **Consolidate 18 ProgramBench docs → 3 canonical surfaces** (PROGRAMBENCH, BOARD_STATUS_<date>, FACTORY_ARCHITECTURE).
3. **Create `docs/_archive/` and `docs/_handoffs/`**, move ~14 superseded/historical files there.
4. **Author a `PROGRAMBENCH_LOCK_PATTERNS.md` catalog** of the 8 reusable techniques; cite from white paper Section 8.
5. **Re-run the IDE tech-debt + capability audits** (both 5-18, well past the codebase's current shape).
