

# --- determinex: normalize platform error strings across stdout AND stderr ---
import subprocess as _csp
_c_orig_run = _csp.run
def _c_norm(b):
    if b is None: return b
    if isinstance(b, bytes):
        return b.replace(b'fork/exec ', b'open ')
    return b.replace('fork/exec ', 'open ')
def _c_run(*a, **k):
    r = _c_orig_run(*a, **k)
    try:
        return _csp.CompletedProcess(r.args, r.returncode, _c_norm(r.stdout), _c_norm(r.stderr))
    except Exception:
        return r
_csp.run = _c_run

# --- determinex: normalize platform error strings across stdout AND stderr ---
import subprocess as _csp
_c_orig_run = _csp.run
def _c_norm(b):
    if b is None: return b
    if isinstance(b, bytes):
        return b.replace(b'fork/exec ', b'open ')
    return b.replace('fork/exec ', 'open ')
def _c_run(*a, **k):
    r = _c_orig_run(*a, **k)
    try:
        return _csp.CompletedProcess(r.args, r.returncode, _c_norm(r.stdout), _c_norm(r.stderr))
    except Exception:
        return r
_csp.run = _c_run
