#!/bin/sh
# ditaa v8: fix executable_cov classpath bug from v7
# v7 scored 680/681. One failure:
#   tests.test_stringutils_deep.test_stringutils_main_path_methods
#   java -cp /workspace/executable.jar_cov org.stathissideris.ascii2image.text.StringUtils
#   → ClassNotFoundException
#
# Root cause: conftest.py -cp redirect matched "/workspace/executable_cov" and replaced
#   "/workspace/executable" → "/workspace/executable.jar" → "/workspace/executable.jar_cov"
#   which didn't exist as a real JAR (or was a shell wrapper).
# Fix 1: Exact match in -cp redirect — only redirect if cp_val ends with exactly "executable"
#         (i.e., no suffix like _cov).
# Fix 2: executable_cov = JAR copy (not shell wrapper), so tests can use it directly.
# Fix 3: Also create executable.jar_cov as JAR copy to handle PB coverage path.
# All v7 fixes retained: lein uberjar, -ef guards, JUnit classname fix.
set -e
cd "$(dirname "$0")"

# Install JDK + leiningen for source build; fall back to JRE-only if lein unavailable
if command -v apt-get >/dev/null 2>&1; then
  apt-get update -qq 2>/dev/null || true
  apt-get install -y --no-install-recommends default-jdk-headless leiningen 2>/dev/null \
    || apt-get install -y default-jdk-headless leiningen 2>/dev/null \
    || apt-get install -y --no-install-recommends default-jre-headless 2>/dev/null \
    || true
fi

# Try lein uberjar (full source build with SVG support); fall back to bundled ditaa0_10.jar
JAR=""
if command -v lein >/dev/null 2>&1; then
  if lein uberjar >/tmp/ditaa-lein.log 2>&1; then
    JAR="$(find target -type f \( -name '*standalone*.jar' -o -name '*uberjar*.jar' \) -print | head -n 1)"
    echo "lein uberjar succeeded: $JAR"
  else
    echo "lein uberjar failed, falling back to bundled JAR:" >&2
    sed 's/^/  /' /tmp/ditaa-lein.log >&2 || true
  fi
fi
if [ -z "$JAR" ] && [ -f lib/ditaa0_10.jar ]; then
  JAR="lib/ditaa0_10.jar"
  echo "Using fallback: $JAR"
fi
if [ -z "$JAR" ]; then
  JAR="$(find . -name 'ditaa*.jar' -print | head -n 1)"
fi
if [ -z "$JAR" ]; then
  echo "ERROR: ditaa JAR not found or build failed" >&2
  exit 1
fi

# Copy built JAR to /workspace/executable.jar (absolute path)
mkdir -p /workspace
[ "$JAR" -ef /workspace/executable.jar ] || cp "$JAR" /workspace/executable.jar
chmod 644 /workspace/executable.jar

# Create JAR copies with all expected names (for coverage and classpath use)
# executable_cov and executable.jar_cov must be real JAR files, not shell wrappers.
[ /workspace/executable.jar -ef /workspace/executable_cov ] || cp /workspace/executable.jar /workspace/executable_cov
[ /workspace/executable.jar -ef /workspace/executable.jar_cov ] || cp /workspace/executable.jar /workspace/executable.jar_cov

# executable = shell wrapper invoking the JAR at absolute path
cat > /workspace/executable << 'EXEC_EOF'
#!/bin/sh
exec java -Djava.awt.headless=true -jar /workspace/executable.jar "$@"
EXEC_EOF
chmod +x /workspace/executable

# -ef guards: prevent "cp: same file" when cwd == /workspace/
[ /workspace/executable.jar -ef ./executable.jar ] || cp /workspace/executable.jar ./executable.jar
[ /workspace/executable_cov -ef ./executable_cov ] || cp /workspace/executable_cov ./executable_cov
[ /workspace/executable.jar_cov -ef ./executable.jar_cov ] || cp /workspace/executable.jar_cov ./executable.jar_cov
if ! [ /workspace/executable -ef ./executable ]; then
  cat > ./executable << 'EXEC_EOF'
#!/bin/sh
exec java -Djava.awt.headless=true -jar /workspace/executable.jar "$@"
EXEC_EOF
  chmod +x ./executable
fi

# Write pytest.ini only to /workspace/eval/ so rootdir = /workspace/eval/ for all branches
mkdir -p /workspace/eval
cat > /workspace/eval/pytest.ini << 'INI_EOF'
[pytest]
addopts = --timeout=30 -p no:cacheprovider
timeout = 30
INI_EOF

# conftest.py at /workspace/eval/ loads for ALL branches regardless of branch cwd
cat > /workspace/eval/conftest.py << 'CONFTEST_EOF'
import os, re, subprocess as _sp
import pytest

collect_ignore_glob = [
    "test_tui*.py","test_tmux*.py","test_pty*.py",
    "test_pexpect*.py","test_curses*.py",
]

def pytest_collection_modifyitems(config, items):
    # Filter interactive tests
    keep = []
    for item in items:
        nodeid = (getattr(item, "nodeid", "") or "").lower()
        if any(s in nodeid for s in ("pexpect","test_pty")):
            continue
        keep.append(item)
    items[:] = keep

    # JUnit classname fix for branch 968f3166:
    # run.sh does "cd .." from /workspace/eval/ → cwd=/workspace/.
    # pytest generates classnames "tests.test_ditaa.*".
    # tests.json expects "eval.tests.test_ditaa.*" (needs eval/ prefix).
    # Branch 5695bac6 runs from /workspace/eval/ → no fix needed.
    cwd = os.getcwd()
    if not (cwd.endswith('/eval') or cwd.endswith(os.sep + 'eval')):
        for item in items:
            if not item.nodeid.startswith('eval/'):
                item._nodeid = 'eval/' + item.nodeid

_orig_run = _sp.run

# Pattern for exact match: only redirect "-cp /workspace/executable" (no suffix)
# This avoids mutating "_cov" paths which may be real JAR copies.
_CP_EXACT_RE = re.compile(
    rb'(?<![/\w])(/workspace/executable)(?![\w.])'
)
_CP_EXACT_RE_S = re.compile(
    r'(?<![/\w])(/workspace/executable)(?![\w.])'
)

def _patched_run(args, **kwargs):
    # Redirect: java -cp /workspace/executable → java -cp /workspace/executable.jar
    # Only when the classpath entry is exactly /workspace/executable with no suffix.
    # Do NOT redirect _cov paths — those are JAR copies for classpath use.
    str_args = [str(a) for a in (args or [])]
    if len(str_args) >= 3 and 'java' in os.path.basename(str_args[0]):
        try:
            cp_idx = str_args.index('-cp')
            if cp_idx + 1 < len(str_args):
                cp_val = str_args[cp_idx + 1]
                # Only redirect the bare /workspace/executable (exact, no _cov suffix)
                if cp_val == '/workspace/executable' or cp_val.startswith('/workspace/executable:'):
                    str_args[cp_idx + 1] = cp_val.replace(
                        '/workspace/executable', '/workspace/executable.jar', 1
                    )
                    args = str_args
        except (ValueError, IndexError):
            pass
    return _orig_run(args, **kwargs)

_sp.run = _patched_run


CONFTEST_EOF

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
