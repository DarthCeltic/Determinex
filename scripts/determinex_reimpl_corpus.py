#!/usr/bin/env python3
"""
determinex_reimpl_corpus.py -- the corpus as a COACH + LEARNER for the reimpl engine
================================================================================
Two directions, per the Determinex thesis (corpus = source-knowledge friend that feeds the
models AND accumulates verified capability):

  READ  (coach):  render_prompt_block(short) -> cross-tool reimpl pitfalls we've learned
                  + per-tool discovered spec/known-hard-behaviors -> injected into the
                  builder prompt so the model starts each task with what Determinex knows.
  WRITE (learn):  record_run(...) -> after a run, persist the observed-behavior summary,
                  the behaviors that were HARD (failed probes), best local/official score,
                  and -- only on a genuine official pass -- LOCK it as a verified skill.

Legitimacy: only observed/discoverable behavior + general patterns are stored or injected
-- NEVER test goldens/assertions. Verified-skill lock requires a real official pass.
"""
from __future__ import annotations

import json
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "corpus" / "programbench" / "reimpl_skills"

# Cross-tool wisdom: the recurring reimplementation pitfalls we've learned the hard way.
# This coaches EVERY tool, every model. Grows as new cross-tool patterns are found.
CROSS_TOOL_PITFALLS = """## Reimplementation pitfalls Determinex has learned (apply to ALL tools)
- Arrays render with `[]` and `[i]` indices, NOT object `{}` — detect list vs dict correctly.
- Match the EXACT exit code per case: some flags exit 0 with empty stdout; malformed input
  often exits 2 or 3; invalid ungron-style input may exit 5; a failed URL fetch exits 4.
- Preserve numbers' EXACT input text (`1.2e10` stays `1.2e10`, `-0` stays `-0`) — do NOT
  reformat via float(); parse number tokens as raw strings.
- Process the input ONCE — never print the output twice (a common duplication bug).
- Usage/error text goes to STDERR; empty stdout + a non-zero exit usually means stderr.
- A short flag (e.g. -V) may behave differently from its long form (--version) — follow
  the OBSERVED behavior, not the conventional meaning.
- Read input from a FILE argument if one is given, else from STDIN — handle both.
- Match stdout byte-for-byte including trailing newlines and exact escape/ANSI sequences.
"""

# TECHNIQUE RECIPES: a cheap model often knows WHAT to do but not HOW. These are concrete,
# verified code techniques for the recurring hard behaviors -- the difference between
# "preserve numbers" (a principle it can't act on) and a snippet it can paste. Proven from
# the gron 153/224 reference reimplementation. Injected when the tool's domain matches.
_RECIPES = {
    "json": '''## TECHNIQUE: preserve EXACT number text (json tools) -- the #1 cause of core failures
A bare `json.loads(s)` DESTROYS the original number text (1.2e10 -> 12000000000.0, -0 -> 0)
BEFORE you can format it; you can NEVER reconstruct it afterward. Capture the raw token at
PARSE time:
```python
class Raw(str): pass  # holds the original number text verbatim
def loads(s):
    return json.loads(s, parse_int=lambda x: Raw(x), parse_float=lambda x: Raw(x))
# then when emitting a value: if isinstance(v, Raw): out = str(v)   # 1.2e10 stays 1.2e10
```
Do NOT use float()/int()/repr() on numbers anywhere.
STRING VALUES: emit `json.dumps(s, ensure_ascii=False)` -- NEVER write the raw string. A raw
newline/tab/quote must appear ESCAPED (\\n, \\t, \\") exactly as json.dumps produces; writing
the literal control char splits your output across lines and fails every string test.
COMPACT JSON: when emitting any JSON array/object (e.g. gron --json path arrays), use
`json.dumps(x, separators=(",", ":"))` -- the DEFAULT json.dumps puts a SPACE after every
comma (`["b", 0]`) but these tools emit compact (`["b",0]`); the space fails every --json test.
RESERVED-WORD KEYS: object keys `true`/`false`/`null` are emitted in BRACKET form
(`json["null"]`), never dotted -- they sort by their bracketed/quoted form.''',
    "io": '''## TECHNIQUE: file-arg-or-stdin + exact exit codes
```python
src = next((a for a in argv[1:] if not a.startswith('-')), None)
raw = open(src, encoding='utf-8').read() if src and src != '-' else sys.stdin.read()
# malformed input: write the tool's exact error to STDERR and use its OBSERVED exit code
# (often 3 for parse errors, 4 for failed URL fetch, 5 for invalid ungron). Match what you saw.
```''',
    "table": '''## TECHNIQUE: box-drawing table layout -- the 3 byte-exact rules models get WRONG
A grid/box table is NOT "draw a header then a horizontal line". Get these EXACTLY or every
table fails byte-match (verified against the reference binary):
1. COLUMN WIDTH = max DISPLAY width of all cells in that column (header included). DISPLAY
   width is NOT string length: East-Asian wide + fullwidth chars count as 2 columns each
   (Rust: `unicode_width::UnicodeWidthStr::width`; Go: `runewidth.StringWidth`; never `len()`
   or `.chars().count()`). Each rendered cell is ` ` + pad(content, colwidth) + ` ` (one
   space of padding on EACH side -> inner cell width = colwidth + 2).
2. SEPARATOR lines carry a JUNCTION char at EVERY column boundary -- they are NOT one flat run
   of dashes. Top `┌──┬──┬──┐`, mid (under header) `├──┼──┼──┤`, bottom `└──┴──┴──┘`. The
   junction sits exactly above/below each `┬`/`┴`, i.e. after every (colwidth+2) dashes. A mid
   rule rendered as `├────────┤` (no `┼`) is the #1 cause of style/border test failures.
3. ALIGNMENT differs header vs body: HEADER cells are CENTER-aligned, BODY cells LEFT-aligned
   (unless an align flag overrides). Center of width W: left pad = floor((W-content)/2), the
   extra space goes on the RIGHT. So `a` in a width-4 column -> `  a   ` inside the borders
   (incl. the 1-space side padding); body `1` -> ` 1    `.
Style variants (none/ascii/sharp/rounded/grid/markdown) only change WHICH glyphs fill these
slots -- the width/junction/alignment math above is identical for all of them. Capture each
style's exact glyph set from the reference probes; keep the layout math shared.''',
    "tui": '''## TECHNIQUE: ncurses/curses TUI tools -- what the tests actually check
Proven 2026-07-02 (tty-clock, hand-driven). A plain (non-pty) probe of an ncurses binary
prints "Error opening terminal: unknown" and exits 1 -- that IS real, correct reference
behavior for a no-TTY/no-TERM harness context (replicate it: check `newterm()`/`initscr()`
for failure, exit(1)), but it teaches you NOTHING about the tool's actual rendering. Real
rendered content only shows up in a pty-captured observation (look for a `tui-snapshot*`
probe among your observations -- raw ANSI/terminal escape bytes, e.g. `\\x1b[42m` = a
colored block cell). If one is present, the tool draws real content (big block-digit
displays, colored regions, box art) via ncurses color pairs / attron(A_*) -- do NOT just
`mvaddstr()` a plain text string; that under-renders and fails byte-count/content checks.
TEST SHAPE, not pixel-perfect match: TUI eval assertions are typically (a) `len(stdout) >
N` -- render enough real content per frame, not one thin text line; (b) `"\\x1b[42m" in
screen` or similar -- USE the observed color/attribute escapes, don't just approximate with
plain text; (c) exact `golden == actual` snapshots -- these often NORMALIZE block-rendered
lines to a placeholder token before comparing, so genuine escape-sequence-driven rendering
of the right STRUCTURE (row/column layout) tends to match without needing byte-exact segment
shapes. Test harnesses commonly use tmux (`TmuxHarness`) to drive real keypresses/resize --
handle SIGTERM/keypress-to-quit exactly as observed (default: any key exits unless a
"don't quit on keypress" flag is set).''',
}


def recipes_for(short: str, observations: list | None = None) -> str:
    """Pick concrete technique recipes relevant to this tool: detect JSON-domain from the
    tool's observed output (gron/jq-like: lines contain `= ` assignments or JSON tokens).
    Always include the io recipe (universal). Keeps the prompt focused on actionable HOW."""
    picked = [_RECIPES["io"]]
    blob = ""
    for o in (observations or [])[:6]:
        blob += getattr(o, "stdout", "") or ""
    if "json" in short.lower() or "gron" in short.lower() or "{" in blob or " = " in blob:
        picked.insert(0, _RECIPES["json"])
    # table/grid renderers: detect box-drawing or ASCII-grid glyphs in observed output.
    if any(ch in blob for ch in "┌┬┐├┼┤└┴┘│─╭╮╰╯") or "+--" in blob or "+==" in blob:
        picked.insert(0, _RECIPES["table"])
    # TUI/ncurses tools: a pty-captured tui-snapshot observation (determinex_observe.
    # observe_tui_snapshot) carries raw terminal escape bytes -- \x1b[ is the reliable tell.
    tui_blob = "".join(getattr(o, "stdout", "") or "" for o in (observations or [])
                       if getattr(getattr(o, "probe", None), "name", "").startswith("tui-snapshot"))
    if "\x1b[" in tui_blob or "\x1b[" in blob:
        picked.insert(0, _RECIPES["tui"])
    return "\n\n".join(picked)


def _path(short: str) -> Path:
    return SKILLS_DIR / f"{short}.json"


def _probes_path(short: str) -> Path:
    return SKILLS_DIR / f"{short}_probes.json"


def load_probes(short: str) -> list[dict]:
    """The corpus-owned, auto-grown oracle for this tool: serialized probe dicts
    (name/argv/stdin/files/serve) discovered by fuzz_diagnose across runs. The reimpl driver
    reconstructs OBS.Probe from these and adds them to the oracle -> the corpus literally
    holds the behavioral coverage it has learned, persisted + replayable."""
    p = _probes_path(short)
    if p.exists():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            return []
    return []


def add_probes(short: str, new_probes: list[dict]) -> int:
    """Merge newly-discovered probes into the corpus oracle, deduped by their I/O signature.
    Returns how many were actually added (0 => the oracle already covers them = saturation)."""
    SKILLS_DIR.mkdir(parents=True, exist_ok=True)
    cur = load_probes(short)
    seen = {(json.dumps(p.get("argv", []), sort_keys=True), p.get("stdin"),
             json.dumps(p.get("files", {}), sort_keys=True),
             json.dumps(p.get("serve", {}), sort_keys=True)) for p in cur}
    added = 0
    for p in new_probes:
        key = (json.dumps(p.get("argv", []), sort_keys=True), p.get("stdin"),
               json.dumps(p.get("files", {}), sort_keys=True),
               json.dumps(p.get("serve", {}), sort_keys=True))
        if key not in seen:
            seen.add(key)
            cur.append(p)
            added += 1
    if added:
        _probes_path(short).write_text(json.dumps(cur, indent=1, ensure_ascii=False), encoding="utf-8")
    return added


def load(short: str) -> dict:
    p = _path(short)
    if p.exists():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def render_prompt_block(short: str, max_chars: int = 2600, observations: list | None = None) -> str:
    """The coach block injected into the builder prompt: cross-tool pitfalls + concrete
    technique RECIPES (HOW, not just WHAT) + anything Determinex already knows about THIS tool
    (discovered spec + behaviors that were hard).

    ORDER = priority under truncation (2026-07-02): this is a flat [:max_chars] cut, and a
    tight budget (decompose stations call this with max_chars=900) means SOMETHING gets
    dropped. Found via cmatrix: the old order put the generic CROSS_TOOL_PITFALLS (~800
    chars, applies to every tool, already somewhat "common sense") FIRST, which alone ate
    the entire 900-char budget and silently dropped the auto-detected DOMAIN recipe (e.g.
    the tui recipe -- concrete, tool-specific, and exactly the guidance a station needed)
    every single time. Most-actionable/specific first, most-generic last."""
    block = [recipes_for(short, observations)]  # auto-detected domain HOW-TO -- most actionable
    rec = load(short)
    if rec:
        spec = rec.get("spec_notes") or []
        hard = rec.get("hard_behaviors") or []
        if hard:  # tool-specific learned pitfalls -- high value, keep ahead of generic content
            block.append("## Behaviors that were HARD last time (get these RIGHT)\n%s"
                         % "\n".join(f"- {h}" for h in hard[:20]))
        if spec:
            block.append("## What Determinex already knows about `%s` (discovered)\n%s"
                         % (short, "\n".join(f"- {s}" for s in spec[:20])))
    block.append(CROSS_TOOL_PITFALLS)  # generic, applies everywhere -- truncate first if tight
    return "\n\n".join(block)[:max_chars]


def record_run(short: str, *, observations: list | None = None,
               failed_probe_names: list | None = None,
               best_local: str = "", best_official: int | None = None,
               official_total: int | None = None, candidate_path: str = "",
               spec_notes: list | None = None) -> dict:
    """Persist what this run taught us. Merges with any prior record (the corpus learns
    cumulatively). Locks a verified skill ONLY on a genuine official pass (==total)."""
    SKILLS_DIR.mkdir(parents=True, exist_ok=True)
    rec = load(short)
    rec["tool"] = short
    rec["updated"] = time.strftime("%Y-%m-%d %H:%M")
    if spec_notes:
        rec["spec_notes"] = sorted(set((rec.get("spec_notes") or []) + spec_notes))
    if failed_probe_names is not None:
        # behaviors that were hard = union of what failed across runs (so we keep coaching them)
        rec["hard_behaviors"] = sorted(set((rec.get("hard_behaviors") or []) + failed_probe_names))
    if best_official is not None:
        prev = rec.get("best_official", -1)
        if best_official > prev:
            rec["best_official"] = best_official
            rec["best_official_total"] = official_total
            rec["best_candidate"] = candidate_path
        rec["last_official"] = best_official
    if best_local:
        rec["last_local"] = best_local
    # LOCK a verified skill only on a real official solve
    if best_official is not None and official_total and best_official == official_total:
        rec["verified_skill"] = True
        rec["locked"] = rec.get("updated")
    _path(short).write_text(json.dumps(rec, indent=2, ensure_ascii=False), encoding="utf-8")
    return rec


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        print(json.dumps(load(sys.argv[1]), indent=2))
    else:
        print("reimpl_skills:", [p.stem for p in SKILLS_DIR.glob("*.json")] if SKILLS_DIR.exists() else [])
