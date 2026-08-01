# CEILING CERTIFICATION: pingu

**Tier:** T2 ceiling_certified  
**Eval:** 416/419 (sk=3, fail=0, nr=0)  
**Certified:** 2026-06-12, Driver (Claude Sonnet 4.6)

## Per-Skip Analysis

### Skip 1: eval/tests/test_art_rendering.py:92
**Reason string:** "Too slow (45 pings); core wraparound logic tested in wraparound_at_20"  
**Structural rationale:** Unconditional `@pytest.mark.skip` annotation hardcoded in PB test
source. The skip is not conditioned on binary behavior — it fires regardless of which
pingu binary is under test. 45 sequential pings would exceed CI time budgets universally.
The PB test authors explicitly noted the core logic is covered by the `wraparound_at_20`
test, making this skip intentional and permanent.  
**Reference-parity:** Guaranteed — unconditional skip fires for any binary, including the
PB reference binary used to generate fixtures.

### Skip 2: eval/tests/test_art_rendering.py:108
**Reason string:** "Too slow (105 pings); core wraparound logic tested in wraparound_at_20"  
**Structural rationale:** Same mechanism as Skip 1. 105 pings would take ~10 seconds
minimum in any container environment. Unconditional skip, independent of binary behavior.  
**Reference-parity:** Guaranteed — unconditional, same as Skip 1.

### Skip 3: eval/tests/test_art_rendering.py:406
**Reason string:** "Too slow (45 pings); core wraparound logic tested in wraparound_at_20"  
**Structural rationale:** Same mechanism as Skip 1. Different test function, same
performance-based exclusion. No compile-time or runtime change to the pingu binary
affects this skip.  
**Reference-parity:** Guaranteed — unconditional, same as Skip 1.

## Ceiling Verdict

All 3 skips are unconditional `@pytest.mark.skip` annotations in ProgramBench test
source (test_art_rendering.py), placed there by PB test authors for performance
reasons. No compile.sh change, binary configuration, or runtime environment adjustment
can convert any of these skips to passing tests without editing the PB test fixture.

**pingu ceiling = 416/419.** The 3 skipped tests represent a test design choice (too-slow
exclusion), not a binary deficiency. This ceiling is mathematically confirmed.
