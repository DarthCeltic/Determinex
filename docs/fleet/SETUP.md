# Fleet hosting setup — what only YOU can do

The engine is built and tested. These are the account/credential steps that require
your logins. Budget ~1–2 hours. Everything here is free-tier.

## 0. Generate the node identity (do this first, offline)

```bash
cd scripts
python -m fleet.cli keygen --out-dir ../secrets
```

- `secrets/node_public.txt` — **publish** this (it ships in the client config).
- `secrets/node_private.txt` — **node only.** Never commit. Add `secrets/` to
  `.gitignore`. On Hetzner: `export DETERMINEX_FLEET_NODE_PRIVKEY="$(cat node_private.txt)"`.
- Note the printed `key_id` — you'll pin it in the Worker.

> The private key is the whole security model. If it leaks, rotate it (new keypair,
> re-publish the public key in the client). Treat it like the API keys.

## 1. Hugging Face — the trust-bearing front (free)

Create under your org (`lunariandatasystems`):

1. **Dataset repo** `determinex-fleet-corpus` — set it **gated** (you approve access).
   This is provenance + the public face. Put `docs/fleet/CONTRIBUTING.md` and
   `PRIVACY.md` as the dataset card. *Admitted, re-verified pairs* land here after
   the node processes them (push from Hetzner with `huggingface_hub`).
2. **Model repo** `determinex-engineer` (and observer/sentinel) — where you push new
   LoRA adapters / GGUF after a retrain. Clients OTA-pull from here.

```bash
pip install huggingface_hub
huggingface-cli login            # your HF token (write scope)
huggingface-cli repo create determinex-fleet-corpus --type dataset
huggingface-cli repo create determinex-engineer  --type model
```

## 2. Cloudflare — the authed encrypted ingest (free)

```bash
npm i -g wrangler
wrangler login                                   # your Cloudflare account
wrangler r2 bucket create determinex-fleet-shards   # holds SEALED ciphertext only
cd cloudflare/fleet-ingest
wrangler secret put EXPECTED_NODE_KEY_ID         # paste the key_id from step 0
wrangler deploy                                  # prints the ingest URL
```

The deploy prints a URL like `https://determinex-fleet-ingest.<you>.workers.dev`. That
is the `--post-url` contributors use. The Worker stores only sealed ciphertext; it
cannot read contributions.

## 3. Node pull loop (Hetzner — private)

R2 is S3-compatible. Configure `rclone` (or `aws s3` with R2 creds) once, then:

```bash
# pull new sealed shards
rclone copy r2:determinex-fleet-shards/incoming ./inbox --include "*.sealed.json"

# open + RE-VERIFY (sandboxed) + admit to the corpus
export DETERMINEX_FLEET_NODE_PRIVKEY="$(cat secrets/node_private.txt)"
cd scripts
python -m fleet.cli ingest ../inbox/*.sealed.json --apply \
    --corpus ../corpus/programbench/training_corpus/fleet_corpus.jsonl
```

Then run the existing flywheel retrain on the grown corpus and push the new adapter
to the HF model repo. For maximum safety against hostile contributions, run the
`ingest` step inside a disposable VM/container (it executes contributed test code,
sandboxed + network-denied, but defense-in-depth is cheap).

## 4. Client config (ships in the app)

Contributors only need the **public** key + the Worker URL:

```bash
cd scripts
python -m fleet.contribute --items my_items.json \
    --node-pub "$(cat ../secrets/node_public.txt)" \
    --post-url https://determinex-fleet-ingest.<you>.workers.dev \
    --yes          # omit --yes for a dry-run that only seals to disk
```

## Pre-launch checklist

- [ ] Node keypair generated; private key on node only; `secrets/` gitignored.
- [ ] HF dataset (gated) + model repos created; cards = CONTRIBUTING + PRIVACY.
- [ ] R2 bucket + Worker deployed; `EXPECTED_NODE_KEY_ID` pinned.
- [ ] CONTRIBUTING.md (consent + data license) and PRIVACY.md **published**.
- [ ] Patent provisional filed (if protecting the fleet mechanism) **before** launch.
- [ ] One real end-to-end contribution dry-run → seal → upload → node ingest verified.
