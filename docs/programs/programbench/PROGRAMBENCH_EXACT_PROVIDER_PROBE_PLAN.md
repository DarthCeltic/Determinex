# ProgramBench Exact Provider Probe Plan

`PROGRAMBENCH_EXACT_PROVIDER_PROBE_PLAN_LOCK_001` defines non-executing exact-provider probe steps for missing ProgramBench image metadata.

Allowed providers are `docker_hub_official`, `ghcr_exact`, `github_release_metadata`, and `huggingface_explicit`. The plan forbids broad search, latest tags, image pulls, Docker runs, and inferred officialness.

For current missing Batch 001 rows, name derivation is marked unsafe until an exact operator or manifest source supplies a candidate.
