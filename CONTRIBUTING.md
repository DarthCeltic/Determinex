# Contributing to Determinex

## Before You Start

Determinex is free and open source under AGPLv3 — see [LICENSE](LICENSE) and
[docs/papers/LICENSING.md](docs/papers/LICENSING.md). By contributing, you
agree that your contribution is licensed under AGPLv3, same as the rest of
the project.

Read [ARCHITECTURE.md](docs/ARCHITECTURE.md) and [WHITE_PAPER.md](docs/WHITE_PAPER.md) first. Determinex has a specific design philosophy — compiler output is ground truth, not model opinions. PRs that work around the Compiler Oracle rather than through it will be rejected.

Release-supported status is granted only by exact cell certification locks. Support-depth is not release support. Tests, demos, benchmark results, or public documentation do not create release-supported cells, release readiness, production readiness, or open availability. Installer readiness is not claimed.

## What We Need

Priority contributions (in order):

1. **New Rosetta families** — MLP encoder/decoder pairs for architectures not in `registry/registry.json`. See `scripts/train_rosetta_bases.py` for the training protocol.
2. **Tree-sitter language support** — `frontend/src-tauri/src/ast_editor.rs` currently handles Rust only. Go and Python grammars needed.
3. **DSL vocabulary extensions** — new intent markers for languages/patterns not in `scripts/dsl_bootstrap.md`.
4. **Bug fixes** — compiler-verified failures in the limits test (`determinex_limits_test.py`) are highest priority.
5. **Benchmark contributions** — verified scores for models not in `scripts/determinex_benchmark.py`'s public score table.

## Setup

```bash
git clone https://github.com/DarthCeltic/determinex
cd determinex

# Python dependencies
pip install -r requirements.txt

# Pre-commit hooks (required)
pip install pre-commit
pre-commit install

# Rust/Tauri (for frontend work)
cargo install tauri-cli
cd frontend && npm install
```

**Ollama required** for any script that runs model inference:
```bash
ollama pull qwen2.5-coder:7b  # minimum for Builder
```

## Running Tests

```bash
# Core limits test — 6 Rust levels, must all pass with 0 retries
python determinex_limits_test.py

# Rust backend
cd frontend/src-tauri && cargo test

# Linting
ruff check scripts/ *.py
ruff format --check scripts/ *.py
```

The pre-commit hooks run `ruff`, check for `subprocess shell=True`, and reject hardcoded absolute paths. Fix all hook failures before pushing.

## Submitting a PR

1. **One concern per PR.** Don't bundle a new Rosetta family with a refactor.
2. **Compiler-verified changes.** If your PR touches code generation, run `determinex_limits_test.py` before and after. Include the output in your PR description.
3. **No silent regressions.** `micro_eval.py` baseline for the affected model before and after, if you touch any fine-tuning data or Modelfiles.
4. **No new `subprocess shell=True`.** The pre-commit hook will reject it.
5. **No hardcoded paths.** Use `DETERMINEX_ROOT` env var or `Path(__file__).parent`.

## Adding a New Rosetta Architecture Family

1. Add entry to `registry/registry.json` with `"sha256": "PLACEHOLDER_RUN_sha256sum_TO_FILL"`
2. Add model to `scripts/train_rosetta_bases.py` `MODELS` dict (HF model ID, architecture family, embedding dim)
3. Run extraction + training (sequential, one model at a time — see Gap 6 in the plan)
4. Fill sha256 in registry after upload
5. Open PR with the `.pt` file attached to a GitHub Release draft

## Architecture Constraints

Do not break these invariants:

- **Compiler Oracle always runs.** Never short-circuit `validate(project_state)` for speed.
- **WAL is append-only.** `.pending` → `.complete` / `.failed` rename must be atomic. Never write directly to `.complete`.
- **Rosetta SHA256 before torch.load().** Verify raw file bytes first, then deserialize. Not the other way.
- **Builder context is bounded.** Target region + signature index only. Never inject full project history.

## Reporting Bugs

Use [GitHub Issues](https://github.com/DarthCeltic/determinex/issues). Include:
- OS, Python version, Ollama version
- Which script failed and the full traceback
- Output of `python determinex_limits_test.py` (pass/fail counts)

Security issues: use [GitHub Security Advisories](https://github.com/DarthCeltic/determinex/security/advisories/new) — not public issues.
