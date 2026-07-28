# Determinex — Screenshot Specifications

> **Status**: Draft for Ryan's review. Agents draft; Ryan captures and publishes.
> Conform to docs/policy/SOVEREIGNTY_SURFACING_STANDARD.md.
> Every screenshot must show a live, current artifact — no mocked or stale data.

---

## SS-01 — Strict Lock Count (eval_index)

**Purpose**: Receipt for benchmark claim (53 strict locks)
**File to capture**: Terminal output
**Command**:
```bash
python3 -c "
import json
with open('corpus/programbench/eval_index.json', encoding='utf-8') as f:
    d = json.load(f)
strict = [v for v in d if v.get('official_full_suite_resolved')]
print(f'Strict locks: {len(strict)} / 200')
for v in strict[:10]: print(f\"  {v['slug']}\")
print('  ...')
"
```
**What must be visible**: The count (`Strict locks: 50 / 200`) and at least 10 tool names.
**When to recapture**: After every new lock archival.

---

## SS-02 — Guard Green (doc-guard + override scan)

**Purpose**: Receipt that published numbers are machine-verified
**Commands** (run sequentially, capture combined output):
```bash
python scripts/pb_override_scan.py --guard
just doc-guard
```
**What must be visible**: Both commands exit 0, "0 violations" visible on screen.
**When to recapture**: Before every public materials release.

---

## SS-03 — Cloak Audit PASSED

**Purpose**: Receipt for 1,813,760 identifiers audited, 0 leaks
**File to capture**: `logs/cloak_audit/` — most recent audit log's verdict line
**Command**:
```bash
python scripts/verify_cloak.py --audit-log logs/cloak_audit/<most_recent>.jsonl
```
**Expected output**:
```
VERDICT: CLEAN — 1,813,760 identifiers audited, 0 restoration failures, 0 privacy leaks
```
**What must be visible**: The VERDICT line, the identifier count, "0 privacy leaks."
**Note**: This requires a fresh `DETERMINEX_CLOAK_AUDIT=1` SWE-bench run to update.
Current receipt: B-Cloaked-RosettaOFF run (see WHITE_PAPER.md §SWE-bench Ablation).

---

## SS-04 — Cloak Side-by-Side (obfuscation visible)

**Purpose**: Demonstrate what Project Cloak does visually
**Setup**: Run a cloaked task with `DETERMINEX_CLOAK=1 DETERMINEX_CLOAK_AUDIT=1` and capture the prompt log.
**Layout**: Split screen (or two separate captures):
- Left panel: Real source code (e.g., `astropy/astropy`) showing real identifier names
- Right panel: The obfuscated prompt sent to cloud AI (`x_0070`, `x_0177`, etc.)
**What must be visible**:
- At least 5 real identifier names on the left
- The same positions showing opaque tokens on the right
- No real identifier names visible in the right panel
**Source file**: Any recent `logs/cloak_audit/` request log entry.

---

## SS-05 — Measurement Audit Document

**Purpose**: Receipt for the self-correction story (77 → 15 → 50)
**File to capture**: `docs/audits/pb_measurement_audit_2026_06_06.md` in editor
**What must be visible**:
- Document title and date (June 6, 2026)
- The headline correction: "77 'locks' → 16 genuine full-suite locks" (or equivalent language)
- Git timestamp (run `git log --oneline docs/audits/pb_measurement_audit_2026_06_06.md`)
**Note**: Capture the git log alongside the doc to prove it's committed history, not edited after-the-fact.

---

## SS-06 — Attribution Log (provenance)

**Purpose**: Receipt for provenance attribution
**File to capture**: `logs/copyright_guard/attribution.jsonl` — last 10 entries
**Command**:
```bash
tail -10 logs/copyright_guard/attribution.jsonl | python3 -m json.tool
```
**What must be visible**: At least 5 entries with `slug`, `source`, `license`, `match_type` fields visible.
**Note**: Attribution log is only populated after running with `determinex_copyright_guard.py --mode observe`.
Run a build session first to generate entries.

---

## SS-07 — Origin Record (git timeline)

**Purpose**: Receipt for April 9-12, 2026 inception claim
**Command**:
```bash
git log --format="%H %ai %s" docs/papers/ARCHITECTURE.md | tail -5
git log --format="%H %ai %s" | grep -E "2026-04-0[9]|2026-04-1[012]" | head -10
```
**What must be visible**:
- Commits dated April 9-12, 2026
- Commit messages showing progression from inception to prototype
- Author: Test (Ryan's git identity)

---

## SS-08 — Eval Report (a single locked tool)

**Purpose**: Receipt for compiler-verified corpus claim
**File to capture**: Any locked tool's eval_report.json
**Suggested tool**: `grex` (3036/3036 — clean, impressive count)
**Command**:
```bash
python3 -c "
import json
with open('corpus/programbench/locked/grex/eval_report.json', encoding='utf-8') as f:
    d = json.load(f)
results = d if isinstance(d, list) else d.get('test_results', [])
passed = sum(1 for r in results if r.get('status') == 'passed')
total = len(results)
print(f'grex: {passed}/{total} — passed=={total}: {passed==total}')
"
```
**What must be visible**: `passed==total` is True, the total count (e.g., 3036/3036).

---

## SS-09 — Proof Center Panel (Tauri app)

**Purpose**: Product screenshot showing provenance in the UI
**Setup**: Launch Tauri app (`cd frontend && npm run tauri dev`), navigate to Proof Center panel (`/proof-center`)
**What must be visible**:
- Attribution entries rendered in the UI
- At least one entry with source + license visible
- The panel heading ("Proof Center" or equivalent)
**Note**: This requires Tauri frontend to be functional and connected to attribution.jsonl.

---

## SS-10 — ProgramBench Leaderboard Context

**Purpose**: Context for benchmark performance claim
**Source**: BenchLM or ProgramBench leaderboard (external — Ryan navigates to it)
**What must be visible**: Other models' scores (0–0.5% range) vs Determinex's count
**Note**: Driver/Codex cannot access external URLs to verify leaderboard state. Ryan must capture this screenshot directly. Do NOT generate or embed a URL — navigate to the leaderboard manually.

---

## Capture Standards

- Terminal font: JetBrains Mono or Consolas, minimum 14pt
- Terminal theme: dark (Dracula, One Dark, or similar)
- No personal info visible (home directory paths, usernames other than the git identity)
- Timestamps must match claimed dates — do not use pre-captured screenshots for claims about current state
- Resolution: 1920×1080 minimum; 2560×1440 preferred for readability
