# CEILING CERTIFICATION: blake3-team__blake3

**Tier:** T2 ceiling_certified  
**Eval:** 1368/1374 (sk=6, fail=0, nr=0)  
**Certified:** 2026-06-12, Driver (Claude Sonnet 4.6)  
**Eval source:** local_b1v2, 2026-06-12 (scratch/pb_b1_blake3_candidate_v2/; SHA256=C4CB1FDD4312E706347A4A17B39009CB69D452C28356B653A278C349F9D88386; prior "hetzner_chase_001" tag was a local batch label, not Hetzner server)  
**Parity verdict:** STRUCTURAL_BY_PROOF — Windows-platform and root-permission skips;
environment invariants independent of binary implementation

## Per-Skip Analysis

### Skips 1+2 (bidir pair): tests.test_harvest.test_slash_normalization_on_windows
**Reason string:** "Windows-specific test"  
**Source:** `/workspace/eval/tests/test_harvest.py:343`  
**Bidir count:** 1 unique test × bidir = 2 skip entries  
**Structural rationale:** This test verifies that `b3sum` correctly normalizes Windows-style
path separators (`\`) to Unix-style (`/`) in output. It is decorated with
`@pytest.mark.skip` using an unconditional "Windows-specific test" reason string. The PB
eval harness runs on Linux (Hetzner x86_64). Path separator normalization is a Windows
filesystem concern; the Linux binary has no backslash paths to normalize. The skip is
unconditional — it applies regardless of binary behavior on Linux.  
**Reference-parity:** Structural by proof — any Linux b3sum binary (including the PB
reference binary) runs on Linux where this test is irrelevant. The skip predicate is the
platform itself, not the binary output.

### Skips 3+4 (bidir pair): tests.test_harvest.test_invalid_unicode_on_windows
**Reason string:** "Windows-specific test"  
**Source:** `/workspace/eval/tests/test_harvest.py:418`  
**Bidir count:** 1 unique test × bidir = 2 skip entries  
**Structural rationale:** Same mechanism as Skip 1+2. This test verifies handling of
invalid Unicode codepoints in Windows-specific filename encodings (e.g., WTF-8 paths that
can exist on Windows but not on Linux filesystems). The Linux kernel rejects file creation
with invalid UTF-8 sequences, so the Windows invalid-Unicode scenario cannot be reproduced
on Linux. The skip is unconditional.  
**Reference-parity:** Structural by proof — platform constraint applies equally to the
reference binary.

### Skips 5+6 (bidir pair): tests.test_io.test_permission_denied_error
**Reason string:** "Cannot test permission denied as root"  
**Source:** `/workspace/eval/tests/test_io.py:234`  
**Bidir count:** 1 unique test × bidir = 2 skip entries  
**Structural rationale:** This test sets file permissions to `0o000` and expects `b3sum`
to produce a "permission denied" error. ProgramBench Docker containers run as root; root
bypasses POSIX read permissions. The unconditional skip reflects that this test cannot
be validated in any root eval environment regardless of the binary implementation.  
**Reference-parity:** Structural by proof — root Docker invariant (same as csview,
cheat__cheat, ripgrep). The reference binary would also trigger this skip.

## Ceiling Verdict

All 6 skips (3 unique bidir pairs) are environment constraint skips:
- Skips 1+2: Windows platform test — irrelevant on Linux (eval environment)
- Skips 3+4: Windows invalid-Unicode test — irrelevant on Linux (eval environment)
- Skips 5+6: Root Docker permission bypass (OS invariant)

**blake3-team__blake3 ceiling = 1368/1374.** Structurally confirmed.

To unlock Windows-specific tests: no path — these require a Windows eval environment.
To unlock root permission test: run eval as non-root (eval environment change).
