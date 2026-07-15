# Smoke — Line Counter

## Goal
A pure Rust function that takes a string slice and returns the number of newline-separated
lines it contains. This is the canonical post-Sprint-0 sanity check for the Hive Mind pipeline:
Architect plans → Engineer builds → Compiler Oracle (rustc) validates.

## Language
rust

## Constraints
- No unsafe blocks
- No external crates beyond the standard library
- Function signature: `pub fn count_lines(text: &str) -> usize`
- Empty input must return 0
- Trailing newline must not produce an extra empty line in the count
- Must compile with `cargo check` under stable Rust

## Files
- src/lib.rs — implements `count_lines` plus at least one `#[test]` that exercises:
  - Empty string returns 0
  - Single line without trailing newline returns 1
  - Multi-line input with and without trailing newline both return correct count

## Acceptance
- `cargo check` clean (zero warnings, zero errors)
- `cargo test` all tests pass
