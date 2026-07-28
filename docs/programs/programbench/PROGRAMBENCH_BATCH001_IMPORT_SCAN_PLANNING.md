# ProgramBench Batch001 Import Scan Planning

`PROGRAMBENCH_BATCH001_IMPORT_SCAN_PLANNING_LOCK_001` writes the next non-executing plan for targets with metadata-only digest admission.

For each admitted target, the plan requires:

- artifact import provenance
- expected artifact tar path
- approved scanner evidence
- scan before hydration or execution
- security decision after scan
- policy admission if scan fails

No import, scan, Docker execution, or ProgramBench rerun is authorized by this plan.
