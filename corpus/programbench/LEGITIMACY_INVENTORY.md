# Legitimacy Inventory — Crucible from-source gate (2026-06-18, corrected)

> `determinex_crucible.py --slug <slug> --require-fresh --build-only` across 37 not-locked
> candidates, building each in its real `:task` reference image. v2 after fixing the
> fresh-detection bug (was cargo-only markers → false-failed silent Go/C/make builds;
> now language-general). **19 FRESH / 18 BUILD_FAIL.**

## FRESH — build legitimately from source (19) = the real lock candidates
Drive each through `programbench eval` (PROGRAMBENCH_DOCKER_CPUS=1); bank clean, fix tails.

| tool | lang | known tail (from prior evals) |
|------|------|-------------------------------|
| `wfxr__code-minimap.0ddeea5` | rust | already an official lock (gate sanity ✓) |
| `ariga__atlas.6d81150` | go | CEILING — official-only `--revisions-schema` feature (proven) |
| `rs__jplot.2a54bcc` | go | 3 TUI escape-seq fails (likely ceiling) |
| `ducaale__xh.4a6e44f` | rust | man-page (build-fix) + httpbin network |
| `hush-shell__hush.560c33a` | rust | `results_read_failed` on branch 10c7b30aafc4 |
| `tarka__xcp.5e5b448` | rust | reflink-fs + root-perm (fd-class ceiling) |
| `axodotdev__oranda.27d60c7` | rust | github network + css-env + 1 timeout |
| `pls-rs__pls.4e1ae50` | rust | unicode/column-align formatting |
| `byron__dua-cli` (FAIL v2) | rust | size formatting |
| `peco__peco.4e58dad` | go | TUI / needs eval |
| `dundee__gdu.ede21d2` | go | needs fresh eval |
| `htop-dev__htop.523600b` | c | needs fresh eval |
| `danmar__cppcheck.0a5b103` | cpp | needs fresh eval |
| `tomarrell__wrapcheck.c058da1` | go | needs fresh eval |
| `zevv__duc.a58fa4e` | c | needs fresh eval |
| `sayanarijit__xplr.1751065` | rust | TUI |
| `ecumene__rust-sloth.051c559` | rust | behavioral |
| `oppiliappan__eva.41ae245` | rust | from-source build scored 42% — real behavioral gap to chase |
| `drew-alleman__datasurgeon.d257cee` | rust | **Determinex reimpl** — extractor format/regex tail (~71%) |
| `yoav-lavi__melody.f4af9b4` | rust | **Determinex reimpl** — DSL coverage (16%) |

## BUILD_FAIL — genuine build break (18), now trustworthy
Most show `bundled=true` = the from-source build FAILED and compile.sh fell back to the
answer-key binary. These need the **build fixed** (deps/source/env) before they can count:
`tui-journal, pipr, gomplate, lazygit, fselect, dutree, onefetch, dog, quinn, bat,
stgit, gittype` (bundled-fallback) · `dust, delta, go-critic, jsonschema,
ascii-image-converter` (build errored, no fallback — pull build_log_tail to see why).

> Next: pull each BUILD_FAIL's real compiler error via
> `determinex_crucible.py <workdir> --slug <slug> --build-only` (no require-fresh) and fix
> the build (missing dep, vendored crate, toolchain version, CRLF in compile.sh).

## Status
Method works; 19 tools build legitimately from source. **Honest count: 65 official
locks** — no new locks yet. Now driving the FRESH set through `programbench eval`,
fixing tails toward clean evals (atlas/jplot/xcp look like ceilings; xh/pls/oranda/
the un-evaled Go+C tools are the live lock hunt).
