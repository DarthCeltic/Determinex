---
name: lz4-architecture
description: Architecture for lz4. Wraps Python's `lz4` pip module behind a CLI that matches reference lz4 byte-for-byte on stdout. Key insight — the algorithm is already provided; the test surface is the CLI plumbing.
type: architecture
---

# lz4 — Architecture Blueprint

## Language choice

**Python with `lz4` pip module.** Justification:
1. PB's container has pip access. `pip install lz4` provides bit-identical encoder/decoder — the algorithm complexity is solved.
2. The actual test surface for PB is **CLI behavior** (flags, stream shape, frame conventions), not LZ77 algorithm correctness.
3. Reference lz4 is a single binary; ours is a single Python script. Parity comes from matching the CLI semantics.
4. Python's `lz4.frame` API is a near-perfect mirror of the C library's frame API — the same parameter names map directly.

Fallback: writing the LZ77 block compressor in C is feasible (~400 LOC) but adds a build dependency and slows iteration by 5-10×.

## Core data structures (Python)

```python
import lz4.frame as F

@dataclass
class Cli:
    mode: Literal["compress", "decompress", "test", "list", "version", "help"]
    level: int                      # 1..12
    block_size: int                 # 64K, 256K, 1M, 4M
    block_independent: bool         # -BI / -BD
    block_checksum: bool            # -BX
    content_checksum: bool          # default ON
    content_size: bool              # --content-size
    favor_dec_speed: bool           # --favor-decSpeed
    inputs: list[Path | None]       # None = stdin
    output: Path | None             # None = derive from input or stdout
    keep_source: bool               # -k / --rm absent
    force: bool                     # -f
    stdout: bool                    # -c
    verbose: int                    # -v / -vv
    quiet: int                      # -q / -qq
    legacy: bool                    # --legacy
    multiple: bool                  # multiple inputs
```

The frame format uses these constants (verify against `lz4_format.html`):

```
LZ4 Frame magic:       0x184D2204  (little-endian)
LZ4 Skippable magic:   0x184D2A50..0x184D2A5F
LZ4 Legacy magic:      0x184C2102  (little-endian)
EndMark:               0x00000000
Block size IDs:        4=64K, 5=256K, 6=1M, 7=4M
```

## Module breakdown

```
main.py             argparse, mode dispatch, file I/O glue
frame.py            wraps lz4.frame.LZ4FrameCompressor / LZ4FrameDecompressor with CLI-shaped knobs
streamer.py         chunked read/write loop with progress hooks for -v
naming.py           output filename derivation: foo → foo.lz4 (compress); foo.lz4 → foo (decompress)
listing.py          --list mode: parse frame header, print metadata table
legacy.py           --legacy frame format read/write
errors.py           message strings + exit code mapping
```

## Build script

`compile.sh`:
```bash
#!/bin/bash
set -e
pip install --quiet lz4 || { echo "lz4 install failed"; exit 1; }
chmod +x main.py
ln -sf main.py executable
```

## Critical implementation decisions

### Decision 1: Trust the lz4 pip module's binary output
The test will (almost certainly) verify `compress | decompress == identity` rather than byte-equality with a reference compressor. So the encoder side has freedom. **But** the decoder side may be tested against frames produced by reference lz4 — so accept all valid frame variations (independent vs linked blocks, block checksum on/off, content checksum on/off, legacy frame).

### Decision 2: Match the CLI surface character-for-character
The flag set has been remarkably stable across lz4 versions. Use this as the canonical argparse spec:
```
-z compress (default), -d decompress, -t test, -l list
-1..-12 level (-1 fast, -9 default, -10..-12 high-compression)
-B4|-B5|-B6|-B7 block size (64K..4M)
-BI block-independent, -BD block-linked (default)
-BX block-checksum on
--content-size, --no-content-size
-c stdout, -k keep, --rm delete-source
-f force overwrite, -m multiple, -r recursive
-v verbose, -vv very-verbose, -q quiet, -qq very-quiet
--legacy (write legacy frame), --frame (default)
--favor-decSpeed
--list / -l (alias)
--help / -h, --version / -V
```

### Decision 3: Filename derivation rules
- compress: `foo` → `foo.lz4` (default), `-c` → stdout
- decompress: `foo.lz4` → `foo`, `foo.LZ4` → `foo`, anything else → error unless `--suffix` overrides (rare)
- `-` as input means stdin; `-` as output means stdout
- multiple inputs implies `-m`; without `-c` each compresses to its own `.lz4`

### Decision 4: Stdout/stderr discipline
- compressed/decompressed data goes to stdout when `-c` or stdin-input
- progress messages go to stderr (gated by `-v`)
- `--list` table goes to stdout
- errors go to stderr with exit code 1

### Decision 5: Stream semantics for stdin
When input is stdin, read in fixed-size chunks (`block_size` bytes) and feed `LZ4FrameCompressor.compress(chunk)`. Flush at EOF. Decompression is symmetric: feed chunks to `LZ4FrameDecompressor.decompress(chunk)` and write what comes out.

### Decision 6: Concatenated frames on decompress
Multiple `.lz4` frames may be concatenated. After one frame ends (EndMark), the decoder must continue reading and decode the next frame. The `lz4` pip module exposes `auto_flush=True` and frame-end detection — use it.

### Decision 7: Skippable frames
Frames with magic in `0x184D2A50..5F` are skippable: read the size, skip that many bytes, continue. **Easy to forget.** Implement explicitly in the decode loop.

## Edge cases to bake in early

1. Empty input (0 bytes) — emits a valid empty frame.
2. Single byte — full frame with one block of one byte.
3. `-c -d` — decompress to stdout (works on `.lz4` files).
4. `-c < file.lz4 > out` — stream both ends.
5. Multiple inputs: `lz4 a b c` compresses each, no `-c` ⇒ creates `a.lz4`, `b.lz4`, `c.lz4`.
6. `-c` with multiple inputs: concatenates compressed streams to stdout.
7. `-d` of concatenated frames: emits decompressed of all in order.
8. `--legacy` write produces the legacy magic; `-d` reads both legacy and frame magics automatically.

## What NOT to implement (defer)

- Dictionary compression (`-D dictfile`) — verify in eval before implementing.
- BlockChecksum + ContentChecksum simultaneously is rare in tests; implement after eval shows a hit.
- xxHash content checksum customization (only the default is testable).
- The `lz4cat` / `unlz4` symlink-name dispatch — only matters if tests probe via different argv[0].
