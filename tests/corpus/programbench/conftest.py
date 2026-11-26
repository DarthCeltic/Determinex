"""Build a small offline Batch001 workspace when testing the filtered public distribution."""

import json
import shutil
from pathlib import Path

import pytest

from corpus.programbench import batch001_import_scan_pipeline as imports
from corpus.programbench import batch001_metadata_campaign as metadata
from corpus.programbench import batch001_unblock_priority as priority
from corpus.programbench import operator_ready_platform as operator
from corpus.programbench import programbench_campaign_platform as platform
from corpus.programbench import programbench_next_unblock_decision as unblock
from tests.conftest import missing_private_evidence
from tests.corpus.programbench.public_doxygen_inputs import build_doxygen_history


@pytest.fixture(scope="session")
def public_batch_inputs(tmp_path_factory):
    if not missing_private_evidence():
        return None

    root = tmp_path_factory.mktemp("public-batch001")
    # One real identifier used by the name-conversion regression, plus nine dummy cases.
    targets = ["ammarabouzor__tui-journal.2b4540d"] + [
        f"example__tool-{i}.1234567" for i in range(1, 10)
    ]

    def save(path, record):
        dest = root / path
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(json.dumps(record), encoding="utf-8")

    save(platform.MISSING_IMAGE_INVENTORY, {"items": [{"tool": name} for name in targets]})
    with pytest.MonkeyPatch.context() as env:
        # All records go beneath the temporary test tree, including generated outbox templates.
        env.setenv("DETERMINEX_PROGRAMBENCH_EVIDENCE_WRITE_ROOT", str(root / "assurance/evidence"))
        env.setenv(
            "DETERMINEX_PROGRAMBENCH_OPERATOR_OUTBOX_WRITE_ROOT",
            str(root / "assurance/operator_outbox/programbench"),
        )
        build_doxygen_history(root, Path(__file__).resolve().parents[3])
        campaign = platform.ProgramBenchCampaignPlatform(platform.PlatformConfig(root=root))
        campaign.run_all()
        operator.ProgramBenchOperatorReadyPlatform(
            operator.OperatorReadyConfig(root=root)
        ).run_all()
        save(unblock.PER_TARGET_GRAPH_REF, {"batch001_targets": [{"instance_id": targets[0]}]})
        save(unblock.LEDGER_REF, {"chain_valid": True, "mutation_detected": False})
        save(unblock.COUNT_GUARD_REF, {"status": "EVIDENCE_COUNT_DRIFT_GUARD_PASSED"})
        priority.ProgramBenchBatch001UnblockPriority(priority.PriorityConfig(root=root)).build()
        steps = metadata.ProgramBenchBatch001MetadataCampaign(
            metadata.Batch001MetadataCampaignConfig(root=root)
        ).run_all()
        admissions = [
            {
                "instance_id": plan["instance_id"],
                "image_name": plan["image_name"],
                "digest": f"sha256:{i:064x}",
                "status": "BATCH001_METADATA_DIGEST_ADMITTED",
            }
            for i, plan in enumerate(steps["plan"]["plans"], start=1)
        ]
        save(imports.DIGEST_ADMISSION_RECORD, {"admissions": admissions})
        imports.ProgramBenchBatch001ImportScanPipeline(
            imports.Batch001ImportScanConfig(root=root)
        ).run_all()
    return root


@pytest.fixture
def public_batch_workspace(public_batch_inputs, tmp_path, monkeypatch):
    if public_batch_inputs is None:
        return

    root = tmp_path / "batch"
    shutil.copytree(public_batch_inputs, root)
    monkeypatch.chdir(root)
    monkeypatch.setenv(
        "DETERMINEX_PROGRAMBENCH_OPERATOR_OUTBOX_WRITE_ROOT",
        str(root / "assurance/operator_outbox/programbench"),
    )
    monkeypatch.setenv(
        "DETERMINEX_PROGRAMBENCH_EVIDENCE_WRITE_ROOT", str(root / "assurance/evidence")
    )
    return root
