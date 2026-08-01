# Pattern 002 Collection-Wall Census

Source: current `corpus/programbench/campaign_landscape.json` rows with `failure_class` in `collection-wall` or `partial-collection`.
Method: `scripts/pb_collection_probe.py` over existing best-known reports only; no evals launched.

- requested/pasted target: `97` collection-wall tools
- current machine roster probed: `100` tools
- successful probes: `99`
- unresolved probes: `1`

## Pile Counts

| pile | tools |
|---|---:|
| `CAP_TRUNCATED` | 25 |
| `EMISSION_LOSS` | 10 |
| `TRUE_WALL_BEHAVIORAL` | 63 |
| `UNKNOWN` | 1 |

## CAP_TRUNCATED Roster

| tool | cap branches | report |
|---|---|---|
| `antonmedv__fx` | 8557934c32db 400/608, e4def75fb3ef 400/1618 | `T:\determinex-staging\hetzner_returns\hetzner_full_200_20260606\results\antonmedv__fx.86d0d34.eval.json` |
| `ariga__atlas` | cbaf9db6ea2e 400/820 | `T:\determinex-programbench\hetzner_results\hetzner_queue_006\results\ariga__atlas.6d81150.eval.json` |
| `arq5x__bedtools2` | b0846e00e790 400/1093 | `T:\determinex-programbench\hetzner_results\hetzner_bottom_push_002\results\results\arq5x__bedtools2.dd57059.eval.json` |
| `chirlu__sox` | 269b33cf14ef 400/1004 | `T:\determinex-programbench\hetzner_results\hetzner_floor_002\results\chirlu__sox.42b3557.eval.json` |
| `cmatsuoka__figlet` | 18e5fb09a17a 400/486 | `T:\determinex-staging\hetzner_returns\hetzner_full_200_20260606\results\cmatsuoka__figlet.202a0a8.eval.json` |
| `crowdagger__crowbook` | 9cd5a99e237f 400/506 | `T:\determinex-programbench\hetzner_results\hetzner_full_200_20260606\results\crowdagger__crowbook.ea214d7.eval.json` |
| `danmar__cppcheck` | 1040f6b8a219 400/1816, b9729b57ee68 400/417 | `T:\determinex-programbench\hetzner_results\hetzner_cppcheck_addons_001\results\danmar__cppcheck.0a5b103.eval.json` |
| `ducaale__xh` | 06aaf86cdfa9 400/912 | `T:\determinex-programbench\hetzner_results\hetzner_argv_bulk_001\results\ducaale__xh.4a6e44f.eval.json` |
| `dundee__gdu` | 9a09132872e3 400/633, abd9c19cdfc1 400/637 | `T:\determinex-programbench\hetzner_results\hetzner_native_002\results\dundee__gdu.ede21d2.eval.json` |
| `epistates__treemd` | 1040f6b8a219 400/1275 | `T:\determinex-programbench\hetzner_results\hetzner_native_003\results\epistates__treemd.825c6dd.eval.json` |
| `facebook__zstd` | bcc0b83fd418 400/463, f7278a893d6d 400/431, ff48618e10b3 400/821 | `T:\determinex-programbench\hetzner_results\hetzner_queue_006\results\facebook__zstd.1168da0.eval.json` |
| `ffmpeg__ffmpeg` | 3f244e346e7e 400/3848 | `T:\determinex-programbench\hetzner_results\hetzner_queue_006\results\ffmpeg__ffmpeg.360a402.eval.json` |
| `gabotechs__dep-tree` | 3d3e605d0ecc 400/622 | `T:\determinex-staging\hetzner_returns\hetzner_full_200_20260606\results\gabotechs__dep-tree.60a95a2.eval.json` |
| `hairyhenderson__gomplate` | 1040f6b8a219 400/1607, 8c56af240bad 400/1229 | `T:\determinex-programbench\hetzner_results\hetzner_queue_006\results\hairyhenderson__gomplate.05eb3aa.eval.json` |
| `johnkerl__miller` | 4e01bbf3b7b0 400/6777, 6d3d0da46d76 400/4527, 79acf88a93fa 400/2207, c55c103e74ae 400/2209 | `T:\determinex-programbench\hetzner_results\hetzner_workspace_wave4_001\results\johnkerl__miller.8d85b46.eval.json` |
| `mgechev__revive` | 328affc08c41 400/639 | `T:\determinex-programbench\hetzner_shards_archive\20260526_cdrive_freeup\hetzner_lockwave_001\runs\pb_revive_version_v6\mgechev__revive.201451e\mgechev__revive.201451e.eval.json` |
| `ninja-build__ninja` | 4f1adf8644e5 400/838 | `T:\determinex-programbench\hetz_import_ninja-build_ninja.cc60300\ninja-build__ninja.cc60300\ninja-build__ninja.cc60300.eval.json` |
| `nukesor__pueue` | 06dabfabaea7 400/668, 803faac7d834 400/555 | `T:\determinex-programbench\hetzner_results\hetzner_drain_002\results\nukesor__pueue.8b9d6fe.eval.json` |
| `rust-lang__mdbook` | 26df40b96ca8 400/619 | `T:\determinex-staging\hetzner_returns\hetzner_full_200_20260606\results\rust-lang__mdbook.37273ba.eval.json` |
| `skeema__skeema` | 34521d0dbd17 400/664, 41d65330ce2f 400/895, 7c9925b9a694 400/435, a903bacb7595 400/1585 | `T:\determinex-programbench\hetzner_results\hetzner_full_200_20260606\results\skeema__skeema.6a76243.eval.json` |
| `tarka__xcp` | 49179779960b 400/743 | `T:\determinex-programbench\determinex_pb_xcp_v4\tarka__xcp.5e5b448\tarka__xcp.5e5b448.eval.json` |
| `typst__typst` | 4f61e62031ac 400/1385 | `T:\determinex-programbench\hetzner_results\hetzner_bottom_push_002\results\results\typst__typst.88356d0.eval.json` |
| `universal-ctags__ctags` | 0368ca6ed669 400/2297 | `T:\determinex-programbench\hetzner_results\hetzner_lock_wave13_001\results\universal-ctags__ctags.243595e.eval.json` |
| `xampprocky__tokei` | d6cf5754a29c 400/563 | `T:\determinex-staging\hetzner_returns\hetzner_full_200_20260606\results\xampprocky__tokei.505d648.eval.json` |
| `zk-org__zk` | ad0a74fcd352 400/1185 | `T:\determinex-programbench\hetzner_results\hetzner_bottom_push_002\results\results\zk-org__zk.10d93d5.eval.json` |

## EMISSION_LOSS Roster

| tool | B-C | true wall | behavioral | report |
|---|---:|---:|---:|---|
| `ammarabouzor__tui-journal` | 714 | 330 | 516 | `T:\determinex-programbench\hetz_import_ammarabouzor_tui-journal.2b4540d\ammarabouzor__tui-journal.2b4540d\ammarabouzor__tui-journal.2b4540d.eval.json` |
| `bootandy__dust` | 457 | 13 | 203 | `T:\determinex-programbench\hetzner_results\hetzner_argv_bulk_001\results\bootandy__dust.62bf1e1.eval.json` |
| `byron__dua-cli` | 642 | 395 | 29 | `T:\determinex-programbench\determinex_pb_dua-cli_vbidir7\byron__dua-cli.8570c15\byron__dua-cli.8570c15.eval.json` |
| `chmln__handlr` | 338 | 9 | 1 | `T:\determinex-programbench\hetzner_shards_archive\20260526_cdrive_freeup\hetzner_codex_native_patch_002\runs\pb_chmln_handlr_native_v2\chmln__handlr.90e78ba\chmln__handlr.90e78ba.eval.json` |
| `guumaster__hostctl` | 518 | 236 | 508 | `T:\determinex-programbench\determinex_pb_factory_guumaster__hostctl.d6d9699_v1\guumaster__hostctl.d6d9699\guumaster__hostctl.d6d9699.eval.json` |
| `htop-dev__htop` | 700 | 500 | 0 | `T:\determinex-programbench\determinex_pb_factory_htop-dev__htop.523600b_v1\htop-dev__htop.523600b\htop-dev__htop.523600b.eval.json` |
| `hush-shell__hush` | 382 | 306 | 1 | `T:\determinex-programbench\hetzner_results\hetzner_floor_wave5_001\results\hush-shell__hush.560c33a.eval.json` |
| `incu6us__goimports-reviser` | 169 | 0 | 1 | `T:\determinex-programbench\hetzner_results\hetzner_bottom_push_002\results\results\incu6us__goimports-reviser.81bd549.eval.json` |
| `ivanceras__svgbob` | 81 | 0 | 0 | `T:\determinex-programbench\hetzner_results\hetzner_svgbob_argv0_v4_20260527\results\ivanceras__svgbob.6d00ad9.eval.json` |
| `jarun__nnn` | 852 | 785 | 117 | `T:\determinex-programbench\determinex_pb_factory_jarun__nnn.cb2c535_v1\jarun__nnn.cb2c535\jarun__nnn.cb2c535.eval.json` |

## TRUE_WALL_BEHAVIORAL Roster

| tool | true wall | behavioral | emission | report |
|---|---:|---:|---:|---|
| `alexpovel__srgn` | 550 | 3 | 533 | `T:\determinex-programbench\hetzner_results\hetzner_argv0_wave_001\results\alexpovel__srgn.89f943b.eval.json` |
| `astaxie__bat` | 482 | 188 | 453 | `T:\determinex-programbench\determinex_pb_bat_vbidir7\astaxie__bat.17d1080\astaxie__bat.17d1080.eval.json` |
| `blake3-team__blake3` | 0 | 656 | 0 | `T:\determinex-programbench\determinex_pb_blake3_vbidir7\blake3-team__blake3.15e83a5\blake3-team__blake3.15e83a5.eval.json` |
| `canop__broot` | 361 | 0 | 204 | `T:\determinex-programbench\determinex_pb_broot_vbidir7\canop__broot.d6c798e\canop__broot.d6c798e.eval.json` |
| `codesnap-rs__codesnap` | 377 | 0 | 356 | `T:\determinex-programbench\determinex_pb_codesnap_vbidir7\codesnap-rs__codesnap.f81e4f3\codesnap-rs__codesnap.f81e4f3.eval.json` |
| `cslarsen__jp2a` | 0 | 393 | 251 | `T:\determinex-programbench\hetz_import_cslarsen_jp2a.61d205f\cslarsen__jp2a.61d205f\cslarsen__jp2a.61d205f.eval.json` |
| `cweill__gotests` | 123 | 396 | 198 | `T:\determinex-programbench\hetz_import_cweill_gotests.2a672c5\cweill__gotests.2a672c5\cweill__gotests.2a672c5.eval.json` |
| `dandavison__delta` | 156 | 45 | 151 | `T:\determinex-programbench\determinex_pb_delta_vbidir7\dandavison__delta.acd758f\dandavison__delta.acd758f.eval.json` |
| `direnv__direnv` | 147 | 809 | 93 | `T:\determinex-programbench\determinex_pb_direnv_vbidir7\direnv__direnv.02040c7\direnv__direnv.02040c7.eval.json` |
| `drew-alleman__datasurgeon` | 17 | 445 | 0 | `T:\determinex-programbench\root\determinex-programbench\determinex_pb_factory_drew-alleman__datasurgeon.d257cee_v1\drew-alleman__datasurgeon.d257cee\drew-alleman__datasurgeon.d257cee.eval.json` |
| `duckdb__duckdb` | 8063 | 582 | 195 | `T:\determinex-programbench\determinex_pb_factory_duckdb__duckdb.bdb65ec_v1\duckdb__duckdb.bdb65ec\duckdb__duckdb.bdb65ec.eval.json` |
| `ecumene__rust-sloth` | 0 | 1 | 0 | `T:\determinex-programbench\mass_run_v2_base\ecumene__rust-sloth.051c559\ecumene__rust-sloth.051c559.eval.json` |
| `eliukblau__pixterm` | 0 | 328 | 78 | `T:\determinex-programbench\determinex_pb_factory_eliukblau__pixterm.1a93fd5_v1\eliukblau__pixterm.1a93fd5\eliukblau__pixterm.1a93fd5.eval.json` |
| `elkowar__pipr` | 248 | 7 | 145 | `T:\determinex-programbench\hetzner_results\hetzner_native_003\results\elkowar__pipr.fae0b17.eval.json` |
| `eudoxia0__hashcards` | 226 | 570 | 407 | `T:\determinex-programbench\determinex_pb_factory_eudoxia0__hashcards.48aa136_v1\eudoxia0__hashcards.48aa136\eudoxia0__hashcards.48aa136.eval.json` |
| `git-bahn__git-graph` | 5 | 408 | 178 | `T:\determinex-programbench\determinex_pb_factory_git-bahn__git-graph.87b4473_v1\git-bahn__git-graph.87b4473\git-bahn__git-graph.87b4473.eval.json` |
| `go-critic__go-critic` | 210 | 401 | 212 | `T:\determinex-programbench\root\determinex-programbench\determinex_pb_factory_go-critic__go-critic.9aea378_v1\go-critic__go-critic.9aea378\go-critic__go-critic.9aea378.eval.json` |
| `google__brotli` | 442 | 0 | 164 | `T:\determinex-programbench\determinex_pb_factory_google__brotli.b3dc9cc_v1\google__brotli.b3dc9cc\google__brotli.b3dc9cc.eval.json` |
| `gromacs__gromacs` | 0 | 64 | 0 | `T:\determinex-programbench\hetzner_results\hetzner_gromacs_v4_001\results\results\gromacs__gromacs.665ea4c.eval.json` |
| `halitechallenge__halite` | 0 | 256 | 107 | `T:\determinex-programbench\determinex_pb_factory_halitechallenge__halite.822cfb6_v1\halitechallenge__halite.822cfb6\halitechallenge__halite.822cfb6.eval.json` |
| `hooklift__gowsdl` | 17 | 194 | 180 | `T:\determinex-programbench\determinex_pb_factory_hooklift__gowsdl.2a06cec_v1\hooklift__gowsdl.2a06cec\hooklift__gowsdl.2a06cec.eval.json` |
| `ip7z__7zip` | 559 | 346 | 176 | `T:\determinex-programbench\determinex_pb_factory_ip7z__7zip.839151e_v1\ip7z__7zip.839151e\ip7z__7zip.839151e.eval.json` |
| `jesseduffield__lazygit` | 384 | 39 | 135 | `T:\determinex-staging\hetzner_returns\hetzner_full_200_20260606\results\jesseduffield__lazygit.1d0db51.eval.json` |
| `jgm__pandoc` | 4863 | 350 | 254 | `T:\determinex-programbench\determinex_pb_factory_jgm__pandoc.5caad90_v1\jgm__pandoc.5caad90\jgm__pandoc.5caad90.eval.json` |
| `jhspetersson__fselect` | 2735 | 314 | 350 | `T:\determinex-programbench\determinex_pb_factory_jhspetersson__fselect.c3559ca_v1\jhspetersson__fselect.c3559ca\jhspetersson__fselect.c3559ca.eval.json` |
| `jonas__tig` | 662 | 856 | 365 | `T:\determinex-programbench\determinex_pb_factory_jonas__tig.8334123_v1\jonas__tig.8334123\jonas__tig.8334123.eval.json` |
| `kyoheiu__felix` | 282 | 449 | 198 | `T:\determinex-programbench\determinex_pb_factory_kyoheiu__felix.95df390_v1\kyoheiu__felix.95df390\kyoheiu__felix.95df390.eval.json` |
| `lfos__calcurse` | 1146 | 44 | 794 | `T:\determinex-programbench\root\determinex-programbench\determinex_pb_factory_lfos__calcurse.49180d5_v1\lfos__calcurse.49180d5\lfos__calcurse.49180d5.eval.json` |
| `lua__lua` | 366 | 614 | 349 | `T:\determinex-programbench\determinex_pb_factory_lua__lua.c6b4848_v1\lua__lua.c6b4848\lua__lua.c6b4848.eval.json` |
| `luajit__luajit` | 2073 | 398 | 703 | `T:\determinex-programbench\determinex_pb_factory_luajit__luajit.a553b3d_v1\luajit__luajit.a553b3d\luajit__luajit.a553b3d.eval.json` |
| `lymphatus__caesium-clt` | 1 | 391 | 145 | `T:\determinex-programbench\determinex_pb_factory_lymphatus__caesium-clt.a529b2e_v1\lymphatus__caesium-clt.a529b2e\lymphatus__caesium-clt.a529b2e.eval.json` |
| `lz4__lz4` | 740 | 861 | 152 | `T:\determinex-programbench\determinex_pb_factory_lz4__lz4.1519f46_v1\lz4__lz4.1519f46\lz4__lz4.1519f46.eval.json` |
| `madler__pigz` | 140 | 406 | 181 | `T:\determinex-programbench\determinex_pb_factory_madler__pigz.fe4894f_v1\madler__pigz.fe4894f\madler__pigz.fe4894f.eval.json` |
| `mkj__dropbear` | 0 | 33 | 0 | `T:\determinex-programbench\mass_run_v2_base\mkj__dropbear.75f699b\mkj__dropbear.75f699b.eval.json` |
| `nachoparker__dutree` | 11 | 368 | 129 | `T:\determinex-programbench\hetzner_results\claude_batch6_missing8_20260606\results\nachoparker__dutree.44e877d.eval.json` |
| `naggie__dstask` | 536 | 753 | 199 | `T:\determinex-programbench\root\determinex-programbench\determinex_pb_factory_naggie__dstask.ff57396_v1\naggie__dstask.ff57396\naggie__dstask.ff57396.eval.json` |
| `nikoladucak__caps-log` | 127 | 551 | 4 | `T:\determinex-programbench\determinex_pb_factory_nikoladucak__caps-log.2cf2d1e_v1\nikoladucak__caps-log.2cf2d1e\nikoladucak__caps-log.2cf2d1e.eval.json` |
| `o2sh__onefetch` | 553 | 485 | 125 | `T:\determinex-programbench\determinex_pb_factory_o2sh__onefetch.e5958ce_v1\o2sh__onefetch.e5958ce\o2sh__onefetch.e5958ce.eval.json` |
| `ogham__dog` | 746 | 570 | 350 | `T:\determinex-programbench\determinex_pb_factory_ogham__dog.721440b_v1\ogham__dog.721440b\ogham__dog.721440b.eval.json` |
| `oppiliappan__statix` | 183 | 347 | 213 | `T:\determinex-programbench\determinex_pb_factory_oppiliappan__statix.e9df54c_v1\oppiliappan__statix.e9df54c\oppiliappan__statix.e9df54c.eval.json` |
| `osgeo__gdal` | 619 | 329 | 350 | `T:\determinex-programbench\determinex_pb_factory_osgeo__gdal.0847f12_v1\osgeo__gdal.0847f12\osgeo__gdal.0847f12.eval.json` |
| `paradigmxyz__solar` | 1440 | 533 | 357 | `T:\determinex-programbench\determinex_pb_factory_paradigmxyz__solar.5190d0e_v1\paradigmxyz__solar.5190d0e\paradigmxyz__solar.5190d0e.eval.json` |
| `peco__peco` | 668 | 677 | 289 | `T:\determinex-programbench\determinex_pb_factory_peco__peco.4e58dad_v1\peco__peco.4e58dad\peco__peco.4e58dad.eval.json` |
| `php__php-src` | 19263 | 854 | 353 | `T:\determinex-programbench\determinex_pb_factory_php__php-src.c891263_v1\php__php-src.c891263\php__php-src.c891263.eval.json` |
| `pls-rs__pls` | 4 | 312 | 0 | `T:\determinex-programbench\determinex_pb_factory_pls-rs__pls.4e1ae50_v1\pls-rs__pls.4e1ae50\pls-rs__pls.4e1ae50.eval.json` |
| `quinn-rs__quinn` | 21 | 279 | 258 | `T:\determinex-programbench\determinex_pb_factory_quinn-rs__quinn.bb359cc_v1\quinn-rs__quinn.bb359cc\quinn-rs__quinn.bb359cc.eval.json` |
| `robertdavidgraham__masscan` | 2141 | 734 | 355 | `T:\determinex-programbench\determinex_pb_factory_robertdavidgraham__masscan.b99d433_v1\robertdavidgraham__masscan.b99d433\robertdavidgraham__masscan.b99d433.eval.json` |
| `rochacbruno__marmite` | 529 | 64 | 250 | `T:\determinex-programbench\determinex_pb_factory_rochacbruno__marmite.7d4bc2d_v1\rochacbruno__marmite.7d4bc2d\rochacbruno__marmite.7d4bc2d.eval.json` |
| `rust-ethereum__ethabi` | 90 | 569 | 219 | `T:\determinex-programbench\determinex_pb_factory_rust-ethereum__ethabi.b1710ad_v1\rust-ethereum__ethabi.b1710ad\rust-ethereum__ethabi.b1710ad.eval.json` |
| `samtools__samtools` | 1143 | 531 | 0 | `T:\determinex-programbench\determinex_pb_factory_samtools__samtools.aa823b5_v1\samtools__samtools.aa823b5\samtools__samtools.aa823b5.eval.json` |
| `segmentio__chamber` | 1023 | 159 | 0 | `T:\determinex-programbench\determinex_pb_chamber_vbidir7\segmentio__chamber.5f93f5f\segmentio__chamber.5f93f5f.eval.json` |
| `sqlite__sqlite` | 16523 | 1 | 276 | `T:\determinex-programbench\determinex_pb_factory_sqlite__sqlite.839433d_v1\sqlite__sqlite.839433d\sqlite__sqlite.839433d.eval.json` |
| `stacked-git__stgit` | 909 | 725 | 354 | `T:\determinex-programbench\determinex_pb_factory_stacked-git__stgit.430027d_v1\stacked-git__stgit.430027d\stacked-git__stgit.430027d.eval.json` |
| `stranger6667__jsonschema` | 1006 | 444 | 369 | `T:\determinex-programbench\determinex_pb_factory_stranger6667__jsonschema.d52e881_v1\stranger6667__jsonschema.d52e881\stranger6667__jsonschema.d52e881.eval.json` |
| `tinycc__tinycc` | 463 | 1243 | 350 | `T:\determinex-programbench\determinex_pb_factory_tinycc__tinycc.9b8765d_v1\tinycc__tinycc.9b8765d\tinycc__tinycc.9b8765d.eval.json` |
| `tomarrell__wrapcheck` | 7 | 445 | 70 | `T:\determinex-programbench\determinex_pb_factory_tomarrell__wrapcheck.c058da1_v1\tomarrell__wrapcheck.c058da1\tomarrell__wrapcheck.c058da1.eval.json` |
| `tree-sitter__tree-sitter` | 1212 | 191 | 31 | `T:\determinex-staging\hetzner_returns\hetzner_full_200_20260606\results\tree-sitter__tree-sitter.5e23cca.eval.json` |
| `tstack__lnav` | 822 | 346 | 0 | `T:\determinex-programbench\determinex_pb_factory_tstack__lnav.ee34494_v1\tstack__lnav.ee34494\tstack__lnav.ee34494.eval.json` |
| `unhappychoice__gittype` | 0 | 1 | 0 | `T:\determinex-programbench\mass_run_v2_base\unhappychoice__gittype.34b72d0\unhappychoice__gittype.34b72d0.eval.json` |
| `xorg62__tty-clock` | 119 | 4 | 37 | `T:\determinex-programbench\hetzner_results\hetzner_bottom_wave2_001\results\results\xorg62__tty-clock.f2f847c.eval.json` |
| `yassinebridi__serpl` | 192 | 251 | 0 | `T:\determinex-programbench\determinex_pb_factory_yassinebridi__serpl.c48a9d7_v1\yassinebridi__serpl.c48a9d7\yassinebridi__serpl.c48a9d7.eval.json` |
| `yoav-lavi__melody` | 0 | 1 | 0 | `T:\determinex-programbench\mass_run_v2_base\yoav-lavi__melody.f4af9b4\yoav-lavi__melody.f4af9b4.eval.json` |
| `zevv__duc` | 575 | 431 | 10 | `T:\determinex-programbench\determinex_pb_factory_zevv__duc.a58fa4e_v1\zevv__duc.a58fa4e\zevv__duc.a58fa4e.eval.json` |

## Other / Unresolved

| tool | pile or error | report |
|---|---|---|
| `parcel-bundler__lightningcss` | `UNKNOWN` | `T:\determinex-programbench\mass_run_v2_base\parcel-bundler__lightningcss.aa2ed1e\parcel-bundler__lightningcss.aa2ed1e.eval.json` |
| `osgeo__proj` | `best_report path does not contain task id osgeo__proj: C:\Dev\Determinex\corpus\programbench\locked\tukaani-project__xz.1007bf0\eval_report.json` |  |
