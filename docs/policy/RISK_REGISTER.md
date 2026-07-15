# Risk Register

Machine-readable risk rows live in:

```text
assurance/risks/risk_register.json
```

Current high-priority risk families:

- ProgramBench drain underutilization
- stale shard confusion
- unclassified failed gates
- missing native-language validator coverage
- unlicensed source entering corpus
- secret-bearing source entering corpus
- broad stderr/stdout filters regressing passing tests
- native-source wrapper debt
- Docker/local resource exhaustion
- unpinned dependency or container image claims

Each risk should have an owner, mitigation, test/evidence path, and residual
risk rating before it is marked controlled.
