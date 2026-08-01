---
name: jq-corpus-impact
description: What completing jq teaches the Determinex Oracle, what future tasks accelerate, and the compounding it produces with prior locks (zoxide, yj, ripsecrets) and prior in-progress (htmlq, shellharden, csview, dutree).
type: corpus-impact
---

# jq — Corpus Impact

## What this teaches the Oracle

The compiler oracle (the only judge in Determinex) gains five labelled-failure categories specific to *interpreter-style tools* once jq is solved end-to-end:

1. **Stream-evaluator failure pairs** (`evaluator.py`)
   - Wrong yield count (1 instead of N) on `Comma`/`Iterate`
   - Eager evaluation where laziness was needed (`first`, `limit`, `until`)
   - Closure capture lost across pipe stages
   These become *exact* (broken eval, fix) training pairs in the WAL — the highest-quality flywheel signal possible because the compiler/probe pinpoints them at test resolution.

2. **JSON formatting failure pairs** (`json_io.py`)
   - Number precision mismatches
   - Surrogate-pair handling
   - Whitespace/indent disagreements
   These transfer directly to **every JSON-emitting tool in the bench** (gron, fx, dsq, trdsql, htmlq's `--pretty` mode) — and beyond the bench, to any tool that reads/writes JSON in the broader corpus.

3. **Path-expression failure pairs** (`paths.py`)
   - Path tracking through assignment operators
   - `del` with overlapping paths
   These are uncommon in the wild but **highly testable** in PB — capturing them gives the Oracle ammo for future stateful-data-walker tools.

4. **Builtin-arity failure pairs** (`builtins.py`)
   - `f/0` vs `f/1` vs `f/2` dispatch errors
   - Optional-flag-arg builtins (regex with optional flags)

5. **CLI flag-combination failure pairs**
   - Conflict resolution (`--tab` vs `--indent N`)
   - Order-dependent flags (`-r -e` vs `-e -r`)

## What this makes faster beyond the immediate cluster

- **All future tools built in Python with stdin/stdout streaming**: the build-script template (`compile.sh` with `chmod +x main.py && ln -s executable main.py`) becomes a known-good fixture. Future tasks reuse it without iteration.
- **All future tools that use Python's `re` module**: the `regex.py` wrapper gives per-test-flag mapping (i, x, s, g, m) that handles every PB test we'll see. Worth ~1 hour saved per regex-using tool.
- **All future tools that need JSON parsing**: `json_io.py` is the canonical answer (Python's stdlib `json` is too lax for jq tests; ours is strict). Reuse forever.
- **All future tools with the "stream of values, transform pipeline" architecture**: the eval-as-generator skeleton is a 60-LOC template that fits any DSL.

## Compounding with already-locked tools

| Locked tool | Compounding effect from jq |
|-------------|----------------------------|
| **zoxide**     | None direct; zoxide's `query` mode does ranked path-matching, but the stream/eval model doesn't apply. |
| **yj**         | yj's JSON branch becomes a 1-line wrapper around `json_io.py`. Reduces yj's surface area to YAML/TOML conversion only — those parsers are already locked, so yj's regression risk drops to near-zero. |
| **ripsecrets** | None direct; ripsecrets is pattern-search-over-files (fd cluster shape). |

## Compounding with currently in-progress tools

| In-progress tool | Current % | Lift from jq lock |
|------------------|-----------|--------------------|
| **htmlq**        | 91.6%     | **Significant.** htmlq's remaining 2.3% gap is almost entirely the "stream of values from selector" model — exactly jq's `evaluator.py` pattern. Port `stream.py` after jq locks → expected lift to 96-98% in 1-2 attempts. The final 2-4% is CSS-selector-edge-case territory and unrelated. |
| **shellharden**  | 87/100    | None (fd/shell-lexer cluster). |
| **csview**       | ~81%      | **Indirect.** csview will benefit from xsv's CSV adapter, which is built on jq's stream model. Expected lift after jq → xsv → csview chain: 4-6 percentage points. |
| **dutree**       | ~54%      | None (fd cluster). |

## Training data emitted

Per attempted-and-locked jq build session, the WAL emits:
- ~1 spec
- ~6-12 attempts × {generated patch, compile errors, test-suite failures, observer diagnosis, fix patch} = **6-12 (error → fix) training pairs**
- 1 final compiler-validated artifact

For a 6,796-test target with an estimated 8 attempts, that's **~50-70 high-quality training rows** entering the corpus from a single anchor lock. At 5 anchors that's ~300 rows of *highest-quality compiler-validated training data* — more than the current entire `2,182-row` real-code-gen baseline (per `project_corpus_reality`).

## Strategic value

**jq is the single highest-value training-corpus addition Determinex can make.** Justification:
1. Largest test surface in the bench (6,796 tests = highest density of compiler-verifiable failure categories).
2. Cluster transfer is direct (not partial) for 5 of 7 unlocks — very high reusability of the artifact.
3. The fixture (stream evaluator + JSON I/O) is genuinely *general* — usable for any future filter-language or stream-transform tool, far beyond ProgramBench.
4. Training pairs are unambiguous: each compiler/probe failure has exactly one source-of-truth fix in the reference jq behaviour.

## Action when locked

1. Move artifact from `T:/determinex-programbench/<run>/jqlang__jq.b33a763/source/` into `corpus/programbench/locked/jq/`.
2. Extract reusable modules to `corpus/programbench/_lib/{stream,json_io,regex,paths}.py`.
3. Append the WAL training pairs to `data/programbench_corpus.jsonl` (new file, parallel to `builder_extra*.jsonl`).
4. Update `corpus/programbench/README.md` status board.
5. Run smoke-test on htmlq using new `_lib/stream.py` — confirm projected lift to 96%+.
6. Commit with tag `programbench-anchor-1-locked`.
