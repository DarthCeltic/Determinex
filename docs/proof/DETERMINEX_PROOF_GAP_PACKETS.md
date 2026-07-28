# Determinex Proof Gap Packets

`DETERMINEX_PROOF_GAP_PACKET_LOCK_001` defines normalized packets for missing or insufficient proof.

Each gap packet states the subject, domain, missing proof type, required authority, blocked authority, reason the proof is required, acceptable sources, rejected sources, operator action, blocker, evidence references, and closed authority flags.

Initial examples cover:

- Batch001 artifact import provenance missing.
- Doxygen security policy admission missing.
- IDE human approval packet missing.
- Live local model config missing.
- Artifact SBOM missing.
- Imported artifact scan missing.

Gap packets are non-authorizing: execution, source mutation, and training eligibility remain false.
