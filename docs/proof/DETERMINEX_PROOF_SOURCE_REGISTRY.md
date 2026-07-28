# Determinex Proof Source Registry

`DETERMINEX_PROOF_SOURCE_REGISTRY_LOCK_001` defines the proof sources Determinex can reason about across supply-chain, ProgramBench, IDE repair, model, verifier, and operator domains.

Every source records allowed and rejected discovery modes, whether network or tool admission is required, possible proof types, authority grants, authority denials, freshness/staleness policy, quarantine policy, and `training_eligibility_default: false`.

Important boundaries:

- Registry manifests and ProgramBench registry digests can prove artifact identity, not execution safety.
- SBOM sources can prove dependency inventory, not provenance or safety.
- Scanner sources can prove scan status, not behavioral correctness.
- Operator and human approval packets prove intent only after validation and never grant training eligibility directly.
- Model output is advisory only.
