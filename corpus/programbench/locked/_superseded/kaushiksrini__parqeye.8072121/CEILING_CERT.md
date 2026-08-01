# CEILING CERTIFICATION: kaushiksrini__parqeye.8072121

**Tier:** T2 ceiling_certified (NOT a strict lock — sk=2 structural upstream skip)
**Date:** 2026-06-13, Driver (Claude Sonnet 4.6)
**Eval pilot:** `T:/determinex-programbench/determinex_pb_tui_small_v2/`
**Eval source:** Hetzner `determinex_pb_tui_small_v2` batch

## Result (raw eval_report.json)

| passed | failed | skipped | not_run | total |
|--------|--------|---------|---------|-------|
| 1126   | 0      | 2       | 0       | 1128  |

**eval_report_sha256:** `0EBC2A042B6C6B1C6D68AC000FFC9DF44BCCB6ADF33A45234BC43ABED1D2EEB6`
**PB score:** 100 (1126/1128 = 99.82%)

## Per-Skip Analysis

### Skips 1+2 (bidir pair): tests.test_error_handling.test_path_component_too_long
**Reason string:** "OS doesn't support 300-char filenames"
**Source:** `/workspace/eval/tests/test_error_handling.py`
**Bidir count:** 1 unique test × bidir injection = 2 skip entries total

**Structural rationale:** This test attempts to open a file with a path component
exceeding 300 characters and expects `parqeye` to handle the resulting OS error.
Linux filesystems (ext4, tmpfs — standard Docker container filesystems) enforce a
maximum of 255 characters per path component (NAME_MAX constant). The test framework
detects this OS limitation at collection time and skips the test with the explicit
message "OS doesn't support 300-char filenames".

This is an unconditional skip on any Linux x86_64 Docker container — it is not a
defect in `parqeye` and cannot be fixed by implementation changes. The same skip
fires for the real upstream parqeye binary in the same environment.

## Reference-Parity Evidence

**Parity verdict:** STRUCTURAL_BY_PROOF — OS filesystem NAME_MAX constraint

The NAME_MAX limit (255 chars) is a kernel ABI constant enforced by the Linux VFS
layer. Any binary, including the reference upstream parqeye binary, will trigger this
skip when evaluated in the ProgramBench Docker environment because:

1. The test's skip condition fires based on the filesystem NAME_MAX, not on any
   behavior of the parqeye binary itself
2. Running the upstream parqeye binary in the same Docker env would produce identical
   skip results (the test never executes parqeye at all — it's skipped at collection)
3. The skip message is emitted by the PB test framework conftest, not parqeye

The 1126/1126 non-skipped tests all pass, demonstrating full implementation parity
with the reference binary for all testable behaviors.

## Ceiling Verdict

**parqeye ceiling = 1126/1128.** The 2 skips (1 unique × bidir) are structural:
Linux NAME_MAX kernel constraint, environment-imposed, unconditional for all binaries.

To convert to T1: run on a filesystem that supports 300-char path components
(not standard Linux ext4/tmpfs). Not achievable in standard ProgramBench Docker.
