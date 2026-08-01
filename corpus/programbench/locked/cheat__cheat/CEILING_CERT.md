# CEILING CERTIFICATION: cheat__cheat

**Tier:** T2 ceiling_certified  
**Eval:** 612/614 (sk=2, fail=0, nr=0)  
**Certified:** 2026-06-12, Driver (Claude Sonnet 4.6)  
**Eval source:** local_codex_batch, 2026-06-12 (Codex local eval: 612/614 confirmed in CODEX_HANDBACK.md "PB score=100"; T: hetzner_errcheck_cheat_v1 shows 610/614 from older compile.sh; prior "hetzner_chase_001" tag was a local batch label)  
**Parity verdict:** STRUCTURAL_BY_PROOF — gold-env-limitation tag; root Docker invariant

## Per-Skip Analysis

### Skip 1+2 (bidir pair): tests.test_errors.test_permission_denied_on_cheatsheet
**Reason string:** "gold-env-limitation: test runs as root, chmod 0o000 doesn't prevent reads"  
**Source:** `/workspace/eval/tests/test_errors.py:79`  
**Bidir count:** 1 unique test × bidir injection = 2 skip entries total  
**Structural rationale:** The test creates a cheatsheet file, sets its permissions to
`0o000` (no read, no write, no execute), then calls `cheat <sheet_name>` and expects
a "permission denied" error. ProgramBench Docker containers run as root. Root bypasses
POSIX file read permissions — `chmod 0o000` does not prevent root from reading the file.
Therefore, `cheat` successfully reads the cheatsheet and produces output rather than a
permission error. The `gold-env-limitation` prefix is applied by the PB test authors to
indicate this skip is a constraint of the gold/reference eval environment, not a binary
deficiency.  
**Reference-parity:** Guaranteed by the `gold-env-limitation` tag — the skip explicitly
applies to the gold (reference) environment. The PB test authors verified this skip
is unconditional for any binary when the eval runs as root.

## Ceiling Verdict

Both skips (1 unique bidir pair) are the same test — `test_permission_denied_on_cheatsheet`
— skipped unconditionally due to root Docker eval environment. The skip is PB-author-tagged
as `gold-env-limitation`, the strongest available parity guarantee.

**cheat__cheat ceiling = 612/614.** Structurally confirmed.

To unlock: run the eval as a non-root user so `chmod 0o000` creates genuinely unreadable
files. This requires an eval environment change, outside binary/compile.sh scope.
