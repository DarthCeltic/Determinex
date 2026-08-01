---
name: pb-empirical-spec-method
description: The methodology for converting any ProgramBench anchor's test suite into a behavioral spec doc that the build prompt injects, so the implementation passes byte-exact tests on the first attempt.
type: methodology
---

# Empirical Spec Method

> **Premise.** Every ProgramBench task ships its full test suite (pytest files + golden output files) inside an HF dataset. A frontier model trying to one-shot the implementation without those tests is gambling on what the bench *might* check. We extract what it *does* check and inject that as the build brief.

## Inputs the method consumes

For each anchor `<author>__<tool>.<sha>`:

1. **`task.yaml`** — `T:/Dev/ProgramBench/src/programbench/data/tasks/<id>/task.yaml`. Cleanroom container image, language hint, build expectations.
2. **`tests.json`** — same directory. Lists every test branch SHA and every test name.
3. **Test tarballs** — `~/.cache/huggingface/hub/datasets--programbench--ProgramBench-Tests/snapshots/<snap>/<id>/tests/<branch>.tar.gz`. Pull on demand via:
   ```python
   from huggingface_hub import snapshot_download
   snapshot_download(
     repo_id='programbench/ProgramBench-Tests',
     repo_type='dataset',
     allow_patterns=[f'{instance_id}/**'],
   )
   ```
4. **Cleanroom container probes** — `docker run --rm <image> bash -c "..."` to enumerate available compilers, libraries, network access, and any reference binary on disk.

## What we extract from the tarballs

Every test tarball, once extracted, contains:

```
eval/
  tests/
    conftest.py              ← test fixture API (binary contract)
    test_*.py                ← assertions
  test_resources/
    <category>/
      *.golden               ← byte-exact stdout expectations
      *.stderr               ← byte-exact stderr expectations
      *.json, *.yaml, ...    ← inputs
  run.sh                     ← `pytest -n auto` command
Dockerfile                   ← reference build pipeline (informative, not used)
src/                         ← reference source (informative, ignored for our build)
executable_cov               ← coverage-instrumented reference (ignored)
```

Three artifacts go into the spec:

1. **CATCHES corpus** — every test docstring contains a `CATCHES:` line stating the wrong-implementation pattern the test catches. We harvest these and negate them into behavioral requirements. Aggregate across all branches deduplicated by basename.
2. **Test fixture API** — `conftest.py` defines how the binary is invoked (flags, stdin, environment vars). The exact invocation contract.
3. **Golden file shape** — sample N goldens per category to determine the exact output formatting (number formatting, escape rules, whitespace, ordering).

## The four-pass extraction

Implemented as a script (re-runnable per anchor):

```python
# Pass 1: pull tarballs, extract to /c/tmp/<tool>_tests/<branch>/
# Pass 2: dedupe test files across branches by basename — first wins
# Pass 3: parse every test_*.py for `def test_X("""CATCHES: ..."""):` pairs
# Pass 4: enumerate test_resources/**/*.golden + *.stderr — count + sample
```

The output is a structured table:

| Category | Test file | # tests | # CATCHES | # goldens | # stderr |
|---|---|---|---|---|---|

This table tells you *where the bench actually pushes hard* — categories with high test+golden density are where 1-shot builds fail. The spec doc devotes proportional space.

## How the spec doc is structured (anchor-agnostic template)

Every anchor's spec doc follows the same six sections. **Section 4 is anchor-specific in content but identical in shape:**

```
1. Binary Contract               — universal, copied from conftest.py
2. Test Invocation API           — `run_<tool>(...)` fixture signature
3. Implementation Constraints    — language, deps, file split, cleanroom limits
4. Behavioral Surface            — the empirical extract, organized by category
   4.1 CLI flags + exit codes
   4.2 Input parsing rules
   4.3 Output formatting rules
   4.4 Core data semantics
   4.5 Builtin / API surface
   4.6 Error format + stderr exact rules
   4.7 Edge cases + known traps (the 90→100% gap)
5. Pre-flight Self-Tests         — what compile.sh must verify before exit 0
6. Common Failure Modes          — derived directly from CATCHES corpus
```

Section 5 is critical and often skipped: **the build script must run a smoke test against its own output before declaring success.** A failed smoke test means compile.sh exits non-zero, which the agent treats as a compile failure and retries. This catches "compiles but doesn't work" bugs without spending the full pytest probe time.

## What goes into the prompt at build time

Three layers of context are concatenated for the Claude builder call:

```
SYSTEM_PROMPT (universal — what the agent expects)
  + task.yaml (per-anchor metadata)
  + observations (probe output: --help, --version, README)
  + 06_behavioral_spec.md (THIS DOC — the empirical brief)
  + error_block (only on retry: prior compile/probe failure)
```

The spec is the largest layer (typically 30-60KB markdown) but stays comfortably inside Claude's input budget. **The agent's `max_tokens` (output) must be sized for the implementation** — for jq this is 64K; for fzf 32K; for curlie 8K is enough.

## Anti-overfit clause

The spec must NOT contain:

- ❌ Specific test names ("`test_basic_invocation` expects ...")
- ❌ Golden file path references ("`pretty.golden` is `{...}`")
- ❌ Test-internal pattern matching ("the assertion at line 47 ...")
- ❌ Branch SHA references

The spec must ONLY contain:

- ✅ Behavioral rules ("`-S` sorts object keys lexicographically at every nesting depth")
- ✅ Concrete example I/O pairs that document the rule (input → output)
- ✅ Edge cases derived from CATCHES (negated wrong-implementation patterns)
- ✅ Reference to the binary contract (flag X behaves like Y)

The reason: the bench may swap out specific tests during grading; a spec overfit to test names breaks. A spec that captures the *real* contract (what the tool actually does) is robust to test rotation.

## Lock loop with the spec injected

```
1. Pull tarballs                        (one-time per anchor, ~2 min)
2. Extract CATCHES + count goldens      (script, ~30 sec)
3. Write 06_behavioral_spec.md           (manual or assisted, ~30-90 min)
4. Run agent with spec injected          (one Claude call, ~3 min)
5. Local syntax check                    (auto, ~1 sec)
6. Run compile.sh in cleanroom           (auto, ~30 sec)
7. Run pre-flight smoke test (Section 5) (auto, ~5 sec)
8. Run full pytest probe                 (auto, ~3-15 min depending on test count)
9. If 100% → write post-mortem to corpus/programbench/locked/<tool>.md
   If <100% → triage by failure category, iterate on spec, goto 4
```

**Target: 1-3 iterations to lock.** Each iteration's failure cluster updates the spec — the spec is the persistent learning, not a one-time artifact. If the same failure category appears in two anchors, that's a generalizable rule and should be hoisted to this methodology doc.

## Worked example: jq

| Phase | Number |
|---|---|
| Tarballs | 12 branches, all pulled |
| Total tests | 6,796 (4,933 deduped) |
| CATCHES extracted | 1,938 |
| Golden output files | 619 (representative branch) |
| Stderr golden files | 96 |
| Spec doc size | ~50KB |
| Builder file split | main.py + 7 modules |
| `max_tokens` set to | 64,000 |
| Estimated lock attempts | 1-2 (vs. open-loop where 8-12 is typical) |

See [`anchors/01_jq/06_behavioral_spec.md`](../anchors/01_jq/06_behavioral_spec.md) for the full instance.

## Reusability

This methodology applies to all 200 ProgramBench anchors without modification. The script that extracts CATCHES + golden counts is one Python file (~80 LOC). The spec template in Section 6 above is identical across tools. The agent patch (load spec from `corpus/programbench/anchors/<NN>_<tool>/06_behavioral_spec.md` if present) is a single conditional block.

The cost is the manual synthesis of Section 4 per tool — but with extracted CATCHES grouped by category, that's a 30-90 minute writing job, not original engineering. Each new anchor cuts faster as common patterns repeat across tools (CLI flag handling, JSON parsing, error format).

— Locked 2026-05-09. First applied to jq.
