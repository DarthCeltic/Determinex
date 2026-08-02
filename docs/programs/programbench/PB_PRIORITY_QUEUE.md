# ProgramBench Priority Queue

**Generated:** 2026-06-26
**Source:** `corpus/programbench/eval_index.json`

Priority order: P1 (T2-cert) → P2 (verify+lock) → P3-P6 (fix failures) → P7 (rebaseline) → P8-P10 (hard/impossible)

⚠ = best_known_passed > official_passed (regression detected)

## Summary

| Bucket | Count |
|--------|-------|
| T1 strict_lock (done) | 66 |
| T2 ceiling_cert (done) | 16 |
| Active (needs work) | 118 |
| Regressions flagged | 0 |

## Ranked Queue

| # | Priority | Tool | Score | f | nr | sk | Next Action | Reg? |
|---|----------|------|-------|---|----|----|-------------|------|
| 1 | P1 T2-cert | `wfxr__csview.8ac4de0` | 347/348 (99.7%) | 0 | 0 | 1 | Write CEILING_CERT.md (1 sk) → T2 |  |
| 2 | P1 T2-cert | `parqeye` | 1126/1128 (99.8%) | 0 | 0 | 2 | Write CEILING_CERT.md (2 sk) → T2 |  |
| 3 | P1 T2-cert | `cheat__cheat.b8098dc` | 612/614 (99.7%) | 0 | 0 | 2 | Write CEILING_CERT.md (2 sk) → T2 |  |
| 4 | P1 T2-cert | `lymphatus__caesium-clt` | 1238/1240 (99.8%) | 0 | 0 | 2 | Write CEILING_CERT.md (2 sk) → T2 |  |
| 5 | P1 T2-cert | `cslarsen__jp2a.61d205f` | 1438/1442 (99.7%) | 0 | 0 | 4 | Write CEILING_CERT.md (4 sk) → T2 |  |
| 6 | P1 T2-cert | `tuc` | 2490/2498 (99.7%) | 0 | 0 | 8 | Write CEILING_CERT.md (8 sk) → T2 |  |
| 7 | P1 T2-cert | `codesnap-rs__codesnap` | 1698/1706 (99.5%) | 0 | 0 | 8 | Write CEILING_CERT.md (8 sk) → T2 |  |
| 8 | P2 verify+lock | `rust-embedded__svd2rust.1760b5e` | 1970/1970 (100.0%) | 0 | 0 | 0 | ⚠PHANTOM(unresolved) — Section 5 raw parse required |  |
| 9 | P2 verify+lock | `yj` | 1457/1457 (100.0%) | 0 | 0 | 0 | ⚠PHANTOM(unresolved) — Section 5 raw parse required |  |
| 10 | P2 verify+lock | `rs__jplot.2a54bcc` | 2157/2157 (100.0%) | 0 | 0 | 0 | ⚠PHANTOM(submetric) — bidir conftest must clear before lock |  |
| 11 | P3 f≤3 | `yoav-lavi__melody` | 2884/2886 (99.9%) | 2 | 0 | 0 | Fix 2 failures → T1 lock |  |
| 12 | P3 f≤3 | `run` | 2700/3026 (89.2%) | 2 | 0 | 324 | Fix 2 failures → T2 cert (sk>0 blocks T1) |  |
| 13 | P4 f≤10 | `tree-sitter__tree-sitter` | 3290/3380 (97.3%) | 4 | 0 | 86 | Fix 4 failures (0.1% fail) → T2 cert (sk>0 blocks T1) |  |
| 14 | P4 f≤10 | `lua__lua` | 2772/2778 (99.8%) | 6 | 0 | 0 | Fix 6 failures (0.2% fail) → T1 lock |  |
| 15 | P4 f≤10 | `axodotdev__oranda` | 1958/1970 (99.4%) | 10 | 0 | 2 | Fix 10 failures (0.5% fail) → T2 cert (sk>0 blocks T1) |  |
| 16 | P5 f≤30 | `pls-rs__pls` | 668/694 (96.3%) | 14 | 0 | 12 | Fix 14 failures (2.0% fail) → near T2 cert (sk>0 blocks T1) |  |
| 17 | P5 f≤30 | `ov` | 4880/4894 (99.7%) | 14 | 0 | 0 | Fix 14 failures (0.3% fail) → near T1 lock |  |
| 18 | P5 f≤30 | `xorg62__tty-clock` | 622/638 (97.5%) | 16 | 0 | 0 | Fix 16 failures (2.5% fail) → near T1 lock |  |
| 19 | P5 f≤30 | `naggie__dstask` | 3164/3190 (99.2%) | 18 | 0 | 8 | Fix 18 failures (0.6% fail) → near T2 cert (sk>0 blocks T1) |  |
| 20 | P5 f≤30 | `rust-lang__mdbook` | 3564/3597 (99.1%) | 21 | 0 | 12 | Fix 21 failures (0.6% fail) → near T2 cert (sk>0 blocks T1) |  |
| 21 | P5 f≤30 | `antonmedv__walk` | 1528/1550 (98.6%) | 22 | 0 | 0 | Fix 22 failures (1.4% fail) → near T1 lock |  |
| 22 | P6 f≤100 | `dandavison__delta` | 2317/2375 (97.6%) | 58 | 0 | 0 | Fix 58 failures (2.4% fail) — significant work |  |
| 23 | P6 f≤100 | `dundee__gdu` | 3026/3093 (97.8%) | 67 | 0 | 0 | Fix 67 failures (2.2% fail) — significant work |  |
| 24 | P6 f≤100 | `go-critic__go-critic` | 1718/1816 (94.6%) | 68 | 0 | 30 | Fix 68 failures (3.7% fail) — significant work |  |
| 25 | P6 f≤100 | `facebook__zstd` | 4518/4644 (97.3%) | 94 | 0 | 32 | Fix 94 failures (2.0% fail) — significant work |  |
| 26 | P6 f≤100 | `sayanarijit__xplr` | 1778/1878 (94.7%) | 100 | 0 | 0 | Fix 100 failures (5.3% fail) — significant work |  |
| 27 | P7 f>100 | `tarka__xcp` | 4036/4180 (96.6%) | 8 | 0 | 40 | Fix 104 failures (2.5% fail) — significant work |  |
| 28 | P7 f>100 | `yassinebridi__serpl` | 966/1084 (89.1%) | 116 | 0 | 2 | Fix 116 failures (10.7% fail) — significant work |  |
| 29 | P7 f>100 | `luajit__luajit` | 6254/6376 (98.1%) | 120 | 0 | 2 | Fix 120 failures (1.9% fail) — significant work |  |
| 30 | P7 f>100 | `skeema__skeema` | 6099/6923 (88.1%) | 132 | 0 | 692 | Fix 132 failures (1.9% fail) — significant work |  |
| 31 | P7 f>100 | `jhspetersson__fselect` | 5318/5592 (95.1%) | 139 | 0 | 135 | Fix 139 failures (2.5% fail) — significant work |  |
| 32 | P7 f>100 | `jarun__nnn` | 3446/3602 (95.7%) | 156 | 0 | 0 | Fix 156 failures (4.3% fail) — significant work |  |
| 33 | P7 f>100 | `monolith` | 1366/1554 (87.9%) | 188 | 0 | 0 | Fix 188 failures (12.1% fail) — significant work |  |
| 34 | P7 f>100 | `ducaale__xh` | 2302/2532 (90.9%) | 228 | 0 | 2 | Fix 228 failures (9.0% fail) — significant work |  |
| 35 | P7 f>100 | `peco__peco` | 3200/3436 (93.1%) | 230 | 0 | 6 | Fix 230 failures (6.7% fail) — significant work |  |
| 36 | P7 f>100 | `ninja-build__ninja` | 3560/3810 (93.4%) | 248 | 0 | 2 | Fix 248 failures (6.5% fail) — significant work |  |
| 37 | P7 f>100 | `zk-org__zk` | 2578/2952 (87.3%) | 294 | 0 | 80 | Fix 294 failures (10.0% fail) — significant work |  |
| 38 | P7 f>100 | `zevv__duc` | 2042/2496 (81.8%) | 424 | 0 | 30 | Fix 424 failures (17.0% fail) — significant work |  |
| 39 | P7 f>100 | `bootandy__dust` | 1392/1930 (72.1%) | 530 | 0 | 8 | Fix 530 failures (27.5% fail) — significant work |  |
| 40 | P7 f>100 | `xampprocky__tokei` | 948/1527 (62.1%) | 572 | 0 | 6 | Fix 573 failures (37.5% fail) — significant work |  |
| 41 | P7 f>100 | `ggreer__the_silver_searcher` | 555/1192 (46.6%) | 0 | 0 | 0 | Fix 637 failures (53.4% fail) — significant work |  |
| 42 | P7 f>100 | `shashwatah__jot` | 119/846 (14.1%) | 0 | 0 | 0 | Fix 727 failures (85.9% fail) — significant work |  |
| 43 | P7 f>100 | `hairyhenderson__gomplate` | 5270/7084 (74.4%) | 1772 | 0 | 42 | Fix 1772 failures (25.0% fail) — significant work |  |
| 44 | P7 f>100 | `gromacs__gromacs` | 40/2764 (1.4%) | 2666 | 0 | 58 | Fix 2666 failures (96.5% fail) — significant work |  |
| 45 | P7 rebaseline | `xq` | 1734/1752 (99.0%) | 9 | 3 | 6 | Remove collection cap + Hetzner eval (3 not_run) |  |
| 46 | P7 rebaseline | `git-bahn__git-graph` | 1322/1399 (94.5%) | 70 | 3 | 4 | Remove collection cap + Hetzner eval (3 not_run) |  |
| 47 | P7 rebaseline | `oha` | 2172/2189 (99.2%) | 5 | 4 | 8 | Remove collection cap + Hetzner eval (4 not_run) |  |
| 48 | P7 rebaseline | `nachoparker__dutree` | 1144/1920 (59.6%) | 692 | 4 | 20 | Remove collection cap + Hetzner eval (4 not_run) |  |
| 49 | P7 rebaseline | `tomarrell__wrapcheck` | 184/677 (27.2%) | 0 | 8 | 0 | Remove collection cap + Hetzner eval (8 not_run) |  |
| 50 | P7 rebaseline | `blacknon__hwatch` | 2588/2614 (99.0%) | 16 | 10 | 0 | Remove collection cap + Hetzner eval (10 not_run) |  |
| 51 | P7 rebaseline | `hush-shell__hush` | 2574/2591 (99.3%) | 2 | 15 | 0 | Remove collection cap + Hetzner eval (15 not_run) |  |
| 52 | P7 rebaseline | `rust-ethereum__ethabi` | 2060/2089 (98.6%) | 0 | 27 | 2 | Remove collection cap + Hetzner eval (27 not_run) |  |
| 53 | P7 rebaseline | `astaxie__bat` | 2460/2573 (95.6%) | 57 | 30 | 26 | Remove collection cap + Hetzner eval (30 not_run) |  |
| 54 | P7 rebaseline | `sharkdp__bat` | 2460/2573 (95.6%) | 57 | 30 | 26 | Remove collection cap + Hetzner eval (30 not_run) |  |
| 55 | P7 rebaseline | `antonmedv__fx` | 5990/6399 (93.6%) | 324 | 77 | 8 | Remove collection cap + Hetzner eval (77 not_run) |  |
| 56 | P7 rebaseline | `drew-alleman__datasurgeon` | 68/664 (10.2%) | 0 | 100 | 0 | Remove collection cap + Hetzner eval (100 not_run) |  |
| 57 | P7 rebaseline | `rochacbruno__marmite` | 1501/1645 (91.2%) | 35 | 106 | 3 | Remove collection cap + Hetzner eval (106 not_run) |  |
| 58 | P7 rebaseline | `canop__broot` | 1005/1152 (87.2%) | 17 | 130 | 0 | Remove collection cap + Hetzner eval (130 not_run) |  |
| 59 | P7 rebaseline | `ecumene__rust-sloth` | 58/578 (10.0%) | 0 | 151 | 0 | Remove collection cap + Hetzner eval (151 not_run) |  |
| 60 | P7 rebaseline | `mkj__dropbear` | 494/1300 (38.0%) | 356 | 295 | 12 | Remove collection cap + Hetzner eval (295 not_run) |  |
| 61 | P7 rebaseline | `segmentio__chamber` | 4124/4486 (91.9%) | 53 | 297 | 12 | Remove collection cap + Hetzner eval (297 not_run) |  |
| 62 | P7 rebaseline | `unhappychoice__gittype` | 1010/1322 (76.4%) | 2 | 306 | 4 | Remove collection cap + Hetzner eval (306 not_run) |  |
| 63 | P7 rebaseline | `osgeo__gdal` | 74/1023 (7.2%) | 0 | 323 | 0 | Remove collection cap + Hetzner eval (323 not_run) |  |
| 64 | P7 rebaseline | `jesseduffield__lazygit` | 1298/1824 (71.2%) | 85 | 429 | 12 | Remove collection cap + Hetzner eval (429 not_run) |  |
| 65 | P7 rebaseline | `o2sh__onefetch` | 1454/1936 (75.1%) | 2 | 478 | 2 | Remove collection cap + Hetzner eval (478 not_run) |  |
| 66 | P7 rebaseline | `ip7z__7zip` | 1050/1591 (66.0%) | 51 | 490 | 0 | Remove collection cap + Hetzner eval (490 not_run) |  |
| 67 | P7 rebaseline | `lfos__calcurse` | 470/1488 (31.6%) | 0 | 604 | 0 | Remove collection cap + Hetzner eval (604 not_run) |  |
| 68 | P7 rebaseline | `tstack__lnav` | 694/1352 (51.3%) | 3 | 655 | 0 | Remove collection cap + Hetzner eval (655 not_run) |  |
| 69 | P7 rebaseline | `arq5x__bedtools2` | 796/1462 (54.4%) | 0 | 662 | 4 | Remove collection cap + Hetzner eval (662 not_run) |  |
| 70 | P7 rebaseline | `tinycc__tinycc` | 1148/2341 (49.0%) | 0 | 742 | 0 | Remove collection cap + Hetzner eval (742 not_run) |  |
| 71 | P7 rebaseline | `samtools__samtools` | 1598/2369 (67.5%) | 1 | 770 | 0 | Remove collection cap + Hetzner eval (770 not_run) |  |
| 72 | P7 rebaseline | `ammarabouzor__tui-journal` | 518/2265 (22.9%) | 0 | 772 | 0 | Remove collection cap + Hetzner eval (772 not_run) |  |
| 73 | P7 rebaseline | `stacked-git__stgit` | 491/2380 (20.6%) | 0 | 810 | 0 | Remove collection cap + Hetzner eval (810 not_run) |  |
| 74 | P7 rebaseline | `ogham__dog` | 290/1813 (16.0%) | 0 | 818 | 0 | Remove collection cap + Hetzner eval (818 not_run) |  |
| 75 | P7 rebaseline | `epistates__treemd` | 1908/2819 (67.7%) | 0 | 905 | 6 | Remove collection cap + Hetzner eval (905 not_run) |  |
| 76 | P7 rebaseline | `paradigmxyz__solar` | 2698/3639 (74.1%) | 8 | 932 | 0 | Remove collection cap + Hetzner eval (932 not_run) |  |
| 77 | P7 rebaseline | `danmar__cppcheck` | 2074/3355 (61.8%) | 44 | 1171 | 66 | Remove collection cap + Hetzner eval (1171 not_run) |  |
| 78 | P7 rebaseline | `robertdavidgraham__masscan` | 599/3073 (19.5%) | 0 | 1855 | 0 | Remove collection cap + Hetzner eval (1855 not_run) |  |
| 79 | P7 rebaseline | `universal-ctags__ctags` | 171/2606 (6.6%) | 0 | 1974 | 0 | Remove collection cap + Hetzner eval (1974 not_run) |  |
| 80 | P7 rebaseline | `johnkerl__miller` | 27444/29861 (91.9%) | 206 | 2207 | 4 | Remove collection cap + Hetzner eval (2207 not_run) |  |
| 81 | P7 rebaseline | `stranger6667__jsonschema` | 247/3373 (7.3%) | 0 | 2461 | 0 | Remove collection cap + Hetzner eval (2461 not_run) |  |
| 82 | P7 rebaseline | `parcel-bundler__lightningcss` | 510/3666 (13.9%) | 0 | 2768 | 0 | Remove collection cap + Hetzner eval (2768 not_run) |  |
| 83 | P7 rebaseline | `duckdb__duckdb` | 70/5988 (1.2%) | 0 | 5093 | 0 | Remove collection cap + Hetzner eval (5093 not_run) |  |
| 84 | P7 rebaseline | `sqlite__sqlite` | 520/17077 (3.0%) | 32 | 16525 | 0 | Remove collection cap + Hetzner eval (16525 not_run) |  |
| 85 | P7 rebaseline | `php__php-src` | 3176/22628 (14.0%) | 18 | 18385 | 0 | Remove collection cap + Hetzner eval (18385 not_run) |  |
| 86 | P8 behavioral | `ffmpeg__ffmpeg` | 228/4479 (5.1%) | 400 | 3851 | 0 | Deep behavioral analysis needed (400 failures — quarantined, no one-shot patches |  |
| 87 | P8 behavioral | `jgm__pandoc` | 2/5721 (0.0%) | 506 | 5213 | 0 | Deep behavioral analysis needed (506 failures — quarantined, no one-shot patches |  |
| 88 | P8 behavioral | `osgeo__proj` | 154/6027 (2.6%) | 616 | 5043 | 214 | Deep behavioral analysis needed (616 failures — quarantined, no one-shot patches |  |
| 89 | P8 behavioral | `halitechallenge__halite` | 18/782 (2.3%) | 756 | 0 | 8 | Deep behavioral analysis needed (756 failures — quarantined, no one-shot patches |  |
| 90 | P8 behavioral | `ast-grep__ast-grep` | 812/1790 (45.4%) | 978 | 0 | 0 | Deep behavioral analysis needed (978 failures — quarantined, no one-shot patches |  |
| 91 | P8 behavioral | `quinn-rs__quinn` | 94/1198 (7.8%) | 1100 | 0 | 4 | Deep behavioral analysis needed (1100 failures — quarantined, no one-shot patche |  |
| 92 | P8 behavioral | `nukesor__pueue` | 44/1266 (3.5%) | 728 | 43 | 16 | Deep behavioral analysis needed (1163 failures — quarantined, no one-shot patche |  |
| 93 | P8 behavioral | `ksxgithub__parallel-disk-usage` | 38/1260 (3.0%) | 1220 | 0 | 2 | Deep behavioral analysis needed (1220 failures — quarantined, no one-shot patche |  |
| 94 | P8 behavioral | `cweill__gotests` | 140/1512 (9.3%) | 1368 | 0 | 4 | Deep behavioral analysis needed (1368 failures — quarantined, no one-shot patche |  |
| 95 | P8 behavioral | `nikoladucak__caps-log` | 1038/2491 (41.7%) | 1400 | 3 | 50 | Deep behavioral analysis needed (1400 failures — quarantined, no one-shot patche |  |
| 96 | P8 behavioral | `rhysd__kiro-editor` | 62/1538 (4.0%) | 1468 | 8 | 0 | Deep behavioral analysis needed (1468 failures — quarantined, no one-shot patche |  |
| 97 | P8 behavioral | `typst__typst` | 1762/3573 (49.3%) | 1806 | 3 | 2 | Deep behavioral analysis needed (1806 failures — quarantined, no one-shot patche |  |
| 98 | P8 behavioral | `chirlu__sox` | 48/2520 (1.9%) | 2048 | 0 | 364 | Deep behavioral analysis needed (2108 failures — quarantined, no one-shot patche |  |
| 99 | P8 behavioral | `htop-dev__htop` | 188/2400 (7.8%) | 2212 | 0 | 0 | Deep behavioral analysis needed (2212 failures — quarantined, no one-shot patche |  |
| 100 | P8 behavioral | `lz4__lz4` | 224/3670 (6.1%) | 3442 | 0 | 4 | Deep behavioral analysis needed (3442 failures — quarantined, no one-shot patche |  |
| 101 | P8 behavioral | `jonas__tig` | 796/4526 (17.6%) | 3538 | 175 | 16 | Deep behavioral analysis needed (3539 failures — quarantined, no one-shot patche |  |
| 102 | P9 tui_wall | `nsh` | 4584/4588 (99.9%) | 4 | 0 | 0 | TUI behavioral (not code-patchable): 4 failures — tmux keyboard handling |  |
| 103 | P9 tui_wall | `hpjansson__chafa.dd4d4c1` | 5544/5552 (99.9%) | 8 | 0 | 0 | TUI behavioral (not code-patchable): 8 failures — tmux keyboard handling |  |
| 104 | P9 tui_wall | `elkowar__pipr` | 1636/1655 (98.9%) | 15 | 0 | 4 | TUI behavioral (not code-patchable): 15 failures — tmux keyboard handling |  |
| 105 | P9 tui_wall | `kyoheiu__felix` | 1886/1929 (97.8%) | 40 | 1 | 2 | Add tmux support → eval (1 not_run) |  |
| 106 | P9 tui_wall | `byron__dua-cli` | 1942/2004 (96.9%) | 54 | 0 | 8 | TUI behavioral (not code-patchable): 54 failures — tmux keyboard handling |  |
| 107 | P9 tui_wall | `gabotechs__dep-tree` | 2656/2758 (96.3%) | 98 | 0 | 4 | TUI behavioral (not code-patchable): 98 failures — tmux keyboard handling |  |
| 108 | P10 impossible | `kyoh86__richgo` | 1572/1610 (97.6%) | 0 | 36 | 2 | ⛔ IMPOSSIBLE — 36 tests.test_cli.*@go_test phantom IDs in tests.json never  |  |
| 109 | P10 impossible | `orf__gping` | 1096/1148 (95.5%) | 0 | 44 | 8 | ⛔ IMPOSSIBLE — 2 irreconcilable ping-missing ENXIO failures (gping doesn't  |  |
| 110 | P10 impossible | `rumdl` | 2614/5184 (50.4%) | 0 | 2512 | 58 | ⛔ IMPOSSIBLE — v2: 9286/9344 (99.4%). 29 upstream @pytest.mark.skip (gold-e |  |
| 111 | P10 impossible | `json-tui` | 1786/1788 (99.9%) | 2 | 0 | 0 | ⛔ IMPOSSIBLE — json_tui_v3 1786/1788: test_navigation_j_k_changes_highlight |  |
| 112 | P10 impossible | `doxygen__doxygen` | 510/514 (99.2%) | 2 | 0 | 2 | ⛔ IMPOSSIBLE — tests.json for 2 of 3 branches has duplicate test IDs with b |  |
| 113 | P10 impossible | `alexpovel__srgn` | 4144/4152 (99.8%) | 6 | 0 | 2 | ⛔ IMPOSSIBLE — PB fixture bug (ALL_CAPS input in rust_strings_upper branch) |  |
| 114 | P10 impossible | `johanneskaufmann__html-to-markdown` | 1956/1962 (99.7%) | 6 | 0 | 0 | ⛔ IMPOSSIBLE — Three branches assert conflicting --version strings ('2.3.4- |  |
| 115 | P10 impossible | `sharkdp__hexyl` | 1880/1914 (98.2%) | 6 | 28 | 0 | ⛔ IMPOSSIBLE — --panels=1 produces 8 bytes/row; tests asserting 1 row for 1 |  |
| 116 | P10 impossible | `sharkdp__fd` | 2524/2672 (94.5%) | 9 | 125 | 14 | ⛔ IMPOSSIBLE — Root user in container makes all files executable defeating  |  |
| 117 | P10 impossible | `rustowl` | 1442/1524 (94.6%) | 20 | 0 | 62 | ⛔ IMPOSSIBLE — 62 upstream skips + 20 real test failures (test_utils.* posi |  |
| 118 | P10 impossible | `dalance__amber` | 1402/1484 (94.5%) | 33 | 39 | 10 | ⛔ IMPOSSIBLE — Contradictory rc=0/rc=1 assertions between branches for iden |  |
| 119 | -- T1 locked | `angle-grinder` | 1143/1143 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 120 | -- T1 locked | `ascii-image-converter` | 488/488 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 121 | -- T1 locked | `bore` | 900/900 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 122 | -- T1 locked | `boyter__scc.515f91c` | 476/476 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 123 | -- T1 locked | `chmln__handlr` | 1812/1812 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 124 | -- T1 locked | `clog-cli` | 1556/1556 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 125 | -- T1 locked | `cmatrix` | 769/769 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 126 | -- T1 locked | `cmatsuoka__figlet` | 2088/2088 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 127 | -- T1 locked | `code-minimap` | 738/738 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 128 | -- T1 locked | `crowdagger__crowbook` | 1774/1774 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 129 | -- T1 locked | `curlie` | 1482/1482 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 130 | -- T1 locked | `deadnix` | 1418/1418 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 131 | -- T1 locked | `diffr` | 1524/1524 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 132 | -- T1 locked | `direnv__direnv` | 1946/1946 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 133 | -- T1 locked | `dsq` | 1532/1532 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 134 | -- T1 locked | `dupl` | 900/900 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 135 | -- T1 locked | `entr` | 1482/1482 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 136 | -- T1 locked | `errcheck` | 1064/1064 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 137 | -- T1 locked | `eureka` | 800/800 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 138 | -- T1 locked | `eva` | 963/963 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 139 | -- T1 locked | `fasttext` | 708/708 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 140 | -- T1 locked | `fblog` | 2254/2254 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 141 | -- T1 locked | `flamelens` | 622/622 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 142 | -- T1 locked | `genact` | 237/237 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 143 | -- T1 locked | `git-trim` | 1422/1422 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 144 | -- T1 locked | `go-mod-outdated` | 342/342 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 145 | -- T1 locked | `grex` | 3036/3036 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 146 | -- T1 locked | `gron` | 233/233 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 147 | -- T1 locked | `guumaster__hostctl` | 2750/2750 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 148 | -- T1 locked | `hck` | 1768/1768 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 149 | -- T1 locked | `hex` | 1754/1754 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 150 | -- T1 locked | `hooklift__gowsdl` | 846/846 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 151 | -- T1 locked | `hyperfine` | 298/298 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 152 | -- T1 locked | `i3-style` | 1500/1500 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 153 | -- T1 locked | `igrep` | 1408/1408 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 154 | -- T1 locked | `isona__dirble` | 2216/2216 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 155 | -- T1 locked | `ivanceras__svgbob` | 948/948 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 156 | -- T1 locked | `jq` | 6874/6874 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 157 | -- T1 locked | `junegunn__fzf.b56d614` | 4156/4156 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 158 | -- T1 locked | `loop` | 1556/1556 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 159 | -- T1 locked | `madler__pigz` | 1876/1876 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 160 | -- T1 locked | `mgechev__revive` | 1772/1772 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 161 | -- T1 locked | `miniserve` | 880/880 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 162 | -- T1 locked | `muffet` | 864/864 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 163 | -- T1 locked | `ngrrram` | 664/664 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 164 | -- T1 locked | `nomino` | 676/676 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 165 | -- T1 locked | `pastel` | 1256/1256 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 166 | -- T1 locked | `pier` | 1556/1556 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 167 | -- T1 locked | `rhit` | 2176/2176 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 168 | -- T1 locked | `ripsecrets` | 937/937 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 169 | -- T1 locked | `rnr` | 1480/1480 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 170 | -- T1 locked | `seqtk` | 880/880 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 171 | -- T1 locked | `shellharden` | 1292/1292 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 172 | -- T1 locked | `stathissideris__ditaa` | 681/681 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 173 | -- T1 locked | `tailspin` | 1570/1570 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 174 | -- T1 locked | `tex-fmt` | 990/990 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 175 | -- T1 locked | `thokr` | 507/507 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 176 | -- T1 locked | `tparse` | 1112/1112 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 177 | -- T1 locked | `trasta298__keifu.3331426` | 826/826 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 178 | -- T1 locked | `trdsql` | 2806/2806 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 179 | -- T1 locked | `xsv` | 2634/2634 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 180 | -- T1 locked | `yq` | 2046/2046 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 181 | -- T1 locked | `zoxide` | 577/577 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 182 | -- T1 locked | `eliukblau__pixterm` | 922/922 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 183 | -- T1 locked | `google__brotli` | 1212/1212 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 184 | -- T1 locked | `ariga__atlas` | 3476/3476 (100.0%) | 0 | 0 | 0 | ✓ T1 LOCKED |  |
| 185 | -- T2 cert'd | `ripgrep` | 2536/2538 (99.9%) | 0 | 0 | 2 | ✓ T2 CEILING CERT |  |
| 186 | -- T2 cert'd | `bellard__quickjs.d7ae12a` | 6076/6088 (99.8%) | 0 | 0 | 12 | ✓ T2 CEILING CERT |  |
| 187 | -- T2 cert'd | `chmln__sd.87d1ba5` | 1728/1738 (99.4%) | 0 | 0 | 10 | ✓ T2 CEILING CERT |  |
| 188 | -- T2 cert'd | `chroma` | 1048/1062 (98.7%) | 0 | 0 | 14 | ✓ T2 CEILING CERT |  |
| 189 | -- T2 cert'd | `elfcat` | 1290/1292 (99.8%) | 0 | 0 | 2 | ✓ T2 CEILING CERT |  |
| 190 | -- T2 cert'd | `htmlq` | 2057/2058 (100.0%) | 0 | 0 | 1 | ✓ T2 CEILING CERT |  |
| 191 | -- T2 cert'd | `nikolassv__bartib` | 1856/1858 (99.9%) | 0 | 0 | 2 | ✓ T2 CEILING CERT |  |
| 192 | -- T2 cert'd | `zip-password-finder` | 1582/1584 (99.9%) | 0 | 0 | 2 | ✓ T2 CEILING CERT |  |
| 193 | -- T2 cert'd | `incu6us__goimports-reviser` | 1216/1218 (99.8%) | 0 | 0 | 2 | ✓ T2 CEILING CERT |  |
| 194 | -- T2 cert'd | `xz` | 4064/4072 (99.8%) | 0 | 0 | 8 | ✓ T2 CEILING CERT |  |
| 195 | -- T2 cert'd | `eudoxia0__hashcards` | 2572/2586 (99.5%) | 0 | 0 | 6 | ✓ T2 CEILING CERT |  |
| 196 | -- T2 cert'd | `blake3-team__blake3` | 1368/1374 (99.6%) | 0 | 0 | 6 | ✓ T2 CEILING CERT |  |
| 197 | -- T2 cert'd | `oppiliappan__statix` | 1948/1956 (99.6%) | 0 | 0 | 8 | ✓ T2 CEILING CERT |  |
| 198 | -- T2 cert'd | `pingu` | 416/419 (99.3%) | 0 | 0 | 3 | ✓ T2 CEILING CERT |  |
| 199 | -- T2 cert'd | `filosottile__age` | 1590/1678 (94.8%) | 0 | 0 | 88 | ✓ T2 CEILING CERT |  |
| 200 | -- T2 cert'd | `argc` | 2664/2820 (94.5%) | 0 | 0 | 156 | ✓ T2 CEILING CERT |  |

---
*Auto-generated by `scripts/pb_priority_queue.py` on 2026-06-26*
