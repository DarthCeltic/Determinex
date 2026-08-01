# ProgramBench Score Breakdown

> Generated: 2026-06-10
> Source: corpus/programbench/eval_index.json (canonical entries only; aliases excluded)
> Official lock definition: passed==total, not_run==0, skipped==0, failed==0, official_full_suite_resolved=True, no eval_override in compile.sh

## Summary

| Bucket | Count | Notes |
|--------|-------|-------|
| **LOCKED 100% (strict_lock)** | **48** | passed==total, zero not_run/skipped/failed |
| Upstream skips (near-locks) | 10 | passed<total only due to upstream pytest.mark.skip |
| Ceiling confirmed | 10 | Structural blockers, not fixable |
| Factory accepted (not yet locked) | 11 | Board improvements, lock criteria not met |
| Pending unlock | 9 | Needs re-eval or archival |
| Board cache only | 114 | No local eval result yet |
| **Total canonical tools** | **201** | |

**Honest score: 48/200 = 24.0% resolved under official metric.**

## Strict Locks (48/200)

| Tool | Passed | Total | Score |
|------|--------|-------|-------|
| angle-grinder | 1143 | 1143 | 100.0% |
| ascii-image-converter | 488 | 488 | 100.0% |
| bartib | 722 | 722 | 100.0% |
| bore | 900 | 900 | 100.0% |
| boyter__scc.515f91c | 476 | 476 | 100.0% |
| clog-cli | 1556 | 1556 | 100.0% |
| cmatrix | 769 | 769 | 100.0% |
| code-minimap | 738 | 738 | 100.0% |
| curlie | 1482 | 1482 | 100.0% |
| deadnix | 1418 | 1418 | 100.0% |
| diffr | 1524 | 1524 | 100.0% |
| dupl | 900 | 900 | 100.0% |
| entr | 1482 | 1482 | 100.0% |
| eva | 963 | 963 | 100.0% |
| fblog | 2254 | 2254 | 100.0% |
| flamelens | 510 | 510 | 100.0% |
| genact | 237 | 237 | 100.0% |
| git-trim | 1422 | 1422 | 100.0% |
| go-mod-outdated | 342 | 342 | 100.0% |
| grex | 3036 | 3036 | 100.0% |
| gron | 233 | 233 | 100.0% |
| hck | 1768 | 1768 | 100.0% |
| hex | 1754 | 1754 | 100.0% |
| hyperfine | 298 | 298 | 100.0% |
| i3-style | 1500 | 1500 | 100.0% |
| jq | 6874 | 6874 | 100.0% |
| loop | 1556 | 1556 | 100.0% |
| miniserve | 880 | 880 | 100.0% |
| muffet | 864 | 864 | 100.0% |
| ngrrram | 664 | 664 | 100.0% |
| nomino | 676 | 676 | 100.0% |
| pastel | 1256 | 1256 | 100.0% |
| pier | 1556 | 1556 | 100.0% |
| rhit | 2176 | 2176 | 100.0% |
| ripsecrets | 937 | 937 | 100.0% |
| rnr | 1480 | 1480 | 100.0% |
| seqtk | 880 | 880 | 100.0% |
| shellharden | 1292 | 1292 | 100.0% |
| stathissideris__ditaa | 681 | 681 | 100.0% |
| tailspin | 1570 | 1570 | 100.0% |
| tex-fmt | 990 | 990 | 100.0% |
| thokr | 507 | 507 | 100.0% |
| tparse | 1112 | 1112 | 100.0% |
| trdsql | 2806 | 2806 | 100.0% |
| xsv | 2634 | 2634 | 100.0% |
| yj | 1457 | 1457 | 100.0% |
| yq | 2046 | 2046 | 100.0% |
| zoxide | 577 | 577 | 100.0% |

## Upstream Skips — Near-Locks (10)

These tools pass all tests except upstream `pytest.mark.skip` tests — not official locks under strict metric.

| Tool | Passed | Total | Skipped | Not_run |
|------|--------|-------|---------|---------|
| chroma | 524 | 531 | 7 | 0 |
| csview | 347 | 348 | 1 | 0 |
| dsq | 1660 | 1666 | 6 | 0 |
| elfcat | 1288 | 1291 | 2 | 1 |
| htmlq | 2057 | 2058 | 1 | 0 |
| quickjs | 3038 | 3044 | 6 | 0 |
| ripgrep | 2536 | 2538 | 2 | 0 |
| sd | 1728 | 1738 | 10 | 0 |
| tuc | 2490 | 2498 | 8 | 0 |
| xq | 876 | 879 | 3 | 0 |

## Ceiling Confirmed (10)

Structural blockers — cannot reach 100% via any compile.sh change.

| Tool | Passed | Total | Reason |
|------|--------|-------|--------|
| dalance__amber | 701 | 868 | Contradictory rc=0/rc=1 assertions between branches for identical invocations. C |
| doxygen__doxygen | 250 | 261 | tests.json for 2 of 3 branches has duplicate test IDs with both eval.tests. and  |
| johanneskaufmann__html-to-markdown | 971 | 1307 | Three branches assert conflicting --version strings ('2.3.4-test' vs 'dev/unknow |
| kyoh86__richgo | 786 | 950 | 36 tests in tests.json have @go_test suffix (e.g., test_wrapper_mode_passing_tes |
| oha | 2116 | 2156 | v15: 2170/2190 (99.1%). 4 permanent upstream-skipped tests (2 harvest tests in b |
| orf__gping | 628 | 735 | 2 irreconcilable ping-missing ENXIO failures (gping doesn't fall back to ping bi |
| rumdl | 1311 | 4542 | v2: 9286/9344 (99.4%). 29 upstream @pytest.mark.skip (gold-env-limitation: SIGPI |
| sharkdp__fd | 418 | 1822 | Root user in container makes all files executable defeating chmod; Python subpro |
| sharkdp__hexyl | 291 | 1270 | --panels=1 produces 8 bytes/row; tests asserting 1 row for 16 bytes are impossib |
| xz | 4060 | 4072 | 2 TTY-dependent failures x2 prefixes (compress_to_stdout_on_tty_error, progress_ |

## Factory Accepted — Not Yet Locked (11)

| Tool | Passed | Total |
|------|--------|-------|
| ast-grep__ast-grep | 17 | 1232 |
| fasttext | 353 | 665 |
| filosottile__age | 137 | 1038 |
| flamelens | 436 | 510 |
| json-tui | 819 | 1208 |
| nikolassv__bartib | 367 | 990 |
| nsh | 2236 | 3371 |
| ov | 3862 | 4195 |
| parqeye | 760 | 920 |
| run | 693 | 1585 |
| sharkdp__bat | 30 | 1178 |
