# DETERMINEX_GOVERNED_ACQUISITION_PACKET_SYSTEM_LOCK_001_REPORT

- Status: `GOVERNED_ACQUISITION_PACKET_SYSTEM_PASSED`.
- Admitted packets: `1`.
- Packet-ready is not acquired; acquired is not support.

## Fixture Matrix

- `missing_source_invalid`: valid `False`, packet_ready `False`, admitted `False`, errors `missing_source`.
- `missing_verify_command_invalid`: valid `False`, packet_ready `False`, admitted `False`, errors `missing_verify_command`.
- `missing_rollback_command_invalid`: valid `False`, packet_ready `False`, admitted `False`, errors `missing_rollback_command`.
- `admitted_without_transcript_invalid`: valid `False`, packet_ready `True`, admitted `False`, errors `admitted_without_verification_transcript`.
- `unlock_without_admission_invalid`: valid `False`, packet_ready `True`, admitted `False`, errors `rows_unlocked_without_admission`.
- `failed_acquisition_records_blocker`: valid `True`, packet_ready `True`, admitted `False`, errors `none`.
- `packet_ready_distinct_from_admitted`: valid `True`, packet_ready `True`, admitted `False`, errors `none`.
- `tool_presence_not_support`: valid `False`, packet_ready `True`, admitted `False`, errors `tool_presence_cannot_claim_support`.

No random upgrades, unbounded global installs, support-from-tool-presence, training-row export, or public go claim is made.
