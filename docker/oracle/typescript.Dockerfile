# Compiler Oracle image: TypeScript
#
# WHY THIS IMAGE EXISTS AT ALL
# `validate_project` could only verify rust/go/python, because _ORACLE_IMAGES had three
# entries. Every other language hit a lenient pass until 2026-07-28, and now fails
# closed -- honest, but not capable. CLAUDE.md has listed `tsc` as part of the oracle the
# whole time; this is what makes that true.
#
# WHY typescript IS BAKED IN RATHER THAN npx'd
# The oracle runs its container with --network=none (the security carve-out: model-
# generated code gets no network). `npx tsc` would try to fetch the compiler at RUN time
# and fail, and that failure is indistinguishable from a type error. Installing at BUILD
# time -- when network is legitimate and no model output is present -- is the only way to
# get a real type check inside the sandbox.
#
# Build:  docker build -t determinex-oracle-ts:20 -f docker/oracle/typescript.Dockerfile .
FROM node:20-alpine

# Pinned: an oracle whose compiler version drifts is an oracle whose verdicts drift.
RUN npm install -g typescript@5.6.3 && tsc --version

# No default tsconfig is baked in on purpose. The first version of this image shipped one
# at / and the oracle ran `tsc --project /determinex-tsconfig.json`, which passed its tests
# while being wrong: tsconfig `include` globs resolve relative to the config file, so tsc
# walked the whole container root and reached the mounted sources through /proc/1/cwd --
# reporting real type errors under unusable paths like `../proc/1/cwd/bad.ts`.
#
# Sources that ship no tsconfig are checked with an explicit file list and flags passed on
# the command line instead (_TS_DEFAULT_CHECK in scripts/hive/compiler.py), so the flags
# live in exactly one place and paths stay relative to the workspace.
WORKDIR /workspace
