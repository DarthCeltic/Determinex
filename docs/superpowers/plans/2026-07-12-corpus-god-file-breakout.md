# Corpus God File Breakout Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Break first-party corpus god files into owned, testable shards while preserving ProgramBench canonical truth and release verification behavior.

**Architecture:** Add compatibility readers and generators first, then migrate one ledger or module at a time behind parity tests. Keep legacy aggregate files readable until all callers are moved, and treat benchmark fixtures/artifacts as packaging surfaces rather than source refactors.

**Tech Stack:** Python 3.11, `pytest`, JSON ledgers under `corpus/programbench`, existing ProgramBench guard scripts, PowerShell-compatible Windows paths.

---

## File Structure

Create:

- `scripts/corpus/programbench/knowledge_store.py` - typed loader for sharded build knowledge plus legacy aggregate fallback.
- `scripts/corpus/programbench/split_build_knowledge.py` - one-shot/idempotent splitter from `build_knowledge.json` to shard files.
- `scripts/corpus/programbench/merge_build_knowledge.py` - deterministic aggregate generator for legacy compatibility.
- `scripts/corpus/programbench/eval_index_store.py` - typed loader for canonical eval records, initially reading the existing aggregate.
- `scripts/corpus/programbench/split_eval_index.py` - sharder that writes by-tool records and regenerates the canonical aggregate.
- `scripts/corpus/programbench/corpus_god_file_guard.py` - guard that reports first-party oversized files and excludes fixture/archive paths.
- `tests/corpus/programbench/test_build_knowledge_store.py`
- `tests/corpus/programbench/test_eval_index_store.py`
- `tests/corpus/programbench/test_corpus_god_file_guard.py`
- `tests/corpus/programbench/churn/test_churn_model_policy.py`
- `tests/corpus/programbench/churn/test_churn_timeout_policy.py`
- `tests/corpus/programbench/churn/test_churn_events_and_state.py`
- `tests/corpus/programbench/churn/test_churn_oracle_routing.py`

Modify:

- `corpus/programbench/build_knowledge.json` - keep as generated aggregate until every reader moves.
- `corpus/programbench/eval_index.json` - keep canonical aggregate, generated from shards only after parity passes.
- `tests/corpus/programbench/test_pb_churn_lock.py` - reduce to import smoke or remove after split tests are passing.
- `scripts/determinex_pb_churn.py` - split only after test split proves behavior boundaries.
- `scripts/determinex_programbench_agent.py` - split last, after characterization coverage exists.

Generated directories:

- `corpus/programbench/build_knowledge/roadmap.json`
- `corpus/programbench/build_knowledge/scoring.json`
- `corpus/programbench/build_knowledge/modules.json`
- `corpus/programbench/build_knowledge/eval_mechanics.json`
- `corpus/programbench/build_knowledge/class_patterns.json`
- `corpus/programbench/build_knowledge/per_tool/*.json`
- `corpus/programbench/eval_index/by_tool/*.json`
- `corpus/programbench/xray/by_tool/*.json`

## Non-Negotiables

- Do not hand-edit `corpus/programbench/eval_index.json`.
- Do not split or rewrite locked upstream `source/` snapshots as source refactors.
- Do not move binaries or archives in this plan; only inventory them for release packaging.
- Every generated aggregate must be byte-stable after `merge -> split -> merge`.
- ProgramBench guard commands must remain green before the release lane resumes.

---

### Task 1: Add a Corpus God File Guard

**Files:**
- Create: `scripts/corpus/programbench/corpus_god_file_guard.py`
- Test: `tests/corpus/programbench/test_corpus_god_file_guard.py`

- [ ] **Step 1: Write the failing test**

```python
from pathlib import Path

from scripts.corpus.programbench.corpus_god_file_guard import audit_paths


def test_guard_flags_first_party_god_files_and_excludes_fixtures(tmp_path: Path) -> None:
    root = tmp_path
    first_party = root / "corpus/programbench/build_knowledge.json"
    first_party.parent.mkdir(parents=True)
    first_party.write_text("x\n" * 2001, encoding="utf-8")

    fixture = root / "corpus/programbench/per_tool_overrides/tool/bin"
    fixture.parent.mkdir(parents=True)
    fixture.write_bytes(b"x" * 5_000_000)

    findings = audit_paths(root, max_lines=1500, max_bytes=1_000_000)

    assert [finding.path for finding in findings] == ["corpus/programbench/build_knowledge.json"]
    assert findings[0].lines == 2001
```

- [ ] **Step 2: Run test to verify it fails**

Run:

```powershell
python -m pytest tests/corpus/programbench/test_corpus_god_file_guard.py -q
```

Expected: fail because `corpus_god_file_guard.py` does not exist.

- [ ] **Step 3: Implement the guard**

```python
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


EXCLUDED_PREFIXES = (
    "corpus/programbench/locked/",
    "corpus/programbench/per_tool_overrides/",
    "corpus/programbench/pending_unlock/",
    "corpus/programbench/training_corpus/",
    "corpus/swebench/",
)


@dataclass(frozen=True)
class GodFileFinding:
    path: str
    bytes: int
    lines: int


def _is_excluded(path: str) -> bool:
    return any(path.startswith(prefix) for prefix in EXCLUDED_PREFIXES)


def audit_paths(root: Path, *, max_lines: int = 1500, max_bytes: int = 1_000_000) -> list[GodFileFinding]:
    findings: list[GodFileFinding] = []
    for path in sorted(root.glob("**/*")):
        if not path.is_file():
            continue
        rel = path.relative_to(root).as_posix()
        if _is_excluded(rel):
            continue
        size = path.stat().st_size
        lines = -1
        if path.suffix in {".py", ".json", ".md", ".txt", ".yaml", ".yml"}:
            try:
                lines = path.read_text(encoding="utf-8").count("\n") + 1
            except UnicodeDecodeError:
                lines = -1
        if size > max_bytes or lines > max_lines:
            findings.append(GodFileFinding(path=rel, bytes=size, lines=lines))
    return findings
```

- [ ] **Step 4: Run test to verify it passes**

Run:

```powershell
python -m pytest tests/corpus/programbench/test_corpus_god_file_guard.py -q
```

Expected: pass.

- [ ] **Step 5: Commit**

```powershell
git add scripts/corpus/programbench/corpus_god_file_guard.py tests/corpus/programbench/test_corpus_god_file_guard.py
git commit -m "Add corpus god file guard"
```

---

### Task 2: Add Build Knowledge Loader Compatibility Tests

**Files:**
- Create: `scripts/corpus/programbench/knowledge_store.py`
- Test: `tests/corpus/programbench/test_build_knowledge_store.py`

- [ ] **Step 1: Write the failing tests**

```python
import json
from pathlib import Path

from scripts.corpus.programbench.knowledge_store import load_build_knowledge


def test_loads_legacy_build_knowledge_json(tmp_path: Path) -> None:
    root = tmp_path
    payload = {"modules": {"pb_parallel.py": "runner"}, "class_patterns": {"go": {"detect": "go.mod"}}}
    path = root / "corpus/programbench/build_knowledge.json"
    path.parent.mkdir(parents=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    assert load_build_knowledge(root) == payload


def test_sharded_build_knowledge_overrides_legacy_when_present(tmp_path: Path) -> None:
    root = tmp_path
    legacy = root / "corpus/programbench/build_knowledge.json"
    legacy.parent.mkdir(parents=True)
    legacy.write_text(json.dumps({"legacy": True}), encoding="utf-8")

    shard_root = root / "corpus/programbench/build_knowledge"
    shard_root.mkdir()
    (shard_root / "modules.json").write_text(json.dumps({"pb_parallel.py": "runner"}), encoding="utf-8")
    (shard_root / "class_patterns.json").write_text(json.dumps({"go": {"detect": "go.mod"}}), encoding="utf-8")

    assert load_build_knowledge(root) == {
        "modules": {"pb_parallel.py": "runner"},
        "class_patterns": {"go": {"detect": "go.mod"}},
    }
```

- [ ] **Step 2: Run tests to verify they fail**

Run:

```powershell
python -m pytest tests/corpus/programbench/test_build_knowledge_store.py -q
```

Expected: fail because `knowledge_store.py` does not exist.

- [ ] **Step 3: Implement the compatibility loader**

```python
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


SHARD_ORDER = (
    "roadmap",
    "scoring",
    "modules",
    "eval_mechanics",
    "class_patterns",
)


def _read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_build_knowledge(root: Path = Path(".")) -> dict[str, Any]:
    shard_root = root / "corpus/programbench/build_knowledge"
    if shard_root.exists():
        merged: dict[str, Any] = {}
        for name in SHARD_ORDER:
            path = shard_root / f"{name}.json"
            if path.exists():
                merged[name] = _read_json(path)
        per_tool_root = shard_root / "per_tool"
        if per_tool_root.exists():
            merged["per_tool"] = {
                path.stem: _read_json(path)
                for path in sorted(per_tool_root.glob("*.json"))
            }
        return merged
    return _read_json(root / "corpus/programbench/build_knowledge.json")
```

- [ ] **Step 4: Run tests to verify they pass**

Run:

```powershell
python -m pytest tests/corpus/programbench/test_build_knowledge_store.py -q
```

Expected: pass.

- [ ] **Step 5: Commit**

```powershell
git add scripts/corpus/programbench/knowledge_store.py tests/corpus/programbench/test_build_knowledge_store.py
git commit -m "Add build knowledge compatibility loader"
```

---

### Task 3: Split and Regenerate Build Knowledge

**Files:**
- Create: `scripts/corpus/programbench/split_build_knowledge.py`
- Create: `scripts/corpus/programbench/merge_build_knowledge.py`
- Modify: `corpus/programbench/build_knowledge.json`
- Create directory/files: `corpus/programbench/build_knowledge/*.json`

- [ ] **Step 1: Add splitter and merger smoke tests**

Append to `tests/corpus/programbench/test_build_knowledge_store.py`:

```python
import subprocess
import sys


def test_split_then_merge_preserves_payload(tmp_path: Path) -> None:
    payload = {
        "_doc": "root doc",
        "roadmap_to_envisioned": {"remaining_work": {"guard": "yes"}},
        "official_metric": {"THE_SCORER": "programbench info"},
        "modules": {"pb_parallel.py": "runner"},
        "eval_mechanics": {"not_run": "counts"},
        "class_patterns": {"go": {"detect": "go.mod"}},
    }
    path = tmp_path / "corpus/programbench/build_knowledge.json"
    path.parent.mkdir(parents=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    subprocess.run(
        [sys.executable, "scripts/corpus/programbench/split_build_knowledge.py", "--root", str(tmp_path)],
        check=True,
    )
    subprocess.run(
        [sys.executable, "scripts/corpus/programbench/merge_build_knowledge.py", "--root", str(tmp_path)],
        check=True,
    )

    assert json.loads(path.read_text(encoding="utf-8")) == payload
```

- [ ] **Step 2: Run test to verify it fails**

Run:

```powershell
python -m pytest tests/corpus/programbench/test_build_knowledge_store.py::test_split_then_merge_preserves_payload -q
```

Expected: fail because the splitter and merger do not exist.

- [ ] **Step 3: Implement deterministic split/merge scripts**

Use these exact top-level shard mappings:

```python
SHARDS = {
    "roadmap": ["roadmap_to_envisioned"],
    "scoring": ["official_metric", "lock_criteria"],
    "modules": ["modules"],
    "eval_mechanics": ["eval_mechanics"],
    "class_patterns": ["class_patterns"],
}
```

Each script must write JSON with:

```python
json.dumps(data, indent=2, sort_keys=False) + "\n"
```

- [ ] **Step 4: Run unit tests**

Run:

```powershell
python -m pytest tests/corpus/programbench/test_build_knowledge_store.py -q
```

Expected: pass.

- [ ] **Step 5: Split the real file and regenerate aggregate**

Run:

```powershell
python scripts/corpus/programbench/split_build_knowledge.py --root .
python scripts/corpus/programbench/merge_build_knowledge.py --root .
git diff -- corpus/programbench/build_knowledge.json corpus/programbench/build_knowledge
```

Expected: shard files are created; `build_knowledge.json` has no semantic change after regeneration.

- [ ] **Step 6: Commit**

```powershell
git add scripts/corpus/programbench/split_build_knowledge.py scripts/corpus/programbench/merge_build_knowledge.py tests/corpus/programbench/test_build_knowledge_store.py corpus/programbench/build_knowledge corpus/programbench/build_knowledge.json
git commit -m "Shard ProgramBench build knowledge"
```

---

### Task 4: Add Eval Index Store Without Moving Canonical Truth Yet

**Files:**
- Create: `scripts/corpus/programbench/eval_index_store.py`
- Test: `tests/corpus/programbench/test_eval_index_store.py`

- [ ] **Step 1: Write compatibility tests**

```python
import json
from pathlib import Path

from scripts.corpus.programbench.eval_index_store import load_eval_records, records_by_slug


def test_loads_legacy_eval_index_list(tmp_path: Path) -> None:
    path = tmp_path / "corpus/programbench/eval_index.json"
    path.parent.mkdir(parents=True)
    path.write_text(json.dumps([{"slug": "bat", "status": "candidate"}]), encoding="utf-8")

    assert load_eval_records(tmp_path) == [{"slug": "bat", "status": "candidate"}]


def test_records_by_slug_rejects_duplicate_slug() -> None:
    records = [{"slug": "bat"}, {"slug": "bat"}]

    try:
        records_by_slug(records)
    except ValueError as exc:
        assert "duplicate eval_index slug: bat" in str(exc)
    else:
        raise AssertionError("duplicate slug was not rejected")
```

- [ ] **Step 2: Run tests to verify they fail**

Run:

```powershell
python -m pytest tests/corpus/programbench/test_eval_index_store.py -q
```

Expected: fail because `eval_index_store.py` does not exist.

- [ ] **Step 3: Implement loader**

```python
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_eval_records(root: Path = Path(".")) -> list[dict[str, Any]]:
    shard_root = root / "corpus/programbench/eval_index/by_tool"
    if shard_root.exists():
        return [
            json.loads(path.read_text(encoding="utf-8"))
            for path in sorted(shard_root.glob("*.json"))
        ]
    return json.loads((root / "corpus/programbench/eval_index.json").read_text(encoding="utf-8"))


def records_by_slug(records: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    by_slug: dict[str, dict[str, Any]] = {}
    for record in records:
        slug = record.get("slug")
        if not isinstance(slug, str) or not slug:
            raise ValueError(f"eval_index record missing slug: {record!r}")
        if slug in by_slug:
            raise ValueError(f"duplicate eval_index slug: {slug}")
        by_slug[slug] = record
    return by_slug
```

- [ ] **Step 4: Run tests**

Run:

```powershell
python -m pytest tests/corpus/programbench/test_eval_index_store.py -q
```

Expected: pass.

- [ ] **Step 5: Commit**

```powershell
git add scripts/corpus/programbench/eval_index_store.py tests/corpus/programbench/test_eval_index_store.py
git commit -m "Add eval index compatibility store"
```

---

### Task 5: Shard Eval Index Behind Guard Parity

**Files:**
- Create: `scripts/corpus/programbench/split_eval_index.py`
- Modify: `corpus/programbench/eval_index.json`
- Create directory/files: `corpus/programbench/eval_index/by_tool/*.json`

- [ ] **Step 1: Add split/merge parity test**

Append to `tests/corpus/programbench/test_eval_index_store.py`:

```python
import subprocess
import sys


def test_split_eval_index_regenerates_same_records(tmp_path: Path) -> None:
    path = tmp_path / "corpus/programbench/eval_index.json"
    path.parent.mkdir(parents=True)
    records = [{"slug": "bat", "status": "candidate"}, {"slug": "jq", "status": "native_rebuild"}]
    path.write_text(json.dumps(records, indent=2), encoding="utf-8")

    subprocess.run(
        [sys.executable, "scripts/corpus/programbench/split_eval_index.py", "--root", str(tmp_path), "--regenerate"],
        check=True,
    )

    assert json.loads(path.read_text(encoding="utf-8")) == records
```

- [ ] **Step 2: Run test to verify it fails**

Run:

```powershell
python -m pytest tests/corpus/programbench/test_eval_index_store.py::test_split_eval_index_regenerates_same_records -q
```

Expected: fail because `split_eval_index.py` does not exist.

- [ ] **Step 3: Implement split script**

Write one JSON file per record at:

```text
corpus/programbench/eval_index/by_tool/<slug>.json
```

Sanitize filenames by replacing `/`, `\`, and `:` with `_`. Keep a sidecar field `_aggregate_order` only if order cannot be recovered from sorted shard names; otherwise preserve the original aggregate order in `eval_index.json` during regeneration.

- [ ] **Step 4: Run unit test**

Run:

```powershell
python -m pytest tests/corpus/programbench/test_eval_index_store.py -q
```

Expected: pass.

- [ ] **Step 5: Run real split and ProgramBench guards**

Run:

```powershell
python scripts/corpus/programbench/split_eval_index.py --root . --regenerate
python scripts/pb_doc_count_check.py --verbose
python scripts/pb_board_guard.py --guard
python scripts/pb_override_scan.py --guard
```

Expected: count output unchanged; both guards pass.

- [ ] **Step 6: Commit**

```powershell
git add scripts/corpus/programbench/split_eval_index.py tests/corpus/programbench/test_eval_index_store.py corpus/programbench/eval_index corpus/programbench/eval_index.json
git commit -m "Shard ProgramBench eval index with aggregate parity"
```

---

### Task 6: Split Churn Lock Tests Before Churn Implementation

**Files:**
- Create: `tests/corpus/programbench/churn/test_churn_model_policy.py`
- Create: `tests/corpus/programbench/churn/test_churn_timeout_policy.py`
- Create: `tests/corpus/programbench/churn/test_churn_events_and_state.py`
- Create: `tests/corpus/programbench/churn/test_churn_oracle_routing.py`
- Modify: `tests/corpus/programbench/test_pb_churn_lock.py`

- [ ] **Step 1: Move tests by concern**

Use the existing assertions from `tests/corpus/programbench/test_pb_churn_lock.py` and group them:

- model selection and cloud/local policy -> `test_churn_model_policy.py`
- timeout defaults, cooldown, and no-progress retry -> `test_churn_timeout_policy.py`
- event JSONL/state/lease behavior -> `test_churn_events_and_state.py`
- oracle, reimpl drive, generation-error rejection -> `test_churn_oracle_routing.py`

- [ ] **Step 2: Run old and new tests together**

Run:

```powershell
python -m pytest tests/corpus/programbench/test_pb_churn_lock.py tests/corpus/programbench/churn -q
```

Expected: pass with duplicate coverage.

- [ ] **Step 3: Reduce the old test file**

Keep only import-level compatibility tests in `tests/corpus/programbench/test_pb_churn_lock.py`:

```python
import scripts.determinex_pb_churn as churn


def test_churn_module_exports_watch_entrypoints() -> None:
    assert callable(churn.main)
    assert callable(churn.default_model_ladder)
```

- [ ] **Step 4: Run split tests**

Run:

```powershell
python -m pytest tests/corpus/programbench/test_pb_churn_lock.py tests/corpus/programbench/churn -q
```

Expected: pass.

- [ ] **Step 5: Commit**

```powershell
git add tests/corpus/programbench/test_pb_churn_lock.py tests/corpus/programbench/churn
git commit -m "Split ProgramBench churn lock tests by behavior"
```

---

### Task 7: Split Churn Runtime by Responsibility

**Files:**
- Create: `scripts/corpus/programbench/churn/model_policy.py`
- Create: `scripts/corpus/programbench/churn/timeout_policy.py`
- Create: `scripts/corpus/programbench/churn/events.py`
- Create: `scripts/corpus/programbench/churn/oracle_route.py`
- Modify: `scripts/determinex_pb_churn.py`

- [ ] **Step 1: Move pure model ladder logic**

Move `default_model_ladder` and cloud enablement checks into `model_policy.py`.

- [ ] **Step 2: Move timeout/cooldown decisions**

Move timeout functions and no-progress cooldown checks into `timeout_policy.py`.

- [ ] **Step 3: Move event/state helpers**

Move JSONL event writing and state-load/save helpers into `events.py`.

- [ ] **Step 4: Move oracle/reimpl command construction**

Move subprocess argument construction into `oracle_route.py`, leaving process execution in the top-level watch loop.

- [ ] **Step 5: Run churn tests**

Run:

```powershell
python -m pytest tests/corpus/programbench/test_pb_churn_lock.py tests/corpus/programbench/churn -q
```

Expected: pass.

- [ ] **Step 6: Commit**

```powershell
git add scripts/determinex_pb_churn.py scripts/corpus/programbench/churn tests/corpus/programbench
git commit -m "Split ProgramBench churn runtime helpers"
```

---

### Task 8: Characterize and Split ProgramBench Agent Last

**Files:**
- Create: `tests/corpus/programbench/test_programbench_agent_characterization.py`
- Create: `scripts/programbench_agent/cli.py`
- Create: `scripts/programbench_agent/packaging.py`
- Create: `scripts/programbench_agent/provenance.py`
- Create: `scripts/programbench_agent/eval_runner.py`
- Modify: `scripts/determinex_programbench_agent.py`

- [ ] **Step 1: Add characterization tests for public entrypoints**

Test that the current CLI parses known commands without executing external Docker/model calls by monkeypatching subprocess and model functions.

- [ ] **Step 2: Extract provenance check**

Move `_run_provenance_check` into `scripts/programbench_agent/provenance.py` and import it back.

- [ ] **Step 3: Extract packaging helpers**

Move tarball/source packaging helpers into `scripts/programbench_agent/packaging.py`.

- [ ] **Step 4: Extract eval runner calls**

Move ProgramBench eval invocation and result parsing into `scripts/programbench_agent/eval_runner.py`.

- [ ] **Step 5: Keep `scripts/determinex_programbench_agent.py` as CLI shim**

It should import `main` from `scripts.programbench_agent.cli` and retain the existing executable path for compatibility.

- [ ] **Step 6: Run agent and corpus tests**

Run:

```powershell
python -m pytest tests/corpus/programbench/test_programbench_agent_characterization.py tests/corpus/programbench -q
```

Expected: pass.

- [ ] **Step 7: Commit**

```powershell
git add scripts/determinex_programbench_agent.py scripts/programbench_agent tests/corpus/programbench/test_programbench_agent_characterization.py
git commit -m "Split ProgramBench agent into focused modules"
```

---

### Task 9: Treat Xray Index as Generated Output

**Files:**
- Create: `scripts/corpus/programbench/xray_index_store.py`
- Create: `scripts/corpus/programbench/split_xray_index.py`
- Modify: `corpus/programbench/xray_index.json`
- Create directory/files: `corpus/programbench/xray/by_tool/*.json`

- [ ] **Step 1: Add loader tests**

Use the same pattern as `eval_index_store.py`, but accept either a list or dict depending on the current xray schema. The test must assert exact round-trip equality for a minimal fixture.

- [ ] **Step 2: Implement splitter**

Shard by the tool/slug field present in each xray record. If records do not have a stable slug field, write a blocker note in `assurance/evidence/corpus_god_file_audit/xray_schema_blocker.md` and do not split.

- [ ] **Step 3: Run split on real file**

Run:

```powershell
python scripts/corpus/programbench/split_xray_index.py --root . --regenerate
```

Expected: `corpus/programbench/xray_index.json` regenerates with no semantic change.

- [ ] **Step 4: Commit**

```powershell
git add scripts/corpus/programbench/xray_index_store.py scripts/corpus/programbench/split_xray_index.py corpus/programbench/xray corpus/programbench/xray_index.json
git commit -m "Shard generated ProgramBench xray index"
```

---

### Task 10: Release Verification After Breakout

**Files:**
- Modify: `assurance/evidence/corpus_god_file_audit/audit_20260712.md`

- [ ] **Step 1: Run focused corpus tests**

Run:

```powershell
python -m pytest tests/corpus/programbench/test_build_knowledge_store.py tests/corpus/programbench/test_eval_index_store.py tests/corpus/programbench/test_corpus_god_file_guard.py tests/corpus/programbench/churn -q
```

Expected: pass.

- [ ] **Step 2: Run ProgramBench truth guards**

Run:

```powershell
python scripts/pb_doc_count_check.py --verbose
python scripts/pb_board_guard.py --guard
python scripts/pb_override_scan.py --guard
```

Expected: pass with unchanged counts.

- [ ] **Step 3: Run release gates**

Run:

```powershell
python scripts/release/determinex_release_gates.py
python scripts/release/full_release_closure.py
```

Expected: no new blockers from corpus structure.

- [ ] **Step 4: Update audit ledger**

Append the commands and results to `assurance/evidence/corpus_god_file_audit/audit_20260712.md`.

- [ ] **Step 5: Commit**

```powershell
git add assurance/evidence/corpus_god_file_audit/audit_20260712.md
git commit -m "Record corpus god file breakout verification"
```

---

## Self-Review

Spec coverage:

- Audits god files in corpus-facing surfaces.
- Separates fixture/package mass from first-party source/control god files.
- Preserves canonical ProgramBench truth through adapters, generators, and guard checks.
- Provides a staged plan that can run before the open-source release lane resumes.

Placeholder scan:

- No `TBD`, `TODO`, or undefined future steps remain.
- Xray has an explicit blocker path if the schema lacks a stable sharding key.

Type consistency:

- Loader APIs use `Path` roots and return Python dictionaries/lists consistently.
- Split/merge scripts use the same root argument and JSON encoding discipline.
