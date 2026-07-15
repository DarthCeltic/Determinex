"""
Tests for scripts/determinex_oracle.py — the Universal Ground-Truth Oracle.

This module had ZERO direct test coverage before 2026-07-02, despite being
the single most load-bearing piece of the system ("the compiler is the
only oracle" — every corpus claim, every training pair, ultimately
traces back to this). Found live during a corpus-center audit: pass/fail
itself was always correct, but total/n_passed were silently dead (always
0/0) on every JUnit-backed oracle (python/jvm/swift/dotnet/ruby/php/
typescript) since the fields were never assigned. Not a correctness bug —
the load-bearing pass/fail guarantee was intact — but a real gap since
determinex_oracle_env's OpenEnv observation contract exposes total/n_passed
to external RL consumers.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import pytest

from determinex_oracle import _junit_counts, _junit_failures, get_oracle


_JUNIT_XML_MIXED = """<?xml version="1.0"?>
<testsuite tests="4" failures="1" errors="1" skipped="1">
  <testcase classname="test_mod" name="test_pass_one" />
  <testcase classname="test_mod" name="test_pass_two" />
  <testcase classname="test_mod" name="test_fails">
    <failure message="assert 1 == 2">AssertionError</failure>
  </testcase>
  <testcase classname="test_mod" name="test_errors">
    <error message="boom">RuntimeError</error>
  </testcase>
  <testcase classname="test_mod" name="test_skipped">
    <skipped message="not applicable" />
  </testcase>
</testsuite>
"""


def test_junit_counts_on_mixed_results(tmp_path):
    xml = tmp_path / "junit.xml"
    xml.write_text(_JUNIT_XML_MIXED, encoding="utf-8")

    total, n_passed = _junit_counts(xml)

    # 5 testcases total: 2 pass, 1 failure, 1 error, 1 skipped.
    assert total == 5
    assert n_passed == 2


def test_junit_failures_on_mixed_results(tmp_path):
    xml = tmp_path / "junit.xml"
    xml.write_text(_JUNIT_XML_MIXED, encoding="utf-8")

    failures = _junit_failures(xml)

    statuses = {f.name: f.status for f in failures}
    assert statuses["test_fails"] == "failure"
    assert statuses["test_errors"] == "failure"  # errors normalize to failure status
    assert statuses["test_skipped"] == "skipped"
    assert "test_pass_one" not in statuses
    assert "test_pass_two" not in statuses


def test_junit_counts_missing_file_returns_zero(tmp_path):
    assert _junit_counts(tmp_path / "does_not_exist.xml") == (0, 0)


def test_junit_counts_malformed_xml_returns_zero(tmp_path):
    xml = tmp_path / "bad.xml"
    xml.write_text("not valid xml <<<", encoding="utf-8")
    assert _junit_counts(xml) == (0, 0)


# ── Live end-to-end: the actual python oracle against real pytest ──────────

def _write_solution(workdir: Path, body: str) -> None:
    (workdir / "solution.py").write_text(body, encoding="utf-8")
    (workdir / "test_solution.py").write_text(
        "from solution import add\n"
        "def test_add():\n"
        "    assert add(2, 3) == 5\n",
        encoding="utf-8",
    )


def test_python_oracle_live_broken_submission_fails_with_real_traceback(tmp_path):
    _write_solution(tmp_path, "def add(a, b):\n    return a - b\n")  # deliberately wrong

    oracle = get_oracle("python")
    result = oracle.verify(tmp_path)

    assert result.passed is False
    assert result.total == 1
    assert result.n_passed == 0
    assert len(result.failures) == 1
    assert "assert" in result.failures[0].text.lower()


def test_python_oracle_live_fixed_submission_passes(tmp_path):
    _write_solution(tmp_path, "def add(a, b):\n    return a + b\n")

    oracle = get_oracle("python")
    result = oracle.verify(tmp_path)

    assert result.passed is True
    assert result.total == 1
    assert result.n_passed == 1
    assert result.failures == []


def test_python_oracle_never_silently_passes_on_collection_error(tmp_path):
    """A submission that doesn't even import cleanly must never report passed=True."""
    (tmp_path / "test_broken_import.py").write_text(
        "from nonexistent_module import whatever\n", encoding="utf-8"
    )

    oracle = get_oracle("python")
    result = oracle.verify(tmp_path)

    assert result.passed is False
