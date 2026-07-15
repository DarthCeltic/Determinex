# Hello Counter

## Goal
A simple Python module that implements a thread-safe counter with increment, decrement, and reset operations. Exposes a CLI that prints the counter value after a configurable number of increments.

## Language
python

## Constraints
- Must be thread-safe (use threading.Lock)
- increment() and decrement() return the new value
- reset() returns 0
- CLI accepts --count N (default 5) and prints final value

## Files
- `counter.py` — Counter class with increment, decrement, reset
- `main.py` — CLI entry point using argparse

## Dependencies
- None (stdlib only)
