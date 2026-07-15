"""
WebArena / VisualWebArena adapter — converts tasks to VisualTaskSpec and
maps observations/scoring to the internal contract.
"""
from __future__ import annotations

import logging
from typing import Any

from agents.base_agent import (
    AgentObservation,
    CorpusType,
    EnvType,
    OracleVerdict,
    OracleType,
    VisualTaskSpec,
)

log = logging.getLogger(__name__)

BENCHMARK_NAME = "webarena"
VISUAL_BENCHMARK_NAME = "visualwebarena"


def load_task(task: dict[str, Any], visual: bool = False) -> VisualTaskSpec:
    """Convert WebArena task dict to VisualTaskSpec."""
    benchmark = VISUAL_BENCHMARK_NAME if visual else BENCHMARK_NAME
    return VisualTaskSpec(
        task_id=str(task.get("task_id", "unknown")),
        env_type=EnvType.BROWSER,
        goal=task.get("intent", ""),
        constraints=[
            f"sites={','.join(task.get('sites', []))}",
            f"start_url={task.get('start_url', '')}",
        ],
        source_benchmark=benchmark,
        max_steps=int(task.get("max_steps", 30)),
        timeout_seconds=int(task.get("time_limit", 300)),
        metadata={
            "task_id": task.get("task_id"),
            "sites": task.get("sites", []),
            "start_url": task.get("start_url", ""),
            "eval": task.get("eval", {}),
            "reference_answers": task.get("reference_answers", {}),
            "image": task.get("image", None),         # VisualWebArena only
        },
    )


def load_observation(page: Any, step: int, screenshot_path: str = "") -> AgentObservation:
    from vision.screenshot_loader import screenshot_hash
    from browser.dom_reader import get_dom_snapshot, dom_hash, current_url
    html = get_dom_snapshot(page)
    url = current_url(page)
    h_hash = screenshot_hash(screenshot_path) if screenshot_path else ""
    d_hash = dom_hash(html)
    return AgentObservation(
        env_type=EnvType.BROWSER,
        step=step,
        screenshot_path=screenshot_path or None,
        screenshot_hash=h_hash or None,
        dom_snapshot=html[:8192],
        dom_hash=d_hash,
        url=url,
    )


def score_verdict(task: dict[str, Any], page: Any, final_answer: str = "") -> OracleVerdict:
    """
    Evaluate task completion using WebArena's eval config.
    Supports: string_match, url_match, element_match, program_html.
    """
    eval_cfg = task.get("eval", {})
    eval_type = eval_cfg.get("eval_types", ["string_match"])[0]

    try:
        if eval_type == "string_match":
            expected = eval_cfg.get("reference_answers", {}).get("must_include", [])
            passed = all(e.lower() in final_answer.lower() for e in expected)
            return OracleVerdict(
                oracle_type=OracleType.BROWSER,
                passed=passed,
                score=1.0 if passed else 0.0,
                evidence=f"string_match expected={expected} final={final_answer[:100]}",
            )

        if eval_type == "url_match":
            from browser.dom_reader import current_url
            from browser.browser_verifier import url_matches
            expected_url = eval_cfg.get("reference_url", "")
            return url_matches(page, expected_url)

        if eval_type == "program_html":
            # Custom evaluator — run the eval program
            return OracleVerdict(
                oracle_type=OracleType.BROWSER,
                passed=False,
                score=0.0,
                evidence="program_html eval not yet implemented",
            )

        return OracleVerdict(oracle_type=OracleType.BROWSER, passed=False, score=0.0,
                             evidence=f"unknown eval_type: {eval_type}")
    except Exception as exc:
        return OracleVerdict(oracle_type=OracleType.BROWSER, passed=False, score=0.0, evidence=str(exc))
