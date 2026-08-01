# ditaa.f2286c4 — Lock Lessons

**Locked**: 2026-06-11 · 681/681 · v8

## Root Cause
Python SyntaxError in compile.sh conftest section: a leading comma on line 95
of the `collect_ignore_glob` list (`    ,"test_pexpect*.py"`) caused a
SyntaxError at import time. The conftest module never loaded, so `_sp.run =
_patched_run` never executed. Pytest then invoked `java -cp
/workspace/executable` (a shell wrapper, not a JAR) as a classpath → Java saw
a shell script as classpath → `ClassNotFoundException` on all 7 tests in one
branch.

## Fix
Remove the leading comma. After fix v2: 681/681.

## Transferable Pattern
Any SyntaxError in the conftest.py cascade silently kills ALL patching (no
error visible until test failures appear). Always `python3 -c "import ast;
ast.parse(open('compile.sh').read())"` is insufficient for heredoc scripts —
instead extract the conftest block and `python3 -c "compile(block, '<cs>', 'exec')"`.

## Key Technique
Lein uberjar from source enables `--svg` flag (ditaa0_10.jar lacks it — 136
tests fail without it). Exact-match `-cp` redirect avoids clobbering `_cov`
paths. `-ef` guards prevent `cp: same file` when cwd == /workspace/.
