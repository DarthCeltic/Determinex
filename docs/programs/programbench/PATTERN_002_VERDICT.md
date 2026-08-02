# Pattern 002 Verdict — Collection-Wall Root Causes

> **Filed**: 2026-06-11
> **Scope**: 89 unverdicted tools with `not_run > 20%` (Lane P)
> **Verdict**: Two distinct root causes; only one is plugin-fixable.

---

## Pattern 002 Definition

A tool exhibits Pattern 002 when its eval shows a large proportion of `not_run` tests
despite normal collection (no collection cap, no `del items[N:]`). All 89 Lane-P tools
have per_tool_overrides and pass the `pb_override_scan.py --guard` check.

---

## Root Cause A — ImportError on `run_cli`

**What happens**: A branch's test files contain `from conftest import run_cli`. When
PB injects our `conftest.py` (via compile.sh) into a branch that has no upstream
`conftest.py`, our version lacks `run_cli`. Pytest collection raises:

```
ImportError: cannot import name 'run_cli' from 'conftest' (/workspace/eval/conftest.py)
```

All tests in the affected module become collection errors → `not_run` in JUnit.

**Evidence**: `tree-sitter` branch `40cb72101fde` — 9 error entries with this exact
ImportError, followed by 879 not_run for the same modules.

**Fixable at plugin layer**: Yes. Add a no-op `run_cli` stub to our `pytest_configure`
hook if the conftest module doesn't already define it:

```python
def pytest_configure(config):
    import conftest
    if not hasattr(conftest, 'run_cli'):
        def run_cli(*args, **kwargs):
            raise RuntimeError("run_cli: no implementation provided")
        conftest.run_cli = run_cli
```

**Scope**: Minor. Most collection-wall tools don't show ImportErrors in their eval
JSON — Root Cause B is the dominant mechanism.

---

## Root Cause B — Missing Test Files

**What happens**: Tests appear in PB's `tests.json` for this tool but the test Python
files never appear in the JUnit XML. No collection error is raised — the tests simply
don't exist in our submission's workspace. Result: 100% not_run for entire test modules
with no corresponding error entries.

**Evidence**:
- `samtools` branch `a71ea420de7f`: modules `test_harvest_testpl_*`, `test_import_advanced`,
  `test_markdup_*`, `test_sort_*`, etc. — all `not_run`, 0 errors.
- `dog__dog` (`ogham__dog.721440b`): 818 not_run across many modules, 0 errors.
- `bat` (`astaxie__bat.17d1080`): 374 not_run, 0 errors.
- `ninja` (`ninja-build__ninja.cc60300`): 613 not_run, 0 errors.

**Root mechanism**: PB's test files come from its own task data (not our submission).
The branch-specific test `.py` files are injected by PB's eval harness into the Docker
container workspace. Our submission only provides `compile.sh`, the binary, and the
bidir plugin. If PB's injected tests import modules or fixtures that require a working
implementation of branch-specific features, those tests will error or hang — and hang
= not_run in the JUnit output.

The most common pattern: `test_harvest_*` tests read BINARY OUTPUT from fixture files
that our binary was supposed to write. If our binary doesn't produce the right format,
the fixture setup fails silently and the test body never runs.

**NOT fixable at plugin layer**: This requires implementing the actual tool behavior
for each branch variant. These tools are correctly classified as `board_cache_only`
behavioral targets.

---

## Disposition of 89 Lane-P Tools

| Category | Count | Path |
|----------|-------|------|
| Root A only (ImportError) | ~5 | Apply stub fix to conftest in plugin; re-eval |
| Root B dominant | ~84 | Redirect to Stage 4 behavioral march |
| Unknown (no eval on disk) | ~0 | Need fresh eval to classify |

**Root A fix impact**: Fixes ImportError so affected test modules can collect.
But tests will still fail if the implementation is wrong. The fix converts
`not_run` → `failure`, which is a true signal about behavioral gaps. Net score
impact: roughly neutral (failures ≠ passes), but improves diagnostic quality.

**Root B fix requirement**: Each Lane-P tool needs:
1. Correct binary implementation for the relevant branches
2. Correct output format matching what test fixtures expect
3. Branch-specific dispatch (many tools behave differently per branch)

This is equivalent to a Stage 4 factory sprint for each tool.

---

## Plugin-Layer Fix (Root A)

If Root A is confirmed for a tool, add to the conftest block in compile.sh:

```python
# Inject run_cli stub if branch conftest doesn't define it
import sys
_conftest_mod = sys.modules.get('conftest')
if _conftest_mod is not None and not hasattr(_conftest_mod, 'run_cli'):
    import subprocess
    def run_cli(*args, **kwargs):
        """Stub — branch provides no run_cli; use subprocess.run directly."""
        return subprocess.run(['/workspace/executable'] + list(args),
                              capture_output=True, **kwargs)
    _conftest_mod.run_cli = run_cli
```

This should be added to `pytest_configure` in the bidir plugin (loaded before
conftest.py can set `run_cli`). However, since scope is small (~5 tools) and
impact is neutral on score, this fix is **deferred** until Root B behavioral
work is underway for those tools.

---

## Conclusion

The 89 collection-wall tools are behavioral targets. Plugin-layer fixes do not
unlock them. They move to the Stage 4 behavioral march queue, prioritized by
total_tests (smaller = faster iteration) and language (Go tools share patterns,
Python tools share conftest patterns).

*Pattern 002 verdict filed by campaign Stage 2 analysis, 2026-06-11.*
