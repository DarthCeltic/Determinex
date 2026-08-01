# CEILING CERTIFICATION: sd (chmln__sd)

**Tier:** T2 ceiling_certified  
**Eval:** 1728/1738 (sk=10, fail=0, nr=0)  
**Certified:** 2026-06-12, Driver (Claude Sonnet 4.6)

## Per-Skip Analysis

### Skip 1: eval/tests/test_harvest.py:217 (×2 with bidir)
**Reason string:** "Original test is ignored - TODO: wait for proper colorization"  
**Structural rationale:** The PB test authors placed an upstream TODO annotation on this
test because the expected colorization output from sd depends on terminal color support and
ANSI detection that varies by environment. The test is hardcoded-skipped pending a stable
colorization oracle. This is a test design exclusion in PB source — no sd binary
implementation or compile.sh change removes the TODO skip without modifying the test fixture.  
**Reference-parity:** Guaranteed — unconditional `@pytest.mark.skip` with TODO, fires for any binary.

### Skip 2: eval/tests/test_harvest.py:330 (×2 with bidir)
**Reason string:** "Test requires non-root user for permission checks"  
**Structural rationale:** ProgramBench Docker containers run as root (uid=0). This test
verifies sd's behavior when it cannot read a file (permission denied). As root, `chmod 000`
does not prevent file access. No binary or compile.sh change affects the container user
identity; this is an OS-level invariant.  
**Reference-parity:** Guaranteed — root-user skip applies to all binaries under PB Docker eval.

### Skip 3: eval/tests/test_harvest.py:374 (×2 with bidir)
**Reason string:** "Test requires non-root user for permission checks"  
**Structural rationale:** Same mechanism as Skip 2 (different test function, identical
root-user constraint).  
**Reference-parity:** Guaranteed — same as Skip 2.

### Skip 4: eval/tests/test_cli.py:161 (×2 with bidir)
**Reason string:** "root bypasses file permission restrictions"  
**Structural rationale:** Same root-user environment constraint as Skip 2, in a different
test file. Tests file-permission-based error handling that is unreachable when running as root.  
**Reference-parity:** Guaranteed — same as Skip 2.

### Skip 5: eval/tests/test_cli.py:186 (×2 with bidir)
**Reason string:** "root bypasses file permission restrictions"  
**Structural rationale:** Same root-user environment constraint as Skip 2 and 4.  
**Reference-parity:** Guaranteed — same as Skip 2.

## Ceiling Verdict

All 10 skips (5 unique × bidir) are structural: 1 upstream TODO skip and 4 root-user
environment skips. None can be resolved by binary or compile.sh changes without either
modifying PB test fixtures or changing the Docker container user (both outside scope).

**sd ceiling = 1728/1738.** Structurally confirmed.
