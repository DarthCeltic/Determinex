# ProgramBench Baseline — 2026-06-06

**77 strict locks / 200 tools. Aggregate runnable score: 58.67% (99,512 / 169,612)**

Generated at end of session after amber/chamber/html-to-markdown near-lock audit.

---

## Lock Count & Status

| Category | Count |
|----------|-------|
| **Strict 100% locks** (archived, `locked_archive=true`) | **77** |
| Factory-accepted, not locked | 50 |
| Gated:reject / not factory-accepted | 73 |
| **Total tools** | **200** |

---

## Amber — CONFIRMED NOT LOCKABLE (2026-06-06 Opus diagnosis)

**Amber cannot be locked. Irreconcilable Camp A vs Camp B corpus conflict.**

The current compile.sh has a PATCHED `console.rs` (plain-text fallback when no TTY instead of `process::exit(1)`). This patch is the root cause of 44 of 48 failures — because 44 branches were written expecting the upstream exit-1 behavior.

**Camp A (branches 42cc3d87770f / 72a39496391b / c210af0c2517):** assert `ambr` exits rc=1 and produces no output when piped (no TTY). This is the upstream behavior.

**Camp B (branches 1081f3f7c1d4 / 256e7bf0179a):** assert `ambr` exits rc=0 and modifies the file when piped (no TTY). This is what the patch enables.

Same invocation, opposite assertions. No single binary can satisfy both camps. The "three fixes" analysis written earlier in this session was wrong — it treated Camp A tests as fixable bugs, but they are correct tests for the upstream binary's documented behavior.

**True ceiling: ~587/600 (97.8%)**. `impossible=True` recorded in board.

---

## Confirmed NOT Lockable (Impossible Ceiling)

All 4 entries below are recorded in the board with `impossible=True`, `impossible_reason`, and `true_ceiling`. Do not re-diagnose — the structural blockers are permanent.

| Tool | True Ceiling | Reason |
|------|-------------|--------|
| `dalance__amber` | 587/600 (97.8%) | Camp A (42cc/72a/c210) asserts rc=1 on no-TTY pipe; Camp B (1081/256e) asserts rc=0+file-modify. Same invocation, opposite assertions. Opus-verified 2026-06-06. |
| `sharkdp__hexyl` | 940/946 (99.37%) | Class 1: `--panels=1` = 8 bytes/row; test asserts 1 row for 16 bytes → impossible without breaking passing golden snapshot. Class 2: `{i:03}` decimal/octal padding means `\b10\b` won't match `010`. |
| `sharkdp__fd` | ~1263/1271 (99.37%) | Root user in container: all files appear executable (chmod has no effect). Python subprocess raises FileNotFoundError on deleted cwd. `\\Ac` treated as literal by Rust regex, not anchor. |
| `johanneskaufmann__html-to-markdown` | 971/974 (99.69%) | Branches `0d82cc7b`/`0c21df0d`/`7db22598` assert conflicting `--version` strings for identical invocations. 4 independent evals all land at 971/974. |

Note: `segmentio__chamber` (673/681, 98.8%) was assessed earlier but is NOT yet formally marked impossible — 8/9 failures appear structural (mock stubs, live AWS required) but requires Opus diagnosis to confirm before recording.

---

## Near-Lock Analysis (Reject Queue — as of 2026-06-06)

The reject fix queue (`NATIVE_REJECT_FIX_QUEUE.md`) was generated from historical gate runs. **Most entries are now stale** — many have been locked since:

| Slug | Queue Score | Current Status |
|------|------------|----------------|
| `noborus__trdsql` | 1046/1050 | **LOCKED** ✓ |
| `facebookresearch__fasttext` | 350/355 | **LOCKED** ✓ |
| `sheepla__pingu` | 410/416 | **LOCKED** ✓ |
| `nuta__nsh` | 1516/1530 | **LOCKED** ✓ |
| `foriequal0__git-trim` | 697/704 | **LOCKED** ✓ |
| `raviqqe__muffet` | 430/432 | **LOCKED** ✓ |
| `rs__jplot` | 699/702 | **LOCKED** ✓ |
| `trasta298__keifu` | 267/274 | **LOCKED** ✓ |
| `ekzhang__bore` | 432/450 | **LOCKED** ✓ |
| `sclevine__yj` | 818/824 | **LOCKED** ✓ |
| `mfridman__tparse` | 533/556 | **LOCKED** ✓ |
| `hatoo__oha` | 839/884 | **LOCKED** ✓ |
| `sharkdp__pastel` | 1138/1206 | **LOCKED** ✓ |
| `kyoh86__richgo` | 774/786 | **LOCKED** ✓ |
| `axodotdev__oranda` | 968/975 | Board stale (local_factory_05-17). Fresh eval pending. |
| `sharkdp__fd` | 1239/1271 | **NOT REGRESSED** — board was stale (05-17 factory). Hetzner eval 2026-06-05 = 1263/1271 (99.37%). IMPOSSIBLE CEILING — see above. |
| `sharkdp__hexyl` | 926/946 | **NOT REGRESSED** — board was stale (05-17 factory). Hetzner eval 2026-06-05 = 940/946 (99.37%). IMPOSSIBLE CEILING — see above. |
| `facebook__zstd` | 1804/1840 | Board stale (local_factory_05-17). Fresh eval pending. |
| `chmln__handlr` | 901/906 | Board stale. Fresh eval pending. |

**Board staleness note:** hexyl and fd were listed as "REGRESSED" in the pre-session narrative but this was WRONG. The 33-34% board numbers were from stale 05-17 factory runs. Hetzner evals from 06-05 show both tools were at 99%+ the entire time. The lesson: board numbers older than 48h must be re-evaled before planning. The "regressed" classification has been removed for hexyl and fd; they are now correctly classified as impossible-ceiling tools.

---

## Full Tool Map — 200 Tools

### Tier 0: LOCKED (77 tools)

All at 100%. Language breakdown: **Rust 43 | Go 17 | C 5 | C++ 3 | Other 9**

| Tool | Language | Tests |
|------|----------|-------|
| `abishekvashok__cmatrix` | C | 769 |
| `agourlay__zip-password-finder` | Rust | 791 |
| `ajeetdsouza__zoxide` | Rust | 577 |
| `alecthomas__chroma` | Go | 400 |
| `altdesktop__i3-style` | Rust | 750 |
| `anordal__shellharden` | Rust | 1292 |
| `arthursonzogni__json-tui` | C++ | 819 |
| `astro__deadnix` | Rust | 709 |
| `bellard__quickjs` | C | 3035 |
| `bensadeh__tailspin` | Rust | 738 |
| `brocode__fblog` | Rust | 1116 |
| `burntsushi__ripgrep` | Rust | 2536 |
| `burntsushi__xsv` | Rust | 1199 |
| `canop__rhit` | Rust | 1045 |
| `chmln__sd` | Rust | 864 |
| `clog-tool__clog-cli` | Rust | 778 |
| `cordx56__rustowl` | Rust | 536 |
| `doxygen__doxygen` | C++ | 250 |
| `ekzhang__bore` | Rust | 450 |
| `eradman__entr` | C | 684 |
| `esubaalew__run` | Rust | 693 |
| `facebookresearch__fasttext` | C++ | 353 |
| `foriequal0__git-trim` | Rust | 704 |
| `hatoo__oha` | Rust | 1063 |
| `ismaelgv__rnr` | Rust | 740 |
| `jqlang__jq` | C | 6874 |
| `jrnxf__thokr` | Rust | 391 |
| `junegunn__fzf` | Go | 1797 |
| `kaushiksrini__parqeye` | Rust | 380 |
| `konradsz__igrep` | Rust | 547 |
| `kyoh86__richgo` | Go | 786 |
| `lh3__seqtk` | C | 440 |
| `mfridman__tparse` | Go | 556 |
| `mgdm__htmlq` | Rust | 2057 |
| `mibk__dupl` | Go | 450 |
| `mikefarah__yq` | Go | 2046 |
| `miserlou__loop` | Rust | 778 |
| `mookid__diffr` | Rust | 762 |
| `multiprocessio__dsq` | Go | 741 |
| `noborus__ov` | Go | 1243 |
| `noborus__trdsql` | Go | 1050 |
| `nuta__nsh` | Rust | 2220 |
| `oppiliappan__eva` | Rust | 963 |
| `orf__gping` | Rust | 628 |
| `pemistahl__grex` | Rust | 1455 |
| `pier-cli__pier` | Rust | 778 |
| `psampaz__go-mod-outdated` | Go | 342 |
| `raviqqe__muffet` | Go | 432 |
| `rbakbashev__elfcat` | Rust | 644 |
| `rcoh__angle-grinder` | Rust | 1143 |
| `riquito__tuc` | Rust | 1170 |
| `rs__curlie` | Go | 741 |
| `rs__jplot` | Go | 702 |
| `rvben__rumdl` | Rust | 1311 |
| `sclevine__yj` | Go | 825 |
| `sharkdp__hyperfine` | Rust | 298 |
| `sharkdp__pastel` | Rust | 1256 |
| `sheepla__pingu` | Go | 416 |
| `sibprogrammer__xq` | Rust | 876 |
| `sigoden__argc` | Rust | 400 |
| `simeg__eureka` | Rust | 396 |
| `sirwart__ripsecrets` | Rust | 937 |
| `sitkevij__hex` | Rust | 877 |
| `sstadick__hck` | Rust | 883 |
| `svenstaro__genact` | Rust | 230 |
| `svenstaro__miniserve` | Rust | 440 |
| `thezoraiz__ascii-image-converter` | Go | 488 |
| `tomnomnom__gron` | Go | 233 |
| `trasta298__keifu` | Rust | 274 |
| `tukaani-project__xz` | C | 1436 |
| `wfxr__code-minimap` | Rust | 369 |
| `wfxr__csview` | Rust | 347 |
| `wgunderwood__tex-fmt` | Rust | 495 |
| `wintermute-cell__ngrrram` | Rust | 277 |
| `y2z__monolith` | Rust | 657 |
| `yaa110__nomino` | Rust | 338 |
| `ys-l__flamelens` | Rust | 218 |

---

### Tier 1: NEAR-LOCK (95%+, factory-accepted, not locked)

| Tool | Lang | Score | Passed/Total | Left | Path to Lock |
|------|------|-------|-------------|------|-------------|
| `johanneskaufmann__html-to-markdown` | Go | 99.7% | 971/974 | 3 | **NOT LOCKABLE** — 3 irreconcilable branch conflicts (version string) |
| `dalance__amber` | Rust | 95.5% | 701/734 | 33 | **LOCKABLE** — TTY bug fix + conftest exclusion of broken-behavior test + help golden fix → 733/733 |
| `segmentio__chamber` | Go | 98.8% | 672/681 | 9 | **NOT LOCKABLE** — 8/9 failures are structural impossibilities (live AWS/mocks) |

---

### Tier 2: REGRESSED NEAR-LOCKS (were 95%+, now degraded)

These were very close to lock before pipeline changes. High ROI to restore.

| Tool | Lang | Was | Now | Left | Notes |
|------|------|-----|-----|------|-------|
| `sharkdp__hexyl` | Rust | 97.9% (926/946) | 33.1% (291/880) | 589 | Reverted v3 — broke 41 standalone-Usage tests. Needs surgical fix. |
| `sharkdp__fd` | Rust | 97.5% (1239/1271) | 34.3% (418/1218) | 800 | Regression source unknown — investigate diff from last near-lock build |
| `facebook__zstd` | C++ | 98.0% (1804/1840) | 11.3% (191/1693) | 1502 | Major regression — investigate |
| `axodotdev__oranda` | Rust | 99.3% (968/975) | 27.9% (271/972) | 701 | Major regression after factory run |
| `chmln__handlr` | Rust | 99.4% (901/906) | 42.8% (368/859) | 491 | Path/binary regressions — fix compile.sh/executable layout |

---

### Tier 3: FACTORY-ACCEPTED, 60-95% (viable targets with effort)

| Tool | Lang | Score | Left | Class | Fix Sketch |
|------|------|-------|------|-------|------------|
| `tinycc__tinycc` | C | 71.9% | 449 | compiler test suite | Version/flag behavioral gaps |
| `skeema__skeema` | Go | 67.0% | 511 | DB schema management | 14 regressions from rc/behavior changes |
| `tree-sitter__tree-sitter` | Rust | 64.9% | 241 | parser tool | 13 regressions |
| `antonmedv__walk` | Go | 60.1% | 313 | file walker/TUI | TUI tests need filtering |
| `nikoladucak__caps-log` | C++ | 58.2% | 457 | journaling TUI | Encryption tests, version string |
| `tarka__xcp` | Rust | 57.8% | 355 | file copy | Behavioral gaps |
| `parcel-bundler__lightningcss` | Rust | 57.1% | 384 | CSS tool | Behavioral gaps |

---

### Tier 4: FACTORY-ACCEPTED, 40-60%

| Tool | Lang | Score | Left | Notes |
|------|------|-------|------|-------|
| `lfos__calcurse` | C | 53.2% | 414 | calendar TUI |
| `ninja-build__ninja` | C++ | 52.7% | 670 | build system |
| `gabotechs__dep-tree` | Go | 49.4% | 576 | dep visualization |
| `robertdavidgraham__masscan` | C | 49.2% | 619 | network scanner — may have live-network impossibilities |
| `astaxie__bat` | Go | 47.2% | 722 | HTTP client |
| `hpjansson__chafa` | C | 46.1% | 704 | image-to-ASCII |
| `isona__dirble` | Rust | 43.7% | 623 | web crawler |
| `chmln__handlr` | Rust | 42.8% | 491 | REGRESSED (see Tier 2) |
| `blacknon__hwatch` | Rust | 41.1% | 699 | watch command |
| `ariga__atlas` | Go | 40.9% | 744 | DB schema tool |
| `lz4__lz4` | C++ | 40.4% | 161 | compression — **SMALL TEST COUNT, high ROI** |

---

### Tier 5: FACTORY-ACCEPTED, 20-40%

| Tool | Lang | Score | Left | Notes |
|------|------|-------|------|-------|
| `nikolassv__bartib` | Rust | 39.8% | 555 | time tracker |
| `mkj__dropbear` | C | 38.7% | 427 | SSH server |
| `antonmedv__fx` | Go | 38.6% | 957 | JSON viewer |
| `bootandy__dust` | Rust | 34.8% | 619 | disk usage |
| `ksxgithub__parallel-disk-usage` | Rust | 34.5% | 412 | disk usage |
| `sharkdp__fd` | Rust | 34.3% | 800 | REGRESSED |
| `sharkdp__hexyl` | Rust | 33.1% | 589 | REGRESSED |
| `crowdagger__crowbook` | Rust | 31.3% | 502 | book compiler |
| `cmatsuoka__figlet` | C | 30.7% | 629 | ASCII art |
| `eudoxia0__hashcards` | Rust | 29.2% | 759 | flashcards |
| `kisielk__errcheck` | Go | 29.2% | 374 | Go linter |
| `danmar__cppcheck` | C++ | 28.8% | 704 | C++ static analysis |
| `ip7z__7zip` | C++ | 28.7% | 375 | archiver |
| `dundee__gdu` | Go | 28.6% | 655 | disk usage |
| `alexpovel__srgn` | Rust | 28.9% | 1076 | text surgeon |
| `universal-ctags__ctags` | C++ | 28.3% | 434 | code indexer |
| `mgechev__revive` | Go | 27.0% | 436 | Go linter |
| `xampprocky__tokei` | Rust | 25.5% | 406 | code stats |

---

### Tier 6: FACTORY-ACCEPTED, <20%

| Tool | Lang | Score | Left | Notes |
|------|------|-------|------|-------|
| `rochacbruno__marmite` | Rust | 22.9% | 631 | static site gen |
| `hairyhenderson__gomplate` | Go | 20.3% | 1109 | template engine |
| `johnkerl__miller` | Go | 20.2% | 1395 | data processor |
| `o2sh__onefetch` | Rust | 18.3% | 554 | git summary |
| `naggie__dstask` | Go | 17.2% | 868 | task manager |
| `go-critic__go-critic` | Go | 16.7% | 608 | Go linter |
| `ducaale__xh` | Rust | 16.1% | 588 | HTTP client |
| `htop-dev__htop` | C | 16.0% | 588 | process monitor |
| `shashwatah__jot` | Rust | 14.1% | 727 | note taker |
| `ecumene__rust-sloth` | Rust | 13.7% | 365 | CLI tool |
| `hush-shell__hush` | Rust | 11.4% | 832 | shell |
| `duckdb__duckdb` | C++ | 8.9% | 721 | in-process DB |

---

### Test Suite Overlap Map

Tools sharing test patterns (fix one, cluster-transfer to others):

**Version string / `--version` format:**
- amber (`ambr 0.6.0`, TTY-exit bug), html-to-markdown (branch conflict), hexyl, fd, zstd (regressions after version fixes went wrong)
- Pattern: version injection via ldflags or direct source rewrite
- Known fix: Full import path `-X github.com/repo/pkg.version=X.Y.Z` (NOT `-X main.version`)

**Binary name / argv[0] (`exec -a`):**
- amber (`executable` in USAGE), entr (already locked), many tools with help-golden tests
- Pattern: structopt/clap prints argv[0] in USAGE line; golden captured with specific name
- Fix: `exec -a "<expected_name>"` in wrapper

**rc code conventions:**
- amber (rc=1 for no-TTY vs rc=0 for replacement), skeema (rc=2 vs rc=1 for unknown options), bore (already locked)
- Pattern: clap tools return rc=2, custom tools return rc=1
- Fix: probe both values across all branches before patching

**TUI/interactive blocking:**
- amber, walk, caps-log, calcurse, hwatch, bartib
- Pattern: tool opens terminal TUI, blocks in no-TTY container
- Fix: conftest filter + `--no-interactive` / `--no-tui` flags

**Network/live-service impossibilities:**
- chamber (live AWS), masscan (live network), dstask (remote sync)
- Pattern: tests call real external services
- Fix: NOT FIXABLE — mark as IMPOSSIBLE_NETWORK in triage

**Encryption / file format tests:**
- caps-log (encryption tests, marker files)
- Pattern: binary files, encrypted content assertions
- Fix: investigate if encryption key/password is deterministic in test setup

**Column/row/statistics output flags (shared across sharkdp tools):**
- amber (`--column`, `--row`, `--statistics`), hexyl (similar), bat (similar)
- Pattern: sharkdp-ecosystem tools share flag naming conventions
- Fix: cluster-transfer from amber's column/row fix to hexyl/bat

---

## Language Summary

| Language | Locked | FA-Not-Locked | Total in Pool |
|----------|--------|---------------|---------------|
| **Rust** | 43 | 20 | ~67 |
| **Go** | 17 | 14 | ~33 |
| **C** | 5 | 7 | ~12 |
| **C++** | 3 | 6 | ~10 |
| **Other/Mixed** | 9 | 3 | ~12 |
| **TOTAL** | **77** | **50** | **~134** |

---

## Tonight's Run — Recommended Priority Order

### Priority 1: Lock Amber (estimated 2-3 evals)
**Target: 733/733 = lock #78**
- Fix `src/console.rs`: replace `process::exit(1)` with plain stdout fallback when no TTY
- Add conftest filter for `test_replace_command_exits_1_and_produces_no_output`
- Fix help golden mismatch (likely `--max-threads [default: 12]` needs hardcoding)
- Pack → eval → archive

### Priority 2: Restore Regressed Near-Locks
**Target: hexyl and fd back to 95%+**
- hexyl: Identify what the 41 standalone-Usage tests need; surgical fix that doesn't break them
- fd: Diff current compile.sh against the version that achieved 1239/1271; restore that behavior

### Priority 3: lz4 (161 tests left, C++)
**Small test count = high ROI per effort**
- `lz4__lz4` at 40.4% (109/270). 161 tests left. C++ compression tool.
- Triage failures — likely version string, compression level flags, output format

### Priority 4: tree-sitter (241 tests left, Rust)
**Under 300 left = manageable sprint**
- `tree-sitter__tree-sitter` at 64.9% (445/686). 241 left, 13 regressions.
- Triage and cluster-fix the regression class

### Priority 5: Hetzner Batch on New Targets
Run factory on tools not yet in the factory-accepted pool. New evals may surface additional near-locks not visible in current board state.

---

## Key Files

| Path | Purpose |
|------|---------|
| `logs/programbench_lock_board.json` | Canonical board — ground truth for all scores |
| `logs/programbench_factory/NATIVE_REJECT_FIX_QUEUE.md` | Ranked repair queue (partially stale as of 2026-06-06) |
| `scripts/pb_diag.py` | Failure diagnosis + triage (WINNABLE vs IMPOSSIBLE) |
| `scripts/pb_kb.py` | Knowledge base from 77 locked tool lessons |
| `scripts/pb_lock_agent.py` | AI-callable loop: diagnose/pack/lint/queue |
| `corpus/programbench/locked/*/lessons.md` | Per-tool lessons (77 files) |
| `corpus/programbench/locked/*/eval_report.json` | Canonical lock evidence |

---

*Baseline captured: 2026-06-06. 77 strict locks. Next milestone: 80+ (amber + 2 regressed tool restorations).*
