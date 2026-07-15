# Dockerfile - Determinex orchestrator container (Sprint 6)
# =======================================================
# Builds a Python 3.11 image with the Hive orchestrator, validators,
# Cloak, and ask CLI. Inference is delegated to a co-located Ollama
# container via the determinex network (see docker-compose.yml).
#
# The image does NOT bake GGUF weights — they stay on the host volume
# (T:/determinex-models on Windows, ~/determinex-models on Linux), mounted
# into the Ollama service.
#
# Build:
#   docker build -t determinex:latest .
# Run via compose:
#   docker compose up

FROM python:3.11-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    DETERMINEX_OLLAMA_URL=http://ollama:11434 \
    DETERMINEX_MODELS_DIR=/models

# System deps:
#   - git: WAL clone / worktree ops in the hive
#   - build-essential: source builds for llama-cpp-python (CPU wheel preferred but fallback works)
#   - shellcheck: oracle pack semantic Bash check
#   - hadolint: oracle pack Dockerfile lint
#   - yamllint: oracle pack YAML lint
#   - curl: healthcheck against ollama
#   - rustc + cargo + go: compiler-oracle ground truth for the build loop
RUN apt-get update && apt-get install -y --no-install-recommends \
        git build-essential curl ca-certificates \
        shellcheck yamllint \
        rustc cargo golang-go \
    && rm -rf /var/lib/apt/lists/*

# hadolint is statically linked; pull a release directly (faster than apt's old build).
ARG HADOLINT_VERSION=2.12.0
RUN curl -fsSL -o /usr/local/bin/hadolint \
      "https://github.com/hadolint/hadolint/releases/download/v${HADOLINT_VERSION}/hadolint-Linux-x86_64" \
    && chmod +x /usr/local/bin/hadolint

WORKDIR /app

# Install Python deps first so source edits don't bust the wheel cache.
COPY scripts/requirements.txt /app/scripts/requirements.txt
RUN pip install -r /app/scripts/requirements.txt \
    && pip install \
        --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cpu \
        llama-cpp-python==0.3.23

# Copy the rest of the orchestration surface.
COPY scripts/   /app/scripts/
COPY rosetta/   /app/rosetta/
COPY specs/     /app/specs/
COPY data/      /app/data/
COPY .env.example /app/.env.example

# Default volumes (declared so docker-compose mounts are explicit)
VOLUME ["/models", "/workspace", "/sessions", "/logs"]

# Sane PYTHONPATH so `from hive import ...` and `from validators import ...` resolve
ENV PYTHONPATH=/app/scripts:/app

# Sanity-check at build time that the validator registry imports.
RUN python -c "import sys; sys.path.insert(0, '/app/scripts'); from validators import VALIDATOR_MAP; \
    print(f'Determinex image: {len(VALIDATOR_MAP)} validators registered')"

# Default entry: the diagnostic ask CLI. Override with `docker run determinex hive new-session ...`
ENTRYPOINT ["python", "/app/scripts/determinex_ask.py"]
CMD ["where"]
