---
name: pb-lib-fixtures
description: Reusable fixtures extracted from locked anchor tools. Each subdir is per language. Fixtures are vendored into cluster siblings, not imported via package managers (PB containers may not have network at submission time).
type: lib-index
---

# Reusable Fixtures (`_lib/`)

When an anchor tool locks at 100%, distill its reusable parts into this directory. Cluster siblings copy or vendor these fixtures rather than reimplementing.

## Layout

```
_lib/
├── py/    ← Python fixtures (jq cluster, lz4 cluster, mixed)
├── go/    ← Go fixtures (fzf cluster, curlie cluster)
├── rs/    ← Rust fixtures (fd cluster)
└── c/     ← C fixtures (rare; only when stdlib-only mandates it)
```

## Per-language expected fixtures (after all anchors lock)

### `py/`
- `json_io.py` — strict RFC 8259 parser + jq-formatted emitter (from jq lock)
- `stream.py` — pipe/comma/iterate generator skeleton (from jq lock)
- `regex_jq.py` — jq-flag-compatible regex wrapper (from jq lock)
- `paths.py` — JSON path tracking for assignments (from jq lock)
- `cli_compress.py` — argparse template for compression CLIs (from lz4 lock)
- `streamer.py` — chunked I/O loop with progress hooks (from lz4 lock)
- `naming.py` — input → output filename derivation (from lz4 lock)

### `go/`
- `tty_unix.go` — termios raw mode + restore (from fzf lock)
- `render.go` — double-buffered viewport with diff-redraw (from fzf lock)
- `events.go` — keystroke → Action enum decoder (from fzf lock)
- `fuzzy.go` — algo v2 with documented constants (from fzf lock)
- `field.go` — `--delimiter` / `--nth` / `--with-nth` (from fzf lock)
- `httpie_parse.go` — HTTPie-syntax discriminator (from curlie lock)
- `url_normalize.go` — URL-with-defaults normalizer (from curlie lock)
- `curl_invoke.go` — Spec → curl-args + exec (from curlie lock)

### `rs/`
- `sharkdp_cli.rs` — clap derivation template (from fd lock)
- `walker.rs` — `ignore::WalkBuilder` template (from fd lock)
- `color.rs` — sharkdp's color scheme constants (from fd lock)
- `error.rs` — `[<binary> error]: ` prefix formatter (from fd lock)
- `smart_case.rs` — Unicode-aware smart-case detector (from fd lock)
- `exec.rs` — placeholder substitution + spawn loop (from fd lock)
- `httpie_parse.rs` — Rust port of curlie's discriminator (for xh prep)

## Vendoring discipline

When a cluster sibling reuses a fixture:
1. Copy the file into the sibling's `source/` (don't symlink — submissions are tarballs).
2. Cite at top: `// Vendored from corpus/programbench/_lib/rs/walker.rs (fd anchor lock 2026-MM-DD)`
3. If you patch it, **also update the master copy** here AND note the divergence.
