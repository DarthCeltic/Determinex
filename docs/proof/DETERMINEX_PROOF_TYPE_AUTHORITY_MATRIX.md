# Determinex Proof Type Authority Matrix

`DETERMINEX_PROOF_TYPE_AUTHORITY_MATRIX_LOCK_001` maps proof types to authority classes they can grant and authority classes they must deny.

Core rules:

- `registry_manifest_digest` grants artifact identity and metadata authority, not execution.
- `sbom` grants dependency inventory authority, not safety or build provenance.
- `slsa_provenance` and `in_toto_attestation` can grant source/build authority when verified, not scan status or execution safety.
- `vulnerability_scan` grants vulnerability scan authority, not behavioral correctness.
- `compiler_test_result` grants scoped verifier authority, not human approval.
- `human_approval_packet` grants operator intent, not verifier success.
- `model_output` grants advisory authority only.
- `programbench_official_artifact` grants benchmark artifact identity, not security execution.
- No proof type grants training eligibility directly.
