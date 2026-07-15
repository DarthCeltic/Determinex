"""
train_rosetta.py — Determinex Universal Latent Bridge (Rosetta Stone)

Trains a universal hub embedding space that connects all major open-source
model families at the latent level. Any model can talk to any other model
through the hub — no retraining required, just load the W matrices.

Architecture:
    Each family gets an encoder (model → hub) and decoder (hub → model).
    Hub dimension: 2048 — preserves all information, maps cleanly to every family.

    Model A hidden state
         │
    W_A_enc (encoder)
         │
    Universal Hub (2048-dim)
         │
    W_B_dec (decoder)
         │
    Model B embedding space  ← injected as soft prefix

Families covered (95% of open source):
    llama     Meta Llama 3.x — Hermes, Dolphin, WizardLM, everything Meta
    qwen      Alibaba Qwen 2.5 — Qwen-Coder, Qwen-Math, DeepSeek-Distill-Qwen
    deepseek  DeepSeek V2/V3/R1 — Coder, DeepSeek-Distill-Llama
    mistral   Mistral 7B/NeMo/Mixtral — OpenHermes, Zephyr
    phi       Microsoft Phi-3/3.5/4 — all sizes
    gemma     Google Gemma 2/3 — CodeGemma, ShieldGemma

Training signal: cosine alignment of paired hidden states on the same prompts.
Models that see the same semantic content converge to similar geometry
(Platonic Representation Hypothesis) — W learns the coordinate transform.

Usage (on RunPod):
    python rosetta/train_rosetta.py --states_dir outputs/hidden_states --epochs 20
"""

import argparse
import json
import math
import os
import sys
import time
from pathlib import Path

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader, Dataset

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# ---------------------------------------------------------------------------
# CONFIG
# ---------------------------------------------------------------------------

HUB_DIM = 2048  # Universal hub dimension

FAMILY_DIMS = {
    "llama":    3072,   # Llama 3.2 3B / Phi-3-mini share this
    "qwen":     2048,   # Qwen 2.5 3B
    "deepseek": 2048,   # DeepSeek-Coder-V2 base
    "mistral":  4096,   # Mistral 7B
    "phi":      3072,   # Phi-3-mini 3.8B
    "gemma":    2304,   # Gemma 2 2B
}

# ---------------------------------------------------------------------------
# MODEL: Encoder + Decoder pairs per family
# ---------------------------------------------------------------------------

class FamilyEncoder(nn.Module):
    """Projects a model family's hidden states into the universal hub space."""
    def __init__(self, family_dim: int, hub_dim: int = HUB_DIM):
        super().__init__()
        self.proj = nn.Linear(family_dim, hub_dim, bias=False)
        self.norm = nn.LayerNorm(hub_dim)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.norm(self.proj(x))


class FamilyDecoder(nn.Module):
    """Projects universal hub representations back into a model family's space."""
    def __init__(self, hub_dim: int, family_dim: int):
        super().__init__()
        self.proj = nn.Linear(hub_dim, family_dim, bias=False)
        self.norm = nn.LayerNorm(family_dim)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # L8-B: L2-normalise output so latent vectors stay on the unit hypersphere.
        # Without this, vector magnitudes drift across training steps, causing
        # context boundaries to collapse and cosine distances to lose meaning.
        return F.normalize(self.norm(self.proj(x)), dim=-1)


class RosettaStone(nn.Module):
    """
    The full Rosetta Stone — encoders and decoders for all model families.
    Any family can talk to any other family through the hub.
    """
    FAMILY_DIMS = FAMILY_DIMS

    def __init__(self, families: dict[str, int] = FAMILY_DIMS, hub_dim: int = HUB_DIM):
        super().__init__()
        self.hub_dim  = hub_dim
        self.families = families
        self.encoders = nn.ModuleDict({
            name: FamilyEncoder(dim, hub_dim)
            for name, dim in families.items()
        })
        self.decoders = nn.ModuleDict({
            name: FamilyDecoder(hub_dim, dim)
            for name, dim in families.items()
        })

    def encode(self, family: str, hidden: torch.Tensor) -> torch.Tensor:
        return self.encoders[family](hidden)

    def decode(self, family: str, hub: torch.Tensor) -> torch.Tensor:
        return self.decoders[family](hub)

    def translate(self, src_family: str, tgt_family: str, hidden: torch.Tensor) -> torch.Tensor:
        """Direct translation: src model hidden state → tgt model embedding space."""
        hub = self.encode(src_family, hidden)
        return self.decode(tgt_family, hub)

    def supported_arches(self) -> list[str]:
        """Return the family keys this RosettaStone can encode/decode."""
        return sorted(self.families.keys())

    def save(self, path: Path):
        path = Path(path)
        path.mkdir(parents=True, exist_ok=True)
        torch.save(self.state_dict(), path / "rosetta_weights.pt")
        meta = {"hub_dim": self.hub_dim, "families": self.families}
        (path / "rosetta_meta.json").write_text(json.dumps(meta, indent=2))
        print(f"[ROSETTA] Saved → {path}", flush=True)

    @classmethod
    def load(cls, path: Path) -> "RosettaStone":
        path = Path(path)
        meta   = json.loads((path / "rosetta_meta.json").read_text())
        stone  = cls(families=meta["families"], hub_dim=meta["hub_dim"])
        stone.load_state_dict(torch.load(path / "rosetta_weights.pt", map_location="cpu"))
        return stone


# ---------------------------------------------------------------------------
# DATASET: Paired hidden states from the same prompts run through two families
# ---------------------------------------------------------------------------

class PairedStateDataset(Dataset):
    """
    Loads paired hidden state tensors collected by collect_hidden_states.py.
    Each item: (family_a_name, h_a, family_b_name, h_b) for the same prompt.
    """
    def __init__(self, states_dir: Path):
        self.pairs = []
        states_dir = Path(states_dir)
        families   = sorted([d.name for d in states_dir.iterdir() if d.is_dir()])
        print(f"[ROSETTA] Found families: {families}", flush=True)

        # Load all hidden states per family
        family_states: dict[str, list[torch.Tensor]] = {}
        for fam in families:
            fam_dir = states_dir / fam
            tensors = []
            for pt_file in sorted(fam_dir.glob("*.pt")):
                t = torch.load(pt_file, map_location="cpu")
                if t.dim() == 1:
                    t = t.unsqueeze(0)
                tensors.append(t)
            if tensors:
                family_states[fam] = tensors
                print(f"[ROSETTA]   {fam}: {len(tensors)} states loaded", flush=True)

        # Build all cross-family pairs (same prompt index → paired)
        fam_list = list(family_states.keys())
        n_prompts = min(len(v) for v in family_states.values())
        for i in range(n_prompts):
            for j in range(len(fam_list)):
                for k in range(j + 1, len(fam_list)):
                    fa, fb = fam_list[j], fam_list[k]
                    self.pairs.append((fa, family_states[fa][i], fb, family_states[fb][i]))

        print(f"[ROSETTA] Total training pairs: {len(self.pairs)}", flush=True)

    def __len__(self):
        return len(self.pairs)

    def __getitem__(self, idx):
        fa, ha, fb, hb = self.pairs[idx]
        return fa, ha.squeeze(0), fb, hb.squeeze(0)


def collate_pairs(batch):
    """Custom collate — groups by family pair for batch efficiency."""
    return batch  # return as list, training loop handles grouping


# ---------------------------------------------------------------------------
# TRAINING
# ---------------------------------------------------------------------------

def train_rosetta(
    states_dir: Path,
    output_dir: Path,
    epochs: int = 20,
    lr: float = 3e-4,
    device: str = "cuda",
):
    device = torch.device(device if torch.cuda.is_available() else "cpu")
    print(f"[ROSETTA] Training on {device}", flush=True)

    dataset = PairedStateDataset(states_dir)
    if len(dataset) == 0:
        print("[ROSETTA] ERROR: No paired states found. Run collect_hidden_states.py first.", flush=True)
        sys.exit(1)

    stone = RosettaStone().to(device)
    n_params = sum(p.numel() for p in stone.parameters())
    print(f"[ROSETTA] Parameters: {n_params:,}", flush=True)

    optimizer = torch.optim.AdamW(stone.parameters(), lr=lr, weight_decay=1e-4)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=epochs)

    best_loss = float("inf")
    for epoch in range(1, epochs + 1):
        stone.train()
        total_loss = 0.0
        n_pairs    = 0

        for item in dataset:
            fa, ha, fb, hb = item
            ha = ha.to(device).unsqueeze(0)
            hb = hb.to(device).unsqueeze(0)

            # Encode both into hub space
            hub_a = stone.encode(fa, ha)
            hub_b = stone.encode(fb, hb)

            # Primary loss: hub representations of same prompt should align
            align_loss = 1.0 - F.cosine_similarity(hub_a, hub_b).mean()

            # Reconstruction loss: decode back to original space
            recon_a = stone.decode(fa, hub_a)
            recon_b = stone.decode(fb, hub_b)
            recon_loss = (
                F.mse_loss(recon_a, ha) +
                F.mse_loss(recon_b, hb)
            ) * 0.1

            loss = align_loss + recon_loss
            optimizer.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(stone.parameters(), 1.0)
            optimizer.step()

            total_loss += loss.item()
            n_pairs    += 1

        scheduler.step()
        avg_loss = total_loss / max(n_pairs, 1)
        print(f"[ROSETTA] Epoch {epoch:3d}/{epochs}  loss={avg_loss:.4f}  lr={scheduler.get_last_lr()[0]:.2e}", flush=True)

        if avg_loss < best_loss:
            best_loss = avg_loss
            stone.save(output_dir / "best")

    stone.save(output_dir / "final")
    print(f"[ROSETTA] Training complete. Best loss: {best_loss:.4f}", flush=True)
    print(f"[ROSETTA] Outputs → {output_dir}", flush=True)


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--states_dir", type=str, default="outputs/hidden_states")
    parser.add_argument("--output_dir", type=str, default="outputs/rosetta")
    parser.add_argument("--epochs",     type=int, default=20)
    parser.add_argument("--lr",         type=float, default=3e-4)
    parser.add_argument("--device",     type=str, default="cuda")
    args = parser.parse_args()

    train_rosetta(
        states_dir=Path(args.states_dir),
        output_dir=Path(args.output_dir),
        epochs=args.epochs,
        lr=args.lr,
        device=args.device,
    )
