# Determinex C: / T: drive inventory — 2026-05-29

Read-only inventory to support a cleanup pass. **No moves, no deletes, no compression performed by this audit.** Scope: `c:/Dev/Determinex/*` working tree + `T:/determinex-*` and `T:/ColdStorage/`.

## Drive headroom

| Drive | Used | Free | Total | Headroom |
|---|---:|---:|---:|---|
| C: | **395.9 GB** | **57.8 GB** | 453.7 GB | **getting tight** (<15% free) |
| T: | 766.5 GB | 1096.5 GB | 1863 GB | ample |

**Implication:** C: is the cleanup priority. Every gigabyte freed from C: is one fewer disk-pressure incident.

## C:/Dev/Determinex — top-level dir sizes

(Cross-validated with `du -sh`: same picture, except `logs/` came out higher in `du` — see note below.)

| Dir | Size | Tracked? | Notes |
|---|---:|---|---|
| **scripts/** | **29 GB** | partial | Dominated by `scripts/fine_tuning/outputs/` (28.87 GB, untracked) |
| **logs/** | **26 GB** (du) / 19.34 GB (PS) | gitignored | `du` counts more — likely files PowerShell couldn't open. Real cleanup yield could be higher than the conservative 18 GB estimate. Dominated by `logs/swebench/` |
| **corpus/** | **13 GB** | mostly tracked | `corpus/programbench/` is 13 GB; `per_tool_overrides/` alone is 3.21 GB / 125k files (see below) |
| **frontend/** | **7.2 GB** | gitignored mostly | `src-tauri/target/` is 7.2 GB (Rust build, regenerable) |
| **data/** | 1.4 GB | gitignored | `data/cache/` is 1.2 GB |
| **bundler/** | 340 MB | partial | PyInstaller/bundle output dir |
| **work/** | 147 MB | partial | Working scratch |
| tests/ | 12 MB | tracked | Test suite |
| assurance/ | 9.5 MB | tracked | Evidence, demo workspaces, operator outbox |
| landing/ | 7.1 MB | tracked | Landing-page assets |
| dataset_generation/ | 4.9 MB | tracked | — |
| docs/ | 2 MB | tracked | The audit subject |
| locks/ | 1.7 MB | tracked | Sentinel locks (~320 JSON files) |
| unsloth_compiled_cache/ | 1.4 MB | gitignored | Unsloth fine-tune cache |
| sessions/ / executors/ / rosetta/ / archive/ / runpod/ etc. | < 1 MB each | mixed | Mostly empty placeholders or small |

**Top-level files >10 MB:**
- `.git/index` — git index, grows with tracked file count (124k tracked = big index). Normal.
- `corpus/auto_curriculum.jsonl` — training curriculum corpus. Expected.
- `data/combined_training.jsonl` — combined training data. Expected.

## Biggest cleanup targets on C:

### 1. `scripts/fine_tuning/outputs/` — **28.87 GB** ⚠️ priority

| Subdir | Size | Status |
|---|---:|---|
| `determinex-engineer-v6/` | 12.70 GB | Old generation |
| `determinex-engineer-v4/` | 12.55 GB | Older generation |
| `engineer-v13-merged/` | 2.96 GB | Merge output |
| `determinex-engineer-v5/` | 423 MB | Old generation |
| `engineer-go-fix-v2/` | 156 MB | Recovery output |
| `engineer-go-fix/` | 86 MB | Older recovery output |

**0 of these files are tracked in git.** The directory isn't in `.gitignore` but the contents are untracked.

**Recommendation:** Move to `T:/determinex-models/legacy-checkpoints/` (which is the canonical model storage per `DETERMINEX_MODELS_DIR=T:/determinex-models`). Keep `determinex-engineer-v11-dsl` (current) on T: where it already lives. Then add `scripts/fine_tuning/outputs/` to `.gitignore` so this doesn't recur.

**Recovers ~29 GB on C:.**

### 2. `logs/swebench/` — **18.59 GB** ⚠️ priority

Old SWE-bench eval logs from the Config B/D/E ablation runs. `.gitignore` already excludes `logs/`. Status per [docs/SWE_BENCH ablation results](docs/_audit/reference_map_20260529.csv): the clean ablation is recorded in `logs/swebench/clean_ablation/SUMMARY_clean.md`.

**Recommendation:** Archive `logs/swebench/` runs older than the **clean ablation result set** to `T:/determinex-logs/swebench-archive-<date>/`, compressed. Keep the canonical `SUMMARY_clean.md` and the live run directories.

**Recovers ~18 GB on C:** (most of it).

### 3. `frontend/src-tauri/target/` — **7.18 GB**

Rust build artifacts (`cargo build`). Regenerable from source. `frontend/src-tauri/target/` is implicitly gitignored via `dist/` / `build/` but worth confirming.

**Recommendation:** `cargo clean` in `frontend/src-tauri/`. Re-builds will take ~5 min next time but disk is reclaimed.

**Recovers ~7 GB on C:.**

### 4. `corpus/programbench/` — 12.97 GB (mostly KEEP)

121,552 tracked files. This is the canonical locked-tool submission corpus (each of the ~35–53 locked tools has its `submission.tar.gz` + `eval_report.json` + `source/` + lessons + receipts). **Intentional and authoritative — do not move.**

There may be unlocked drafts mixed in; spot-check `corpus/programbench/drafts/` if it exists, but most of this 13 GB is load-bearing for the ProgramBench score.

### 5. `frontend/node_modules/` — 596 MB

Gitignored, regenerable from `package-lock.json`. **Standard practice: leave it.** Reinstall with `npm ci` if it gets corrupted.

### 6. `data/cache/` — 1.2 GB

Runtime cache. Gitignored. **Leave it.** Will trim itself over time or via the app's own cache TTL.

## T: drive Determinex-owned dirs

| Dir | Size | Purpose |
|---|---:|---|
| `T:/determinex-models/` | 170.9 GB | Canonical model storage (per `DETERMINEX_MODELS_DIR`) |
| `T:/determinex-programbench/` | 35.2 GB | Pre-cloned SWE-bench / ProgramBench repos for fast eval |
| `T:/determinex-datasets/` | 13.1 GB | Dataset storage |
| `T:/determinex-target/` | 11.8 GB | Likely a Tauri or Rust target redirected to T: |
| `T:/ColdStorage/` | 8.1 GB | Cold-storage tier (now also holds the docs baseline tarball, 416 KB) |
| `T:/determinex-staging/` | 2.5 GB | Staging area |
| `T:/determinex-logs/` | 0.8 GB | Log archive (underused — only 800 MB; can absorb logs/swebench archive) |
| `T:/determinex_artifacts/` | 0.7 GB | Misc artifacts |
| `T:/determinex_corpus/` | 0.5 GB | Corpus mirror/cache |
| `T:/determinex_audit/` | 0 GB | Empty placeholder |
| `T:/Dev_overflow/` | 1 GB | General overflow |
| `T:/Dev-backups/` | 0.2 GB | General backups |

**T: has 1096 GB free** — plenty of room for everything moved off C:.

**Note:** There are two parallel naming conventions on T: — `determinex-*` (dash) and `determinex_*` (underscore). Worth normalizing to one convention as a separate hygiene pass; right now both exist and may indicate duplicate/divergent stores.

## Git hygiene

- **124,777 tracked files** total
- `corpus/programbench/`: 121,552 tracked (97% of all tracked files)
- `scripts/`: 897 tracked
- `assurance/`: 459 tracked
- `tests/`: 326 tracked
- `locks/`: 320 tracked
- `docs/`: 263 tracked
- `frontend/`: 182 tracked
- **0 tracked `__pycache__` / `.pytest_cache` / `*.pyc` / `*.pyo`** ✓ (gitignore is doing its job)
- `.gitignore` is 217 lines, comprehensive coverage

## .gitignore status — actual coverage

**Correction to my earlier note:** The current `.gitignore` already covers everything I'd proposed:

- `scripts/fine_tuning/outputs/` ✓ (line under "ML training artifacts")
- `frontend/src-tauri/target/` ✓ (line under "Rust compilation artifacts")
- `target/` ✓ (catch-all Rust target)
- `*.gguf`, `*.pt`, `*.safetensors`, `*.bin` ✓ (ML weights)
- `unsloth_compiled_cache/` ✓
- `/logs/` ✓ (covers `logs/swebench/`)

**The only gap I'd suggest:** `frontend/src-tauri/.fastembed_cache/` (87 MB, regenerable cache) — not currently listed. Tiny win; not urgent.

So the 28.9 GB on `scripts/fine_tuning/outputs/` is **already untracked** — moving the contents off C: is a pure disk-space win with no git impact.

## Large tracked binaries in `corpus/programbench/` ⚠️ new finding

Aggregate numbers (full scan):

| Subdir | Size | Tracked file count |
|---|---:|---:|
| `corpus/programbench/per_tool_overrides/` | **3.21 GB** | **125,526** |
| `corpus/programbench/locked/` | 0.30 GB | 3,853 |

`per_tool_overrides/` is **10× the size** and **32× the file count** of `locked/`. It's the dominant single contributor to the 124,777 total tracked files.

Bytes-only summary:
- **126 tracked files larger than 5 MB**, totalling **~1.55 GB**.
- That's the obvious Git-LFS-candidate set; the conventional LFS threshold is much lower (~100 KB for binaries), so the true LFS-eligible set is larger.

Top 17 binaries by size:

| Binary | Size | Path |
|---|---:|---|
| gomplate | 52.4 MB | `per_tool_overrides/hairyhenderson__gomplate.05eb3aa/gomplate` |
| duckdb | 49.6 MB | `per_tool_overrides/duckdb__duckdb.bdb65ec/duckdb` |
| codesnap | 48.0 MB | `per_tool_overrides/codesnap-rs__codesnap.f81e4f3/codesnap` |
| sequences.csv.gz | 46.3 MB | `per_tool_overrides/duckdb__duckdb.bdb65ec/data/csv/sequences.csv.gz` |
| ast-grep | 45.1 MB | `per_tool_overrides/ast-grep__ast-grep.dde0fe0/ast-grep` |
| bedtools | 43.7 MB | `per_tool_overrides/arq5x__bedtools2.dd57059/bedtools` |
| atlas | 41.6 MB | `per_tool_overrides/ariga__atlas.6d81150/atlas` |
| chamber | 34.8 MB | `per_tool_overrides/segmentio__chamber.5f93f5f/chamber` |
| oranda | 34.6 MB | `per_tool_overrides/axodotdev__oranda.27d60c7/oranda` |
| xsv | 29.1 MB | `per_tool_overrides/burntsushi__xsv.f430466/xsv` ← also tracked at `locked/xsv/source/xsv` (29.1 MB) |
| data_file.c | 20.5 MB | `per_tool_overrides/php__php-src.c891263/ext/fileinfo/data_file.c` |
| actiontable.go | 19.1 MB | `per_tool_overrides/johnkerl__miller.8d85b46/pkg/parsing/parser/actiontable.go` (parser table) |
| lazygit | 19.0 MB | `per_tool_overrides/jesseduffield__lazygit.1d0db51/lazygit` |
| srgn | 18.8 MB | `per_tool_overrides/alexpovel__srgn.89f943b/srgn` |
| fx | 18.1 MB | `per_tool_overrides/antonmedv__fx.86d0d34/fx` |
| trdsql | 17.3 MB | `per_tool_overrides/noborus__trdsql.d8c5ff6/trdsql` ← also `locked/trdsql/source/trdsql` (17.3 MB) |
| gdu | 14.7 MB | `per_tool_overrides/dundee__gdu.ede21d2/gdu` |

Two issues:

1. **At least 2 binaries duplicated** between `per_tool_overrides/` and `locked/<tool>/source/` (xsv, trdsql — both ~17–29 MB each). Worth a focused diff to find all pairs.
2. **Compiled Linux/Mac binaries tracked in git** is industry-non-standard. Git LFS is the conventional move for >5 MB binaries; otherwise these inflate every clone and every git operation. The `per_tool_overrides/` pattern looks intentional (overrides for tool builds the eval harness re-uses), but the binaries themselves are reproducible from `source/` + build commands.

**Recommendation (not actioned this session):**

- Identify the full list of duplicate binaries between `per_tool_overrides/` and `locked/<tool>/source/`. Drop the `per_tool_overrides/` copy if `locked/source/` is canonical.
- Move pre-built binaries to a `T:/determinex-programbench/per-tool-binaries/<tool>/` cache, referenced by a JSON pointer in the corpus. Saves potentially hundreds of MB of tracked git state.
- Or migrate to Git LFS for the binaries that must stay tracked. Standard practice for >5 MB build artifacts.

This is a separate workstream from doc cleanup; surfacing it here for visibility.

## Stale-evidence archival (selected option from prior turn)

Survey of `assurance/evidence/**/run_*.json`:

| Age threshold | Count |
|---|---:|
| Total run_*.json | 194 |
| Older than 14 days | **0** |
| Older than 30 days | **0** |

**Result:** Nothing is currently archivable under the 14-day threshold. The project's evidence directory is entirely from the May 2026 ramp; no stale archival makes sense yet. **No action recommended on this front today.** Re-run the scan in ~2 weeks; entries from late May will start aging out.

## Untracked items in working tree (5 directories + files)

These are Codex-lane artifacts from recent commits that haven't been merged or that Codex has not committed yet:
- `assurance/demo_workspaces/go_toolchain_repair_and_vite_static_smoke/`
- `assurance/demo_workspaces/universal_100_matrix_probe_execution_batch_002/`
- `assurance/evidence/determinex_react_universal_100_matrix_probe_execution_batch_binding/`
- `assurance/evidence/determinex_tandem_status/`
- `assurance/evidence/evidence_count_drift_guard/run_20260528.EVIDENCE_COUNT_DRIFT_GUARD_BLOCKED_UNEXPLAINED_ADDITION.json`
- `assurance/evidence/go_toolchain_repair_and_vite_static_smoke/`
- `assurance/evidence/merge_audit_inbox/claude_opus48_merge_authority_audit_dump_20260528.{json,md}`
- `assurance/evidence/universal_100_claude_binding_handoff/`
- `assurance/evidence/universal_100_matrix_probe_batch_001_reconciliation/`

**These are NOT Claude's to clean up** — they're shared-evidence reconciliation territory. Leave them; Codex sweeps them.

## Recovery plan — by ROI

| Action | Recovered | Effort | Risk |
|---|---:|---|---|
| Move `scripts/fine_tuning/outputs/` → `T:/determinex-models/legacy-checkpoints/` | **~29 GB** | low (file move) | low (untracked) |
| Archive `logs/swebench/` older runs → `T:/determinex-logs/swebench-archive-…tar.gz` | **~18 GB** | low (tar + delete) | low (gitignored, log data) |
| `cargo clean` in `frontend/src-tauri/` | **~7 GB** | trivial | none (regenerable) |
| Add the 3 `.gitignore` lines above | 0 (preventive) | trivial | none |
| **Total potential recovery on C:** | **~54 GB** | | |

Going from 57.8 GB free → 111.8 GB free would put C: back into healthy territory (24% free).

## What to do next (when ready to act)

1. **Confirm the recovery plan and any per-file objections** — the only judgment-call items are: (a) is *any* of `scripts/fine_tuning/outputs/determinex-engineer-v4|v5|v6` still needed locally, or all safe to move to T:? (b) is the `logs/swebench/clean_ablation/` directory the *only* keeper, or are there other log subdirs that should stay on C:?
2. **Move + tar in one targeted batch** with explicit per-target authorization.
3. **Append `.gitignore` lines** — separate, additive commit.
4. **Re-run this inventory script** after to confirm C: free has jumped.

Helper for re-run:
```powershell
Get-ChildItem -Directory | Select-Object Name, @{
  Name='SizeMB';
  Expression={[math]::Round((Get-ChildItem -Recurse -File -ErrorAction SilentlyContinue | Measure-Object Length -Sum).Sum/1MB,0)}
} | Sort-Object SizeMB -Descending
```
