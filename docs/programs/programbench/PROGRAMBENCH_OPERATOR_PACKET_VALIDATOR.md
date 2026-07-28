# ProgramBench Operator Packet Validator

`PROGRAMBENCH_OPERATOR_PACKET_VALIDATOR_LOCK_001` validates local operator packets without granting execution.

The validator checks schema version, packet type, exact scope, digest binding, references, hashes, timestamp, staleness, operator identity, signature, fixture status, and overbroad authority.

Fixture packets can be accepted only in fixture mode. A validated packet still must be routed to the correct non-executing admission gate.
