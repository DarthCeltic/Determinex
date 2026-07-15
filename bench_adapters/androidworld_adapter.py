"""
AndroidWorld adapter — converts mobile GUI tasks to VisualTaskSpec.
Requires emulator isolation (DETERMINEX_REQUIRE_EMULATOR=1).
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

BENCHMARK_NAME = "androidworld"


def load_task(task: dict[str, Any]) -> VisualTaskSpec:
    return VisualTaskSpec(
        task_id=str(task.get("task_id", "unknown")),
        env_type=EnvType.MOBILE,
        goal=task.get("task", ""),
        constraints=[
            f"app={task.get('app_name', '')}",
            f"category={task.get('category', '')}",
        ],
        source_benchmark=BENCHMARK_NAME,
        max_steps=int(task.get("max_steps", 20)),
        timeout_seconds=int(task.get("time_limit", 300)),
        metadata={
            "task_id": task.get("task_id"),
            "app_name": task.get("app_name", ""),
            "category": task.get("category", ""),
            "params": task.get("params", {}),
            "verifier": task.get("verifier", {}),
            "sandbox_active": False,  # set to True after emulator confirms running
        },
    )


def load_observation(
    serial: str,
    screenshot_path: str,
    step: int,
) -> AgentObservation:
    from vision.screenshot_loader import screenshot_hash
    from mobile.uiautomator_reader import dump_ui_xml
    import hashlib
    xml = dump_ui_xml(serial)
    xml_hash = hashlib.sha256(xml.encode()).hexdigest() if xml else ""
    return AgentObservation(
        env_type=EnvType.MOBILE,
        step=step,
        screenshot_path=screenshot_path,
        screenshot_hash=screenshot_hash(screenshot_path),
        accessibility_tree=xml[:8192] if xml else None,
        accessibility_hash=xml_hash,
        metadata={"serial": serial},
    )


def score_verdict(
    task: dict[str, Any],
    serial: str,
    screenshot_after: str,
) -> OracleVerdict:
    verifier = task.get("verifier", {})
    verifier_type = verifier.get("type", "ui_element")

    try:
        if verifier_type == "ui_element":
            text = verifier.get("text", "")
            from mobile.mobile_verifier import ui_text_exists
            return ui_text_exists(serial, text)

        if verifier_type == "activity":
            activity = verifier.get("activity", "")
            from mobile.mobile_verifier import activity_matches
            return activity_matches(serial, activity)

        if verifier_type == "screenshot_match":
            reference = verifier.get("reference_screenshot", "")
            from mobile.mobile_verifier import screenshot_region_matches
            return screenshot_region_matches(reference, screenshot_after)

        if verifier_type == "file_exists":
            path = verifier.get("path", "")
            from mobile.mobile_verifier import file_exists_on_device
            return file_exists_on_device(serial, path)

        if verifier_type == "package_opened":
            package = verifier.get("package", task.get("app_name", ""))
            from mobile.mobile_verifier import package_opened
            return package_opened(serial, package)

        return OracleVerdict(oracle_type=OracleType.MOBILE, passed=False, score=0.0,
                             evidence=f"unknown verifier_type: {verifier_type}")
    except Exception as exc:
        return OracleVerdict(oracle_type=OracleType.MOBILE, passed=False, score=0.0, evidence=str(exc))
