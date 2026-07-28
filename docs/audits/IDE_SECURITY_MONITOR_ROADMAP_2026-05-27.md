# IDE Security Monitor Roadmap - 2026-05-27

## Goal

Extend the existing IDE health telemetry loop into a lightweight local security monitor. The IDE already polls CPU, backend health, model state, and ProgramBench status; the same surface should report security-relevant drift without turning Determinex into an antivirus product.

## Scope

The security monitor should report signals, not make destructive decisions automatically.

### Phase 1 - Passive Signals

- Listening ports: enumerate local listeners and flag public binds (`0.0.0.0`, `::`) for Ollama, vLLM, LiteLLM, FastAPI, MCP, Tauri sidecars, and benchmark dashboards.
- Risky Python packages: surface installed versions for `starlette`, `fastapi`, `litellm`, `vllm`, `uvicorn`, `gradio`, and `mcp`, with known minimum-safe versions recorded in a local advisory table.
- BadHost guard: flag `starlette <= 1.0.0` and any running ASGI service until Starlette is patched or fronted by a validating reverse proxy.
- Docker exposure: show running containers, published ports, and whether an AI service image is using `latest` instead of a pinned digest/tag.
- Secret-file indexing: report files blocked from RAG/indexing because they match `.env`, key, token, credential, SSH, or cloud config patterns.
- Workspace file churn: count newly created executables/scripts in the workspace and staging directories since the last scan.

### Phase 2 - File Maliciousness Watcher

- Watch workspace, `.determinex_staging`, `sessions`, and `logs` for newly created executable files, shell scripts, PowerShell scripts, Python files, and archive drops.
- Compute SHA-256 for new executables and keep a local allowlist ledger.
- Flag suspicious patterns in new scripts: encoded PowerShell, curl/wget pipe-to-shell, credential exfil strings, netcat reverse shell patterns, and broad recursive delete commands.
- Surface findings in the IDE as `info`, `warn`, or `blocker`; never delete files automatically.

### Phase 3 - Action Hooks

- Add `Quarantine` action that moves a suspicious generated artifact into `.determinex_staging/security_quarantine/` with a manifest and original path.
- Add `Explain` action that opens a local-only security explanation prompt using the suspicious file content and matched rules.
- Add `Trust` action that records a hash allowlist entry for generated binaries/scripts known to be legitimate.
- Add exportable security report JSON for bug reports and audit handoff.

## Backend Integration

Add a new Rust IPC command next to `get_health_telemetry`:

```text
get_security_telemetry -> SecurityTelemetry
```

Suggested response shape:

```text
SecurityTelemetry {
  status: "clean" | "warn" | "critical",
  listeners: [SecurityListener],
  package_findings: [PackageFinding],
  docker_findings: [DockerFinding],
  file_findings: [FileFinding],
  blocked_secret_files: [BlockedSecretFile],
  last_scan_ms: number
}
```

The frontend should render this in the same system/CPU watcher area as health telemetry, with a compact badge and expandable details.

## Guardrails

- Do not upload file contents, hashes, process lists, or package lists to any cloud service.
- Keep the scanner local and deterministic.
- Default to reporting; require explicit user action for quarantine or trust.
- Keep the scan cheap enough to run every 30-60 seconds when the IDE is visible, and pause polling when hidden.

## Immediate Known Advisory

- BadHost / CVE-2026-48710: Starlette `<= 1.0.0` can let malformed `Host` headers poison `request.url.path`, bypassing path-based auth middleware in affected ASGI apps. Minimum safe version: `starlette>=1.0.1`.
