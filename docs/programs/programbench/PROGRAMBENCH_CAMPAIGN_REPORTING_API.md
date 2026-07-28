# ProgramBench Campaign Reporting API

`PROGRAMBENCH_CAMPAIGN_REPORTING_API_LOCK_001` provides a read-only deterministic JSON report for ProgramBench campaign state.

The CLI entrypoint is:

```powershell
.\.venv\Scripts\python.exe scripts\corpus\programbench\programbench_campaign_report.py --json
```

The report includes batch summary, instance summaries, skip reasons, operator actions, training eligibility summary, rerun readiness summary, and evidence references.

It is read-only and does not run Docker, ProgramBench, scanners, rebuilds, remediation, or training-row generation.
