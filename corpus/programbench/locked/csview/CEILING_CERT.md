# CEILING CERTIFICATION: csview

**Tier:** T2 ceiling_certified  
**Eval:** 347/348 (sk=1, fail=0, nr=0)  
**Certified:** 2026-06-12, Driver (Claude Sonnet 4.6)

## Per-Skip Analysis

### Skip 1: eval/tests/test_csview_io.py:96
**Reason string:** "running as root; cannot reliably make file unreadable"  
**Structural rationale:** ProgramBench Docker containers run all builds and evals as root
(uid=0). The test attempts `chmod 000` on a file and then verifies the binary reports an
error — but root bypasses Unix permission checks unconditionally. This is an OS invariant:
`os.geteuid() == 0` means `chmod 000` does not restrict root access. No binary
implementation can make root-user file-unreadability work in Docker without changing the
container user, which is outside compile.sh scope.  
**Reference-parity:** Guaranteed — the skip condition is `running as root`, which applies
identically to the PB reference binary and any implementation under test.

## Ceiling Verdict

The 1 skip is an environment constraint (Docker root user) that no compile.sh or binary
change can overcome. The test itself documents this explicitly with the skip reason.

**csview ceiling = 347/348.** Structurally confirmed.
