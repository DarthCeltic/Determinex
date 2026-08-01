---
name: pb-locked-zoxide-lessons
description: Post-mortem for ajeetdsouza__zoxide.67ca1bc. Locked at 100% on 2026-05-12 - 577/577 evaluable tests passing across 2 branches. Distills the keyword-matching rule that closed the lock.
type: lessons
---

# zoxide - Lessons

> **Locked**: 2026-05-12. **Score**: 100/100, 577/577. **Branches**: 2 (`a9c8e0729570`, `aa89e180e290`). **Cluster**: peripheral (CLI-only state-machine tool - no obvious cluster siblings).

## TL;DR - what unlocked the last test

The final failing test was `TestQueryKeywordMatching.test_last_keyword_must_be_in_last_component`. Our matcher accepted `zoxide query loc` for a database entry at `/usr/local/bin` because it searched every keyword sequentially across the whole path. Real zoxide matching requires the **final plain keyword**, in normal query mode, to match the **last path component** (basename).

The fix anchored the final keyword to the basename **only for normal, non-interactive queries**, while keeping permissive full-path matching for:
- Interactive queries (where parent-component matches are valid candidates in the selector)
- Keywords that contain a slash or backslash (e.g., `foo/`, `oo/ba`, `test\data`) - those are explicit path-fragment searches and must match the whole path

That single mode + keyword-shape conditional fixed the last failure without regressing anything in the 576 other tests.

## The narrowing journey

Round 1 - over-application: anchor **every** final keyword to basename. Score dropped to **570/577** because it broke `foo/`-style queries that were supposed to match `foo/anywhere-in-path`.

Round 2 - over-relax: revert anchoring entirely. Back to **576/577** with the original failure.

Round 3 (the lock): narrow the rule by **query mode** (`normal` vs `interactive`) AND by **keyword shape** (contains slash/backslash or not). Both conditions must hold before anchoring. **577/577.**

## Lessons

1. **Never trust a single failing test name as the whole rule.** The test name said "last keyword must be in last component" - but the rule is narrower than that wording suggests. It only applies to non-interactive queries with simple (no-slash) keywords. Read the test ASSERTIONS, not the test NAME.
2. **A new conditional with two AND'd terms is almost always safer than a single broader rule.** Going from "always" -> "only when mode == normal AND keyword has no slash" cost a few extra lines of code and saved 7 tests from regression.
3. **The 577/577 lock came in 3 rounds.** First patch was wrong (over-anchored). Second patch was wrong (under-anchored). Third patch - narrow by mode and keyword shape - was right. Don't accept the first patch that ticks one box; rerun the official eval against the full set before declaring victory.

## Surface map (modules covered)

- `tests.test_edit` (46), `tests.test_query` (44), `tests.test_add` (40), `tests.test_edge_cases` (38), `tests.test_init` (36), `tests.test_integration` (36), `tests.test_environment` (34), `tests.test_import` (34), `tests.test_cli_errors` (33), `tests.test_remove` (30), `tests.test_completions` (29), `eval.tests.test_zoxide.TestInitCommand` (27), `tests.test_errors` (23), `eval.tests.test_zoxide.TestQueryCommand` (20), `eval.tests.test_zoxide.TestImportCommand` (18), and ~89 other module entries.
- The closing patch lives inside the query-matching module. All other modules were already passing once the upstream-faithful rewrite was in place.

## Cluster transfer notes

zoxide is **peripheral** - most of its complexity is the SQLite-like state machine for the navigation database plus shell-init script generation (init for bash/zsh/fish/posix/elvish/nushell/xonsh/cmd/powershell). Lessons transferable to siblings:

- **Multi-shell init script generation**: if you reimplement a tool that emits per-shell init scripts (e.g., `starship init <shell>`), expect 8+ distinct output templates whose only valid oracle is the upstream binary's output. Diff per-shell, not per-line.
- **Keyword/path matching by mode + shape**: pattern reusable for any tool that distinguishes "match this token literally" vs "match this token as a path fragment" (e.g., fzf, fd in some flag combinations).
- **Database file format parity**: zoxide writes a binary database file format. Tests check both the format on disk AND query results. Lift the binary-write/read pair carefully - one mis-byte cascades into all read tests.

## Architecture summary

```
main.py
|-- parse_args() - clap-style with `-` separator handling and per-subcommand parsers
|-- DB
|   |-- load()/save() - versioned binary format (header + entries)
|   `-- add/edit/remove/import - frecency math (`rank = freq * 0.5^(age_days/30)`)
|-- query/
|   |-- normal mode - keyword matching with FINAL-KEYWORD-BASENAME-ANCHORING (mode=normal AND no slash)
|   `-- interactive mode - permissive full-path matching, parent components allowed
|-- init/<shell>.tmpl - per-shell init script templates (bash, zsh, fish, posix, elvish, nu, xonsh, cmd, powershell)
`-- completions/<shell> - per-shell completion script emitters
```

## Verifying behavior against upstream

```bash
cd /tmp/zoxide_branch  # extracted from any test branch tarball - has Cargo.toml + src/
cargo build --release
./target/release/zoxide <args>  # use this as ground truth when test goldens disagree
```

