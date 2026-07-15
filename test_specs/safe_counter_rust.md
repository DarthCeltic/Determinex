# Safe Counter

## Goal
A thread-safe counter in Rust. Exposes a CLI that spawns N threads, each incrementing
the counter once, then prints the final count. Demonstrates Arc<Mutex<T>> RAII locking.

## Language
rust

## Constraints
- Must use Arc<Mutex<u64>> for shared state
- Each thread increments exactly once
- CLI accepts --count N (default 5), spawns N threads
- All threads must join before printing
- No unsafe blocks

## Files
- `src/counter.rs` — Counter struct wrapping Arc<Mutex<u64>> with new() and increment()
- `src/main.rs` — CLI entry point using clap or std::env::args, spawns threads, prints result

## Dependencies
- None beyond std (use std::sync, std::thread, std::env::args)
