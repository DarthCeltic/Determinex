# hex.61ae69b — Lock Lessons

**Locked**: 2026-06-11 · 1754/1754 · v2

## Root Cause
Factory tarball (v1) contained OLD compile.sh with `del items[400:]` collection
cap and TUI interactive filter — same factory-era issue as eva.41ae245.
The cap suppressed 877 tests (showed ~877 instead of 1754).

## Fix
Rebuild tarball from clean per_tool_overrides compile.sh. Result: 1754/1754.

## Transferable Pattern
Same as eva.41ae245: factory tarballs pre-guard-cleanup systematically contain
forbidden patterns. Rebuild from current per_tool_overrides.

## Key Technique
hex is a Rust hex viewer. Bidir injection handles eval.tests.* <-> tests.*
classname mirroring. No special patching needed beyond clean bidir + cap removal.
