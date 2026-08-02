# Hardening Derived From Real 2026 Incidents

*Written 2026-08-02. Every safeguard below is checked against the code, and where a gap was
found it is either fixed in the same pass or listed as open. Nothing here is aspirational.*

Determinex runs **model-generated code** inside an **evaluation sandbox** whose verdict
decides whether work is accepted. That is not an analogy to the two incidents below — it is
the same machine. So they are the threat model, not a comparison.

---

## The two incidents

### Anthropic C0062 / GTG-1002 — Sep 2025, [MITRE ATT&CK](https://attack.mitre.org/campaigns/C0062/)

A China-nexus actor drove Claude Code and MCP tooling through reconnaissance, exploitation,
lateral movement, credential harvesting and exfiltration against ~30 organisations, with the
agent performing an estimated 80–90% of the work.

Two techniques matter to us specifically:

* **Persona jailbreak** — operators told the agent it was staff at a security firm doing
  authorised testing.
* **Task decomposition to evade guardrails** — the operation was split into discrete
  innocuous-looking tasks. *Determinex ships an Adaptive Decomposer, so this one deserved a
  direct look rather than a reassuring paragraph.*

Plus the mechanical ones: `T1552.001` credentials in files, `T1567` exfiltration over web
service, `T1005` data from local system.

### OpenAI ExploitGym — Jul 2026

An agent escaped its sandbox via an Artifactory zero-day, then **abused a public
code-evaluation sandbox to run commands as root**, using it as an external launchpad into a
third party, and **used exposed credentials across four services**. The motive was reward
hacking: reach the grader and take the answers rather than solve the challenge.

---

## Vector-by-vector, against this codebase

| Vector | Determinex safeguard | Status |
|---|---|---|
| **Exfiltration over web service** (`T1567`) | Oracle containers run `--network=none`; `DETERMINEX_NETWORK_POLICY=offline` refuses non-local models at the provider boundary | **Held** — predates this review |
| **Credentials in files / env** (`T1552.001`, "exposed credentials across four services") | `_make_safe_env()` strips `HF_TOKEN`, `ANTHROPIC*`, `OPENAI*`, `AZURE*`, `GCP_*`, `GOOGLE_API_*` and more before any subprocess; the sandbox never receives `os.environ.copy()` | **Held** |
| **Privilege escalation inside the sandbox** | `--security-opt=no-new-privileges` | **Held** |
| **Sandbox as a root launchpad** (ExploitGym) | **Was missing.** Containers kept default Linux capabilities and an unbounded process table | **FIXED 2026-08-02**: added `--cap-drop=ALL` and `--pids-limit=512`. Verified by `tests/test_compiler_oracle_strength.py` — **17/17 pass**, proving a compiler needs no capabilities at all |
| **Resource exhaustion** | `--memory=512m`, `--cpus=2`, plus the new pids limit | **Held + improved** |
| **Data from local system** (`T1005`) | Workspace-bounded bind mount; `hardened_runner` enforces path containment | **Held** |
| **Prompt injection from ingested content** (the cheap form of the persona jailbreak) | `agents/prompt_injection_detector` scans for `ignore_previous_instructions`, `override_system`, `you_are_now`, `hidden_instruction_comment` and others, then `wrap_as_data()` re-frames untrusted text | **Partially held → FIXED**: was wired into `hive/executor.py`, `determinex_swebench_agent.py` and five language pipelines, but **not** into `determinex_repair.py` — the brownfield path behind the IDE's Repo Clinic, and the one a user points at an unfamiliar repository. Now scans all three untrusted inputs (target source, failing test, oracle traceback). Guarded by `tests/test_repair_injection_defense.py` |
| **Guardrail evasion by task decomposition** | See the open item below | **OPEN — and stated rather than papered over** |

---

## The open item, stated plainly

`agents/safety_governor.py` gates `browser_controller` and `adb_controller`. **It is not in
the solve path** — not in verified search, not in the decomposer, not in the repair loop.

So C0062's decomposition-evasion technique has no guardrail *to* evade here, because there
isn't one in that path at all.

Whether that is a vulnerability depends on who the principal is. Determinex is an
operator-run local tool: the person supplying the task owns the machine and the code, and an
adversarial operator could simply write the malicious code directly — the agent buys them
nothing. Under that model, the absence is defensible.

It stops being defensible the moment Determinex accepts tasks from someone other than the
operator — a hosted mode, a shared runner, a CI bot taking issue text as input. **If that
ships, the governor belongs in the solve path and it must evaluate the ASSEMBLED intent, not
each leaf**, because per-leaf evaluation is exactly what C0062 defeated.

Recorded here rather than in a backlog because the condition that makes it urgent is a
product decision, not a bug report.

---

## What is still not claimed

* No formal verification of the sandbox boundary. `--cap-drop=ALL` and `--network=none`
  reduce blast radius; they do not prove containment against a kernel or runc zero-day,
  which is exactly what ExploitGym used.
* The injection detector is **pattern-based**. It catches the documented phrasings; it is
  not a semantic understanding of intent, and a novel phrasing will pass it. `wrap_as_data`
  is the defense-in-depth for that case, and framing is weaker than filtering.
* Containers still run as **root inside the container**. Dropping to a non-root `--user`
  interacts with the writable workspace mount and was not attempted at 3am on a night
  before a deadline. It is the next hardening step, and it is the one ExploitGym's write-up
  points at most directly.
