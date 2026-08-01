# ProgramBench Self-Fix Triage — auto-fixable vs flagged

> Generated 2026-06-17 by `determinex_autofix report` over the 56 near-lock (>=95%) tools. Each gap classified reopenable (auto-fixable, with remediation) vs genuine-ceiling (flag for manual/accept).

## Summary
- **Auto-fixable (0 ceiling): 51 tools**
- **Has-ceiling (flag): 5 tools**
- **One-gap quick wins: 15 tools** (1 test from lock)


## FLAGGED — genuine ceiling component (finish manually / accept)

| tool | % | reopenable | ceiling | remediation |
|---|--:|--:|--:|---|
| cslarsen__jp2a | 99.72 | 0 | 2 |  |
| pingu | 99.27 | 0 | 3 |  |
| orf__gping | 98.78 | 4 | 4 | error-string-normalize,pty-allocate |
| tree-sitter__tree-sitter | 97.26 | 29 | 16 | install-dependency,pytest-current-test-routing |
| facebook__zstd | 95.32 | 108 | 2 | install-dependency,locale-pin |

## QUICK WINS — 1 gap, reopenable (push first on Hetzner)

| tool | % | remediation |
|---|--:|---|
| htmlq | 99.95 | (generic) |
| ariga__atlas | 99.94 | pytest-current-test-routing |
| json-tui | 99.89 | pytest-current-test-routing |
| nikolassv__bartib | 99.89 | (generic) |
| monolith | 99.87 | (generic) |
| tailspin | 99.87 | pytest-current-test-routing |
| zip-password-finder | 99.87 | (generic) |
| elfcat | 99.84 | install-dependency |
| incu6us__goimports-reviser | 99.83 | (generic) |
| quinn-rs__quinn | 99.83 | (generic) |
| parqeye | 99.82 | (generic) |
| csview | 99.71 | drop-privileges |
| ngrrram | 99.7 | (generic) |
| cheat__cheat | 99.67 | (generic) |
| doxygen__doxygen | 99.6 | install-dependency |

## ALL AUTO-FIXABLE (by closeness)

| tool | % | n_gaps | remediation |
|---|--:|--:|---|
| htmlq | 99.95 | 1 | (generic) |
| ariga__atlas | 99.94 | 1 | pytest-current-test-routing |
| ripgrep | 99.92 | 2 | (generic) |
| nsh | 99.91 | 2 | pytest-current-test-routing |
| json-tui | 99.89 | 1 | pytest-current-test-routing |
| nikolassv__bartib | 99.89 | 1 | (generic) |
| monolith | 99.87 | 1 | (generic) |
| tailspin | 99.87 | 1 | pytest-current-test-routing |
| zip-password-finder | 99.87 | 1 | (generic) |
| elfcat | 99.84 | 1 | install-dependency |
| incu6us__goimports-reviser | 99.83 | 1 | (generic) |
| quinn-rs__quinn | 99.83 | 1 | (generic) |
| hpjansson__chafa.dd4d4c1 | 99.82 | 5 | scalar-build |
| parqeye | 99.82 | 1 | (generic) |
| alexpovel__srgn | 99.81 | 4 | pytest-current-test-routing |
| quickjs | 99.8 | 6 | install-dependency |
| xz | 99.8 | 4 | (generic) |
| hck | 99.77 | 2 | pytest-current-test-routing |
| csview | 99.71 | 1 | drop-privileges |
| ov | 99.71 | 7 | error-string-normalize,pty-allocate,pytest-current-test-routing |
| ngrrram | 99.7 | 1 | (generic) |
| tuc | 99.68 | 4 | (generic) |
| cheat__cheat | 99.67 | 1 | (generic) |
| xq | 99.65 | 3 | (generic) |
| ducaale__xh | 99.61 | 5 | pytest-current-test-routing |
| doxygen__doxygen | 99.6 | 1 | install-dependency |
| johanneskaufmann__html-to-markdown | 99.59 | 4 | pytest-current-test-routing |
| oppiliappan__statix | 99.58 | 4 | (generic) |
| blake3-team__blake3 | 99.56 | 3 | (generic) |
| eudoxia0__hashcards | 99.45 | 7 | pytest-current-test-routing |
| sd | 99.42 | 5 | (generic) |
| rumdl | 99.37 | 29 | (generic) |
| oha | 99.36 | 7 | install-dependency,pytest-current-test-routing |
| axodotdev__oranda | 99.29 | 7 | pytest-current-test-routing |
| naggie__dstask | 99.12 | 14 | pytest-current-test-routing |
| hush-shell__hush | 98.85 | 15 | remove-collection-cap |
| errcheck | 98.71 | 7 | pytest-current-test-routing |
| chroma | 98.68 | 7 | (generic) |
| madler__pigz | 98.39 | 15 | install-dependency,pytest-current-test-routing |
| elkowar__pipr | 98.32 | 14 | (generic) |
| xorg62__tty-clock | 98.12 | 6 | pytest-current-test-routing |
| luajit__luajit | 98.01 | 63 | install-dependency,pytest-current-test-routing,scalar-build |
| rust-lang__mdbook | 97.92 | 27 | (generic) |
| tarka__xcp | 97.73 | 28 | drop-privileges |
| dandavison__delta | 97.56 | 29 | pytest-current-test-routing |
| arq5x__bedtools2 | 97.16 | 31 | error-string-normalize,install-dependency,pytest-current-test-routing |
| byron__dua-cli | 96.86 | 31 | drop-privileges,pytest-current-test-routing |
| kyoheiu__felix | 95.81 | 41 | pytest-current-test-routing |
| sayanarijit__xplr | 95.63 | 41 | pytest-current-test-routing |
| kyoh86__richgo | 95.48 | 37 | remove-collection-cap |
| astaxie__bat | 95.19 | 70 | error-string-normalize,locale-pin,pytest-current-test-routing |
