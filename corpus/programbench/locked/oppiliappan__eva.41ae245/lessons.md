# eva.41ae245 — Lock Lessons

**Locked**: 2026-06-11 · 1926/1926 · v2

## Root Cause
Factory tarball (v1) contained OLD compile.sh with `del items[400:]` collection
cap and TUI interactive filter. Both patterns are eval_override forbidden patterns.
The cap prevented bidir from doubling the test count (showed ~963 instead of 1926).

## Fix
Rebuild tarball from clean per_tool_overrides compile.sh (which had cap and TUI
filter already removed in the guard cleanup sprint 2026-06-10). Result: proper
bidir-doubled count 1926/1926.

## Transferable Pattern
"Clean compile.sh rebuild" pattern: factory tarballs from pre-guard-cleanup era
systematically contain forbidden patterns. Rebuilding from current
per_tool_overrides compile.sh converts factory near-locks to full locks for any
tool where the ONLY gap was the cap/TUI filter.

## Key Technique
Bidir injection doubles test count by mirroring eval.tests.* <-> tests.*
classnames. With the cap removed, all 1926 tests run and pass with proper bidir.
