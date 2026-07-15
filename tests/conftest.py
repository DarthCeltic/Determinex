"""
tests/conftest.py — pytest bootstrap for Determinex.

Puts the project root, `scripts/`, and `determinex_trainer/` on sys.path so tests
can `import hive.*`, `import determinex_cloak`, etc. without invoking pytest
plugins or PYTHONPATH gymnastics.

Also exposes a couple of light fixtures shared by the cloak and swebench
smoke tests.
"""
from __future__ import annotations

import os
import sys
import tempfile
from pathlib import Path

import pytest

_ROOT = Path(__file__).resolve().parent.parent
for _p in (_ROOT, _ROOT / "scripts", _ROOT / "determinex_trainer"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

# Fixture projects include intentionally broken repos for intake/corpus tests;
# they are data, not test modules for the Determinex suite itself.
collect_ignore = ["fixtures"]

# Some scripts read DETERMINEX_ROOT to anchor logs/state. Keep tests isolated
# from the user's real logs by default.
os.environ.setdefault("DETERMINEX_ROOT", str(_ROOT))
os.environ.setdefault(
    "DETERMINEX_PROGRAMBENCH_EVIDENCE_WRITE_ROOT",
    str(_ROOT / ".tmp" / "pytest-programbench-evidence"),
)
os.environ.setdefault(
    "DETERMINEX_PROGRAMBENCH_OPERATOR_OUTBOX_WRITE_ROOT",
    str(_ROOT / ".tmp" / "pytest-programbench-operator-outbox"),
)


@pytest.fixture
def tmp_repo(tmp_path: Path) -> Path:
    """A throwaway directory shaped like a tiny project root."""
    (tmp_path / "src").mkdir()
    (tmp_path / "tests").mkdir()
    return tmp_path


@pytest.fixture
def sample_python_module(tmp_repo: Path) -> Path:
    """Write a small Python module the cloak tests can obfuscate."""
    src = tmp_repo / "src" / "app.py"
    src.write_text(
        "def compute_total(price, qty):\n"
        "    discount = 0.1 if qty > 10 else 0.0\n"
        "    return price * qty * (1 - discount)\n"
        "\n"
        "class OrderRecord:\n"
        "    def __init__(self, sku, qty):\n"
        "        self.sku = sku\n"
        "        self.qty = qty\n",
        encoding="utf-8",
    )
    return src
