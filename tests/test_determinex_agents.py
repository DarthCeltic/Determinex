"""tests/test_determinex_agents.py

Covers the additions made to scripts/determinex_agents.py for the multi-agent
chat room feature: resolve_argv() (the pure, no-subprocess argv-resolution
contract the Rust chat backend relies on to spawn+stream a CLI itself) and
the local-ollama registration. Originally rode on aider's --model flag;
aider isn't installed here and this environment blocks pip installs, so
local-ollama now drives determinex_local_agent.py directly (Ollama HTTP +
swe_agent's proven SEARCH/REPLACE primitives) -- needs nothing beyond Python
and a running Ollama, which are both already present.
"""
from __future__ import annotations

import shutil
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
for _p in (_ROOT, _ROOT / "scripts"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import determinex_agents as agents  # noqa: E402


def test_resolve_argv_local_ollama_substitutes_task_and_model():
    # local-ollama's template uses {task_file}, not {task} -- a chat-room
    # prompt (Mission Plan + transcript window) as a raw positional CLI
    # argument blew through Windows' command-line length limit (os error 206)
    # on every single turn. resolve_argv() writes the task to a temp file and
    # substitutes its path instead, so the task content is verified by
    # reading that file back, not by string-matching argv.
    argv = agents.resolve_argv("local-ollama", "fix the bug", Path("C:/ws"),
                                model="qwen2.5-coder:14b-instruct-q4_K_M")
    # argv[0] is shutil.which("python")-resolved (PATHEXT shims on Windows
    # aren't found by Rust's Command::new the way a shell finds them) --
    # not the bare "python" the pre-resolution code used to return.
    assert argv[0] == (shutil.which("python") or "python")
    assert argv[1].endswith("determinex_local_agent.py")
    assert argv[2] == "--task-file"
    task_file = Path(argv[3])
    assert task_file.read_text(encoding="utf-8") == "fix the bug"
    assert argv[4:] == [
        "--workspace", "C:\\ws" if sys.platform == "win32" else "C:/ws",
        "--model", "qwen2.5-coder:14b-instruct-q4_K_M",
    ]
    task_file.unlink()


def test_resolve_argv_local_ollama_aliases_resolve_the_same():
    for alias in ("aider-local", "ollama"):
        argv = agents.resolve_argv(alias, "fix the bug", Path("C:/ws"), model="tag")
        assert argv[1].endswith("determinex_local_agent.py")
        assert "tag" in argv


def test_resolve_argv_no_model_omits_the_flag_entirely():
    """No model selected -> the --model flag must be ABSENT, not present-and-empty.

    This previously asserted `argv[-1] == ""` ("empty, not a crash"), but an
    explicit `--model ""` is NOT harmless: argparse only applies a default when
    the flag is absent, so the empty string won and determinex_local_agent.py
    called Ollama with no model name -- every local-ollama chat turn died with
    `HTTP 404 ... is '' pulled? (ollama pull )` whenever the user hadn't picked
    a model, which is the default state of the UI.
    """
    argv = agents.resolve_argv("local-ollama", "fix the bug", Path("C:/ws"))
    assert "--model" not in argv
    assert "" not in argv


def test_resolve_argv_unknown_agent_raises():
    try:
        agents.resolve_argv("not-a-real-agent", "task", Path("C:/ws"))
        assert False, "expected KeyError"
    except KeyError:
        pass


def test_resolve_argv_existing_agents_unaffected_by_model_substitution():
    """Regression: with no model= passed, aider/cursor-agent/claude-code/
    codex/gemini-cli resolve identically to before {model} substitution and
    model_flag existed (aider/cursor-agent have neither a {model} token nor
    a model_flag; claude-code/codex/gemini-cli's model_flag is a no-op
    unless model= is actually passed -- see the model_flag assertions below
    for the ANY LLM case where it IS passed).

    claude-code/codex deliberately carry NO {task} in their argv template
    (fixed 2026-07-21, see determinex_agents.py's registration comments and
    stdin_prompt flag) -- their whole prompt goes in via stdin instead, so
    it never touches the Windows command line and can't trip os error 206
    (ERROR_FILENAME_EXCED_RANGE) regardless of prompt size."""
    # argv[0] is shutil.which()-resolved (see resolve_argv's PATHEXT note) --
    # falls back to the bare probe name when not installed (cursor-agent).
    claude_exe = shutil.which("claude") or "claude"
    codex_exe = shutil.which("codex") or "codex"
    gemini_exe = shutil.which("gemini") or "gemini"
    assert agents.resolve_argv("claude-code", "do x", Path("C:/ws")) == [claude_exe, "-p"]
    assert agents._AGENTS["claude-code"].stdin_prompt is True
    assert agents.resolve_argv("codex", "do x", Path("C:/ws")) == [codex_exe, "exec"]
    assert agents._AGENTS["codex"].stdin_prompt is True
    assert agents.resolve_argv("gemini-cli", "do x", Path("C:/ws")) == [gemini_exe, "-p", "do x", "--skip-trust"]
    assert agents.resolve_argv("cursor-agent", "do x", Path("C:/ws")) == ["cursor-agent", "do x"]
    # ANY LLM: claude-code/codex/gemini-cli each have a model_flag="--model"
    # (2026-07-22) -- passing model=... now appends [--model, value] since
    # none of their templates carry a {model} token. cursor-agent has no
    # model_flag at all, so a model there IS still a harmless no-op.
    assert agents.resolve_argv("claude-code", "do x", Path("C:/ws"), model="opus") == \
        [claude_exe, "-p", "--model", "opus"]
    assert agents.resolve_argv("cursor-agent", "do x", Path("C:/ws"), model="irrelevant") == \
        ["cursor-agent", "do x"]


def test_resolve_argv_workspace_substitution(monkeypatch):
    template = ["python", "{task}", "--cwd", "{workspace}"]
    fake_agent = agents.Agent(name="_test-workspace-agent", probe="python",
                              install_hint="", runner=agents._cli_runner(template),
                              argv_template=template)
    monkeypatch.setitem(agents._AGENTS, "_test-workspace-agent", fake_agent)

    argv = agents.resolve_argv("_test-workspace-agent", "task", Path("C:/some/ws"))
    python_exe = shutil.which("python") or "python"
    assert argv == [python_exe, "task", "--cwd", str(Path("C:/some/ws"))]


def test_run_agent_still_works_after_model_param_addition(monkeypatch, tmp_path):
    """Regression: run_agent()'s existing non-chat callers (AgentsPanel.tsx via
    agent_registry.rs) never pass `model` -- confirm the default (None) still
    threads cleanly through to the runner without a TypeError."""
    calls = []

    def fake_runner(task, workspace, timeout, model=None):
        calls.append((task, workspace, timeout, model))
        return "ok", 0

    fake_agent = agents.Agent(name="_test-fake-agent", probe="python",
                              install_hint="", runner=fake_runner)
    monkeypatch.setitem(agents._AGENTS, "_test-fake-agent", fake_agent)

    # bypass real oracle for this pure plumbing check
    result = agents.run_agent("_test-fake-agent", "task", tmp_path, verify=False)
    assert result.ran is True
    assert calls[0] == ("task", tmp_path, 300, None)
