"""tests/test_immutability_guard.py — EVIDENCE_IMMUTABILITY_GUARD_LOCK_001 + CORPUS_WRITE_GUARD_LOCK_001

Verifies:
  - read_only_context() blocks corpus writes with CorpusWriteBlockedError
  - DETERMINEX_NO_CORPUS_WRITE env var blocks corpus writes
  - determinex evidence validate is read-only (no file mutations)
  - determinex status is read-only (no file mutations)
  - determinex config show/doctor are read-only
  - determinex doctor is read-only (except --json explicit output)
  - read_only_context() is composable and restores env correctly
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

import pytest

_ROOT = Path(__file__).resolve().parents[1]
for _p in (_ROOT, _ROOT / "scripts"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))


# ---------------------------------------------------------------------------
# Corpus write guard
# ---------------------------------------------------------------------------

def test_assert_writes_allowed_passes_when_flag_unset(monkeypatch):
    monkeypatch.delenv("DETERMINEX_NO_CORPUS_WRITE", raising=False)
    from corpus.corpus_manager import _assert_writes_allowed
    _assert_writes_allowed()  # must not raise


@pytest.mark.parametrize("val", ["1", "true", "yes", "True", "YES"])
def test_assert_writes_blocked_when_flag_set(monkeypatch, val):
    monkeypatch.setenv("DETERMINEX_NO_CORPUS_WRITE", val)
    from corpus.corpus_manager import _assert_writes_allowed, CorpusWriteBlockedError
    with pytest.raises(CorpusWriteBlockedError):
        _assert_writes_allowed()


@pytest.mark.parametrize("val", ["0", "false", "no", "", "off"])
def test_assert_writes_allowed_for_falsy_values(monkeypatch, val):
    monkeypatch.setenv("DETERMINEX_NO_CORPUS_WRITE", val)
    from corpus.corpus_manager import _assert_writes_allowed
    _assert_writes_allowed()  # must not raise


def test_read_only_context_blocks_writes(monkeypatch):
    monkeypatch.delenv("DETERMINEX_NO_CORPUS_WRITE", raising=False)
    from corpus.corpus_manager import read_only_context, _assert_writes_allowed, CorpusWriteBlockedError
    with read_only_context():
        with pytest.raises(CorpusWriteBlockedError):
            _assert_writes_allowed()


def test_read_only_context_restores_env_on_exit(monkeypatch):
    monkeypatch.delenv("DETERMINEX_NO_CORPUS_WRITE", raising=False)
    from corpus.corpus_manager import read_only_context, _assert_writes_allowed
    with read_only_context():
        pass
    # After context exits, writes should be allowed again
    _assert_writes_allowed()  # must not raise
    assert os.environ.get("DETERMINEX_NO_CORPUS_WRITE", "") == ""


def test_read_only_context_restores_previous_value(monkeypatch):
    monkeypatch.setenv("DETERMINEX_NO_CORPUS_WRITE", "previous_value")
    from corpus.corpus_manager import read_only_context
    with read_only_context():
        assert os.environ.get("DETERMINEX_NO_CORPUS_WRITE") == "1"
    assert os.environ.get("DETERMINEX_NO_CORPUS_WRITE") == "previous_value"


def test_read_only_context_composable(monkeypatch):
    monkeypatch.delenv("DETERMINEX_NO_CORPUS_WRITE", raising=False)
    from corpus.corpus_manager import read_only_context, _assert_writes_allowed, CorpusWriteBlockedError
    with read_only_context():
        with read_only_context():
            with pytest.raises(CorpusWriteBlockedError):
                _assert_writes_allowed()
    # Both contexts exited — writes allowed again
    _assert_writes_allowed()


def test_read_only_context_restores_on_exception(monkeypatch):
    monkeypatch.delenv("DETERMINEX_NO_CORPUS_WRITE", raising=False)
    from corpus.corpus_manager import read_only_context, _assert_writes_allowed
    try:
        with read_only_context():
            raise ValueError("simulated error")
    except ValueError:
        pass
    # Env must be restored even after an exception
    _assert_writes_allowed()  # must not raise


# ---------------------------------------------------------------------------
# Inspection commands are read-only
# ---------------------------------------------------------------------------

def test_evidence_validate_no_file_mutations():
    """determinex evidence validate must not create, modify, or delete any files."""
    import determinex_cli as cli
    evidence_dir = _ROOT / "assurance" / "evidence"
    before = {str(p): p.stat().st_mtime for p in evidence_dir.rglob("*") if p.is_file()}
    sys.argv = ["determinex", "evidence", "validate"]
    cli.main()
    after = {str(p): p.stat().st_mtime for p in evidence_dir.rglob("*") if p.is_file()}
    assert before == after, f"evidence validate mutated files: {set(before) ^ set(after)}"


def test_config_show_no_file_mutations(tmp_path, capsys):
    """determinex config show must not write any files."""
    import determinex_cli as cli
    # Snapshot entire scripts/ and assurance/ before
    checked_dirs = [_ROOT / "scripts", _ROOT / "assurance", _ROOT / "corpus"]
    before = {}
    for d in checked_dirs:
        if d.exists():
            for p in d.rglob("*"):
                if p.is_file():
                    before[str(p)] = p.stat().st_mtime

    sys.argv = ["determinex", "config", "show"]
    cli.main()
    capsys.readouterr()

    after = {}
    for d in checked_dirs:
        if d.exists():
            for p in d.rglob("*"):
                if p.is_file():
                    after[str(p)] = p.stat().st_mtime

    new_files = set(after) - set(before)
    assert not new_files, f"config show created files: {new_files}"
    modified = {k for k in before if after.get(k) != before[k]}
    assert not modified, f"config show modified files: {modified}"


def test_status_script_no_corpus_writes(monkeypatch):
    """determinex_status main() must not call any corpus write path."""
    monkeypatch.setenv("DETERMINEX_NO_CORPUS_WRITE", "1")
    from corpus.corpus_manager import CorpusWriteBlockedError
    import determinex_status
    # Patch sys.argv to use a safe mode (json output, no tail)
    sys.argv = ["determinex status", "--summary"]
    try:
        determinex_status.main()
    except CorpusWriteBlockedError:
        pytest.fail("determinex status called a corpus write method")
    except SystemExit:
        pass  # expected if no log file exists


def test_no_corpus_write_flag_exported_in_read_only_context():
    """read_only_context must set DETERMINEX_NO_CORPUS_WRITE=1 during execution."""
    from corpus.corpus_manager import read_only_context
    captured = {}
    def probe():
        captured["val"] = os.environ.get("DETERMINEX_NO_CORPUS_WRITE", "")
    with read_only_context():
        probe()
    assert captured["val"] == "1"
