# Determinex Fleet — Privacy Policy (draft)

> **Draft — review with counsel before publishing.** Plain-language description of
> what the fleet contribution path collects, protects, retains, and deletes.

## What we collect

Only what you explicitly opt in to send: **Cloak-obfuscated, oracle-verified code
units** and their derived training pairs, sealed (encrypted) to the node key. Plus,
if you choose to provide one, a **self-chosen handle**.

We do **not** collect: your name, email, IP-as-identity, account credentials, machine
identifiers, or any telemetry. No background "phone home" exists — contribution is a
deliberate, per-shard action.

## How it is protected

- **Identifier obfuscation (Cloak)** before anything leaves your machine — real names
  become opaque tokens; the client fails closed if it cannot fully obfuscate.
- **Explicit consent preview** — you see the exact payload and must opt in.
- **End-to-end sealing** — encrypted in transit and at rest; only the node's private
  key (held offline on our server) can open a shard. The ingest endpoint stores
  ciphertext only.
- **Node-side re-verification** — contributions are re-checked against a compiler/
  test oracle; only what passes is retained.

## What is NOT scrubbed (important)

Cloak obfuscates **identifiers**, not arbitrary string **values**. If your code
contains a secret embedded as a literal (an API key, password, token, personal data),
Cloak will not remove it. **Do not contribute code containing embedded secrets or
personal data.** This is also stated at the consent step.

## Retention & deletion

- Admitted, re-verified pairs are stored (obfuscated) in the fleet corpus and may be
  used to train redistributed models. Once a model is trained on a pair, that
  influence cannot be surgically removed from the weights.
- Sealed shards in the ingest bucket are deleted after processing.
- **Withdrawal:** contributions are content-addressed with no identity linkage. To
  remove a specific shard, contact the maintainer with the `ref` id from upload
  **before** a retrain incorporates it. After a retrain, removal is not possible.

## Children / sensitive data

The fleet is for source code only. Do not contribute personal, sensitive, or
regulated data of any kind.

## Contact

Lunarian Data Systems — see repository contact. Changes to this policy are published
in this file with a dated revision.
