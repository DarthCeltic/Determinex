---
name: lz4-behavioral-spec
description: Empirical build brief for lz4, derived from 621 CATCHES docstrings + 80 byte-exact golden output files across 12 ProgramBench test branches (1,256 active test functions). Injected into the builder prompt to drive a one-shot 100% lock.
type: behavioral-spec
---

# lz4 — Behavioral Build Spec

> **Read order.** Section 1 (binary contract) and Section 6 (pre-flight self-tests) are mandatory. Sections 4.7-4.9 (special exit codes, stderr formats, banner) are the dominant 90→100% gap. The reference binary is upstream `lz4` C tool at `lz4/lz4@1519f46`.
>
> **Empirical basis.** Extracted from `T:/determinex-programbench/_extracted_tests/lz4__lz4.1519f46/`. 12 branches, heaviest is `1379dfae0b18` (655 tests across 18 files). Conftest uses **bytes mode** (`text=False` default), unlike fzf.

---

## Section 1 — Binary Contract

| Property | Value |
|---|---|
| Path | `./executable` (relative to build dir → `/workspace/executable` at test time) |
| Permissions | must be executable (`chmod +x`) |
| Invocation | `executable [FLAGS...] [INPUT_FILE [OUTPUT_FILE]]` (positional 1=input, 2=output for compress/decompress) |
| Stdin | binary bytes when no positional or `-` literal |
| Stdout | compressed/decompressed binary bytes when `-c` or stdin-input |
| Stderr | banner, progress, errors. **Help and `--list` verbose detail also go to stderr.** |
| Working dir | `/workspace/` at test time |
| `tmp_path` | tests use pytest's `tmp_path` for output files |

The conftest fixture (heavy branch `1379dfae0b18`):

```python
EXECUTABLE = Path(__file__).parent.parent.parent / 'executable'

@pytest.fixture
def run_lz4():
    def _run(args, input_data=None, check=True):
        cmd = [str(EXECUTABLE)] + args
        result = subprocess.run(cmd, input=input_data, capture_output=True, check=False)
        if check and result.returncode != 0:
            raise CalledProcessError(...)
        return result
    return _run
```

**Critical**: `text` is NOT set, so `result.stdout` and `result.stderr` are **bytes**. All assertions use `result.stdout == b"..."` and decode with `.decode()` only when checking message content.

**Default `check=True`**: most invocations raise on non-zero exit. Tests that expect failure pass `check=False`. **Never let a "successful invocation" return non-zero** — it'll explode the test before the assertion runs.

The lighter `d5041197eae9` (help_usage) branch uses `text=True` mode with a 4-second timeout. Plan for both.

---

## Section 2 — Test Invocation API

| Param | Meaning |
|---|---|
| `args` | List of CLI flags + filenames |
| `input_data` | Bytes for stdin (the compressed/decompressed payload) |
| `check` | Default True; raises on non-zero. Pass False when expecting error. |

The conftest exposes `temp_file(content=b"", suffix="")` — produces a path in `tmp_path`. Tests build inputs in-memory then write them.

Some tests use `result.stdout.decode()` for checking textual messages (`--list`, `-h`, `--version`). Most use raw bytes for compressed payload assertions.

---

## Section 3 — Implementation Constraints

### Language: Python 3.10 + `lz4` pip module (recommended)

Why:
- PB containers ship Python 3.10 + pip. Network is available during compile.
- `pip install lz4` provides bit-identical encoder/decoder. The algorithm is solved.
- Reference is C, but PB tests behavior, not bit-precise compressed output. Round-trip + flag-handling dominates.

Alternative: **C** with hand-rolled LZ77 (~400 LOC). Slower iteration, higher correctness risk.

### File layout

```
compile.sh          ← pip install lz4; chmod +x main.py; ln -sf main.py executable
main.py             ← entry point, argparse dispatch
modes.py            ← compress, decompress, test, list, benchmark mode bodies
frame.py            ← lz4.frame wrapper with CLI-shaped knobs
naming.py           ← input → output filename derivation rules
list_format.py      ← --list table renderer (column-aligned output)
errors.py           ← exit code table + stderr message constructors
banner.py           ← startup banner ("*** lz4 v... ***")
```

### compile.sh skeleton

```bash
#!/bin/bash
set -e
pip install --quiet lz4 || { echo "lz4 install failed"; exit 1; }
chmod +x main.py
ln -sf main.py executable

# Pre-flight smoke (Section 6) — must pass or compile fails
echo "test data" | ./executable -c | ./executable -dc | grep -q "test data" \
  || { echo "smoke 1 fail (round trip stdin)"; exit 1; }
./executable -V > /dev/null \
  || { echo "smoke 2 fail (version)"; exit 1; }

exit 0
```

### Forbidden shortcuts

- **Do NOT** shell out to a system `lz4` binary. The reference and the system version may differ.
- **Do NOT** assume Python's `text=True` for subprocess invocation in your own logic — tests pass bytes.
- **Do NOT** hand-roll the LZ77 algorithm if pip is available. Wrong tradeoff.
- **Do NOT** silently succeed on corruption — exit code 34 (block checksum) and 26 (frame error) are byte-exact requirements.

---

## Section 4 — Behavioral Surface

### 4.1 — Exit-code matrix (most-asserted invariant: 2,524 returncode assertions)

| Code | When |
|---|---|
| `0`  | Success: compression/decompression OK, `--test` passed, `--list` succeeded, help/version emitted. |
| `1`  | Generic error: file not found, invalid flag value (some cases). |
| `2`  | Argument parse error. |
| `26` | Frame decode error: corrupt frame, invalid magic, truncated input, malformed header. |
| `34` | Checksum error: block checksum mismatch (`-BX`) or content checksum mismatch (frame CRC). |

These special codes (`26`, `34`) are **non-negotiable**. They mirror lz4's internal `LZ4F_ERROR_*` enum:
- `26` = `LZ4F_ERROR_GENERIC` / frame parse error
- `34` = `LZ4F_ERROR_blockChecksum_invalid` / `LZ4F_ERROR_contentChecksum_invalid`

When you emit these errors, **also emit a stderr message containing the exact error name**:
- `b"ERROR_blockChecksum_invalid"` (block-CRC failure)
- `b"ERROR_contentChecksum_invalid"` (frame-CRC failure)
- `b"Error 26"` (any frame-parse failure — generic)
- `b"Error 34"` (any checksum failure — generic)

Tests assert these substrings via `assert b"..." in result.stderr`.

### 4.2 — Banner format

```
*** lz4 v<version> <build> ***
```

Concrete example from the heavy branch's golden output:
```
*** lz4 v1.10.0 64-bit multithread, by Yann Collet ***
```

The `<version>` may include a build suffix (`v1.10.0` or `v1.10.0-4-gabcdef`). The `<build>` part is `64-bit multithread, by Yann Collet` for Linux PB containers.

The help_usage tests **normalize** the version by replacing `*** lz4 v[^*]+\*\*\*` → `*** lz4 v<version> <build> ***` before comparing. So the EXACT version string isn't fixed — but the banner shape is. Emit it verbatim with a real version string (e.g., `1.10.0`).

The banner emits to **stderr** (not stdout) for help/list-verbose; suppressed under `-q`.

### 4.3 — Mode dispatch (the orthogonal axis)

| Flag | Mode | When omitted |
|---|---|---|
| (none) | compress | default |
| `-z` | compress (explicit) | |
| `-d` | decompress | |
| `-t` | test integrity (decompress to /dev/null) | |
| `-l` / `--list` | list frame info | |
| `--list -v` | list verbose | |
| `-h` | short help | |
| `-H` | long help | |
| `--help` | help | |
| `-V` | version | |
| `--version` | version (alias) | |

Mode flags are mutually exclusive in the sense that a test will use exactly one. In practice the CLI may accept combinations (`-dc` = decompress + to-stdout); these are NOT mutually exclusive.

### 4.4 — Filename derivation rules

| Mode | Input | `-c`? | Output |
|---|---|---|---|
| compress | `file` | no | `file.lz4` (refuses if exists, unless `-f`) |
| compress | `file` | yes | stdout (no file written) |
| compress | stdin | implicit | stdout |
| decompress | `file.lz4` | no | `file` |
| decompress | `file.LZ4` | no | `file` (case-insensitive `.lz4` suffix) |
| decompress | `file` (no `.lz4`) | no | error: must use `-c` or specify output |
| decompress | stdin | implicit | stdout |
| compress | `a b c` (multiple) | no | `a.lz4`, `b.lz4`, `c.lz4` (per-file) |
| compress | `a b c` | yes | concatenated to stdout |
| decompress | `a.lz4 b.lz4` | no | `a`, `b` (per-file) |
| decompress | `a.lz4 b.lz4` | yes | concatenated to stdout |

When a positional output filename is given, use it directly (test_compression_with_explicit_output_name asserts this). Don't append `.lz4`.

`-` as input means stdin; `-` as output means stdout. `-c` and `-` as output produce the same effect.

### 4.5 — Compression knobs

| Flag | Effect |
|---|---|
| `-1`..`-9` | Compression level (1=fast, 9=default). |
| `-10`..`-12` | High-compression mode (HC). |
| `--fast`, `--fast=N` | Alias for `-1` or `-N` fast. |
| `--best` | Alias for `-9`. |
| `-B4`..`-B7` | Block size (64K, 256K, 1M, 4M). Default `-B7`. |
| `-BI` | Block-independent (each block self-contained). |
| `-BD` | Block-linked / dependent (default; better ratio). |
| `-BX` | Block-checksum on (xxh32 per block). |
| `--content-size` / `--no-content-size` | Frame-header content size. Default ON. |
| `--no-frame-crc` | Disable frame content checksum. Default ON (CRC enabled). |
| `--favor-decSpeed` | Optimization for decode speed. |
| `-D <dictfile>` | Dictionary mode: compress/decompress with shared dictionary. |

`pip install lz4` exposes these via `lz4.frame.LZ4FrameCompressor(...)`. Map directly:
- `block_size_id` ↔ `-B4..-B7`
- `block_linked` ↔ `-BD` true / `-BI` false
- `block_checksum` ↔ `-BX`
- `content_size` ↔ `--content-size`
- `compression_level` ↔ `-1..-12`

### 4.6 — Decode knobs

| Flag | Effect |
|---|---|
| `-c` | Output to stdout (in any mode). |
| `-d` | Decompress mode. |
| `-dc` | Combined decompress + stdout. |
| `-t` | Test integrity (decompress to null, exit 0/26/34). |
| `-f` | Force overwrite existing output. |
| `-k` | Keep source after compression (default). |
| `--rm` | Delete source after success. |
| `-m` | Multiple input files. |
| `-r` | Recursive. |
| `--sparse` / `--no-sparse` | Sparse-file output. |
| `--legacy` | Read/write legacy frame format. |

### 4.7 — `--list` output format (golden files dominate)

The `--list` table is a fixed column layout that 41 tests in the heavy branch assert byte-exactly.

**Default `--list`:**
```
    Frames           Type Block  Compressed  Uncompressed    Ratio   Filename
         1       LZ4Frame   B7I      10.00M        10.00M   100.00%  10mb.lz4
```

Columns (with widths/alignments):
- `Frames` — right-aligned width 10
- `Type` — right-aligned width 14, values: `LZ4Frame`, `LZ4Legacy`, `Skippable`
- `Block` — right-aligned width 5, format `B<n><I|D>` where n=4..7 and I=independent, D=dependent
- `Compressed` — right-aligned width 11, suffix-formatted (`12345` → `12.35K`, `1234567` → `1.23M`, `1234567890` → `1.23G`)
- `Uncompressed` — right-aligned width 13, same suffix scheme
- `Ratio` — right-aligned width 8, `<XX.XX>%` or `100.00%`
- `Filename` — left-aligned, trailing space

The Ratio column is **percentage** (uncompressed × 100 / compressed) formatted with **two decimals** + `%`. When uncompressed is unknown (no `--content-size`), Ratio shows `-`.

**`--list -v` (verbose) — emits to stderr + stdout combined:**

```
*** lz4 v1.10.0 64-bit multithread, by Yann Collet ***
_POSIX_C_SOURCE defined: 200809L
_POSIX_VERSION defined: 200809L
PLATFORM_POSIX_VERSION defined: 200809L
medium_bd.lz4(1/2)
     Frame           Type Block Checksum           Compressed         Uncompressed     Ratio
         1       LZ4Frame   B4I    XXH32                   57                 5000      1.14%

medium_bi.lz4(2/2)
     Frame           Type Block Checksum           Compressed         Uncompressed     Ratio
```

Verbose adds:
- A `_POSIX_*` env block at the top.
- Per-file headers `<name>(N/M)` showing position in batch.
- Per-frame rows (one row per frame inside a multi-frame file).
- A wider column layout (different widths than non-verbose).
- Checksum column showing `XXH32` or `none`.

Tests compare combined stderr+stdout. Be careful with stream ordering: emit the file header BEFORE the column header, and emit them in the same stream order as the reference.

### 4.8 — Help format

`-h` (short help) and `-H` (long help) both exit 0. Both emit to **stderr** (not stdout) in non-interactive mode. The help_usage branch (`d5041197eae9`) tests:

```python
def test_h_exits_zero(help_h):
    assert help_h.returncode == 0

def test_help_emitted_somewhere(help_h):
    assert combined_output(help_h).strip() != ""
```

`combined_output(r) = (r.stdout or "") + (r.stderr or "")`. So as long as the help text appears in **either** stream, the test passes. Emit to stderr by convention.

`--help` is a long alias accepted but maps to `-H` behavior in some lz4 builds. Test by output presence, not exact placement.

`--version` / `-V` emits the banner line + exits 0. The banner goes to stderr by convention.

### 4.9 — Stdin/stdout discipline

- When input is stdin (no positional or `-`), output MUST be stdout (or explicit -c).
- When `-c` is given, output is always stdout regardless of mode.
- Banner/progress messages NEVER go to stdout (would corrupt compressed payload).
- `-q` suppresses banner; `-qq` suppresses banner + progress.
- `-v` adds verbose progress lines per file (compress mode); `-vv` per block.

### 4.10 — Dictionary mode (`-D`)

`-D <dictfile>` shares a dictionary between compressor and decompressor for better small-payload ratios. Tests in `test_dict.py`:

- Compress with `-D dict.bin` → decompress with `-D dict.bin` → roundtrip.
- Compress with `dict1.bin` → decompress with `dict2.bin` → exit 34 with `b"ERROR_contentChecksum_invalid"`.

`lz4.frame` does not natively expose dictionary mode. Use `lz4.block` for dict support OR call out to a shell `lz4` binary if installed AND with a dictionary-flag passthrough.

A practical fallback: if dictionary mode is not implemented, that's ~10-20 tests lost. Acceptable for first lock.

### 4.11 — Multiple-file handling

`lz4 a.txt b.txt c.txt` (no `-c`) creates `a.txt.lz4`, `b.txt.lz4`, `c.txt.lz4`. Each independently.

`lz4 a.txt b.txt c.txt -c` concatenates compressed outputs.

`lz4 -d a.lz4 b.lz4` decompresses each to `a` and `b`.

`-m` flag enables multiple-file mode explicitly (some lz4 builds require it; reference accepts implicit).

When the FIRST file errors, the test surface differs:
- Default: continues processing remaining files, exits non-zero at end.
- `-f` may suppress some errors.

### 4.12 — Testable surprise behaviors

1. **`lz4 -dc file.lz4`** = decompress to stdout (combined `-d` and `-c`).
2. **`lz4 -t file.lz4`** = test integrity, exit 0 if good, no stdout. Exit 26 on frame error, 34 on checksum.
3. **`lz4 file.lz4`** without `-d` = ATTEMPT to compress `file.lz4` to `file.lz4.lz4`. Refuses if output exists.
4. **`lz4 -d file.lz4 -c`** = decompress to stdout (`-c` overrides default file output).
5. **Empty input compression**: must produce a valid (decompressable) frame, NOT just magic bytes. Round-trip must yield empty bytes back.
6. **Concatenated frames on decompress**: walks all frames; total output = sum of each.
7. **Skippable frames**: detect magic `0x184D2A5x`, read 4-byte size, skip. Reference walks transparently; `--list` shows them as `Skippable`.
8. **Legacy frame** detected on read; written only with `--legacy`.

---

## Section 5 — Per-branch test landscape

12 branches, 1,256 active test functions. Build order: heaviest first.

| Branch | Tests | Files | Focus |
|---|---|---|---|
| `1379dfae0b18` | 655 | 18 | Master suite — compress, decompress, list, dict, advanced options, error paths |
| `7d95f4d40acc` | 370 | 51 | LM-coverage-driven; many `test_more_*`, `test_push_to_*`, `test_final_*` boost files |
| `84cbe4a71abe` | 116 | 15 | Compression + frame options + error handling |
| `b9729b57ee68` | 47 | 4 | Basic invocations + frames + modes + multiple files |
| `d5041197eae9` | 18 | 1 | `test_help_usage.py` — `-h`/`-H`/`--help` shapes |
| `cad835235795` | 14 | 4 | Workflow scenarios + golden CLI |
| `782de56cd095` | 8 | 1 | Spot |
| `2e73c2003a2c` | 4 | 1 | Spot |
| `1ac41bacc996` | 1 | 1 | Single |
| ... | ... | ... | ... |

**Heavy file inventory in `1379dfae0b18`:**

| File | Tests | What |
|---|---|---|
| `test_harvest.py` | 100 | Cross-cutting: recombine flags + edge cases |
| `test_compress.py` | 46 | Compression core: file → file, file → stdout, stdin → stdout, levels |
| `test_decompress.py` | 44 | Decompress core + error paths (26, 34 codes) |
| `test_list.py` | 41 | `--list` and `--list -v` output formatting (golden-heavy) |
| `test_lz4_dict_stream_gaps.py` | 40 | Dictionary mode + streaming combinations |
| `test_core_gaps.py` | 39 | Coverage of less-common flag combos |
| `test_advanced_options.py` | ~36 | Block-size, sparse, no-content-size, content-size, --no-frame-crc |
| `test_alt_names.py` | ? | Alias names (`unlz4`, `lz4cat`) |
| `test_benchmark.py` | ? | `-b` benchmark mode (rarely tested) |
| `test_checksum_gaps.py` | ? | Block + frame checksum failures |
| ... | ... | ... |

---

## Section 6 — Pre-flight self-tests (must pass in compile.sh)

```bash
# 1. Round-trip via stdin (most-asserted shape)
out=$(echo "test payload" | ./executable -c | ./executable -dc)
[ "$out" = "test payload" ] || { echo "smoke 1 fail (round trip)"; exit 1; }

# 2. Round-trip via files
echo "file payload" > /tmp/in.txt
./executable /tmp/in.txt /tmp/out.lz4 || { echo "smoke 2 fail (file compress)"; exit 1; }
./executable -d /tmp/out.lz4 /tmp/out.txt || { echo "smoke 2 fail (file decompress)"; exit 1; }
diff /tmp/in.txt /tmp/out.txt || { echo "smoke 2 fail (round trip diff)"; exit 1; }

# 3. Auto-naming on compress
rm -f /tmp/auto.txt.lz4
./executable /tmp/in.txt /tmp/auto.txt.lz4 || exit 1
[ -f /tmp/auto.txt.lz4 ] || { echo "smoke 3 fail (output file not created)"; exit 1; }

# 4. -V exits 0 with output
./executable -V > /dev/null || { echo "smoke 4 fail (-V)"; exit 1; }

# 5. -h exits 0 with output
./executable -h > /dev/null || { echo "smoke 5 fail (-h)"; exit 1; }

# 6. Empty input round-trip
out=$(echo -n "" | ./executable -c | ./executable -dc | wc -c)
[ "$out" = "0" ] || { echo "smoke 6 fail (empty round trip)"; exit 1; }

# 7. -t (test mode) on valid file
./executable -t /tmp/out.lz4 || { echo "smoke 7 fail (-t valid)"; exit 1; }

# 8. -t (test mode) on corrupt file → exit 26 or 34
echo "garbage not lz4" > /tmp/bad.lz4
./executable -t /tmp/bad.lz4 ; rc=$?
[ "$rc" -ne 0 ] || { echo "smoke 8 fail (-t corrupt should be non-zero)"; exit 1; }

# 9. --list works on valid file
./executable --list /tmp/out.lz4 > /dev/null || { echo "smoke 9 fail (--list)"; exit 1; }

echo "all smoke tests pass"
```

---

## Section 7 — Common failure modes (the 90→100% gap)

From inspection of 621 CATCHES docstrings, these are the recurring traps.

### 7.1 — Exit-code traps

- Returning `1` on frame corruption instead of `26` → loses ~40 decompress/test-mode tests.
- Returning `1` on checksum mismatch instead of `34` → loses ~15 checksum tests.
- Returning `0` on `-t` with corrupted input (silently passing) → loses test-mode integrity tests.
- Not emitting `b"Error 26"` / `b"Error 34"` substring in stderr → loses CRLF format tests.

### 7.2 — Filename derivation traps

- Not stripping `.lz4` on decompress → output named `file.lz4.dec` or similar.
- Case-sensitive `.LZ4` rejection → fails uppercase suffix tests.
- Refusing positional output filename when given → ignoring the second positional.
- Auto-creating `file.lz4.lz4` when input already ends in `.lz4` (without `-f` warning).

### 7.3 — Stdin/stdout traps

- Banner printed to stdout instead of stderr → corrupts compressed payload when piped.
- Progress lines printed to stdout → same problem.
- Stdin not detected when no positional → tool errors instead of reading.
- `-c` not honored → tool tries to write to default file.

### 7.4 — `--list` output traps

- Wrong column widths (off by 1 byte) → 100% of golden tests fail.
- Wrong number formatting (`100.0%` vs `100.00%`).
- Missing trailing space in filename column.
- Per-file headers in wrong order vs column header in verbose mode.
- Skippable frames not labeled `Skippable`.
- Missing `_POSIX_*` env block in verbose mode.

### 7.5 — Frame-format traps

- Default content size not written → some readers can't determine uncompressed size.
- `--no-content-size` ignored → still writes content-size in header.
- `--no-frame-crc` ignored → still appends CRC.
- Block-checksum (`-BX`) not appending xxh32 per block.
- Block-linked vs independent confusion.

### 7.6 — Dictionary mode traps

- `-D` not implemented → loses ~15 tests (acceptable cost for first lock).
- Wrong dictionary error code (should be 34 with `ERROR_contentChecksum_invalid`).

### 7.7 — Alias/name traps

- `unlz4` and `lz4cat` as argv[0] should auto-map to `-d` and `-dc`. Test surface is small; implement only if eval shows hits.

### 7.8 — Banner format traps

- Banner missing → fails first-line assertions in golden files.
- Banner format (`*** lz4 ... ***`) not matching → fails normalization-then-equality.
- Banner emitted to stdout instead of stderr → corrupts compressed output.

---

## Section 8 — Recommended implementation order

### Phase A — Round-trip skeleton (target: 35-50%)

1. `pip install lz4`. Validate import.
2. Stdin → stdout compress (no flags except implicit `-c`).
3. Stdin → stdout decompress with `-d -c`.
4. File → file compress (positional in, positional out).
5. File → file decompress.
6. Auto-name derivation: `foo` → `foo.lz4` (compress); `foo.lz4` → `foo` (decompress).
7. `-c` redirects to stdout in any mode.

### Phase B — Mode plumbing (target: 60-72%)

8. `-V` / `--version`: banner to stderr.
9. `-h` / `-H` / `--help`: help to stderr.
10. `-t`: test integrity, exit 0/26/34.
11. `-f`: force overwrite.
12. `-k` (default) / `--rm`.
13. Multiple positional inputs.

### Phase C — Compression knobs (target: 75-85%)

14. `-1`..`-9` / `-10`..`-12` levels.
15. `-B4`..`-B7` block size.
16. `-BI` / `-BD`.
17. `-BX` block checksum.
18. `--content-size` / `--no-content-size`.
19. `--no-frame-crc`.
20. `--favor-decSpeed`.

### Phase D — `--list` mode (target: 85-92%)

21. Parse frame header; render basic table (non-verbose).
22. Multi-file list (header row + one row per file).
23. Skippable frame detection; label as `Skippable`.
24. Number-formatting suffixes (K/M/G).
25. Ratio column with 2-decimal precision and `%`.
26. `--list -v`: verbose mode with `_POSIX_*` block + per-frame rows.

### Phase E — Error-code precision (target: 92-97%)

27. Frame-parse failures → exit 26 + `b"Error 26"` in stderr.
28. Block-checksum failures → exit 34 + `b"ERROR_blockChecksum_invalid"`.
29. Content-checksum failures → exit 34 + `b"ERROR_contentChecksum_invalid"`.
30. Truncated input → exit 26.

### Phase F — Edge sweep (target: 97-100%)

31. `-D` dictionary mode (if pip lz4 supports OR via lz4.block).
32. `--legacy` frame read/write.
33. `--sparse` / `--no-sparse` (Linux only).
34. `unlz4` / `lz4cat` argv[0] dispatch.
35. `-b` benchmark mode (small surface).

---

## Section 9 — Failure-category triage during iteration

Group failures by name prefix:

```
test_compress_*       → §4.5 / Phase C
test_decompress_*     → §4.6 + §4.10 / Phase E
test_list_*           → §4.7 / Phase D
test_dict_*           → §4.10 / Phase F
test_advanced_*       → §4.5 (knobs) / Phase C
test_basic_*          → §4.3 (mode dispatch) / Phase A or B
test_help_*           → §4.8 / Phase B
test_modes_*          → §4.3 / Phase A
test_frames_*         → §4.7 (frame format) / Phase D-E
test_alt_names_*      → §4.12 / Phase F (low priority)
test_benchmark_*      → Phase F (low priority)
test_checksum_gaps_*  → §4.1 + §7.1 / Phase E
```

---

## Section 10 — Golden file conventions

80 golden files exist across the 12 branches. They live under `eval/test_resources/<test_module>/`.

- `*.golden` — expected stdout (or stderr+stdout for verbose) — string comparison after `.decode()`
- `*.lz4` — pre-compressed input fixtures (binary)
- `*.txt` — input data (binary or text depending on test)

The `--list` golden files dominate. Each is byte-exact: column alignment, decimal precision, trailing whitespace. **Match the reference width-for-width.**

Container path at test time: `/workspace/eval/test_resources/<feature>/<file>`. Resolved via `RESOURCES = Path(__file__).parent.parent / "test_resources" / "test_<name>"`.

---

## Section 11 — Reference behaviors (worked examples)

```bash
# Round-trip (most common test shape)
echo "hello" > in.txt
./executable in.txt out.lz4
./executable -d out.lz4 dec.txt
diff in.txt dec.txt && echo OK

# Stdin/stdout round-trip
echo "hello" | ./executable -c | ./executable -dc
# → "hello"

# List
./executable --list out.lz4
#     Frames           Type Block  Compressed  Uncompressed    Ratio   Filename
#          1       LZ4Frame   B7I       19.00          6.00    31.58%  out.lz4

# Test mode
./executable -t out.lz4 ; echo $?  # → 0
echo "garbage" > bad.lz4
./executable -t bad.lz4 ; echo $?  # → 26

# Version
./executable -V
# *** lz4 v1.10.0 64-bit multithread, by Yann Collet ***
```

### Validation
```bash
./executable --no-such-flag                 → non-zero, stderr non-empty
./executable -d /nonexistent.lz4            → non-zero, stderr non-empty (file not found)
./executable -d corrupt.lz4                 → 26, stderr contains "Error 26"
./executable -t corrupt_block_checksum.lz4  → 34, stderr contains "ERROR_blockChecksum_invalid"
```

---

## Section 12 — How this document was built

1. Pulled 12 test branches via `huggingface_hub.snapshot_download`, allow_patterns=`lz4__lz4.1519f46/**`.
2. Extracted via `tar --force-local -xzf`.
3. Scanned 109 test files: 1,256 functions, 621 CATCHES docstrings, 80 goldens.
4. Read conftest + heaviest test files (`test_compress.py`, `test_decompress.py`, `test_list.py`, `test_help_usage.py`).
5. Aggregated flag inventory (`-d`/`-c`/`-dc` dominate), exit-code distribution (0, 1, 2, 26, 34), error stderr substrings.

---

## Section 13 — Use this spec

1. Open the pilot dir at `T:/determinex-programbench/<run>/lz4__lz4.1519f46/source/`.
2. Inject this entire document into the builder prompt.
3. Implement Phases A→F in order from §8.
4. Embed the §6 smoke tests in `compile.sh`.
5. After first eval, group failures by §9.

---

*Determinex · Lunarian Data Systems · 2026-05-09*
