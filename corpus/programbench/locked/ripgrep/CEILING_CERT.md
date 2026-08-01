# CEILING CERTIFICATION: ripgrep

**Tier:** T2 ceiling_certified  
**Eval:** 2536/2538 (sk=2, fail=0, nr=0)  
**Certified:** 2026-06-12, Driver (Claude Sonnet 4.6)  
**Parity evidence:** `corpus/programbench/parity_artifacts/ripgrep/parity_evidence.md`  
**Parity verdict:** STRUCTURAL_BY_PROOF (skip 1) + HARNESS_INVARIANT (skip 2)

## Per-Skip Analysis

### Skip 1: tests.test_walk_errors.test_files_with_no_read_permission_as_non_root
**Reason string:** "Test requires non-root user (root bypasses permissions)"  
**Source:** `/workspace/eval/tests/test_walk_errors.py:502`  
**Structural rationale:** ProgramBench Docker containers run as root. The `chmod 0o000` call
that the test uses to make a file unreadable does not work when the process runs as root —
root bypasses POSIX file permissions. This is a kernel-level invariant. No binary or
compile.sh change can make a root process unable to read a chmod-restricted file.
The test uses `@pytest.mark.skip` with an unconditional condition.  
**Reference-parity:** Structural by proof — any binary (including the PB reference binary)
will trigger this skip when the eval container runs as root. The skip is not a binary
capability check; it's an OS permission check that always fails for root.

### Skip 2: eval.tests.test_rg_behavior.test_line_number_default_and_no_filename_behavior
**Reason string:** "test_line_number_default_and_no_filename_behavior depends on test_basic_recursive_search"  
**Source:** `/usr/local/lib/python3.10/dist-packages/pytest_dependency.py:101`  
**Structural rationale:** This is a pytest_dependency harness artifact in the bidir-injected
`eval.tests.*` namespace. The test `test_basic_recursive_search` **passed** in the
`eval.tests.*` namespace (confirmed in eval_report.json), but the pytest_dependency plugin
resolves dependency IDs using the short name `test_basic_recursive_search` — which does not
match the fully-qualified `eval.tests.test_rg_behavior.test_basic_recursive_search` node ID.
The dependency lookup fails even though the dependency test passed. The `tests.*` namespace
version of this test ran and passed independently. This is a bidir-namespace/pytest_dependency
interaction, not a binary capability failure. The skip is deterministic for this eval
configuration.  
**Reference-parity:** Harness invariant — the reference binary would also trigger this skip
because the skip is caused by the pytest_dependency ID resolution in the bidir namespace, not
by the binary's output. Confirmed: the `tests.*` counterpart of this test passes for our
implementation, confirming the binary behavior is correct.

## Ceiling Verdict

Both skips are environment/harness constraints independent of binary capability:
- Skip 1: root Docker invariant (OS permission bypass — structural)
- Skip 2: pytest_dependency namespace resolution artifact (bidir harness — deterministic)

**ripgrep ceiling = 2536/2538.** Structurally confirmed.

No binary or compile.sh modification can cause either test to run in this eval environment.
To unlock Skip 1: run eval as non-root (eval environment change, outside scope).
To unlock Skip 2: fix pytest_dependency resolution in bidir conftest (global harness change,
affects all tools with `@pytest.mark.depends` decorators).
