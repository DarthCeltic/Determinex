# CEILING CERTIFICATION: cslarsen__jp2a

**Tier:** T2 ceiling_certified  
**Eval:** 1424/1428 (sk=4, fail=0, nr=0)  
**Certified:** 2026-06-12T20:30Z, Driver (Claude Sonnet 4.6)

## Addendum Fields

| Field | Value |
|-------|-------|
| `eval_report_sha256` | `83ECE370C85A68DF9E1234FEAE6B5CB35F899046950727C8AE046395D26C0367` |
| `solution_branch` | `submission` |
| `executable_sha256` | `c0d5afe629949eb9c77154a4aa51363bd612d125927b8344243df15d88b6997c` |
| `eval_source` | `A4-CHASE Hetzner shard — /root/determinex-programbench/a4_chase_shard/cslarsen__jp2a.61d205f/` |
| `eval_date` | `2026-06-12` |
| `unique_skip_count` | `2` (× bidir = 4 total) |
| `skip_branch` | `878c75d1dc8f` |

## Per-Skip Analysis

### Skip 1: tests.test_harvest.test_curl_download_sourceforge (×2 with bidir)
**Test name:** `tests.test_harvest.test_curl_download_sourceforge`  
**Bidir counterpart:** `eval.tests.test_harvest.test_curl_download_sourceforge`  
**Branch:** `878c75d1dc8f`  
**Reason string:** `"Network test - requires downloading from URL, may be flaky in CI"`  
**Structural rationale:** PB Docker containers run in network-isolated environments
without reliable outbound HTTP access. This test downloads a jp2a source/image from a
SourceForge URL to exercise remote image processing capability. The skip is placed by
the PB test authors (unconditional `pytest.mark.skip`) because the download may fail
or be flaky in any CI/eval environment regardless of binary implementation. No compile.sh
or jp2a binary change provides network connectivity inside a network-isolated Docker
container. This is a PB author decision, not a binary deficiency.  
**Reference-parity:** Structural by proof — the network constraint applies identically to
the PB reference binary; the skip is a test design choice for CI stability. Any binary
(including the official jp2a release) will trigger this skip in network-isolated Docker.

### Skip 2: tests.test_harvest.test_curl_download_sf (×2 with bidir)
**Test name:** `tests.test_harvest.test_curl_download_sf`  
**Bidir counterpart:** `eval.tests.test_harvest.test_curl_download_sf`  
**Branch:** `878c75d1dc8f`  
**Reason string:** `"Network test - requires downloading from URL, may be flaky in CI"`  
**Structural rationale:** Same mechanism as Skip 1 — different URL (alternative SourceForge
mirror), same network-isolation constraint. Unconditional `pytest.mark.skip` by PB authors.  
**Reference-parity:** Structural by proof — same guarantee as Skip 1.

## Ceiling Verdict

All 4 skips (2 unique × bidir) are network-isolation environment constraints. PB Docker
eval containers cannot make outbound HTTP requests to arbitrary URLs. No binary or
compile.sh change can provide network connectivity.

The skip reason string `"Network test - requires downloading from URL, may be flaky in CI"`
is a PB author tag — used for tests that require external HTTP access. This tag category
is a known structural constraint category for ProgramBench evals (same pattern as
`tests.test_harvest.*` skips in other tools). Reference-parity is guaranteed.

**jp2a ceiling = 1424/1428.** Structurally confirmed. T2 ceiling_certified.
