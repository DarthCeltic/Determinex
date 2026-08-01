---
name: swebench-grpc__grpc-go
description: SWE-bench repo behavioral spec for grpc/grpc-go. Aggregated from 16 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# grpc/grpc-go — SWE-bench Repo Spec

> **16 bug-fix instances** across 1 dataset(s); language(s): go.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| multi-swe-bench | 16 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `balancer/grpclb/grpclb.go` | 5 |
| `balancer/grpclb/grpclb_remote_balancer.go` | 4 |
| `clientconn.go` | 3 |
| `balancer/base/balancer.go` | 2 |
| `internal/resolver/dns/dns_resolver.go` | 2 |
| `resolver_conn_wrapper.go` | 2 |
| `internal/internal.go` | 2 |
| `resolver/dns/dns_resolver.go` | 2 |
| `dialoptions.go` | 2 |
| `balancer/rls/internal/keys/builder.go` | 1 |
| `vet.sh` | 1 |
| `credentials/alts/utils.go` | 1 |
| `xds/internal/resolver/xds_resolver.go` | 1 |
| `resolver/resolver.go` | 1 |
| `service_config.go` | 1 |
| `xds/internal/balancer/xds.go` | 1 |
| `serviceconfig/serviceconfig.go` | 1 |
| `balancer/balancer.go` | 1 |
| `resolver/manual/manual.go` | 1 |
| `balancer_conn_wrappers.go` | 1 |
| `server.go` | 1 |
| `credentials/credentials.go` | 1 |
| `health/client.go` | 1 |
| `internal/backoff/backoff.go` | 1 |
| `backoff.go` | 1 |
| `balancer/xds/xds_client.go` | 1 |
| `balancer/grpclb/grpclb_picker.go` | 1 |
| `benchmark/benchmark.go` | 1 |
| `benchmark/benchmain/main.go` | 1 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: **

Sample FAIL_TO_PASS test names (first 10):
```
```

## Section 4 — Problem-theme distribution

Top themes across 16 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|

## Section 5 — Sample issues (no patches — those are the answer)

## Section 6 — Builder guidance

When building a fix for an instance in grpc/grpc-go:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. balancer/grpclb/grpclb.go appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 16 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "grpc/grpc-go"`).

First 20 instance_ids:

- `grpc__grpc-go-3476` (dataset: `multi-swe-bench`)
- `grpc__grpc-go-3361` (dataset: `multi-swe-bench`)
- `grpc__grpc-go-3351` (dataset: `multi-swe-bench`)
- `grpc__grpc-go-3258` (dataset: `multi-swe-bench`)
- `grpc__grpc-go-3201` (dataset: `multi-swe-bench`)
- `grpc__grpc-go-3119` (dataset: `multi-swe-bench`)
- `grpc__grpc-go-2996` (dataset: `multi-swe-bench`)
- `grpc__grpc-go-2951` (dataset: `multi-swe-bench`)
- `grpc__grpc-go-2932` (dataset: `multi-swe-bench`)
- `grpc__grpc-go-2760` (dataset: `multi-swe-bench`)
- `grpc__grpc-go-2744` (dataset: `multi-swe-bench`)
- `grpc__grpc-go-2735` (dataset: `multi-swe-bench`)
- `grpc__grpc-go-2631` (dataset: `multi-swe-bench`)
- `grpc__grpc-go-2630` (dataset: `multi-swe-bench`)
- `grpc__grpc-go-2629` (dataset: `multi-swe-bench`)
- `grpc__grpc-go-2371` (dataset: `multi-swe-bench`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
