# htmlq lock

Tool: `mgdm__htmlq.6e31bc8`

Locked on: 2026-06-03

Official ProgramBench eval:

- Score: `100/100`
- Runnable denominator: `2057/2057 passed`
- Extra manifest entries: `0 not_run`, `1 skipped`
- Eval artifact: `eval_report.json`
- Submission artifact: `submission.tar.gz`
- Source: `source/compile.sh` plus upstream Rust source under `source/`

Notes:

- The 1 `skipped` entry is infrastructure-related, not a real test failure.
- The original lock came after building the upstream `htmlq 0.4.0` Rust binary
  (`cargo build --release`) and verifying the Python behavior against it
  byte-for-byte. Two apparently-contradictory `--remove-nodes` tests both
  matched the upstream kuchiki Descendants iterator-invalidation quirk: detaching
  a node that is the matched element's first child ends iteration; detaching a
  deeper or sibling node does not.
- Other load-bearing techniques: html5lib parser with explicit UTF-8 and
  `multi_valued_attributes=None`, alphabetically-sorted attribute serialization
  (html5ever behavior), URL normalization with trailing `/` on bare-host URLs
  and percent-encoded non-ASCII path chars, `--rewrite-links` scoped to
  `<a>`/`<link>`/`<area>` `href` only, void-element handling for pretty-print
  trailing newlines, and clap-2-style focused USAGE for arg-specific errors.
- See `lessons.md` for the full 8-discovery post-mortem and architecture map.
- Executable hash: `322bb78d0eadcd6c`

## NATIVE CONVERSION (2026-06-03)

Converted from Python reimplementation to real Rust upstream
`github.com/mgdm/htmlq` at pinned commit `6e31bc8`. Official ProgramBench eval
raw rows: `2057 passed`, `1 skipped`, no branch errors, no warnings. This
converts the ProgramBench lock archive to the native Rust implementation; it
does not claim release support or family support.
