---
name: jq-transfer-map
description: For each tool jq's mastery unlocks, the SPECIFIC algorithm/data-structure/pattern that transfers, plus partial-transfer flags where additional work is needed.
type: transfer-map
---

# jq → Cluster Transfer Map

> "Direct" = anchor's fixture is reusable as-is or near-as-is. "Partial" = pattern transfers but a key component must be re-built.

| Tool   | Bench # | Transfer | Specific knowledge that transfers | Additional work |
|--------|---------|----------|------------------------------------|-----------------|
| **gron**   | #28  | Direct  | The whole `path(f) → ["a", 0, "b"]` machinery from `paths.py`. gron's job is `walk(json) → emit "json[0].a.b = 1;"`. Use jq's `paths` builtin output, format each as a flat assignment line. Add `-u` ungron mode by reversing the format (parse `key = value;` → reconstruct via `setpath`). | gron's ungron parser (one-pass scanner over assignment list); shellsafe-quoting of keys with non-identifier chars. ~150 LOC. |
| **fx**     | #23  | Direct  | The whole filter-evaluator stream model. fx is interactive but the **non-interactive `-l` (lambda) mode** evaluates a JS-like expression over JSON — same evaluator skeleton, different lexer/parser front-end. Reuse `evaluator.py`'s pipe/iterate/select machinery; replace front-end. | A JS-expression-subset parser (~200 LOC). The TUI is a minor concern in PB tests; the test count concentrates on `-l` and pipe modes. |
| **sd**     | #60  | Partial | Reuse jq's `regex.py` (Python `re`) wrapper and `gsub` semantics. sd is `sed`-compatible but treats stdin as a flat byte stream, not JSON values. The transfer is **regex compilation + replacement-string handling** (`$1`, `\1`, `\\`). | Stream-mode flag plumbing (`-s` string mode), `-p` preview, `-n` dry-run. No JSON parsing. ~80 LOC on top of regex module. |
| **xsv**    | #41  | Direct  | The "stream rows through a filter pipeline" pattern from `evaluator.py`. xsv operates on CSV rows where jq operates on JSON values. CSV parsing is stdlib (`csv` module). xsv's `select`, `cat`, `headers`, `count`, `index`, `slice`, `sort`, `frequency`, `stats` map almost 1:1 onto jq builtins of the same names. | A CSV reader/writer wrapping (5 LOC of stdlib `csv`). xsv's `flatten` and `fixlengths` have no jq analog (~50 LOC). |
| **htmlq** *(in progress)* | #57 | Direct | Replace jq's filter compiler with a CSS selector compiler (already chosen — Python's `lxml.cssselect` or hand-rolled). Reuse `emit_json` patterns for `--text`, `--attribute`, `--pretty` (which emits HTML, not JSON, but uses the same "emit collected nodes" abstraction). The hardest jq lesson — **stream of values from a filter** — is exactly htmlq's hardest lesson too. | CSS selector → element predicates (1500-LOC ceiling at 91.6% suggests nesting/combinator tail still needs work). HTML serialization with attribute-order preservation. |
| **dsq**    | #84  | Direct  | Reuse jq's JSON parser (`json_io.py`) for the JSON input adapter. dsq is "embed sqlite3, load JSON/CSV/etc as a table, run user SQL". The transferable piece is **schema inference from JSON** — jq's `paths` + `type` walk is exactly the schema-inference pass dsq needs. | sqlite3 stdlib bindings (1 line); CSV/Parquet/Excel adapters (TSV trivial, Parquet via `pyarrow` if pip ok). The SQL itself is sqlite3, not new code. |
| **trdsql** | #100 | Direct  | Same as dsq. Different author, different language reference (Go), but PB tests check the same surface: read structured input, accept SQL, emit structured output. Reuse the dsq fixture once that lands. | Output formats (LTSV is unique to trdsql but tiny). |

## Compounding with already-locked tools

- **yj (locked)** — yj converts between YAML/JSON/TOML. jq's JSON I/O is one of yj's four formats. **Reuse jq's `json_io.py` directly inside yj's converter.** No additional lift.
- **zoxide (locked)** — no shared code path. zoxide is a `cd`-replacement; stays in the FS-state cluster.
- **ripsecrets (closing)** — no shared code path. ripsecrets is regex-pattern-on-files; closer to fd's surface.
- **htmlq (in progress, 91.6%)** — actively in the jq cluster. The remaining 2.3% is almost certainly nested-selector edge cases that jq's `evaluator.py` model handles cleanly (`for av in eval_filter(a, ctx, val): yield from eval_filter(b, ctx, av)`). Lift htmlq from 91.6% → 100% **after** jq locks, by porting the eval-as-stream pattern in.
- **csview (in progress, ~81%)** — csview is a CSV viewer; reuses xsv's CSV reader pattern. Will lift after jq → xsv lands.

## Transfer-map quality gate

After jq locks at 100%, before starting any cluster sibling:
1. **Audit `evaluator.py`** — extract the pipe/comma/iterate primitives into a separate `stream.py` module. Sibling tools reuse `stream.py` directly.
2. **Audit `regex.py`** — extract into `corpus/programbench/_lib/regex_jq.py` so `sd` can `from corpus_lib.regex_jq import compile, sub`.
3. **Document each fixture's API** in this file's appendix when the time comes.

## Anti-transfer notes (where the pattern doesn't help)

- **fx interactive mode**: jq has no TUI; if PB tests fx interactively, that's net-new work in the fzf cluster style.
- **sd binary mode**: sd can rewrite binary files. jq is text-only. If `-b` mode is tested, that's net-new.
- **dsq output buffering**: dsq streams sqlite3 results; jq's evaluator is fully eager on small inputs. Memory bound differs.
