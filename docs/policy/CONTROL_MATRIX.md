# Control Matrix

Canonical machine-readable controls live in:

```text
assurance/controls/control_matrix.json
```

The operating model is:

```text
claim -> control -> implementation -> test -> evidence -> lock manifest
```

Core control families:

- input policy and intent classification
- cloud egress filtering
- Project Cloak and Visual Cloak
- action safety governor
- Docker / VM / emulator execution boundaries
- HMAC-signed corpus writes
- license, secret, malware, and dedupe gates
- dependency and container scanning
- benchmark adapter verifier loops
- ProgramBench gate/hint-audit drain

Controls without tests are provisional. Tests without evidence are not locks.
