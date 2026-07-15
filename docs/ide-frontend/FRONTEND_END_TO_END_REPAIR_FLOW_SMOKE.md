# Frontend End-to-End Repair Flow Smoke

> Locked under `locks/sentinel/FRONTEND_END_TO_END_REPAIR_FLOW_SMOKE_LOCK_001.json`.

In-process smoke trace that walks the visible repair flow through the
production Tauri dispatcher (`scripts/ide/_tauri_driver._dispatch`) —
the same function the Rust bridge shells out to. Ten stages, one per
visible-panel command, in display order: workspace status, model route,
diagnose (dry-run + live opt-in), patch plan, temp verify, human approval
packet, source apply (dry-run, no real mutation), and repair flow state.

Every stage's response carries `source_mutation_authorized=false` and
`training_eligible=false`. The trace's `live_model_called` and
`network_called` are both `false`. No subprocess is spawned. No socket
is opened. The trace serializes to deterministic JSON.
