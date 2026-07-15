# Storage Operations

> The disk-side runbook for Determinex: where things live, what backs them up,
> how logs rotate, and which directory is the single source of truth for
> models. Locked under `locks/sentinel/STORAGE_OPERATIONS_LOCK_001.json`.

---

## 1. Storage Topology

| Tier | Path | Purpose | Drive-letter required? |
|---|---|---|---|
| Repo | `c:/Dev/Determinex` | Source code, tests, locks, docs. Git-tracked. | No (relative). |
| T:/ data | `T:/determinex-models` | Quantized GGUF models, Rosetta MLP weights. | No — local fallback `data/models/`. |
| T:/ data | `T:/determinex_corpus` | Training corpus shards (.jsonl). | No — local fallback `corpus/`. |
| T:/ data | `T:/determinex-swebench` | Pre-cloned SWE-bench repos (zero clone overhead). | **Yes**. No fallback — external benchmark data. |
| T:/ data | `T:/determinex-programbench` | Per-tool ProgramBench build/eval output. | **Yes**. No fallback. |
| T:/ data | `T:/Dev/ProgramBench` | ProgramBench harness (`uv run programbench eval …`). | **Yes**. No fallback. |
| T:/ data | `T:/determinex-staging` | ProgramBench staging area. | No — local fallback `data/pb_staging/`. |
| T:/ data | `T:/huggingface_cache` | HF model + dataset cache. | No — local fallback `~/.cache/huggingface/`. |
| T:/ data | `T:/determinex_audit/events` | JSONL event log (observability). | No — local fallback `logs/events/`. |
| T:/ data | `T:/determinex_artifacts/quarantine` | Quarantined unpinned artifacts. | No — local fallback `data/quarantine/`. |
| T:/ data | `T:/determinex_artifacts/cache` | Pinned-artifact cache (post-policy admit). | No — local fallback `data/artifact_cache/`. |
| Local DB | `.determinex/chrono.sqlite` | Session WAL + provenance DB. | No. |
| Logs | `logs/` | Run logs, gate escalations, audit dumps. | No. |
| Assurance | `assurance/evidence/` | Signed evidence index + audit artifacts. | No. |

The single authoritative path resolver is `scripts/determinex_settings.py`. No
script may hardcode T:/ paths; all access goes through `get_settings()`. This is
enforced by `CONFIG_SPINE_LOCK_001` and `PATH_PORTABILITY_LOCK_001`.

---

## 2. Model Cache Authority

**Single source of truth: `DETERMINEX_MODELS_DIR`** (default `T:/determinex-models`,
local fallback `data/models/`).

Rules:

- `register_models.ps1` / `register_models.sh` must read `DETERMINEX_MODELS_DIR`
  from `.env` before resolving GGUF locations. No other script may register
  Ollama tags against a different path.
- Ollama's own blob store (`~/.ollama/models/` on POSIX,
  `C:\Users\<u>\.ollama\models\` on Windows) is treated as a **derived
  cache** of `DETERMINEX_MODELS_DIR`. If it fills C:\ unexpectedly, set
  `OLLAMA_MODELS=T:\OllamaModels` (do NOT use `mklink` — the auditor now
  auto-detects this on boot; see `[[project_ollama_storage]]`).
- HuggingFace cache (`HF_HOME`) is independent of `DETERMINEX_MODELS_DIR`. It
  exists for training-side downloads (Unsloth, tokenizer manifests). Never
  point inference scripts at `HF_HOME`.
- Rosetta MLP weights (`rosetta_v1.pt`) live under
  `DETERMINEX_MODELS_DIR/rosetta_v1.pt`. The path is settable via
  `DETERMINEX_ROSETTA_PT_PATH` for tests.

If `T:/` is absent on the host, models register against `data/models/` and the
agent works in degraded mode (small quantized variants only). `determinex doctor`
reports the active model directory.

---

## 3. T:/ Drive Backup Strategy

T:/ holds the bulky, regenerable-but-slow-to-rebuild artifacts. The backup
posture is **tiered by regenerability**, not by size.

### Tier A — Cannot be regenerated; must be backed up

| Path | Why critical | Backup target |
|---|---|---|
| `T:/determinex-models/rosetta_v1.pt` | Result of 5-arch training run, validated by SHA256. Retraining costs hours of RunPod time. | `c:/Dev/backups/rosetta_v1_<date>.pt.gz` weekly. Also pushed to RunPod volume snapshot when changed. |
| `T:/determinex_corpus/*.jsonl` | Hand-curated + verified seed corpus. Loss = repeat curation work. | `c:/Dev/backups/corpus_<date>.tar.zst` weekly. |
| `T:/determinex-models/*.gguf` (custom-trained) | LoRA-fine-tuned variants (engineer-v11-dsl, observer-v6-dsl, sentinel-v5-dsl). RunPod training cost. | `c:/Dev/backups/determinex_models_<date>.tar` monthly. RunPod snapshot canonical. |

### Tier B — Can be regenerated; back up index, not contents

| Path | Recovery procedure |
|---|---|
| `T:/determinex-swebench/` | `git clone` from upstream SWE-bench repo list. Index: `data/swebench_instances.json`. Snap restore time: ~30 min for 300 instances. |
| `T:/determinex-programbench/` | `scripts/seed_knowledge_base.py --reseed-programbench` + per-tool build pipeline. Index: `corpus/programbench/README.md` (canonical board). |
| `T:/huggingface_cache/` | Re-downloads on demand. No backup needed; pure cache. |

### Tier C — Ephemeral

| Path | Disposition |
|---|---|
| `T:/determinex_artifacts/quarantine/` | Auto-purged 30 days after admission decision. No backup. |
| `T:/determinex_artifacts/cache/` | Eviction by LRU when over 100 GB. No backup. |
| `T:/determinex-staging/` | Wiped between ProgramBench campaigns. No backup. |

### Backup mechanics

- Backup script: `scripts/ops/backup_tier_a.ps1` (Windows) runs Saturdays via
  Task Scheduler. Writes to `c:/Dev/backups/`.
- Backup destination size cap: 50 GB. Older-than-90-day backups pruned
  automatically.
- Restore test: documented in §6.

---

## 4. Log Rotation Policy

Determinex emits four log streams. Each has a rotation rule.

| Stream | Path | Format | Rotation | Retention |
|---|---|---|---|---|
| Observability events | `T:/determinex_audit/events/*.jsonl` (or `logs/events/`) | JSONL, append-only | 1 file per day, name `events_YYYYMMDD.jsonl` | 90 days, then gzip + move to `assurance/` if any locked-event references it; else delete. |
| Session WAL | `sessions/<session-id>/wal.jsonl` | JSONL, atomic fsync per record | Per-session; closed on session end | Indefinite (small, audit-grade). |
| SWE-bench / PB run logs | `logs/swebench/<run-id>/`, `logs/programbench/<run-id>/` | mixed JSONL + text | Per-run directory | 180 days. Locked runs (referenced from a Sentinel lock manifest) retained indefinitely. |
| Cloak audit | `logs/swebench/<run-id>/cloak_audit/` | JSONL request bodies | Per-run | Indefinite if claim is published; else 180 days. **Never auto-deleted** while the corresponding lock is active. |

Rotation runner: `scripts/ops/rotate_logs.py`, invoked nightly via
Task Scheduler. The script:

1. Walks the four streams.
2. For each candidate file, checks for references in
   `assurance/evidence/evidence_index.json` and `locks/sentinel/*.json`. If
   referenced, the file is retained regardless of age.
3. Compresses files older than the stream's retention window.
4. Writes a rotation summary to `logs/events/_rotation_<date>.jsonl`.

`DETERMINEX_NO_CORPUS_WRITE=1` blocks corpus writes but does **not** block
log rotation — rotation is a maintenance operation, not a corpus mutation.

---

## 5. Free-Space Monitoring

`determinex doctor` reports free-space pressure with three thresholds per
volume:

| State | Free space | Action |
|---|---|---|
| OK | ≥ 50 GB free | No action. |
| WARN | 20–50 GB free | Doctor surfaces yellow notice. Operator should review Tier C purge candidates. |
| FAIL | < 20 GB free | Doctor surfaces red FAIL. SWE-bench / ProgramBench runs that need workspace egress refuse to start. |

The pressure check is gated by `DETERMINEX_DISK_GUARD=1` (default ON). Setting
it to 0 disables the guard but leaves the doctor reporting intact (advisory
only).

This rule exists because of the documented SWE-bench eval failures: disk
pressure on workers caused per-instance image-export errors that understated
the cloaked configs' true scores (see `docs/PROJECT_CLOAK.md` §status). A
larger-disk rerun is gated on FAIL state being clean before the run is allowed
to start.

---

## 6. Restore Drill (Quarterly)

Once per quarter, perform a paper-and-disk restore drill:

1. Pick the latest Tier A backup (`rosetta_v1_<date>.pt.gz`,
   `corpus_<date>.tar.zst`).
2. Decompress into a scratch directory (NOT `T:/determinex-models/` — never
   overwrite the live copy during a drill).
3. Verify SHA256 against the manifest in `assurance/evidence/`.
4. Spot-check by loading the rosetta MLP via `scripts/determinex_rosetta.py
   verify --pt <scratch-path>`.
5. Append the drill record to
   `assurance/evidence/storage_drills/<YYYYMMDD>.json`.

The drill is not automated. It is recorded in
`logs/events/` and reported in the next `determinex doctor` run via the
`storage_drill_age_days` metric. WARN at >120 days, FAIL at >180 days.

---

## 7. Operator Cheatsheet

```text
# Where are my models?
determinex config show | grep models_dir

# Where are my logs going?
determinex config show | grep audit_dir

# How much free space do I have?
determinex doctor | grep -i "disk\|free\|space"

# Trigger a Tier-A backup right now
pwsh scripts/ops/backup_tier_a.ps1

# Rotate logs now (instead of waiting for the nightly run)
python scripts/ops/rotate_logs.py --now

# Verify a restored Tier-A backup
python scripts/determinex_rosetta.py verify --pt <scratch-path>
```

---

## 8. Invariants

The following must hold continuously; any violation is a STORAGE_OPERATIONS
regression:

- All T:/ paths have either a documented local fallback (PATH_PORTABILITY
  invariants) or a documented reason for requiring the drive.
- `DETERMINEX_MODELS_DIR` is the **only** model cache authority. No script
  hardcodes alternative model paths.
- Tier-A backups exist (file present) and verify (SHA256 matches manifest).
- Log rotation respects evidence/lock references — locked artifacts never
  auto-delete.
- Free-space FAIL state blocks bench runs that need workspace egress.
- Quarterly restore drill record exists and is < 180 days old.

---

*Lock: `locks/sentinel/STORAGE_OPERATIONS_LOCK_001.json`. Related:
`locks/sentinel/CONFIG_SPINE_LOCK_001.json`,
`locks/sentinel/PATH_PORTABILITY_LOCK_001.json`,
`locks/sentinel/EVIDENCE_IMMUTABILITY_GUARD_LOCK_001.json`,
`locks/sentinel/CORPUS_WRITE_GUARD_LOCK_001.json`.*
