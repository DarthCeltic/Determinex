# executors/ — Language-family executors

> One module per language family. Shared contract. Cockpit-aware lifecycle.
> Built 2026-05-13 as part of the Run-Ledger / Failure-Classifier / Patch-Advisor cockpit refactor.

## Why this exists

Before this directory, every benchmark build went through ad-hoc scripts that yelled across the room at each other (`mass_run_v2_scaffold.py`, `mass_run_v2_pack.py`, `programbench_image_preflight.py`, `programbench_eval_runner.py`). Each was correct in isolation, but together they had no single API. Adding a new language meant re-discovering the contract.

This directory makes the contract explicit. **Each executor owns the full lifecycle of one language family.** The cockpit (live monitor + patch advisor) talks to executors through a stable seven-phase API instead of stitching together CLI calls.

## The contract — seven phases

```
probe -> scaffold -> build -> pack -> eval -> classify -> report
```

Each phase is independently runnable and returns a structured result. Re-running a later phase does not redo earlier phases unless explicitly asked.

| Phase | Responsibility | Result type |
|---|---|---|
| **probe** | Read `task.yaml`, `tests.json`, upstream README; extract declared CLI surface, deps, test count | `ProbeResult` |
| **scaffold** | Write `source/{main.<ext>, compile.sh, README_DETERMINEX.md, probes/}` to a work dir | `ScaffoldResult` |
| **build** | Run `compile.sh`; produce `./executable` (real file, never a symlink) | `BuildResult` |
| **pack** | Tar `source/` → `submission.tar.gz` with deterministic mtimes/perms | `PackResult` |
| **eval** | Run programbench eval (or per-bench harness); write `<inst>.eval.json` | `EvalResult` |
| **classify** | Route eval JSON through `scripts/failure_classifier.py` central taxonomy | `ClassifyResult` |
| **report** | Markdown summary + recommendation handoff to the advisor | `ReportResult` |

Every phase writes a `LedgerEvent` so `scripts/programbench_live_monitor.py` sees the lifecycle in real time.

## The shared base

`executors/base.py` defines:

- `Executor` — the abstract base class with default `pack` / `classify` / `report` implementations (most languages don't need to override these)
- `ExecutorContract` — typing protocol so the orchestrator can duck-check any executor
- Result dataclasses (`ProbeResult`, `ScaffoldResult`, etc.) — JSON-serializable, stable across versions
- `ExecutorError` — single exception type all phases raise on terminal failure

## Languages — implementation order

Mapped to `corpus/programbench/_strategy/language_family_sprint_matrix.md`. Implementation priority follows the residual-tool language distribution (68 Rust, 28 Go, 13 C, 6 C++):

| Family | Default executable | Status | Notes |
|---|---|---|---|
| `python_executor.py` | `cp main.py executable` | next | Cheap. Default for unknown small tools. |
| `rust_executor.py` | `cargo build --release && cp target/release/<bin> executable` | next | Cold compile 90-180s, warm 8-20s. 68 of 115 residuals. |
| `go_executor.py` | `go build -o executable .` | next | 1-3s build. 28 of 115 residuals. |
| `c_executor.py` | `cc -O2 -o executable *.c` | next | 13 of 115 residuals. |
| `cpp_executor.py` | `c++ -O2 -std=c++17 -o executable *.cpp` | next | 6 of 115 residuals. |
| `node_executor.py` | `cp main.js executable` with shebang | later | For JS-origin CLIs. |
| `shell_executor.py` | `cp main.sh executable && chmod +x` | later | For wrappers / small filters. |
| `ruby_executor.py` | `cp main.rb executable` | later | Few residuals; CLI matters more than language. |
| `php_executor.py` | shell wrapper or executable PHP | later | Few residuals. |
| `java_executor.py` | `javac` + jar + launcher script | later | JVM warmup cost dominates. |

The remaining 15 families from the language-family sprint matrix (Kotlin, Scala, C#, PowerShell, R, Julia, Dart, Elixir, Haskell, Swift, etc.) ship after the top-5 plus Node/Shell are validated.

## Hard rules every executor must honor

1. `compile.sh` MUST produce a real `./executable` file, not a symlink. ProgramBench moves the file to `/opt/programbench-stashed-executable-do-not-modify` before hashing; symlinks break after the move.
2. Submission tarballs are packed from the source root: `tar -czf submission.tar.gz -C source .`
3. The `executable` must accept `--help`, `--version`, an unknown flag (with the family's canonical error wording), and an empty input — those four conditions account for ~40% of the test surface across all 157 residual ProgramBench tools.
4. Every phase writes a ledger event tagged with `family=<language>` so the cockpit can filter.
5. Image preflight runs before the first official eval per tool: `scripts/programbench_image_preflight.py <instance_id> --source-dir <work_dir/source>`.

## Cockpit integration

The orchestrator calls an executor's phases and the cockpit observes them through the ledger:

```text
executor.probe(...)        -> LedgerEvent(phase="probe",   status="completed")
executor.scaffold(...)     -> LedgerEvent(phase="scaffold",status="completed")
executor.build(...)        -> LedgerEvent(phase="build",   status="completed", artifact=str(exec_path))
executor.pack(...)         -> LedgerEvent(phase="pack",    status="completed", artifact=str(submission))
executor.eval(...)         -> LedgerEvent(phase="eval",    status="completed", score=..., artifact=str(eval_json))
executor.classify(...)     -> LedgerEvent(phase="classify",status="completed", failures={...})
executor.report(...)       -> LedgerEvent(phase="report",  status="completed")
```

Live monitor and patch advisor read these events to:
- Render progress bars per tool
- Spot dominant failure families across the batch
- Propose universal patches as soon as the dominant family is clear (typically after 10-15 tools)

## Three-speed eval gate

Once an executor is wired, any proposed scaffold patch goes through:

1. **Micro** — 20 hand-built synthetic tests for the 8 universal CLI patterns (seconds)
2. **Shard** — 10-15 representative tools (~10 min)
3. **Full** — all 115 residuals (~3-6 h)

Full runs only happen when both lower gates lift. The previous workflow ran full runs as the discovery loop; now they're the receipt.

## Out of scope here

- Generation (model calls). Executors do not call cloud or local models. Patches arrive via `scripts/mass_run_v2_scaffold.py` (template-based) or the agent driver (`scripts/determinex_programbench_agent.py`) for model-driven runs.
- Test fixture editing. Executors NEVER modify eval test fixtures unless the upstream binary proves them broken.
- Frontend rendering. The cockpit's Benchmark Lab tab is a separate frontend module; executors only emit events.

## References

- `scripts/run_ledger.py` — universal event substrate (JSONL + SQLite)
- `scripts/failure_classifier.py` — central family taxonomy
- `scripts/programbench_live_monitor.py` — cockpit reader
- `scripts/programbench_patch_advisor.py` — generic core + ProgramBench profile
- `corpus/programbench/_strategy/language_family_sprint_matrix.md` — 25-family routing matrix
- `corpus/programbench/_strategy/per_language_scaffolds.md` — copy-pasteable scaffolds for Python/Go/Rust/C
- `corpus/programbench/_strategy/universal_cli_patterns.md` — 8 universal + 14 secondary CLI patterns from the 256k-test scan
