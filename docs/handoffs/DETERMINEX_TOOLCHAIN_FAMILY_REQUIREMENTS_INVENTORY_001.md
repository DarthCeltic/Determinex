# DETERMINEX_TOOLCHAIN_FAMILY_REQUIREMENTS_INVENTORY_001

- Known-world rows scanned: `383`.
- Requirements identified: `9`.
- Release cells/families: `13 / 0`.

## Groups

- `already_available`: `2` requirement(s): python_local_proof_runtime, node_npm_runtime.
- `packet_needed`: `1` requirement(s): governed_authority_packet.
- `requires_external_provider_network`: `1` requirement(s): programbench_eval_harness.
- `requires_heavy_sdk_manual_install`: `1` requirement(s): installer_clean_host_signing.
- `requires_operator_legal_review`: `1` requirement(s): security_review_sbom_tooling.
- `safe_to_acquire_overnight`: `2` requirement(s): local_verifier_portfolio, docker_runtime.
- `should_remain_blocked`: `1` requirement(s): monolithic_status_runtime.

## Requirements

- `python_local_proof_runtime`: `.venv Python runtime` rows `99` packet `already_available` blocker `PYTHON_RUNTIME_REQUIRED`.
- `local_verifier_portfolio`: `local verifier fixture portfolio` rows `66` packet `packet_needed` blocker `LOCAL_VERIFIER_REQUIRED`.
- `programbench_eval_harness`: `ProgramBench eval harness` rows `200` packet `packet_needed` blocker `PROGRAMBENCH_EVAL_REQUIRED`.
- `docker_runtime`: `Docker local runtime` rows `200` packet `already_available` blocker `DOCKER_RUNTIME_REQUIRED`.
- `node_npm_runtime`: `Node/npm verifier runtime` rows `165` packet `already_available` blocker `NODE_NPM_RUNTIME_REQUIRED`.
- `security_review_sbom_tooling`: `SBOM/security review tooling` rows `11` packet `packet_needed` blocker `SECURITY_REVIEW_REQUIRED`.
- `monolithic_status_runtime`: `monolithic status runtime repair` rows `1` packet `packet_needed` blocker `MONOLITHIC_STATUS_RUNTIME_UNRESOLVED`.
- `installer_clean_host_signing`: `installer clean-host/signing matrix` rows `3` packet `packet_needed` blocker `INSTALL_LAUNCH_UNINSTALL_SIGNING_CLEAN_HOST_GATES_REQUIRED`.
- `governed_authority_packet`: `governed authority packet` rows `2` packet `packet_needed` blocker `AUTHORITY_PACKET_REQUIRED`.

No blind acquisition or support-from-tool-presence claim is made.
