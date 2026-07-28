# Determinex Proof Generation Tool Admission

`DETERMINEX_PROOF_GENERATION_TOOL_ADMISSION_LOCK_001` defines admission policy for external evidence-producing tools without installing or running them.

Covered tools: `syft`, `trivy`, `grype`, `cosign`, `slsa-verifier`, `in-toto`, `skopeo`, `crane`, `regctl`, `oras`, and `osv-scanner`.

Boundaries:

- `syft` can generate SBOMs; it cannot prove safety.
- `trivy` and `grype` can generate vulnerability scan status; they cannot prove correctness.
- `cosign` can verify signatures; it cannot prove safety by itself.
- `skopeo`, `crane`, `regctl`, and `oras` can inspect or copy exact artifacts to quarantine modes; they cannot execute them.
- `slsa-verifier` and `in-toto` can verify provenance/attestation material; they cannot grant scan status or training eligibility.

No tool grants execution or training eligibility directly.
