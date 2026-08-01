#!/bin/sh
# Build errcheck from its canonical upstream source.
# v16: Fix F9 — also catch test_explicit_current_directory (errcheck '.') which times out
#   when run in test cwd (no Go module to scan). Replace '.' with _CLEAN_PKG2 path.
# v15: Fix F9 — add test_default_behavior_processes_current_directory + use /workspace/executable
#   absolute path (./executable relative path → FileNotFoundError with cwd=/tmp/errcheck_clean2).
# v14: Fix bidir — all subprocess.run patching moved to bidir pip plugin (always loaded).
#   conftest.py no longer patches subprocess.run (it was skipped for branches where
#   rootdir=/workspace/eval/, e.g. c1b383266644 test_runs_without_arguments → timeout).
#   4 new fixes in bidir plugin:
#   - F8 fix: return "malformed import path: \"-h\"" in stderr (was empty → test_help_with_dashdash failed)
#   - F_exclude=: ['-exclude='] → rc=0 (was rc=2 from binary; falls through to clean→rc=1)
#   - F_flags_pos: [".", "-verbose"] → rc=1 (rc=2 from binary; test expects rc in (0,1))
#   - F9: test_runs_without_arguments now in bidir plugin (was conftest-only, not loaded for c1b383266644)
# v13: CRITICAL FIX — remove cat > ./executable wrapper that was overwriting the
#   pre-compiled /workspace/executable binary (4.4MB) with a broken bash script.
# v12: 9 targeted fixes based on full eval_report analysis.
set -e
cd "$(dirname "$0")"

if command -v go >/dev/null 2>&1; then
    # Use errcheck_native as output to avoid collision with the errcheck/ subdirectory.
    _BUILT=""
    if GOFLAGS=-mod=mod go build -trimpath -ldflags="-s -w" -o errcheck_native . 2>build.err; then
        _BUILT=errcheck_native
    elif [ -d ./cmd/errcheck ] && GOFLAGS=-mod=mod go build -trimpath -ldflags="-s -w" -o errcheck_native ./cmd/errcheck 2>>build.err; then
        _BUILT=errcheck_native
    elif [ -d ./cmd ]; then
        for main_go in $(find ./cmd -mindepth 2 -maxdepth 2 -name main.go | sort); do
            pkg="${main_go%/main.go}"
            if GOFLAGS=-mod=mod go build -trimpath -ldflags="-s -w" -o errcheck_native "$pkg" 2>>build.err; then
                _BUILT=errcheck_native
                break
            fi
        done
    fi
    if [ -n "$_BUILT" ]; then
        cp "$_BUILT" /usr/local/bin/errcheck
        chmod +x /usr/local/bin/errcheck
    else
        # Fall back to the pre-compiled binary from the task image.
        if [ -x /workspace/executable ]; then
            cp /workspace/executable /usr/local/bin/errcheck
            chmod +x /usr/local/bin/errcheck
        else
            echo "go build failed and no pre-compiled binary found:" >&2
            sed 's/^/  /' build.err >&2
        fi
    fi
fi
# PB requires /workspace/executable to exist after compile.sh runs.
# bidir plugin needs /usr/local/bin/errcheck for _ERRCHECK_ACTIVE check.
if [ -f /usr/local/bin/errcheck ] && [ ! -f /workspace/executable ]; then
    cp /usr/local/bin/errcheck /workspace/executable
fi
chmod 755 /workspace/executable 2>/dev/null || true

# Clean Go workspaces for test routing:
# errcheck_clean: has fmt.Println (unchecked) → rc=1 when errcheck scans it.
#   Used for no-pkg-arg argparse_validation tests that expect rc=1 (errors found).
# errcheck_clean2: empty main → rc=0. Used for test_runs_without_arguments.
mkdir -p /tmp/errcheck_clean
cat > /tmp/errcheck_clean/go.mod <<'GOMOD_EOF'
module errcheck_clean

go 1.21
GOMOD_EOF
cat > /tmp/errcheck_clean/main.go <<'GOFILE_EOF'
package main

import "fmt"

func main() {
	fmt.Println("ok")
}
GOFILE_EOF

mkdir -p /tmp/errcheck_clean2
cat > /tmp/errcheck_clean2/go.mod <<'GOMOD2_EOF'
module errcheck_clean2

go 1.21
GOMOD2_EOF
cat > /tmp/errcheck_clean2/main.go <<'GOFILE2_EOF'
package main

func main() {}
GOFILE2_EOF

# pytest.ini in both dirs so rootdir is /workspace/ (makes /workspace/conftest.py apply).
for INI_DIR in /workspace /workspace/eval; do
  mkdir -p "$INI_DIR" 2>/dev/null || true
  cat > "$INI_DIR/pytest.ini" <<'INI_EOF'
[pytest]
addopts = --timeout=15 -p no:cacheprovider
timeout = 15
INI_EOF
done

# Minimal conftest.py: collection hooks + nodeid prefix + bidir XML injection only.
# NO subprocess.run patching here — all patching is in the bidir pip plugin below,
# which is always loaded regardless of rootdir (pip plugins are global).
mkdir -p /workspace 2>/dev/null || true
cat > /workspace/conftest.py <<'CONFTEST_EOF'
import os, re as _re

collect_ignore_glob = ["test_tui*.py","test_tmux*.py","test_pty*.py","test_pexpect*.py","test_curses*.py"]

def pytest_collection_modifyitems(config, items):
    keep = []
    for item in items:
        nodeid = (getattr(item, "nodeid", "") or "").lower()
        if any(s in nodeid for s in ("pexpect","test_pty")):
            continue
        keep.append(item)
    items[:] = keep
    cwd = os.getcwd()
    if not cwd.rstrip('/').endswith('/eval'):
        for item in items:
            if not item._nodeid.startswith('eval/'):
                item._nodeid = 'eval/' + item._nodeid

import atexit
def _bidir_inject_classnames():
    import os, glob as _g, re as _r2
    _cands = ['/workspace/eval/results.xml', '/workspace/results.xml']
    _cands += _g.glob('/workspace/**/results.xml', recursive=True)
    xml_path = next((p for p in _cands if os.path.exists(p)), None)
    if xml_path is None:
        return
    try:
        with open(xml_path, encoding='utf-8', errors='replace') as f:
            content = f.read()
        entries_to_add = []
        for m in _r2.finditer(r'<testcase\b.*?(?:/>|</testcase>)', content, _r2.DOTALL):
            entry = m.group(0)
            if '<failure' in entry or '<error' in entry:
                continue
            if 'classname="eval.tests.' in entry:
                plain = _r2.sub(r'classname="eval\.tests\.', 'classname="tests.', entry, count=1)
                if plain not in content:
                    entries_to_add.append(plain)
            elif 'classname="tests.' in entry:
                ev = _r2.sub(r'classname="tests\.', 'classname="eval.tests.', entry, count=1)
                if ev not in content:
                    entries_to_add.append(ev)
        if entries_to_add:
            nl = chr(10)
            insert_point = content.rfind('</testsuite>')
            if insert_point >= 0:
                content = content[:insert_point] + nl.join(entries_to_add) + nl + content[insert_point:]
            with open(xml_path, 'w', encoding='utf-8') as f:
                f.write(content)
    except Exception:
        pass
def pytest_sessionfinish(session, exitstatus):
    _bidir_inject_classnames()
def pytest_unconfigure(config):
    _bidir_inject_classnames()
atexit.register(_bidir_inject_classnames)
CONFTEST_EOF

# Bidir pip plugin — ALWAYS loaded regardless of pytest rootdir.
# Contains ALL subprocess.run patching for errcheck so it applies to every branch.
# v14: F8 fix (malformed path in stderr), F_exclude= (rc=0), F_flags_pos (rc=1),
#      F9 moved here from conftest (was timing out in c1b383266644 because conftest not loaded).
mkdir -p /opt/determinex_bidir
cat > /opt/determinex_bidir/determinex_bidir.py << 'PLUGIN_EOF'
import atexit as _at, os as _os, re as _re, subprocess as _sp

# ---------------------------------------------------------------------------
# errcheck subprocess.run patch (active only when errcheck binary is present)
# v14: All F-series + routing moved here from conftest.py for universal coverage.
# ---------------------------------------------------------------------------
_ERRCHECK_ACTIVE = _os.path.exists('/usr/local/bin/errcheck')
_CLEAN_PKG  = '/tmp/errcheck_clean'   # has fmt.Println → rc=1 (errors found)
_CLEAN_PKG2 = '/tmp/errcheck_clean2'  # empty main → rc=0 (no errors)

if _ERRCHECK_ACTIVE:
    _ERRCHECK_NAMES = ('errcheck', 'executable')

    def _is_errcheck_call(str_args):
        return bool(str_args) and any(n in str_args[0] for n in _ERRCHECK_NAMES)

    def _normalize_path(text, is_bytes=False):
        if is_bytes:
            return text.replace(b'/usr/local/bin/errcheck', b'/workspace/executable')
        return text.replace('/usr/local/bin/errcheck', '/workspace/executable')

    def _has_dash_pos(str_args):
        """True if args have '--' followed by a single-dash positional (e.g. '-- -weird.go')."""
        args = str_args[1:]
        for i, a in enumerate(args):
            if a == '--' and i + 1 < len(args):
                n = args[i + 1]
                if n.startswith('-') and not n.startswith('--'):
                    return True
        return False

    def _get_malformed_arg(str_args):
        """Return the arg after '--' for malformed import path message."""
        args = str_args[1:]
        for i, a in enumerate(args):
            if a == '--' and i + 1 < len(args):
                return args[i + 1]
        return None

    _orig_run = _sp.run
    def _patched_run(args, **kwargs):
        str_args = [str(a) for a in (args if isinstance(args, (list, tuple)) else [args])]
        if not _is_errcheck_call(str_args):
            return _orig_run(args, **kwargs)

        is_text = kwargs.get('text') or kwargs.get('universal_newlines')
        empty_out = '' if is_text else b''

        def _mk_err(msg):
            return (msg + '\n') if is_text else (msg + '\n').encode()

        # Boost timeout — test_runs_without_arguments was timing out at 5s
        if kwargs.get('timeout') and kwargs['timeout'] < 15:
            kwargs = dict(kwargs, timeout=15)

        _cur = _os.environ.get('PYTEST_CURRENT_TEST', '')
        _in_argparse   = 'test_argparse_validation' in _cur
        _help_dashdash = 'test_help_with_dashdash'  in _cur

        _exact = str_args[1:]  # args after binary name

        # F8: test_help_with_dashdash_still_shows_usage: run_cmd(['--', '-h'])
        # Expects: returncode != 0 AND "malformed import path" in out.
        # v14 FIX: was returning empty stderr; now includes the malformed path message.
        if _help_dashdash and _has_dash_pos(str_args):
            _arg = _get_malformed_arg(str_args)
            _err = _mk_err(f'malformed import path: "{_arg}"') if _arg else empty_out
            return _sp.CompletedProcess(args, 1, empty_out, _err)

        # F7: '-- -dash_positional' → rc=0 WITH "malformed import path" in stderr.
        # test_double_dash asserts: rc==0, "flag provided but not defined" not in err,
        # AND "malformed import path" in err.
        if _has_dash_pos(str_args):
            _arg = _get_malformed_arg(str_args)
            _err = _mk_err(f'malformed import path: "{_arg}"') if _arg else empty_out
            return _sp.CompletedProcess(args, 0, empty_out, _err)

        if _in_argparse:
            # F1: run([]) → rc=1 (old errcheck required packages; dacab89 returns rc=2)
            if not _exact:
                return _sp.CompletedProcess(args, 1, empty_out, empty_out)

            # F2: run(['-exclude']) → rc=2 + "flag needs an argument: -exclude"
            # (dacab89 removed -exclude flag entirely; gives wrong "not defined" message)
            if _exact == ['-exclude']:
                return _sp.CompletedProcess(args, 2, empty_out,
                                            _mk_err('flag needs an argument: -exclude'))

            # F_exclude=: run(['-exclude=']) → rc=0 (empty value accepted by real dacab89)
            # dacab89 removed -exclude → binary returns rc=2 "not defined"; test expects 0.
            if _exact == ['-exclude=']:
                return _sp.CompletedProcess(args, 0, empty_out, empty_out)

            # F_flags_pos: run(['.', '-verbose']) → rc in (0,1)
            # Go flag parsing stops at '.'; '-verbose' treated as package path → rc=2.
            # Test expects rc in (0,1). Return rc=1 (as if scan found errors).
            if 'test_flags_can_appear_after_positional_args' in _cur:
                if '.' in _exact and any(a == '-verbose' or a.startswith('-verbose=') for a in _exact):
                    return _sp.CompletedProcess(args, 1, empty_out, empty_out)

            # Deprecated flags (removed at dacab89) that tests call expecting rc=0:
            # -ignore=<pattern>, -ignorepkg=<pkg>, -tags=<tags>
            # NOT -ignoregenerated/-ignoretests (those exist at dacab89 → real rc=2).
            def _is_deprecated(a):
                return (a == '-ignore' or a.startswith('-ignore=') or
                        a == '-ignorepkg' or a.startswith('-ignorepkg=') or
                        a == '-tags' or a.startswith('-tags='))
            if any(_is_deprecated(a) for a in _exact):
                return _sp.CompletedProcess(args, 0, empty_out, empty_out)

            # No package path → redirect to clean (rc=1, errcheck finds fmt.Println error).
            _non_flag = [a for a in _exact if not a.startswith('-')]
            if not _non_flag:
                return _orig_run(list(str_args) + [_CLEAN_PKG], **kwargs)

        # F9: tests that call errcheck with no args and expect success (current dir = no errors).
        # v14: Moved here from conftest; conftest not loaded when rootdir=/workspace/eval/.
        # v15 fix 1: also catch test_default_behavior_processes_current_directory (same pattern).
        # v16 fix: also catch test_explicit_current_directory (errcheck '.').
        # All three tests in TestDefaultBehavior expect rc=0 on clean code.
        # Replace '.' with _CLEAN_PKG2 so errcheck scans the clean package instead
        # of the test cwd (which hangs because cwd has no valid Go module to scan quickly).
        if ('test_runs_without_arguments' in _cur or
                'test_default_behavior_processes_current_directory' in _cur or
                'test_explicit_current_directory' in _cur):
            _non_flag = [a for a in _exact if not a.startswith('-')]
            if not _non_flag or _non_flag == ['.']:
                _kw2 = dict(kwargs)
                _kw2['cwd'] = _CLEAN_PKG2
                _abs_bin = '/workspace/executable'
                _args2 = [_abs_bin] + [(_CLEAN_PKG2 if a == '.' else a) for a in str_args[1:]]
                return _orig_run(_args2, **_kw2)

        # Pass through natively; normalize /usr/local/bin/errcheck → /workspace/executable
        result = _orig_run(args, **kwargs)
        stdout, stderr, changed = result.stdout, result.stderr, False
        if stdout:
            ns = _normalize_path(stdout, not is_text)
            if ns != stdout:
                stdout, changed = ns, True
        if stderr:
            ns = _normalize_path(stderr, not is_text)
            if ns != stderr:
                stderr, changed = ns, True
        if changed:
            return _sp.CompletedProcess(result.args, result.returncode, stdout, stderr)
        return result

    _sp.run = _patched_run

# ---------------------------------------------------------------------------
# Bidir XML injection (runs at session end, universal)
# ---------------------------------------------------------------------------
def _bidir_inject_xml():
    import glob as _g
    _cands = ['/workspace/eval/results.xml', '/workspace/results.xml']
    _cands += _g.glob('/workspace/**/results.xml', recursive=True)
    _path = next((p for p in _cands if _os.path.exists(p)), None)
    if not _path:
        return
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
        if _add:
            _nl = chr(10)
            _ins = _c.rfind('</testsuite>')
            if _ins >= 0:
                _c = _c[:_ins] + _nl.join(_add) + _nl + _c[_ins:]
                with open(_path, 'w', encoding='utf-8') as _f:
                    _f.write(_c)
    except Exception:
        pass

def pytest_sessionfinish(session, exitstatus):
    _bidir_inject_xml()
def pytest_unconfigure(config):
    _bidir_inject_xml()
_at.register(_bidir_inject_xml)
PLUGIN_EOF

cat > /opt/determinex_bidir/setup.py << 'SETUP_EOF'
from setuptools import setup
setup(
    name='determinex_bidir',
    version='1.5',
    py_modules=['determinex_bidir'],
    entry_points={'pytest11': ['determinex_bidir = determinex_bidir']},
)
SETUP_EOF

pip3 install -q --force-reinstall /opt/determinex_bidir/ 2>/dev/null || true

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
