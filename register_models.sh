#!/usr/bin/env bash
# register_models.sh — Linux/macOS helper to register Determinex DSL models in Ollama
# Usage: bash register_models.sh
# Requires: Ollama running, DETERMINEX_MODELS_DIR set in .env or environment

set -euo pipefail

# Load DETERMINEX_MODELS_DIR from .env if not already in environment
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [[ -z "${DETERMINEX_MODELS_DIR:-}" && -f "$SCRIPT_DIR/.env" ]]; then
    DETERMINEX_MODELS_DIR="$(grep -m1 '^DETERMINEX_MODELS_DIR=' "$SCRIPT_DIR/.env" | cut -d= -f2- | tr -d '"' | tr -d "'")"
fi

if [[ -z "${DETERMINEX_MODELS_DIR:-}" ]]; then
    echo "[ERROR] DETERMINEX_MODELS_DIR is not set."
    echo "  Set it in .env: DETERMINEX_MODELS_DIR=/path/to/determinex-models"
    echo "  Or export it:  export DETERMINEX_MODELS_DIR=/mnt/data/determinex-models"
    exit 1
fi

echo "[DETERMINEX] Using DETERMINEX_MODELS_DIR = $DETERMINEX_MODELS_DIR"

register_model() {
    local tag="$1"
    local gguf_path="$2"
    local num_ctx="$3"
    local role="$4"

    echo ""
    echo "[DETERMINEX] Checking: $tag — $role"

    if ollama list 2>/dev/null | grep -q "$tag"; then
        echo "  Already registered — skipping."
        return
    fi

    if [[ ! -f "$gguf_path" ]]; then
        echo "  WARNING: GGUF not found at: $gguf_path"
        echo "  Run the RunPod training pipeline first, then re-run this script."
        return
    fi

    local tmp_file
    tmp_file="$(mktemp /tmp/determinex_modelfile_XXXXXX.txt)"
    printf 'FROM %s\nPARAMETER num_ctx %s\nPARAMETER temperature 0\n' "$gguf_path" "$num_ctx" > "$tmp_file"

    echo "  Registering from $gguf_path ..."
    if ollama create "$tag" -f "$tmp_file"; then
        echo "  Registered: $tag"
    else
        echo "  WARNING: Registration failed for $tag"
    fi
    rm -f "$tmp_file"
}

register_model \
    "determinex-engineer-v11-dsl" \
    "$DETERMINEX_MODELS_DIR/versions/engineer/v11-dsl/determinex-engineer-v11-dsl.gguf" \
    "4096" \
    "Builder (Qwen2.5-Coder-1.5B, DSL v11)"

register_model \
    "determinex-observer-v6-dsl" \
    "$DETERMINEX_MODELS_DIR/versions/observer/v6-dsl/determinex-observer-v6-dsl.gguf" \
    "4096" \
    "Monitor (Qwen2.5-3B, DSL v6) — oracle/architect use sentinel"

register_model \
    "determinex-sentinel-v5-dsl" \
    "$DETERMINEX_MODELS_DIR/versions/sentinel/v5-dsl/determinex-sentinel-v5-dsl.gguf" \
    "4096" \
    "Architect / Oracle (Mistral-7B, DSL v5)"

echo ""
echo "[DETERMINEX] Model registration complete."
echo "Verify with: ollama list"
