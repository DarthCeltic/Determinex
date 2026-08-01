# CEILING CERTIFICATION: tuc (riquito__tuc)

**Tier:** T2 ceiling_certified  
**Eval:** 2490/2498 (sk=8, fail=0, nr=0)  
**Certified:** 2026-06-12, Driver (Claude Sonnet 4.6)

## Per-Skip Analysis

### Skip 1: eval/tests/test_harvest.py:589 (×2 with bidir)
**Reason string:** "Binary has regex support - this test is for no-regex builds"  
**Structural rationale:** The tuc upstream project has two build configurations:
regex-enabled (default Rust feature flags) and no-regex (compiled without the regex
dependency). PB generated test fixtures against the no-regex build specifically to test
tuc's behavior when regex features are absent. Our binary is compiled with regex support
(the standard configuration), so these no-regex-path tests are skipped unconditionally
by the conftest. Compiling without regex would break the majority of tuc's functionality
and all other passing tests; this is a mutually exclusive build choice.  
**Reference-parity:** Guaranteed — the skip fires based on the binary's regex capability,
which is a fixed build-time property. The PB reference binary (no-regex build) passes
these, but a regex-enabled build always skips them. Our ceiling is on the regex-enabled build.

### Skip 2: eval/tests/test_harvest.py:600 (×2 with bidir)
**Reason string:** "Binary has regex support - this test is for no-regex builds"  
**Structural rationale:** Same mechanism as Skip 1. Different test function covering
another no-regex-specific code path.  
**Reference-parity:** Same as Skip 1.

### Skip 3: eval/tests/test_harvest.py:611 (×2 with bidir)
**Reason string:** "Binary has regex support - this test is for no-regex builds"  
**Structural rationale:** Same mechanism as Skip 1 and 2.  
**Reference-parity:** Same as Skip 1.

### Skip 4: eval/tests/test_input_advanced.py:410 (×2 with bidir)
**Reason string:** "Permission test not applicable in root containers"  
**Structural rationale:** ProgramBench Docker runs as root (uid=0). This test verifies
error handling for unreadable input files, which requires non-root file permission
enforcement. Root bypasses `chmod 000` unconditionally — no tuc binary implementation
can trigger a "permission denied" error from root in Docker.  
**Reference-parity:** Guaranteed — root-user skip applies to all binaries under PB Docker eval.

## Ceiling Verdict

All 8 skips (4 unique × bidir) are structural: 3 no-regex-build skips (binary build
configuration is a fixed compile-time choice that cannot satisfy both regex and no-regex
test paths simultaneously) and 1 root-user permission skip. No compile.sh or binary
change resolves any of these without editing PB test fixtures.

**tuc ceiling = 2490/2498.** Structurally confirmed.
