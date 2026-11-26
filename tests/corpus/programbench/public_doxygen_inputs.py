"""Offline inputs for exercising the public ProgramBench pipeline without archived run files."""

import json
import shutil
from pathlib import Path

from corpus.programbench.alternate_cleanroom_image_provenance_record import (
    make_alternate_cleanroom_image_provenance_record,
)
from corpus.programbench.cleanroom_image_hydration_record import (
    make_cleanroom_image_hydration_record,
)
from corpus.programbench.cleanroom_image_scan_record import make_cleanroom_image_scan_record
from corpus.programbench.cleanroom_image_scan_triage_record import (
    make_cleanroom_image_scan_triage_record,
)
from corpus.programbench.dockerhub_manifest_provenance_record import (
    make_dockerhub_manifest_provenance_record,
)
from corpus.programbench.operator_provenance_request_packet_record import (
    make_operator_provenance_request_packet_record,
)
from corpus.programbench.rebuild_provenance_quarantine_decision_record import (
    make_rebuild_provenance_quarantine_decision_record,
)

from corpus.programbench import codex_completion_campaign as campaign
from corpus.programbench import official_artifact_security_decision as security
from corpus.programbench import upstream_artifact_authority_recheck as authority


def build_doxygen_history(root, source):
    """Use signed synthetic input records, then run the actual authority and policy stages."""
    image = campaign.IMAGE
    digest = campaign.DIGEST
    registry = Path("locks/sentinel/PROGRAMBENCH_ONLINE_PROVIDER_REGISTRY_LOCK_001.json")
    probe = Path("scripts/determinex_programbench_probe.py")
    for rel in (registry, probe):
        (root / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source / rel, root / rel)

    def save(path, record):
        dest = root / path
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(json.dumps(record), encoding="utf-8")

    save(
        campaign.MANIFEST,
        make_dockerhub_manifest_provenance_record(
            status="EXACT_REMOTE_MANIFEST_FOUND",
            triage_record="fixture",
            image_reference=image,
            registry="docker.io",
            repository=image.split(":")[0],
            tag="task_cleanroom",
            manifest_digest=digest,
            target={"fixture": True},
        ),
    )
    save(
        campaign.REBUILD_DECISION,
        make_rebuild_provenance_quarantine_decision_record(
            status="REBUILD_QUARANTINE_DECISION_PARTIAL_ONLY",
            decision="partial",
            image_reference=image,
            image_digest=digest,
            recipe_provenance_recovery="fixture",
            authorization={"image_rebuild_authorized": False},
        ),
    )
    save(
        campaign.OPERATOR_REQUEST,
        make_operator_provenance_request_packet_record(
            status="OPERATOR_PROVENANCE_REQUEST_PACKET_WRITTEN",
            current_decision="partial",
            image_reference=image,
            image_digest=digest,
            rebuild_quarantine_decision=str(campaign.REBUILD_DECISION),
        ),
    )
    save(
        campaign.SCAN,
        make_cleanroom_image_scan_record(
            status="CLEANROOM_IMAGE_SCAN_FAILED",
            import_record="fixture",
            artifact_path="fixture",
            image_reference=image,
            expected_digest=digest,
            observed_digest=digest,
            file_sha256="0" * 64,
            file_size=0,
            scanner="offline fixture",
            scanner_version="1",
            findings_summary={"critical": 1, "high": 2, "medium": 3, "low": 4, "total": 10},
        ),
    )
    save(
        campaign.HYDRATION,
        make_cleanroom_image_hydration_record(
            status="CLEANROOM_IMAGE_SCAN_FAILED",
            admission_record="fixture",
            image_reference=image,
            source_url_or_registry="fixture",
            expected_digest=digest,
            observed_digest=digest,
            target={"fixture": True},
            policy_result="CLEANROOM_IMAGE_POLICY_BLOCKED",
        ),
    )
    save(
        campaign.TRIAGE,
        make_cleanroom_image_scan_triage_record(
            status="CLEANROOM_IMAGE_SCAN_TRIAGED",
            recommendation="hold",
            image_reference=image,
            artifact_path="fixture",
            expected_digest=digest,
            observed_digest=digest,
            file_sha256="0" * 64,
            scan_record=str(campaign.SCAN),
            hydration_record=str(campaign.HYDRATION),
            category_summary={"dominant_category": "language_runtime"},
        ),
    )
    save(
        campaign.ALTERNATE,
        make_alternate_cleanroom_image_provenance_record(
            status="ALTERNATE_CLEANROOM_PROVENANCE_NOT_FOUND",
            decision="none",
            original_image_reference=image,
            original_image_digest=digest,
            operator_provenance_request=str(campaign.OPERATOR_REQUEST),
        ),
    )
    save(campaign.ROOT_CAUSE, {"rerun_scope": {"tool": campaign.INSTANCE_ID, "max_attempts": 1}})
    recheck = authority.ProgramBenchUpstreamArtifactAuthorityRecheck(
        authority.UpstreamArtifactAuthorityRecheckConfig(root=root)
    )
    recheck.recheck(
        manifest_record_path=campaign.MANIFEST,
        operator_request_path=campaign.OPERATOR_REQUEST,
        rebuild_decision_path=campaign.REBUILD_DECISION,
        scan_record_path=campaign.SCAN,
        hydration_record_path=campaign.HYDRATION,
        alternate_record_path=campaign.ALTERNATE,
        provider_registry_lock_path=registry,
        triage_record_path=campaign.TRIAGE,
    )
    security.ProgramBenchOfficialArtifactSecurityDecision(
        security.OfficialArtifactSecurityDecisionConfig(root=root)
    ).decide(campaign.UPSTREAM_RECHECK)
    campaign.ProgramBenchCodexCompletionCampaign(campaign.CampaignConfig(root=root)).run_all()
