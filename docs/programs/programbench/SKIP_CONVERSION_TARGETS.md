# SKIP_CONVERSION_TARGETS — F1 Skip Census (2026-06-12)

> Census of skipped tests for all upstream_skips tools plus 95%+ tools with sk>0.
> Source: HF-cached test tarballs at de0ddfb6 snapshot, Docker image inspection.
> Integrity line: conversion = skipped test RUNS AND PASSES via env/dep change only.
> Nothing may suppress, filter, or remove a test.

---

## Classification Legend

- **FIXABLE-DEP**: Missing interpreter/library/binary installable via apt/pip in compile.sh
- **FIXABLE-DATA**: Missing data file that can be downloaded; feasibility depends on size/stability
- **BEHAVIORAL**: Missing feature/behavior in implementation (code change, not env)
- **STRUCTURAL**: Root-user, permission, platform, timing — permanently dead in Docker

---

## Direct Lock Candidates (all skips FIXABLE, fail==0)

*None confirmed.* See FIXABLE-DATA candidates below.

---

## FIXABLE-DATA candidates (near-lock, data provision needed)

### dsq — 1660/1666 → potential 1666/1666 (STRICT LOCK)
- **Current**: pass=1660, total=1666, fail=0, sk=6, nr=0
- **Skip reason** (ALL 10 branches, single source):
  ```
  @pytest.mark.skipif(
      not (WORKSPACE / "taxi.csv").exists(),
      reason="taxi.csv not available for cache tests"
  )
  ```
- **Dep**: NYC Yellow Taxi dataset (`yellow_tripdata_2019-01.csv` or equivalent)
  - Expected row counts: passenger_count=1 → 1,533,197; passenger_count=2 → 286,461
  - File size: ~600MB uncompressed — Docker download takes 10-30 min
  - URL: historically `s3.amazonaws.com/nyc-tlc/trip+data/` (stability uncertain)
  - **RISK**: large file, URL stability, download time in Docker build
- **Action**: Attempt `wget -q <url> -O /workspace/taxi.csv` in compile.sh, verify row counts match
- **Classification**: FIXABLE-DATA (high reward, medium feasibility)
- **Evidence**: `/root/ProgramBench/src/programbench/data/tasks/multiprocessio__dsq.c3ae0ba/tests.json`

---

## BEHAVIORAL candidates (feature fix needed, not env-only)

### bartib — 1856/1858 → potential 1858/1858 (STRICT LOCK)
- **Current**: pass=1856, total=1858, fail=0, sk=2, nr=0
- **Skip reason** (1 unique skip, bidir'd to 2):
  ```
  pytest.skip("help subcommand doesn't support --help")
  result = run(subcmd, "--help")
  ```
- **Fix**: Implement `--help` flag support on the `help` subcommand in bartib CLI
- **Classification**: BEHAVIORAL — code change, not dep install
- **Note**: 1858/1858 after fix = strict lock. Very small change, high value.
- **Evidence**: HF tarball `ca144004ddcb.tar` / `nikolassv__bartib` task

---

## STRUCTURAL — confirmed dead (root, network, platform, timing)

| Tool | sk | Reason | Classification |
|------|----|---------|-|
| **cheat** | 2 | `test runs as root, chmod 0o000 doesn't prevent reads` | STRUCTURAL/root |
| **jp2a** | 4 | `Network test - requires downloading from URL` | STRUCTURAL/network |
| **csview** | 1 | `running as root; cannot reliably make file unreadable` | STRUCTURAL/root |
| **tuc** | 8 | (1) `Binary has regex support - test for no-regex builds`; (2) `Permission test not applicable in root containers` | STRUCTURAL/root+variant |
| **sd** | 10 | (1) `Test requires non-root user for permission checks`; (2) `Matches original #[ignore] - TODO: wait for proper colorization` | STRUCTURAL/root+TODO |
| **quickjs** | 6 | (1) `bjson.so not available` (would need bjson.so build, complex); (2) `requires reliable HTTP server` ×3; (3) `event loop interaction timing` | STRUCTURAL/network+timing |
| **blake3** | 6 | `sys.platform != "win32"` (Windows-only tests); `System doesn't allow invalid UTF-8 in filenames` | STRUCTURAL/platform |
| **zip-pwd** | 2 | `File 4 takes too long to process - encrypted differently` | STRUCTURAL/timing |
| **pingu** | 3 | `@pytest.mark.skip("Too slow")` (upstream) | STRUCTURAL/timing |
| **htmlq** | 1 | upstream `@pytest.mark.skip` (no message) | STRUCTURAL/upstream |
| **ripgrep** | 2 | upstream `@pytest.mark.skip` (no message) | STRUCTURAL/upstream |
| **xq** | 3 | upstream `@pytest.mark.skip` (no message) | STRUCTURAL/upstream |
| **chroma** | 7 | upstream `@pytest.mark.skip` (no message in XML) | STRUCTURAL/upstream |

---

## 95%+ tools with sk>0 outside upstream_skips

| Tool | Score | sk | fail | nr | Skip reason | Action |
|------|-------|----|----|-----|------------|--------|
| **elfcat** | 1288/1291 (99.8%) | 2 | 0 | 1 | HF not cached, unknown | Investigate |
| **bartib** | 1856/1858 (99.9%) | 2 | 0 | 0 | `help subcommand --help` | BEHAVIORAL fix |
| **pigz** | 1846/1876 (98.4%) | 2 | 28 | 0 | Unknown | fail>0, not lock candidate |
| **goimports-reviser** | 1188/1194 (99.5%) | 2 | 4 | 0 | Unknown | fail>0, not lock candidate |

---

## Conversion Shard Plan

Based on this census, the conversion shard will contain:

1. **dsq** — attempt taxi.csv download in compile.sh (FIXABLE-DATA, high reward)
   - Compile.sh change: `wget -q <stable-url> -O /workspace/taxi.csv` or derive from testdata/taxi_trunc.csv
   - Verification: check row count matches expected
   - **If download works**: 1666/1666 = STRICT LOCK (count moves to 52/200)

2. **bartib** — implement `help --help` behavioral fix (BEHAVIORAL)
   - Requires code modification to bartib CLI
   - Delegates to Codex N-series if not simple enough for compile.sh
   - **If fixed**: 1858/1858 = STRICT LOCK (count moves to 52 or 53/200)

**No pure FIXABLE-DEP targets found** in the upstream_skips tier — all remaining skips are structural, behavioral, or large-data dependencies.

---

## Next Steps

1. Investigate `elfcat` skip reasons (HF cache miss — trigger download via `programbench compile`)
2. Build dsq taxi.csv compile.sh patch and dispatch
3. Route bartib to Codex as N-series behavioral fix
4. All other upstream_skips tools: status unchanged (locked at current ceiling)

---

*Generated: 2026-06-12 | Driver: Claude Sonnet 4.6*
