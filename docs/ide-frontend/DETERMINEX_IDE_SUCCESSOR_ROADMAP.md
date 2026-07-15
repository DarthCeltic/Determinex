# Determinex IDE Successor Roadmap

## Purpose

Determinex is now the public product name. The product direction is no longer only
"put the brain in VS Code." The target is a standalone, proof-native IDE that can
become the natural successor to VS Code for agentic, verifier-bound development.

This document is a roadmap and status contract. It is not a release-readiness
claim.

## Brand Boundary

- Public product surfaces should say Determinex.
- Former Determinex references are allowed only when they identify real legacy
  scripts, environment variables, model tags, repository paths, historical docs,
  or evidence.
- Internal `determinex_*` and `DETERMINEX_*` identifiers remain until a coordinated
  internal rename. Do not mechanically rename them inside operational tooling.

## Successor Standard

To be a credible VS Code successor, Determinex must meet the baseline editor
expectations users already have:

- Open an existing repo without setup friction.
- Edit, search, diff, run tasks, run tests, inspect logs, and manage terminals.
- Preserve settings, keybindings, layout, trust state, and workspace state.
- Support an extension story that is either compatible with VS Code/Open VSX or
  clearly better for proof-native workflows.
- Ship installers, updates, SBOM, clean-host install proof, and rollback paths.

The current IDE already has a Tauri/Next shell, Monaco editor, terminal dock,
project hub, command palette, tool dock, Proof Center, model routing surfaces,
and oracle/benchmark concepts. Those are foundations, not completion.

## Differentiators

Determinex should not win by copying VS Code panel-for-panel. It should win where
VS Code was not designed around verifier-bound agents:

- Proof-native workbench: every readiness badge and product claim must point to a
  collector, evidence path, and verifier.
- Agentic lanes: background workers should be pauseable, replayable, auditable,
  and approval-gated before mutation.
- Correctness amplifier: model output is a proposal; compilers, tests, oracles,
  and benchmark harnesses decide acceptance.
- Local-first privacy: provider routing, network policy, Cloak, redaction, and
  audit trails belong in the main workflow, not hidden settings.
- Release cockpit: installer, SBOM, clean-host install, benchmark, family
  support, and public-claim gates should be visible in one operator view.

## Current Pillars

The machine-readable source for the IDE panel is
`frontend/src/lib/successorRoadmap.ts`.

The release-gate collector is `scripts/release/determinex_release_gates.py`.
Its current snapshot is
`assurance/evidence/determinex_release_gate_status/release_gates_20260707.json`.
The frontend projection is `frontend/src/lib/releaseGateStatus.ts`.

Current pillar states:

- Workbench parity: partial.
- Proof-native development: partial.
- Agentic workbench: partial.
- Local and remote execution fabric: partial.
- Privacy and governance cockpit: partial.
- VS Code/Open VSX compatibility: planned.
- Release cockpit: partial.

Every current pillar is marked `releaseReady: false` on purpose. That prevents a
roadmap panel from becoming a launch claim.

## Current Release Gate Snapshot

- SBOM coverage: passed for the currently committed Python and npm SBOM files.
- Installer/signing/public distribution: partial. Installer packet evidence
  exists, but signing, SmartScreen/trust, legal/IP packet, public repo scrub,
  full status suite, and unsigned packet blockers remain.
- Clean-host install proof: blocked on clean runner/Docker health evidence.
- First end-to-end user workflow: blocked on local Builder/Ollama health.
- VS Code/Open VSX compatibility: planned.
- Internal Determinex rename: partial because legacy `determinex_*` and
  `DETERMINEX_*` identifiers remain by project contract.

Overall `release_ready` remains `false`.

## Next Locks

- Clean-host install and first-run workspace open proof.
- VS Code workspace and settings migration plan.
- Extension API and marketplace compatibility contract.
- Collector-backed privacy, proof, and release readiness badges.
- Replayable agent lane controls with durable approvals.
- Unified local, container, and remote runner cockpit.
