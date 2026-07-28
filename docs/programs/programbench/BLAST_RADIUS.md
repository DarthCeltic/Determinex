# ProgramBench Blast Radius Map

**Generated:** 2026-06-12  
**Source:** Raw eval_report.json from A4-CHASE shard + Hetzner factory evals  
**Purpose:** Cluster failures by signature to rank fixes by tools-unlocked-per-fix  

> A fix that clears f=2 on three tools beats a fix that clears f=8 on one.
> T2-track tools (sk>0) should never appear in strict projections.

---

## Strict-Eligibility Filter (hard gate)

**Strict-eligible = nr==0, sk==0, f>0, sub_bucket NOT tui_wall/behavioral_deep.**

| Tool | f | nr | sk | sub_bucket | Eligible? |
|------|---|----|----|-----------|-----------|
| `isona__dirble` | 4 | 0 | 0 | near_miss | **YES — strict** (rerun EADDRINUSE first) |
| `kisielk__errcheck` | 12 | 0 | 0 | near_miss | **YES — strict** |
| `mgechev__revive` | 40 | 0 | 0 | near_miss | YES — strict (larger effort) |
| `direnv__direnv` | 4 | 0 | 2 | near_miss | NO — T2-track (sk=2 Ruby) |
| `incu6us__goimports-reviser` | 4 | 0 | 2 | near_miss | NO — T2-track (sk=2) |
| `hatoo__oha` | 16 | 0 | 4 | near_miss | NO — T2-track (sk=4) |
| `madler__pigz` | 28 | 0 | 2 | near_miss | NO — T2-track (sk=2) |
| `nuta__nsh` | 4 | 0 | 0 | **tui_wall** | NO — TUI behavioral, not code-patchable |
| `cmatsuoka__figlet` | 4 | 0 | 0 | behavioral_deep | NO — quarantined (chase regression) |
| `crowdagger__crowbook` | 14 | 0 | 0 | behavioral_deep | NO — quarantined (chase regression) |

---

## Failure Signature Clusters

Ranked by **tools unlocked per fix**, descending.

---

### CLUSTER A — EADDRINUSE / Socket Collision (environmental flake)

**Signature:** `OSError: [Errno 98] Address already in use`  
**Root cause:** Port binding race in multi-worker Docker eval. Test opens a socket and the
previous test's socket hasn't fully released. Not a binary bug.  
**Fix recipe:** Rerun the eval. If the failure clears, it was a flake. If persistent,
add a port retry with `SO_REUSEADDR` or test isolation (separate loopback port per test).

| Tool | Failures matching | Unlocked if cleared |
|------|------------------|---------------------|
| `isona__dirble` | f=2 (bidir) `test_timeout_terminates_slow_requests` | STRICT T1 (if 2nd failure also clears) |

**Priority:** RERUN FIRST before any patch — zero code change, free T1 candidate.  
**Playbook:** RECIPE 009 (seed integrity) — record result either way.

---

### CLUSTER B — URL Validation / Timeout vs Error Message

**Signature:** `assert 'Invalid URL: not-a-url' in 'TIMEOUT'`  
**Root cause:** Test expects the binary to quickly reject an invalid URL with an error
message, but the binary times out instead of short-circuiting on URL parse failure.  
**Fix recipe:** Add early URL validation before making any HTTP connections. If URL fails
`urllib.parse` or regex check, print error and exit with rc=1 immediately.

| Tool | Failures matching | Unlocked if cleared |
|------|------------------|---------------------|
| `isona__dirble` | f=2 (bidir) `test_uri_file_with_mixed_valid_invalid_urls` | STRICT T1 (with Cluster A) |

**Priority:** Single fix unlocks dirble to T1 IF Cluster A also clears.  
**Recipe:** New — add URL pre-validation before network dispatch.

---

### CLUSTER C — rc=1 on Valid Flag Invocations (errcheck argparse) ⚠ IMPOSSIBLE CEILING

**Signature:** `assert 1 == 0` on flag-parsing tests (`-ignore`, `-tags`, `-ignorepkg`)  
**Root cause:** errcheck returns rc=1 for flag combinations that should succeed. Six unique
test patterns (12 bidir). Of these, 5 unique (10 bidir) are structurally unfixable:
branch 11c421a3b5f4 re-extracts `main_test.go` with unchecked `r.Close()/w.Close()` calls
that return rc=1; the test expects rc=0 — a cross-branch fixture contradiction. No binary
change resolves a contradiction between two branches of the same fixture.

Best reachable ceiling: ~1054/1064 (f=10 remaining, sk=0). **NOT a T1 lock — errcheck
has been reclassified to impossible_ceiling.**

| Tool | Failures matching | Unlocked if cleared |
|------|------------------|---------------------|
| `kisielk__errcheck` | f=12 (6 unique × bidir) | ⛔ impossible_ceiling (f≥10 always) |

**Priority:** Demoted. errcheck cannot reach T1. Not worth patching.  
**Reclassification date:** 2026-06-12 (confirmed from ceiling_note in eval_index).

---

### CLUSTER D — Help/Usage Format Normalization Drift

**Signature:** `assert 'direnv v<VER...ven message\n' == 'direnv v<VER...ven message\n'`  
**Root cause:** `direnv help` vs `direnv --help` produce subtly different output (extra
line, different ordering, or trailing content). Test normalizes version string but another
whitespace/format difference remains.  
**Fix recipe:** Normalize help output — ensure `help` subcommand and `--help` flag produce
byte-identical output after version string substitution.

| Tool | Failures matching | Unlocked if cleared |
|------|------------------|---------------------|
| `direnv__direnv` | f=2 (bidir) `test_help_subcommand_equals_dashdashhelp_normalized` | T2-track only (sk=2 Ruby stays) |

**Priority:** T2-track — clearing this reduces direnv to f=2 (PATH) for a T2 analysis. Does
NOT unlock strict T1 alone.  
**Recipe:** RECIPE 005 (clap/help class) — help text normalization.

---

### CLUSTER E — Empty PATH / Exec Detection

**Signature:** `assert ("can't find bash" in "direnv: error command 'echo' not found on PATH ''")`  
**Root cause:** Test sets PATH='' and expects direnv to report it can't find bash when
executing a `.envrc` that calls echo. Our binary reports the echo failure instead of
the bash absence. The test checks for bash-specific language.  
**Fix recipe:** When executing `.envrc` with empty PATH, detect that the shell interpreter
(bash) is missing before attempting to exec commands, and emit the "can't find bash"
diagnostic.

| Tool | Failures matching | Unlocked if cleared |
|------|------------------|---------------------|
| `direnv__direnv` | f=2 (bidir) `test_exec_with_empty_path_environment` | T2-track only |

**Priority:** T2-track. With Cluster D, clearing both gives direnv f=0, sk=2 → CEILING_CERT → T2.  
**Combined impact:** D + E together = direnv T2 cert. Two fixes, one T2.

---

### CLUSTER F — Structural Environment Skips (T2-track only, no fix possible)

**Signature:** `pytest.mark.skip` with environment reasons

| Test | Tool | Reason | Parity |
|------|------|--------|--------|
| `test_ruby_layout_scenario` | direnv | "Ruby not available" | Structural — no ruby in Docker |
| `test_output_write_modifies_file`, `test_list_diff_and_set_exit_status` | goimports-reviser | (see eval) | Structural |
| `test_ext_is_terminal_behavior` | goimports-reviser | (terminal detection) | Structural — no TTY |
| `test_format_host_port_ipv6_basic`, etc. | oha (sk=4) | harvest/network | Structural — no network |
| `test_test_mode_corrupt_returns_nonzero`, `test_unix_compress_interop` | pigz (sk=2) | (compress tool) | Structural |

**Action:** Document in CEILING_CERT.md per tool when f=0 is achieved.

---

### CLUSTER G — TUI Keyboard Behavioral (not code-patchable)

**Signature:** tmux Ctrl+E / Escape key handling differences  

| Tool | f | Details |
|------|---|---------|
| `nuta__nsh` | 4 | Ctrl+E (cursor to end-of-line), Escape from history mode — tmux timing/behavior differences |

**Action:** Not a code fix. Would require modifying test fixtures or implementing nsh's
line editor to exactly match the test's expected tmux key sequences. Sub_bucket: tui_wall.
No near-lock path without test fixture modification (which is prohibited).

---

### CLUSTER H — Version/Info Format Regression (behavioral_deep, quarantined)

**Signature:** figlet `-I5` returns `flc` vs expected `flf2`; usage string truncated

| Tool | Details | Status |
|------|---------|--------|
| `cmatsuoka__figlet` | 10 unique regressions in A4-CHASE: font format code, usage string, copyright whitespace | behavioral_deep — quarantined (chase SHA 64252cee) |
| `crowdagger__crowbook` | 14 unique regressions: CLI conflict, LaTeX, argparse, help text | behavioral_deep — quarantined (chase SHA 0e3b1cce) |

**Action:** No further one-shot patches until prior-best compile.sh is recovered and root
cause of regression is understood. Prior bests: figlet 2084/2088 (f=4), crowbook 1760/1774
(f=14). Investigation needed: what changed between prior-best and chase submissions.  
**Corpus signal:** These regressions are logged in RECIPE 009.

---

## Summary: Tools-Unlocked-per-Fix Ranking

| Rank | Fix | Tools unlocked | Type |
|------|-----|----------------|------|
| 1 | Dirble port-9988 fixture + URI pre-validation (Clusters A+B) | dirble × 1 T1 | f4 eval running |
| 2 | direnv Cluster D + E combined | direnv × 1 T2 | 2 fixes, 1 T2 |
| 3 | goimports-reviser fix | goimports-reviser × 1 T2 (sk=2 ceiling) | 1 fix, 1 T2 |
| 4 | bartib dedicated re-eval (tmux filter removal) | bartib × 1 T2 (if f=0 confirmed) | Hetzner eval |
| 5 | age CEILING_CERT | age × 1 T2 ✓ DONE | — |
| 6 | argc CEILING_CERT | argc × 1 T2 ✓ DONE | — |
| ⛔ | errcheck Cluster C | ~~errcheck × 1 T1~~ IMPOSSIBLE | ceiling ~1054/1064 (f≥10 always) |

**Strict T1 path:** dirble f4 → if EADDRINUSE + URI-TIMEOUT both clear → T1=54. That is the
honest near-term strict ceiling — the strict-eligible pool after this session is **dirble only**.

**T2 path:** T2=15 already. direnv D+E → T2=16. bartib rerun → T2=17.

**errcheck removed from T1 projection.** 5 unique (10 bidir) failures are cross-branch
fixture contradictions — impossible ceiling regardless of implementation.

---

*BLAST_RADIUS.md — Phase 1 output, 2026-06-12. Next refresh: after A4/A4b harvest.*
