"""
SWE-bench Multimodal adapter — converts 517 JS/visual instances to VisualTaskSpec.
Handles screenshot evidence, DOM snapshots, and visual oracle verification.
"""

from __future__ import annotations

import logging
from typing import Any

from agents.base_agent import (
    AgentObservation,
    EnvType,
    OracleType,
    OracleVerdict,
    VisualTaskSpec,
)

log = logging.getLogger(__name__)

BENCHMARK_NAME = "swebench_multimodal"


def load_instance(instance: dict[str, Any]) -> VisualTaskSpec:
    """Convert a SWE-bench Multimodal instance dict to VisualTaskSpec."""
    return VisualTaskSpec(
        task_id=instance.get("instance_id", "unknown"),
        env_type=EnvType.BROWSER,
        goal=instance.get("problem_statement", ""),
        constraints=[
            f"repo={instance.get('repo', '')}",
            f"base_commit={instance.get('base_commit', '')}",
        ],
        source_benchmark=BENCHMARK_NAME,
        max_steps=40,
        timeout_seconds=600,
        metadata={
            "repo": instance.get("repo", ""),
            "base_commit": instance.get("base_commit", ""),
            "patch": instance.get("patch", ""),
            "test_patch": instance.get("test_patch", ""),
            "screenshots": instance.get("screenshots", []),
            "dom_snapshots": instance.get("dom_snapshots", []),
        },
    )


def load_observation_from_screenshot(
    screenshot_path: str,
    instance: dict[str, Any],
    step: int = 0,
) -> AgentObservation:
    from vision.screenshot_loader import screenshot_hash

    return AgentObservation(
        env_type=EnvType.BROWSER,
        step=step,
        screenshot_path=screenshot_path,
        screenshot_hash=screenshot_hash(screenshot_path),
        url=instance.get("url", ""),
        metadata={"instance_id": instance.get("instance_id", "")},
    )


def score_verdict(
    instance: dict[str, Any],
    patch_applied: bool,
    test_passed: bool,
    visual_match_score: float = 0.0,
) -> OracleVerdict:
    """Composite oracle verdict for SWE-bench Multimodal."""
    passed = patch_applied and test_passed
    score = 0.0
    if patch_applied:
        score += 0.4
    if test_passed:
        score += 0.4
    score += visual_match_score * 0.2

    return OracleVerdict(
        oracle_type=OracleType.TEST,
        passed=passed,
        score=round(score, 3),
        evidence=f"patch_applied={patch_applied} test_passed={test_passed} visual={visual_match_score:.3f}",
        metadata={"instance_id": instance.get("instance_id", "")},
    )


def to_corpus_record(
    spec: VisualTaskSpec,
    verdict: OracleVerdict,
    patch: str,
) -> dict[str, Any]:
    """Build the payload dict for CorpusManager.write_code_verdict()."""
    return {
        "lang": "javascript",
        "spec_text": spec.goal,
        "patch": patch,
        "compile_result": "pass" if verdict.passed else "fail",
        "compile_errors": [],
        "test_result": "pass" if verdict.passed else "fail",
        "test_errors": [],
        "attempt": 1,
        "model_builder": "unknown",
    }
