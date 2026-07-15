# Determinex Threat Model

## Assets

- source code and repository history
- user files and screenshots
- secrets, API keys, credentials
- corpus records and model weights
- benchmark fixtures and hidden-test outputs
- lock manifests and assurance evidence
- cloud-bound prompts and model responses

## Trust Boundaries

- user input
- benchmark task input
- local model output
- cloud model output
- browser, desktop, and mobile surfaces
- corpus writer
- verifier commands
- training pipeline
- remote eval workers

## Attacker Classes

- malicious prompt or benchmark task
- poisoned repository README, test, issue, or fixture
- compromised dependency or container image
- malicious corpus contributor
- webpage or screenshot prompt injection
- cloud-provider leakage risk
- local host malware

## Threat Categories

- prompt injection
- sensitive data exfiltration
- unsafe action execution
- model or corpus poisoning
- supply-chain compromise
- sandbox escape
- policy bypass
- provenance loss

## Control Rule

Every threat must map to at least one control, one test, and one evidence
artifact. Missing evidence means the threat is open.
