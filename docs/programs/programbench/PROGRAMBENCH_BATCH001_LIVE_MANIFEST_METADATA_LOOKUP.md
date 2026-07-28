# ProgramBench Batch001 Live Manifest Metadata Lookup

`PROGRAMBENCH_BATCH001_LIVE_MANIFEST_METADATA_LOOKUP_LOCK_001` used the safe registry client against the ten derived Batch001 `EASY_METADATA_ONLY` targets.

The lookup used only exact image references and tag `task_cleanroom`. It did not pull images, fetch layers, import artifacts, run Docker, or run ProgramBench.

Result: all ten DockerHub manifests were found and returned immutable `sha256:` digests. These digests remain metadata-only evidence.
