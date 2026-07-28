# DETERMINEX_RELEASE_FAMILY_PROMOTION_PRECONDITION_TIGHTENING_BATCH_003

Date: 2026-06-02

## Status

- Release-supported exact cells: `13`.
- Release-supported families: `0`.
- Family promotion in Batch 003: none.

## Nearest Candidate Families

1. `determinex_surface`
   - Required exact cells: Proof Center installed-app display, claim scanner, ProgramBench factory/provenance, installer path, proof report export.
   - Missing proof anchors: full row-table Proof Center binding, signed/trusted installer boundary, source/app data freshness verifier.
   - Proof Center visibility requirement: current truth block is visible; per-row details still pending.
   - Tests before family count can become 1: installed-app display test, claim scanner guard, release registry mutation signoff, evidence index/ledger/drift guard.

2. `programbench`
   - Required exact cells: strict-lock archive verification for every promoted tool, support-mapping boundary, proof that benchmark lock is not product support.
   - Missing proof anchors: archive lock for `trasta298__keifu`; next strict-lock wave toward 75; stale-count guard.
   - Proof Center visibility requirement: 55 strict + 1 unarchived / 52.74% visible.
   - Tests before family count can become 1: board refresh verifier, strict archive verifier, claim scanner, release registry signoff.

3. `security`
   - Required exact cells: SBOM, clean-runner continuity, license/security review, false-claim scanner.
   - Missing proof anchors: complete release SBOM claim, security review signoff, public distribution/legal packet.
   - Proof Center visibility requirement: SBOM / clean-runner status visible as bounded, not release readiness.
   - Tests before family count can become 1: SBOM hash verifier, security/license guard, release registry signoff.

## Common Preconditions

- Detector, fixture, verifier, toolchain/authority, and bounded execution must all pass for exact cells.
- Proof Center must display exact blocker or proof path for each row being promoted.
- Claim scanners must remain clean after docs/paper updates.
- Evidence index, append-only ledger, and drift guard must be green.
- Fresh-host install and signed/trusted installer proof are required where packaging/distribution is part of the family.

No family may move from `0` until these criteria pass.
