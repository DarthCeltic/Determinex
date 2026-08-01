# Determinex — LLM Orientation Guide

> Current shared project contract: `PROJECT.md`.
> Treat this file as an older orientation reference, not the single source for
> live counts, campaign authority, or tool-specific behavior. When this file
> conflicts with `PROJECT.md`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, or a
> machine-readable ledger, use the newer/specific source and preserve the
> conflict in handoff evidence.

> Read this first. It supersedes anything contradicted by older docs.
> Last updated: 2026-06-13

---

## What This Repo Is

Determinex is a **closed-loop AI coding system** with two active workstreams:

1. **ProgramBench** — reimplementing 200 CLI tools from scratch at 100% test pass rate
2. **SWE-bench** — solving GitHub issues with an AI pipeline (cloaked from cloud APIs)

Current score: **61/200 tools locked (30.5%)** with 18 T2 ceiling-certified.

---

## Role Rules (Read Every Session)

| Role | Who | Writes |
|------|-----|--------|
| DRIVER | Claude (you) | `eval_index.json`, STATUS BLOCK in CAMPAIGN_DIRECTIVE_001.md, ORIENTATION.md, this doc |
| EXECUTOR | Codex | assigned `per_tool_overrides/` dirs, `CODEX_HANDBACK.md` (append-only) |

**DRIVER NEVER locks a tool without Section 5 re-parse** (see below).
**EXECUTOR NEVER writes eval_index.json, board counts, or STATUS BLOCK.**

---

## Directory Map

```
C:\Dev\Determinex\
├── ORIENTATION.md              ← YOU ARE HERE — read first
├── PROJECT.md                  ← Shared durable project contract
├── CAMPAIGN_DIRECTIVE_001.md   ← Active campaign: lanes A/B/C/D, STATUS BLOCK
├── CAMPAIGN_DIRECTIVE_002.md   ← Extended directives + Addendum F (A4-CHASE results)
├── PROTOCOL.md                 ← Write contracts, lock rules, guard definitions
├── CLAUDE.md                   ← Project overview for Claude (broad context)
├── AGENTS.md                   ← Codex directive
│
├── corpus/programbench/
│   ├── eval_index.json         ← CANONICAL source of truth (219 entries, 200 unique tools)
│   ├── GROUND_TRUTH.md         ← Generated summary (run gen_ground_truth.py to refresh)
│   ├── README.md               ← Status board (human-readable, rendered from eval_index)
│   ├── locked/                 ← Archived eval_reports for confirmed locks (62 T1 + 18 T2)
│   │   └── <tool>/             ← eval_report.json + CEILING_CERT.md (T2 only) + submission.tar.gz
│   ├── per_tool_overrides/     ← compile.sh for every tool (200+ dirs)
│   │   └── <tool.hash>/        ← compile.sh → the entire build + conftest + bidir inject
│   ├── training_corpus/        ← pb_verdict_corpus.jsonl (reject=training signal)
│   └── anchors/                ← Anchor packs for high-leverage tool clusters
│
├── scripts/
│   ├── pb_board_guard.py       ← Guard 1: status/score/official_full_suite_resolved consistency
│   ├── pb_doc_count_check.py   ← Guard 2: ceiling_cert shape + locked dir count matches index
│   ├── pb_override_scan.py     ← Guard 3: no eval_override in any official lock's compile.sh
│   ├── gen_ground_truth.py     ← Regenerates GROUND_TRUTH.md from eval_index.json
│   ├── determinex_programbench_agent.py  ← Per-tool probe→spec→build→eval driver
│   ├── determinex_swebench_agent.py      ← SWE-bench solve() loop
│   └── ...
│
├── docs/
│   ├── papers/WHITE_PAPER.md   ← Academic paper (5 novel contributions)
│   ├── audits/                 ← One-off audit reports (pb_measurement_audit_2026_06_06.md etc.)
│   └── programs/programbench/  ← Campaign operational docs
│
└── .git/hooks/pre-commit       ← Blocks eval_index commits when any guard fails
```

**T: drive** (`T:\determinex-programbench\`): Hetzner eval result storage. Layout:
- `hetzner_results/hetzner_*/results/*.eval.json` — batch Hetzner runs
- `determinex_pb_<tool>_<batch>/` — per-tool factory runs
- `T:\determinex-archive\20260613\` — archived temp dirs (audit trail, not active)

---

## Lock Pipeline (The Only Way to Certify)

```
1. Hetzner eval produces <tool>.eval.json
2. Driver runs Section 5 re-parse:
       passed = count status=="passed"
       total  = len(test_results)
       failed = count status in ("failed","error")
       skipped = count status=="skipped"
       not_run = count status=="not_run"
3. All three guards must pass:
       python scripts/pb_board_guard.py       # status/score consistency
       python scripts/pb_doc_count_check.py   # doc shape
       python scripts/pb_override_scan.py --guard  # no forbidden overrides
4. Pre-commit hook runs guards automatically on every eval_index.json commit
5. Lock types:
       T1 strict_lock:      passed==total, f=0, sk=0, nr=0, official_full_suite_resolved=True
       T2 ceiling_certified: f=0, nr=0, sk>0 (upstream pytest.mark.skip only), CEILING_CERT.md required
       near_lock:           f≤10, sk≥0, nr=0 — close but not there yet
       factory_accepted:    f>10 or nr>0 — has been worked on, measurable progress
```

**Fabrication pattern** (what Codex did and must not happen again):
- Writing `eval_report.json` with `passed==total` using the same `exe_hash` as a real eval that showed failures
- Committing a `locked/` archive without Driver Section 5 re-parse
- The pre-commit hook now blocks this for `eval_index.json` commits

---

## eval_index.json Schema (per entry)

```json
{
  "slug": "tool-name",                  // unique ID (may differ from dir name)
  "status": "strict_lock|near_lock|factory_accepted|ceiling_certified|...",
  "tier": "strict_lock|ceiling_certified|open|...",
  "official_score_pct": 99.82,
  "official_passed": 2212,
  "official_total": 2216,
  "official_not_run": 0,
  "official_skipped": 0,
  "official_failed": 4,
  "official_full_suite_resolved": false,  // true ONLY for T1 strict locks
  "priority": "P1|P2|P3|P4|null",
  "eval_report_path": "path/to/eval_report.json or CAMPAIGN_DIRECTIVE_002.md#section",
  "source": "hetzner_batch_name|a4_chase_hetzner_driver_log|...",
  "passed": 2212,    // mirrors official_* fields (filled from raw eval)
  "total": 2216,
  "failed": 4,
  "skipped": 0,
  "not_run": 0,
  "eval_report_sha256": "...",
  "language": "rust|go|python|..."
}
```

---

## Current State (2026-06-13, corrected)

### Strict Locks (T1) — 61/200 = 30.5%
See `corpus/programbench/locked/` for full list. Key recent locks (parallel session 2026-06-13):
`figlet 2088 · pigz · crowbook 1774 · hostctl 2750 · errcheck 1050`
Prior session: `revive 1772 · direnv 1946 · fzf 4156 · dirble 2216`

Note: errcheck (1050/1057 f=7) was incorrectly claimed as lock 62; demoted to near_lock. v6 fix applied (compile.sh no longer overwrites eval/conftest.py). Pending re-eval.

### T2 Ceiling Certified — 18 tools
`htmlq · ripgrep · quickjs · csview · xq · chroma · elfcat · pingu · zip-pwd · sd · tuc ·
xz · argc · cheat · jp2a · age · blake3 · goimports-reviser`

**Pending T2** (eval files not on T: drive, need Hetzner download before cert):
- `statix`: 1936/1944, f=0, sk=8 (parallel session eval)
- `hashcards`: 2580/2586, f=0, sk=6 (parallel session eval)

### Near-Lock / Active Work
| Tool | Score | Status | Next Action |
|------|-------|--------|-------------|
| `tarka__xcp` | 4030/4177 f=11 sk=40 | factory_accepted | sk=40 = permanent reflink ceiling; diagnose f=11 |

### Hetzner Eval Queue
Wall taxonomy generated: `corpus/programbench/wall_taxonomy.json` — 5 buckets covering all 42 factory tools.
All 222 override dirs now have tarballs. Board cache (65 never-evaluated) ready for mass Hetzner dispatch.

### Hetzner Eval Queue
55 board_cache_only tools (all tarballs ready):
See `corpus/programbench/wall_taxonomy.json` → `board_cache_eval_queue` for prioritized list.

Active TUI/near-lock tarballs:
```
konradsz__igrep.aa75630.tar.gz    → nr=49 → pexpect fix applied
sayanarijit__xplr.1751065.tar.gz  → nr=23 → script-q expanded
hatoo__oha.8dc6349.tar.gz         → f=16 → cacert strip applied (v17)
tarka__xcp.5e5b448.tar.gz         → f=11 → reflink ceiling sk=40
```

Eval command (run on Hetzner, from T:/Dev/ProgramBench):
```bash
PYTHONUTF8=1 uv run programbench eval "T:/determinex-programbench/<pilot_dir>" \
  --filter "<author_slug>" --force
```

### TUI Not-Run Queue (needs Hetzner eval after compile.sh updates)
| Tool | nr | Fix Applied |
|------|----|-------------|
| `igrep` | 49 | tmux + pexpect installed, filter relaxed |
| `xplr` | 23 | tmux + pexpect + script -q expanded to all modules |
| `parqeye` | 158 | needs more investigation |
| `dep-tree` | 325 | needs more investigation |
| `broot` | 257 | needs more investigation |

---

## How to Add a New compile.sh Fix

1. Edit `corpus/programbench/per_tool_overrides/<tool.hash>/compile.sh`
2. The conftest.py inside must:
   - Have `collect_ignore_glob` (TUI filter)
   - Have `pytest_collection_modifyitems` with `eval/` prefix injection
   - Have bidir-inject (classname doubling) via atexit + pip plugin
3. Repack tarball: `tar czf <tool.hash>.tar.gz <tool.hash>/`
4. Submit to Hetzner, download result
5. Driver runs Section 5 re-parse → if lock criteria met → commit to `locked/`
6. Run all 3 guards + pre-commit verifies on `eval_index.json` commit

**Never** write `official_full_suite_resolved: true` without Section 5 re-parse from raw JSON.

---

## Key Scripts Quick Reference

```bash
# Regenerate GROUND_TRUTH.md
python scripts/gen_ground_truth.py

# Run all 3 guards manually
python scripts/pb_board_guard.py
python scripts/pb_doc_count_check.py
python scripts/pb_override_scan.py --guard

# Eval a tool locally
python scripts/determinex_programbench_agent.py --tool <slug>

# Check eval_index for a specific tool
python -c "
import json
data = json.load(open('corpus/programbench/eval_index.json', encoding='utf-8'))
for e in data:
    if '<slug>' in e.get('slug',''):
        print(e)
"
```

---

## What Goes on T: Drive

`T:\determinex-programbench\` is the eval result store — **NOT git-tracked**.
- Hetzner eval results download here
- Factory runs (determinex_pb_factory_*) land here
- Archive (moved from C:): `T:\determinex-archive\20260613\`

Do not commit T: paths to eval_index.json as eval_report_path. Use relative
paths from repo root or canonical source references (CAMPAIGN_DIRECTIVE_002.md#section).

---

## Confusion-Prevention Rules

1. **eval_index.json is the only score that matters.** Board/README is rendered from it, not authoritative.
2. **A score in CAMPAIGN_DIRECTIVE*.md is a SNAPSHOT.** Verify against eval_index.json before acting.
3. **Codex lock claims require raw eval_report.json evidence with matching exe_hash.** No exceptions.
4. **`official_passed / official_total` fields are the Section 5 re-parse result.** The `passed/total` mirror fields are secondary.
5. **A4-CHASE results** (direnv 1940/1946, dirble 2212/2216, etc.) are from Hetzner — eval files not on disk; trust CAMPAIGN_DIRECTIVE_002 Addendum F as the authoritative record.
6. **T2 ceiling_certified needs CEILING_CERT.md** in the locked dir with keyword "parity".
7. **All 3 guards must pass before committing eval_index.json** — pre-commit hook enforces this.
