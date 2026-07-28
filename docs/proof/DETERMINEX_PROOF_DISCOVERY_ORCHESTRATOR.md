# Determinex Proof Discovery Orchestrator

`DETERMINEX_PROOF_DISCOVERY_ORCHESTRATOR_LOCK_001` maps proof gaps to next actions without executing tools or granting authority.

Decision classes:

- `DISCOVER`: exact metadata lookup plans, such as exact registry manifest digest discovery.
- `GENERATE`: admitted tool generation plans, such as SBOM or scan generation after prerequisites exist.
- `REQUEST_OPERATOR`: operator-supplied packets, approvals, config, or provenance.
- `BLOCK`: remain blocked until prerequisite authority exists.

The orchestrator currently routes ProgramBench artifact tar provenance and IDE human approval gaps to `REQUEST_OPERATOR`, and SBOM/scan gaps to `GENERATE` plans only.
