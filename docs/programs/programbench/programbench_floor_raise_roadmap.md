# ProgramBench Floor-Raise Roadmap

Date: 2026-05-21

Goal: move every tool toward the 50-80% band first, then reserve hand-finishing for the hard residuals. No tool is deferred; expensive tools are still listed, but feeder engines and recipe misses go first.

## Current Board

- Overall best: `84736/161099` (`52.5987%`).
- Verified locks: `55`.
- Operating rule: Codex may run one official Docker gate at a time; Claude can keep four lanes saturated. Accepted gates are applied immediately when runnable count is stable.

## Ranking Model

Priority is a hybrid score: expected recoverable tests times recipe confidence. Recipe confidence rises for low-score/high-surface tools, missing or incomplete overrides, available best source, and reusable family engines. It drops for known compiler/interpreter/database cores and TUI-heavy tools. This keeps all tools in scope while doing feeder work first.

## Family Engine Readiness

This section is the missing execution layer: it says whether a family already has a reusable primitive, where it comes from, and what must be built before the highest-ranked tools in that family should be attacked.

| Family | Status | Existing Source | Next Build Step |
|---|---|---|---|
| `json_table` | partial | gron lock-style rewrite + yq floor engine + xsv discovery engine | Extract a shared JSON/YAML/CSV expression/table core, then port to dsq/trdsql before miller/jq. |
| `doc_markup` | partial | html-to-markdown/h2md at 75% and marmite recipe-miss lane in flight | Generalize selector/list/frontmatter/render primitives, then revisit marmite/rumdl/mdbook. |
| `search_filter` | partial | ripgrep locked, igrep at 80%, fd/silver/fzf lessons available | Build a reusable grep/finder option parser and matcher for peco/fd/ctags/srgn. |
| `fs_tree` | partial | dutree at 58%, file tree formatting lessons available | Build inode/stat fixture simulator and tree/table renderer for xcp/gdu/dust/dua/treemd. |
| `fake_activity` | partial | amber/tailspin/loop/pingu floors plus log/activity emitters | Port canned-module runner to genact/fblog/chamber, then exact stream modes. |
| `compression` | seed | lz4 at 25% with safety-wrapper lessons | Create archive header/roundtrip shell for zstd/brotli/7zip/pigz before exact compression. |
| `render_color` | partial | hex/hexyl floors, bat discovery engine, chafa lane activity | Separate pager/config/plain-output engine from syntax/color rendering; use bat/pastel first. |
| `shell_lang` | seed | shellharden locked but it is a formatter, not a general interpreter | Implement CLI shell-pass for hush/lua/luajit/nsh before attempting real interpreters. |
| `git_project` | partial | skeema/go-mod/git-trim/git-graph lessons | Build deterministic fake git/project workspace layer for stgit/ninja/atlas/hostctl. |
| `network_system` | partial | curlie at 78%, hwatch/rhit lanes, request/response translation lessons | Build HTTP/network stub translator for oha/masscan/xh/dog/miniserve style tests. |
| `other_cli` | unbuilt | mixed bag; no single engine | Split into subfamilies after one recovery pass; avoid treating this as one abstraction. |

Status meanings: `partial` means at least one successful tool has a reusable primitive to port; `seed` means useful lessons exist but the family engine still needs construction; `unbuilt` means split the family further before spending a lane.

## Top 40 Damage Targets

| Rank | Tool | Score | Passed | Runnable | Family | Lane | Expected Gain | Conf | Action |
|---:|---|---:|---:|---:|---|---|---:|---:|---|
| 1 | `facebook__zstd.1168da0` | 11.28% | 191 | 1693 | compression | floor-engine | 995 | 0.77 | replace scaffold with reusable family engine, gate once |
| 2 | `johnkerl__miller.8d85b46` | 20.19% | 353 | 1748 | json_table | floor-engine | 871 | 0.67 | cluster failures, port family primitive, gate once |
| 3 | `peco__peco.4e58dad` | 8.23% | 89 | 1081 | search_filter | floor-engine | 668 | 0.85 | replace scaffold with reusable family engine, gate once |
| 4 | `naggie__dstask.ff57396` | 17.18% | 180 | 1048 | search_filter | floor-engine | 554 | 0.77 | replace scaffold with reusable family engine, gate once |
| 5 | `lua__lua.c6b4848` | 11.39% | 117 | 1027 | shell_lang | general-floor | 602 | 0.65 | replace scaffold with reusable family engine, gate once |
| 6 | `luajit__luajit.a553b3d` | 18.27% | 205 | 1122 | shell_lang | general-floor | 581 | 0.65 | replace scaffold with reusable family engine, gate once |
| 7 | `hush-shell__hush.560c33a` | 11.40% | 107 | 939 | shell_lang | general-floor | 551 | 0.65 | replace scaffold with reusable family engine, gate once |
| 8 | `rcoh__angle-grinder.9c2fc88` | 7.29% | 51 | 700 | json_table | floor-engine | 439 | 0.80 | replace scaffold with reusable family engine, gate once |
| 9 | `antonmedv__fx.86d0d34` | 38.58% | 601 | 1558 | json_table | floor-engine | 490 | 0.67 | cluster failures, port family primitive, gate once |
| 10 | `nukesor__pueue.8b9d6fe` | 2.03% | 14 | 688 | network_system | general-floor | 468 | 0.68 | replace scaffold with reusable family engine, gate once |
| 11 | `sharkdp__bat.f822bd0` | 4.59% | 30 | 654 | render_color | fixture-engine | 428 | 0.74 | replace scaffold with reusable family engine, gate once |
| 12 | `rust-lang__mdbook.37273ba` | 20.74% | 213 | 1027 | doc_markup | fixture-engine | 506 | 0.61 | cluster failures, port family primitive, gate once |
| 13 | `shashwatah__jot.a92aad8` | 14.07% | 119 | 846 | other_cli | general-floor | 474 | 0.65 | replace scaffold with reusable family engine, gate once |
| 14 | `epistates__treemd.825c6dd` | 25.86% | 263 | 1017 | fs_tree | floor-engine | 449 | 0.67 | cluster failures, port family primitive, gate once |
| 15 | `sharkdp__fd.40d8eb3` | 34.32% | 418 | 1218 | search_filter | floor-engine | 435 | 0.67 | cluster failures, port family primitive, gate once |
| 16 | `yoav-lavi__melody.f4af9b4` | 16.38% | 131 | 800 | other_cli | general-floor | 429 | 0.65 | replace scaffold with reusable family engine, gate once |
| 17 | `jhspetersson__fselect.c3559ca` | 9.09% | 60 | 660 | other_cli | general-floor | 402 | 0.68 | replace scaffold with reusable family engine, gate once |
| 18 | `zk-org__zk.10d93d5` | 4.44% | 27 | 608 | other_cli | general-floor | 399 | 0.68 | replace scaffold with reusable family engine, gate once |
| 19 | `incu6us__goimports-reviser.81bd549` | 6.23% | 37 | 594 | other_cli | general-floor | 379 | 0.68 | replace scaffold with reusable family engine, gate once |
| 20 | `dundee__gdu.ede21d2` | 28.65% | 263 | 918 | fs_tree | floor-engine | 380 | 0.67 | cluster failures, port family primitive, gate once |
| 21 | `axodotdev__oranda.27d60c7` | 27.88% | 271 | 972 | doc_markup | fixture-engine | 410 | 0.61 | cluster failures, port family primitive, gate once |
| 22 | `osgeo__gdal.0847f12` | 10.59% | 74 | 699 | other_cli | general-floor | 416 | 0.60 | replace scaffold with reusable family engine, gate once |
| 23 | `ffmpeg__ffmpeg.360a402` | 10.24% | 68 | 664 | other_cli | general-floor | 397 | 0.60 | replace scaffold with reusable family engine, gate once |
| 24 | `rochacbruno__marmite.7d4bc2d` | 22.86% | 187 | 818 | doc_markup | fixture-engine | 386 | 0.61 | cluster failures, port family primitive, gate once |
| 25 | `go-critic__go-critic.9aea378` | 16.71% | 122 | 730 | other_cli | general-floor | 389 | 0.60 | replace scaffold with reusable family engine, gate once |
| 26 | `byron__dua-cli.8570c15` | 33.26% | 308 | 926 | fs_tree | floor-engine | 341 | 0.67 | cluster failures, port family primitive, gate once |
| 27 | `hairyhenderson__gomplate.05eb3aa` | 20.33% | 283 | 1392 | other_cli | general-floor | 413 | 0.55 | cluster failures, port family primitive, gate once |
| 28 | `ducaale__xh.4a6e44f` | 16.12% | 113 | 701 | other_cli | general-floor | 378 | 0.60 | replace scaffold with reusable family engine, gate once |
| 29 | `htop-dev__htop.523600b` | 16.00% | 112 | 700 | other_cli | general-floor | 378 | 0.60 | replace scaffold with reusable family engine, gate once |
| 30 | `bootandy__dust.62bf1e1` | 34.77% | 330 | 949 | fs_tree | floor-engine | 335 | 0.67 | cluster failures, port family primitive, gate once |
| 31 | `kyoheiu__felix.95df390` | 16.35% | 113 | 691 | other_cli | general-floor | 371 | 0.60 | replace scaffold with reusable family engine, gate once |
| 32 | `ivanceras__svgbob.6d00ad9` | 0.93% | 4 | 431 | render_color | fixture-engine | 298 | 0.74 | replace scaffold with reusable family engine, gate once |
| 33 | `stathissideris__ditaa.f2286c4` | 0.70% | 3 | 427 | render_color | fixture-engine | 296 | 0.74 | replace scaffold with reusable family engine, gate once |
| 34 | `cmatsuoka__figlet.202a0a8` | 30.73% | 279 | 908 | render_color | fixture-engine | 357 | 0.61 | cluster failures, port family primitive, gate once |
| 35 | `google__brotli.b3dc9cc` | 8.17% | 42 | 514 | other_cli | general-floor | 318 | 0.68 | replace scaffold with reusable family engine, gate once |
| 36 | `cslarsen__jp2a.61d205f` | 19.55% | 139 | 711 | other_cli | general-floor | 359 | 0.60 | replace scaffold with reusable family engine, gate once |
| 37 | `o2sh__onefetch.e5958ce` | 18.29% | 124 | 678 | other_cli | general-floor | 351 | 0.60 | replace scaffold with reusable family engine, gate once |
| 38 | `segmentio__chamber.5f93f5f` | 38.63% | 379 | 981 | fake_activity | floor-engine | 308 | 0.67 | cluster failures, port family primitive, gate once |
| 39 | `jonas__tig.8334123` | 27.16% | 440 | 1620 | other_cli | general-floor | 370 | 0.55 | cluster failures, port family primitive, gate once |
| 40 | `cweill__gotests.2a672c5` | 17.16% | 110 | 641 | other_cli | general-floor | 339 | 0.60 | replace scaffold with reusable family engine, gate once |

## Family Feeder Order

### json_table

Top feeder expected gain from first 10: `1927` tests.
- `johnkerl__miller.8d85b46`: 353/1748 (20.19%), lane `floor-engine`, action: cluster failures, port family primitive, gate once
- `rcoh__angle-grinder.9c2fc88`: 51/700 (7.29%), lane `floor-engine`, action: replace scaffold with reusable family engine, gate once
- `antonmedv__fx.86d0d34`: 601/1558 (38.58%), lane `floor-engine`, action: cluster failures, port family primitive, gate once
- `jqlang__jq.b33a763`: 1394/1521 (91.65%), lane `push-to-lock`, action: cluster residual failures and run focused exactness pass

### doc_markup

Top feeder expected gain from first 10: `1939` tests.
- `rust-lang__mdbook.37273ba`: 213/1027 (20.74%), lane `fixture-engine`, action: cluster failures, port family primitive, gate once
- `axodotdev__oranda.27d60c7`: 271/972 (27.88%), lane `fixture-engine`, action: cluster failures, port family primitive, gate once
- `rochacbruno__marmite.7d4bc2d`: 187/818 (22.86%), lane `fixture-engine`, action: cluster failures, port family primitive, gate once
- `johanneskaufmann__html-to-markdown.3006818`: 742/974 (76.18%), lane `push-to-lock`, action: cluster residual failures and run focused exactness pass
- `crowdagger__crowbook.ea214d7`: 229/731 (31.33%), lane `fixture-engine`, action: cluster failures, port family primitive, gate once
- `typst__typst.88356d0`: 16/740 (2.16%), lane `algorithmic-shell-pass`, action: replace scaffold with reusable family engine, gate once
- `jgm__pandoc.5caad90`: 1/604 (0.17%), lane `algorithmic-shell-pass`, action: replace scaffold with reusable family engine, gate once

### search_filter

Top feeder expected gain from first 10: `3276` tests.
- `peco__peco.4e58dad`: 89/1081 (8.23%), lane `floor-engine`, action: replace scaffold with reusable family engine, gate once
- `naggie__dstask.ff57396`: 180/1048 (17.18%), lane `floor-engine`, action: replace scaffold with reusable family engine, gate once
- `sharkdp__fd.40d8eb3`: 418/1218 (34.32%), lane `floor-engine`, action: cluster failures, port family primitive, gate once
- `ggreer__the_silver_searcher.a61f178`: 555/1191 (46.60%), lane `floor-engine`, action: cluster failures, port family primitive, gate once
- `eliukblau__pixterm.1a93fd5`: 66/458 (14.41%), lane `floor-engine`, action: replace scaffold with reusable family engine, gate once
- `ast-grep__ast-grep.dde0fe0`: 17/350 (4.86%), lane `floor-engine`, action: replace scaffold with reusable family engine, gate once
- `universal-ctags__ctags.243595e`: 171/605 (28.26%), lane `floor-engine`, action: cluster failures, port family primitive, gate once
- `filosottile__age.706dfc1`: 137/554 (24.73%), lane `floor-engine`, action: cluster failures, port family primitive, gate once
- `ksxgithub__parallel-disk-usage.96978ed`: 217/629 (34.50%), lane `floor-engine`, action: cluster failures, port family primitive, gate once
- `konradsz__igrep.aa75630`: 574/703 (81.65%), lane `push-to-lock`, action: cluster residual failures and run focused exactness pass

### fs_tree

Top feeder expected gain from first 10: `1847` tests.
- `epistates__treemd.825c6dd`: 263/1017 (25.86%), lane `floor-engine`, action: cluster failures, port family primitive, gate once
- `dundee__gdu.ede21d2`: 263/918 (28.65%), lane `floor-engine`, action: cluster failures, port family primitive, gate once
- `byron__dua-cli.8570c15`: 308/926 (33.26%), lane `floor-engine`, action: cluster failures, port family primitive, gate once
- `bootandy__dust.62bf1e1`: 330/949 (34.77%), lane `floor-engine`, action: cluster failures, port family primitive, gate once
- `jarun__nnn.cb2c535`: 377/1022 (36.89%), lane `floor-engine`, action: cluster failures, port family primitive, gate once
- `nachoparker__dutree.44e877d`: 558/947 (58.92%), lane `floor-engine`, action: raise to 70-80 then move on
- `tarka__xcp.5e5b448`: 486/841 (57.79%), lane `floor-engine`, action: raise to 70-80 then move on

### fake_activity

Top feeder expected gain from first 10: `793` tests.
- `segmentio__chamber.5f93f5f`: 379/981 (38.63%), lane `floor-engine`, action: cluster failures, port family primitive, gate once
- `dalance__amber.69a0f52`: 552/780 (70.77%), lane `push-to-lock`, action: cluster residual failures and run focused exactness pass
- `nikoladucak__caps-log.2cf2d1e`: 636/1093 (58.19%), lane `floor-engine`, action: raise to 70-80 then move on
- `bensadeh__tailspin.6278437`: 461/785 (58.73%), lane `floor-engine`, action: raise to 70-80 then move on
- `sheepla__pingu.926d475`: 252/413 (61.02%), lane `floor-engine`, action: raise to 70-80 then move on

### compression

Top feeder expected gain from first 10: `1407` tests.
- `facebook__zstd.1168da0`: 191/1693 (11.28%), lane `floor-engine`, action: replace scaffold with reusable family engine, gate once
- `madler__pigz.fe4894f`: 321/837 (38.35%), lane `floor-engine`, action: cluster failures, port family primitive, gate once
- `chirlu__sox.42b3557`: 6/606 (0.99%), lane `algorithmic-shell-pass`, action: replace scaffold with reusable family engine, gate once
- `lz4__lz4.1519f46`: 109/270 (40.37%), lane `floor-engine`, action: cluster failures, port family primitive, gate once

### render_color

Top feeder expected gain from first 10: `2364` tests.
- `sharkdp__bat.f822bd0`: 30/654 (4.59%), lane `fixture-engine`, action: replace scaffold with reusable family engine, gate once
- `ivanceras__svgbob.6d00ad9`: 4/431 (0.93%), lane `fixture-engine`, action: replace scaffold with reusable family engine, gate once
- `stathissideris__ditaa.f2286c4`: 3/427 (0.70%), lane `fixture-engine`, action: replace scaffold with reusable family engine, gate once
- `cmatsuoka__figlet.202a0a8`: 279/908 (30.73%), lane `fixture-engine`, action: cluster failures, port family primitive, gate once
- `sharkdp__hexyl.2e26437`: 291/880 (33.07%), lane `fixture-engine`, action: cluster failures, port family primitive, gate once
- `hpjansson__chafa.dd4d4c1`: 601/1305 (46.05%), lane `fixture-engine`, action: cluster failures, port family primitive, gate once
- `astaxie__bat.17d1080`: 645/1367 (47.18%), lane `fixture-engine`, action: cluster failures, port family primitive, gate once
- `sitkevij__hex.61ae69b`: 579/877 (66.02%), lane `fixture-engine`, action: raise to 70-80 then move on

### shell_lang

Top feeder expected gain from first 10: `2942` tests.
- `lua__lua.c6b4848`: 117/1027 (11.39%), lane `general-floor`, action: replace scaffold with reusable family engine, gate once
- `luajit__luajit.a553b3d`: 205/1122 (18.27%), lane `general-floor`, action: replace scaffold with reusable family engine, gate once
- `hush-shell__hush.560c33a`: 107/939 (11.40%), lane `general-floor`, action: replace scaffold with reusable family engine, gate once
- `nuta__nsh.bdd0702`: 1025/1368 (74.93%), lane `push-to-lock`, action: cluster residual failures and run focused exactness pass
- `php__php-src.c891263`: 27/1293 (2.09%), lane `algorithmic-shell-pass`, action: replace scaffold with reusable family engine, gate once
- `duckdb__duckdb.bdb65ec`: 70/791 (8.85%), lane `algorithmic-shell-pass`, action: replace scaffold with reusable family engine, gate once
- `tinycc__tinycc.9b8765d`: 1148/1597 (71.88%), lane `push-to-lock`, action: cluster residual failures and run focused exactness pass

### git_project

Top feeder expected gain from first 10: `762` tests.
- `stacked-git__stgit.430027d`: 491/1549 (31.70%), lane `general-floor`, action: cluster failures, port family primitive, gate once
- `guumaster__hostctl.d6d9699`: 407/1163 (35.00%), lane `general-floor`, action: cluster failures, port family primitive, gate once
- `git-bahn__git-graph.87b4473`: 178/731 (24.35%), lane `general-floor`, action: cluster failures, port family primitive, gate once
- `ariga__atlas.6d81150`: 515/1259 (40.91%), lane `general-floor`, action: cluster failures, port family primitive, gate once
- `skeema__skeema.6a76243`: 1036/1547 (66.97%), lane `general-floor`, action: raise to 70-80 then move on
- `ninja-build__ninja.cc60300`: 746/1416 (52.68%), lane `general-floor`, action: raise to 70-80 then move on
- `foriequal0__git-trim.07c2f50`: 418/710 (58.87%), lane `general-floor`, action: raise to 70-80 then move on

### network_system

Top feeder expected gain from first 10: `886` tests.
- `nukesor__pueue.8b9d6fe`: 14/688 (2.03%), lane `general-floor`, action: replace scaffold with reusable family engine, gate once
- `tstack__lnav.ee34494`: 4/350 (1.14%), lane `general-floor`, action: replace scaffold with reusable family engine, gate once
- `blacknon__hwatch.edfcb62`: 488/1187 (41.11%), lane `general-floor`, action: cluster failures, port family primitive, gate once
- `hatoo__oha.8dc6349`: 348/834 (41.73%), lane `general-floor`, action: cluster failures, port family primitive, gate once
- `chmln__handlr.90e78ba`: 368/859 (42.84%), lane `general-floor`, action: cluster failures, port family primitive, gate once
- `robertdavidgraham__masscan.b99d433`: 599/1218 (49.18%), lane `general-floor`, action: cluster failures, port family primitive, gate once

### other_cli

Top feeder expected gain from first 10: `4076` tests.
- `shashwatah__jot.a92aad8`: 119/846 (14.07%), lane `general-floor`, action: replace scaffold with reusable family engine, gate once
- `yoav-lavi__melody.f4af9b4`: 131/800 (16.38%), lane `general-floor`, action: replace scaffold with reusable family engine, gate once
- `jhspetersson__fselect.c3559ca`: 60/660 (9.09%), lane `general-floor`, action: replace scaffold with reusable family engine, gate once
- `zk-org__zk.10d93d5`: 27/608 (4.44%), lane `general-floor`, action: replace scaffold with reusable family engine, gate once
- `incu6us__goimports-reviser.81bd549`: 37/594 (6.23%), lane `general-floor`, action: replace scaffold with reusable family engine, gate once
- `osgeo__gdal.0847f12`: 74/699 (10.59%), lane `general-floor`, action: replace scaffold with reusable family engine, gate once
- `ffmpeg__ffmpeg.360a402`: 68/664 (10.24%), lane `general-floor`, action: replace scaffold with reusable family engine, gate once
- `go-critic__go-critic.9aea378`: 122/730 (16.71%), lane `general-floor`, action: replace scaffold with reusable family engine, gate once
- `hairyhenderson__gomplate.05eb3aa`: 283/1392 (20.33%), lane `general-floor`, action: cluster failures, port family primitive, gate once
- `ducaale__xh.4a6e44f`: 113/701 (16.12%), lane `general-floor`, action: replace scaffold with reusable family engine, gate once

## Immediate Operating Plan

1. Keep Claude's four lanes on active official evals and accepted-gate application.
2. Codex owns the floor-raise lane: audit, source recovery, reusable engine patches, pack, and at most one Docker gate at a time.
3. For each candidate: inspect extracted tests, identify reusable family primitive, patch once, pack, gate, apply if accepted, and move on after one or two lifts.
4. Do not chase byte-exact residuals until every recipe-miss tool has either crossed 50% or been tagged as a true hand-specialist wall.
5. Re-run this script after every wave; the target list is expected to change as feeders land.

## Artifact

Machine-readable matrix: `logs/programbench_floor_raise_targets.json`.
