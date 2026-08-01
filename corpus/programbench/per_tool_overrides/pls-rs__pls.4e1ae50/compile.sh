#!/bin/sh
# pls v4: multi-path binary search then cargo build fallback.
# PB compiled image may have binary at target/release/pls (from upstream build).
# v2 no-rebuild was wrong (copied wrapper→circular). v3 cargo failed (no source or
# rust-version constraint blocked it). v4: search compiled paths first, then cargo.
set -e
cd "$(dirname "$0")"

# Step 1: search known pre-built binary locations in the compiled task image.
# Do NOT pick up shell scripts (magic bytes #! = 0x23 0x21).
for BIN in ./target/release/pls /usr/local/bin/pls /usr/bin/pls ./pls; do
    if [ -f "$BIN" ] && [ -x "$BIN" ] && ! head -c 2 "$BIN" 2>/dev/null | grep -q '#!'; then
        [ "$BIN" != /usr/local/bin/pls ] && cp "$BIN" /usr/local/bin/pls && chmod +x /usr/local/bin/pls
        echo "pls found at $BIN" >&2
        break
    fi
done

# Step 2: cargo build if still missing.
if [ ! -f /usr/local/bin/pls ] && command -v cargo >/dev/null 2>&1; then
    sed -i '/^rust-version/d' Cargo.toml 2>/dev/null || true
    if cargo build --release --offline 2>build.err || cargo build --release 2>>build.err; then
        [ -f target/release/pls ] && cp target/release/pls /usr/local/bin/pls
    else
        echo "cargo build failed:" >&2; sed 's/^/  /' build.err >&2
    fi
fi
chmod +x /usr/local/bin/pls 2>/dev/null || true

cat > executable <<'EXEC_EOF'
#!/usr/bin/env bash
exec -a "$0" /usr/local/bin/pls "$@"
EXEC_EOF
chmod +x ./executable

# --- determinex pty + anti-hang: install as pytest11 plugin (reliable load) ---
mkdir -p /opt/determinex_pty
cat > /opt/determinex_pty/determinex_pty_plugin.py <<'DETERMINEX_PTY_EOF'
"""determinex pty + anti-hang sidecar.  PYTEST_DONT_REWRITE

PYTEST_DONT_REWRITE is load-bearing: this module is loaded as a pytest11 plugin, so
pytest assertion-rewrites it by default. Rewriting a module that subclasses the C-level
subprocess.Popen (class _PtPopen below) corrupts the class-body code object ->
`class _PtPopen(_pt_orig_popen): TypeError: function() argument 'code' must be code, not
str` at plugin-load -> ZERO tests collected -> every test not_run -> 0/X. The docstring
marker tells pytest to skip rewriting this module. (Regression root cause, 2026-06-23.)
"""
# --- determinex anti-hang sidecar (killable subprocess timeout; opt-in tty-stdin) ---
import os as _pt_os, subprocess as _pt_sp
try:
    import pty as _pt_pty
except Exception:
    _pt_pty = None
_PT_TIMEOUT = float(_pt_os.environ.get("DETERMINEX_PTY_TIMEOUT", "30"))
# tty-stdin is OPT-IN: handing a TUI tool a pty makes isatty(0)==True, which pushes
# NON-interactive tools (gdu -n, etc.) INTO interactive mode -> they then block. The
# universal, always-safe anti-hang is the subprocess timeout below; only set
# DETERMINEX_PTY_STDIN=1 for a tool that genuinely refuses a non-tty.
_PT_STDIN_TTY = _pt_os.environ.get("DETERMINEX_PTY_STDIN", "0") == "1"
_pt_orig_run = _pt_sp.run
_pt_orig_popen = _pt_sp.Popen


def _pt_is_tool(args):
    a = args if isinstance(args, (list, tuple)) else [args]
    j = " ".join(map(str, a))
    return ("/workspace/executable" in j or j.strip().startswith("./executable")
            or j.strip().startswith("executable") or "/usr/local/bin/" in j)


def _pt_killpg(proc):
    try:
        _pt_os.killpg(_pt_os.getpgid(proc.pid), 9)
    except Exception:
        try: proc.kill()
        except Exception: pass


def _pt_run(args, *p, **k):
    if not _pt_is_tool(args):
        return _pt_orig_run(args, *p, **k)
    k.setdefault("start_new_session", True)          # own group -> killable as a tree
    if not k.get("timeout"):
        k["timeout"] = _PT_TIMEOUT                   # subprocess waitpid-timeout (works where SIGALRM can't)
    _fds = []
    if _PT_STDIN_TTY and _pt_pty is not None and "stdin" not in k and "input" not in k:
        try:
            _m, _s = _pt_pty.openpty(); k["stdin"] = _s; _fds = [_m, _s]
        except Exception:
            _fds = []
    try:
        return _pt_orig_run(args, *p, **k)
    finally:
        for _fd in _fds:                              # CLOSE both pty fds -> no leak (the gdu fd-exhaustion bug)
            try: _pt_os.close(_fd)
            except Exception: pass


# ROOT-CAUSE GUARD (2026-06-23): a sibling determinex plugin (droppriv) function-wraps
# subprocess.Popen and loads BEFORE pty (alphabetical), so _pt_orig_popen can already be a
# FUNCTION -> `class _PtPopen(<function>)` raises TypeError (argument 'code' must be code,
# not str) at plugin-load -> 0 tests collected. Only subclass when Popen is still a real
# class; the always-safe subprocess.run timeout wrapper applies regardless.
if isinstance(_pt_orig_popen, type):
    class _PtPopen(_pt_orig_popen):
        def __init__(self, args, *p, **k):
            self._pt_tool = _pt_is_tool(args)
            if self._pt_tool:
                k.setdefault("start_new_session", True)
            super().__init__(args, *p, **k)

        def communicate(self, input=None, timeout=None):
            if getattr(self, "_pt_tool", False) and timeout is None:
                timeout = _PT_TIMEOUT
            try:
                return super().communicate(input=input, timeout=timeout)
            except _pt_sp.TimeoutExpired:
                _pt_killpg(self)
                raise
    _pt_sp.Popen = _PtPopen

_pt_sp.run = _pt_run
# --- end determinex pty + anti-hang sidecar ---
DETERMINEX_PTY_EOF
cat > /opt/determinex_pty/setup.py <<'DETERMINEX_PTY_SETUP'
from setuptools import setup
setup(name="determinex_pty", version="1.0", py_modules=["determinex_pty_plugin"],
      entry_points={"pytest11": ["determinex_pty = determinex_pty_plugin"]})
DETERMINEX_PTY_SETUP
( cd /opt/determinex_pty && pip3 install -q . 2>/dev/null || pip install -q . 2>/dev/null || true )

# --- determinex subprocess guard: a hung tool invocation can't hang the eval (pytest-timeout signal-method can't kill a hung child -- the lz4 hang) ---
mkdir -p /opt/determinex_subproc_guard
cat > /opt/determinex_subproc_guard/determinex_subprocess_guard.py <<'DETERMINEX_GUARD_EOF'
"""determinex_subprocess_guard -- pytest11 plugin: a hung tool invocation can't hang the whole eval.

THE HANG (lz4 class): a test does subprocess.run([tool, ...]) / Popen(...).communicate() with NO
inner timeout, and the tool blocks forever on a C-level read (e.g. reading stdin with no EOF).
pytest-timeout's default SIGALRM raises in the test thread, BUT `with Popen() as p:` then calls
p.__exit__ -> p.wait(), which blocks on the still-running child -> the eval hangs past the per-test
timeout (lz4 ran >1800s with --timeout=30 set). pytest-timeout is defeated because it never KILLS
the child.

THE FIX: monkeypatch subprocess so every child (a) starts in its own session (killpg targets the
whole tree), (b) gets a real default timeout if the test didn't set one, and (c) is process-group
KILLED on timeout. A hung tool invocation then dies, the test fails fast (TimeoutExpired), and the
eval COMPLETES -- the tool gets scored -> gated -> fixed, instead of hanging. Systemic: install in
every compile.sh (like the bidir/hermetic plugins) so ANY hung-child tool is handled.

Env: DETERMINEX_SUBPROC_TIMEOUT (default 60s). Loaded as a pytest11 plugin OR imported directly.
"""
from __future__ import annotations

import os
import signal
import subprocess
import sys

_T = int(os.environ.get("DETERMINEX_SUBPROC_TIMEOUT", "60"))
_NT = os.name == "nt"


def _killpg(proc) -> None:
    """Kill the child's whole process group so a tool that forked grandchildren can't survive."""
    killpg = getattr(os, "killpg", None)
    getpgid = getattr(os, "getpgid", None)
    try:
        if not _NT and killpg and getpgid:
            killpg(getpgid(proc.pid), getattr(signal, "SIGKILL", 9))
            return
    except Exception:
        pass
    try:
        proc.kill()
    except Exception:
        pass


def install() -> None:
    """Monkeypatch subprocess.Popen.__init__/communicate and subprocess.run. Idempotent."""
    if getattr(subprocess, "_determinex_guarded", False):
        return
    subprocess._determinex_guarded = True  # type: ignore[attr-defined]

    _real_init = subprocess.Popen.__init__
    def _init(self, *a, **kw):  # child gets its own session so killpg hits the whole tree
        if not _NT and "start_new_session" not in kw and kw.get("preexec_fn") is None:
            kw["start_new_session"] = True
        _real_init(self, *a, **kw)
    subprocess.Popen.__init__ = _init  # type: ignore[assignment]

    _real_comm = subprocess.Popen.communicate
    def _comm(self, input=None, timeout=None):  # default timeout + killpg on ANY exit
        if timeout is None:
            timeout = _T
        try:
            return _real_comm(self, input=input, timeout=timeout)
        except BaseException:
            # ANY exit from communicate -> kill the child's group. Covers our own TimeoutExpired
            # AND pytest-timeout's SIGALRM exception (signal-method canNOT kill the child itself --
            # the lz4 hang). Without this the child outlives the timeout and Popen.__exit__'s wait()
            # blocks on it forever -> the whole eval hangs.
            _killpg(self)
            try:
                _real_comm(self, timeout=5)  # reap so the parent's pipe wait can't hang
            except Exception:
                pass
            raise
    subprocess.Popen.communicate = _comm

    # Popen.__exit__ calls wait() -- give it a bounded timeout + killpg so it can NEVER block on a
    # still-running child (the exact place the lz4 eval hung).
    _real_wait = subprocess.Popen.wait
    def _wait(self, timeout=None):
        # An EXPLICIT timeout (e.g. communicate's internal self.wait) must behave normally -- raise
        # TimeoutExpired so the caller can propagate it. Only a BARE wait() (Popen.__exit__, or a
        # test's p.wait() on a hung child) gets bounded + killpg'd so it can't block forever.
        if timeout is not None:
            return _real_wait(self, timeout=timeout)
        try:
            return _real_wait(self, timeout=_T)
        except subprocess.TimeoutExpired:
            _killpg(self)
            try:
                return _real_wait(self, timeout=5)
            except Exception:
                return -9
    subprocess.Popen.wait = _wait  # type: ignore[assignment]  # type: ignore[assignment]

    _real_run = subprocess.run
    def _run(*a, **kw):
        # (1) a default timeout, and (2) a NON-BLOCKING stdin. The #1 hang cause is a tool that
        # reads stdin (filter mode) invoked as subprocess.run([tool], capture_output=True) with no
        # input -> it blocks on a C-level read FOREVER (the 23.5h orphan; lz4's tests timing out at
        # 5s then rerun x3 = the slow "hang"). Defaulting stdin to DEVNULL gives it immediate EOF ->
        # it returns at once, no timeout, no rerun. Scoped to run() (not Popen) so xdist/execnet,
        # which set stdin=PIPE explicitly on their gateway Popen, are untouched. Respect any caller
        # that provides input= or its own stdin.
        if kw.get("timeout") is None:
            kw["timeout"] = _T
        if not _NT and kw.get("input") is None and kw.get("stdin") is None and len(a) <= 3:
            kw["stdin"] = subprocess.DEVNULL
        return _real_run(*a, **kw)
    subprocess.run = _run  # type: ignore[assignment]


_WATCHDOG = int(os.environ.get("DETERMINEX_TEST_WATCHDOG", "90"))


# A daemon the tests spawn that REPARENTS away from pytest (so killing direct children misses it)
# and KEEPS THE OUTPUT PIPE OPEN -> the outer harness's subprocess.run(docker)->select() never sees
# EOF even after pytest exits. tmux is the archetype (its server double-forks to PID 1); the tool
# binary launched in a tmux pane (/workspace/executable, the PB convention) is the other. Matched by
# cmdline so they die regardless of where they reparented. DETERMINEX_GUARD_KILL adds more patterns.
_ESCAPERS = ["tmux", "/workspace/executable"] + [
    p for p in os.environ.get("DETERMINEX_GUARD_KILL", "").split(",") if p.strip()
]


def _kill_children() -> None:
    """Kill the hung test's spawned processes so a hung select()/read() unblocks AND the outer eval
    harness's docker pipe can finally close. Two targets, both by scanning /proc:
      (1) DIRECT children of this pytest process (their groups -- our patched Popen gives each its
          own session, so killpg takes the whole subtree); and
      (2) ESCAPED daemons (tmux server, the tool binary) matched by cmdline -- these reparent to
          PID 1 and hold the inherited stdout fd open, which is the REAL reason the lz4/TUI evals
          hang forever (docker never sees EOF). Killing direct children alone misses them."""
    me = os.getpid()
    killpg = getattr(os, "killpg", None)
    getpgid = getattr(os, "getpgid", None)
    sig = getattr(signal, "SIGKILL", 9)
    targets: set[int] = set()
    try:
        for d in os.listdir("/proc"):
            if not d.isdigit():
                continue
            pid = int(d)
            if pid == me:
                continue
            try:
                stat = open("/proc/" + d + "/stat", encoding="utf-8").read()
                ppid = int(stat.rsplit(")", 1)[1].split()[1])  # robust to comm with spaces/parens
            except Exception:
                ppid = 0
            escaped = False
            if pid != me:
                try:
                    cmd = open("/proc/" + d + "/cmdline", "rb").read().replace(b"\x00", b" ").decode("utf-8", "replace")
                except Exception:
                    cmd = ""
                escaped = any(pat in cmd for pat in _ESCAPERS)
            if ppid == me or escaped:
                targets.add(pid)
    except Exception:
        pass
    if not targets:
        return
    try:  # one marker on the REAL stderr (bypasses pytest capture) so a fired watchdog is visible
        err = sys.__stderr__ or sys.stderr
        if err is not None:
            err.write(f"determinex-guard: killing {len(targets)} hung proc(s) [tmux/executable/children]\n")
            err.flush()
    except Exception:
        pass
    for pid in targets:
        try:
            if killpg and getpgid:
                killpg(getpgid(pid), sig)
            else:
                os.kill(pid, sig)
        except Exception:
            try:
                os.kill(pid, sig)
            except Exception:
                pass


# pytest11 entry-point hook: pytest imports this plugin and calls the hooks below.
def pytest_configure(config):  # noqa: ARG001
    install()


def pytest_sessionfinish(session, exitstatus):  # noqa: ARG001
    # THE decisive hook for the lz4/TUI class: when pytest finishes (even after signal-timeout has
    # marked hung tests failed), a tmux server or the tool binary can still be alive -- reparented to
    # PID 1, holding the inherited stdout fd. That keeps the OUTER eval harness's subprocess.run(
    # docker)->select() from ever seeing EOF, so the eval hangs at 100% forever. Killing the escapers
    # here lets docker's pipe close, the harness return, and the tool finally get SCORED.
    _kill_children()


try:  # the per-test watchdog hook (only when loaded as a pytest plugin)
    import pytest as _pytest

    @_pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_protocol(item, nextitem):  # noqa: ARG001
        import threading
        done = threading.Event()

        def _watch():
            if not done.wait(_WATCHDOG):  # the whole test protocol exceeded the watchdog
                _kill_children()          # -> kill its children so an orphan-pipe select/read unblocks

        th = threading.Thread(target=_watch, daemon=True)
        th.start()
        try:
            yield
        finally:
            done.set()
except Exception:
    pass


# Importing the module also installs (covers conftest `import determinex_subprocess_guard`).
install()
DETERMINEX_GUARD_EOF
cat > /opt/determinex_subproc_guard/setup.py <<'DETERMINEX_GUARD_SETUP'
from setuptools import setup
setup(name='determinex_subprocess_guard', version='1.0', py_modules=['determinex_subprocess_guard'],
      entry_points={'pytest11': ['determinex_subprocess_guard = determinex_subprocess_guard']})
DETERMINEX_GUARD_SETUP
( cd /opt/determinex_subproc_guard && pip3 install -q . 2>/dev/null || pip install -q . 2>/dev/null || true )
# --- end determinex subprocess guard ---
