---
name: programbench-families
description: 26-family factory — reusable scaffold generators, micro fixtures, error conventions, and "do not do this" scars for each tool family. Built so Claude can mass-produce per-tool v1 scaffolds without hand-driving each one.
type: corpus
---

> **STATUS NOTE (2026-07-16, audited by Ryan's direct question — "it might be orphaned").**
> Confirmed orphaned relative to the current pipeline: `generator_lib.py::run_cli()` writes
> `main.py` **regardless of family** (rust_cli included) — this whole scaffold-generation half
> of the system produces Python lookalikes, which conflicts with the Native-Only Rule adopted
> after this system was built (last substantive commit `bf52f47fa`, the sprint4 era, predates
> it). Nothing in the current native reimplementation driver
> (`scripts/determinex_pb_reimpl.py`, `scripts/determinex_reimpl_drive.py`) calls into this
> directory. Do not run `scaffold_generator.py` expecting a native-language submission.
>
> The **convention knowledge inside each `FAMILY.md`** (help/version/error-rc/flag shape per
> tool archetype) is NOT orphaned — it's real, hand-verified, and was unused only because
> nothing wired it forward. As of 2026-07-16 it's read by
> `determinex_pb_reimpl.py::_family_conventions_block()` and injected into the native
> reimplementation prompt for any tool that matches a family (via
> `programbench_classify_family.py`), excluding `rust_cli`/`go_cli` (already absorbed into
> `corpus/programbench/language_reference/{rust,go}.md`) and `python_cli`/`node_cli` (not
> native-reimpl targets). See `corpus/programbench/language_reference/` for the language- and
> systems-level grounding layers built alongside this fix.

# 26-Family Factory

> **Why this exists.** Lock-factory sprints 1 & 2 produced +214pp across 9 tools by hand-building each `main.py`. That cadence works but doesn't scale. The 26-family factory captures the *patterns* of per-tool work as reusable family-scoped generators. Claude can then mass-produce baseline v1 scaffolds for new tools by pulling the right family, running its generator against the probe surface, and getting a starting point in ~3 minutes instead of ~30.

## Layout

```
families/
├── README.md                  ← this manifest
├── _template/                 ← copy this to start a new family
│   ├── FAMILY.md              ← purpose, exemplar tools, error conventions
│   ├── common_flags.py        ← module-level shared flag set (--help, --version, etc.)
│   ├── error_conventions.md   ← rc codes, error wordings, when to use which
│   ├── micro_fixtures.py      ← 5-10 deterministic test cases the family ships with
│   ├── known_traps.md         ← "do not do this" — scars from sprint 1/2
│   └── scaffold_generator.py  ← takes (instance_id, probe) → emits main.py + compile.sh
└── wave1/                     ← highest-leverage families (built first)
    ├── rust_cli/
    ├── go_cli/
    ├── python_cli/
    ├── node_cli/
    ├── shell_coreutils/
    ├── git_wrappers/
    ├── file_renamers/
    ├── search_grep/
    ├── text_diff/
    └── formatters/
```

## What each FAMILY.md contains

1. **Purpose** — what tools belong to this family (with examples from sprints 1-2)
2. **Common flags** — flag set every tool in the family supports
3. **Error conventions** — rc codes used, error wording patterns
4. **Test surface shape** — what kinds of tests this family typically faces
5. **Known traps** — concrete "do not do this" rules from our scars
6. **Generator** — pseudocode for the scaffold_generator.py
7. **Exemplar locked tool** — link to the sprint-1/2 result that proves the pattern

## How a sprint operator uses this

```bash
# 1. Find which family a new instance belongs to
python scripts/programbench_classify_family.py <instance_id>
# → e.g. "rust_cli + search_grep"

# 2. Run the family generator against the probe
python corpus/programbench/families/wave1/rust_cli/scaffold_generator.py \
    --instance <instance_id> \
    --probe-from T:/determinex-programbench/mass_run_v2_base/<iid>/<iid>.eval.json \
    --out T:/determinex-programbench/determinex_pb_<tool>_v1/

# 3. Pack, eval, iterate
```

The generator produces a starting scaffold that handles the 80% case (flag parsing, help, version, error wording per family conventions). Per-tool gap-probing then drives the specific 20%.

## The waves

### Wave 1 — highest-leverage (10 families)
| Family | Sprint-1/2 exemplars | Lift achieved |
|---|---|---|
| `rust_cli` | nomino, tex-fmt, tuc, git-trim | +40.03 / +32.93 / +40.03 / +40.57 |
| `go_cli` | cheat | +2.60 (low — Go family less proven) |
| `python_cli` | — | (no sprint-1 wins yet) |
| `node_cli` | — | (TODO) |
| `shell_coreutils` | tuc (cut-alike) | +40.03 |
| `git_wrappers` | git-trim | +40.57 |
| `file_renamers` | nomino | +36.39 |
| `search_grep` | igrep | +29.97 |
| `text_diff` | diffr | +25.70 |
| `formatters` | tex-fmt | +32.93 |

### Wave 2 — common file/text formats
| Family | Notes |
|---|---|
| `json_yaml_toml` | jq is the anchor; htmlq is locked |
| `csv_table` | csview is sprint-residual |
| `regex_tools` | ripgrep is locked; igrep partial |
| `archive_compression` | lz4 anchor |
| `network_http` | curlie anchor |
| `database` | skeema quarantined |
| `config_env` | direnv was sprint-1 (no lift) |
| `tui_terminal` | igrep, fzf anchor |

### Wave 3 — domain-specific
| Family | Notes |
|---|---|
| `latex_document` | tex-fmt is the exemplar |
| `codegen` | svd2rust is sprint-2 (low lift) |
| `compiler_wrappers` | (TODO) |
| `animation_output` | genact is sprint-1 (no lift — quarantine-tier) |
| `benchmark_timing` | hyperfine quarantined |
| `editor_integrated` | cheat needs $EDITOR |
| `package_manager` | (TODO) |
| `security_scanner` | ripsecrets is locked |

## Rule from sprint 3 (locked)

> Go to 100% only when a tool reaches **85+** AND remaining failures are concentrated.
> Otherwise stop at strong partial, record the family lesson, move on.

Sprint 3 proved this: igrep flattened at 73% (TUI tests need pty), diffr partially recovered to 69% (color rendering ceiling), tex-fmt got to ~50%+ (LaTeX wrapping ceiling). All three would have been multi-hour grinds for marginal gains.

## Generation date / state

- Created: 2026-05-14
- After sprint 3 partial close
- Wave 1 in progress
- Waves 2-3 stubs only

## Cross-references

- [[project-lockfactory-pattern]] — proves per-tool >> universal (33×)
- [[feedback-surgical-revert-pattern]] — igrep v2b recovery technique
- [`_strategy/per_language_scaffolds.md`](../_strategy/per_language_scaffolds.md) — the original copy-paste templates the families now formalize
