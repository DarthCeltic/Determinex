# CEILING CERTIFICATION: htmlq

**Tier:** T2 ceiling_certified  
**Eval:** 2057/2058 (sk=1, fail=0, nr=0)  
**Certified:** 2026-06-12, Driver (Claude Sonnet 4.6)

## Per-Skip Analysis

### Skip 1: eval/tests/test_15_final_massive_push.py:35
**Reason string:** "Incompatible flags"  
**Structural rationale:** The PB test at line 35 exercises a combination of htmlq flags
that are documented as mutually exclusive or incompatible by the upstream htmlq project.
The test is marked skip because the behavior is undefined (the upstream tool may error,
panic, or produce arbitrary output). This is a test design exclusion — the PB authors
chose not to assert on behavior the upstream binary itself does not define. No binary
implementation of htmlq can define a stable, testable behavior for truly incompatible
flag combinations without changing the upstream API contract.  
**Reference-parity:** Guaranteed — the skip fires unconditionally regardless of binary
behavior (the `@pytest.mark.skip` annotation is not conditioned on binary output).

## Ceiling Verdict

The 1 skip is an unconditional PB test design exclusion for undefined/incompatible
flag behavior. No compile.sh or implementation change converts it to a passing test.

**htmlq ceiling = 2057/2058.** Structurally confirmed.
