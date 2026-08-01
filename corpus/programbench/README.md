---
name: programbench-master-catalog
description: One-stop reference for all 200 ProgramBench tools — scores, tiers, paths, descriptions, cluster siblings, ceilings.
generated: auto — run `python3 scripts/gen_pb_readme.py` to refresh
last_updated: 2026-06-29T14:48:31Z
---

# ProgramBench Master Catalog

> **Generated:** 2026-06-29  
> **Source of truth:** `corpus/programbench/eval_index.json`  
> **Do not edit by hand** — run `python3 scripts/gen_pb_readme.py` to regenerate.

## Quick Stats

| Metric | Value |
|--------|-------|
| **T1 strict locks** | **66 / 200** (33.0%) |
| **T2 ceiling certified** | **16** |
| T3 open (needs work) | 118 |
| Total tests covered (T1 only) | 95,451 |
| Total tests in catalog | 491,684 |
| Aliases / duplicates (not counted) | 31 |

## Key Files & Paths

| What | Where |
|------|-------|
| Eval index (machine source of truth) | `corpus/programbench/eval_index.json` |
| Tier table (auto-generated) | `corpus/programbench/GROUND_TRUTH.md` |
| Priority action queue | `docs/programs/programbench/PB_PRIORITY_QUEUE.md` |
| Per-tool locked archives | `corpus/programbench/locked/<tool>/` |
| Per-tool compile.sh overrides | `corpus/programbench/per_tool_overrides/<author__repo.hash>/` |
| Training corpus (verdict jsonl) | `corpus/programbench/training_corpus/pb_verdict_corpus.jsonl` |
| Fix queue | `logs/programbench_factory/NATIVE_REJECT_FIX_QUEUE.md` |
| Eval command | `cd T:/Dev/ProgramBench && PYTHONUTF8=1 uv run programbench eval <pilot_dir> --force` |

## Lock Definition (mandatory)

- **T1 strict_lock**: `passed == total`, `not_run == 0`, `skipped == 0`, `failed == 0` in raw eval_report.json
- **T2 ceiling_certified**: `fail=0`, `nr=0`, `sk>0`, `CEILING_CERT.md` present with per-skip structural rationale
- **Never sum T1+T2 in headlines.** T2 is NOT a lock. Report as separate numbers.
- Guard: `python3 scripts/pb_override_scan.py --guard` must pass 0 violations before archiving any lock.

## Cluster / Transfer Map

Completing a tool often transfers directly to its siblings. Key clusters:

| Cluster | Tools | Transfer mechanism |
|---------|-------|-------------------|
| JSON ecosystem | jq · yq · xq · gron · dsq · trdsql · fx · fselect | Filter/transform DSL, streaming JSON parse |
| Rust sharkdp | ripgrep · fd · bat · hexyl | Shared CLI conventions, clap arg parsing |
| Disk usage | dust · duc · dua-cli · gdu · dutree | TUI tree rendering, du syscall patterns |
| Terminal image | ascii-image-converter · jp2a · chafa · pixterm | ANSI escape rendering, image decode |
| Compressors | lz4 · zstd · brotli · pigz · xz | Streaming block API, frame format |
| Log analysis | angle-grinder · fblog · rhit · lnav | Log parsing, field extraction, aggregation |
| Go linters | errcheck · go-critic · revive · wrapcheck | AST walk, pass/fail exit code, report format |
| TUI explorers | fzf · broot · walk · xplr · felix · nnn | Tmux protocol, TUI key events, render loop |
| Git TUI | lazygit · tig · stgit | Git plumbing API, TUI screen layout |

## What's Needed to Reach the Vision

> Set Determinex any code/idea → it is taken in, gated, fixed, and proven. This ledger is
> generated from `build_knowledge.json:roadmap_to_envisioned` (RAG-retrievable — the system's
> own answer to *what next + how*). Edit it there, not here.

### Self-healing (automatable DETECT→FIX)

- **bidir_strip** — DETECT determinex_pb_lock_registry.py check-integrity (sha drift) -> FIX determinex_pb_bidir_restore.py restore on the tarball -> RE-VERIFY registry verify. Source compile.sh already carry bidir so repacks won't re-strip. AUTOMATABLE end-to-end.
- **build_broken_rc127** — DETECT rc=127 / <5% pass -> determinex_pb_autofix triage classifies (toolchain/cgo/build-target/source-gap) -> applies the class fix -> re-eval. AUTOMATABLE.
- **disk_full** — disk_guard daemon prunes unused docker images >82%. mem rotation via memguard. AUTOMATED on the eval box.
- **tool_invocation_hang** — DETECT eval slow/no-results + tool blocked on stdin/tmux (host py-spy via /proc cgroup) -> FIX inject determinex_subprocess_guard (stdin DEVNULL + killpg + escaper-kill + watchdog) -> re-eval completes+scores. HARD_CAP + orphan_reaper are always-on nets. See class_patterns.tool_invocation_hang. AUTOMATABLE: determinex_pb_inject_guard --all.

### Remaining PB work

- **tui_unlock_deploy** — 172 tools have genuine tmux/pty/tui not_run AFTER bidir; 0 tarballs install tmux. NEED: compile.sh apt-get install tmux + PTY (pb_tui_unlock_batch/determinex_pb_pty) + un-filter, then re-eval. The last-mile for the bidir-recovered ~95-99% tail (e.g. jplot residual 14).
- **reverify_after_bidir** — bidir restore changed lock tarball shas -> re-verify through the registry (re-pin) so check-integrity is green.
- **metric_wiring** — pb_parallel.score is raw; the GATE/ingest must use determinex_pb_official_score (without_ignored) + the registry's raw-clean gate. Authoritative scorer = programbench info.
- **family_expansion** — PB is the proving ground; the envisioned product locks ANY language/domain. Per-family oracle wiring (Kotlin/Swift/C#) is the breadth roadmap (see project_family_march_progress).
- **guard_bulk_inject** — Inject determinex_subprocess_guard into ALL per_tool_overrides + locked tarballs (determinex_pb_inject_guard --all, then repack/redeploy) so EVERY tool's eval is hang-robust (stdin-block / TUI / orphan-pipe) and 'any code that hangs' still gets SCORED. Injected so far: lz4 (proven). This is the last general-robustness gap for PB.

### System-wide (the whole product)

- **editor_last_mile** — VS Code ext packages to .vsix + wired to the backend JSON CLI; remaining = the standalone Tauri shell's Rust #[tauri::command] + React pages + packaging/distribution. Needs the Tauri/Node dev+build env.
- **oracle_breadth** — Universal oracle wired for Go/Rust/TS/Python; per-language wiring beyond (Kotlin/Swift/C#) needs their toolchains. The 'any code' breadth.
- **greenfield_depth** — Vague example-free ideas use model-proposed consensus examples (flagged oracle_proposed, confirm); richer model-assisted test inference is next. The 'any idea' depth.
- **amplify_field_prove** — DETERMINEX_AMPLIFY engine-proven in-repo; field-prove on a full PB tool through the Docker harness.
- **hardened_runner_signoff** — 6 UNKNOWN_REQUIRES_REVIEW runner sites execute trusted-by-design code; security-governance owner sign-off to clean-classify (bundle with the Ethics Oracle at go-live).

*How to ask the system: determinex_pb_lock_registry.py reconcile (VERIFIED/NEEDS_REVERIFY/NEGATIVE buckets) + this roadmap = the system's answer to 'what else + how'. build_knowledge.class_patterns = how-to-fix per class.*

## T1 Strict Locks (passed == total, 0 fail, 0 nr, 0 sk)

| Slug | Description | Lang | Tests | Tarball | Eval Report | Override | Lessons | Cluster siblings |
|------|-------------|------|-------|---------|-------------|----------|---------|------------------|
| `angle-grinder` | Log parsing & aggregation DSL; filter/group-by/sum on log lines | rs | 1143/1143 (100.0%) | Y | `corpus/programbench/locked/angle-grinder/eval_report.json` | — | — | `rhit`, `fblog` |
| `ariga__atlas` | Database schema management and migration tool (Ent/SQL) | go | 3476/3476 (100.0%) | Y | `corpus/programbench/locked/ariga__atlas.6d81150/eval_report.json` | `ariga__atlas` | — | — |
| `ascii-image-converter` | Converts images to ASCII art in terminal | go | 488/488 (100.0%) | Y | `corpus/programbench/locked/ascii-image-converter/eval_report.json` | — | — | — |
| `bore` | TCP tunnel — exposes local ports through a remote server | rs | 900/900 (100.0%) | Y | `corpus/programbench/locked/bore/eval_report.json` | — | — | `miniserve`, `muffet` |
| `boyter__scc.515f91c` | Code counter — lines of code/comments/blanks per language (scc) | go | 476/476 (100.0%) | Y | `corpus/programbench/locked/boyter__scc.515f91c/eval_report.json` | `boyter__scc.515f91c` | — | — |
| `chmln__handlr` | XDG MIME handler replacement for xdg-open | rs | 1812/1812 (100.0%) | Y | `corpus/programbench/locked/chmln__handlr.90e78ba/eval_report.json` | `chmln__handlr` | — | — |
| `clog-cli` | Changelog generator from conventional commit history | rs | 1556/1556 (100.0%) | Y | `corpus/programbench/locked/clog-cli/eval_report.json` | — | — | `git-trim` |
| `cmatrix` | Matrix-style falling-character terminal animation | c | 769/769 (100.0%) | Y | `corpus/programbench/locked/cmatrix/eval_report.json` | — | — | `genact` |
| `cmatsuoka__figlet` | Large ASCII art text banners from fonts | c | 2088/2088 (100.0%) | Y | `corpus/programbench/locked/cmatsuoka__figlet.202a0a8/eval_report.json` | `cmatsuoka__figlet.202a0a8` | — | — |
| `code-minimap` | Terminal minimap of source code scrollbar | rs | 738/738 (100.0%) | Y | `corpus/programbench/locked/code-minimap/eval_report.json` | — | — | — |
| `crowdagger__crowbook` | Markdown-to-book converter (EPUB/HTML/PDF) | rs | 1774/1774 (100.0%) | Y | `corpus/programbench/locked/crowdagger__crowbook.ea214d7/eval_report.json` | `crowdagger__crowbook.ea214d7` | — | — |
| `curlie` | HTTP client combining curl flags with httpie-style output | go | 1482/1482 (100.0%) | Y | `corpus/programbench/locked/curlie/eval_report.json` | — | — | `muffet` |
| `deadnix` | Nix file analyzer; finds unused variables in Nix expressions | rs | 1418/1418 (100.0%) | Y | `corpus/programbench/locked/deadnix/eval_report.json` | — | Y | — |
| `diffr` | Diff viewer with character-level highlighting | rs | 1524/1524 (100.0%) | Y | `corpus/programbench/locked/diffr/eval_report.json` | — | — | — |
| `direnv__direnv` | Shell extension to load/unload env vars per directory | go | 1946/1946 (100.0%) | Y | `corpus/programbench/locked/direnv__direnv.02040c7/eval_report.json` | `direnv__direnv.02040c7` | — | — |
| `dsq` | SQL queries over CSV/JSON/Parquet; multi-format join | go | 1532/1532 (100.0%) | — | `corpus/programbench/locked/multiprocessio__dsq.c3ae0ba/eval_report.json` | — | — | `jq`, `trdsql` |
| `dupl` | Source code duplicate detector across files | go | 900/900 (100.0%) | Y | `corpus/programbench/locked/dupl/eval_report.json` | — | — | — |
| `eliukblau__pixterm` | Renders images as colored ASCII art in terminal | go | 922/922 (100.0%) | Y | `C:/tmp/a3_harvest/eliukblau__pixterm.1a93fd5.eval.json` | `eliukblau__pixterm.1a93fd5` | — | `ascii-image-converter`, `hpjansson__chafa.dd4d4c1` |
| `entr` | File watcher — re-runs commands when files change | c | 1482/1482 (100.0%) | — | `corpus/programbench/locked/eradman__entr.8e2e8b4/eval_report.json` | — | — | — |
| `errcheck` | — | ? | 1064/1064 (100.0%) | — | `corpus/programbench/locked/kisielk__errcheck.dacab89/kisielk__errcheck.dacab89.eval.json` | — | — | — |
| `eureka` | TUI note-taking app for capturing ideas quickly | rs | 800/800 (100.0%) | — | `corpus/programbench/locked/simeg__eureka.df3796c/eval_report.json` | — | — | — |
| `eva` | Calculator REPL with variable support and arbitrary precision | rs | 963/963 (100.0%) | Y | `corpus/programbench/locked/eva/eval_report.json` | — | — | — |
| `fasttext` | Facebook's text classification and word vector library | c++ | 708/708 (100.0%) | — | `corpus/programbench/locked/facebookresearch__fasttext.1142dc4/eval_report.json` | — | — | — |
| `fblog` | JSON log viewer with color highlighting and field filtering | rs | 2254/2254 (100.0%) | Y | `corpus/programbench/locked/fblog/eval_report.json` | — | — | `angle-grinder`, `rhit` |
| `flamelens` | Interactive flamegraph viewer in terminal | rs | 622/622 (100.0%) | Y | `corpus/programbench/locked/flamelens/eval_report.json` | — | — | — |
| `genact` | Fake activity simulator — makes terminal look busy | rs | 237/237 (100.0%) | Y | `corpus/programbench/locked/genact/eval_report.json` | — | — | `cmatrix` |
| `git-trim` | Trims merged/stale git branches automatically | rs | 1422/1422 (100.0%) | Y | `corpus/programbench/locked/git-trim/eval_report.json` | — | — | `clog-cli` |
| `go-mod-outdated` | Lists outdated Go module dependencies | go | 342/342 (100.0%) | Y | `corpus/programbench/locked/go-mod-outdated/eval_report.json` | — | — | — |
| `google__brotli` | Brotli compression algorithm CLI encoder/decoder | c | 1212/1212 (100.0%) | Y | `corpus/programbench/locked/google__brotli.b3dc9cc/eval_report.json` | `google__brotli.b3dc9cc` | — | `madler__pigz` |
| `grex` | Generates minimal regex patterns from user-provided examples | rs | 3036/3036 (100.0%) | Y | `corpus/programbench/locked/grex/eval_report.json` | — | — | — |
| `gron` | Flattens JSON to greppable discrete assignments | go | 233/233 (100.0%) | Y | `corpus/programbench/locked/gron/eval_report.json` | — | — | `jq` |
| `guumaster__hostctl` | Hosts file manager — enable/disable groups of host entries | go | 2750/2750 (100.0%) | Y | `corpus/programbench/locked/guumaster__hostctl.d6d9699/eval_report.json` | `guumaster__hostctl.d6d9699` | — | — |
| `hck` | Field-splitting like cut but with regex delimiters | rs | 1768/1768 (100.0%) | Y | `corpus/programbench/locked/sstadick__hck.b66c751/eval_report.json` | — | — | — |
| `hex` | Hex dump viewer with color and multiple display modes | rs | 1754/1754 (100.0%) | Y | `corpus/programbench/locked/hex/eval_report.json` | — | — | — |
| `hooklift__gowsdl` | WSDL-to-Go code generator for SOAP web services | go | 846/846 (100.0%) | Y | `T:/determinex-programbench/hetzner_results/a3_cap_26_harvest/determinex_pb_hooklift_gowsdl_2a06cec/hooklift__gowsdl.2a06cec/hooklift__gowsdl.2a06cec.eval.json` | `hooklift__gowsdl.2a06cec` | — | — |
| `hyperfine` | Benchmarking tool — runs commands N times, stats on timing | rs | 298/298 (100.0%) | Y | `corpus/programbench/locked/hyperfine/eval_report.json` | — | — | — |
| `i3-style` | Applies color themes to i3/Sway window manager configs | rs | 1500/1500 (100.0%) | Y | `corpus/programbench/locked/i3-style/eval_report.json` | — | — | — |
| `igrep` | Searches regex in files; opens matches in vim/nvim (TUI) | rs | 1408/1408 (100.0%) | — | `corpus/programbench/locked/konradsz__igrep.aa75630/eval_report.json` | — | — | `ripgrep` |
| `isona__dirble` | Fast web directory brute-forcer / content discovery | rs | 2216/2216 (100.0%) | Y | `corpus/programbench/locked/isona__dirble.e2dea9f/eval_report.json` | `isona__dirble.e2dea9f` | — | — |
| `ivanceras__svgbob` | ASCII diagram-to-SVG converter | rs | 948/948 (100.0%) | Y | `corpus/programbench/locked/ivanceras__svgbob.6d00ad9/eval_report.json` | `ivanceras__svgbob.6d00ad9` | — | `stathissideris__ditaa` |
| `jq` | JSON processor — filters, transforms, queries JSON streams | c | 6874/6874 (100.0%) | Y | `corpus/programbench/locked/jq/eval_report.json` | — | — | `yq`, `xq`, `dsq`, `gron` |
| `junegunn__fzf.b56d614` | General-purpose fuzzy finder for terminal (most widely used TUI) | go | 4156/4156 (100.0%) | Y | `corpus/programbench/locked/junegunn__fzf.b56d614/eval_report.json` | `junegunn__fzf.b56d614` | — | `peco`, `skim` |
| `loop` | Runs commands in a loop with delay/count/until options | rs | 1556/1556 (100.0%) | Y | `corpus/programbench/locked/loop/eval_report.json` | — | — | `entr` |
| `madler__pigz` | Parallel gzip compressor — multi-threaded gzip replacement | c | 1876/1876 (100.0%) | Y | `corpus/programbench/locked/madler__pigz.fe4894f/eval_report.json` | `madler__pigz` | — | — |
| `mgechev__revive` | Fast, extensible Go linter with configurable rules | go | 1772/1772 (100.0%) | Y | `corpus/programbench/locked/mgechev__revive.201451e/eval_report.json` | `mgechev__revive.201451e` | — | — |
| `miniserve` | Minimal HTTP file server — serve a directory over HTTP | rs | 880/880 (100.0%) | Y | `corpus/programbench/locked/miniserve/eval_report.json` | — | — | `bore`, `muffet` |
| `muffet` | Fast website link checker; crawls for broken links | go | 864/864 (100.0%) | Y | `corpus/programbench/locked/muffet/eval_report.json` | — | Y | `miniserve` |
| `ngrrram` | Typing speed trainer for command-line users | rs | 664/664 (100.0%) | — | `corpus/programbench/locked/wintermute-cell__ngrrram.8ea13c3/eval_report.json` | — | — | `thokr` |
| `nomino` | Bulk file renamer with regex patterns | rs | 676/676 (100.0%) | Y | `corpus/programbench/locked/nomino/eval_report.json` | — | — | `rnr` |
| `pastel` | Color manipulation CLI — convert, mix, lighten/darken colors | rs | 1256/1256 (100.0%) | Y | `corpus/programbench/locked/pastel/eval_report.json` | — | — | — |
| `pier` | Command alias manager — save and run frequently-used commands | rs | 1556/1556 (100.0%) | Y | `corpus/programbench/locked/pier/eval_report.json` | — | — | — |
| `rhit` | Apache/Nginx log analyzer with fast path stats | rs | 2176/2176 (100.0%) | — | `corpus/programbench/locked/canop__rhit.ae90bcb/eval_report.json` | — | — | `angle-grinder`, `fblog` |
| `ripsecrets` | Scans files/git history for hardcoded secrets and API keys | rs | 937/937 (100.0%) | Y | `corpus/programbench/locked/ripsecrets/eval_report.json` | — | Y | — |
| `rnr` | Recursive bulk file/directory renamer with regex support | rs | 1480/1480 (100.0%) | Y | `corpus/programbench/locked/rnr/eval_report.json` | — | — | `nomino` |
| `seqtk` | Fast FASTQ/FASTA sequence processing toolkit | c | 880/880 (100.0%) | Y | `corpus/programbench/locked/seqtk/eval_report.json` | — | — | — |
| `shellharden` | Shell script linter/formatter; hardens quoting and variable handling | rs | 1292/1292 (100.0%) | Y | `corpus/programbench/locked/shellharden/eval_report.json` | — | — | `ripgrep` |
| `stathissideris__ditaa` | Converts ASCII art diagrams to PNG/SVG images | java | 681/681 (100.0%) | Y | `corpus/programbench/locked/stathissideris__ditaa/eval_report.json` | `stathissideris__ditaa.f2286c4` | — | — |
| `tailspin` | Log file highlighter — colorizes log levels, IPs, paths, dates | rs | 1570/1570 (100.0%) | — | `corpus/programbench/locked/bensadeh__tailspin.6278437/eval_report.json` | — | — | `fblog` |
| `tex-fmt` | LaTeX formatter — consistent indentation for TeX/LaTeX files | rs | 990/990 (100.0%) | Y | `corpus/programbench/locked/tex-fmt/eval_report.json` | — | — | — |
| `thokr` | Terminal typing test with WPM/accuracy stats | rs | 507/507 (100.0%) | Y | `corpus/programbench/locked/thokr/eval_report.json` | — | — | `ngrrram` |
| `tparse` | Formats and colorizes go test output with pass/fail/coverage stats | go | 1112/1112 (100.0%) | Y | `corpus/programbench/locked/tparse/eval_report.json` | — | — | — |
| `trasta298__keifu.3331426` | TUI bookmark/note manager with sqlite backend | rs | 826/826 (100.0%) | Y | `corpus/programbench/locked/trasta298__keifu.3331426/eval_report.json` | `trasta298__keifu.3331426` | — | — |
| `trdsql` | SQL queries over CSV/TSV/JSON/LTSV; supports MySQL/PG syntax | go | 2806/2806 (100.0%) | Y | `corpus/programbench/locked/trdsql/eval_report.json` | — | — | `dsq` |
| `xsv` | Fast CSV toolkit — slice, select, join, search, stats on CSV | rs | 2634/2634 (100.0%) | Y | `corpus/programbench/locked/burntsushi__xsv.f430466/eval_report.json` | — | — | `dsq`, `trdsql` |
| `yq` | YAML/JSON/TOML processor; jq-syntax queries for YAML | go | 2046/2046 (100.0%) | Y | `corpus/programbench/locked/yq/eval_report.json` | — | — | `jq`, `xq` |
| `zoxide` | Smarter cd; learns frecency-ranked directory jumps | rs | 577/577 (100.0%) | Y | `corpus/programbench/locked/zoxide/eval_report.json` | — | Y | `nomino`, `rnr` |

## T2 Ceiling Certified (f=0, nr=0, sk>0, CEILING_CERT.md present)

| Slug | Description | Lang | Score | sk | CEILING_CERT | Override | Cluster |
|------|-------------|------|-------|----|--------------|----------|---------|
| `argc` | Bash argument parser generator — creates CLI from comments | rs | 2664/2820 (94.5%) | 156 | Y | — | — |
| `bellard__quickjs.d7ae12a` | — | c | 6076/6088 (99.8%) | 12 | — | `bellard__quickjs.d7ae12a` | — |
| `blake3-team__blake3` | BLAKE3 cryptographic hash function CLI (b3sum) | rs | 1368/1374 (99.6%) | 6 | Y | `blake3-team__blake3.15e83a5` | — |
| `chmln__sd.87d1ba5` | — | ? | 1728/1738 (99.4%) | 10 | Y | `chmln__sd.87d1ba5` | — |
| `chroma` | Syntax highlighter library + CLI for 200+ languages | go | 1048/1062 (98.7%) | 14 | Y | — | — |
| `elfcat` | ELF binary viewer — parse and display ELF headers/sections | rs | 1290/1292 (99.8%) | 2 | — | — | — |
| `eudoxia0__hashcards` | CLI flashcard system using hash-based spaced repetition | rs | 2572/2586 (99.5%) | 6 | Y | `eudoxia0__hashcards.48aa136` | — |
| `filosottile__age` | Simple, modern file encryption (age format) | go | 1590/1678 (94.8%) | 88 | Y | `filosottile__age.706dfc1` | — |
| `htmlq` | CSS selector queries on HTML — like jq but for HTML | rs | 2057/2058 (100.0%) | 1 | Y | — | `jq`, `xq` |
| `incu6us__goimports-reviser` | Go import sorter/grouper that enforces import sections | go | 1216/1218 (99.8%) | 2 | Y | `incu6us__goimports-reviser.81bd549` | — |
| `nikolassv__bartib` | TUI time tracker with start/stop/list commands | rs | 1856/1858 (99.9%) | 2 | Y | `nikolassv__bartib` | — |
| `oppiliappan__statix` | Nix linter with fix suggestions | rs | 1948/1956 (99.6%) | 8 | Y | `oppiliappan__statix.e9df54c` | `deadnix` |
| `pingu` | Ping replacement with pingu ASCII art animation | rs | 416/419 (99.3%) | 3 | Y | — | — |
| `ripgrep` | Regex search; respects .gitignore; fastest grep replacement | rs | 2536/2538 (99.9%) | 2 | Y | — | `shellharden` |
| `xz` | XZ/LZMA compression algorithm CLI | c | 4064/4072 (99.8%) | 8 | — | — | `facebook__zstd`, `google__brotli` |
| `zip-password-finder` | Brute-force ZIP password cracker (wordlist/charset) | rs | 1582/1584 (99.9%) | 2 | Y | — | — |

## T3 Open (135 tools — needs work)

### T3 near_miss — close to T1/T2, specific fix needed

| Slug | Description | Lang | Score | f/nr/sk | Override | Eval report | Next action | Ceiling/notes |
|------|-------------|------|-------|---------|----------|-------------|-------------|---------------|
| `rust-embedded__svd2rust.1760b5e` | Converts CMSIS-SVD files to Rust peripheral access crate | rs | 1970/1970 (100.0%) ⚠PHANTOM(unresolved) | — | `rust-embedded__svd2rust` | `corpus/programbench/locked/rust-embedded__svd2rust.1760b5e/eval_report.json` | Verify → archive → T1 |  |
| `yj` | Converts between YAML/TOML/JSON/HCL formats | go | 1457/1457 (100.0%) ⚠PHANTOM(unresolved) | — | — | `corpus/programbench/locked/yj/eval_report.json` | Verify → archive → T1 |  |
| `parqeye` | Parquet file viewer — display schema and rows from .parquet files | go | 1126/1128 (99.8%) | sk=2 | — | `corpus/programbench/locked/parqeye/eval_report.json` | Write CEILING_CERT (2 sk) → T2 | 158 TUI tests not_run in Docker (test_tui_advanced.*, test_tui_behavior.*, test_ |
| `cslarsen__jp2a.61d205f` | — | c | 1438/1442 (99.7%) | sk=4 | `cslarsen__jp2a.61d205f` | `corpus/programbench/locked/tier_2_upstream_skips/cslarsen__jp2a.61d205f/eval_report.json` | Write CEILING_CERT (4 sk) → T2 |  |
| `cheat__cheat.b8098dc` | — | go | 612/614 (99.7%) | sk=2 | `cheat__cheat.b8098dc` | `corpus/programbench/locked/tier_2_upstream_skips/cheat__cheat.b8098dc/eval_report.json` | Write CEILING_CERT (2 sk) → T2 |  |
| `tuc` | Field cutter like cut with delimiter regex and ranges | rs | 2490/2498 (99.7%) | sk=8 | — | `corpus/programbench/locked/tier_2_upstream_skips/riquito__tuc.16fb471/eval_report.json` | Write CEILING_CERT (8 sk) → T2 |  |
| `wfxr__csview.8ac4de0` | — | ? | 347/348 (99.7%) | sk=1 | `wfxr__csview.8ac4de0` | `—` | Write CEILING_CERT (1 sk) → T2 |  |
| `codesnap-rs__codesnap` | Takes code snapshots with syntax highlighting (like carbon.sh) | rs | 1698/1706 (99.5%) | sk=8 | `codesnap-rs__codesnap` | `—` | Write CEILING_CERT (8 sk) → T2 | F7 diagnostic: 1418 rendering failures (headless/env). sk=8 upstream skips. |
| `lymphatus__caesium-clt` | Lossy image compressor CLI | c++ | 1238/1240 (99.8%) | sk=2 | `lymphatus__caesium-clt.a529b2e` | `T:/determinex-programbench/hetzner_results/a3_cap_26_harvest/determinex_pb_lymphatus_caesium_clt_a529b2e/lymphatus__caesium-clt.a529b2e/lymphatus__caesium-clt.a529b2e.eval.json` | Write CEILING_CERT (2 sk) → T2 |  |
| `oha` | HTTP load tester with real-time TUI stats dashboard | rs | 2172/2189 (99.2%) | f=5 nr=4 sk=8 | — | `corpus/programbench/locked/oha/eval_report.json` | Remove cap + eval (4 nr) | sweep_v1: 2172/2189 (99.2%). 8 skips (4 unique permanent upstream). 4 not_run (T |
| `xq` | XML/HTML query tool with jq-like syntax | go | 1734/1752 (99.0%) | f=9 nr=3 sk=6 | — | `corpus/programbench/locked/tier_2_upstream_skips/sibprogrammer__xq.b89f681/eval_report.json` | Remove cap + eval (3 nr) |  |
| `axodotdev__oranda` | Static site generator for project announcements/releases | rs | 1958/1970 (99.4%) | f=10 sk=2 | `axodotdev__oranda.27d60c7` | `—` | Fix 10 fail (0.5%) → T1 | 42 failures in Docker are all GitHub API/network dependent: test_github_data, te |
| `ov` | Feature-rich pager — replacement for less/more with TUI | go | 4880/4894 (99.7%) | f=14 | — | `corpus/programbench/locked/ov/eval_report.json` | Fix 14 fail (0.3%) → near-lock |  |
| `blacknon__hwatch` | watch replacement with diff highlighting and history | rs | 2588/2614 (99.0%) | f=16 nr=10 | `blacknon__hwatch` | `—` | Remove cap + eval (10 nr) | 73 NR (TUI tests filtered, test_tui_*/test_basic_tui not runnable in headless Do |
| `rust-lang__mdbook` | Markdown documentation book renderer (used by Rust Book) | rs | 3564/3597 (99.1%) | f=21 sk=12 | `rust-lang__mdbook.37273ba` | `T:/determinex-programbench/hetzner_results/a3_cap_26_harvest/determinex_pb_rust_lang_mdbook_37273ba/rust-lang__mdbook.37273ba/rust-lang__mdbook.37273ba.eval.json` | Fix 21 fail (0.6%) → near-lock |  |
| `antonmedv__walk` | Terminal file browser — fast minimal TUI file navigator | go | 1528/1550 (98.6%) | f=22 | `antonmedv__walk` | `T:/determinex-programbench/hetzner_results/b2v2_harvest/determinex_pb_antonmedv_walk_bf802ef/antonmedv__walk.bf802ef/antonmedv__walk.bf802ef.eval.json` | Fix 22 fail (1.4%) → near-lock |  |

### T3 tui_wall — blocked on TUI/tmux test execution

| Slug | Description | Lang | Score | f/nr/sk | Override | Eval report | Next action | Ceiling/notes |
|------|-------------|------|-------|---------|----------|-------------|-------------|---------------|
| `rs__jplot.2a54bcc` | Real-time terminal plot of stdin data streams | go | 2157/2157 (100.0%) ⚠PHANTOM(submetric) | — | `rs__jplot.2a54bcc` | `corpus/programbench/locked
s__jplot.2a54bcc/eval_report.json` | Verify → archive → T1 |  |
| `nsh` | Experimental shell with Lisp-inspired syntax | rs | 4584/4588 (99.9%) | f=4 | — | `corpus/programbench/locked/nsh/eval_report.json` | Fix 4 fail (0.1%) → T1 | nsh_v3 4574/4578: Ctrl+E (cursor to end) ignored by nsh line editor; Escape from |
| `hpjansson__chafa.dd4d4c1` | Terminal graphics with tmux support (chafa) | c | 5544/5552 (99.9%) | f=8 | `hpjansson__chafa.dd4d4c1` | `—` | Fix 8 fail (0.1%) → T1 | 8 tmux tests not_run because tmux is unavailable in the Docker eval environment, |
| `elkowar__pipr` | TUI pipeline builder — compose shell pipes interactively | rs | 1636/1655 (98.9%) | f=15 sk=4 | `elkowar__pipr.fae0b17` | `—` | Fix 15 fail (0.9%) → near-lock |  |
| `kyoheiu__felix` | TUI file manager with vim-like keybindings | rs | 1886/1929 (97.8%) | f=40 nr=1 sk=2 | `kyoheiu__felix.95df390` | `T:/determinex-programbench/hetzner_results/a3_cap_26_harvest/determinex_pb_kyoheiu_felix_95df390/kyoheiu__felix.95df390/kyoheiu__felix.95df390.eval.json` | Add tmux (1 nr) |  |
| `byron__dua-cli` | Disk Usage Analyzer TUI — fast du with interactive browser | rs | 1942/2004 (96.9%) | f=54 sk=8 | `byron__dua-cli.8570c15` | `—` | Fix 54 fail (2.7%) — large effort | 27 unique failures: empty-dir size assertion (ext4 allocates 4KiB block, tests e |
| `gabotechs__dep-tree` | Dependency tree visualizer (TUI) for source files | rs | 2656/2758 (96.3%) | f=98 sk=4 | `gabotechs__dep-tree` | `—` | Fix 98 fail (3.6%) — large effort |  |

### T3 behavioral_deep — complex behavioral failures, large gap

| Slug | Description | Lang | Score | f/nr/sk | Override | Eval report | Next action | Ceiling/notes |
|------|-------------|------|-------|---------|----------|-------------|-------------|---------------|
| `ffmpeg__ffmpeg` | FFmpeg — video/audio converter, encoder, decoder, streamer | c | 228/4479 (5.1%) | f=400 nr=3851 | `ffmpeg__ffmpeg.360a402` | `—` | Remove cap + eval (3851 nr) |  |
| `jgm__pandoc` | Universal document converter (Markdown/HTML/DOCX/PDF/etc) | haskell | 2/5721 (0.0%) | f=506 nr=5213 | `jgm__pandoc.5caad90` | `—` | Remove cap + eval (5213 nr) |  |
| `osgeo__proj` | PROJ cartographic projections and coordinate transformations | c++ | 154/6027 (2.6%) | f=616 nr=5043 sk=214 | `osgeo__proj.75d455c` | `—` | Remove cap + eval (5043 nr) |  |
| `halitechallenge__halite` | Halite strategy game bot framework and CLI | c++ | 18/782 (2.3%) | f=756 sk=8 | `halitechallenge__halite.822cfb6` | `C:/tmp/a3_harvest/halitechallenge__halite.822cfb6.eval.json` | Fix 756 fail (96.7%) — large effort |  |
| `ast-grep__ast-grep` | AST-based code search and rewrite tool | rs | 812/1790 (45.4%) | f=978 | `ast-grep__ast-grep.dde0fe0` | `corpus/programbench/in_progress/codex_override_001/ast-grep/eval_report.json` | Fix 978 fail (54.6%) — large effort |  |
| `quinn-rs__quinn` | QUIC network protocol implementation CLI and library | rs | 94/1198 (7.8%) | f=1100 sk=4 | `quinn-rs__quinn.bb359cc` | `T:/determinex-programbench/hetzner_results/a3_cap_26_harvest/determinex_pb_quinn_rs_quinn_bb359cc/quinn-rs__quinn.bb359cc/quinn-rs__quinn.bb359cc.eval.json` | Fix 1100 fail (91.8%) — large effort |  |
| `nukesor__pueue` | Task queue manager for long-running shell commands | rs | 44/1266 (3.5%) | f=1163 nr=43 sk=16 | `nukesor__pueue.8b9d6fe` | `—` | Remove cap + eval (43 nr) |  |
| `ksxgithub__parallel-disk-usage` | pdu — parallel du with TUI progress and tree output | rs | 38/1260 (3.0%) | f=1220 sk=2 | `ksxgithub__parallel-disk-usage` | `—` | Fix 1220 fail (96.8%) — large effort |  |
| `cweill__gotests` | Generates Go test boilerplate from function signatures | go | 140/1512 (9.3%) | f=1368 sk=4 | `cweill__gotests.2a672c5` | `C:/tmp/a3_harvest/cweill__gotests.2a672c5.eval.json` | Fix 1368 fail (90.5%) — large effort |  |
| `nikoladucak__caps-log` | TUI journaling tool with calendar view and markdown | rs | 1038/2491 (41.7%) | f=1400 nr=3 sk=50 | `nikoladucak__caps-log.2cf2d1e` | `—` | Remove cap + eval (3 nr) | F5 diagnostic: sk=42 (bidir of 21 TUI skips) + nr=18. upstream_skips ceiling con |
| `rhysd__kiro-editor` | Terminal text editor in the vein of kilo | go | 62/1538 (4.0%) | f=1468 nr=8 | `rhysd__kiro-editor.4157485` | `—` | Remove cap + eval (8 nr) |  |
| `typst__typst` | Modern document typesetting language + compiler (LaTeX alternative) | rs | 1762/3573 (49.3%) | f=1806 nr=3 sk=2 | `typst__typst.88356d0` | `—` | Remove cap + eval (3 nr) |  |
| `chirlu__sox` | Sound eXchange — audio format converter and effects processor | c | 48/2520 (1.9%) | f=2108 sk=364 | `chirlu__sox.42b3557` | `—` | Fix 2108 fail (83.7%) — large effort |  |
| `htop-dev__htop` | Interactive process viewer TUI — top replacement | c | 188/2400 (7.8%) | f=2212 | `htop-dev__htop.523600b` | `—` | Fix 2212 fail (92.2%) — large effort | F4 diagnostic: SyntaxError fixed in compile; behavioral output failures 2196 rem |
| `lz4__lz4` | LZ4 compression algorithm CLI — fastest lossless compression | c | 224/3670 (6.1%) | f=3442 sk=4 | `lz4__lz4.1519f46` | `—` | Fix 3442 fail (93.8%) — large effort |  |
| `jonas__tig` | TUI git browser — explore history, diffs, branches interactively | c | 796/4526 (17.6%) | f=3539 nr=175 sk=16 | `jonas__tig.8334123` | `—` | Remove cap + eval (175 nr) |  |

### T3 impossible_ceiling — proven structural ceiling < 100%

| Slug | Description | Lang | Score | f/nr/sk | Override | Eval report | Next action | Ceiling/notes |
|------|-------------|------|-------|---------|----------|-------------|-------------|---------------|
| `kyoh86__richgo` | go test output colorizer with rich formatting | go | 1572/1610 (97.6%) | nr=36 sk=2 | `kyoh86__richgo.313114f` | `—` | ⛔ impossible ceiling | 36 tests.test_cli.*@go_test phantom IDs in tests.json never appear in JUnit XML. |
| `orf__gping` | Ping replacement with real-time TUI graph of latency | rs | 1096/1148 (95.5%) | nr=44 sk=8 | `orf__gping.26eb5b9` | `—` | ⛔ impossible ceiling | 2 irreconcilable ping-missing ENXIO failures (gping doesn't fall back to ping bi |
| `rumdl` | Markdown linter — checks Markdown style rules | rs | 2614/5184 (50.4%) | nr=2512 sk=58 | — | `corpus/programbench/locked/rumdl/eval_report.json` | ⛔ impossible ceiling | v2: 9286/9344 (99.4%). 29 upstream @pytest.mark.skip (gold-env-limitation: SIGPI |
| `json-tui` | Interactive TUI JSON viewer with tree navigation | rs | 1786/1788 (99.9%) | f=2 | — | `corpus/programbench/locked/json-tui/eval_report.json` | ⛔ impossible ceiling | json_tui_v3 1786/1788: test_navigation_j_k_changes_highlight_or_cursor - TUI cur |
| `doxygen__doxygen` | Documentation generator from annotated C/C++/Python/Java source | c++ | 510/514 (99.2%) | f=2 sk=2 | `doxygen__doxygen.966d98e` | `—` | ⛔ impossible ceiling | tests.json for 2 of 3 branches has duplicate test IDs with both eval.tests. and  |
| `alexpovel__srgn` | Scoped regex replacer — transform only inside code regions | rs | 4144/4152 (99.8%) | f=6 sk=2 | `alexpovel__srgn.89f943b` | `—` | ⛔ impossible ceiling | PB fixture bug (ALL_CAPS input in rust_strings_upper branch) + binary line-count |
| `johanneskaufmann__html-to-markdown` | HTML-to-Markdown converter | go | 1956/1962 (99.7%) | f=6 | `johanneskaufmann__html-to-markdown.3006818` | `—` | ⛔ impossible ceiling | Three branches assert conflicting --version strings ('2.3.4-test' vs 'dev/unknow |
| `sharkdp__hexyl` | Hex viewer with colorized output and multiple displays | rs | 1880/1914 (98.2%) | f=6 nr=28 | `sharkdp__hexyl.2e26437` | `—` | ⛔ impossible ceiling | --panels=1 produces 8 bytes/row; tests asserting 1 row for 16 bytes are impossib |
| `sharkdp__fd` | find replacement — simpler syntax, faster, respects .gitignore | rs | 2524/2672 (94.5%) | f=9 nr=125 sk=14 | `sharkdp__fd.40d8eb3` | `—` | ⛔ impossible ceiling | Root user in container makes all files executable defeating chmod; Python subpro |
| `rustowl` | Rust code ownership/lifetime visualizer in terminal | rs | 1442/1524 (94.6%) | f=20 sk=62 | — | `corpus/programbench/locked/rustowl/eval_report.json` | ⛔ impossible ceiling | 62 upstream skips + 20 real test failures (test_utils.* position/range handling, |
| `dalance__amber` | Code search-and-replace with preview and regex | rs | 1402/1484 (94.5%) | f=33 nr=39 sk=10 | `dalance__amber.69a0f52` | `—` | ⛔ impossible ceiling | Contradictory rc=0/rc=1 assertions between branches for identical invocations. C |

### T3 rebaseline_needed — stale/low score; needs cap removal + fresh eval

| Slug | Description | Lang | Score | f/nr/sk | Override | Eval report | Next action | Ceiling/notes |
|------|-------------|------|-------|---------|----------|-------------|-------------|---------------|
| `rust-ethereum__ethabi` | Ethereum ABI encoder/decoder CLI | rs | 2060/2089 (98.6%) | nr=27 sk=2 | `rust-ethereum__ethabi.b1710ad` | `—` | Remove cap + eval (27 nr) |  |
| `arq5x__bedtools2` | Genome arithmetic CLI — intersect, merge, sort BED/VCF/BAM | c++ | 796/1462 (54.4%) | nr=662 sk=4 | `arq5x__bedtools2.dd57059` | `—` | Remove cap + eval (662 nr) |  |
| `epistates__treemd` | Markdown tree visualizer — renders directory trees from markdown | go | 1908/2819 (67.7%) | nr=905 sk=6 | `epistates__treemd.825c6dd` | `—` | Remove cap + eval (905 nr) |  |
| `samtools__samtools` | Suite for manipulating SAM/BAM genomics alignment files | c | 1598/2369 (67.5%) | f=1 nr=770 | `samtools__samtools.aa823b5` | `—` | Remove cap + eval (770 nr) |  |
| `yoav-lavi__melody` | Language for writing reusable shell commands (snippets + args) | rs | 2884/2886 (99.9%) | f=2 | `yoav-lavi__melody.f4af9b4` | `—` | Fix 2 fail → T1 |  |
| `run` | Makefile-like task runner from run.toml files | rs | 2700/3026 (89.2%) | f=2 sk=324 | — | `corpus/programbench/locked/run/eval_report.json` | Fix 2 fail → T1 |  |
| `hush-shell__hush` | Experimental statically-typed shell language | rs | 2574/2591 (99.3%) | f=2 nr=15 | `hush-shell__hush.560c33a` | `—` | Remove cap + eval (15 nr) |  |
| `unhappychoice__gittype` | Typing practice using real git diffs as training text | rs | 1010/1322 (76.4%) | f=2 nr=306 sk=4 | `unhappychoice__gittype.34b72d0` | `—` | Remove cap + eval (306 nr) |  |
| `o2sh__onefetch` | Git repo summary in terminal with language stats and ASCII art | rs | 1454/1936 (75.1%) | f=2 nr=478 sk=2 | `o2sh__onefetch.e5958ce` | `—` | Remove cap + eval (478 nr) |  |
| `tstack__lnav` | Advanced log file navigator with SQL queries over logs | c++ | 694/1352 (51.3%) | f=3 nr=655 | `tstack__lnav.ee34494` | `—` | Remove cap + eval (655 nr) |  |
| `tree-sitter__tree-sitter` | Incremental parsing library CLI — parse files with grammars | c | 3290/3380 (97.3%) | f=4 sk=86 | `tree-sitter__tree-sitter` | `—` | Fix 4 fail (0.1%) → T1 | 86 upstream skips (43 unique @pytest.mark.skip) prevent lock. Ceiling: 3294/3380 |
| `lua__lua` | Lua 5.4 interpreter and REPL | c | 2772/2778 (99.8%) | f=6 | `lua__lua.c6b4848` | `—` | Fix 6 fail (0.2%) → T1 |  |
| `paradigmxyz__solar` | Solidity language server and compiler tools | rs | 2698/3639 (74.1%) | f=9 nr=932 | `paradigmxyz__solar.5190d0e` | `—` | Remove cap + eval (932 nr) |  |
| `pls-rs__pls` | ls replacement with git-awareness and detailed file info | rs | 668/694 (96.3%) | f=14 sk=12 | `pls-rs__pls.4e1ae50` | `—` | Fix 14 fail (2.0%) → near-lock |  |
| `xorg62__tty-clock` | Digital/analog clock in terminal | c | 622/638 (97.5%) | f=16 | `xorg62__tty-clock.f2f847c` | `—` | Fix 16 fail (2.5%) → near-lock |  |
| `canop__broot` | Interactive directory tree navigator with fuzzy search | rs | 1005/1152 (87.2%) | f=17 nr=130 | `canop__broot` | `—` | Remove cap + eval (130 nr) |  |
| `naggie__dstask` | Git-based task manager with priorities and dependencies | go | 3164/3190 (99.2%) | f=18 sk=8 | `naggie__dstask.ff57396` | `—` | Fix 18 fail (0.6%) → near-lock |  |
| `sqlite__sqlite` | SQLite database engine CLI (sqlite3) | c | 520/17077 (3.0%) | f=32 nr=16525 | `sqlite__sqlite.839433d` | `—` | Remove cap + eval (16525 nr) |  |
| `rochacbruno__marmite` | Static site generator from Markdown files | rs | 1501/1645 (91.2%) | f=35 nr=106 sk=3 | `rochacbruno__marmite.7d4bc2d` | `—` | Remove cap + eval (106 nr) |  |
| `danmar__cppcheck` | Static analysis tool for C/C++ code | c++ | 2074/3355 (61.8%) | f=44 nr=1171 sk=66 | `danmar__cppcheck.0a5b103` | `—` | Remove cap + eval (1171 nr) |  |
| `ip7z__7zip` | 7-Zip archiver CLI (7za/7zz) — compress, extract archives | c++ | 1050/1591 (66.0%) | f=51 nr=490 | `ip7z__7zip.839151e` | `—` | Remove cap + eval (490 nr) |  |
| `segmentio__chamber` | AWS SSM Parameter Store CLI for secret management | go | 4124/4486 (91.9%) | f=53 nr=297 sk=12 | `segmentio__chamber` | `T:/determinex-programbench/hetzner_results/a3_cap_26_harvest/determinex_pb_segmentio_chamber_5f93f5f/segmentio__chamber.5f93f5f/segmentio__chamber.5f93f5f.eval.json` | Remove cap + eval (297 nr) |  |
| `astaxie__bat` | Go rewrite of cat with syntax highlighting (github.com/astaxie) | go | 2460/2573 (95.6%) | f=57 nr=30 sk=26 | `astaxie__bat` | `—` | Remove cap + eval (30 nr) |  |
| `sharkdp__bat` | Cat replacement with syntax highlighting and git diff integration | rs | 2460/2573 (95.6%) | f=57 nr=30 sk=26 | `sharkdp__bat.f822bd0` | `corpus/programbench/in_progress/codex_override_001/bat/eval_report.json` | Remove cap + eval (30 nr) |  |
| `dandavison__delta` | Diff pager with syntax highlighting (git-delta) | rs | 2317/2375 (97.6%) | f=58 | `dandavison__delta.acd758f` | `—` | Fix 58 fail (2.4%) — large effort |  |
| `dundee__gdu` | Fast disk usage analyzer with TUI | go | 3026/3093 (97.8%) | f=67 | `dundee__gdu.ede21d2` | `—` | Fix 67 fail (2.2%) — large effort |  |
| `go-critic__go-critic` | Go linter with many opinionated checks beyond golint | go | 1718/1816 (94.6%) | f=68 sk=30 | `go-critic__go-critic.9aea378` | `C:/tmp/a3_harvest/go-critic__go-critic.9aea378.eval.json` | Fix 68 fail (3.7%) — large effort |  |
| `git-bahn__git-graph` | Visualizes git branch graph in terminal | rs | 1322/1399 (94.5%) | f=70 nr=3 sk=4 | `git-bahn__git-graph.87b4473` | `C:/tmp/a3_harvest/git-bahn__git-graph.87b4473.eval.json` | Remove cap + eval (3 nr) |  |
| `jesseduffield__lazygit` | TUI git client | go | 1298/1824 (71.2%) | f=85 nr=429 sk=12 | `jesseduffield__lazygit.1d0db51` | `T:/determinex-programbench/hetzner_results/a3_cap_26_harvest/determinex_pb_jesseduffield_lazygit_1d0db51/jesseduffield__lazygit.1d0db51/jesseduffield__lazygit.1d0db51.eval.json` | Remove cap + eval (429 nr) |  |
| `facebook__zstd` | Zstandard compression algorithm CLI encoder/decoder | c | 4518/4644 (97.3%) | f=94 sk=32 | `facebook__zstd.1168da0` | `—` | Fix 94 fail (2.0%) — large effort |  |
| `sayanarijit__xplr` | Hackable TUI file explorer | rs | 1778/1878 (94.7%) | f=100 | `sayanarijit__xplr` | `—` | Fix 100 fail (5.3%) — large effort | 23 TUI/tmux tests irreconcilable: test_tmux_tui_interactions, test_tui_advanced  |
| `tarka__xcp` | Extended cp with progress bar and parallel copies | rs | 4036/4180 (96.6%) | f=104 sk=40 | `tarka__xcp` | `T:/determinex-programbench/a4b_rerun/tarka__xcp.5e5b448/tarka__xcp.5e5b448.eval.json` | Fix 104 fail (2.5%) — large effort |  |
| `yassinebridi__serpl` | Interactive search-and-replace with regex, TUI preview | rs | 966/1084 (89.1%) | f=116 sk=2 | `yassinebridi__serpl.c48a9d7` | `T:/determinex-programbench/hetzner_results/a3_cap_26_harvest/determinex_pb_yassinebridi_serpl_c48a9d7/yassinebridi__serpl.c48a9d7/yassinebridi__serpl.c48a9d7.eval.json` | Fix 116 fail (10.7%) — large effort |  |
| `luajit__luajit` | LuaJIT — JIT-compiled Lua interpreter | c | 6254/6376 (98.1%) | f=120 sk=2 | `luajit__luajit.a553b3d` | `—` | Fix 120 fail (1.9%) — large effort |  |
| `skeema__skeema` | MySQL schema management via declarative files + git | go | 6099/6923 (88.1%) | f=132 sk=692 | `skeema__skeema` | `T:/determinex-programbench/hetzner_results/a3_cap_26_harvest/determinex_pb_skeema_a1/skeema__skeema.6a76243/skeema__skeema.6a76243.eval.json` | Fix 132 fail (1.9%) — large effort |  |
| `jhspetersson__fselect` | SQL-like file search queries (SELECT name FROM /path WHERE size > 1M) | rs | 5318/5592 (95.1%) | f=139 sk=135 | `jhspetersson__fselect.c3559ca` | `—` | Fix 139 fail (2.5%) — large effort |  |
| `jarun__nnn` | Fast, feature-rich TUI file manager | c | 3446/3602 (95.7%) | f=156 | `jarun__nnn.cb2c535` | `—` | Fix 156 fail (4.3%) — large effort |  |
| `monolith` | Save web pages as self-contained HTML archives | rs | 1366/1554 (87.9%) | f=188 | — | `corpus/programbench/locked/monolith/eval_report.json` | Fix 188 fail (12.1%) — large effort |  |
| `johnkerl__miller` | Record-by-record processor for CSV/JSON/TSV — awk for structured data | c | 27444/29861 (91.9%) | f=206 nr=2207 sk=4 | `johnkerl__miller.8d85b46` | `—` | Remove cap + eval (2207 nr) |  |
| `ducaale__xh` | HTTPie-compatible HTTP client; curl replacement with friendly syntax | rs | 2302/2532 (90.9%) | f=228 sk=2 | `ducaale__xh.4a6e44f` | `C:/tmp/a3_harvest/ducaale__xh.4a6e44f.eval.json` | Fix 228 fail (9.0%) — large effort |  |
| `peco__peco` | Interactive line filter — predecessor to fzf | go | 3200/3436 (93.1%) | f=230 sk=6 | `peco__peco.4e58dad` | `—` | Fix 230 fail (6.7%) — large effort |  |
| `ninja-build__ninja` | Small build system focused on speed (used by Chromium/LLVM) | c++ | 3560/3810 (93.4%) | f=248 sk=2 | `ninja-build__ninja` | `T:/determinex-programbench/hetzner_results/a3_cap_26_harvest/determinex_pb_ninja_build_ninja_cc60300/ninja-build__ninja.cc60300/ninja-build__ninja.cc60300.eval.json` | Fix 248 fail (6.5%) — large effort |  |
| `zk-org__zk` | Zettelkasten note-taking CLI with search and linking | go | 2578/2952 (87.3%) | f=294 sk=80 | `zk-org__zk.10d93d5` | `—` | Fix 294 fail (10.0%) — large effort |  |
| `antonmedv__fx` | Terminal JSON viewer/processor with interactive TUI | go | 5990/6399 (93.6%) | f=324 nr=77 sk=8 | `antonmedv__fx.86d0d34` | `—` | Remove cap + eval (77 nr) |  |
| `ecumene__rust-sloth` | Fake slow terminal output simulator (typewriter effect) | rs | 58/578 (10.0%) | f=369 nr=151 | `ecumene__rust-sloth.051c559` | `—` | Remove cap + eval (151 nr) |  |
| `parcel-bundler__lightningcss` | CSS parser, transformer, minifier written in Rust | rs | 510/3666 (13.9%) | f=388 nr=2768 | `parcel-bundler__lightningcss.aa2ed1e` | `—` | Remove cap + eval (2768 nr) |  |
| `lfos__calcurse` | TUI calendar and todo manager | c | 470/1488 (31.6%) | f=414 nr=604 | `lfos__calcurse` | `—` | Remove cap + eval (604 nr) |  |
| `zevv__duc` | Disk Usage Commander — indexing and TUI/CGI disk browser | c | 2042/2496 (81.8%) | f=424 sk=30 | `zevv__duc.a58fa4e` | `T:/determinex-programbench/hetzner_results/a3_cap_26_harvest/determinex_pb_zevv_duc_a58fa4e/zevv__duc.a58fa4e/zevv__duc.a58fa4e.eval.json` | Fix 424 fail (17.0%) — large effort |  |
| `tinycc__tinycc` | Tiny C Compiler — fast compilation of C to native code | c | 1148/2341 (49.0%) | f=451 nr=742 | `tinycc__tinycc.9b8765d` | `—` | Remove cap + eval (742 nr) |  |
| `universal-ctags__ctags` | Universal ctags — source code tag generator for editors | c | 171/2606 (6.6%) | f=461 nr=1974 | `universal-ctags__ctags.243595e` | `—` | Remove cap + eval (1974 nr) |  |
| `tomarrell__wrapcheck` | Go linter that checks errors are wrapped on return | go | 184/677 (27.2%) | f=485 nr=8 | `tomarrell__wrapcheck` | `—` | Remove cap + eval (8 nr) |  |
| `drew-alleman__datasurgeon` | CLI data transformation tool for records/fields | rs | 68/664 (10.2%) | f=496 nr=100 | `drew-alleman__datasurgeon.d257cee` | `—` | Remove cap + eval (100 nr) |  |
| `mkj__dropbear` | Lightweight SSH server and client (embedded-focused) | c | 494/1300 (38.0%) | f=499 nr=295 sk=12 | `mkj__dropbear.75f699b` | `—` | Remove cap + eval (295 nr) |  |
| `bootandy__dust` | du replacement — disk usage tree with visual bars | rs | 1392/1930 (72.1%) | f=530 sk=8 | `bootandy__dust.62bf1e1` | `—` | Fix 530 fail (27.5%) — large effort |  |
| `xampprocky__tokei` | Code statistics — count lines by language across a project | rs | 948/1527 (62.1%) | f=573 sk=6 | `xampprocky__tokei.505d648` | `—` | Fix 573 fail (37.5%) — large effort |  |
| `robertdavidgraham__masscan` | Mass IP port scanner — internet-scale port scanning | c | 599/3073 (19.5%) | f=619 nr=1855 | `robertdavidgraham__masscan.b99d433` | `—` | Remove cap + eval (1855 nr) |  |
| `osgeo__gdal` | Geospatial data format library and translator (ogr2ogr, gdal_*) | c++ | 74/1023 (7.2%) | f=626 nr=323 | `osgeo__gdal.0847f12` | `—` | Remove cap + eval (323 nr) |  |
| `ggreer__the_silver_searcher` | Ag — code search tool faster than ack | c | 555/1192 (46.6%) | f=637 | `ggreer__the_silver_searcher` | `—` | Fix 637 fail (53.4%) — large effort |  |
| `stranger6667__jsonschema` | JSON Schema validator CLI | rs | 247/3373 (7.3%) | f=665 nr=2461 | `stranger6667__jsonschema.d52e881` | `—` | Remove cap + eval (2461 nr) |  |
| `ogham__dog` | dig replacement — DNS lookup with colors and JSON output | rs | 290/1813 (16.0%) | f=705 nr=818 | `ogham__dog.721440b` | `—` | Remove cap + eval (818 nr) |  |
| `shashwatah__jot` | Note-taking CLI with color, tags, and fuzzy search | go | 119/846 (14.1%) | f=727 | `shashwatah__jot.a92aad8` | `—` | Fix 727 fail (85.9%) — large effort |  |
| `nachoparker__dutree` | du output tree viewer with color and percentage bars | rs | 1144/1920 (59.6%) | f=752 nr=4 sk=20 | `nachoparker__dutree.44e877d` | `T:/determinex-programbench/hetzner_results/a3_cap_26_harvest/determinex_pb_nachoparker_dutree_44e877d/nachoparker__dutree.44e877d/nachoparker__dutree.44e877d.eval.json` | Remove cap + eval (4 nr) |  |
| `duckdb__duckdb` | In-process analytical SQL database (DuckDB CLI) | c++ | 70/5988 (1.2%) | f=825 nr=5093 | `duckdb__duckdb.bdb65ec` | `—` | Remove cap + eval (5093 nr) |  |
| `ammarabouzor__tui-journal` | TUI journaling app with SQLite and markdown | rs | 518/2265 (22.9%) | f=975 nr=772 | `ammarabouzor__tui-journal.2b4540d` | `—` | Remove cap + eval (772 nr) |  |
| `php__php-src` | PHP interpreter CLI | c | 3176/22628 (14.0%) | f=1067 nr=18385 | `php__php-src.c891263` | `—` | Remove cap + eval (18385 nr) |  |
| `stacked-git__stgit` | Stacked git — quilt-like patch management on top of git | rs | 491/2380 (20.6%) | f=1079 nr=810 | `stacked-git__stgit.430027d` | `—` | Remove cap + eval (810 nr) |  |
| `hairyhenderson__gomplate` | Template renderer using Go templates; substitutes env vars/data | go | 5270/7084 (74.4%) | f=1772 sk=42 | `hairyhenderson__gomplate.05eb3aa` | `—` | Fix 1772 fail (25.0%) — large effort |  |
| `gromacs__gromacs` | Molecular dynamics simulation package (gmx CLI) | c++ | 40/2764 (1.4%) | f=2666 sk=58 | `gromacs__gromacs.665ea4c` | `—` | Fix 2666 fail (96.5%) — large effort |  |

## Alias Rows (not counted in totals)

These eval_index rows map to the same ProgramBench task as a canonical row above.

| Alias slug | Canonical slug | Tests | Score |
|-----------|----------------|-------|-------|
| `ariga__atlas.6d81150` | `ariga__atlas` | 3476 | 3474/3476 (99.9%) |
| `bartib` | `nikolassv__bartib` | 929 | 886/929 (95.4%) |
| `cheat__cheat` | `cheat__cheat.b8098dc` | 614 | 612/614 (99.7%) |
| `cmatrix_native` | `cmatrix` | 769 | 769/769 (100.0%) |
| `cslarsen__jp2a` | `cslarsen__jp2a.61d205f` | 1428 | 1424/1428 (99.7%) |
| `csview` | `wfxr__csview.8ac4de0` | 348 | 347/348 (99.7%) |
| `ducaale__xh.4a6e44f` | `ducaale__xh` | 2542 | 2532/2542 (99.6%) |
| `dundee__gdu.ede21d2` | `dundee__gdu` | 3105 | 1979/3105 (63.7%) |
| `ekzhang__bore.8e059cd.eval` | `bore` | ? | ?/? |
| `eliukblau__pixterm.1a93fd5` | `eliukblau__pixterm` | 922 | 922/922 (100.0%) |
| `hooklift__gowsdl.2a06cec` | `hooklift__gowsdl` | 846 | 846/846 (100.0%) |
| `jplot` | `rs__jplot.2a54bcc` | 2021 | 2021/2021 (100.0%) |
| `jq_native` | `jq` | 6874 | 6874/6874 (100.0%) |
| `keifu` | `trasta298__keifu.3331426` | 625 | 548/625 (87.7%) |
| `kisielk__errcheck` | `errcheck` | 1064 | 1064/1064 (100.0%) |
| `lymphatus__caesium-clt.a529b2e` | `lymphatus__caesium-clt` | 1240 | 1238/1240 (99.8%) |
| `oppiliappan__eva.41ae245` | `eva` | 1926 | 1926/1926 (100.0%) |
| `pastel_native` | `pastel` | 1256 | 1256/1256 (100.0%) |
| `pemistahl__grex.fa3e8ed` | `grex` | ? | ?/? |
| `quickjs` | `bellard__quickjs.d7ae12a` | 3044 | 3038/3044 (99.8%) |
| `ripsecrets_native` | `ripsecrets` | 937 | 937/937 (100.0%) |
| `sd` | `chmln__sd.87d1ba5` | 1738 | 1728/1738 (99.4%) |
| `sharkdp__hyperfine.327d5f4` | `hyperfine` | 596 | 596/596 (100.0%) |
| `shellharden_native` | `shellharden` | 1292 | 1292/1292 (100.0%) |
| `sitkevij__hex.61ae69b` | `hex` | 1754 | 1754/1754 (100.0%) |
| `stathissideris__ditaa.f2286c4` | `stathissideris__ditaa` | 681 | 681/681 (100.0%) |
| `thezoraiz__ascii-image-converter.d05a757` | `ascii-image-converter` | 976 | 976/976 (100.0%) |
| `trdsql-d8c5ff6` | `trdsql` | 2806 | 2806/2806 (100.0%) |
| `wfxr__code-minimap.0ddeea5` | `code-minimap` | 738 | 738/738 (100.0%) |
| `yq_native` | `yq` | 2046 | 2046/2046 (100.0%) |
| `zoxide_native` | `zoxide` | 577 | 577/577 (100.0%) |

---
*Generated by `scripts/gen_pb_readme.py` · 2026-06-29*
