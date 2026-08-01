# ProgramBench — Smartest Compounding Path (not "easiest lock" — max leverage)

_Strategy (operator, 2026-06-15): a system at ~98% across many tools is smarter than one tool
at 100% — the harvested passing-tests + techniques make the WHOLE system better at the
remaining %. So: get everything high + `f=0` (sound), compound the knowledge, let the elevated
base drive the stragglers. Reserve "locked" for true 100%. Hard residuals → Opus-per-tool +
corpus verification._

## The soundness signal: `f=0` beats raw %
A tool with **`f=0` (zero failures)** is **correct as far as it runs** — its residual is only
skips/not_run (incomplete, not *wrong*). That knowledge is sound and harvestable. **All 16
tier-1 not-locked tools are `f=0`** — the binaries are correct; the gap is test *completion* +
honest ceilings, not bugs. Harvest every `f=0` tool's passing patterns + techniques into the
corpus (flywheel) regardless of exact %.

## Leverage ranking (solve high-leverage classes first → each compounds to the most tools)

| Rank | Residual class | Technique | Status | Why it compounds |
|---|---|---|---|---|
| 1 | **prefix-dupe not_run** | bidir-mirror | **PROVEN** | fills ~619 not_run across doxygen/fasttext/igrep/parqeye in one technique; reusable corpus-wide |
| 2 | **tty/tmux/pty** | pty-allocate | **PROVEN (36 locked)** | largest residual class; technique already proven in 36 tools — pure reuse |
| 3 | **build-fail / CRLF** | build-routing + CRLF-normalize | **PROVEN (baked)** | gets 0-passed tools to sound; CRLF can't recur (baked into pack) |
| 4 | **upstream-skip** | ceiling-cert (evidence) | CERTIFY | removes 8 tools from the "chase" — they're *done-as-ceiling*, frees focus |
| 5 | **root-perm skip** | drop-privileges | ITERATING (v2 un-skips but not passing) | 2 tools; needs v3 or honest in-container ceiling |
| 6 | **genuinely-missing not_run** | per-tool / Opus + corpus verify | MANUAL | 7 tools; the genuine hard tail — hand-loop |

## The path (order of attack)
1. **bidir everywhere** (proven, highest fill) — applied to the tier-1 prefix-dupe set; apply to any tier-3 that shows prefix-dupe not_run after first eval.
2. **pty-allocate reuse** for the tty/tmux residual class (the biggest) — pull the proven mechanism from the 36 locked tools.
3. **Compound the `f=0` knowledge** — harvest passing patterns + techniques from every sound tool into the corpus/flywheel; the elevated base helps the stragglers.
4. **Ceiling-cert the upstream-skips** with evidence — done-as-ceiling, archived to T:.
5. **Hand-loop the genuinely-missing** — Opus-per-tool for correct context + corpus verification, per the standing meta-loop.

## Run plan
- **Run the 110 untouched tier-3** through the reuse engine (CRLF-normalized pack → parallel eval → reports → autofix-all bidir/pty/build → re-eval). This expands the corpus + the leverage map "as it runs."
- **As tools land**: lock true 100%; harvest `f=0` knowledge; bucket the rest by class.
- The map refines as tier-3 data lands — high-leverage classes get attacked first so each subsequent solve is faster.

_Locks (true 100%, sha-pinned) this session: 39 base + ascii/thokr/angle-grinder. The point of
this doc: the *next* effort goes where it compounds hardest, not where it's merely easiest._
