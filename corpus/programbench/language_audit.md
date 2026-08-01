# ProgramBench Language Core Audit

> Generated: 2026-06-08 04:30 UTC
>
> **Core languages** (Rust, Go, C, C++, Python, JS, TS) have established compile.sh patterns
> and predictable test behavior. These run FIRST.
>
> **Non-core languages** (Java, Haskell, unknown, etc.) need extra infra work.
> These run LAST.

## Summary

| Category | Count |
|----------|-------|
| Core language tools | 115 |
| Non-core language tools | 78 |
| Ceiling-confirmed (skip) | 7 |
| **Total** | **200** |

## Language Breakdown

- **unknown** (✗ non-core): 77 tools
- **rust** (✓ core): 70 tools
- **go** (✓ core): 23 tools
- **c** (✓ core): 16 tools
- **python** (✓ core): 3 tools
- **cpp** (✓ core): 3 tools
- **java** (✗ non-core): 1 tools

## Core Language Queue (run first)

| # | Slug | Lang | Score | Status | Has Sub |
|---|------|------|-------|--------|---------|
| 1 | angle-grinder | rust | 100.0% (1143/1143) | strict_lock | ✓ |
| 2 | ascii-image-converter | rust | 100.0% (488/488) | strict_lock | ✓ |
| 3 | boyter__scc.515f91c | go | 100.0% (476/476) | strict_lock | ✓ |
| 4 | cmatrix | c | 100.0% (769/769) | strict_lock | ✓ |
| 5 | genact | rust | 100.0% (237/237) | strict_lock | ✓ |
| 6 | go-mod-outdated | go | 100.0% (342/342) | strict_lock | ✓ |
| 7 | gron | go | 100.0% (233/233) | strict_lock | ✓ |
| 8 | hyperfine | rust | 100.0% (298/298) | strict_lock | ✓ |
| 9 | jq | c | 100.0% (6874/6874) | strict_lock | ✓ |
| 10 | pastel | rust | 100.0% (1256/1256) | strict_lock | ✓ |
| 11 | ripsecrets | rust | 100.0% (937/937) | strict_lock | ✓ |
| 12 | shellharden | rust | 100.0% (1292/1292) | strict_lock | ✓ |
| 13 | yq | go | 100.0% (2046/2046) | strict_lock | ✓ |
| 14 | zoxide | rust | 100.0% (577/577) | strict_lock | ✓ |
| 15 | htmlq | rust | 100.0% (2057/2058) | upstream_skips | ✓ |
| 16 | ripgrep | rust | 99.9% (2536/2538) | upstream_skips | ✓ |
| 17 | quickjs | c | 99.8% (3038/3044) | upstream_skips | ✓ |
| 18 | csview | rust | 99.7% (347/348) | upstream_skips | ✓ |
| 19 | xq | rust | 99.7% (876/879) | upstream_skips | ✓ |
| 20 | entr | c | 92.4% (620/671) | pending_unlock | ✓ |
| 21 | git-trim | go | 91.4% (704/770) | pending_unlock | ✓ |
| 22 | elfcat | rust | 90.2% (644/714) | pending_unlock | ✓ |
| 23 | oha | rust | 86.6% (1063/1228) | pending_unlock | ✓ |
| 24 | muffet | go | 85.4% (432/506) | pending_unlock | ✓ |
| 25 | tparse | go | 84.9% (556/655) | pending_unlock | ✓ |
| 26 | tex-fmt | rust | 84.0% (495/589) | pending_unlock | ✓ |
| 27 | sayanarijit__xplr | rust | 83.3% (686/824) | board_cache_only | ✗ |
| 28 | pingu | rust | 80.9% (416/514) | pending_unlock | ✓ |
| 29 | rhit | rust | 79.3% (1045/1317) | pending_unlock | ✓ |
| 30 | xsv | rust | 78.2% (1199/1534) | pending_unlock | ✓ |
| 31 | i3-style | python | 78.0% (750/961) | pending_unlock | ✓ |
| 32 | hck | rust | 77.6% (883/1138) | pending_unlock | ✓ |
| 33 | chroma | rust | 76.9% (400/520) | pending_unlock | ✓ |
| 34 | clog-cli | rust | 76.9% (778/1012) | pending_unlock | ✓ |
| 35 | igrep | rust | 75.9% (547/721) | pending_unlock | ✓ |
| 36 | dsq | go | 75.5% (741/982) | pending_unlock | ✓ |
| 37 | miniserve | rust | 75.1% (440/586) | pending_unlock | ✓ |
| 38 | deadnix | rust | 74.6% (709/951) | pending_unlock | ✓ |
| 39 | rustowl | rust | 74.0% (536/724) | pending_unlock | ✓ |
| 40 | eva | rust | 73.5% (963/1310) | pending_unlock | ✓ |
| 41 | seqtk | c | 73.3% (440/600) | pending_unlock | ✓ |
| 42 | jplot | go | 72.4% (702/969) | pending_unlock | ✓ |
| 43 | pier | rust | 72.3% (778/1076) | pending_unlock | ✓ |
| 44 | tailspin | rust | 71.9% (738/1026) | pending_unlock | ✓ |
| 45 | yj | go | 70.6% (825/1168) | pending_unlock | ✓ |
| 46 | hex | rust | 70.3% (877/1247) | pending_unlock | ✓ |
| 47 | zip-password-finder | rust | 70.2% (791/1127) | pending_unlock | ✓ |
| 48 | sd | rust | 69.6% (864/1241) | pending_unlock | ✓ |
| 49 | ngrrram | rust | 69.6% (277/398) | pending_unlock | ✓ |
| 50 | loop | rust | 69.5% (778/1119) | pending_unlock | ✓ |
| 51 | diffr | rust | 69.5% (762/1096) | pending_unlock | ✓ |
| 52 | fblog | rust | 69.4% (1116/1609) | pending_unlock | ✓ |
| 53 | rust-embedded__svd2rust | rust | 69.1% (746/1079) | board_cache_only | ✗ |
| 54 | json-tui | rust | 67.8% (819/1208) | pending_unlock | ✓ |
| 55 | nsh | rust | 66.2% (2220/3353) | pending_unlock | ✓ |
| 56 | keifu | rust | 66.0% (274/415) | pending_unlock | ✓ |
| 57 | curlie | rust | 65.6% (741/1130) | pending_unlock | ✓ |
| 58 | fzf | go | 65.1% (1797/2760) | pending_unlock | ✓ |
| 59 | tuc | rust | 64.0% (1170/1827) | pending_unlock | ✓ |
| 60 | flamelens | rust | 63.6% (218/343) | pending_unlock | ✓ |
| 61 | xz | c | 63.1% (1436/2274) | pending_unlock | ✓ |
| 62 | bore | rust | 62.8% (450/716) | pending_unlock | ✓ |
| 63 | tarka__xcp | rust | 60.5% (891/1473) | board_cache_only | ✗ |
| 64 | thokr | rust | 60.0% (391/652) | pending_unlock | ✓ |
| 65 | antonmedv__walk | go | 59.9% (471/786) | board_cache_only | ✗ |
| 66 | trdsql | go | 59.5% (1050/1764) | pending_unlock | ✓ |
| 67 | eureka | rust | 59.3% (396/668) | pending_unlock | ✓ |
| 68 | ov | rust | 58.2% (1243/2137) | pending_unlock | ✓ |
| 69 | nikoladucak__caps-log | cpp | 55.9% (636/1138) | board_cache_only | ✗ |
| 70 | monolith | rust | 55.9% (657/1176) | pending_unlock | ✓ |
| 71 | parqeye | python | 54.5% (380/697) | pending_unlock | ✓ |
| 72 | nachoparker__dutree | rust | 53.7% (579/1079) | board_cache_only | ✗ |
| 73 | fasttext | cpp | 53.1% (353/665) | pending_unlock | ✓ |
| 74 | grex | rust | 53.1% (1455/2742) | pending_unlock | ✓ |
| 75 | tinycc__tinycc | c | 49.0% (1148/2341) | board_cache_only | ✗ |
| 76 | ggreer__the_silver_searcher | c | 46.6% (555/1192) | board_cache_only | ✗ |
| 77 | run | rust | 43.7% (693/1585) | pending_unlock | ✓ |
| 78 | isona__dirble | rust | 43.6% (483/1108) | board_cache_only | ✗ |
| 79 | skeema__skeema | go | 41.9% (1036/2475) | board_cache_only | ✗ |
| 80 | gabotechs__dep-tree | go | 38.4% (563/1466) | board_cache_only | ✗ |
| 81 | nikolassv__bartib | rust | 37.1% (367/990) | board_cache_only | ✗ |
| 82 | astaxie__bat | go | 36.8% (645/1754) | board_cache_only | ✗ |
| 83 | ninja-build__ninja | cpp | 36.7% (746/2030) | board_cache_only | ✗ |
| 84 | ksxgithub__parallel-disk-usage | rust | 34.4% (217/630) | board_cache_only | ✗ |
| 85 | chmln__handlr | rust | 33.0% (368/1116) | board_cache_only | ✗ |
| 86 | lfos__calcurse | c | 31.6% (470/1488) | board_cache_only | ✗ |
| 87 | madler__pigz | c | 29.8% (321/1076) | board_cache_only | ✗ |
| 88 | blacknon__hwatch | rust | 29.4% (488/1662) | board_cache_only | ✗ |
| 89 | ariga__atlas | go | 29.1% (515/1769) | board_cache_only | ✗ |
| 90 | bootandy__dust | rust | 29.1% (330/1134) | board_cache_only | ✗ |
| 91 | argc | rust | 29.1% (400/1375) | pending_unlock | ✓ |
| 92 | kisielk__errcheck | go | 28.9% (154/532) | board_cache_only | ✗ |
| 93 | rumdl | rust | 28.9% (1311/4542) | pending_unlock | ✓ |
| 94 | segmentio__chamber | go | 28.2% (672/2379) | board_cache_only | ✗ |
| 95 | tree-sitter__tree-sitter | c | 27.7% (445/1608) | board_cache_only | ✗ |
| 96 | codesnap-rs__codesnap | rust | 27.4% (302/1101) | board_cache_only | ✗ |
| 97 | canop__broot | rust | 27.2% (236/867) | board_cache_only | ✗ |
| 98 | tomarrell__wrapcheck | go | 27.2% (184/677) | board_cache_only | ✗ |
| 99 | mkj__dropbear | c | 26.7% (269/1007) | board_cache_only | ✗ |
| 100 | jarun__nnn | c | 26.3% (377/1433) | board_cache_only | ✗ |
| 101 | jesseduffield__lazygit | go | 26.2% (315/1200) | board_cache_only | ✗ |
| 102 | oppiliappan__statix | rust | 24.2% (267/1105) | board_cache_only | ✗ |
| 103 | guumaster__hostctl | go | 23.8% (407/1709) | board_cache_only | ✗ |
| 104 | ammarabouzor__tui-journal | rust | 22.9% (518/2265) | board_cache_only | ✗ |
| 105 | byron__dua-cli | rust | 22.2% (308/1390) | board_cache_only | ✗ |
| 106 | crowdagger__crowbook | rust | 21.5% (229/1067) | board_cache_only | ✗ |
| 107 | hpjansson__chafa | c | 21.4% (601/2808) | board_cache_only | ✗ |
| 108 | zevv__duc | c | 21.4% (219/1024) | board_cache_only | ✗ |
| 109 | cmatsuoka__figlet | c | 21.1% (279/1320) | board_cache_only | ✗ |
| 110 | git-bahn__git-graph | rust | 20.9% (178/851) | board_cache_only | ✗ |
| 111 | stacked-git__stgit | python | 20.6% (491/2380) | board_cache_only | ✗ |
| 112 | rnr | rust | 0.0% (0/742) | pending_unlock | ✓ |
| 113 | dupl | go | 0.0% (0/450) | pending_unlock | ✓ |
| 114 | code-minimap | rust | 0.0% (0/370) | pending_unlock | ✓ |
| 115 | nomino | rust | 0.0% (0/338) | pending_unlock | ✓ |

## Non-Core Language Queue (run last — needs infra work first)

> [!WARNING]
> These tools require extra compile.sh patterns or language runtimes.
> Gemini Flash: do NOT attempt to lock these without first adding the runtime.

| # | Slug | Lang | Score | Status | Has Sub |
|---|------|------|-------|--------|---------|
| 1 | stathissideris__ditaa | java | 100.0% (681/681) | strict_lock | ✓ |
| 2 | axodotdev__oranda | unknown | 20.5% (271/1321) | board_cache_only | ✗ |
| 3 | antonmedv__fx | unknown | 20.0% (601/3002) | board_cache_only | ✗ |
| 4 | eudoxia0__hashcards | unknown | 19.6% (313/1596) | board_cache_only | ✗ |
| 5 | robertdavidgraham__masscan | unknown | 19.5% (599/3073) | board_cache_only | ✗ |
| 6 | jonas__tig | unknown | 18.6% (440/2364) | board_cache_only | ✗ |
| 7 | rust-ethereum__ethabi | unknown | 18.1% (226/1250) | board_cache_only | ✗ |
| 8 | alexpovel__srgn | unknown | 17.7% (437/2472) | board_cache_only | ✗ |
| 9 | yassinebridi__serpl | unknown | 17.2% (88/511) | board_cache_only | ✗ |
| 10 | mgechev__revive | unknown | 17.2% (161/937) | board_cache_only | ✗ |
| 11 | dundee__gdu | unknown | 16.0% (263/1641) | board_cache_only | ✗ |
| 12 | ogham__dog | unknown | 16.0% (290/1813) | board_cache_only | ✗ |
| 13 | rust-lang__mdbook | unknown | 15.7% (213/1358) | board_cache_only | ✗ |
| 14 | xampprocky__tokei | unknown | 15.7% (139/888) | board_cache_only | ✗ |
| 15 | quinn-rs__quinn | unknown | 15.3% (123/806) | board_cache_only | ✗ |
| 16 | dandavison__delta | unknown | 15.0% (183/1221) | board_cache_only | ✗ |
| 17 | cheat__cheat | unknown | 15.0% (46/307) | board_cache_only | ✗ |
| 18 | cslarsen__jp2a | unknown | 14.9% (139/930) | board_cache_only | ✗ |
| 19 | shashwatah__jot | unknown | 14.1% (119/846) | board_cache_only | ✗ |
| 20 | parcel-bundler__lightningcss | unknown | 13.9% (510/3666) | board_cache_only | ✗ |
| 21 | rochacbruno__marmite | unknown | 13.5% (187/1385) | board_cache_only | ✗ |
| 22 | filosottile__age | unknown | 13.2% (137/1038) | board_cache_only | ✗ |
| 23 | epistates__treemd | unknown | 13.0% (263/2019) | board_cache_only | ✗ |
| 24 | go-critic__go-critic | unknown | 13.0% (122/941) | board_cache_only | ✗ |
| 25 | hooklift__gowsdl | unknown | 12.9% (76/587) | board_cache_only | ✗ |
| 26 | direnv__direnv | unknown | 12.6% (127/1006) | board_cache_only | ✗ |
| 27 | eliukblau__pixterm | unknown | 12.5% (66/527) | board_cache_only | ✗ |
| 28 | lymphatus__caesium-clt | unknown | 12.5% (94/755) | board_cache_only | ✗ |
| 29 | cweill__gotests | unknown | 12.4% (110/889) | board_cache_only | ✗ |
| 30 | kyoheiu__felix | unknown | 12.3% (113/919) | board_cache_only | ✗ |
| 31 | ip7z__7zip | unknown | 12.2% (151/1234) | board_cache_only | ✗ |
| 32 | danmar__cppcheck | unknown | 11.2% (285/2544) | board_cache_only | ✗ |
| 33 | naggie__dstask | unknown | 10.8% (180/1661) | board_cache_only | ✗ |
| 34 | paradigmxyz__solar | unknown | 10.6% (285/2693) | board_cache_only | ✗ |
| 35 | unhappychoice__gittype | unknown | 10.4% (86/828) | board_cache_only | ✗ |
| 36 | drew-alleman__datasurgeon | unknown | 10.2% (68/664) | board_cache_only | ✗ |
| 37 | ecumene__rust-sloth | unknown | 10.0% (58/578) | board_cache_only | ✗ |
| 38 | samtools__samtools | unknown | 9.6% (145/1511) | board_cache_only | ✗ |
| 39 | o2sh__onefetch | unknown | 9.4% (124/1325) | board_cache_only | ✗ |
| 40 | pls-rs__pls | unknown | 9.0% (32/354) | board_cache_only | ✗ |
| 41 | yoav-lavi__melody | unknown | 8.2% (131/1607) | board_cache_only | ✗ |
| 42 | hairyhenderson__gomplate | unknown | 8.1% (283/3496) | board_cache_only | ✗ |
| 43 | htop-dev__htop | unknown | 8.0% (112/1393) | board_cache_only | ✗ |
| 44 | ducaale__xh | unknown | 8.0% (113/1415) | board_cache_only | ✗ |
| 45 | halitechallenge__halite | unknown | 7.4% (36/485) | board_cache_only | ✗ |
| 46 | stranger6667__jsonschema | unknown | 7.3% (247/3373) | board_cache_only | ✗ |
| 47 | osgeo__gdal | unknown | 7.2% (74/1023) | board_cache_only | ✗ |
| 48 | facebook__zstd | unknown | 6.9% (191/2788) | board_cache_only | ✗ |
| 49 | lua__lua | unknown | 6.8% (117/1715) | board_cache_only | ✗ |
| 50 | elkowar__pipr | unknown | 6.7% (50/742) | board_cache_only | ✗ |
| 51 | hush-shell__hush | unknown | 6.6% (107/1615) | board_cache_only | ✗ |
| 52 | universal-ctags__ctags | unknown | 6.6% (171/2606) | board_cache_only | ✗ |
| 53 | xorg62__tty-clock | unknown | 6.4% (22/342) | board_cache_only | ✗ |
| 54 | lz4__lz4 | unknown | 5.8% (109/1869) | board_cache_only | ✗ |
| 55 | luajit__luajit | unknown | 5.6% (205/3674) | board_cache_only | ✗ |
| 56 | blake3-team__blake3 | unknown | 5.3% (36/685) | board_cache_only | ✗ |
| 57 | peco__peco | unknown | 5.2% (89/1705) | board_cache_only | ✗ |
| 58 | incu6us__goimports-reviser | unknown | 5.0% (37/747) | board_cache_only | ✗ |
| 59 | google__brotli | unknown | 4.4% (42/955) | board_cache_only | ✗ |
| 60 | sharkdp__bat | unknown | 2.5% (30/1178) | board_cache_only | ✗ |
| 61 | johnkerl__miller | unknown | 2.2% (353/15786) | board_cache_only | ✗ |
| 62 | ffmpeg__ffmpeg | unknown | 2.1% (68/3266) | board_cache_only | ✗ |
| 63 | zk-org__zk | unknown | 2.0% (27/1331) | board_cache_only | ✗ |
| 64 | jhspetersson__fselect | unknown | 1.7% (60/3480) | board_cache_only | ✗ |
| 65 | nukesor__pueue | unknown | 1.4% (14/1009) | board_cache_only | ✗ |
| 66 | ast-grep__ast-grep | unknown | 1.4% (17/1232) | board_cache_only | ✗ |
| 67 | duckdb__duckdb | unknown | 1.2% (70/5988) | board_cache_only | ✗ |
| 68 | sqlite__sqlite | unknown | 1.0% (135/14138) | board_cache_only | ✗ |
| 69 | typst__typst | unknown | 0.8% (16/2027) | board_cache_only | ✗ |
| 70 | ivanceras__svgbob | unknown | 0.7% (4/554) | board_cache_only | ✗ |
| 71 | arq5x__bedtools2 | unknown | 0.7% (7/1060) | board_cache_only | ✗ |
| 72 | chirlu__sox | unknown | 0.4% (6/1469) | board_cache_only | ✗ |
| 73 | tstack__lnav | unknown | 0.4% (4/1005) | board_cache_only | ✗ |
| 74 | gromacs__gromacs | unknown | 0.3% (4/1264) | board_cache_only | ✗ |
| 75 | php__php-src | unknown | 0.2% (27/15054) | board_cache_only | ✗ |
| 76 | osgeo__proj | unknown | 0.1% (3/5793) | board_cache_only | ✗ |
| 77 | jgm__pandoc | unknown | 0.0% (1/5482) | board_cache_only | ✗ |
| 78 | rhysd__kiro-editor | unknown | 0.0% (0/0) | board_cache_only | ✗ |

## Ceiling-Confirmed (skip entirely)

- doxygen__doxygen (unknown): irreconcilable ceiling, do not attempt
- orf__gping (unknown): irreconcilable ceiling, do not attempt
- kyoh86__richgo (go): irreconcilable ceiling, do not attempt
- dalance__amber (rust): irreconcilable ceiling, do not attempt
- johanneskaufmann__html-to-markdown (unknown): irreconcilable ceiling, do not attempt
- sharkdp__fd (unknown): irreconcilable ceiling, do not attempt
- sharkdp__hexyl (unknown): irreconcilable ceiling, do not attempt