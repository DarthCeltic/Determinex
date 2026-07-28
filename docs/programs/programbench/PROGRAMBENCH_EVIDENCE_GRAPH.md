# ProgramBench Evidence Graph

`PROGRAMBENCH_EVIDENCE_GRAPH_LOCK_001` links ProgramBench state, provenance, security, policy, preflight, skip, training eligibility, and operator action records.

Graph nodes include type, path, status, and optional instance id. Graph edges use explicit reasons such as `consumes`, `blocks`, `supersedes`, `requires`, `authorizes`, and `denies`.

The Doxygen graph shows official artifact authority with scan failure, policy admission required, execution blocked, and training eligibility false.

No graph edge creates an unauthorized path to execution or training eligibility.
