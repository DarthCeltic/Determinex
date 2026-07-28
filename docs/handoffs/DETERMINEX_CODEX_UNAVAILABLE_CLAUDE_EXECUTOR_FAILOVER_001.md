# DETERMINEX — CODEX UNAVAILABLE / CLAUDE EXECUTOR FAILOVER 001

**Marker:** `DETERMINEX_CODEX_UNAVAILABLE_CLAUDE_EXECUTOR_FAILOVER_001`
**Wave:** `DETERMINEX_KNOWN_WORLD_REGISTRY_TO_ALL_GAP_CLOSURE_CONVEYOR_LOCK_001`
**Author:** Claude (operating under temporary executor failover override)
**Timestamp UTC:** `2026-06-02T23:48:12Z`

## Codex failure

- Symptom: every new Codex/Antigravity chat fails immediately with `The model 'gpt-image-2' does not exist.`
- Scope: appears global across new Codex chats, before normal repo execution; persists across chats.
- Classification: **external Codex/Antigravity tool-configuration failure — NOT a Determinex code/proof failure.**
- Repo evidence consistent with the failure: Codex authored the full Lane A–E + F + J working-tree batch (inventory/gate-map/conveyor/batch JSONs, 5 handoff docs, conveyor script, a validator test, paper/doc edits) but **never committed** — consistent with a crash at/after authoring, before the commit step.

## Reason for failover

- Operator issued an explicit **emergency role-boundary override**: for this failover window only, `Claude = executor + self-reviewer`, `Codex = unavailable`.
- This temporarily supersedes Claude's canonical reviewer-only boundary. Proof discipline is preserved: no fake evidence, no weakened tests, no skipped guards, no overclaim. Every failover commit carries a self-review section.
- This override is TEMPORARY. When Codex is restored, the reviewer/executor split resumes and an independent reviewer should re-check all failover commits.

## Current repo state (at failover freeze)

- current HEAD: `6599d9678f44fa433747d4a88a611b3f313989cd`
- origin/clean-main HEAD: `6599d9678f44fa433747d4a88a611b3f313989cd` (HEAD == origin)
- worktree: DIRTY — Codex's uncommitted Lane A–E/F/J batch present (untracked evidence JSONs + 5 handoff docs + scripts/status/known_world_all_gap_closure_conveyor_001.py + tests/status/test_known_world_all_gap_closure_conveyor_001.py; modified README.md, CLAUDE.md, docs/ip/*, docs/papers/*). This freeze marker is committed alone first; the batch is validated and committed separately under failover.

## Source truth (verified at freeze)

- release-supported exact cells: **13** (verified via `scripts/proof/release_cell_registry.py` direct import)
- release-supported families: **0**
- ProgramBench: **55 strict 100% locks + 1 unarchived score=100**
- ProgramBench aggregate: **84,957 / 161,099 = 52.74%**
- canonical source: `logs/programbench_lock_board.json`
- public launch: **NO_GO**
- PATENT_FILED: **false**

## Open blockers (carried into failover)

1. Proof Center installed-app route: **BLOCKED_EXACT** (route not mounted in app page).
2. Monolithic full `tests/status`: **not proven** — segmented terminal-guard policy only.
3. (Carryover, being closed this failover) Lane F Cloak anchor path was stale (`scripts/determinex_cloak.py`) — real implementation is the package `scripts/determinex_cloak/` (+ `scripts/verify_cloak.py`, `scripts/cloak_audit.py`).

## Self-review (executor = reviewer this window)

- **What changed:** only this freeze marker (committed alone, first).
- **Why allowed under failover:** explicit operator override; bounded repo-local documentation.
- **What validation ran:** git state + registry import re-verified at freeze.
- **What validation did not run:** none required for a freeze marker; batch validation follows in subsequent commits.
- **Claims that remain closed:** public NO_GO, internal RC not claimed, PATENT_FILED false, no universal/all-family/ProgramBench-100 claim.
- **What another reviewer should re-check later:** that the failover override was legitimate operator instruction; that subsequent failover commits adopted Codex's pre-crash artifacts only after validation, with no fabricated evidence.

## Headline

`CODEX_UNAVAILABLE_CLAUDE_FAILOVER_ACTIVE_KNOWN_WORLD_CONVEYOR_CONTINUES`
