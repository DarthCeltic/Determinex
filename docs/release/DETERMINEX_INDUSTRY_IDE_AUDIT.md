# Determinex Industry IDE Audit

Status date: 2026-07-08

This document is the durable audit surface for the request to make Determinex an exceptional, top-of-industry, proof-governed IDE. It is not a release certificate. The app-visible checklist lives in `frontend/src/lib/industryIdeBacklog.ts` and is rendered by `frontend/src/components/SuccessorRoadmapPanel.tsx`.

## Claim Boundary

Checked means current repo evidence supports that narrow item. Partial means the mechanism or surface exists but is not proven end to end. Blocked means the next proof or release gate cannot be honestly marked complete yet. Planned means the feature or proof contract still needs implementation.

Determinex remains `releaseReady=false` until the release gate collector and clean-host evidence say otherwise.

## Current Checked Items

- Built-in add-on install and uninstall state: checked by `frontend/src/lib/addonStorage.ts`, `frontend/src/lib/__tests__/addonStorage.test.ts`, and commit `9d844aaf5`.
- Setup rerun tests: checked by `frontend/src/lib/__tests__/networkPolicy.test.ts` and prior setup repair work.
- Clean-host gate false-positive guard: checked by `scripts/release/clean_host_install_transcript.py`, `scripts/release/determinex_release_gates.py`, and tests requiring a full install, launch, Proof Center smoke, workspace command smoke, and uninstall transcript before the clean-host gate can pass.
- NSIS download bundle exists for local/operator setup testing, but the release closure currently records `download_bundle_source_commit_not_current` after the latest release-gate changes.
- Extension compatibility contract: checked by `docs/release/DETERMINEX_EXTENSION_COMPATIBILITY_CONTRACT.md`; runtime compatibility remains gated by `extension_compat`.
- Internal rename migration contract: checked by `docs/release/DETERMINEX_INTERNAL_RENAME_MIGRATION.md`; active legacy identifiers remain by project contract.

## Highest-Priority Blockers

- Clean-host install, launch, workflow, and uninstall proof is blocked until the clean-host runner is executed outside the sandbox and a valid `determinex-clean-host-install-transcript-v1` packet is recorded.
- Windows code signing and SmartScreen trust are blocked by `windows_trust` until a valid `determinex-windows-trust-evidence-v1` packet is recorded.
- MSI/WiX distribution is blocked by `windows_msi`; the current downloadable package is the unsigned NSIS setup artifact only.
- Legal, license, IP, and model notice packet is blocked by `legal_public_distribution` until public distribution review is executed.
- ProgramBench public release proof is blocked at `0/200` official full-suite strict locks; native rebuild, factory-accepted, ceiling, and cache rows are explicitly non-authorizing.
- Fresh SWE-bench privacy-cost reruns are blocked until B-Uncloaked, RegionControl, and Cloaked evidence is refreshed.

## Partial But Real Strengths

- Tauri/Next workbench shell, Monaco editor, terminal dock, project hub, command palette, and attachable tools exist.
- Proof Center, Mission Control, release gates, protected release packet schemas, claim scanner, SBOM evidence, and roadmap status surfaces exist.
- Hive sessions, agent trace, local model routing, network policy, and Project Cloak primitives exist.
- ProgramBench and SWE-bench tooling exist, but public claims remain gated by `programbench_200` and `swebench_fresh` release gates.

## Next Execution Order

1. Run clean-host install proof outside the sandbox and attach install, launch, workflow, uninstall, and residue evidence.
2. Finish installer trust: code signing, SmartScreen verification, and either MSI/WiX proof or NSIS-only release decision.
3. Record protected release packets for Windows trust, legal/IP public distribution, MSI/WiX, extension runtime compatibility, and internal rename migration after their external/runtime checks pass.
4. Add a universal workspace smoke test: open a fresh repo, detect stack, run commands, repair one failure, verify, and explain.
5. Define the Determinex extension API and VS Code/Open VSX compatibility contract.
6. Add replayable agent lane controls: pause, resume, cancel, retry, diff review, rollback, logs, and artifacts.
7. Expand the language/toolchain matrix with fixture projects and run/test/build/lint recipes.
8. Bind every privacy, proof, and release badge to fresh collector output and timestamped evidence.
9. Continue ProgramBench official full-suite locks toward 200/200 and run fresh official SWE-bench Lite privacy-mode reruns before any benchmark publication claims.

## Verification Commands

Use these commands when updating this audit:

```powershell
cd frontend
npm.cmd test -- --run
npm.cmd run build
cd ..
.venv\Scripts\python.exe scripts\claim_scanner\day_one_public_claim_scanner.py --print
```

Expected release boundary: claim scanner passes, but public release remains blocked until `scripts/release/determinex_release_gates.py` returns a release GO with clean-host and signing evidence.
