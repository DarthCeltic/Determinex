# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| 1.x (latest) | ✅ |
| < 1.0 | ❌ |

## Reporting a Vulnerability

**Do not open a public GitHub issue for security vulnerabilities.**

Report security issues privately via [GitHub Security Advisories](https://github.com/DarthCeltic/determinex/security/advisories/new).

Security reports do not grant source mutation authority, real-user source mutation authority, proof execution authority, training rows, release readiness, production readiness, installer readiness, or open availability. Training eligibility remains false unless a separate signed evidence gate grants it.

Include:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Your suggested fix (optional)

You will receive a response within 48 hours. If the issue is confirmed, a patch will be released as soon as possible and you will be credited in the release notes (unless you prefer anonymity).

## Scope

In scope:
- Remote code execution via AI-generated content
- Tauri IPC privilege escalation
- API key extraction from the local SQLite store
- Prompt injection attacks that break out of the sandboxed workspace

Out of scope:
- Attacks requiring physical access to the machine
- Denial-of-service against local services (Ollama, etc.)
- Issues in third-party dependencies (report upstream)
