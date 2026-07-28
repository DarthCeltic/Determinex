# ProgramBench 200-Tool Completion Map

Generated: `2026-05-24T05:58:37+00:00`

This is the live routing map for driving every ProgramBench tool to Rule A without leaving Python logic in native-language tools. Routes are based on the current lock board plus `LANGUAGE_AUDIT.json`.

## Summary

- Tools: `201`
- Locked/100 band: `12`
- Missing override directories: `20`
- Aggregate runnable: `62928/154902`
- Bands: `100=12`, `90-99=8`, `70-89=10`, `50-69=17`, `25-49=72`, `0-24=75`, `0=7`
- Audit actions: `rewrite-native=130`, `scaffold-stub=18`, `keep-thin=15`, `already-native=14`, `locked=12`, `unknown=8`, `investigate=2`, `keep-python=2`
- Routes: `native:native-source=124`, `native:rust=18`, `native:go=14`, `locked=12`, `thin:rust=8`, `missing-override=8`, `native:c=6`, `thin:unknown=6`, `investigate=2`, `source:python=2`, `thin:c=1`

## Immediate Queue

| priority | score | passed/runnable | audit | source | route | slug | action |
|---:|---:|---:|---|---|---|---|---|
| 1 | 99.8 | 431/432 | already-native | go | native:go | `raviqqe__muffet` | push remaining failures in native source |
| 2 | 98.5 | 774/786 | already-native | go | native:go | `kyoh86__richgo` | push remaining failures in native source |
| 3 | 98.5 | 770/782 | already-native | rust | native:rust | `mookid__diffr` | push remaining failures in native source |
| 4 | 97.4 | 267/274 | already-native | rust | native:rust | `trasta298__keifu` | push remaining failures in native source |
| 5 | 96.1 | 823/856 | already-native | rust | native:rust | `sstadick__hck` | push remaining failures in native source |
| 6 | 88.2 | 762/864 | already-native | rust | native:rust | `chmln__sd` | push remaining failures in native source |
| 7 | 78.0 | 607/778 | already-native | rust | native:rust | `miserlou__loop` | push remaining failures in native source |
| 8 | 74.9 | 1025/1368 | already-native | rust | native:rust | `nuta__nsh` | push remaining failures in native source |
| 9 | 98.4 | 811/824 | rewrite-native | go | native:go | `sclevine__yj` | replace Python/stub logic with real native source |
| 10 | 91.7 | 1394/1521 | rewrite-native | c | native:c | `jqlang__jq` | replace Python/stub logic with real native source |
| 11 | 90.5 | 716/791 | rewrite-native | unknown | native:native-source | `agourlay__zip-password-finder` | replace Python/stub logic with real native source |
| 12 | 88.1 | 661/750 | rewrite-native | unknown | native:native-source | `altdesktop__i3-style` | replace Python/stub logic with real native source |
| 13 | 81.7 | 574/703 | scaffold-stub | rust | native:rust | `konradsz__igrep` | replace Python/stub logic with real native source |
| 14 | 78.7 | 583/741 | rewrite-native | go | native:go | `rs__curlie` | replace Python/stub logic with real native source |
| 15 | 76.2 | 742/974 | rewrite-native | unknown | native:native-source | `johanneskaufmann__html-to-markdown` | replace Python/stub logic with real native source |
| 16 | 71.9 | 1148/1597 | rewrite-native | c | native:c | `tinycc__tinycc` | replace Python/stub logic with real native source |
| 180 | 70.9 | 683/963 | keep-python | python | source:python | `oppiliappan__eva` | finish exact behavior in Python source |
| 181 | 70.8 | 552/780 | keep-python | python | source:python | `dalance__amber` | finish exact behavior in Python source |

## Full 200-Tool Map

| priority | band | score | passed/runnable | audit | source | route | slug | reason |
|---:|---|---:|---:|---|---|---|---|---|
| 1 | 90-99 | 99.8 | 431/432 | already-native | go | native:go | `raviqqe__muffet` | native go source already present (41 files) |
| 2 | 90-99 | 98.5 | 774/786 | already-native | go | native:go | `kyoh86__richgo` | native go source already present (22 files) |
| 3 | 90-99 | 98.5 | 770/782 | already-native | rust | native:rust | `mookid__diffr` | native rust source already present (7 files) |
| 4 | 90-99 | 97.4 | 267/274 | already-native | rust | native:rust | `trasta298__keifu` | native rust source already present (26 files) |
| 5 | 90-99 | 96.1 | 823/856 | already-native | rust | native:rust | `sstadick__hck` | native rust source already present (7 files) |
| 6 | 70-89 | 88.2 | 762/864 | already-native | rust | native:rust | `chmln__sd` | native rust source already present (10 files) |
| 7 | 70-89 | 78.0 | 607/778 | already-native | rust | native:rust | `miserlou__loop` | native rust source already present (2 files) |
| 8 | 70-89 | 74.9 | 1025/1368 | already-native | rust | native:rust | `nuta__nsh` | native rust source already present (40 files) |
| 9 | 90-99 | 98.4 | 811/824 | rewrite-native | go | native:go | `sclevine__yj` | substantive Python (78 lines, 4 funcs) implementing a go tool |
| 10 | 90-99 | 91.7 | 1394/1521 | rewrite-native | c | native:c | `jqlang__jq` | substantive Python (133 lines, 3 funcs) implementing a c tool |
| 11 | 90-99 | 90.5 | 716/791 | rewrite-native | unknown | native:native-source | `agourlay__zip-password-finder` | substantive Python (348 lines, 3 funcs) implementing a unknown tool |
| 12 | 70-89 | 88.1 | 661/750 | rewrite-native | unknown | native:native-source | `altdesktop__i3-style` | substantive Python (287 lines, 7 funcs) implementing a unknown tool |
| 13 | 70-89 | 81.7 | 574/703 | scaffold-stub | rust | native:rust | `konradsz__igrep` | scaffold main.py with no bundled binary - low yield, needs native rewrite |
| 14 | 70-89 | 78.7 | 583/741 | rewrite-native | go | native:go | `rs__curlie` | substantive Python (672 lines, 5 funcs) implementing a go tool |
| 15 | 70-89 | 76.2 | 742/974 | rewrite-native | unknown | native:native-source | `johanneskaufmann__html-to-markdown` | substantive Python (419 lines, 10 funcs) implementing a unknown tool |
| 16 | 70-89 | 71.9 | 1148/1597 | rewrite-native | c | native:c | `tinycc__tinycc` | substantive Python (177 lines, 2 funcs) implementing a c tool |
| 17 | 25-49 | 41.7 | 348/834 | keep-thin | unknown | thin:unknown | `hatoo__oha` | main.py is thin exec wrapper around bundled ELF binary (oha) |
| 18 | 25-49 | 34.8 | 330/949 | keep-thin | rust | thin:rust | `bootandy__dust` | main.py is thin exec wrapper around bundled ELF binary (dust) |
| 19 | 25-49 | 34.3 | 418/1218 | keep-thin | rust | thin:rust | `sharkdp__fd` | main.py is thin exec wrapper around bundled ELF binary (fd) |
| 20 | 25-49 | 33.3 | 308/926 | keep-thin | rust | thin:rust | `byron__dua-cli` | main.py is thin exec wrapper around bundled ELF binary (dua) |
| 21 | 25-49 | 33.1 | 291/880 | keep-thin | rust | thin:rust | `sharkdp__hexyl` | main.py is thin exec wrapper around bundled ELF binary (hexyl) |
| 22 | 0-24 | 21.6 | 135/626 | keep-thin | c | thin:c | `sqlite__sqlite` | main.py is thin exec wrapper around bundled ELF binary (sqlite3) |
| 23 | 0-24 | 20.7 | 213/1027 | keep-thin | rust | thin:rust | `rust-lang__mdbook` | main.py is thin exec wrapper around bundled ELF binary (mdbook) |
| 24 | 0-24 | 20.3 | 89/439 | keep-thin | unknown | thin:unknown | `svenstaro__miniserve` | main.py is thin exec wrapper around bundled ELF binary (miniserve) |
| 25 | 0-24 | 16.5 | 191/1156 | keep-thin | rust | thin:rust | `sharkdp__pastel` | main.py is thin exec wrapper around bundled ELF binary (pastel) |
| 26 | 0-24 | 16.1 | 113/701 | keep-thin | rust | thin:rust | `ducaale__xh` | main.py is thin exec wrapper around bundled ELF binary (xh) |
| 27 | 0-24 | 8.8 | 70/791 | keep-thin | unknown | thin:unknown | `duckdb__duckdb` | main.py is thin exec wrapper around bundled ELF binary (duckdb) |
| 28 | 0-24 | 4.9 | 17/350 | keep-thin | unknown | thin:unknown | `ast-grep__ast-grep` | main.py is thin exec wrapper around bundled ELF binary (ast-grep) |
| 29 | 0-24 | 3.5 | 38/1081 | keep-thin | rust | thin:rust | `burntsushi__xsv` | main.py is thin exec wrapper around bundled ELF binary (xsv) |
| 30 | 0-24 | 2.2 | 16/740 | keep-thin | unknown | thin:unknown | `typst__typst` | main.py is thin exec wrapper around bundled ELF binary (typst) |
| 31 | 0-24 | 2.0 | 7/349 | keep-thin | unknown | thin:unknown | `arq5x__bedtools2` | main.py is thin exec wrapper around bundled ELF binary (bedtools) |
| 32 | 50-69 | 67.0 | 1036/1547 | rewrite-native | unknown | native:native-source | `skeema__skeema` | substantive Python (341 lines, 20 funcs) implementing a unknown tool |
| 33 | 50-69 | 66.0 | 579/877 | rewrite-native | unknown | native:native-source | `sitkevij__hex` | substantive Python (197 lines, 5 funcs) implementing a unknown tool |
| 34 | 50-69 | 61.0 | 252/413 | scaffold-stub | go | native:go | `sheepla__pingu` | scaffold main.py with no bundled binary - low yield, needs native rewrite |
| 35 | 50-69 | 60.5 | 471/778 | rewrite-native | unknown | native:native-source | `clog-tool__clog-cli` | substantive Python (425 lines, 6 funcs) implementing a unknown tool |
| 36 | 50-69 | 58.9 | 558/947 | rewrite-native | unknown | native:native-source | `nachoparker__dutree` | substantive Python (574 lines, 18 funcs) implementing a unknown tool |
| 37 | 50-69 | 58.9 | 418/710 | scaffold-stub | unknown | native:native-source | `foriequal0__git-trim` | scaffold main.py with no bundled binary - low yield, needs native rewrite |
| 38 | 50-69 | 58.7 | 461/785 | rewrite-native | unknown | native:native-source | `bensadeh__tailspin` | substantive Python (200 lines, 2 funcs) implementing a unknown tool |
| 39 | 50-69 | 58.7 | 358/610 | rewrite-native | unknown | native:native-source | `eradman__entr` | substantive Python (105 lines, 1 funcs) implementing a unknown tool |
| 40 | 50-69 | 58.2 | 636/1093 | rewrite-native | unknown | native:native-source | `nikoladucak__caps-log` | substantive Python (174 lines, 6 funcs) implementing a unknown tool |
| 41 | 50-69 | 57.8 | 486/841 | rewrite-native | unknown | native:native-source | `tarka__xcp` | substantive Python (282 lines, 4 funcs) implementing a unknown tool |
| 42 | 50-69 | 57.0 | 510/894 | rewrite-native | unknown | native:native-source | `parcel-bundler__lightningcss` | substantive Python (232 lines, 7 funcs) implementing a unknown tool |
| 43 | 50-69 | 53.2 | 470/884 | rewrite-native | unknown | native:native-source | `lfos__calcurse` | substantive Python (266 lines, 2 funcs) implementing a unknown tool |
| 44 | 50-69 | 52.7 | 746/1416 | rewrite-native | unknown | native:native-source | `ninja-build__ninja` | substantive Python (272 lines, 4 funcs) implementing a unknown tool |
| 45 | 50-69 | 52.0 | 385/741 | rewrite-native | unknown | native:native-source | `multiprocessio__dsq` | substantive Python (366 lines, 8 funcs) implementing a unknown tool |
| 46 | 25-49 | 49.4 | 563/1139 | rewrite-native | unknown | native:native-source | `gabotechs__dep-tree` | substantive Python (233 lines, 7 funcs) implementing a unknown tool |
| 47 | 25-49 | 49.2 | 599/1218 | rewrite-native | unknown | native:native-source | `robertdavidgraham__masscan` | substantive Python (403 lines, 6 funcs) implementing a unknown tool |
| 48 | 25-49 | 47.4 | 305/644 | rewrite-native | unknown | native:native-source | `rbakbashev__elfcat` | substantive Python (562 lines, 6 funcs) implementing a unknown tool |
| 49 | 25-49 | 47.2 | 645/1367 | rewrite-native | unknown | native:native-source | `astaxie__bat` | substantive Python (245 lines, 2 funcs) implementing a unknown tool |
| 50 | 25-49 | 46.1 | 601/1305 | rewrite-native | unknown | native:native-source | `hpjansson__chafa` | substantive Python (238 lines, 4 funcs) implementing a unknown tool |
| 51 | 25-49 | 44.5 | 308/692 | rewrite-native | unknown | native:native-source | `tree-sitter__tree-sitter` | substantive Python (174 lines, 10 funcs) implementing a unknown tool |
| 52 | 25-49 | 44.2 | 362/819 | rewrite-native | unknown | native:native-source | `arthursonzogni__json-tui` | substantive Python (159 lines, 3 funcs) implementing a unknown tool |
| 53 | 25-49 | 43.7 | 483/1106 | rewrite-native | unknown | native:native-source | `isona__dirble` | substantive Python (288 lines, 2 funcs) implementing a unknown tool |
| 54 | 25-49 | 42.8 | 368/859 | rewrite-native | unknown | native:native-source | `chmln__handlr` | substantive Python (292 lines, 16 funcs) implementing a unknown tool |
| 55 | 25-49 | 42.7 | 211/494 | rewrite-native | unknown | native:native-source | `wgunderwood__tex-fmt` | substantive Python (297 lines, 9 funcs) implementing a unknown tool |
| 56 | 25-49 | 42.7 | 531/1245 | rewrite-native | unknown | native:native-source | `riquito__tuc` | substantive Python (291 lines, 11 funcs) implementing a unknown tool |
| 57 | 25-49 | 41.9 | 125/298 | rewrite-native | rust | native:rust | `sharkdp__hyperfine` | substantive Python (404 lines, 19 funcs) implementing a rust tool |
| 58 | 25-49 | 41.6 | 292/702 | rewrite-native | unknown | native:native-source | `rs__jplot` | substantive Python (536 lines, 12 funcs) implementing a unknown tool |
| 59 | 25-49 | 41.1 | 139/338 | scaffold-stub | unknown | native:native-source | `yaa110__nomino` | scaffold main.py with no bundled binary - low yield, needs native rewrite |
| 60 | 25-49 | 41.1 | 488/1187 | rewrite-native | unknown | native:native-source | `blacknon__hwatch` | substantive Python (1087 lines, 47 funcs) implementing a unknown tool |
| 61 | 25-49 | 40.9 | 515/1259 | rewrite-native | go | native:go | `ariga__atlas` | substantive Python (242 lines, 9 funcs) implementing a go tool |
| 62 | 25-49 | 40.4 | 109/270 | rewrite-native | unknown | native:native-source | `lz4__lz4` | substantive Python (389 lines, 4 funcs) implementing a unknown tool |
| 63 | 25-49 | 39.8 | 367/922 | rewrite-native | unknown | native:native-source | `nikolassv__bartib` | substantive Python (585 lines, 19 funcs) implementing a unknown tool |
| 64 | 25-49 | 38.6 | 269/696 | rewrite-native | unknown | native:native-source | `mkj__dropbear` | substantive Python (1087 lines, 47 funcs) implementing a unknown tool |
| 65 | 25-49 | 38.6 | 379/981 | rewrite-native | unknown | native:native-source | `segmentio__chamber` | substantive Python (243 lines, 23 funcs) implementing a unknown tool |
| 66 | 25-49 | 38.4 | 321/837 | rewrite-native | unknown | native:native-source | `madler__pigz` | substantive Python (284 lines, 2 funcs) implementing a unknown tool |
| 67 | 25-49 | 37.5 | 398/1060 | rewrite-native | unknown | native:native-source | `brocode__fblog` | substantive Python (426 lines, 10 funcs) implementing a unknown tool |
| 68 | 25-49 | 36.9 | 377/1022 | rewrite-native | c | native:c | `jarun__nnn` | substantive Python (69 lines, 1 funcs) implementing a c tool |
| 69 | 25-49 | 36.8 | 270/733 | rewrite-native | unknown | native:native-source | `sayanarijit__xplr` | substantive Python (269 lines, 16 funcs) implementing a unknown tool |
| 70 | 25-49 | 36.5 | 437/1198 | rewrite-native | unknown | native:native-source | `rvben__rumdl` | substantive Python (307 lines, 10 funcs) implementing a unknown tool |
| 71 | 25-49 | 35.6 | 302/849 | rewrite-native | unknown | native:native-source | `codesnap-rs__codesnap` | substantive Python (228 lines, 6 funcs) implementing a unknown tool |
| 72 | 25-49 | 35.2 | 136/386 | rewrite-native | unknown | native:native-source | `rust-embedded__svd2rust` | substantive Python (232 lines, 7 funcs) implementing a unknown tool |
| 73 | 25-49 | 35.1 | 236/672 | scaffold-stub | rust | native:rust | `canop__broot` | scaffold main.py with no bundled binary - low yield, needs native rewrite |
| 74 | 25-49 | 35.0 | 407/1163 | rewrite-native | unknown | native:native-source | `guumaster__hostctl` | substantive Python (400 lines, 18 funcs) implementing a unknown tool |
| 75 | 25-49 | 34.9 | 518/1485 | rewrite-native | unknown | native:native-source | `ammarabouzor__tui-journal` | substantive Python (1087 lines, 47 funcs) implementing a unknown tool |
| 76 | 25-49 | 34.6 | 269/778 | scaffold-stub | unknown | native:native-source | `pier-cli__pier` | scaffold main.py with no bundled binary - low yield, needs native rewrite |
| 77 | 25-49 | 34.5 | 217/629 | rewrite-native | unknown | native:native-source | `ksxgithub__parallel-disk-usage` | substantive Python (347 lines, 4 funcs) implementing a unknown tool |
| 78 | 25-49 | 33.2 | 130/391 | rewrite-native | unknown | native:native-source | `jrnxf__thokr` | substantive Python (361 lines, 6 funcs) implementing a unknown tool |
| 79 | 25-49 | 32.9 | 219/666 | rewrite-native | unknown | native:native-source | `zevv__duc` | substantive Python (393 lines, 12 funcs) implementing a unknown tool |
| 80 | 25-49 | 32.4 | 114/352 | scaffold-stub | unknown | native:native-source | `facebookresearch__fasttext` | scaffold main.py with no bundled binary - low yield, needs native rewrite |
| 81 | 25-49 | 32.3 | 162/502 | rewrite-native | rust | native:rust | `cordx56__rustowl` | substantive Python (1087 lines, 47 funcs) implementing a rust tool |
| 82 | 25-49 | 31.7 | 491/1549 | rewrite-native | unknown | native:native-source | `stacked-git__stgit` | substantive Python (294 lines, 24 funcs) implementing a unknown tool |
| 83 | 25-49 | 31.3 | 229/731 | rewrite-native | unknown | native:native-source | `crowdagger__crowbook` | substantive Python (472 lines, 8 funcs) implementing a unknown tool |
| 84 | 25-49 | 30.9 | 307/995 | rewrite-native | unknown | native:native-source | `canop__rhit` | substantive Python (1087 lines, 47 funcs) implementing a unknown tool |
| 85 | 25-49 | 30.7 | 279/908 | rewrite-native | unknown | native:native-source | `cmatsuoka__figlet` | substantive Python (266 lines, 4 funcs) implementing a unknown tool |
| 86 | 25-49 | 29.7 | 297/999 | rewrite-native | unknown | native:native-source | `noborus__trdsql` | substantive Python (481 lines, 12 funcs) implementing a unknown tool |
| 87 | 25-49 | 29.2 | 290/992 | rewrite-native | rust | native:rust | `ogham__dog` | substantive Python (619 lines, 11 funcs) implementing a rust tool |
| 88 | 25-49 | 29.2 | 313/1072 | rewrite-native | unknown | native:native-source | `eudoxia0__hashcards` | substantive Python (281 lines, 8 funcs) implementing a unknown tool |
| 89 | 25-49 | 29.2 | 154/528 | rewrite-native | unknown | native:native-source | `kisielk__errcheck` | substantive Python (182 lines, 3 funcs) implementing a unknown tool |
| 90 | 25-49 | 28.9 | 437/1513 | rewrite-native | unknown | native:native-source | `alexpovel__srgn` | substantive Python (480 lines, 18 funcs) implementing a unknown tool |
| 91 | 25-49 | 28.8 | 285/989 | rewrite-native | unknown | native:native-source | `danmar__cppcheck` | substantive Python (196 lines, 1 funcs) implementing a unknown tool |
| 92 | 25-49 | 28.7 | 151/526 | rewrite-native | unknown | native:native-source | `ip7z__7zip` | substantive Python (291 lines, 5 funcs) implementing a unknown tool |
| 93 | 25-49 | 28.6 | 263/918 | rewrite-native | go | native:go | `dundee__gdu` | substantive Python (265 lines, 3 funcs) implementing a go tool |
| 94 | 25-49 | 28.6 | 105/367 | rewrite-native | unknown | native:native-source | `wfxr__code-minimap` | substantive Python (338 lines, 7 funcs) implementing a unknown tool |
| 95 | 25-49 | 28.3 | 171/605 | rewrite-native | unknown | native:native-source | `universal-ctags__ctags` | substantive Python (383 lines, 5 funcs) implementing a unknown tool |
| 96 | 25-49 | 28.2 | 267/948 | rewrite-native | unknown | native:native-source | `oppiliappan__statix` | substantive Python (212 lines, 7 funcs) implementing a unknown tool |
| 97 | 25-49 | 28.1 | 183/651 | rewrite-native | unknown | native:native-source | `dandavison__delta` | substantive Python (457 lines, 3 funcs) implementing a unknown tool |
| 98 | 25-49 | 27.9 | 271/972 | rewrite-native | unknown | native:native-source | `axodotdev__oranda` | substantive Python (502 lines, 11 funcs) implementing a unknown tool |
| 99 | 25-49 | 27.7 | 184/664 | rewrite-native | unknown | native:native-source | `tomarrell__wrapcheck` | substantive Python (167 lines, 6 funcs) implementing a unknown tool |
| 100 | 25-49 | 27.2 | 440/1620 | rewrite-native | unknown | native:native-source | `jonas__tig` | substantive Python (112 lines, 4 funcs) implementing a unknown tool |
| 101 | 25-49 | 27.1 | 247/912 | rewrite-native | unknown | native:native-source | `stranger6667__jsonschema` | substantive Python (432 lines, 6 funcs) implementing a unknown tool |
| 102 | 25-49 | 27.0 | 161/597 | rewrite-native | unknown | native:native-source | `mgechev__revive` | substantive Python (102 lines, 1 funcs) implementing a unknown tool |
| 103 | 25-49 | 26.6 | 101/380 | rewrite-native | unknown | native:native-source | `kaushiksrini__parqeye` | substantive Python (92 lines, 5 funcs) implementing a unknown tool |
| 104 | 25-49 | 25.9 | 263/1017 | rewrite-native | unknown | native:native-source | `epistates__treemd` | substantive Python (1087 lines, 47 funcs) implementing a unknown tool |
| 105 | 25-49 | 25.7 | 88/342 | rewrite-native | unknown | native:native-source | `yassinebridi__serpl` | substantive Python (182 lines, 8 funcs) implementing a unknown tool |
| 106 | 25-49 | 25.6 | 50/195 | rewrite-native | unknown | native:native-source | `elkowar__pipr` | substantive Python (1087 lines, 47 funcs) implementing a unknown tool |
| 107 | 25-49 | 25.5 | 139/545 | rewrite-native | unknown | native:native-source | `xampprocky__tokei` | substantive Python (279 lines, 4 funcs) implementing a unknown tool |
| 108 | 25-49 | 25.0 | 177/708 | rewrite-native | unknown | native:native-source | `astro__deadnix` | substantive Python (238 lines, 7 funcs) implementing a unknown tool |
| 109 | 0-24 | 24.7 | 137/554 | rewrite-native | unknown | native:native-source | `filosottile__age` | substantive Python (577 lines, 24 funcs) implementing a unknown tool |
| 110 | 0-24 | 24.4 | 178/731 | rewrite-native | unknown | native:native-source | `git-bahn__git-graph` | substantive Python (1087 lines, 47 funcs) implementing a unknown tool |
| 111 | 0-24 | 23.3 | 226/971 | rewrite-native | unknown | native:native-source | `rust-ethereum__ethabi` | substantive Python (591 lines, 29 funcs) implementing a unknown tool |
| 112 | 0-24 | 22.9 | 187/818 | rewrite-native | unknown | native:native-source | `rochacbruno__marmite` | substantive Python (287 lines, 4 funcs) implementing a unknown tool |
| 113 | 0-24 | 20.7 | 145/700 | rewrite-native | unknown | native:native-source | `samtools__samtools` | substantive Python (48 lines, 2 funcs) implementing a unknown tool |
| 114 | 0-24 | 20.6 | 123/597 | rewrite-native | unknown | native:native-source | `quinn-rs__quinn` | substantive Python (1087 lines, 47 funcs) implementing a unknown tool |
| 115 | 0-24 | 20.4 | 127/624 | rewrite-native | unknown | native:native-source | `direnv__direnv` | substantive Python (213 lines, 15 funcs) implementing a unknown tool |
| 116 | 0-24 | 20.3 | 283/1392 | rewrite-native | unknown | native:native-source | `hairyhenderson__gomplate` | substantive Python (542 lines, 13 funcs) implementing a unknown tool |
| 117 | 0-24 | 20.2 | 353/1748 | rewrite-native | unknown | native:native-source | `johnkerl__miller` | substantive Python (497 lines, 10 funcs) implementing a unknown tool |
| 118 | 0-24 | 19.5 | 139/711 | rewrite-native | rust | native:rust | `cslarsen__jp2a` | substantive Python (1087 lines, 47 funcs) implementing a rust tool |
| 119 | 0-24 | 19.3 | 86/446 | rewrite-native | unknown | native:native-source | `unhappychoice__gittype` | substantive Python (329 lines, 12 funcs) implementing a unknown tool |
| 120 | 0-24 | 18.4 | 83/450 | rewrite-native | unknown | native:native-source | `mibk__dupl` | substantive Python (300 lines, 10 funcs) implementing a unknown tool |
| 121 | 0-24 | 18.3 | 124/678 | scaffold-stub | unknown | native:native-source | `o2sh__onefetch` | scaffold main.py with no bundled binary - low yield, needs native rewrite |
| 122 | 0-24 | 18.3 | 205/1122 | rewrite-native | unknown | native:native-source | `luajit__luajit` | substantive Python (77 lines, 1 funcs) implementing a unknown tool |
| 123 | 0-24 | 18.1 | 76/419 | scaffold-stub | unknown | native:native-source | `hooklift__gowsdl` | scaffold main.py with no bundled binary - low yield, needs native rewrite |
| 124 | 0-24 | 17.2 | 63/366 | rewrite-native | unknown | native:native-source | `ekzhang__bore` | substantive Python (416 lines, 6 funcs) implementing a unknown tool |
| 125 | 0-24 | 17.2 | 180/1048 | rewrite-native | unknown | native:native-source | `naggie__dstask` | substantive Python (286 lines, 19 funcs) implementing a unknown tool |
| 126 | 0-24 | 17.2 | 110/641 | rewrite-native | unknown | native:native-source | `cweill__gotests` | substantive Python (229 lines, 5 funcs) implementing a unknown tool |
| 127 | 0-24 | 16.7 | 122/730 | rewrite-native | unknown | native:native-source | `go-critic__go-critic` | substantive Python (246 lines, 7 funcs) implementing a unknown tool |
| 128 | 0-24 | 16.4 | 131/800 | rewrite-native | unknown | native:native-source | `yoav-lavi__melody` | substantive Python (45 lines, 1 funcs) implementing a unknown tool |
| 129 | 0-24 | 16.4 | 113/691 | rewrite-native | unknown | native:native-source | `kyoheiu__felix` | substantive Python (249 lines, 4 funcs) implementing a unknown tool |
| 130 | 0-24 | 16.0 | 112/700 | rewrite-native | unknown | native:native-source | `htop-dev__htop` | substantive Python (215 lines, 2 funcs) implementing a unknown tool |
| 131 | 0-24 | 15.3 | 94/614 | rewrite-native | unknown | native:native-source | `lymphatus__caesium-clt` | substantive Python (228 lines, 5 funcs) implementing a unknown tool |
| 132 | 0-24 | 15.0 | 46/306 | rewrite-native | unknown | native:native-source | `cheat__cheat` | substantive Python (320 lines, 11 funcs) implementing a unknown tool |
| 133 | 0-24 | 14.7 | 58/395 | rewrite-native | unknown | native:native-source | `simeg__eureka` | substantive Python (122 lines, 9 funcs) implementing a unknown tool |
| 134 | 0-24 | 14.6 | 107/734 | rewrite-native | unknown | native:native-source | `ismaelgv__rnr` | substantive Python (548 lines, 11 funcs) implementing a unknown tool |
| 135 | 0-24 | 14.4 | 66/458 | scaffold-stub | unknown | native:native-source | `eliukblau__pixterm` | scaffold main.py with no bundled binary - low yield, needs native rewrite |
| 136 | 0-24 | 14.1 | 119/846 | rewrite-native | unknown | native:native-source | `shashwatah__jot` | substantive Python (204 lines, 5 funcs) implementing a unknown tool |
| 137 | 0-24 | 14.0 | 35/250 | rewrite-native | unknown | native:native-source | `doxygen__doxygen` | substantive Python (48 lines, 2 funcs) implementing a unknown tool |
| 138 | 0-24 | 13.7 | 58/423 | rewrite-native | rust | native:rust | `ecumene__rust-sloth` | substantive Python (221 lines, 4 funcs) implementing a rust tool |
| 139 | 0-24 | 13.5 | 90/666 | rewrite-native | unknown | native:native-source | `sigoden__argc` | substantive Python (295 lines, 9 funcs) implementing a unknown tool |
| 140 | 0-24 | 12.6 | 59/470 | rewrite-native | unknown | native:native-source | `thezoraiz__ascii-image-converter` | substantive Python (243 lines, 3 funcs) implementing a unknown tool |
| 141 | 0-24 | 12.1 | 68/564 | rewrite-native | unknown | native:native-source | `drew-alleman__datasurgeon` | substantive Python (377 lines, 8 funcs) implementing a unknown tool |
| 142 | 0-24 | 11.4 | 107/939 | rewrite-native | unknown | native:native-source | `hush-shell__hush` | substantive Python (153 lines, 3 funcs) implementing a unknown tool |
| 143 | 0-24 | 11.4 | 117/1027 | rewrite-native | c | native:c | `lua__lua` | substantive Python (48 lines, 2 funcs) implementing a c tool |
| 144 | 0-24 | 11.3 | 191/1693 | rewrite-native | unknown | native:native-source | `facebook__zstd` | substantive Python (293 lines, 5 funcs) implementing a unknown tool |
| 145 | 0-24 | 10.8 | 30/277 | rewrite-native | unknown | native:native-source | `wintermute-cell__ngrrram` | substantive Python (305 lines, 8 funcs) implementing a unknown tool |
| 146 | 0-24 | 10.6 | 74/699 | rewrite-native | unknown | native:native-source | `osgeo__gdal` | substantive Python (48 lines, 2 funcs) implementing a unknown tool |
| 147 | 0-24 | 10.4 | 36/347 | rewrite-native | unknown | native:native-source | `blake3-team__blake3` | substantive Python (474 lines, 9 funcs) implementing a unknown tool |
| 148 | 0-24 | 10.2 | 68/664 | rewrite-native | unknown | native:native-source | `ffmpeg__ffmpeg` | substantive Python (48 lines, 2 funcs) implementing a unknown tool |
| 149 | 0-24 | 10.2 | 22/215 | rewrite-native | unknown | native:native-source | `xorg62__tty-clock` | substantive Python (343 lines, 8 funcs) implementing a unknown tool |
| 150 | 0-24 | 9.3 | 36/387 | rewrite-native | unknown | native:native-source | `halitechallenge__halite` | substantive Python (319 lines, 7 funcs) implementing a unknown tool |
| 151 | 0-24 | 9.3 | 32/344 | scaffold-stub | unknown | native:native-source | `pls-rs__pls` | scaffold main.py with no bundled binary - low yield, needs native rewrite |
| 152 | 0-24 | 9.3 | 67/722 | rewrite-native | unknown | native:native-source | `esubaalew__run` | substantive Python (248 lines, 5 funcs) implementing a unknown tool |
| 153 | 0-24 | 9.1 | 60/660 | rewrite-native | unknown | native:native-source | `jhspetersson__fselect` | substantive Python (451 lines, 10 funcs) implementing a unknown tool |
| 154 | 0-24 | 8.2 | 89/1081 | rewrite-native | go | native:go | `peco__peco` | substantive Python (261 lines, 3 funcs) implementing a go tool |
| 155 | 0-24 | 8.2 | 42/514 | rewrite-native | unknown | native:native-source | `google__brotli` | substantive Python (48 lines, 2 funcs) implementing a unknown tool |
| 156 | 0-24 | 7.3 | 51/700 | rewrite-native | rust | native:rust | `rcoh__angle-grinder` | substantive Python (67 lines, 2 funcs) implementing a rust tool |
| 157 | 0-24 | 6.2 | 37/594 | rewrite-native | unknown | native:native-source | `incu6us__goimports-reviser` | substantive Python (278 lines, 7 funcs) implementing a unknown tool |
| 158 | 0-24 | 4.6 | 30/654 | rewrite-native | rust | native:rust | `sharkdp__bat` | substantive Python (305 lines, 3 funcs) implementing a rust tool |
| 159 | 0-24 | 4.4 | 27/608 | scaffold-stub | unknown | native:native-source | `zk-org__zk` | scaffold main.py with no bundled binary - low yield, needs native rewrite |
| 160 | 0-24 | 2.1 | 27/1293 | rewrite-native | unknown | native:native-source | `php__php-src` | substantive Python (48 lines, 2 funcs) implementing a unknown tool |
| 161 | 0-24 | 2.0 | 14/688 | rewrite-native | rust | native:rust | `nukesor__pueue` | substantive Python (230 lines, 8 funcs) implementing a rust tool |
| 162 | 0-24 | 1.7 | 4/230 | rewrite-native | unknown | native:native-source | `svenstaro__genact` | substantive Python (223 lines, 3 funcs) implementing a unknown tool |
| 163 | 0-24 | 1.2 | 4/340 | scaffold-stub | unknown | native:native-source | `gromacs__gromacs` | scaffold main.py with no bundled binary - low yield, needs native rewrite |
| 164 | 0-24 | 1.1 | 4/350 | scaffold-stub | unknown | native:native-source | `tstack__lnav` | scaffold main.py with no bundled binary - low yield, needs native rewrite |
| 165 | 0-24 | 1.0 | 6/606 | scaffold-stub | c | native:c | `chirlu__sox` | scaffold main.py with no bundled binary - low yield, needs native rewrite |
| 166 | 0-24 | 0.9 | 4/431 | scaffold-stub | rust | native:rust | `ivanceras__svgbob` | scaffold main.py with no bundled binary - low yield, needs native rewrite |
| 167 | 0-24 | 0.7 | 3/427 | scaffold-stub | rust | native:rust | `stathissideris__ditaa` | scaffold main.py with no bundled binary - low yield, needs native rewrite |
| 168 | 0-24 | 0.5 | 3/593 | rewrite-native | unknown | native:native-source | `osgeo__proj` | substantive Python (18 lines, 1 funcs) implementing a unknown tool |
| 169 | 0-24 | 0.3 | 1/349 | rewrite-native | unknown | native:native-source | `boyter__scc` | substantive Python (372 lines, 2 funcs) implementing a unknown tool |
| 170 | 0-24 | 0.2 | 1/604 | rewrite-native | unknown | native:native-source | `jgm__pandoc` | substantive Python (39 lines, 1 funcs) implementing a unknown tool |
| 171 | 0 | 0.0 | 0/350 | scaffold-stub | c | native:c | `bellard__quickjs` | scaffold main.py with no bundled binary - low yield, needs native rewrite |
| 172 | 50-69 | 69.7 | 235/337 | already-native | go | native:go | `psampaz__go-mod-outdated` | native go source already present (3 files) |
| 173 | 50-69 | 61.2 | 742/1212 | already-native | go | native:go | `junegunn__fzf` | native go source already present (53 files) |
| 174 | 50-69 | 60.1 | 471/784 | already-native | go | native:go | `antonmedv__walk` | native go source already present (11 files) |
| 175 | 25-49 | 43.9 | 244/556 | already-native | go | native:go | `mfridman__tparse` | native go source already present (14 files) |
| 176 | 25-49 | 41.5 | 315/759 | already-native | go | native:go | `jesseduffield__lazygit` | native go source already present (2165 files) |
| 177 | 25-49 | 38.6 | 601/1558 | already-native | go | native:go | `antonmedv__fx` | native go source already present (44 files) |
| 178 | 0-24 | 14.1 | 62/440 | investigate | unknown | investigate | `lh3__seqtk` | no main.py present and no native source detected |
| 179 | 0-24 | 13.3 | 81/607 | investigate | unknown | investigate | `y2z__monolith` | no main.py present and no native source detected |
| 180 | 70-89 | 70.9 | 683/963 | keep-python | python | source:python | `oppiliappan__eva` | tool's upstream is itself Python |
| 181 | 70-89 | 70.8 | 552/780 | keep-python | python | source:python | `dalance__amber` | tool's upstream is itself Python |
| 182 | 25-49 | 46.6 | 555/1191 | unknown | create override | missing-override | `ggreer__the_silver_searcher` | board row has no override directory audited |
| 183 | 0-24 | 22.7 | 285/1256 | unknown | create override | missing-override | `paradigmxyz__solar` | board row has no override directory audited |
| 184 | 0 | 0.0 | 0/0 | unknown | create override | missing-override | `alecthomas__chroma` | board row has no override directory audited |
| 185 | 0 | 0.0 | 0/0 | unknown | create override | missing-override | `kyoh86__richgo.313114f;c` | board row has no override directory audited |
| 186 | 0 | 0.0 | 0/0 | unknown | create override | missing-override | `noborus__ov` | board row has no override directory audited |
| 187 | 0 | 0.0 | 0/0 | unknown | create override | missing-override | `rhysd__kiro-editor` | board row has no override directory audited |
| 188 | 0 | 0.0 | 0/0 | unknown | create override | missing-override | `tukaani-project__xz` | board row has no override directory audited |
| 189 | 0 | 0.0 | 0/0 | unknown | create override | missing-override | `ys-l__flamelens` | board row has no override directory audited |
| 190 | 100 | 100.0 | 2536/2536 | locked | done | locked | `burntsushi__ripgrep` | board row has no override directory audited |
| 191 | 100 | 100.0 | 2056/2056 | locked | done | locked | `mgdm__htmlq` | board row has no override directory audited |
| 192 | 100 | 100.0 | 1455/1455 | locked | done | locked | `pemistahl__grex` | board row has no override directory audited |
| 193 | 100 | 100.0 | 1292/1292 | locked | done | locked | `anordal__shellharden` | board row has no override directory audited |
| 194 | 100 | 100.0 | 937/937 | locked | done | locked | `sirwart__ripsecrets` | board row has no override directory audited |
| 195 | 100 | 100.0 | 876/876 | locked | done | locked | `sibprogrammer__xq` | board row has no override directory audited |
| 196 | 100 | 100.0 | 665/665 | locked | done | locked | `abishekvashok__cmatrix` | board row has no override directory audited |
| 197 | 100 | 100.0 | 657/657 | locked | done | locked | `mikefarah__yq` | board row has no override directory audited |
| 198 | 100 | 100.0 | 628/628 | locked | done | locked | `orf__gping` | board row has no override directory audited |
| 199 | 100 | 100.0 | 577/577 | locked | done | locked | `ajeetdsouza__zoxide` | board row has no override directory audited |
| 200 | 100 | 100.0 | 347/347 | locked | done | locked | `wfxr__csview` | board row has no override directory audited |
| 201 | 100 | 100.0 | 233/233 | locked | done | locked | `tomnomnom__gron` | board row has no override directory audited |
