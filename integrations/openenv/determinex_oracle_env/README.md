# determinex_oracle_env — an OpenEnv environment with no LLM judge

## What this is

An [OpenEnv](https://github.com/huggingface/OpenEnv)-compatible environment
(`Environment` / `Action` / `Observation` / `EnvClient`, HTTP + WebSocket,
`openenv.yaml` manifest) that wraps `scripts/determinex_oracle.py` — Determinex's
Universal Ground-Truth Oracle. An agent submits code; the environment writes
it into an isolated per-episode workspace and runs the real toolchain
(`rustc`, `go build`, `tsc`+`jest`, `pytest`, `cargo test`, ...) against it.
The reward is that verdict: `1.0` if the suite passes end-to-end, `0.0`
otherwise. Nothing in between, nothing inferred, nothing scored by a model.

## Why we're doing this

Determinex's whole architecture rests on one claim: **the compiler is the only
oracle** (see `CLAUDE.md` / `docs/architecture/`). Every training pair in
Determinex's flywheel, every ProgramBench lock, every SWE-bench patch — all of
it is gated by a real toolchain, never an LLM judge, because LLM judges are
exactly the kind of soft, gameable signal that makes RL training noisy and
lets a model learn to satisfy the grader instead of the task.

OpenEnv's own governance (Meta-PyTorch, Hugging Face, and 20+ supporting
orgs as of mid-2026) is explicitly moving toward the same conclusion — the
ecosystem's own framing is "grounded scaling," i.e. agentic RL needs
deterministic environments, not vibes-based reward. That's not a coincidence
we're riding; it's the same argument Determinex has been making internally
since before OpenEnv existed. Contributing this environment is the honest,
substantive way to show that argument rather than assert it.

Three concrete reasons this is the right integration, not just goodwill:

1. **It's real reuse, not new surface area.** This wraps the exact oracle
   module Determinex's own Hive Mind loop calls. No parallel verification logic
   was written for this. If `determinex_oracle.py` gets better, this gets
   better for free, and vice versa — bugs found via OpenEnv usage are bugs
   fixed in Determinex's own reward model.
2. **It's the safe surface to open.** This exposes verification (pass/fail
   + compiler output), not the proprietary Hive orchestration, Rosetta
   Stone, Cloak obfuscation, or model weights. A user runs their own patches
   against their own task workspace; nothing proprietary crosses the wire.
3. **It's positioning, done honestly.** Per the pre-announcement messaging
   review: the risk with OpenEnv isn't the comparison, it's over-claiming
   against it ("we've invented the future of agent environments"). Shipping
   a working, narrowly-scoped, evidence-backed environment does the opposite
   — it says "here's exactly what this proves" instead of asserting a
   platform claim nobody asked to see verified.

## How it works

```
reset(task_dir=<reference project>, language=<oracle key>)
  -> copies task_dir into a fresh, isolated tempdir (episodes never
     collide or corrupt the reference)

step(DeterminexOracleAction(files={...}, remove=[...]))
  -> writes/deletes the submitted files in the episode workspace
  -> determinex_oracle.get_oracle(language).verify(workdir)
  -> DeterminexOracleObservation(passed, oracle, total, n_passed, failures, raw_tail)
  -> reward = 1.0 if passed else 0.0; done = True once passed (or if the
     toolchain for `language` isn't installed on this host)
```

`task_dir` can point at any buildable project skeleton — including any of
Determinex's own `corpus/programbench/per_tool_overrides/<tool>/` directories,
which makes every one of Determinex's 200 ProgramBench reimplementation tasks
immediately usable as an OpenEnv training/eval environment with zero extra
authoring.

## Security note

`determinex_oracle.py::_run` already routes execution through Determinex's
hardened runner (workspace-bounded, env-scrubbed) per the project's security
carve-out — this environment does not add or bypass any sandboxing; it
inherits whatever guarantees the oracle module already has. Model-generated
code submitted via `step()` is untrusted input and is treated as such by the
oracle it's already treated as such by.

## Status

MVP: core `Environment`/`Action`/`Observation`/`EnvClient` + HTTP app +
manifest are implemented and importable. Not yet done: a Dockerfile for
hosted deployment (the `coding_env` reference ships one; this doesn't yet),
and `SUPPORTS_CONCURRENT_SESSIONS` is left at the conservative default
(`False`) pending verification that concurrent `cargo`/`go build` calls
across episodes don't contend on shared toolchain caches.

## License

**Corrected 2026-07-01** — see [`docs/security/OPENENV_SUBMISSION.md`](../../../docs/security/OPENENV_SUBMISSION.md)
for the full research. Short version: the note below (2026-06-29) assumed
contributing an environment means merging code into `meta-pytorch/OpenEnv`
itself (BSD-3-Clause), which would require Determinex's whole `LICENSE` to
change first. That's not how it actually works — environments are
published independently to the Hugging Face Environment Hub (`openenv
push`), not merged into the core repo. The core `openenv` interface library
stays BSD-3-Clause; this directory just depends on it, same as any project
importing a permissively-licensed SDK. No Hub documentation found so far
mandates a specific license for a contributed environment's own code.
Before actually publishing: confirm directly against the live Hub
submission page (docs move), and/or scope a standalone permissive license
for just this directory as cheap insurance either way — see the submission
doc for detail. Does not require touching Determinex's top-level `LICENSE`.

Original 2026-06-29 note (superseded, kept for history): "This directory
targets compatibility with OpenEnv's own BSD-3-Clause license for upstream
contribution. Determinex's own top-level `LICENSE` is currently
Source-Available; see the open-source licensing decision tracked in
`RELEASE_AUDIT_HANDOFF_2026_06_29.md` before this is proposed upstream."
