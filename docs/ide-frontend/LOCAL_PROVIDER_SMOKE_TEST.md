# Local Provider Smoke Test

> Locked under `locks/sentinel/LOCAL_PROVIDER_SMOKE_TEST_LOCK_001.json`.

Bounded availability check for a configured local provider. Composes
the compat harness with a `LocalModelConfigRecord` and a fixture
`FixtureProvider`. Output is always captured as `output_trusted=False`.
