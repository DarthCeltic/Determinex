---
name: lz4-impl-sequence
description: lz4 build order. Get round-trip working first, then CLI scaffolding, then frame-format edges, then list mode and legacy frames.
type: implementation-sequence
---

# lz4 — Implementation Sequence

## Phase A — Round-trip skeleton (target: 35-50%)

1. **`pip install lz4`** in compile.sh. Validate import.
2. **Compress stdin → stdout** (no flags except `-z` default). Use `lz4.frame.compress(stdin.read())`. Gate: `echo hello | lz4 -c | lz4 -dc` outputs `hello`.
3. **Decompress stdin → stdout** with `-d -c`. Gate: round-trip a known file.
4. **Compress file → file.lz4** (no `-c`). Gate: `lz4 foo` writes `foo.lz4`, leaves `foo` alone (default `-k`).
5. **Decompress file.lz4 → file**. Gate: `lz4 -d foo.lz4` writes `foo`.

## Phase B — Mode flags + filename plumbing (target: 60-75%)

6. **`-c` redirects to stdout in any mode**.
7. **`-f` allows overwriting existing output**.
8. **`-k` (default) keeps source; `--rm` deletes after success**.
9. **Multiple inputs**: `lz4 a b c` → `a.lz4 b.lz4 c.lz4`.
10. **Stdin without `-`** with `-c`: works. Without `-c`: error.
11. **Test mode `-t`**: decompress to /dev/null; exit 0 on success.

## Phase C — Compression knobs (target: 78-86%)

12. **Levels `-1`..`-9`**: pass to `lz4.frame.compress(level=N)`.
13. **HC levels `-10`..`-12`**: same parameter; `lz4.frame` accepts `compression_level=N` up to 12.
14. **Block size `-B4`..`-B7`**: pass `block_size_id=N` (lz4.frame uses `BlockSizeID`).
15. **Block independent `-BI`**: `block_linked=False`.
16. **Block checksum `-BX`**: `block_checksum=True`.
17. **`--no-content-size`**: `content_size=False`.
18. **`--legacy`**: write legacy magic. Note: `lz4.frame` does NOT support legacy by default — implement via `lz4.block` API directly. ~30 LOC.

## Phase D — Frame-decode edges (target: 88-93%)

19. **Concatenated frames on decompress**: loop until EOF. The `lz4.frame.LZ4FrameDecompressor` exposes `unused_data` for trailing bytes — use to detect frame boundaries.
20. **Skippable frames**: detect magic `0x184D2A5x`, read 4-byte size, skip that many bytes. Implement in a manual frame parser around the `lz4.frame` decompressor.
21. **Legacy frame on decompress**: detect legacy magic, switch to `lz4.block.decompress` chunked over 8MB blocks.
22. **Truncated frame error**: catch `RuntimeError` from `lz4.frame.decompress`, emit `Error 24 : Frame error : ERROR_*` shape.

## Phase E — `--list` mode (target: 94-97%)

23. **Parse frame header** without decompressing. The frame magic + FLG + BD + content_size (if set) + HC byte. ~80 LOC.
24. **Format the list table** with column widths matching reference. Test the ratio formatting (3 decimals).
25. **Multi-frame list**: walk all frames in the file, sum compressed/uncompressed.
26. **Skippable in list**: print as `Skippable` type.

## Phase F — Edge sweep (target: 98-100%)

27. **Banner suppression**: print to stderr unless `-q` or output-is-stdout.
28. **Verbose progress lines**: emit per-file at `-v`, per-block at `-vv`.
29. **Recursive `-r`**: `os.walk` directory inputs (rarely tested but present in the spec).
30. **`--favor-decSpeed`**: pass through to compressor (newer lz4.frame supports it).
31. **Argv-name dispatch** (only if tests symlink): `lz4cat` → `-dc`, `unlz4` → `-d`.

## The 90→100% gap

Where this anchor's tail typically lives:

1. **Banner / progress output exact format**. Even one extra space breaks dozens of tests if they grep stderr.
2. **Filename derivation case-sensitivity**: `.LZ4` (uppercase) → strip suffix; `.lZ4` mixed case → varies, verify reference.
3. **`-l` ratio column padding**. Right-align decimals, three places.
4. **Concatenated-frame boundary handling**: ensure the second frame starts at the byte right after EndMark + (optional content_checksum).
5. **Skippable frame in middle of stream** vs at end.
6. **`-c` short-circuiting**: reference lz4 with `-c` and multiple files concatenates compressed output. With `-c -d` decompresses each in order.
7. **Empty input compression**: must produce a valid (decompressable) frame, NOT just the magic bytes.
8. **`--no-frame-crc` interaction with content-checksum-on-decode**: decode must not validate when CRC was disabled at encode.
9. **Stderr-on-error contains file path**: errors mention the input filename.
10. **Exit code 1 on first error in `-m` multi-input**: continue processing other files OR halt? Reference: continues, exits 1 at end.

## Failure-category triage

```
Group A — Round-trip failure (compress→decompress doesn't match input)
Group B — CLI flag plumbing (wrong combination, default mismatch)
Group C — Filename derivation
Group D — Frame-format edges (skippable, legacy, concatenated)
Group E — `-l` listing format
Group F — Banner / verbose / quiet output text
Group G — Exit code mismatch
```

**Group A is fatal — fix before anything else.** If round-trip is broken, every other test fails.
