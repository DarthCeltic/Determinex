#!/usr/bin/env python3
"""
determinex_local_agent.py -- a real, no-extra-install local-model agent
=============================================================================
Ryan: "ollama is on the system though... so fix it." The chat room's
local-ollama participant was registered against `aider`, which isn't
installed here and can't be installed by this session (the auto-mode
classifier hard-blocks pip installs). Ollama itself IS already running on
this machine with models already pulled -- this script drives it directly,
reusing this project's own proven local-model primitives
(swe_agent.inference._ollama for the HTTP call, swe_agent.patch's
SEARCH/REPLACE parser+applicator, already battle-tested by the SWE-bench
agent) instead of depending on an external CLI package.

Same argv-driven contract as every other agent in determinex_agents.py's
registry (task positional, --workspace, --model) so it plugs into
resolve_argv()/agent_chat.rs without any special-casing.

Prompt protocol: the model is asked to prefix each edit with a
"### FILE: <relative/path>" marker line, followed by a
<<<SEARCH/===/>>>REPLACE block (swe_agent.patch's existing, fuzzy-matching
format) -- this is the one piece that doesn't already exist upstream (the
SWE-bench harness always targets one pre-known file; here the model must
name which file each edit targets, since a chat turn can touch several).

CLI
---
    python scripts/determinex_local_agent.py "<task>" --workspace W --model TAG
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

_HERE = str(Path(__file__).resolve().parent)
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from swe_agent.inference import _ollama  # noqa: E402
from swe_agent.patch import _apply_search_replace_blocks, _parse_search_replace_blocks  # noqa: E402
import determinex_local_model_bench as _bench  # noqa: E402

_FILE_MARKER_RE = re.compile(r'^###\s*FILE:\s*(.+?)\s*$', re.MULTILINE)
_MAX_LISTED_FILES = 60
_SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", "target",
             "dist", "build", ".next", ".pytest_cache"}
_DEFAULT_MODEL = "qwen2.5-coder:14b-instruct-q4_K_M"


def _list_workspace_files(workspace: Path, limit: int = _MAX_LISTED_FILES) -> list[str]:
    out: list[str] = []
    try:
        for p in sorted(workspace.rglob("*")):
            if p.is_dir():
                continue
            rel = p.relative_to(workspace)
            if any(part in _SKIP_DIRS for part in rel.parts):
                continue
            out.append(str(rel))
            if len(out) >= limit:
                break
    except OSError:
        pass
    return out


def _build_prompt(task: str, workspace: Path) -> str:
    files = _list_workspace_files(workspace)
    file_list = "\n".join(files) if files else "(empty or unreadable workspace)"
    return (
        f"{task}\n\n"
        f"--- workspace files (relative paths) ---\n{file_list}\n--- end file list ---\n\n"
        "For every change, emit a block in EXACTLY this format (one per file/edit):\n\n"
        "### FILE: relative/path/to/file.py\n"
        "<<<SEARCH\n"
        "<exact existing lines to find>\n"
        "===\n"
        "<replacement lines>\n"
        ">>>REPLACE\n\n"
        "Use a real relative path from the file list above (or a new path for a new file, "
        "with an empty SEARCH block). Only emit blocks for changes you actually intend -- "
        "don't restate the whole file. If you're only responding/discussing and not editing "
        "anything, emit no blocks at all."
    )


def _split_by_file(raw: str) -> dict:
    """Split the model's response on '### FILE: <path>' markers, returning
    {relative_path: raw_block_text_for_that_file}."""
    markers = list(_FILE_MARKER_RE.finditer(raw))
    out: dict = {}
    for i, m in enumerate(markers):
        path = m.group(1).strip()
        start = m.end()
        end = markers[i + 1].start() if i + 1 < len(markers) else len(raw)
        out.setdefault(path, "")
        out[path] += raw[start:end]
    return out


def run(task: str, workspace: Path, model: str) -> tuple[str, int]:
    """The whole loop: prompt -> local model -> per-file SEARCH/REPLACE apply.
    Returns (summary_text, returncode) matching every other agent CLI's
    (raw_output, returncode) contract."""
    prompt = _build_prompt(task, workspace)
    # _ollama's own 180s default is too short on constrained hardware --
    # live-measured 113s just to generate 2 tokens for a 14B model on a 6GB
    # card (see determinex_local_model_bench.py) -- reuse the same
    # measured/community/placeholder-tiered estimate the chat backend uses
    # for its own process-level timeout, rather than a second guessed number.
    timeout = _bench.estimate_timeout_seconds(model)
    response = _ollama(model, prompt, system=(
        "You are a careful software engineer editing a real codebase. Make "
        "minimal, correct changes using the SEARCH/REPLACE block format you "
        "were given. Never invent file content you haven't seen."
    ), timeout=timeout)
    if not response:
        return ("[local-agent] Ollama returned no response -- is it running and is "
                f"'{model}' pulled? (ollama pull {model})", 1)

    by_file = _split_by_file(response)
    if not by_file:
        # No edit blocks -- treat the whole response as a discussion/reply,
        # same as a cloud agent that only talks in a given turn.
        return (response, 0)

    lines = [response, "", "--- edits applied ---"]
    any_applied = False
    any_attempted = False
    for rel_path, block_text in by_file.items():
        blocks = _parse_search_replace_blocks(block_text)
        if not blocks:
            continue
        any_attempted = True
        target = workspace / rel_path
        try:
            current = target.read_text(encoding="utf-8", errors="replace") if target.exists() else ""
        except OSError as e:
            lines.append(f"  {rel_path}: FAILED to read ({e})")
            continue
        updated, failed = _apply_search_replace_blocks(current, blocks)
        if updated != current:
            try:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(updated, encoding="utf-8")
                any_applied = True
                lines.append(f"  {rel_path}: applied {len(blocks) - len(failed)}/{len(blocks)} block(s)")
            except OSError as e:
                lines.append(f"  {rel_path}: FAILED to write ({e})")
        if failed:
            lines.append(f"  {rel_path}: {len(failed)} block(s) did not match and were skipped")

    returncode = 0 if (any_applied or not any_attempted) else 1
    return ("\n".join(lines), returncode)


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Local Ollama-driven agent (no external CLI dependency)")
    parser.add_argument("task", nargs="?", default=None)
    parser.add_argument("--task-file", default=None,
                         help="read the task prompt from this file instead of the positional arg -- "
                              "a large prompt (mission plan + transcript window) as a raw CLI argument "
                              "can exceed Windows' command-line length limit (os error 206, "
                              "ERROR_FILENAME_EXCED_RANGE)")
    parser.add_argument("--workspace", required=True)
    parser.add_argument("--model", default=_DEFAULT_MODEL)
    args = parser.parse_args()

    if args.task_file:
        task = Path(args.task_file).read_text(encoding="utf-8", errors="replace")
    elif args.task is not None:
        task = args.task
    else:
        parser.error("either the task positional or --task-file is required")

    # An explicitly-passed-but-empty `--model ""` beats argparse's default
    # (a default only applies when the flag is absent), which would send an
    # empty model name to Ollama and 404. Callers that have no model selected
    # should omit the flag, but treat empty as "use the default" here too so a
    # regression upstream can never resurrect that failure mode.
    model = args.model.strip() if args.model else ""
    summary, code = run(task, Path(args.workspace), model or _DEFAULT_MODEL)
    print(summary)
    return code


if __name__ == "__main__":
    sys.exit(main())
