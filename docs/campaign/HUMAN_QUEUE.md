# DETERMINEX — Human Queue

> Items awaiting Ryan's decision or action. Each block: what it is, why it matters,
> exact decision needed, date queued, cycle age.
> Agents cannot unblock these. They are surfaced here so Ryan can see them.
> Items >3 cycles old get ESCALATED flag.

---

## HQ-001 — Materials Pack Review
**Queued**: 2026-06-11 (Cycle 5)
**What it is**: Three draft docs for public-facing launch materials:
- `docs/materials/demo_script.md` — 3-minute demo storyboard
- `docs/materials/social_pack.md` — 10 social posts with receipts + screenshot specs
- `docs/materials/screenshot_specs.md` — exact capture specs for 10 receipt screenshots
**Why it matters**: The Sovereignty Surfacing Standard (PROTOCOL.md Section 13) requires
Ryan's approval before any materials ship. These are drafts — agents cannot post.
**Decision needed**: Review each doc. Approve to publish, or redirect with changes.
**Note**: Numbers (53 strict locks, 1,813,760 identifiers) must be rechecked at post time.
Screenshots must be fresh captures, not recycled.

---

## HQ-002 — Training-Eligibility Batch Approval
**Queued**: 2026-06-11 (Cycle 5)
**What it is**: Section 12(e) requires operator approval before any compiler-verified
(fail→fix) pairs are marked `training_eligible=true`. The verdict corpus
(`pb_verdict_corpus.jsonl`) currently has entries flagged for review.
**Why it matters**: These pairs ARE the flywheel — they teach the next model. But training
on bad data is worse than no training. Every batch needs a human sign-off before it goes
into the training queue.
**Decision needed**:
1. Review `corpus/programbench/training_corpus/pb_verdict_corpus.jsonl` (gitignored-local)
2. Set `training_eligible: true` on batches that meet your bar, or add rejection notes
3. Tell driver to set the flag; driver never sets it autonomously
**Current batch**: 7 rows from v4 cycle bounces (fzf/ov/fasttext/bartib/age/bat/ast-grep)

---

## HQ-003 — Verdict Corpus Backup Decision
**Queued**: 2026-06-11 (Cycle 5)
**What it is**: `corpus/programbench/training_corpus/pb_verdict_corpus.jsonl` is gitignored
(local-only). A flywheel asset with zero backup is a single disk failure from gone.
**Why it matters**: The verdict corpus IS the training signal. If lost, all campaign work
since it was created is gone from the model perspective.
**Decision needed**: Choose one:
A. **Un-gitignore and commit** — simplest, but training data enters the public repo
B. **Encrypt and commit** — keeps data but adds complexity
C. **Backup to T: drive** — copy to T:\determinex-training-backup\ after every cycle (driver automates)
D. **Gitignore but add to STORAGE_OPERATIONS.md backup protocol** — explicit manual backup reminder
**Driver recommendation**: Option C — automatic copy to T: after every cycle, no repo change.

---

## HQ-004 — Parity Publish Decision (First Bank)
**Queued**: 2026-06-11 (Cycle 5)
**What it is**: 11 parity candidates (htmlq, ripgrep, xq, csview, quickjs, chroma, sd,
dsq, tuc, elfcat, zip-password-finder) are all "upstream-skip-only" gaps. Pingu will be
the first Tier A parity artifact (3 unconditional `@pytest.mark.skip("Too slow")` decorators).
Once pingu's reference-diff artifact is archived, published parity count goes from 0 → 1.
**Why it matters**: The board shows "parity: 0 published" which understates what we've
achieved. Getting to 1 published parity breaks the 0-artifacts streak.
**Decision needed**: Approve publication of Tier A parity (pingu) once reference-diff
artifact is archived. Driver will ask for approval at that point.
**Note**: Tier B (ripgrep xdist cascade skips) requires a reference run first — driver
will commission that in cycle 6.

---

## HQ-005 — SWE-bench Cloak Rerun Launch
**Queued**: 2026-06-11 (Cycle 5)
**What it is**: B-Uncloaked and E-RegionControl SWE-bench reruns are needed to get
publication-grade privacy-cost delta numbers. Currently all cloaked configs are lower bounds.
**Why it matters**: The headline claim "R-Y = actual cost of sovereignty" requires both B-Uncloaked
and E-RegionControl to run cleanly (no disk-full errors). Current B-Uncloaked is 14.0% audited.
**Decision needed**: Authorize overnight Hetzner SWE-bench run (B-Uncloaked first, then E-RegionControl)
once ProgramBench lock evals are complete. Runs require ~$10-20 of Hetzner compute time.
**Blockers**: Hetzner is currently saturated with ProgramBench evals (CODEX-002 + ROLLING-001).
Driver will request window when Hetzner is clear.

---

## HQ-006 — Patent Filing Status
**Queued**: 2026-06-10 (Cycle 1) — **CARRIED FORWARD**
**What it is**: Patent provisional filing for Fleet Learning Architecture + Project Cloak
+ Rosetta Stone. Six claims documented in `project_fleet_learning.md` memory.
**Why it matters**: Public release without filed provisional = public disclosure bars future
filing. Timeline: file BEFORE public GitHub release.
**Decision needed**: File provisional or set explicit "won't file" decision so agents know
not to delay public release on this account.
**Current status**: Not filed as of 2026-06-10.

---

## REPORT: Queue Status

| ID | Item | Queued | Cycles | Status |
|----|------|--------|--------|--------|
| HQ-001 | Materials Pack Review | 2026-06-11 | 1 | Awaiting Ryan |
| HQ-002 | Training-Eligibility Approval | 2026-06-11 | 1 | Awaiting Ryan |
| HQ-003 | Verdict Corpus Backup Decision | 2026-06-11 | 1 | Awaiting Ryan |
| HQ-004 | Parity Publish Decision | 2026-06-11 | 1 | Awaiting Ryan (after pingu artifacts) |
| HQ-005 | SWE-bench Cloak Rerun | 2026-06-11 | 1 | Awaiting Ryan approval + Hetzner window |
| HQ-006 | Patent Filing Status | 2026-06-10 | 2 | **ESCALATED** (>1 cycle) |

Items reaching 3 cycles get an ESCALATED header in the Section 11 report.
