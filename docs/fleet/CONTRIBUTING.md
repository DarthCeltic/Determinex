# Contributing to the Determinex Fleet Corpus

> **Draft terms — review with counsel before publishing.** This governs what you
> agree to when you opt in to share verified work. It is the legal gate that must be
> live before any contribution is accepted.

## What you contribute

When you opt in, Determinex shares **verified (error → fix) work**: small, self-contained
code units that *passed a real compiler/test oracle on your machine*, plus the
training pair derived from them. You choose to contribute — nothing is sent
automatically.

## What is protected before anything leaves your machine

1. **Cloak obfuscation.** Every real identifier (function, class, variable, file
   symbol) is replaced by an opaque token (`x_NNNN`). Logic and structure are
   preserved so the work can be re-verified; *names and intent are not sent.* If
   obfuscation cannot fully run, the client **refuses to send** (fail-closed).
2. **Consent preview.** The client prints the **exact obfuscated payload** that would
   be sent and requires explicit opt-in (`--yes`). Default is a dry-run that only
   seals the shard to disk.
3. **Sealed transport.** The payload is encrypted (X25519 + ChaCha20Poly1305) to the
   node's public key. The upload endpoint stores only ciphertext and cannot read it.

## What you affirm by contributing (the license grant)

By opting in you represent and agree that:

- **You have the right to share this code.** It is your own work, or it is under a
  license that permits this use, and sharing it does not violate any employer/NDA/
  third-party obligation. *Do not contribute code you are not authorized to share.*
- **You grant** Ryan Gurganious a non-exclusive, worldwide, royalty-free
  license to use the contributed (obfuscated) material to train, evaluate, and improve
  Determinex models, and to redistribute the resulting models.
- **You understand** contributions are re-verified and may be dropped, deduplicated,
  or not used. No contribution is guaranteed to be used.
- **No secrets.** You will not contribute credentials, keys, personal data, or
  proprietary data embedded as string literals. Cloak obfuscates *identifiers*, not
  arbitrary secret *values* — do not rely on it to scrub embedded secrets.

## Sign-off

Contributions follow a Developer Certificate of Origin (DCO)-style affirmation: by
opting in, you certify the above. An optional self-chosen handle may be attached;
**no account, email, or PII is required or collected** beyond what you volunteer.

## Withdrawal

Because contributions are obfuscated and content-addressed (no identity linkage),
targeted deletion after admission is best-effort. To withdraw a specific shard,
contact the maintainer with the `ref` id returned at upload **before** a retrain
incorporates it. See [PRIVACY.md](PRIVACY.md).
