---
name: swebench-zeromicro__go-zero
description: SWE-bench repo behavioral spec for zeromicro/go-zero. Aggregated from 15 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# zeromicro/go-zero — SWE-bench Repo Spec

> **15 bug-fix instances** across 1 dataset(s); language(s): go.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| multi-swe-bench | 15 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `rest/server.go` | 4 |
| `core/mapping/unmarshaler.go` | 3 |
| `rest/engine.go` | 3 |
| `go.sum` | 2 |
| `zrpc/server.go` | 2 |
| `go.mod` | 2 |
| `core/collection/timingwheel.go` | 1 |
| `core/logx/fields.go` | 1 |
| `core/logx/writer.go` | 1 |
| `core/logc/logs.go` | 1 |
| `rest/handler/tracinghandler.go` | 1 |
| `core/jsonx/json.go` | 1 |
| `zrpc/internal/serverinterceptors/statinterceptor.go` | 1 |
| `rest/types.go` | 1 |
| `zrpc/internal/client.go` | 1 |
| `zrpc/client.go` | 1 |
| `zrpc/internal/rpcserver.go` | 1 |
| `rest/handler/recoverhandler.go` | 1 |
| `core/logx/durationlogger.go` | 1 |
| `core/logx/tracelogger.go` | 1 |
| `core/logx/config.go` | 1 |
| `rest/handler/loghandler.go` | 1 |
| `core/logx/logs.go` | 1 |
| `tools/goctl/util/ctx/gomod.go` | 1 |
| `tools/goctl/util/ctx/gopath.go` | 1 |
| `tools/goctl/util/path.go` | 1 |
| `core/discov/publisher.go` | 1 |
| `zrpc/internal/rpcpubserver.go` | 1 |
| `core/discov/internal/registry.go` | 1 |
| `core/discov/config.go` | 1 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: **

Sample FAIL_TO_PASS test names (first 10):
```
```

## Section 4 — Problem-theme distribution

Top themes across 15 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|

## Section 5 — Sample issues (no patches — those are the answer)

## Section 6 — Builder guidance

When building a fix for an instance in zeromicro/go-zero:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. rest/server.go appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 15 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "zeromicro/go-zero"`).

First 20 instance_ids:

- `zeromicro__go-zero-2787` (dataset: `multi-swe-bench`)
- `zeromicro__go-zero-2537` (dataset: `multi-swe-bench`)
- `zeromicro__go-zero-2463` (dataset: `multi-swe-bench`)
- `zeromicro__go-zero-2363` (dataset: `multi-swe-bench`)
- `zeromicro__go-zero-2283` (dataset: `multi-swe-bench`)
- `zeromicro__go-zero-2116` (dataset: `multi-swe-bench`)
- `zeromicro__go-zero-2032` (dataset: `multi-swe-bench`)
- `zeromicro__go-zero-1969` (dataset: `multi-swe-bench`)
- `zeromicro__go-zero-1964` (dataset: `multi-swe-bench`)
- `zeromicro__go-zero-1907` (dataset: `multi-swe-bench`)
- `zeromicro__go-zero-1821` (dataset: `multi-swe-bench`)
- `zeromicro__go-zero-1783` (dataset: `multi-swe-bench`)
- `zeromicro__go-zero-1456` (dataset: `multi-swe-bench`)
- `zeromicro__go-zero-990` (dataset: `multi-swe-bench`)
- `zeromicro__go-zero-964` (dataset: `multi-swe-bench`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
