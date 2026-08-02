# DETERMINEX_RELEASE_FAMILY_PROMOTION_PRECONDITIONS_001

## Status

Release-supported exact cells remain `13`. Release-supported families remain `0`.

This document records preconditions only. It does not promote any family.

## Family Promotion Preconditions

A release-supported family promotion requires all of the following:

- Every exact cell in the family has detector evidence, fixture evidence, verifier evidence, toolchain or acquisition evidence, bounded execution evidence, and release-registry signoff.
- The family has a machine-readable evidence packet that lists every exact cell and proves no cell is inferred from siblings.
- The Proof Center can display the family row with each exact blocker or proof path.
- Claim scanners reject broader language such as "all apps", "all languages", "universal support", and "release-ready" unless every gate is present.
- Evidence index, append-only ledger, and drift guard are refreshed after the lock lands.
- If the family depends on installer, clean-host, signing, browser, Tauri GUI, or provider-network behavior, those gates must be proven by real artifacts, not source presence.
- Full monolithic `tests/status` may be recorded only if it actually completes; segmented validation must remain labeled segmented.

## Required Negative Checks

- No family promotion from ProgramBench benchmark score alone.
- No family promotion from detector-only coverage.
- No family promotion from a source route, static panel, or screenshot without route/runtime proof.
- No public release, beta, internal RC, or production readiness claim from exact-cell proof.

## Next Lock

`DETERMINEX_FIRST_RELEASE_FAMILY_PROMOTION_PRECHECK_LOCK_001`: pick one family, enumerate every exact cell, bind required evidence paths, and fail closed if any exact cell remains unsupported.
