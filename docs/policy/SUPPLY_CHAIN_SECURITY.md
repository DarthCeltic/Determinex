# Supply Chain Security

Determinex treats dependencies, benchmark harnesses, containers, and corpus source
material as supply-chain inputs.

## Required Gates

- pinned dependency versions
- lockfile verification
- dependency vulnerability scan
- container image inventory and digest review
- license inventory
- secret scan
- malware-pattern scan
- SBOM generation

## Tools

```text
scripts/security/generate_sbom.py
scripts/security/dependency_scan.py
scripts/security/license_scan.py
scripts/security/container_scan.py
scripts/security/verify_lockfiles.py
scripts/corpus/code_ingest/corpus_packager.py
```

## Policy

Critical or high unwaived vulnerability findings block release claims.
Unknown-license source blocks training ingest. Containers tagged `latest` are
allowed only for local experimentation and must not back a lock claim.
