# Incident Response

## Incident Types

- secret detected in corpus source
- unsafe action attempted
- cloud-bound payload failed egress policy
- verifier artifact tampering
- dependency or container critical vulnerability
- remote worker overload or data-loss event
- benchmark fixture corruption

## Response

1. Stop the affected lane.
2. Preserve logs and manifests.
3. Mark corpus records rejected if signatures or provenance are suspect.
4. Write an incident row under `assurance/incidents/incident_log.jsonl`.
5. Add or update a regression test.
6. Reopen the lane only after evidence is refreshed.
