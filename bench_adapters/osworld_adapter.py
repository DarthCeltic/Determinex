"""
OSWorld-Verified adapter — converts desktop GUI tasks to VisualTaskSpec.
Requires VM isolation (DETERMINEX_REQUIRE_VM=1).
"""
from __future__ import annotations

import logging
from typing import Any

from agents.base_agent import (
    AgentObservation,
    EnvType,
    OracleVerdict,
    OracleType,
    VisualTaskSpec,
)

log = logging.getLogger(__name__)

BENCHMARK_NAME = "osworld"


def load_task(task: dict[str, Any]) -> VisualTaskSpec:
    return VisualTaskSpec(
        task_id=str(task.get("id", "unknown")),
        env_type=EnvType.DESKTOP,
        goal=task.get("instruction", ""),
        constraints=[
            f"app={task.get('app', '')}",
            f"os={task.get('os', 'ubuntu')}",
        ],
        source_benchmark=BENCHMARK_NAME,
        max_steps=int(task.get("max_steps", 20)),
        timeout_seconds=int(task.get("time_limit", 300)),
        metadata={
            "id": task.get("id"),
            "app": task.get("app", ""),
            "os": task.get("os", "ubuntu"),
            "init_state": task.get("init_state", {}),
            "evaluator": task.get("evaluator", {}),
            "sandbox_active": False,  # set to True after VM confirms running
        },
    )


def load_observation(
    screenshot_path: str,
    vm_id: str,
    step: int,
    window_title: str = "",
) -> AgentObservation:
    from vision.screenshot_loader import screenshot_hash
    return AgentObservation(
        env_type=EnvType.DESKTOP,
        step=step,
        screenshot_path=screenshot_path,
        screenshot_hash=screenshot_hash(screenshot_path),
        window_title=window_title,
        metadata={"vm_id": vm_id},
    )


def score_verdict(
    task: dict[str, Any],
    screen_controller: Any,
    screenshot_after: str,
) -> OracleVerdict:
    evaluator = task.get("evaluator", {})
    eval_type = evaluator.get("func", "screenshot_match")

    try:
        if eval_type == "screenshot_match":
            reference_screenshot = evaluator.get("reference_screenshot", "")
            if reference_screenshot:
                from desktop.desktop_verifier import visual_match
                return visual_match(reference_screenshot, screenshot_after)
            return OracleVerdict(
                oracle_type=OracleType.DESKTOP, passed=False, score=0.0,
                evidence="no reference screenshot provided",
            )

        if eval_type == "text_match":
            expected = evaluator.get("expected", "")
            from desktop.desktop_verifier import screenshot_contains_text
            return screenshot_contains_text(screenshot_after, expected)

        if eval_type == "file_exists":
            path = evaluator.get("path", "")
            from desktop.desktop_verifier import file_exists_in_vm
            return file_exists_in_vm(screen_controller, path)

        return OracleVerdict(oracle_type=OracleType.DESKTOP, passed=False, score=0.0,
                             evidence=f"unknown eval_type: {eval_type}")
    except Exception as exc:
        return OracleVerdict(oracle_type=OracleType.DESKTOP, passed=False, score=0.0, evidence=str(exc))
