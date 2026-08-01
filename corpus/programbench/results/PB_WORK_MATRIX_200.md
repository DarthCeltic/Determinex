# PB Work Matrix — All 200 Tasks

Joins: official 200-task PB leaderboard + our latest eval.json + per-tool failure clusters + override registry.

## Summary

| Tier | Count | % of 200 |
|------|------:|---------:|
| LOCKED (100%) | 1 | 0.5% |
| Near-lock (95-99%) | 2 | 1.0% |
| Upper (70-94%) | 1 | 0.5% |
| Mid (30-69%) | 17 | 8.5% |
| Floor (1-29%) | 173 | 86.5% |
| Zero (0%) | 1 | 0.5% |
| Unscored | 5 | 2.5% |

**Evaluated: 195 / 200 (97.5%)**
**Resolved (100%): 1 / 200 (0.5%)** — leaderboard primary metric
**Almost (≥95%): 3 / 200 (1.5%)**

**Skipped-only tools (1): zero actual failures, just need infra/test-dep fixes:**
- **sirwart/ripsecrets** (99.79%, 2 skipped): `test_directory_recursion_finds_nested_file depends on test_detects_secret_in_file_and_form`

---

## Tier 1 — LOCK NOW (≥95%, smallest gap)

| rank | tool | our % | pass/fail/skip | gap | top failure | effort | path |
|---:|------|---:|---|---:|---|---|---|
| 3 | BurntSushi/ripgrep | 99.96 | 2537/1/0 | 0.04 | returned_none | XS: fix 1 specific tests (~30 min) | Inspect 1 failures, surgical fix per test |
| 141 | sirwart/ripsecrets | 99.79 | 935/0/2 | 0.21 | None | XS: unblock 2 skipped tests (env or test-dep) (~30-60 min) | Skipped only (2): test_directory_recursion_finds_nested_file depends on test_detects_secret_in_fil |

## Tier 2 — PUSH TO LOCK (70-94%)

| rank | tool | our % | pass/fail/skip | gap | top failure | override | path |
|---:|------|---:|---|---:|---|---|---|
| 78 | anordal/shellharden | 76.32 | 986/306/0 | 23.68 | string_output_mismatch | no | Write/extend override; verify against bench-test-as-oracle |

## Tier 3 — MID (30-69%)

| rank | tool | our % | pass/fail/skip | gap | top failure | override | effort |
|---:|------|---:|---|---:|---|---|---|
| 123 | sclevine/yj | 63.64 | 525/299/1 | 36.36 | other_assertion | no | L: rewrite override + bench-as-oracle (~6-10 hrs) |
| 151 | konradsz/igrep | 50.0 | 352/351/1 | 50.00 | other_assertion | yes | L: rewrite override + bench-as-oracle (~6-10 hrs) |
| 198 | NikolaDucak/caps-log | 46.57 | 530/563/21 | 53.43 | other_assertion | yes | L: rewrite override + bench-as-oracle (~6-10 hrs) |
| 15 | ggreer/the_silver_searcher | 46.56 | 555/636/1 | 53.44 | other_assertion | no | L: rewrite override + bench-as-oracle (~6-10 hrs) |
| 146 | nachoparker/dutree | 45.25 | 433/484/10 | 54.75 | string_output_mismatch | yes | L: rewrite override + bench-as-oracle (~6-10 hrs) |
| 35 | orf/gping | 42.04 | 309/319/4 | 57.96 | other_assertion | yes | L: rewrite override + bench-as-oracle (~6-10 hrs) |
| 14 | sharkdp/hyperfine | 41.95 | 125/173/0 | 58.05 | other_assertion | yes | L: rewrite override + bench-as-oracle (~6-10 hrs) |
| 189 | foriequal0/git-trim | 38.18 | 294/410/0 | 61.82 | rc_mismatch_got1_want0 | yes | L: rewrite override + bench-as-oracle (~6-10 hrs) |
| 138 | oppiliappan/eva | 37.33 | 489/474/0 | 62.67 | rc_mismatch_got1_want0 | yes | L: rewrite override + bench-as-oracle (~6-10 hrs) |
| 111 | mfridman/tparse | 37.25 | 244/312/0 | 62.75 | other_assertion | yes | L: rewrite override + bench-as-oracle (~6-10 hrs) |
| 148 | kyoh86/richgo | 36.32 | 345/441/1 | 63.68 | other_assertion | yes | L: rewrite override + bench-as-oracle (~6-10 hrs) |
| 110 | skeema/skeema | 33.33 | 825/722/80 | 66.67 | other_assertion | yes | L: rewrite override + bench-as-oracle (~6-10 hrs) |
| 70 | eradman/entr | 32.34 | 217/393/1 | 67.66 | other_assertion | yes | L: rewrite override + bench-as-oracle (~6-10 hrs) |
| 80 | sayanarijit/xplr | 31.03 | 270/463/0 | 68.97 | other_assertion | yes | L: rewrite override + bench-as-oracle (~6-10 hrs) |
| 57 | mgdm/htmlq | 30.61 | 630/1427/1 | 69.39 | other_assertion | yes | L: rewrite override + bench-as-oracle (~6-10 hrs) |
| 178 | Isona/dirble | 30.33 | 347/759/2 | 69.67 | other_assertion | no | L: rewrite override + bench-as-oracle (~6-10 hrs) |
| 115 | rs/jplot | 30.13 | 292/410/0 | 69.87 | other_assertion | yes | L: rewrite override + bench-as-oracle (~6-10 hrs) |

## Tier 4 — FLOOR (1-29%)

| rank | tool | our % | pass/fail/skip | top failure | override | effort |
|---:|------|---:|---|---|---|---|
| 196 | ArthurSonzogni/json-tui | 29.97 | 362/457/0 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 92 | madler/pigz | 29.83 | 321/516/2 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 75 | abishekvashok/cmatrix | 29.09 | 274/391/0 | rc_mismatch_got2_want0 | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 126 | blacknon/hwatch | 29.06 | 483/704/3 | other_assertion | no | XL: full override + scaffold rewrite (~10-20 hrs) |
| 106 | gabotechs/dep-tree | 28.58 | 419/720/2 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 188 | codesnap-rs/codesnap | 27.43 | 302/547/4 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 34 | Canop/broot | 27.22 | 236/434/0 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 197 | tomarrell/wrapcheck | 27.18 | 184/480/5 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 1 | junegunn/fzf | 26.66 | 702/510/0 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 96 | astaxie/bat | 26.45 | 464/903/13 | other_assertion | no | XL: full override + scaffold rewrite (~10-20 hrs) |
| 22 | jarun/nnn | 26.31 | 377/644/5 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 2 | jesseduffield/lazygit | 26.25 | 315/444/13 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 175 | wfxr/code-minimap | 24.71 | 105/262/1 | string_output_mismatch | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 145 | oppiliappan/statix | 24.16 | 267/680/4 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 114 | guumaster/hostctl | 23.82 | 407/755/0 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 152 | nikolassv/bartib | 23.64 | 234/673/2 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 128 | Canop/rhit | 23.31 | 307/688/0 | other_assertion | no | XL: full override + scaffold rewrite (~10-20 hrs) |
| 99 | mkj/dropbear | 23.24 | 234/331/6 | other_assertion | no | XL: full override + scaffold rewrite (~10-20 hrs) |
| 74 | cordx56/rustowl | 23.18 | 162/336/7 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 163 | AmmarAbouZor/tui-journal | 22.87 | 518/967/8 | other_assertion | no | XL: full override + scaffold rewrite (~10-20 hrs) |
| 68 | Byron/dua-cli | 22.16 | 308/618/5 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 50 | ariga/atlas | 21.93 | 388/864/3 | other_assertion | no | XL: full override + scaffold rewrite (~10-20 hrs) |
| 87 | antonmedv/walk | 21.82 | 187/349/1 | other_assertion | no | XL: full override + scaffold rewrite (~10-20 hrs) |
| 33 | ninja-build/ninja | 21.77 | 442/973/1 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 118 | sibprogrammer/xq | 21.54 | 240/636/3 | string_output_mismatch | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 171 | zevv/duc | 21.39 | 219/446/9 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 166 | wfxr/csview | 21.26 | 74/273/1 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 8 | sharkdp/fd | 21.24 | 387/831/10 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 139 | git-bahn/git-graph | 20.92 | 178/552/2 | other_assertion | no | XL: full override + scaffold rewrite (~10-20 hrs) |
| 162 | trasta298/keifu | 20.72 | 86/188/4 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 177 | stacked-git/stgit | 20.63 | 491/1058/21 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 190 | axodotdev/oranda | 20.51 | 271/700/4 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 168 | Miserlou/Loop | 20.2 | 226/552/0 | string_output_mismatch | no | XL: full override + scaffold rewrite (~10-20 hrs) |
| 184 | jrnxf/thokr | 19.94 | 130/261/0 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 194 | agourlay/zip-password-finder | 19.88 | 224/567/1 | other_assertion | no | XL: full override + scaffold rewrite (~10-20 hrs) |
| 172 | altdesktop/i3-style | 19.77 | 190/560/0 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 136 | clog-tool/clog-cli | 19.75 | 204/574/0 | other_assertion | no | XL: full override + scaffold rewrite (~10-20 hrs) |
| 54 | bensadeh/tailspin | 19.59 | 201/537/0 | other_assertion | no | XL: full override + scaffold rewrite (~10-20 hrs) |
| 169 | KSXGitHub/parallel-disk-usage | 19.36 | 152/477/1 | other_assertion | no | XL: full override + scaffold rewrite (~10-20 hrs) |
| 187 | brocode/fblog | 19.08 | 307/753/6 | other_assertion | no | XL: full override + scaffold rewrite (~10-20 hrs) |
| 19 | tree-sitter/tree-sitter | 19.07 | 308/375/2 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 95 | segmentio/chamber | 19.0 | 379/600/0 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 32 | jonas/tig | 18.61 | 440/1179/8 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 160 | astro/deadnix | 18.61 | 177/531/1 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 195 | rust-ethereum/ethabi | 18.08 | 226/744/0 | string_output_mismatch | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 39 | bootandy/dust | 17.64 | 200/749/16 | rc_mismatch_got2_want0 | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 98 | kisielk/errcheck | 17.61 | 100/428/4 | other_assertion | no | XL: full override + scaffold rewrite (~10-20 hrs) |
| 153 | yassinebridi/serpl | 17.22 | 88/254/0 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 17 | facebookresearch/fastText | 17.17 | 114/238/0 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 132 | dalance/amber | 16.59 | 144/198/0 | other_assertion | no | XL: full override + scaffold rewrite (~10-20 hrs) |
| 23 | antonmedv/fx | 16.39 | 492/1066/0 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 199 | mibk/dupl | 16.37 | 83/367/0 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 21 | rust-lang/mdBook | 15.68 | 213/813/6 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 76 | quinn-rs/quinn | 15.26 | 123/474/2 | other_assertion | no | XL: full override + scaffold rewrite (~10-20 hrs) |
| 143 | alexpovel/srgn | 15.21 | 376/1137/0 | rc_mismatch_got2_want0 | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 13 | dandavison/delta | 14.99 | 183/468/0 | rc_mismatch_got2_want0 | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 31 | cheat/cheat | 14.98 | 46/260/1 | string_output_mismatch | no | XL: full override + scaffold rewrite (~10-20 hrs) |
| 121 | eudoxia0/hashcards | 14.97 | 239/833/4 | missing_dict_key | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 125 | cslarsen/jp2a | 14.95 | 139/572/3 | other_assertion | no | XL: full override + scaffold rewrite (~10-20 hrs) |
| 107 | cmatsuoka/figlet | 14.92 | 197/711/0 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 176 | kaushiksrini/parqeye | 14.49 | 101/279/1 | rc_unexpected_zero | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 81 | hpjansson/chafa | 14.46 | 406/899/0 | other_assertion | no | XL: full override + scaffold rewrite (~10-20 hrs) |
| 180 | mookid/diffr | 13.53 | 151/631/0 | rc_mismatch_got2_want0 | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 63 | doxygen/doxygen | 13.41 | 35/215/1 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 131 | nuta/nsh | 13.33 | 373/995/12 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 20 | FiloSottile/age | 13.2 | 137/417/50 | rc_mismatch_got1_want0 | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 88 | JohannesKaufmann/html-to-markdown | 13.08 | 171/801/0 | other_assertion | no | XL: full override + scaffold rewrite (~10-20 hrs) |
| 182 | Epistates/treemd | 13.03 | 263/754/5 | other_assertion | no | XL: full override + scaffold rewrite (~10-20 hrs) |
| 185 | ismaelgv/rnr | 12.97 | 103/631/2 | rc_mismatch_got2_want0 | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 113 | hooklift/gowsdl | 12.95 | 76/343/0 | missing_file | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 150 | rust-embedded/svd2rust | 12.64 | 136/249/0 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 26 | direnv/direnv | 12.62 | 127/497/3 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 127 | eliukblau/pixterm | 12.52 | 66/392/0 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 193 | Lymphatus/caesium-clt | 12.45 | 94/520/1 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 73 | cweill/gotests | 12.37 | 110/531/2 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 167 | chmln/handlr | 12.37 | 138/721/6 | rc_mismatch_got2_want0 | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 130 | rbakbashev/elfcat | 12.32 | 88/556/1 | missing_file | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 144 | kyoheiu/felix | 12.3 | 113/578/0 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 174 | psampaz/go-mod-outdated | 12.28 | 42/295/5 | rc_mismatch_got2_want0 | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 61 | ogham/dog | 11.91 | 216/776/3 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 94 | raviqqe/muffet | 11.86 | 60/372/0 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 156 | crowdagger/crowbook | 11.81 | 126/605/0 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 102 | go-critic/go-critic | 11.37 | 107/623/4 | other_assertion | no | XL: full override + scaffold rewrite (~10-20 hrs) |
| 192 | paradigmxyz/solar | 10.58 | 285/970/2 | other_assertion | no | XL: full override + scaffold rewrite (~10-20 hrs) |
| 120 | unhappychoice/gittype | 10.39 | 86/360/3 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 108 | lh3/seqtk | 10.33 | 62/378/0 | string_output_mismatch | no | XL: full override + scaffold rewrite (~10-20 hrs) |
| 142 | Drew-Alleman/DataSurgeon | 10.24 | 68/495/0 | rc_mismatch_got2_want0 | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 40 | ekzhang/bore | 9.97 | 63/296/0 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 122 | rvben/rumdl | 9.84 | 437/761/30 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 105 | samtools/samtools | 9.6 | 145/555/0 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 51 | pemistahl/grex | 9.4 | 253/1152/0 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 183 | pier-cli/pier | 9.29 | 100/675/0 | rc_mismatch_got1_want0 | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 133 | pls-rs/pls | 9.04 | 32/312/6 | string_output_mismatch | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 86 | rs/curlie | 9.03 | 102/639/0 | rc_mismatch_got2_want0 | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 165 | yaa110/nomino | 8.93 | 36/302/0 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 147 | simeg/eureka | 8.68 | 58/337/1 | rc_mismatch_got2_want0 | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 154 | riquito/tuc | 8.64 | 155/931/4 | string_output_mismatch | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 56 | svenstaro/miniserve | 8.53 | 50/389/1 | uncategorized | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 116 | naggie/dstask | 8.49 | 141/906/5 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 79 | yoav-lavi/melody | 8.15 | 131/669/0 | string_output_mismatch | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 69 | dundee/gdu | 7.98 | 131/787/20 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 84 | multiprocessio/dsq | 7.54 | 74/667/3 | rc_mismatch_got1_want0 | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 173 | wintermute-cell/ngrrram | 7.54 | 30/247/0 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 52 | htop-dev/htop | 7.47 | 104/596/0 | rc_mismatch_got1_want0 | no | XL: full override + scaffold rewrite (~10-20 hrs) |
| 181 | shashwatah/jot | 7.46 | 78/735/0 | string_output_mismatch | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 200 | HaliteChallenge/Halite | 7.42 | 36/326/4 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 18 | robertdavidgraham/masscan | 7.39 | 227/991/0 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 158 | Stranger6667/jsonschema | 7.32 | 247/665/0 | rc_mismatch_got0_want1 | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 112 | lfos/calcurse | 7.26 | 108/775/0 | rc_mismatch_got2_want0 | no | XL: full override + scaffold rewrite (~10-20 hrs) |
| 67 | OSGeo/gdal | 7.23 | 74/625/1 | other_assertion | no | XL: full override + scaffold rewrite (~10-20 hrs) |
| 25 | Y2Z/monolith | 7.19 | 81/526/0 | other_assertion | no | XL: full override + scaffold rewrite (~10-20 hrs) |
| 45 | sharkdp/hexyl | 6.93 | 88/792/16 | rc_mismatch_got2_want0 | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 16 | facebook/zstd | 6.85 | 191/1502/11 | rc_mismatch_got2_want0 | no | XL: full override + scaffold rewrite (~10-20 hrs) |
| 46 | lua/lua | 6.82 | 117/910/2 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 191 | elkowar/pipr | 6.74 | 50/145/0 | other_assertion | no | XL: full override + scaffold rewrite (~10-20 hrs) |
| 64 | sharkdp/pastel | 6.67 | 98/1058/0 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 119 | xorg62/tty-clock | 6.43 | 22/193/1 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 117 | sigoden/argc | 6.3 | 69/597/34 | rc_mismatch_got2_want0 | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 149 | rochacbruno/marmite | 6.28 | 87/731/3 | boolean_false | no | XL: full override + scaffold rewrite (~10-20 hrs) |
| 186 | sitkevij/hex | 6.26 | 78/799/0 | rc_mismatch_got2_want0 | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 89 | TheZoraiz/ascii-image-converter | 6.19 | 30/440/1 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 29 | XAMPPRocky/tokei | 5.74 | 51/493/2 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 157 | WGUNDERWOOD/tex-fmt | 5.6 | 33/461/1 | rc_mismatch_got2_want0 | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 71 | LuaJIT/LuaJIT | 5.58 | 205/917/0 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 55 | ducaale/xh | 5.51 | 78/623/3 | rc_mismatch_got2_want0 | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 37 | lz4/lz4 | 5.49 | 99/1013/2 | rc_mismatch_got2_want0 | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 101 | sheepla/pingu | 5.45 | 28/385/6 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 65 | BLAKE3-team/BLAKE3 | 5.26 | 36/311/3 | string_output_mismatch | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 72 | mgechev/revive | 5.23 | 49/548/0 | rc_mismatch_got2_want0 | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 53 | peco/peco | 5.22 | 89/991/0 | rc_mismatch_got2_want0 | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 164 | incu6us/goimports-reviser | 4.95 | 37/557/3 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 43 | hatoo/oha | 4.71 | 56/778/4 | rc_mismatch_got2_want0 | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 155 | ecumene/rust-sloth | 4.5 | 26/397/4 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 27 | google/brotli | 4.4 | 42/472/0 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 38 | o2sh/onefetch | 4.3 | 57/621/2 | rc_mismatch_got2_want0 | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 134 | Esubaalew/run | 4.27 | 67/605/0 | string_output_mismatch | no | XL: full override + scaffold rewrite (~10-20 hrs) |
| 62 | danmar/cppcheck | 3.93 | 100/889/28 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 100 | noborus/trdsql | 3.91 | 69/930/1 | rc_mismatch_got1_want0 | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 60 | chmln/sd | 3.87 | 48/816/5 | rc_mismatch_got1_want0 | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 91 | ip7z/7zip | 3.0 | 37/489/0 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 161 | sstadick/hck | 2.64 | 30/825/1 | rc_mismatch_got1_want0 | no | XL: full override + scaffold rewrite (~10-20 hrs) |
| 170 | hush-shell/hush | 2.6 | 42/897/0 | rc_mismatch_got2_want0 | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 5 | sharkdp/bat | 2.55 | 30/624/23 | rc_mismatch_got1_want0 | no | XL: full override + scaffold rewrite (~10-20 hrs) |
| 41 | BurntSushi/xsv | 2.48 | 38/1042/1 | other_assertion | no | XL: full override + scaffold rewrite (~10-20 hrs) |
| 12 | jqlang/jq | 2.13 | 133/1368/0 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 59 | universal-ctags/ctags | 2.11 | 55/550/27 | rc_mismatch_got2_want0 | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 4 | FFmpeg/FFmpeg | 2.08 | 68/596/0 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 97 | zk-org/zk | 2.03 | 27/411/15 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 82 | jhspetersson/fselect | 1.72 | 60/600/40 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 90 | hairyhenderson/gomplate | 1.49 | 52/1340/0 | rc_mismatch_got1_want0 | no | XL: full override + scaffold rewrite (~10-20 hrs) |
| 66 | Nukesor/pueue | 1.39 | 14/428/13 | rc_mismatch_got2_want0 | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 30 | ast-grep/ast-grep | 1.38 | 17/333/0 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 137 | tarka/xcp | 1.36 | 20/821/2 | missing_file | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 48 | sqlite/sqlite | 0.95 | 135/491/0 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 58 | parcel-bundler/lightningcss | 0.87 | 32/862/4 | rc_mismatch_got2_want0 | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 28 | tomnomnom/gron | 0.86 | 2/231/0 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 47 | johnkerl/miller | 0.82 | 130/1618/2 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 6 | typst/typst | 0.79 | 16/724/3 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 85 | rcoh/angle-grinder | 0.74 | 11/689/0 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 83 | ivanceras/svgbob | 0.72 | 4/427/0 | subprocess_failed | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 124 | arq5x/bedtools2 | 0.66 | 7/342/1 | string_output_mismatch | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 93 | tinycc/tinycc | 0.56 | 13/1584/2 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 129 | stathissideris/ditaa | 0.44 | 3/424/0 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 36 | svenstaro/genact | 0.42 | 1/229/0 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 135 | chirlu/sox | 0.41 | 6/570/0 | rc_mismatch_got2_want0 | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 44 | tstack/lnav | 0.4 | 4/346/0 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 24 | mikefarah/yq | 0.35 | 8/649/0 | rc_mismatch_got2_want0 | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 140 | gromacs/gromacs | 0.32 | 4/336/10 | other_assertion | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 10 | duckdb/duckdb | 0.28 | 17/774/104 | rc_mismatch_got2_want0 | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 49 | boyter/scc | 0.21 | 1/348/1 | rc_mismatch_got1_want0 | no | XL: full override + scaffold rewrite (~10-20 hrs) |
| 9 | php/php-src | 0.18 | 27/879/2 | rc_mismatch_got2_want0 | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 103 | OSGeo/PROJ | 0.05 | 3/590/107 | missing_file | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |
| 7 | jgm/pandoc | 0.02 | 1/603/0 | rc_mismatch_got2_want0 | yes | L+: override flat; deeper diagnosis (~8-12 hrs) |

## Tier 5 — ZERO (evaluated but 0%)

| rank | tool | tests | top failure | effort |
|---:|------|---:|---|---|
| 42 | bellard/quickjs | 3036 | rc_mismatch_got2_want0 | L+: override flat; deeper diagnosis (~8-12 hrs) |

## Tier 6 — UNSCORED (no scaffold or no eval yet)

| rank | tool | lang | stars | tests | frontier % | effort |
|---:|------|---|---:|---:|---:|---|
| 77 | alecthomas/chroma | go | 4910 | 503 | 41.7 | M: scaffold+probe (2-4 hrs) |
| 104 | noborus/ov | go | 1935 | 1854 | 87.6 | L: scaffold+probe (4-8 hrs) |
| 109 | tukaani-project/xz | c | 1522 | 1410 | 84.7 | M: scaffold+probe (2-4 hrs) |
| 159 | rhysd/kiro-editor | rs | 761 | 595 | 95.3 | M: scaffold+probe (2-4 hrs) |
| 179 | YS-L/flamelens | rs | 622 | 224 | 62.1 | M: scaffold+probe (2-4 hrs) |

---

## How to use this matrix

- **Tier 1**: easiest 100%-resolutions. Each one = one Resolved leaderboard slot.
- **Tier 2**: high-confidence locks with override work.
- **Tier 3**: write/extend overrides + bench-test-as-oracle.
- **Tier 4**: full override + scaffold-rewrite passes.
- **Tier 5/6**: generate scaffolds first (factory mass-run).

Refresh: `python scripts/analysis/per_tool_failures.py && python scripts/analysis/pb_work_matrix.py`
