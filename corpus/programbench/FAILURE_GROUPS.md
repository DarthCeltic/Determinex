# ProgramBench Failure Groups (caps confirmed gone) — 2026-06-17

> Non-lock tools: 139 | locks: 61. Clustered by dominant error signature so fixes attack GROUPS not tools. Caps verified removed (pb_override_scan --guard passed).

## Tiers

- build-broken (<50%): 56
- partial (50-95%): 27
- near-lock (>=95%): 56

## Failure groups (size-ordered)


### [79] AssertionError
- duckdb__duckdb — 14/5802 (0%) nr=5093 fail=774 err=0
- gromacs__gromacs — 4/1264 (0%) nr=914 fail=336 err=0
- ip7z__7zip — 5/1062 (0%) nr=708 fail=489 err=0
- rhysd__kiro-editor — 10/697 (1%) nr=251 fail=874 err=0
- jhspetersson__fselect — 49/3205 (2%) nr=2780 fail=600 err=0
- ogham__dog — 35/1704 (2%) nr=0 fail=3364 err=0
- sharkdp__bat — 33/979 (3%) nr=0 fail=1814 err=0
- yoav-lavi__melody — 50/1260 (4%) nr=807 fail=669 err=0
- danmar__cppcheck — 99/2273 (4%) nr=1527 fail=889 err=0
- lua__lua — 64/1373 (5%) nr=686 fail=910 err=0
- go-critic__go-critic — 59/825 (7%) nr=207 fail=623 err=0
- robertdavidgraham__masscan — 207/2830 (7%) nr=1855 fail=991 err=0
- halitechallenge__halite — 32/391 (8%) nr=94 fail=326 err=25
- cweill__gotests — 79/742 (11%) nr=246 fail=531 err=0
- hooklift__gowsdl — 45/419 (11%) nr=168 fail=343 err=0
- eliukblau__pixterm — 54/458 (12%) nr=69 fail=392 err=0
- epistates__treemd — 230/1793 (13%) nr=997 fail=754 err=0
- lymphatus__caesium-clt — 80/591 (14%) nr=140 fail=520 err=0
- ksxgithub__parallel-disk-usage — 97/621 (16%) nr=155 fail=477 err=0
- jonas__tig — 396/2349 (17%) nr=175 fail=3538 err=1
- yassinebridi__serpl — 88/511 (17%) nr=169 fail=254 err=0
- rust-ethereum__ethabi — 176/1012 (17%) nr=279 fail=744 err=1
- ammarabouzor__tui-journal — 243/1361 (18%) nr=772 fail=967 err=0
- zk-org__zk — 277/1471 (19%) nr=0 fail=1534 err=774
- git-bahn__git-graph — 159/732 (22%) nr=118 fail=552 err=1
- jarun__nnn — 357/1531 (23%) nr=0 fail=2338 err=0
- codesnap-rs__codesnap — 205/852 (24%) nr=248 fail=547 err=0
- mkj__dropbear — 231/946 (24%) nr=305 fail=331 err=131
- tomarrell__wrapcheck — 151/607 (25%) nr=8 fail=480 err=0
- nikoladucak__caps-log — 434/1136 (38%) nr=18 fail=1328 err=0
- ggreer__the_silver_searcher — 555/1190 (47%) nr=0 fail=636 err=0
- typst__typst — 881/1788 (49%) nr=3 fail=1806 err=0
- jesseduffield__lazygit — 649/1127 (58%) nr=429 fail=84 err=1
- nachoparker__dutree — 569/948 (60%) nr=4 fail=338 err=30
- xampprocky__tokei — 471/763 (62%) nr=0 fail=576 err=1
- dundee__gdu — 987/1550 (64%) nr=0 fail=1128 err=0
- sharkdp__hexyl — 640/971 (66%) nr=325 fail=6 err=0
- bootandy__dust — 678/951 (71%) nr=0 fail=538 err=0
- hairyhenderson__gomplate — 2633/3542 (74%) nr=0 fail=1776 err=0
- dalance__amber — 611/778 (79%) nr=129 fail=33 err=0
- blacknon__hwatch — 990/1260 (79%) nr=73 fail=394 err=0
- zevv__duc — 1016/1244 (82%) nr=0 fail=213 err=0
- johnkerl__miller — 13681/15992 (86%) nr=2207 fail=204 err=0
- antonmedv__walk — 655/757 (87%) nr=96 fail=8 err=1
- skeema__skeema — 3028/3440 (88%) nr=0 fail=132 err=0
- stacked-git__stgit — 2143/2375 (90%) nr=97 fail=115 err=0
- antonmedv__fx — 2904/3148 (92%) nr=77 fail=326 err=0
- gabotechs__dep-tree — 1326/1426 (93%) nr=0 fail=98 err=0
- peco__peco — 1597/1715 (93%) nr=0 fail=230 err=0
- ninja-build__ninja — 1758/1883 (93%) nr=0 fail=248 err=0
- pls-rs__pls — 334/354 (94%) nr=0 fail=14 err=0
- rustowl — 721/762 (95%) nr=0 fail=10 err=0
- facebook__zstd — 2241/2351 (95%) nr=0 fail=94 err=0
- kyoheiu__felix — 938/979 (96%) nr=0 fail=80 err=0
- byron__dua-cli — 955/986 (97%) nr=0 fail=54 err=0
- arq5x__bedtools2 — 1062/1093 (97%) nr=0 fail=22 err=0
- dandavison__delta — 1159/1188 (98%) nr=0 fail=58 err=0
- tarka__xcp — 1208/1236 (98%) nr=0 fail=8 err=0
- rust-lang__mdbook — 1270/1297 (98%) nr=0 fail=21 err=0
- luajit__luajit — 3107/3170 (98%) nr=0 fail=124 err=0
- xorg62__tty-clock — 313/319 (98%) nr=0 fail=12 err=0
- elkowar__pipr — 821/835 (98%) nr=0 fail=9 err=3
- madler__pigz — 917/932 (98%) nr=0 fail=28 err=0
- errcheck — 537/544 (99%) nr=0 fail=10 err=0
- orf__gping — 647/655 (99%) nr=0 fail=4 err=0
- naggie__dstask — 1572/1586 (99%) nr=0 fail=20 err=0
- axodotdev__oranda — 978/985 (99%) nr=0 fail=12 err=0
- oha — 1079/1086 (99%) nr=2 fail=3 err=0
- eudoxia0__hashcards — 1261/1268 (99%) nr=0 fail=8 err=0
- johanneskaufmann__html-to-markdown — 977/981 (100%) nr=0 fail=8 err=0
- ngrrram — 331/332 (100%) nr=0 fail=1 err=0
- ov — 2428/2435 (100%) nr=0 fail=14 err=0
- hck — 881/883 (100%) nr=0 fail=4 err=0
- alexpovel__srgn — 2074/2078 (100%) nr=0 fail=6 err=0
- hpjansson__chafa.dd4d4c1 — 2753/2758 (100%) nr=0 fail=10 err=0
- tailspin — 782/783 (100%) nr=0 fail=2 err=0
- json-tui — 892/893 (100%) nr=0 fail=2 err=0
- nsh — 2238/2240 (100%) nr=0 fail=4 err=0
- ariga__atlas — 1702/1703 (100%) nr=0 fail=2 err=0

### [23] clean/upstream-skip
- argc — 1187/1265 (94%) nr=0 fail=0 err=0
- filosottile__age — 795/839 (95%) nr=0 fail=0 err=0
- chroma — 524/531 (99%) nr=0 fail=0 err=0
- pingu — 410/413 (99%) nr=0 fail=0 err=0
- rumdl — 4601/4630 (99%) nr=0 fail=0 err=0
- blake3-team__blake3 — 684/687 (100%) nr=0 fail=0 err=0
- oppiliappan__statix — 957/961 (100%) nr=0 fail=0 err=0
- doxygen__doxygen — 250/251 (100%) nr=0 fail=0 err=0
- xq — 856/859 (100%) nr=0 fail=0 err=0
- cheat__cheat — 306/307 (100%) nr=0 fail=0 err=0
- tuc — 1241/1245 (100%) nr=0 fail=0 err=0
- csview — 347/348 (100%) nr=0 fail=0 err=0
- cslarsen__jp2a — 719/721 (100%) nr=0 fail=0 err=0
- xz — 2019/2023 (100%) nr=0 fail=0 err=0
- quickjs — 3038/3044 (100%) nr=0 fail=0 err=0
- parqeye — 562/563 (100%) nr=0 fail=0 err=0
- quinn-rs__quinn — 586/587 (100%) nr=0 fail=0 err=0
- incu6us__goimports-reviser — 604/605 (100%) nr=0 fail=0 err=0
- elfcat — 643/644 (100%) nr=0 fail=0 err=0
- zip-password-finder — 788/789 (100%) nr=0 fail=0 err=0
- nikolassv__bartib — 925/926 (100%) nr=0 fail=0 err=0
- ripgrep — 2500/2502 (100%) nr=0 fail=0 err=0
- htmlq — 2057/2058 (100%) nr=0 fail=0 err=0

### [16] No such file
- sqlite__sqlite — 0/16801 (0%) nr=16525 fail=552 err=0
- jgm__pandoc — 1/5467 (0%) nr=5213 fail=506 err=0
- tstack__lnav — 5/1172 (0%) nr=0 fail=2238 err=0
- parcel-bundler__lightningcss — 30/3155 (1%) nr=1929 fail=2384 err=0
- tinycc__tinycc — 26/2062 (1%) nr=0 fail=4068 err=0
- samtools__samtools — 23/1819 (1%) nr=0 fail=2820 err=754
- universal-ctags__ctags — 43/2400 (2%) nr=1945 fail=599 err=0
- chirlu__sox — 24/1260 (2%) nr=0 fail=2048 err=60
- o2sh__onefetch — 29/1204 (2%) nr=0 fail=2364 err=0
- ffmpeg__ffmpeg — 113/4163 (3%) nr=3851 fail=400 err=0
- ecumene__rust-sloth — 21/453 (5%) nr=9 fail=842 err=3
- lfos__calcurse — 101/1920 (5%) nr=243 fail=3106 err=75
- lz4__lz4 — 106/1826 (6%) nr=0 fail=3440 err=0
- htop-dev__htop — 92/1189 (8%) nr=8 fail=2196 err=0
- unhappychoice__gittype — 87/850 (10%) nr=143 fail=1236 err=1
- drew-alleman__datasurgeon — 66/564 (12%) nr=100 fail=495 err=1

### [6] FileNotFoundError
- nukesor__pueue — 0/1019 (0%) nr=711 fail=97 err=246
- osgeo__proj — 3/7160 (0%) nr=6515 fail=1284 err=0
- rochacbruno__marmite — 75/845 (9%) nr=564 fail=731 err=0
- shashwatah__jot — 77/829 (9%) nr=199 fail=735 err=33
- sharkdp__fd — 812/1367 (59%) nr=547 fail=9 err=0
- segmentio__chamber — 2062/2392 (86%) nr=297 fail=52 err=1

### [4] not_run-only
- stranger6667__jsonschema — 1903/3006 (63%) nr=1101 fail=0 err=0
- run — 1155/1507 (77%) nr=187 fail=0 err=0
- kyoh86__richgo — 781/818 (95%) nr=36 fail=0 err=0
- hush-shell__hush — 1288/1303 (99%) nr=15 fail=0 err=0

### [2] error:
- paradigmxyz__solar — 272/2247 (12%) nr=1435 fail=970 err=1
- astaxie__bat — 1386/1456 (95%) nr=0 fail=114 err=0

### [1] E     ...Full output truncated (1241 lines hidden)
- ast-grep__ast-grep — 406/895 (45%) nr=0 fail=978 err=0

### [1] ModuleNotFoundError
- canop__broot — 681/827 (82%) nr=130 fail=15 err=2

### [1] E     ...Full output truncated (455 lines hidden),
- ducaale__xh — 1266/1271 (100%) nr=0 fail=8 err=0

### [1] E     ...Full output truncated (9 lines hidden), u
- monolith — 776/777 (100%) nr=0 fail=1 err=0

### [1] E    +  where 1 = CompletedProcess(args=['/workspa
- osgeo__gdal — 79/1319 (6%) nr=0 fail=2476 err=0

### [1] fatal error:
- php__php-src — 1588/20525 (8%) nr=18385 fail=18 err=1049

### [1] Timeout
- sayanarijit__xplr — 898/939 (96%) nr=0 fail=82 err=0

### [1] Permission denied
- sd — 852/857 (99%) nr=0 fail=2 err=0

### [1] E     ...Full output truncated (18 lines hidden), 
- tree-sitter__tree-sitter — 1595/1640 (97%) nr=0 fail=4 err=0
