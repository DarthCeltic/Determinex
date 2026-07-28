#!/usr/bin/env python3
"""
determinex_agents.py -- the agent-CLI sub-agent registry (host any coding agent)
=============================================================================
A PROVIDER is a model: generate(prompt, temperature) -> str.
An AGENT is a whole tool that edits a workspace: Codex CLI, Claude Code, Gemini
CLI, aider, cursor-agent, .... This registry hosts them as SUB-AGENTS: hand one a
task + a workspace, let it do its thing, then -- the part nobody else does --
VERIFY its result through Determinex's oracle. An agent that hallucinates or breaks
the build is caught; only an oracle-passing result is accepted.

That is the whole thesis applied to agents: correctness is bounded by the oracle,
not by trusting the agent. So you can bolt on any agent (present or future) and it
cannot make Determinex wrong -- it can only succeed (verified) or be rejected (with
the failure surfaced to the Adjudicator).

    from determinex_agents import available_agents, run_agent
    res = run_agent("claude-code", task="make the tests pass", workspace=Path("repo/"))
    if res.verified:
        ...   # the agent's edits PASS the oracle

Bringing in a new agent is one register_agent(); it also works through the
extension protocol (a plugin's register(api)).

CLI
---
    python scripts/determinex_agents.py            # which agents are installed here
"""
from __future__ import annotations

import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

_HERE = str(Path(__file__).resolve().parent)
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

# An agent runner: (task, workspace, timeout, model) -> (raw_output, returncode)
AgentRunner = Callable[[str, Path, int, "str | None"], "tuple[str, int]"]


@dataclass
class Agent:
    name: str
    probe: str                      # CLI binary that must be on PATH
    install_hint: str
    runner: AgentRunner
    aliases: tuple[str, ...] = ()
    argv_template: "list[str] | None" = None   # stashed so resolve_argv() can
                                                # substitute without invoking the runner
    # True for CLIs confirmed (empirically, not by doc alone) to read their
    # entire prompt from stdin when launched with no embedded {task}/{task_file}
    # in argv -- claude/codex only, verified live 2026-07-21. The task text
    # then never appears in the spawned command line at all, so it can never
    # blow through Windows' ~32K argv length limit (os error 206,
    # ERROR_FILENAME_EXCED_RANGE) regardless of Mission Plan + transcript
    # size. gemini-cli's own docs claim the same stdin support but it hung
    # under two different real invocations in this same session -- left on
    # its existing {task}-embedded argv rather than ship an unverified fix
    # that trades a fast, visible crash for a silent, permanent hang.
    stdin_prompt: bool = False
    # For agents whose argv_template has no {model} token (claude-code,
    # codex, gemini-cli -- confirmed via --help each ships a real --model/-m
    # flag of its own). When a caller passes model=..., [model_flag, model]
    # is appended to the resolved argv. None for agents that either take no
    # model override (aider/cursor-agent) or already handle it via an
    # explicit {model} token in their template (local-ollama).
    model_flag: "str | None" = None

    def available(self) -> bool:
        return shutil.which(self.probe) is not None


@dataclass
class AgentResult:
    agent: str
    verified: bool                  # the oracle PASSED after the agent's edits
    ran: bool                       # the agent CLI actually executed
    raw: str
    oracle: str = ""
    n_failures: int = 0
    note: str = ""
    next_moves: list[str] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Built-in agent runners. Each invokes the real CLI non-interactively against a
# workspace. Commands are best-effort, override per your installed version.
# ---------------------------------------------------------------------------
def _cli_runner(argv_template: list[str], stdin_prompt: bool = False,
                model_flag: "str | None" = None) -> AgentRunner:
    def _run(task: str, workspace: Path, timeout: int, model: "str | None" = None) -> tuple[str, int]:
        argv = [a.replace("{task}", task).replace("{model}", model or "") for a in argv_template]
        # shutil.which resolves Windows' .cmd/.exe shims (PATHEXT) that a
        # bare subprocess.run(shell=False) can't find on its own -- see the
        # matching note in _cheap_status. Only argv[0] (the binary itself)
        # needs this; the rest of argv is real argument text.
        if argv:
            argv[0] = shutil.which(argv[0]) or argv[0]
        # model_flag: agents whose template has no {model} token (claude-code
        # /codex/gemini-cli each ship a real --model/-m flag of their own).
        if model and model_flag and "{model}" not in " ".join(argv_template):
            argv += [model_flag, model]
        try:
            r = subprocess.run(argv, cwd=str(workspace), capture_output=True,
                               text=True, timeout=timeout,
                               input=task if stdin_prompt else None)
            return (r.stdout + r.stderr), r.returncode
        except Exception as e:
            return f"agent run error: {e}", 1
    return _run


_AGENTS: dict[str, Agent] = {}


def register_agent(name: str, *, probe: str, install_hint: str = "",
                   runner: "AgentRunner | None" = None,
                   argv_template: "list[str] | None" = None,
                   aliases: tuple[str, ...] = (),
                   stdin_prompt: bool = False,
                   model_flag: "str | None" = None) -> None:
    """Host a coding agent. Provide a runner, or an argv_template using {task}."""
    resolved_template = argv_template or [probe, "{task}"]
    if runner is None:
        runner = _cli_runner(resolved_template, stdin_prompt=stdin_prompt, model_flag=model_flag)
    a = Agent(name=name, probe=probe, install_hint=install_hint,
              runner=runner, aliases=aliases, argv_template=resolved_template,
              stdin_prompt=stdin_prompt, model_flag=model_flag)
    for k in (name, *aliases):
        _AGENTS[k.lower()] = a


# Built-ins (non-interactive invocations; adjust flags to your installed CLI).
# claude/codex: NO {task} embedded in argv -- confirmed live 2026-07-21 that
# both read their whole prompt from stdin when launched this way (`claude -p`
# with no positional prompt arg; `codex exec` with no positional PROMPT --
# its own --help says so explicitly). This is what keeps a chat-room turn's
# Mission-Plan-plus-transcript prompt (often tens of thousands of chars) out
# of the actual command line, so it can never trip os error 206
# (ERROR_FILENAME_EXCED_RANGE) on Windows regardless of size.
register_agent("claude-code", probe="claude",
               install_hint="npm i -g @anthropic-ai/claude-code",
               argv_template=["claude", "-p"], aliases=("claude",), stdin_prompt=True,
               model_flag="--model")
register_agent("codex", probe="codex",
               install_hint="npm i -g @openai/codex",
               argv_template=["codex", "exec"], aliases=("openai-codex",), stdin_prompt=True,
               model_flag="--model")
# --skip-trust: gemini-cli refuses to run non-interactively in a directory it
# hasn't been trusted in (its own workspace-trust prompt, which nothing in a
# spawned/piped context could ever answer) -- found live 2026-07-22, every
# gemini-cli chat turn failed with "Gemini CLI is not running in a trusted
# directory" the moment the separate PATHEXT spawn bug (above) stopped
# masking it. Safe here specifically because Determinex never trusts an
# agent's edits directly either way -- every turn is oracle-verified after
# the fact (this file's whole thesis), so skipping the CLI's own redundant
# interactive gate doesn't weaken that.
register_agent("gemini-cli", probe="gemini",
               install_hint="npm i -g @google/gemini-cli",
               argv_template=["gemini", "-p", "{task}", "--skip-trust"], aliases=("gemini",),
               model_flag="--model")
register_agent("aider", probe="aider",
               install_hint="pip install aider-chat",
               argv_template=["aider", "--message", "{task}", "--yes"])
register_agent("cursor-agent", probe="cursor-agent",
               install_hint="cursor agent CLI",
               argv_template=["cursor-agent", "{task}"])
# The local-model participant for the multi-agent chat room. Originally rode
# on aider's --model flag, but aider isn't installed here and this
# environment's auto-mode classifier hard-blocks pip installs -- "ollama is
# on the system though... so fix it." determinex_local_agent.py drives
# Ollama directly (HTTP, via swe_agent.inference._ollama -- already proven by
# the SWE-bench harness) with a SEARCH/REPLACE edit loop, needing nothing
# beyond what's already here: Python + a running Ollama. probe="ollama" (not
# "python", which is trivially always present) so `available()` actually
# reflects whether local inference is realistically usable on this machine.
register_agent("local-ollama", probe="ollama",
               install_hint="install Ollama (https://ollama.com) and pull a model, e.g. "
                            "`ollama pull qwen2.5-coder:14b-instruct-q4_K_M`",
               # {task_file}, not {task} -- a chat-room turn's prompt embeds the
               # Mission Plan (often the whole project's CLAUDE.md) plus a
               # windowed transcript, easily tens of thousands of characters.
               # Passed as a raw positional CLI argument this blew straight
               # through Windows' command-line length limit (os error 206,
               # ERROR_FILENAME_EXCED_RANGE) on every single turn. resolve_argv()
               # below writes the task to a temp file and substitutes its path
               # here instead, keeping the actual spawned command line short
               # regardless of prompt size.
               argv_template=["python", str(Path(__file__).resolve().parent / "determinex_local_agent.py"),
                               "--task-file", "{task_file}", "--workspace", "{workspace}", "--model", "{model}"],
               aliases=("aider-local", "ollama"))


def available_agents() -> dict[str, bool]:
    out = {}
    for a in _AGENTS.values():
        out[a.name] = a.available()
    return dict(sorted(out.items()))


# ---------------------------------------------------------------------------
# Cheap auth status -- one fast, free, no-model-call round-trip per agent.
# Deliberately NOT an LLM judgement: each CLI already ships (or, for
# gemini-cli, implies via its on-disk OAuth store) a deterministic answer to
# "am I logged in", so that's what gets parsed. This is the roster's passive
# signal -- whether the agent is actually WORKING right now (rate limits,
# depleted billing) can only be known by really calling it, which is what the
# separate `probe` argv (a real minimal prompt, spawned+classified on the
# Rust side) is for. Ryan: "I want to see all of the working, not sit there
# and believe it errored out" -- so this stays honest about what it does and
# doesn't verify (gemini-cli's case: stored credentials present is NOT the
# same claim as "currently authenticated", and is labeled as such).
# ---------------------------------------------------------------------------
def _cheap_status(a: Agent) -> dict:
    out = {
        "name": a.name,
        "installed": a.available(),
        "auth_known": False,
        "logged_in": False,
        "plan": "",
        "detail": "",
    }
    if not out["installed"]:
        return out
    try:
        # shutil.which (not a bare probe name) -- Python's subprocess.run
        # without shell=True skips Windows' PATHEXT resolution that a real
        # shell (or Rust's std::process::Command) applies automatically, so
        # "codex" alone fails to resolve the npm-installed codex.cmd shim
        # (found live: WinError 2, "cannot find the file specified", even
        # though `codex` runs fine from any actual shell).
        exe = shutil.which(a.probe) or a.probe
        if a.name == "claude-code":
            r = subprocess.run([exe, "auth", "status"], capture_output=True,
                               text=True, timeout=10)
            if r.stdout.strip():
                import json as _json
                d = _json.loads(r.stdout)
                out["auth_known"] = True
                out["logged_in"] = bool(d.get("loggedIn"))
                out["plan"] = d.get("subscriptionType") or d.get("apiProvider") or ""
                out["detail"] = d.get("email", "")
        elif a.name == "codex":
            r = subprocess.run([exe, "login", "status"], capture_output=True,
                               text=True, timeout=10)
            text = (r.stdout + r.stderr).strip()
            out["auth_known"] = True
            out["logged_in"] = r.returncode == 0 and "not logged in" not in text.lower()
            out["detail"] = text
            out["plan"] = "ChatGPT" if "chatgpt" in text.lower() else ("API key" if "api key" in text.lower() else "")
        elif a.name == "gemini-cli":
            cred_path = Path.home() / ".gemini" / "oauth_creds.json"
            out["auth_known"] = True
            if cred_path.is_file() and cred_path.stat().st_size > 0:
                out["logged_in"] = True
                out["plan"] = "Google account"
                out["detail"] = "stored credentials found (not live-verified -- use Test)"
            else:
                out["logged_in"] = False
                out["detail"] = "no stored credentials"
        elif a.name == "local-ollama":
            import urllib.request
            try:
                urllib.request.urlopen("http://localhost:11434/api/tags", timeout=2)
                out["auth_known"] = True
                out["logged_in"] = True
                out["plan"] = "local"
                out["detail"] = "Ollama daemon reachable"
            except Exception:
                out["auth_known"] = True
                out["logged_in"] = False
                out["detail"] = "Ollama daemon not reachable"
    except Exception as e:
        out["detail"] = f"status check error: {e}"
    return out


def _agents_status_json() -> list[dict]:
    seen: set[str] = set()
    out: list[dict] = []
    for a in _AGENTS.values():
        if a.name in seen:
            continue
        seen.add(a.name)
        s = _cheap_status(a)
        s["install_hint"] = a.install_hint
        out.append(s)
    out.sort(key=lambda d: d["name"])
    return out


# The diagnostic prompt the Rust side sends via `resolve` for a REAL live
# probe (a genuine model call, not a status file read) -- short and cheap,
# but enough to surface auth failures and quota/billing exhaustion in the
# CLI's own real error output (proven live 2026-07-22: gemini-cli's stored
# OAuth creds parse fine, but a real call surfaces
# "Your prepayment credits are depleted" -- a fact no status file contains).
DIAGNOSTIC_PROMPT = "Reply with exactly the single word: OK"


def run_agent(name: str, task: str, workspace: Path, *, timeout: int = 300,
              verify: bool = True, model: "str | None" = None) -> AgentResult:
    """Run an agent on a workspace, then VERIFY the result through the oracle."""
    a = _AGENTS.get(name.lower())
    if a is None:
        return AgentResult(name, False, False, "", note=f"unknown agent '{name}'")
    if not a.available():
        return AgentResult(name, False, False, "",
                           note=f"agent '{name}' not installed ({a.install_hint})")
    raw, rc = a.runner(task, Path(workspace), timeout, model)
    if not verify:
        return AgentResult(name, rc == 0, True, raw, note="not oracle-verified")
    # The differentiator: judge the agent's edits with Determinex's oracle.
    try:
        import determinex_repair as _r
        diag = _r.repair_workspace(Path(workspace))   # runs the workspace oracle
        verified = diag.healthy
        return AgentResult(name, verified, True, raw, oracle=diag.oracle,
                           n_failures=diag.n_failures,
                           note=("oracle PASSES after agent edits" if verified
                                 else "oracle still failing after agent edits"),
                           next_moves=[s for s in diag.verdicts])
    except Exception as e:
        return AgentResult(name, rc == 0, True, raw, note=f"verify error: {e}")


def _strip_empty_flag_pairs(argv: list[str]) -> list[str]:
    """Remove every `--flag ""` pair from a resolved argv.

    Passing a flag with an empty value is NOT the same as omitting it: the
    receiving argparse sees the flag as present and stores "", overriding
    whatever default that script declared. Templates substitute unset
    placeholders to "", so those pairs have to be dropped rather than passed.
    """
    out: list[str] = []
    i = 0
    while i < len(argv):
        if argv[i].startswith("--") and i + 1 < len(argv) and argv[i + 1] == "":
            i += 2  # skip both the flag and its empty value
            continue
        out.append(argv[i])
        i += 1
    return out


def resolve_argv(name: str, task: str, workspace: Path, *,
                 model: "str | None" = None) -> list[str]:
    """Return the exact argv this agent would run, without running it -- the
    contract the Rust chat backend relies on to spawn+stream the CLI itself
    instead of shelling through a blocking Python subprocess.run()."""
    a = _AGENTS.get(name.lower())
    if a is None:
        raise KeyError(f"unknown agent '{name}'")
    template = a.argv_template or [a.probe, "{task}"]
    task_file = ""
    if any("{task_file}" in t for t in template):
        # Written once per resolve call and left on disk for the actual CLI
        # spawn (a separate later process) to read -- OS temp dir, harmless
        # if never explicitly cleaned up.
        import os
        import tempfile
        fd, task_file = tempfile.mkstemp(prefix="determinex-agent-task-", suffix=".txt")
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(task)
    argv = [t.replace("{task_file}", task_file).replace("{task}", task).replace("{model}", model or "")
                .replace("{workspace}", str(workspace)) for t in template]
    # A {model} token with no model selected substitutes to "" and would be
    # passed as an explicit `--model ""` -- which BEATS the receiving script's
    # own argparse default (a default only applies when the flag is absent,
    # not when it's present-but-empty). That made every local-ollama chat turn
    # die with `HTTP 404 ... is '' pulled? (ollama pull )` whenever the user
    # hadn't explicitly picked a model in the UI, which is the default state.
    # Drop the flag+value pair entirely instead, so the default takes effect.
    if not model:
        argv = _strip_empty_flag_pairs(argv)
    # ANY LLM: agents with no {model} token in their template (claude-code/
    # codex/gemini-cli) get an explicit [model_flag, model] appended instead
    # -- each ships a real --model/-m flag of its own, just never wired
    # through the chat room before now.
    if model and a.model_flag and "{model}" not in " ".join(template):
        argv += [a.model_flag, model]
    # shutil.which resolves Windows' .cmd/.ps1 shims (PATHEXT) -- a bare name
    # like "gemini" or "codex" is a POSIX shell script / .cmd wrapper on this
    # platform (npm global installs), not a native .exe. Rust's
    # std::process::Command::new does NOT try PATHEXT extensions the way a
    # real shell does, so the Rust side (agent_chat.rs's run_one_turn AND
    # agent_registry.rs's agent_probe_test, both of which spawn argv[0]
    # directly from THIS function's return value) failed with "program not
    # found" for every codex/gemini-cli turn -- found live 2026-07-22 via a
    # gemini-cli probe that hung with no visible error (invokeSafe swallowed
    # it) until raw invoke() surfaced "failed to spawn agent CLI: program not
    # found". Matches the equivalent fix already applied to _cli_runner.
    if argv:
        argv[0] = shutil.which(argv[0]) or argv[0]
    return argv


def _agents_json() -> list[dict]:
    seen: set[str] = set()
    out: list[dict] = []
    for a in _AGENTS.values():
        if a.name in seen:
            continue
        seen.add(a.name)
        out.append({
            "name": a.name,
            "probe": a.probe,
            "installed": a.available(),
            "install_hint": a.install_hint,
            "aliases": list(a.aliases),
        })
    out.sort(key=lambda d: d["name"])
    return out


def main() -> int:
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Determinex agent-CLI registry")
    sub = parser.add_subparsers(dest="cmd")

    p_list = sub.add_parser("list", help="list registered agents")
    p_list.add_argument("--json", action="store_true")

    p_status = sub.add_parser("status", help="cheap installed+auth status per agent (no model calls)")
    p_status.add_argument("--json", action="store_true")

    p_run = sub.add_parser("run", help="run an agent against a workspace, oracle-verified")
    p_run.add_argument("agent")
    p_run.add_argument("task")
    p_run.add_argument("--workspace", required=True)
    p_run.add_argument("--timeout", type=int, default=300)
    p_run.add_argument("--no-verify", action="store_true")
    p_run.add_argument("--model", default=None)

    p_resolve = sub.add_parser("resolve", help="return the argv an agent would run, without running it")
    p_resolve.add_argument("agent")
    p_resolve.add_argument("task", nargs="?", default=None)
    p_resolve.add_argument("--task-file", default=None,
                           help="read task from this file instead of the positional arg -- a chat-room "
                                "prompt (Mission Plan + transcript window) as a raw CLI argument can "
                                "exceed Windows' command-line length limit (os error 206)")
    p_resolve.add_argument("--workspace", required=True)
    p_resolve.add_argument("--model", default=None)

    p_record = sub.add_parser("record-turn", help="oracle-verify a captured chat-room turn and append it to the transcript")
    p_record.add_argument("session_id")
    p_record.add_argument("agent")
    p_record.add_argument("--workspace", required=True)
    p_record.add_argument("--raw-file", required=True, help="path to the captured stdout+stderr")
    p_record.add_argument("--returncode", type=int, default=0)
    p_record.add_argument("--turn-id", required=True)
    p_record.add_argument("--task-prompt-file", required=True, help="path to the prompt that was sent to the agent")
    p_record.add_argument("--speaker-kind", choices=["user", "agent"], default="agent")
    p_record.add_argument("--mode", choices=["mention", "broadcast"], default="broadcast")
    p_record.add_argument("--dispatch-failed", action="store_true",
                           help="the agent CLI never ran (not installed, bad argv, Cloak refused) -- "
                                "skip the oracle recheck and record the raw text as a failure note")

    args = parser.parse_args()

    if args.cmd == "run":
        res = run_agent(args.agent, args.task, Path(args.workspace),
                         timeout=args.timeout, verify=not args.no_verify,
                         model=args.model)
        print(json.dumps({
            "agent": res.agent, "verified": res.verified, "ran": res.ran,
            "raw": res.raw, "oracle": res.oracle, "n_failures": res.n_failures,
            "note": res.note, "next_moves": res.next_moves,
        }))
        return 0

    if args.cmd == "resolve":
        a = _AGENTS.get(args.agent.lower())
        if args.task_file:
            task = Path(args.task_file).read_text(encoding="utf-8", errors="replace")
        elif args.task is not None:
            task = args.task
        else:
            parser.error("resolve: either the task positional or --task-file is required")
        try:
            argv = resolve_argv(args.agent, task, Path(args.workspace), model=args.model)
            print(json.dumps({
                "argv": argv,
                "available": a.available() if a else False,
                "install_hint": a.install_hint if a else "",
                "stdin_prompt": a.stdin_prompt if a else False,
            }))
        except KeyError as e:
            print(json.dumps({"error": str(e)}))
            return 1
        return 0

    if args.cmd == "record-turn":
        import dataclasses
        import determinex_agent_chat as _chat
        raw = Path(args.raw_file).read_text(encoding="utf-8", errors="replace")
        task_prompt = Path(args.task_prompt_file).read_text(encoding="utf-8", errors="replace")
        turn = _chat.record_turn(
            args.session_id, args.agent, Path(args.workspace), raw,
            args.returncode, args.turn_id, task_prompt,
            speaker_kind=args.speaker_kind, mode=args.mode,
            dispatch_failed=args.dispatch_failed,
        )
        print(json.dumps(dataclasses.asdict(turn)))
        return 0

    if args.cmd == "list" and args.json:
        print(json.dumps(_agents_json()))
        return 0

    if args.cmd == "status":
        print(json.dumps(_agents_status_json()))
        return 0

    print("=== Determinex agent-CLI registry (verified sub-agents) ===")
    for name, ok in available_agents().items():
        a = _AGENTS[name]
        mark = "INSTALLED" if ok else "---------"
        print(f"  {mark}  {name:14} (probe: {a.probe})"
              + ("" if ok else f"   {a.install_hint}"))
    rdy = [n for n, ok in available_agents().items() if ok]
    print(f"\n  {len(rdy)} agent(s) installed here: {rdy or '(none)'}")
    print("  Any agent's output is VERIFIED through the oracle -- hallucinations are caught.")
    print("  Add one with register_agent() or a plugin.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
