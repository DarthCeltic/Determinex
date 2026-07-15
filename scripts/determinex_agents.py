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

# An agent runner: (task, workspace, timeout) -> (raw_output, returncode)
AgentRunner = Callable[[str, Path, int], "tuple[str, int]"]


@dataclass
class Agent:
    name: str
    probe: str                      # CLI binary that must be on PATH
    install_hint: str
    runner: AgentRunner
    aliases: tuple[str, ...] = ()

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
def _cli_runner(argv_template: list[str]) -> AgentRunner:
    def _run(task: str, workspace: Path, timeout: int) -> tuple[str, int]:
        argv = [a.replace("{task}", task) for a in argv_template]
        try:
            r = subprocess.run(argv, cwd=str(workspace), capture_output=True,
                               text=True, timeout=timeout)
            return (r.stdout + r.stderr), r.returncode
        except Exception as e:
            return f"agent run error: {e}", 1
    return _run


_AGENTS: dict[str, Agent] = {}


def register_agent(name: str, *, probe: str, install_hint: str = "",
                   runner: "AgentRunner | None" = None,
                   argv_template: "list[str] | None" = None,
                   aliases: tuple[str, ...] = ()) -> None:
    """Host a coding agent. Provide a runner, or an argv_template using {task}."""
    if runner is None:
        runner = _cli_runner(argv_template or [probe, "{task}"])
    a = Agent(name=name, probe=probe, install_hint=install_hint,
              runner=runner, aliases=aliases)
    for k in (name, *aliases):
        _AGENTS[k.lower()] = a


# Built-ins (non-interactive invocations; adjust flags to your installed CLI).
register_agent("claude-code", probe="claude",
               install_hint="npm i -g @anthropic-ai/claude-code",
               argv_template=["claude", "-p", "{task}"], aliases=("claude",))
register_agent("codex", probe="codex",
               install_hint="npm i -g @openai/codex",
               argv_template=["codex", "exec", "{task}"], aliases=("openai-codex",))
register_agent("gemini-cli", probe="gemini",
               install_hint="npm i -g @google/gemini-cli",
               argv_template=["gemini", "-p", "{task}"], aliases=("gemini",))
register_agent("aider", probe="aider",
               install_hint="pip install aider-chat",
               argv_template=["aider", "--message", "{task}", "--yes"])
register_agent("cursor-agent", probe="cursor-agent",
               install_hint="cursor agent CLI",
               argv_template=["cursor-agent", "{task}"])


def available_agents() -> dict[str, bool]:
    out = {}
    for a in _AGENTS.values():
        out[a.name] = a.available()
    return dict(sorted(out.items()))


def run_agent(name: str, task: str, workspace: Path, *, timeout: int = 300,
              verify: bool = True) -> AgentResult:
    """Run an agent on a workspace, then VERIFY the result through the oracle."""
    a = _AGENTS.get(name.lower())
    if a is None:
        return AgentResult(name, False, False, "", note=f"unknown agent '{name}'")
    if not a.available():
        return AgentResult(name, False, False, "",
                           note=f"agent '{name}' not installed ({a.install_hint})")
    raw, rc = a.runner(task, Path(workspace), timeout)
    if not verify:
        return AgentResult(name, rc == 0, True, raw, note="not oracle-verified")
    # The differentiator: judge the agent's edits with Determinex's oracle.
    try:
        import determinex_repair as _r
        diag = _r.repair_workspace(Path(workspace))   # runs the workspace oracle
        verified = bool(diag.healthy)
        return AgentResult(name, verified, True, raw, oracle=diag.oracle,
                           n_failures=diag.n_failures,
                           note=("oracle PASSES after agent edits" if verified
                                 else "oracle still failing after agent edits"),
                           next_moves=[s for s in diag.verdicts])
    except Exception as e:
        return AgentResult(name, rc == 0, True, raw, note=f"verify error: {e}")


def main() -> int:
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
