# Safe Counter (single file)

## Goal
A thread-safe counter in a single Rust source file. Spawns N threads, each increments
the counter once using Arc<Mutex<u64>>, then prints the final count. Shows that
Determinex can produce compiler-verified, data-race-free concurrent code.

## Language
rust

## Constraints
- All code in src/main.rs — no separate modules
- Must use Arc<Mutex<u64>> for shared state
- Must use std::sync::Arc and std::sync::Mutex — no external crates
- Spawn N threads (default 5 from command line arg, parse with std::env::args)
- Each thread clones the Arc, locks the Mutex, increments the u64 by 1
- Join all thread handles before printing
- Print: "Final count: N"
- No unsafe blocks

## Files
- `src/main.rs` — everything here: Counter struct, main function, thread spawning

## Dependencies
- None (stdlib only)
