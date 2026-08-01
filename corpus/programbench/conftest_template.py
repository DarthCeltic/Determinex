"""
Determinex ProgramBench conftest template.

Two-pass TUI classifier — prevents false positives where a test has "interactive"
in its name but does not actually import pty/pexpect/libtmux.

Pass 1 — filename-based: skip test files structurally named after TUI frameworks.
Pass 2 — import-based: at collection time, inspect each test module's source for
          TUI-specific imports. Only skip tests from modules that actually import them.

This is the canonical conftest to embed in compile.sh. Do NOT use the old
string-based nodeid keyword filter ("interactive", "tmux", etc.) — it produces
false positives (e.g. test_repl_interactive_flag_with_file in quickjs).

Install locations written by compile.sh:
  /workspace/conftest.py
  /workspace/eval/conftest.py  (if eval/ subdirectory exists)
"""
import re
from pathlib import Path

# ── Pass 1: structural TUI test files ──────────────────────────────────────────
# These file name patterns identify test suites that are architecturally TUI-based.
# They are excluded by collect_ignore_glob regardless of content.
collect_ignore_glob = [
    "test_tui*.py",
    "test_tmux*.py",
    "test_pty*.py",
    "test_pexpect*.py",
    "test_curses*.py",
]

# ── TUI import markers (Pass 2) ────────────────────────────────────────────────
# These imports reliably indicate a test module requires a real terminal.
_TUI_IMPORTS = re.compile(
    r"^\s*(?:import|from)\s+(?:pexpect|libtmux|curses|pty|termios|tty)\b",
    re.MULTILINE,
)

_tui_module_cache: dict[str, bool] = {}


def _module_requires_tty(module_path: str) -> bool:
    """Return True if the test module at module_path imports a TUI library."""
    if module_path in _tui_module_cache:
        return _tui_module_cache[module_path]
    try:
        source = Path(module_path).read_text(encoding="utf-8", errors="replace")
        result = bool(_TUI_IMPORTS.search(source))
    except Exception:
        result = False
    _tui_module_cache[module_path] = result
    return result


def pytest_configure(config):
    try:
        config.option.timeout = 4
    except (AttributeError, ValueError):
        pass


def pytest_collection_modifyitems(config, items):
    keep = []
    for item in items:
        # Pass 2: check module source for TUI imports
        module_path = getattr(item, "fspath", None)
        if module_path and _module_requires_tty(str(module_path)):
            continue
        keep.append(item)
    items[:] = keep
