# ProgramBench Safe Registry Manifest Client

`PROGRAMBENCH_SAFE_REGISTRY_MANIFEST_CLIENT_LOCK_001` adds an exact-reference Docker Registry metadata client for ProgramBench images.

Allowed behavior:

- exact `programbench/...:task_cleanroom` repository and tag only
- DockerHub bearer-token flow for repository pull scope
- manifest `GET` with Docker v2 and OCI manifest/index accept headers
- `Docker-Content-Digest`, media type, schema version, platform summary, and manifest body hash capture

Blocked behavior:

- Docker CLI or Docker daemon use
- Docker pull, layer/blob download, image import, or container run
- latest tags, catalog search, tag listing, broad search, or inferred officialness
- cache readiness, executable state, or training eligibility

The client emits metadata-only results. A found digest is usable only as metadata evidence for a later admission gate.
