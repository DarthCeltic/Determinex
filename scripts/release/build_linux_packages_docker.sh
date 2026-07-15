#!/usr/bin/env bash
set -euo pipefail

export DEBIAN_FRONTEND=noninteractive
unset LD_LIBRARY_PATH
unset LIBRARY_PATH
unset CARGO_TARGET_DIR

apt-get update
apt-get install -y \
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
  wget \
  xz-utils

curl -fsSL https://deb.nodesource.com/setup_20.x -o /tmp/nodesource_setup.sh
bash /tmp/nodesource_setup.sh
apt-get install -y nodejs

curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs -o /tmp/rustup-init.sh
sh /tmp/rustup-init.sh -y --profile minimal --default-toolchain stable
export PATH="/root/.cargo/bin:$PATH"

export CARGO_TARGET_DIR=/tmp/determinex-linux-cargo-target
export npm_config_cache=/tmp/determinex-npm-cache
export TAURI_SIGNING_PRIVATE_KEY=""
export TAURI_SIGNING_PRIVATE_KEY_PASSWORD=""
SIDECAR_VENV=/tmp/determinex-sidecar-build-venv

mkdir -p "$CARGO_TARGET_DIR" "$npm_config_cache"

node --version
npm --version
rustc --version
cargo --version

python3 -m venv "$SIDECAR_VENV"
"$SIDECAR_VENV/bin/python" -m pip install --upgrade pip wheel
"$SIDECAR_VENV/bin/python" -m pip install \
  pyinstaller \
  litellm \
  rich \
  python-dotenv \
  tiktoken \
  numpy \
  psutil \
  pyyaml \
  anthropic \
  httpx \
  requests

"$SIDECAR_VENV/bin/python" bundler/build_hive_sidecar.py --triple x86_64-unknown-linux-gnu

cd /workspace/frontend
npm ci
npm run tauri -- build --bundles appimage,deb,rpm

cd /workspace
python3 scripts/release/package_download_bundle.py \
  --installer-dir "$CARGO_TARGET_DIR/release/bundle" \
  --output-dir release_build_work/determinex-linux-download-bundles \
  --evidence-dir assurance/evidence/determinex_download_bundle_linux_local
