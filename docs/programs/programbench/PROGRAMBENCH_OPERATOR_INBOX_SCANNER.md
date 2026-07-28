# ProgramBench Operator Inbox Scanner

`PROGRAMBENCH_OPERATOR_INBOX_SCANNER_LOCK_001` scans `assurance/operator_inbox/programbench/` for local JSON packets and validates them.

The scanner handles a missing inbox as empty, rejects parse errors, never mutates packet files, and never approves execution or training eligibility.
