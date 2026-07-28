# DETERMINEX — MASTER PLAN TO FULL IDE REALIZATION (living doc)

**Owner:** Claude (lead coordinator, keeps this current every wave). **Started:** 2026-06-03.
**North star:** the IDE that *knows what it's looking at, gets what it needs through governed authority, and builds / repairs / tests / verifies / packages / proves / documents / reports across the known programming + digital-infrastructure world — exact support where proven, exact blocker where not, no fake green, operating on real code.*

This is the single roadmap. Percentages are **internal estimates**, not public claims. Updated each wave; status lives in the lane handoffs + this doc's scorecard.

---

## 0. Honest current state (3 layers)
- **Accounting:** ✅ done — 383 known-world rows mapped; engine primitives all present.
- **Engine/machinery:** ✅ substantially built — hive, compiler oracle (14 validators), SWE-bench solve+repair, ProgramBench factory (56 strict locks), Cloak (package), Rosetta, detectors (23), promotion harness, governed acquisition packets, per-family proof template.
- **Proven native support:** ❌ ~0 — every row is blocked/benchmark-only/candidate. The whole remaining job = **manufacture real proofs against real external targets** (per the external-fixture correction directive).

**Scorecard (internal estimate, 2026-06-03):**
| Dimension | % | Note |
|---|---|---|
| Proof/governance spine | ~90% | gates, claim scanner, evidence index/ledger, harness, packets all real |
| Backend engine (hive/oracle/cloak/repair/PB) | ~75% | works on benchmarks; needs external-target wiring + flywheel retrain |
| Frontend (Tauri shell + panels) | ~55% | route mounted, GUI smoke verified; deeper nav + all-panel-live + signing left |
| Packaging/installer | ~30% | unsigned local NSIS only; no signed/trusted, no clean-host matrix |
| Status/test runtime | ~50% | segmented honest; monolithic tests/status not proven |
| ProgramBench | 56 strict / 52.74% | real benchmark; not yet bridged to native support |
| Known-world ACCOUNTING | ~100% | 383 rows mapped |
| Known-world NATIVE SUPPORT | ~1–2% | 1 self-surface candidate; ~0 external proven |
| Release-family progress | 0 families | criteria defined; none pass |
| C:/T: storage + memory continuity | ~60% | works but undocumented/fragile; see §5 |
| Tech debt / coordination | ~50% | self-referential proof debt, coord-doc contention, ceremony ratio |
| Public-launch readiness | NO_GO | gated on patent + proof packet + hardening |
| **Full envisioned IDE** | **~35–40%** | engine+accounting strong; proven-coverage + product + real-repo are the gap |

---

## 1. WORKSTREAM A — Native-support manufacturing (the core capability)
The engine exists; point it at real targets. Per `DETERMINEX_NATIVE_SUPPORT_CRITERION_AND_EXTERNAL_FIXTURE_CORRECTION_DIRECTIVE_001.md`.
- A1. Encode the native-support criterion in the harness (external fixture + behavioral verifier + repair-loop; reject self-surface/shallow). **NEXT.**
- A2. Prove ONE real external family end-to-end (Python CLI from PB-locked source / a real repo) → measure true per-row cost.
- A3. Per-family proof templates (reusable detector-rule + fixture + verifier + toolchain packet) — one build per family, cheap fan-out to its rows.
- A4. ProgramBench→native-support bridge: 56 locked tools → real "Determinex works on X-based repos" proofs (highest-yield: ~56→200 rows of real evidence).
- A5. Family order: Python CLI → JS/TS → Go → Rust → Java → C/C++ → then DB/infra/ML/security/legacy.
- A6. Every non-promoted row carries an EXACT blocker; the hard tail (license/network/heavy-SDK/commercial) becomes permanent honest blockers.

## 2. WORKSTREAM B — Backend engine finish
- B1. Wire oracle/SWE-bench/PB engines as the native-support verifiers (don't write shallow new ones).
- B2. Governed acquisition packet fan-out: admit toolchains (node/cargo/go/python/…) so external builds run; license/network ones = exact blockers.
- B3. Repair-loop hardening on real repos (currently SWE-bench-scoped) — the "fix + re-verify" pillar.
- B4. Model/flywheel: C1/C3/C7 (v11/v6/v5) — re-eval queued; flywheel retrain on real (error→fix) pairs from the proof runs (the moat). Confirm corpus is real, not DSL-only.
- B5. Rosetta Layer 2 (soft-prefix) — v1.5 milestone (lower priority than native support).

## 3. WORKSTREAM C — Frontend (Tauri + Next product shell)
- C1. Proof Center: source route mounted + installed-app GUI smoke VERIFIED (done). Next: deeper navigation, live data for all 9 proof-display targets, not static.
- C2. The 5 product panels (Idea Lab, Repo Clinic, Maintenance Bay, Learning Studio, Proof/Operator Center) — each gated by verified-demo-status; make each operate on real workspaces, not demo fixtures.
- C3. Wire the Tauri shell to the live hive/oracle/packets (currently the shell does not carry full hive orchestration IPC — it's in determinex_hive.py). **This is the frontend↔backend glue gap.**
- C4. Installed-app: signed/trusted installer (currently unsigned NSIS), clean-host install/uninstall matrix.
- C5. UX polish to the dark/glass standard once function is real.

## 4. WORKSTREAM D — In-between glue + tech debt
- D1. Frontend↔backend IPC: real command surface from Tauri → hive/oracle/packets (C3 above). The biggest "in-between" gap.
- D2. Self-referential proof debt: stop proving Determinex against itself (fixed by the external-fixture rule; sweep existing self-surface "eligibility").
- D3. Coordination friction: coord-doc contention (Claude+Codex same file), Codex 429/idle/overwrite history, ceremony-to-capability ratio. Mitigations: AGENTS.md rules (done), per-agent doc sections, fewer-bigger commits, higher Codex rate tier.
- D4. Test-suite runtime: monolithic tests/status can't complete in time → segmented policy. Need: parallelization / slow-cluster fix / durable runner (Workstream F).
- D5. Evidence/ledger scale: append-only ledger ~1889 entries + full re-serialization churn per wave (15k-line diffs). Consider incremental ledger writes.
- D6. Dead/duplicate code sweep, ruff/pyright clean, archive/ hygiene.

## 5. WORKSTREAM E — C:/T: storage + memory architecture (operator-flagged)
Current split (from .env + CLAUDE.md): **T:** models (`DETERMINEX_MODELS_DIR=T:/determinex-models`), Ollama blobs (`OLLAMA_MODELS=T:/OllamaModels`), SWE-bench repos (`T:/determinex-swebench`), ProgramBench (`T:/determinex-programbench`), build staging (`T:/determinex-staging`). **C:** working repo (`C:/Dev/Determinex`), `.determinex/` SQLite chrono DB, evidence ledger, agent memories (`C:/Users/ryang/.claude`, `.codex`).
- E1. **Document the canonical drive map** (what lives where + why) — currently tribal/undocumented = fragility risk. One doc.
- E2. **Cross-drive memory/continuity**: the proof ledger (C:) references model/eval artifacts (T:); if T: detaches, evidence dangles. Define integrity: hashes + presence checks across drives; graceful-degrade when T: absent (some checks already skip).
- E3. **Build-cache relocation** to T: (`T_DRIVE_CARGO_BUILD_CACHE_RELOCATION_VERIFIED` exists) — extend to node/npm/uv caches so C: doesn't bloat.
- E4. **Agent memory bridge**: Claude memory (`.claude/.../memory`) + Codex memory (`.codex`) + the chrono DB are separate. Define what persists where + a continuity protocol so context survives restarts (relevant to "keep going when you wake").
- E5. Backups: git bundles (`backups/`) + T: artifacts — verify a restore path exists.

## 6. WORKSTREAM F — Release + product hardening
- F1. Signed/trusted installer (cert + signing pipeline).
- F2. Clean-host install/launch/uninstall matrix (fresh VM/Sandbox).
- F3. Monolithic tests/status runtime closure (or durable segmentation runner with honest reporting).
- F4. Release cells 13 → grow only on proof; release-family 0 → 1 (first family via Workstream A + family criteria).
- F5. Public proof docs (CLAIMS/KNOWN_LIMITS/PROOF/REPRODUCE/SUPPORT_MATRIX/INSTALL/SECURITY) — drafted; finalize at go/no-go.

## 7. WORKSTREAM G — Real-repo leap (the product, not the benchmark)
- G1. Design + authorize the governed real-repo workflow: read-only inspect → sandbox copy → operator-approved mutation → proof → rollback. (Lane F prep started.)
- G2. Cross the real-user-repo mutation boundary safely (currently gated off). This is what makes it "natively does YOUR code," not just benchmarks.
- G3. Wire into Repo Clinic / Maintenance Bay panels.

## 8. WORKSTREAM H — Governance + IP + launch gating (mostly maintain)
- H1. Keep gates: claim scanner, day-one scanner, evidence index, append-only ledger, count-drift, anti-god terminal. (Strong.)
- H2. Patent packet (drafted, docs/ip/) → filing is operator/counsel action. PATENT_FILED stays false until filed.
- H3. Public launch: NO_GO until patent filed + proof packet public-ready + hardening + go/no-go. Donation/support rails: parked (launch plumbing, not now).
- H4. Papers (WHITE_PAPER/ARCHITECTURE/PROGRAMBENCH) — keep lockstep with evidence every wave.

---

## Sequenced program (dependency order)
1. **A1 native-support criterion in harness** (unblocks all real promotion).
2. **A2 first external family end-to-end** (Python CLI) → real per-row cost.
3. **A4/B2 PB→native bridge + toolchain packets** (highest-yield fan-out).
4. **A3 family templates → fan out** families in order (Python→JS/TS→Go→Rust→…).
5. **D1/C3 frontend↔backend IPC** (make the shell drive the engine live) — parallelizable with 3–4.
6. **F3 status runtime + F1/F2 installer hardening** (product credibility).
7. **G1/G2 real-repo boundary** (the leap) — after engine proves on fixtures.
8. **A6 hard-tail exact blockers + F4 first release-family** + **H papers/patent/launch gating**.
9. **E storage/memory hardening** runs continuously alongside (low-risk, do in idle).

## Operating model (run-while-you-sleep)
- Each wave = one workstream slice. Codex builds; Claude leads/reviews/fixes/closes; both append to the wave control doc; gates enforced; final report per wave.
- Claude maintains THIS doc's scorecard + sequenced program each wave (the "full plan tracking" you asked for).
- Autonomy: scheduled wakeups keep the loop alive; if Codex 429s/stalls, Claude takes the smallest safe lane. No fake green, ever.
- "Keep going when you wake": every wave leaves HEAD==origin, clean worktree, a final report, and this doc updated — so you can read the state cold and redirect.

## Live status (updated each wave)
- 2026-06-03: Foundations landed (harness, packets, per-family template, Batch 004 keifu→56). Lane A/B reviewed (B = self-surface, honest-but-thin → external-fixture directive written + AGENTS.md rule added). Lane C bridge + Lane D acquisition fan-out landed (Claude review pending). NEXT: Batch 006 = A1 (criterion in harness) + A2 (first REAL external Python-CLI family proof).
- Next single bottleneck: **A1+A2 — encode the criterion and prove one real external family.** Everything fans out behind it.
