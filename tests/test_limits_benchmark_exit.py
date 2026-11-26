"""Exit-code regressions for the model-backed limits benchmark (no model required)."""

import io
import json
import subprocess
import sys
import urllib.request

import pytest
from hive import manifest

from scripts import determinex_limits_test as limits


@pytest.mark.parametrize(
    ("levels", "outcomes", "expected_exit", "expected_ids"),
    [
        ("1,2", [True, True], 0, [1, 2]),
        ("1,2", [False], 1, [1]),
        ("3,4", [True, False], 1, [3, 4]),
        ("1,2", [True, KeyboardInterrupt()], 130, [1]),
        ("1", [KeyboardInterrupt()], 130, []),
    ],
)
def test_exit_status_and_saved_report(
    tmp_path, monkeypatch, capsys, levels, outcomes, expected_exit, expected_ids
):
    monkeypatch.setattr(limits, "REPO_ROOT", tmp_path)
    results = iter(outcomes)

    def run(*args):
        result = next(results)
        if isinstance(result, KeyboardInterrupt):
            raise result
        return {"ok": result}

    monkeypatch.setattr(limits, "fallback_run", run)
    assert limits.main(["--levels", levels]) == expected_exit
    report = json.loads((tmp_path / "determinex_limits_report.json").read_text())
    assert [row["id"] for row in report["results"]] == expected_ids
    output = capsys.readouterr().out
    assert ("All levels passed" in output) == (expected_exit == 0)


@pytest.mark.parametrize("levels", ["", "1,99", "99", "abc"])
def test_cli_rejects_invalid_levels(levels):
    run = subprocess.run(
        [sys.executable, str(limits.__file__), "--levels", levels], capture_output=True, text=True
    )
    assert run.returncode == 2
    assert "error:" in run.stderr


@pytest.mark.parametrize(
    ("detail", "child_status", "expected_ok"),
    [
        ({"steps": [{"status": "complete"}]}, 0, True),
        ({"steps": [{"status": "complete"}]}, 1, False),
        ({"steps": []}, 0, False),
        ({"steps": [{"status": "complete"}, {"status": "pending"}]}, 0, False),
        (None, 0, False),
    ],
)
def test_subprocess_requires_a_successful_exit_and_completed_manifest(
    tmp_path, monkeypatch, detail, child_status, expected_ok
):
    monkeypatch.setattr(limits, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(manifest, "resolve_repo_root", lambda: tmp_path)
    script_dir = tmp_path / "scripts"
    script_dir.mkdir()
    (script_dir / "determinex_hive.py").touch()
    session = tmp_path / "sessions" / "testsession"
    session.mkdir(parents=True)
    if detail is not None:
        (session / "manifest.json").write_text(json.dumps(detail))

    def invoke(args, **kwargs):
        command = args[2]
        stdout = '{"session_id": "testsession"}' if command == "new-session" else ""
        status = child_status if command == "run-session" else 0
        return subprocess.CompletedProcess(args, status, stdout, "")

    monkeypatch.setattr(subprocess, "run", invoke)
    assert limits.run_hive_build("test spec", "python", 3)["ok"] is expected_ok


@pytest.mark.parametrize(
    ("steps", "expected_ok"),
    [([], False), ([{"status": "pending"}], False), ([{"status": "complete"}], True)],
)
def test_http_requires_completed_steps_even_if_session_says_complete(
    monkeypatch, steps, expected_ok
):
    def respond(req, timeout):
        url = req if isinstance(req, str) else req.full_url
        if url.endswith("/create"):
            data = {"session_id": "fixture-session"}
        elif "/status/" in url:
            data = {"status": "complete", "steps": steps}
        else:
            data = {}
        return io.BytesIO(json.dumps({"data": data}).encode())

    monkeypatch.setattr(urllib.request, "urlopen", respond)
    assert limits._run_via_http("test spec", "python", 1, 1)["ok"] is expected_ok
