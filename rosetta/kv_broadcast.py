"""rosetta/kv_broadcast.py — Layer 3 KV-cache broadcast: DESIGN STUB ONLY.

This module is intentionally not implemented. It defines the future Phase-3
boundary for true transformer KV-cache sharing between Determinex agents.

What "KV-cache broadcast" actually means (terminology lock):
  - Layer 1   = DSL control plane (text-format protocol messages)
  - Layer 2A  = Rosetta text-space approximation
  - Layer 2B  = direct soft-prefix injection via llama-cpp-python (embd batches)
  - Layer 2C  = latent memory / hidden-state RAG (compressed pooled states)
  - Layer 3   = THIS — literal transformer K/V cache tensor transfer between
                models at a fixed mid-layer boundary

Why this is a stub, not an implementation:
  - llama-cpp-python does not expose per-layer KV-cache pointers.
  - llama.cpp's KV cache is layout-dependent (head split, dtype, paged-attention
    blocking). Two models must share head_dim, num_kv_heads, dtype, and rope
    settings, OR be passed through a learned remapper.
  - A proper implementation requires a llama.cpp fork (or C extension) exposing:
        llama_kv_cache_view_get(ctx, layer, pos_lo, pos_hi) -> tensor
        llama_kv_cache_view_set(ctx, layer, pos_lo, snapshot) -> int
        llama_eval_with_token_callback(ctx, batch, on_token)
  - None of those exist in the upstream API today.

The paper claim must reflect this:
    Layer 3 (KV broadcast) is DESIGNED, not BUILT.

Anything that calls into KVBroadcastEngine receives NotImplementedError with a
plain explanation. There is no fallback path — silently downgrading to text
would lie about which layer ran.
"""

from __future__ import annotations

from collections.abc import Callable, Iterator
from dataclasses import dataclass
from typing import Any

from rosetta.model_registry import ModelSpec

_BACKEND_REQUIRED = (
    "Requires llama.cpp fork, C extension, or custom backend that exposes "
    "per-layer KV-cache view/set + token-streaming callback."
)


# ---------------------------------------------------------------------------
# Snapshots and callbacks (data classes only — no behavior)
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class KVSnapshot:
    """A captured slice of one model's KV cache.

    layer        : transformer block index the snapshot was drawn from
    position_lo  : inclusive starting position in the sequence
    position_hi  : exclusive ending position in the sequence
    k_blob       : opaque bytes — raw K tensor for the [layer, lo:hi) slice
    v_blob       : opaque bytes — raw V tensor for the same slice
    dtype        : "f16" | "f32" | "q8_0" — must match the receiving model
    head_dim     : per-head channel count — must match the receiving model
    num_kv_heads : grouped-query attention head count
    source_spec  : ModelSpec the snapshot was captured from
    """

    layer: int
    position_lo: int
    position_hi: int
    k_blob: bytes
    v_blob: bytes
    dtype: str
    head_dim: int
    num_kv_heads: int
    source_spec: ModelSpec


@dataclass(frozen=True)
class TokenCallback:
    """A callback the Builder will fire on every emitted token.

    The Monitor can yield an interrupt response (continue / stop / steer)
    based on the token stream — this is what makes Layer 3 fundamentally
    different from Layer 2 (Layer 2 fires once, Layer 3 fires per-token).
    """

    on_token: Callable[[int, str], str | None]
    # Return values from on_token:
    #   None       — continue normally
    #   "stop"     — terminate generation
    #   "steer:<text>" — inject a steering string at the next decode step


# ---------------------------------------------------------------------------
# Engine (every method explicitly raises NotImplementedError)
# ---------------------------------------------------------------------------


class KVBroadcastEngine:
    """Layer 3 KV-cache broadcast engine. DESIGN STUB ONLY.

    Anyone calling these methods gets NotImplementedError with a reason. The
    Phase-3 implementation will live in an experimental branch with a llama.cpp
    fork; this stub exists so dependent code can import the interface, type-
    check against it, and have a clean socket for the future engine to plug in.
    """

    def __init__(self, *args: Any, **kwargs: Any):
        self._ready = False  # never True — explicit, no silent activation

    @property
    def ready(self) -> bool:
        """Always False in the stub. True will only ever be set by the real engine."""
        return False

    def capture(
        self,
        *,
        model: Any,
        layer: int,
        position_lo: int,
        position_hi: int,
    ) -> KVSnapshot:
        """Capture a [layer, lo:hi) slice of model's KV cache. NOT IMPLEMENTED."""
        raise NotImplementedError(_BACKEND_REQUIRED)

    def inject(
        self,
        *,
        model: Any,
        snapshot: KVSnapshot,
    ) -> None:
        """Inject a KVSnapshot into model's KV cache at snapshot's position. NOT IMPLEMENTED."""
        raise NotImplementedError(_BACKEND_REQUIRED)

    def stream_with_monitor(
        self,
        *,
        builder: Any,
        monitor: Any,
        prompt: str,
        on_token: Callable[[int, str], str | None] | None = None,
    ) -> Iterator[str]:
        """Stream tokens from builder while monitor receives each one live.

        The yield is the builder's token; on_token fires synchronously per-token
        and may return a steering signal. NOT IMPLEMENTED.
        """
        raise NotImplementedError(_BACKEND_REQUIRED)

    def remap_for_target(
        self,
        snapshot: KVSnapshot,
        target_spec: ModelSpec,
    ) -> KVSnapshot:
        """If source and target differ in head_dim / num_kv_heads / dtype, project
        the snapshot through a learned KV-remapper into target's layout. NOT IMPLEMENTED."""
        raise NotImplementedError(_BACKEND_REQUIRED)


# ---------------------------------------------------------------------------
# Diagnostics
# ---------------------------------------------------------------------------


def status() -> dict:
    """Report the engine status for the healthcheck. Always 'NOT IMPLEMENTED BY DESIGN'.

    This is the contract the user specified: every layer reports one of
        ACTIVE / UNAVAILABLE WITH REASON / NOT IMPLEMENTED BY DESIGN
    Layer 3 always reports the third.
    """
    return {
        "layer": "Layer 3 (KV-cache broadcast)",
        "status": "NOT IMPLEMENTED BY DESIGN",
        "reason": _BACKEND_REQUIRED,
        "interface": ["KVSnapshot", "TokenCallback", "KVBroadcastEngine"],
        "methods": ["capture", "inject", "stream_with_monitor", "remap_for_target"],
    }


# ---------------------------------------------------------------------------
# CLI — confirms the stub is wired but not active
# ---------------------------------------------------------------------------


def _cli():
    import json

    print(json.dumps(status(), indent=2))
    # Demonstrate that calling actually raises (not just that we report a stub).
    print()
    print("Confirming each method raises NotImplementedError:")
    engine = KVBroadcastEngine()
    for method_name, callargs in [
        ("capture", dict(model=None, layer=0, position_lo=0, position_hi=1)),
        ("inject", dict(model=None, snapshot=None)),
        ("remap_for_target", dict(snapshot=None, target_spec=None)),
    ]:
        try:
            getattr(engine, method_name)(**callargs)
            print(f"  {method_name:24}  FAIL — should have raised")
        except NotImplementedError as e:
            print(f"  {method_name:24}  OK — NotImplementedError: {str(e)[:70]}...")
        except TypeError as e:
            # E.g. snapshot=None into inject which inspects fields
            print(f"  {method_name:24}  raised TypeError before NotImplementedError: {e}")

    # stream_with_monitor returns an iterator — exhausting it triggers the raise
    try:
        it = engine.stream_with_monitor(builder=None, monitor=None, prompt="x")
        next(iter(it))
        print(f"  {'stream_with_monitor':24}  FAIL — should have raised")
    except NotImplementedError as e:
        print(f"  {'stream_with_monitor':24}  OK — NotImplementedError: {str(e)[:70]}...")


if __name__ == "__main__":
    _cli()
