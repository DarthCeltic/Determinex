# Determinex Privacy Policy — DRAFT, NOT LEGAL ADVICE, NOT BINDING

> **This is a starting point for actual legal review, not a policy in
> effect.** It was drafted 2026-07-01 from the verified current behavior of
> the software (see "How this was verified" below) so that Ryan/counsel have
> an accurate draft to edit rather than a blank page or generic SaaS
> boilerplate that wouldn't match what Determinex actually does. Do not publish,
> link from a release, or represent this as Determinex's privacy policy until a
> qualified attorney has reviewed and approved it.

## How this was verified (not assumed)

Before drafting, the following was checked against the actual codebase
rather than assumed:

- **No third-party telemetry/analytics.** Grepped for common
  telemetry SDKs (PostHog, Segment, Mixpanel, Amplitude) — the only real hit
  is `scripts/determinex_otel.py`, which is OpenTelemetry instrumentation
  exporting to a *self-hosted* OTLP endpoint (Grafana Tempo/Jaeger), not a
  third-party service. Determinex does not phone home.
- **Cloud API calls are explicit opt-in**, gated by
  `DETERMINEX_ALLOW_CLOUD_FALLBACK=1` (`scripts/hive/api_client.py::_resolve_model`)
  — without it, a cloud model call raises rather than silently proceeding.
- **Project Cloak** obfuscates identifiers before any cloud API call when
  enabled (`DETERMINEX_CLOAK=1`), and `hive/safety_gate.py::pre_api_gate`
  enforces Cloak-or-block for cloud providers when
  `DETERMINEX_REQUIRE_CLOAK=1` (default).
- **Data storage is local**: sessions, corpus, logs, model weights all live
  under the user's own `C:\Dev\Determinex` install — no Determinex-operated
  backend receives or stores this data.

## 1. What Determinex is

Determinex is locally-installed software. It is not a hosted service. Unless
you explicitly configure cloud API access, Determinex processes your code and
data entirely on your own machine.

## 2. Data Determinex processes

- **Your source code and specs**, to generate/repair/analyze code locally.
- **Local logs and session records** (build attempts, compiler results,
  training-queue entries) — stored under `logs/` and `sessions/` on your
  own disk, never transmitted anywhere by default.
- **Model weights and training corpus** — stored under your configured
  `DETERMINEX_MODELS_DIR`, local to your machine.

## 3. When data leaves your machine

Only when you explicitly enable cloud model access
(`DETERMINEX_ALLOW_CLOUD_FALLBACK=1`) and configure a cloud provider API key.
In that case:

- The prompt/spec content for that specific call is sent to the configured
  provider (Anthropic, DeepSeek, Google, OpenRouter, etc.) under **that
  provider's own privacy policy and terms** — Determinex does not control or
  see what the provider does with it beyond the API response.
- If Project Cloak is enabled, identifiers in your code (variable/function/
  class names) are replaced with opaque tokens before the cloud call, and
  restored locally afterward — the cloud provider never sees your real
  identifier names. Cloak does not anonymize the *structure* or *logic* of
  the code, only identifiers.
- Egress scanning (`determinex_safety.check_egress`) blocks known secret/
  credential patterns from reaching a cloud call, but is not a guarantee
  against all possible sensitive-data leakage — review what you send.

## 4. Third-party model providers

If you use a cloud model, that provider's own data-handling terms apply to
whatever is sent to them. Determinex does not control provider-side retention,
training-on-your-data policies, or geographic data handling — consult each
provider's own privacy policy (Anthropic, DeepSeek, Google, OpenAI, etc.)
before sending sensitive code through them.

## 5. Local model use

When using local models (Ollama), no data leaves your machine for that
call — inference runs entirely on your own hardware.

## 6. What we (Lunarian Data Systems) do not do

- We do not operate a backend that receives your code, logs, or usage data.
- We do not sell or share data, because we do not collect any in the first
  place under normal local-only operation.
- [TODO — legal to confirm]: if/when a hosted or telemetry-enabled tier is
  ever introduced, this document must be revised before that ships.

## 7. Open questions for legal review

- Should this policy cover the *installer/updater* separately (crash
  reports, update-check pings) once auto-update ships? Not yet built — see
  the release-engineering blocker doc.
- GDPR/CCPA applicability once any hosted component exists.
- Data processing addendum needs, if Determinex is ever offered as an
  enterprise/hosted product (see CLAUDE.md's "VPC Forge enterprise tier").
