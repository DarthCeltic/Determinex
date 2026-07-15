# Determinex — Frontend

React/Next.js shell for the Determinex AI development assistant.

## Overview

This is the UI layer of Determinex. It runs inside a Tauri window and communicates
with the Rust orchestration core exclusively via Tauri IPC commands — no HTTP,
no localhost, no network.

## Stack

- Next.js (static export, `output: 'export'`)
- TypeScript strict
- Tauri IPC for all backend communication

## Dev

Run from the project root — do not run the frontend in isolation:

```bash
cargo tauri dev
```

This starts both the Rust backend and the Next.js frontend together.

## IPC Commands

All backend calls go through `invoke()`:

```ts
import { invoke } from '@tauri-apps/api/core'

// Examples
await invoke('orchestrate_plan', { prompt })
await invoke('get_models_registry')
await invoke('toggle_vanguard', { enabled })
```

See the Rust `src-tauri/src/` for the full command surface.
