# OpenEnv Submission — What, How, Why (researched 2026-07-01)

> Answers "what would we be submitting, how, and why" with primary-source
> research (GitHub repo, Hugging Face blog, live web search), not just the
> prior session's summary notes. Supersedes the licensing-blocker framing
> in `project_openenv_and_aifoundry_20260629.md` (memory) and the stale
> note in `integrations/openenv/determinex_oracle_env/README.md`.

## What OpenEnv is

[OpenEnv](https://github.com/meta-pytorch/OpenEnv) (also mirrored at
`huggingface/OpenEnv`) is a joint Meta-PyTorch / Hugging Face interface
library that standardizes how RL-training agents talk to execution
environments — a Gymnasium-style API (`reset()` / `step()` / `state()`)
with typed `Action`/`Observation`/`State` dataclasses, container isolation
(each environment runs in its own Docker container), and a client/server
split so the environment can run remotely from the training loop. Announced
mid-2026 with a technical committee spanning Meta-PyTorch, Hugging Face,
Nvidia, Microsoft, Prime Intellect, Unsloth, Modal, Mercor, Fleet AI,
Reflection, and RadixArk.

**The problem it solves**: exposing millions of raw tools directly to a
model during RL training is neither practical nor safe. OpenEnv gives each
task a "secure, semantically clear sandbox that defines exactly what's
required for a task, and nothing more" — a deterministic, reproducible unit
of interaction instead of an open-ended tool call.

## Why this is a natural fit for Determinex, not opportunistic borrowing

Determinex's entire architecture already rests on one non-negotiable claim:
**the compiler is the only oracle** — every training pair, every
ProgramBench lock, every SWE-bench patch is gated by a real toolchain
verdict, never an LLM judge, because a soft/gameable reward signal is
exactly what lets a model learn to satisfy the grader instead of solve the
task. OpenEnv's own framing — "grounded scaling," deterministic reward over
vibes-based scoring — is the *same argument*, arrived at independently.
Contributing a working environment proves that argument with evidence
instead of asserting it in a blog post.

## What we would actually be submitting

`integrations/openenv/determinex_oracle_env/` — already built and smoke-tested
(2026-06-29, re-verified structurally this session). It wraps
`scripts/determinex_oracle.py` (Determinex's Universal Ground-Truth Oracle) as a
real OpenEnv `Environment`:

```
determinex_oracle_env/
├── models.py            Action/Observation/State dataclasses
├── client.py             EnvClient implementation
├── openenv.yaml           Environment manifest
├── pyproject.toml         Dependencies
└── server/
    ├── environment.py     Environment subclass — the actual logic
    ├── app.py              FastAPI instantiation (HTTP + WebSocket)
    └── requirements.txt
```

This exactly matches the scaffold OpenEnv's own `openenv init` CLI
generates, confirmed against the live repo — meaning it's already shaped
the way the ecosystem expects, not a custom structure that needs adapting.

**What it does**: an agent submits a code patch via `step()`; the
environment writes it into an isolated per-episode workspace and runs the
real toolchain (`rustc`, `go build`, `tsc`+`jest`, `pytest`, `cargo test`,
...) against it via the existing oracle. Reward is `1.0` if the suite
passes end-to-end, `0.0` otherwise — nothing inferred, nothing scored by a
model. `task_dir` can point at any buildable project skeleton, including
any of Determinex's 200 `corpus/programbench/per_tool_overrides/<tool>/`
directories — so the entire ProgramBench corpus becomes usable as OpenEnv
training/eval environments with zero extra authoring.

**What it deliberately does NOT expose**: Hive Mind orchestration, the
Rosetta Stone latent-bridge, Project Cloak, or model weights. Only
verification (pass/fail + compiler output) crosses the wire — an agent runs
its own patch against its own task workspace.

**Not yet done**: a `Dockerfile` for hosted deployment (OpenEnv's reference
`coding_env` example ships one; this doesn't yet — needed before an actual
Hub publish since environments run containerized), and
`SUPPORTS_CONCURRENT_SESSIONS` is left `False` pending verification that
concurrent `cargo`/`go build` calls across episodes don't contend on shared
toolchain caches.

## How submission actually works (this is the part that changes the calculus)

Researched directly against the GitHub repo README and the Hugging Face
announcement blog, not assumed:

- **Contributing an environment is not a pull request into
  `meta-pytorch/OpenEnv`.** The core repo is the *interface library*
  (BSD-3-Clause) — `Environment`, `Action`, `Observation`, the CLI. You
  depend on it (`pip install openenv` or equivalent), you don't submit code
  into it.
- **Environments are published independently to the Hugging Face
  Environment Hub**, a separate registry, via the `openenv push` CLI
  command (deploys to a Hugging Face Space, with a privacy flag). "Every
  environment uploaded to the Hub that conforms to the OpenEnv
  specification automatically gains" hub integration (discoverability,
  tooling).
- **No explicit license mandate was found for Hub-published environments**
  in the README or announcement blog. The core library's BSD-3-Clause
  license governs the interface you're depending on — same as any project
  that imports a permissively-licensed SDK without itself needing to adopt
  that SDK's license.

**This directly changes the prior blocker framing.** The 2026-06-29 note
(both in memory and in this integration's own README) assumed contributing
meant merging code into the BSD-3-Clause core repo, which would require
flipping Determinex's entire `LICENSE` first — a genuinely hard-to-reverse
call that was correctly escalated to you rather than decided unilaterally.
That assumption doesn't hold up against how OpenEnv's contribution model
actually works: publishing `determinex_oracle_env` as its own Hub environment
doesn't require Determinex's top-level `LICENSE` to change at all.

## What's still worth confirming before actually publishing

This research used the public README, the Hugging Face announcement blog,
and web search — solid primary sources, but I did not get into the actual
Hub submission form or `CONTRIBUTING.md` (a Hugging Face model-repo page
for the hackathon org returned a 401 in an earlier check this session, and
I didn't chase every possible Hub-specific doc). Two cheap ways to close
that gap before a real publish:

1. Read the Hub's actual submission page directly once you're able to
   (may need to be signed into Hugging Face).
2. Regardless of what #1 finds, it costs nothing to scope a standalone
   permissive license for just this directory — e.g. an SPDX header or a
   small `LICENSE` file inside `integrations/openenv/determinex_oracle_env/`
   stating it's available under MIT/Apache-2.0, distinct from the rest of
   the repo's AGPLv3 terms (AGPLv3 code generally isn't mergeable into a
   BSD-3-Clause upstream without a separate permissive grant for that piece).
   This is a common, well-established
   pattern (subdirectory-scoped licensing in an otherwise differently-
   licensed monorepo) and removes any ambiguity regardless of what the Hub
   actually requires — cheap insurance, doesn't touch your main `LICENSE`.

## What remains to actually ship it

1. Write the `Dockerfile` (the one concrete missing piece per the
   integration's own "Status" section).
2. Verify `SUPPORTS_CONCURRENT_SESSIONS=False` is still the right call, or
   test concurrent toolchain-cache behavior and flip it if safe.
3. Decide the directory-scoped license question above (or confirm it's a
   non-issue after checking the Hub page directly).
4. Run `openenv push` (or the equivalent current CLI command — versions
   move) to publish to the Hub. **This is a public, visible action** — it
   should happen only when you explicitly say go, not automatically.
