# Determinex Fleet Learning

Opt-in, consent-first, **oracle-verified** corpus contribution. Downloaded Determinex
instances can *willingly* share their verified (error → fix) work to improve the
shared models — without leaking proprietary code, and without letting bad data in.

> Status: **v1 engine built + tested in-repo** (`tests/test_fleet.py`, 6/6).
> Hosting (HF repos + Cloudflare Worker/R2) is an operator setup step — see
> [SETUP.md](SETUP.md). Governance docs ([CONTRIBUTING.md](CONTRIBUTING.md),
> [PRIVACY.md](PRIVACY.md)) must be published **before** accepting any contribution.

## Why this is safe (the two guarantees)

1. **Nothing proprietary leaves the contributor.** Every contributed item is
   **Cloak-obfuscated** — every real identifier becomes an opaque `x_NNNN` token —
   and then **sealed** (X25519 + ChaCha20Poly1305) to the node's public key. The
   client shows the *exact* obfuscated payload and requires an explicit opt-in
   (`--yes`); default is dry-run. If Cloak cannot fully obfuscate, the client
   **fails closed** and sends nothing.
2. **Nothing bad gets into the corpus.** On the node, every contributed pair is
   **re-verified against the same deterministic oracle that built the corpus**
   (`get_oracle(lang).verify`). A poisoned/garbage contribution cannot compile or
   pass tests, so it is dropped — it can never become training data. The fleet is
   poisoning-resistant by construction.

## Architecture (v1 — shipped)

```
CONTRIBUTOR (any downloaded Determinex)              NODE (you, Hetzner — private)
  verified (error→fix) item                         DETERMINEX_FLEET_NODE_PRIVKEY (secret)
    │ Cloak obfuscate (fail-closed)                    │
    │ consent preview + explicit opt-in                │ pull sealed shards from R2
    │ seal → node PUBLIC key                           │ open  (only the node can)
    ▼                                                  ▼ re-verify each item vs ORACLE
  POST sealed envelope ──► Cloudflare Worker ──► R2 ──► admit PASS → fleet_corpus.jsonl
        (sees only ciphertext)   (sealed only)         drop FAIL/poison/dup
                                                        │
   HF model repo  ◄── push new LoRA adapter ◄── flywheel retrain on grown corpus
        │ OTA pull
        ▼
   contributors get smarter models
```

- **Trust-bearing front:** Hugging Face — a gated **dataset repo** (provenance) and a
  **model repo** (OTA adapter distribution). Where contributors already are.
- **Authed ingest:** a **Cloudflare Worker + R2** (free tier, zero egress) takes the
  sealed POST and stores opaque ciphertext. The Worker never decrypts.
- **Private worker:** your **Hetzner** box holds the private key, pulls, re-verifies,
  retrains. Never the public face.

## Components

| Piece | Path |
|---|---|
| Sealed-box crypto (X25519+ChaCha20) | `scripts/fleet/crypto.py` |
| Wire schema | `scripts/fleet/protocol.py` |
| Consent-first client (Cloak + preview + seal) | `scripts/fleet/contribute.py` |
| **Keystone:** node re-verification + ingest | `scripts/fleet/ingest_verify.py` |
| Operator CLI (`keygen`, `ingest`) | `scripts/fleet/cli.py` |
| Cloudflare ingest Worker | `cloudflare/fleet-ingest/` |
| Tests (6/6) | `tests/test_fleet.py` |

## v2 roadmap (documented, not built)

Never-sees-plaintext federation: clients train **local LoRA deltas** and upload only
adapter deltas / DP-noised signals; raw code never leaves the machine. v1's Cloak +
seal + node-side oracle re-verification is the shippable floor; v2 is the upgrade.

## Pre-launch gate

This is a fleet-contribution feature on your patent-candidate list. If you intend to
protect it, **file the provisional before this ships publicly** — public disclosure
starts the clock (US 1-yr grace; elsewhere it bars patentability). See the IP audit.
