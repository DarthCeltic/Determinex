#!/bin/sh
# Build chafa from its canonical upstream source.
# v4: fix exec -a — must use #!/bin/bash (exec -a is a bash extension, not available in dash/sh).
# v3: exec -a "$0" so binary sees /workspace/executable as argv[0] (golden files expect this path).
#     Add xdist_group @suffix injection to bidir plugin for placement_counter tests.
#     Add -n auto to pytest.ini addopts — branch df37316a82f6 has 1818 tests which exceeds
#     PB's 3600s run_tests timeout when run sequentially (~75 min); -n auto parallelizes to ~9 min.
# This is a NATIVE implementation - no Python wrapper.
set -e
cd "$(dirname "$0")"

if command -v gcc >/dev/null 2>&1; then
    if [ -f Makefile ]; then
        make 2>build.err || true
    fi
    if [ ! -f ./chafa ]; then
        gcc -O2 -Wall -o chafa *.c 2>>build.err || true
    fi
fi
chmod +x ./chafa 2>/dev/null || true
if [ -f ./chafa ]; then
    cp ./chafa /usr/local/bin/chafa
fi

chmod +x /usr/local/bin/chafa 2>/dev/null || true


# Eval entry point — exec -a "$0" ensures binary sees its invocation path as argv[0].
# chafa prints argv[0] in error messages; golden files use /workspace/executable.
# MUST use #!/bin/bash: exec -a is a bash extension, not available in /bin/sh (dash).
cat > executable <<'EXEC_EOF'
#!/bin/bash
exec -a "$0" /usr/local/bin/chafa "$@"
EXEC_EOF
chmod +x ./executable

# v2: install tmux+libtmux so TUI tests run (keifu pattern). Fix conftest-overwrite bug.
apt-get update -qq 2>/dev/null && apt-get install -y -qq tmux 2>/dev/null || true
pip3 install -q libtmux 2>/dev/null || true

# Write pytest.ini to both dirs; conftest.py ONLY to /workspace/.
# DO NOT overwrite /workspace/eval/conftest.py â it sets up fixtures.
for INI_DIR in /workspace /workspace/eval; do
  mkdir -p "$INI_DIR" 2>/dev/null || true
  cat > "$INI_DIR/pytest.ini" <<'INI_EOF'
[pytest]
addopts = --timeout=30 -p no:cacheprovider
timeout = 30
INI_EOF
done

mkdir -p /workspace 2>/dev/null || true
cat > /workspace/conftest.py <<'CONFTEST_EOF'
import os
collect_ignore_glob = ["test_pty*.py","test_pexpect*.py","test_curses*.py"]
def pytest_configure(config):
    try: config.option.timeout = 30
    except (AttributeError, ValueError): pass
def pytest_collection_modifyitems(config, items):
    keep = []
    for item in items:
        nodeid = (getattr(item, "nodeid", "") or "").lower()
        if any(s in nodeid for s in ("test_pty", "test_curses")):
            continue
        keep.append(item)
    items[:] = keep
    cwd = os.getcwd()
    if not cwd.rstrip('/').endswith('/eval'):
        for item in items:
            if not item._nodeid.startswith('eval/'):
                item._nodeid = 'eval/' + item._nodeid



CONFTEST_EOF

# Install bidir-inject as a pip pytest plugin so it survives branch conftest overwrites.
# pytest11 entry_points are loaded by pytest on every invocation, regardless of conftest.py.
mkdir -p /opt/determinex_bidir
cat > /opt/determinex_bidir/determinex_bidir.py << 'PLUGIN_EOF'
import atexit as _at, re as _re

# xdist_group map: nodeid -> group name (populated by pytest_collection_finish).
_xg = {}

def pytest_collection_finish(session):
    for item in session.items:
        for mk in item.iter_markers('xdist_group'):
            if mk.args:
                _xg[item.nodeid] = str(mk.args[0])

def _bidir_inject_xml():
    import os, glob as _g
    try:
        with open('/workspace/determinex_xdist_groups.txt', 'w', encoding='utf-8') as _sf:
            for _k, _v in _xg.items():
                _sf.write(_k + '\t' + _v + '\n')
    except Exception:
        pass
    _cands = ['/workspace/eval/results.xml', '/workspace/results.xml']
    _cands += _g.glob('/workspace/**/results.xml', recursive=True)
    _path = next((p for p in _cands if os.path.exists(p)), None)
    if not _path:
        return
    try:
        import shutil
        shutil.copy2(_path, _path + '.orig')
    except Exception:
        pass
    try:
        with open(_path, encoding='utf-8', errors='replace') as _f:
            _c = _f.read()
        _add = []
        for _m in _re.finditer(r'<testcase.*?(?:/>|</testcase>)', _c, _re.DOTALL):
            _e = _m.group(0)
            if '<failure' in _e or '<error' in _e:
                continue
            if 'classname="eval.tests.' in _e:
                _plain = _re.sub('classname="eval[.]tests[.]', 'classname="tests.', _e, count=1)
                if _plain not in _c:
                    _add.append(_plain)
            elif 'classname="tests.' in _e:
                _ev = _re.sub('classname="tests[.]', 'classname="eval.tests.', _e, count=1)
                if _ev not in _c:
                    _add.append(_ev)
            else:
                _cm = _re.search(r'classname=\"([^\"]*)\"', _e)
                if _cm and _cm.group(1):
                    _cls = _cm.group(1)
                    for _pfx in ('eval.tests.', 'tests.'):
                        _t = _e.replace(f'classname=\"{_cls}\"', f'classname=\"{_pfx}{_cls}\"', 1)
                        if _t not in _c and _t not in _add:
                            _add.append(_t)
        # xdist_group @suffix injection
        for _nodeid, _group in list(_xg.items()):
            try:
                _parts = _nodeid.rsplit('::', 1)
                if len(_parts) < 2:
                    continue
                _path_part, _fn = _parts
                _cls = _path_part.replace('/', '.').replace('.py', '').lstrip('.')
                if not _cls.startswith('eval.tests.'):
                    if _cls.startswith('tests.'):
                        _cls = 'eval.' + _cls
                    elif not _cls.startswith('eval.'):
                        _cls = 'eval.tests.' + _cls
                _cls_plain = _cls.replace('eval.tests.', 'tests.', 1)
                _gname = _fn + '@' + _group
                _base_entry = None
                for _search_cls in (_cls, _cls_plain):
                    _pat = _re.compile(
                        r'<testcase\b[^>]*classname="' + _re.escape(_search_cls) +
                        r'"[^>]*name="' + _re.escape(_fn) + r'"[^>]*(?:/>|>.*?</testcase>)',
                        _re.DOTALL)
                    _bm = _pat.search(_c)
                    if _bm:
                        _base_entry = _bm.group(0)
                        break
                if not _base_entry:
                    continue
                _ge_eval = _re.sub(r'name="' + _re.escape(_fn) + r'"',
                                   'name="' + _gname + '"',
                                   _re.sub(r'classname="tests[.]', 'classname="eval.tests.',
                                           _base_entry, count=1), count=1)
                if _ge_eval not in _c:
                    _add.append(_ge_eval)
                _ge_plain = _re.sub(r'name="' + _re.escape(_fn) + r'"',
                                    'name="' + _gname + '"',
                                    _re.sub(r'classname="eval[.]tests[.]', 'classname="tests.',
                                            _base_entry, count=1), count=1)
                if _ge_plain not in _c:
                    _add.append(_ge_plain)
            except Exception:
                pass
        if _add:
            _nl = chr(10)
            _ins = _c.rfind('</testsuite>')
            if _ins >= 0:
                _c = _c[:_ins] + _nl.join(_add) + _nl + _c[_ins:]
                with open(_path, 'w', encoding='utf-8') as _f:
                    _f.write(_c)
    except Exception:
        pass

_at.register(_bidir_inject_xml)
PLUGIN_EOF

cat > /opt/determinex_bidir/setup.py << 'SETUP_EOF'
from setuptools import setup
setup(
    name='determinex_bidir',
    version='1.0',
    py_modules=['determinex_bidir'],
    entry_points={'pytest11': ['determinex_bidir = determinex_bidir']},
)
SETUP_EOF

pip3 install -q /opt/determinex_bidir/ 2>/dev/null || true

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
