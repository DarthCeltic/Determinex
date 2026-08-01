# Family: node_cli  [STUB]

> Status: STUB — no sprint-1/2 exemplars yet. Fill in after first node_cli tool is processed.

## Likely conventions (verify with probes)

- Tools likely use `argparse` (python) / `commander` or `yargs` (node)
- Argparse errors → rc=2; runtime → rc=1
- Help format: typically begins with `usage:` line

## Generator pseudocode

```python
def generate(instance_id, probe):
    # 1. Detect arg-parsing library from probe wordings
    # 2. argparse: "usage:", "error: argument", rc=2
    # 3. commander: "Usage:", "error: unknown option", rc=1
```

## Exemplar tools

None yet — TODO after first tool of this family is sprinted.
