---
name: lz4-transfer-map
description: Per cluster tool, what specifically transfers from lz4. The CLI shape is universal; the algorithm is not. Honest accounting of what's reusable.
type: transfer-map
---

# lz4 → Cluster Transfer Map

> **Honest framing**: lz4's *algorithm* doesn't transfer to brotli/zstd/pigz. What transfers is the **CLI shape, file-naming conventions, stream-I/O scaffold, and frame-format mental model**. Each sibling tool requires its own algorithm wiring (or pip-module equivalent).

| Tool | Bench # | Transfer | Specific knowledge that transfers | Additional work |
|------|---------|----------|------------------------------------|-----------------|
| **brotli** | #27 | Partial | Whole CLI argparse table (`-c`, `-d`, `-1..-11`, `-k`, `-f`, stdin/stdout via `-`, suffix `.br`). Filename derivation: `foo` → `foo.br` exactly mirrors `foo.lz4`. Stream chunked I/O loop. `--list` is **NOT** supported by brotli — drop. | `pip install brotli`; algorithm provided. Levels go to 11 not 12. No frame-format details (brotli is not framed, just a stream). No legacy/skippable variants. ~200 LOC swap. |
| **zstd** | #16 | Partial | CLI argparse table (`-c`, `-d`, `-1..-22`, `-k`, `-f`, suffix `.zst`). Stream chunked I/O. Frame mental model carries: zstd has its own frame format with magic `0x28B52FFD`, dictionary support, content-size, skippable frames identical in concept to lz4's. **The skippable-frame parser pattern from lz4 transfers directly.** | `pip install zstandard`; algorithm provided. Wider level range (1-22). `--long=N` for window size — zstd-specific. `--train` mode for dictionary creation (large surface). zstd's `--list` exists; format differs from lz4's. ~400 LOC. Highest test count (2,038) means zstd is expensive even with the CLI scaffold reused. |
| **pigz** | #92 | Partial | CLI argparse (`-c`, `-d`, `-1..-9`, `-k`, `-f`, suffix `.gz`). pigz is parallel gzip. Stream I/O is the same. **Filename derivation, stdout/stdin discipline, and exit-code matrix transfer 1:1.** | `pip install zlib` (stdlib actually). Parallel decompression is the headline feature but PB likely tests serial behavior. `-p N` for thread count. `-z` for zlib not gzip output. No frame-format complexity. ~150 LOC. |
| **BLAKE3** | #65 | Minimal | Stream-input pattern only (read stdin, emit fixed-size hash). Filename arg handling (positional, multiple files, `-`). `-c` stdout convention. No compress/decompress logic. | `pip install blake3`. Output format: hex-default, `--no-names`, length variable (`-l N` for output length). Multi-output streams (`--keyed`, `--derive`). Different test surface entirely; treat as a separate cluster member, not a direct transfer. ~80 LOC. |
| **cmatrix** | #75 | Minimal | Almost no transfer. cmatrix renders the Matrix-style falling glyphs to a terminal. The only commonality with lz4: **stream-output pattern** (write loop with optional flush). Reading flags is similar. | TTY raw mode (overlap with fzf cluster!). Random glyph generation. Color cycling. **Strong overlap with fzf's TTY layer** — consider building cmatrix *after fzf*, not after lz4. ~250 LOC over fzf's `_lib/tty_unix.go`. |

## Re-evaluating cmatrix

cmatrix is in this anchor's cluster only because it sits at #75 and isn't obviously elsewhere. The honest answer: **cmatrix should be built after fzf locks** using fzf's TTY fixture. lz4 contributes nothing to cmatrix.

When the corpus tracker is built, move cmatrix to the **fzf cluster** in the manifest.

## Compounding with already-locked / in-progress

- **zoxide / yj / ripsecrets / htmlq / shellharden / csview / dutree** — none in this cluster's domain. lz4's transfer is forward-only.

## Reusable fixtures to extract after lz4 locks

- `_lib/py/cli_compress.py` — argparse template for compression CLIs (`-c`, `-d`, `-t`, `-l`, `-1..-N`, `-k`, `-f`, `-r`, `-m`, stdin/stdout, suffix detection)
- `_lib/py/streamer.py` — chunked read/write loop with progress hooks, error handling, exit-code mapping
- `_lib/py/naming.py` — input → output filename derivation rules

## Anti-transfer notes

1. **Algorithm is non-portable.** Every compressor is its own beast. The pip-module-wrapping pattern is what transfers.
2. **Dictionary mode** is unique to each compressor (zstd most prominent). Don't try to share.
3. **Parallel decompression** (pigz) has no analog in lz4.
4. **brotli has no `--list` mode**; cmatrix has no compression. The shared fixture must be **opt-in**, not assumed.

## Honest cluster cost

This is the lowest-compounding anchor of the five. The reasoning to still include it:
- 5 tools at average 1,200 tests each → ~6,000 tests theoretically reachable.
- Realistic resolve rate at 100%: **3 of 5** (lz4, brotli, pigz). zstd is high-test-count and harder; cmatrix is in fzf's domain.
- Net: 4 locked tools (lz4 + brotli + pigz + 1 of {zstd, cmatrix}) for the cost of 1 deep anchor study.

If after lz4 locks the cluster sibling math doesn't pan out, **promote zstd to its own anchor study** rather than treating it as a transfer.
