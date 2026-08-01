# CODEX-ROLLING-007 Staging Manifest

Claim time: 2026-06-11T11:55:35-04:00

Claimed slugs:
- ogham__dog
- samtools__samtools
- stacked-git__stgit
- yoav-lavi__melody

Protocol role: Codex executor. This package is a staging proposal only; driver verifies, dispatches, certifies, archives, and updates canonical state.

## Recon

All four rows are `board_cache_only` in `corpus/programbench/eval_index.json`.

| Tool | Board-cache score | not_run | collected before | target denominator |
|---|---:|---:|---:|---:|
| ogham__dog | 290/1813 | 818 | 995 | 1813 |
| samtools__samtools | 145/1511 | 811 | 700 | 1511 |
| stacked-git__stgit | 491/2380 | 810 | 1570 | 2380 |
| yoav-lavi__melody | 131/1607 | 807 | 800 | 1607 |

Failure class: scaffold-broken. Current vbidir7 tarballs had `collect_ignore_glob` and keyword filtering in `pytest_collection_modifyitems`, suppressing large parts of the test surface.

Applicable patterns:
- Pattern 004: compile.sh must remain LF-only before packing.
- Prior handback change request: tools are part of the mixed-prefix bidir class, so this batch does not attempt a per-tool shared harness fix.

No `results.xml.orig` files existed in extracted sources. The `determinex_bidir` XML injection plugin was preserved.

## Source Tarballs

Original sources:
- dog: `T:\determinex-programbench\determinex_pb_dog_vbidir7\ogham__dog.721440b\submission.tar.gz`
- samtools: `T:\determinex-programbench\determinex_pb_samtools_vbidir7\samtools__samtools.aa823b5\submission.tar.gz`
- stgit: `T:\determinex-programbench\determinex_pb_stgit_vbidir7\stacked-git__stgit.430027d\submission.tar.gz`
- melody: `T:\determinex-programbench\determinex_pb_melody_vbidir7\yoav-lavi__melody.f4af9b4\submission.tar.gz`

## Edits

For each `source/compile.sh`:
- Removed `collect_ignore_glob`.
- Removed keyword-based item filtering and `items[:] = keep`.
- Preserved timeout configuration.
- Preserved `eval/` nodeid normalization.
- Preserved `determinex_bidir` plugin install and XML injection.

## Validation

- Git Bash syntax check passed for all four compile scripts: `C:\Program Files\Git\bin\bash.exe -n`.
- Focused cap/filter grep returned no matches for `collect_ignore`, `items[:] = keep`, `del items`, `test_tui`, `test_tmux`, `test_pty`, `test_interactive`, `test_pexpect`, or `test_curses`.
- LF-only compile.sh confirmed:
  - dog: LF, 5190 bytes
  - samtools: LF, 4796 bytes
  - stgit: LF, 5214 bytes
  - melody: LF, 5122 bytes
- Tar sanity: each `submission.tar.gz` contains root `./compile.sh` and no `target/` members.
- Free space before staging/dispatch decision: C:/ 78.99 GB free, T:/ 891.68 GB free.

Plain `bash -n` was not usable on this workstation because `bash` resolved to WSL and WSL has no installed distro. Git Bash syntax checks were used instead.

## Hashes

| Tool | File | SHA256 |
|---|---|---|
| dog | submission.tar.gz | 08ED513B984CB2E86194D3AA84744772BD7DBAE95EBFDD9202AD36829D28E49D |
| dog | submission.original.tar.gz | CF07C519E8B8A9936869B366A7DBAB3AC5D060630A82F2E43AA4FB2D600A7BC8 |
| dog | source/compile.sh | CE958C91DBB2A1A11FF784A39A89B53951AA091EB26F320F56C01FE6649DA00A |
| samtools | submission.tar.gz | 3813FC80E686066180E0BD9F475056D27BB348A86EBC9944E6ABF625E6EE9555 |
| samtools | submission.original.tar.gz | C672A5568F211EB0BCFFBC88A3C25B63AD8AD9D9CDCBA6073388FB09CA925301 |
| samtools | source/compile.sh | C8C4361F0CA1BAB6D821437303617125A01251F1EED2A33E1C70F9D26D25B867 |
| stgit | submission.tar.gz | D29EAB22984362C012497266F0B08F360A1C42B39D1C25B79B324FF6BC818078 |
| stgit | submission.original.tar.gz | 6EC24DB3F84446BB7CACA73366FB7A0917A1C9E4D214E7C32949A89A81337419 |
| stgit | source/compile.sh | 343751AFBB4CE4F19446715DE9D0E9EE20A9AF256FC9F1ECE6857ADB3BB15585 |
| melody | submission.tar.gz | DBE6E584624F1B71778EE8EB2BCC3BFF9D0B355168E486C1E7B34C49E719178F |
| melody | submission.original.tar.gz | A0052400D703F6D41ED34A6131665AB77563F5C14ADF8604050DFB4AF3741B2F |
| melody | source/compile.sh | BA573E038DD1984D7B67106CD9FBCB3A50ACC4DD94D691FE432B7C7BB11520F3 |

## Eval Status

No local ProgramBench evals were launched for this batch. CODEX-ROLLING-006 already demonstrated local runtime pressure with a 45-minute no-output timeout on treemd. These artifacts are staged for driver/Hetzner dispatch and post-filter failure classification from completed eval reports.
