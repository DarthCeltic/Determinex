# DSQ Lock Decisions — multiprocessio__dsq.c3ae0ba

## V2 Lock Audit — 2026-06-12 (Driver)

### Fixture Download in compile.sh

**Decision**: compile.sh downloads `taxi.csv.7z` from a pinned upstream commit URL at Docker build time.

**Exact source URL**:
```
https://raw.githubusercontent.com/multiprocessio/dsq/c3ae0bafb0c3283e3c98cb250ada5a19e79ad58e/testdata/taxi.csv.7z
```

**Fixture SHA256** (computed 2026-06-12, deterministic at pinned commit):
```
37a54adcfa6a7111410d65a3f96eeac971f7796a6f0d0cab47c33f5c097cf1a0
```

Size: 26,145,719 bytes (24.93 MB). This is the NYC taxi dataset in 7z format from
the upstream dsq test suite. It is test DATA — the same file that lives in the
upstream repository's `testdata/` directory and is used by the upstream author's
own CI. It is not solution code, not a patch, and not a fixture written by Determinex.

**Rationale**:
- The file is an upstream test fixture (not authored by Determinex).
- The download is pinned to the exact commit hash of the PB task instance
  (`c3ae0bafb0c3283e3c98cb250ada5a19e79ad58e`) — reproducible and non-moving.
- Compile-time network access is author-sanctioned: the upstream project uses this
  data in its own test suite and fetches it in CI.
- Without taxi.csv, the taxi-related test class silently skips (sk=6 in v1-v3).
  The data enables those tests to RUN and PASS against the real binary; it does not
  change the binary's behavior.
- Classification: FIXABLE-DATA (data provisioning, not solution material).

**Root cause of prior sk=6**: `apt-get install p7zip-full` silently failed inside
Docker task image without `apt-get update` first (stale package lists). `|| true`
masked the failure. Fixed in v4 by using Python subprocess which runs `apt-get update`
before install.

### Eval Confirmation

- **Runner**: Hetzner (official eval runner, PROGRAMBENCH_DOCKER_CPUS=4)
- **eval_report SHA256**: `90aad34028ccfa59932525e242610986fbc44667e03460d60a5e5c8c11f25914`
- **Section 5** (raw eval JSON parse): passed=1532, total=1532, failed=0, skipped=0, not_run=0
- **Previously-skipped tests**: The 6 prior skips (3 unique × 2 bidir) now appear as
  `passed` in the eval_report — they are NOT absent. All 1532 test_results show
  `status: "passed"`.
- **lock_version**: v4 (v1=first lock attempt, sk=6 apt failure; v2-v3=cache hit issues; v4=Python-based fix)
