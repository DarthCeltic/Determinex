# Determinex Lock Portfolio Plan - 26 Families

Date: 2026-05-12

Purpose: build a broad, verified lock portfolio across ProgramBench and parallel coding benches. A lock means official evidence says the task is solved: `passed == total` for ProgramBench, resolved official outcome for SWE-bench, and all tests passing for HumanEval/Windows eval variants.

## Operating Rules

1. Lock one tool at a time unless tasks are truly independent and have disjoint workspaces.
2. Near-locks beat broad runs. Close `>=95%` tools before spending budget on wide generation.
3. Every lock must produce:
   - official eval artifact
   - source/submission archive location
   - failure taxonomy
   - closing patch note
   - corpus lesson
   - scoreboard refresh
   - corpus reseed
   - git commit and push
4. Rounded/display `100` is not a lock. Only exact official pass counts count.
5. After each lock, update this file if the next target changes.

## Current Verified Locks

| Tool | Family | Evidence |
|------|--------|----------|
| htmlq | HTML/XML/document query | 2056/2056 |
| ripsecrets | secret/security scanning | 935/935 |
| zoxide | stateful path/query CLI | 577/577 |
| ripgrep | text search / regex / ignore traversal | 2536/2536 scored |

## Immediate Queue

1. `jq` or `yj` - structured JSON/YAML transform.
2. `lz4` - compression / binary stream fidelity.
3. `curlie` - HTTP/API CLI semantics.
4. `fzf` - interactive fuzzy/TUI behavior.
5. `fd` - filesystem traversal and ignore semantics.

## 26-Family Coverage Map

| # | Family | Anchor/Example | Transfer Value |
|---|--------|----------------|----------------|
| 1 | Text search | ripgrep | regex, glob, ignore files, headings, stats |
| 2 | Filesystem traversal | fd | path filters, symlinks, hidden files |
| 3 | Secret/security scanning | ripsecrets | scanners, allowlists, reporting |
| 4 | HTML/XML query | htmlq | selectors, structured document output |
| 5 | Structured JSON/YAML | jq/yj | parsing, transforms, data output |
| 6 | CSV/tabular data | xsv/qsv family | columns, delimiters, sort/filter |
| 7 | Compression/streaming | lz4 | binary IO, checksums, formats |
| 8 | Archive/package formats | tar/zip-like | metadata, tree reconstruction |
| 9 | HTTP/API CLI | curlie/httpie-like | methods, headers, bodies, status UX |
| 10 | Interactive/TUI | fzf | terminal state, fuzzy selection, previews |
| 11 | Stateful path DB | zoxide | ranking, database state, shell integration |
| 12 | Git/VCS tools | git helper | diffs, branches, repo state |
| 13 | Checksums/hashing | sha/md5-like | binary exactness, streaming |
| 14 | Date/time | date-like | time zones, formatting, relative dates |
| 15 | Process/system | ps/du/df-like | platform-specific system output |
| 16 | Env/config tools | dotenv/env-like | env parsing, shell quoting |
| 17 | Package/dependency tools | npm/cargo/go mod-like | manifests, semantic versions |
| 18 | Database/query CLI | sqlite-ish | SQL output, import/export |
| 19 | Parser/linter | shellharden | lexical states, syntax preservation |
| 20 | Formatter | prettier/rustfmt-like | idempotence, syntax-aware rewrite |
| 21 | Markdown/text render | md/html render | text fidelity, wrapping, tables |
| 22 | Image/media inspect | exif/image tool | binary headers, metadata |
| 23 | Shell completion/init | shell integration tools | generated shell code |
| 24 | Windows-native CLI | powershell/path tools | drive letters, CRLF, codepages |
| 25 | Algorithmic pure code | HumanEval | function-level correctness |
| 26 | Patch/issue repair | SWE-bench | repo diagnosis, minimal patches |

## Parallel Corpora

| Corpus | Lock Definition | Artifact |
|--------|-----------------|----------|
| ProgramBench | official `passed == total` | `eval_report.json` + submission |
| SWE-bench | official resolved instance | patch + test log + report |
| HumanEval | all hidden/visible tests pass | prompt + solution + tests |
| Windows Eval | verified Windows behavior | PowerShell transcript + tests |
| Cloak | uncloaked and cloaked both solve | semantic key + diff + eval |

## Three-Day Push

Day 1:
- `ripgrep` locked at 2536/2536 scored.
- Start structured data (`jq` or `yj`) and compression (`lz4`) reconnaissance.

Day 2:
- Lock one structured-data anchor.
- Lock or push close one binary/streaming anchor.
- Build SWE-bench locked-instance corpus skeleton.

Day 3:
- Lock HTTP/API or interactive/TUI anchor.
- Add HumanEval and Windows-eval corpus templates.
- Produce patent-facing evidence packet: architecture diagram, verification loop, corpus flywheel, privacy/Cloak claims with current evidence and open ablations.

Patent note: this file is an engineering evidence plan, not legal advice. Patent claims should be reviewed by counsel before filing.
