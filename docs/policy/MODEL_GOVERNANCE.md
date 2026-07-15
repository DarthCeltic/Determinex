# Model Governance

Every model used by Determinex must have:

- model name and version
- source location
- role assignment
- training corpus snapshot
- evaluation results
- known limitations
- safety controls active at inference
- release or deployment status

Local-first models should remain the default for private code. Cloud models may
only see Cloaked or explicitly approved payloads.
