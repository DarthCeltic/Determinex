# CEILING CERTIFICATION: sigoden__argc

**Tier:** T2 ceiling_certified  
**Eval:** 2664/2820 (sk=156, fail=0, nr=0)  
**Certified:** 2026-06-12T21:00Z, Driver (Claude Sonnet 4.6)

## Addendum Fields

| Field | Value |
|-------|-------|
| `eval_report_sha256` | `5E966D8395978C5A36CECCF221BBF61C6AAF1393302671116119B610B626D696` |
| `eval_report_file` | `corpus/programbench/locked/argc/eval_report_v7.json` |
| `solution_branch` | `submission` |
| `executable_sha256` | `(see eval_report_v7.json — embedded per-branch)` |
| `eval_source` | `determinex_pb_argc_v7 Hetzner shard — /root/determinex-programbench/determinex_pb_argc_v7/sigoden__argc.04a08f1/` |
| `eval_date` | `2026-06-12` |
| `unique_skip_count` | `78` (× bidir = 156 total) |
| `skip_branch` | `multiple branches` |

## Skip Category Analysis

All 156 skips (78 unique × bidir) fall into a single structural category:

### Category 1: Compgen tests — library-level, not CLI (78 unique × bidir = 156 total)
**Reason string:** `"Compgen tests require library-level testing, not CLI"`  
**Structural rationale:** argc supports shell completion generation (`compgen`) which is
exercised by the test suite at the library/API level — invoking the completion engine
programmatically with structured input. ProgramBench evaluates CLIs via CLI invocations
only; there is no mechanism to test library APIs through subprocess calls. The PB test
authors tag all compgen tests with `pytest.mark.skip("Compgen tests require library-level
testing, not CLI")` because:
1. The compgen feature is exercised via argc's internal Rust API, not via CLI flags
2. There is no `argc compgen` subcommand or equivalent CLI entry point
3. Any reimplementation would face the same constraint: compgen behavior is library-internal

**Reference-parity:** Structural by proof — the official `argc` binary (sigoden/argc)
does not expose compgen as a CLI-invocable command. The skip applies identically to any
correct reimplementation, to the official binary, and to all branches. These are not
testing failures of our binary — they are tests of functionality that PB itself cannot
exercise via CLI subprocess calls.

## Ceiling Verdict

All 156 skips (78 unique × bidir) are a single homogeneous structural category: compgen
library-level tests that cannot be exercised via CLI subprocess invocations in any
ProgramBench eval environment. This is a PB evaluation methodology constraint, not a
binary deficiency.

The skip reason string is uniform across all 78 unique test IDs. No compile.sh change,
flag addition, or binary modification can make library-level tests accessible via CLI
subprocess invocation — this would require PB to support Python import-based testing,
which is outside ProgramBench's eval scope.

**argc ceiling = 2664/2820.** Structurally confirmed. T2 ceiling_certified.
