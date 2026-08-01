# ProgramBench Reimplementation Playbook

> The model-facing knowledge layer for the LEGITIMATE task. ProgramBench is a
> **reverse-engineering** benchmark: given only a compiled binary + its docs, write
> a **brand-new codebase** whose executable reproduces the original's *observable
> behavior*. Hidden tests compare your executable's behavior to the original's.
>
> **This is NOT a build-from-source task.** Shipping the tool's real upstream source,
> `cargo install`/`go get`-ing it, cloning the repo (at eval OR pack time), or wrapping
> the reference binary are ALL the forbidden shortcut — they bypass the challenge.
> The corpus is the friend that helps you *figure the tool out and rebuild it yourself*.

---

## The rules of the environment (v1.1.0+/v1.2.2)

1. **No internet.** No outbound connectivity during inference OR during `compile.sh`
   (DNS blackholed, `utils/internet_control.py`). `pip install`, `cargo build`(online),
   `apt-get`, `git clone`, `wget`/`curl` all FAIL at build time. **Loopback (localhost)
   is available** for tasks that speak a network protocol.
2. **Execute-only binary (perms 111).** You can RUN the reference binary with any args
   and see its output. You CANNOT read it (no decompile, no Ghidra).
3. **No binary analysis.** `strace`/`ltrace`/`objdump`/disassemblers are disallowed.
   All knowledge comes from *running* the binary through its normal interface.
4. **Original binary removed at eval.** Any file matching the original binary's hash is
   deleted before tests run → thin wrappers are caught. (Shipped *source* is not
   hash-caught, but it is still the forbidden shortcut — do not do it.)
5. **Clean room image** (`task_cleanroom_v6`, default). No build artifacts, no `.git`,
   no cached deps, fresh anonymous commit. The image has only the binary + docs.
6. **Score = `n_resolved / 200`** over the full benchmark (not attempted). A task is
   "solved" only at an EXACT 100 (`passed == total` after `for_branches` +
   `without_ignored`). Partial pass-rates are the realistic, honest output.

What you GET: the executable (runnable), the README/help/man docs, and any **binary
test assets** (images/audio) the tests need. Text inputs (`.c`/`.json`/`.php`) are NOT
provided — generate representative ones yourself (part of the challenge).

---

## The reverse-engineering loop (how to discover behavior)

Run the binary; never read it. Be systematic — most failures are missed flag
combinations and exact-output-format mismatches, not deep logic.

1. **Surface the interface.** `--help`/`-h`, `--version`/`-V`, no-args, bad args,
   `<subcommand> --help` for each subcommand. Capture stdout, stderr, AND exit code
   separately — tests assert all three.
2. **Read the docs** (README, man) for documented flags/formats the help omits.
3. **Probe every flag/subcommand** against representative inputs. Diff outputs as you
   toggle one flag at a time — that isolates each flag's exact effect.
4. **Nail output formatting EXACTLY**: trailing newline or not, whitespace/alignment,
   field order, number formatting/zero-padding, color/ANSI (and whether `NO_COLOR`/TTY
   suppresses it), JSON key order, locale/timezone effects.
5. **Hunt edge cases** the tests will: empty input, missing file, invalid input, large
   input, stdin vs file vs arg, unknown flag (usage-to-stderr? exit 1? exit 2?),
   `--` separator, combined short flags.
6. **Determinism**: if output varies (timestamps, paths, PIDs, ordering), find the env
   knob the original respects (TZ, SOURCE_DATE_EPOCH, locale, seed) so your output
   matches under the test's environment — don't hardcode the observed value.

---

## Reimplementation strategy

- **Language: pick the easiest Turing-complete one** — Python is usually best (fast to
  write, rich stdlib, no build step). Church-Turing says you can reproduce any C/Rust/Go
  behavior in Python; you are NOT required to match the implementation language.
- **Match behavior, not internals.** You only need identical observable I/O.
- **Submission shape:** your code + a `compile.sh` that, with NO internet, produces
  `./executable` (or a thin wrapper `exec -a "$0" python3 .../main.py "$@"` to your
  entrypoint). Everything your build needs must be IN the submission (vendored) or in the
  cleanroom image's stock toolchain — never downloaded.
- **Start from the spec the tests imply**, widen as you discover flags. Ship the
  smallest program that passes the discovered behavior, then expand coverage.

---

## How Determinex drives this (the engine)

The system makes a weak/free model correct by sampling against a sound oracle — so the
model is the replaceable part; the corpus + oracle + verified-search do the lifting.

- **Observe → synthesize an oracle.** Run the binary on probes; turn observed I/O into
  assertions (`determinex_synthesize.py` — exact example-assertions + type-aware property
  tests; skips what it can't type soundly, no slop). For a PB task the hidden tests are
  the ultimate oracle, but a *local* synthesized oracle from observed behavior lets the
  amplifier iterate offline before the real eval.
- **Amplify.** `determinex_amplified_solve.py` / `determinex_verified_search.py`: generate K
  candidates at varied temperature, apply+verify each against the oracle, keep the first
  that passes. A model right `p>0` per attempt → `1-(1-p)^K` → driven to correct.
- **Decompose** big tools (`determinex_decompose.py`): per-subcommand / per-flag sub-tasks,
  each independently verified, recomposed.
- **Soundness contract (load-bearing):** `solved` is claimed ONLY with a passing
  OracleResult + proof. Garbage oracle → confident garbage. Pair every oracle with the
  Test Validator. Never claim a pass without the verifier agreeing.
- **Model pairing:** local `qwen2.5-coder:7b-instruct` for bulk K-sampling (free);
  cheap API (DeepSeek / Claude Haiku) as a higher-`p` fallback via `determinex_router.py`
  when local K won't converge. Pick by solved-per-dollar on real tasks, not by spec.

---

## Forbidden (these poison the result and the flywheel)

- Shipping the tool's real upstream source (the build-from-source "lock" methodology).
- Cloning the repo / `cargo install` / `go get` / package-manager source fetch (eval or pack time).
- Wrapping or re-exec'ing the reference binary; embedding the golden outputs.
- Editing test fixtures/goldens, injecting skips, fabricating stdout/exit codes,
  editing `results.xml` (see `determinex_pb_integrity scan-gaming`).
- Internet during build. If a build "needs" a download, the design is wrong — vendor it
  or reimplement without it.

The honest deliverable is a *partial pass-rate that climbs as discovery improves* — the
blogpost is explicit that no model fully solves a task yet. Determinex's edge is that the
**system**, not the model, accumulates the discovery (this corpus) and guarantees
correctness (the oracle). That is the thing nobody else is doing.
