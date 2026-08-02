"""Per-rig K calibration: the objective must reproduce known hardware, and never guess.

K is the correctness knob (`P = 1 - (1 - p)^K`), so a wrong K is not a slow run -- it is a
run that accrues correctness at the wrong rate, or one that falls off a throughput cliff the
hardware already knew about. These tests pin three things:

  1. the objective picks the knee that was found BY HAND on real AMD Radeon data
  2. it detects the collapse, and does not mistake "still climbing" for a collapse
  3. an uncalibrated rig gets a conservative K *and says so*, never a silent guess
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

_SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from determinex_calibrate import (  # noqa: E402
    UNCALIBRATED_K,
    Calibration,
    KPoint,
    host_fingerprint,
    optimal_k,
    pick_optimal,
    sweep,
)

# Captured verbatim from amd_gpu_evidence/k_sweep_and_prefix_cache.json -- a real sweep on
# AMD Radeon Cloud, ROCm 7.2.1, vLLM 0.16.1, Qwen2.5-Coder-7B-Instruct.
RADEON = [(1, 8.922, 28.7), (8, 9.297, 220.3), (16, 9.906, 413.5), (24, 10.375, 592.2),
          (32, 10.75, 739.9), (48, 13.625, 849.7), (64, 29.594, 512.6)]

# Measured on a consumer box, Ollama + Qwen2.5-Coder-1.5B, warm, 2026-08-02.
CONSUMER = [(1, 2.725, 17.6), (2, 3.083, 27.6), (4, 3.978, 45.5),
            (6, 5.033, 55.0), (8, 5.706, 61.5), (12, 7.359, 69.4)]


def _points(rows):
    return [KPoint(k, w, int(t * w), t, round(k / w, 3)) for k, w, t in rows]


def test_objective_reproduces_the_radeon_knee_found_by_hand():
    """The whole design rests on this: candidates/second must find the same knee a human
    found by staring at the sweep. If it does not, the metric is wrong."""
    best, collapsed = pick_optimal(_points(RADEON))
    assert best == 48, f"expected the hand-found knee K=48, got {best}"
    assert collapsed == 64, f"expected the measured collapse at K=64, got {collapsed}"


def test_collapse_is_detected_not_inferred():
    """K=64 collapsed because it exceeded the server's declared 61.83x concurrency. The
    detector must find it from the numbers, without being told the declared limit."""
    pts = _points(RADEON)
    _, collapsed = pick_optimal(pts)
    at = next(p for p in pts if p.k == collapsed)
    peak = max(p.cand_per_s for p in pts)
    assert at.cand_per_s < peak, "a 'collapse' must be slower than the peak, or it is not one"


def test_still_climbing_is_not_reported_as_a_collapse():
    """NEGATIVE CONTROL. The consumer box never collapsed within K<=12. Reporting a phantom
    collapse would cap every rig at whatever K the sweep happened to stop at."""
    best, collapsed = pick_optimal(_points(CONSUMER))
    assert collapsed is None, f"no collapse was measured, but one was reported at K={collapsed}"
    assert best == 12, f"expected the top of the swept range, got {best}"


def test_the_two_machines_disagree_which_is_the_entire_point():
    """One constant cannot serve both. If these ever agree, the fixture is wrong."""
    radeon_k, _ = pick_optimal(_points(RADEON))
    consumer_k, _ = pick_optimal(_points(CONSUMER))
    assert radeon_k != consumer_k
    assert radeon_k > consumer_k, "the datacentre GPU should sustain more concurrency"


def test_uncalibrated_rig_is_told_it_is_uncalibrated(tmp_path, monkeypatch):
    """Never a silent guess -- the same doctrine determinex_oracle enforces for a missing
    oracle. A run at the fallback K must be distinguishable from a measured one."""
    import determinex_calibrate as dc

    monkeypatch.setattr(dc, "PROFILE_PATH", tmp_path / "none.json")
    k, provenance = optimal_k("ollama", "no-such-model")
    assert k == UNCALIBRATED_K
    assert "UNCALIBRATED" in provenance
    assert "determinex_calibrate" in provenance, "must name the command that fixes it"


def test_calibrated_rig_reports_its_provenance(tmp_path, monkeypatch):
    import determinex_calibrate as dc

    prof = tmp_path / "cal.json"
    monkeypatch.setattr(dc, "PROFILE_PATH", prof)
    cal = Calibration(
        backend="vllm", model="m", host=host_fingerprint(), optimal_k=48,
        cand_per_s=3.523, collapsed_at=64, declared_hint=61, points=[],
        measured_at="2026-08-02T00:00:00",
    )
    dc.save_calibration(cal)
    k, provenance = optimal_k("vllm", "m")
    assert k == 48
    assert provenance.startswith("calibrated")


def test_profile_carries_no_personal_data():
    """The profile can travel with an opted-in corpus share, so the machine key must not
    identify a person or a filesystem."""
    fp = host_fingerprint()
    assert "ryang" not in fp.lower()
    assert ":" not in fp and "\\" not in fp and "/" not in fp


def test_sweep_warms_before_measuring():
    """Without a warm-up the first K pays the model load and reports a number that is not
    the machine's -- that mistake produced a flatly wrong conclusion on the first attempt."""
    calls = {"n": 0}

    def gen() -> int:
        calls["n"] += 1
        return 10

    sweep(gen, ks=[1], repeats=1, warmup=2)
    assert calls["n"] == 3, f"expected 2 warm-up + 1 measured call, got {calls['n']}"


def test_env_override_beats_calibration(monkeypatch):
    """The operator always wins. Calibration is advice, not a cage."""
    sys.path.insert(0, str(_SCRIPTS / "hive"))
    from hive.amplifier_bridge import env_k

    monkeypatch.setenv("DETERMINEX_AMPLIFY_K", "3")
    assert env_k(default=6, backend="vllm", model="m") == 3


@pytest.mark.parametrize("bad", ["", "abc", "-1"])
def test_bad_env_value_does_not_crash_a_build(monkeypatch, bad):
    from hive.amplifier_bridge import env_k

    monkeypatch.setenv("DETERMINEX_AMPLIFY_K", bad)
    assert env_k(default=6) >= 1


def test_vllm_hint_arithmetic_matches_the_declared_limit():
    """31504 blocks * 16 tokens / 8192 = 61, and the server's boot log said 61.83x. The hint
    is only a sweep bound, but it should agree with the hardware that produced it."""
    blocks, block_size, max_len = 31504, 16, 8192
    assert (blocks * block_size) // max_len == 61
    collapsed = pick_optimal(_points(RADEON))[1]
    assert collapsed > 61, "the measured collapse should sit just past the declared ceiling"
