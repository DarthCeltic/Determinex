# Determinex — Machine Security Posture (2026-06-14)

> Defensive security for **your own box**, independent of whether Determinex ships.
> This box runs autonomous agents and executes model-generated code, and holds
> live API keys. This document records the audit, the fixes applied, and the few
> things only *you* can do.

## Audit findings

| Check | Result |
|---|---|
| `.env` git-ignored? | ✅ Yes (`git check-ignore .env` confirms) |
| `.env` currently tracked? | ✅ No |
| API keys in any **tracked** file? | ✅ No real keys (the only key-*shaped* hits are the `ripsecrets` secret-detector's own test fixtures + secret-scanner code — by design, not leaks) |
| API keys in **pushed / remote** history? | ✅ **No** — the remote (`github.com/lunariandatasystems-cmd/determinex`) history is clean of `.env`; an `origin/clean-main` branch shows history was deliberately scrubbed before pushing |
| API keys in **local** git history? | ⚠️ **Yes** — commits `7f8dacd3e` (initial) and `482f02f43` contain `.env` with keys. **Local only — not pushed.** |
| Live keys in current `.env` on disk? | ⚠️ 3 (Anthropic, DeepSeek, Gemini), plaintext |
| Did the secret-catching pre-commit hook cover API keys? | ⚠️ No — `detect-private-key` catches PEM keys only, not `sk-ant-`/`AIza` |
| Model-generated code execution | ✅ Routed through `intake.hardened_runner` (workspace-bounded, env-scrubbed, **network + Docker denied by default**) in build/repair/synthesize; SWE-bench uses Docker |

**Bottom line:** no off-box leak. The real residual exposures are (a) live keys sitting
in *local* git history, (b) live keys plaintext in `.env`, and (c) the autonomy
directive's blanket "zero permission gates."

### Note on the many key-shaped strings under `corpus/`

A naive scan flags ~100 "keys" in `corpus/programbench/**`. These are **not yours and
not a breach**: they are the benchmark *tools'* own test vectors and fixtures shipped
with their source — `ripsecrets`' fake detection fixtures, mbedtls/openssl/age/dropbear
crypto **test PEMs**, the AWS documentation example key `AKIA...EXAMPLE`, etc.
They are public, came with the upstream tools, and are not credentials. `secret_scan.py`
excludes `corpus/`, secret-detection tooling, and `testdata`/`test_vectors`/`crypto`
paths for exactly this reason. (Caveat: GitHub *push-protection* may still flag some of
these test PEMs as a nuisance — they are safe to allow, being upstream test data.)

## Fixes applied (in this repo)

1. **Pre-commit secret hygiene** (`.pre-commit-config.yaml`):
   - `no-env-file` — hard-fails any commit that stages a `.env` file.
   - `no-api-keys` — rejects Anthropic / Google / OpenAI / generic key shapes in staged content.
2. **Standalone secret scanner** (`scripts/security/secret_scan.py`):
   - `python scripts/security/secret_scan.py` — fast `git grep` over tracked files.
   - `--pushed` — scan only what the remote has (the off-box leak check).
   - `--history` — scan all local history. Redacts matches; exits non-zero if a secret sits anywhere leakable.
3. **Autonomy security carve-out** (root `C:\Dev\CLAUDE.md` + `Determinex/CLAUDE.md`):
   "Zero permission gates" now explicitly applies to *operator-initiated dev
   commands only*. Model-generated / untrusted code is **never** auto-executed raw —
   only through the sandbox or Docker. Secrets are never committed/pushed/printed.
4. **Sandboxed execution** — the model-generated-code paths run through
   `intake.hardened_runner` (no raw `subprocess`), verified this session.

## What only YOU can do (action items)

1. **Rotate the three API keys.** They have lived in local git history and sit
   plaintext in `.env`. Even though not pushed, rotation is the safe move:
   - Anthropic: console.anthropic.com → API keys → revoke + regenerate
   - Google/Gemini: aistudio.google.com / Cloud console → regenerate
   - DeepSeek: platform.deepseek.com → API keys → regenerate
   Then update `.env`. After rotating, `python scripts/security/secret_scan.py` again.
2. **(Optional, advanced) Scrub `.env` from local history.** Since the remote is
   already clean, this is low-urgency, but it removes the last local copy:
   ```bash
   pip install git-filter-repo
   git filter-repo --path .env --invert-paths --force
   ```
   ⚠️ This **rewrites history** — back up the repo first, and re-verify the remote
   is unaffected. Do not run on a branch you intend to merge into pushed history.
3. **Never `git push --all` / `git push <old-branch>`** from this repo without first
   running `secret_scan.py --history` — the local history still contains `.env`, and
   a force-push of old refs could expose it.
4. **Box hygiene:** treat this machine as holding secrets — disk encryption,
   screen lock, no untrusted remote access. The keys are real.

## Standing guarantees (enforced going forward)

- Pre-commit blocks any `.env` or API-key string from entering git.
- Model-generated code only executes sandboxed (hardened runner / Docker).
- The autonomy directive carve-out is in both CLAUDE.md files; agents read it.
- `secret_scan.py` is runnable anytime as the on-demand audit.

## Hardened Runner — Actual Boundary (audited 2026-07-01)

`intake.hardened_runner` is real and does what its docstring claims:
`shell=False` always, `cwd` validated inside `workspace`, a fixed env-var
blocklist stripped unconditionally, a 600s timeout cap, and an argv[0]
denylist for Docker/container tools + standalone network CLIs (curl, wget,
nc, ssh, scp, rsync, ftp, dig, ...). What it is **not** — stated here so
"network + Docker denied by default" above isn't read as more than it is:

- **Not a network namespace.** The block is an argv[0] denylist. A
  general-purpose interpreter (python/node/bash/powershell) invoked to run
  untrusted code can still make arbitrary HTTP/socket calls internally —
  invisible to a program-name check. Interpreters are deliberately not
  denylisted because intake/build/repair legitimately needs them; there is
  no way to close this gap with an argv[0] list alone.
- **Not a filesystem jail.** Only `cwd` is validated as inside `workspace`.
  Command *arguments* pointing at absolute paths elsewhere on disk are not
  checked — e.g. nothing here stops `["cat", "C:\\Users\\...\\secret.txt"]`
  from reading outside the workspace if a malicious/buggy generated command
  tried it.
- **No OS-level resource limits.** Only a wall-clock timeout; no
  ulimit/cgroup/Job Object caps on memory or process count here. (Separately,
  `hive/compiler.py`'s Compiler Oracle subprocess path *does* use a Windows
  Job Object with real resource limits — that's a different subsystem
  protecting a different pipeline, not this one.)

**Where the real boundary lives:** Docker, for anything that needs one (SWE-bench
already routes through it). Treat hardened_runner as a best-effort guard
against the *easy* mistakes (shell injection, obvious network/Docker tools,
env-var injection vectors, workspace-relative path traversal), not as a
hard security boundary against a genuinely adversarial payload.

## Runtime Monitoring — What Exists vs What Doesn't (audited 2026-07-01)

There is no single "anomaly detection" system. What exists, honestly assessed:

- **Event-level audit**: the Ethics Oracle's tamper-evident WAL
  (`scripts/determinex_safety.py::wal_append`) records every safety violation
  with an escalation tier; `EscalationState` tracks per-subject violation
  counts and hard-blocks at RESTRICT/CUTOFF. This is real-time and
  enforcing, but scoped to safety-gate violations only — it does not watch
  general resource usage, process behavior, or API call patterns.
- **Operational event stream**: `scripts/run_ledger.py` is a general
  append-only JSONL+SQLite ledger for long-running jobs (task started/
  completed/failed, scores, artifacts). It's a record, not a monitor — it
  answers "what happened" on query, it does not alert on "something's wrong
  right now."
- **Task-loop stall detection**: `scripts/determinex_progress.py`
  (`ProgressTracker`) detects when a solve-attempt loop is plateauing or
  looping and emits WIDEN/RE_DECOMPOSE/ESCALATE — but it's scoped to the
  Correctness Amplifier's verified-search loop, not general process health.
- **PB eval stall detection**: `pb_eval_unified.run_local_eval`'s
  test-progress stall detector (CPU-based, catches a hung eval in ~4 min) —
  scoped to ProgramBench evals specifically.

**What's genuinely missing**: a unified layer that watches for *abuse or
compromise patterns* across a session in real time — e.g. an unexpected
spike in cloud API spend velocity (budget_guard/hive/budget.py enforce a
hard cap but don't alert on an unusual *rate*), a sudden burst of
hardened_runner NETWORK_REFUSED/DOCKER_REFUSED blocks (which would suggest
generated code is repeatedly trying to escape the sandbox — currently only
visible by grepping logs after the fact), or process counts/memory climbing
outside the normal envelope for a given pipeline. None of the four systems
above talk to each other or roll up into a single "is this session behaving
normally" signal. Building that roll-up is future work, not yet started.
