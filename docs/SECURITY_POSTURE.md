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
| API keys in **pushed / remote** history? | ✅ **No** — the remote (`github.com/DarthCeltic/determinex`) history is clean of `.env`; an `origin/clean-main` branch shows history was deliberately scrubbed before pushing |
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

## Evidence-signing keys — 23 families fall back to a key published in the source (S1.13)

Each module below signs its evidence records with
`hmac.new(<key>, canonical_json(record), blake2b)` and, when its override variable is unset,
uses a key written literally in the source file. **None of these variables is set in this
checkout**, so the literal is the live path, and the paired `verify_*` therefore compares
`hmac(k, x)` against `hmac(k, x)` with a `k` any reader of the repository knows. It detects
accidental corruption; it cannot detect forgery, despite being named and shaped like an
integrity check. `root_cause_packet_gate` rejects on signature mismatch, which reads as
enforcement and is not.

**Scope of the weakness.** These sign local evidence inside the developer's own checkout. The
literals are not credentials — nothing authenticates to a remote service with them — so this is
integrity theatre rather than a leak. It is listed here because the project's claim is that it
does not overstate what it has verified, and an undisclosed weak check violates that directly.

**Mitigation available today.** Set the variable to at least 32 bytes of hex. A shorter or
non-hex value is ignored and silently falls back to the literal:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

**Why not simply fixed.** The correct pattern already exists in
`scripts/corpus/corpus_manager.py::_load_hmac_key` — configured key if valid, otherwise an
ephemeral `os.urandom(32)` with a loud warning, so an unconfigured run fails closed. Adopting it
in these 23 would invalidate every record already written across all of them, and because the
gate rejects on mismatch that turns today's green evidence red. It needs a `signing_key_source`
field plus a re-sign pass (`scripts/corpus/resign_corpus_records.py` is the existing tool of
that shape), i.e. a migration rather than an edit.

`tests/test_evidence_signing_key_hygiene.py` bounds the set: a 24th family cannot join it
silently, a migrated family must be struck from the list in the same change, the fail-closed
reference cannot regress, and this table cannot drift from the code.

| Module (`scripts/`) | Override variable |
| --- | --- |
| `corpus/programbench/alternate_cleanroom_image_provenance_record.py` | `DETERMINEX_ALTERNATE_CLEANROOM_IMAGE_PROVENANCE_KEY` |
| `corpus/programbench/approved_scanner_setup_record.py` | `DETERMINEX_APPROVED_SCANNER_SETUP_KEY` |
| `corpus/programbench/artifact_source_escalation_record.py` | `DETERMINEX_ARTIFACT_SOURCE_ESCALATION_KEY` |
| `corpus/programbench/bounded_rerun_record.py` | `DETERMINEX_BOUNDED_RERUN_KEY` |
| `corpus/programbench/cleanroom_build_recipe_provenance_gap_record.py` | `DETERMINEX_CLEANROOM_BUILD_RECIPE_PROVENANCE_GAP_KEY` |
| `corpus/programbench/cleanroom_build_recipe_recovery_record.py` | `DETERMINEX_CLEANROOM_BUILD_RECIPE_RECOVERY_KEY` |
| `corpus/programbench/cleanroom_image_hydration_record.py` | `DETERMINEX_CLEANROOM_IMAGE_HYDRATION_KEY` |
| `corpus/programbench/cleanroom_image_import_record.py` | `DETERMINEX_CLEANROOM_IMAGE_IMPORT_KEY` |
| `corpus/programbench/cleanroom_image_remediation_plan_record.py` | `DETERMINEX_CLEANROOM_IMAGE_REMEDIATION_PLAN_KEY` |
| `corpus/programbench/cleanroom_image_scan_record.py` | `DETERMINEX_CLEANROOM_IMAGE_SCAN_KEY` |
| `corpus/programbench/cleanroom_image_scan_triage_record.py` | `DETERMINEX_CLEANROOM_IMAGE_SCAN_TRIAGE_KEY` |
| `corpus/programbench/cleanroom_image_scanner_admission_record.py` | `DETERMINEX_CLEANROOM_SCANNER_ADMISSION_KEY` |
| `corpus/programbench/cleanroom_recipe_provenance_recovery_record.py` | `DETERMINEX_CLEANROOM_RECIPE_PROVENANCE_RECOVERY_KEY` |
| `corpus/programbench/codex_completion_campaign_record.py` | `DETERMINEX_PROGRAMBENCH_CODEX_COMPLETION_CAMPAIGN_KEY` |
| `corpus/programbench/dockerhub_manifest_provenance_record.py` | `DETERMINEX_DOCKERHUB_MANIFEST_PROVENANCE_KEY` |
| `corpus/programbench/infra_failure_triage_record.py` | `DETERMINEX_INFRA_FAILURE_TRIAGE_KEY` |
| `corpus/programbench/official_artifact_security_decision_record.py` | `DETERMINEX_OFFICIAL_ARTIFACT_SECURITY_DECISION_KEY` |
| `corpus/programbench/operator_artifact_admission_record.py` | `DETERMINEX_OPERATOR_ARTIFACT_ADMISSION_KEY` |
| `corpus/programbench/operator_provenance_request_packet_record.py` | `DETERMINEX_OPERATOR_PROVENANCE_REQUEST_PACKET_KEY` |
| `corpus/programbench/real_bounded_rerun_record.py` | `DETERMINEX_REAL_BOUNDED_RERUN_KEY` |
| `corpus/programbench/rebuild_provenance_quarantine_decision_record.py` | `DETERMINEX_REBUILD_PROVENANCE_QUARANTINE_DECISION_KEY` |
| `corpus/programbench/root_cause_packet.py` | `DETERMINEX_ROOT_CAUSE_PACKET_KEY` |
| `corpus/programbench/upstream_artifact_authority_recheck_record.py` | `DETERMINEX_UPSTREAM_ARTIFACT_AUTHORITY_RECHECK_KEY` |

Count: **23** families.
