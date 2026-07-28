"""shared_prompts.py -- the fixed prompt set every hidden-state collector runs, regardless of
which backend loads the model (HF transformers or a local GGUF via llama-cpp-python).

Extracted out of collect_hidden_states.py so a GGUF-based collector (collect_hidden_states_gguf.py)
can import the SAME prompts without pulling in torch/transformers/bitsandbytes -- this module has
zero dependencies, on purpose, so importing it never forces a heavy or CUDA-specific package to
load for a code path that doesn't need it.

Same prompt -> different model -> different coordinate system -> same meaning.
W learns the coordinate transform.
"""
from __future__ import annotations

SHARED_PROMPTS: list[str] = [
    # Rust
    "Write a Rust function that counts occurrences of a character in a string.",
    "Write a Rust function using Arc<Mutex<i32>> to sum a vector across threads.",
    "Write a Rust function using RefCell<Vec<i32>> to append items.",
    "Write idiomatic Rust to find the first even number in a slice.",
    "Write a Rust struct with impl block for a simple stack data structure.",
    # Go
    "Write a Go function that wraps an error using fmt.Errorf with %w.",
    "Write a Go function using defer and recover to catch panics safely.",
    "Write a Go function that reads from a channel with a timeout using select.",
    "Write idiomatic Go error handling for a file read operation.",
    "Write a Go function that uses goroutines to process items concurrently.",
    # Python
    "Write a Python function that divides two numbers, returning None on zero divisor.",
    "Write a Python function with type annotations that filters even numbers.",
    "Write a Python context manager for timing code execution.",
    "Write a Python dataclass for representing a 2D point with distance method.",
    "Write a Python async function that fetches URLs concurrently.",
    # TypeScript
    "Write a TypeScript function with a discriminated union for shape area calculation.",
    "Write a TypeScript async function that retries a failed operation with backoff.",
    "Write a TypeScript generic function that safely gets a nested object property.",
    "Write TypeScript with proper error handling using Result-style types.",
    "Write a TypeScript class implementing an observable event emitter.",
    # General reasoning
    "Explain the difference between stack and heap memory allocation.",
    "What is the purpose of a mutex in concurrent programming?",
    "Explain how LoRA fine-tuning modifies a language model.",
    "What is the Platonic Representation Hypothesis in machine learning?",
    "Explain the difference between synchronous and asynchronous programming.",
    # Architecture
    "Design a simple message queue system with producer and consumer.",
    "Explain the actor model for concurrent computation.",
    "What are the tradeoffs between microservices and monolithic architecture?",
    "Design a rate limiter for an API endpoint.",
    "Explain how vector databases enable semantic search.",
]
