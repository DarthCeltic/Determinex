# ProgramBench Operator CLI

`PROGRAMBENCH_OPERATOR_CLI_LOCK_001` adds a read-only operator-facing CLI.

Examples:

```powershell
.\.venv\Scripts\python.exe scripts\corpus\programbench\programbench_operator_cli.py status --json
.\.venv\Scripts\python.exe scripts\corpus\programbench\programbench_operator_cli.py actions --json
.\.venv\Scripts\python.exe scripts\corpus\programbench\programbench_operator_cli.py packets --out assurance/operator_outbox/programbench
.\.venv\Scripts\python.exe scripts\corpus\programbench\programbench_operator_cli.py inbox-scan --json
.\.venv\Scripts\python.exe scripts\corpus\programbench\programbench_operator_cli.py simulate-unblock --json
.\.venv\Scripts\python.exe scripts\corpus\programbench\programbench_operator_cli.py evidence-graph --json
```

Only `packets` writes files, and it writes templates only.
