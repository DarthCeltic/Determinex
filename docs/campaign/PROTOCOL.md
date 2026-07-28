# DETERMINEX DUAL-AGENT CAMPAIGN PROTOCOL v2
# Canonical. Both agents read this file at session start. Repo: C:\Dev\Determinex.
# Benchmark: T:/Dev/ProgramBench. Compiler is the ONLY oracle. Honest count only.

## 0. MISSION — the June 25 definition of done
The bar is not a lock count. The bar: every public-facing claim survives
hostile scrutiny from a skeptical, well-funded reviewer. Done means:
  1. Two public numbers — strict (passed==total, 0 not_run/skipped/failed) and
     reference-parity — published, labeled, and byte-consistent across README,
     WHITE_PAPER, and PROGRAMBENCH docs. `just doc-guard` green.

     Reference-parity (definition): the strict-lock set PLUS tools whose
     only gap to passed==total is upstream pytest.mark.skip tests the
     provided reference binary also cannot pass, each proven by an archived
     reference-diff artifact (same container, same tests). Strict ⊂
     reference-parity. Published as tool counts only. Aggregate
     runnable-test percentages are NEVER publishable (subset-metric class —
     see pb_measurement_audit_2026_06_06.md).

  2. Every strict lock passes pb_override_scan.py --guard AND pb_board_guard.py.
  3. Every claimed ceiling has archived reference-diff evidence.
  4. SWE-bench Cloak rerun imported (fresh B-Uncloaked + E-RegionControl) —
     scheduled into Hetzner idle/overnight windows, never displacing lock evals,
     never cancelled mid-config (partial runs are why the current numbers are
     lower bounds).
  5. REPRODUCTION.md exists: a stranger with Docker can verify 3 named locks
     end-to-end from archived artifacts alone.
  6. RELEASE_CHECKLIST.md current every cycle. Patent filing is HUMAN-OWNED:
     agents track its status, never block on it, never act on it.
Locks are the engine (Hetzner contention: locks win), but a lock that fails
items 1–3 under scrutiny is worth less than zero.

## 1. STATE MODEL — machine state vs human render
Machine state (canonical, CLAUDE-WRITE-ONLY):
  corpus/programbench/eval_index.json        — tool truth
  docs/campaign/campaign_assignments.json    — batch ownership
  docs/campaign/parked.json                  — parked verdicts + evidence paths
Human render (regenerated each cycle, never hand-edited as source):
  docs/campaign/DUAL_AGENT_BOARD.md          — rendered FROM the JSONs
Codex-write-only:
  docs/campaign/CODEX_HANDBACK.md            — append-only results + proposals
Nothing else is shared mutable state. Markdown is never the source of truth —
the doc-guard lesson applies to the campaign layer too.

## 2. ROLES
CLAUDE (driver): owns all machine-state writes, all archives under locked/,
  guard runs, ceiling rulings, board render, Hetzner dispatch ledger,
  RELEASE_CHECKLIST. Serializes every eval_index write.
CODEX (executor — VS Code extension on the SAME workstation): executes
  assigned batches only. Repair→build→eval, appends handbacks. NEVER writes
  eval_index, assignments, the board, or locked/ archives. NEVER edits shared
  infrastructure without an approved change request (Section 6).

## 3. OWNERSHIP — batch-scoped, replaces time leases
Claude assigns work in campaign_assignments.json:
  { "batch_id": "...", "owner": "codex", "slugs": [...],
    "issued": "...", "status": "active | handed_back | reconciled" }
One slug = one owner. Codex touches ONLY slugs in its active batch. No time
expiry — episodic agents have no clock. A batch stays open until handed back
or reclaimed by Claude at reconcile. Self-assignment is prohibited.

ROLLING QUEUE (self-claim protocol):
The driver maintains rolling_queue in campaign_assignments.json: an ordered,
pre-approved list of slugs Codex may self-claim WITHOUT waiting for a batch.
Codex claims the next ≤4 slugs by appending a CLAIM entry (slug, timestamp)
to CODEX_HANDBACK.md — its own write-only file — and the claim is valid
immediately. The driver reconciles claims into campaign_assignments.json each
cycle. Self-claiming outside the queue order, or any slug not in the queue,
remains prohibited. Archives, eval_index, and lock verdicts remain
driver-only — the queue changes who STARTS work, never who CERTIFIES it.

## 4. CLAUDE CYCLE — every session, in this order
  1. THREE-WAY RECONCILE: eval_index.json ↔ filesystem (locked/ dirs) ↔
     campaign_assignments.json. Fix and log any drift BEFORE new work.
     (The June 7 deep filesystem audit, made routine instead of heroic.)
  2. Read new CODEX_HANDBACK.md entries.
  3. VERIFY every proposed lock per Section 5. Archive or bounce with reason.
  4. Update eval_index + parked.json, render the board, update RELEASE_CHECKLIST.
  5. Assign next batch per Section 8 priorities. Log all dispatch decisions.

## 5. LOCK VERIFICATION — no archive without ALL of these
  a. eval_report.json exists at the handback path; Claude parses it DIRECTLY:
     passed == total, not_run == 0, skipped == 0, failed == 0.
  b. Tarball + compile.sh hashes recorded in the archive manifest.
  c. pb_override_scan.py --guard → 0 violations.
  d. pb_board_guard.py → 0 violations.
  e. tests.json count sanity vs eval_report total (thokr-style bidir extras
     documented explicitly when present).
A stated score in a handback is NEVER sufficient — display-100 vs true-100,
hash_executable_failed, and stale board fields all live in this repo's history.

## 6. SHARED-INFRASTRUCTURE FREEZE
Per-tool override edits: free, within your owned batch only.
Edits to anything that fans out (conftest templates, pb_eval_unified.py,
runner scripts, guard scripts, anything under scripts/ touching >1 tool):
  - Codex: file a CHANGE REQUEST in the handback (diff + affected-tool list).
  - Claude: approve only after a smoke re-eval of 3–5 existing locked tools
    passes clean, BEFORE the change reaches the board.
"Every fix breaks 2-3 tests in another suite" — now with two agents. The
freeze is the answer.

## 7. LOAD GOVERNOR — one 1660 Ti daily-driver box, two agents
COMBINED local limit: 2 concurrent evals TOTAL across both agents. Enforced by
checking campaign_assignments.json dispatch entries before any local run.
A senses/PTY diagnostic pass counts as an eval slot.
If CPU 1-min avg > 80% OR free RAM < 4GB: queue to Hetzner or wait.
If interactive use is detected (it's the daily driver): prefer Hetzner.
HETZNER: max 4 workers. Monster tools (>2000 tests) and batch campaigns go
remote. Contention: lock evals preempt; the Cloak rerun fills idle and
overnight capacity. Spin down idle shards. Log every dispatch decision.

## 8. WAVE PRIORITY
T1 — Mechanical conversions (highest EV): remaining partial_eval_100 re-evals;
  high-not_run tools (miller-class, sqlite/duckdb/php). REQUIRED first step
  per tool: run pb_senses.py (artifact-only classifier; taxonomy in script
  header); driver adjudicates unclassified rows. Fix the CLASS, then re-eval.
T2 — factory_accepted + pending_unlock: verify per Section 5 and lock.
T3 — TUI cluster: ONE reusable PTY harness (pexpect — proven on thokr #48),
  applied across the class. Pattern once, tools many.
T4 — codec/scientific tail (ffmpeg, gromacs, sox, proj): diagnostic-only.
  Classify the wall, archive ceiling evidence, do not grind.

## 9. STOP CONDITIONS & PARKING
- 3 eval cycles on one tool with no score improvement → PARK.
- Harness/image-layer walls (igrep-class: PB wipes /workspace/, task-image
  binary path breaks) → PARK with verdict "harness-gap:parked" + evidence
  path written to parked.json.
- Regression vs best (jplot-v3-class) → ship best artifact, PARK, record
  the best version's evidence path.
Parked is a FORMAL verdict. Every session reads parked.json before touching
any tool. Nothing parked is re-attempted without citing new information.

## 10. CEILING DISCIPLINE — both agents, no exceptions
A ceiling is confirmed ONLY by an archived artifact showing the REFERENCE
binary failing/skipping the SAME tests in the SAME container. Until then it
is "suspected ceiling — needs reference-diff." Never edit eval fixtures.
Never inject upstream source into the candidate. No static-RE on reference
binaries — pb_senses_guard.py enforces.

## 10a. PARITY EVIDENCE — TWO-TIER STANDARD (2026-06-11)
Tier A: unconditional @pytest.mark.skip decorator (no condition expression)
  → static artifact sufficient. The skip fires regardless of environment; a
  reference run would produce the same skip. Archive the decorator source
  line as evidence.
Tier B: runtime pytest.skip() / @pytest.mark.skipif(condition) /
  framework-cascade skip → reference run required OR documented
  binary-independence proof required. Includes: root-permission skips
  (rootuser check), environment availability skips (toolchain missing),
  pytest-dependency cascades. Binary-independence proof: demonstrate the
  reference binary also cannot pass the test (e.g., root-user test: both
  binaries fail without root, independent of binary correctness).
Classify ALL parity candidates into Tier A or Tier B before producing
artifacts. Tier B "proven by binary-independence" must be documented
explicitly in the parity archive alongside the reference-diff artifact.

## 11. CADENCE & REPORTING
Per Claude cycle, report: locks gained (verified, not proposed), ceilings
confirmed (with evidence paths), parks, dispatch decisions, and the
RELEASE_CHECKLIST delta. Honest count only. No subset metric, ever. Two
numbers, always labeled: strict and reference-parity.

## 12. CORPUS FLYWHEEL — standing duty, every cycle
(a) lessons.md: every new lock's root cause + fix → append to
    corpus/programbench/locked/<tool>/lessons.md
(b) cross-tool patterns: transferable root causes → append to
    corpus/programbench/cross_tool_patterns.md
(c) RAG reseed: after ≥3 new locks, run:
    python scripts/seed_knowledge_base.py --programbench-only --reseed-programbench
(d) verdict corpus: confirm each lock/park/ceiling in
    corpus/programbench/training_corpus/pb_verdict_corpus.jsonl
    (format: {"slug","verdict","root_cause","fix_summary","eval_date"})
(e) training queue: compiler-verified (fail→fix) pairs routed to training
    queue. training_eligible stays FALSE until operator approval.
    Flag batch for Ryan. DO NOT set training_eligible=true autonomously.
Report corpus delta in every Section 11 cycle report.

## 13. SURFACING STANDARD — public-facing artifact gate
Every public-facing artifact (report, README section, demo script, UI copy, social draft,
screenshot spec, storyboard) generated by either agent must conform to
docs/policy/SOVEREIGNTY_SURFACING_STANDARD.md before shipping. Agents draft; Ryan publishes.

Claim scanner extension (runs at lock-archive time AND before materials release):
(a) Canonical one-liner verbatim when used — no paraphrasing
(b) Scope qualifiers present on every published number (tool counts, benchmark scores,
    Cloak audit stats)
(c) Numbers eval_index-derived — `just doc-guard` must be green
(d) No unverifiable superlatives: "best"/"first"/"only"/"state of the art" require a
    documented evidence path or must be cut
(e) Receipt set intact: every claim points to an artifact path in the Receipt Set
    (SOVEREIGNTY_SURFACING_STANDARD.md Section 2)

Bounce rule: Materials that fail the surfacing standard bounce to revision at same
severity as a failed compile gate. No exceptions for "just a draft."

Priority fence: surfacing work fills cycle gaps — never displaces Sections 4-9 duties.
