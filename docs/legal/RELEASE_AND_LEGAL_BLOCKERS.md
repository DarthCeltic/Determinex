# Release & Legal Blockers Requiring Ryan's Decision

> These items cannot be resolved by an agent acting alone — each requires
> either a purchase decision, a real external search/filing, or authority
> only Ryan (as the human principal) has. Documented 2026-07-01 as part of
> the Tier 3 release-engineering/legal sweep so they're tracked rather than
> silently dropped.

## 1. Code signing certificate

**Blocker**: Tauri's Windows/Mac installers are unsigned. No code-signing
certificate exists in this repo or has been purchased.

**Why it needs Ryan**: requires a real-money purchase (EV/OV code-signing
cert, ~$70-400+/year depending on vendor and whether hardware-token EV
signing is used) and identity verification tied to Ryan Gurganious as
a legal entity — not something that can be provisioned by an agent.

**What's ready once a cert exists**: Tauri's build config
(`frontend/src-tauri/tauri.conf.json`) supports a `bundle.windows.certificateThumbprint`
/ `bundle.macOS.signingIdentity` field — wiring the actual signing step into
the build is mechanical once the cert is in hand. Not done yet since there's
nothing to wire.

## 2. Auto-updater

**Blocker**: no Tauri updater endpoint configured (`plugins.updater` in
`tauri.conf.json` is absent). Auto-update needs a signing keypair
(`tauri signer generate`) and a hosted update-manifest endpoint.

**Why it's bundled with #1**: Tauri's updater signature scheme is separate
from code-signing certs but is also a "generate a real keypair, decide
where the update manifest is hosted" decision — reasonable to make together
with the code-signing decision rather than as two unrelated calls.

**What's ready once decided**: the updater plugin is a config addition +
keypair generation; no architectural blocker, just an unmade decision about
hosting (Determinex currently doesn't have a public release channel — see
CLAUDE.md's note that GitHub is storage-only, not a CI/release pipeline).

## 3. Cross-platform build proof (Mac/Linux)

**Blocker**: development happens on Windows. Mac/Linux Tauri builds have
not been proven to actually run — the frontend build is verified on Windows
only (`npm run build`, `cargo check` — both Windows-verified this session
and prior sessions).

**Why it needs Ryan (or at least isn't agent-resolvable today)**: no Mac/
Linux machine or CI runner is available in this environment to actually
build and smoke-test on those platforms. Claiming "cross-platform support"
without running the build on those platforms would be exactly the kind of
false-confidence claim this session has been correcting elsewhere (PB lock
counts, dependency scan false-pass, security gate blind spots) — better to
leave it honestly unverified than assert it works.

## 4. Trademark search on "Determinex"

**Blocker**: no real USPTO (or equivalent) trademark search has been run.

**Why it needs Ryan**: a real trademark clearance search requires either a
paid search service or legal counsel — not something an agent can
meaningfully substitute for with a web search. This is *more* urgent than
usual: project memory (`user_ide_preference.md`-adjacent notes) records that
Ryan has already flagged a likely name collision with a Tokyo-based AI
company also using "Determinex," and directed keeping distribution local for
now pending a resolution. This doc doesn't change that guidance — it's
recorded here so the trademark question doesn't fall out of the release
punch list.

**Current mitigation already in place**: per Ryan's prior instruction,
public/external distribution is paused; local-only operation continues
without a trademark blocker since no public-facing use of the name is
occurring under this session's authority.

## Summary

| Item | Blocked on | Agent-actionable today? |
|---|---|---|
| Code signing cert | Purchase + identity verification | No |
| Auto-updater | Keypair + hosting decision (bundle with cert decision) | No |
| Mac/Linux build proof | Access to non-Windows build environment | No |
| Trademark search | Paid search / counsel + name-collision resolution | No |

None of these are technical implementation gaps — they're either purchase/
legal-authority decisions or require infrastructure (non-Windows build
hosts) not present in this environment. Flagging them here keeps them
visible on the release punch list rather than silently dropped because no
code change was possible.
