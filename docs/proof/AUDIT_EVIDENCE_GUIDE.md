# Audit Evidence Guide

Use this guide to decide whether a Determinex claim is supported.

## Evidence Classes

- lock manifest: final claim artifact
- verifier output: compiler/test/security result
- corpus record: signed training trace
- gate result: ProgramBench floor/lock decision
- hint audit: reject classification and next action
- SBOM/license/security scan: supply-chain evidence

## Storage

- ProgramBench gates: `logs/programbench_factory/`
- ProgramBench notes: `corpus/programbench/in_progress/`
- Hetzner returns: `T:/determinex-staging/hetzner_returns/`
- Hetzner mirror: `T:/determinex-programbench/hetzner_results/`
- Corpus: `T:/determinex_corpus/`
- Assurance: `assurance/`

## Rule

If an artifact is not reproducible from a verifier or signed manifest, do not
use it as proof in docs, claims, or model cards.
