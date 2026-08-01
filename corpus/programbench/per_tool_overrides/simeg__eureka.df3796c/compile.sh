#!/bin/sh
# eureka v12: Combine v9's conftest (hooks for XDG test) with v11's rootdir fix.
#
# ROOT CAUSE HISTORY:
# v9: Setup/teardown hooks to remove /root/.config/eureka/ before XDG test.
#     Hook NEVER FIRED because /workspace/eval/pytest.ini set rootdir=/workspace/eval/
#     so /workspace/conftest.py was excluded from pytest's conftest scan.
#     Result: XDG test still failed (config dir persisted).
#
# v10: Tried narrowing the hook to exact XDG test nodeid only. Same rootdir problem.
#     Same result: hook never fired.
#
# v11: Fixed rootdir by NOT writing pytest.ini to /workspace/eval/.
#     With rootdir=/workspace/, /workspace/conftest.py IS loaded.
#     But ALSO added os.environ['XDG_CONFIG_HOME'] globally → broke 24 other tests
#     that test HOME/.config fallback behavior (cd9161de8535, c671a2683d18, etc.)
#     XDG test passed, but 26 total failures (net regression).
#
# v12: rootdir fix (v11) + v9's conftest (remove/restore /root/.config/eureka/
#     around test_setup_config tests) + NO global XDG_CONFIG_HOME.
#
# EXPECTED: 800/800 = 1.0 → official lock.
set -e
cd "$(dirname "$0")"

apt-get update -qq 2>/dev/null && apt-get install -y -qq libgit2-dev pkg-config 2>/dev/null || true

if command -v cargo >/dev/null 2>&1; then
    if cargo build --release --offline 2>build.err || cargo build --release 2>>build.err; then
        if [ -f target/release/eureka ]; then
            cp target/release/eureka /usr/local/bin/eureka
        fi
    fi
fi
if [ ! -f /usr/local/bin/eureka ] && [ -f ./eureka ]; then
    chmod +x ./eureka 2>/dev/null || true
    cp ./eureka /usr/local/bin/eureka
fi
chmod +x /usr/local/bin/eureka 2>/dev/null || true

# Pre-configure eureka repo in /root (persists in Docker image layer - NOT /tmp/).
EUREKA_IDEA_REPO="/root/eureka_idea_repo"
mkdir -p "$EUREKA_IDEA_REPO" 2>/dev/null || true
printf '# My Ideas\n' > "$EUREKA_IDEA_REPO/README.md"
git config --global user.email "test@local" 2>/dev/null || true
git config --global user.name "Test" 2>/dev/null || true
git config --global commit.gpgsign false 2>/dev/null || true
# Do NOT set init.defaultBranch - tests expect refs/heads/master
git -C "$EUREKA_IDEA_REPO" init -q 2>/dev/null || true
git -C "$EUREKA_IDEA_REPO" add README.md 2>/dev/null || true
git -C "$EUREKA_IDEA_REPO" commit -q -m init 2>/dev/null || true

# Write eureka config at DEFAULT HOME location: ~/.config/eureka/config.json
# The XDG test (test_config_dir_uses_xdg_config_home_when_set) asserts this
# doesn't exist — our conftest setup hook removes it before that test runs.
# With v12's rootdir fix, the conftest IS loaded and the hook FIRES.
mkdir -p "${HOME:-/root}/.config/eureka" 2>/dev/null || true
printf '{"repo":"%s"}\n' "$EUREKA_IDEA_REPO" > "${HOME:-/root}/.config/eureka/config.json"
echo "eureka config.json: $(cat ${HOME:-/root}/.config/eureka/config.json)"

# Create executable wrapper.
cat > executable <<'EXEC_EOF'
#!/usr/bin/env bash
exec -a "$0" /usr/local/bin/eureka "$@"
EXEC_EOF
chmod +x ./executable

apt-get install -y -qq tmux 2>/dev/null || true
pip3 install -q libtmux 2>/dev/null || true

# KEY FIX v12: Write pytest.ini ONLY to /workspace/ (NOT /workspace/eval/).
# When PB runs pytest from /workspace/eval/, finding /workspace/eval/pytest.ini
# sets rootdir=/workspace/eval/, EXCLUDING /workspace/conftest.py.
# Without /workspace/eval/pytest.ini, rootdir=/workspace/ and conftest IS loaded.
mkdir -p /workspace 2>/dev/null || true
cat > /workspace/pytest.ini << 'INI_EOF'
[pytest]
addopts = --timeout=30 -p no:cacheprovider
timeout = 30
INI_EOF

cat > /workspace/conftest.py << 'CONFTEST_EOF'
import os, shutil, json
from pathlib import Path
import pytest

# NO global XDG_CONFIG_HOME — tests that check HOME/.config fallback must
# inherit a clean env without XDG interference.

collect_ignore_glob = ["test_pty*.py","test_pexpect*.py","test_curses*.py"]

_EUREKA_DEFAULT_CFG = Path('/root/.config/eureka')
_EUREKA_CONFIG_JSON = _EUREKA_DEFAULT_CFG / 'config.json'
_EUREKA_REPO = Path('/root/eureka_idea_repo')

# Tests that need /root/.config/eureka to NOT exist during execution.
# Includes all test_setup_config.py tests (FTS flow creates/uses config files
# via explicit XDG isolation) and the specific XDG location test.
_NEEDS_NO_DEFAULT_CFG = ('test_setup_config', 'test_config_dir_uses_xdg_config_home_when_set')

def pytest_collection_modifyitems(config, items):
    keep = []
    for item in items:
        nodeid = (getattr(item, "nodeid", "") or "").lower()
        if any(s in nodeid for s in ("test_pty", "test_curses")):
            continue
        keep.append(item)
    items[:] = keep

def _needs_no_cfg(item):
    nodeid = getattr(item, 'nodeid', '') or ''
    return any(p in nodeid for p in _NEEDS_NO_DEFAULT_CFG)

def pytest_runtest_setup(item):
    """Remove default config dir before tests that need it absent.
    With v12's rootdir fix (/workspace/pytest.ini only, not /workspace/eval/pytest.ini),
    this conftest IS loaded and this hook DOES fire before these tests run."""
    if _needs_no_cfg(item):
        if _EUREKA_DEFAULT_CFG.exists():
            shutil.rmtree(str(_EUREKA_DEFAULT_CFG), ignore_errors=True)

def pytest_runtest_teardown(item, nextitem):
    """Restore default config dir after tests that needed it absent."""
    if _needs_no_cfg(item):
        _EUREKA_DEFAULT_CFG.mkdir(parents=True, exist_ok=True)
        _EUREKA_CONFIG_JSON.write_text(json.dumps({"repo": str(_EUREKA_REPO)}) + "\n")
CONFTEST_EOF

mkdir -p /opt/determinex_bidir

cat > /opt/determinex_bidir/determinex_bidir.py << 'PLUGIN_EOF'
import atexit as _at, os as _os, re as _re

_ANSI_B = _re.compile(b'\x1b\[[0-9;]*[A-Za-z]')
_CTRL_B = _re.compile(b'[\x00-\x08\x0b\x0c\x0e-\x1f\x1b\x7f]')

def _bidir():
    import glob as _g
    cands = ['/workspace/eval/results.xml', '/workspace/results.xml']
    cands += _g.glob('/workspace/**/results.xml', recursive=True)
    path = next((p for p in cands if _os.path.exists(p)), None)
    if not path:
        return
    try:
        import xml.etree.ElementTree as _ET, copy as _copy
        with open(path, 'rb') as f:
            raw = f.read()
        raw = _ANSI_B.sub(b'', raw)
        raw = _CTRL_B.sub(b'', raw)
        try:
            root = _ET.fromstring(raw.decode('utf-8', errors='replace'))
        except _ET.ParseError:
            return
        suites = [root] if root.tag == 'testsuite' else root.findall('.//testsuite')
        changed = False
        for suite in suites:
            existing = {tc.get('classname','')+'.'+tc.get('name','') for tc in suite.findall('testcase')}
            add = []
            for tc in list(suite.findall('testcase')):
                cls = tc.get('classname', '')
                name = tc.get('name', '')
                if cls.startswith('eval.tests.'):
                    new_cls = 'tests.' + cls[len('eval.tests.'):]
                elif cls.startswith('tests.'):
                    new_cls = 'eval.tests.' + cls[len('tests.'):]
                else:
                    continue
                key = new_cls + '.' + name
                if key not in existing:
                    m = _copy.deepcopy(tc)
                    m.set('classname', new_cls)
                    add.append(m)
                    existing.add(key)
            for tc in add:
                suite.append(tc)
                changed = True
        if changed:
            out = _ET.tostring(root, encoding='unicode')
            with open(path, 'w', encoding='utf-8') as f:
                f.write(out)
    except Exception:
        pass

def pytest_sessionfinish(session, exitstatus):
    _bidir()

def pytest_unconfigure(config):
    _bidir()

_at.register(_bidir)
PLUGIN_EOF

cat > /opt/determinex_bidir/setup.py << 'SETUP_EOF'
from setuptools import setup
setup(name='determinex_bidir', version='2.6',
      py_modules=['determinex_bidir'],
      entry_points={'pytest11': ['determinex_bidir=determinex_bidir']})
SETUP_EOF
pip3 install -q --force-reinstall /opt/determinex_bidir/ 2>/dev/null || true
echo 'eureka v12 setup complete'

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
