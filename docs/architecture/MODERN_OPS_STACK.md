# Determinex Modern Ops Stack (2026-05-16)

This document is the **deployment runbook** for everything built in the wave-3 modernization push.

The goal: replace 1980s-style shell scripts + JSON files + manual SSH polling with
state-of-the-art self-hosted infrastructure.

## What we replaced

| 1980s | Modern |
|---|---|
| `tail -f` across pool_local-*.log | **Loki + Grafana** log aggregation |
| `wc -l done.txt` manual polling | **Prometheus + Grafana** dashboards + auto-refresh |
| `/root/queue/*.txt` flock-based queue | **Postgres** `work_queue` with SKIP LOCKED atomic claim |
| 6 separate JSON files for state | **SQLite + Postgres** with pgvector |
| Manual `docker rmi` cycle | **Patched programbench**: cached compiled images persist |
| Hand-rolled architect/builder/monitor loop | **LangGraph** state graph with conditional routing |
| 17 manual iterations of regen→push→eval | **n8n workflow** auto-triggers on pool drain |
| `scp` + `ssh` for every deploy | **GitOps via ArgoCD** + `git push` |
| No experiment tracking | **W&B** runs with score history |
| No tracing | **OpenTelemetry Collector** → Grafana Tempo |
| Plaintext `.env` secrets | **HashiCorp Vault** dev mode |
| Manual SSH keys | **Tailscale** wireguard mesh |
| Raw `docker run` per worker | **k3s Deployment + HPA** (auto-scale on queue depth) |
| Ollama single-instance | **vLLM** with tensor parallelism |
| File-based markdown RAG | **pgvector HNSW** semantic search |

## Files in this wave

### Code / scripts
- `scripts/determinex_db.py` — SQLite state DB CLI (init, import-evals, top, bottom, history, stats)
- `scripts/determinex_queue.py` — Redis/Postgres queue (replaces /root/queue/*.txt)
- `scripts/determinex_notify.py` — Discord/Slack/Telegram/Generic webhook poster
- `scripts/determinex_metrics.py` — Prometheus exporter on :9101
- `scripts/determinex_otel.py` — OpenTelemetry tracing instrumentation
- `scripts/determinex_wandb.py` — W&B experiment logging
- `scripts/determinex_rag_index.py` — pgvector ingest + semantic query
- `scripts/determinex_langgraph_orchestrator.py` — LangGraph multi-agent skeleton
- `scripts/determinex_vllm_serve.sh` — vLLM serving with tensor parallel auto-detect
- `scripts/worker_v2.sh` — modernized worker (webhook, metrics, OTEL)
- `scripts/install_hetzner_stack.sh` — one-shot Hetzner bootstrap
- `scripts/pool_prewarm.sh` — pre-warm Docker images outside the timer (legacy, kept for fallback)

### Infrastructure
- `docker/monitoring/docker-compose.yml` — full ops stack
- `docker/monitoring/prometheus.yml`
- `docker/monitoring/loki-config.yaml`
- `docker/monitoring/promtail-config.yml`
- `docker/monitoring/postgres-init.sql` — schema with pgvector + view + claim_next function
- `docker/monitoring/grafana-provisioning/datasources/datasources.yml`
- `docker/monitoring/grafana-provisioning/dashboards/dashboards.yml`
- `docker/monitoring/grafana-provisioning/dashboards/determinex-overview.json`
- `docker/monitoring/n8n-workflows/determinex_eval_loop.json`
- `k3s/manifests/determinex-worker.yaml` — Deployment + HPA + Postgres StatefulSet
- `k3s/argocd/determinex-app.yaml` — GitOps Application

### CI/CD
- `.github/workflows/determinex-eval.yml` — lint + smoke + dispatch-to-Hetzner

## Deployment order

### Phase A — Local (no Hetzner changes)
```bash
# 1. SQLite state — already working
python scripts/determinex_db.py init
python scripts/determinex_db.py import-evals
python scripts/determinex_db.py stats

# 2. Set webhook
export DETERMINEX_NOTIFY_URL='https://discord.com/api/webhooks/.../...'
python scripts/determinex_notify.py "Stack v3 installed"
```

### Phase B — Hetzner ops stack
```bash
# 1. scp configs
scp -r docker/monitoring/* root@5.78.192.163:/root/determinex-ops/
scp scripts/install_hetzner_stack.sh root@5.78.192.163:/root/

# 2. SSH and bootstrap
ssh root@5.78.192.163
TAILSCALE_AUTHKEY=tskey-xxx \
DETERMINEX_NOTIFY_URL=https://discord.com/... \
bash /root/install_hetzner_stack.sh

# 3. Browser-access via Tailscale (or public IP)
# Grafana:     http://determinex-eval:3000
# uptime-kuma: http://determinex-eval:3001
# n8n:         http://determinex-eval:5678
# memos:       http://determinex-eval:5230
# vault:       http://determinex-eval:8200
```

### Phase C — Programbench cache patch (one-time, manual)
```bash
ssh root@5.78.192.163
cp /root/ProgramBench/src/programbench/eval/eval.py /root/ProgramBench/src/programbench/eval/eval.py.determinex_bak
python3 /tmp/pb_patch.py  # already uploaded
```
This makes all subsequent evals 5-10× faster because compiled images persist.

### Phase D — Worker upgrade
```bash
scp scripts/worker_v2.sh root@5.78.192.163:/root/queue/worker.sh
chmod +x /root/queue/worker.sh
```

### Phase E — k3s + ArgoCD (long-term)
```bash
ssh root@5.78.192.163
# install_hetzner_stack.sh already installs k3s
k3s kubectl create namespace argocd
k3s kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
k3s kubectl apply -f /root/determinex/k3s/argocd/determinex-app.yaml
# ArgoCD now auto-syncs k3s/manifests/* on every git push
```

### Phase F — vLLM serving (replaces Ollama for higher throughput)
```bash
./scripts/determinex_vllm_serve.sh determinex-engineer-v11-dsl
# Now point your providers config at http://localhost:8000/v1
```

## Acceptance checklist

- [ ] Patch applied — `programbench-compiled/*:determinex-cached` images visible after first eval
- [ ] Discord webhook fires on every tool completion (test: `python scripts/determinex_notify.py "test"`)
- [ ] SQLite has scores — `python scripts/determinex_db.py top 15`
- [ ] Grafana shows live pool state at port 3000
- [ ] uptime-kuma alerts when worker.sh dies
- [ ] n8n workflow imported and active
- [ ] vLLM responds to OpenAI-compatible API
- [ ] ArgoCD reconciles k3s manifests from git
- [ ] OpenTelemetry spans visible in Grafana

## Estimated impact

| Metric | Before | After |
|---|---|---|
| Eval time per tool (cached) | 10-15 min | 1-3 min |
| Full pool drain | 3-4 hours | 30-60 min |
| Time to debug failure | 5+ min (tail multiple logs) | <30s (Loki search) |
| Iterations per day | 4-6 | 20-40 |
| Manual SSH+scp+restart cycle | 17 last session | 0 (n8n auto-loop) |
