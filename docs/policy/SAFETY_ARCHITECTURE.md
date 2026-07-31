# Determinex Safety Architecture

**Date:** 2026-05-27  
**Status:** Implemented and active

---

## Overview

Determinex's safety system enforces the Usage Policy at every pipeline stage through five independent layers. Each layer is designed to fail-closed: if the layer encounters an unexpected error, it denies rather than passes the request.

No single layer is sufficient. Together they address: deliberate misuse, accidental misuse, prompt injection, reframing attacks, credential leakage, malicious generated code, and corpus poisoning.

---

## Layer Map

```
User Input (spec / question / issue)
         │
         ▼
[L0] Content Policy ─── categorical keyword scan → DENY or PASS
         │
         ▼
[L1] Intent Classifier ─ signal + amplifying context → DENY or PASS
         │
         ▼
   DAG Generator → Builder (LLM generates code)
         │
         ▼
[L2] Egress Filter ───── secrets in prompts → DENY before cloud API call
         │
         ▼
   Cloud / Local API call
         │
         ▼
[L3] Output Scanner ──── malicious patterns in Builder code → DENY or PASS
         │
         ▼
   Compiler Oracle (rustc / go / python / tsc) — functionality gate
         │
         ▼
[L4] Corpus Sign/Verify ─ HMAC on verdict corpus entries → tamper detection
         │
         ▼
   Training Flywheel
```

Additionally:

- **Docker enforcement** (compiler sandbox): `DETERMINEX_REQUIRE_DOCKER=1` blocks fallback to lower-isolation execution tiers
- **Cloak enforcement**: `DETERMINEX_REQUIRE_CLOAK=1` blocks cloud API calls when identifier obfuscation is inactive

---

## Layer 0 — Content Policy

**File:** `scripts/determinex_safety.py` → `_DENY_PATTERNS`  
**Called from:** `scripts/determinex_hive.py` via `pre_spec_gate()` before session creation  
**Mode:** Fail-closed, raises `SafetyDenied`

### What it does

Categorical keyword scan across the full spec text. Uses pre-compiled regex patterns per harm category. A single match in any category triggers an immediate denial.

### Harm categories covered

**Absolute (zero-exception):**
- `MALWARE_RANSOMWARE` — ransomware, file encryptors, crypto lockers
- `MALWARE_WIPER` — disk wipers, data destruction, MBR overwriters
- `MALWARE_DROPPER` — payload delivery, self-replicating, dropper malware
- `MALWARE_TROJAN` — backdoors, trojans, hidden implants
- `MALWARE_BOOTKIT` — rootkits, bootkits, UEFI implants, kernel rootkits
- `MALWARE_BOTNET` — botnet clients, C2 infrastructure, bot herders
- `EXPLOIT_SHELLCODE` — shellcode generation and packaging
- `EXPLOIT_BUFFEROVERFLOW` — heap spray, ROP chains, use-after-free exploits
- `EXPLOIT_CVE` — CVE weaponization, working exploit code
- `EXPLOIT_PRIVESC` — privilege escalation exploits, SUID exploits
- `ATTACK_DDOS` — DDoS tools, flooding, amplification attacks
- `ATTACK_SCANNING` — automated exploit scanners
- `CREDENTIAL_HARVEST` — credential stealers, LSASS dumpers, Mimikatz equivalents
- `CREDENTIAL_STUFFING` — stuffing tools, password sprayers, brute-force login
- `CREDENTIAL_PHISHING` — phishing kits, phishing page generators, smishing
- `RAT_REMOTE_ACCESS` — remote access trojans, reverse shell implants
- `KEYLOGGER` — keystroke loggers, keyboard sniffers
- `STALKERWARE` — covert tracking, hidden phone spy, stealth monitoring
- `SCREENSHOT_COVERT` — hidden screen capture, stealth recording
- `INFOOPS_ASTROTURFING` — sock puppet networks, coordinated inauthentic behavior
- `INFOOPS_DISINFO` — automated propaganda, fake news generators
- `HARASSMENT_FLOOD` — contact bombing, SMS bombing, harassment bots
- `HARASSMENT_DOXX` — doxxing tools, identity exposure, anonymous unmasking
- `FRAUD_ACADEMIC` — ghostwriting for submission, plagiarism laundering
- `FRAUD_IDENTITY` — forged documents, fake IDs, counterfeit credentials
- `FRAUD_FINANCIAL` — carding tools, bank fraud, invoice fraud
- `CSAM` — child sexual abuse material
- `WEAPONS_INSTRUCTIONS` — explosives, chemical/biological weapons, IEDs
- `WEAPONS_CRITICAL_INFRA` — attacks on power grids, water, hospitals, nuclear

**Ethical (legal but harmful):**
- `SURVEILLANCE_UNDISCLOSED` — monitoring without telling the monitored person
- `MANIPULATION_DARKPATTERN` — fake urgency, hidden unsubscribe, misdirection UI
- `MANIPULATION_ADDICTION` — variable reward addiction optimization
- `REVIEW_MANIPULATION` — fake review generation, review bombing
- `DISCRIMINATION_PROXY` — proxy-based discriminatory screening
- `ECONOMIC_WAGETHEFT` — timesheet fraud, wage theft automation
- `SPAM_INFRASTRUCTURE` — bulk unsolicited email/SMS
- `CRYPTO_UNAUTHORIZED` — cryptojacking, covert mining deployment
- `VOICE_CLONE_HARM` — voice cloning for fraud or impersonation
- `DEEPFAKE_HARM` — non-consensual deepfakes, synthetic defamation
- `OSINT_TARGETING` — OSINT aggregation for stalking or targeting
- `PREDATORY_FINANCE` — debt trap maximization, predatory lending tools

### Configuration

```
DETERMINEX_SAFETY_MODE=strict   (default) — raise SafetyDenied on violation
DETERMINEX_SAFETY_MODE=warn     — log and return unsafe verdict, do not raise
DETERMINEX_SAFETY_MODE=audit    — log everything, always pass (test only)
```

---

## Layer 1 — Intent Classifier

**File:** `scripts/determinex_safety.py` → `_COMPILED_INTENT`  
**Called from:** `check_spec()` after L0 passes  
**Mode:** Fail-closed, raises `SafetyDenied`

### What it does

Catches requests that reframe prohibited content using indirect language. A match requires BOTH a suspicious signal keyword AND at least one amplifying contextual pattern in the same text.

Example: "monitor" alone passes (legitimate). "monitor without the user's knowledge" → `COVERT_MONITORING` → DENY.

### Signal + context pairs

| Signal | Amplifiers | Category |
|---|---|---|
| `monitor` | without consent / covert / hidden / stealth | `COVERT_MONITORING` |
| `track` | without consent / stalking / locate someone | `COVERT_TRACKING` |
| `scrape / harvest / collect` | without consent / to target / to profile | `NONCONSENSUAL_DATA` |
| `automate` | harassment / flood / spam | `AUTOMATED_HARASSMENT` |
| `bypass / evade / circumvent` | antivirus / detection / EDR / sandbox | `EVASION` |
| `inject / hook / intercept` | process memory / DLL / LSASS / credential | `CODE_INJECTION` |
| `persistence / persist` | registry / startup / cron / survive reboot | `PERSISTENCE_MECHANISM` |
| `exfiltrate / send to server` | without knowledge / covert / credentials | `DATA_EXFILTRATION` |
| `obfuscate / packer / encrypt payload` | detection / antivirus / malware | `OBFUSCATION_FOR_EVASION` |
| `clone / mimic` | voice / face / without consent / deepfake | `SYNTHETIC_IDENTITY` |

---

## Layer 2 — Egress Filter

**File:** `scripts/hive/safety_gate.py` → `pre_api_gate()`  
**Called from:** `scripts/hive/api_client.py` → `api_call()` before every API call  
**Mode:** Fail-closed, raises `SafetyDenied` or `RuntimeError`

### What it does

1. **Secret detection:** Scans all outbound prompt content for known secret token patterns (AWS keys, GCP keys, GitHub tokens, OpenAI keys, Anthropic keys, Slack tokens, SendGrid, PEM private keys, credential-embedded URLs).

2. **Env var assignment detection:** Blocks prompts containing credential environment variable assignments (e.g. `ANTHROPIC_API_KEY=sk-...`).

3. **Cloak enforcement:** If `DETERMINEX_REQUIRE_CLOAK=1` (default) and the target is a cloud provider (non-Ollama), blocks the call if Cloak is not active.

### Configuration

```
DETERMINEX_REQUIRE_CLOAK=1      (default) — block cloud calls without Cloak
DETERMINEX_REQUIRE_CLOAK=0      — allow unobfuscated cloud calls (privacy reduction)
```

---

## Layer 3 — Output Scanner

**File:** `scripts/determinex_safety.py` → `check_output()` / `scripts/hive/compiler.py` → `scan_builder_output_security()`  
**Called from:** `scripts/hive/compiler.py` after Builder code is generated  
**Mode:** Fail-closed, raises `SafetyDenied`

### What it does

Scans generated production code for malicious-intent patterns. Unlike the test harness sentinel (which blocks all `fs`/`net` imports), this scanner targets behavioral indicators of malicious intent.

### Hard-block patterns (single match = deny)

| Pattern ID | What it detects |
|---|---|
| `EXFIL_HARDCODED_HOST` | HTTP/socket calls to hardcoded external hostnames |
| `LSASS_READ` | LSASS process memory reads, MiniDump, SeDebugPrivilege |
| `SHADOW_READ` | Reads to `/etc/shadow` (Unix password database) |
| `REGISTRY_CRED_READ` | Windows SAM/SECURITY registry credential reads |
| `KEYLOG_API` | SetWindowsHookEx WH_KEYBOARD, GetAsyncKeyState, pynput listener |
| `PROCESS_MASQUERADE` | setproctitle to svchost/explorer (anti-forensics) |
| `ANTIDEBUG` | IsDebuggerPresent, CheckRemoteDebugger, ptrace TRACEME |
| `ANTIVM` | VirtualBox/VMware/QEMU detection routines |
| `SHELLCODE_PATTERN` | Long hex byte runs matching shellcode structure |
| `MMAP_EXEC` | Memory-mapped executable pages (shellcode injection) |
| `CRYPTO_HIJACK` | Stratum URLs, xmrig, cryptominer pool connections |

### Contextual patterns (signal + amplifier required)

| Signal | Amplifier | Category |
|---|---|---|
| `shutil.rmtree / os.remove` | system paths (`/etc`, `C:\Windows`) | `DESTRUCTIVE_SYSTEM_PATH` |
| `startup / HKCU\Run / crontab` | persist / survive / autostart | `PERSISTENCE_WRITE` |
| `subprocess.run(shell=True)` | string formatting/concatenation in command | `COMMAND_INJECTION_RISK` |

### Python dynamic execution

Additional check for: `__import__()`, `exec(compile(...))`, `eval(base64...)`, `marshal.loads`, `pickle.loads(base64...)`.

---

## Layer 4 — Corpus Integrity

**File:** `scripts/determinex_safety.py` → `sign_corpus_entry()` / `verify_corpus_entry()`  
**Wrappers:** `scripts/hive/workspace.py` → `sign_corpus_entry()` / `verify_corpus_entry()`  
**Mode:** Raises `CorpusTamperError` on verification failure

### What it does

Every verdict corpus entry written to `pb_verdict_corpus.jsonl` is HMAC-signed using BLAKE2b-256. The signature covers the canonical JSON serialization of the entry (sorted keys, ASCII-safe). At ingest time for retraining, entries with missing or invalid signatures are rejected.

### Key management

```
DETERMINEX_CORPUS_HMAC_KEY=<hex, 32 bytes minimum>   — production key, persists across restarts
(not set)                                          — session-ephemeral key (in-process protection only)
```

Set `DETERMINEX_CORPUS_HMAC_KEY` in `.env` before running any training pipeline in production.

---

## Sandbox Enforcement

**File:** `scripts/hive/compiler.py` → `_docker_run()`  
**Config:** `DETERMINEX_REQUIRE_DOCKER=1` (default)

When Docker execution fails, the system no longer silently falls back to WSL2 or direct execution (lower isolation tiers). Instead it raises a `RuntimeError` with instructions to fix Docker or explicitly opt out.

| Tier | Isolation | Network | Credential exposure |
|---|---|---|---|
| Docker | Container, ephemeral | `--network=none` | None (no host env) |
| WSL2 | Process, `env -i` | Host firewall only | None (env stripped) |
| Direct | Process, env stripped | Host firewall only | Possible via system calls |

To use WSL2 or direct mode: `DETERMINEX_REQUIRE_DOCKER=0`.

---

## Cloak Enforcement

**File:** `scripts/hive/safety_gate.py` → `pre_api_gate()`  
**Config:** `DETERMINEX_REQUIRE_CLOAK=1` (default)

Cloud API calls (non-Ollama) are blocked if Cloak is not active. This prevents source code from being sent to external LLM providers in plaintext.

To disable: `DETERMINEX_REQUIRE_CLOAK=0`. This reduces privacy protection and should only be set in air-gapped / Ollama-only deployments.

---

## Environment Variable Reference

| Variable | Default | Effect |
|---|---|---|
| `DETERMINEX_SAFETY_MODE` | `strict` | `strict`=raise on violation, `warn`=log only, `audit`=always pass |
| `DETERMINEX_REQUIRE_DOCKER` | `1` | `1`=block fallback to non-Docker execution, `0`=allow fallback |
| `DETERMINEX_REQUIRE_CLOAK` | `1` | `1`=block cloud calls without Cloak, `0`=allow plaintext cloud calls |
| `DETERMINEX_CLOAK` | (unset) | `1`=enable Project Cloak obfuscation |
| `DETERMINEX_CORPUS_HMAC_KEY` | (ephemeral) | 32-byte hex key for corpus HMAC signatures |

---

## Implementation Files

| File | Role |
|---|---|
| `scripts/determinex_safety.py` | Core engine: content policy, intent classifier, egress filter, output scanner, corpus HMAC |
| `scripts/hive/safety_gate.py` | Pipeline adapter: `pre_spec_gate`, `pre_api_gate`, `post_generation_gate`, corpus gates |
| `scripts/hive/compiler.py` | `scan_builder_output_security()` (SEC-2), Docker enforcement in `_docker_run()` |
| `scripts/hive/api_client.py` | `api_call()` wired to `pre_api_gate()` before every cloud call |
| `scripts/hive/workspace.py` | `sign_corpus_entry()` / `verify_corpus_entry()` wrappers |
| `scripts/determinex_hive.py` | `cmd_new_session()` wired to `pre_spec_gate()` at CLI entry |
| `USAGE_POLICY.md` | Human-readable policy statement |

---

*Determinex Safety Architecture · Ryan Gurganious · 2026-05-27*
