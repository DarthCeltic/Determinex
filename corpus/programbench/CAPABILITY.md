# Determinex — ProgramBench Full-Capability Map

_Generated 2026-07-01 from `capability_map.json` (schema determinex-pb-capability-map-v2). Single source of truth for lock status: `verified_locks.json`._

> **What this is:** every ProgramBench task, the capability it exercises (language / eval-reconciliation technique / behavioral surface), and its verification status. A capability is **PROVEN** only when the tool is a sha-verified clean lock; everything else is in progress.

## Status (the honest count)

| Status | Count | Meaning |
|---|---:|---|
| CLAIMED | 92 | locked archive exists but unverified (likely degraded record) — re-eval to promote |
| UNLOCKED_WORKING | 108 | factory/working copy exists, not yet locked |
| **TOTAL** | **200** | full ProgramBench task universe |

## Coverage breadth

- **Languages (6):** c/c++, go, haskell, jvm, python, rust
- **Eval/build techniques (14):** argv0-preserve, bidir-mirror, build-target-detect, clock-freeze, clock-route, env-home-route, error-normalize, locale-pin, nodeid-prefix-route, privilege-route, pty-allocate, source-completion, tui-collection-filter, version-pin
- **Behavioral surfaces (10):** ansi-color, datetime, encoding, exit-code, output-mode, path-tmp, regex-search, tty-render, version-build, whitespace

## PROVEN locks (canonical, sha-pinned)

_(none yet)_

## Technique coverage (tasks exercising each)

| Item | # tasks |
|---|---:|
| tui-collection-filter | 178 |
| argv0-preserve | 167 |
| error-normalize | 166 |
| pty-allocate | 165 |
| nodeid-prefix-route | 162 |
| bidir-mirror | 74 |
| clock-freeze | 56 |
| clock-route | 56 |
| locale-pin | 55 |
| source-completion | 44 |
| build-target-detect | 27 |
| privilege-route | 26 |
| env-home-route | 10 |
| version-pin | 4 |

## Language coverage

| Item | # tasks |
|---|---:|
| c/c++ | 190 |
| python | 169 |
| rust | 99 |
| go | 47 |
| haskell | 1 |
| jvm | 1 |

## Behavioral surface coverage

| Item | # tasks |
|---|---:|
| datetime | 92 |
| encoding | 92 |
| output-mode | 92 |
| regex-search | 91 |
| version-build | 90 |
| exit-code | 88 |
| whitespace | 88 |
| path-tmp | 87 |
| ansi-color | 78 |
| tty-render | 76 |

## In-progress (the production line)

**CLAIMED (92)** — locked archive, awaiting re-verify:

> `angle-grinder`, `argc`, `ascii-image-converter`, `atlas`, `bartib`, `bore`, `brotli`, `chroma`, `clog-cli`, `cmatrix`, `code-minimap`, `crowbook`, `csview`, `curlie`, `deadnix`, `diffr`, `dirble`, `direnv`, `ditaa`, `doxygen`, `dsq`, `dupl`, `elfcat`, `entr`, `errcheck`, `eureka`, `eva`, `fasttext`, `fblog`, `figlet`, `flamelens`, `fzf`, `genact`, `git-trim`, `go-mod-outdated`, `gowsdl`, `gping`, `grex`, `gron`, `handlr`, `hck`, `hex`, `hostctl`, `htmlq`, `hyperfine`, `i3-style`, `igrep`, `jplot`, `jq`, `json-tui`, `keifu`, `loop`, `miniserve`, `monolith`, `muffet`, `ngrrram`, `nomino`, `nsh`, `pastel`, `pier`, `pigz`, `pingu`, `pixterm`, `quickjs`, `revive`, `rhit`, `richgo`, `ripgrep`, `ripsecrets`, `rnr`, `rumdl`, `run`, `rustowl`, `scc`, `sd`, `seqtk`, `shellharden`, `svd2rust`, `svgbob`, `tailspin`, `tex-fmt`, `thokr`, `tparse`, `trdsql`, `trdsql-d8c5ff6`, `tuc`, `xq`, `xsv`, `xz`, `yq`, `zip-password-finder`, `zoxide`

**UNLOCKED_WORKING (108)** — factory copy, not yet locked:

> `7zip`, `age`, `amber`, `ast-grep`, `bat`, `bedtools2`, `blake3`, `broot`, `caesium-clt`, `calcurse`, `caps-log`, `chafa`, `chamber`, `cheat`, `codesnap`, `cppcheck`, `ctags`, `datasurgeon`, `delta`, `dep-tree`, `dog`, `dropbear`, `dstask`, `dua-cli`, `duc`, `duckdb`, `dust`, `dutree`, `ethabi`, `fd`, `felix`, `ffmpeg`, `fselect`, `fx`, `gdal`, `gdu`, `git-graph`, `gittype`, `go-critic`, `goimports-reviser`, `gomplate`, `gotests`, `gromacs`, `halite`, `hashcards`, `hexyl`, `html-to-markdown`, `htop`, `hush`, `hwatch`, `jot`, `jp2a`, `jsonschema`, `kiro-editor`, `lazygit`, `lightningcss`, `lnav`, `lua`, `luajit`, `lz4`, `marmite`, `masscan`, `mdbook`, `melody`, `miller`, `ninja`, `nnn`, `oha`, `onefetch`, `oranda`, `ov`, `pandoc`, `parallel-disk-usage`, `parqeye`, `peco`, `php-src`, `pipr`, `pls`, `proj`, `pueue`, `quinn`, `rust-sloth`, `samtools`, `serpl`, `skeema`, `solar`, `sox`, `sqlite`, `srgn`, `statix`, `stgit`, `the_silver_searcher`, `tig`, `tinycc`, `tokei`, `tree-sitter`, `treemd`, `tty-clock`, `tui-journal`, `typst`, `walk`, `wrapcheck`, `xcp`, `xh`, `xplr`, `yj`, `zk`, `zstd`

---
*Regenerate: `python scripts/determinex_pb_capability_map.py build` then `python scripts/gen_capability_doc.py`. Lock status is authoritative in `verified_locks.json`; this doc is a rendering.*