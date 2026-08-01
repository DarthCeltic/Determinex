---
name: lz4-fuzzing-surface
description: Specific testable behaviors for lz4. Heavy emphasis on filename derivation, stdin/stdout discipline, frame variants (independent/linked, checksum, legacy, skippable), and exit-code matrix.
type: fuzzing-surface
---

# lz4 — Fuzzing Attack Surface

1,829 tests across 12 branches. The 765-test branch likely covers compression/decompression round-trips; the 649-test branch likely covers CLI flag combinations + filename derivation.

## CLI matrix (every flag testable)

### Mode flags
- `-z` compress (default if no mode given)
- `-d` / `--decompress` decompress
- `-t` / `--test` test integrity (decompress to /dev/null)
- `-l` / `--list` print frame info
- `-V` / `--version`, `-h` / `--help`

### Compression level
- `-1`..`-9` (1=fastest, 9=default)
- `-10`..`-12` (HC mode — slower, better)
- `--best` alias for `-9`
- `--fast[=N]` alias for `-1` or `-N`-fast

### Block options
- `-B4`/`-B5`/`-B6`/`-B7` block size (64K, 256K, 1M, 4M); default `-B7` (4M)
- `-BI` block-independent (each block self-contained)
- `-BD` block-linked / dependent (default; better ratio)
- `-BX` block-checksum on (each block has trailing xxh32)
- `--content-size` write decompressed size in header (default on)
- `--no-content-size`
- `--no-frame-crc` disable content checksum
- `--favor-decSpeed`

### File handling
- `-c` to stdout (do not derive filename)
- `-k` keep source file after compression (default)
- `--rm` delete source after success
- `-f` force overwrite of output
- `-m` multiple input files (implicit when >1 positional)
- `-r` recursive (compress directories)
- positional `-` is stdin / stdout
- input ending in `.lz4` (or `.LZ4`) — decompress strips suffix

### Verbosity
- `-v` verbose, `-vv` very-verbose
- `-q` quiet, `-qq` very-quiet (silent)

### Frame variant
- `--legacy` write legacy LZ4 magic (read both transparently)
- `--frame` write modern frame (default)

### Decompression-only
- `--no-sparse` / `--sparse` sparse-file output (size hint)

## Filename derivation rules (tested heavily)

| Mode | Input | `-c`? | Output |
|------|-------|-------|--------|
| compress | `file` | no | `file.lz4` (refuses if exists, unless `-f`) |
| compress | `file` | yes | stdout (no file written) |
| compress | stdin | yes (implied) | stdout |
| compress | stdin | (no flag) | error: must provide `-c` for stdin |
| decompress | `file.lz4` | no | `file` |
| decompress | `file.lz4` | yes | stdout |
| decompress | `file.LZ4` | no | `file` (case-insensitive suffix) |
| decompress | `file` (no .lz4) | no | error: unknown suffix; with `-c` allowed |
| decompress | stdin | yes (implied) | stdout |
| compress | `a b c` (multiple) | no | `a.lz4`, `b.lz4`, `c.lz4` |
| compress | `a b c` | yes | concat to stdout |

**Trap**: many implementations accidentally accept `lz4 file.lz4` as decompression. Reference lz4 still defaults to compress unless `-d` or invoked as `unlz4`/`lz4cat`. Verify behavior in PB tests.

## Stream / frame edges

1. **Empty input** — produces a 7-byte frame: magic(4) + FLG(1) + BD(1) + HC(1) + EndMark(4)... actually empty produces ~11 bytes minimum. Verify exactly with the reference binary.
2. **EOF mid-frame** — `-d` on truncated input emits error to stderr, exits 1. The error message includes the byte offset (`Frame error: ERROR_GENERIC`).
3. **Concatenated frames** — `-d` walks all frames; total output is concat of each frame's decompressed contents.
4. **Skippable frames** — `-d` skips them silently. `-l` lists them with type "skippable".
5. **Legacy magic** detected on read; `-z` writes legacy only with `--legacy`.
6. **Block-checksum** on read: if mismatch, emit "Block checksum mismatch" error.
7. **Content-checksum** on read: if mismatch, emit "Content checksum mismatch" at end-of-frame.

## `-l` / `--list` output format

The list command prints a table:
```
Frames  Type      Block  Compressed   Uncompressed  Ratio  Filename
     1  LZ4Frame   4MB        12345        1048576  0.012  foo.lz4
```

Columns: Frames, Type (LZ4Frame|LZ4Legacy|Skippable), Block (size), Compressed bytes, Uncompressed bytes (or `?` if unknown), Ratio, Filename.

Ratio column rounds to 3 decimals with trailing zeros (e.g. `0.012`, `1.000`). The numeric format is the most common 90→100% sticking point.

## Exit codes

- 0: success
- 1: error (any kind — file not found, frame corruption, write permission, checksum mismatch)
- 2: usage error (bad flag)

## Stderr behavior

- Banner suppressed by `-q`. Default banner format: `*** LZ4 command line interface 64-bits vN.N.N, by Yann Collet ***`. **TEST MAY OR MAY NOT** check banner content; suppress only with `-q` or `-c`-to-stdout.
- Progress lines under `-v`: `Compressed file <name> : <orig> -> <comp> bytes (<ratio>%)`
- Errors: `Error 24 : Frame error : ERROR_GENERIC` (number is internal error code).

## Testable surprise behaviors

1. **`lz4 -dc file.lz4`** = decompress to stdout (combined `-d` and `-c`).
2. **`lz4 -t file.lz4`** = test integrity, exit 0 if good, no output to stdout.
3. **`lz4 file.lz4`** without `-d` = ATTEMPT to compress `file.lz4` to `file.lz4.lz4`. Reference behavior is to refuse if `-f` not given (output exists).
4. **`lz4 -d file.lz4 -c`** = decompress to stdout *and* don't write `file`.
5. **`-vv` shows compression progress per block**; `-v` only shows final stats.
6. **`-f` is required to overwrite an existing output file**, even if `-c` redirects elsewhere — actually no, `-c` to stdout never needs `-f`. Verify edge.
7. **Stdin without `-` positional**: `cat file | lz4 -c > out.lz4` works; `cat file | lz4 > out.lz4` errors (must specify `-c`). Verify in current reference.

## Likely test name structure

- `test_compress_basic`, `test_decompress_basic`, `test_round_trip`
- `test_block_size_64k`, `test_block_size_4m`, `test_block_independent`, `test_block_linked`
- `test_block_checksum`, `test_content_checksum`, `test_no_content_checksum`
- `test_levels_1_through_9`, `test_hc_levels_10_to_12`
- `test_legacy_frame`, `test_skippable_frame`, `test_concatenated_frames`
- `test_filename_derivation_compress`, `test_filename_derivation_decompress`
- `test_stdin_stdout`, `test_multiple_files`, `test_force_overwrite`
- `test_list_mode`, `test_test_mode`, `test_version`, `test_help`
- `test_truncated_frame_error`, `test_corrupt_checksum_error`
- `test_quiet`, `test_verbose`, `test_progress_messages`
