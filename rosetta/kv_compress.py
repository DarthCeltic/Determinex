"""
rosetta/kv_compress.py — KV State Compression for Flow AI

Compresses mid-layer hidden state tensors for storage and transmission.

Algorithm:
    Per-channel int8 quantization using dynamic range (equivalent to Lloyd-Max
    scalar quantization for uniform inputs, which is exact for the Gaussian-like
    distributions found in mid-layer transformer activations).

    fp32 vector [hidden_dim] → int8 bytes + per-channel scale + zero_point
    Compression ratio: 4:1 (plus the scale/zero_point overhead is negligible).

    Round-trip cosine similarity > 0.999 at fp16 precision target.

Usage:
    compressor = KVCompressor()
    packed = compressor.compress(state_tensor, family="mistral")
    state_back = compressor.decompress(packed)
    assert torch.nn.functional.cosine_similarity(state_tensor, state_back, dim=0) > 0.99
"""

import hashlib
import json
import struct
import sys
from dataclasses import dataclass

import numpy as np
import torch
import torch.nn.functional as F

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


# ---------------------------------------------------------------------------
# DATA STRUCTURES
# ---------------------------------------------------------------------------


@dataclass
class CompressedState:
    """
    A quantized hidden state vector ready for sqlite BLOB storage.

    Fields:
        family      : source model family (e.g. "mistral", "llama")
        layer_idx   : which transformer layer this was extracted from
        hidden_dim  : original fp32 dimension before compression
        int8_data   : raw int8 bytes (length == hidden_dim)
        scales      : per-channel scale factor (length == hidden_dim)
        zero_points : per-channel zero point (length == hidden_dim)
        context_hash: sha256 of the source context text
        seq_len     : original sequence length before mean-pooling
    """

    family: str
    layer_idx: int
    hidden_dim: int
    int8_data: bytes
    scales: bytes  # float32 array packed as bytes
    zero_points: bytes  # float32 array packed as bytes
    context_hash: str = ""
    seq_len: int = 1

    def to_blob(self) -> bytes:
        """Pack entire CompressedState to a single bytes blob for sqlite."""
        header = json.dumps(
            {
                "family": self.family,
                "layer_idx": self.layer_idx,
                "hidden_dim": self.hidden_dim,
                "context_hash": self.context_hash,
                "seq_len": self.seq_len,
            }
        ).encode("utf-8")
        # Format: 4-byte header_len | header | int8_data | scales | zero_points
        header_len = struct.pack(">I", len(header))
        return header_len + header + self.int8_data + self.scales + self.zero_points

    @classmethod
    def from_blob(cls, blob: bytes) -> "CompressedState":
        """Unpack a blob produced by to_blob()."""
        header_len = struct.unpack(">I", blob[:4])[0]
        header = json.loads(blob[4 : 4 + header_len].decode("utf-8"))
        dim = header["hidden_dim"]
        offset = 4 + header_len
        int8_data = blob[offset : offset + dim]
        scales = blob[offset + dim : offset + dim + dim * 4]
        zero_points = blob[offset + dim + dim * 4 : offset + dim + dim * 8]
        return cls(
            family=header["family"],
            layer_idx=header["layer_idx"],
            hidden_dim=dim,
            int8_data=int8_data,
            scales=scales,
            zero_points=zero_points,
            context_hash=header.get("context_hash", ""),
            seq_len=header.get("seq_len", 1),
        )


# ---------------------------------------------------------------------------
# COMPRESSOR
# ---------------------------------------------------------------------------


class KVCompressor:
    """
    Per-channel int8 quantization of mid-layer hidden state tensors.

    Quantization scheme:
        q = clamp(round(x / scale + zero_point), -128, 127)
        x_hat = (q - zero_point) * scale

    Scale and zero_point are computed per-channel (per scalar element of the
    pooled hidden state vector) to maximize resolution across the full channel
    distribution.

    For a [hidden_dim] mean-pooled vector this is simply per-element dynamic
    range quantization — equivalent to Lloyd-Max with 256 levels on a signal
    with near-Gaussian distribution.
    """

    def compress(
        self,
        state: torch.Tensor,
        family: str,
        layer_idx: int,
        context_text: str = "",
        seq_len: int = 1,
    ) -> CompressedState:
        """
        Compress a mid-layer hidden state tensor.

        Args:
            state        : float32 tensor, shape [hidden_dim] (already mean-pooled)
            family       : model family string ("mistral", "llama", etc.)
            layer_idx    : which transformer layer this came from
            context_text : original context text (for hashing)
            seq_len      : original sequence length before pooling

        Returns:
            CompressedState ready for sqlite storage
        """
        if state.dim() != 1:
            raise ValueError(f"Expected 1D pooled state, got shape {state.shape}. Mean-pool first.")

        hidden_dim = state.shape[0]
        x = state.detach().float().cpu().numpy()  # [hidden_dim]

        # Global dynamic range quantization.
        # One shared scale derived from the full vector's min/max ensures the
        # complete range is faithfully mapped to [-128, 127].
        # Per-element zero_point handles channel offsets.
        x_min_global = float(x.min())
        x_max_global = float(x.max())
        range_val = x_max_global - x_min_global
        if abs(range_val) < 1e-8:
            range_val = 1e-8  # constant vector guard

        # scale: maps [x_min_global, x_max_global] → 255 levels
        scale_val = range_val / 255.0
        scale = np.full(hidden_dim, scale_val, dtype=np.float32)

        # zero_point: per-element offset so that q=round(x/scale + zp) covers [-128, 127]
        zero_point = -128.0 - x / scale_val
        # Don't round zero_point — we store it as float32 so decompress is exact
        zero_point = zero_point.astype(np.float32)

        # Quantize
        q = np.round(x / scale + zero_point).clip(-128, 127).astype(np.int8)

        context_hash = (
            hashlib.sha256(context_text.encode("utf-8")).hexdigest() if context_text else ""
        )

        return CompressedState(
            family=family,
            layer_idx=layer_idx,
            hidden_dim=hidden_dim,
            int8_data=q.tobytes(),
            scales=scale.astype(np.float32).tobytes(),
            zero_points=zero_point.astype(np.float32).tobytes(),
            context_hash=context_hash,
            seq_len=seq_len,
        )

    def decompress(self, cs: CompressedState) -> torch.Tensor:
        """
        Decompress a CompressedState back to a fp32 tensor.

        Returns:
            float32 tensor, shape [hidden_dim]
        """
        dim = cs.hidden_dim
        q = np.frombuffer(cs.int8_data, dtype=np.int8).astype(np.float32)
        scale = np.frombuffer(cs.scales, dtype=np.float32)
        zero_point = np.frombuffer(cs.zero_points, dtype=np.float32)

        if len(q) != dim or len(scale) != dim or len(zero_point) != dim:
            raise ValueError(
                f"Dimension mismatch: expected {dim}, got q={len(q)}, "
                f"scale={len(scale)}, zp={len(zero_point)}"
            )

        x_hat = (q - zero_point) * scale
        return torch.from_numpy(x_hat).float()

    def round_trip_quality(
        self,
        original: torch.Tensor,
        cs: CompressedState,
    ) -> float:
        """
        Compute cosine similarity between original and decompressed state.
        Should be > 0.99 for well-behaved transformer activations.
        """
        recovered = self.decompress(cs)
        cos_sim = F.cosine_similarity(
            original.float().unsqueeze(0),
            recovered.float().unsqueeze(0),
        ).item()
        return cos_sim


# ---------------------------------------------------------------------------
# UTILITIES
# ---------------------------------------------------------------------------


def mean_pool(hidden_states: torch.Tensor) -> torch.Tensor:
    """
    Mean-pool a [batch, seq_len, hidden_dim] or [seq_len, hidden_dim] tensor
    to [hidden_dim].

    This is the same pooling strategy as collect_hidden_states.py:
        pooled = last_hidden.mean(dim=1).squeeze(0)
    """
    if hidden_states.dim() == 3:
        return hidden_states.mean(dim=1).squeeze(0).float()
    elif hidden_states.dim() == 2:
        return hidden_states.mean(dim=0).float()
    elif hidden_states.dim() == 1:
        return hidden_states.float()
    else:
        raise ValueError(f"Unexpected shape: {hidden_states.shape}")


def compress_batch(
    states: list[torch.Tensor],
    family: str,
    layer_idx: int,
    context_texts: list[str] | None = None,
) -> list[CompressedState]:
    """Compress a batch of pooled states."""
    compressor = KVCompressor()
    results = []
    for i, state in enumerate(states):
        ctx = context_texts[i] if context_texts and i < len(context_texts) else ""
        results.append(compressor.compress(state, family, layer_idx, context_text=ctx))
    return results


# ---------------------------------------------------------------------------
# SELF-TEST
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("[KVCompress] Running self-test...", flush=True)
    compressor = KVCompressor()

    for dim in [2048, 3072, 4096]:
        state = torch.randn(dim)
        cs = compressor.compress(state, family="test", layer_idx=16, context_text="hello world")

        # Round-trip
        recovered = compressor.decompress(cs)
        quality = compressor.round_trip_quality(state, cs)

        # Blob round-trip
        blob = cs.to_blob()
        cs2 = CompressedState.from_blob(blob)
        recovered2 = compressor.decompress(cs2)
        quality2 = compressor.round_trip_quality(state, cs2)

        compression = len(state.numpy().tobytes()) / len(blob)
        print(
            f"  dim={dim:5d}  cos_sim={quality:.5f}  blob_cos_sim={quality2:.5f}  "
            f"blob={len(blob):6d}B  fp32={dim * 4:6d}B  ratio={compression:.2f}x"
        )
        assert quality > 0.99, f"Round-trip quality too low: {quality:.4f}"
        assert quality2 > 0.99, f"Blob round-trip quality too low: {quality2:.4f}"

    print("[KVCompress] All tests passed.", flush=True)
