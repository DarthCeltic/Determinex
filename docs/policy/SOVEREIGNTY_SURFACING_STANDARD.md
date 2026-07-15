# Determinex — Sovereignty Surfacing Standard

> **Version**: 1.0 — 2026-06-11
> **Authority**: Driver (Claude). Any agent output that constitutes a public-facing claim
> must conform to this document or it bounces — same enforcement as a failed compile gate.
> **Scope**: Docs, demos, UI copy, screenshots, video scripts, social posts, code comments
> that will appear in public-facing materials.

---

## 1. The Canonical One-Liner

> **"Your code never leaves in the clear. Nothing unverified ever gets in. Receipts for both."**

This sentence is verbatim everywhere it appears. No paraphrasing. No synonym substitution.
When the one-liner is used, both clauses travel together — never split.

### Two-sentence version (for section intros and slide subtitles):
> Determinex obfuscates your entire codebase before any cloud AI call — every private identifier
> maps to an opaque token, and the AI never sees the real names. Every training sample that
> enters the corpus has been validated by a real compiler, not an LLM judge.

### One-paragraph version (for press, README, about pages):
> Determinex is a local-first AI coding system built on two commitments: sovereignty out and
> integrity in. Before any cloud AI interaction, Project Cloak maps every proprietary
> identifier — every function name, class name, variable — to an opaque token. The AI solves
> your problem without ever seeing your code's real structure. On the other side, nothing
> enters Determinex's training corpus without first passing a real compiler — rustc, go build,
> tsc, gcc — which provides the deterministic ground truth that LLM judges cannot. Both
> properties are auditable: the Cloak audit log captures every API request; the corpus
> carries compiler-verified provenance for every sample. The receipts exist. You can check them.

---

## 2. The Receipt Set (Approved Proof Points)

**Rule**: A claim that cannot point to an artifact below does not ship.
Numbers are derived from eval_index.json + audit logs at claim time. Never hand-type.

### Receipt 1 — Benchmark performance (ProgramBench)
| Claim | Artifact | How to verify |
|-------|----------|---------------|
| **{N} tool reimplementations fully resolved** (strict) | `corpus/programbench/eval_index.json` → entries with `official_full_suite_resolved: true` | `python scripts/pb_board_guard.py` — 0 violations required |
| **{M} reference-parity** (parity) | Same file → entries with `parity_verified: true` | Count only after reference-diff artifact archived |

> Current verified count (2026-06-11): **47 strict / 0 parity published**
> Update at every cycle by re-running `python scripts/pb_board_guard.py`.
> doc-guard (`just doc-guard`) must be green before any doc containing these numbers ships.

**Scope qualifier (always attached):**
> "Determinex resolved {N} of 200 CLI tools in ProgramBench's official metric (passed==total,
> zero not_run tests). This is a tool-count, not a task-point percentage. Each resolved tool
> passed every test in its test suite, including all branches."

### Receipt 2 — Privacy sovereignty (Project Cloak)
| Claim | Artifact | How to verify |
|-------|----------|---------------|
| **1,813,760 identifiers audited, 0 leaks** | `logs/cloak_audit/` (run with `DETERMINEX_CLOAK_AUDIT=1`) | `python scripts/verify_cloak.py` → PASSED verdict |

> Source: B-Cloaked-RosettaOFF SWE-bench run. Publishable proof requires a fresh `DETERMINEX_CLOAK_AUDIT=1` run and a `verify_cloak.py PASSED` verdict. Do not cite the number without the associated audit path.

**Scope qualifier (always attached):**
> "Audited across {N} SWE-bench instances in the B-Cloaked-RosettaOFF ablation run.
> The audit log is at `logs/cloak_audit/`. Independent verification: extract the log,
> run `scripts/verify_cloak.py --audit-log <path>`, confirm PASSED verdict."

### Receipt 3 — Corpus integrity (Compiler Oracle)
| Claim | Artifact | How to verify |
|-------|----------|---------------|
| **Every training sample compiler-verified** | `corpus/programbench/locked/*/eval_report.json` | Each locked tool's eval_report shows passed==total, 0 not_run |
| **Provenance attribution log** | `logs/copyright_guard/attribution.jsonl` | Run `python scripts/determinex_copyright_guard.py --mode observe` |

**Scope qualifier:**
> "Compiler verification applies to the ProgramBench training corpus (CLI reimplementation tasks).
> The Compiler Oracle is the deterministic judge — not an LLM, not a rubric."

### Receipt 4 — Self-correction and honesty (Measurement audit)
| Claim | Artifact | How to verify |
|-------|----------|---------------|
| **June 6 audit corrected 77→15→47** | `docs/audits/pb_measurement_audit_2026_06_06.md` | Audit doc is timestamped, public, in git history |

> The self-correction story: early metric (passed/runnable, excluding not_run) diverged from
> the official ProgramBench metric (passed/total, counting not_run). We caught it, published
> the discrepancy, corrected the count, and built a guard (`pb_override_scan.py --guard`) that
> prevents the same mistake from recurring. This is the strongest credibility asset.

**Scope qualifier:**
> "The June 2026 measurement audit reduced our claimed count from 77 to 15 (current: 47 after
> continued work). The audit doc is committed to the repository. The automated guard is part
> of every lock-archival checklist."

### Receipt 5 — Origin record (73-hour inception)
| Claim | Artifact | How to verify |
|-------|----------|---------------|
| **April 9-12, 2026: inception to full prototype** | `docs/papers/ARCHITECTURE.md` (git timeline section) | `git log --format="%H %ai %s" docs/papers/ARCHITECTURE.md` |

> "One developer. Lincolnton, NC. Third-year student. Consumer GPU (GTX 1660 Ti).
> The commit history is the receipt."

---

## 3. Scope Qualifiers (Always Travel with Claims)

These three qualifiers ship with every published number. No exceptions.

1. **Provenance qualifier**: "Provenance is checked against {N} registered reference sources
   (academic papers, open-source libraries, patents). Attribution tags are written to
   `logs/copyright_guard/attribution.jsonl` when matches are detected."

2. **Benchmark qualifier**: "Benchmark results are tool counts under ProgramBench's official
   metric, not a general coding-ability claim. The tool count and the methodology are the
   claim — not 'best in class' or 'state of the art' without supporting evidence."

3. **Product qualifier**: "Benchmark results are not product support. ProgramBench performance
   measures training-corpus quality and the eval-in-loop architecture, not production-grade
   tool generation for arbitrary inputs."

---

## 4. Narrative Frame (Human-Authored Materials Only)

The narrative below is for Ryan's use in social posts, video scripts, and press.
Agents draft; Ryan publishes. Agents never post autonomously.

**Verifiable facts (state these; do not embellish):**
- Solo developer, Lincolnton, NC
- Third-year university student (concurrent with development)
- Consumer GPU: GTX 1660 Ti 6GB VRAM
- Development commenced April 9, 2026 (git timeline)
- Working multi-agent prototype in 73 hours
- All benchmark claims are backed by publicly verifiable artifacts

**The self-correction story** (most disarming credibility asset):
> We counted 77 locks. Then we found the measurement bug — our metric excluded not_run tests.
> We ran the audit, published the discrepancy, corrected the count to 15, and built a guard
> that makes the same mistake impossible in future. Current honest count: 47.
> The audit doc is in the repo. The guard is in CI. We didn't hide it.

**Forbidden adjectives** (require evidence path or get cut):
- "best" → requires comparative study with documented methodology
- "first" → requires prior-art search with sources
- "only" → requires exhaustive search with documented scope
- "state of the art" → requires citation of the art being compared against

---

## 5. Enforcement

**Claim scanner** (`scripts/pb_override_scan.py --guard` + `just doc-guard`):
- Enforces number consistency (tool counts must match eval_index)
- Runs automatically before any lock archive
- MUST be green before public materials ship

**Section 13 of PROTOCOL.md** extends the claim scanner to marketing copy:
- One-liner verbatim check (when used)
- Scope qualifiers present (tool counts have qualifiers attached)
- Numbers eval_index-derived (no hand-typed counts)
- No unverifiable superlatives without evidence path

**Bounce rule**: Any agent output (report, README section, demo script, UI copy, social draft,
storyboard) that fails the surfacing standard bounces to revision. Same severity as a failed
compile gate. No exceptions for "it's just a draft."

---

## 6. Living Document

Update this document when:
- A new receipt artifact is established (new audit type, new benchmark)
- A scope qualifier needs refinement (new edge case discovered)
- The canonical one-liner is refined (requires Ryan's sign-off — driver cannot change unilaterally)
- A new forbidden adjective is identified

Do not update benchmark numbers inline — those come from eval_index at claim time.
