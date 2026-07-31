# Toolchain image for the Linux release build.
#
# WHY THIS EXISTS
# scripts/release/build_linux_packages_docker.sh installs its whole toolchain on every run:
# apt packages, Node 20 from nodesource, rustup, and a PyInstaller venv. Measured
# 2026-07-29 on this machine that is ~24 minutes before a single line of project code
# compiles -- and because the first three attempts each failed AFTER that point (npm ci
# lockfile, CRLF shebang, missing `python`), every fix cost a fresh 24-minute wait to
# discover the next one.
#
# Baking the toolchain makes a retry start at `npm ci`. The script stays runnable on a bare
# ubuntu:24.04 too: its install steps are guarded, so they no-op when the tool is present.
#
# Build once:
#   docker build -t determinex-linux-build:24.04 -f docker/release/linux-build.Dockerfile .
# Then:
#   docker run --rm -v "C:/path/to/export:/workspace" -w /workspace \
#     determinex-linux-build:24.04 bash scripts/release/build_linux_packages_docker.sh
FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

# Tauri v2's Linux prerequisites plus the packaging tools. `python-is-python3` is the one
# that is easy to miss and fatal: frontend/package.json's `pretauri` hook shells out to
# `python`, and Ubuntu ships only `python3`, so the build died at
# `sh: 1: python: not found` after everything else had succeeded.
RUN apt-get update && apt-get install -y --no-install-recommends \
      build-essential \
      ca-certificates \
      curl \
      file \
      libayatana-appindicator3-dev \
      librsvg2-dev \
      libssl-dev \
      libwebkit2gtk-4.1-dev \
      libxdo-dev \
      patchelf \
      pkg-config \
      python3 \
      python3-pip \
      python3-venv \
      python-is-python3 \
      wget \
      xz-utils \
      desktop-file-utils \
      fakeroot \
      rpm \
    && rm -rf /var/lib/apt/lists/*

# Node 20, matching the version the release workflow pins.
RUN curl -fsSL https://deb.nodesource.com/setup_20.x -o /tmp/nodesource_setup.sh \
    && bash /tmp/nodesource_setup.sh \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/* /tmp/nodesource_setup.sh

# Rust, minimal profile -- the build only needs cargo/rustc.
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs -o /tmp/rustup-init.sh \
    && sh /tmp/rustup-init.sh -y --profile minimal --default-toolchain stable \
    && rm /tmp/rustup-init.sh
ENV PATH="/root/.cargo/bin:${PATH}"

# The sidecar build venv, pre-populated. Lives outside /workspace so a mounted export does
# not shadow it and so it survives between runs.
ENV SIDECAR_VENV=/opt/determinex-sidecar-venv
RUN python3 -m venv "$SIDECAR_VENV" \
    && "$SIDECAR_VENV/bin/python" -m pip install --no-cache-dir --upgrade pip wheel \
    && "$SIDECAR_VENV/bin/python" -m pip install --no-cache-dir \
         pyinstaller litellm rich python-dotenv tiktoken numpy psutil pyyaml \
         anthropic httpx requests

# Keep cargo and npm scratch OFF the bind mount: small-file I/O through Docker Desktop's
# Windows filesystem translation is what makes an otherwise-quick install crawl.
ENV CARGO_TARGET_DIR=/tmp/determinex-linux-cargo-target \
    npm_config_cache=/tmp/determinex-npm-cache \
    DETERMINEX_LINUX_TOOLCHAIN_PREBAKED=1

# PyInstaller links against the Python SHARED library, which is a *recommended* dependency
# of python3 -- so `--no-install-recommends` above silently dropped it and the sidecar build
# died with:
#
#   ERROR: Python shared library ('libpython3.12.so.1.0') was not found!
#
# The earlier bare-ubuntu run worked only because it installed recommends by default. Added
# as a trailing layer rather than folded into the apt block above purely to preserve the
# build cache for the Node/Rust/venv layers, which cost ~8 minutes to redo.
RUN apt-get update && apt-get install -y --no-install-recommends libpython3.12 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace
